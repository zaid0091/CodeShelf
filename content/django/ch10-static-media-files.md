---
title: Static and Media Files
description: Configure STATIC_URL, MEDIA_URL, FileField, collectstatic, WhiteNoise, S3 storages, cache-busting, and private uploads
order: 10
tags: [django, static, media, files, deployment]
---

# Chapter 10 — Static and Media Files

> Static files ship with your code. Media files come from your users. Get both pipelines right.
>
> **Difficulty:** Intermediate &nbsp;·&nbsp; **Estimated time:** 45 – 60 min &nbsp;·&nbsp; **Prerequisites:** [Chapter 5 — Templates](./ch05-templates.md), [Chapter 6 — Forms](./ch06-forms.md)

---

## Learning Outcome

By the end of this lesson, you will be able to:

- ✔ Articulate the difference between **static** and **media** files in one sentence
- ✔ Configure **`STATIC_URL`**, **`STATICFILES_DIRS`**, **`STATIC_ROOT`** for dev and prod
- ✔ Reference assets safely from templates with **`{% static %}`**
- ✔ Run **`collectstatic`** as part of every deploy
- ✔ Configure **`MEDIA_URL`** and **`MEDIA_ROOT`** and serve uploads in dev
- ✔ Save user uploads with **`FileField`** and **`ImageField`** (and install **Pillow**)
- ✔ Pick the right production strategy: **nginx**, **WhiteNoise**, or **S3 + django-storages**
- ✔ Cache-bust assets with **`ManifestStaticFilesStorage`** and `findstatic` to debug missing files
- ✔ Keep **private uploads** off the public internet using signed URLs or per-request views

---

## Visual Preview

The two pipelines side by side:

```text
STATIC FILES (you ship them in the repo)
┌──────────────────────────────────────────────────────────────────┐
│  blog/static/blog/style.css  ──┐                                 │
│  myproject/static/site.js    ──┼──▶ collectstatic ──▶ STATIC_ROOT│
│  accounts/static/accounts/…  ──┘                                 │
│                                                                  │
│  Template:   {% load static %}                                   │
│              <link href="{% static 'site.js' %}">                │
│  Browser:    GET /static/site.js  ──▶ nginx / WhiteNoise / CDN   │
└──────────────────────────────────────────────────────────────────┘

MEDIA FILES (users upload them at runtime)
┌──────────────────────────────────────────────────────────────────┐
│  <input type="file" name="avatar"> ──▶ Django form               │
│         │                                                        │
│         ▼                                                        │
│  request.FILES["avatar"]  ──▶  user.avatar = file (FileField)    │
│         │                                                        │
│         ▼                                                        │
│  saved to MEDIA_ROOT/avatars/2026/05/26/<uuid>.png               │
│         │                                                        │
│         ▼                                                        │
│  Template:   <img src="{{ user.avatar.url }}">                   │
│  Browser:    GET /media/avatars/…  ──▶ nginx / S3 / CDN          │
└──────────────────────────────────────────────────────────────────┘
```

By the end of this lesson, both pipelines will be configured for dev, ready for production, and protected against the most common mistakes (cached stale CSS, leaked private uploads, missing Pillow).

---

## Core Concept

### Static vs. media — the line that fixes everything

> **Definition — Static file:** A file that ships with your codebase and changes only when you deploy. CSS, JS, images, fonts, favicons, the homepage hero illustration.
>
> **Definition — Media file:** A file uploaded by users at runtime. Avatars, attachments, signed contracts, product photos.

Two different lifecycles → two different pipelines. Most static-vs-media bugs come from accidentally treating one as the other.

### `STATIC_URL`, `STATICFILES_DIRS`, `STATIC_ROOT`

| Setting | Purpose | Example |
|---------|---------|---------|
| `STATIC_URL` | URL prefix the browser hits | `"/static/"` |
| `STATICFILES_DIRS` | Source folders Django **reads** in dev | `[BASE_DIR / "static"]` |
| `STATIC_ROOT` | Output folder `collectstatic` **writes to** for production | `BASE_DIR / "staticfiles"` |

In dev, Django serves files **from `STATICFILES_DIRS` + every app's `static/` directory**. In production, you run `collectstatic` once and serve **`STATIC_ROOT`** with a real web server.

### `MEDIA_URL` and `MEDIA_ROOT`

| Setting | Purpose | Example |
|---------|---------|---------|
| `MEDIA_URL` | URL prefix for user uploads | `"/media/"` |
| `MEDIA_ROOT` | Disk location where uploads are saved | `BASE_DIR / "media"` |

`MEDIA_ROOT` is **outside** version control. Add `media/` to `.gitignore`.

### Two key tags / helpers

```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/site.css' %}">

<img src="{{ user.avatar.url }}" alt="">
```

`{% static %}` is for files **in your repo**; `obj.field.url` is for files **uploaded by users**. Mixing them is a frequent beginner bug.

### Dev `runserver` is special

When `DEBUG=True`, Django automatically serves static files. To also serve **media** in dev, you wire it up explicitly with the `static()` helper in `urls.py`. In production, **nothing in Django serves these files** — that job belongs to nginx, WhiteNoise, or S3.

---

## Syntax

The minimum **static** wiring (`settings.py`):

```python
STATIC_URL        = "/static/"
STATICFILES_DIRS  = [BASE_DIR / "static"]      # source folders (dev)
STATIC_ROOT       = BASE_DIR / "staticfiles"    # collectstatic target (prod)
```

The minimum **media** wiring (`settings.py`):

```python
MEDIA_URL  = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

Serve **media** in dev only (`mysite/urls.py`):

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your patterns ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Use **static** in templates:

```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/site.css' %}">
<script src="{% static 'js/app.js' %}"></script>
```

Use **media** on a model + template:

```python
class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", blank=True)
```

```django
{% if user.avatar %}
  <img src="{{ user.avatar.url }}" alt="{{ user.username }}">
{% endif %}
```

---

## Live Code Playground

A complete dev-ready setup with both pipelines and a working avatar upload.

### `mysite/settings.py`

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ── Static (your code) ───────────────────────────────────────
STATIC_URL       = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT      = BASE_DIR / "staticfiles"

# Cache-busting: Django 5+ uses STORAGES for backend selection
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

# ── Media (user uploads) ─────────────────────────────────────
MEDIA_URL  = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

### `mysite/urls.py`

```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",       include("blog.urls")),
]

# ⚠️ Dev only — production should serve /media/ via nginx or S3
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### `accounts/models.py` — `ImageField` + Pillow

```python
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio    = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/%Y/%m/", blank=True)
```

```bash
pip install Pillow                  # required for ImageField
python manage.py makemigrations
python manage.py migrate
```

### `accounts/forms.py` — file upload form

```python
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["bio", "avatar"]
```

### `accounts/views.py`

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import ProfileForm


@login_required
def profile_edit(request):
    if request.method == "POST":
        # Both POST data AND uploaded files are needed
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "accounts/profile_edit.html", {"form": form})
```

### `accounts/templates/accounts/profile_edit.html`

```django
{% extends "base.html" %}
{% load static %}

{% block content %}
  <h1>Edit profile</h1>

  <!-- enctype is mandatory for file uploads -->
  <form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}

    {% if user.avatar %}
      <img src="{{ user.avatar.url }}" alt="Current avatar" width="120">
    {% else %}
      <img src="{% static 'images/avatar-default.png' %}" alt="" width="120">
    {% endif %}

    <button type="submit">Save</button>
  </form>
{% endblock %}
```

### Folder layout

```text
myproject/
├── static/
│   └── images/avatar-default.png      ← shipped with code
├── media/                             ← gitignored
│   └── avatars/2026/05/<uploaded>.png ← created at runtime
├── staticfiles/                       ← collectstatic output (gitignored)
└── ...
```

> 💡 **Tip:** `upload_to="avatars/%Y/%m/"` partitions uploads by year/month so a single folder never holds millions of files. `"avatars/"` works too but doesn't scale.

---

## Step-by-Step Example

Configure both pipelines from zero in a fresh project.

### Step 1 — Set the four settings

```python
# settings.py
STATIC_URL       = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT      = BASE_DIR / "staticfiles"
MEDIA_URL        = "/media/"
MEDIA_ROOT       = BASE_DIR / "media"
```

### Step 2 — Make sure `staticfiles` is installed

`INSTALLED_APPS` must include `django.contrib.staticfiles` (Django adds it by default — verify it's still there).

### Step 3 — Create a static file and reference it

```text
static/
└── css/
    └── site.css
```

```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/site.css' %}">
```

Run `python manage.py runserver`, view-source the page, click the CSS link — you should see your stylesheet served at `/static/css/site.css`.

### Step 4 — Add a `FileField` and a form

```python
class Document(models.Model):
    title = models.CharField(max_length=200)
    file  = models.FileField(upload_to="documents/")
```

```python
class DocumentForm(forms.ModelForm):
    class Meta:
        model  = Document
        fields = ["title", "file"]
```

### Step 5 — Wire up the upload view (with `request.FILES`)

```python
def upload(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("upload-success")
    else:
        form = DocumentForm()
    return render(request, "upload.html", {"form": form})
```

### Step 6 — Set `enctype` on the form

```django
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Upload</button>
</form>
```

Forgetting `enctype="multipart/form-data"` is the #1 reason `request.FILES` is empty.

### Step 7 — Serve `/media/` in dev

```python
# mysite/urls.py
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Visit `/media/documents/<uploaded>.pdf` to confirm the file is served.

### Step 8 — Debug missing files with `findstatic`

```bash
python manage.py findstatic css/site.css
# /full/path/to/static/css/site.css
```

If `findstatic` returns nothing, the file isn't in any of `STATICFILES_DIRS` or any app's `static/` directory.

### Step 9 — Run `collectstatic` once

```bash
python manage.py collectstatic
```

Every static file from every app and every entry in `STATICFILES_DIRS` is copied into `STATIC_ROOT`. **This is the only command you run in production for static files.**

---

## Try It Yourself

> **Task:** Build an **upload-and-display gallery** at `/gallery/` where:
>
> 1. Users can upload an image (`title` + `image`) via a `ModelForm`.
> 2. The image is saved under `gallery/%Y/%m/`.
> 3. The gallery page shows every uploaded image as a thumbnail with the title.
> 4. The form correctly handles `enctype` and `request.FILES`.
> 5. In dev (`DEBUG=True`), uploaded images are served at `/media/gallery/...`.

Hints:

- Install Pillow before defining `ImageField`.
- The view's GET branch lists `Photo.objects.order_by("-created_at")`; the POST branch validates the form and redirects on success.
- In the template, use `{{ photo.image.url }}` for the file URL — never `{% static photo.image.url %}`.
- Use a single view that handles both GET (list + form) and POST (handle upload).

Try it before peeking at the solution.

---

## Solution

<details>
<summary>Click to reveal the solution</summary>

### `gallery/models.py`

```python
from django.db import models


class Photo(models.Model):
    title      = models.CharField(max_length=200)
    image      = models.ImageField(upload_to="gallery/%Y/%m/")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
```

### `gallery/forms.py`

```python
from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model  = Photo
        fields = ["title", "image"]
```

### `gallery/views.py`

```python
from django.shortcuts import redirect, render
from .forms import PhotoForm
from .models import Photo


def gallery(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("gallery:home")
    else:
        form = PhotoForm()

    photos = Photo.objects.all()
    return render(request, "gallery/home.html", {"form": form, "photos": photos})
```

### `gallery/urls.py`

```python
from django.urls import path
from . import views

app_name = "gallery"

urlpatterns = [
    path("", views.gallery, name="home"),
]
```

### `gallery/templates/gallery/home.html`

```django
{% extends "base.html" %}
{% load static %}

{% block content %}
  <h1>Gallery</h1>

  <form method="post" enctype="multipart/form-data" class="upload">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
  </form>

  <div class="grid">
    {% for photo in photos %}
      <figure>
        <img src="{{ photo.image.url }}" alt="{{ photo.title }}" width="240">
        <figcaption>{{ photo.title }}</figcaption>
      </figure>
    {% empty %}
      <p>No photos yet — upload the first one above.</p>
    {% endfor %}
  </div>
{% endblock %}
```

### What's happening

1. **`enctype="multipart/form-data"`** is what tells the browser to send file bytes; without it, `request.FILES` is empty and nothing uploads.
2. **`PhotoForm(request.POST, request.FILES)`** — both arguments are required for forms with file fields.
3. **`upload_to="gallery/%Y/%m/"`** keeps any single directory from blowing past the OS file-count limit.
4. **`{{ photo.image.url }}`** uses the storage backend to build the right URL — works the same whether files live on disk, on S3, or behind a CDN.
5. **`{% load static %}`** is for static assets shipped with the project (e.g., the default avatar) — never for user uploads.

</details>

---

## Key Notes & Tips

> 💡 **Tip:** Every app can have its own `<app>/static/<app>/...` folder. Like templates, **namespace** the path with the app name to avoid collisions: `blog/static/blog/style.css`, not `blog/static/style.css`.

> 💡 **Tip:** `python manage.py findstatic <path>` is your fastest debugging tool when a file isn't loading. It prints every absolute path Django would search.

> 💡 **Tip:** Use **`ManifestStaticFilesStorage`** in production (configured under `STORAGES["staticfiles"]` in Django 5+). It hashes filenames at `collectstatic` time so users never see stale CSS after a deploy.

> 💡 **Tip:** Every form that accepts files needs **two** things at the same time: `enctype="multipart/form-data"` on the `<form>` and `request.FILES` passed to the form constructor.

> 💡 **Tip:** For images, install **Pillow** (`pip install Pillow`). Without it, `ImageField.save()` raises `ImportError`, and `makemigrations` won't know the dimensions auto-fields are even possible.

> ⚠️ **Warning:** `collectstatic` only copies files **from** your project **to** `STATIC_ROOT`. Don't put hand-edited files in `STATIC_ROOT` — the next `collectstatic --clear` deletes them.

> ⚠️ **Warning:** `runserver` only auto-serves static files when **`DEBUG=True`**. With `DEBUG=False` you need a real server (or WhiteNoise) — otherwise every CSS/JS request returns 404.

> ⚠️ **Warning:** **Never** serve user-uploaded HTML as `text/html` from `MEDIA_URL`. Browsers will execute it. Force a content-type like `application/octet-stream` or always serve through a download-only view.

> ⚠️ **Warning:** Add `media/` and `staticfiles/` to `.gitignore`. The first contains user data; the second is regenerated on every deploy.

> ⚠️ **Warning:** Don't put **secrets** in `MEDIA_URL`. If a contract or invoice should be private, gate it behind a Django view that checks permissions and uses `FileResponse` — or use S3 + signed URLs.

---

## Common Mistakes

- ❌ **Forgetting `enctype="multipart/form-data"`.** `request.FILES` is empty and the form silently has no file.
- ❌ **Forgetting `request.FILES`** when constructing the form. The model saves with no file attached.
- ❌ **Using `{% static photo.image.url %}`.** That builds `/static/media/...` — wrong. Use plain `{{ photo.image.url }}`.
- ❌ **Skipping `pip install Pillow`** before adding an `ImageField`. Migrations won't even apply.
- ❌ **Putting `media/` inside `static/`.** They have different lifecycles — keep them separate.
- ❌ **Running `collectstatic` in development.** Don't. Run it as part of your deploy pipeline only.
- ❌ **Hard-coding `/static/site.css` in templates.** Use `{% static 'site.css' %}` so cache-busting and CDN prefixes work.
- ❌ **Leaving `DEBUG=True` in production to "make CSS load".** That leaks every secret in `settings.py` on the next traceback. Configure WhiteNoise or nginx properly instead.
- ❌ **Serving private uploads via `MEDIA_URL`.** Anyone with the URL can download the file. Use signed URLs or a permission-checked view.
- ❌ **Editing `STATIC_ROOT` directly.** It's a generated artifact — `--clear` will wipe your changes.

---

## Mini Quiz

**Q1.** Which setting tells `collectstatic` **where to write** the gathered files?

- A) `STATIC_URL`
- B) `STATICFILES_DIRS`
- C) `STATIC_ROOT` ✔
- D) `MEDIA_ROOT`

**Q2.** What's the difference between **static** and **media** files?

- A) Static is binary, media is text
- B) Static ships with your code; media is uploaded by users at runtime ✔
- C) Static lives in S3, media lives on disk
- D) They're synonyms

**Q3.** Which two things must a form include to handle file uploads correctly?

- A) `request.GET` and `enctype="application/json"`
- B) `request.FILES` and `enctype="multipart/form-data"` ✔
- C) Just `request.FILES`
- D) Just `enctype="multipart/form-data"`

**Q4.** What does **`ManifestStaticFilesStorage`** do?

- A) Encrypts every static asset
- B) Hashes filenames at `collectstatic` time so old caches expire after deploys ✔
- C) Uploads static files to S3
- D) Compresses CSS and JS

**Q5.** Where is the safest place to store **private** user uploads?

- A) Under the public `MEDIA_URL`, in a folder named `private/`
- B) In a hidden folder named with a random prefix
- C) Behind a Django view that checks permissions, or in a private S3 bucket served via signed URLs ✔
- D) Inside `STATIC_ROOT`

---

## Real World Example

A typical production stack uses **WhiteNoise** for static and **S3** for media — one server config, one cloud bucket, both ready for scale.

### `requirements/prod.txt`

```text
django>=5.0,<6.0
gunicorn
psycopg[binary]
whitenoise[brotli]
django-storages[boto3]
Pillow
```

### `mysite/settings/prod.py`

```python
from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = [os.environ["DOMAIN"]]

# ── Static (served by WhiteNoise from STATIC_ROOT) ───────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",        # ← right after security
    *MIDDLEWARE[1:],
]

STATIC_URL  = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# ── Media (served by S3 via django-storages) ─────────────────
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_BUCKET"]
AWS_S3_REGION_NAME      = os.environ["AWS_REGION"]
AWS_S3_FILE_OVERWRITE   = False
AWS_DEFAULT_ACL         = None      # private by default; objects are not world-readable

# Django 5+: per-pipeline backends
STORAGES = {
    "default": {                                            # MEDIA / FileField uploads
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {"location": "media"},
    },
    "staticfiles": {                                        # collectstatic target
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
```

### Deploy script

```bash
pip install -r requirements/prod.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput              # writes hashed files to STATIC_ROOT
gunicorn mysite.wsgi --bind 0.0.0.0:8000 --workers 4
```

### Private downloads via signed URL

```python
# documents/views.py
import boto3
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Document


@login_required
def download(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    if doc.owner != request.user and not request.user.is_superuser:
        return HttpResponseRedirect("/403/")

    s3 = boto3.client("s3", region_name=settings.AWS_S3_REGION_NAME)
    url = s3.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": settings.AWS_STORAGE_BUCKET_NAME,
            "Key":    doc.file.name,
        },
        ExpiresIn=300,        # 5 minutes
    )
    return HttpResponseRedirect(url)
```

**What this demonstrates:**

| Pattern | Where |
|---------|-------|
| Static via WhiteNoise | `WhiteNoiseMiddleware` + `CompressedManifestStaticFilesStorage` |
| Cache-busting + brotli compression | Hashed filenames + on-the-fly compression for free |
| Media via S3 | `S3Storage` with `AWS_DEFAULT_ACL=None` (private bucket) |
| Per-environment storage backends | `STORAGES` dict — different backends for static vs. media |
| Private downloads via signed URLs | `boto3.generate_presigned_url` with a 5-minute expiry |
| Owner check before signing | The view authorizes; the URL is only usable for 5 minutes anyway |

This is the static + media layer of a real Django product running on a single web node and an S3 bucket — no separate file server required.

---

## Summary

Today you learned:

- ✔ **Static** files live in your repo; **media** files are uploaded by users. Two pipelines, two settings groups.
- ✔ Static settings: `STATIC_URL` (browser path), `STATICFILES_DIRS` (dev source), `STATIC_ROOT` (prod target).
- ✔ Media settings: `MEDIA_URL` (browser path), `MEDIA_ROOT` (disk location).
- ✔ Reference repo assets with **`{% load static %}`** + **`{% static 'path' %}`**; reference uploaded files with **`obj.field.url`**.
- ✔ File upload forms always need **`enctype="multipart/form-data"`** **and** **`request.FILES`**.
- ✔ Use **`ImageField`** (with **Pillow**) for images and **`upload_to="prefix/%Y/%m/"`** to partition uploads.
- ✔ In production, **never** serve static or media from `runserver`. Use **WhiteNoise**, **nginx**, or a **CDN** for static; **S3** (or another object store) for media.
- ✔ Cache-bust with **`ManifestStaticFilesStorage`** so deploys never serve stale CSS.
- ✔ Debug missing assets with **`python manage.py findstatic <path>`**.
- ✔ Keep **private uploads** off public URLs — use signed URLs or permission-checked views.

### Key Takeaways

```text
✅ Static = your code; Media = user uploads
✅ {% static 'x' %} for code; obj.field.url for uploads
✅ enctype="multipart/form-data" + request.FILES (always together)
✅ pip install Pillow before defining ImageField
✅ collectstatic runs ONCE per deploy, in CI/CD
✅ Use ManifestStaticFilesStorage for cache-busting in prod
✅ runserver does not serve files in production — use WhiteNoise / nginx / CDN
✅ Private uploads → signed URLs or permission-checked download views
✅ media/ and staticfiles/ belong in .gitignore
```

### Settings Cheat Sheet

```python
# ── Dev settings.py ──────────────────────────────────────────
STATIC_URL       = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT      = BASE_DIR / "staticfiles"
MEDIA_URL        = "/media/"
MEDIA_ROOT       = BASE_DIR / "media"

# ── mysite/urls.py — serve /media/ in dev only ───────────────
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ── Prod with WhiteNoise + S3 (Django 5+) ────────────────────
MIDDLEWARE = ["django.middleware.security.SecurityMiddleware",
              "whitenoise.middleware.WhiteNoiseMiddleware", ...]

STORAGES = {
    "default": {                                # FileField → S3
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {"location": "media"},
    },
    "staticfiles": {                            # collectstatic → hashed + compressed
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ── Templates ────────────────────────────────────────────────
{% load static %}
<link rel="stylesheet" href="{% static 'css/site.css' %}">
<img src="{{ user.avatar.url }}" alt="">

# ── Forms ────────────────────────────────────────────────────
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
</form>
form = MyForm(request.POST, request.FILES, instance=obj)

# ── Commands ─────────────────────────────────────────────────
python manage.py findstatic css/site.css       # locate a static file
python manage.py collectstatic --noinput       # production deploy step
```

### Glossary

| Term | Definition |
|------|------------|
| Static file | File shipped with your code (CSS, JS, images, fonts) |
| Media file | File uploaded by a user at runtime |
| `STATIC_URL` | Browser-facing prefix for static files |
| `STATICFILES_DIRS` | Source folders Django reads in dev |
| `STATIC_ROOT` | Output folder where `collectstatic` writes |
| `MEDIA_URL` | Browser-facing prefix for media files |
| `MEDIA_ROOT` | Disk location where uploads are stored |
| `{% static %}` | Template tag that resolves a static URL |
| `FileField` | Model field that stores a file path |
| `ImageField` | Subclass of `FileField` that requires Pillow |
| `upload_to` | Prefix or callable that decides where the file lives |
| `request.FILES` | Dict-like of uploaded files on the request |
| `collectstatic` | Management command that gathers files into `STATIC_ROOT` |
| `findstatic` | Management command that locates a static file path |
| `ManifestStaticFilesStorage` | Cache-busting storage backend with hashed filenames |
| WhiteNoise | Middleware that serves static files in production |
| django-storages | Library providing storage backends (S3, GCS, Azure) |
| Signed URL | Time-limited URL granting access to a private object |

---

## Next Lesson Navigation

| ← Previous Lesson | Next Lesson → |
|-------------------|---------------|
| [Migrations](./ch09-migrations.md) | [Class-Based Views](./ch11-class-based-views.md) |
