---
title: Backend Development with Next.js
description: Route Handlers for GET, POST, PUT, DELETE — build a complete Todo REST API
order: 7
tags: [nextjs, route-handlers, api, rest, todo]
---

# Section 7 — Backend Development with Next.js

> **Difficulty:** Intermediate · **Time:** 90 min · **Prerequisites:** [Section 4](./ch04-data-fetching-and-state.md)

---

## Learning Outcome

- ✔ Write backend logic with **Route Handlers** (`route.js`)
- ✔ Handle **GET, POST, PUT, DELETE**
- ✔ Read the **Request** object and return **JSON**
- ✔ Build a full **Todo API**

---

## Writing Backend Code in Next.js

Route Handlers live in **`route.js`** files (not `page.js`). They define API endpoints.

```text
app/api/todos/route.js       →  /api/todos
app/api/todos/[id]/route.js  →  /api/todos/:id
```

---

## Creating GET Route Handler in Next.js

```jsx
// app/api/todos/route.js

export async function GET() {
  const todos = [
    { id: '1', title: 'Learn Next.js', done: false },
  ];

  return Response.json(todos);
}
```

Test: `http://localhost:3000/api/todos`

---

## Dynamic Route Handler in Next.js

```jsx
// app/api/todos/[id]/route.js

export async function GET(request, { params }) {
  const { id } = params;
  const todo = await findTodo(id);

  if (!todo) {
    return Response.json({ error: 'Not found' }, { status: 404 });
  }

  return Response.json(todo);
}
```

---

## Understanding Request Object in Next.js

```jsx
export async function GET(request) {
  const { searchParams } = new URL(request.url);
  const page = searchParams.get('page') ?? '1';

  const headers = request.headers;
  const cookie = headers.get('cookie');

  return Response.json({ page });
}
```

| API | Purpose |
|-----|---------|
| `request.url` | Full URL |
| `request.json()` | Parse POST/PUT body |
| `request.headers` | Headers |
| `request.cookies` | Cookies (Next.js helper) |

---

## Handling POST Request in Next.js

```jsx
// app/api/todos/route.js

export async function POST(request) {
  const body = await request.json();
  const { title } = body;

  if (!title?.trim()) {
    return Response.json({ error: 'Title required' }, { status: 400 });
  }

  const todo = await createTodo({ title, done: false });
  return Response.json(todo, { status: 201 });
}
```

---

## Implementing Edit Todo Functionality (PUT)

```jsx
// app/api/todos/[id]/route.js

export async function PUT(request, { params }) {
  const body = await request.json();
  const updated = await updateTodo(params.id, body);

  if (!updated) {
    return Response.json({ error: 'Not found' }, { status: 404 });
  }

  return Response.json(updated);
}
```

---

## Handling DELETE Request in Next.js

```jsx
export async function DELETE(request, { params }) {
  const deleted = await deleteTodo(params.id);

  if (!deleted) {
    return Response.json({ error: 'Not found' }, { status: 404 });
  }

  return Response.json({ success: true });
}
```

---

## Integrating GET and POST Todo API (Frontend)

```jsx
'use client';

import { useEffect, useState } from 'react';

export function TodoList() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    fetch('/api/todos')
      .then((r) => r.json())
      .then(setTodos);
  }, []);

  async function addTodo(title) {
    const res = await fetch('/api/todos', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title }),
    });
    const todo = await res.json();
    setTodos((prev) => [...prev, todo]);
  }

  return (/* render todos + form */);
}
```

---

## Integrating PUT and DELETE Todo API

```jsx
async function toggleTodo(id, done) {
  await fetch(`/api/todos/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ done }),
  });
}

async function removeTodo(id) {
  await fetch(`/api/todos/${id}`, { method: 'DELETE' });
  setTodos((prev) => prev.filter((t) => t.id !== id));
}
```

> 💡 **Tip:** In production, move DB logic to a `lib/` module; keep `route.js` thin.

---

## Summary

- ✔ **`route.js`** exports `GET`, `POST`, `PUT`, `DELETE` functions
- ✔ Return **`Response.json(data, { status })`**
- ✔ Dynamic APIs use **`[id]/route.js`**

| ← Previous | Next → |
|------------|--------|
| [Styling](./ch06-styling-in-nextjs.md) | [MongoDB](./ch08-mongodb-in-nextjs.md) |
