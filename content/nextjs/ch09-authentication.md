---
title: Mastering Authentication in Next.js
description: Register, login, cookies, sessions, protected API routes, signed cookies, bcrypt, profile, and logout
order: 9
tags: [nextjs, authentication, cookies, session, bcrypt]
---

# Section 9 — Mastering Authentication in Next.js

> **Difficulty:** Advanced · **Time:** 120 min · **Prerequisites:** [Section 8](./ch08-mongodb-in-nextjs.md)

---

## Learning Outcome

- ✔ Implement **register** and **login** flows
- ✔ Work with **cookies** and **sessions**
- ✔ **Protect** API routes with reusable helpers
- ✔ **Hash passwords** with bcrypt

---

## Understanding Auth Flow in Next.js

```text
Register → hash password → save user in DB
Login    → verify password → create session cookie
Request  → read cookie → attach user to request
Logout   → clear cookie
```

Auth runs on the **server** (Route Handlers, Server Actions, middleware).

---

## Implementing Register User in Next.js

```bash
npm install bcryptjs
```

```jsx
// app/api/auth/register/route.js

import { connectDB } from '@/lib/db';
import { User } from '@/models/User';
import bcrypt from 'bcryptjs';

export async function POST(request) {
  await connectDB();
  const { name, email, password } = await request.json();

  const exists = await User.findOne({ email });
  if (exists) {
    return Response.json({ error: 'Email taken' }, { status: 400 });
  }

  const hashed = await bcrypt.hash(password, 12);
  const user = await User.create({ name, email, password: hashed });

  return Response.json({ id: user._id, email: user.email }, { status: 201 });
}
```

---

## Working With Cookies in Next.js

```jsx
import { cookies } from 'next/headers';

export async function GET() {
  const cookieStore = cookies();
  const token = cookieStore.get('session')?.value;
  // verify token...
}
```

Set a cookie in a Route Handler:

```jsx
import { cookies } from 'next/headers';

cookies().set('session', token, {
  httpOnly: true,
  secure: process.env.NODE_ENV === 'production',
  sameSite: 'lax',
  path: '/',
  maxAge: 60 * 60 * 24 * 7, // 7 days
});
```

---

## Implementing Login User in Next.js

```jsx
// app/api/auth/login/route.js

import bcrypt from 'bcryptjs';
import { createSessionToken } from '@/lib/auth';

export async function POST(request) {
  const { email, password } = await request.json();
  const user = await User.findOne({ email });
  if (!user) {
    return Response.json({ error: 'Invalid credentials' }, { status: 401 });
  }

  const valid = await bcrypt.compare(password, user.password);
  if (!valid) {
    return Response.json({ error: 'Invalid credentials' }, { status: 401 });
  }

  const token = await createSessionToken(user._id.toString());
  cookies().set('session', token, { httpOnly: true, /* ... */ });

  return Response.json({ success: true });
}
```

---

## Protecting Todo Endpoints With Reusable Functions

```js
// lib/auth.js

import { cookies } from 'next/headers';
import { verifySessionToken } from './jwt';

export async function getCurrentUser() {
  const token = cookies().get('session')?.value;
  if (!token) return null;
  return verifySessionToken(token);
}

export async function requireUser() {
  const user = await getCurrentUser();
  if (!user) throw new Error('Unauthorized');
  return user;
}
```

```jsx
// app/api/todos/route.js

export async function GET() {
  const user = await requireUser();
  const todos = await Todo.find({ userId: user.id });
  return Response.json(todos);
}
```

---

## Signing Cookies in Next.js

Use **signed** or **encrypted** tokens (JWT or `iron-session`) so users cannot forge session data.

```bash
npm install jose
```

```js
import { SignJWT, jwtVerify } from 'jose';

const secret = new TextEncoder().encode(process.env.JWT_SECRET);

export async function createSessionToken(userId) {
  return new SignJWT({ userId })
    .setProtectedHeader({ alg: 'HS256' })
    .setExpirationTime('7d')
    .sign(secret);
}

export async function verifySessionToken(token) {
  const { payload } = await jwtVerify(token, secret);
  return payload;
}
```

---

## Session Based Authentication in Next.js

**Session auth** = server identifies user via **cookie** on each request.

| Approach | Pros |
|----------|------|
| JWT in httpOnly cookie | Stateless, works on serverless |
| Database sessions | Easy revoke, more DB reads |

For learning projects, JWT in httpOnly cookie is common.

---

## Adding User Profile Feature

```jsx
// app/profile/page.js

import { getCurrentUser } from '@/lib/auth';
import { redirect } from 'next/navigation';

export default async function ProfilePage() {
  const user = await getCurrentUser();
  if (!user) redirect('/login');

  return (
    <div>
      <h1>Profile</h1>
      <p>Email: {user.email}</p>
    </div>
  );
}
```

---

## Implementing Logout Functionality

```jsx
// app/api/auth/logout/route.js

import { cookies } from 'next/headers';

export async function POST() {
  cookies().set('session', '', { maxAge: 0 });
  return Response.json({ success: true });
}
```

---

## Hashing Passwords in Next.js

| Rule | Why |
|------|-----|
| Never store plain passwords | Database leaks expose users |
| Use **bcrypt** cost 10–12 | Slow for attackers, OK for login |
| Never return password field | Use `.select('-password')` in Mongoose |

```js
const hashed = await bcrypt.hash(password, 12);
const match = await bcrypt.compare(plainPassword, hashed);
```

---

## Summary

- ✔ **Register** with hashed passwords · **Login** sets httpOnly cookie
- ✔ **`requireUser()`** protects APIs and pages
- ✔ **JWT** or session library for signed tokens

| ← Previous | Next → |
|------------|--------|
| [MongoDB](./ch08-mongodb-in-nextjs.md) | [Deployment](./ch10-deployment-and-production.md) |
