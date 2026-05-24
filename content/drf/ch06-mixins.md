---
title: Mixins
description: ListModelMixin, CreateModelMixin, Retrieve/Update/Destroy mixins, and combining mixins with APIView.
order: 6
tags: [drf, mixins, views]
---

# Chapter 6: Mixins

## 6.1 What are Mixins?

Imagine you are building with LEGO blocks:

```text

You want: A car with wings that can go underwater

Instead of building EVERYTHING from scratch:
  - CarBlock      (has wheels, engine)
  - WingBlock     (has wings)
  - SubmarineBlock (has propeller, waterproofing)

You COMBINE these blocks = Flying Submarine Car!

Similarly in DRF:
  - ListModelMixin    (ability to LIST objects)
  - CreateModelMixin  (ability to CREATE objects)
  - RetrieveModelMixin (ability to GET one object)
  - UpdateModelMixin  (ability to UPDATE objects)
  - DestroyModelMixin (ability to DELETE objects)

You COMBINE the ones you need!
```

> **Definition:** Mixins are small classes that provide a single piece of reusable behavior. They are not meant to be used alone — you combine multiple mixins with a base class (GenericAPIView) to create the exact functionality you need.

## 6.2 GenericAPIView

Before using mixins, you need to understand GenericAPIView. It is an enhanced APIView that adds:

```python

# GenericAPIView provides:
queryset = ...          # Which objects to work with
serializer_class = ...  # Which serializer to use
lookup_field = 'pk'     # Which field to use for single object lookup

# And these helper methods:
self.get_queryset()     # Returns the queryset
self.get_serializer()   # Returns the serializer
self.get_object()       # Returns a single object (uses lookup_field)
```

## 6.3 Available Mixins

```python

from rest_framework import mixins, generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(
    mixins.ListModelMixin,       # Adds .list() method
    mixins.CreateModelMixin,     # Adds .create() method
    generics.GenericAPIView      # The base class (always last!)
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request, *args, **kwargs):
        """
        When GET request comes, call the list() method
        provided by ListModelMixin.
        """
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        """
        When POST request comes, call the create() method
        provided by CreateModelMixin.
        """
        return self.create(request, *args, **kwargs)

class BookDetailView(
    mixins.RetrieveModelMixin,   # Adds .retrieve() method
    mixins.UpdateModelMixin,     # Adds .update() and .partial_update() methods
    mixins.DestroyModelMixin,    # Adds .destroy() method
    generics.GenericAPIView
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
What each mixin does internally:

# ListModelMixin.list()
def list(self, request, *args, **kwargs):
    queryset = self.get_queryset()           # Get all objects
    queryset = self.filter_queryset(queryset) # Apply filters
    page = self.paginate_queryset(queryset)   # Apply pagination
    if page is not None:
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)

# CreateModelMixin.create()
def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)          # ← Hook point!
    return Response(serializer.data, status=status.HTTP_201_CREATED)

def perform_create(self, serializer):
    serializer.save()                        # You can override this!

# RetrieveModelMixin.retrieve()
def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()             # Get single object by pk
    serializer = self.get_serializer(instance)
    return Response(serializer.data)

# UpdateModelMixin.update()
def update(self, request, *args, **kwargs):
    instance = self.get_object()
    partial = kwargs.pop('partial', False)
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)          # ← Hook point!
    return Response(serializer.data)

def perform_update(self, serializer):
    serializer.save()                        # You can override this!

# DestroyModelMixin.destroy()
def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    self.perform_destroy(instance)           # ← Hook point!
    return Response(status=status.HTTP_204_NO_CONTENT)

def perform_destroy(self, instance):
    instance.delete()                        # You can override this!
Important: perform_create, perform_update, perform_destroy

These are hook methods — places where you can add custom logic:

class BookListCreateView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        """
        Override this to add custom logic before saving.
        Example: automatically set the owner to the current user.
        """
        serializer.save(owner=self.request.user)
        # You could also:
        # - Send an email notification
        # - Log the creation
        # - Update a counter
```

### 🎯 Interview Point

**Why use mixins instead of writing the logic directly in APIView?**

DRY Principle — The list/create/retrieve/update/delete logic is the same for almost every model. Mixins avoid writing this same code repeatedly.
Consistency — All your views behave the same way (same pagination, same error handling).
Hook Methods — perform_create, perform_update, perform_destroy let you customize without rewriting everything.
Composability — Pick exactly which actions you need. Want only list + create? Use only those two mixins.
