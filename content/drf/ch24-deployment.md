---
title: Chapter 24 — Deployment Basics
description: Production settings, requirements, and Docker for DRF APIs
order: 24
tags: [drf, deployment, docker, production]
---

# Chapter 24: Deployment Basics

Moving a DRF API to production means tightening security, pinning dependencies, and running behind a production WSGI server — often in a container.

---

## 24.1 Production Settings

```python
# config/settings.py

DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']

# Remove browsable API — JSON only
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}
```

### Additional production checklist

| Setting | Purpose |
|---------|---------|
| `SECRET_KEY` from environment | Never commit secrets |
| `DATABASES` → PostgreSQL | Robust production DB |
| `STATIC_ROOT` + `collectstatic` | Serve admin/static via CDN or whitenoise |
| `SECURE_SSL_REDIRECT = True` | Force HTTPS |
| `CORS_ALLOWED_ORIGINS` | Explicit frontend origins only |

---

## 24.2 Requirements

Freeze dependencies before deploy:

```bash
pip freeze > requirements.txt
```

Example `requirements.txt`:

```text
django==5.0
djangorestframework==3.14
djangorestframework-simplejwt==5.3
django-filter==23.5
django-cors-headers==4.3
drf-spectacular==0.27
gunicorn==21.2
psycopg2-binary==2.9
Pillow==10.2
```

Run with Gunicorn:

```bash
gunicorn config.wsgi --bind 0.0.0.0:8000 --workers 4
```

Put **Nginx** or **Caddy** in front for TLS termination, static files, and request buffering.

---

## 24.3 Docker Basics

```dockerfile
# Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000"]
```

### Typical deploy flow

1. Build image: `docker build -t myapi .`
2. Run migrations: `docker run myapi python manage.py migrate`
3. Start container with env vars (`DATABASE_URL`, `SECRET_KEY`, `ALLOWED_HOSTS`)
4. Use `docker-compose` for app + PostgreSQL + Redis

### Interview points

- Never run `runserver` in production — use **Gunicorn** + reverse proxy.
- `BrowsableAPIRenderer` exposes HTML forms — disable in production.
- Separate `settings/development.py` and `settings/production.py` (Chapter 25).
