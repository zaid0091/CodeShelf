---
title: DRF Course Overview
description: Complete Django REST Framework course — from APIs to production projects
order: 0
tags: [drf, overview]
---

# The Complete Django REST Framework Course

From absolute beginner to professional — every concept explained.

## Course structure

### Part 1: Foundations

| Chapter | Topic |
|---------|--------|
| [Introduction — APIs](./ch01-introduction-apis.md) | APIs, REST, JSON, HTTP, status codes, DRF overview |
| [Setup & Configuration](./ch02-setup-configuration.md) | Install Django/DRF, models, admin, testing tools |

### Part 2: Serializers — The Heart of DRF

| Chapter | Topic |
|---------|--------|
| [Serializers](./ch03-serializers.md) | Serializer vs ModelSerializer, validation, SerializerMethodField |

### Part 3: Views — Handling Requests

| Chapter | Topic |
|---------|--------|
| [Function-Based Views](./ch04-function-based-views.md) | `@api_view`, request/response cycle |
| [Class-Based Views](./ch05-class-based-views.md) | `APIView`, dispatch |
| [Mixins](./ch06-mixins.md) | Reusable CRUD behavior |
| [Generic Views](./ch07-generic-views.md) | `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView` |
| [ViewSets & Routers](./ch08-viewsets-routers.md) | `ModelViewSet`, custom `@action`, routers |

### Part 4: Security

| Chapter | Topic |
|---------|--------|
| [Authentication](./ch09-authentication.md) | Session, Basic, Token auth |
| [Permissions](./ch10-permissions.md) | Built-in and custom permissions |

### Part 5: API Features

| Chapter | Topic |
|---------|--------|
| [Pagination](./ch11-pagination.md) | Page, limit-offset, cursor |
| [Filtering, Search & Ordering](./ch12-filtering-search-ordering.md) | `django-filter`, search, sort |
| [Throttling](./ch13-throttling.md) | Rate limiting |
| [Serializer Relations](./ch14-serializer-relations.md) | FK/M2M representation |
| [Nested Serializers](./ch15-nested-serializers.md) | Deep reads and writes |
| [File Uploads](./ch16-file-uploads.md) | Images, PDFs, parsers |
| [Signals](./ch17-signals.md) | Auto-actions on save/delete |
| [Testing](./ch18-testing.md) | `APITestCase` |
| [JWT Authentication](./ch19-jwt-authentication.md) | SimpleJWT |
| [Custom User & Registration](./ch20-custom-user-registration.md) | `AbstractUser`, register API |
| [Performance](./ch21-performance-optimization.md) | `select_related`, caching |
| [Error Handling](./ch22-error-handling.md) | Custom exception handler |
| [API Documentation](./ch23-api-documentation.md) | drf-spectacular / Swagger |
| [Deployment](./ch24-deployment.md) | Production settings, Docker |
| [Best Practices](./ch25-best-practices.md) | Structure, security |

### Part 6: Real Projects

| Chapter | Topic |
|---------|--------|
| [Project: Todo API](./project-todo-api.md) | Full CRUD + custom actions |
| [Project: Blog API](./project-blog-api.md) | Posts, comments, nested routes |
| [Project: E-Commerce API](./project-ecommerce-api.md) | Cart, checkout, orders |
| [Interview Preparation](./ch26-interview-preparation.md) | Common DRF interview Q&A |

## How to use these notes

1. Read **Part 1** first if you are new to APIs.
2. Work through **Part 2–3** hands-on in a `bookstore_api` project.
3. Add **security** and **features** as your API grows.
4. Build the **three projects** in Part 6 to consolidate everything.

> **Tip:** Use the sidebar search (`Ctrl+K`) to jump to topics like "JWT", "pagination", or "ViewSet".
