---
title: Setup and Project Structure
description: Installing Django, creating projects and apps, settings.py, and manage.py
order: 2
tags: [django, setup, project]
---

# Chapter 2: Setup and Project Structure

> **In this chapter you will install Django, create a project and app, and run your first server.**

---

## Table of Contents

1. [Installation and Virtual Environments](#installation-and-virtual-environments)
2. [Creating Your First Project](#creating-your-first-project)
3. [Understanding manage.py](#understanding-manage.py)
4. [Creating and Registering Apps](#creating-and-registering-apps)
5. [settings.py Deep Dive](#settings.py-deep-dive)
6. [Wiring URLs: Project and App](#wiring-urls:-project-and-app)
7. [First Migration and Database](#first-migration-and-database)
8. [Superuser and Admin Preview](#superuser-and-admin-preview)
9. [Recommended Project Layout](#recommended-project-layout)
10. [Environment Variables and Secrets](#environment-variables-and-secrets)
11. [Reading Django Error Pages](#reading-django-error-pages)
12. [Chapter 2 Setup Checklist](#chapter-2-setup-checklist)
13. [Best Practices](#best-practices)
14. [Common Mistakes](#common-mistakes)
15. [Interview Points](#interview-points)
16. [Exercises](#exercises)
17. [Chapter Summary](#chapter-summary)

---
## Installation and Virtual Environments

> **Definition:** A **virtual environment** is an isolated Python environment for one project. Django and its dependencies install there without conflicting with other projects.

You learned virtual environments in the CodeShelf Python course. Django projects **always** use one.

### Windows (PowerShell)

```bash
cd D:\projects\myblog
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install "django>=5.0,<6.0"
python -m django --version
```

### macOS / Linux

```bash
cd ~/projects/myblog
python3 -m venv .venv
source .venv/bin/activate
pip install "django>=5.0,<6.0"
django-admin --version
```

### requirements.txt

```text
django>=5.0,<6.0
```

Commit `requirements.txt` to git. Teammates run `pip install -r requirements.txt` for identical versions.

| Check | Command |
|-------|---------|
| Python version | `python --version` (3.10+ recommended) |
| Django installed | `python -m django --version` |
| Pip list | `pip list` |

### Why this matters

Understanding **Installation and Virtual Environments** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Installation and Virtual Environments** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Creating Your First Project

`django-admin` is Django's command-line utility for administrative tasks.

```bash
django-admin startproject mysite
cd mysite
```

### What `startproject` creates

```text
mysite/
├── manage.py
└── mysite/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

| File | Purpose |
|------|---------|
| `manage.py` | CLI entry: runserver, migrate, shell, test |
| `settings.py` | Database, installed apps, middleware, templates |
| `urls.py` | Root URL routing |
| `wsgi.py` | Production server entry point |
| `asgi.py` | Async / Channels entry point |

### First run

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` — you should see the Django welcome rocket page.

```bash
python manage.py runserver 8080
```

Runs on port 8080 instead of 8000.

### Why this matters

Understanding **Creating Your First Project** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Creating Your First Project** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Understanding manage.py

`manage.py` sets `DJANGO_SETTINGS_MODULE` and delegates to Django's command runner.

```python
# manage.py (simplified idea)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
execute_from_command_line(sys.argv)
```

### Essential commands (learn these first)

| Command | What it does |
|---------|----------------|
| `runserver` | Development HTTP server (never for production) |
| `migrate` | Apply database migrations |
| `makemigrations` | Create migration files from model changes |
| `createsuperuser` | Create admin login |
| `shell` | Python REPL with Django loaded |
| `test` | Run test suite |
| `startapp NAME` | Create a new app |
| `collectstatic` | Gather static files for production |

### Example workflow

```bash
python manage.py startapp blog
# edit models.py
python manage.py makemigrations blog
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Why this matters

Understanding **Understanding manage.py** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Understanding manage.py** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Creating and Registering Apps

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
└── views.py
```

Create `blog/urls.py` yourself (not generated by default):

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog-index"),
]
```

Register in `settings.py`:

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

> **Rule:** If the app is not in `INSTALLED_APPS`, Django ignores its models, templates, and static files.

### Why this matters

Understanding **Creating and Registering Apps** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Creating and Registering Apps** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## settings.py Deep Dive

`settings.py` is the control center of your project.

### Critical settings

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-change-me"  # use env var in production
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [...]
MIDDLEWARE = [...]
ROOT_URLCONF = "mysite.urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

| Setting | Development | Production |
|---------|-------------|------------|
| `DEBUG` | `True` | **`False`** |
| `ALLOWED_HOSTS` | `[]` ok locally | `["yourdomain.com"]` |
| `SECRET_KEY` | dev key | long random env var |
| `DATABASES` | SQLite fine | PostgreSQL typical |

### TEMPLATES and static (preview)

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": [...]},
    },
]

STATIC_URL = "static/"
```

Full template/static chapters: [ch05](./ch05-templates.md), [ch10](./ch10-static-media-files.md).

### Why this matters

Understanding **settings.py Deep Dive** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **settings.py Deep Dive** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Wiring URLs: Project and App

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
# blog/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Blog home</h1>")
```

Visit `http://127.0.0.1:8000/blog/` — not `/` unless you add a root route.

### Named URLs

```python
path("", views.index, name="blog-index"),
```

Use `reverse("blog-index")` in Python and `{% url 'blog-index' %}` in templates later.

### Why this matters

Understanding **Wiring URLs: Project and App** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Wiring URLs: Project and App** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## First Migration and Database

```bash
python manage.py migrate
```

Creates tables for built-in apps: auth, admin, sessions, contenttypes.

```bash
python manage.py showmigrations
```

`[X]` means applied; `[ ]` means pending.

### SQLite file

After migrate, `db.sqlite3` appears in the project root. It is your database file in development.

> **Production:** Use PostgreSQL or MySQL — not SQLite for concurrent write-heavy sites.

### Why this matters

Understanding **First Migration and Database** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **First Migration and Database** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Superuser and Admin Preview

```bash
python manage.py createsuperuser
```

Follow prompts for username, email, password.

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin/` and log in.

Full admin customization: [Chapter 7](./ch07-admin-panel.md).

### Why this matters

Understanding **Superuser and Admin Preview** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Superuser and Admin Preview** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Recommended Project Layout

Small tutorials use flat layout. Real projects often grow:

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
├── media/
├── manage.py
└── requirements.txt
```

| Pattern | Benefit |
|---------|---------|
| `config/` instead of duplicate name | Clear separation |
| Split settings | Safe production defaults |
| `apps/` folder | Many apps stay organized |

Deployment split settings: [Chapter 12](./ch12-deployment-basics.md).

### Why this matters

Understanding **Recommended Project Layout** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Recommended Project Layout** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Environment Variables and Secrets

Never commit production secrets.

```python
import os

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-key")
DEBUG = os.environ.get("DEBUG", "True") == "True"
```

Use `python-dotenv` or `django-environ` locally:

```text
# .env (gitignored)
SECRET_KEY=your-long-random-key
DEBUG=True
```

```python
# .gitignore
.env
db.sqlite3
__pycache__/
*.pyc
.venv/
```

### Why this matters

Understanding **Environment Variables and Secrets** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Environment Variables and Secrets** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Reading Django Error Pages

With `DEBUG=True`, Django shows a detailed yellow error page:

| Section | Use it to |
|---------|-----------|
| Exception type | Know error class (DoesNotExist, etc.) |
| Traceback | Find exact line in your code |
| Request info | See URL, method, POST data |
| Settings | Confirm which settings module loaded |

**In production** (`DEBUG=False`), users see a generic 500 page — you log errors server-side.

Common first errors:
- `TemplateDoesNotExist` — wrong template path
- `NoReverseMatch` — URL name typo
- `AppRegistryNotReady` — model import order issue

### Why this matters

Understanding **Reading Django Error Pages** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Reading Django Error Pages** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Chapter 2 Setup Checklist

Before moving to models, confirm:

```text
[ ] Virtual environment active
[ ] Django installed and version printed
[ ] startproject completed
[ ] startapp blog completed
[ ] blog in INSTALLED_APPS
[ ] blog/urls.py created and included
[ ] View returns HttpResponse
[ ] migrate run successfully
[ ] createsuperuser works
[ ] /admin/ login works
```

### Why this matters

Understanding **Chapter 2 Setup Checklist** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Chapter 2 Setup Checklist** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Best Practices

Apply conventions from this chapter consistently.

See also [Best Practices](./ch13-best-practices.md) for project-wide standards.

- Read official docs for your Django version
- Keep views thin and models focused
- Use named URLs everywhere
- Run `python manage.py check` before commits

---

## Common Mistakes

Many beginners hit the same walls. Learn from these early.

| Mistake | What goes wrong | Fix |
|---------|-----------------|-----|
| Forgetting INSTALLED_APPS | Models/templates ignored | Add app to INSTALLED_APPS |
| Wrong urls include path | 404 on app URLs | Match path prefix and include() |
| Committing SECRET_KEY | Security breach if repo public | Use environment variables |
| Using runserver in production | Insecure, not scalable | Use Gunicorn + nginx |
| No virtual environment | Package conflicts | venv per project |

---

## Interview Points

**Q: What does manage.py do?** — Sets DJANGO_SETTINGS_MODULE and runs management commands.

**Q: Project vs app?** — Project configures site; app is reusable feature module.

**Q: Purpose of migrate?** — Applies migration files to sync database schema.

---

## Exercises

> Practice is how Django becomes muscle memory. Complete these after reading the chapter.

### Exercise 2.1: Create project and app

Create `mysite` and `blog` app; register app; add view at `/blog/`.

<details>
<summary>Click to reveal solution for Exercise 2.1</summary>

Follow chapter commands: startproject, startapp, INSTALLED_APPS, urls include, HttpResponse view.

</details>

---

### Exercise 2.2: Run migrations

Run migrate and createsuperuser; log into admin.

<details>
<summary>Click to reveal solution for Exercise 2.2</summary>

`python manage.py migrate` then `createsuperuser`, visit /admin/.

</details>

---

### Exercise 2.3: Explore shell

Open `manage.py shell` and import django; print version.

<details>
<summary>Click to reveal solution for Exercise 2.3</summary>

```python
import django
django.get_version()
```

</details>

---

### Exercise 2.4: Document settings

List five settings from settings.py and explain each.

<details>
<summary>Click to reveal solution for Exercise 2.4</summary>

DEBUG, SECRET_KEY, DATABASES, INSTALLED_APPS, ROOT_URLCONF, etc.

</details>

---
## Chapter Summary

Excellent work completing Chapter 2. Here is what you learned:

- Completed Chapter 2: Setup and Project Structure
- Reviewed core patterns and examples
- Practiced with exercises

### Key rules to remember

```
✅ Practice in a real project
✅ Use official docs
❌ Skip migrations
❌ Disable security middleware in production
```

---

## Next Chapter

Continue to the next chapter.

**➡️ [Next Chapter →](./ch03-models-orm.md)**

---

*Chapter 2 of the Complete Django Guide | [Report an issue](https://github.com/zaid0091/CodeShelf/issues)*

---

## Extended Study Guide: Setup and Project Structure

### Glossary

| Term | Definition |
|------|------------|
| Django | High-level Python web framework |
| MTV | Model-Template-View architecture |
| ORM | Object-Relational Mapper for database access |
| QuerySet | Lazy database query representation |
| Migration | Version-controlled schema change file |

### Self-check questions

1. Can you explain this chapter's main idea in two sentences?
2. Can you write the key code patterns from memory?
3. Can you debug one common error mentioned in Common Mistakes?

### Command reference

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py shell
python manage.py test
```
---

## Extended Study Guide: Chapter 2

> Use this section for review, interviews, and spaced repetition after completing **Setup and Project Structure**.

### Frequently Asked Questions

**Q: Why django-admin vs manage.py?**

django-admin works globally before a project exists. manage.py is project-specific and sets DJANGO_SETTINGS_MODULE.

**Q: What if I forget to activate the virtual environment?**

You may install packages globally or use the wrong Python. Always check `which python` or `Get-Command python`.

**Q: Can I rename the project folder?**

Yes, but update references in settings, wsgi.py, manage.py, and ROOT_URLCONF if the inner package name changes.

**Q: Why create blog/urls.py manually?**

startapp does not create urls.py by default. You add routing per app.

**Q: What is BASE_DIR?**

Path to project root (parent of settings package). Used for templates, static, database file paths.

**Q: When does db.sqlite3 appear?**

After running migrate the first time.

**Q: Can two apps have the same model name?**

Yes, in different apps. Tables are namespaced: blog_post vs shop_product.

**Q: What does python manage.py check do?**

Validates settings and model configuration without running the server.

**Q: Why is SECRET_KEY important?**

Signs sessions, CSRF tokens, and password reset tokens. Compromise means forge sessions.

**Q: What port does runserver use?**

8000 by default. Pass port as argument to change.


### Step-by-Step Walkthrough

1. Create folder myblog and `python -m venv .venv`.
2. Activate venv and `pip install django`.
3. `django-admin startproject config .` (dot = current directory layout) OR classic startproject.
4. `python manage.py startapp blog`.
5. Add blog to INSTALLED_APPS.
6. Create blog/views.py index view and blog/urls.py.
7. Include blog.urls in project urls.py at path blog/.
8. runserver and visit /blog/.
9. migrate and createsuperuser; visit /admin/.

### Additional Code Patterns

#### Pattern 2.1

```python
INSTALLED_APPS = [..., 'blog']
```

#### Pattern 2.2

```python
path('blog/', include('blog.urls'))
```

### Review checklist

```text
[ ] I can explain the main concepts without notes
[ ] I typed the code examples myself
[ ] I completed all exercises
[ ] I fixed at least one error using the traceback
[ ] I read the linked official Django documentation
```
