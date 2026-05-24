---
title: Project 2 — Blog API
description: Full DRF Blog API with nested comments, publishing, and optimized queries
order: 27
tags: [drf, project, blog, nested-routes]
---

# Project 2: Blog API

A blog platform with **categories**, **posts** (list vs detail serializers), **nested comments**, and a **publish** action. Demonstrates `select_related`, `prefetch_related`, and manual nested URL routing.

---

## models.py

```python
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=500, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cover_image = models.ImageField(upload_to='posts/', blank=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
```

---

## serializers.py

```python
from rest_framework import serializers
from .models import Category, Post, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at']
        read_only_fields = ['author']

class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'excerpt', 'author',
            'category', 'cover_image', 'published_at', 'comment_count'
        ]

    def get_comment_count(self, obj):
        return obj.comments.count()

class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', 'slug']

    def create(self, validated_data):
        from django.utils.text import slugify
        validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)
```

---

## views.py

```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.utils import timezone

from .models import Category, Post, Comment
from .serializers import (
    CategorySerializer,
    PostListSerializer,
    PostDetailSerializer,
    CommentSerializer,
)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category__slug', 'is_published', 'author']
    search_fields = ['title', 'content']
    ordering = ['-published_at']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.select_related(
                'author', 'category'
            ).prefetch_related('comments')
        return Post.objects.filter(is_published=True).select_related(
            'author', 'category'
        )

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        post = self.get_object()
        post.is_published = True
        post.published_at = timezone.now()
        post.save()
        return Response({'message': f'"{post.title}" published!'})

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)
```

---

## urls.py — Nested routes

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CategoryViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'posts/<int:post_pk>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
    ),
    path(
        'posts/<int:post_pk>/comments/<int:pk>/',
        CommentViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}),
    ),
]
```

---

## API endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/posts/` | Published posts (staff sees all) |
| POST | `/api/posts/` | Create draft post |
| POST | `/api/posts/{id}/publish/` | Publish post |
| GET | `/api/categories/` | List categories |
| GET | `/api/posts/{id}/comments/` | List comments on post |
| POST | `/api/posts/{id}/comments/` | Add comment |
