---
title: Views and URLs
description: Map URLs to function-based views, work with HttpRequest and HttpResponse, return JSON, handle POST, decorate views, and customize error pages
order: 4
tags: [django, views, urls, urlconf, http]
---

# Chapter 4 — Views and URLs

> URLs route requests to views — the bridge between the browser and your Python code.
>
> **Difficulty:** Beginner → Intermediate &nbsp;·&nbsp; **Estimated time:** 40 – 55 min &nbsp;·&nbsp; **Prerequisites:** [Chapter 3 — Models and ORM](./ch03-models-orm.md)

---

## Learning Outcome

By the end of this lesson, you will be able to:

- ✔ Define **URL patterns** with `path()` and use built-in converters (`<int:>`, `<slug:>`, `<uuid:>`, `<path:>`)
- ✔ Write **function-based views** that read models, render templates, and return responses
- ✔ Read data off the **`HttpRequest`** object — `method`, `GET`, `POST`, `FILES`, `user`, `session`, `headers`
- ✔ Return different **`HttpResponse`** types — HTML, JSON, redirect, 404, custom status codes
- ✔ Use **named URLs** with `reverse()`, `{% url %}`, and the `redirect()` shortcut
- ✔ Compose URL files across apps with **`include()`** and **namespaces**
- ✔ Handle **POST** requests safely and restrict methods with `@require_http_methods`
- ✔ Apply **decorators** for auth, caching, and method restrictions
- ✔ Wire **custom 404 / 500** error pages

---

## Visual Preview

Here is the request → URL → view → response flow you will build by the end of this lesson:

```text
Browser  ──GET /blog/42/────▶  Django

                blog/urls.py
                    │
                    ▼
   path("<int:pk>/", views.post_detail, name="post-detail")
                    │
                    ▼
            views.post_detail(request, pk=42)
                    │
                    ▼
      get_object_or_404(Post, pk=42, published=True)
                    │
                    ▼
       render(request, "blog/post_detail.html", {...})
                    │
                    ▼
                HTTP 200 + HTML  ──▶  Browser
```

And what you'll be able to do in templates and Python:

```python
return redirect("blog:post-detail", pk=post.pk)
```

```django
<a href="{% url 'blog:post-detail' pk=post.pk %}">Read more</a>
```

One named URL — referenced from Python and templates without hard-coding a single `/blog/42/`.

---

## Core Concept

### What a URLconf is

> **Definition — URLconf:** A Python module — usually `urls.py` — whose top-level `urlpatterns` list maps URL patterns to view callables. Django walks this list **top to bottom** and dispatches to the first match.

### What a view is

> **Definition — View:** A Python callable that takes an `HttpRequest` and returns an `HttpResponse`. That's it. Function or class, template or JSON — every Django view follows that contract.

### Path converters keep URLs typed

Path converters (`<int:pk>`, `<slug:slug>`, `<uuid:id>`, `<path:rest>`) **capture and convert** parts of the URL into Python arguments your view receives. No more manual string parsing.

### Named URLs are non-negotiable

Always pass `name=` to `path()`. Then reference URLs by name from Python (`reverse("post-detail", kwargs={"pk": 1})`) and templates (`{% url 'post-detail' pk=1 %}`). When you rename a URL, you change it in **one** place.

### include() makes apps portable

A project's root `urls.py` should mostly `include()` each app's `urls.py`. With `namespace=`/`app_name`, the same URL name (`post-list`) can live in multiple apps without collision (`blog:post-list` vs. `shop:post-list`).

---

## Syntax

A URL pattern:

```python
path("<converter:variable>/", view_callable, name="url-name")
```

A function-based view:

```python
def view_name(request, <captured-args>):
    # ... read models, build context, etc.
    return HttpResponse(...)   # or render(...) or JsonResponse(...) or redirect(...)
```

Wiring an app's URLs into the project:

```python
# mysite/urls.py
path("blog/", include("blog.urls"))
```

That triple — **`path()` + view + `include()`** — covers 95% of Django routing.

---

## Live Code Playground

A complete blog with list, detail, search, and a JSON endpoint. Drop these files into the `blog` app you built in earlier chapters.

### `blog/views.py`

```python
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from .models import Post


def post_list(request):
    q = request.GET.get("q", "").strip()
    posts = Post.objects.filter(published=True)
    if q:
        posts = posts.filter(title__icontains=q)
    return render(request, "blog/post_list.html", {"posts": posts, "q": q})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    return render(request, "blog/post_detail.html", {"post": post})


@require_http_methods(["GET", "POST"])
def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            post = Post.objects.create(title=title, body="", slug=title.lower().replace(" ", "-"))
            return redirect("blog:post-detail", pk=post.pk)
    return render(request, "blog/post_form.html")


def post_list_json(request):
    data = list(Post.objects.filter(published=True).values("id", "title"))
    return JsonResponse(data, safe=False)
```

### `blog/urls.py`

```python
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("",                 views.post_list,      name="post-list"),
    path("create/",          views.post_create,    name="post-create"),
    path("api/posts/",       views.post_list_json, name="post-list-json"),
    path("<int:pk>/",        views.post_detail,    name="post-detail"),
]
```

### `mysite/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/",  include("blog.urls")),
]
```

### Try it

```bash
python manage.py runserver
```

| URL | What it does |
|-----|--------------|
| `/blog/` | List all published posts |
| `/blog/?q=django` | Search posts by title |
| `/blog/42/` | View post with `pk=42` (404 if missing) |
| `/blog/create/` | Form to create a new post (GET + POST) |
| `/blog/api/posts/` | JSON list of all published posts |

> 💡 **Tip:** Notice how URL order matters — `create/` and `api/posts/` must come **before** `<int:pk>/` so they don't get swallowed by the integer converter.

---

## Step-by-Step Example

Let's build the **list + detail** flow from zero so every part is testable.

### Step 1 — Add the URL pattern

In `blog/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post-list"),
]
```

### Step 2 — Write the view

In `blog/views.py`:

```python
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, "blog/post_list.html", {"posts": posts})
```

### Step 3 — Create the template

In `blog/templates/blog/post_list.html`:

```django
<h1>Posts</h1>
<ul>
  {% for post in posts %}
    <li><a href="{% url 'post-detail' pk=post.pk %}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
```

### Step 4 — Add the detail route and view

```python
# urls.py
path("<int:pk>/", views.post_detail, name="post-detail"),
```

```python
# views.py
from django.shortcuts import get_object_or_404

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    return render(request, "blog/post_detail.html", {"post": post})
```

### Step 5 — Test happy and sad paths

| URL | Expected result |
|-----|------------------|
| `/blog/` | List of published posts |
| `/blog/1/` | Detail of post 1 (if published) |
| `/blog/99999/` | **404 page** (raised by `get_object_or_404`) |
| `/blog/abc/` | **404 page** (path converter rejects non-int) |

### Step 6 — Add a query-string search

```python
def post_list(request):
    q = request.GET.get("q", "").strip()
    posts = Post.objects.filter(published=True)
    if q:
        posts = posts.filter(title__icontains=q)
    return render(request, "blog/post_list.html", {"posts": posts, "q": q})
```

Test it: `/blog/?q=django` → only posts whose title contains "django".

---

## Try It Yourself

> **Task:** Add a **tag-filtered** post list at `/blog/tag/<slug:tag>/`.
>
> Requirements:
>
> 1. Use the `<slug:tag>` path converter to capture a tag name.
> 2. Filter posts by tag (assume `Post` has a `tags` `ManyToManyField` from Chapter 3).
> 3. Add a `name="post-by-tag"` and link to it from `post_list.html` with `{% url %}`.
> 4. Return a friendly **404** if the tag doesn't exist.

Hints:

- Use `get_object_or_404(Tag, name=tag)` to validate the tag.
- Query with `Post.objects.filter(tags=tag_obj, published=True)`.
- For the template link: `{% url 'post-by-tag' tag=tag.name %}`.

Try it before peeking at the solution.

---

## Solution

<details>
<summary>Click to reveal the solution</summary>

### `blog/urls.py`

```python
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("",                  views.post_list,    name="post-list"),
    path("tag/<slug:tag>/",   views.post_by_tag,  name="post-by-tag"),
    path("<int:pk>/",         views.post_detail,  name="post-detail"),
]
```

### `blog/views.py`

```python
from django.shortcuts import render, get_object_or_404
from .models import Post, Tag


def post_by_tag(request, tag):
    tag_obj = get_object_or_404(Tag, name=tag)
    posts = Post.objects.filter(tags=tag_obj, published=True)
    return render(request, "blog/post_list.html", {"posts": posts, "tag": tag_obj})
```

### Template link

```django
{% for t in post.tags.all %}
  <a href="{% url 'blog:post-by-tag' tag=t.name %}">#{{ t.name }}</a>
{% endfor %}
```

### What's happening

1. `<slug:tag>` captures URL segments matching `[-a-zA-Z0-9_]+` and passes the value to the view as a string.
2. `get_object_or_404(Tag, name=tag)` returns a `404` if no tag matches — better than a 500 error.
3. `Post.objects.filter(tags=tag_obj)` uses the `ManyToManyField` defined on `Post` in Chapter 3.
4. The named URL `blog:post-by-tag` is used in both `redirect()` (Python) and `{% url %}` (template) — no hard-coded paths.

</details>

---

## Key Notes & Tips

> 💡 **Tip:** Always pass `name=` to every `path()`. It's free, and it future-proofs every link in your project.

> 💡 **Tip:** Use `redirect("blog:post-detail", pk=post.pk)` instead of `redirect(f"/blog/{post.pk}/")`. The string form silently breaks the day you rename the URL.

> 💡 **Tip:** `redirect()` accepts a URL name, a model instance with `get_absolute_url`, or a plain URL string — pick the named-URL form by default.

> ⚠️ **Warning:** URL patterns are matched **top to bottom**. Put **specific** routes (`create/`, `api/posts/`) **before** **catch-all** routes (`<int:pk>/`).

> ⚠️ **Warning:** `request.POST` does **not** parse JSON bodies. For JSON APIs read `request.body` and `json.loads(...)`, or use Django REST Framework.

> ⚠️ **Warning:** With `DEBUG=True`, Django shows debug pages — your custom `handler404` / `handler500` only run when `DEBUG=False`.

> 💡 **Tip:** Decorator order matters. The **bottom** decorator runs first when the request comes in. `@login_required` above `@require_POST` means "check login first, then check method".

---

## Common Mistakes

- ❌ **Hard-coding URLs in templates and Python.** `<a href="/blog/{{ post.pk }}/">` breaks the day you change the URL. Use `{% url 'blog:post-detail' pk=post.pk %}`.
- ❌ **Putting `<int:pk>/` before `create/`** in `urlpatterns`. The integer converter rejects `create`, but generic catch-alls like `<path:rest>/` will swallow everything.
- ❌ **Forgetting `app_name = "blog"`** in the app's `urls.py` when you use `namespace="blog"`. Django raises `NoReverseMatch` for `blog:post-list`.
- ❌ **Using `.get()` instead of `get_object_or_404()`.** A missing row crashes the view with a 500 error; you want a friendly 404.
- ❌ **Trusting `request.GET.get("page")` without casting.** Wrap with `int(..., default)` and bound the value so users can't pass `?page=999999999`.
- ❌ **Returning raw HTML strings from views.** Use `render()` with a template — it gives you escaping, inheritance, and a real separation of concerns.
- ❌ **Building APIs with `JsonResponse` everywhere.** For anything serious, use Django REST Framework — serializers, validation, permissions, pagination, throttling all come for free.

---

## Mini Quiz

**Q1.** Which path converter would match `/blog/hello-django/`?

- A) `<int:slug>`
- B) `<str:slug>`
- C) `<slug:slug>` ✔
- D) `<path:slug>`

**Q2.** What does `get_object_or_404(Post, pk=pk)` do when the post is missing?

- A) Returns `None`
- B) Raises `Http404` which Django turns into a 404 response ✔
- C) Raises a 500 server error
- D) Returns an empty `Post()` instance

**Q3.** What's the **correct** way to redirect to a named URL with a parameter?

- A) `redirect(f"/blog/{post.pk}/")`
- B) `redirect("post-detail", pk=post.pk)` ✔
- C) `HttpResponseRedirect("blog:post-detail")`
- D) `reverse("post-detail")`

**Q4.** What does `app_name = "blog"` in `blog/urls.py` enable?

- A) It registers the app in `INSTALLED_APPS`
- B) It namespaces URLs so you can write `reverse("blog:post-list")` ✔
- C) It sets the database table prefix
- D) Nothing — it's only used by the admin

**Q5.** In what order do decorators execute on the way **in** to a view?

- A) Top to bottom
- B) Bottom to top (the decorator closest to the function runs first) ✔
- C) Alphabetical
- D) Doesn't matter — order is irrelevant

---

## Real World Example

A typical SaaS dashboard uses every routing concept from this chapter.

### Project URLs

```python
# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/",    admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("billing/",  include("billing.urls")),
    path("api/",      include("api.urls")),
    path("",          include("dashboard.urls")),
]

handler404 = "config.views.page_not_found"
handler500 = "config.views.server_error"
```

### App URLs with namespace + mixed methods

```python
# dashboard/urls.py
from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("",                          views.home,          name="home"),
    path("projects/",                 views.project_list,  name="project-list"),
    path("projects/<uuid:id>/",       views.project_detail, name="project-detail"),
    path("projects/<uuid:id>/edit/",  views.project_edit,   name="project-edit"),
]
```

### A view that combines auth, method restriction, and a redirect

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from .models import Project


@login_required
@require_http_methods(["GET", "POST"])
def project_edit(request, id):
    project = get_object_or_404(Project, id=id, owner=request.user)

    if request.method == "POST":
        project.name = request.POST.get("name", project.name).strip()
        project.save(update_fields=["name"])
        return redirect("dashboard:project-detail", id=project.id)

    return render(request, "dashboard/project_edit.html", {"project": project})
```

**What this demonstrates:**

| Pattern | Where |
|---------|-------|
| Per-feature `urls.py` | `accounts`, `billing`, `api`, `dashboard` each own their routes |
| `<uuid:id>` converter | Type-safe URL parameter for opaque IDs |
| Namespaced reverse | `dashboard:project-detail` keeps URLs unambiguous |
| Auth + method decorators | `@login_required` + `@require_http_methods` compose cleanly |
| Owner check inside the view | Returns 404 if the project doesn't belong to the user — no info leakage |
| Custom `handler404` / `handler500` | Project-wide error pages with branded styling |

This is the routing layer of a real Django product, condensed into one screen.

---

## Summary

Today you learned:

- ✔ A **URLconf** is a `urlpatterns` list that maps paths to view callables.
- ✔ **Path converters** (`<int:>`, `<slug:>`, `<uuid:>`, `<path:>`) capture and type-cast parts of the URL.
- ✔ A **view** is just `def view(request, ...) -> HttpResponse:` — function-based or class-based, it always honors that contract.
- ✔ `render()`, `get_object_or_404()`, `redirect()`, and `JsonResponse` cover almost every response you'll need.
- ✔ **Named URLs** + `reverse()` + `{% url %}` eliminate hard-coded paths forever.
- ✔ **`include()`** mounts each app's URLs under a path prefix; `app_name` + `namespace` keep names collision-free.
- ✔ **Decorators** add auth (`@login_required`), method restrictions (`@require_http_methods`), and caching (`@cache_page`) — order matters.
- ✔ **`handler404`** and **`handler500`** customize the error pages users actually see in production.

### Key Takeaways

```text
✅ Always pass name= to every path()
✅ Use {% url %} and reverse() — never hard-code URLs
✅ Place specific routes before generic ones in urlpatterns
✅ Prefer get_object_or_404 over .get() in views
✅ Use redirect("name", kwarg=value) — not f-string URLs
✅ Namespace app URLs with app_name + namespace
✅ Restrict methods with @require_http_methods
✅ Custom 404/500 only render when DEBUG=False
```

### Command Reference

```bash
python manage.py runserver           # Start the dev server
python manage.py shell               # Test reverse() and the ORM interactively
python manage.py check               # Validate URL config and settings
python manage.py show_urls           # (with django-extensions) list every URL
python manage.py test                # Run the test suite
```

### Glossary

| Term | Definition |
|------|------------|
| URLconf | A module with a `urlpatterns` list mapping paths to views |
| `path()` | URL pattern using simple converters (`<int:>`, `<slug:>`, …) |
| `re_path()` | URL pattern using a regular expression |
| Path converter | Captures a URL segment and converts it (`<int:pk>` → `int`) |
| View | Callable that takes `HttpRequest` and returns `HttpResponse` |
| `HttpRequest` | The incoming request — `method`, `GET`, `POST`, `user`, `FILES`, `session` |
| `HttpResponse` | The outgoing response — body, status code, headers |
| `JsonResponse` | `HttpResponse` subclass that serializes Python to JSON |
| `render()` | Shortcut for `template + context → HttpResponse` |
| `get_object_or_404()` | Returns a model instance or raises `Http404` |
| `redirect()` | Shortcut that returns a 302 (or 301) response |
| `reverse()` | Builds a URL from a name and kwargs |
| Named URL | URL with `name="..."` that can be referenced by name |
| `include()` | Mounts another `urlpatterns` list under a prefix |
| Namespace | Prefix for URL names (`blog:post-list`) to avoid collisions |
| Decorator | Wrapper that adds behavior to a view (auth, method, cache) |
| `handler404` / `handler500` | Project-level callables for custom error pages |

---

## Next Lesson Navigation

| ← Previous Lesson | Next Lesson → |
|-------------------|---------------|
| [Models and ORM](./ch03-models-orm.md) | [Templates](./ch05-templates.md) |
