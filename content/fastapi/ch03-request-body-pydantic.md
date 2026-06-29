---
title: Request Body & Pydantic
description: Learn how to handle JSON payloads using Pydantic models, write validations with Field, handle nested objects, and define custom response schemas in FastAPI.
order: 3
tags: [fastapi, pydantic, request-body, validation, models]
---

# Chapter 3: Request Body & Pydantic

> **Understand how to accept JSON payloads in HTTP request bodies, define structures using Pydantic, validate individual fields, and format responses.**

---

## Table of Contents

1. [What is a Request Body?](#what-is-a-request-body)
2. [Declaring Pydantic Models](#declaring-pydantic-models)
3. [Field Validation](#field-validation)
4. [Nested Models](#nested-models)
5. [Response Models](#response-models)
6. [Best Practices](#best-practices)
7. [Common Mistakes](#common-mistakes)
8. [Interview Points](#interview-points)
9. [Exercises](#exercises)
10. [Chapter Summary](#chapter-summary)

---

## What is a Request Body?

A request body is data sent by the client to your API inside the HTTP request payload (typically via `POST`, `PUT`, or `PATCH`). Unlike path or query parameters, the body is formatted as JSON.

---

## Declaring Pydantic Models

In FastAPI, you declare request bodies by defining a class that inherits from Pydantic's `BaseModel`.

```python
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Define the Pydantic schema
class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# 2. Add it as a parameter in your route
@app.post("/products/")
def create_product(product: Product):
    product_dict = product.model_dump() # Convert to dict
    if product.tax:
        price_with_tax = product.price + product.tax
        product_dict.update({"total_price": price_with_tax})
    return product_dict
```
FastAPI automatically parses the incoming JSON, validates it against the schema types, and binds the values to the `product` parameter as an instance of the `Product` model.

---

## Field Validation

You can add constraints to individual model fields using Pydantic's `Field` function.

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, pattern="^[a-zA-Z0-9_]+$")
    email: str = Field(..., description="A valid email address")
    age: int = Field(..., ge=18, le=120, description="Users must be of legal age")
```
*   `Field(...)`: The `...` represents a required field.
*   `ge`, `le`: Numeric constraints (greater than/equal, less than/equal).
*   `min_length`, `max_length`: String size rules.

---

## Nested Models

Pydantic models can nest inside one another, allowing you to model complex JSON objects and arrays.

```python
from typing import List, Set

class Image(BaseModel):
    url: str
    name: str

class Article(BaseModel):
    title: str
    tags: Set[str] = set() # Unique values
    images: List[Image] = [] # Nested list of Image objects
```
Example JSON payload accepted:
```json
{
  "title": "Learning FastAPI",
  "tags": ["python", "api"],
  "images": [
    { "url": "https://example.com/logo.png", "name": "logo" }
  ]
}
```

---

## Response Models

FastAPI allows you to filter and validate outgoing data using the `response_model` parameter on path decorators. This is useful for hiding sensitive data like passwords or internal databases IDs.

```python
class UserCreate(BaseModel):
    username: str
    email: str
    password: str # Input schema includes password

class UserOut(BaseModel):
    username: str
    email: str # Output schema excludes password

@app.post("/users/", response_model=UserOut)
def create_user(user: UserCreate):
    # Process user registration (e.g., save to DB)
    return user
```
*Even though the route returns a model containing a password, the response sent back to the browser will only contain fields declared in `UserOut`.*

---

## Best Practices

*   **Separate schemas**: Use separate schemas for creation requests (`UserCreate`), update requests (`UserUpdate`), and read responses (`UserOut`).
*   **Use `model_dump()`**: In Pydantic v2, use `model.model_dump()` to convert a model instance to a dictionary. (Avoid `model.dict()`, which is deprecated).

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Using `dict()` in Pydantic v2 | Throws warnings or errors in newer versions | Replace `product.dict()` with `product.model_dump()`. |
| Missing response model filters | Might leak hashed passwords or private data fields | Use `response_model` in the `@app.route` decorator to restrict output. |

---

## Interview Points

> **📌 Interview Point 1: How does FastAPI use response models?**
> The `response_model` argument in the route decorator performs:
> 1. Data validation on the output.
> 2. Data serialization (converting Python objects to JSON-compatible types).
> 3. Data filtering (removing undeclared fields).

> **📌 Interview Point 2: What is the difference between Pydantic v1 and v2?**
> Pydantic v2 (written in Rust) is up to 20x faster. It replaces `.dict()` with `.model_dump()`, and `.json()` with `.model_dump_json()`. FastAPI supports Pydantic v2 natively.

---

## Exercises

### Exercise 1: Create a Blog Post schema with validations ⭐
**Task:** Define a Pydantic model for a `Post` containing:
- `title` (required, min length 5)
- `content` (required)
- `category` (optional, default "General")
Create a POST endpoint `/posts/` that accepts this model and returns it.

<details>
<summary>💡 Hint (click to reveal)</summary>
Subclass `BaseModel` and use `Field` for the title validation constraints.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str = Field(..., min_length=5)
    content: str
    category: Optional[str] = "General"

@app.post("/posts/")
def create_post(post: Post):
    return post
```
</details>

---

## Chapter Summary

*   Define request body structures by inheriting from Pydantic's `BaseModel`.
*   Validate attributes using constraints in `Field(...)`.
*   Use `response_model` in route decorators to filter out secrets and format output schemas.

---

## Previous / Next Chapter

**⬅️ [Previous: Path & Query Parameters](./ch02-path-query-parameters.md)**

**➡️ [Next: Dependency Injection](./ch04-dependency-injection.md)**

---

*Chapter 3 of the FastAPI Guide | CodeShelf*
