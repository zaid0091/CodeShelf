---
title: Chapter 13 — Throttling
description: Rate limiting API requests with DRF throttle classes
order: 13
tags: [drf, throttling, rate-limiting, security]
---

# Chapter 13: Throttling

**Throttling** limits how often a client may call an API within a time window. Unlike **permissions** (whether you may access a resource), throttling answers **how often** you may request.

## Definitions

| Term | Meaning |
|------|---------|
| **Throttle** | Rate limiter that delays or rejects excess requests. |
| **Rate** | String like `'100/hour'`, `'10/minute'`, `'1000/day'`. |
| **Scope** | Named bucket for scoped throttles (e.g. `'uploads'`). |
| **Cache** | Throttle state is stored in Django's cache framework. |

---

## 13.1 Why Throttling

Use throttling to:

- Prevent **abuse** and brute-force attacks (login, OTP).
- Protect **server resources** (DB, CPU, third-party quotas).
- Enforce **fair usage** on multi-tenant or public APIs.
- Comply with **SLA tiers** (free vs paid rate limits).

Throttling runs **after** authentication — you can throttle per user, per IP, or per API key.

```python
# When throttled, DRF returns:
# HTTP 429 Too Many Requests
# {
#     "detail": "Request was throttled. Expected available in 42 seconds."
# }
```

### Throttling vs permissions

| | Permissions | Throttling |
|---|-------------|------------|
| Question | Can you do this? | How often? |
| Failure code | 403 Forbidden | 429 Too Many Requests |
| Typical use | Role-based access | Rate limits |

### Interview points

- Throttles use **Django cache** — use Redis in production for consistent limits across workers.
- Throttling is checked **per view** before the main handler runs.
- Does not replace **network-level** rate limiting (nginx, API gateway) — complement it.

---

## 13.2 Setting Up Throttling

### Global defaults

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day',
    },
}
```

Ensure cache is configured:

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

### Built-in throttle classes

| Class | Identifies client by |
|-------|----------------------|
| `AnonRateThrottle` | IP address (unauthenticated) |
| `UserRateThrottle` | User PK (authenticated) |
| `ScopedRateThrottle` | User + scope string from view |

### Per-view throttling

```python
from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
```

### Scoped throttle

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'anon': '20/minute',
        'user': '60/minute',
        'uploads': '10/hour',
    },
}
```

```python
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView

class FileUploadView(APIView):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'uploads'

    def post(self, request):
        ...
```

### Disable throttling on a view

```python
class HealthCheckView(APIView):
    throttle_classes = []  # no throttling

    def get(self, request):
        return Response({'status': 'ok'})
```

### Testing throttles

```python
from django.core.cache import cache
from rest_framework.test import APIClient

def test_throttle():
    cache.clear()
    client = APIClient()
    for _ in range(100):
        response = client.get('/api/products/')
    assert response.status_code in (200, 429)
```

### Interview points

- Rate format: **`number/period`** — `s`, `sec`, `m`, `min`, `h`, `hour`, `d`, `day`.
- Multiple throttle classes: **all** must allow the request (most restrictive wins).
- `ScopedRateThrottle` requires `throttle_scope` on the view and matching key in `DEFAULT_THROTTLE_RATES`.

---

## 13.3 Custom Throttle Classes

Subclass `SimpleRateThrottle` or `UserRateThrottle` and implement `get_cache_key()`.

### Throttle by API key header

```python
from rest_framework.throttling import SimpleRateThrottle

class APIKeyRateThrottle(SimpleRateThrottle):
    scope = 'api_key'

    def get_cache_key(self, request, view):
        api_key = request.headers.get('X-API-Key')
        if not api_key:
            return None  # skip this throttle
        return self.cache_format % {
            'scope': self.scope,
            'ident': api_key,
        }
```

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'api_key': '5000/day',
    },
}
```

### Premium user higher limits

```python
class TieredUserRateThrottle(UserRateThrottle):
    def get_rate(self):
        user = self.request.user
        if user.is_authenticated and getattr(user, 'is_premium', False):
            return '10000/day'
        return '1000/day'

    def allow_request(self, request, view):
        self.rate = self.get_rate()
        self.num_requests, self.duration = self.parse_rate(self.rate)
        return super().allow_request(request, view)
```

### Burst + sustained (conceptual pattern)

```python
class BurstRateThrottle(SimpleRateThrottle):
    scope = 'burst'

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)
        return self.cache_format % {'scope': self.scope, 'ident': ident}
```

```python
# settings.py — apply burst on sensitive views only
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'burst': '5/minute',
        'login': '5/minute',
    },
}
```

```python
class LoginView(APIView):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'login'
```

### `wait()` and Retry-After

When throttled, `Throttle.wait()` returns seconds until the next allowed request — used in the `429` response message.

### Interview points

- `get_cache_key()` returning **None** skips that throttle for the request.
- Custom throttles must call **`parse_rate()`** if you override `get_rate()` dynamically.
- For distributed systems, share **Redis** cache; locmem breaks limits across processes.
- Combine with **authentication** so anonymous users get stricter `anon` limits.

---

## Chapter summary

1. Configure **DEFAULT_THROTTLE_CLASSES** and **DEFAULT_THROTTLE_RATES**.
2. Use **ScopedRateThrottle** for endpoint-specific limits (login, uploads).
3. Implement **custom throttles** for API keys, tiers, or tenants.
4. Always use a **shared cache** in production.

Throttling protects your API; permissions protect your data — use both.
