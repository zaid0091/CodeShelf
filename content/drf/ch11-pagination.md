---
title: Chapter 11 — Pagination
description: Page, limit-offset, and cursor pagination in Django REST Framework
order: 11
tags: [drf, pagination, api-design]
---

# Chapter 11: Pagination

Large collections returned in a single response hurt performance and usability. **Pagination** splits results into pages so clients request data in manageable chunks.

## Definitions

| Term | Meaning |
|------|---------|
| **Pagination** | Splitting a queryset into pages with metadata (count, next, previous links). |
| **Page size** | Number of records per page. |
| **Cursor** | Opaque pointer to a position in the dataset (used in cursor pagination). |

---

## 11.1 Introduction to Pagination

Without pagination, `GET /api/products/` might return thousands of rows — slow queries, huge JSON payloads, and poor mobile UX.

DRF provides three built-in pagination styles:

1. **Page number** — `?page=2` (most common, human-friendly).
2. **Limit/offset** — `?limit=10&offset=20` (SQL-like).
3. **Cursor** — `?cursor=cD0yMDIz` (best for live feeds, stable under inserts).

### Global configuration

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

Any `ListAPIView` or `ModelViewSet` list action automatically paginates when a default class is set.

### Per-view pagination

```python
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
```

### Typical paginated response

```json
{
    "count": 150,
    "next": "http://127.0.0.1:8000/api/products/?page=2",
    "previous": null,
    "results": [
        {"id": 1, "name": "Widget"},
        {"id": 2, "name": "Gadget"}
    ]
}
```

### Interview points

- Why paginate? **Performance**, **bandwidth**, **UX**, and **rate-limit fairness**.
- Pagination is applied in the **renderer/parser pipeline** after the view builds the queryset.
- Disabling pagination: set `pagination_class = None` on the view.

---

## 11.2 PageNumberPagination

Clients navigate with `?page=N`. DRF computes offset as `(page - 1) * page_size`.

```python
from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'           # default: 'page'
    page_size_query_param = 'size'      # allow ?size=25
    max_page_size = 50
    last_page_strings = ('last',)       # optional: ?page=last
```

```python
# views.py
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
```

```bash
curl "http://127.0.0.1:8000/api/products/?page=2&size=5"
```

### Custom page link format

Override `get_paginated_response()` to change the response shape:

```python
class CustomPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'meta': {
                'total': self.page.paginator.count,
                'current_page': self.page.number,
                'total_pages': self.page.paginator.num_pages,
            },
            'data': data,
        })
```

### Interview points

- **PageNumberPagination** uses `LIMIT/OFFSET` under the hood — deep pages (`page=10000`) can be slow on large tables.
- Always **order** the queryset consistently when paginating (e.g. `order_by('id')`).
- `Invalid page` returns **404** by default.

---

## 11.3 LimitOffsetPagination

Mimics SQL `LIMIT` and `OFFSET`. Common in APIs that expose offset-based navigation.

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,  # used as default limit when PAGE_SIZE is set
}
```

```python
from rest_framework.pagination import LimitOffsetPagination

class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 100
```

```bash
curl "http://127.0.0.1:8000/api/products/?limit=10&offset=20"
```

Response shape matches page-number style (`count`, `next`, `previous`, `results`).

### When to use

- Integrating with clients that already use limit/offset.
- Simple “load more” UIs where page numbers are not shown.

### Interview points

- Same **deep offset** performance issue as page numbers on very large datasets.
- `next` and `previous` links are built from current limit/offset.

---

## 11.4 CursorPagination

Uses an encoded **cursor** (often a timestamp or PK) instead of page numbers. Stable when rows are inserted/deleted during browsing.

```python
from rest_framework.pagination import CursorPagination

class ProductCursorPagination(CursorPagination):
    page_size = 10
    ordering = '-created_at'   # required: stable ordering field
    cursor_query_param = 'cursor'
```

```python
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductCursorPagination
```

```bash
curl "http://127.0.0.1:8000/api/products/"
curl "http://127.0.0.1:8000/api/products/?cursor=cD0yMDI0LTAxLTAx"
```

Response (no total `count` by default — expensive on large tables):

```json
{
    "next": "http://127.0.0.1:8000/api/products/?cursor=cD0yMDI0",
    "previous": null,
    "results": [...]
}
```

### Custom cursor pagination

```python
class ProductCursorPagination(CursorPagination):
    page_size = 20
    ordering = '-id'

    def get_ordering(self, request, queryset, view):
        ordering = request.query_params.get('ordering')
        if ordering:
            return (ordering,)
        return self.ordering
```

### Interview points

- **Cannot jump to arbitrary page** — only next/previous (by design).
- Requires a **unique, sequential** ordering field (often `-created_at` or `-id`).
- Best for **infinite scroll**, **activity feeds**, and **real-time** data.
- Avoids **duplicate/skipped rows** when data changes between requests (unlike offset pagination).

---

## Chapter summary

| Style | Query params | Pros | Cons |
|-------|--------------|------|------|
| Page number | `?page=2` | Intuitive, total count | Slow deep pages |
| Limit/offset | `?limit=10&offset=20` | Familiar to SQL devs | Slow deep offsets |
| Cursor | `?cursor=...` | Stable, fast at scale | No random access, no count |

Choose **page number** for admin dashboards, **cursor** for social feeds, and **limit/offset** when clients expect it.
