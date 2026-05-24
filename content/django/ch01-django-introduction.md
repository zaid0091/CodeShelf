---
title: Django Introduction
description: Django history, MTV architecture, batteries-included design, and when to use Django
order: 1
tags: [django, mtv, introduction]
---

# Chapter 1: Django Introduction

> **Welcome to Django!**
> In this chapter you will learn what Django is, how it organizes web applications, and why teams choose it for production sites. You already know Python from the CodeShelf Python course — Django is where that knowledge meets the web.

---

## Table of Contents

1. [What is Django?](#what-is-django)
2. [History of Django](#history-of-django)
3. [Why Use Django?](#why-use-django)
4. [MTV Architecture Explained](#mtv-architecture-explained)
5. [Request and Response Cycle](#request-and-response-cycle)
6. [Middleware Overview](#middleware-overview)
7. [WSGI and ASGI](#wsgi-and-asgi)
8. [Django vs Other Frameworks](#django-vs-other-frameworks)
9. [Project vs Application](#project-vs-application)
10. [Batteries Included](#batteries-included)
11. [Django Design Philosophy](#django-design-philosophy)
12. [When to Choose Django](#when-to-choose-django)
13. [When Not to Choose Django](#when-not-to-choose-django)
14. [Hello Django Preview](#hello-django-preview)
15. [Django Version and Docs](#django-version-and-docs)
16. [Learning Path in This Course](#learning-path-in-this-course)
17. [Best Practices](#best-practices)
18. [Common Mistakes](#common-mistakes)
19. [Interview Points](#interview-points)
20. [Exercises](#exercises)
21. [Chapter Summary](#chapter-summary)

---
## What is Django?

> **In this section:** You will understand the Django web framework clearly enough to explain it in an interview and use it in a real project.

> **Definition:** **Django** is a free, open-source **web framework** written in Python. A framework gives you structure, tools, and conventions so you do not rebuild routing, database access, forms, and security from scratch on every project.

Think of building a house. You *could* cut every board and forge every nail yourself (raw Python + HTTP). Django is more like a **prefab kit with an architect's blueprint**: walls, plumbing, and electrical standards are already designed; you customize rooms and paint.

Django handles:

- **URL routing** — map `/blog/5/` to Python code

- **Database layer (ORM)** — Python classes instead of hand-written SQL for most work

- **Templates** — HTML with safe placeholders

- **Forms** — validation and HTML generation

- **Authentication** — users, sessions, permissions

- **Admin interface** — automatic management UI for your data

You write **your** business logic; Django handles repetitive web plumbing.

---

## History of Django

Understanding Django's origin explains its opinions (batteries included, admin-first, newsroom speed).

### The timeline

```text
📅 2003–2004
   └── Web developers at the Lawrence Journal-World newspaper need to build
       many content sites quickly (election results, sports, events).

📅 2005
   └── Django is open-sourced, named after jazz guitarist Django Reinhardt.
       Creators: Adrian Holovaty and Simon Willison (with community growth).

📅 2008
   └── Django 1.0 — API stability promise for production users.

📅 2013+
   └── Custom user models, class-based views mature, mobile/API era.

📅 2020s
   └── Async support (ASGI), modern template features, continued LTS releases.
```

### Who uses Django today?

| Company / project | Why Django fits |
|-------------------|-----------------|
| Instagram (early stack) | Rapid iteration at scale |
| Mozilla support tools | Admin + auth + ORM |
| Pinterest (parts) | Content and user data |
| Disqus, Eventbrite | High-traffic web platforms |

Django is **mature** — bugs are found and fixed; patterns are documented; hiring managers recognize it.

---

## Why Use Django?

| Advantage | What it means for you |
|-----------|------------------------|
| **Batteries included** | Auth, sessions, admin, ORM, forms — no hunting for 10 libraries on day one |
| **Security by default** | CSRF middleware, XSS escaping in templates, ORM parameterization |
| **Admin for free** | Staff can manage content without you building CRUD pages first |
| **Strong documentation** | Official docs are among the best in open source |
| **Ecosystem** | Packages for REST (DRF), CMS, payments, etc. |
| **Conventions** | New teammates recognize `settings.py`, `urls.py`, `models.py` |

### Speed of development

A blog with posts, users, and an admin panel is realistically **hours**, not weeks, once you know the basics. That speed is why startups and internal tools teams love Django.

### When speed matters less

If you only need a tiny JSON API with no HTML and no admin, a micro-framework might feel lighter — but many teams still choose Django + Django REST Framework for one codebase.

---

## MTV Architecture Explained

Django advertises **MTV**: **Model**, **Template**, **View**. It is analogous to the older **MVC** (Model–View–Controller) pattern from other frameworks.

| MTV layer | Responsibility | MVC analogy |
|-----------|----------------|-------------|
| **Model** | Data structure, database tables, business rules | Model |
| **Template** | HTML presentation (what the user sees) | View |
| **View** | Python function/class: process request, talk to models, pick template | Controller |

> **Naming confusion:** In Django, the word **"view"** means **controller logic**, not "the HTML page." The template is the visual view.

### Flow diagram

```text
     Browser
        │
        ▼ HTTP GET /blog/
   ┌────────────┐
   │  URLconf   │  urls.py — which view handles this path?
   └─────┬──────┘
         ▼
   ┌────────────┐
   │   View     │  views.py — get data, decide response
   └─────┬──────┘
         │ queries
         ▼
   ┌────────────┐
   │   Model    │  models.py — Post, User, etc.
   └─────┬──────┘
         │ rows
         ▼
   ┌────────────┐
   │ Template   │  post_list.html — render HTML
   └─────┬──────┘
         ▼
     HTTP Response (HTML)
```

We cover each layer in depth in later chapters: [Models](./ch03-models-orm.md), [Views & URLs](./ch04-views-urls.md), [Templates](./ch05-templates.md).

---

## Request and Response Cycle

Every page load follows the same pipeline.

### Step-by-step: user visits `/blog/`

1. **Browser** sends `GET /blog/` to the server.
2. **WSGI/ASGI server** (e.g. Gunicorn in production) hands the request to Django.
3. **Middleware** runs (security, sessions, CSRF setup, authentication).
4. **URL resolver** reads `ROOT_URLCONF`, matches `path("blog/", include("blog.urls"))`, then app routes.
5. **View** `post_list(request)` runs — often queries `Post.objects.filter(published=True)`.
6. **Template** renders with context `{"posts": posts}`.
7. **HttpResponse** returns HTML; middleware wraps response; browser displays page.

```python
# Conceptual view — full setup in Chapter 2
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, "blog/post_list.html", {"posts": posts})
```

> **Definition:** An **HttpRequest** object carries method, headers, GET/POST data, user, and session. An **HttpResponse** carries status code, headers, and body (HTML, JSON, redirect).

---

## Middleware Overview

> **Definition:** **Middleware** is a chain of hooks that process every request **before** the view and every response **after** the view.

```python
# Default middleware (simplified) — settings.py
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
```

| Middleware | Role |
|------------|------|
| Security | HTTPS redirects, security headers |
| Session | Loads/saves session data |
| CSRF | Validates tokens on unsafe methods |
| Authentication | Attaches `request.user` |

Order matters: sessions must exist before auth can load the user from the session.

---

## WSGI and ASGI

Python web apps speak a standard interface to servers:

| Interface | Full name | Typical use |
|-----------|-----------|-------------|
| **WSGI** | Web Server Gateway Interface | Traditional synchronous Django |
| **ASGI** | Asynchronous Server Gateway Interface | WebSockets, async views, Channels |

```python
# mysite/wsgi.py — production entry point
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
application = get_wsgi_application()
```

In development, `python manage.py runserver` uses WSGI internally. In production, **Gunicorn** or **uWSGI** calls `application`. See [Deployment](./ch12-deployment-basics.md).

---

## Django vs Other Frameworks

| Framework | Strengths | Tradeoffs |
|-----------|-----------|-----------|
| **Django** | Full-stack, ORM, admin, auth | More structure; heavier for tiny APIs |
| **Flask** | Minimal, flexible | You assemble auth, admin, ORM yourself |
| **FastAPI** | Async APIs, OpenAPI docs | Less built-in for server-rendered HTML sites |
| **Django REST Framework** | REST on top of Django | API-focused; still uses Django core |

**Choose Django when:** you want a relational database, HTML pages, user accounts, and fast internal admin tools in one project.

**Consider alternatives when:** you only need a stateless JSON microservice and will never use templates or admin (still, many teams use Django + DRF anyway).

---

## Project vs Application

Django splits work into two container types:

```text
bookstore/                 ← PROJECT (one per website)
├── manage.py
├── bookstore/
│   ├── settings.py        ← configuration for entire site
│   ├── urls.py            ← root URL routing
│   └── wsgi.py
├── catalog/               ← APP (feature module)
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── orders/                ← APP (another feature)
    └── ...
```

| Term | Meaning | Analogy |
|------|---------|---------|
| **Project** | Entire website configuration | The shopping mall building |
| **App** | Reusable feature module | One store inside the mall |

**Rules of thumb:**
- One **project** per deployed site (usually).
- Multiple **apps** per project: `blog`, `accounts`, `shop`.
- Apps can be reused across projects if you design them generically.

Full creation steps: [Chapter 2](./ch02-setup-project-structure.md).

---

## Batteries Included

`django.contrib` ships many subsystems:

| Package | Purpose |
|---------|---------|
| `auth` | Users, groups, permissions |
| `admin` | Auto CRUD UI |
| `sessions` | Session storage |
| `messages` | One-time flash messages |
| `staticfiles` | CSS/JS collection |
| `contenttypes` | Generic relations |
| `postgres` | PostgreSQL-specific fields |

You enable them in `INSTALLED_APPS` in `settings.py`. You do not have to use all of them, but they are there when you need them.

---

## Django Design Philosophy

| Principle | Meaning in practice |
|-----------|---------------------|
| **DRY** | Don't Repeat Yourself — one model definition drives DB, forms, admin |
| **Explicit is better than implicit** | URL patterns are visible in `urls.py` |
| **Loose coupling** | Apps should work independently where possible |
| **Fast iteration** | Admin + ORM reduce time to working prototype |

Django is **opinionated** — it rewards following conventions. Fighting every convention (e.g. putting all code in one file) slows you down.

---

## When to Choose Django

**Strong fit:**
- Content sites, blogs, documentation portals
- SaaS dashboards with accounts and permissions
- Internal tools (inventory, support tickets)
- CRUD-heavy applications
- Teams that want conventions and built-in admin

**Real example:** A startup building a project-management tool needs users, teams, tasks, and a staff admin to fix data. Django gives auth + admin on week one.

---

## When Not to Choose Django

**Consider other tools when:**
- You need extreme real-time (games, collaborative editors) — may add Django Channels or another stack
- You only expose a tiny stateless API and hate monoliths — FastAPI is popular
- Your team is 100% JavaScript and wants one language on server and client — Node ecosystem

**Note:** "Django is slow" is usually **misconfigured database queries**, not the framework itself. Optimization is covered in [Best Practices](./ch13-best-practices.md).

---

## Hello Django Preview

Here is the smallest useful slice — you will build this hands-on in Chapter 2.

```python
# blog/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, Django!</h1>")
```

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
]
```

Visit `http://127.0.0.1:8000/blog/` after `runserver` — you should see the greeting.

---

## Django Version and Docs

Always check your installed version:

```bash
python -m django --version
```

| Resource | URL pattern |
|----------|-------------|
| Official docs | https://docs.djangoproject.com/ |
| Tutorial | "Writing your first Django app" in docs |
| Release notes | Read before upgrading major versions |

This course targets **Django 5.x** patterns. Older tutorials may use deprecated APIs — when in doubt, check the docs for your version.

---

## Learning Path in This Course

| Chapter | Topic |
|---------|-------|
| 1 | Introduction (you are here) |
| 2 | Setup & project structure |
| 3 | Models & ORM |
| 4 | Views & URLs |
| 5 | Templates |
| 6 | Forms |
| 7 | Admin |
| 8 | Authentication |
| 9 | Migrations |
| 10 | Static & media |
| 11 | Class-based views |
| 12 | Deployment |
| 13 | Best practices |
| 14 | Interview prep |

**Prerequisite:** CodeShelf Python course (functions, classes, modules, virtual environments).

---

## Best Practices

From day one, adopt habits that scale:

1. **Use a virtual environment** per project — never install Django globally.
2. **Pin dependencies** in `requirements.txt`.
3. **One app per feature area** — not one giant `models.py` for everything.
4. **Use named URLs** — `reverse("post-detail", kwargs={"pk": 1})` not hard-coded `/blog/1/`.
5. **Keep `SECRET_KEY` out of git** — use environment variables in production.
6. **Read error pages in development** — Django's debug page is a teaching tool.

---

## Common Mistakes

Many beginners hit the same walls. Learn from these early.

| Mistake | What goes wrong | Fix |
|---------|-----------------|-----|
| Confusing MTV with MVC names | Thinking Django 'view' is HTML | Remember: View = Python logic; Template = HTML |
| One giant app for everything | Unmaintainable codebase | Split into blog, accounts, shop apps |
| Skipping virtualenv | Dependency conflicts between projects | python -m venv .venv always |
| Disabling security in prod | DEBUG=True leaks secrets | DEBUG=False, ALLOWED_HOSTS set |
| Not reading tracebacks | Random trial-and-error fixes | Start at the bottom of the traceback |

---

## Interview Points

**Q: What is Django?** — High-level Python web framework with ORM, templates, forms, auth, admin.

**Q: Explain MTV.** — Model = data; Template = presentation; View = request handler (like MVC controller).

**Q: Project vs app?** — Project = site config; app = modular feature, reusable.

**Q: What is middleware?** — Global request/response processors (sessions, CSRF, auth).

**Q: WSGI vs ASGI?** — WSGI = sync standard; ASGI = async + WebSockets.

---

## Exercises

> Practice is how Django becomes muscle memory. Complete these after reading the chapter.

### Exercise 1.1: Explore Django documentation

Open the official Django documentation. List three built-in `django.contrib` applications and one sentence describing each.

<details>
<summary>Click to reveal solution for Exercise 1.1</summary>

Example answers:
- **auth** — user accounts, groups, permissions
- **admin** — automatic CRUD interface for models
- **sessions** — stores session data across requests

</details>

---

### Exercise 1.2: Draw the MTV flow

On paper or in a text file, draw the path from browser `GET /posts/` to HTML response. Label URLconf, view, model, template, and database.

> **Hint:** Start at the browser and end at the HTTP response.

<details>
<summary>Click to reveal solution for Exercise 1.2</summary>

Browser → URLconf matches `/posts/` → view `post_list` → ORM query on Post model → database returns rows → view passes `posts` to template → template renders HTML → HttpResponse to browser.

</details>

---

### Exercise 1.3: Compare frameworks

Write one paragraph comparing Django to Flask for a team building a membership site with admin tools.

<details>
<summary>Click to reveal solution for Exercise 1.3</summary>

Django includes auth, admin, and ORM out of the box, which fits a membership site needing staff dashboards. Flask is lighter but requires choosing and integrating extensions for users and admin, increasing initial setup time. For CRUD-heavy membership sites, Django's conventions often deliver faster MVP delivery.

</details>

---

### Exercise 1.4: Install Django

Create a virtual environment, install Django, and print the version.

<details>
<summary>Click to reveal solution for Exercise 1.4</summary>

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate
pip install "django>=5.0,<6.0"
python -m django --version
```



</details>

---
## Chapter Summary

Excellent work completing Chapter 1. Here is what you learned:

- ### Core ideas
- - Django is a **batteries-included** Python web framework.
- - **MTV**: Models (data), Templates (HTML), Views (logic).
- - **Project** = whole site; **App** = feature module.
- - Requests pass through **middleware**, **URLconf**, **view**, optionally **ORM** and **templates**.
- - Use Django for CRUD-heavy, user-facing, admin-backed applications.

### Key rules to remember

```
✅ Use virtual environments and pin Django in requirements.txt
✅ Split features into apps
✅ Learn MTV before fighting conventions
❌ Do not confuse Django View with HTML page
❌ Do not run production with DEBUG=True
```

---

## Next Chapter

You are ready to install Django and create your first project.

**➡️ [Next Chapter →](./ch02-setup-project-structure.md)**

---

*Chapter 1 of the Complete Django Guide | [Report an issue](https://github.com/zaid0091/CodeShelf/issues)*

---

## Extended Study Guide: Django Introduction

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

## Extended Study Guide: Chapter 1

> Use this section for review, interviews, and spaced repetition after completing **Django Introduction**.

### Frequently Asked Questions

**Q: Is Django only for websites?**

Django is primarily for web applications (HTML + APIs). Many teams pair it with Django REST Framework for JSON APIs and separate frontends.

**Q: Can I use Django if I only know basic Python?**

Yes, if you completed functions, classes, modules, and virtual environments in the CodeShelf Python course. This Django course builds on that foundation.

**Q: What is the difference between Django and Django REST Framework?**

Django is the full web framework. DRF is a library that adds REST API tools (serializers, API views) on top of Django.

**Q: Why MTV instead of MVC?**

Historical naming. Django's View is the controller-like logic; Template is the presentation. The pattern is the same idea as MVC.

**Q: What runs first on each request?**

Middleware runs before URL resolution. The view runs after a URL match. Middleware runs again on the response way out.

**Q: Is Django synchronous or asynchronous?**

Django supports both. Traditional views are sync; ASGI and async views exist for modern workloads.

**Q: What database does Django use by default?**

SQLite for new projects in development. Production typically uses PostgreSQL.

**Q: Do I need to know SQL?**

Helpful but not required to start. The ORM covers most needs. Learn SQL for complex reporting and optimization.

**Q: What is the admin used for?**

Internal staff tools: content moderation, support, data fixes. Not usually shown to public users.

**Q: How does Django help with security?**

CSRF middleware, XSS template escaping, ORM parameterization, password hashing, and security middleware headers.


### Step-by-Step Walkthrough

1. Read the chapter introduction and MTV diagram.
2. Sketch the request cycle on paper without looking.
3. List three sites or products that could use Django and why.
4. Install Django in a fresh virtual environment.
5. Browse docs.djangoproject.com intro pages for 15 minutes.
6. Write one paragraph: when you would choose Django vs Flask for a project.

### Additional Code Patterns

#### Pattern 1.1

```python
# Minimal view (preview)
from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello')
```

### Review checklist

```text
[ ] I can explain the main concepts without notes
[ ] I typed the code examples myself
[ ] I completed all exercises
[ ] I fixed at least one error using the traceback
[ ] I read the linked official Django documentation
```
