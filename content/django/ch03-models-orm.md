---
title: Models and ORM
description: Model fields, relationships, QuerySets, lookups, and managers
order: 3
tags: [django, orm, models]
---

# Chapter 3: Models and ORM

## 3.1 What is the ORM?

> **Definition:** Django's **ORM** (Object-Relational Mapper) maps Python classes to database tables and provides a Python API for queries instead of raw SQL.

Models live in `models.py`. Changes require [migrations](./ch09-migrations.md).

## 3.2 Defining a model

```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
```

| Method/attr | Purpose |
|-------------|---------|
| `__str__` | String representation (admin, shell) |
| `Meta.ordering` | Default QuerySet order |
| `auto_now_add` | Set once on create |
| `auto_now` | Update on every save |

## 3.3 Common field types

| Field | DB type | Use |
|-------|---------|-----|
| `CharField` | VARCHAR | Short text |
| `TextField` | TEXT | Long text |
| `IntegerField` | INTEGER | Integers |
| `BooleanField` | BOOLEAN | True/False |
| `DateField` / `DateTimeField` | DATE / TIMESTAMP | Dates |
| `EmailField` | VARCHAR | Validated email |
| `URLField` | VARCHAR | URLs |
| `SlugField` | VARCHAR | URL-safe strings |
| `FileField` / `ImageField` | VARCHAR path | Uploads |
| `JSONField` | JSON | Structured data |

## 3.4 Field options

| Option | Purpose |
|--------|---------|
| `max_length` | Required for CharField |
| `default` | Default value |
| `null=True` | DB allows NULL |
| `blank=True` | Form validation allows empty |
| `unique=True` | Unique constraint |
| `choices` | Predefined options |
| `db_index=True` | Database index |

```python
STATUS_CHOICES = [
    ("draft", "Draft"),
    ("published", "Published"),
]

status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
```

**Rule of thumb:** use `blank=True` for optional form fields; use `null=True` for optional non-string DB columns.

## 3.5 Relationships

```python
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag, blank=True)
    featured = models.OneToOneField("Post", null=True, blank=True, on_delete=models.SET_NULL)
```

| Relationship | SQL | Reverse access |
|--------------|-----|----------------|
| `ForeignKey` | Many-to-one | `user.posts.all()` |
| `ManyToManyField` | Join table | `post.tags.all()` |
| `OneToOneField` | Unique FK | `profile.user` |

### `on_delete` options

| Value | Behavior |
|-------|----------|
| `CASCADE` | Delete related objects |
| `PROTECT` | Prevent delete |
| `SET_NULL` | Set FK to NULL (needs `null=True`) |
| `SET_DEFAULT` | Set default value |

## 3.6 CRUD with QuerySets

```python
# Create
post = Post.objects.create(title="Hello", body="World")
Post(title="Hi", body="...").save()

# Read
Post.objects.all()
Post.objects.filter(published=True)
Post.objects.get(pk=1)
Post.objects.filter(title__icontains="django")

# Update
post.title = "Updated"
post.save()
Post.objects.filter(published=False).update(published=True)

# Delete
post.delete()
Post.objects.filter(views=0).delete()
```

> **Definition:** A **QuerySet** is a lazy collection of model instances — SQL runs when evaluated (iteration, `list()`, `len()`, etc.).

## 3.7 Lookup expressions

```python
Post.objects.filter(views__gte=100)
Post.objects.filter(title__startswith="Django")
Post.objects.filter(created_at__year=2024)
Post.objects.filter(created_at__date=date.today())
Post.objects.exclude(published=False)
Post.objects.order_by("-created_at")[:10]
Post.objects.distinct()
Post.objects.count()
Post.objects.exists()
```

| Lookup | Meaning |
|--------|---------|
| `exact`, `iexact` | Case-sensitive/insensitive exact |
| `contains`, `icontains` | Substring |
| `in` | In list |
| `gt`, `gte`, `lt`, `lte` | Comparisons |
| `isnull` | NULL check |

## 3.8 Q objects and F expressions

```python
from django.db.models import Q, F

Post.objects.filter(Q(published=True) | Q(author__username="admin"))
Post.objects.filter(title__icontains="django").filter(published=True)

Post.objects.update(views=F("views") + 1)
```

## 3.9 Aggregation

```python
from django.db.models import Count, Avg, Max

Post.objects.aggregate(avg_views=Avg("views"))
User.objects.annotate(post_count=Count("posts"))
```

## 3.10 Custom managers

```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)

class Post(models.Model):
    # fields defined above...
    objects = models.Manager()
    published = PublishedManager()

Post.published.all()
```

## Exercises

1. Create `Post` and `Tag` models with FK and M2M; run makemigrations/migrate.
2. In `shell`, create 5 posts and filter published ones.
3. Use `__icontains` and `order_by` to build a search query.
4. Add `__str__` and `Meta.ordering` to all models.

## Summary

Models define schema; the ORM provides QuerySets for CRUD, filtering, and aggregation. Choose fields and relationships carefully; migrations track schema changes.

## Next chapter

Continue to [Views & URLs](./ch04-views-urls.md).
