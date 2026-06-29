---
title: Dependency Injection
description: Understand FastAPI's Dependency Injection system. Learn how to write reusable dependencies, manage resource lifecycles with yield, and build sub-dependencies.
order: 4
tags: [fastapi, dependency-injection, depends, architecture, reusable-code]
---

# Chapter 4: Dependency Injection

> **Explore FastAPI's built-in dependency injection system. Learn how to inject shared logic, manage database connections, and override dependencies for unit testing.**

---

## Table of Contents

1. [What is Dependency Injection?](#what-is-dependency-injection)
2. [Declaring Dependencies in FastAPI](#declaring-dependencies-in-fastapi)
3. [Sub-dependencies](#sub-dependencies)
4. [Dependencies with yield (Resource Lifecycle)](#dependencies-with-yield-resource-lifecycle)
5. [Class-Based Dependencies](#class-based-dependencies)
6. [Best Practices](#best-practices)
7. [Common Mistakes](#common-mistakes)
8. [Interview Points](#interview-points)
9. [Exercises](#exercises)
10. [Chapter Summary](#chapter-summary)

---

## What is Dependency Injection?

Dependency Injection (DI) is a software design pattern where objects or functions are provided with the services or resources they depend on, rather than creating them internally.

In web applications, typical dependencies include:
*   Database connections or sessions.
*   Security schemas and authentication/authorization checkers.
*   External API clients.
*   Logging systems.

FastAPI has a extremely powerful, native dependency injection system that integrates with all your path operations.

---

## Declaring Dependencies in FastAPI

You inject dependencies using `Depends` from `fastapi`. First, define a helper function, and then pass it as a parameter default.

```python
from typing import Optional
from fastapi import FastAPI, Depends

app = FastAPI()

# 1. Define a dependency function
def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 10):
    return {"q": q, "skip": skip, "limit": limit}

# 2. Inject it into your route
@app.get("/items/")
def read_items(commons: dict = Depends(common_parameters)):
    return {"items": [], "params": commons}

@app.get("/users/")
def read_users(commons: dict = Depends(common_parameters)):
    return {"users": [], "params": commons}
```
FastAPI automatically parses the parameters (`q`, `skip`, `limit`) from the query string, runs `common_parameters`, and passes its return value to `commons`.

---

## Sub-dependencies

Dependencies can depend on other dependencies themselves. FastAPI automatically resolves the entire graph of dependencies.

```python
def query_extractor(q: Optional[str] = None):
    return q

# This dependency requires query_extractor
def query_checker(query: str = Depends(query_extractor)):
    if not query:
        return "default search"
    return query.upper()

@app.get("/search/")
def search(query: str = Depends(query_checker)):
    return {"processed_query": query}
```

---

## Dependencies with yield (Resource Lifecycle)

FastAPI supports dependencies that can execute cleanup logic after the route completes. This is done using the `yield` keyword instead of `return`.

This is the standard pattern for database sessions:

```python
def get_db_session():
    # Setup step
    db = DatabaseConnection()
    db.open_session()
    try:
        # Deliver the session to the route
        yield db
    finally:
        # Cleanup step (executed after request completes)
        db.close_session()
```
*If an exception occurs during the route execution, it propagates to the `finally` block, ensuring resources are safely closed and not leaked.*

---

## Class-Based Dependencies

Sometimes, dependencies need configurations or state. You can write class-based dependencies to group attributes and logic.

```python
class RoleChecker:
    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, user_role: str = "guest"):
        if user_role not in self.allowed_roles:
            from fastapi import HTTPException
            raise HTTPException(status_code=403, detail="Operation not allowed")
        return True

# Initialize checkers with specific configurations
admin_only = RoleChecker(["admin"])
staff_only = RoleChecker(["admin", "staff"])

@app.post("/admin/delete-database")
def delete_db(is_admin: bool = Depends(admin_only)):
    return {"message": "Database deleted!"}
```

---

## Best Practices

*   **Override dependencies in tests**: Utilize `app.dependency_overrides` during unit tests to inject mock database sessions or test accounts without modifying core code.
*   **Reuse dependencies**: Place shared logic (e.g., authentication) into reusable dependencies rather than copying code across multiple endpoints.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Declaring database sessions without `yield` | Connection leaks, exhausting database pool capacity | Always use `yield` in a `try...finally` block to close connections. |
| Calling the dependency function inside `Depends` | `Depends(get_db())` rather than `Depends(get_db)` invokes the function too early | Pass the function reference itself: `Depends(get_db)`. |

---

## Interview Points

> **📌 Interview Point 1: What is the lifecycle of a dependency in FastAPI?**
> A dependency is created when a request starts and resolves. If multiple dependencies rely on the same sub-dependency, FastAPI evaluates it only once per request and caches the result (unless `use_cache=False` is passed to `Depends`).

> **📌 Interview Point 2: How do you perform dependency overriding?**
> By using `app.dependency_overrides[original_dependency] = mock_dependency`. This is extremely useful in testing environments.

---

## Exercises

### Exercise 1: Write an authentication dependency ⭐
**Task:** Write a dependency `verify_api_key` that checks if an incoming header `X-API-Key` equals `secret-key-123`. If not, raise an `HTTPException(401)`.

<details>
<summary>💡 Hint (click to reveal)</summary>
Use `Header` to extract headers and raise `HTTPException` if key mismatch.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
from fastapi import Header, HTTPException, Depends

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != "secret-key-123":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key

@app.get("/secure-data")
def secure_data(api_key: str = Depends(verify_api_key)):
    return {"data": "Top secret information!"}
```
</details>

---

## Chapter Summary

*   Declare reusable arguments/logic using `Depends(dependency_function)`.
*   Use `yield` inside a dependency to execute cleanup tasks (like database connection closing).
*   Mock dependencies in unit tests using `app.dependency_overrides`.

---

## Previous / Next Chapter

**⬅️ [Previous: Request Body & Pydantic](./ch03-request-body-pydantic.md)**

**➡️ [Next: Database Integration (SQLAlchemy)](./ch05-database-integration-sqlalchemy.md)**

---

*Chapter 4 of the FastAPI Guide | CodeShelf*
