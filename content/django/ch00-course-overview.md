---
title: Django Course Overview
description: Complete Django course — from MTV fundamentals to production-ready applications, deployment, and interview prep
order: 0
tags: [django, python, backend, web-development, overview]
---

# The Complete Django Course

From absolute beginner to production-ready — every Django concept explained with examples, exercises, and real-world patterns.

This course takes you from your first `django-admin startproject` all the way to deploying secure, scalable web applications. By the end you will be able to design, build, test, and ship full-stack Django apps with confidence — and answer common interview questions fluently.

## Course structure

### Part 1: Django Foundations

The mental model and tooling required to start building real Django applications.

| Chapter | Topic |
|---------|--------|
| [Django Introduction](./ch01-django-introduction.md) | What Django is, history, MTV architecture, request/response cycle, middleware, WSGI/ASGI |
| [Setup & Project Structure](./ch02-setup-project-structure.md) | Installing Django, virtual environments, `startproject`, project vs. app layout |

### Part 2: Core Django Development

The four pillars every Django app is built on — models, views, templates, and forms.

| Chapter | Topic |
|---------|--------|
| [Models & ORM](./ch03-models-orm.md) | Models, fields, relationships, QuerySets, lookups, `select_related`/`prefetch_related` |
| [Views & URLs](./ch04-views-urls.md) | Function-based views, URL routing, `path()`/`re_path()`, request and response objects |
| [Templates](./ch05-templates.md) | Template language, inheritance, context, filters, tags, and template loading |
| [Forms](./ch06-forms.md) | `Form` and `ModelForm`, validation, error handling, CSRF protection, file uploads |

### Part 3: Built-in Django Features

Django's "batteries included" — the powerful tools that ship with the framework.

| Chapter | Topic |
|---------|--------|
| [Admin Panel](./ch07-admin-panel.md) | Registering models, `ModelAdmin`, list display, search, custom actions |
| [Authentication](./ch08-authentication.md) | User model, login/logout, permissions, groups, password reset, decorators |
| [Migrations](./ch09-migrations.md) | `makemigrations`, `migrate`, schema evolution, data migrations, squashing |
| [Static & Media Files](./ch10-static-media-files.md) | `STATIC_URL`, `MEDIA_URL`, `collectstatic`, serving uploads in dev and production |

### Part 4: Advanced Django & Production

Patterns that take you from "it works on my laptop" to "it runs reliably for real users".

| Chapter | Topic |
|---------|--------|
| [Class-Based Views](./ch11-class-based-views.md) | `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`, mixins, FBV vs. CBV |
| [Deployment Basics](./ch12-deployment-basics.md) | Gunicorn, Nginx, environment variables, `DEBUG=False`, allowed hosts, static files in prod |
| [Best Practices](./ch13-best-practices.md) | Settings split, security headers, query optimization, project layout conventions |
| [Interview Preparation](./ch14-interview-prep.md) | Common Django interview questions, ORM gotchas, scaling discussions |

## Prerequisites

Before starting this course you should be comfortable with:

| Requirement | Why it matters |
|-------------|----------------|
| Python 3.10+ | Django is Python — functions, classes, decorators, and exceptions are used throughout |
| HTML & CSS | Required to write templates and understand how Django renders pages |
| SQL basics | Helps you reason about what the ORM is doing under the hood |
| Command line | You will run `python manage.py …` commands constantly |
| Git (optional) | Recommended once you start building real projects |

> **Tip:** If you are new to Python, work through the [Python course](../python/ch00-course-overview.md) first — especially chapters on functions, OOP, and modules.

## How to use these notes

1. Read **Part 1** end-to-end before writing any code — the mental model is more important than syntax.
2. From **Part 2** onward, build a single sample project (a blog, todo app, or bookstore) alongside the chapters so concepts compound.
3. Run **every command** in your own terminal — `manage.py` skills only develop through repetition.
4. Use **Part 3** features as you need them; they are independent and can be revisited.
5. Read **Part 4** before deploying anything publicly or attending a Django interview.

## Recommended learning path

```text
Week 1:  ch01 Introduction  →  ch02 Setup            (concepts + first project)
Week 2:  ch03 Models & ORM                            (schema, migrations, shell)
Week 3:  ch04 Views/URLs   →  ch05 Templates          (first dynamic pages)
Week 4:  ch06 Forms        →  ch07 Admin              (data in and out of the DB)
Week 5:  ch08 Auth         →  ch09 Migrations         (real users + safe schema changes)
Week 6:  ch10 Static/Media →  ch11 Class-Based Views  (production assets + reusable views)
Week 7:  ch12 Deployment   →  ch13 Best Practices     (ship it + harden it)
Week 8:  ch14 Interview Prep                          (consolidate everything)
```

## Tools you will use

| Tool | Purpose |
|------|---------|
| `django` (pip) | The framework itself — installed into a virtual environment |
| `python manage.py` | CLI for migrations, running servers, opening shells, creating users |
| Virtual environment (`venv`) | Isolated dependencies per project, avoids global pollution |
| SQLite | Default development database — zero setup |
| PostgreSQL | Recommended production database (covered in Part 4) |
| Gunicorn + Nginx | Production WSGI server + reverse proxy |
| VS Code / Cursor / PyCharm | Editors with Django-aware extensions |

## What you will build (skills, not a single project)

By the end of this course you will be able to:

- Design relational schemas with the Django ORM, including one-to-many and many-to-many relationships
- Implement complete CRUD flows with both function- and class-based views
- Build and validate forms — including file uploads — with proper CSRF protection
- Customize the Django admin so non-technical users can manage your data
- Authenticate users, restrict views by permission, and reset passwords securely
- Manage schema changes with migrations, including data migrations and squashing
- Serve static and media files correctly in both development and production
- Deploy a Django app behind Gunicorn and Nginx with `DEBUG=False`, environment variables, and HTTPS
- Apply security and performance best practices to a real codebase
- Discuss Django architecture, ORM internals, and scaling considerations in an interview

## Chapter summaries

### [Chapter 1 — Django Introduction](./ch01-django-introduction.md)

What Django is, why companies like Instagram and Pinterest use it, and how MTV differs from MVC. Covers the request/response cycle, middleware, WSGI vs. ASGI, project vs. app, and when **not** to choose Django.

### [Chapter 2 — Setup & Project Structure](./ch02-setup-project-structure.md)

Create an isolated virtual environment, install Django, run `django-admin startproject`, and understand every file the scaffold creates — `manage.py`, `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`. Compare project-level config with app-level code.

### [Chapter 3 — Models & ORM](./ch03-models-orm.md)

Define models, pick the right field types, and express `ForeignKey`, `ManyToManyField`, and `OneToOneField` relationships. Master QuerySet laziness, field lookups, `Q` and `F` objects, aggregation, custom managers, and the difference between `select_related` and `prefetch_related`.

### [Chapter 4 — Views & URLs](./ch04-views-urls.md)

Write function-based views, return `HttpResponse` and `JsonResponse`, redirect, and handle 404s. Route requests with `path()` converters, named URLs, `include()`, and `reverse()`. Understand the request object — `GET`, `POST`, `FILES`, `user`, `session`.

### [Chapter 5 — Templates](./ch05-templates.md)

Use the Django template language — variables, filters, `{% if %}`, `{% for %}`, and `{% url %}`. Build a base layout with `{% extends %}` and `{% block %}`, include partials, and configure `TEMPLATES` and template loaders.

### [Chapter 6 — Forms](./ch06-forms.md)

Build forms with `forms.Form` and `forms.ModelForm`, render them in templates, validate input with `clean_<field>()` and `clean()`, display field errors, and handle file uploads. Cover CSRF protection end-to-end.

### [Chapter 7 — Admin Panel](./ch07-admin-panel.md)

Register models, configure `list_display`, `list_filter`, `search_fields`, and `readonly_fields`. Customize the change form with `fieldsets`, define inlines, add custom admin actions, and override the default admin templates.

### [Chapter 8 — Authentication](./ch08-authentication.md)

Use Django's built-in `User` model, log users in and out, protect views with `@login_required` and `@permission_required`, manage groups and permissions, and wire up password reset emails.

### [Chapter 9 — Migrations](./ch09-migrations.md)

Generate migrations with `makemigrations`, apply them with `migrate`, inspect SQL with `sqlmigrate`, write data migrations, handle conflicts, and squash migration history for long-lived projects.

### [Chapter 10 — Static & Media Files](./ch10-static-media-files.md)

Configure `STATIC_URL`, `STATIC_ROOT`, `MEDIA_URL`, and `MEDIA_ROOT`. Serve static files in development, collect them for production with `collectstatic`, handle user-uploaded media, and understand the role of `whitenoise` and cloud storage.

### [Chapter 11 — Class-Based Views](./ch11-class-based-views.md)

Replace boilerplate CRUD views with `ListView`, `DetailView`, `CreateView`, `UpdateView`, and `DeleteView`. Compose behavior with mixins like `LoginRequiredMixin`, override `get_queryset()` and `form_valid()`, and decide when to prefer FBVs.

### [Chapter 12 — Deployment Basics](./ch12-deployment-basics.md)

Move from `runserver` to a production stack — Gunicorn behind Nginx, environment-driven settings, `DEBUG=False`, `ALLOWED_HOSTS`, secure cookies, HTTPS, and serving static files correctly. Includes a deployment checklist.

### [Chapter 13 — Best Practices](./ch13-best-practices.md)

Split settings by environment, store secrets in env vars, write fat models / thin views, optimize queries with `only()` and `defer()`, and structure projects so they stay readable as they grow.

### [Chapter 14 — Interview Preparation](./ch14-interview-prep.md)

Common Django interview questions with concise and deep answers — MTV architecture, ORM internals, `select_related` vs `prefetch_related`, middleware, signals, CSRF, and scaling. Includes whiteboard-style design discussions.

## Key definitions

> **Definition — Django:** A high-level, batteries-included Python web framework that enables rapid development of secure, maintainable web applications using the **MTV (Model–Template–View)** architectural pattern.

> **Definition — MTV (Model–Template–View):** Django's variation of MVC. **Models** describe the database, **Templates** describe the HTML, and **Views** contain the logic that ties them together. Django's "controller" is the framework itself.

> **Definition — Project vs. App:** A **project** is the deployable web application (one `settings.py`, one `urls.py`). An **app** is a self-contained, reusable module inside a project — e.g., `blog`, `accounts`, `payments`. A project can have many apps.

> **Definition — ORM (Object-Relational Mapper):** A layer that maps database rows to Python objects so you can query and update the database with method calls (`Book.objects.filter(...)`) instead of raw SQL.

> **Definition — Migration:** A versioned, code-generated description of a schema change. Migrations let you evolve your database alongside your models, in lockstep across all environments.

> **Definition — Middleware:** A pipeline of components that process every HTTP request before it reaches a view and every response before it leaves Django. Used for auth, sessions, CSRF, security headers, and more.

> **Definition — QuerySet:** A lazy, chainable representation of a database query. Nothing hits the database until the QuerySet is iterated, sliced, or otherwise evaluated.

## Quick start

Spin up a working Django project in under two minutes:

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate     # macOS / Linux
.venv\Scripts\activate        # Windows

# 2. Install Django
pip install django

# 3. Create a project and an app
django-admin startproject mysite .
python manage.py startapp blog

# 4. Apply built-in migrations and create a superuser
python manage.py migrate
python manage.py createsuperuser

# 5. Run the dev server
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) — you should see the Django rocket. The admin is at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

```python
# blog/views.py — your first Django view
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from Django!")
```

```python
# mysite/urls.py — wire the view to a URL
from django.contrib import admin
from django.urls import path
from blog.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
]
```

## Study tips

| Tip | Detail |
|-----|--------|
| Type along, don't copy | Manually typing `models.CharField(...)` builds muscle memory |
| Read the traceback | Django's error pages tell you exactly which file, line, and template caused the failure |
| Use the shell | `python manage.py shell` is the fastest way to experiment with the ORM |
| Read the source | Django's source code is famously readable — peek at `django/views/generic/` for CBVs |
| Bookmark the docs | [docs.djangoproject.com](https://docs.djangoproject.com/) is the single best Django reference on the web |
| Pair with DRF later | After [Chapter 11](./ch11-class-based-views.md), you are ready to start the [DRF course](../drf/ch00-course-overview.md) |

## Common mistakes to avoid

- **Skipping virtual environments.** Installing Django globally pollutes your system Python and breaks future projects.
- **Editing migrations by hand without understanding them.** Use `makemigrations` and let Django generate them; review with `sqlmigrate`.
- **N+1 query patterns.** Looping over related objects without `select_related` or `prefetch_related` turns one page load into hundreds of SQL queries.
- **Leaving `DEBUG=True` in production.** This leaks settings, source paths, and secrets in error pages.
- **Hardcoding secrets in `settings.py`.** Use environment variables from day one.
- **Writing fat views.** Business logic belongs on the model (or in a service module), not crammed into view functions.
- **Mixing project and app responsibilities.** Apps should be reusable; project-level concerns (settings, root URLs) stay in the project.

## Time estimate

| Part | Chapters | Approx. hours |
|------|----------|---------------|
| Part 1 — Foundations | ch01 – ch02 | 4 – 6 |
| Part 2 — Core development | ch03 – ch06 | 14 – 20 |
| Part 3 — Built-in features | ch07 – ch10 | 10 – 14 |
| Part 4 — Advanced & production | ch11 – ch14 | 10 – 14 |
| **Total** | **ch01 – ch14** | **~ 38 – 54 hours** |

Adjust based on your background — prior Python and SQL experience can cut Parts 1–2 in half.

## Related courses in CodeShelf

| Course | Connection |
|--------|------------|
| [Python](../python/ch00-course-overview.md) | Prerequisite language — functions, OOP, and decorators are used throughout |
| [Django REST Framework](../drf/ch00-course-overview.md) | The natural next step — build JSON APIs on top of what you learn here |
| [JavaScript](../javascript/ch00-course-overview.md) | Useful for adding interactivity to Django templates |
| [React](../react/ch00-course-overview.md) | Pair a Django/DRF backend with a React frontend for a modern full-stack app |

## Exercises

1. Install Python 3.10+ and confirm `python --version` works.
2. Create a virtual environment named `.venv` and activate it.
3. Run the **Quick start** snippet above and view the Django welcome page in your browser.
4. Open the Django shell (`python manage.py shell`) and import `django` — print `django.get_version()`.
5. Skim the chapter list and mark the topics you already know vs. the ones you want to focus on.

> **Tip:** Use the sidebar search (`Ctrl + K`) to jump to topics like "ORM", "migrations", or "class-based views" at any time.

> **Key takeaway:** This course is designed to be read in order, but every chapter is self-contained enough to use as a reference later. Bookmark [Chapter 3 — Models & ORM](./ch03-models-orm.md) and [Chapter 13 — Best Practices](./ch13-best-practices.md) — you will return to them often.

## Next chapter

Continue to [Chapter 1 — Django Introduction](./ch01-django-introduction.md) to understand the MTV architecture and the full request/response lifecycle before you write any code.
