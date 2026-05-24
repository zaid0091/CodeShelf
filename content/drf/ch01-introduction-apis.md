---
title: Introduction — Understanding APIs
description: APIs, REST principles, JSON, HTTP methods, status codes, and DRF architecture overview.
order: 1
tags: [drf, apis, rest, http, json]
---

# Chapter 1: Introduction — Understanding APIs

## 1.1 What is an API?

Imagine you go to a restaurant. You sit at your table, but you cannot go into the kitchen and cook food yourself. Instead, there is a waiter who takes your order, goes to the kitchen, tells the chef what you want, and brings the food back to your table.

In the world of software:

You (the customer) = The Frontend (React, Mobile App, another system)
The Kitchen = The Backend (Database, Server, Business Logic)
The Waiter = The API
```text

YOU (Frontend)  →  WAITER (API)  →  KITCHEN (Backend/Database)
                                          ↓
YOU (Frontend)  ←  WAITER (API)  ←  FOOD (Data/Response)
```

> **Definition:** An API (Application Programming Interface) is a set of rules and endpoints that allows one piece of software to talk to another piece of software. It defines how to request data, what data you can request, and what format the response will come in.

### Why do we need APIs?

Without APIs, every application would need to directly access the database. This creates problems:

Security — anyone could read/modify your data
No control — you cannot limit what data is exposed
No structure — every app would query differently
No separation — frontend and backend are tightly coupled
With APIs:

You control exactly what data is exposed
You add authentication and permissions
Every client uses the same standard interface
Frontend and backend are completely independent
### Real-World Examples of APIs:

```text

When you open a weather app:
  Your Phone → Weather API → Weather Database → API → Your Phone
  
When you pay with Google Pay:
  Google Pay App → Payment API → Bank Server → API → Google Pay App

When you log in with Google on a website:
  Website → Google OAuth API → Google Servers → API → Website
```

## 1.2 What is a REST API?

Not all APIs are the same. There are different styles of building APIs:

SOAP (old, complex, XML-based)
GraphQL (newer, flexible, single endpoint)
gRPC (fast, binary, used internally)
REST (most popular, simple, uses HTTP)
REST stands for REpresentational State Transfer.

### Think of REST like a library system:

```text

You want a book → You go to the BOOKS section → You find book #42
                   (Resource)                     (Identifier)

In REST API terms:
You want user data → You go to /users/ endpoint → You find /users/42/
                     (Resource Collection)         (Specific Resource)
```

REST has 6 rules (constraints):

```text

1. CLIENT-SERVER
   → Frontend and Backend are SEPARATE
   → They only talk through the API
   
2. STATELESS
   → Server does NOT remember previous requests
   → Every request must contain ALL information needed
   → Like a forgetful waiter — you must repeat your table number every time
   
3. UNIFORM INTERFACE
   → Use standard HTTP methods (GET, POST, PUT, DELETE)
   → Use standard URLs (/users/, /books/42/)
   → Use standard formats (JSON)
   
4. CACHEABLE
   → Responses can be cached (saved temporarily)
   → So the same request doesn't hit the database every time
   
5. LAYERED SYSTEM
   → Can have load balancers, proxies between client and server
   → Client doesn't need to know about these layers
   
6. CODE ON DEMAND (Optional)
   → Server can send executable code to client
   → Rarely used in practice
```

> **Definition:** A REST API is an API that follows REST architectural principles. It uses standard HTTP methods to perform operations on resources identified by URLs, and typically exchanges data in JSON format.

## 1.3 JSON Basics

JSON (JavaScript Object Notation) is the language APIs use to communicate. Think of it as a universal translator — no matter what language your frontend or backend uses, they both understand JSON.

```json

{
    "name": "Harry Potter",
    "author": "J.K. Rowling",
    "price": 499.99,
    "is_available": true,
    "genres": ["Fantasy", "Adventure", "Fiction"],
    "publisher": {
        "name": "Bloomsbury",
        "country": "UK"
    },
    "ratings": null
}
```

### JSON data types:

```text

String   → "hello"          (text in double quotes)
Number   → 42, 3.14         (integer or decimal)
Boolean  → true, false      (yes or no)
Null     → null             (empty/nothing)
Array    → [1, 2, 3]        (list of items)
Object   → {"key": "value"} (key-value pairs)
```

### JSON vs Python Dictionary:

```text

JSON                          Python Dict
────────────────────────────────────────────
"name": "John"                'name': 'John'
true / false                  True / False
null                          None
Keys MUST be strings          Keys can be anything
Double quotes ONLY            Single or double quotes
```

### Why JSON and not HTML?

```text

HTML is for HUMANS (browsers render it visually):
  <h1>Harry Potter</h1>
  <p>Price: 499.99</p>

JSON is for MACHINES (programs parse it easily):
  {"title": "Harry Potter", "price": 499.99}
  
A mobile app cannot understand HTML structure.
But it can easily read JSON and display it however it wants.
```

## 1.4 HTTP Methods

HTTP methods are the verbs of the internet. They tell the server what action you want to perform.

### Think of a NOTEBOOK:

GET     → READ a page             → "Show me what's written"
POST    → WRITE a new page        → "Add this new entry"
PUT     → REWRITE an entire page  → "Replace everything on this page"
PATCH   → EDIT part of a page     → "Change just the title"
DELETE  → TEAR OUT a page         → "Remove this page"
Detailed breakdown:

```python

# GET — Retrieve data (SAFE — doesn't change anything)
# "Give me all books" or "Give me book #5"
GET /api/books/          → Returns list of all books
GET /api/books/5/        → Returns book with id=5

# POST — Create new data
# "Here's a new book, please save it"
POST /api/books/         → Creates a new book
# Request body: {"title": "New Book", "price": 299}

# PUT — Replace entire resource (ALL fields required)
# "Replace ALL information of book #5"
PUT /api/books/5/        → Replaces ALL fields of book 5
# Request body: {"title": "Updated", "author": "New Author", "price": 399}
# If you forget a field, it becomes null/default!

# PATCH — Update part of resource (only changed fields)
# "Just change the price of book #5"
PATCH /api/books/5/      → Updates only specified fields
# Request body: {"price": 199}
# Other fields remain unchanged!

# DELETE — Remove a resource
# "Delete book #5"
DELETE /api/books/5/     → Deletes book with id=5
```

### PUT vs PATCH — The Difference:

```text

Imagine a student profile:
{
    "name": "Rahul",
    "age": 20,
    "city": "Mumbai",
    "phone": "9999999999"
}

PUT (Full Update) — You must send ALL fields:
{"name": "Rahul", "age": 21, "city": "Mumbai", "phone": "9999999999"}
If you send only {"age": 21}, other fields may be erased!

PATCH (Partial Update) — Send only what changed:
{"age": 21}
Other fields stay the same. Much safer for small changes!
```

### 🎯 Interview Point

**What is the difference between PUT and PATCH?**

PUT replaces the entire resource — all fields are required. If you omit a field, it may be set to null.
PATCH updates only the specified fields — other fields remain unchanged.
PUT is idempotent (same result no matter how many times you call it).
PATCH is also typically idempotent in practice, but technically doesn't have to be.

## 1.5 HTTP Status Codes

When you send a request to an API, the server responds with a status code — a number that tells you what happened.

### Think of traffic lights:

```text

🟢 2xx = GREEN  = Success! Everything is fine.
🟡 3xx = YELLOW = Redirect. Go somewhere else.
🔴 4xx = RED    = Your mistake. You did something wrong.
💀 5xx = SKULL  = Server's mistake. Something broke on their end.
The most important status codes:

SUCCESS (2xx):
  200 OK                  → Request successful (general success)
  201 Created             → New resource was created (after POST)
  204 No Content          → Success but nothing to return (after DELETE)

REDIRECT (3xx):
  301 Moved Permanently   → Resource moved to a new URL forever
  302 Found               → Resource temporarily at a different URL
  304 Not Modified        → Cached version is still valid

CLIENT ERRORS (4xx) — YOUR fault:
  400 Bad Request         → You sent invalid data
  401 Unauthorized        → You're not logged in (no credentials)
  403 Forbidden           → You're logged in but not allowed
  404 Not Found           → Resource doesn't exist
  405 Method Not Allowed  → HTTP method not supported on this endpoint
  409 Conflict            → Conflicts with current state (duplicate)
  422 Unprocessable Entity → Data format is correct but content is invalid
  429 Too Many Requests   → You're being rate-limited (slow down!)

SERVER ERRORS (5xx) — SERVER'S fault:
  500 Internal Server Error → Something crashed on the server
  502 Bad Gateway           → Server got invalid response from upstream
  503 Service Unavailable   → Server is overloaded or down for maintenance
Real-world analogy:

You walk into a restaurant:

200 → "Here's your food, enjoy!" ✅
201 → "Your reservation has been made!" ✅
204 → "Your reservation has been cancelled." ✅ (nothing to show)

400 → "Sir, you can't order a 'purple pizza'. That doesn't exist." ❌
401 → "Sir, you need a membership card to enter." 🔒
403 → "Sir, you have a basic membership. The VIP area is not for you." 🚫
404 → "Sir, there is no table #99. We only have 50 tables." ❓
429 → "Sir, you've already ordered 10 times in 1 minute. Please wait." ⏰

500 → "Sorry, our kitchen caught fire." 🔥
503 → "Sorry, we're closed for renovation." 🚧
```

## 1.6 Request-Response Cycle

Every API interaction follows this cycle:

```text

STEP 1: CLIENT SENDS REQUEST
┌────────────────────────────────────────────┐
│  Request:                                  │
│    Method: POST                            │
│    URL: https://api.example.com/books/     │
│    Headers:                                │
│      Content-Type: application/json        │
│      Authorization: Token abc123           │
│    Body:                                   │
│      {"title": "New Book", "price": 299}   │
└────────────────────────────────────────────┘
                    │
                    ▼
STEP 2: SERVER PROCESSES REQUEST
┌────────────────────────────────────────────┐
│  DRF internally:                           │
│  1. URL Router finds the right view        │
│  2. Authentication — Who is this user?     │
│  3. Permissions — Can they do this?        │
│  4. Throttling — Are they sending too many?│
│  5. Parser — Convert JSON to Python dict   │
│  6. Serializer — Validate the data         │
│  7. View logic — Save to database          │
│  8. Serializer — Convert Python to JSON    │
│  9. Renderer — Format the response         │
└────────────────────────────────────────────┘
                    │
                    ▼
STEP 3: SERVER SENDS RESPONSE
┌────────────────────────────────────────────┐
│  Response:                                 │
│    Status Code: 201 Created                │
│    Headers:                                │
│      Content-Type: application/json        │
│    Body:                                   │
│      {"id": 1, "title": "New Book",        │
│       "price": 299}                        │
└────────────────────────────────────────────┘
```

## 1.7 What is Django REST Framework?

```text

Django alone:
  - Builds WEBSITES that return HTML pages
  - Uses templates to render pages
  - Good for server-side rendered apps
  
Django + DRF:
  - Builds APIs that return JSON data
  - Uses serializers to convert data
  - Good for mobile apps, SPAs, microservices
```

> **Definition:** Django REST Framework (DRF) is a powerful and flexible toolkit built on top of Django that makes it easy to build Web APIs. It provides serializers, views, authentication, permissions, pagination, and many other tools specifically designed for API development.

### Why DRF and not just Django views?

You CAN build APIs with plain Django:

```python

# Plain Django API view (without DRF)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        data = []
        for book in books:
            data.append({
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'price': float(book.price),
            })
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        body = json.loads(request.body)
        # Manual validation...
        if not body.get('title'):
            return JsonResponse({'error': 'Title required'}, status=400)
        # Manual creation...
        book = Book.objects.create(
            title=body['title'],
            author=body['author'],
            price=body['price'],
        )
        return JsonResponse({
            'id': book.id,
            'title': book.title,
        }, status=201)
```

Problems with this approach:

Manual JSON conversion for every model
Manual validation — no automatic error messages
Manual status codes
No authentication system
No permissions system
No pagination
No browsable API for testing
CSRF issues
No content negotiation
Lots of repetitive code
Same thing with DRF:

```python

# DRF API view — clean, simple, powerful
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
That is 3 lines to get full CRUD API with validation, authentication, pagination, and more!

```

What DRF gives you:

```text

┌─────────────────────────────────────────────────┐
│           Django REST Framework                  │
├─────────────────────────────────────────────────┤
│  Serializers    → Convert data to/from JSON     │
│  Views          → Handle API requests           │
│  Authentication → Who are you?                  │
│  Permissions    → What can you do?              │
│  Throttling     → How often can you ask?        │
│  Pagination     → Split results into pages      │
│  Filtering      → Search and filter data        │
│  Renderers      → Format output (JSON/HTML)     │
│  Parsers        → Read input (JSON/Form/File)   │
│  Validators     → Check if data is correct      │
│  Routers        → Auto-generate URLs            │
│  Browsable API  → Test API in browser           │
│  Test utilities → Write API tests easily        │
└─────────────────────────────────────────────────┘
```

## 1.8 DRF Architecture Overview

```text

┌──────────────────────────────────────────────────────────────────┐
│                     DRF REQUEST LIFECYCLE                        │
│                                                                  │
│  Client Request                                                  │
│       │                                                          │
│       ▼                                                          │
│  ┌─────────┐                                                     │
│  │  URLs   │  → Django URL dispatcher + DRF Router               │
│  └────┬────┘                                                     │
│       ▼                                                          │
│  ┌─────────────────┐                                             │
│  │  Middleware      │  → CORS, CSRF, Security checks             │
│  └────┬────────────┘                                             │
│       ▼                                                          │
│  ┌─────────────────┐                                             │
│  │  Authentication  │  → Identify the user (Token? JWT? Session?)│
│  └────┬────────────┘                                             │
│       ▼                                                          │
│  ┌─────────────────┐                                             │
│  │  Permissions     │  → Can this user perform this action?      │
│  └────┬────────────┘                                             │
│       ▼                                                          │
│  ┌─────────────────┐                                             │
│  │  Throttling      │  → Is this user sending too many requests? │
│  └────┬────────────┘                                             │
│       ▼                                                          │
│  ┌─────────────────┐                                             │
│  │  Content Negotiation │  → What format? (JSON, XML, etc.)     │
│  └────┬────────────┘                                             │
│       ▼                                                          │
│  ┌─────────────────┐                                             │
│  │  Parser          │  → Parse request body (JSON → Python dict) │
│  └────┬────────────┘                                             │
│       ▼                                                          │
│  ┌─────────────────┐                                             │
│  │  VIEW            │  → Your business logic runs here           │
│  │  (uses Serializer│     - Validate input data                  │
│  │   and Model)     │     - Query database                       │
│  │                  │     - Process data                          │
│  └────┬────────────┘     - Serialize output                      │
│       ▼                                                          │
│  ┌─────────────────┐                                             │
│  │  Renderer        │  → Convert Python → JSON (or HTML/XML)    │
│  └────┬────────────┘                                             │
│       ▼                                                          │
│  Response sent to Client                                         │
└──────────────────────────────────────────────────────────────────┘
```

## Practice Exercise — Chapter 1

```text

Exercise 1.1: Answer these questions:
```

### a) What HTTP method would you use to update ONLY the email of a user?

### b) What status code does the server return when you create a new resource?

### c) What is the difference between 401 and 403?

  d) Convert this Python dict to valid JSON:
     {'name': 'John', 'active': True, 'age': None}
  e) What is wrong with this URL design: POST /api/deleteUser/5/

Exercise 1.2: Design REST API URLs for a Library system:
  - List all members
  - Add a new member
  - Get details of member #7
  - Update member #7's phone number
  - Delete member #7
  - List all books borrowed by member #7
