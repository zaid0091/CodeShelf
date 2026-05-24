---
title: Django Interview Preparation
description: Common Django interview questions, ORM patterns, architecture, and system design
order: 14
tags: [django, interview, career]
---

# Chapter 14: Django Interview Preparation

## 14.1 Preparation roadmap

| Area | Review chapters |
|------|-----------------|
| MTV / request cycle | [Introduction](./ch01-django-introduction.md), [Views](./ch04-views-urls.md) |
| ORM & migrations | [Models](./ch03-models-orm.md), [Migrations](./ch09-migrations.md) |
| Auth & security | [Authentication](./ch08-authentication.md), [Best Practices](./ch13-best-practices.md) |
| Templates & forms | [Templates](./ch05-templates.md), [Forms](./ch06-forms.md) |
| Production | [Deployment](./ch12-deployment-basics.md) |

Solid [Python fundamentals](../python/ch14-interview-prep.md) are assumed.

## 14.2 Core conceptual questions

**Q: Explain Django's MTV architecture.**

Models hold data and business rules; Templates render HTML; Views process requests and connect models to templates. URLconf routes URLs to views.

**Q: What happens when a request hits Django?**

Middleware → URL resolver → view → (optional ORM) → template render → middleware → response.

**Q: Difference between project and app?**

Project = site configuration; app = modular feature (blog, users) reusable across projects.

**Q: `null=True` vs `blank=True`?**

`null` is database-level (NULL allowed); `blank` is validation-level (forms may omit). For strings, prefer `blank=True` without `null=True`.

## 14.3 ORM interview topics

```python
# select_related vs prefetch_related
Post.objects.select_related("author")
Post.objects.prefetch_related("tags")

# F expressions — race-safe increment
Post.objects.filter(pk=1).update(views=F("views") + 1)

# Q objects
Post.objects.filter(Q(published=True) | Q(author=user))
```

| Question | Key point |
|----------|-----------|
| N+1 queries | Fix with select/prefetch |
| `get()` vs `filter()` | get raises if 0 or >1 |
| Migrations | Version schema; don't edit applied |
| Raw SQL when? | Complex reports; still parameterize |

## 14.4 FBV vs CBV

| FBV | CBV |
|-----|-----|
| Explicit, simple | DRY for CRUD |
| Any logic | Generic views + mixins |
| Easier for beginners | Steeper learning curve |

See [Class-Based Views](./ch11-class-based-views.md).

## 14.5 Security questions

**Q: How does Django prevent CSRF?**

Token in forms validated by middleware on POST/PUT/DELETE.

**Q: How prevent SQL injection?**

ORM parameterizes queries; escape user input in raw SQL.

**Q: What must change in production?**

`DEBUG=False`, strong `SECRET_KEY`, `ALLOWED_HOSTS`, HTTPS cookies, real DB.

## 14.6 Middleware

> **Definition:** **Middleware** is a layer processing every request/response globally — auth, sessions, CSRF, security headers.

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    ...
]
```

Order matters — e.g., `SessionMiddleware` before `AuthenticationMiddleware`.

## 14.7 Caching (common follow-up)

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def post_list(request):
    ...
```

```python
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
    }
}
```

## 14.8 Signals (brief)

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Post)
def notify_subscribers(sender, instance, created, **kwargs):
    if created:
        send_notification(instance)
```

Use sparingly — hidden coupling. Prefer explicit service calls when possible.

## 14.9 System design prompts

Be ready to sketch:

- User auth flow (session vs JWT)
- Blog with comments and moderation
- File upload pipeline ([Static & Media](./ch10-static-media-files.md))
- Scaling reads (cache, read replicas)
- Background jobs (Celery)

## 14.10 Coding exercises

1. Write a view that returns JSON list of posts with author name — no N+1.
2. Implement slug-based detail URL with `get_object_or_404`.
3. Custom permission: only author can edit post (FBV or CBV mixin).
4. Explain migration steps for adding a non-null FK to existing table.

## 14.11 Resources

| Resource | Focus |
|----------|-------|
| Official Django docs | Authoritative reference |
| Django source (select parts) | Deep internals |
| This course (ch01–ch13) | Structured review |
| Build a small CRUD app | Hands-on confidence |

## Summary

Django interviews test MTV flow, ORM efficiency, auth/security defaults, and production awareness. Review core chapters, practice explaining tradeoffs aloud, and build one complete app end-to-end.

## Course complete

Return to [Course Overview](./ch00-course-overview.md) or explore [DRF](../drf/ch00-course-overview.md) for API development.
