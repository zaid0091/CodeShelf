---
title: Project 1 — Todo API
description: Full DRF Todo API with filtering, search, and custom actions
order: 26
tags: [drf, project, todo, viewset]
---

# Project 1: Todo API

A per-user todo API demonstrating **ModelViewSet**, **owner scoping**, **filtering/search/ordering**, and **custom `@action` endpoints**.

## Features

| Feature | Implementation |
|---------|----------------|
| CRUD todos | `ModelViewSet` |
| User isolation | `get_queryset()` filters by `owner` |
| Filter by status/priority | `DjangoFilterBackend` |
| Search title/description | `SearchFilter` |
| Pending list | `@action(detail=False)` |
| Toggle complete | `@action(detail=True, methods=['post'])` |

---

## models.py

```python
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        default='medium'
    )
    due_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

---

## serializers.py

```python
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    is_overdue = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['owner']

    def get_is_overdue(self, obj):
        from datetime import date
        if obj.due_date and not obj.is_completed:
            return obj.due_date < date.today()
        return False
```

---

## views.py

```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_completed', 'priority']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date', 'priority']

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def pending(self, request):
        todos = self.get_queryset().filter(is_completed=False)
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        todo = self.get_object()
        todo.is_completed = not todo.is_completed
        todo.save()
        return Response(self.get_serializer(todo).data)
```

---

## urls.py

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router = DefaultRouter()
router.register('todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
]
```

---

## API endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/todos/` | List user's todos |
| POST | `/api/todos/` | Create todo |
| GET | `/api/todos/{id}/` | Retrieve todo |
| PUT/PATCH | `/api/todos/{id}/` | Update todo |
| DELETE | `/api/todos/{id}/` | Delete todo |
| GET | `/api/todos/pending/` | Incomplete todos |
| POST | `/api/todos/{id}/toggle/` | Toggle `is_completed` |

### Example queries

```
GET /api/todos/?is_completed=false&priority=high
GET /api/todos/?search=meeting&ordering=-due_date
```
