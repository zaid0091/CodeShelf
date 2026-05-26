---
title: Authentication
description: Identify users with Django's auth system — login, logout, password hashing, decorators, groups, permissions, and custom user models
order: 8
tags: [django, auth, authentication, permissions, users]
---

# Chapter 8 — Authentication

> Authentication answers **"who is this user?"** — authorization answers **"what are they allowed to do?"**
>
> **Difficulty:** Intermediate &nbsp;·&nbsp; **Estimated time:** 50 – 70 min &nbsp;·&nbsp; **Prerequisites:** [Chapter 6 — Forms](./ch06-forms.md), [Chapter 7 — Admin Panel](./ch07-admin-panel.md)

---

## Learning Outcome

By the end of this lesson, you will be able to:

- ✔ Use Django's built-in **`User`** model to create users with hashed passwords
- ✔ Wire up Django's built-in **`LoginView`** and **`LogoutView`** with templates
- ✔ Protect function-based views with **`@login_required`** and **`@permission_required`**
- ✔ Protect class-based views with **`LoginRequiredMixin`** and **`UserPassesTestMixin`**
- ✔ Read `request.user` and check `is_authenticated`, `is_staff`, and `is_superuser`
- ✔ Use **groups** and **per-model permissions** for role-based access
- ✔ Configure **`AUTH_USER_MODEL`** and a **custom user** based on `AbstractUser`
- ✔ Tune **password validators** in `AUTH_PASSWORD_VALIDATORS`
- ✔ Understand **sessions** and the cookies that back them
- ✔ Implement **object-level permissions** with custom checks in views

---

## Visual Preview

The full authentication flow you will build in this chapter:

```text
                     ┌────────────────────────────────────────┐
                     │           Anonymous user               │
                     └────────────────┬───────────────────────┘
                                      │ visits /dashboard/
                                      ▼
                     @login_required catches the request
                                      │
                                      ▼
                  redirected to LOGIN_URL ("/accounts/login/")
                                      │
                                      ▼
              ┌─────────────────────────────────────────┐
              │  POST /accounts/login/                  │
              │  username=ada   password=********       │
              └────────────────┬────────────────────────┘
                               │
                               ▼
                authenticate(username, password)
                               │
                               ▼
                login(request, user)  → session cookie set
                               │
                               ▼
                redirect to ?next=/dashboard/
                               │
                               ▼
                ┌─────────────────────────────────────┐
                │  GET /dashboard/                    │
                │  request.user.is_authenticated → ✓  │
                │  Hi, ada!                           │
                └─────────────────────────────────────┘
```

By the end of this lesson, the dashboard page above will be locked behind a real login, the password will be hashed with PBKDF2, the session will live in a secure cookie, and a per-row permission check will decide whether Ada can edit the resource she's viewing.

---

## Core Concept

### Authentication vs. authorization

> **Definition — Authentication:** Verifying **identity**. "Are you really Ada?" — usually answered with a username + password.
>
> **Definition — Authorization:** Verifying **permission**. "Can Ada edit this post?" — answered with permissions, groups, or custom rules.

Django ships with both layers in **`django.contrib.auth`**.

### The User model is your starting point

Every Django project gets a `User` model out of the box (`django.contrib.auth.models.User`). It has `username`, `email`, `password` (hashed), `is_active`, `is_staff`, `is_superuser`, and timestamps. Use **`User.objects.create_user(...)`** — never `User.objects.create()` — so the password gets hashed.

### `request.user` is everywhere

`AuthenticationMiddleware` attaches the current user to every request. In a view: `request.user`. In a template: `{{ user }}`. If nobody is logged in, `request.user` is an instance of `AnonymousUser` (`is_authenticated` is `False`).

### Sessions are how Django remembers you

> **Definition — Session:** A small server-side store keyed by a random ID. After login, Django sets a `sessionid` cookie; on every subsequent request it looks up the matching session row and re-attaches the user.

Sessions live in the database by default. In production, set `SESSION_COOKIE_SECURE=True` so the cookie is only sent over HTTPS.

### Permissions and groups

| | What it represents | Example |
|---|--------------------|---------|
| **Permission** | A flag like `blog.add_post` (auto-generated per model) | `user.has_perm("blog.delete_post")` |
| **Group** | A bundle of permissions you can assign to many users | `Editors` group includes `change_post`, `add_post` |

For role-based access (Editor, Admin, Reader), use groups. For one-off rules ("can the user edit *this specific* post?"), check inside the view.

### `AUTH_USER_MODEL` — set it before the first `migrate`

If you ever want to add fields to `User`, swap in a custom user **before** running migrations on a fresh database:

```python
# settings.py
AUTH_USER_MODEL = "accounts.User"
```

Switching after the first migration is painful. Always create a custom user on day one — even if you don't need extra fields yet.

---

## Syntax

The minimum auth toolbox you'll use daily:

```python
# Create a user (password is hashed automatically)
User.objects.create_user(username="ada", email="ada@x.com", password="raw")

# Verify a password
user = authenticate(request, username="ada", password="raw")    # User or None

# Log in / log out
login(request, user)                # sets session cookie
logout(request)                     # clears it

# Protect a view
@login_required
def dashboard(request):
    ...

# Check inside a view
if request.user.is_authenticated:
    ...

# Check a permission
if request.user.has_perm("blog.delete_post"):
    ...
```

In templates:

```django
{% if user.is_authenticated %}
  Hi, {{ user.username }} — <a href="{% url 'logout' %}">Log out</a>
{% else %}
  <a href="{% url 'login' %}">Log in</a>
{% endif %}
```

---

## Live Code Playground

A complete login / logout / register / protected dashboard, plus a custom user model.

### `accounts/models.py` — custom user (AbstractUser)

```python
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model — keep all built-in fields, add a few of our own."""
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True)

    def __str__(self):
        return self.username
```

### `mysite/settings.py`

```python
AUTH_USER_MODEL = "accounts.User"

LOGIN_URL          = "accounts:login"
LOGIN_REDIRECT_URL = "dashboard:home"
LOGOUT_REDIRECT_URL = "home"

# Session cookie — production hardening
SESSION_COOKIE_SECURE   = True   # set to False in dev if not on HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
     "OPTIONS": {"min_length": 10}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
```

### `accounts/forms.py`

```python
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=150)
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    confirm  = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    def clean_username(self):
        username = self.cleaned_data["username"].strip()
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("That username is taken.")
        return username

    def clean_password(self):
        pwd = self.cleaned_data["password"]
        validate_password(pwd)        # runs AUTH_PASSWORD_VALIDATORS
        return pwd

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password") != cleaned.get("confirm"):
            self.add_error("confirm", "Passwords do not match.")
        return cleaned
```

### `accounts/views.py`

```python
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import RegisterForm

User = get_user_model()


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data["username"],
                email=data["email"],
                password=data["password"],
            )
            login(request, user)                   # log them in immediately
            return redirect("dashboard:home")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "accounts/profile.html", {"user": request.user})
```

### `accounts/urls.py`

```python
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register, profile

app_name = "accounts"

urlpatterns = [
    path("login/",    CustomLoginView.as_view(),  name="login"),
    path("logout/",   CustomLogoutView.as_view(), name="logout"),
    path("register/", register,                   name="register"),
    path("profile/",  profile,                    name="profile"),
]
```

### `accounts/templates/accounts/login.html`

```django
{% extends "base.html" %}
{% block content %}
  <h1>Log in</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Log in</button>
  </form>
  <p>No account? <a href="{% url 'accounts:register' %}">Register</a></p>
{% endblock %}
```

### A protected view + per-object permission check

```python
# blog/views.py
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from .models import Post


@login_required
@permission_required("blog.change_post", raise_exception=True)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # object-level check: only the author can edit
    if post.author != request.user and not request.user.is_superuser:
        return HttpResponseForbidden("Not your post.")

    return render(request, "blog/post_form.html", {"post": post})
```

> 💡 **Tip:** Always reference the user model with `get_user_model()` — never `from django.contrib.auth.models import User`. The first works with both the default and custom user models; the second silently breaks the day you swap them.

---

## Step-by-Step Example

Build login + a protected dashboard from zero, in a fresh project.

### Step 1 — Confirm `django.contrib.auth` is installed

In `mysite/settings.py`, `INSTALLED_APPS` already includes:

```python
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
```

`MIDDLEWARE` already includes:

```python
"django.contrib.sessions.middleware.SessionMiddleware",
"django.contrib.auth.middleware.AuthenticationMiddleware",
```

### Step 2 — Create a superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

You now have one user. Log into `/admin/` to confirm it works.

### Step 3 — Wire the built-in auth URLs

```python
# mysite/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    ...
    path("accounts/", include("django.contrib.auth.urls")),
]
```

This gives you `login/`, `logout/`, `password_change/`, `password_reset/` and friends — for free.

### Step 4 — Add a login template

Django's `LoginView` looks for `registration/login.html` by default. Create it:

```text
templates/registration/login.html
```

```django
{% extends "base.html" %}
{% block content %}
  <h1>Log in</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Log in</button>
  </form>
{% endblock %}
```

### Step 5 — Configure redirects

```python
# settings.py
LOGIN_URL           = "/accounts/login/"
LOGIN_REDIRECT_URL  = "/dashboard/"
LOGOUT_REDIRECT_URL = "/"
```

### Step 6 — Build a protected view

```python
# dashboard/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request, "dashboard/home.html")
```

### Step 7 — Try the flow

1. Visit `/dashboard/` while logged out → redirected to `/accounts/login/?next=/dashboard/`.
2. Log in → redirected back to `/dashboard/`.
3. `request.user.is_authenticated` is `True`; `request.user.username` is your superuser name.

### Step 8 — Add a logout link

```django
{% if user.is_authenticated %}
  <form method="post" action="{% url 'logout' %}">
    {% csrf_token %}
    <button type="submit">Log out</button>
  </form>
{% endif %}
```

Logout in Django 5 is a **POST** — wrap it in a form so it can't be triggered by an `<img>` or `<a>`.

---

## Try It Yourself

> **Task:** Build a "**My posts**" page that:
>
> 1. Requires login.
> 2. Lists only the posts authored by the current user.
> 3. Has an **Edit** button next to each post — but only if the current user is **the author** OR is in the **`Editors`** group.
> 4. Returns **403 Forbidden** for everyone else who tries to edit (not 302 / not 404).

Hints:

- For the list, filter `Post.objects.filter(author=request.user)`.
- Check group membership with `request.user.groups.filter(name="Editors").exists()`.
- For the per-object permission, raise `PermissionDenied` from `django.core.exceptions` — Django turns it into 403 automatically.
- Use `{% if user == post.author or user.groups.all|join:',' == 'Editors' %}` is **wrong** — do the check in the view and pass a flag in the context.

Try it before peeking at the solution.

---

## Solution

<details>
<summary>Click to reveal the solution</summary>

### `blog/views.py`

```python
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from .models import Post


def _can_edit(user, post):
    return user == post.author or user.groups.filter(name="Editors").exists()


@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by("-created_at")
    return render(request, "blog/my_posts.html", {"posts": posts})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not _can_edit(request.user, post):
        raise PermissionDenied                # → 403
    # ... handle GET / POST for the edit form ...
    return render(request, "blog/post_form.html", {"post": post})
```

### `blog/templates/blog/my_posts.html`

```django
{% extends "base.html" %}
{% block content %}
  <h1>My posts</h1>
  <ul>
    {% for post in posts %}
      <li>
        <a href="{% url 'blog:post-detail' pk=post.pk %}">{{ post.title }}</a>
        — <a href="{% url 'blog:post-edit' pk=post.pk %}">Edit</a>
      </li>
    {% empty %}
      <li>You haven't written anything yet.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

### Why this works

1. **`@login_required`** stops anonymous users at the door — they hit `LOGIN_URL` with a `?next=` parameter that bounces them back after login.
2. **Filtering on `author=request.user`** in the view enforces row-level visibility. Doing this in the template (e.g., `{% if post.author == user %}`) leaks every other user's post.
3. **`PermissionDenied`** maps to a **403** response. `Http404` would falsely tell attackers "this post doesn't exist" — `PermissionDenied` is the honest answer.
4. **Group membership check** (`user.groups.filter(name="Editors").exists()`) is the canonical pattern for role-based authorization — much cleaner than custom flags on the user model.

</details>

---

## Key Notes & Tips

> 💡 **Tip:** Use **`get_user_model()`** instead of importing `User` directly. It returns whatever model `AUTH_USER_MODEL` points at — your code stays portable.

> 💡 **Tip:** When defining FKs to the user model, always use `settings.AUTH_USER_MODEL` (a string), not `User` (a class). String references avoid circular imports and respect custom user models.

> 💡 **Tip:** Set up a **custom user model** on day one of every new project — even an empty `class User(AbstractUser): pass` is enough. Adding fields later is cheap; switching the model later is brutal.

> 💡 **Tip:** **`@login_required(login_url=..., redirect_field_name=...)`** lets you customize the redirect target and the `?next=` parameter name per view.

> 💡 **Tip:** For class-based views, mix in **`LoginRequiredMixin`** as the **first** base class — `class MyView(LoginRequiredMixin, ListView):`. Order matters; mixins must come before the generic view.

> ⚠️ **Warning:** **Never** call `User.objects.create()` to make a new user — it stores the password in plain text. Always use `User.objects.create_user(...)` or `user.set_password(raw)` followed by `user.save()`.

> ⚠️ **Warning:** **Never** check `if request.user:` to test "are they logged in?" — `AnonymousUser` is truthy. Use `if request.user.is_authenticated:` instead.

> ⚠️ **Warning:** Switching `AUTH_USER_MODEL` **after** running migrations breaks every existing `auth_user` foreign key in your database. The supported workaround (drop + recreate) is OK on day one and a nightmare on day 90.

> ⚠️ **Warning:** Don't enforce row-level access in `list_filter`, templates, or query parameters — those are UI sugar. Filter the queryset in the view (or `get_queryset` for CBVs / admin) so unauthorized rows never leave the database.

---

## Common Mistakes

- ❌ **`User.objects.create(password=raw)`.** Stores the password in plain text. Use `create_user()` or `user.set_password(); user.save()`.
- ❌ **`if request.user:`** as an authentication check. `AnonymousUser` is truthy. Use `request.user.is_authenticated`.
- ❌ **Importing `User` directly** (`from django.contrib.auth.models import User`). Breaks the day you swap in a custom user. Use `get_user_model()` or `settings.AUTH_USER_MODEL`.
- ❌ **Setting `AUTH_USER_MODEL` after the first `migrate`.** Add a custom user on day one, even if it's empty.
- ❌ **Filtering rows in the template** (`{% if post.author == user %}`). Other users' posts have already been queried; you've just hidden them client-side. Filter in the view.
- ❌ **Returning 404 for permission failures.** Use `PermissionDenied` (or `HttpResponseForbidden`) so the response is honestly 403.
- ❌ **Disabling password validators in production.** Keep at least `MinimumLengthValidator` (length ≥ 10) and `CommonPasswordValidator` enabled.
- ❌ **Forgetting `SESSION_COOKIE_SECURE=True` in production.** Without it, the session cookie can be sent over plain HTTP and intercepted.
- ❌ **Using `{{ user.password }}` in a template.** Even hashed, it's a secret. Don't render it.
- ❌ **Triggering logout via `<a href="/accounts/logout/">`.** Django 5 requires logout to be a POST so it can't be CSRF'd. Use a small form.

---

## Mini Quiz

**Q1.** Which method correctly creates a new user with a hashed password?

- A) `User.objects.create(username="ada", password="raw")`
- B) `User(username="ada", password="raw").save()`
- C) `User.objects.create_user(username="ada", password="raw")` ✔
- D) `User.objects.bulk_create([...])`

**Q2.** Inside a view, how do you check if the current user is logged in?

- A) `if request.user:`
- B) `if request.user is not None:`
- C) `if request.user.is_authenticated:` ✔
- D) `if request.session["logged_in"]:`

**Q3.** What's the **safest** time to introduce a custom `AUTH_USER_MODEL`?

- A) Whenever you feel like it
- B) After running `migrate` for the first time
- C) **Before** running `migrate` for the first time, on a fresh database ✔
- D) Only in production

**Q4.** Which class should you mix into a class-based view to require authentication?

- A) `LoginRequiredMixin` ✔
- B) `RequiresLoginMixin`
- C) `AuthMixin`
- D) `UserPassesTestMixin`

**Q5.** A user tries to edit another user's post. What's the correct response?

- A) 200 OK with a hidden error
- B) 302 redirect to `/login/`
- C) 404 Not Found
- D) 403 Forbidden — raised via `PermissionDenied` ✔

---

## Real World Example

A typical multi-role SaaS combines a custom user, groups, decorators, mixins, and object-level checks.

### `accounts/models.py`

```python
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatars/", blank=True)

    @property
    def is_editor(self):
        return self.groups.filter(name="Editors").exists()

    @property
    def is_billing_admin(self):
        return self.groups.filter(name="BillingAdmins").exists()
```

### `accounts/permissions.py`

```python
from django.core.exceptions import PermissionDenied


def can_edit_post(user, post):
    if not user.is_authenticated:
        raise PermissionDenied
    if user == post.author or user.is_editor or user.is_superuser:
        return True
    raise PermissionDenied


def can_view_invoice(user, invoice):
    if not user.is_authenticated:
        raise PermissionDenied
    if invoice.tenant.has_member(user) or user.is_billing_admin:
        return True
    raise PermissionDenied
```

### Function-based views

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .permissions import can_edit_post


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    can_edit_post(request.user, post)         # raises 403 if denied
    return render(request, "blog/post_form.html", {"post": post})
```

### Class-based views

```python
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from .models import Post


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "body", "published"]
    template_name = "blog/post_form.html"

    def test_func(self):
        post = self.get_object()
        u = self.request.user
        return u == post.author or u.is_editor or u.is_superuser
```

### Template chrome

```django
<nav>
  <a href="{% url 'blog:post-list' %}">Blog</a>
  {% if user.is_authenticated %}
    <a href="{% url 'accounts:profile' %}">{{ user.username }}</a>
    {% if user.is_editor %}
      <a href="{% url 'editor:dashboard' %}">Editor</a>
    {% endif %}
    {% if user.is_billing_admin %}
      <a href="{% url 'billing:invoices' %}">Billing</a>
    {% endif %}
    <form method="post" action="{% url 'logout' %}" class="inline">
      {% csrf_token %}
      <button type="submit">Log out</button>
    </form>
  {% else %}
    <a href="{% url 'accounts:login' %}">Log in</a>
    <a href="{% url 'accounts:register' %}">Sign up</a>
  {% endif %}
</nav>
```

**What this demonstrates:**

| Pattern | Where |
|---------|-------|
| Custom user with role properties | `User.is_editor`, `User.is_billing_admin` |
| Centralized permission helpers | `accounts/permissions.py` keeps rules out of views |
| `PermissionDenied` for honest 403s | Never lies with 404 about authorization |
| `LoginRequiredMixin` + `UserPassesTestMixin` | Two mixins, one ordered list, one CBV |
| `test_func()` reuses model + group rules | Same logic as the FBV view, in one place |
| Group-driven nav | UI surface adapts to the user's role |
| POST logout via small form | Compliant with Django 5 logout policy |

This is the auth layer of a real Django product, condensed into one screen.

---

## Summary

Today you learned:

- ✔ **Authentication** = "who?"; **authorization** = "what are they allowed to do?"
- ✔ **`django.contrib.auth`** ships users, groups, permissions, login/logout views, password reset, password validators, and session middleware out of the box.
- ✔ Use `User.objects.create_user(...)` (or `set_password`) — never raw `create()` — for password hashing.
- ✔ `request.user.is_authenticated` is the right check; `if request.user:` is wrong.
- ✔ Protect FBVs with `@login_required` and `@permission_required`; protect CBVs with `LoginRequiredMixin` and `UserPassesTestMixin`.
- ✔ Define **`AUTH_USER_MODEL`** on **day one** of every project. Use `get_user_model()` and `settings.AUTH_USER_MODEL` everywhere.
- ✔ Permissions are auto-generated per model (`add_x`, `change_x`, `delete_x`, `view_x`); bundle them into **groups** for roles.
- ✔ Object-level checks belong in views — raise `PermissionDenied` for 403, not `Http404`.
- ✔ Configure `AUTH_PASSWORD_VALIDATORS` to enforce length and reject common passwords.
- ✔ Set `SESSION_COOKIE_SECURE=True` in production so session cookies travel over HTTPS only.

### Key Takeaways

```text
✅ create_user / set_password — never raw create()
✅ Always check request.user.is_authenticated
✅ Use get_user_model() and settings.AUTH_USER_MODEL
✅ Set up a custom user model on day one
✅ @login_required for FBVs, LoginRequiredMixin for CBVs
✅ Groups for roles; permissions for actions
✅ PermissionDenied → 403 (the honest answer)
✅ AUTH_PASSWORD_VALIDATORS enabled in every environment
✅ SESSION_COOKIE_SECURE=True in production
✅ Django 5 logout is a POST — wrap it in a form
```

### Auth Cheat Sheet

```python
# ── Settings ────────────────────────────────────────────────
AUTH_USER_MODEL     = "accounts.User"
LOGIN_URL           = "accounts:login"
LOGIN_REDIRECT_URL  = "dashboard:home"
LOGOUT_REDIRECT_URL = "home"

# ── Creating users ──────────────────────────────────────────
User = get_user_model()
User.objects.create_user(username="ada", email="a@x.com", password="raw")
User.objects.create_superuser(username="root", email="r@x.com", password="raw")

# ── Authenticating manually ─────────────────────────────────
user = authenticate(request, username=u, password=p)
if user is not None:
    login(request, user)
logout(request)

# ── Decorators (FBV) ────────────────────────────────────────
@login_required(login_url="accounts:login")
@permission_required("blog.change_post", raise_exception=True)
def view(request): ...

# ── Mixins (CBV) ────────────────────────────────────────────
class V(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "blog.change_post"

class V(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user == self.get_object().author

# ── Groups & permissions ────────────────────────────────────
from django.contrib.auth.models import Group, Permission
editors = Group.objects.create(name="Editors")
editors.permissions.add(Permission.objects.get(codename="change_post"))
user.groups.add(editors)
user.has_perm("blog.change_post")
user.groups.filter(name="Editors").exists()

# ── Templates ───────────────────────────────────────────────
{% if user.is_authenticated %}
  Hi, {{ user.username }}
  {% if perms.blog.change_post %} ... {% endif %}
{% endif %}
```

### Glossary

| Term | Definition |
|------|------------|
| Authentication | Verifying who a user is (typically username + password) |
| Authorization | Verifying what an authenticated user is allowed to do |
| `User` | Django's built-in user model, or a `AbstractUser`-based custom one |
| `AnonymousUser` | The user object attached to unauthenticated requests |
| `request.user` | The current user, attached by `AuthenticationMiddleware` |
| `is_authenticated` | `True` for real users, `False` for `AnonymousUser` |
| `is_staff` | Allows login to `/admin/` |
| `is_superuser` | Bypasses all permission checks |
| Session | Server-side data keyed by a cookie ID; persists login state |
| Permission | A flag like `blog.change_post`, auto-generated per model |
| Group | A named bundle of permissions assignable to many users |
| `AUTH_USER_MODEL` | Setting that points to your project's user model |
| `get_user_model()` | The portable way to fetch the active user model |
| `@login_required` | FBV decorator that enforces authentication |
| `LoginRequiredMixin` | CBV mixin that enforces authentication |
| `UserPassesTestMixin` | CBV mixin running a custom `test_func()` |
| `PermissionDenied` | Exception that produces a 403 Forbidden response |
| `PBKDF2` | Default password-hashing algorithm in Django |

---

## Next Lesson Navigation

| ← Previous Lesson | Next Lesson → |
|-------------------|---------------|
| [Admin Panel](./ch07-admin-panel.md) | [Migrations](./ch09-migrations.md) |
