---
title: Class-Based Views (APIView)
description: APIView, HTTP method handlers, as_view(), and when to use class-based views.
order: 5
tags: [drf, views, apiview, class-based]
---

# Chapter 5: Class-Based Views (APIView)

## 5.1 Why Class-Based Views?

Function-based views work fine, but they have problems:

```text

Problem 1: Code Repetition
  Every view has the same try/except for getting objects.
  Every POST view has the same validation pattern.
  
Problem 2: No Inheritance
  You can't reuse common logic across views.
  
Problem 3: Hard to Organize
  All HTTP methods are in one function with if/elif chains.

Class-Based Views solve all of this:
  - Each HTTP method gets its own method (get, post, put, delete)
  - Common logic goes in base classes
  - Inheritance lets you reuse code
  - Cleaner and more organized
```

## 5.2 APIView — The Base Class

```python

# books/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(APIView):
    """
    Handles the COLLECTION of books.
    GET  → List all books
    POST → Create a new book
    """
    
    def get(self, request):
        """
        Handle GET requests — list all books.
        Notice: method name is lowercase 'get', not 'GET'.
        DRF automatically calls this method for GET requests.
        """
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Handle POST requests — create a new book."""
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailAPIView(APIView):
    """
    Handles a SINGLE book.
    GET    → Retrieve
    PUT    → Full update
    PATCH  → Partial update
    DELETE → Delete
    """
    
    def get_object(self, pk):
        """Helper method to get book or return 404."""
        return get_object_or_404(Book, pk=pk)
    
    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

## 5.3 URLs for Class-Based Views

```python

# books/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # .as_view() converts the CLASS into a view function
    # Django's URL dispatcher needs a function, not a class
    path('books/', views.BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailAPIView.as_view(), name='book-detail'),
]
```

### Why .as_view()?

```text

Django's URL system expects a callable FUNCTION.
A class is not callable like a function.
.as_view() creates a function that:
  1. Creates an instance of your class
  2. Calls the appropriate method (get/post/put/delete)
     based on the HTTP method
  3. Returns the response
```

## 5.4 How APIView Processes a Request Internally

```python

# This is SIMPLIFIED pseudocode of what happens inside APIView

class APIView:
    def dispatch(self, request, *args, **kwargs):
        """
        This method is called for EVERY request.
        It's the main entry point.
        """
        # Step 1: Wrap Django's HttpRequest into DRF's Request
        request = self.initialize_request(request)
        
        # Step 2: Run authentication, permissions, throttling
        self.initial(request, *args, **kwargs)
        
        # Step 3: Find the right method based on HTTP method
        if request.method == 'GET':
            response = self.get(request, *args, **kwargs)
        elif request.method == 'POST':
            response = self.post(request, *args, **kwargs)
        elif request.method == 'PUT':
            response = self.put(request, *args, **kwargs)
        elif request.method == 'PATCH':
            response = self.patch(request, *args, **kwargs)
        elif request.method == 'DELETE':
            response = self.delete(request, *args, **kwargs)
        
        # Step 4: Return the response
        return response
    
    def initial(self, request, *args, **kwargs):
        """Run before any view method."""
```

### self.perform_authentication(request)   # Who are you?

### self.check_permissions(request)        # Are you allowed?

### self.check_throttles(request)          # Too many requests?

### 🎯 Interview Point

**Explain how APIView dispatches requests.**

When a request comes in, APIView's dispatch() method:
Wraps Django's HttpRequest into DRF's enhanced Request
Runs perform_authentication() to identify the user
Runs check_permissions() to verify access rights
Runs check_throttles() to prevent abuse
Routes to the appropriate handler method (get/post/put/delete) based on the HTTP method
If the method isn't defined, returns 405 Method Not Allowed
Catches exceptions and converts them to proper error responses
