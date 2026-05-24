---
title: ViewSets & Routers
description: "ViewSet, ModelViewSet, @action, routers, URL patterns, and nested ViewSets."
order: 8
tags: [drf, viewsets, routers]
---

# Chapter 8: ViewSets & Routers

## 8.1 What are ViewSets?

Up to now, you needed two separate classes for each model:

One for the collection (list/create)
One for single items (retrieve/update/delete)
ViewSets combine everything into one class:

```text

Before (2 classes, 2 URL patterns):
  BookListCreateView     → /api/books/
  BookDetailView         → /api/books/<pk>/

After (1 class, 0 URL patterns):
  BookViewSet            → Router generates ALL URLs automatically!
```

## 8.2 ModelViewSet

```python

# books/views.py

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet that provides ALL CRUD operations:
    
    list()           → GET    /api/books/        → List all books
    create()         → POST   /api/books/        → Create a book
    retrieve()       → GET    /api/books/1/      → Get book 1
    update()         → PUT    /api/books/1/      → Full update book 1
    partial_update() → PATCH  /api/books/1/      → Partial update book 1
    destroy()        → DELETE /api/books/1/      → Delete book 1
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

## 8.3 Routers

Routers automatically generate URL patterns for ViewSets.

```python

# books/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Step 1: Create a router
router = DefaultRouter()

# Step 2: Register your ViewSet
router.register(
    prefix='books',           # URL prefix: /api/books/
    viewset=views.BookViewSet,
    basename='book'           # Used for URL names: book-list, book-detail
)

# Step 3: Include router URLs
urlpatterns = [
    path('', include(router.urls)),
]
What the router generates:

```

```text

router.register('books', BookViewSet, basename='book')

Generates these URL patterns:
  /api/books/           name='book-list'       → GET (list), POST (create)
  /api/books/{pk}/      name='book-detail'     → GET, PUT, PATCH, DELETE
  /api/books/.json      name='book-list'       → JSON format
  /api/books/{pk}/.json name='book-detail'     → JSON format

DefaultRouter also adds:
  /api/                 name='api-root'        → API root (lists all endpoints)
Two types of routers:

```

```python

# DefaultRouter — adds API root view, supports .json format suffix
router = DefaultRouter()

# SimpleRouter — no API root, no format suffixes
router = SimpleRouter()

# Use DefaultRouter for most cases.
```

## 8.4 Types of ViewSets

```python

# 1. ModelViewSet — Full CRUD (all 6 actions)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# 2. ReadOnlyModelViewSet — Only list() and retrieve()
class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only GET /books/ and GET /books/1/ work
    # No POST, PUT, PATCH, DELETE

# 3. ViewSet — Empty base, define everything yourself
class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        # ... your custom logic
        pass
    
    def retrieve(self, request, pk=None):
        # ... your custom logic
        pass
```

## 8.5 Custom Actions

### What if you need endpoints beyond standard CRUD?

```python

from rest_framework.decorators import action
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # ---- COLLECTION ACTION (detail=False) ----
    # URL: GET /api/books/available/
    @action(detail=False, methods=['get'])
    def available(self, request):
        """List only available books"""
        available_books = Book.objects.filter(is_available=True)
        serializer = self.get_serializer(available_books, many=True)
        return Response(serializer.data)
    
    # URL: GET /api/books/statistics/
    @action(detail=False, methods=['get'], url_path='statistics')
    def stats(self, request):
        """Get book statistics"""
        from django.db.models import Avg, Count, Max, Min, Sum
        data = Book.objects.aggregate(
            total_books=Count('id'),
            avg_price=Avg('price'),
            max_price=Max('price'),
            min_price=Min('price'),
            total_value=Sum('price'),
        )
        return Response(data)
    
    # URL: GET /api/books/by-author/?author=Rowling
    @action(detail=False, methods=['get'], url_path='by-author')
    def by_author(self, request):
        """Filter books by author name"""
        author = request.query_params.get('author', '')
        if not author:
            return Response(
                {'error': 'Please provide an author name'},
                status=400
            )
        books = Book.objects.filter(author__icontains=author)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
    
    # ---- DETAIL ACTION (detail=True) ----
    # URL: POST /api/books/5/mark-unavailable/
    @action(detail=True, methods=['post'], url_path='mark-unavailable')
    def mark_unavailable(self, request, pk=None):
        """Mark a specific book as unavailable"""
        book = self.get_object()
        book.is_available = False
        book.save()
        serializer = self.get_serializer(book)
        return Response({
            'message': f'"{book.title}" marked as unavailable',
            'book': serializer.data
        })
    
    # URL: GET /api/books/5/similar/
    @action(detail=True, methods=['get'])
    def similar(self, request, pk=None):
        """Find books by the same author"""
        book = self.get_object()
        similar_books = Book.objects.filter(
            author=book.author
        ).exclude(pk=book.pk)
        serializer = self.get_serializer(similar_books, many=True)
        return Response(serializer.data)
detail=True vs detail=False:

```

```text

detail=False → Works on the COLLECTION (no pk needed)
  URL: /api/books/available/
  URL: /api/books/statistics/
  Like asking: "Show me all available books"

detail=True → Works on a SINGLE ITEM (pk required)
  URL: /api/books/5/mark-unavailable/
  URL: /api/books/5/similar/
  Like asking: "Mark book #5 as unavailable"
```

## 8.6 Customizing ModelViewSet

```python

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    
    def get_queryset(self):
        """Dynamic queryset based on user"""
        user = self.request.user
        if user.is_staff:
            return Book.objects.all()
        return Book.objects.filter(is_available=True)
    
    def get_serializer_class(self):
        """Different serializers for different actions"""
        if self.action == 'list':
            return BookListSerializer
        elif self.action == 'retrieve':
            return BookDetailSerializer
        return BookSerializer
    
    def get_permissions(self):
        """Different permissions for different actions"""
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        """Custom save logic for creation"""
        serializer.save(owner=self.request.user)
    
    def perform_update(self, serializer):
        """Custom save logic for update"""
        serializer.save(updated_by=self.request.user)
    
    def perform_destroy(self, instance):
        """Custom delete logic — soft delete"""
        instance.is_available = False
        instance.save()
        # Instead of instance.delete()
The self.action attribute:

```

```text

self.action tells you which action is being performed:
  'list'           → GET /books/
  'create'         → POST /books/
  'retrieve'       → GET /books/1/
  'update'         → PUT /books/1/
  'partial_update' → PATCH /books/1/
  'destroy'        → DELETE /books/1/
  'available'      → Your custom action name
```

## 8.7 Multiple ViewSets with One Router

```python

# books/urls.py

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('books', views.BookViewSet, basename='book')
router.register('authors', views.AuthorViewSet, basename='author')
router.register('categories', views.CategoryViewSet, basename='category')
router.register('reviews', views.ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]

# This generates URLs for ALL models:
# /api/books/         /api/books/1/
# /api/authors/       /api/authors/1/
# /api/categories/    /api/categories/1/
# /api/reviews/       /api/reviews/1/
# /api/               → API root showing all endpoints
```

## 8.8 Choosing the Right Approach

```text

┌──────────────────────────────────────────────────────────┐
│              WHEN TO USE WHAT                             │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  @api_view (FBV):                                       │
│    ✓ Very simple, one-off endpoints                     │
│    ✓ Webhook receivers                                  │
│    ✓ Custom logic that doesn't fit CRUD pattern         │
│    Example: /api/health-check/                          │
│                                                          │
│  APIView (CBV):                                         │
│    ✓ Complex custom logic                               │
│    ✓ Endpoints with unusual behavior                    │
│    ✓ When you need full control                         │
│    Example: /api/login/, /api/register/                 │
│                                                          │
│  Generic Views:                                          │
│    ✓ Standard CRUD operations                           │
│    ✓ When you need just some actions (not all)          │
│    ✓ When you want to be explicit about what's allowed  │
│    Example: Read-only public API                        │
│                                                          │
│  ModelViewSet + Router:                                  │
│    ✓ Full CRUD APIs (most common)                       │
│    ✓ When you want ALL operations                       │
│    ✓ When you want automatic URLs                       │
│    ✓ MOST APIs in production use this!                  │
│    Example: Any model-based CRUD API                    │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## Practice Exercise — Chapter 8

```text

Exercise 8.1:
  Convert your Student API to use ModelViewSet + Router.
  Add these custom actions:
    a) GET /api/students/toppers/ → Students with grade 'A'
    b) GET /api/students/5/classmates/ → Students with same grade as student 5
    c) POST /api/students/5/deactivate/ → Set is_active=False

Exercise 8.2:
  Create a full Blog API:
    Models: Category, Post, Comment
    ViewSets: One for each model
    Register all in a single router
    Add custom action: GET /api/posts/recent/ → Posts from last 7 days
```
