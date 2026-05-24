---
title: Serializers
description: Serializer and ModelSerializer, fields, validation, nested serializers, and custom logic.
order: 3
tags: [drf, serializers, validation]
---

# Chapter 3: Serializers

## 3.1 What is a Serializer?

Think about how you communicate with someone who speaks a different language. You need a translator.

```text

Your brain thinks in English → Translator → Other person hears in Spanish
Other person speaks Spanish  → Translator → You hear in English
In DRF:

Database stores data in Python objects → Serializer → Client receives JSON
Client sends JSON data               → Serializer → Database stores Python objects
Two directions:

SERIALIZATION (Python → JSON):
  Book object from database
  → Serializer converts it
  → JSON sent to client
  
  Book(title="Harry Potter", price=499)
  →  {"title": "Harry Potter", "price": 499}

DESERIALIZATION (JSON → Python):
  JSON received from client
  → Serializer validates it
  → Serializer converts it
  → Python object saved to database
  
  {"title": "New Book", "price": 299}
  → validates (is price positive? is title provided?)
  → Book(title="New Book", price=299)
  → saved to database
```

> **Definition:** A Serializer in DRF converts complex data types (like Django model instances or querysets) into Python native datatypes that can then be rendered into JSON. It also handles validation and deserialization — converting incoming JSON data back into complex types after validating the data.

### Why not just use json.dumps() and json.loads()?

```python

import json

# This FAILS with Django model objects:
book = Book.objects.get(id=1)
json.dumps(book)  # TypeError: Object of type Book is not JSON serializable

# You'd have to manually do:
data = {
    'id': book.id,
    'title': book.title,
    'price': float(book.price),  # Decimal isn't JSON serializable either!
    'published_date': str(book.published_date),  # Date isn't either!
}
json.dumps(data)  # Now it works, but SO much manual work!

# And for validation on incoming data:
body = json.loads(request.body)
```

### # Is title provided? Is it a string? Is it under 200 chars?

### # Is price a number? Is it positive?

### # Is published_date a valid date?

# YOU have to check ALL of this manually!

# Serializers handle ALL of this automatically!
## 3.2 Basic Serializer (serializers.Serializer)

Let's start with the most basic type of serializer where you define every field manually.

```python

# books/serializers.py

from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    """
    Basic Serializer — you define each field manually.
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False, allow_blank=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    published_date = serializers.DateField()
    isbn = serializers.CharField(max_length=13)
    pages = serializers.IntegerField(default=0)
    is_available = serializers.BooleanField(default=True)
    
    def create(self, validated_data):
        """
        Called when you do serializer.save() on NEW data.
        validated_data = data that passed all validation checks.
        """
        from .models import Book
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Called when you do serializer.save() on EXISTING data.
        instance = the existing Book object from database.
        validated_data = the new data to update with.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.pages = validated_data.get('pages', instance.pages)
        instance.is_available = validated_data.get('is_available', instance.is_available)
        instance.save()
        return instance
```

How validated_data.get('title', instance.title) works:

```python

# .get(key, default) returns the value for key if it exists,
# otherwise returns the default.

# If user sends {"title": "New Title"}:
validated_data.get('title', instance.title)
# → Returns "New Title" (the new value)

# If user sends {} (no title):
validated_data.get('title', instance.title)
# → Returns instance.title (keeps the old value)
```

## 3.3 ModelSerializer (The Better Way)

ModelSerializer is like Serializer but smarter. It automatically:

Creates fields based on your model
Creates create() method
Creates update() method
Adds validators from your model (unique, max_length, etc.)
```python

# books/serializers.py

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    ModelSerializer — automatically generates everything from the model.
    """
    class Meta:
        model = Book                    # Which model to serialize
        fields = '__all__'              # Include ALL fields
That is it. Those 4 lines replace the entire 40+ line Serializer from above!

Different ways to specify fields:

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        
        # Option 1: ALL fields
        fields = '__all__'
        
        # Option 2: Specific fields only (RECOMMENDED for security)
        fields = ['id', 'title', 'author', 'price', 'is_available']
        
        # Option 3: All fields EXCEPT some
        exclude = ['created_at', 'updated_at']
        
        # Note: You can use either 'fields' or 'exclude', NOT both!
```

Common Mistake: Using fields = '__all__' in production. This exposes ALL fields including sensitive ones. Always explicitly list the fields you want to expose.

### 🎯 Interview Point

**What is the difference between Serializer and ModelSerializer?**

Serializer: You manually define every field and must write create() and update() methods yourself.
ModelSerializer: Automatically generates fields from the model, automatically creates create() and update() methods, and includes model-level validators. It's a shortcut that reduces boilerplate code significantly.
Use Serializer when your data doesn't map to a model (like login data). Use ModelSerializer when it does.
What does ModelSerializer generate behind the scenes?
You can check by running this in Django shell:

```bash

python manage.py shell
```

```python

from books.serializers import BookSerializer

# Print what fields DRF generated
serializer = BookSerializer()
print(repr(serializer))
Output:

```

```text

BookSerializer():
    id = IntegerField(label='ID', read_only=True)
    title = CharField(max_length=200)
    author = CharField(max_length=100)
    description = CharField(allow_blank=True, required=False, style={'base_template': 'textarea.html'})
    price = DecimalField(decimal_places=2, max_digits=8)
    published_date = DateField()
    isbn = CharField(max_length=13, validators=[<UniqueValidator(queryset=Book.objects.all())>])
    pages = IntegerField(required=False)
    is_available = BooleanField(required=False)
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)
Notice:

id is automatically read_only=True (you can't set the ID)
isbn has UniqueValidator automatically (because model has unique=True)
created_at is read_only=True (because of auto_now_add=True)
description has required=False (because model has blank=True)
```

## 3.4 Serializer Fields in Detail

```python

from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
        # read_only_fields — user CANNOT set these
        read_only_fields = ['id', 'created_at', 'updated_at']
        
        # extra_kwargs — add extra options to auto-generated fields
        extra_kwargs = {
            'title': {
                'required': True,
                'min_length': 2,
                'max_length': 200,
                'help_text': 'The title of the book',
                'error_messages': {
                    'required': 'You must provide a title!',
                    'blank': 'Title cannot be empty!',
                    'min_length': 'Title must be at least 2 characters!',
                },
            },
            'price': {
                'min_value': 0,
                'max_value': 99999.99,
                'error_messages': {
                    'min_value': 'Price cannot be negative!',
                },
            },
            'description': {
                'required': False,
                'allow_blank': True,
            },
            'isbn': {
                'required': True,
            },
            'author': {
                'required': True,
            },
        }
Field options explained:

```

```text

required=True       → Field MUST be provided (error if missing)
required=False      → Field is optional (can be omitted)
read_only=True      → Shown in output, but CANNOT be set in input
write_only=True     → Can be set in input, but NOT shown in output
                       (perfect for passwords!)
allow_blank=True    → Empty string "" is allowed (for CharFields)
allow_null=True     → null/None is allowed
default='value'     → Use this value if not provided
help_text='...'     → Description shown in browsable API
source='field_name' → Map to a different model field
read_only vs write_only:

read_only=True:
  GET response:  {"id": 1, "title": "Book"}     ← ID is SHOWN
  POST request:  {"id": 999, "title": "Book"}    ← ID is IGNORED
  
  Use for: id, created_at, computed fields

write_only=True:
  POST request:  {"password": "secret123"}       ← Password is ACCEPTED
  GET response:  {"username": "john"}             ← Password is HIDDEN
  
  Use for: passwords, confirmation fields
```

## 3.5 SerializerMethodField (Computed Fields)

Sometimes you want to include data in the response that is not directly a model field — it is computed or calculated.

```python

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    # These fields DON'T exist in the model — they're calculated
    discount_price = serializers.SerializerMethodField()
    title_length = serializers.SerializerMethodField()
    is_expensive = serializers.SerializerMethodField()
    summary = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'price', 
            'discount_price', 'title_length', 'is_expensive', 'summary',
            'is_available'
        ]
    
    def get_discount_price(self, obj):
        """
        Method name MUST be: get_<field_name>
        'obj' is the current Book instance being serialized.
        """
        return round(float(obj.price) * 0.9, 2)  # 10% discount
    
    def get_title_length(self, obj):
        return len(obj.title)
    
    def get_is_expensive(self, obj):
        return obj.price > 500
    
    def get_summary(self, obj):
        return f"{obj.title} by {obj.author} — ₹{obj.price}"
Output:

```

```json

{
    "id": 1,
    "title": "Harry Potter",
    "author": "J.K. Rowling",
    "price": "499.99",
    "discount_price": 449.99,
    "title_length": 12,
    "is_expensive": false,
    "summary": "Harry Potter by J.K. Rowling — ₹499.99",
    "is_available": true
}
Key Rule: SerializerMethodField is always read-only. You cannot send discount_price in a POST/PUT request — it is only shown in the response.

```

### 🎯 Interview Point

**How do you add a computed field to a serializer?**

Use SerializerMethodField(). Define a method named get_<field_name>(self, obj) that returns the computed value. The obj parameter is the model instance currently being serialized.

## 3.6 Validation

Validation is one of the most important features of serializers. It ensures that incoming data is correct and safe before saving to the database.

DRF validates data in this order:

```text

1. Field-level validation    → Each field checked individually
2. validate_<field>() methods → Your custom per-field validation
3. validate() method         → Cross-field validation (multiple fields)
4. Validators (model/field)  → UniqueValidator, etc.
Field-Level Validation
```

```python

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate_title(self, value):
        """
        Validate the 'title' field specifically.
        Method name MUST be: validate_<field_name>
        'value' is the value submitted for this field.
        """
        # Rule 1: Title cannot be all numbers
        if value.isdigit():
            raise serializers.ValidationError(
                "Title cannot be all numbers!"
            )
        
        # Rule 2: Title must have at least 2 words
        if len(value.split()) < 2:
            raise serializers.ValidationError(
                "Title must have at least 2 words!"
            )
        
        # Rule 3: Title cannot contain special characters
        import re
        if re.search(r'[!@#$%^&*()_+=\[\]{};:\'",.<>?/\\|`~]', value):
            raise serializers.ValidationError(
                "Title cannot contain special characters!"
            )
        
        # MUST return the value if valid
        return value
    
    def validate_price(self, value):
        """Validate price field"""
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than zero!"
            )
        if value > 50000:
            raise serializers.ValidationError(
                "Price cannot exceed ₹50,000!"
            )
        return value
    
    def validate_isbn(self, value):
        """Validate ISBN field"""
        if len(value) not in [10, 13]:
            raise serializers.ValidationError(
                "ISBN must be 10 or 13 characters long!"
            )
        if not value.isdigit():
            raise serializers.ValidationError(
                "ISBN must contain only digits!"
            )
        return value
    
    def validate_published_date(self, value):
        """Validate published_date field"""
        from datetime import date
        if value > date.today():
            raise serializers.ValidationError(
                "Published date cannot be in the future!"
            )
        return value
Object-Level Validation

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate(self, data):
        """
        Object-level validation — validate MULTIPLE fields together.
        'data' is a dictionary of ALL validated field values.
        This runs AFTER all field-level validations pass.
        """
        # Rule 1: Title and author cannot be the same
        title = data.get('title', '')
        author = data.get('author', '')
        if title.lower() == author.lower():
            raise serializers.ValidationError({
                'title': 'Title and author name cannot be the same!'
            })
        
        # Rule 2: Free books must be marked as available
        price = data.get('price', 0)
        is_available = data.get('is_available', True)
        if price == 0 and not is_available:
            raise serializers.ValidationError(
                "Free books must be marked as available!"
            )
        
        # Rule 3: Books with more than 1000 pages must cost more than ₹500
        pages = data.get('pages', 0)
        if pages > 1000 and price < 500:
            raise serializers.ValidationError(
                "Books with more than 1000 pages must cost at least ₹500!"
            )
        
        # MUST return data if valid
        return data
Validation Error Response
When validation fails, DRF automatically returns a 400 response:

```

```json

{
    "title": ["Title must have at least 2 words!"],
    "price": ["Price must be greater than zero!"],
    "isbn": ["ISBN must be 10 or 13 characters long!"]
}
External Validators
```

```python

# books/validators.py

from rest_framework.exceptions import ValidationError
import re

def validate_no_profanity(value):
    """Reusable validator — can be used on any CharField"""
    bad_words = ['spam', 'fake', 'xxx']
    for word in bad_words:
        if word.lower() in value.lower():
            raise ValidationError(
                f"The text contains inappropriate content: '{word}'"
            )

def validate_alphabetic(value):
    """Only letters and spaces allowed"""
    if not re.match(r'^[a-zA-Z\s]+$', value):
        raise ValidationError(
            "Only letters and spaces are allowed!"
        )

# books/serializers.py
from .validators import validate_no_profanity, validate_alphabetic

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=200,
        validators=[validate_no_profanity]  # Attach external validator
    )
    author = serializers.CharField(
        max_length=100,
        validators=[validate_alphabetic, validate_no_profanity]
    )
    
    class Meta:
        model = Book
        fields = '__all__'
```

### 🎯 Interview Point

**Explain the validation flow in DRF serializers.**

Field deserialization — Each field converts input to Python type (e.g., string "123" to int 123). If conversion fails, error is raised.
Field validators — Built-in validators (max_length, min_value) and custom validators run.
validate_<field>() methods — Your per-field validation methods run.
validate() method — Your object-level validation runs (can check multiple fields together).
If all pass → validated_data is populated and ready to use.
If any fail → serializer.errors contains the error details.

## 3.7 Testing Serializers in Django Shell

```bash

python manage.py shell
```

```python

from books.models import Book
from books.serializers import BookSerializer

# ===== SERIALIZATION (Model → JSON-ready dict) =====

# Create a book first
book = Book.objects.create(
    title="The Alchemist",
    author="Paulo Coelho",
    price=299.99,
    published_date="2023-01-15",
    isbn="9780062315007",
    pages=197
)

# Serialize ONE object
serializer = BookSerializer(book)
print(serializer.data)
# {'id': 1, 'title': 'The Alchemist', 'author': 'Paulo Coelho', 
#  'price': '299.99', ...}
# This is an OrderedDict — ready to be converted to JSON

# Serialize MULTIPLE objects (QuerySet)
books = Book.objects.all()
serializer = BookSerializer(books, many=True)  # many=True is REQUIRED!
print(serializer.data)
# [{'id': 1, ...}, {'id': 2, ...}, ...]

# ===== DESERIALIZATION (dict → Model) =====

# Incoming data (as if from a POST request)
input_data = {
    'title': 'New Book Title',
    'author': 'New Author',
    'price': '499.99',
    'published_date': '2024-06-01',
    'isbn': '1234567890123',
    'pages': 300,
}

# Create serializer with data
serializer = BookSerializer(data=input_data)

# ALWAYS validate before saving!
if serializer.is_valid():
    book = serializer.save()  # Calls create() internally
    print(f"Created: {book}")
    print(f"Saved data: {serializer.data}")
else:
    print(f"Errors: {serializer.errors}")

# ===== UPDATE (dict → existing Model) =====

existing_book = Book.objects.get(id=1)
update_data = {'price': '199.99', 'is_available': False}

serializer = BookSerializer(
    instance=existing_book,     # The object to update
    data=update_data,           # The new data
    partial=True                # Partial update (like PATCH)
)

if serializer.is_valid():
    updated_book = serializer.save()  # Calls update() internally
    print(f"Updated: {updated_book.price}")
else:
    print(f"Errors: {serializer.errors}")

# ===== VALIDATION DEMO =====

bad_data = {
    'title': '',        # Empty title
    'price': '-50',     # Negative price
}

serializer = BookSerializer(data=bad_data)
is_valid = serializer.is_valid()   # Returns False
print(is_valid)                    # False
print(serializer.errors)
# {'title': ['This field may not be blank.'],
#  'author': ['This field is required.'],
#  'price': ['Price must be greater than zero!'],
#  ...}

# Shortcut: raise_exception=True
# Instead of checking is_valid(), you can do:
serializer = BookSerializer(data=bad_data)
serializer.is_valid(raise_exception=True)
# This automatically returns a 400 response with error details
```

Common Mistake: Forgetting many=True when serializing a QuerySet.

```python

books = Book.objects.all()  # This is a QuerySet (multiple objects)
serializer = BookSerializer(books)        # WRONG! Will crash
serializer = BookSerializer(books, many=True)  # CORRECT!
```

Common Mistake: Forgetting to pass data= keyword.

```python

# Serializing (reading):
serializer = BookSerializer(book)          # No 'data=' keyword

# Deserializing (writing):
serializer = BookSerializer(data=input)    # Must use 'data=' keyword!
```

## Practice Exercise — Chapter 3

```text

Exercise 3.1:
  Create a MovieSerializer for a Movie model with:
    - title (CharField, max 200, required, min 2 chars)
    - director (CharField, max 100, required, only letters allowed)
    - release_year (IntegerField, must be between 1888 and current year)
    - genre (CharField, max 50)
    - rating (DecimalField, 0.0 to 10.0)
    - duration_minutes (PositiveIntegerField)
    - is_released (BooleanField, default True)
    
  Add these computed fields:
    - duration_hours (convert minutes to hours like "2h 30m")
    - is_classic (True if released before 2000)
    
  Add these validations:
    - Title cannot contain numbers
    - If is_released is True, release_year must be <= current year
    - Rating cannot be 0 for released movies
    
Exercise 3.2:
  Test your serializer in Django shell:
    a) Create 3 movies using the serializer
    b) Serialize all movies (use many=True)
    c) Try creating a movie with invalid data and print errors
    d) Update only the rating of a movie (partial update)
```
