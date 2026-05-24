---
title: Chapter 25 — Best Practices
description: Scalable DRF project structure and security guidelines
order: 25
tags: [drf, best-practices, security, architecture]
---

# Chapter 25: Best Practices

Professional DRF projects separate concerns by **app**, split **settings by environment**, and apply **security defaults** on every endpoint.

---

## 25.1 Project Structure

```
project/
├── config/                 # Project settings
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── users/              # User management
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── permissions.py
│   │   └── tests/
│   ├── books/              # Book management
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── filters.py
│   │   ├── pagination.py
│   │   └── tests/
│   └── core/               # Shared utilities
│       ├── permissions.py
│       ├── pagination.py
│       └── exceptions.py
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env
```

| Layer | Responsibility |
|-------|----------------|
| `config/settings/` | Environment-specific configuration |
| `apps/*` | Domain logic — one bounded context per app |
| `core/` | Reusable permissions, pagination, exception handlers |

---

## 25.2 Security Best Practices

```python
# 1. Never expose sensitive fields
fields = ['id', 'title', 'price']  # Explicit, not '__all__'

# 2. Always validate input
serializer.is_valid(raise_exception=True)

# 3. Use permissions on every view
permission_classes = [IsAuthenticated]

# 4. Rate limit your API
throttle_classes = [UserRateThrottle]

# 5. Use HTTPS in production
SECURE_SSL_REDIRECT = True

# 6. Set CORS properly
CORS_ALLOWED_ORIGINS = ['https://your-frontend.com']  # Not ALLOW_ALL!

# 7. Hide debug info in production
DEBUG = False
```

### Security summary

| Practice | Why |
|----------|-----|
| Explicit `fields` | Prevents leaking `password`, internal flags |
| `raise_exception=True` | Consistent 400 responses, no silent failures |
| Permissions on every view | Default-deny; `AllowAny` only when intentional |
| Throttling | Mitigates abuse and brute-force |
| HTTPS + strict CORS | Protects tokens and blocks rogue browsers |
| `DEBUG = False` | Hides stack traces and settings |

### Interview points

- Put shared `permission_classes` in `REST_FRAMEWORK` defaults, override per view when needed.
- Store secrets in `.env` (never in git) — use `django-environ` or similar.
- Write tests for permissions and auth edge cases (Chapter 18).
