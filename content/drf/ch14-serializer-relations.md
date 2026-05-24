---
title: Chapter 14 — Serializer Relations
description: PrimaryKeyRelatedField, HyperlinkedRelatedField, and representing foreign keys in DRF
order: 14
tags: [drf, serializers, relations]
---

# Chapter 14: Serializer Relations

Relational fields connect serializers to other models. DRF provides several ways to represent **ForeignKey**, **ManyToMany**, and reverse relations — from compact IDs to hyperlinks and nested objects.

## Definitions

| Term | Meaning |
|------|---------|
| **Related field** | Serializer field that reads/writes a relation to another model. |
| **PrimaryKeyRelatedField** | Accepts/returns the related object's primary key. |
| **HyperlinkedRelatedField** | Accepts/returns a URL to the related resource. |
| **SlugRelatedField** | Uses a unique slug field instead of PK. |
| **StringRelatedField** | Read-only; uses `__str__` on the related model. |

---

## 14.1 PrimaryKeyRelatedField

The most common choice for writable APIs: send and receive integer (or UUID) IDs.

### Model setup

```python
# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    tags = models.ManyToManyField('Tag', blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=50)
```

### Serializer

```python
from rest_framework import serializers
from .models import Product, Category, Tag

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'tags']
```

### Request/response

```json
{
    "id": 1,
    "name": "Laptop",
    "category": 3,
    "tags": [1, 5, 8]
}
```

```bash
curl -X POST http://127.0.0.1:8000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Phone", "category": 2, "tags": [1]}'
```

### Options

```python
category = serializers.PrimaryKeyRelatedField(
    queryset=Category.objects.all(),
    allow_null=True,       # FK nullable
    required=False,
)

tags = serializers.PrimaryKeyRelatedField(
    queryset=Tag.objects.all(),
    many=True,
    allow_empty=True,
)
```

### Read-only related display

```python
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    category_name = serializers.StringRelatedField(source='category')

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'category_name']
```

### SlugRelatedField alternative

When clients know slugs instead of IDs:

```python
category = serializers.SlugRelatedField(
    queryset=Category.objects.all(),
    slug_field='slug'
)
```

```json
{"name": "Tablet", "category": "electronics"}
```

### Interview points

- **queryset** is required on writable `PrimaryKeyRelatedField` for validation.
- Invalid PK → **400** validation error: `"Invalid pk \"99\" - object does not exist."`
- For large related tables, narrow **queryset** (active only) or use autocomplete endpoints.
- `ModelSerializer` auto-creates `PrimaryKeyRelatedField` for FK/M2M — explicit declaration overrides behavior.

---

## 14.2 HyperlinkedRelatedField

Represents relations as **URLs**, aligning with HATEOAS-style APIs. Requires named URL patterns.

### URL configuration

```python
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

### Serializer

```python
class ProductSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
      model = Product
      fields = ['url', 'id', 'name', 'category', 'tags']
      extra_kwargs = {
          'url': {'view_name': 'product-detail', 'lookup_field': 'pk'},
          'category': {'view_name': 'category-detail', 'lookup_field': 'pk'},
          'tags': {'view_name': 'tag-detail', 'lookup_field': 'pk'},
      }
```

Or explicit fields:

```python
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        view_name='category-detail',
        queryset=Category.objects.all(),
        lookup_field='pk'
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'category']
```

### Request/response

```json
{
    "id": 1,
    "name": "Laptop",
    "category": "http://127.0.0.1:8000/api/categories/3/"
}
```

```bash
curl -X POST http://127.0.0.1:8000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Phone", "category": "http://127.0.0.1:8000/api/categories/2/"}'
```

### HyperlinkedIdentityField

Reverse relation as a list of URLs:

```python
class CategorySerializer(serializers.ModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail'
    )

    class Meta:
        model = Category
        fields = ['id', 'name', 'products']
```

### Global hyperlink settings

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
}
```

Use `reverse()` view names consistently; with routers, view names are like `product-detail`, `category-detail`.

### Interview points

- **HyperlinkedRelatedField** needs correct **view_name** and request context for absolute URLs.
- Clients must send **full URL** on write (or relative if configured) — less convenient than PK for mobile apps.
- **HyperlinkedModelSerializer** auto-generates URL fields for model relations.
- PK fields are more common in practice; hyperlinks excel in **discoverable**, **browser-navigable** APIs.

---

## 14.3 All relation field types (Bookstore example)

Models with relationships:

```python
# books/models.py
from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['book', 'user']
```

### Approach 1: Default (PrimaryKeyRelatedField)

```python
class BookSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
# Output: {"author": 1, "category": 3}
```

### Approach 2: StringRelatedField (read-only)

```python
class BookSerializer2(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = '__all__'
# Output: {"author": "J.K. Rowling", "category": "Fiction"}
```

### Approach 3: SlugRelatedField (read + write by slug)

```python
class BookSerializer3(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='name', queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = '__all__'
# Write: {"author": "J.K. Rowling"} instead of ID
```

### Approach 4: HyperlinkedRelatedField

```python
class BookSerializer4(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
# Output: {"author": "http://localhost:8000/api/authors/1/"}
```

### Approach 5: Nested serializer (most detailed)

```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class BookSerializer5(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True,
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_id', 'price']

# Read:  {"author": {"id": 1, "name": "Rowling", "email": "..."}}
# Write: {"author_id": 1, "title": "..."}
```

---

## Chapter summary

| Field | Write | Read | Typical use |
|-------|-------|------|-------------|
| `PrimaryKeyRelatedField` | PK | PK | Mobile/SPA APIs |
| `SlugRelatedField` | slug | slug | Human-readable keys |
| `StringRelatedField` | — | `__str__` | Display only |
| `HyperlinkedRelatedField` | URL | URL | HATEOAS / browsable API |

Choose **PK** for simplicity; choose **hyperlinks** when URL identity is part of your API contract.
