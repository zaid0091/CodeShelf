---
title: Testing FastAPI Applications
description: Write unit and integration tests for FastAPI using pytest. Learn how to test sync/async routes, override dependencies, and run mock databases.
order: 7
tags: [fastapi, testing, pytest, client, mock, async]
---

# Chapter 7: Testing FastAPI Applications

> **Build test coverage. Learn how to write synchronous tests with TestClient, asynchronous tests with HTTPX AsyncClient, and use dependency overrides.**

---

## Table of Contents

1. [Testing Toolkit (Pytest & HTTPX)](#testing-toolkit-pytest--httpx)
2. [Testing Synchronous Endpoints (TestClient)](#testing-synchronous-endpoints-testclient)
3. [Testing Asynchronous Endpoints (AsyncClient)](#testing-asynchronous-endpoints-asyncclient)
4. [Using Dependency Overrides for Mocking](#using-dependency-overrides-for-mocking)
5. [Configuring Test Databases with Pytest Fixtures](#configuring-test-databases-with-pytest-fixtures)
6. [Best Practices](#best-practices)
7. [Common Mistakes](#common-mistakes)
8. [Interview Points](#interview-points)
9. [Exercises](#exercises)
10. [Chapter Summary](#chapter-summary)

---

## Testing Toolkit (Pytest & HTTPX)

FastAPI relies on standard testing frameworks. Install `pytest` and `httpx` (required for testing clients):

```bash
pip install pytest httpx
```

---

## Testing Synchronous Endpoints (TestClient)

For synchronous endpoints or operations that don't block, use FastAPI's built-in `TestClient` (which wraps HTTPX):

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"ping": "pong"}
```

Create a `test_main.py` file:

```python
# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}
```

Run tests from the terminal:
```bash
pytest test_main.py
```

---

## Testing Asynchronous Endpoints (AsyncClient)

If your app uses `async def` and database layers, you should write async tests. Use `pytest-asyncio` and HTTPX's `AsyncClient`:

```bash
pip install pytest-asyncio
```

```python
# test_async.py
import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_async_ping():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/ping")
        assert response.status_code == 200
        assert response.json() == {"ping": "pong"}
```

---

## Using Dependency Overrides for Mocking

To run tests without executing database queries or hitting authentication tokens, override target dependencies:

```python
from main import app, get_current_user

# 1. Define dummy user mock
def mock_current_user():
    return {"username": "test_user", "email": "test@example.com"}

# 2. Assign override
app.dependency_overrides[get_current_user] = mock_current_user

# 3. Write test matching the override context
def test_protected_route():
    client = TestClient(app)
    response = client.get("/users/me")
    assert response.status_code == 200
    assert response.json()["username"] == "test_user"
    
    # 4. Clean up overrides after test completes
    app.dependency_overrides.clear()
```

---

## Configuring Test Databases with Pytest Fixtures

Use pytest fixtures to spin up temporary databases (like SQLite in-memory) for the duration of tests:

```python
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from main import app, get_db
from database import Base

# Setup clean, separate in-memory sqlite DB for tests
TEST_DB_URL = "sqlite+aiosqlite:///:memory:"
test_engine = create_async_engine(TEST_DB_URL, echo=False)
TestSessionLocal = async_sessionmaker(
    bind=test_engine, class_=AsyncSession, expire_on_commit=False
)

@pytest.fixture(scope="function")
async def db_session():
    async with test_engine.begin() as conn:
        # Create all tables before test starts
        await conn.run_sync(Base.metadata.create_all)
        
    async with TestSessionLocal() as session:
        yield session
        await session.close()
        
    async with test_engine.begin() as conn:
        # Tear down tables after test ends
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture(scope="function")
async def client(db_session):
    # Override get_db to return our test database session
    async def override_get_db():
        yield db_session
        
    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()
```

---

## Best Practices

*   **Clean Up Overrides**: Always call `app.dependency_overrides.clear()` in tear-downs (or fixtures) to prevent test contamination.
*   **Fixture Scopes**: Use `function` scope for database fixtures to guarantee tests run with fresh, empty tables.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Running async tests without `@pytest.mark.asyncio` | Pytest fails with type errors or runs synchronously, ignoring `await` calls | Decorate async test functions with `@pytest.mark.asyncio`. |
| Forgetting to clear overrides | Bleeds mocks into other test cases, resulting in false-positive/negative tests | Run `app.dependency_overrides.clear()` in test cleanup. |

---

## Interview Points

> **📌 Interview Point 1: Why do we use HTTPX `AsyncClient` instead of `TestClient` for async routes?**
> The standard `TestClient` uses synchronous mechanisms to run the application code. While it works for many async routes (by running them in an ad-hoc loop), testing actual async operations (like background tasks or WebSocket connections) requires an `AsyncClient` to keep the event loop active.

> **📌 Interview Point 2: What is the purpose of `app.dependency_overrides`?**
> It is an internal dictionary where key-value pairs map original dependency callables to mock functions. FastAPI inspects this dictionary before executing any injection graphs.

---

## Exercises

### Exercise 1: Write a basic route test ⭐
**Task:** Given a route `/greeting` returning `{"hello": "world"}`, write a pytest case using `TestClient` to assert status code 200 and verifying output.

<details>
<summary>💡 Hint (click to reveal)</summary>
Instantiate `TestClient` and query the `/greeting` path.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
from fastapi.testclient import TestClient
from fastapi import FastAPI

app = FastAPI()

@app.get("/greeting")
def get_greeting():
    return {"hello": "world"}

def test_greeting_route():
    client = TestClient(app)
    response = client.get("/greeting")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}
```
</details>

---

## Chapter Summary

*   Use `TestClient` for basic API request testing.
*   Use `httpx.AsyncClient` + `@pytest.mark.asyncio` to test async routes.
*   Replace databases and authorization checks during testing using `app.dependency_overrides`.

---

## Previous / Next Chapter

**⬅️ [Previous: JWT Authentication & Security](./ch06-jwt-authentication.md)**

**➡️ [Next: Deployment & Production](./ch08-deployment-best-practices.md)**

---

*Chapter 7 of the FastAPI Guide | CodeShelf*
