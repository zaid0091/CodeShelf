---
title: Class-Based Views
description: Master ListView, DetailView, CreateView, UpdateView, DeleteView, and reusable mixins — the DRY way to build CRUD in Django
order: 11
tags: [django, cbv, generic-views, mixins]
---

# Chapter 11 — Class-Based Views

> Trade twelve lines of FBV boilerplate for two lines of CBV configuration — and inherit features for free.
>
> **Difficulty:** Intermediate &nbsp;·&nbsp; **Estimated time:** 50 – 70 min &nbsp;·&nbsp; **Prerequisites:** [Chapter 4 — Views and URLs](./ch04-views-urls.md), [Chapter 6 — Forms](./ch06-forms.md), [Chapter 8 — Authentication](./ch08-authentication.md)

---

## Learning Outcome

By the end of this lesson, you will be able to:

- ✔ Explain how a **class-based view** dispatches an HTTP method to a Python method
- ✔ Wire CBVs into `urls.py` with **`.as_view()`**
- ✔ Use **`ListView`** and **`DetailView`** to read data
- ✔ Use **`CreateView`**, **`UpdateView`**, and **`DeleteView`** to write data
- ✔ Override the key hooks: **`get_queryset`**, **`get_context_data`**, **`form_valid`**, **`get_success_url`**
- ✔ Compose behavior with **mixins** like `LoginRequiredMixin`, `UserPassesTestMixin`, `PermissionRequiredMixin`
- ✔ Customize **template names** and **`context_object_name`** to match your project conventions
- ✔ Trace the **method resolution flow** (`as_view → dispatch → http_method_lower → render`)
- ✔ Decide when to use a **CBV** and when to stay with an **FBV**

---

## Visual Preview

A function-based and class-based version of the same `Post` list — same output, very different code:

```text
FBV (function-based view):                CBV (class-based view):
┌────────────────────────────────────┐    ┌──────────────────────────────────┐
│ def post_list(request):            │    │ class PostListView(ListView):    │
│     posts = (                      │    │     model = Post                 │
│         Post.objects                │    │     paginate_by = 10              │
│         .filter(published=True)    │    │     context_object_name = "posts"│
│         .order_by("-created_at")   │    │                                  │
│     )                              │    │     def get_queryset(self):      │
│     paginator = Paginator(         │    │         return (                 │
│         posts, 10                  │    │             super()              │
│     )                              │    │             .get_queryset()      │
│     page = paginator.get_page(     │    │             .filter(             │
│         request.GET.get("page")    │    │                 published=True   │
│     )                              │    │             )                    │
│     return render(                 │    │             .order_by(           │
│         request,                   │    │                 "-created_at"    │
│         "blog/post_list.html",     │    │             )                    │
│         {"posts": page},           │    │         )                        │
│     )                              │    └──────────────────────────────────┘
└────────────────────────────────────┘
                                          urls.py:
                                            path("",
                                              PostListView.as_view(),
                                              name="post-list",
                                            )
```

By the end of this lesson, you'll write the right side reflexively for every standard CRUD page in your project.

---

## Core Concept

### What a class-based view is

> **Definition — Class-based view (CBV):** A view written as a Python class instead of a function. HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) map to instance methods (`get`, `post`, `put`, `delete`). You wire it into `urls.py` with the classmethod **`.as_view()`**.

The class lives, the request flows in, `dispatch()` reads the method, and the matching `get`/`post`/`...` runs. That's the entire mechanism.

### `View`, generic views, and the inheritance tree

```text
                                View
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        ▼                         ▼                         ▼
   TemplateView              ListView (read)           CreateView (write)
                                                       UpdateView
                                                       DeleteView
                                                       FormView
```

Every "generic" view (`ListView`, `DetailView`, etc.) is just `View` plus a stack of **mixins** that pre-fill the boring 80% of CRUD.

### The five generic CRUD views

| Generic view | Reads / writes | Default template | Default context |
|--------------|----------------|------------------|-----------------|
| `ListView` | Reads many | `<app>/<model>_list.html` | `object_list`, `page_obj` |
| `DetailView` | Reads one | `<app>/<model>_detail.html` | `object` |
| `CreateView` | Writes (insert) | `<app>/<model>_form.html` | `form` |
| `UpdateView` | Writes (update) | `<app>/<model>_form.html` | `form`, `object` |
| `DeleteView` | Writes (delete) | `<app>/<model>_confirm_delete.html` | `object` |

### The hooks you'll override 95% of the time

| Hook | When it runs | Use it for |
|------|--------------|------------|
| `get_queryset(self)` | Before listing or fetching a row | Filter by user, scope, status |
| `get_context_data(self, **kwargs)` | Before rendering | Add extra variables to the template |
| `form_valid(self, form)` | After validation, before save | Attach `request.user`, fire signals |
| `get_success_url(self)` | After save | Redirect to the new/updated row |
| `dispatch(self, request, *args)` | At the very top | Auth, rate-limit, custom routing |

### FBV vs. CBV in one sentence

> Use a **CBV** when you're doing one of the five CRUD shapes; use an **FBV** when the view is fundamentally bespoke and inheritance would just hide the logic.

---

## Syntax

The minimum CBV:

```python
from django.views import View
from django.http import HttpResponse


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello!")
```

Wired into `urls.py`:

```python
from django.urls import path
from .views import HelloView

urlpatterns = [
    path("hello/", HelloView.as_view(), name="hello"),
]
```

The shape of every generic CBV you'll ever write:

```python
class PostListView(LoginRequiredMixin, ListView):
    # Data
    model               = Post                          # OR set queryset/get_queryset
    queryset            = None
    context_object_name = "posts"
    paginate_by         = 10

    # Template
    template_name = "blog/post_list.html"

    # Hooks
    def get_queryset(self):
        return super().get_queryset().filter(published=True)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["popular_tags"] = Tag.objects.popular()
        return ctx
```

---

## Live Code Playground

Complete CRUD for a `Post` model — list, detail, create, update, delete — using generic CBVs.

### `blog/views.py`

```python
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


# ── List ────────────────────────────────────────────────────────────
class PostListView(ListView):
    model               = Post
    template_name       = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by         = 10

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by("-created_at")


# ── Detail ──────────────────────────────────────────────────────────
class PostDetailView(DetailView):
    model               = Post
    template_name       = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        # never return drafts on the public site
        return Post.objects.filter(published=True)


# ── Create ──────────────────────────────────────────────────────────
class PostCreateView(LoginRequiredMixin, CreateView):
    model         = Post
    fields        = ["title", "body", "published"]
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user        # attach the current user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})


# ── Update ──────────────────────────────────────────────────────────
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model         = Post
    fields        = ["title", "body", "published"]
    template_name = "blog/post_form.html"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})


# ── Delete ──────────────────────────────────────────────────────────
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model         = Post
    template_name = "blog/post_confirm_delete.html"
    success_url   = reverse_lazy("blog:post-list")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user or self.request.user.is_superuser
```

### `blog/urls.py`

```python
from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
)

app_name = "blog"

urlpatterns = [
    path("",                     PostListView.as_view(),   name="post-list"),
    path("new/",                 PostCreateView.as_view(), name="post-create"),
    path("<int:pk>/",            PostDetailView.as_view(), name="post-detail"),
    path("<int:pk>/edit/",       PostUpdateView.as_view(), name="post-update"),
    path("<int:pk>/delete/",     PostDeleteView.as_view(), name="post-delete"),
]
```

### `blog/templates/blog/post_list.html`

```django
{% extends "base.html" %}
{% block content %}
  <h1>Latest posts</h1>

  <ul>
    {% for post in posts %}
      <li>
        <a href="{% url 'blog:post-detail' pk=post.pk %}">{{ post.title }}</a>
        <small>{{ post.created_at|date:"M j, Y" }}</small>
      </li>
    {% empty %}
      <li>No posts yet.</li>
    {% endfor %}
  </ul>

  {% if is_paginated %}
    <nav class="pagination">
      {% if page_obj.has_previous %}
        <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
      {% endif %}
      Page {{ page_obj.number }} of {{ paginator.num_pages }}
      {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">Next</a>
      {% endif %}
    </nav>
  {% endif %}
{% endblock %}
```

### `blog/templates/blog/post_form.html`

```django
{% extends "base.html" %}
{% block content %}
  <h1>{% if object %}Edit post{% else %}New post{% endif %}</h1>

  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
  </form>
{% endblock %}
```

### `blog/templates/blog/post_confirm_delete.html`

```django
{% extends "base.html" %}
{% block content %}
  <h1>Delete "{{ object.title }}"?</h1>

  <form method="post">
    {% csrf_token %}
    <p>This action can't be undone.</p>
    <button type="submit">Delete</button>
    <a href="{% url 'blog:post-detail' pk=object.pk %}">Cancel</a>
  </form>
{% endblock %}
```

> 💡 **Tip:** `CreateView` and `UpdateView` share the **same** template (`<app>/<model>_form.html`) because their job is identical — render `{{ form }}` and post back. The only difference users see is the heading.

---

## Step-by-Step Example

Convert a function-based `post_list` into a class-based one, then layer features on.

### Step 1 — Start from the FBV

```python
def post_list(request):
    posts = Post.objects.filter(published=True).order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})
```

```python
# urls.py
path("", post_list, name="post-list"),
```

### Step 2 — Replace it with a `ListView`

```python
from django.views.generic import ListView


class PostListView(ListView):
    model = Post
```

```python
# urls.py
path("", PostListView.as_view(), name="post-list"),
```

`ListView` automatically:

- Queries `Post.objects.all()`.
- Renders `blog/post_list.html`.
- Passes `object_list` and `post_list` into the context.

### Step 3 — Customize the queryset

```python
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by("-created_at")
```

### Step 4 — Use a friendlier context name

```python
class PostListView(ListView):
    model               = Post
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by("-created_at")
```

Your template can now do `{% for post in posts %}` instead of `{% for post in object_list %}`.

### Step 5 — Add pagination for free

```python
class PostListView(ListView):
    model               = Post
    context_object_name = "posts"
    paginate_by         = 10

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by("-created_at")
```

The template now receives `paginator`, `page_obj`, and `is_paginated`. Add the pagination nav (see playground).

### Step 6 — Add extra context

```python
def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx["popular_tags"] = Tag.objects.popular()
    return ctx
```

`{{ popular_tags }}` is now available in the template.

### Step 7 — Lock it down with a mixin

```python
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(LoginRequiredMixin, ListView):
    ...
```

Anonymous users now hit `LOGIN_URL` with `?next=...` — same behavior as `@login_required`, no decorator stacking required.

> ⚠️ **Mixin order matters:** `LoginRequiredMixin` must come **before** the generic view. The Method Resolution Order (MRO) walks left to right, so the mixin's `dispatch` runs first.

---

## Try It Yourself

> **Task:** Build CRUD for a `Comment` model under each post:
>
> 1. List comments **for one post** at `/blog/<int:post_pk>/comments/` using `ListView`.
> 2. Create a comment via `CreateView` at `/blog/<int:post_pk>/comments/new/`. Attach `request.user` and the parent post in `form_valid`.
> 3. Allow only the **author** of a comment to delete it via `DeleteView`. Return `403` for anyone else.
> 4. After delete, redirect back to the parent post's detail page.

Hints:

- Comment list: override `get_queryset` to filter by the URL kwarg `self.kwargs["post_pk"]`.
- Create: pull the post in `form_valid` with `get_object_or_404(Post, pk=self.kwargs["post_pk"])`.
- Delete: combine `LoginRequiredMixin` + `UserPassesTestMixin`. Override `get_success_url` to return `reverse("blog:post-detail", kwargs={"pk": self.object.post_id})`.

Try it before peeking at the solution.

---

## Solution

<details>
<summary>Click to reveal the solution</summary>

### `blog/models.py` (sketch)

```python
class Comment(models.Model):
    post       = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author     = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post_id}"
```

### `blog/views.py`

```python
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView
from .models import Comment, Post


class CommentListView(ListView):
    model               = Comment
    template_name       = "blog/comment_list.html"
    context_object_name = "comments"
    paginate_by         = 25

    def get_queryset(self):
        return (
            Comment.objects
            .filter(post_id=self.kwargs["post_pk"])
            .select_related("author")
            .order_by("-created_at")
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["post"] = get_object_or_404(Post, pk=self.kwargs["post_pk"])
        return ctx


class CommentCreateView(LoginRequiredMixin, CreateView):
    model         = Comment
    fields        = ["body"]
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post   = get_object_or_404(Post, pk=self.kwargs["post_pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.kwargs["post_pk"]})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model         = Comment
    template_name = "blog/comment_confirm_delete.html"

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.post_id})
```

### `blog/urls.py`

```python
urlpatterns += [
    path("<int:post_pk>/comments/",
         CommentListView.as_view(),   name="comment-list"),
    path("<int:post_pk>/comments/new/",
         CommentCreateView.as_view(), name="comment-create"),
    path("comments/<int:pk>/delete/",
         CommentDeleteView.as_view(), name="comment-delete"),
]
```

### Why this works

1. **`self.kwargs["post_pk"]`** is how a CBV reads URL captures — the same converters from Chapter 4.
2. **`form_valid`** is the right hook to attach foreign keys — `super().form_valid(form)` calls `form.save()` and triggers `get_success_url()`.
3. **`UserPassesTestMixin.test_func`** returns `True` only for the comment's author, producing a clean **403** for anyone else (because of `raise_exception=True`-equivalent default behavior on test failure).
4. **`select_related("author")`** kills the N+1 problem when the template prints `{{ comment.author.username }}` for every row.
5. **`reverse_lazy`** vs. **`reverse`**: use `reverse_lazy` for **class-level** attributes (`success_url = reverse_lazy(...)`), use `reverse` inside **methods** (`return reverse(...)`).

</details>

---

## Key Notes & Tips

> 💡 **Tip:** Default template names follow the pattern **`<app>/<model>_<verb>.html`** — e.g., `blog/post_list.html`, `blog/post_detail.html`, `blog/post_form.html`, `blog/post_confirm_delete.html`. Use them and stop fighting the framework.

> 💡 **Tip:** `ListView` provides three context variables: **`object_list`**, **`<model>_list`** (e.g., `post_list`), and your custom **`context_object_name`**. Pick one and stay consistent.

> 💡 **Tip:** Use **`reverse_lazy`** for class-level attributes (`success_url = reverse_lazy(...)`), and plain **`reverse`** inside methods. The lazy version delays URL resolution until the URL conf is loaded.

> 💡 **Tip:** Override **`get_queryset`** instead of setting `queryset` when the result depends on the request (`self.request.user`, `self.kwargs`).

> 💡 **Tip:** Use Django's CBV docs at [ccbv.co.uk](https://ccbv.co.uk/) to see every method, attribute, and inheritance chain for any class-based view.

> ⚠️ **Warning:** **Mixin order matters.** Authentication mixins (`LoginRequiredMixin`, `UserPassesTestMixin`, `PermissionRequiredMixin`) must come **before** the generic view: `class V(LoginRequiredMixin, ListView)`. The Method Resolution Order walks left to right.

> ⚠️ **Warning:** `CreateView`/`UpdateView` with a model include **`fields = "__all__"`** is dangerous — same mass-assignment risk as `ModelForm`. Always pass an explicit list.

> ⚠️ **Warning:** Django 5+ requires **POST** for `LogoutView` and `DeleteView`. Linking from `<a href>` won't trigger them — use a small `<form method="post">`.

> ⚠️ **Warning:** Setting `success_url` (a string) and `get_success_url` (a method) at the same time is harmless but confusing. Pick one.

> 💡 **Tip:** `View.as_view()` accepts attribute overrides — `MyView.as_view(template_name="custom.html")` — handy for one-off URL configs without subclassing.

---

## Common Mistakes

- ❌ **Forgetting `.as_view()` in `urlpatterns`.** `path("", PostListView, ...)` fails because Django needs a callable; `PostListView.as_view()` returns the wrapped callable.
- ❌ **Putting the mixin **after** the generic view** (`class V(ListView, LoginRequiredMixin)`). The MRO no longer fires the auth check first; anonymous users sneak in.
- ❌ **Using `reverse()` at class level.** `success_url = reverse("post-list")` runs at import time, when the URL conf may not be loaded. Use `reverse_lazy`.
- ❌ **Setting `model = Post` and `queryset = Post.objects.all()` and `get_queryset(...)` all at once.** Pick one. The general rule: `get_queryset` wins over `queryset`, which wins over `model`.
- ❌ **Returning the wrong type from `form_valid`.** It must return `super().form_valid(form)` (which redirects) or your own `HttpResponseRedirect`. Returning `None` or a model instance crashes.
- ❌ **`fields = "__all__"`** on user-facing CBVs. Mass-assignment risk — pass an explicit list.
- ❌ **Triggering `DeleteView` via GET.** Django's `DeleteView` only deletes on **POST**. The GET handler renders the confirm template.
- ❌ **Subclassing `ListView` for a single object.** Use `DetailView`. Subclassing `DetailView` to render a list. Use `ListView`. Pick the verb that matches the verb you're doing.
- ❌ **Confusing `dispatch` with `get`.** `dispatch` is the entry point that calls `get`/`post`/...; override it for cross-method logic (auth, rate-limit). For just-`GET` work, override `get` instead.
- ❌ **Hand-rolling everything in a `View` subclass when a generic view would do.** That's a CBV with all the awkwardness and none of the upside. Use `ListView`, `DetailView`, etc., when the verb fits.

---

## Mini Quiz

**Q1.** What does **`.as_view()`** return when used in `urlpatterns`?

- A) The class itself
- B) A callable that creates an instance and dispatches the request ✔
- C) A `Promise` resolved at request time
- D) A subclass with `request` baked in

**Q2.** Which order is correct for combining mixins with a generic view?

- A) `class V(ListView, LoginRequiredMixin):`
- B) `class V(LoginRequiredMixin, ListView):` ✔
- C) Order doesn't matter
- D) `class V(View, ListView, LoginRequiredMixin):`

**Q3.** Inside a `CreateView`, where should you attach `request.user` to the new instance?

- A) `dispatch()`
- B) `get_context_data()`
- C) `form_valid(self, form)` — set `form.instance.author = self.request.user` then return `super().form_valid(form)` ✔
- D) `get_queryset()`

**Q4.** What's the **default template name** for `PostUpdateView` (model `Post`, app `blog`)?

- A) `blog/post_update.html`
- B) `blog/post_form.html` ✔
- C) `blog/post_detail.html`
- D) `blog/post_edit.html`

**Q5.** Which helper should you use for the **`success_url`** class attribute?

- A) `reverse(...)`
- B) `reverse_lazy(...)` ✔
- C) `redirect(...)`
- D) `resolve_url(...)`

---

## Real World Example

A SaaS dashboard typically wires every CRUD page through a generic CBV stack — auth + permission + CBV + mixins + tests.

### `projects/views.py`

```python
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProjectForm
from .models import Project


class OwnerScopedMixin:
    """
    Reusable mixin: returns only objects owned by the current user
    unless they are a superuser.
    """

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_superuser:
            return qs
        return qs.filter(owner=self.request.user)


class ProjectListView(LoginRequiredMixin, OwnerScopedMixin, ListView):
    model               = Project
    template_name       = "projects/list.html"
    context_object_name = "projects"
    paginate_by         = 25
    ordering            = ["-created_at"]


class ProjectDetailView(LoginRequiredMixin, OwnerScopedMixin, DetailView):
    model         = Project
    template_name = "projects/detail.html"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model         = Project
    form_class    = ProjectForm
    template_name = "projects/form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f"'{self.object.name}' created.")
        return response

    def get_success_url(self):
        return reverse_lazy("projects:detail", kwargs={"pk": self.object.pk})


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model         = Project
    form_class    = ProjectForm
    template_name = "projects/form.html"

    def test_func(self):
        return self.get_object().owner == self.request.user

    def get_success_url(self):
        return reverse_lazy("projects:detail", kwargs={"pk": self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model         = Project
    template_name = "projects/confirm_delete.html"
    success_url   = reverse_lazy("projects:list")

    def test_func(self):
        return self.get_object().owner == self.request.user
```

### `projects/urls.py`

```python
from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path("",                       views.ProjectListView.as_view(),   name="list"),
    path("new/",                   views.ProjectCreateView.as_view(), name="create"),
    path("<int:pk>/",              views.ProjectDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/",         views.ProjectUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/",       views.ProjectDeleteView.as_view(), name="delete"),
]
```

**What this demonstrates:**

| Pattern | Where |
|---------|-------|
| Reusable scoping mixin | `OwnerScopedMixin` — applied to list and detail views |
| MRO-correct order | `LoginRequiredMixin, OwnerScopedMixin, ListView` |
| Explicit `form_class` | Uses the validation rules in `ProjectForm` |
| `form_valid` to attach user | One-line ownership assignment |
| Flash message via `messages` | UX feedback on create |
| `test_func` for object-level auth | Update and delete are owner-scoped |
| `success_url` vs. `get_success_url` | Static URL vs. dynamic URL |
| `reverse_lazy` everywhere class-level | Avoids "URL conf not loaded" issues |
| Tiny `urls.py` | Five lines for full CRUD |

This is the view layer of a real Django product, condensed into one screen.

---

## Summary

Today you learned:

- ✔ A **CBV** is a class whose HTTP method handlers (`get`, `post`, ...) are dispatched by `dispatch()`.
- ✔ Wire CBVs into URLs with **`.as_view()`** — never the class directly.
- ✔ The five generic CRUD views — **`ListView`**, **`DetailView`**, **`CreateView`**, **`UpdateView`**, **`DeleteView`** — cover 95% of pages.
- ✔ Override **`get_queryset`** for filtering, **`get_context_data`** for extra context, **`form_valid`** for save-time logic, **`get_success_url`** for redirects.
- ✔ **Mixins** like `LoginRequiredMixin` and `UserPassesTestMixin` add behavior — but their **order matters**: mixins **before** the generic view.
- ✔ Default templates follow `<app>/<model>_<verb>.html`; default context includes `object`, `object_list`, and a `<model>_<verb>` alias.
- ✔ Use **`reverse_lazy`** at class level, **`reverse`** inside methods.
- ✔ Use **CBV** for standard CRUD; stay with **FBV** for bespoke flows.
- ✔ Django 5+ requires `DeleteView` to be triggered via **POST** — wrap in a `<form>`.

### Key Takeaways

```text
✅ HTTP methods → instance methods (get, post, …)
✅ .as_view() in urlpatterns — never the class itself
✅ Override get_queryset / get_context_data / form_valid / get_success_url
✅ Mixin order: auth/permission BEFORE the generic view
✅ Default templates: <app>/<model>_<verb>.html
✅ reverse_lazy at class level, reverse inside methods
✅ form_valid: form.instance.x = ...; return super().form_valid(form)
✅ fields = ["..."] (explicit) — never fields = "__all__" on user-facing CBVs
✅ DeleteView is POST-only — never <a href>
✅ Use FBV when CBV inheritance hides more than it helps
```

### CBV Cheat Sheet

```python
# ── Generic views ───────────────────────────────────────────
class XListView(ListView):
    model               = X
    queryset            = X.objects.published()      # OR
    paginate_by         = 25
    ordering            = ["-created_at"]
    context_object_name = "items"
    template_name       = "x/x_list.html"            # default

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["extra"] = ...
        return ctx


class XDetailView(DetailView):
    model         = X
    template_name = "x/x_detail.html"                # default
    pk_url_kwarg  = "pk"                             # or slug_url_kwarg


class XCreateView(LoginRequiredMixin, CreateView):
    model         = X
    fields        = ["title", "body"]                # or form_class = XForm
    template_name = "x/x_form.html"                  # default

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("x:detail", kwargs={"pk": self.object.pk})


class XUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model         = X
    fields        = ["title", "body"]
    template_name = "x/x_form.html"

    def test_func(self):
        return self.get_object().owner == self.request.user


class XDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model         = X
    success_url   = reverse_lazy("x:list")
    template_name = "x/x_confirm_delete.html"        # default

    def test_func(self):
        return self.get_object().owner == self.request.user


# ── URL ─────────────────────────────────────────────────────
path("<int:pk>/edit/", XUpdateView.as_view(), name="x-update")


# ── Common mixins ───────────────────────────────────────────
LoginRequiredMixin             # require auth
PermissionRequiredMixin        # permission_required = "app.codename"
UserPassesTestMixin            # override test_func(self)


# ── Method flow ─────────────────────────────────────────────
url → as_view() → __init__ → dispatch(request) → http_method_lower(request)
                                                  ├ get_queryset
                                                  ├ get_object (detail/update/delete)
                                                  ├ get_form (create/update)
                                                  ├ form_valid / form_invalid
                                                  ├ get_context_data
                                                  └ render_to_response
```

### Glossary

| Term | Definition |
|------|------------|
| Class-based view | View written as a class; HTTP methods map to instance methods |
| `.as_view()` | Classmethod that returns a callable for `urlpatterns` |
| `View` | Root CBV class — bare-bones method dispatch |
| Generic view | CBV with mixins pre-applied (e.g., `ListView`) |
| Mixin | Class providing reusable behavior (`LoginRequiredMixin`, …) |
| `get_queryset` | Hook returning the QuerySet for list/detail views |
| `get_context_data` | Hook adding extra variables to the template context |
| `form_valid` | Hook called after form validation passes |
| `get_success_url` | Method returning the redirect URL after a successful write |
| `dispatch` | Entry point that picks the HTTP-method handler |
| `context_object_name` | Friendly name for the object/queryset in the template |
| `paginate_by` | Page size for `ListView` |
| `pk_url_kwarg` | URL kwarg used to look up the object (default `"pk"`) |
| `slug_url_kwarg` | URL kwarg for slug lookup |
| `template_name` | Override for the default template path |
| `success_url` | Static class-level redirect URL (use `reverse_lazy`) |
| `MRO` | Method Resolution Order — controls mixin precedence |
| `reverse_lazy` | Lazy URL builder for class-level attributes |
| FBV | Function-based view |

---

## Next Lesson Navigation

| ← Previous Lesson | Next Lesson → |
|-------------------|---------------|
| [Static and Media Files](./ch10-static-media-files.md) | [Deployment Basics](./ch12-deployment-basics.md) |
