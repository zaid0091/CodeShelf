---
title: Signals with DRF
description: Using Django signals alongside Django REST Framework for side effects and decoupling
order: 17
tags: [drf, signals, django]
---

# Chapter 17: Signals with DRF

> **Welcome!** This chapter covers **Django signals with DRF** in Django REST Framework with beginner-friendly explanations.

---

## Table of Contents

1. [Introduction to Django signals with DRF](#intro-django-signals-with-drf)
2. [Core concepts](#core-django-signals-with-drf)
3. [Step-by-step example](#example-django-signals-with-drf)
4. [HTTP and curl examples](#curl-django-signals-with-drf)
5. [Configuration in settings.py](#settings-django-signals-with-drf)
6. [Advanced patterns](#advanced-django-signals-with-drf)
7. [Testing this feature](#testing-django-signals-with-drf)
8. [Common Mistakes](#common-mistakes)
9. [Interview Points](#interview-points)
10. [Exercises](#exercises)
11. [Chapter Summary](#chapter-summary)

---

## Introduction to Django signals with DRF

> **Definition:** **Django signals with DRF** — a key part of building production-ready APIs with Django REST Framework.



You should already know Django models, views, and URLs. Here we apply those ideas to **Django signals with DRF**.

```python
# models.py — example domain for this chapter
from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```
---

### Django signals with DRF — Mental Model

When learning **Django signals with DRF**, think about the **mental model**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Django signals with DRF
curl -X GET http://127.0.0.1:8000/api/example-1/ \
  -H "Content-Type: application/json"
```

### Django signals with DRF — Step By Step Flow

When learning **Django signals with DRF**, think about the **step-by-step flow**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Django signals with DRF
curl -X GET http://127.0.0.1:8000/api/example-2/ \
  -H "Content-Type: application/json"
```

### Django signals with DRF — Comparison Table

When learning **Django signals with DRF**, think about the **comparison table**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Django signals with DRF
curl -X GET http://127.0.0.1:8000/api/example-3/ \
  -H "Content-Type: application/json"
```

### Django signals with DRF — Real World Analogy

When learning **Django signals with DRF**, think about the **real-world analogy**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Django signals with DRF
curl -X GET http://127.0.0.1:8000/api/example-4/ \
  -H "Content-Type: application/json"
```

### Django signals with DRF — Security Angle

When learning **Django signals with DRF**, think about the **security angle**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Django signals with DRF
curl -X GET http://127.0.0.1:8000/api/example-5/ \
  -H "Content-Type: application/json"
```

### Django signals with DRF — Testing Angle

When learning **Django signals with DRF**, think about the **testing angle**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Django signals with DRF
curl -X GET http://127.0.0.1:8000/api/example-6/ \
  -H "Content-Type: application/json"
```

### Django signals with DRF — Production Tip

When learning **Django signals with DRF**, think about the **production tip**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Django signals with DRF
curl -X GET http://127.0.0.1:8000/api/example-7/ \
  -H "Content-Type: application/json"
```

### Django signals with DRF — Debugging Checklist

When learning **Django signals with DRF**, think about the **debugging checklist**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Django signals with DRF
curl -X GET http://127.0.0.1:8000/api/example-8/ \
  -H "Content-Type: application/json"
```

## Step-by-step example

We build a minimal end-to-end flow: model → serializer → view → URL → test with curl.

```python
# serializers.py
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

# views.py
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
```
---

## HTTP and curl examples

Test every endpoint from the terminal before wiring the frontend.

```bash
# 
curl -X GET http://127.0.0.1:8000/api/django-signals-with-drf/ \
  -H "Content-Type: application/json"
```



```bash
# 
curl -X POST http://127.0.0.1:8000/api/django-signals-with-drf/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Example"}'
```



```bash
# 
curl -X GET http://127.0.0.1:8000/api/django-signals-with-drf/1/ \
  -H "Content-Type: application/json"
```



```bash
# 
curl -X PATCH http://127.0.0.1:8000/api/django-signals-with-drf/1/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Updated"}'
```



```bash
# 
curl -X DELETE http://127.0.0.1:8000/api/django-signals-with-drf/1/ \
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

Tune defaults for **Django signals with DRF** in `REST_FRAMEWORK` so you do not repeat settings on every view.

---

## Advanced patterns

Combine **Django signals with DRF** with permissions, filtering, and pagination from other chapters.

Override hooks like `get_queryset()`, `perform_create()`, or serializer `validate()` for business rules.

---

## Testing this feature

```python
from rest_framework.test import APITestCase

class OrderTests(APITestCase):
    def test_list(self):
        response = self.client.get('/api/django-signals-with-drf/')
        self.assertEqual(response.status_code, 200)
```

---

## Deep dive 1: Django signals with DRF in practice

Scenario 1: A mobile app consumes your **Django signals with DRF** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 1
curl -X GET http://127.0.0.1:8000/api/django-signals-with-drf/?page=1 \
  -H "Content-Type: application/json"
```


---

## Deep dive 2: Django signals with DRF in practice

Scenario 2: A mobile app consumes your **Django signals with DRF** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 2
curl -X GET http://127.0.0.1:8000/api/django-signals-with-drf/?page=2 \
  -H "Content-Type: application/json"
```


---

## Deep dive 3: Django signals with DRF in practice

Scenario 3: A mobile app consumes your **Django signals with DRF** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 3
curl -X GET http://127.0.0.1:8000/api/django-signals-with-drf/?page=3 \
  -H "Content-Type: application/json"
```


---

## Deep dive 4: Django signals with DRF in practice

Scenario 4: A mobile app consumes your **Django signals with DRF** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 4
curl -X GET http://127.0.0.1:8000/api/django-signals-with-drf/?page=4 \
  -H "Content-Type: application/json"
```


---

## Deep dive 5: Django signals with DRF in practice

Scenario 5: A mobile app consumes your **Django signals with DRF** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 5
curl -X GET http://127.0.0.1:8000/api/django-signals-with-drf/?page=5 \
  -H "Content-Type: application/json"
```


---

## Deep dive 6: Django signals with DRF in practice

Scenario 6: A mobile app consumes your **Django signals with DRF** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 6
curl -X GET http://127.0.0.1:8000/api/django-signals-with-drf/?page=6 \
  -H "Content-Type: application/json"
```


---

## Deep dive 7: Django signals with DRF in practice

Scenario 7: A mobile app consumes your **Django signals with DRF** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 7
curl -X GET http://127.0.0.1:8000/api/django-signals-with-drf/?page=7 \
  -H "Content-Type: application/json"
```


---

## Deep dive 8: Django signals with DRF in practice

Scenario 8: A mobile app consumes your **Django signals with DRF** endpoint. Document expected request headers, pagination query params, and error JSON shape.

| Scenario | Expected status |
| --- | --- |
| Valid create | 201 |
| Missing required field | 400 |
| Not found | 404 |
| Not allowed | 403 |



```bash
# Pagination example 8
curl -X GET http://127.0.0.1:8000/api/django-signals-with-drf/?page=8 \
  -H "Content-Type: application/json"
```


---

## Common Mistakes

### ❌ Skipping Django signals with DRF docs

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

### Q: What is Django signals with DRF in DRF?

It is part of the request/response pipeline for Django signals with DRF.

### Q: How does it interact with serializers?

Serializers validate and shape data; views orchestrate.

### Q: How do you debug failures?

Check status code, `response.data`, Django logs, and query count.

### Q: What is Django signals with DRF in DRF?

It is part of the request/response pipeline for Django signals with DRF.

### Q: How does it interact with serializers?

Serializers validate and shape data; views orchestrate.

### Q: How do you debug failures?

Check status code, `response.data`, Django logs, and query count.

### Q: What is Django signals with DRF in DRF?

It is part of the request/response pipeline for Django signals with DRF.

### Q: How does it interact with serializers?

Serializers validate and shape data; views orchestrate.

### Q: How do you debug failures?

Check status code, `response.data`, Django logs, and query count.

### Q: What is Django signals with DRF in DRF?

It is part of the request/response pipeline for Django signals with DRF.

### Q: How does it interact with serializers?

Serializers validate and shape data; views orchestrate.

### Q: How do you debug failures?

Check status code, `response.data`, Django logs, and query count.

## Exercises

### Exercise 1

Implement a minimal `Order` API using Django signals with DRF.

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

- Understood the role of Django signals with DRF in DRF
- Built model → serializer → view flow
- Practiced curl and status codes
- Avoided common beginner mistakes

### Key rules

```text
✅ Understood the role of Django signals with DRF in DRF
✅ Built model → serializer → view flow
✅ Practiced curl and status codes
✅ Avoided common beginner mistakes
```

**➡️ [Next →](./ch18-testing.md)**

---

*Last updated: 2025 | Django REST Framework Course*
