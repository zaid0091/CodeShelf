---
title: Django Introduction
description: Django history, MTV architecture, batteries-included design, and when to use Django
order: 1
tags: [django, mtv, introduction]
---

# Chapter 1: Django Introduction

## 1.1 What is Django?

> **Definition:** **Django** is a free, open-source web framework written in Python. It provides tools for URL routing, ORM, templates, forms, authentication, and an admin interface out of the box.

Created in 2005 at a Kansas newspaper, Django prioritizes **rapid development**, **security**, and **scalability**.

## 1.2 Why Django?

| Advantage | Explanation |
|-----------|-------------|
| Batteries included | Auth, admin, ORM, forms built-in |
| Security defaults | CSRF, XSS helpers, SQL injection protection via ORM |
| Mature ecosystem | Packages, hosting, documentation |
| Admin interface | Free CRUD UI for models |
| Scalable | Used by Instagram, Pinterest, Mozilla |

## 1.3 MTV architecture

Django uses **MTV** — analogous to MVC:

| Layer | Role | Analogous to MVC |
|-------|------|------------------|
| **Model** | Data and business logic | Model |
| **Template** | Presentation (HTML) | View |
| **View** | Request handling logic | Controller |

```text
Browser Request
      ↓
   URLconf (urls.py)
      ↓
   View (views.py)  ←→  Model (models.py) ←→ Database
      ↓
   Template (HTML)
      ↓
   HTTP Response
```

See [Views & URLs](./ch04-views-urls.md) and [Templates](./ch05-templates.md).

## 1.4 Request/response cycle

```python
# Simplified flow
# 1. User visits /blog/
# 2. urls.py maps path to blog.views.index
# 3. View queries Post.objects.all()
# 4. View renders template with context
# 5. HttpResponse returned to browser
```

> **Definition:** **WSGI** (Web Server Gateway Interface) is the standard interface between web servers and Python web apps. Django ships with `wsgi.py` for deployment.

## 1.5 Django vs alternatives

| Framework | Strengths | Tradeoffs |
|-----------|-----------|-----------|
| Django | Full-stack, ORM, admin | Heavier for tiny APIs |
| Flask | Minimal, flexible | More manual setup |
| FastAPI | Async APIs, OpenAPI | Less built-in for HTML sites |
| DRF | REST on Django | API-focused layer |

For traditional web apps with HTML + database, Django is a strong default.

## 1.6 Project vs app

```text
mysite/          ← project (settings, root urls)
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── blog/        ← app (feature module)
    ├── models.py
    ├── views.py
    └── urls.py
```

- **Project:** One per website — configuration container
- **App:** Reusable module — one app per feature area

Detail in [Setup & Project Structure](./ch02-setup-project-structure.md).

## 1.7 Django design principles

| Principle | Meaning |
|-----------|---------|
| DRY | Don't Repeat Yourself |
| Explicit is better | Clear URL patterns, settings |
| Loose coupling | Apps independent where possible |
| Fast iteration | Admin + ORM speed development |

## 1.8 What Django includes

| Component | Purpose |
|-----------|---------|
| `django.contrib.auth` | User authentication |
| `django.contrib.admin` | Auto-generated admin |
| `django.contrib.sessions` | Session framework |
| `django.contrib.messages` | Flash messages |
| `django.contrib.staticfiles` | Static file handling |

## 1.9 When to choose Django

**Good fit:**

- Content sites, dashboards, SaaS with accounts
- CRUD-heavy applications
- Teams wanting conventions and built-in admin

**Consider alternatives:**

- Pure JSON micro-API (FastAPI, DRF-only)
- Real-time-heavy apps (may add Channels)

## 1.10 Hello Django (preview)

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

Full setup in the next chapter.

## Exercises

1. Read the Django "Overview" docs and list three built-in apps you expect to use.
2. Draw the MTV flow for a blog post list page.
3. Compare Django to one other Python web framework in one paragraph.
4. Install Django locally: `pip install django`.

## Summary

Django is a batteries-included Python web framework organized around MTV. Projects contain apps; views connect URLs, models, and templates.

## Next chapter

Continue to [Setup & Project Structure](./ch02-setup-project-structure.md).
