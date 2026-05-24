---
title: Static and Media Files
description: STATIC_URL, MEDIA_URL, collectstatic, serving files in dev and production
order: 10
tags: [django, static, media]
---

# Chapter 10: Static and Media Files

## 10.1 Static vs media

| Type | Source | Examples |
|------|--------|----------|
| **Static** | Developer assets | CSS, JS, images in repo |
| **Media** | User uploads | Avatars, PDFs, uploads |

Both need URL settings and different handling in [deployment](./ch12-deployment-basics.md).

## 10.2 Static files configuration

```python
# settings.py
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]       # dev extras
STATIC_ROOT = BASE_DIR / "staticfiles"           # collectstatic target
```

```text
project/
├── static/
│   └── css/
│       └── style.css
└── blog/
    └── static/
        └── blog/
            └── logo.png
```

App static files use `app/static/app/` namespace.

## 10.3 Using static in templates

```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<img src="{% static 'blog/logo.png' %}" alt="Logo">
```

Ensure `django.contrib.staticfiles` is in `INSTALLED_APPS`.

## 10.4 collectstatic

```bash
python manage.py collectstatic
```

Copies all static files to `STATIC_ROOT` for production serving via nginx/Whitenoise.

## 10.5 Media files configuration

```python
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
```

```python
# models.py
class Profile(models.Model):
    avatar = models.ImageField(upload_to="avatars/%Y/%m/")
```

```django
<img src="{{ user.profile.avatar.url }}" alt="Avatar">
```

## 10.6 Development serving

```python
# urls.py — DEBUG only
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [...]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Django dev server serves static automatically with `staticfiles`; media needs the snippet above.

## 10.7 Production serving

| File type | Served by |
|-----------|-----------|
| Static | nginx, S3, Whitenoise |
| Media | nginx, S3, CDN |

Never use Django views to serve large media at scale — use the web server or object storage.

## 10.8 Whitenoise (common pattern)

```bash
pip install whitenoise
```

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    ...
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

## 10.9 Storage backends

```python
# settings.py — S3 example (django-storages)
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_STORAGE_BUCKET_NAME = "my-bucket"
```

Abstracts local vs cloud storage behind the same model fields.

## 10.10 Security notes

- Validate uploaded file types and more than just the extension
- Set size limits
- Do not serve user uploads from the same path as static assets
- Use signed URLs for private files in cloud storage

## 10.11 Finding static files (finders)

Django collects static files using **finders**:

| Finder | Location |
|--------|----------|
| `FileSystemFinder` | `STATICFILES_DIRS` |
| `AppDirectoriesFinder` | Each app's `static/` subfolder |

```python
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
```

Run `python manage.py findstatic admin/css/base.css` to debug path resolution.

## 10.12 Cache busting in production

`CompressedManifestStaticFilesStorage` (Whitenoise or Django) hashes filenames so browsers fetch new CSS/JS after deploys:

```python
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
```

Template `{% static 'css/style.css' %}` resolves to a hashed URL automatically.

## Exercises

1. Add global CSS via `STATICFILES_DIRS` and link it in `base.html`.
2. Add an `ImageField` to a model; configure `MEDIA_*` settings.
3. Run `collectstatic` and inspect `STATIC_ROOT`.
4. Document how you would serve files in production with nginx.

## Summary

Static files ship with your code; media files are user-generated. Configure URLs and roots, use `{% static %}`, and run `collectstatic` before deployment.

## Next chapter

Continue to [Class-Based Views](./ch11-class-based-views.md).
