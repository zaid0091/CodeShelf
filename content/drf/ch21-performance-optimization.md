---
title: Chapter 21 — Performance Optimization
description: Query optimization, caching, and selective field loading in DRF
order: 21
tags: [drf, performance, orm, caching]
---

# Chapter 21: Performance Optimization

Production APIs must stay fast under load. Most DRF performance wins come from **fewer database queries**, **smaller payloads**, and **caching** — not from micro-optimizing Python.

## Definitions

| Term | Meaning |
|------|---------|
| **N+1 query problem** | One query for the main objects plus one extra query per related row when relations are accessed lazily in a loop. |
| **select_related** | SQL `JOIN` in a single query for `ForeignKey` and `OneToOneField`. |
| **prefetch_related** | Separate query for related rows, joined in Python — for `ManyToMany` and reverse `ForeignKey`. |
| **only() / defer()** | Load only (or exclude) specific columns from the database. |
| **cache_page** | Django view decorator that caches the full HTTP response for a TTL. |

---

## 21.1 Query Optimization

### The N+1 problem

When a serializer accesses `book.author` for each book in a list, Django may run **1 query for books + N queries for authors**.

```python
# ── THE N+1 PROBLEM ──

# BAD — makes N+1 database queries:
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    # For 100 books with authors:
    # 1 query for books + 100 queries for each book's author = 101 queries!

# GOOD — use select_related (ForeignKey/OneToOne):
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author', 'category')
    # 1 query with JOIN = 1 query total!

# GOOD — use prefetch_related (ManyToMany/Reverse ForeignKey):
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.prefetch_related('reviews')
    # 2 queries total: 1 for books + 1 for all reviews

# COMBINED:
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related(
        'author', 'category'     # ForeignKey fields
    ).prefetch_related(
        'reviews'                # Reverse relation
    )
```

### When to use which

```
select_related:
  → For ForeignKey and OneToOneField
  → Does a SQL JOIN (single query)
  → "Get the author AT THE SAME TIME as the book"

prefetch_related:
  → For ManyToManyField and reverse ForeignKey
  → Does a separate query then joins in Python
  → "Get all reviews in a second query, then attach to books"
```

| Method | SQL strategy | Best for |
|--------|--------------|----------|
| `select_related('author')` | `JOIN` | Forward FK, OneToOne |
| `prefetch_related('reviews')` | 2+ queries | M2M, reverse FK |

### Interview points

- Use `django-debug-toolbar` or `connection.queries` in development to count queries.
- `Prefetch()` objects allow filtering the prefetched queryset.
- Always optimize the **queryset** used by the view, not only the serializer.

---

## 21.2 Caching

Cache **read-heavy, rarely changing** list endpoints (e.g. categories, featured products).

```python
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
```

**Notes:**

- `cache_page` keys on full URL (including query string) — pagination params create separate cache entries.
- In production, configure **Redis** or **Memcached** as `CACHES` backend instead of LocMem.
- Invalidate or shorten TTL when data changes frequently.

---

## 21.3 Only Select Needed Fields

For list views, you often do not need every column (e.g. large `description` text).

```python
class BookViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            # Only get needed columns from database
            return Book.objects.only('id', 'title', 'price')
        return Book.objects.all()
```

| Method | Effect |
|--------|--------|
| `only('id', 'title')` | SELECT only these fields (+ PK); other fields trigger extra queries if accessed |
| `defer('description')` | SELECT everything except deferred fields |

Use `only()` when the list serializer exposes a small subset of fields.

### Interview points

- Combining `select_related` + `only()` reduces both query count and row size.
- Add **database indexes** on fields used in `filter()`, `order_by()`, and foreign keys.
- Enable **pagination** (Chapter 11) — the cheapest way to cap response size.
