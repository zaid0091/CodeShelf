---
title: Django Best Practices
description: Project structure, security, ORM performance, testing, and coding conventions
order: 13
tags: [django, best-practices, security]
---

# Chapter 13: Django Best Practices

## 13.1 Project organization

```text
myproject/
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── blog/
│   └── accounts/
├── templates/
├── static/
├── tests/
├── manage.py
└── requirements.txt
```

| Practice | Benefit |
|----------|---------|
| One app per domain | Reusable, testable |
| `apps/` folder | Clear boundaries |
| Split settings | Safe prod defaults |

## 13.2 Fat models, thin views

Put business logic on models or services, not views:

```python
class Post(models.Model):
    ...

    def publish(self):
        self.published = True
        self.published_at = timezone.now()
        self.save(update_fields=["published", "published_at"])
```

```python
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect("post-detail", pk=pk)
```

## 13.3 ORM performance

```python
# N+1 problem — BAD
for post in Post.objects.all():
    print(post.author.username)

# GOOD — select_related for FK
for post in Post.objects.select_related("author"):
    print(post.author.username)

# prefetch_related for M2M/reverse FK
posts = Post.objects.prefetch_related("tags")
```

| Method | Use for |
|--------|---------|
| `select_related` | ForeignKey, OneToOne |
| `prefetch_related` | ManyToMany, reverse FK |
| `only` / `defer` | Limit columns |
| `exists()` / `count()` | Avoid loading rows |

See [Models & ORM](./ch03-models-orm.md).

## 13.4 Security essentials

| Risk | Mitigation |
|------|------------|
| SQL injection | Use ORM; parameterize raw SQL |
| XSS | Auto-escape = templates; careful `\|safe` |
| CSRF | `{% csrf_token %}` on forms |
| Clickjacking | `XFrameOptionsMiddleware` |
| Secret leakage | Env vars, never commit `.env` |

```python
# settings.py production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
```

## 13.5 Query optimization rules

1. Use `django-debug-toolbar` in development
2. Log slow queries
3. Add DB indexes on filtered/sorted columns
4. Paginate large lists

```python
class Post(models.Model):
    slug = models.SlugField(db_index=True)
```

## 13.6 Testing

```python
from django.test import TestCase, Client
from django.urls import reverse
from .models import Post

class PostTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list_returns_200(self):
        response = self.client.get(reverse("post-list"))
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        Post.objects.create(title="Test", body="Body")
        self.assertEqual(Post.objects.count(), 1)
```

```bash
python manage.py test
```

## 13.7 URL and naming conventions

- Use kebab-case paths: `/blog/create/`
- Named URLs: `name="post-detail"`
- App namespaces for large projects

## 13.8 Settings anti-patterns

| Avoid | Prefer |
|-------|--------|
| `DEBUG=True` in prod | Environment-specific settings |
| Hard-coded secrets | `os.environ` |
| SQLite in prod | PostgreSQL |
| `ALLOWED_HOSTS = ["*"]` with DEBUG off | Explicit hosts |

## 13.9 Code style

Follow [PEP 8](../python/ch13-best-practices.md). Use:

- `get_object_or_404` over bare `.get()`
- `reverse()` / `{% url %}` over hard-coded paths
- Custom managers for repeated QuerySets

## 13.10 Documentation and requirements

- README: setup, migrate, test, run
- Pin dependencies in `requirements.txt`
- Changelog for API-breaking changes

## Exercises

1. Refactor a fat view — move logic to a model method.
2. Fix an N+1 query using `select_related`.
3. Write two tests: list view 200 and model creation.
4. Audit your `settings.py` against the security table above.

## Summary

Structure projects clearly, keep views thin, optimize ORM access, test critical paths, and treat security settings as non-negotiable in production.

## Next chapter

Continue to [Interview Preparation](./ch14-interview-prep.md).
