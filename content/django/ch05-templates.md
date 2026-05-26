---
title: Templates
description: Master the Django Template Language — variables, tags, filters, inheritance, includes, CSRF, escaping, and custom template tags
order: 5
tags: [django, templates, dtl, html, frontend]
---

# Chapter 5 — Templates

> Turn data into HTML — write secure, reusable, inheritable templates with the Django Template Language (DTL).
>
> **Difficulty:** Beginner &nbsp;·&nbsp; **Estimated time:** 45 – 60 min &nbsp;·&nbsp; **Prerequisites:** [Chapter 4 — Views and URLs](./ch04-views-urls.md), basic HTML

---

## Learning Outcome

By the end of this lesson, you will be able to:

- ✔ Configure the **template loader** and place templates in the right folder
- ✔ Use DTL **variables** `{{ … }}`, **tags** `{% … %}`, and **comments** `{# … #}`
- ✔ Build a **base layout** and extend it with `{% extends %}` + `{% block %}`
- ✔ Render lists with `{% for %}` (and `{% empty %}`) and conditions with `{% if %}` / `{% elif %}` / `{% else %}`
- ✔ Apply **filters** like `|date`, `|default`, `|truncatewords`, `|pluralize`, `|length`
- ✔ Generate links and assets safely with `{% url %}` and `{% static %}`
- ✔ Protect every POST form with **`{% csrf_token %}`**
- ✔ Trust Django's **auto-escaping** and know when (and why not) to use `|safe`
- ✔ Reuse fragments with `{% include %}` and inject globals via **context processors**
- ✔ Write your own **custom template tags and filters**

---

## Visual Preview

Three files turn into one rendered page:

```text
┌────────────────────────────┐    ┌─────────────────────────┐
│ blog/views.py              │    │ blog/post_list.html     │
│                            │    │                         │
│ posts = Post.objects       │    │ {% extends "base.html"  │
│   .filter(published=True)  │    │   %}                    │
│                            │    │ {% block content %}     │
│ render(request,            │ ─▶ │   {% for p in posts %}  │
│   "blog/post_list.html",   │    │     <h2>{{ p.title }}   │
│   {"posts": posts})        │    │   {% endfor %}          │
└────────────────────────────┘    │ {% endblock %}          │
                                  └────────────┬────────────┘
                                               │
                                               ▼
                                  ┌─────────────────────────┐
                                  │ rendered HTML           │
                                  │                         │
                                  │ <h2>Hello Django</h2>   │
                                  │ <h2>Templates rock</h2> │
                                  │ <h2>DTL deep dive</h2>  │
                                  └─────────────────────────┘
```

By the end of this lesson, the page above will inherit a base layout, render dynamic links with `{% url %}`, escape user content automatically, and degrade gracefully when the post list is empty.

---

## Core Concept

### Templates separate logic from presentation

> **Definition — Template:** A text file (usually HTML) with **placeholders** (`{{ var }}`) and **control structures** (`{% if %}`, `{% for %}`) that Django renders into a final string for the browser.

DTL deliberately limits what you can do — there is no `if x = call_python_function()` because that kind of logic belongs in **views** or **template tags**, not in HTML.

### Three syntactic primitives

| Syntax | Used for | Example |
|--------|----------|---------|
| `{{ variable }}` | Output a value (auto-escaped) | `{{ post.title }}` |
| `{% tag %}` | Control flow / template logic | `{% if user.is_authenticated %}` |
| `{# comment #}` | Template-only comment (not rendered) | `{# TODO: refactor #}` |

### Template inheritance is the killer feature

A **base** template defines `{% block name %}…{% endblock %}` slots. **Child** templates use `{% extends %}` and override the blocks they care about. You write your shared layout, navigation, and footer **once**.

### Auto-escaping is on by default

Every `{{ value }}` is escaped — `<`, `>`, `&`, `"`, and `'` become HTML entities. This neutralizes **XSS** attacks. The escape only relaxes when you explicitly opt out with `|safe` or `{% autoescape off %}`.

### App-namespaced template paths

Even though all apps' `templates/` folders are searched, you should always nest your template inside an app subfolder:

```text
blog/templates/blog/post_list.html
```

This prevents `accounts/post_list.html` from accidentally shadowing `blog/post_list.html`.

---

## Syntax

The four DTL constructs you will use every day:

```django
{{ variable }}                              {# variable output #}
{{ variable|filter:argument }}              {# value with filter applied #}

{% tag %} ... {% endtag %}                  {# block tag #}
{% standalone_tag arg1 arg2 %}              {# inline tag #}

{# comment that won't appear in the rendered HTML #}
```

The minimum **base / child** template skeleton:

```django
{# base.html #}
<!doctype html>
<html>
  <body>
    {% block content %}{% endblock %}
  </body>
</html>
```

```django
{# child.html #}
{% extends "base.html" %}
{% block content %}
  Hello!
{% endblock %}
```

---

## Live Code Playground

A complete blog template stack — base layout, list page, detail page, partial, and a custom filter.

### `mysite/settings.py` (templates entry — usually already correct)

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],     # project-wide templates
        "APP_DIRS": True,                     # also search blog/templates/, accounts/templates/, ...
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

### `templates/base.html`

```django
{% load static %}
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{% block title %}My Blog{% endblock %}</title>
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
  <header>
    <a href="{% url 'blog:post-list' %}">Blog</a>
    {% if user.is_authenticated %}
      <span>Hi, {{ user.username }}</span>
    {% endif %}
  </header>

  <main>
    {% block content %}{% endblock %}
  </main>

  <footer>&copy; {% now "Y" %} CodeShelf</footer>
</body>
</html>
```

### `blog/templates/blog/post_list.html`

```django
{% extends "base.html" %}

{% block title %}Posts — {{ block.super }}{% endblock %}

{% block content %}
  <h1>Latest posts</h1>

  <ul class="post-list">
    {% for post in posts %}
      <li>
        <a href="{% url 'blog:post-detail' pk=post.pk %}">{{ post.title }}</a>
        <small>{{ post.created_at|date:"M j, Y" }}</small>
        <p>{{ post.body|truncatewords:20 }}</p>
      </li>
    {% empty %}
      <li>No posts yet.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

### `blog/templates/blog/post_detail.html`

```django
{% extends "base.html" %}

{% block title %}{{ post.title }}{% endblock %}

{% block content %}
  <article>
    <h1>{{ post.title }}</h1>
    <p>Published {{ post.created_at|date:"F j, Y" }} · {{ post.body|wordcount }} words</p>
    <div>{{ post.body|linebreaks }}</div>

    {% include "blog/partials/comment_form.html" with post=post %}
  </article>
{% endblock %}
```

### `blog/templates/blog/partials/comment_form.html`

```django
<form method="post" action="{% url 'blog:comment-create' pk=post.pk %}">
  {% csrf_token %}
  <textarea name="body" required></textarea>
  <button type="submit">Post comment</button>
</form>
```

### A custom filter — `blog/templatetags/blog_extras.py`

```python
from django import template

register = template.Library()


@register.filter
def reading_minutes(text, wpm=200):
    """Estimate reading time in minutes."""
    word_count = len(text.split())
    return max(1, round(word_count / wpm))
```

Use it in a template:

```django
{% load blog_extras %}
<small>{{ post.body|reading_minutes }} min read</small>
```

> 💡 **Tip:** After adding a `templatetags/` package, restart `runserver`. Django caches loaded tag libraries.

---

## Step-by-Step Example

Build the **`base.html` → `post_list.html`** flow from zero so every step is testable.

### Step 1 — Verify the template settings

Open `mysite/settings.py` and confirm:

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
    },
]
```

`APP_DIRS=True` makes Django search `<app>/templates/` automatically. `DIRS` lets you keep shared templates (like `base.html`) at the project root.

### Step 2 — Create the project-level `base.html`

```text
templates/base.html
```

```django
<!doctype html>
<html>
<head><title>{% block title %}Blog{% endblock %}</title></head>
<body>
  {% block content %}{% endblock %}
</body>
</html>
```

### Step 3 — Create the app-namespaced child template

```text
blog/templates/blog/post_list.html
```

```django
{% extends "base.html" %}
{% block title %}Posts{% endblock %}
{% block content %}
  <h1>Posts</h1>
  <ul>
    {% for post in posts %}
      <li>{{ post.title }}</li>
    {% empty %}
      <li>No posts yet.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

### Step 4 — Wire it up from a view

```python
# blog/views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, "blog/post_list.html", {"posts": posts})
```

### Step 5 — Hit the URL

`/blog/` should now render the inherited layout with the dynamic post list. If the list is empty, you should see **"No posts yet."** — the `{% empty %}` branch.

### Step 6 — Add a filter

Change the loop body to:

```django
<li>
  {{ post.title }} — {{ post.created_at|date:"M j, Y" }}
  <p>{{ post.body|truncatewords:15 }}</p>
</li>
```

You instantly get formatted dates and a short summary — without touching the view.

### Step 7 — Add a partial

Move the `<li>...</li>` into `blog/templates/blog/partials/post_card.html` and replace it with:

```django
{% include "blog/partials/post_card.html" with post=post %}
```

The page renders identically, but the partial is now reusable on the home page, search results, or anywhere else.

---

## Try It Yourself

> **Task:** Add a **search bar** to `post_list.html` that:
>
> 1. Lives inside a partial at `blog/templates/blog/partials/search_bar.html`.
> 2. Includes the search bar at the top of `post_list.html` using `{% include %}`.
> 3. POSTs to the same URL with a CSRF token.
> 4. Pre-fills the input with the current `q` value if one was submitted.
> 5. Shows a friendly **"No results for 'foo'"** message when the query returns no posts (use `{% if posts %} … {% else %} … {% endif %}` or the `{% empty %}` branch).

Hints:

- The view should already pass `q` and `posts` in the context (see Chapter 4's playground).
- Inside the partial, write `<input name="q" value="{{ q|default:'' }}">`.
- Use `{% csrf_token %}` even on a method-`get` form? **No** — CSRF only protects unsafe methods (POST/PUT/DELETE). For a search bar, `method="get"` is correct and no token is needed.

Try it before peeking at the solution.

---

## Solution

<details>
<summary>Click to reveal the solution</summary>

### `blog/templates/blog/partials/search_bar.html`

```django
<form method="get" action="{% url 'blog:post-list' %}" class="search-bar">
  <input
    type="search"
    name="q"
    value="{{ q|default:'' }}"
    placeholder="Search posts..."
  >
  <button type="submit">Search</button>
</form>
```

### `blog/templates/blog/post_list.html`

```django
{% extends "base.html" %}

{% block title %}Posts{% endblock %}

{% block content %}
  <h1>Posts</h1>

  {% include "blog/partials/search_bar.html" %}

  {% if q %}
    <p>Showing results for "<strong>{{ q }}</strong>"</p>
  {% endif %}

  <ul>
    {% for post in posts %}
      <li>
        <a href="{% url 'blog:post-detail' pk=post.pk %}">{{ post.title }}</a>
        <small>{{ post.created_at|date:"M j, Y" }}</small>
      </li>
    {% empty %}
      {% if q %}
        <li>No results for "{{ q }}".</li>
      {% else %}
        <li>No posts yet.</li>
      {% endif %}
    {% endfor %}
  </ul>
{% endblock %}
```

### What's happening

1. `{% include "blog/partials/search_bar.html" %}` reuses one HTML chunk on every page that needs search.
2. `value="{{ q|default:'' }}"` keeps the user's query visible after submit. The `|default:''` filter handles the case where `q` is `None`.
3. `method="get"` puts the query in the URL (`?q=django`) — bookmarkable and CSRF-token-free.
4. `{% empty %}` runs only when the QuerySet is empty, and the nested `{% if q %}` differentiates "no results for this search" vs. "no posts at all".

</details>

---

## Key Notes & Tips

> 💡 **Tip:** Always nest templates inside an app folder — `blog/templates/blog/post_list.html`, not `blog/templates/post_list.html`. This avoids name collisions across apps.

> 💡 **Tip:** Use `{% url 'name' %}` in templates instead of writing literal URLs. The day you change a route, every template still works.

> 💡 **Tip:** `{{ value|default:"—" }}` and `{{ value|default_if_none:"—" }}` differ — the first treats `False` and `""` as "missing", the second only triggers on `None`.

> 💡 **Tip:** `block.super` lets a child append to a parent block instead of replacing it: `{% block title %}{{ block.super }} — Posts{% endblock %}`.

> ⚠️ **Warning:** Never write `{{ user_input|safe }}`. The `|safe` filter disables auto-escaping and re-opens the door to XSS. Only use it on content **you** generated (e.g., already-sanitized markdown).

> ⚠️ **Warning:** `{% csrf_token %}` is **required** on every `<form method="post">`. Forgetting it produces a `403 Forbidden — CSRF verification failed` error.

> ⚠️ **Warning:** `TemplateDoesNotExist` lists **every path Django searched**. Read it carefully — your template is almost always one folder away from where Django expected it.

> 💡 **Tip:** Restart the dev server after creating a `templatetags/` package or adding a new `__init__.py`. Django won't pick up new tag libraries until it does a full discovery pass.

---

## Common Mistakes

- ❌ **Putting templates directly in `blog/templates/post_list.html`.** They work, but they collide with other apps. Always nest in an app subfolder.
- ❌ **Forgetting `{% csrf_token %}` inside POST forms.** Django returns 403 and you spend 20 minutes searching for the cause.
- ❌ **Trusting user input with `|safe`.** That single character disables Django's XSS protection on that variable.
- ❌ **Putting business logic in templates.** If you find yourself wanting `{% if a > b and c.startswith("x") %}`, move that decision into the view or a model property.
- ❌ **Hard-coding URLs in `<a href>`.** Use `{% url 'app:name' %}` so renaming a route never breaks a link.
- ❌ **Forgetting `{% load static %}`** before `{% static 'css/style.css' %}`. Django raises `'static' is not a registered tag library`.
- ❌ **Forgetting `{% load <app>_extras %}`** in templates that use your custom filters.
- ❌ **Calling methods with arguments in templates.** DTL doesn't allow it — write a model property or template tag instead.
- ❌ **Indenting `{% include %}` arguments incorrectly.** `{% include "x.html" with foo=bar baz=qux %}` — no commas, no quotes around variable names.

---

## Mini Quiz

**Q1.** Which directive is used to inherit from a parent template?

- A) `{% include "base.html" %}`
- B) `{% extends "base.html" %}` ✔
- C) `{% block "base.html" %}`
- D) `{% inherit "base.html" %}`

**Q2.** What does Django do with `{{ post.title }}` by default?

- A) Outputs the raw value
- B) **Auto-escapes** HTML special characters to prevent XSS ✔
- C) Strips HTML tags entirely
- D) Wraps it in a `<p>` tag

**Q3.** What is the **correct** path for a `post_list.html` template that belongs to the `blog` app?

- A) `templates/post_list.html`
- B) `blog/post_list.html`
- C) `blog/templates/post_list.html`
- D) `blog/templates/blog/post_list.html` ✔

**Q4.** Which tag must appear inside every `<form method="post">`?

- A) `{% form_token %}`
- B) `{% csrf_token %}` ✔
- C) `{% security_token %}`
- D) `{% post_token %}`

**Q5.** What does `{{ post.body|truncatewords:15 }}` do?

- A) Truncates `post.body` to the first 15 **characters**
- B) Truncates `post.body` to the first 15 **words** ✔
- C) Returns the 15th word in `post.body`
- D) Splits `post.body` into 15-word chunks

---

## Real World Example

A typical product layout uses every concept from this chapter at the same time.

### `templates/base.html`

```django
{% load static %}
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{% block title %}Acme{% endblock %}</title>

  <link rel="stylesheet" href="{% static 'css/main.css' %}">
  {% block extra_head %}{% endblock %}
</head>
<body class="{% block body_class %}{% endblock %}">

  {% include "partials/navbar.html" %}

  <main class="container">
    {% if messages %}
      <div class="flash-messages">
        {% for message in messages %}
          <div class="flash flash--{{ message.tags }}">{{ message }}</div>
        {% endfor %}
      </div>
    {% endif %}

    {% block content %}{% endblock %}
  </main>

  {% include "partials/footer.html" %}

  <script src="{% static 'js/app.js' %}"></script>
  {% block extra_scripts %}{% endblock %}
</body>
</html>
```

### A page that uses every primitive at once

```django
{% extends "base.html" %}
{% load static blog_extras %}

{% block title %}{{ project.name }} — {{ block.super }}{% endblock %}

{% block extra_head %}
  <meta name="description" content="{{ project.summary|truncatechars:160 }}">
{% endblock %}

{% block content %}
  <header class="project-header">
    <h1>{{ project.name }}</h1>
    <p>
      Created {{ project.created_at|date:"F j, Y" }}
      · {{ project.tasks.count }} task{{ project.tasks.count|pluralize }}
      · {{ project.description|reading_minutes }} min read
    </p>
  </header>

  {% if project.tasks.all %}
    <ul class="task-list">
      {% for task in project.tasks.all %}
        {% include "tasks/partials/task_card.html" with task=task %}
      {% endfor %}
    </ul>
  {% else %}
    <p>No tasks yet. <a href="{% url 'tasks:create' project_id=project.id %}">Create the first one →</a></p>
  {% endif %}

  {% if request.user == project.owner %}
    <form method="post" action="{% url 'projects:archive' project.id %}">
      {% csrf_token %}
      <button type="submit">Archive project</button>
    </form>
  {% endif %}
{% endblock %}
```

**What this demonstrates:**

| Pattern | Where |
|---------|-------|
| `{% extends %}` | Inherits the project layout |
| `{% block %}` + `block.super` | Composes the page title with the site title |
| `{% load static blog_extras %}` | Multiple libraries on one line |
| `{% include … with … %}` | Reusable task card with explicit context |
| `{% if request.user == project.owner %}` | Conditional UI based on the auth user |
| `{% csrf_token %}` | Required for the archive POST form |
| Filters (`date`, `truncatechars`, `pluralize`, custom `reading_minutes`) | Presentation logic kept out of Python |
| `{% url %}` | Every link is name-based, never hard-coded |
| `messages` from a context processor | Flash messages without manual context |

This is the templating layer of a real Django product, condensed into one screen.

---

## Summary

Today you learned:

- ✔ Templates separate **presentation from logic** — DTL is intentionally limited so business rules stay in views and models.
- ✔ Three primitives: `{{ variable }}`, `{% tag %}`, `{# comment #}`.
- ✔ `{% extends %}` + `{% block %}` is the foundation of every Django UI — write your layout once.
- ✔ `{% for %}` with `{% empty %}` and `{% if %}` cover almost every loop and condition you need.
- ✔ Filters (`|date`, `|default`, `|truncatewords`, `|pluralize`, `|length`, …) format values without touching Python.
- ✔ Always link with `{% url 'app:name' %}` and load assets with `{% static 'path' %}` after `{% load static %}`.
- ✔ Auto-escaping protects you from XSS — never disable it on user content.
- ✔ Every POST form needs `{% csrf_token %}` — Django enforces it via middleware.
- ✔ Reuse fragments with `{% include "x.html" with var=value %}`.
- ✔ Custom filters and tags live in `<app>/templatetags/` and unlock per-project formatting helpers.

### Key Takeaways

```text
✅ Nest templates in app subfolders to avoid name collisions
✅ Use {% extends %} + {% block %} for every page
✅ Trust auto-escaping; avoid |safe on user content
✅ {% csrf_token %} on every <form method="post">
✅ Use {% url 'app:name' %} — never hard-code paths
✅ Filters belong in templates; logic belongs in views
✅ Custom tags live in <app>/templatetags/<name>.py
```

### Tag and Filter Cheat Sheet

```django
{# Variables #}
{{ post.title }}                 {# attribute access #}
{{ posts|length }}               {# pipe to filter #}
{{ value|default:"—" }}          {# fallback #}
{{ value|default_if_none:"—" }}  {# fallback only on None #}

{# Tags #}
{% if condition %} … {% elif … %} … {% else %} … {% endif %}
{% for item in items %} … {% empty %} … {% endfor %}
{% url 'app:name' arg1=value %}
{% load static %}
{% static 'css/style.css' %}
{% csrf_token %}
{% include "partials/x.html" with foo=bar %}
{% extends "base.html" %}
{% block content %} … {% endblock %}
{% now "Y-m-d" %}

{# Common filters #}
|date:"M j, Y"
|time:"H:i"
|truncatewords:20
|truncatechars:160
|linebreaks
|linebreaksbr
|length
|pluralize         {# “1 post” / “2 posts” #}
|yesno:"yes,no,maybe"
|lower / |upper / |title / |capfirst
|safe              {# disables escaping — use with care #}
|escape            {# force escaping #}
```

### Glossary

| Term | Definition |
|------|------------|
| Template | Text file with `{{ }}` and `{% %}` placeholders that Django renders into HTML |
| DTL | Django Template Language — the syntax used in `.html` templates |
| Variable | `{{ name }}` — outputs an auto-escaped value |
| Tag | `{% name %}` — control flow and template logic |
| Filter | `{{ value|name:arg }}` — transforms a value before output |
| `block` / `extends` | Slots used for template inheritance |
| `include` | Renders another template inline, optionally with extra context |
| Auto-escape | Default protection against XSS — escapes `< > & " '` |
| `\|safe` | Filter that opts a value out of auto-escaping |
| `csrf_token` | Hidden field protecting POST/PUT/DELETE forms |
| Context processor | Function that adds variables to every template's context |
| Custom tag/filter | User-defined helper registered in `<app>/templatetags/` |
| Template loader | Class that finds template files (filesystem, app dirs, …) |
| `TemplateDoesNotExist` | Exception listing every path Django searched |

---

## Next Lesson Navigation

| ← Previous Lesson | Next Lesson → |
|-------------------|---------------|
| [Views and URLs](./ch04-views-urls.md) | [Forms](./ch06-forms.md) |
