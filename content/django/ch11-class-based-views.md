---
title: Class-Based Views
description: ListView, DetailView, CreateView, UpdateView, DeleteView, and mixins
order: 11
tags: [django, cbv, generic-views]
---

# Chapter 11: Class-Based Views

## 11.1 Why class-based views?

> **Definition:** **Class-based views (CBVs)** encapsulate request handling in classes. Generic CBVs provide reusable CRUD patterns with less code than function-based views.

Compare with [Views & URLs](./ch04-views-urls.md) FBVs — choose CBVs for standard patterns, FBVs for unique logic.

## 11.2 Basic CBV

```python
from django.views import View
from django.http import HttpResponse

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello")

    def post(self, request):
        return HttpResponse("Posted", status=201)
```

```python
path("hello/", HelloView.as_view(), name="hello"),
```

HTTP method maps to `get`, `post`, `put`, `delete`, etc.

## 11.3 ListView

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(published=True)
```

Default template: `blog/post_list.html` if following `app/model_list.html` convention.

## 11.4 DetailView

```python
from django.views.generic import DetailView

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(published=True)
```

## 11.5 CreateView and UpdateView

```python
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import PostForm

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post-list")
```

Integrates with [Forms](./ch06-forms.md) automatically.

## 11.6 DeleteView

```python
from django.views.generic import DeleteView

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")
```

## 11.7 URL wiring

```python
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("create/", PostCreateView.as_view(), name="post-create"),
]
```

## 11.8 Mixins

```python
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
```

| Mixin | Purpose |
|-------|---------|
| `LoginRequiredMixin` | Require authentication |
| `PermissionRequiredMixin` | Check named permission |
| `UserPassesTestMixin` | Custom access test |

See [Authentication](./ch08-authentication.md).

## 11.9 CBV method flow (ListView)

```text
as_view() → dispatch() → get() → get_queryset() → get_context_data() → render
```

Override hooks rather than rewriting entire methods when possible.

## 11.10 When to use FBV vs CBV

| Prefer FBV | Prefer CBV |
|------------|------------|
| Complex conditional logic | Standard CRUD |
| Multiple unrelated actions | Mixins compose well |
| Very small one-off endpoints | Built-in pagination |

## Exercises

1. Replace post list/detail FBVs with `ListView` and `DetailView`.
2. Add `PostCreateView` with author assignment in `form_valid`.
3. Protect create/update with `LoginRequiredMixin`.
4. Add pagination with `paginate_by = 5`.

## Summary

Generic CBVs speed up CRUD. Combine mixins for auth; override `get_queryset` and `form_valid` for custom behavior.

## Next chapter

Continue to [Deployment Basics](./ch12-deployment-basics.md).
