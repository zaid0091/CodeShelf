---
title: Project 1 — Todo API
description: Full DRF Todo API with filtering, search, and custom actions
order: 26
tags: [drf, project, todo, viewset]
---

# Project 1 — Todo API

> **Welcome!** Hands-on project: **Project 1 — Todo API**. Build it step by step after Chapters 1–20.

---

## Table of Contents

1. [Project overview](#project-overview)
2. [Requirements](#requirements)
3. [Project setup](#project-setup)
4. [Models](#models)
5. [Serializers](#serializers)
6. [Views and URLs](#views-and-urls)
7. [Authentication](#authentication)
8. [Testing with curl](#testing-with-curl)
9. [Common Mistakes](#common-mistakes)
10. [Interview Points](#interview-points)
11. [Exercises](#exercises)
12. [Summary](#summary)

---

## Project overview

Build a complete **Project 1 — Todo API** using DRF best practices.

Features:
- CRUD todos
- Owner scoping
- Filters and search
- Custom actions

---

### Project 1 — Todo API — Mental Model

When learning **Project 1 — Todo API**, think about the **mental model**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Project 1 — Todo API
curl -X GET http://127.0.0.1:8000/api/example-1/ \
  -H "Content-Type: application/json"
```

### Project 1 — Todo API — Step By Step Flow

When learning **Project 1 — Todo API**, think about the **step-by-step flow**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Project 1 — Todo API
curl -X GET http://127.0.0.1:8000/api/example-2/ \
  -H "Content-Type: application/json"
```

### Project 1 — Todo API — Comparison Table

When learning **Project 1 — Todo API**, think about the **comparison table**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Project 1 — Todo API
curl -X GET http://127.0.0.1:8000/api/example-3/ \
  -H "Content-Type: application/json"
```

### Project 1 — Todo API — Real World Analogy

When learning **Project 1 — Todo API**, think about the **real-world analogy**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Project 1 — Todo API
curl -X GET http://127.0.0.1:8000/api/example-4/ \
  -H "Content-Type: application/json"
```

### Project 1 — Todo API — Security Angle

When learning **Project 1 — Todo API**, think about the **security angle**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Project 1 — Todo API
curl -X GET http://127.0.0.1:8000/api/example-5/ \
  -H "Content-Type: application/json"
```

### Project 1 — Todo API — Testing Angle

When learning **Project 1 — Todo API**, think about the **testing angle**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Project 1 — Todo API
curl -X GET http://127.0.0.1:8000/api/example-6/ \
  -H "Content-Type: application/json"
```

### Project 1 — Todo API — Production Tip

When learning **Project 1 — Todo API**, think about the **production tip**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Project 1 — Todo API
curl -X GET http://127.0.0.1:8000/api/example-7/ \
  -H "Content-Type: application/json"
```

### Project 1 — Todo API — Debugging Checklist

When learning **Project 1 — Todo API**, think about the **debugging checklist**. In DRF, every request passes through URL routing, authentication, permissions, throttling, parsers, the view, serializers, renderers, and finally the HTTP response. Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.

| Check | Question to ask |
| --- | --- |
| Request | What HTTP method and URL am I using? |
| Auth | Is the user identified (`request.user`)? |
| Permissions | Does this user have rights for this action? |
| Data | Is the JSON body valid for the serializer? |
| Response | Is the status code correct (201 for create, 204 for delete)? |

```bash
# Example read for Project 1 — Todo API
curl -X GET http://127.0.0.1:8000/api/example-8/ \
  -H "Content-Type: application/json"
```

## Models

```python
from django.db import models
from django.conf import settings

class ProjectModel(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='%(class)s_items',
    )
    created_at = models.DateTimeField(auto_now_add=True)
```
---

## Milestone 1

Implement feature slice 1 for Project 1 — Todo API. Run migrations and test with curl.

```bash
# 
curl -X GET http://127.0.0.1:8000/api/project-todo-api/ \
  -H "Content-Type: application/json"
```


---

## Milestone 2

Implement feature slice 2 for Project 1 — Todo API. Run migrations and test with curl.

```bash
# 
curl -X GET http://127.0.0.1:8000/api/project-todo-api/ \
  -H "Content-Type: application/json"
```


---

## Milestone 3

Implement feature slice 3 for Project 1 — Todo API. Run migrations and test with curl.

```bash
# 
curl -X GET http://127.0.0.1:8000/api/project-todo-api/ \
  -H "Content-Type: application/json"
```


---

## Milestone 4

Implement feature slice 4 for Project 1 — Todo API. Run migrations and test with curl.

```bash
# 
curl -X GET http://127.0.0.1:8000/api/project-todo-api/ \
  -H "Content-Type: application/json"
```


---

## Milestone 5

Implement feature slice 5 for Project 1 — Todo API. Run migrations and test with curl.

```bash
# 
curl -X GET http://127.0.0.1:8000/api/project-todo-api/ \
  -H "Content-Type: application/json"
```


---

## Milestone 6

Implement feature slice 6 for Project 1 — Todo API. Run migrations and test with curl.

```bash
# 
curl -X GET http://127.0.0.1:8000/api/project-todo-api/ \
  -H "Content-Type: application/json"
```


---

## Milestone 7

Implement feature slice 7 for Project 1 — Todo API. Run migrations and test with curl.

```bash
# 
curl -X GET http://127.0.0.1:8000/api/project-todo-api/ \
  -H "Content-Type: application/json"
```


---

## Milestone 8

Implement feature slice 8 for Project 1 — Todo API. Run migrations and test with curl.

```bash
# 
curl -X GET http://127.0.0.1:8000/api/project-todo-api/ \
  -H "Content-Type: application/json"
```


---

## Common Mistakes

### ❌ No owner scoping

Filter querysets by `request.user`.

## Interview Points

### Q: How would you deploy this?

Gunicorn + Postgres + Redis cache (Chapter 24).

## Exercises

### Exercise 1

Add filtering to Project 1 — Todo API.

### Exercise 2

Write 5 APITestCase tests.

### Exercise 3

Add JWT auth.

<details>
<summary>Sample answers (check after you try)</summary>

Answers vary by design; focus on RESTful URLs, correct HTTP verbs, and DRF patterns from this chapter.

</details>

## Chapter Summary

- Completed Project 1 — Todo API architecture

### Key rules

```text
✅ Completed Project 1 — Todo API architecture
```

---

*Last updated: 2025 | Django REST Framework Course*
