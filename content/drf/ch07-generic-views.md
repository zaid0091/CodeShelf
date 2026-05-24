---
title: Generic Views
description: ListCreateAPIView, RetrieveUpdateDestroyAPIView, generics shortcuts, and get_queryset customization.
order: 7
tags: [drf, generic-views, views]
---

# Chapter 7: Generic Views

## 7.1 What are Generic Views?

Generic Views are pre-combined mixins. They save you from having to manually wire get() to list() and post() to create().

```text

EVOLUTION OF DRF VIEWS:

Level 1: @api_view (FBV)
  → Most manual work, full control
  → 30+ lines per view

Level 2: APIView (CBV)
  → Separate methods, but still manual
  → 20+ lines per view

Level 3: Mixins + GenericAPIView
  → Pre-built logic, but you wire methods manually
  → 10+ lines per view

Level 4: Generic Views ← YOU ARE HERE
  → Everything pre-built, just set queryset & serializer
  → 3-5 lines per view! ✨

Level 5: ViewSets + Routers
  → Everything including URLs is automatic
  → 3 lines total!
```

## 7.2 All Generic Views

```python

from rest_framework import generics

# ──── SINGLE-ACTION VIEWS ────

# List only (GET collection)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create only (POST)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve only (GET single)
class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Update only (PUT/PATCH)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Delete only (DELETE)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ──── COMBINED VIEWS (Most Used) ────

# List + Create (GET collection + POST)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve + Update (GET single + PUT/PATCH)
class BookRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve + Destroy (GET single + DELETE)
class BookRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve + Update + Destroy (GET single + PUT/PATCH + DELETE)
class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

## 7.3 The Most Common Pattern

For 90% of APIs, you need just two views for each model:

```python

# books/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/books/     → List all books
    POST /api/books/     → Create a new book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/books/1/  → Retrieve book 1
    PUT    /api/books/1/  → Full update book 1
    PATCH  /api/books/1/  → Partial update book 1
    DELETE /api/books/1/  → Delete book 1
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
That is 6 lines of code for a complete CRUD API! Compare this with the 50+ lines in the function-based approach.

```

## 7.4 Customizing Generic Views

```python

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer, BookListSerializer

class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """
        Override get_queryset() for DYNAMIC filtering.
        
        Why not just set queryset = Book.objects.filter(...)?
        Because queryset is evaluated ONCE when Django starts.
        get_queryset() is called on EVERY request — always fresh!
        """
        user = self.request.user
        
        # If admin, show all books. If regular user, show only available ones.
        if user.is_staff:
            return Book.objects.all()
        return Book.objects.filter(is_available=True)
    
    def get_serializer_class(self):
        """
        Use DIFFERENT serializers for different actions.
        List view needs minimal data (fast).
        Create view needs full data (complete).
        """
        if self.request.method == 'GET':
            return BookListSerializer   # Minimal fields for listing
        return BookSerializer           # Full fields for creating
    
    def perform_create(self, serializer):
        """
        Called just before saving a new book.
        Add any extra data that isn't in the request.
        """
        serializer.save(
            added_by=self.request.user  # Automatically set who added it
        )
    
    def list(self, request, *args, **kwargs):
        """
        Override list() to add custom data to the response.
        """
        response = super().list(request, *args, **kwargs)
        # Add total count to the response
        response.data = {
            'count': self.get_queryset().count(),
            'results': response.data
        }
        return response
```

Common Mistake: Setting queryset as a filtered queryset that depends on request.

```python

# WRONG — queryset is evaluated at startup, not per-request
class BookListView(generics.ListAPIView):
    queryset = Book.objects.filter(owner=request.user)  # ERROR!
    # 'request' doesn't exist at class definition time!

# CORRECT — use get_queryset() for dynamic filtering
class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)
```

## Practice Exercise — Chapter 5, 6, 7

```text

Exercise 7.1:
  Rewrite your Student CRUD API using:
  a) APIView (class-based)
  b) Mixins + GenericAPIView
  c) Generic Views (ListCreateAPIView + RetrieveUpdateDestroyAPIView)
  
  Compare the amount of code in each approach.

Exercise 7.2:
  Create a "Product" API using Generic Views:
  - Model: name, category, price, stock, is_active
  - List view: Only show active products
  - Create view: Automatically set is_active=True
  - Use different serializers for list (minimal) and detail (full)
```
