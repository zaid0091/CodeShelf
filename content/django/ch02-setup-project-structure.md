---
title: Setup and Project Structure
description: Install Django, create a project and app, understand every file the scaffold generates, configure settings, run migrations, and serve your first page
order: 2
tags: [django, setup, project, structure, settings]
---

# Chapter 2 — Setup and Project Structure

> Install Django the right way, scaffold a project and app, and understand every file Django creates for you.
>
> **Difficulty:** Beginner &nbsp;·&nbsp; **Estimated time:** 35 – 45 min &nbsp;·&nbsp; **Prerequisites:** [Chapter 1 — Django Introduction](./ch01-django-introduction.md), Python 3.10+, basic command line

---

## Learning Outcome

By the end of this lesson, you will be able to:

- ✔ Create and activate a Python **virtual environment** on Windows, macOS, or Linux
- ✔ Install Django and verify the installed version
- ✔ Scaffold a project with `django-admin startproject` and an app with `manage.py startapp`
- ✔ Explain the purpose of `manage.py`, `settings.py`, `urls.py`, `wsgi.py`, and `asgi.py`
- ✔ Register an app in `INSTALLED_APPS` and serve a route from it
- ✔ Run the dev server, apply migrations, and create a superuser
- ✔ Recognize the **professional project layout** with `config/` and `apps/` folders
- ✔ Keep secrets out of source control using environment variables

---

## Visual Preview

In the next 30 minutes you will create this exact file tree:

```text
myblog/
├── .venv/                      ← virtual environment (not committed)
├── .env                        ← secrets (not committed)
├── .gitignore
├── requirements.txt
├── db.sqlite3                  ← created by `migrate`
├── manage.py                   ← Django CLI entry point
├── mysite/                     ← project package
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── blog/                       ← your first app
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── tests.py
    ├── urls.py                 ← you'll create this manually
    └── views.py
```

And here is what you'll see in the browser at the end:

```text
http://127.0.0.1:8000/blog/
  Hello from the blog app!

http://127.0.0.1:8000/admin/
  Django administration login page
```

---

## Core Concept

### Virtual environments — non-negotiable

> **Definition — Virtual environment:** An isolated Python installation tied to a single project, so its dependencies do not collide with other projects or your system Python.

Without one, installing Django for project A can break project B. Every professional Django project starts with a `.venv` folder.

### Project vs. app — the unit of organization

> **Definition — Project:** The whole deployable website. Holds `settings.py`, the root `urls.py`, and the WSGI/ASGI entry points.
>
> **Definition — App:** A self-contained, reusable feature module (e.g., `blog`, `accounts`, `payments`). A project can have many apps; one app can live in many projects.

You create projects with `django-admin startproject` and apps with `python manage.py startapp`.

### `settings.py` is the control center

`settings.py` defines **everything Django needs to know** about your project — installed apps, middleware, database, templates, static files, allowed hosts, secret key, and timezone. Read it once carefully; you will keep coming back to it.

### URL routing happens in two layers

1. The **project's** `urls.py` (`mysite/urls.py`) is the root — it should mostly `include()` app-level URL files.
2. Each **app** has its own `urls.py` that owns the routes for that app's features.

This two-layer split is what makes Django apps **portable**.

### Migrations keep your schema in sync

> **Definition — Migration:** A versioned, code-generated description of a schema change. `makemigrations` writes the file; `migrate` applies it to the database.

You will run `python manage.py migrate` at least once before the first time you start the server — to create Django's built-in tables (`auth_user`, `django_session`, …).

---

## Syntax

The four commands you will run for **every new Django project**:

```bash
python -m venv .venv               # 1. Create a virtual environment
django-admin startproject <name>   # 2. Scaffold the project
python manage.py startapp <name>   # 3. Create an app
python manage.py runserver         # 4. Start the dev server
```

The minimal `settings.py` snippet that activates a new app:

```python
INSTALLED_APPS = [
    # ... built-ins
    "blog",
]
```

The minimal pair of URL files that wires a view to a path:

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog-index"),
]
```

```python
# mysite/urls.py
from django.urls import path, include

urlpatterns = [
    path("blog/", include("blog.urls")),
]
```

---

## Live Code Playground

Below is the complete setup, top to bottom. Copy it into your terminal and follow along.

### 1. Create and enter the project folder

```bash
mkdir myblog && cd myblog
```

### 2. Create and activate a virtual environment

```bash
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Django

```bash
python -m pip install --upgrade pip
pip install "django>=5.0,<6.0"
python -m django --version
```

### 4. Scaffold the project (in the current folder)

```bash
django-admin startproject mysite .
```

> 💡 **Tip:** The trailing `.` keeps `manage.py` in your current folder instead of creating a nested `mysite/mysite/` layout.

### 5. Create your first app

```bash
python manage.py startapp blog
```

### 6. Register the app — `mysite/settings.py`

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",
]
```

### 7. Write the view — `blog/views.py`

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello from the blog app!</h1>")
```

### 8. Wire the URLs — `blog/urls.py` (create this file)

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog-index"),
]
```

### 9. Include the app URLs — `mysite/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
]
```

### 10. Run migrations and start the server

```bash
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/) — you should see **Hello from the blog app!**

---

## Step-by-Step Example

Let's break the setup into clear, testable steps so you can fix anything that goes wrong.

### Step 1 — Verify Python

```bash
python --version       # or: python3 --version
```

You need **Python 3.10 or newer**. If the command is missing, install Python from [python.org](https://www.python.org/) first.

### Step 2 — Make a project folder

```bash
mkdir myblog
cd myblog
```

### Step 3 — Create the virtual environment

```bash
python -m venv .venv
```

Your folder now contains a `.venv/` directory. **Never** commit it to git.

### Step 4 — Activate it

| OS | Command |
|---|---|
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (cmd) | `.venv\Scripts\activate.bat` |
| macOS / Linux | `source .venv/bin/activate` |

Your shell prompt should now show `(.venv)` at the front.

### Step 5 — Install Django

```bash
pip install "django>=5.0,<6.0"
```

Verify:

```bash
python -m django --version
# 5.x.x
```

### Step 6 — Scaffold the project

```bash
django-admin startproject mysite .
```

Django creates `manage.py` and `mysite/` with `settings.py`, `urls.py`, `asgi.py`, `wsgi.py`.

### Step 7 — Run the initial migrations

```bash
python manage.py migrate
```

This creates `db.sqlite3` and Django's built-in tables (users, sessions, etc.).

### Step 8 — Start the server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) — you should see Django's rocket.

### Step 9 — Create an app

```bash
python manage.py startapp blog
```

A new `blog/` folder appears with `views.py`, `models.py`, `admin.py`, and friends.

### Step 10 — Register the app

Add `"blog"` to `INSTALLED_APPS` in `mysite/settings.py`. **Without this, Django ignores the app entirely.**

### Step 11 — Write the first view and URL

Edit `blog/views.py`, create `blog/urls.py`, and include it from `mysite/urls.py` (see the Playground above).

### Step 12 — Create a superuser

```bash
python manage.py createsuperuser
```

Enter a username, email, and password. Then visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in.

### Step 13 — Lock down secrets

Create a `.gitignore`:

```gitignore
.venv/
.env
db.sqlite3
__pycache__/
*.pyc
```

Move `SECRET_KEY` and `DEBUG` to a `.env` file. You'll use a library like `python-decouple` or `django-environ` to read them in Chapter 12.

---

## Try It Yourself

> **Task:** Extend the project so it has **two apps** — `blog` and `accounts` — each serving its own page.
>
> - `/blog/` should render **"Welcome to the blog!"**
> - `/accounts/login/` should render **"Login page coming soon."**
>
> Both apps must be properly registered in `INSTALLED_APPS`, and each must own its own `urls.py`.

Hints:

1. Run `python manage.py startapp accounts` after the `blog` app.
2. Don't forget to add `"accounts"` to `INSTALLED_APPS`.
3. The project's root `urls.py` should `include()` both app URL files.
4. Use a named URL for each route (e.g., `name="accounts-login"`).

Test both URLs in the browser before checking the solution.

---

## Solution

<details>
<summary>Click to reveal the solution</summary>

### `mysite/settings.py`

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",
    "accounts",
]
```

### `blog/views.py`

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to the blog!</h1>")
```

### `blog/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog-index"),
]
```

### `accounts/views.py`

```python
from django.http import HttpResponse

def login_page(request):
    return HttpResponse("<h1>Login page coming soon.</h1>")
```

### `accounts/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="accounts-login"),
]
```

### `mysite/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("accounts/", include("accounts.urls")),
]
```

### Run it

```bash
python manage.py runserver
```

Visit:

- [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/) → **Welcome to the blog!**
- [http://127.0.0.1:8000/accounts/login/](http://127.0.0.1:8000/accounts/login/) → **Login page coming soon.**

**Why this works:** Each app owns its own `urls.py`. The project's root `urls.py` only routes path prefixes (`blog/` and `accounts/`) to the right app, keeping the apps independent and reusable.

</details>

---

## Key Notes & Tips

> 💡 **Tip:** Use the trailing `.` in `django-admin startproject mysite .` to avoid the dreaded `mysite/mysite/` double-nesting. It is the layout used by almost every professional Django project.

> 💡 **Tip:** Run `python manage.py migrate` **before** the first `runserver`. Otherwise the auth, session, and admin tables won't exist and login will fail.

> 💡 **Tip:** Pin your Django version in `requirements.txt` (e.g., `django>=5.0,<6.0`) so a future major release doesn't break your project on a fresh install.

> ⚠️ **Warning:** **Never** commit `.env`, `.venv/`, or `db.sqlite3` to git. Add them to `.gitignore` from day one.

> ⚠️ **Warning:** `python manage.py runserver` is a **development** server only. In production, use Gunicorn or Daphne behind Nginx with `DEBUG=False`.

> ⚠️ **Warning:** Always check that your prompt shows `(.venv)` before running `pip install` — otherwise you'll install Django globally and pollute your system Python.

---

## Common Mistakes

- ❌ **Forgetting to add the app to `INSTALLED_APPS`.** Django silently ignores it — models won't be detected, migrations won't be generated, templates may not load.
- ❌ **Skipping the virtual environment.** Sooner or later two projects need different Django versions and `pip` can no longer satisfy both.
- ❌ **Editing `settings.py` while the server is running and forgetting to restart.** Most files hot-reload; `settings.py` and `INSTALLED_APPS` changes sometimes don't.
- ❌ **Hardcoding `SECRET_KEY` in `settings.py` and pushing to GitHub.** GitHub scrapers detect it within minutes.
- ❌ **Running `runserver` without `migrate` first.** You'll see "no such table: auth_user" errors when accessing `/admin/`.
- ❌ **Naming the project and the app the same thing.** Python's import system will get confused and you'll waste an hour debugging.
- ❌ **Storing `db.sqlite3` in git.** Migrations are the source of truth — the database file is generated.

---

## Mini Quiz

**Q1.** Which command creates a Django **project** (not an app)?

- A) `python manage.py startapp mysite`
- B) `django-admin startproject mysite` ✔
- C) `pip install django mysite`
- D) `python -m django newproject mysite`

**Q2.** What does the trailing `.` do in `django-admin startproject mysite .`?

- A) It hides the project folder
- B) It creates the project in the **current** directory instead of a nested one ✔
- C) It runs the project immediately
- D) It activates the virtual environment

**Q3.** What happens if you forget to add an app to `INSTALLED_APPS`?

- A) Django raises an error at startup
- B) Templates load but models do not
- C) Django ignores the app entirely — models, migrations, and admin all stop working ✔
- D) Only the admin panel is affected

**Q4.** Which command applies pending migrations to the database?

- A) `python manage.py makemigrations`
- B) `python manage.py migrate` ✔
- C) `python manage.py syncdb`
- D) `python manage.py applymigrations`

**Q5.** Where should you store production secrets like `SECRET_KEY` and database passwords?

- A) Directly inside `settings.py`
- B) In a comment at the top of `manage.py`
- C) In environment variables (e.g., a `.env` file outside git) ✔
- D) Hardcoded inside views

---

## Real World Example

Professional Django projects rarely live in the default layout. They use a **split-settings** structure that separates dev, staging, and production:

```text
myproject/
├── config/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py          ← shared settings
│   │   ├── dev.py           ← imports base + dev overrides
│   │   └── prod.py          ← imports base + prod overrides
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/
│   ├── blog/
│   ├── accounts/
│   └── billing/
│
├── templates/                ← shared templates
├── static/                   ← shared static assets
├── media/                    ← user-uploaded files
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── .env.example
├── .gitignore
├── manage.py
└── README.md
```

**Why teams use this layout:**

| Pattern | Benefit |
|---------|---------|
| `config/` package | Clearly separates project-level wiring from feature apps |
| `apps/` folder | Keeps domain features in one place; easier to scan |
| Split settings | One `DEBUG=True` per environment — no more accidents |
| Split requirements | `pip install -r requirements/prod.txt` skips dev tools |
| `.env.example` | Documents required env vars without leaking real values |

You will work with this layout in Chapter 12 (Deployment) and Chapter 13 (Best Practices). For now, the default layout is enough — but knowing where you're heading helps every decision along the way.

---

## Summary

Today you learned:

- ✔ Every Django project starts inside a **virtual environment** — no exceptions.
- ✔ `django-admin startproject` scaffolds the project; `python manage.py startapp` scaffolds an app.
- ✔ Apps are **invisible** to Django until they appear in `INSTALLED_APPS`.
- ✔ `manage.py` is Django's command-line entry point — `runserver`, `migrate`, `createsuperuser`, `shell`, `startapp`, and more.
- ✔ Routing happens in two layers: the project's root `urls.py` `include()`s each app's `urls.py`.
- ✔ Migrations are the source of truth for your schema; run `migrate` before the first server start.
- ✔ Secrets belong in environment variables, **never** in `settings.py` or git.

### Key Takeaways

```text
✅ Use a virtual environment for every project
✅ Pin Django and key dependencies in requirements.txt
✅ Register every app in INSTALLED_APPS
✅ Keep each app's URLs in its own urls.py and include() them from the project
✅ Always run migrate before the first runserver
✅ Move secrets out of settings.py and add them to .gitignore
```

### Command Reference

```bash
python -m venv .venv                          # Create a virtual environment
source .venv/bin/activate                     # Activate (macOS / Linux)
.venv\Scripts\Activate.ps1                    # Activate (Windows PowerShell)

pip install "django>=5.0,<6.0"                # Install Django
python -m django --version                    # Verify Django version

django-admin startproject mysite .            # Scaffold a project
python manage.py startapp blog                # Create an app

python manage.py runserver                    # Start the dev server
python manage.py runserver 8080               # Use a custom port

python manage.py makemigrations               # Generate migration files
python manage.py migrate                      # Apply migrations
python manage.py showmigrations               # List migrations and their state

python manage.py createsuperuser              # Create an admin user
python manage.py shell                        # Open the Django shell
python manage.py collectstatic                # Gather static files for prod
python manage.py test                         # Run the test suite
```

### Glossary

| Term | Definition |
|------|------------|
| Virtual environment | Isolated Python install per project |
| Project | Whole Django site — settings + root URLs |
| App | Reusable feature module inside a project |
| `manage.py` | Django's command-line entry point |
| `settings.py` | Central configuration file |
| `INSTALLED_APPS` | List of apps Django actively loads |
| `urlpatterns` | List of URL → view mappings |
| Migration | Versioned description of a schema change |
| Superuser | Admin user with full permissions |
| `.env` | File holding environment-specific secrets |

---

## Next Lesson Navigation

| ← Previous Lesson | Next Lesson → |
|-------------------|---------------|
| [Django Introduction](./ch01-django-introduction.md) | [Models and ORM](./ch03-models-orm.md) |
