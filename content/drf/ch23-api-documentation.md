---
title: API Documentation (Swagger)
description: OpenAPI docs and Swagger UI with drf-spectacular
order: 23
tags: [drf, swagger, openapi, drf-spectacular]
---

# Chapter 23: API Documentation (Swagger)

> **Welcome!** This chapter covers **OpenAPI documentation** in Django REST Framework with beginner-friendly explanations.

---

## Table of Contents

1. [Introduction to OpenAPI documentation](#intro-openapi-documentation)
2. [Core concepts](#core-openapi-documentation)
3. [Step-by-step example](#example-openapi-documentation)
4. [HTTP and curl examples](#curl-openapi-documentation)
5. [Configuration in settings.py](#settings-openapi-documentation)
6. [Advanced patterns](#advanced-openapi-documentation)
7. [Testing this feature](#testing-openapi-documentation)
8. [Common Mistakes](#common-mistakes)
9. [Interview Points](#interview-points)
10. [Exercises](#exercises)
11. [Chapter Summary](#chapter-summary)

---

## Introduction to OpenAPI documentation

> **Definition:** **OpenAPI documentation** — a key part of building production-ready APIs with Django REST Framework.



You should already know Django models, views, and URLs. Here we apply those ideas to **OpenAPI documentation**.

```python
# models.py — example domain for this chapter
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```
---

### OpenAPI documentation — Mental Model

When learning **OpenAPI documentation**, think about the **mental model**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for OpenAPI documentation
curl -X GET http://127.0.0.1:8000/api/example-1/ \
  -H "Content-Type: application/json"
```

### OpenAPI documentation — Step By Step Flow

When learning **OpenAPI documentation**, think about the **step-by-step flow**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for OpenAPI documentation
curl -X GET http://127.0.0.1:8000/api/example-2/ \
  -H "Content-Type: application/json"
```

### OpenAPI documentation — Comparison Table

When learning **OpenAPI documentation**, think about the **comparison table**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for OpenAPI documentation
curl -X GET http://127.0.0.1:8000/api/example-3/ \
  -H "Content-Type: application/json"
```

### OpenAPI documentation — Real World Analogy

When learning **OpenAPI documentation**, think about the **real-world analogy**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for OpenAPI documentation
curl -X GET http://127.0.0.1:8000/api/example-4/ \
  -H "Content-Type: application/json"
```

### OpenAPI documentation — Security Angle

When learning **OpenAPI documentation**, think about the **security angle**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for OpenAPI documentation
curl -X GET http://127.0.0.1:8000/api/example-5/ \
  -H "Content-Type: application/json"
```

### OpenAPI documentation — Testing Angle

When learning **OpenAPI documentation**, think about the **testing angle**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for OpenAPI documentation
curl -X GET http://127.0.0.1:8000/api/example-6/ \
  -H "Content-Type: application/json"
```

### OpenAPI documentation — Production Tip

When learning **OpenAPI documentation**, think about the **production tip**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for OpenAPI documentation
curl -X GET http://127.0.0.1:8000/api/example-7/ \
  -H "Content-Type: application/json"
```

### OpenAPI documentation — Debugging Checklist

When learning **OpenAPI documentation**, think about the **debugging checklist**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for OpenAPI documentation
curl -X GET http://127.0.0.1:8000/api/example-8/ \
  -H "Content-Type: application/json"
```

## Step-by-step example

We build a minimal end-to-end flow: model → serializer → view → URL → test with curl.

```python
# serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```
---

## HTTP and curl examples

Test every endpoint from the terminal before wiring the frontend.

```bash
# 
curl -X GET http://127.0.0.1:8000/api/openapi-documentation/ \
  -H "Content-Type: application/json"
```



```bash
# 
curl -X POST http://127.0.0.1:8000/api/openapi-documentation/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Example"}'
```



```bash
# 
curl -X GET http://127.0.0.1:8000/api/openapi-documentation/1/ \
  -H "Content-Type: application/json"
```



```bash
# 
curl -X PATCH http://127.0.0.1:8000/api/openapi-documentation/1/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Updated"}'
```



```bash
# 
curl -X DELETE http://127.0.0.1:8000/api/openapi-documentation/1/ \
  -H "Content-Type: application/json"
```



---

## Configuration in settings.py

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}
```

Tune defaults for **OpenAPI documentation** in `REST_FRAMEWORK` so you do not repeat settings on every view.

---

## Advanced patterns

Combine **OpenAPI documentation** with permissions, filtering, and pagination from other chapters.

Override hooks like `get_queryset()`, `perform_create()`, or serializer `validate()` for business rules.

---

## Testing this feature

```python
from rest_framework.test import APITestCase

class BookTests(APITestCase):
    def test_list(self):
        response = self.client.get('/api/openapi-documentation/')
        self.assertEqual(response.status_code, 200)
```

---

## Deep dive 1: OpenAPI documentation in practice

Scenario 1: A mobile app consumes your **OpenAPI documentation** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 1
curl -X GET http://127.0.0.1:8000/api/openapi-documentation/?page=1 \
  -H "Content-Type: application/json"
```


---

## Deep dive 2: OpenAPI documentation in practice

Scenario 2: A mobile app consumes your **OpenAPI documentation** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 2
curl -X GET http://127.0.0.1:8000/api/openapi-documentation/?page=2 \
  -H "Content-Type: application/json"
```


---

## Deep dive 3: OpenAPI documentation in practice

Scenario 3: A mobile app consumes your **OpenAPI documentation** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 3
curl -X GET http://127.0.0.1:8000/api/openapi-documentation/?page=3 \
  -H "Content-Type: application/json"
```


---

## Deep dive 4: OpenAPI documentation in practice

Scenario 4: A mobile app consumes your **OpenAPI documentation** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 4
curl -X GET http://127.0.0.1:8000/api/openapi-documentation/?page=4 \
  -H "Content-Type: application/json"
```


---

## Deep dive 5: OpenAPI documentation in practice

Scenario 5: A mobile app consumes your **OpenAPI documentation** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 5
curl -X GET http://127.0.0.1:8000/api/openapi-documentation/?page=5 \
  -H "Content-Type: application/json"
```


---

## Deep dive 6: OpenAPI documentation in practice

Scenario 6: A mobile app consumes your **OpenAPI documentation** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 6
curl -X GET http://127.0.0.1:8000/api/openapi-documentation/?page=6 \
  -H "Content-Type: application/json"
```


---

## Deep dive 7: OpenAPI documentation in practice

Scenario 7: A mobile app consumes your **OpenAPI documentation** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 7
curl -X GET http://127.0.0.1:8000/api/openapi-documentation/?page=7 \
  -H "Content-Type: application/json"
```


---

## Deep dive 8: OpenAPI documentation in practice

Scenario 8: A mobile app consumes your **OpenAPI documentation** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 8
curl -X GET http://127.0.0.1:8000/api/openapi-documentation/?page=8 \
  -H "Content-Type: application/json"
```


---

## Common Mistakes

### ❌ Skipping OpenAPI documentation docs

Document behavior in OpenAPI (Chapter 23).

### ❌ Fat views

Keep views thin; put validation in serializers.

### ❌ Wrong HTTP method

Match REST verbs to actions.

### ❌ No authentication on write endpoints

Use `IsAuthenticated` for creates/updates.

### ❌ Returning 200 for everything

Use precise status codes.

## Interview Points

### Q: What is OpenAPI documentation in DRF?

It is part of the request/response pipeline for OpenAPI documentation.

### Q: How does it interact with serializers?

Serializers validate and shape data; views orchestrate.

### Q: How do you debug failures?

Check status code, `response.data`, Django logs, and query count.

### Q: What is OpenAPI documentation in DRF?

It is part of the request/response pipeline for OpenAPI documentation.

### Q: How does it interact with serializers?

Serializers validate and shape data; views orchestrate.

### Q: How do you debug failures?

Check status code, `response.data`, Django logs, and query count.

### Q: What is OpenAPI documentation in DRF?

It is part of the request/response pipeline for OpenAPI documentation.

### Q: How does it interact with serializers?

Serializers validate and shape data; views orchestrate.

### Q: How do you debug failures?

Check status code, `response.data`, Django logs, and query count.

### Q: What is OpenAPI documentation in DRF?

It is part of the request/response pipeline for OpenAPI documentation.

### Q: How does it interact with serializers?

Serializers validate and shape data; views orchestrate.

### Q: How do you debug failures?

Check status code, `response.data`, Django logs, and query count.

## Exercises

### Exercise 1

Implement a minimal `Book` API using OpenAPI documentation.

### Exercise 2

Write curl commands for list, create, update, delete.

### Exercise 3

Add a test with `APITestCase`.

### Exercise 4

List three ways this chapter's topic improves security or UX.

### Exercise 5

Break one rule on purpose and document the error response.

<details>
<summary>Sample answers (check after you try)</summary>

Answers vary by design; focus on RESTful URLs, correct HTTP verbs, and DRF patterns from this chapter.

</details>

## Chapter Summary

- Understood the role of OpenAPI documentation in DRF
- Built model → serializer → view flow
- Practiced curl and status codes
- Avoided common beginner mistakes

### Key rules

```text
✅ Understood the role of OpenAPI documentation in DRF
✅ Built model → serializer → view flow
✅ Practiced curl and status codes
✅ Avoided common beginner mistakes
```

**➡️ [Next →](./ch24-deployment.md)**

---

*Last updated: 2025 | Django REST Framework Course*
