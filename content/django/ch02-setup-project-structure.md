---
title: Setup and Project Structure
description: Installing Django, creating projects and apps, settings.py, and manage.py
order: 2
tags: [django, setup, project]
---

# Chapter 2: Setup and Project Structure

## 2.1 Installation

Use a [virtual environment](../python/ch12-virtual-env-pip.md):

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install django
django-admin --version
```

Pin in `requirements.txt`:

```text
django>=5.0,<6.0
```

## 2.2 Creating a project

```bash
django-admin startproject mysite
cd mysite
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` — default welcome page appears.

## 2.3 Project layout

```text
mysite/
├── manage.py
├── mysite/
│   ├── __init__.py
│   ├── settings.py      # configuration
│   ├── urls.py          # root URL routing
│   ├── asgi.py          # async entry (optional)
│   └── wsgi.py          # production entry
└── db.sqlite3           # after migrate
```

| File | Role |
|------|------|
| `manage.py` | CLI for Django commands |
| `settings.py` | Database, apps, middleware, templates |
| `urls.py` | Root URL patterns |
| `wsgi.py` | WSGI application for servers |

## 2.4 Creating an app

```bash
python manage.py startapp blog
```

```text
blog/
├── __init__.py
├── admin.py
├── apps.py
├── migrations/
│   └── __init__.py
├── models.py
├── tests.py
├── views.py
└── urls.py   # create this file
```

Register the app in `settings.py`:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",  # your app
]
```

## 2.5 Key settings

```python
# mysite/settings.py
DEBUG = True
ALLOWED_HOSTS = []

SECRET_KEY = "change-me-in-production"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

| Setting | Purpose |
|---------|---------|
| `DEBUG` | Verbose errors — **False** in production |
| `SECRET_KEY` | Cryptographic signing |
| `DATABASES` | DB connection config |
| `INSTALLED_APPS` | Enabled Django apps |

## 2.6 Wiring app URLs

```python
# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
]
```

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog-index"),
]
```

## 2.7 First migration

```bash
python manage.py migrate
```

Creates auth, sessions, admin tables in SQLite.

## 2.8 Superuser and admin

```bash
python manage.py createsuperuser
python manage.py runserver
```

Visit `/admin/` and log in.

See [Admin Panel](./ch07-admin-panel.md).

## 2.9 manage.py commands reference

| Command | Purpose |
|---------|---------|
| `runserver` | Development server |
| `migrate` | Apply migrations |
| `makemigrations` | Create migration files |
| `shell` | Python shell with Django loaded |
| `test` | Run tests |
| `collectstatic` | Gather static files |

## 2.10 Recommended project layout (larger apps)

```text
mysite/
├── config/           # project settings (rename from mysite/)
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   └── blog/
├── templates/
├── static/
└── manage.py
```

Split settings for dev/prod in [Deployment](./ch12-deployment-basics.md).

## Exercises

1. Create project `mysite` and app `blog`; register the app.
2. Add a view returning "Blog home" and wire `/blog/` URL.
3. Run `migrate` and create a superuser.
4. Explore `python manage.py shell` and import `django`.

## Summary

`startproject` creates configuration; `startapp` creates feature modules. Register apps, include URLconfs, and use `manage.py` for all operations.

## Next chapter

Continue to [Models & ORM](./ch03-models-orm.md).
