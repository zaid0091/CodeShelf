---
title: Views and URLs
description: Function-based views, URLconf, HttpRequest, HttpResponse, and redirects
order: 4
tags: [django, views, urls]
---

# Chapter 4: Views and URLs

## 4.1 URL routing

> **Definition:** **URLconf** maps URL patterns to view callables. Django walks `urlpatterns` top-to-bottom and calls the first match.

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post-list"),
    path("<int:pk>/", views.post_detail, name="post-detail"),
    path("create/", views.post_create, name="post-create"),
]
```

| Converter | Matches |
|-----------|---------|
| `str` | Non-empty string (default) |
| `int` | Integer |
| `slug` | Slug (letters, numbers, hyphens) |
| `uuid` | UUID |
| `path` | Full path including `/` |

## 4.2 Function-based views (FBV)

```python
# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    return render(request, "blog/post_detail.html", {"post": post})
```

| Helper | Use |
|--------|-----|
| `render()` | Template + context → HttpResponse |
| `get_object_or_404()` | Fetch or 404 |
| `redirect()` | HTTP redirect |
| `reverse()` | URL by name |

## 4.3 HttpRequest object

```python
def debug_request(request):
    method = request.method       # GET, POST, ...
    user = request.user           # auth user
    GET = request.GET             # query string
    POST = request.POST           # form body
    path = request.path
    headers = request.headers
    session = request.session
```

Access query params:

```python
search = request.GET.get("q", "")
page = int(request.GET.get("page", 1))
```

## 4.4 HttpResponse types

```python
from django.http import JsonResponse, HttpResponseNotFound

def api_posts(request):
    data = list(Post.objects.values("id", "title"))
    return JsonResponse(data, safe=False)

def not_found_view(request):
    return HttpResponseNotFound("Not found")
```

## 4.5 Named URLs and reverse

```python
# In templates: {% url 'post-detail' pk=post.pk %}
# In views:
from django.urls import reverse

url = reverse("post-detail", kwargs={"pk": 42})
return HttpResponseRedirect(reverse("post-list"))
```

Always prefer named URLs over hard-coded paths.

## 4.6 include() and namespaces

```python
# mysite/urls.py
urlpatterns = [
    path("blog/", include("blog.urls", namespace="blog")),
]

# blog/urls.py
app_name = "blog"
urlpatterns = [...]

# reverse("blog:post-detail", kwargs={"pk": 1})
```

## 4.7 POST handling (preview)

```python
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Post.objects.create(title=title, body="...")
        return redirect("post-list")
    return render(request, "blog/post_form.html")
```

Full form handling in [Forms](./ch06-forms.md).

## 4.8 HTTP methods summary

| Method | Typical use |
|--------|-------------|
| GET | Read / display |
| POST | Create / mutate |
| PUT/PATCH | Update (APIs) |
| DELETE | Delete (APIs) |

## 4.9 View decorators

```python
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

@login_required
@cache_page(60 * 15)
def dashboard(request):
    ...
```

See [Authentication](./ch08-authentication.md).

## 4.10 Error views

Configure in root `urls.py` or use defaults:

```python
handler404 = "mysite.views.custom_404"
handler500 = "mysite.views.custom_500"
```

## Exercises

1. Create list and detail views for `Post`; wire URLs with `int:pk`.
2. Use `get_object_or_404` and named URL `reverse`.
3. Add a view that reads `?q=` from GET and filters posts.
4. Return `JsonResponse` for `/blog/api/posts/`.

## Summary

URLs map paths to views; views receive `request` and return `HttpResponse`. Use `render`, named URLs, and helpers for clean routing.

## Next chapter

Continue to [Templates](./ch05-templates.md).
