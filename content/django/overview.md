---
title: Django Overview
description: Django MTV architecture and project structure
order: 1
tags: [basics, mtv]
---

# Django Overview

Django is a high-level Python web framework that encourages rapid development with a clean, pragmatic design.

## MTV Architecture

| Layer | Role | Analogous to |
|-------|------|--------------|
| **Model** | Data & business logic | Database layer |
| **Template** | Presentation (HTML) | View layer |
| **View** | Request handling logic | Controller |

## Project Structure

```
myproject/
├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── myapp/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── templates/
```

## Quick Start

```bash
# Create project
django-admin startproject myproject
cd myproject

# Create app
python manage.py startapp blog

# Run migrations
python manage.py migrate

# Start dev server
python manage.py runserver
```

## settings.py — Register App

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    # ...
    "blog",  # your app
]
```

## Basic View

```python
# blog/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django!")
```

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

## Django ORM Preview

```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```
