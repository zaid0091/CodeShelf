---
title: Forms
description: Build, validate, and render user input safely with forms.Form and ModelForm — including CSRF, widgets, custom validation, file uploads, and formsets
order: 6
tags: [django, forms, modelform, validation, csrf]
---

# Chapter 6 — Forms

> Validate user input, render HTML, surface errors, and stay safe from CSRF — all from one Python class.
>
> **Difficulty:** Intermediate &nbsp;·&nbsp; **Estimated time:** 50 – 70 min &nbsp;·&nbsp; **Prerequisites:** [Chapter 5 — Templates](./ch05-templates.md), familiarity with `request.POST` from [Chapter 4](./ch04-views-urls.md)

---

## Learning Outcome

By the end of this lesson, you will be able to:

- ✔ Define a **`forms.Form`** with the right field types and options
- ✔ Process forms in a view with the canonical **GET-empty / POST-bound** pattern
- ✔ Use **`is_valid()`**, **`cleaned_data`**, **`clean_<field>()`**, and **`clean()`** for validation
- ✔ Render forms with `{{ form.as_p }}`, manual loops, and per-field error display
- ✔ Bind a **`ModelForm`** to a model and call `form.save()` to persist data
- ✔ Add **CSRF protection** to every POST form
- ✔ Customize **widgets** with CSS classes, placeholders, and HTML attributes
- ✔ Handle **file uploads** with `enctype="multipart/form-data"` and `request.FILES`
- ✔ Manage multiple rows at once with **formsets** and **`modelformset_factory`**
- ✔ Avoid **mass-assignment** by listing fields explicitly

---

## Visual Preview

The full lifecycle of a Django form, from empty render to validated save:

```text
GET  /contact/
        │
        ▼
   form = ContactForm()        ← unbound, no data
        │
        ▼
   render(request, "contact.html", {"form": form})
        │
        ▼
   ┌──────────────────────────────────────────┐
   │ <form method="post">                     │
   │   {% csrf_token %}                       │
   │   {{ form.as_p }}                        │
   │   <button type="submit">Send</button>    │
   │ </form>                                  │
   └──────────────────────────────────────────┘

POST /contact/   (user submits)
        │
        ▼
   form = ContactForm(request.POST)
        │
        ▼
   form.is_valid() ────── False ──▶ re-render with form.errors
        │ True
        ▼
   form.cleaned_data["email"]
        │
        ▼
   send mail / save model / redirect
```

The key insight: **the same view handles both GET and POST**, and the same form class produces the HTML, validates the data, and exposes the errors.

---

## Core Concept

### What a Form does

> **Definition — Form:** A Python class (subclass of `forms.Form`) that bundles three responsibilities: **render** HTML inputs, **validate** submitted data, and **expose** cleaned values and errors.

Without forms you'd hand-write HTML, repeat validation logic in every view, and build error UIs from scratch. Forms collapse all of that into one class.

### Bound vs. unbound

> **Definition — Unbound form:** `Form()` — no data attached, no validation runs, no errors. Rendered for the initial GET.
>
> **Definition — Bound form:** `Form(request.POST)` — data attached, ready to validate. Rendered after a failed POST.

A form **doesn't know if it's valid** until you call `form.is_valid()`. Calling `is_valid()` runs every field's validators, your `clean_<field>()` methods, and your `clean()` method, and populates `form.cleaned_data` and `form.errors`.

### Three layers of validation

1. **Field validation** — `EmailField()` checks for valid email syntax automatically.
2. **`clean_<field>()`** — your method to validate one field (e.g., reject a banned username).
3. **`clean()`** — your method to validate **across fields** (e.g., "password" must equal "password_confirm").

Each layer runs in order; `cleaned_data` only contains the values that passed.

### `Form` vs. `ModelForm`

| | **`forms.Form`** | **`forms.ModelForm`** |
|---|------------------|----------------------|
| Used for | Arbitrary input (search, contact, login) | Creating / editing model instances |
| Defines fields | Manually | Auto-generates from a model |
| Saves data | You call `Model.objects.create(...)` | `form.save()` does it for you |
| Best for | One-off forms | CRUD pages |

### CSRF in one sentence

> **Definition — CSRF (Cross-Site Request Forgery):** An attack that tricks a logged-in user into submitting a request from another origin. Django blocks it by requiring a hidden `csrfmiddlewaretoken` on every unsafe request.

Every `<form method="post">` needs `{% csrf_token %}`. AJAX POSTs need the `X-CSRFToken` header.

---

## Syntax

The minimum **`Form`** definition:

```python
from django import forms

class MyForm(forms.Form):
    field_name = forms.FieldType(<options>)
```

The minimum **`ModelForm`** definition:

```python
class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ["title", "body"]
```

The canonical **view pattern**:

```python
def my_view(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # ... use form.cleaned_data
            return redirect("success-url")
    else:
        form = MyForm()
    return render(request, "template.html", {"form": form})
```

---

## Live Code Playground

A complete contact form with validation, plus a `ModelForm` for `Post`. Drop these into the `blog` app from earlier chapters.

### `blog/forms.py`

```python
from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "Your name"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "input", "placeholder": "you@example.com"}),
    )
    subject = forms.ChoiceField(
        choices=[
            ("", "Pick a topic"),
            ("billing", "Billing"),
            ("support", "Support"),
            ("other", "Other"),
        ],
        widget=forms.Select(attrs={"class": "input"}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "input", "rows": 5}),
        min_length=10,
    )
    accept_terms = forms.BooleanField(label="I accept the terms")

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if name.lower() == "admin":
            raise ValidationError("That name is reserved.")
        return name

    def clean(self):
        cleaned = super().clean()
        subject = cleaned.get("subject")
        message = cleaned.get("message", "")
        if subject == "billing" and "invoice" not in message.lower():
            raise ValidationError(
                "For billing questions, please include an invoice number."
            )
        return cleaned


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "slug", "body", "published"]
        widgets = {
            "body": forms.Textarea(attrs={"rows": 8, "class": "input"}),
        }
        labels = {
            "body": "Post content",
        }
        help_texts = {
            "slug": "URL-friendly version of the title (lowercase, dashes).",
        }
```

### `blog/views.py`

```python
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm, PostForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # in real life: send_mail(...) or save to DB
            messages.success(request, f"Thanks {data['name']}, we'll be in touch.")
            return redirect("blog:contact")
    else:
        form = ContactForm()
    return render(request, "blog/contact.html", {"form": form})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("blog:post-detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form, "mode": "create"})


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:post-detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form, "mode": "edit"})
```

### `blog/templates/blog/contact.html`

```django
{% extends "base.html" %}
{% block title %}Contact{% endblock %}

{% block content %}
  <h1>Contact us</h1>

  <form method="post" novalidate>
    {% csrf_token %}

    {% if form.non_field_errors %}
      <div class="form-errors">
        {{ form.non_field_errors }}
      </div>
    {% endif %}

    {% for field in form %}
      <div class="form-row {% if field.errors %}has-error{% endif %}">
        {{ field.label_tag }}
        {{ field }}
        {% if field.help_text %}
          <small>{{ field.help_text }}</small>
        {% endif %}
        {% if field.errors %}
          <ul class="errors">
            {% for error in field.errors %}<li>{{ error }}</li>{% endfor %}
          </ul>
        {% endif %}
      </div>
    {% endfor %}

    <button type="submit">Send</button>
  </form>
{% endblock %}
```

> 💡 **Tip:** The `novalidate` attribute disables the browser's built-in HTML5 validation so you can test Django's server-side validation. Remove it in production if you want both layers.

---

## Step-by-Step Example

Build the **contact form** from zero so each step is testable.

### Step 1 — Create the form class

In `blog/forms.py`:

```python
from django import forms

class ContactForm(forms.Form):
    name    = forms.CharField(max_length=100)
    email   = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, min_length=10)
```

### Step 2 — Add the canonical view

```python
# blog/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)   # your real logic goes here
            return redirect("blog:contact")
    else:
        form = ContactForm()
    return render(request, "blog/contact.html", {"form": form})
```

### Step 3 — Wire the URL

```python
# blog/urls.py
path("contact/", views.contact, name="contact"),
```

### Step 4 — Render the form (quickest possible template)

```django
{% extends "base.html" %}
{% block content %}
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Send</button>
  </form>
{% endblock %}
```

### Step 5 — Submit a bad payload

Try `email = not-an-email`. Django re-renders the page with a red error next to the email field — no extra code on your part.

### Step 6 — Add a custom field validator

```python
def clean_name(self):
    name = self.cleaned_data["name"].strip()
    if name.lower() == "admin":
        raise ValidationError("That name is reserved.")
    return name
```

Submit `name = admin` → see your custom error.

### Step 7 — Add a cross-field validator

```python
def clean(self):
    cleaned = super().clean()
    if cleaned.get("name", "").lower() in cleaned.get("message", "").lower():
        raise ValidationError("Please don't include your name in the message.")
    return cleaned
```

Errors raised in `clean()` show up as **`form.non_field_errors`** — render them above the form.

### Step 8 — Switch to manual rendering

Replace `{{ form.as_p }}` with the per-field loop from the playground. You get full control over CSS classes, error placement, and help text.

---

## Try It Yourself

> **Task:** Build a **registration form** that:
>
> 1. Asks for `username`, `email`, `password`, and `password_confirm`.
> 2. Rejects usernames shorter than 3 characters or already taken (`User.objects.filter(username=...).exists()`).
> 3. Requires the password to be at least 8 characters and to **match** `password_confirm`.
> 4. Renders password fields with `forms.PasswordInput()` widgets.
> 5. On success, creates the user and redirects to `/login/`.

Hints:

- Validate the username inside `clean_username()`.
- Validate the password match inside `clean()` (it needs **two** fields, so the per-field method won't work).
- Use `User.objects.create_user(username=..., email=..., password=...)` so the password is hashed properly — never `User.objects.create()` for passwords.
- `forms.PasswordInput()` is the widget; the field is still `forms.CharField`.

Try it before peeking at the solution.

---

## Solution

<details>
<summary>Click to reveal the solution</summary>

### `accounts/forms.py`

```python
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=150)
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        label="Confirm password",
    )

    def clean_username(self):
        username = self.cleaned_data["username"].strip()
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("That username is already taken.")
        return username

    def clean(self):
        cleaned = super().clean()
        pwd = cleaned.get("password")
        confirm = cleaned.get("password_confirm")
        if pwd and confirm and pwd != confirm:
            self.add_error("password_confirm", "Passwords do not match.")
        return cleaned
```

### `accounts/views.py`

```python
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(
                username=data["username"],
                email=data["email"],
                password=data["password"],
            )
            return redirect("accounts:login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})
```

### `accounts/templates/accounts/register.html`

```django
{% extends "base.html" %}
{% block content %}
  <h1>Create an account</h1>

  <form method="post">
    {% csrf_token %}
    {{ form.non_field_errors }}
    {% for field in form %}
      <p>
        {{ field.label_tag }}
        {{ field }}
        {{ field.errors }}
      </p>
    {% endfor %}
    <button type="submit">Register</button>
  </form>
{% endblock %}
```

### Why this works

1. `clean_username()` validates **one** field — uniqueness — and runs before `clean()`.
2. `clean()` validates **two** fields together; we attach the error to `password_confirm` with `self.add_error()` so the error appears next to that field instead of in `non_field_errors`.
3. `User.objects.create_user(..., password=...)` hashes the password automatically. `User.objects.create(..., password=...)` would store it in plaintext.
4. `widget=forms.PasswordInput()` flips the `<input>` from `type="text"` to `type="password"` — the field type stays `CharField`.

</details>

---

## Key Notes & Tips

> 💡 **Tip:** `form.cleaned_data` only exists **after** `form.is_valid()` returns `True`. Calling it before is a `AttributeError` waiting to happen.

> 💡 **Tip:** When editing an existing object, pass `instance=obj` to your `ModelForm`: `PostForm(request.POST, instance=post)`. The form pre-fills with the object's current values and `save()` updates that row instead of creating a new one.

> 💡 **Tip:** For an "edit" view, the same template renders both create and edit pages — the `instance=` argument and the URL are the only differences.

> 💡 **Tip:** `form.add_error("field_name", "message")` lets you attach an error to a specific field from inside `clean()`. Use it when you need cross-field validation but want the error to appear next to a single input.

> ⚠️ **Warning:** Use `fields = [...]` on `ModelForm.Meta`, **never** `fields = "__all__"` for forms exposed to untrusted users. The latter accepts every model field, including ones you didn't intend (like `is_staff`, `owner`, `price`).

> ⚠️ **Warning:** File upload forms need **two** things: `enctype="multipart/form-data"` on the `<form>` and `request.FILES` passed to the form: `MyForm(request.POST, request.FILES)`.

> ⚠️ **Warning:** AJAX POST without the CSRF token returns **403 Forbidden**. Send the token in the `X-CSRFToken` header (read it from the `csrftoken` cookie or `{{ csrf_token }}`).

> ⚠️ **Warning:** Never `User.objects.create(password=raw_password)` — that stores the password in plain text. Use `User.objects.create_user(...)` or `user.set_password(...)` followed by `user.save()`.

---

## Common Mistakes

- ❌ **Forgetting `{% csrf_token %}`.** Every `<form method="post">` returns 403 without it.
- ❌ **Using `form.data` instead of `form.cleaned_data`.** `data` is the raw, un-validated input; `cleaned_data` is the type-cast, validated result.
- ❌ **Calling `form.cleaned_data` before `form.is_valid()`.** Always check `is_valid()` first.
- ❌ **`fields = "__all__"` on a `ModelForm` exposed to users.** Mass-assignment vulnerability — attackers can set any column.
- ❌ **Using `User.objects.create()` for new users.** That skips password hashing. Use `create_user()` or `set_password()` + `save()`.
- ❌ **Validating two fields in `clean_<field>()`.** Per-field clean only sees its own value. Cross-field validation belongs in `clean()`.
- ❌ **Forgetting `request.FILES` on file-upload forms.** The form has no idea a file was uploaded; `cleaned_data["avatar"]` will be `None`.
- ❌ **Forgetting `enctype="multipart/form-data"`.** Without it, browsers don't send file bytes.
- ❌ **Trusting `request.POST.get("price")` for important data.** Use a `Form` so the value is type-cast, validated, and rejected if missing.

---

## Mini Quiz

**Q1.** Which method should you call **before** reading `form.cleaned_data`?

- A) `form.clean()`
- B) `form.is_valid()` ✔
- C) `form.save()`
- D) `form.full_clean()`

**Q2.** Where does an error raised inside the form's `clean()` method (without `add_error`) appear?

- A) On the first field of the form
- B) In `form.non_field_errors` ✔
- C) Silently swallowed
- D) On every field

**Q3.** Which **`ModelForm`** option introduces a mass-assignment risk on user-facing forms?

- A) `fields = ["title"]`
- B) `exclude = ["created_at"]`
- C) `fields = "__all__"` ✔
- D) `widgets = {...}`

**Q4.** What two things are required to handle file uploads correctly?

- A) `enctype="multipart/form-data"` on the `<form>` and `request.FILES` passed to the form ✔
- B) `enctype="text/plain"` and `request.POST`
- C) Just `request.FILES`
- D) `enctype="application/x-www-form-urlencoded"` and `request.GET`

**Q5.** Which method correctly creates a new Django user with a hashed password?

- A) `User.objects.create(username=u, password=p)`
- B) `User(username=u, password=p).save()`
- C) `User.objects.create_user(username=u, password=p)` ✔
- D) `User.objects.bulk_create([User(username=u, password=p)])`

---

## Real World Example

A typical SaaS "post a job" form combines a `ModelForm`, file upload, custom validation, and the create-or-edit pattern.

### `jobs/models.py`

```python
class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    company_logo = models.ImageField(upload_to="logos/", blank=True)
    is_remote = models.BooleanField(default=False)
    posted_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
```

### `jobs/forms.py`

```python
from django import forms
from django.core.exceptions import ValidationError
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["title", "description", "salary_min", "salary_max",
                  "company_logo", "is_remote"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 8}),
        }

    def clean(self):
        cleaned = super().clean()
        lo, hi = cleaned.get("salary_min"), cleaned.get("salary_max")
        if lo is not None and hi is not None and lo > hi:
            self.add_error("salary_max", "Maximum salary must be ≥ minimum.")
        return cleaned

    def clean_company_logo(self):
        logo = self.cleaned_data.get("company_logo")
        if logo and logo.size > 2 * 1024 * 1024:
            raise ValidationError("Logo must be smaller than 2 MB.")
        return logo
```

### `jobs/views.py`

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import JobForm
from .models import Job


@login_required
def job_create(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect("jobs:detail", pk=job.pk)
    else:
        form = JobForm()
    return render(request, "jobs/form.html", {"form": form, "mode": "create"})


@login_required
def job_edit(request, pk):
    job = get_object_or_404(Job, pk=pk, posted_by=request.user)
    form = JobForm(request.POST or None, request.FILES or None, instance=job)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("jobs:detail", pk=job.pk)
    return render(request, "jobs/form.html", {"form": form, "mode": "edit"})
```

### Template (shared by create and edit)

```django
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.non_field_errors }}
  {% for field in form %}
    <div class="form-row">
      {{ field.label_tag }} {{ field }}
      {{ field.errors }}
    </div>
  {% endfor %}
  <button type="submit">{% if mode == "edit" %}Save changes{% else %}Post job{% endif %}</button>
</form>
```

**What this demonstrates:**

| Pattern | Where |
|---------|-------|
| Explicit `fields = [...]` on `Meta` | Prevents mass-assigning `posted_by`, `created_at` |
| Cross-field `clean()` | `salary_min ≤ salary_max` |
| Per-field `clean_<field>()` | Logo size limit (2 MB) |
| `commit=False` | Attach the current user before the row hits the database |
| `instance=job` | Same form class for both create and edit |
| `request.FILES` + `enctype="multipart/form-data"` | File upload flows |
| Owner-scoped `get_object_or_404` | Users can't edit other users' jobs |
| `@login_required` | Forms require an authenticated user |

This is the form layer of a real Django product, condensed into one screen.

---

## Summary

Today you learned:

- ✔ A **Form** bundles HTML rendering, validation, and error handling into one Python class.
- ✔ Forms are **unbound** (no data) on GET and **bound** (with `request.POST`) on POST.
- ✔ Validation runs in three layers: field validators → `clean_<field>()` → `clean()`.
- ✔ `form.cleaned_data` is the type-cast, validated result; access it **only after** `is_valid()` is true.
- ✔ A **`ModelForm`** auto-generates fields from a model and lets you persist with `form.save()` (use `commit=False` if you need to set extra fields first).
- ✔ Always pass **explicit `fields = [...]`** to a `ModelForm` to avoid mass-assignment.
- ✔ Every POST form needs **`{% csrf_token %}`**; AJAX needs the **`X-CSRFToken`** header.
- ✔ **Widgets** customize HTML attributes (`class`, `placeholder`, `rows`); the field type controls validation.
- ✔ File uploads require `enctype="multipart/form-data"` and `request.FILES`.
- ✔ **Formsets** (`formset_factory`, `modelformset_factory`) handle multiple rows in one submission.

### Key Takeaways

```text
✅ Use forms.Form for arbitrary input, ModelForm for CRUD
✅ Always check form.is_valid() before reading cleaned_data
✅ clean_<field>() for one field, clean() for cross-field
✅ Pass explicit fields=[...] on ModelForm.Meta — never "__all__"
✅ {% csrf_token %} on every POST form, X-CSRFToken on AJAX
✅ enctype="multipart/form-data" + request.FILES for uploads
✅ form.save(commit=False) when you need to set extra fields
✅ Use User.objects.create_user() — never .create() for passwords
```

### Cheat Sheet

```python
# View pattern
def my_view(request):
    if request.method == "POST":
        form = MyForm(request.POST, request.FILES)   # FILES only for uploads
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            return redirect("success")
    else:
        form = MyForm()
    return render(request, "template.html", {"form": form})

# ModelForm
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
        widgets = {"body": forms.Textarea(attrs={"rows": 8})}

# Custom validation
def clean_username(self):              # one field
    ...
def clean(self):                        # cross-field
    cleaned = super().clean()
    self.add_error("field_name", "msg")
    return cleaned

# Formset
from django.forms import modelformset_factory
PostFormSet = modelformset_factory(Post, fields=["title", "body"], extra=2)
formset = PostFormSet(request.POST or None, queryset=Post.objects.filter(...))
if formset.is_valid():
    formset.save()
```

### Glossary

| Term | Definition |
|------|------------|
| Form | Class that renders HTML, validates input, and exposes errors |
| ModelForm | Form auto-generated from a model |
| Bound form | Form constructed with submitted data (`Form(request.POST)`) |
| Unbound form | Form with no data attached (`Form()`) |
| `is_valid()` | Runs all validators and populates `cleaned_data` / `errors` |
| `cleaned_data` | Validated, type-cast values keyed by field name |
| `clean_<field>()` | Hook for validating a single field |
| `clean()` | Hook for cross-field validation |
| `add_error()` | Attaches an error to a specific field from inside `clean()` |
| `non_field_errors` | Errors raised in `clean()` without a target field |
| Widget | Controls HTML rendering of a field (input, textarea, select) |
| CSRF | Cross-Site Request Forgery — blocked by `{% csrf_token %}` |
| Mass assignment | Accepting more fields than intended (e.g., `__all__`) |
| Formset | Collection of forms processed as one submission |
| ModelFormSet | Formset bound to a queryset of model instances |
| `commit=False` | `save()` option to defer DB write so you can set more fields |

---

## Next Lesson Navigation

| ← Previous Lesson | Next Lesson → |
|-------------------|---------------|
| [Templates](./ch05-templates.md) | [Admin Panel](./ch07-admin-panel.md) |
