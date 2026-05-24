---
title: Chapter 20 — Custom User & Registration
description: Custom User model, registration serializers, and signup API with Django REST Framework
order: 20
tags: [drf, authentication, user-model, registration]
---

# Chapter 20: Custom User & Registration

Django's default `User` model is fine for tutorials; production apps typically use a **custom user model** (email login, extra fields) and a **registration API** that creates users and returns tokens.

## Definitions

| Term | Meaning |
|------|---------|
| **Custom User model** | Subclass of `AbstractUser` or `AbstractBaseUser`. |
| **AUTH_USER_MODEL** | Setting pointing to your user model — set before first migration. |
| **Registration endpoint** | Public POST that creates a user with validation. |
| **Write-only password** | Password in request only; never returned in responses. |

---

## 20.1 Custom User Model

### Create before first migrate

If the project already migrated `auth.User`, switching models is painful. For new projects:

```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # createsuperuser prompts for these

    def __str__(self):
        return self.email
```

```python
# settings.py
AUTH_USER_MODEL = 'accounts.User'
```

```python
# accounts/apps.py
from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
```

```bash
python manage.py makemigrations accounts
python manage.py migrate
```

### Custom manager (optional, email-only)

```python
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
```

### User serializer (read)

```python
# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'phone', 'date_of_birth']
        read_only_fields = ['id']
```

### Me endpoint

```python
# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserSerializer(
            request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
```

```python
# urls.py
urlpatterns = [
    path('api/me/', MeView.as_view(), name='me'),
]
```

### Interview points

- **`AUTH_USER_MODEL`** must be set **before** the first `migrate`.
- Reference users as `settings.AUTH_USER_MODEL` or `get_user_model()` — never hardcode `User`.
- `USERNAME_FIELD` defines the login identifier (`email` vs `username`).
- `AbstractUser` = full featured; `AbstractBaseUser` = minimal custom.

---

## 20.2 Registration API

### Registration serializer

```python
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2', 'phone']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password': 'Password fields did not match.'}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data.get('username', ''),
            password=validated_data['password'],
            phone=validated_data.get('phone', ''),
        )
        return user
```

### Registration view

```python
from rest_framework import generics, permissions, status
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            UserSerializer(user).data,
            status=status.HTTP_201_CREATED
        )
```

### Register + return JWT

```python
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
```

### Request example

```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "new@example.com",
    "username": "newuser",
    "password": "SecurePass123!",
    "password2": "SecurePass123!"
  }'
```

```json
{
    "user": {
        "id": 2,
        "email": "new@example.com",
        "username": "newuser",
        "phone": ""
    },
    "access": "eyJ0eXAiOiJKV1Qi...",
    "refresh": "eyJ0eXAiOiJKV1Qi..."
}
```

### URL layout

```python
# accounts/urls.py
from django.urls import path
from .views import RegisterView, MeView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', MeView.as_view(), name='me'),
]
```

```python
# project urls.py
path('api/auth/', include('accounts.urls')),
```

### Email verification (outline)

```python
class RegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(...)
        user.is_active = False  # require email verification
        user.save()
        send_verification_email(user)
        return user
```

```python
class VerifyEmailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, token):
        user = validate_verification_token(token)
        user.is_active = True
        user.save()
        return Response({'detail': 'Email verified.'})
```

### Throttle registration

```python
from rest_framework.throttling import AnonRateThrottle

class RegisterView(generics.CreateAPIView):
    throttle_classes = [AnonRateThrottle]
    throttle_scope = 'register'
```

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'register': '5/hour',
    },
}
```

### Tests

```python
class RegistrationTests(APITestCase):
    def test_register_success(self):
        payload = {
            'email': 'a@test.com',
            'username': 'usera',
            'password': 'ComplexPass1!',
            'password2': 'ComplexPass1!',
        }
        response = self.client.post('/api/auth/register/', payload, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(email='a@test.com').exists())
        self.assertIn('access', response.data)

    def test_password_mismatch(self):
        response = self.client.post('/api/auth/register/', {
            'email': 'b@test.com',
            'password': 'ComplexPass1!',
            'password2': 'DifferentPass1!',
        }, format='json')
        self.assertEqual(response.status_code, 400)
```

### Interview points

- Use Django's **`validate_password`** — never roll your own rules only.
- **Never return** `password` in API responses (`write_only=True`).
- **Unique email** enforced at model (`unique=True`) and serializer.
- Set **`is_active=False`** until email verified when required.
- Registration is **AllowAny**; throttle to prevent spam accounts.
- Link to **JWT** or session login immediately after signup for better UX.

---

## Chapter summary

1. Define **custom User** early; set `AUTH_USER_MODEL`.
2. Build **RegisterSerializer** with password confirmation and validators.
3. Expose **POST /register/**; optionally return **JWT** tokens.
4. Add **/me/**, throttling, and email verification for production.

Custom users plus a solid registration flow are the foundation of real-world DRF authentication.
