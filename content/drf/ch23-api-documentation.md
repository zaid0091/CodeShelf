---
title: Chapter 23 — API Documentation (Swagger)
description: OpenAPI docs and Swagger UI with drf-spectacular
order: 23
tags: [drf, swagger, openapi, drf-spectacular]
---

# Chapter 23: API Documentation (Swagger)

Interactive API docs help frontend teams and external consumers discover endpoints, request bodies, and response schemas. **drf-spectacular** generates **OpenAPI 3** schemas from your DRF views and serializers.

## Definitions

| Term | Meaning |
|------|---------|
| **OpenAPI** | Standard format (YAML/JSON) describing REST APIs. |
| **Swagger UI** | Browser UI that renders OpenAPI and lets you try requests. |
| **drf-spectacular** | Third-party package that replaces deprecated `coreapi` schema generation. |
| **Schema view** | Endpoint that serves the raw OpenAPI document (`/api/schema/`). |

---

## Installation

```bash
pip install drf-spectacular
```

---

## Configuration

```python
# config/settings.py
INSTALLED_APPS = [
    # ...
    'drf_spectacular',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Bookstore API',
    'VERSION': '1.0.0',
}
```

---

## URL routes

```python
# config/urls.py
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # ... your API routes ...
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]
```

Visit **http://127.0.0.1:8000/api/docs/** for interactive documentation.

---

## Optional enhancements

```python
# On a ViewSet — customize operation summary
from drf_spectacular.utils import extend_schema

class BookViewSet(viewsets.ModelViewSet):
    @extend_schema(summary='List all books', tags=['Books'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
```

| Endpoint | Purpose |
|----------|---------|
| `/api/schema/` | Raw OpenAPI JSON/YAML |
| `/api/docs/` | Swagger UI |
| `/api/redoc/` | ReDoc UI (add `SpectacularRedocView`) |

### Interview points

- OpenAPI is generated from **serializers** and **view introspection** — keep serializers accurate.
- Disable or protect `/api/docs/` in production (auth or IP allowlist).
- `drf-spectacular` is the modern choice over `drf-yasg` for new projects.
