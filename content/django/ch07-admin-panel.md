---
title: Admin Panel
description: ModelAdmin customization, list display, filters, search, inlines, and actions
order: 7
tags: [django, admin]
---

# Chapter 7: Admin Panel

## 7.1 Django admin overview

> **Definition:** The **Django admin** is an automatic CRUD interface for registered models — ideal for staff users and internal tools.

Enable by adding `django.contrib.admin` to `INSTALLED_APPS` and visiting `/admin/` after [creating a superuser](./ch02-setup-project-structure.md).

## 7.2 Registering models

```python
# blog/admin.py
from django.contrib import admin
from .models import Post, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published", "created_at"]
    list_filter = ["published", "created_at"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "created_at"
    ordering = ["-created_at"]

admin.site.register(Tag)
```

| Option | Purpose |
|--------|---------|
| `list_display` | Columns on list page |
| `list_filter` | Sidebar filters |
| `search_fields` | Search box (icontains) |
| `prepopulated_fields` | Auto slug from title |
| `date_hierarchy` | Date drill-down |

## 7.3 Editing fields layout

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title", "slug", "author"]}),
        ("Content", {"fields": ["body", "published"]}),
        ("Metadata", {"fields": ["created_at"], "classes": ["collapse"]}),
    ]
    readonly_fields = ["created_at"]
```

## 7.4 Inlines

Edit related objects on the same page:

```python
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
```

| Inline class | Layout |
|--------------|--------|
| `TabularInline` | Table rows |
| `StackedInline` | Stacked fields |

## 7.5 Custom admin actions

```python
@admin.action(description="Mark selected posts as published")
def make_published(modeladmin, request, queryset):
    queryset.update(published=True)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = [make_published]
```

## 7.6 Permissions

Admin respects model-level permissions:

| Permission | Capability |
|------------|------------|
| `add` | Create objects |
| `change` | Edit objects |
| `delete` | Delete objects |
| `view` | View-only (Django 2.1+) |

```python
def has_delete_permission(self, request, obj=None):
    return request.user.is_superuser
```

## 7.7 Customizing list display

```python
@admin.display(description="Word count")
def word_count(self, obj):
    return len(obj.body.split())

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "word_count", "published"]
```

## 7.8 Admin site branding

```python
# mysite/urls.py or admin config
from django.contrib import admin

admin.site.site_header = "My Blog Admin"
admin.site.site_title = "Blog"
admin.site.index_title = "Dashboard"
```

## 7.9 Filtering QuerySets in admin

```python
class PostAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
```

## 7.10 Admin vs custom views

| Use admin when | Build custom UI when |
|----------------|----------------------|
| Internal staff tools | Public-facing UX |
| Rapid CRUD needed | Complex workflows |
| Low customization | Brand-specific design |

Public users interact via [views](./ch04-views-urls.md) and [forms](./ch06-forms.md).

## Exercises

1. Register `Post` with `list_display`, `list_filter`, and `search_fields`.
2. Add a `make_published` admin action.
3. Use `prepopulated_fields` for slug from title.
4. Create a `TabularInline` for comments on the Post admin page.

## Summary

The admin provides instant management UI for [models](./ch03-models-orm.md). Customize with `ModelAdmin`, inlines, and actions for productive internal tools.

## Next chapter

Continue to [Authentication](./ch08-authentication.md).
