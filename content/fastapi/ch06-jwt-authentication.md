---
title: JWT Authentication & Security
description: Secure your FastAPI applications using OAuth2, JWT tokens, and password hashing. Learn how to authenticate users and build a current user dependency.
order: 6
tags: [fastapi, security, jwt, oauth2, authentication, hashing]
---

# Chapter 6: JWT Authentication & Security

> **Secure your endpoints by implementing hashing algorithms for passwords, generating JSON Web Tokens, and resolving user identities on protected routes.**

---

## Table of Contents

1. [Understanding OAuth2 and JWT](#understanding-oauth2-and-jwt)
2. [Password Hashing with Passlib](#password-hashing-with-passlib)
3. [Generating JSON Web Tokens (JWT)](#generating-json-web-tokens-jwt)
4. [Creating the OAuth2 Token Endpoint](#creating-the-oauth2-token-endpoint)
5. [Authenticating Protected Routes](#authenticating-protected-routes)
6. [Best Practices](#best-practices)
7. [Common Mistakes](#common-mistakes)
8. [Interview Points](#interview-points)
9. [Exercises](#exercises)
10. [Chapter Summary](#chapter-summary)

---

## Understanding OAuth2 and JWT

FastAPI simplifies security workflows. In typical JWT flows:
1. The client logs in with a username and password.
2. The server verifies details and sends back a signed **JWT (JSON Web Token)**.
3. The client includes this token in the header (`Authorization: Bearer <token>`) for subsequent API requests.
4. The server decodes and validates the token to identify the user.

---

## Password Hashing with Passlib

Never store plain passwords. Use `passlib` with the `bcrypt` hashing module.

```bash
pip install "passlib[bcrypt]"
```

Define security helpers inside `security.py`:

```python
from passlib.context import CryptContext

# Define crypt context to use bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
```

---

## Generating JSON Web Tokens (JWT)

Install `pyjwt` to handle tokens:

```bash
pip install pyjwt
```

Add token signing utilities to `security.py`:

```python
from datetime import datetime, timedelta, timezone
import jwt

SECRET_KEY = "super-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```

---

## Creating the OAuth2 Token Endpoint

FastAPI provides `OAuth2PasswordRequestForm` to parse form data payloads, which is standard for OAuth2 protocols.

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
import security

app = FastAPI()

# Dummy DB
users_db = {
    "alice": {
        "username": "alice",
        "hashed_password": security.get_password_hash("secret123"),
        "email": "alice@example.com"
    }
}

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not security.verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
```

---

## Authenticating Protected Routes

Create a dependency `get_current_user` that decodes headers, validates JWT payloads, and retrieves user records.

```python
from fastapi.security import OAuth2PasswordBearer
import jwt

# This class instructs FastAPI to extract the token from Authorization: Bearer <token>
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
        
    user = users_db.get(username)
    if user is None:
        raise credentials_exception
    return user

# Protect your endpoints
@app.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return {
        "username": current_user["username"],
        "email": current_user["email"]
    }
```
*When visiting `/docs`, Swagger UI will automatically display an **Authorize** button. Clicking it and authenticating allows the browser to cache the token and attach it to outgoing requests.*

---

## Best Practices

*   **Secure the Secret Key**: Store `SECRET_KEY` in environment configurations. Never commit it to git history.
*   **Set token expirations**: Keep token lifetimes short (e.g. 15–60 minutes) to prevent long-lived credentials reuse if intercepted.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Mismatch between `tokenUrl` in `OAuth2PasswordBearer` and login path | Swagger UI "Authorize" button fails to log in | Ensure `tokenUrl="token"` matches the login endpoint path (`/token`). |
| Missing expiry checks | Tokens work forever, posing major security leaks | Set `exp` timestamp in the JWT payload and decode it securely. |

---

## Interview Points

> **📌 Interview Point 1: What is the `sub` claim inside a JWT token?**
> The `sub` (Subject) claim contains the identifier of the principal (user). It is standard practice to store the user's ID or unique username in this field.

> **📌 Interview Point 2: Why do we return `{"WWW-Authenticate": "Bearer"}` headers on HTTP 401?**
> This is specified in RFC 6750. It instructs browsers and REST clients to use the Bearer scheme to submit credentials.

---

## Exercises

### Exercise 1: Write an endpoint displaying user email only ⭐
**Task:** Create a protected GET endpoint `/users/me/email` that resolves the user, but only returns `{"email": "user@example.com"}`.

<details>
<summary>💡 Hint (click to reveal)</summary>
Inject `get_current_user` as a dependency and retrieve the `"email"` key from the dictionary.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
@app.get("/users/me/email")
async def get_my_email(current_user: dict = Depends(get_current_user)):
    return {"email": current_user["email"]}
```
</details>

---

## Chapter Summary

*   Use `passlib` with `bcrypt` to securely hash and verify passwords.
*   Generate signed JWT access tokens containing username sub claims.
*   Implement `OAuth2PasswordBearer` to extract and validate tokens on protected routes.

---

## Previous / Next Chapter

**⬅️ [Previous: Database Integration (SQLAlchemy)](./ch05-database-integration-sqlalchemy.md)**

**➡️ [Next: Testing FastAPI Applications](./ch07-testing-fastapi.md)**

---

*Chapter 6 of the FastAPI Guide | CodeShelf*
