---
title: Deployment Basics
description: Production settings, Gunicorn, WSGI, environment variables, and hosting overview
order: 12
tags: [django, deployment, production]
---

# Chapter 12: Deployment Basics

## 12.1 Development vs production

| Aspect | Development | Production |
|--------|-------------|------------|
| `DEBUG` | `True` | **`False`** |
| Server | `runserver` | Gunicorn + nginx |
| Database | SQLite | PostgreSQL |
| Static files | Dev helpers | `collectstatic` + CDN/nginx |
| Secrets | `.env` locally | Environment variables |

## 12.2 Production settings checklist

```python
DEBUG = False
ALLOWED_HOSTS = ["example.com", "www.example.com"]

SECRET_KEY = os.environ["SECRET_KEY"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

Never commit secrets. Use `.env` locally and platform env vars in production.

## 12.3 WSGI and Gunicorn

```python
# mysite/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
application = get_wsgi_application()
```

```bash
pip install gunicorn
gunicorn mysite.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

> **Definition:** **Gunicorn** is a Python WSGI HTTP server that runs your Django app behind a reverse proxy like nginx.

## 12.4 Typical production stack

```text
Client → nginx (SSL, static) → Gunicorn (Django) → PostgreSQL
                              ↘ Redis (cache/celery)
```

## 12.5 nginx snippet (static + proxy)

```nginx
location /static/ {
    alias /var/www/staticfiles/;
}

location / {
    proxy_pass http://127.0.0.1:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```

See [Static & Media Files](./ch10-static-media-files.md).

## 12.6 Deployment checklist

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn config.wsgi:application
```

| Step | Purpose |
|------|---------|
| Install deps | Reproducible environment |
| Migrate | Apply schema |
| collectstatic | Gather CSS/JS |
| Run WSGI server | Serve application |

## 12.7 Environment variables with django-environ

```python
import environ

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(BASE_DIR / ".env")

DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
```

## 12.8 Logging

```python
LOGGING = {
    "version": 1,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}
```

Log errors to stdout for container platforms (Heroku, Railway, Fly.io).

## 12.9 Hosting options

| Platform | Notes |
|----------|-------|
| Railway / Render / Fly.io | Managed, good for side projects |
| AWS / GCP / Azure | Full control, more setup |
| DigitalOcean App Platform | Simple PaaS |
| VPS + Docker | Custom stack |

## 12.10 Health checks

```python
# simple view
from django.http import HttpResponse

def health(request):
    return HttpResponse("ok")
```

Use for load balancer probes — exclude from heavy middleware if needed.

## 12.11 Docker overview (optional)

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## Exercises

1. Split settings into `base.py`, `dev.py`, `prod.py`.
2. Run Gunicorn locally against your project.
3. List five settings that must change when `DEBUG=False`.
4. Write a deployment checklist for a PostgreSQL-backed app.

## Summary

Production Django uses `DEBUG=False`, a real database, Gunicorn/WSGI, collected static files, and secure cookies. Plan settings and secrets before your first deploy.

## Next chapter

Continue to [Best Practices](./ch13-best-practices.md).
