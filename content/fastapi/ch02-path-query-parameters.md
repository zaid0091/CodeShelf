---
title: Path & Query Parameters
description: Learn how to declare path and query parameters in FastAPI, perform type conversions, and validate parameters using Query and Path classes.
order: 2
tags: [fastapi, routing, path-parameters, query-parameters, validation]
---

# Chapter 2: Path & Query Parameters

> **Learn how to capture variables from URLs, configure optional values, auto-convert types, and add validations using Query and Path.**

---

## Table of Contents

1. [Path Parameters](#path-parameters)
2. [Query Parameters](#query-parameters)
3. [Type Conversion & Validation](#type-conversion--validation)
4. [Path Validation](#path-validation)
5. [Query Validation](#query-validation)
6. [Best Practices](#best-practices)
7. [Common Mistakes](#common-mistakes)
8. [Interview Points](#interview-points)
9. [Exercises](#exercises)
10. [Chapter Summary](#chapter-summary)

---

## Path Parameters

Path parameters are variables embedded inside the URL path itself. They are defined inside curly braces `{}` in the route and matched to the function arguments.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

### Automatic Type Validation
If you visit `http://127.0.0.1:8000/items/foo`, FastAPI will return a `422 Unprocessable Entity` status code indicating the value is not an integer:
```json
{
  "detail": [
    {
      "loc": ["path", "item_id"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

---

## Query Parameters

When you declare function arguments that are not part of the path, they are automatically interpreted as query parameters (URL query string key-value pairs).

```python
@app.get("/items/")
def list_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```
Visiting `http://127.0.0.1:8000/items/?skip=20&limit=5` returns `{"skip": 20, "limit": 5}`.

### Optional Query Parameters
Declare query parameters as optional by assigning a default value of `None`, or using standard Python `Optional`:

```python
from typing import Optional

@app.get("/items/{item_id}")
def get_item(item_id: int, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "search_query": q}
    return {"item_id": item_id}
```

---

## Type Conversion & Validation

FastAPI leverages type hints to convert inputs into specific Python classes. For example, booleans are parsed intelligently:

```python
@app.get("/items/{item_id}")
def get_item_status(item_id: int, short: bool = False):
    return {"item_id": item_id, "short_format": short}
```
Entering any of `short=true`, `short=1`, `short=yes`, or `short=on` will correctly parse `short` as `True`.

---

## Path Validation

You can add metadata and validation rules to path parameters using the `Path` class.

```python
from fastapi import Path

@app.get("/users/{user_id}")
def get_user(
    user_id: int = Path(..., title="The ID of the user to get", ge=1, le=1000)
):
    return {"user_id": user_id}
```
*   `ge=1`: Greater than or equal to 1.
*   `le=1000`: Less than or equal to 1000.
*   `...` (Ellipsis): Demarcates that the path parameter is required.

---

## Query Validation

Similarly, validation rules can be added to query parameters using the `Query` class.

```python
from fastapi import Query

@app.get("/search/")
def search(
    q: Optional[str] = Query(None, min_length=3, max_length=50, pattern="^[a-zA-Z0-9]+$")
):
    return {"query": q}
```
*   `min_length`/`max_length`: Sets limits on string characters.
*   `pattern`: Applies regular expression validation.

---

## Best Practices

*   **Order matters for overlapping routes**: Always define static paths (like `/users/me`) *before* dynamic paths (like `/users/{user_id}`). Otherwise, the server will match `"me"` as a `user_id`.
*   **Document query parameters**: Provide descriptions inside `Query(None, description="...")` to automatically enrich your Swagger docs.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Mismatching variable names | FastAPI cannot bind the URL parameter to the function argument | Ensure the name inside the curly braces `{item_id}` exactly matches the function parameter name `item_id`. |
| Putting dynamic paths first | Blocks access to static endpoints | Define `/items/all` before `/items/{item_id}`. |

---

## Interview Points

> **📌 Interview Point 1: What is the significance of the Ellipsis `...` in Path or Query parameters?**
> The `...` (Ellipsis) represents that the parameter is required. In modern FastAPI/Pydantic, you can also omit it, but declaring it explicitly makes it obvious.

> **📌 Interview Point 2: How does FastAPI handle validation errors?**
> It raises a `RequestValidationError` which triggers an internal exception handler, returning a structured `422 Unprocessable Entity` JSON response.

---

## Exercises

### Exercise 1: Write a validated path endpoint ⭐
**Task:** Create a dynamic path GET `/books/{book_id}` where `book_id` is an integer between 100 and 999 inclusive.

<details>
<summary>💡 Hint (click to reveal)</summary>
Use `Path(..., ge=100, le=999)`.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
from fastapi import Path

@app.get("/books/{book_id}")
def get_book(book_id: int = Path(..., ge=100, le=999)):
    return {"book_id": book_id}
```
</details>

---

## Chapter Summary

*   **Path parameters** are part of the URL path (`/items/{id}`); **Query parameters** are in the query string (`/items/?limit=10`).
*   FastAPI uses type hints to cast and validate input.
*   Use `Path` and `Query` from `fastapi` for parameter constraints (ranges, regex patterns).

---

## Previous / Next Chapter

**⬅️ [Previous: Introduction to FastAPI](./ch01-introduction.md)**

**➡️ [Next: Request Body & Pydantic](./ch03-request-body-pydantic.md)**

---

*Chapter 2 of the FastAPI Guide | CodeShelf*
