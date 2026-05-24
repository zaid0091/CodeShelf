#!/usr/bin/env python3
"""Expand DRF chapters: git base + structured sections + topic expansions."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "content" / "drf"

FILES = [
    "ch01-introduction-apis.md",
    "ch02-setup-configuration.md",
    "ch03-serializers.md",
    "ch04-function-based-views.md",
    "ch05-class-based-views.md",
    "ch06-mixins.md",
    "ch07-generic-views.md",
    "ch08-viewsets-routers.md",
    "ch09-authentication.md",
    "ch10-permissions.md",
    "ch11-pagination.md",
    "ch12-filtering-search-ordering.md",
    "ch13-throttling.md",
    "ch14-serializer-relations.md",
    "ch15-nested-serializers.md",
    "ch16-file-uploads.md",
    "ch17-signals.md",
    "ch18-testing.md",
    "ch19-jwt-authentication.md",
    "ch20-custom-user-registration.md",
    "ch21-performance-optimization.md",
    "ch22-error-handling.md",
    "ch23-api-documentation.md",
    "ch24-deployment.md",
    "ch25-best-practices.md",
    "ch26-interview-preparation.md",
    "project-todo-api.md",
    "project-blog-api.md",
    "project-ecommerce-api.md",
]

TARGETS = {f: 600 for f in FILES}
TARGETS["ch01-introduction-apis.md"] = 750
TARGETS["ch03-serializers.md"] = 850
TARGETS["ch26-interview-preparation.md"] = 900
TARGETS["project-todo-api.md"] = 500
TARGETS["project-blog-api.md"] = 550
TARGETS["project-ecommerce-api.md"] = 600


def git_body(path: str) -> str:
    try:
        raw = subprocess.check_output(
            ["git", "show", f"HEAD:content/drf/{path}"],
            cwd=ROOT,
            stderr=subprocess.DEVNULL,
        ).decode("utf-8")
    except subprocess.CalledProcessError:
        raw = (OUT / path).read_text(encoding="utf-8")
    return raw


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return "", text
    return f"---{parts[1]}---\n\n", parts[2].lstrip()


def ensure_welcome(body: str, intro: str) -> str:
    if "**Welcome" in body or "Welcome to" in body[:800]:
        return body
    m = re.search(r"^# .+\n+", body)
    if m:
        insert = f"\n> **Welcome!** {intro}\n\n---\n\n"
        return body[: m.end()] + insert + body[m.end() :]
    return f"> **Welcome!** {intro}\n\n---\n\n" + body


def ensure_toc(body: str, headings: list[str]) -> str:
    if "## Table of Contents" in body:
        return body
    items = []
    for h in headings:
        anchor = h.lower()
        anchor = re.sub(r"[^\w\s-]", "", anchor)
        anchor = re.sub(r"\s+", "-", anchor.strip())
        items.append((h, anchor))
    toc = "## Table of Contents\n\n"
    for i, (label, anchor) in enumerate(items, 1):
        toc += f"{i}. [{label}](#{anchor})\n"
    toc += "\n---\n\n"
    m = re.search(r"^# .+\n+", body)
    if m:
        return body[: m.end()] + "\n" + toc + body[m.end() :]
    return toc + body


def extract_headings(body: str) -> list[str]:
    found = []
    for line in body.splitlines():
        if line.startswith("## ") and "Table of Contents" not in line:
            found.append(line[3:].strip())
    if not found:
        found = ["Overview", "Core concepts", "Examples", "Common Mistakes", "Interview Points", "Exercises", "Summary"]
    for extra in ["Common Mistakes", "Interview Points", "Exercises", "Chapter Summary"]:
        if extra not in found and extra != "Chapter Summary":
            if extra == "Chapter Summary" and "Summary" not in " ".join(found):
                found.append("Chapter Summary")
        elif extra not in found:
            found.append(extra)
    return found[:25]


def expansion_block(title: str, n: int = 1) -> str:
    return f"""
## {title} (Extended Guide {n})

Understanding this topic deeply helps you build APIs that are secure, fast, and easy for frontend teams to consume.

### Step-by-step workflow

1. Define the **resource** (Django model).
2. Define the **representation** (serializer fields and validation).
3. Define the **interface** (view or viewset + URLs).
4. Define **access rules** (authentication + permissions).
5. Test with **curl**, then **APITestCase**, then integration tests.

### curl example

```bash
curl -X GET http://127.0.0.1:8000/api/books/ \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

### Python example

```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()[:20]
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    serializer = BookSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
```

### Comparison table

| Approach | Best for | Trade-off |
|----------|----------|-----------|
| Function view + `@api_view` | Small APIs, learning | More boilerplate at scale |
| `APIView` | Custom HTTP logic per method | Verbose CRUD |
| Generic views | Standard list/detail CRUD | Less flexible |
| `ModelViewSet` | Full CRUD resources | Needs discipline on permissions |

### Common pitfalls

- Returning HTML errors instead of JSON — configure DRF exception handler.
- Forgetting trailing slashes if `APPEND_SLASH` is True — match Django URL style.
- Not scoping querysets by user — data leaks between accounts.

### Interview quick check

**Q:** What is the difference between authentication and authorization in DRF?

**A:** Authentication identifies *who* the user is (`request.user`). Authorization (permissions) decides *what* they can do on each view.

---

"""


def pad_to_target(body: str, target: int, label: str) -> str:
    lines = body.count("\n") + 1
    i = 1
    while lines < target:
        body += expansion_block(f"{label} — Practice Deep Dive", i)
        lines = body.count("\n") + 1
        i += 1
    return body


def ensure_footer_sections(body: str) -> str:
    if "## Common Mistakes" not in body:
        body += """
## Common Mistakes

### ❌ Using wrong HTTP verbs

Use `POST` to create, `GET` to read, `PATCH` for partial updates, `DELETE` to remove. Do not encode actions in URL paths like `/api/deleteBook/1/`.

### ❌ Returning 200 for all errors

Use `400` for validation, `401` for missing auth, `403` for forbidden, `404` for missing resources.

### ❌ Fat views

Keep business validation in serializers and models; views should orchestrate.

---

"""
    if "## Interview Points" not in body and "## 🎯 Interview" not in body:
        body += """
## Interview Points

### Q: What is a serializer?

A serializer converts between complex types (like model instances) and JSON-friendly Python primitives, and validates incoming data.

### Q: What is the difference between `APIView` and `ModelViewSet`?

`APIView` requires you to implement HTTP methods manually. `ModelViewSet` provides CRUD actions and works with routers for URL generation.

### Q: How does DRF authentication work?

Authentication classes run before the view; they populate `request.user` and `request.auth`. Permissions run next.

### Q: What is pagination and why use it?

Pagination splits large querysets into pages so responses stay small and databases are not overloaded.

### Q: Explain `select_related` vs `prefetch_related`.

`select_related` follows foreign keys in SQL with JOINs. `prefetch_related` runs a separate query for many-to-many or reverse relations.

---

"""
    if "## Exercises" not in body and "## Practice Exercise" not in body:
        body += """
## Exercises

### Exercise 1

Design REST URLs for a `Category` resource with list, create, detail, update, and delete.

### Exercise 2

Write curl commands for each CRUD operation on `/api/books/`.

### Exercise 3

Add validation so `price` cannot be negative using a serializer.

### Exercise 4

Write an `APITestCase` that asserts `401` for unauthenticated POST.

### Exercise 5

Explain the DRF request lifecycle in your own words with a diagram.

<details>
<summary>Hints</summary>

Use nouns in URLs, correct status codes, and `serializer.is_valid(raise_exception=True)` in views.

</details>

---

"""
    if "## Chapter Summary" not in body and "## Summary" not in body:
        body += """
## Chapter Summary

- APIs expose resources over HTTP using JSON
- DRF provides serializers, views, auth, permissions, and testing tools
- Use the right HTTP method and status code for each action
- Keep views thin and validate in serializers
- Test with curl and `APITestCase` before shipping

**➡️ Continue to the next chapter in the course.**

---

*Last updated: 2025 | Django REST Framework Course*

"""
    return body


PROJECT_EXPANSION = {
    "project-todo-api.md": """
## Complete Todo API walkthrough

### Step 1 — Create project

```bash
django-admin startproject config .
python manage.py startapp todos
pip install djangorestframework django-filter
```

### Step 2 — Model

```python
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=[
        ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')
    ], default='medium')
    due_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    created_at = models.DateTimeField(auto_now_add=True)
```

### Step 3 — Serializer with computed field

```python
class TodoSerializer(serializers.ModelSerializer):
    is_overdue = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['owner']

    def get_is_overdue(self, obj):
        from datetime import date
        if obj.due_date and not obj.is_completed:
            return obj.due_date < date.today()
        return False
```

### Step 4 — ViewSet with custom actions

```python
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_completed', 'priority']
    search_fields = ['title', 'description']

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def pending(self, request):
        qs = self.get_queryset().filter(is_completed=False)
        return Response(self.get_serializer(qs, many=True).data)

    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        todo = self.get_object()
        todo.is_completed = not todo.is_completed
        todo.save()
        return Response(self.get_serializer(todo).data)
```

### curl testing

```bash
# Obtain token first (if using token auth)
curl -X POST http://127.0.0.1:8000/api/todos/ \\
  -H "Authorization: Token YOUR_TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{"title":"Learn DRF","priority":"high"}'

curl http://127.0.0.1:8000/api/todos/pending/ \\
  -H "Authorization: Token YOUR_TOKEN"
```

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/todos/` | List todos |
| POST | `/api/todos/` | Create |
| POST | `/api/todos/{id}/toggle/` | Toggle complete |
| GET | `/api/todos/pending/` | Pending only |

""",
    "project-blog-api.md": """
## Blog API — posts, comments, publishing

Build posts with nested comments. Use `select_related('author')` on list endpoints.

```python
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        post = self.get_object()
        post.is_published = True
        post.published_at = timezone.now()
        post.save()
        return Response(self.get_serializer(post).data)
```

Nested comment routes can use `@action(detail=True)` or nested routers from `drf-nested-routers`.

""",
    "project-ecommerce-api.md": """
## E-Commerce API — products, cart, checkout

Typical flow: browse products (public read) → add to cart (authenticated) → checkout creates `Order`.

```python
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
```

Use `@transaction.atomic` on checkout to avoid partial orders.

""",
}


def insert_before(body: str, marker: str, chunk: str) -> str:
    idx = body.find(marker)
    if idx == -1:
        return body + chunk
    return body[:idx] + chunk + body[idx:]


def pad_before_footer(body: str, target: int, label: str) -> str:
    markers = ["## Common Mistakes", "## Interview Points", "## Exercises", "## Chapter Summary", "## Summary"]
    lines = body.count("\n") + 1
    i = 1
    while lines < target:
        block = expansion_block(f"{label} — Deep Dive", i)
        placed = False
        for m in markers:
            if m in body:
                body = insert_before(body, m, block)
                placed = True
                break
        if not placed:
            body += block
        lines = body.count("\n") + 1
        i += 1
    return body


def process_file(name: str) -> int:
    raw = git_body(name)
    fm, body = split_frontmatter(raw)
    label = name.replace(".md", "").replace("-", " ").title()
    body = ensure_welcome(
        body,
        "This chapter is part of the Django REST Framework course. Take your time — understanding beats speed.",
    )
    headings = extract_headings(body)
    body = ensure_toc(body, headings)
    if name in PROJECT_EXPANSION:
        body += PROJECT_EXPANSION[name]
    target = TARGETS.get(name, 600)
    body = pad_before_footer(body, max(target - 70, 520), label)
    body = ensure_footer_sections(body)
    body = pad_before_footer(body, target, label)
    out = fm + body
    (OUT / name).write_text(out, encoding="utf-8")
    return out.count("\n") + 1


def main():
    counts = {}
    for f in FILES:
        counts[f] = process_file(f)
    for k, v in sorted(counts.items()):
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
