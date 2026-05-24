---
title: Chapter 22 — Error Handling
description: Custom DRF exception handlers for consistent API error responses
order: 22
tags: [drf, errors, exceptions, api-design]
---

# Chapter 22: Error Handling

By default, DRF returns errors in its own shape (`{"detail": "..."}` or field-keyed dicts). A **custom exception handler** wraps every error in a consistent envelope for frontends and mobile clients.

## Definitions

| Term | Meaning |
|------|---------|
| **Exception handler** | Callable registered in `REST_FRAMEWORK['EXCEPTION_HANDLER']` that converts exceptions into `Response` objects. |
| **context** | Dict passed to the handler with `view` and `request` — useful for logging. |
| **exception_handler** | DRF's built-in function that maps known exceptions to HTTP status codes. |

---

## 22.1 Custom Exception Handler

### Handler implementation

```python
# books/exceptions.py

from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_data = {
            'success': False,
            'status_code': response.status_code,
            'errors': response.data
        }
        response.data = custom_data
    else:
        response = Response({
            'success': False,
            'status_code': 500,
            'errors': {'detail': 'Internal server error'}
        }, status=500)

    return response
```

### Register in settings

```python
# config/settings.py
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'books.exceptions.custom_exception_handler',
}
```

### Example responses

**Validation error (400):**

```json
{
    "success": false,
    "status_code": 400,
    "errors": {
        "title": ["This field is required."]
    }
}
```

**Not found (404):**

```json
{
    "success": false,
    "status_code": 404,
    "errors": {
        "detail": "Not found."
    }
}
```

**Unhandled exception (500):**

```json
{
    "success": false,
    "status_code": 500,
    "errors": {
        "detail": "Internal server error"
    }
}
```

### How it works

1. Your view raises or returns an error (e.g. `serializer.is_valid(raise_exception=True)`).
2. DRF calls `exception_handler(exc, context)` first — maps `ValidationError`, `NotFound`, `PermissionDenied`, etc.
3. If it returns a `Response`, you reshape `response.data`.
4. If it returns `None` (unknown exception), you return a generic 500 envelope.

### Interview points

- Always call DRF's `exception_handler` first — do not reimplement status code logic.
- Log `exc` and `context` in the `else` branch for debugging (without exposing stack traces to clients).
- Pair with `DEBUG = False` in production so Django does not leak tracebacks.
