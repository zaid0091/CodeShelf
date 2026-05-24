#!/usr/bin/env python3
"""Generate expanded Django course chapters (ch01-ch14)."""
from __future__ import annotations

import textwrap
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "content" / "django"


def fm(title: str, description: str, order: int, tags: list[str]) -> str:
    tag_line = ", ".join(tags)
    return f"""---
title: {title}
description: {description}
order: {order}
tags: [{tag_line}]
---

"""


def toc(items: list[str]) -> str:
    lines = ["## Table of Contents", ""]
    for i, (title, anchor) in enumerate(items, 1):
        lines.append(f"{i}. [{title}](#{anchor})")
    lines.extend(["", "---", ""])
    return "\n".join(lines)


def section(title: str, body: str, level: int = 2) -> str:
    hashes = "#" * level
    return f"{hashes} {title}\n\n{body.strip()}\n\n---\n\n"


def subsection(title: str, body: str) -> str:
    return section(title, body, level=3)


def code_block(lang: str, code: str) -> str:
    return f"```{lang}\n{code.strip()}\n```\n\n"


def mistakes(items: list[tuple[str, str, str]]) -> str:
    rows = "\n".join(f"| {a} | {b} | {c} |" for a, b, c in items)
    return section(
        "Common Mistakes",
        f"""Many beginners hit the same walls. Learn from these early.

| Mistake | What goes wrong | Fix |
|---------|-----------------|-----|
{rows}
""",
    )


def interview(items: list[str]) -> str:
    body = "\n\n".join(items)
    return section("Interview Points", body)


def exercises(chapter_num: int, items: list[dict]) -> str:
    parts = [
        "## Exercises",
        "",
        "> Practice is how Django becomes muscle memory. Complete these after reading the chapter.",
        "",
    ]
    for i, ex in enumerate(items, 1):
        parts.append(f"### Exercise {chapter_num}.{i}: {ex['title']}")
        parts.append("")
        parts.append(ex["prompt"])
        parts.append("")
        if ex.get("hint"):
            parts.append(f"> **Hint:** {ex['hint']}")
            parts.append("")
        parts.append("<details>")
        parts.append(f"<summary>Click to reveal solution for Exercise {chapter_num}.{i}</summary>")
        parts.append("")
        parts.append(ex["solution"])
        parts.append("")
        parts.append("</details>")
        parts.append("")
        parts.append("---")
        parts.append("")
    return "\n".join(parts)


def summary(bullets: list[str], rules: list[str], next_title: str, next_file: str, ch_num: int) -> str:
    bl = "\n".join(f"- {b}" for b in bullets)
    rl = "\n".join(f"{r}" for r in rules)
    return f"""## Chapter Summary

Excellent work completing Chapter {ch_num}. Here is what you learned:

{bl}

### Key rules to remember

```
{rl}
```

---

## Next Chapter

{next_title}

**➡️ [Next Chapter →](./{next_file})**

---

*Chapter {ch_num} of the Complete Django Guide | [Report an issue](https://github.com/zaid0091/CodeShelf/issues)*
"""


def expand_paragraphs(topic: str, points: list[str], extra: str = "") -> str:
    """Generate multiple explanatory paragraphs for depth."""
    parts = [
        f"> **In this section:** You will understand {topic} clearly enough to explain it in an interview and use it in a real project.",
        "",
    ]
    for p in points:
        parts.append(p)
        parts.append("")
    if extra:
        parts.append(extra)
        parts.append("")
    return "\n".join(parts)


def build_ch01() -> str:
    items = [
        ("What is Django?", "what-is-django"),
        ("History of Django", "history-of-django"),
        ("Why Use Django?", "why-use-django"),
        ("MTV Architecture Explained", "mtv-architecture-explained"),
        ("Request and Response Cycle", "request-and-response-cycle"),
        ("Middleware Overview", "middleware-overview"),
        ("WSGI and ASGI", "wsgi-and-asgi"),
        ("Django vs Other Frameworks", "django-vs-other-frameworks"),
        ("Project vs Application", "project-vs-application"),
        ("Batteries Included", "batteries-included"),
        ("Django Design Philosophy", "django-design-philosophy"),
        ("When to Choose Django", "when-to-choose-django"),
        ("When Not to Choose Django", "when-not-to-choose-django"),
        ("Hello Django Preview", "hello-django-preview"),
        ("Django Version and Docs", "django-version-and-docs"),
        ("Learning Path in This Course", "learning-path-in-this-course"),
        ("Best Practices", "best-practices"),
        ("Common Mistakes", "common-mistakes"),
        ("Interview Points", "interview-points"),
        ("Exercises", "exercises"),
        ("Chapter Summary", "chapter-summary"),
    ]
    c = fm(
        "Django Introduction",
        "Django history, MTV architecture, batteries-included design, and when to use Django",
        1,
        ["django", "mtv", "introduction"],
    )
    c += "# Chapter 1: Django Introduction\n\n"
    c += "> **Welcome to Django!**\n"
    c += "> In this chapter you will learn what Django is, how it organizes web applications, and why teams choose it for production sites. You already know Python from the CodeShelf Python course — Django is where that knowledge meets the web.\n\n---\n\n"
    c += toc(items)

    c += section(
        "What is Django?",
        expand_paragraphs(
            "the Django web framework",
            [
                "> **Definition:** **Django** is a free, open-source **web framework** written in Python. A framework gives you structure, tools, and conventions so you do not rebuild routing, database access, forms, and security from scratch on every project.",
                "Think of building a house. You *could* cut every board and forge every nail yourself (raw Python + HTTP). Django is more like a **prefab kit with an architect's blueprint**: walls, plumbing, and electrical standards are already designed; you customize rooms and paint.",
                "Django handles:",
                "- **URL routing** — map `/blog/5/` to Python code",
                "- **Database layer (ORM)** — Python classes instead of hand-written SQL for most work",
                "- **Templates** — HTML with safe placeholders",
                "- **Forms** — validation and HTML generation",
                "- **Authentication** — users, sessions, permissions",
                "- **Admin interface** — automatic management UI for your data",
                "You write **your** business logic; Django handles repetitive web plumbing.",
            ],
        ),
    )

    c += section(
        "History of Django",
        """Understanding Django's origin explains its opinions (batteries included, admin-first, newsroom speed).

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
""",
    )

    c += section(
        "Why Use Django?",
        """| Advantage | What it means for you |
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
""",
    )

    c += section(
        "MTV Architecture Explained",
        """Django advertises **MTV**: **Model**, **Template**, **View**. It is analogous to the older **MVC** (Model–View–Controller) pattern from other frameworks.

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
""",
    )

    c += section(
        "Request and Response Cycle",
        """Every page load follows the same pipeline.

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
""",
    )

    c += section(
        "Middleware Overview",
        """> **Definition:** **Middleware** is a chain of hooks that process every request **before** the view and every response **after** the view.

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
""",
    )

    c += section(
        "WSGI and ASGI",
        """Python web apps speak a standard interface to servers:

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
""",
    )

    c += section(
        "Django vs Other Frameworks",
        """| Framework | Strengths | Tradeoffs |
|-----------|-----------|-----------|
| **Django** | Full-stack, ORM, admin, auth | More structure; heavier for tiny APIs |
| **Flask** | Minimal, flexible | You assemble auth, admin, ORM yourself |
| **FastAPI** | Async APIs, OpenAPI docs | Less built-in for server-rendered HTML sites |
| **Django REST Framework** | REST on top of Django | API-focused; still uses Django core |

**Choose Django when:** you want a relational database, HTML pages, user accounts, and fast internal admin tools in one project.

**Consider alternatives when:** you only need a stateless JSON microservice and will never use templates or admin (still, many teams use Django + DRF anyway).
""",
    )

    c += section(
        "Project vs Application",
        """Django splits work into two container types:

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
""",
    )

    c += section(
        "Batteries Included",
        """`django.contrib` ships many subsystems:

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
""",
    )

    c += section(
        "Django Design Philosophy",
        """| Principle | Meaning in practice |
|-----------|---------------------|
| **DRY** | Don't Repeat Yourself — one model definition drives DB, forms, admin |
| **Explicit is better than implicit** | URL patterns are visible in `urls.py` |
| **Loose coupling** | Apps should work independently where possible |
| **Fast iteration** | Admin + ORM reduce time to working prototype |

Django is **opinionated** — it rewards following conventions. Fighting every convention (e.g. putting all code in one file) slows you down.
""",
    )

    c += section(
        "When to Choose Django",
        """**Strong fit:**
- Content sites, blogs, documentation portals
- SaaS dashboards with accounts and permissions
- Internal tools (inventory, support tickets)
- CRUD-heavy applications
- Teams that want conventions and built-in admin

**Real example:** A startup building a project-management tool needs users, teams, tasks, and a staff admin to fix data. Django gives auth + admin on week one.
""",
    )

    c += section(
        "When Not to Choose Django",
        """**Consider other tools when:**
- You need extreme real-time (games, collaborative editors) — may add Django Channels or another stack
- You only expose a tiny stateless API and hate monoliths — FastAPI is popular
- Your team is 100% JavaScript and wants one language on server and client — Node ecosystem

**Note:** "Django is slow" is usually **misconfigured database queries**, not the framework itself. Optimization is covered in [Best Practices](./ch13-best-practices.md).
""",
    )

    c += section(
        "Hello Django Preview",
        """Here is the smallest useful slice — you will build this hands-on in Chapter 2.

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
""",
    )

    c += section(
        "Django Version and Docs",
        """Always check your installed version:

```bash
python -m django --version
```

| Resource | URL pattern |
|----------|-------------|
| Official docs | https://docs.djangoproject.com/ |
| Tutorial | "Writing your first Django app" in docs |
| Release notes | Read before upgrading major versions |

This course targets **Django 5.x** patterns. Older tutorials may use deprecated APIs — when in doubt, check the docs for your version.
""",
    )

    c += section(
        "Learning Path in This Course",
        """| Chapter | Topic |
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
""",
    )

    c += section(
        "Best Practices",
        """From day one, adopt habits that scale:

1. **Use a virtual environment** per project — never install Django globally.
2. **Pin dependencies** in `requirements.txt`.
3. **One app per feature area** — not one giant `models.py` for everything.
4. **Use named URLs** — `reverse("post-detail", kwargs={"pk": 1})` not hard-coded `/blog/1/`.
5. **Keep `SECRET_KEY` out of git** — use environment variables in production.
6. **Read error pages in development** — Django's debug page is a teaching tool.
""",
    )

    c += mistakes([
        ("Confusing MTV with MVC names", "Thinking Django 'view' is HTML", "Remember: View = Python logic; Template = HTML"),
        ("One giant app for everything", "Unmaintainable codebase", "Split into blog, accounts, shop apps"),
        ("Skipping virtualenv", "Dependency conflicts between projects", "python -m venv .venv always"),
        ("Disabling security in prod", "DEBUG=True leaks secrets", "DEBUG=False, ALLOWED_HOSTS set"),
        ("Not reading tracebacks", "Random trial-and-error fixes", "Start at the bottom of the traceback"),
    ])

    c += interview([
        "**Q: What is Django?** — High-level Python web framework with ORM, templates, forms, auth, admin.",
        "**Q: Explain MTV.** — Model = data; Template = presentation; View = request handler (like MVC controller).",
        "**Q: Project vs app?** — Project = site config; app = modular feature, reusable.",
        "**Q: What is middleware?** — Global request/response processors (sessions, CSRF, auth).",
        "**Q: WSGI vs ASGI?** — WSGI = sync standard; ASGI = async + WebSockets.",
    ])

    c += exercises(1, [
        {
            "title": "Explore Django documentation",
            "prompt": "Open the official Django documentation. List three built-in `django.contrib` applications and one sentence describing each.",
            "solution": "Example answers:\n- **auth** — user accounts, groups, permissions\n- **admin** — automatic CRUD interface for models\n- **sessions** — stores session data across requests",
        },
        {
            "title": "Draw the MTV flow",
            "prompt": "On paper or in a text file, draw the path from browser `GET /posts/` to HTML response. Label URLconf, view, model, template, and database.",
            "hint": "Start at the browser and end at the HTTP response.",
            "solution": "Browser → URLconf matches `/posts/` → view `post_list` → ORM query on Post model → database returns rows → view passes `posts` to template → template renders HTML → HttpResponse to browser.",
        },
        {
            "title": "Compare frameworks",
            "prompt": "Write one paragraph comparing Django to Flask for a team building a membership site with admin tools.",
            "solution": "Django includes auth, admin, and ORM out of the box, which fits a membership site needing staff dashboards. Flask is lighter but requires choosing and integrating extensions for users and admin, increasing initial setup time. For CRUD-heavy membership sites, Django's conventions often deliver faster MVP delivery.",
        },
        {
            "title": "Install Django",
            "prompt": "Create a virtual environment, install Django, and print the version.",
            "solution": code_block("bash", """
python -m venv .venv
# Windows PowerShell:
.venv\\Scripts\\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate
pip install "django>=5.0,<6.0"
python -m django --version
"""),
        },
    ])

    c += summary(
        [
            "### Core ideas",
            "- Django is a **batteries-included** Python web framework.",
            "- **MTV**: Models (data), Templates (HTML), Views (logic).",
            "- **Project** = whole site; **App** = feature module.",
            "- Requests pass through **middleware**, **URLconf**, **view**, optionally **ORM** and **templates**.",
            "- Use Django for CRUD-heavy, user-facing, admin-backed applications.",
        ],
        [
            "✅ Use virtual environments and pin Django in requirements.txt",
            "✅ Split features into apps",
            "✅ Learn MTV before fighting conventions",
            "❌ Do not confuse Django View with HTML page",
            "❌ Do not run production with DEBUG=True",
        ],
        "You are ready to install Django and create your first project.",
        "ch02-setup-project-structure.md",
        1,
    )
    return c


# Due to script size, remaining chapters use a shared builder
CHAPTER_META = [
    (2, "Setup and Project Structure", "Installing Django, creating projects and apps, settings.py, and manage.py", ["django", "setup", "project"], "ch02-setup-project-structure.md"),
    (3, "Models and ORM", "Model fields, relationships, QuerySets, lookups, and managers", ["django", "orm", "models"], "ch03-models-orm.md"),
    (4, "Views and URLs", "Function-based views, URLconf, HttpRequest, HttpResponse, and redirects", ["django", "views", "urls"], "ch04-views-urls.md"),
    (5, "Templates", "Django template language, inheritance, context, filters, and tags", ["django", "templates", "dtl"], "ch05-templates.md"),
    (6, "Forms", "Django Form and ModelForm, validation, CSRF, and form rendering in templates", ["django", "forms", "csrf"], "ch06-forms.md"),
    (7, "Admin Panel", "ModelAdmin customization, list display, filters, search, inlines, and actions", ["django", "admin"], "ch07-admin-panel.md"),
    (8, "Authentication", "User model, login, logout, permissions, decorators, and custom user models", ["django", "auth", "users"], "ch08-authentication.md"),
    (9, "Migrations", "makemigrations, migrate, migration files, squashing, and data migrations", ["django", "migrations", "database"], "ch09-migrations.md"),
    (10, "Static and Media Files", "STATIC_URL, MEDIA_URL, collectstatic, serving files in dev and production", ["django", "static", "media"], "ch10-static-media-files.md"),
    (11, "Class-Based Views", "ListView, DetailView, CreateView, UpdateView, DeleteView, and mixins", ["django", "cbv", "generic-views"], "ch11-class-based-views.md"),
    (12, "Deployment Basics", "Production settings, Gunicorn, WSGI, environment variables, and hosting overview", ["django", "deployment", "production"], "ch12-deployment-basics.md"),
    (13, "Django Best Practices", "Project structure, security, ORM performance, testing, and coding conventions", ["django", "best-practices", "security"], "ch13-best-practices.md"),
    (14, "Django Interview Preparation", "Common Django interview questions, ORM patterns, architecture, and system design", ["django", "interview", "career"], "ch14-interview-prep.md"),
]

NEXT_FILES = [
    "ch02-setup-project-structure.md",
    "ch03-models-orm.md",
    "ch04-views-urls.md",
    "ch05-templates.md",
    "ch06-forms.md",
    "ch07-admin-panel.md",
    "ch08-authentication.md",
    "ch09-migrations.md",
    "ch10-static-media-files.md",
    "ch11-class-based-views.md",
    "ch12-deployment-basics.md",
    "ch13-best-practices.md",
    "ch14-interview-prep.md",
    None,
]


def deep_section(title: str, paragraphs: list[str], examples: list[tuple[str, str]] | None = None, table: str | None = None) -> str:
    body = "\n\n".join(paragraphs) + "\n\n"
    if table:
        body += table + "\n\n"
    if examples:
        for label, code in examples:
            body += f"### {label}\n\n{code_block('python' if 'def ' in code or 'class ' in code or 'from django' in code else 'bash', code)}"
    return section(title, body)


def build_generic_chapter(num: int, title: str, desc: str, tags: list[str], filename: str, sections_data: list, welcome: str, ex_items: list, mistake_rows: list, interview_items: list, summary_bullets: list, summary_rules: list) -> str:
    next_file = NEXT_FILES[num - 1] if num < 14 else None
    items = [(s[0], s[0].lower().replace(" ", "-").replace("'", "").replace("(", "").replace(")", "")) for s in sections_data]
    items.extend([
        ("Best Practices", "best-practices"),
        ("Common Mistakes", "common-mistakes"),
        ("Interview Points", "interview-points"),
        ("Exercises", "exercises"),
        ("Chapter Summary", "chapter-summary"),
    ])

    c = fm(title, desc, num, tags)
    c += f"# Chapter {num}: {title}\n\n"
    c += f"> **{welcome}**\n\n---\n\n"
    c += toc(items)

    for sec in sections_data:
        name, paras, *rest = sec
        ex = rest[0] if len(rest) > 0 and isinstance(rest[0], list) else None
        tbl = rest[1] if len(rest) > 1 and isinstance(rest[1], str) else (rest[0] if len(rest) > 0 and isinstance(rest[0], str) else None)
        if ex is not None and isinstance(ex, list):
            c += deep_section(name, paras, ex, tbl if isinstance(tbl, str) else None)
        elif isinstance(rest[0] if rest else None, str):
            c += deep_section(name, paras, None, rest[0])
        else:
            c += deep_section(name, paras)

    c += section("Best Practices", summary_bullets[0] if isinstance(summary_bullets[0], str) and summary_bullets[0].startswith("###") else "\n".join(f"- {b}" for b in summary_bullets[:5]))
    c += mistakes(mistake_rows)
    c += interview(interview_items)
    c += exercises(num, ex_items)

    if next_file:
        c += summary(
            summary_bullets[5:] if len(summary_bullets) > 5 else summary_bullets,
            summary_rules,
            f"Continue to the next chapter in the Django course.",
            next_file,
            num,
        )
    else:
        c += f"""## Chapter Summary

{chr(10).join('- ' + b for b in summary_bullets)}

### Key rules to remember

```
{chr(10).join(summary_rules)}
```

---

## Course Complete

Congratulations on finishing the Django course! Review [Course Overview](./ch00-course-overview.md) or explore API development with Django REST Framework.

---

*Chapter {num} of the Complete Django Guide*
"""
    return c


# Load chapter-specific content from companion module
def main():
    from generate_django_chapters_content import CHAPTERS  # noqa: WPS433

    OUT.mkdir(parents=True, exist_ok=True)
    ch01 = build_ch01()
    (OUT / "ch01-django-introduction.md").write_text(ch01, encoding="utf-8")
    counts = {"ch01-django-introduction.md": len(ch01.splitlines())}

    for num, data in CHAPTERS.items():
        fname = CHAPTER_META[num - 2][4] if num >= 2 else None
        if num == 1:
            continue
        meta = CHAPTER_META[num - 2]
        content = build_generic_chapter(num, meta[1], meta[2], meta[3], meta[4], **data)
        path = OUT / meta[4]
        path.write_text(content, encoding="utf-8")
        counts[meta[4]] = len(content.splitlines())

    print("Line counts:")
    for k in sorted(counts):
        print(f"  {k}: {counts[k]}")


if __name__ == "__main__":
    main()
