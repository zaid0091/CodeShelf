---
title: Introduction — Understanding APIs
description: APIs, REST principles, JSON, HTTP methods, status codes, and DRF architecture overview.
order: 1
tags: [drf, apis, rest, http, json]
---

# Chapter 1: Introduction — Understanding APIs

> **Welcome!** This chapter explains what APIs are, how REST works, and where Django REST Framework fits. No DRF code is required yet — you only need basic Django awareness.

---

## Table of Contents

1. [What is an API?](#what-is-an-api)
2. [REST Principles](#rest-principles)
3. [JSON Basics](#json-basics)
4. [HTTP Methods](#http-methods)
5. [HTTP Status Codes](#http-status-codes)
6. [Request-Response Cycle](#request-response-cycle)
7. [What is Django REST Framework?](#what-is-django-rest-framework)
8. [DRF Architecture Overview](#drf-architecture-overview)
9. [Tools: curl and HTTPie](#tools-curl-and-httpie)
10. [Common Mistakes](#common-mistakes)
11. [Interview Points](#interview-points)
12. [Exercises](#exercises)
13. [Chapter Summary](#chapter-summary)

---

## What is an API?

> **Definition:** **API (Application Programming Interface)** — a contract that lets one program request data or actions from another using agreed URLs, methods, and formats.



Imagine a restaurant: you (the client) do not enter the kitchen (database). You tell the waiter (API) your order; the waiter brings food (JSON response).

```text
CLIENT (React/mobile)  →  API (DRF views)  →  SERVER/DATABASE
         ←  JSON response  ←
```

```python
# Plain Django returns HTML; APIs return JSON for machines.
# DRF specializes in that JSON contract.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def health(request):
    return Response({'status': 'ok'})
```
---

## REST Principles

REST (REpresentational State Transfer) organizes APIs around **resources** (nouns) and **HTTP verbs** (actions).

| Constraint | Meaning for beginners |
| --- | --- |
| Client-Server | Frontend and API are separate apps |
| Stateless | Each request carries all context (e.g. token); server stores no session memory in REST purists' view |
| Uniform Interface | Use standard verbs on resource URLs |
| Cacheable | GET responses can be cached |
| Layered | Load balancers/CDNs can sit in front |



---

### REST and HTTP — Mental Model

When learning **REST and HTTP**, think about the **mental model**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for REST and HTTP
curl -X GET http://127.0.0.1:8000/api/example-1/ \
  -H "Content-Type: application/json"
```

### REST and HTTP — Step By Step Flow

When learning **REST and HTTP**, think about the **step-by-step flow**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for REST and HTTP
curl -X GET http://127.0.0.1:8000/api/example-2/ \
  -H "Content-Type: application/json"
```

### REST and HTTP — Comparison Table

When learning **REST and HTTP**, think about the **comparison table**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for REST and HTTP
curl -X GET http://127.0.0.1:8000/api/example-3/ \
  -H "Content-Type: application/json"
```

### REST and HTTP — Real World Analogy

When learning **REST and HTTP**, think about the **real-world analogy**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for REST and HTTP
curl -X GET http://127.0.0.1:8000/api/example-4/ \
  -H "Content-Type: application/json"
```

### REST and HTTP — Security Angle

When learning **REST and HTTP**, think about the **security angle**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for REST and HTTP
curl -X GET http://127.0.0.1:8000/api/example-5/ \
  -H "Content-Type: application/json"
```

### REST and HTTP — Testing Angle

When learning **REST and HTTP**, think about the **testing angle**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for REST and HTTP
curl -X GET http://127.0.0.1:8000/api/example-6/ \
  -H "Content-Type: application/json"
```

### REST and HTTP — Production Tip

When learning **REST and HTTP**, think about the **production tip**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for REST and HTTP
curl -X GET http://127.0.0.1:8000/api/example-7/ \
  -H "Content-Type: application/json"
```

### REST and HTTP — Debugging Checklist

When learning **REST and HTTP**, think about the **debugging checklist**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for REST and HTTP
curl -X GET http://127.0.0.1:8000/api/example-8/ \
  -H "Content-Type: application/json"
```

## JSON Basics

JSON is the default wire format for DRF. Keys use double quotes; booleans are lowercase `true`/`false`.

```json
{"title": "DRF Book", "price": 29.99, "in_stock": true, "tags": ["api", "django"]}
```

---

## HTTP Methods

| Method | Purpose | Safe? | Idempotent? |
| --- | --- | --- | --- |
| GET | Read | Yes | Yes |
| POST | Create | No | No |
| PUT | Replace entire resource | No | Yes |
| PATCH | Partial update | No | Usually |
| DELETE | Remove | No | Yes |



```bash
# List books
curl -X GET http://127.0.0.1:8000/api/books/ \
  -H "Content-Type: application/json"
```



```bash
# Create book
curl -X POST http://127.0.0.1:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{"title":"New Book","price":10}'
```



```bash
# Update price only
curl -X PATCH http://127.0.0.1:8000/api/books/1/ \
  -H "Content-Type: application/json" \
  -d '{"price":15}'
```



---

## HTTP Status Codes

Status codes tell the client what happened without parsing the body.

| Code | When |
| --- | --- |
| 200 | OK — success |
| 201 | Created — after POST |
| 204 | No Content — often DELETE |
| 400 | Bad request — invalid JSON or validation |
| 401 | Not authenticated |
| 403 | Authenticated but forbidden |
| 404 | Resource not found |
| 500 | Server error |



---

## Request-Response Cycle

```text
Client → URL Router → Auth → Permissions → Throttle → Parser → View → Serializer → Renderer → Client
```

---

## What is Django REST Framework?

> **Definition:** **Django REST Framework (DRF)** — a toolkit on top of Django for building Web APIs with serializers, browsable API, auth, pagination, and more.



```python
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

---

## DRF Architecture Overview

See lifecycle diagram in section above; each layer is configurable in `settings.py`.

---

## Tools: curl and HTTPie

```bash
# curl
curl -X GET http://127.0.0.1:8000/api/books/ \
  -H "Content-Type: application/json"
```



```bash
# HTTPie (prettier)
http GET http://127.0.0.1:8000/api/books/
```

---

## Common Mistakes

### ❌ Using verbs in URLs

Prefer `DELETE /api/users/5/` not `POST /api/deleteUser/5/`.

### ❌ Ignoring status codes

Return 201 on create, 404 when missing, 400 on validation errors.

### ❌ Confusing 401 and 403

401 = not logged in; 403 = logged in but not allowed.

### ❌ Sending Python dicts as JSON

Use `true`/`false`/`null`, not `True`/`False`/`None`.

### ❌ PUT for tiny changes

Use PATCH for partial updates.

## Interview Points

### Q: What is REST?

An architectural style using resources, HTTP methods, and stateless messages, usually JSON.

### Q: PUT vs PATCH?

PUT replaces the whole resource; PATCH updates only sent fields.

### Q: What is idempotent?

Repeating the request does not change the outcome beyond the first success (GET, PUT, DELETE).

### Q: Why JSON for APIs?

Lightweight, language-neutral, easy for browsers and mobile apps to parse.

### Q: What does DRF add to Django?

Serializers, API views, auth classes, browsable API, pagination, testing helpers.

### Q: What is REST?

An architectural style using resources, HTTP methods, and stateless messages, usually JSON.

### Q: PUT vs PATCH?

PUT replaces the whole resource; PATCH updates only sent fields.

### Q: What is idempotent?

Repeating the request does not change the outcome beyond the first success (GET, PUT, DELETE).

### Q: Why JSON for APIs?

Lightweight, language-neutral, easy for browsers and mobile apps to parse.

### Q: What does DRF add to Django?

Serializers, API views, auth classes, browsable API, pagination, testing helpers.

## Exercises

### Exercise 1

Design REST URLs for a `Product` resource (list, create, detail, update, delete).

### Exercise 2

Convert `{'name': 'Ada', 'active': True}` to valid JSON.

### Exercise 3

Which method updates only `email`? Which status code after successful POST?

### Exercise 4

Explain the request lifecycle in your own words with a diagram.

### Exercise 5

Use curl to call a public API (e.g. jsonplaceholder) and document status + body.

<details>
<summary>Sample answers (check after you try)</summary>

Answers vary by design; focus on RESTful URLs, correct HTTP verbs, and DRF patterns from this chapter.

</details>

## Chapter Summary

- APIs let clients talk to servers through a defined contract
- REST uses resources + HTTP verbs + JSON
- Status codes communicate success and failure types
- DRF layers auth, permissions, serializers, and views on Django

### Key rules

```text
✅ APIs let clients talk to servers through a defined contract
✅ REST uses resources + HTTP verbs + JSON
✅ Status codes communicate success and failure types
✅ DRF layers auth, permissions, serializers, and views on Django
```

**➡️ [Next →](./ch02-setup-configuration.md)**

---

*Last updated: 2025 | Django REST Framework Course*
