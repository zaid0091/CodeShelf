---
title: Chapter 19 — JWT Authentication (SimpleJWT)
description: Stateless JWT auth with djangorestframework-simplejwt — setup, endpoints, and customization
order: 19
tags: [drf, jwt, authentication, simplejwt]
---

# Chapter 19: JWT Authentication (SimpleJWT)

**JSON Web Tokens (JWT)** are compact, signed tokens for **stateless** authentication. The client stores access (and often refresh) tokens and sends them on each request. **djangorestframework-simplejwt** is the standard JWT plugin for DRF.

## Definitions

| Term | Meaning |
|------|---------|
| **JWT** | Base64-encoded header.payload.signature token. |
| **Access token** | Short-lived token for API requests. |
| **Refresh token** | Long-lived token used only to obtain new access tokens. |
| **Bearer token** | `Authorization: Bearer <access_token>` header. |
| **SimpleJWT** | `rest_framework_simplejwt` package for DRF. |

---

## 19.1 Introduction to JWT

### JWT vs session / token auth

| | Session | DRF Token | JWT |
|---|---------|-----------|-----|
| Storage | Server session DB | Token table per user | Client-side (memory/storage) |
| Stateless | No | Semi | Yes (access token) |
| Expiry | Session cookie | Often none | Built-in `exp` claim |
| Revocation | Easy | Delete token row | Harder (blacklist needed) |

### JWT structure (decoded)

```json
{
  "header": {"alg": "HS256", "typ": "JWT"},
  "payload": {
    "token_type": "access",
    "exp": 1710000000,
    "user_id": 1
  }
}
```

### When to use JWT

- SPAs and mobile apps
- Microservices sharing auth
- APIs behind multiple domains (CORS)

Avoid JWT when you need **instant server-side revocation** without a blacklist.

### Interview points

- **Never store JWT in localStorage** if XSS is a concern — httpOnly cookies are debated; know tradeoffs.
- **Access token short**, **refresh token long** and protected.
- JWT is **signed**, not encrypted — do not put secrets in the payload.

---

## 19.2 SimpleJWT Setup

### Install

```bash
pip install djangorestframework-simplejwt
```

```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

### Signing key

Uses `SECRET_KEY` by default. Optional dedicated key:

```python
SIMPLE_JWT = {
    'SIGNING_KEY': env('JWT_SIGNING_KEY', default=SECRET_KEY),
}
```

### Protect a view

```python
from rest_framework import viewsets, permissions

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
```

### Manual request

```bash
curl http://127.0.0.1:8000/api/products/ \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."
```

### Interview points

- SimpleJWT validates signature, expiry, and token type (`access` vs `refresh`).
- Invalid/expired token → **401 Unauthorized**.

---

## 19.3 Token Endpoints

### URL configuration

```python
# urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', include('myapp.urls')),
]
```

### Obtain pair (login)

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "tester", "password": "pass1234"}'
```

```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Refresh access token

```bash
curl -X POST http://127.0.0.1:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."}'
```

```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Verify token

```bash
curl -X POST http://127.0.0.1:8000/api/token/verify/ \
  -H "Content-Type: application/json" \
  -d '{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."}'
```

Empty **200** = valid; **401** = invalid.

### Custom login serializer (email login)

```python
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD  # or override validate

    def validate(self, attrs):
        email = attrs.get('email') or attrs.get('username')
        password = attrs.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid credentials')
        attrs['username'] = user.username
        return super().validate(attrs)
```

```python
class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
```

### Interview points

- **Obtain pair** = login; **refresh** = new access without password.
- Only send **refresh** to `/token/refresh/`, not to every API route.
- Rotate refresh tokens when `ROTATE_REFRESH_TOKENS` is True.

---

## 19.4 Customizing JWT

### Lifetime and algorithm

```python
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'ALGORITHM': 'HS256',
}
```

### Blacklist (logout)

```bash
pip install djangorestframework-simplejwt  # blacklist in same package
```

```python
INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt.token_blacklist',
]
```

```bash
python manage.py migrate
```

```python
# urls.py
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
```

```bash
curl -X POST http://127.0.0.1:8000/api/token/blacklist/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "<refresh_token>"}'
```

### Custom claims in token

```python
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['is_staff'] = user.is_staff
        return token
```

Access custom claims in views via `request.auth` (the validated token object).

### User id in authentication

```python
# Default USER_ID_FIELD = 'id', USER_ID_CLAIM = 'user_id'
# views.py
def my_view(request):
    user = request.user  # populated from JWT
```

### Multiple authentication classes

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}
```

### Interview points

- Enable **blacklist** for logout and refresh rotation security.
- **HS256** = symmetric (one secret); **RS256** = public/private keys for microservices.
- Shorter **access** lifetime limits damage if token is stolen.
- Custom claims: keep payload **small** — JWT travels every request.

---

## Chapter summary

1. Install **simplejwt** and set `JWTAuthentication` as default.
2. Expose **token**, **refresh**, **verify** (and **blacklist** for logout).
3. Client sends `Authorization: Bearer <access>`.
4. Tune **SIMPLE_JWT** lifetimes, rotation, and custom claims.

JWT fits stateless clients; pair with **HTTPS**, short access TTL, and refresh/blacklist strategy for production.
