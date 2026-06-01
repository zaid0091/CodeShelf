---
title: Mastering Server Actions in Next.js
description: Server Actions, useActionState, manual calls, Zod validation, register/login without traditional API routes
order: 11
tags: [nextjs, server-actions, forms, zod, useActionState]
---

# Section 11 — Mastering Server Actions in Next.js

> **Difficulty:** Advanced · **Time:** 90 min · **Prerequisites:** [Section 9](./ch09-authentication.md)

---

## Learning Outcome

- ✔ Define and use **Server Actions**
- ✔ Call actions from **Client Components** and **forms**
- ✔ Validate with **Zod** and handle errors with **`useActionState`**

---

## What are Server Actions in Next.js?

> **Definition:** Server Actions are **async functions** that run on the server, callable from forms or client code — no separate API route file needed.

```jsx
// app/actions/todo.js
'use server';

import { revalidatePath } from 'next/cache';
import { connectDB } from '@/lib/db';
import { Todo } from '@/models/Todo';

export async function createTodo(formData) {
  const title = formData.get('title');
  await connectDB();
  await Todo.create({ title });
  revalidatePath('/todos');
}
```

```jsx
// app/todos/page.js

import { createTodo } from '@/app/actions/todo';

export default function TodosPage() {
  return (
    <form action={createTodo}>
      <input name="title" required />
      <button type="submit">Add</button>
    </form>
  );
}
```

---

## Using Server Actions in Client Component

```jsx
'use client';

import { createTodo } from '@/app/actions/todo';

export function TodoForm() {
  return (
    <form action={createTodo}>
      <input name="title" />
      <button type="submit">Add</button>
    </form>
  );
}
```

---

## Understanding useActionState Hook

Returns **state** and **formAction** for showing errors and pending UI.

```jsx
'use client';

import { useActionState } from 'react';
import { registerUser } from '@/app/actions/auth';

export function RegisterForm() {
  const [state, formAction, pending] = useActionState(registerUser, null);

  return (
    <form action={formAction}>
      <input name="email" type="email" required />
      <input name="password" type="password" required />
      {state?.error && <p className="error">{state.error}</p>}
      <button disabled={pending}>{pending ? 'Saving...' : 'Register'}</button>
    </form>
  );
}
```

```jsx
// app/actions/auth.js
'use server';

export async function registerUser(prevState, formData) {
  const email = formData.get('email');
  // validate, create user...
  if (error) return { error: 'Email already exists' };
  return { success: true };
}
```

---

## Calling Server Action Manually

```jsx
'use client';

import { deleteTodo } from '@/app/actions/todo';

export function DeleteButton({ id }) {
  return (
    <button onClick={() => deleteTodo(id)}>Delete</button>
  );
}
```

```jsx
'use server';

export async function deleteTodo(id) {
  await Todo.findByIdAndDelete(id);
  revalidatePath('/todos');
}
```

---

## Form Validation with Zod

```bash
npm install zod
```

```jsx
'use server';

import { z } from 'zod';

const RegisterSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
});

export async function registerUser(prevState, formData) {
  const parsed = RegisterSchema.safeParse({
    email: formData.get('email'),
    password: formData.get('password'),
  });

  if (!parsed.success) {
    return { error: parsed.error.flatten().fieldErrors };
  }

  // create user...
}
```

---

## Adding Register Feature Using Server Action

Combine Zod + bcrypt + cookie (same logic as Section 9 API, but in one action).

```jsx
'use server';

export async function registerUser(prevState, formData) {
  const result = RegisterSchema.safeParse(Object.fromEntries(formData));
  if (!result.success) return { error: 'Invalid input' };

  const hashed = await bcrypt.hash(result.data.password, 12);
  await User.create({ email: result.data.email, password: hashed });
  redirect('/login');
}
```

---

## Implementing Login Feature Using Server Action

```jsx
'use server';

export async function loginUser(prevState, formData) {
  const email = formData.get('email');
  const password = formData.get('password');
  const user = await User.findOne({ email });
  if (!user || !(await bcrypt.compare(password, user.password))) {
    return { error: 'Invalid credentials' };
  }
  cookies().set('session', await createSessionToken(user._id));
  redirect('/todos');
}
```

---

## Using Server Actions without Forms

```jsx
await incrementLike(postId);
await saveSettings({ theme: 'dark' });
```

Any server function marked `'use server'` can be imported and awaited from client event handlers.

---

## Summary

- ✔ **`'use server'`** marks actions · use **`revalidatePath`** after mutations
- ✔ **`useActionState`** for form feedback
- ✔ **Zod** for validation · actions replace many Route Handlers for forms

| ← Previous | Next → |
|------------|--------|
| [Deployment](./ch10-deployment-and-production.md) | [Advanced Features](./ch12-advanced-features.md) |
