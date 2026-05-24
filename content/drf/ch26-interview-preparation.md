---
title: Chapter 26 — Interview Preparation
description: Common Django REST Framework interview questions and answers
order: 29
tags: [drf, interview, career]
---

# Chapter 26: Interview Preparation

Review these **11 common DRF interview questions** with concise answers you can expand in a technical interview.

---

## Q1: What is the difference between Serializer and ModelSerializer?

**Answer:** `Serializer` requires manually defining every field and `create()` / `update()` methods. `ModelSerializer` auto-generates fields from the model, auto-creates `create()` / `update()` methods, and includes model validators.

| Use case | Class |
|----------|-------|
| Login forms, composite payloads | `Serializer` |
| CRUD on Django models | `ModelSerializer` |

---

## Q2: What is the difference between APIView and ViewSet?

**Answer:** `APIView` handles **one URL endpoint** with separate methods (`get`, `post`, `put`, `delete`). `ViewSet` handles **all CRUD operations** for a model in one class with actions (`list`, `create`, `retrieve`, `update`, `destroy`). ViewSets work with **Routers** for automatic URL generation.

---

## Q3: Explain the DRF request lifecycle.

**Answer:**

```
Request → URL Resolution → Authentication → Permission Check →
Throttle Check → Content Negotiation → Parser → View Logic →
Serialization → Renderer → Response
```

Each step can short-circuit with an error response (e.g. 401 Unauthorized, 403 Forbidden, 429 Too Many Requests).

---

## Q4: What is the difference between authentication and permission?

**Answer:**

| Concept | Question answered | Runs |
|---------|-------------------|------|
| **Authentication** | WHO is the user? | First |
| **Permission** | WHAT can they do? | After auth |

Authentication verifies identity (session, token, JWT). Permission verifies access rights (`IsAuthenticated`, object-level checks).

---

## Q5: What is the N+1 query problem and how to fix it?

**Answer:** When you have related objects, Django makes **1 query** for the main objects and **N additional queries** for each related object accessed in a loop.

**Fix:**

- `select_related()` for `ForeignKey` (SQL `JOIN`)
- `prefetch_related()` for reverse relations and `ManyToMany` (separate query + Python join)

---

## Q6: What is the difference between select_related and prefetch_related?

**Answer:**

| Method | SQL strategy | Use for |
|--------|--------------|---------|
| `select_related` | Single query with `JOIN` | `ForeignKey`, `OneToOneField` |
| `prefetch_related` | Separate query, join in Python | `ManyToMany`, reverse `ForeignKey` |

---

## Q7: How does JWT authentication work?

**Answer:**

1. User logs in with credentials.
2. Server generates **Access Token** (short-lived) and **Refresh Token** (long-lived).
3. Client sends Access Token with each request (`Authorization: Bearer <token>`).
4. When it expires, client uses Refresh Token to get a new Access Token.

JWT is **stateless** — no database lookup needed per request (until you add a blocklist).

---

## Q8: What is the difference between has_permission and has_object_permission?

**Answer:**

| Method | Scope | When it runs |
|--------|-------|--------------|
| `has_permission` | View-level | All requests, before object lookup |
| `has_object_permission` | Object-level | Single-object actions, after retrieve |

`has_permission` must return `True` for `has_object_permission` to be called.

---

## Q9: How do you handle file uploads in DRF?

**Answer:**

1. Use `ImageField` / `FileField` on the model.
2. Set `parser_classes = [MultiPartParser, FormParser]` on the view.
3. Configure `MEDIA_URL` and `MEDIA_ROOT` in settings.
4. Serve media in development with `static()` in `urls.py`.

---

## Q10: What pagination types does DRF support?

**Answer:**

| Class | Query params | Best for |
|-------|--------------|----------|
| `PageNumberPagination` | `?page=2` | General APIs |
| `LimitOffsetPagination` | `?limit=10&offset=20` | SQL-style paging |
| `CursorPagination` | Encoded cursor | Infinite scroll, live feeds |

You can create **custom pagination** by subclassing and overriding `get_paginated_response()`.

---

## Q11: How do you optimize a DRF API for production?

**Answer:**

- Use `select_related` / `prefetch_related` to eliminate N+1 queries.
- Enable **pagination** on list endpoints.
- Add **caching** (`cache_page`, Redis backend).
- Use `only()` / `defer()` to limit columns on list views.
- Add **database indexes** on filtered and ordered fields.
- Use **separate settings** (`development.py` / `production.py`).
- Set `DEBUG = False`, JSON-only renderers, HTTPS, and proper CORS.
- Apply **throttling** and authentication on sensitive endpoints.
- Deploy with **Gunicorn** + reverse proxy; use PostgreSQL in production.
- Monitor query count and response times (APM, logging).

---

## Quick revision checklist

- [ ] Can explain Serializer vs ModelSerializer
- [ ] Can draw the request lifecycle
- [ ] Knows N+1 fixes and when to use each ORM method
- [ ] Understands JWT flow and permission hooks
- [ ] Can describe pagination types and production optimizations
