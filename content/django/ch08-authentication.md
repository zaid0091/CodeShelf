---
title: Authentication
description: User model, login, logout, permissions, decorators, and custom user models
order: 8
tags: [django, auth, users]
---

# Chapter 8: Authentication

## 8.1 Django auth system

> **Definition:** **Authentication** verifies who a user is; **authorization** determines what they can do. Django provides both via `django.contrib.auth`.

Included apps: `auth`, `sessions`, `contenttypes`. Enabled by default in new projects.

## 8.2 User model

```python
from django.contrib.auth.models import User

# Common fields
user.username
user.email
user.is_staff      # Can access admin
user.is_superuser  # All permissions
user.is_active
user.check_password("secret")
user.set_password("newsecret")
user.save()
```

Create users:

```bash
python manage.py createsuperuser
```

```python
from django.contrib.auth.models import User

User.objects.create_user(username="alice", email="a@example.com", password="pass123")
User.objects.create_superuser(username="admin", password="adminpass")
```

## 8.3 Login and logout views

```python
# urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
```

```python
# settings.py
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "blog-index"
LOGOUT_REDIRECT_URL = "login"
```

Login template:

```django
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Log in</button>
</form>
```

## 8.4 Protecting views

```python
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@permission_required("blog.change_post", raise_exception=True)
def edit_post(request, pk):
    ...
```

## 8.5 User in templates

```django
{% if user.is_authenticated %}
  Hello, {{ user.username }}
  <a href="{% url 'logout' %}">Log out</a>
{% else %}
  <a href="{% url 'login' %}">Log in</a>
{% endif %}
```

## 8.6 Permissions and groups

```python
from django.contrib.auth.models import Permission, Group

group = Group.objects.create(name="Editors")
perm = Permission.objects.get(codename="change_post")
group.permissions.add(perm)
user.groups.add(group)
user.has_perm("blog.change_post")
```

## 8.7 Associating models with users

```python
class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
```

Always use `get_user_model()` or `settings.AUTH_USER_MODEL` for FKs.

## 8.8 Custom user model

```python
# settings.py
AUTH_USER_MODEL = "accounts.CustomUser"

# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=100, blank=True)
```

Must be set **before** first migration.

## 8.9 Password validators

```python
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
]
```

## 8.10 Session security

- Use HTTPS in production
- Set `SESSION_COOKIE_SECURE = True`
- Rotate `SECRET_KEY` if compromised

## Exercises

1. Add login/logout URLs and templates.
2. Protect post-create view with `@login_required`.
3. Create an "Editors" group with change permission on Post.
4. Skim custom user model only on new projects.

## Summary

Django auth handles users, sessions, groups, and permissions. Use built-in views and decorators before building auth from scratch.

## Next chapter

Continue to [Migrations](./ch09-migrations.md).
