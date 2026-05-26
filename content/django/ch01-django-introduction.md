---
title: Django Introduction
description: Understand what Django is, the MTV architecture, the request/response lifecycle, middleware, and WSGI/ASGI — with a complete Hello Django walkthrough
order: 1
tags: [django, introduction, mtv, python, backend]
---

# Chapter 1 — Django Introduction

> Understand what Django is, how it processes a request from URL to HTML, and write your first working view.
>
> **Difficulty:** Beginner &nbsp;·&nbsp; **Estimated time:** 25 – 35 min &nbsp;·&nbsp; **Prerequisites:** Basic Python (functions, imports), familiarity with the command line

---

## Learning Outcome

By the end of this lesson, you will be able to:

- ✔ Explain what Django is and why it exists
- ✔ Describe the **MTV** (Model–Template–View) architecture in your own words
- ✔ Trace a request through Django from browser → server → middleware → URL → view → response
- ✔ Distinguish a Django **project** from a Django **app**
- ✔ Know when to choose Django over Flask, FastAPI, or Express.js
- ✔ Run your first "Hello Django" view in under five minutes

---

## Visual Preview

Before any theory, here is what a Django request actually looks like from end to end:

```text
Browser  ──GET /blog/──▶  Web Server (Gunicorn)
                              │
                              ▼
                        Django Middleware
                              │
                              ▼
                        URL Dispatcher
                              │
                              ▼
                            View ──▶ Model ──▶ Database
                              │                   │
                              │ ◀─── data ────────┘
                              ▼
                          Template ──▶ rendered HTML
                              │
                              ▼
                        Middleware (response)
                              │
                              ▼
                          HTTP Response  ──▶  Browser
```

And here is the output of the smallest possible Django app you will build at the end of this chapter:

```text
http://127.0.0.1:8000/

  Hello Django!
```

That single line of rendered HTML touches every component of the framework you are about to learn.

---

## Core Concept

### What is Django?

> **Definition — Django:** A high-level, open-source Python web framework that helps developers build secure, scalable, and maintainable web applications quickly. It follows the **MTV (Model–Template–View)** architectural pattern and ships with batteries included — an ORM, admin panel, authentication, templating, forms, and security middleware.

Without a framework, you would manually write URL routing, authentication, database connections, form validation, and CSRF protection for every project. Django provides all of these out of the box so you can focus on **business logic**, not plumbing.

### MTV Architecture

Django splits an application into three responsibilities:

| Layer | Job | Example |
|-------|-----|---------|
| **Model** | Defines data and database structure | `class Post(models.Model)` |
| **Template** | Renders HTML for the browser | `{{ post.title }}` |
| **View** | Contains logic; ties models and templates together | `def post_list(request): ...` |

If you have seen MVC before, Django's **View** is the controller and Django's **Template** is the view — the framework itself plays the controller role behind the scenes.

### The Request/Response Cycle

Every HTTP request flows through the same pipeline:

1. **Browser** sends an HTTP request.
2. A **web server** (Gunicorn, uWSGI, Daphne, Uvicorn) hands the request to Django.
3. **Middleware** runs in order — sessions, auth, CSRF, security headers.
4. The **URL dispatcher** matches the path against `urlpatterns` and picks a view.
5. The **view** executes — it may query models, call services, or just return a string.
6. A **template** (optional) renders the data into HTML.
7. Middleware runs **in reverse** on the response, then Django returns it to the browser.

### Middleware in One Sentence

> **Definition — Middleware:** A pipeline of components that processes every request **before** it reaches a view and every response **before** it leaves Django.

Common middleware you'll meet in `settings.py`:

| Middleware | Purpose |
|------------|---------|
| `SecurityMiddleware` | HTTPS, HSTS, content-type sniffing protection |
| `SessionMiddleware` | Loads/saves the session cookie |
| `AuthenticationMiddleware` | Attaches `request.user` |
| `CsrfViewMiddleware` | Validates the CSRF token on unsafe methods |

### WSGI vs. ASGI

| | **WSGI** | **ASGI** |
|---|----------|----------|
| Full name | Web Server Gateway Interface | Asynchronous Server Gateway Interface |
| Style | Synchronous, one request at a time | Asynchronous, concurrent |
| Best for | Traditional CRUD apps | WebSockets, real-time, async views |
| Common servers | Gunicorn, uWSGI | Uvicorn, Daphne |

Django supports both — pick WSGI unless you need WebSockets or `async def` views.

### Project vs Application (Django)

> **Definition — Project:**  
A project is the complete Django setup for a website or web application. It contains global configuration such as `settings.py`, the root `urls.py`, and overall deployment settings. A project acts as the container for one or more apps.

---

> **Definition — App:**  
An app is a self-contained and reusable module that provides a specific feature within a project. Each app focuses on a single responsibility, such as `blog`, `accounts`, or `payments`. A single project can include multiple apps working together to build the full application.

---

> **Important Note:**  
At least one app is required in every Django project, because all functionality (views, models, URLs, etc.) is implemented inside apps.

| Term | Analogy |
|------|---------|
| Project | A shopping mall |
| App | An individual shop inside the mall |

---

## Syntax

The minimal Django building blocks you will see in every project look like this:

```python
# A view: a Python function that takes a request and returns a response
def my_view(request):
    return HttpResponse("...")
```

```python
# A URL pattern: maps a path to a view
urlpatterns = [
    path("some-path/", my_view, name="my-view"),
]
```

```python
# A model: maps a Python class to a database table
class MyModel(models.Model):
    field_name = models.CharField(max_length=200)
```

Three primitives — **view**, **URL pattern**, **model** — power the entire framework.

---

## Live Code Playground

Here is the complete code for your first Django app. Open three files in your editor and follow along — you can copy, edit, and run this end-to-end.

### `blog/views.py`

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello Django!</h1>")
```

### `blog/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog-index"),
]
```

### `mysite/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
]
```

### Run it

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/) and you should see **Hello Django!**

> 💡 **Tip:** The `include()` call in the project's `urls.py` is what makes Django apps **modular** — every app owns its own URL file.

---

## Step-by-Step Example

Let's build the Hello Django example from scratch, one step at a time.

### Step 1 — Create a project

```bash
python -m venv .venv
source .venv/bin/activate            # macOS / Linux
.venv\Scripts\activate               # Windows

pip install django
django-admin startproject mysite .
```

Django creates `manage.py` and a `mysite/` folder with `settings.py`, `urls.py`, `wsgi.py`, and `asgi.py`.

### Step 2 — Create an app

```bash
python manage.py startapp blog
```

A new `blog/` folder appears with `views.py`, `models.py`, `admin.py`, and friends.

### Step 3 — Register the app

Open `mysite/settings.py` and add `"blog"` to `INSTALLED_APPS`:

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

### Step 4 — Write the view

In `blog/views.py`:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello Django!</h1>")
```

### Step 5 — Wire the URL

Create `blog/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog-index"),
]
```

And include it from `mysite/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
]
```

### Step 6 — Run and observe

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/) — you are now reading a response produced by your own Django view.

---

## Try It Yourself

> **Task:** Modify the `index` view so that when you visit `/blog/hello/<your-name>/` it greets you by name.
>
> Example: `/blog/hello/Hassan/` should render **"Hello, Hassan!"** in an `<h2>` tag.

You'll need to:

1. Add a new URL pattern using a path converter — e.g., `<str:name>`.
2. Update the view signature to accept the extra argument.
3. Use an f-string to embed the name in the response.

Try it before peeking at the solution.

---

## Solution

<details>
<summary>Click to reveal the solution</summary>

### `blog/views.py`

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello Django!</h1>")

def greet(request, name):
    return HttpResponse(f"<h2>Hello, {name}!</h2>")
```

### `blog/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog-index"),
    path("hello/<str:name>/", views.greet, name="blog-greet"),
]
```

### Try the URL

Visit [http://127.0.0.1:8000/blog/hello/Hassan/](http://127.0.0.1:8000/blog/hello/Hassan/) — you should see **Hello, Hassan!**

**What happened internally:**

1. Django matched `hello/<str:name>/` and captured `"Hassan"` as the `name` parameter.
2. It called `greet(request, name="Hassan")`.
3. The view returned an `HttpResponse` containing the formatted HTML.
4. Middleware added headers, and the browser rendered the result.

</details>

---

## Key Notes & Tips

> 💡 **Tip:** A Django **view** is just a Python function that takes a `request` and returns a `response`. Everything else — middleware, templates, the ORM — is optional polish around that core idea.

> 💡 **Tip:** Apps are reusable. Once you write a `blog` app properly, you can drop it into another project with very little glue code.

> ⚠️ **Warning:** Do not put business logic inside `urls.py`. URLs only **route**; views **decide**. Mixing the two is a common beginner mistake that bites later.

> ⚠️ **Warning:** Never run `python manage.py runserver` in production. It is a development-only server. Always deploy behind Gunicorn or Daphne with `DEBUG=False`.

> 💡 **Tip:** Django's official docs at [docs.djangoproject.com](https://docs.djangoproject.com/) are some of the best technical docs in the industry. Bookmark them now.

---

## Common Mistakes

- ❌ **Confusing project and app.** A project holds settings; an app holds features. You create projects with `startproject` and apps with `startapp`.
- ❌ **Forgetting to add the app to `INSTALLED_APPS`.** The app exists on disk but Django ignores it until it is registered.
- ❌ **Calling Django's MTV "MVC".** It is similar, but Django's *Template* is MVC's view, and Django's *View* is MVC's controller.
- ❌ **Thinking Django is slow.** Django is fast; slow apps almost always come from N+1 queries, missing indexes, or absent caching — not the framework.
- ❌ **Skipping virtual environments.** Installing Django globally pollutes your system Python and breaks future projects.
- ❌ **Editing `urlpatterns` without restarting the server.** Most changes hot-reload automatically, but a few (e.g., `settings.py` updates) require a manual restart.

---

## Mini Quiz

Test your understanding before moving on.

**Q1.** What does **MTV** stand for in Django?

- A) Model–Template–View ✔
- B) Model–Test–Validate
- C) Module–Template–View
- D) Model–Transport–View

**Q2.** Which Django component handles **business logic** and ties models and templates together?

- A) Template
- B) View ✔
- C) URL dispatcher
- D) Middleware

**Q3.** A Django **project** can contain how many **apps**?

- A) Exactly one
- B) Zero or one
- C) As many as you want ✔
- D) Apps and projects are the same thing

**Q4.** Which interface should you use if you need **WebSockets** or async views?

- A) WSGI
- B) ASGI ✔
- C) CGI
- D) FastCGI

**Q5.** What is the purpose of **middleware**?

- A) To replace views in async mode
- B) To run logic before and after every request/response globally ✔
- C) To define database tables
- D) To compile templates

---

## Real World Example

Django powers production systems that millions of people use every day.

| Company | What Django powers |
|---------|-------------------|
| **Instagram** | Backend of the world's largest photo-sharing platform |
| **Pinterest** | Content management and discovery feed |
| **Mozilla** | Support, add-ons, and internal tooling |
| **Disqus** | Comments embedded across millions of websites |
| **Eventbrite** | Event creation, ticketing, and analytics |

**Typical Django product shape:**

A SaaS startup builds:

- An **accounts** app for signup, login, and password reset.
- A **billing** app that wraps Stripe and handles subscriptions.
- A **dashboard** app that shows user data with class-based views.
- A **api** app that exposes JSON endpoints for the mobile client.

Each app is self-contained, registered in `INSTALLED_APPS`, and routed through the project's root `urls.py`. The same patterns you used in the **Try It Yourself** task scale up to systems serving millions of users.

---

## Summary

Today you learned:

- ✔ Django is a **high-level Python web framework** that includes batteries — ORM, admin, auth, forms, templates, and security middleware.
- ✔ Django follows the **MTV** (Model–Template–View) architecture.
- ✔ Every request flows through **middleware → URL dispatcher → view → (model/template) → response**.
- ✔ **WSGI** is for synchronous apps; **ASGI** is for async and real-time apps.
- ✔ A **project** is the whole site; an **app** is a reusable feature module inside it.
- ✔ A view is just a Python function that takes a `request` and returns a `response`.
- ✔ You built your first Django view, wired a URL, and accepted a dynamic path parameter.

### Key Takeaways

```text
✅ Django is a high-level Python web framework
✅ Django follows MTV architecture
✅ Django includes many built-in tools (admin, auth, ORM, forms)
✅ Middleware processes every request and response globally
✅ Apps are reusable feature modules; projects compose them
✅ Django is ideal for scalable, secure web applications
```

### Command Reference

```bash
django-admin startproject mysite .     # Create a project
python manage.py startapp blog         # Create an app
python manage.py runserver             # Start the dev server
python manage.py makemigrations        # Generate migration files
python manage.py migrate               # Apply migrations
python manage.py createsuperuser       # Create an admin user
python manage.py shell                 # Open the Django shell
python -m django --version             # Check installed version
```

### Glossary

| Term | Definition |
|------|------------|
| Django | A high-level Python web framework |
| MTV | Model–Template–View, Django's architectural pattern |
| Project | The whole deployable site (settings + root URLs) |
| App | A reusable feature module inside a project |
| Middleware | Code that runs before/after every request and response |
| QuerySet | A lazy, chainable database query |
| Migration | A versioned schema change file |
| WSGI | Synchronous Python server interface |
| ASGI | Asynchronous Python server interface |
| LTS | Long-Term Support release with extended security fixes |

---

## Next Lesson Navigation

| ← Previous Lesson | Next Lesson → |
|-------------------|---------------|
| [Course Overview](./ch00-course-overview.md) | [Setup & Project Structure](./ch02-setup-project-structure.md) |
