---
title: Django Course Overview
description: Complete Django course — from MTV basics to deployment and interview prep
order: 0
tags: [django, overview]
---

# The Complete Django Course

Build production-ready web applications with Django — models, views, templates, auth, and deployment.

## Course structure

### Part 1: Foundations

| Chapter | Topic |
|---------|--------|
| [Django Introduction](./ch01-django-introduction.md) | What Django is, MTV, batteries-included philosophy |
| [Setup & Project Structure](./ch02-setup-project-structure.md) | Install, startproject, startapp, settings |

### Part 2: Core Django

| Chapter | Topic |
|---------|--------|
| [Models & ORM](./ch03-models-orm.md) | Fields, relationships, QuerySets, managers |
| [Views & URLs](./ch04-views-urls.md) | Function views, URLconf, request/response |
| [Templates](./ch05-templates.md) | Django template language, inheritance, context |
| [Forms](./ch06-forms.md) | Form class, ModelForm, validation, CSRF |

### Part 3: Built-in Features

| Chapter | Topic |
|---------|--------|
| [Admin Panel](./ch07-admin-panel.md) | ModelAdmin, list filters, inlines |
| [Authentication](./ch08-authentication.md) | User model, login, logout, permissions |
| [Migrations](./ch09-migrations.md) | makemigrations, migrate, squashing |
| [Static & Media Files](./ch10-static-media-files.md) | STATIC_*, MEDIA_*, collectstatic |

### Part 4: Advanced & Production

| Chapter | Topic |
|---------|--------|
| [Class-Based Views](./ch11-class-based-views.md) | ListView, DetailView, mixins |
| [Deployment Basics](./ch12-deployment-basics.md) | Gunicorn, WSGI, env settings |
| [Best Practices](./ch13-best-practices.md) | Project layout, security, performance |
| [Interview Preparation](./ch14-interview-prep.md) | Common Django interview Q&A |

## Prerequisites

| Requirement | Notes |
|-------------|--------|
| Python 3.10+ | See [Python course](../python/ch00-course-overview.md) |
| Basic HTML/CSS | Helpful for templates |
| SQL concepts | Helpful for ORM chapter |
| Command line | Run manage.py commands |

## Recommended learning path

```text
ch01 Introduction → ch02 Setup → ch03 Models → ch04 Views/URLs
       ↓
ch05 Templates → ch06 Forms → ch07 Admin → ch08 Auth
       ↓
ch09 Migrations → ch10 Static/Media → ch11 CBVs → ch12 Deployment
       ↓
ch13 Best Practices → ch14 Interview Prep
```

## What you will build

Hands-on exercises across chapters culminate in skills to build a blog or CRUD app:

- Define models and run migrations
- Wire URLs to views and render templates
- Handle forms and user authentication
- Customize the admin and serve static files
- Deploy with a production WSGI server

## Key definitions

> **Definition — Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the **MTV** pattern (Model–Template–View).

> **Definition — ORM:** Object-Relational Mapper — lets you interact with the database using Python classes instead of raw SQL.

> **Definition — App vs Project:** A **project** is the whole website configuration; an **app** is a modular component (blog, users, shop) that can be reused across projects.

## Quick start preview

```bash
python -m venv .venv
source .venv/bin/activate
pip install django
django-admin startproject mysite
cd mysite
python manage.py startapp blog
python manage.py runserver
```

## Tools you will use

| Tool | Purpose |
|------|---------|
| `manage.py` | Run server, migrations, shell, tests |
| Django admin | Internal CRUD at `/admin/` |
| `django-debug-toolbar` | Query and template debugging (dev) |
| Gunicorn + nginx | Production serving ([Deployment](./ch12-deployment-basics.md)) |

## Related courses

After completing Django fundamentals, consider:

- [Python course](../python/ch00-course-overview.md) — language depth if needed
- [DRF course](../drf/ch00-course-overview.md) — REST APIs on top of Django

## Study tips

| Tip | Detail |
|-----|--------|
| Build a blog app | Follow each chapter and extend one project |
| Read error pages | Django debug page explains many mistakes when `DEBUG=True` |
| Use the shell | `python manage.py shell` to experiment with the ORM |
| Commit often | Track migrations and settings in git |

## Time estimate

| Part | Chapters | Approx. hours |
|------|----------|---------------|
| Part 1 — Foundations | ch01–ch02 | 4–6 |
| Part 2 — Core Django | ch03–ch06 | 12–16 |
| Part 3 — Built-in Features | ch07–ch10 | 8–12 |
| Part 4 — Advanced & Production | ch11–ch14 | 10–14 |

Building one complete blog alongside the course is the best way to retain concepts.

## Chapter navigation

Every chapter ends with **Exercises**, a **Summary**, and a **Next chapter** link. Internal links use relative paths such as `./ch03-models-orm.md` so the course works as standalone markdown files.

## Exercises

1. Confirm Python and pip work; skim the Python course if needed.
2. Install Django and run `django-admin --version`.
3. Map each chapter to topics you already know vs. need to learn.
4. Create a `django-practice/` folder for exercises throughout the course.

## Next chapter

Continue to [Django Introduction](./ch01-django-introduction.md).
