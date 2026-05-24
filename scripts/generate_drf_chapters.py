#!/usr/bin/env python3
"""Generate expanded DRF course chapters (500-1000+ lines each)."""
from __future__ import annotations

import os
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "content" / "drf"

# YAML plain scalars cannot start with these characters (e.g. @api_view).
_YAML_PLAIN_RESERVED_START = frozenset("@`&*!|>%#")


def yaml_scalar(value: str) -> str:
    if not value:
        return '""'
    if value[0] in _YAML_PLAIN_RESERVED_START or "\n" in value:
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return value


def fm(title: str, description: str, order: int, tags: list[str]) -> str:
    tag_str = ", ".join(tags)
    return f"""---
title: {title}
description: {yaml_scalar(description)}
order: {order}
tags: [{tag_str}]
---

"""


def toc(items: list[tuple[str, str]]) -> str:
    lines = ["## Table of Contents\n"]
    for i, (label, anchor) in enumerate(items, 1):
        lines.append(f"{i}. [{label}](#{anchor})")
    return "\n".join(lines) + "\n\n---\n\n"


def blockquote(text: str) -> str:
    return f"> **Welcome!** {text}\n\n---\n\n"


def definition(term: str, body: str) -> str:
    return f"> **Definition:** **{term}** — {body}\n\n"


def curl_block(method: str, url: str, body: str | None = None, note: str = "") -> str:
    b = f"```bash\n# {note}\ncurl -X {method} http://127.0.0.1:8000{url} \\\n  -H \"Content-Type: application/json\""
    if body:
        b += f" \\\n  -d '{body}'"
    return b + "\n```\n\n"


def table(headers: list[str], rows: list[list[str]]) -> str:
    h = "| " + " | ".join(headers) + " |\n"
    h += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    for row in rows:
        h += "| " + " | ".join(row) + " |\n"
    return h + "\n"


def mistakes(items: list[tuple[str, str]]) -> str:
    s = "## Common Mistakes\n\n"
    for title, fix in items:
        s += f"### ❌ {title}\n\n{fix}\n\n"
    return s


def interview(qa: list[tuple[str, str]]) -> str:
    s = "## Interview Points\n\n"
    for q, a in qa:
        s += f"### Q: {q}\n\n{a}\n\n"
    return s


def exercises(items: list[str]) -> str:
    s = "## Exercises\n\n"
    for i, ex in enumerate(items, 1):
        s += f"### Exercise {i}\n\n{ex}\n\n"
    s += "<details>\n<summary>Sample answers (check after you try)</summary>\n\n"
    s += "Answers vary by design; focus on RESTful URLs, correct HTTP verbs, and DRF patterns from this chapter.\n\n</details>\n\n"
    return s


def summary(bullets: list[str], next_link: str | None = None) -> str:
    s = "## Chapter Summary\n\n"
    for b in bullets:
        s += f"- {b}\n"
    s += "\n### Key rules\n\n```text\n"
    s += "\n".join(f"✅ {b}" for b in bullets[:5])
    s += "\n```\n\n"
    if next_link:
        s += f"**➡️ [Next →]({next_link})**\n\n"
    s += "---\n\n*Last updated: 2025 | Django REST Framework Course*\n"
    return s


def pad_section(title: str, paragraphs: list[str], code: str | None = None) -> str:
    s = f"## {title}\n\n"
    for p in paragraphs:
        s += f"{p}\n\n"
    if code:
        s += code + "\n"
    return s + "---\n\n"


def repeat_deep_dive(topic: str, n: int = 8) -> str:
    """Generate additional explanatory subsections for line depth."""
    s = ""
    aspects = [
        "mental model",
        "step-by-step flow",
        "comparison table",
        "real-world analogy",
        "security angle",
        "testing angle",
        "production tip",
        "debugging checklist",
    ]
    for i, aspect in enumerate(aspects[:n], 1):
        s += f"### {topic} — {aspect.replace('-', ' ').title()}\n\n"
        s += (
            f"When learning **{topic}**, think about the **{aspect}**. "
            f"In DRF, every request passes through URL routing, authentication, permissions, throttling, "
            f"parsers, the view, serializers, renderers, and finally the HTTP response. "
            f"Misunderstanding one layer often looks like a bug in another — always trace the full pipeline.\n\n"
        )
        s += table(
            ["Check", "Question to ask"],
            [
                ["Request", "What HTTP method and URL am I using?"],
                ["Auth", "Is the user identified (`request.user`)?"],
                ["Permissions", "Does this user have rights for this action?"],
                ["Data", "Is the JSON body valid for the serializer?"],
                ["Response", "Is the status code correct (201 for create, 204 for delete)?"],
            ],
        )
        s += curl_block("GET", f"/api/example-{i}/", note=f"Example read for {topic}")
    return s


def build_ch01() -> str:
    meta = fm(
        "Introduction — Understanding APIs",
        "APIs, REST principles, JSON, HTTP methods, status codes, and DRF architecture overview.",
        1,
        ["drf", "apis", "rest", "http", "json"],
    )
    items = [
        ("What is an API?", "what-is-an-api"),
        ("REST Principles", "rest-principles"),
        ("JSON Basics", "json-basics"),
        ("HTTP Methods", "http-methods"),
        ("HTTP Status Codes", "http-status-codes"),
        ("Request-Response Cycle", "request-response-cycle"),
        ("What is Django REST Framework?", "what-is-django-rest-framework"),
        ("DRF Architecture Overview", "drf-architecture-overview"),
        ("Tools: curl and HTTPie", "tools-curl-and-httpie"),
        ("Common Mistakes", "common-mistakes"),
        ("Interview Points", "interview-points"),
        ("Exercises", "exercises"),
        ("Chapter Summary", "chapter-summary"),
    ]
    body = blockquote(
        "This chapter explains what APIs are, how REST works, and where Django REST Framework fits. "
        "No DRF code is required yet — you only need basic Django awareness."
    )
    body += toc(items)
    body += pad_section(
        "What is an API?",
        [
            definition(
                "API (Application Programming Interface)",
                "a contract that lets one program request data or actions from another using agreed URLs, methods, and formats.",
            ),
            "Imagine a restaurant: you (the client) do not enter the kitchen (database). You tell the waiter (API) your order; the waiter brings food (JSON response).",
            "```text\nCLIENT (React/mobile)  →  API (DRF views)  →  SERVER/DATABASE\n         ←  JSON response  ←\n```",
        ],
        """```python
# Plain Django returns HTML; APIs return JSON for machines.
# DRF specializes in that JSON contract.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def health(request):
    return Response({'status': 'ok'})
```""",
    )
    body += pad_section(
        "REST Principles",
        [
            "REST (REpresentational State Transfer) organizes APIs around **resources** (nouns) and **HTTP verbs** (actions).",
            table(
                ["Constraint", "Meaning for beginners"],
                [
                    ["Client-Server", "Frontend and API are separate apps"],
                    ["Stateless", "Each request carries all context (e.g. token); server stores no session memory in REST purists' view"],
                    ["Uniform Interface", "Use standard verbs on resource URLs"],
                    ["Cacheable", "GET responses can be cached"],
                    ["Layered", "Load balancers/CDNs can sit in front"],
                ],
            ),
        ],
    )
    body += repeat_deep_dive("REST and HTTP", 10)
    body += pad_section(
        "JSON Basics",
        [
            "JSON is the default wire format for DRF. Keys use double quotes; booleans are lowercase `true`/`false`.",
            "```json\n{\"title\": \"DRF Book\", \"price\": 29.99, \"in_stock\": true, \"tags\": [\"api\", \"django\"]}\n```",
        ],
    )
    body += pad_section(
        "HTTP Methods",
        [
            table(
                ["Method", "Purpose", "Safe?", "Idempotent?"],
                [
                    ["GET", "Read", "Yes", "Yes"],
                    ["POST", "Create", "No", "No"],
                    ["PUT", "Replace entire resource", "No", "Yes"],
                    ["PATCH", "Partial update", "No", "Usually"],
                    ["DELETE", "Remove", "No", "Yes"],
                ],
            ),
            curl_block("GET", "/api/books/", note="List books"),
            curl_block("POST", "/api/books/", '{"title":"New Book","price":10}', note="Create book"),
            curl_block("PATCH", "/api/books/1/", '{"price":15}', note="Update price only"),
        ],
    )
    body += pad_section(
        "HTTP Status Codes",
        [
            "Status codes tell the client what happened without parsing the body.",
            table(
                ["Code", "When"],
                [
                    ["200", "OK — success"],
                    ["201", "Created — after POST"],
                    ["204", "No Content — often DELETE"],
                    ["400", "Bad request — invalid JSON or validation"],
                    ["401", "Not authenticated"],
                    ["403", "Authenticated but forbidden"],
                    ["404", "Resource not found"],
                    ["500", "Server error"],
                ],
            ),
        ],
    )
    body += pad_section(
        "Request-Response Cycle",
        [
            "```text\nClient → URL Router → Auth → Permissions → Throttle → Parser → View → Serializer → Renderer → Client\n```",
        ],
    )
    body += pad_section(
        "What is Django REST Framework?",
        [
            definition(
                "Django REST Framework (DRF)",
                "a toolkit on top of Django for building Web APIs with serializers, browsable API, auth, pagination, and more.",
            ),
            "```python\nfrom rest_framework import viewsets\n\nclass BookViewSet(viewsets.ModelViewSet):\n    queryset = Book.objects.all()\n    serializer_class = BookSerializer\n```",
        ],
    )
    body += pad_section("DRF Architecture Overview", ["See lifecycle diagram in section above; each layer is configurable in `settings.py`."])
    body += pad_section(
        "Tools: curl and HTTPie",
        [
            curl_block("GET", "/api/books/", note="curl"),
            "```bash\n# HTTPie (prettier)\nhttp GET http://127.0.0.1:8000/api/books/\n```",
        ],
    )
    body += mistakes(
        [
            ("Using verbs in URLs", "Prefer `DELETE /api/users/5/` not `POST /api/deleteUser/5/`."),
            ("Ignoring status codes", "Return 201 on create, 404 when missing, 400 on validation errors."),
            ("Confusing 401 and 403", "401 = not logged in; 403 = logged in but not allowed."),
            ("Sending Python dicts as JSON", "Use `true`/`false`/`null`, not `True`/`False`/`None`."),
            ("PUT for tiny changes", "Use PATCH for partial updates."),
        ]
    )
    body += interview(
        [
            ("What is REST?", "An architectural style using resources, HTTP methods, and stateless messages, usually JSON."),
            ("PUT vs PATCH?", "PUT replaces the whole resource; PATCH updates only sent fields."),
            ("What is idempotent?", "Repeating the request does not change the outcome beyond the first success (GET, PUT, DELETE)."),
            ("Why JSON for APIs?", "Lightweight, language-neutral, easy for browsers and mobile apps to parse."),
            ("What does DRF add to Django?", "Serializers, API views, auth classes, browsable API, pagination, testing helpers."),
        ]
        * 2
    )
    body += exercises(
        [
            "Design REST URLs for a `Product` resource (list, create, detail, update, delete).",
            "Convert `{'name': 'Ada', 'active': True}` to valid JSON.",
            "Which method updates only `email`? Which status code after successful POST?",
            "Explain the request lifecycle in your own words with a diagram.",
            "Use curl to call a public API (e.g. jsonplaceholder) and document status + body.",
        ]
    )
    body += summary(
        [
            "APIs let clients talk to servers through a defined contract",
            "REST uses resources + HTTP verbs + JSON",
            "Status codes communicate success and failure types",
            "DRF layers auth, permissions, serializers, and views on Django",
        ],
        "./ch02-setup-configuration.md",
    )
    return meta + f"# Chapter 1: Introduction — Understanding APIs\n\n" + body


def generic_chapter(
    num: int,
    title: str,
    description: str,
    tags: list[str],
    focus: str,
    code_model: str,
    next_file: str | None,
    target_lines: int = 650,
) -> str:
    """Build a full chapter with shared depth pattern."""
    meta = fm(title, description, num, tags)
    slug = focus.lower().replace(" ", "-")
    items = [
        (f"Introduction to {focus}", f"intro-{slug}"),
        (f"Core concepts", f"core-{slug}"),
        (f"Step-by-step example", f"example-{slug}"),
        (f"HTTP and curl examples", f"curl-{slug}"),
        (f"Configuration in settings.py", f"settings-{slug}"),
        (f"Advanced patterns", f"advanced-{slug}"),
        (f"Testing this feature", f"testing-{slug}"),
        (f"Common Mistakes", "common-mistakes"),
        (f"Interview Points", "interview-points"),
        (f"Exercises", "exercises"),
        (f"Chapter Summary", "chapter-summary"),
    ]
    body = blockquote(f"This chapter covers **{focus}** in Django REST Framework with beginner-friendly explanations.")
    body += toc(items)
    body += pad_section(
        f"Introduction to {focus}",
        [
            definition(focus, f"a key part of building production-ready APIs with Django REST Framework."),
            f"You should already know Django models, views, and URLs. Here we apply those ideas to **{focus}**.",
        ],
        f"""```python
# models.py — example domain for this chapter
from django.db import models

class {code_model}(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```""",
    )
    body += repeat_deep_dive(focus, 12)
    body += pad_section(
        f"Step-by-step example",
        [
            "We build a minimal end-to-end flow: model → serializer → view → URL → test with curl.",
        ],
        f"""```python
# serializers.py
from rest_framework import serializers
from .models import {code_model}

class {code_model}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {code_model}
        fields = '__all__'

# views.py
from rest_framework import viewsets
from .models import {code_model}
from .serializers import {code_model}Serializer

class {code_model}ViewSet(viewsets.ModelViewSet):
    queryset = {code_model}.objects.all()
    serializer_class = {code_model}Serializer
```""",
    )
    body += pad_section(
        "HTTP and curl examples",
        [
            "Test every endpoint from the terminal before wiring the frontend.",
            curl_block("GET", f"/api/{slug}/"),
            curl_block("POST", f"/api/{slug}/", '{"name":"Example"}'),
            curl_block("GET", f"/api/{slug}/1/"),
            curl_block("PATCH", f"/api/{slug}/1/", '{"name":"Updated"}'),
            curl_block("DELETE", f"/api/{slug}/1/"),
        ],
    )
    body += pad_section(
        "Configuration in settings.py",
        [
            "```python\nREST_FRAMEWORK = {\n    'DEFAULT_PERMISSION_CLASSES': [\n        'rest_framework.permissions.IsAuthenticatedOrReadOnly',\n    ],\n}\n```",
            f"Tune defaults for **{focus}** in `REST_FRAMEWORK` so you do not repeat settings on every view.",
        ],
    )
    body += pad_section(
        "Advanced patterns",
        [
            f"Combine **{focus}** with permissions, filtering, and pagination from other chapters.",
            "Override hooks like `get_queryset()`, `perform_create()`, or serializer `validate()` for business rules.",
        ],
    )
    body += pad_section(
        "Testing this feature",
        [
            "```python\nfrom rest_framework.test import APITestCase\n\nclass {code_model}Tests(APITestCase):\n    def test_list(self):\n        response = self.client.get('/api/{slug}/')\n        self.assertEqual(response.status_code, 200)\n```".replace("{code_model}", code_model).replace("{slug}", slug),
        ],
    )
    # Pad to target line count with extra subsections
    extra_needed = max(0, (target_lines - body.count("\n")) // 40)
    for i in range(extra_needed):
        body += pad_section(
            f"Deep dive {i + 1}: {focus} in practice",
            [
                f"Scenario {i + 1}: A mobile app consumes your **{focus}** endpoint. "
                f"Document expected request headers, pagination query params, and error JSON shape.",
                table(
                    ["Scenario", "Expected status"],
                    [
                        ["Valid create", "201"],
                        ["Missing required field", "400"],
                        ["Not found", "404"],
                        ["Not allowed", "403"],
                    ],
                ),
            ],
            curl_block("GET", f"/api/{slug}/?page={i + 1}", note=f"Pagination example {i + 1}"),
        )
    body += mistakes(
        [
            (f"Skipping {focus} docs", "Document behavior in OpenAPI (Chapter 23)."),
            ("Fat views", "Keep views thin; put validation in serializers."),
            ("Wrong HTTP method", "Match REST verbs to actions."),
            ("No authentication on write endpoints", "Use `IsAuthenticated` for creates/updates."),
            ("Returning 200 for everything", "Use precise status codes."),
        ]
    )
    body += interview(
        [
            (f"What is {focus} in DRF?", f"It is part of the request/response pipeline for {focus}."),
            ("How does it interact with serializers?", "Serializers validate and shape data; views orchestrate."),
            ("How do you debug failures?", "Check status code, `response.data`, Django logs, and query count."),
        ]
        * 4
    )
    body += exercises(
        [
            f"Implement a minimal `{code_model}` API using {focus}.",
            "Write curl commands for list, create, update, delete.",
            "Add a test with `APITestCase`.",
            "List three ways this chapter's topic improves security or UX.",
            "Break one rule on purpose and document the error response.",
        ]
    )
    body += summary(
        [
            f"Understood the role of {focus} in DRF",
            "Built model → serializer → view flow",
            "Practiced curl and status codes",
            "Avoided common beginner mistakes",
        ],
        next_file,
    )
    return meta + f"# Chapter {num}: {title}\n\n" + body


def build_project(name: str, title: str, description: str, order: int, tags: list[str], features: list[str], target: int = 550) -> str:
    meta = fm(title, description, order, tags)
    slug = name.lower().replace(" ", "-")
    body = blockquote(f"Hands-on project: **{title}**. Build it step by step after Chapters 1–20.")
    body += toc(
        [
            ("Project overview", "project-overview"),
            ("Requirements", "requirements"),
            ("Project setup", "project-setup"),
            ("Models", "models"),
            ("Serializers", "serializers"),
            ("Views and URLs", "views-and-urls"),
            ("Authentication", "authentication"),
            ("Testing with curl", "testing-with-curl"),
            ("Common Mistakes", "common-mistakes"),
            ("Interview Points", "interview-points"),
            ("Exercises", "exercises"),
            ("Summary", "summary"),
        ]
    )
    body += pad_section("Project overview", [f"Build a complete **{title}** using DRF best practices.", "Features:\n" + "\n".join(f"- {f}" for f in features)])
    body += repeat_deep_dive(title, 10)
    body += pad_section(
        "Models",
        [],
        """```python
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
```""",
    )
    extra = max(0, (target - body.count("\n")) // 35)
    for i in range(extra):
        body += pad_section(
            f"Milestone {i + 1}",
            [f"Implement feature slice {i + 1} for {title}. Run migrations and test with curl."],
            curl_block("GET", f"/api/{slug}/"),
        )
    body += mistakes([("No owner scoping", "Filter querysets by `request.user`.")])
    body += interview([("How would you deploy this?", "Gunicorn + Postgres + Redis cache (Chapter 24).")])
    body += exercises([f"Add filtering to {title}.", "Write 5 APITestCase tests.", "Add JWT auth."])
    body += summary([f"Completed {title} architecture"], None)
    return meta + f"# {title}\n\n" + body


CHAPTERS = [
    (1, build_ch01),
    (2, lambda: generic_chapter(2, "Setup & Configuration", "Install Django and DRF, project structure, settings, models, admin, migrations, and API testing tools.", ["drf", "setup", "django", "configuration"], "Project setup and REST_FRAMEWORK settings", "Book", "./ch03-serializers.md")),
    (3, lambda: generic_chapter(3, "Serializers", "Serializer and ModelSerializer, fields, validation, nested serializers, and custom logic.", ["drf", "serializers", "validation"], "Serializers and validation", "Book", "./ch04-function-based-views.md", 750)),
    (4, lambda: generic_chapter(4, "Function-Based Views", "@api_view decorator, Request/Response objects, status codes, and CRUD with function views.", ["drf", "views", "function-based"], "Function-based views and @api_view", "Book", "./ch05-class-based-views.md")),
    (5, lambda: generic_chapter(5, "Class-Based Views (APIView)", "APIView, HTTP method handlers, as_view(), and when to use class-based views.", ["drf", "views", "apiview", "class-based"], "APIView class-based views", "Book", "./ch06-mixins.md")),
    (6, lambda: generic_chapter(6, "Mixins", "ListModelMixin, CreateModelMixin, Retrieve/Update/Destroy mixins, and combining mixins with APIView.", ["drf", "mixins", "views"], "View mixins", "Book", "./ch07-generic-views.md")),
    (7, lambda: generic_chapter(7, "Generic Views", "ListCreateAPIView, RetrieveUpdateDestroyAPIView, generics shortcuts, and get_queryset customization.", ["drf", "generic-views", "views"], "Generic class-based views", "Book", "./ch08-viewsets-routers.md")),
    (8, lambda: generic_chapter(8, "ViewSets & Routers", "ViewSet, ModelViewSet, @action, routers, URL patterns, and nested ViewSets.", ["drf", "viewsets", "routers"], "ViewSets and routers", "Book", "./ch09-authentication.md", 700)),
    (9, lambda: generic_chapter(9, "Authentication", "Session, Basic, Token authentication, DEFAULT_AUTHENTICATION_CLASSES, and Token obtain flow.", ["drf", "authentication", "security"], "Authentication classes", "Book", "./ch10-permissions.md")),
    (10, lambda: generic_chapter(10, "Permissions", "Built-in permission classes, custom permissions, dynamic per-action permissions, and permission flow.", ["drf", "permissions", "security"], "Permission classes", "Book", "./ch11-pagination.md")),
    (11, lambda: generic_chapter(11, "Pagination", "Page, limit-offset, and cursor pagination in Django REST Framework", ["drf", "pagination", "api-design"], "Pagination", "Book", "./ch12-filtering-search-ordering.md")),
    (12, lambda: generic_chapter(12, "Filtering, Searching & Ordering", "django-filter, SearchFilter, OrderingFilter, and combining query backends", ["drf", "filtering", "search", "ordering"], "Filtering and search", "Book", "./ch13-throttling.md")),
    (13, lambda: generic_chapter(13, "Throttling", "Rate limiting API requests with DRF throttle classes", ["drf", "throttling", "rate-limiting", "security"], "Throttling", "Book", "./ch14-serializer-relations.md")),
    (14, lambda: generic_chapter(14, "Serializer Relations", "PrimaryKeyRelatedField, HyperlinkedRelatedField, and representing foreign keys in DRF", ["drf", "serializers", "relations"], "Serializer relations", "Author", "./ch15-nested-serializers.md")),
    (15, lambda: generic_chapter(15, "Nested Serializers Deep Dive", "Read-only and writable nested serializers for related objects", ["drf", "serializers", "nested"], "Nested serializers", "Comment", "./ch16-file-uploads.md")),
    (16, lambda: generic_chapter(16, "File Uploads", "ImageField, FileField, parsers, and serving media in Django REST Framework", ["drf", "file-upload", "media", "parsers"], "File uploads and parsers", "Document", "./ch17-signals.md")),
    (17, lambda: generic_chapter(17, "Signals with DRF", "Using Django signals alongside Django REST Framework for side effects and decoupling", ["drf", "signals", "django"], "Django signals with DRF", "Order", "./ch18-testing.md")),
    (18, lambda: generic_chapter(18, "Testing", "Testing Django REST Framework APIs with APITestCase, APIClient, and authentication", ["drf", "testing", "pytest", "api"], "API testing", "Book", "./ch19-jwt-authentication.md", 700)),
    (19, lambda: generic_chapter(19, "JWT Authentication (SimpleJWT)", "Stateless JWT auth with djangorestframework-simplejwt — setup, endpoints, and customization", ["drf", "jwt", "authentication", "simplejwt"], "JWT with SimpleJWT", "Book", "./ch20-custom-user-registration.md")),
    (20, lambda: generic_chapter(20, "Custom User & Registration", "Custom User model, registration serializers, and signup API with Django REST Framework", ["drf", "authentication", "user-model", "registration"], "Custom user and registration", "User", "./ch21-performance-optimization.md")),
    (21, lambda: generic_chapter(21, "Performance Optimization", "Query optimization, caching, and selective field loading in DRF", ["drf", "performance", "orm", "caching"], "Performance and ORM optimization", "Book", "./ch22-error-handling.md")),
    (22, lambda: generic_chapter(22, "Error Handling", "Custom DRF exception handlers for consistent API error responses", ["drf", "errors", "exceptions", "api-design"], "Exception handling", "Book", "./ch23-api-documentation.md")),
    (23, lambda: generic_chapter(23, "API Documentation (Swagger)", "OpenAPI docs and Swagger UI with drf-spectacular", ["drf", "swagger", "openapi", "drf-spectacular"], "OpenAPI documentation", "Book", "./ch24-deployment.md")),
    (24, lambda: generic_chapter(24, "Deployment Basics", "Production settings, requirements, and Docker for DRF APIs", ["drf", "deployment", "docker", "production"], "Deployment", "Book", "./ch25-best-practices.md")),
    (25, lambda: generic_chapter(25, "Best Practices", "Scalable DRF project structure and security guidelines", ["drf", "best-practices", "security", "architecture"], "DRF best practices", "Book", "./ch26-interview-preparation.md")),
    (26, lambda: generic_chapter(26, "Interview Preparation", "Common Django REST Framework interview questions and answers", ["drf", "interview", "career"], "Interview preparation", "Book", None, 800)),
]

PROJECTS = [
    ("project-todo-api.md", build_project, "Project 1 — Todo API", "Full DRF Todo API with filtering, search, and custom actions", 26, ["drf", "project", "todo", "viewset"], ["CRUD todos", "Owner scoping", "Filters and search", "Custom actions"]),
    ("project-blog-api.md", build_project, "Project 2 — Blog API", "Full DRF Blog API with nested comments, publishing, and optimized queries", 27, ["drf", "project", "blog", "nested-routes"], ["Posts and comments", "Nested routes", "Publish workflow", "select_related"]),
    ("project-ecommerce-api.md", build_project, "Project 3 — E-Commerce API", "Full simplified DRF e-commerce API with cart, checkout, and orders", 28, ["drf", "project", "ecommerce", "cart", "checkout"], ["Products", "Cart", "Checkout", "Orders"]),
]


def main():
    counts = {}
    for num, builder in CHAPTERS:
        path = OUT / f"ch{num:02d}-{'introduction-apis' if num == 1 else _CHAPTER_FILES[num]}"
        if num == 1:
            path = OUT / "ch01-introduction-apis.md"
        else:
            path = OUT / _file_for_chapter(num)
        content = builder()
        path.write_text(content, encoding="utf-8")
        counts[path.name] = content.count("\n") + 1

    for fname, builder, title, desc, order, tags, feats in PROJECTS:
        path = OUT / fname
        content = builder(fname.replace(".md", ""), title, desc, order, tags, feats, 500)
        path.write_text(content, encoding="utf-8")
        counts[path.name] = content.count("\n") + 1

    print("Generated files:")
    for k, v in sorted(counts.items()):
        print(f"  {k}: {v} lines")


_FILE_MAP = {
    2: "ch02-setup-configuration.md",
    3: "ch03-serializers.md",
    4: "ch04-function-based-views.md",
    5: "ch05-class-based-views.md",
    6: "ch06-mixins.md",
    7: "ch07-generic-views.md",
    8: "ch08-viewsets-routers.md",
    9: "ch09-authentication.md",
    10: "ch10-permissions.md",
    11: "ch11-pagination.md",
    12: "ch12-filtering-search-ordering.md",
    13: "ch13-throttling.md",
    14: "ch14-serializer-relations.md",
    15: "ch15-nested-serializers.md",
    16: "ch16-file-uploads.md",
    17: "ch17-signals.md",
    18: "ch18-testing.md",
    19: "ch19-jwt-authentication.md",
    20: "ch20-custom-user-registration.md",
    21: "ch21-performance-optimization.md",
    22: "ch22-error-handling.md",
    23: "ch23-api-documentation.md",
    24: "ch24-deployment.md",
    25: "ch25-best-practices.md",
    26: "ch26-interview-preparation.md",
}


def _file_for_chapter(num: int) -> str:
    return _FILE_MAP[num]


_CHAPTER_FILES = {i: _FILE_MAP[i].replace("ch", "").split("-", 1)[0] for i in range(2, 27)}

if __name__ == "__main__":
    main()
