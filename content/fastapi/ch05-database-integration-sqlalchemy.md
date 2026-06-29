---
title: Database Integration (SQLAlchemy)
description: Learn how to integrate FastAPI with databases using SQLAlchemy. Write async models, manage sessions with dependency injection, and set up migrations using Alembic.
order: 5
tags: [fastapi, sqlalchemy, database, async, migrations, alembic]
---

# Chapter 5: Database Integration (SQLAlchemy)

> **Learn how to connect FastAPI to a SQL database, define models, manage asynchronous database sessions using dependency injection, and perform migrations with Alembic.**

---

## Table of Contents

1. [Asynchronous Database Operations](#asynchronous-database-operations)
2. [Setting Up SQLAlchemy (Async Engine & Session)](#setting-up-sqlalchemy-async-engine--session)
3. [Declaring SQLAlchemy Models](#declaring-sqlalchemy-models)
4. [Creating the Database Session Dependency](#creating-the-database-session-dependency)
5. [Integrating Pydantic and SQLAlchemy](#integrating-pydantic-and-sqlalchemy)
6. [Writing CRUD Endpoints](#writing-crud-endpoints)
7. [Database Migrations with Alembic](#database-migrations-with-alembic)
8. [Best Practices](#best-practices)
9. [Common Mistakes](#common-mistakes)
10. [Interview Points](#interview-points)
11. [Exercises](#exercises)
12. [Chapter Summary](#chapter-summary)

---

## Asynchronous Database Operations

In high-concurrency systems, blocking database operations freeze the event loop. Utilizing async database drivers (`asyncpg` for PostgreSQL, `aiosqlite` for SQLite) with SQLAlchemy ensures that the thread pool remains unblocked while queries execute.

---

## Setting Up SQLAlchemy (Async Engine & Session)

Create a `database.py` file to handle connections:

```python
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

# SQLite async connection URL (requires aiosqlite package)
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Create the async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create session factory
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Declarative Base for models
Base = declarative_base()
```

---

## Declaring SQLAlchemy Models

Create a `models.py` file:

```python
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class DBUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
```

---

## Creating the Database Session Dependency

Create a database session dependency in your routes file (e.g., `main.py`):

```python
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from database import SessionLocal

# This dependency yields a session and guarantees it gets closed
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
```

---

## Integrating Pydantic and SQLAlchemy

To serialize database model outputs directly into Pydantic models, configure the Pydantic schema to read fields from ORM attributes:

```python
from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    is_active: bool

    # Enable ORM compatibility in Pydantic v2
    model_config = ConfigDict(from_attributes=True)
```

---

## Writing CRUD Endpoints

Write async API operations using SQLAlchemy's async API commands:

```python
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import DBUser
from database import get_db
import schemas # assuming the Pydantic classes are inside schemas.py

app = FastAPI()

@app.post("/users/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    # Check if user already exists
    query = select(DBUser).where(DBUser.username == user.username)
    result = await db.execute(query)
    existing_user = result.scalars().first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
        
    db_user = DBUser(username=user.username, email=user.email)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", response_model=schemas.UserResponse)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    query = select(DBUser).where(DBUser.id == user_id)
    result = await db.execute(query)
    db_user = result.scalars().first()
    
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
```

---

## Database Migrations with Alembic

In production, you should never run code that alters database schemas on startup. Use Alembic to manage database changes iteratively.

```bash
# 1. Install alembic
pip install alembic

# 2. Initialize Alembic inside project
alembic init alembic

# 3. Inside alembic.ini, set connection url:
# sqlalchemy.url = sqlite+aiosqlite:///./test.db

# 4. Inside alembic/env.py, import models and set target_metadata:
# from models import Base
# target_metadata = Base.metadata

# 5. Create an initial migration script
alembic revision --autogenerate -m "Initial tables"

# 6. Apply migration to database
alembic upgrade head
```

---

## Best Practices

*   **Avoid `expire_on_commit=True`**: In asynchronous mode, expire attributes can trigger unwanted lazy-loads, throwing errors since fetching is non-blocking. Set `expire_on_commit=False` when creating the session factory.
*   **Write migrations**: Always use Alembic for production databases. Do not use `Base.metadata.create_all()` in production code.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Running synchronous engine drivers (e.g. `sqlite:///`) in async code | Blocks the entire execution queue of FastAPI | Use async drivers (`sqlite+aiosqlite:///` or `postgresql+asyncpg:///`) and use `create_async_engine`. |
| Modifying database outside transactions | Data integrity issues and query locks | Always use `await db.commit()` within `try` blocks and roll back if errors occur. |

---

## Interview Points

> **📌 Interview Point 1: What is the purpose of `from_attributes=True` in Pydantic?**
> In Pydantic v2 (previously `orm_mode = True` in v1), this setting allows Pydantic to read properties from database objects (ORM instances) that contain attribute accessors instead of standard dictionary lookups (`obj.username` vs `obj["username"]`).

> **📌 Interview Point 2: Why do we use `select()` instead of `.query` in SQLAlchemy 2.0?**
> SQLAlchemy 2.0 deprecated the `.query` syntax in favor of the cleaner, functional `select()` statements, which align better with async engine architectures.

---

## Exercises

### Exercise 1: Create an Async CRUD route for deleting users ⭐
**Task:** Write a DELETE endpoint `/users/{user_id}` that finds a database user by ID and removes them. Return `{"detail": "User deleted"}` upon success.

<details>
<summary>💡 Hint (click to reveal)</summary>
Retrieve the user using `select()`, and if found, call `await db.delete(db_user)` followed by `await db.commit()`.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
@app.delete("/users/{user_id}", status_code=200)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    query = select(DBUser).where(DBUser.id == user_id)
    result = await db.execute(query)
    db_user = result.scalars().first()
    
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
        
    await db.delete(db_user)
    await db.commit()
    return {"detail": "User deleted"}
```
</details>

---

## Chapter Summary

*   Use `sqlalchemy.ext.asyncio` for non-blocking database queries.
*   Yield database sessions inside dependencies for safe transactional scopes and resource closing.
*   Manage schema revisions in production using Alembic commands.

---

## Previous / Next Chapter

**⬅️ [Previous: Dependency Injection](./ch04-dependency-injection.md)**

**➡️ [Next: JWT Authentication & Security](./ch06-jwt-authentication.md)**

---

*Chapter 5 of the FastAPI Guide | CodeShelf*
