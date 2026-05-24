---
title: Setup & Configuration
description: Install Django and DRF, project structure, settings, models, admin, migrations, and API testing tools.
order: 2
tags: [drf, setup, django, configuration]
---

# Chapter 2: Setup & Configuration

## 2.1 Installing Django and DRF

```bash

# Step 1: Create a project folder
mkdir bookstore_api
cd bookstore_api

# Step 2: Create virtual environment
python -m venv venv

# Step 3: Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Step 4: Install Django and DRF
pip install django
pip install djangorestframework

# Step 5: Create Django project
django-admin startproject config .
# The dot (.) means "create in current directory"
# "config" is a popular name for the project folder
# because it contains configuration files

# Step 6: Create an app
python manage.py startapp books

# Step 7: Verify installation
python -c "import rest_framework; print(rest_framework.VERSION)"
```

### Why "config" as project name?

Many developers name the project "config" because:
  config/
    settings.py   ← Configuration
    urls.py       ← Configuration
    wsgi.py       ← Configuration

It makes more sense than:
  myproject/
    settings.py   ← This is config, not "myproject"
## 2.2 Project Structure

```text

bookstore_api/              ← Root folder
├── config/                 ← Project configuration
│   ├── __init__.py
│   ├── settings.py         ← All settings
│   ├── urls.py             ← Root URL configuration
│   ├── asgi.py             ← ASGI server config
│   └── wsgi.py             ← WSGI server config
├── books/                  ← Our app
│   ├── __init__.py
│   ├── admin.py            ← Admin panel config
│   ├── apps.py             ← App config
│   ├── models.py           ← Database models
│   ├── serializers.py      ← CREATE THIS FILE (DRF)
│   ├── views.py            ← API views
│   ├── urls.py             ← CREATE THIS FILE (App URLs)
│   ├── tests.py            ← Tests
│   └── migrations/         ← Database migration files
│       └── __init__.py
├── venv/                   ← Virtual environment
├── manage.py               ← Django management command
└── db.sqlite3              ← Database (created after migrate)
```

## 2.3 Configure settings.py

```python

# config/settings.py

INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',           # ← ADD THIS — enables DRF
    
    # Local apps (your apps)
    'books',                    # ← ADD THIS — your app
]
```

### Why do we add rest_framework to INSTALLED_APPS?

```text

When you add 'rest_framework' to INSTALLED_APPS, Django:
1. Loads DRF's template files (for the browsable API)
2. Loads DRF's static files (CSS/JS for the browsable API)
3. Makes DRF's management commands available
4. Registers DRF's configuration

Without it, DRF's browsable API won't render properly,
and some features won't work.
```

## 2.4 Create the Model

```python

# books/models.py

from django.db import models

class Book(models.Model):
    """
    Each book in our bookstore.
    This is the DATABASE TABLE definition.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']   # Newest first
        verbose_name_plural = 'Books'

    def __str__(self):
        return f"{self.title} by {self.author}"
Field explanations:

```

```text

CharField(max_length=200)     → Short text (title, name)
TextField()                   → Long text (description, bio)
DecimalField(8, 2)           → Precise numbers (money: 999999.99)
DateField()                   → Date only (2024-01-15)
DateTimeField()               → Date + Time (2024-01-15 10:30:00)
BooleanField()                → True/False
PositiveIntegerField()        → Positive whole numbers (0, 1, 2...)
CharField(unique=True)        → No duplicates allowed

auto_now_add=True → Set ONCE when created (never changes)
auto_now=True     → Updates EVERY time the object is saved
blank=True        → Form/serializer can submit empty value
null=True         → Database can store NULL
default=''        → Default value if nothing provided
```

## 2.5 Register in Admin

```python

# books/admin.py

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'price', 'is_available', 'created_at']
    list_filter = ['is_available', 'author']
    search_fields = ['title', 'author', 'isbn']
    list_editable = ['is_available']
    readonly_fields = ['created_at', 'updated_at']
```

## 2.6 Run Migrations and Create Superuser

```bash

# Create migration files (SQL instructions)
python manage.py makemigrations

# Apply migrations (create tables in database)
python manage.py migrate

# Create admin user
python manage.py createsuperuser
# Username: admin
# Email: admin@example.com
# Password: admin123 (for development only!)

# Run the server
python manage.py runserver
```

### What happens during migration?

```text

makemigrations:
  Reads your models.py
  → Creates migration files (like SQL blueprints)
  → books/migrations/0001_initial.py

migrate:
  Reads migration files
  → Executes SQL to create/modify database tables
  → Creates the 'books_book' table with all columns
```

## 2.7 API Testing Tools

You need a way to test your API (send requests and see responses).

### Option 1: Browser (DRF Browsable API)

```text

Just visit http://127.0.0.1:8000/api/books/ in your browser.
DRF provides a beautiful HTML interface to test APIs.
This is one of DRF's best features!
```

### Option 2: Postman (Most Popular)

```text

Download from: https://www.postman.com/
- Free desktop app
- Save requests in collections
- Set headers, body, auth easily
- See formatted responses
- Share with team
```

### Option 3: Thunder Client (VS Code Extension)

```text

Install from VS Code Extensions marketplace.
- Works inside VS Code
- Lightweight alternative to Postman
- Free
```

### Option 4: curl (Command Line)

```bash

# GET request
curl http://127.0.0.1:8000/api/books/

# POST request with JSON data
curl -X POST http://127.0.0.1:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Book", "price": "299.99"}'

# With authentication token
curl http://127.0.0.1:8000/api/books/ \
  -H "Authorization: Token abc123def456"
```

### Option 5: httpie (Friendlier command line)

```bash

pip install httpie

# GET
http GET http://127.0.0.1:8000/api/books/

# POST
http POST http://127.0.0.1:8000/api/books/ title="Test" price=299.99
```

## Practice Exercise — Chapter 2

```text

Exercise 2.1:
  a) Create a new Django project called "school_api"
  b) Create an app called "students"
  c) Create a Student model with fields:
     - name (CharField, max 100)
     - email (EmailField, unique)
     - roll_number (IntegerField, unique)
     - grade (CharField, max 2)
     - date_of_birth (DateField)
     - is_active (BooleanField, default True)
     - enrolled_at (DateTimeField, auto_now_add)
  d) Register it in admin
  e) Run migrations
  f) Create a superuser
  g) Add 3 students through the admin panel
```
