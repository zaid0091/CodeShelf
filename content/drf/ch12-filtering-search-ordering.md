---
title: Chapter 12 — Filtering, Searching & Ordering
description: django-filter, SearchFilter, OrderingFilter, and combining query backends
order: 12
tags: [drf, filtering, search, ordering]
---

# Chapter 12: Filtering, Searching & Ordering

List endpoints often need query parameters to narrow, search, and sort results. DRF delegates this to **filter backends** that modify the queryset before pagination.

## Definitions

| Term | Meaning |
|------|---------|
| **Filter backend** | Class that applies query params to a queryset (`filter_queryset`). |
| **django-filter** | Third-party library for declarative field filters (`FilterSet`). |
| **SearchFilter** | DRF backend for `?search=` across multiple fields. |
| **OrderingFilter** | DRF backend for `?ordering=field` sort control. |

---

## 12.1 Introduction

Filter backends run in order. Configure globally or per view:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}
```

```python
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'in_stock']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']  # default ordering
```

```bash
pip install django-filter
```

```python
# settings.py — INSTALLED_APPS
INSTALLED_APPS = [
    ...
    'django_filters',
]
```

### Interview points

- Filtering happens **before** pagination — you filter the full queryset, then paginate.
- Multiple backends **stack** — all applicable params apply together.
- Without `django-filter`, use `filterset_fields` only with `DjangoFilterBackend`.

---

## 12.2 Filtering with DjangoFilterBackend

### Simple field filters

```python
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'brand', 'in_stock']
```

```bash
curl "http://127.0.0.1:8000/api/products/?category=electronics&in_stock=true"
```

### FilterSet class (recommended)

```python
# filters.py
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    created_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')

    class Meta:
        model = Product
        fields = ['category', 'brand', 'in_stock']
```

```python
# views.py
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
```

```bash
curl "http://127.0.0.1:8000/api/products/?min_price=10&max_price=100&name=phone"
```

### Related and custom filters

```python
class OrderFilter(django_filters.FilterSet):
    customer_name = django_filters.CharFilter(
        field_name='customer__username',
        lookup_expr='icontains'
    )
    status = django_filters.ChoiceFilter(choices=Order.STATUS_CHOICES)

    class Meta:
        model = Order
        fields = ['status', 'created_at']
```

### Interview points

- `filterset_fields` is shorthand; **FilterSet** supports ranges, choices, and related lookups.
- Lookup expressions: `exact`, `icontains`, `gte`, `in`, etc. (same as Django ORM).
- Invalid filter values typically return **empty queryset** or validation errors depending on setup.

---

## 12.3 SearchFilter

Provides a single `search` query param that ORs across `search_fields`.

```python
from rest_framework.filters import SearchFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description', 'brand__name']
```

```bash
curl "http://127.0.0.1:8000/api/products/?search=laptop"
```

### Lookup prefixes on search fields

| Prefix | Lookup | Example field |
|--------|--------|---------------|
| (none) | `icontains` | `'name'` |
| `^` | `istartswith` | `'^name'` |
| `=` | `iexact` | `'=sku'` |
| `@` | `search` (PostgreSQL full-text) | `'@description'` |
| `$` | `iregex` | `'$name'` |

```python
search_fields = ['^name', '=sku', 'description']
```

### Custom search behavior

```python
class ProductViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', '')
        if search:
            queryset = queryset.filter(
                models.Q(name__icontains=search) |
                models.Q(tags__name__icontains=search)
            ).distinct()
        return queryset
```

### Interview points

- **One search box** → multiple columns (OR logic).
- For complex search, use **django-filter**, **PostgreSQL full-text**, or **Elasticsearch**.
- `search` is separate from field-specific filters — they can be combined.

---

## 12.4 OrderingFilter

Allows clients to sort via `?ordering=field` or `?ordering=-field` (descending).

```python
from rest_framework.filters import OrderingFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['price', 'name', 'created_at']
    ordering = ['-created_at']  # default when no ?ordering=
```

```bash
curl "http://127.0.0.1:8000/api/products/?ordering=price"
curl "http://127.0.0.1:8000/api/products/?ordering=-price,name"
```

### Restrict ordering for security

Only list fields in `ordering_fields` — never expose `ordering_fields = '__all__'` on public APIs without care (SQL injection via ORM is mitigated but DoS via expensive sorts is real).

```python
ordering_fields = ['price', 'created_at']  # whitelist
```

### Interview points

- Prefix `-` means **descending**.
- Multiple fields: `?ordering=-price,name`.
- Default `ordering` applies when the client sends no param.

---

## 12.5 Combining Filters

Stack backends and test combined query strings.

```python
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at', 'name']
    ordering = ['-created_at']
```

```bash
curl "http://127.0.0.1:8000/api/products/?category=electronics&search=pro&ordering=-price&page=1"
```

### Order of execution

1. View's `get_queryset()`
2. Each filter backend's `filter_queryset(request, queryset, view)`
3. Pagination
4. Serialization

### GenericAPIView hooks

```python
class ProductViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        qs = Product.objects.filter(is_active=True)
        user = self.request.user
        if not user.is_staff:
            qs = qs.filter(owner=user)
        return qs
```

Object-level permissions still apply on **retrieve/update/delete**; `get_queryset()` scopes **lists** and lookups.

### Interview points

- **Filter → search → order → paginate** is the mental model.
- Document supported query params in OpenAPI/Swagger (`drf-spectacular` or `coreapi`).
- Conflicting params: last backend wins for ordering; filters are ANDed.

---

## Chapter summary

| Backend | Param | Use case |
|---------|-------|----------|
| DjangoFilterBackend | `?field=value` | Exact/range/related filters |
| SearchFilter | `?search=term` | Full-text-ish search across columns |
| OrderingFilter | `?ordering=field` | Client-controlled sort |

Install **django-filter**, define **FilterSet** classes for non-trivial logic, and always **whitelist** `ordering_fields`.
