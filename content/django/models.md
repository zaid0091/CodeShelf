---
title: Django Models & ORM
description: Database models, queries, and migrations
order: 2
tags: [orm, database]
---

# Django Models & ORM

Django's ORM lets you interact with your database using Python instead of SQL.

## Field Types

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    views = models.IntegerField(default=0)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", blank=True)
```

## Common Field Options

| Option | Purpose |
|--------|---------|
| `max_length` | Max chars for CharField |
| `default` | Default value |
| `null=True` | DB allows NULL |
| `blank=True` | Form validation allows empty |
| `unique=True` | Unique constraint |
| `choices` | Predefined options |

## Migrations

```bash
python manage.py makemigrations   # create migration files
python manage.py migrate          # apply to database
python manage.py showmigrations   # list migration status
```

## QuerySet Operations

```python
# Create
Article.objects.create(title="Hello", body="World")

# Read
Article.objects.all()
Article.objects.filter(published=True)
Article.objects.get(pk=1)
Article.objects.filter(title__icontains="django")

# Update
article = Article.objects.get(pk=1)
article.views += 1
article.save()

# Or bulk update
Article.objects.filter(published=False).update(published=True)

# Delete
article.delete()
Article.objects.filter(views=0).delete()
```

## Lookup Expressions

```python
Article.objects.filter(views__gte=100)    # views >= 100
Article.objects.filter(title__startswith="Django")
Article.objects.filter(created_at__year=2024)
Article.objects.exclude(published=False)
Article.objects.order_by("-created_at")[:10]
```

## Relationships

```python
# ForeignKey — many-to-one
author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
user.articles.all()  # reverse lookup

# ManyToMany
tags = models.ManyToManyField(Tag)
article.tags.add(tag1, tag2)
article.tags.all()
```
