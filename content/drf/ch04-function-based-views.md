---
title: Function-Based Views
description: "@api_view decorator, Request/Response objects, status codes, and CRUD with function views."
order: 4
tags: [drf, views, function-based]
---

# Chapter 4: Function-Based Views

## 4.1 The @api_view Decorator

In plain Django, you write views using def my_view(request). In DRF, you enhance these with the @api_view decorator.

### What does @api_view do behind the scenes?

Without @api_view:
  - request is Django's HttpRequest (basic)
  - You get request.POST, request.GET
  - You return HttpResponse or JsonResponse
  - No authentication/permission checking
  - No content negotiation
  - No browsable API

With @api_view:
  - request becomes DRF's Request (enhanced)
  - You get request.data (works for JSON, form data, files — everything!)
  - You return DRF's Response (handles JSON automatically)
  - Authentication is checked
  - Permissions are checked
  - Throttling is checked
  - Browsable API works
  - Content negotiation works
```python

# books/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])  # Specify which HTTP methods are allowed
def book_list(request):
    """
    GET  → List all books
    POST → Create a new book
    """
    
    if request.method == 'GET':
        # Step 1: Get all books from database
        books = Book.objects.all()
        
        # Step 2: Serialize (convert Python objects → JSON-ready data)
        serializer = BookSerializer(books, many=True)
        
        # Step 3: Return the response
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        # Step 1: Deserialize (convert incoming JSON → Python data)
        serializer = BookSerializer(data=request.data)
        
        # Step 2: Validate the data
        if serializer.is_valid():
            # Step 3: Save to database (calls serializer's create() method)
            serializer.save()
            
            # Step 4: Return the created object
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # If validation fails, return errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
Let me explain each part:

# request.data
# This is DRF's magic. It handles ALL content types:
#   - JSON body     → request.data works
#   - Form data     → request.data works  
#   - Multipart     → request.data works
#   - Query params  → request.query_params (separate)
# In plain Django, you'd need: request.POST, request.body, json.loads(), etc.

# Response(data, status)
# DRF's Response automatically:
#   - Converts Python dict/list to JSON
#   - Sets Content-Type header to application/json
#   - Renders browsable API in browser
#   - Handles content negotiation

# status.HTTP_200_OK
# Same as writing 200, but MORE READABLE
# DRF provides constants for all status codes
```

## 4.2 Detail View (Single Object)

```python

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_detail(request, pk):
    """
    GET    → Retrieve a single book
    PUT    → Update ALL fields of a book
    PATCH  → Update SOME fields of a book
    DELETE → Delete a book
    
    'pk' comes from the URL: /api/books/5/ → pk=5
    """
    
    # Step 0: Find the book (common for all methods)
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(
            {'detail': 'Book not found.'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    # ---- GET: Retrieve ----
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    # ---- PUT: Full Update ----
    elif request.method == 'PUT':
        # Full update: ALL fields required
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # ---- PATCH: Partial Update ----
    elif request.method == 'PATCH':
        # Partial update: only changed fields required
        serializer = BookSerializer(
            instance=book,
            data=request.data,
            partial=True          # ← This makes it partial!
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # ---- DELETE: Destroy ----
    elif request.method == 'DELETE':
        book.delete()
        return Response(
            {'detail': 'Book deleted successfully.'},
            status=status.HTTP_204_NO_CONTENT
        )
```

## 4.3 URL Configuration

```python

# books/urls.py  (CREATE this file)

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
]

# <int:pk> means:
#   - Capture a part of the URL
#   - It must be an integer
#   - Pass it to the view as parameter 'pk'
#   - Example: /api/books/5/ → pk=5

# config/urls.py  (UPDATE this file)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),  # ← All API URLs start with /api/
]
Now your API endpoints are:

```

```text

GET    http://127.0.0.1:8000/api/books/          → List all books
POST   http://127.0.0.1:8000/api/books/          → Create a book
GET    http://127.0.0.1:8000/api/books/1/         → Get book id=1
PUT    http://127.0.0.1:8000/api/books/1/         → Full update book id=1
PATCH  http://127.0.0.1:8000/api/books/1/         → Partial update book id=1
DELETE http://127.0.0.1:8000/api/books/1/         → Delete book id=1
```

## 4.4 request Object in Detail

```python

@api_view(['POST'])
def demo_request(request):
    """Understanding the DRF Request object"""
    
    # 1. request.data — The parsed request body
    # Works for JSON, form data, multipart uploads
    print(request.data)
    # {'title': 'New Book', 'price': 299}
    
    # 2. request.query_params — URL query parameters
    # URL: /api/books/?search=python&page=2
    print(request.query_params)
    # {'search': 'python', 'page': '2'}
    search = request.query_params.get('search', '')
    page = request.query_params.get('page', 1)
    
    # 3. request.method — The HTTP method
    print(request.method)
    # 'POST'
    
    # 4. request.user — The authenticated user
    print(request.user)
    # <User: admin> or AnonymousUser
    
    # 5. request.auth — Authentication token/credentials
    print(request.auth)
    # Token object or None
    
    # 6. request.content_type — What format was sent
    print(request.content_type)
    # 'application/json'
    
    # 7. request.META — All HTTP headers and server info
    print(request.META.get('HTTP_AUTHORIZATION'))
    # 'Token abc123...'
    
    # 8. request.FILES — Uploaded files
    print(request.FILES)
    # {'image': <UploadedFile: photo.jpg>}
    
    return Response({'message': 'Request received'})
request.data vs Django's request.POST and request.body:

# Plain Django — Different methods for different content types:
request.POST          # Only works for form data
request.body          # Raw bytes — you need json.loads()
request.GET           # Query parameters

# DRF — One method for everything:
request.data          # Works for JSON, form data, files — EVERYTHING
request.query_params  # Query parameters (cleaner name than .GET)
```

## 4.5 Using get_object_or_404

```python

from django.shortcuts import get_object_or_404

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    # Instead of try/except, use this shortcut:
    book = get_object_or_404(Book, pk=pk)
    # If book doesn't exist, automatically returns 404 response
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    # ... rest of the view
```

Common Mistake: Forgetting status= in Response.

```python

return Response(serializer.data, status.HTTP_201_CREATED)    # WRONG
return Response(serializer.data, status=status.HTTP_201_CREATED)  # CORRECT
```

## Practice Exercise — Chapter 4

```text

Exercise 4.1:
  Build a complete CRUD API for a "Student" model using 
  function-based views with @api_view:
  
  Endpoints:
    GET    /api/students/      → List all students
    POST   /api/students/      → Create a student
    GET    /api/students/5/    → Get student id=5
    PUT    /api/students/5/    → Full update
    PATCH  /api/students/5/    → Partial update
    DELETE /api/students/5/    → Delete
  
  Test all 6 operations using the browsable API.

Exercise 4.2:
  Add a search feature to your book_list view:
    GET /api/books/?search=python
    → Returns only books whose title contains "python"
    
  Hint: Use request.query_params.get('search', '')
        and Book.objects.filter(title__icontains=search)
```
