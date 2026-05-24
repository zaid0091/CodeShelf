---
title: Authentication
description: Session, Basic, Token authentication, DEFAULT_AUTHENTICATION_CLASSES, and Token obtain flow.
order: 9
tags: [drf, authentication, security]
---

# Chapter 9: Authentication

## 9.1 What is Authentication?

```text

Authentication = "WHO are you?"

Real-world analogy:
You walk into an office building.
The security guard asks: "Can I see your ID card?"
You show your ID → The guard now knows WHO you are.
This is Authentication.

In API terms:
The client sends a request with credentials (token, username/password).
DRF checks those credentials and identifies the user.

Authentication is NOT the same as Authorization:

Authentication = WHO are you? → "I am John"
Authorization  = WHAT can you do? → "John can read, but cannot delete"

Authentication → Chapter 9 (this chapter)
Authorization  → Chapter 10 (Permissions)
```

## 9.2 DRF Authentication Types

```text

┌─────────────────────────────────────────────────────────────┐
│                  AUTHENTICATION TYPES                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Session Authentication                                   │
│     How: Browser cookies                                     │
│     Good for: Web apps with Django templates                │
│     Not for: Mobile apps, third-party APIs                  │
│                                                              │
│  2. Basic Authentication                                     │
│     How: Username:password in every request (Base64 encoded)│
│     Good for: Testing, internal tools                       │
│     Not for: Production (password sent every time!)         │
│                                                              │
│  3. Token Authentication                                     │
│     How: Permanent token stored in database                 │
│     Good for: Simple API authentication                     │
│     Not for: High-security apps (token never expires)       │
│                                                              │
│  4. JWT Authentication (BEST for most APIs)                  │
│     How: Access token (short-lived) + Refresh token          │
│     Good for: Mobile apps, SPAs, microservices              │
│     Industry standard for modern APIs                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 9.3 Token Authentication (Built-in)

Step 1: Setup

```python

# config/settings.py

INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework.authtoken',  # ← ADD THIS for token auth
    'books',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}
```

```bash

# Create the token table
python manage.py migrate
Step 2: Create Login/Logout Views

```

```python

# books/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

@api_view(['POST'])
@permission_classes([AllowAny])  # Anyone can try to login
def login_view(request):
    """
    POST /api/login/
    Body: {"username": "john", "password": "secret123"}
    
    Returns a token that the client uses for future requests.
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    # Validate input
    if not username or not password:
        return Response(
            {'error': 'Please provide both username and password'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Authenticate user (checks username + password)
    user = authenticate(username=username, password=password)
    
    if user is not None:
        # Create token if it doesn't exist, or get existing one
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'message': 'Login successful!'
        }, status=status.HTTP_200_OK)
    else:
        return Response(
            {'error': 'Invalid username or password'},
            status=status.HTTP_401_UNAUTHORIZED
        )

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Must be logged in to logout
def logout_view(request):
    """
    POST /api/logout/
    Header: Authorization: Token abc123...
    
    Deletes the user's token, forcing them to login again.
    """
    # Delete the token
    request.user.auth_token.delete()
    
    return Response(
        {'message': 'Logged out successfully'},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    """
    GET /api/profile/
    Header: Authorization: Token abc123...
    
    Returns the current user's profile.
    """
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_staff': user.is_staff,
        'date_joined': user.date_joined,
    })
Step 3: URLs

# books/urls.py

urlpatterns = [
    # Authentication endpoints
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    
    # API endpoints
    path('', include(router.urls)),
]
Step 4: How clients use tokens

```

```bash

# 1. Login to get token
curl -X POST http://127.0.0.1:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'

# Response:
# {"token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b", 
#  "username": "admin", ...}

# 2. Use token in ALL future requests
curl http://127.0.0.1:8000/api/books/ \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"

# 3. Logout (delete token)
curl -X POST http://127.0.0.1:8000/api/logout/ \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
```

How Token Authentication works internally:

```text

1. Client sends: Authorization: Token abc123xyz

2. DRF TokenAuthentication:
   a. Reads the header
   b. Extracts "abc123xyz"
   c. Looks up in Token table: Token.objects.get(key="abc123xyz")
   d. If found → request.user = token.user (the User object)
   e. If not found → returns 401 Unauthorized

3. Now in your view, request.user is the authenticated user!
```
