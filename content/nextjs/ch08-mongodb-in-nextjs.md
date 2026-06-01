---
title: Working with MongoDB in Next.js
description: Connect MongoDB, create Mongoose models, and implement full CRUD for todos
order: 8
tags: [nextjs, mongodb, mongoose, database]
---

# Section 8 — Working with MongoDB in Next.js

> **Difficulty:** Intermediate · **Time:** 60 min · **Prerequisites:** [Section 7](./ch07-backend-route-handlers.md)

---

## Learning Outcome

- ✔ **Connect** MongoDB in a Next.js app
- ✔ Define **Mongoose models**
- ✔ Perform **Create, Read, Update, Delete** from Route Handlers

---

## Connecting MongoDB in Next.js

Use **MongoDB Atlas** (free tier) or local MongoDB. Store the URI in `.env.local`:

```env
MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/mydb
```

```bash
npm install mongoose
```

```js
// lib/db.js

import mongoose from 'mongoose';

const MONGODB_URI = process.env.MONGODB_URI;

if (!MONGODB_URI) {
  throw new Error('Please define MONGODB_URI in .env.local');
}

let cached = global.mongoose;

if (!cached) {
  cached = global.mongoose = { conn: null, promise: null };
}

export async function connectDB() {
  if (cached.conn) return cached.conn;

  if (!cached.promise) {
    cached.promise = mongoose.connect(MONGODB_URI).then((m) => m);
  }

  cached.conn = await cached.promise;
  return cached.conn;
}
```

> 💡 **Tip:** Caching the connection prevents **too many connections** during hot reload in dev.

---

## Creating Mongoose Model in Next.js

```js
// models/Todo.js

import mongoose from 'mongoose';

const TodoSchema = new mongoose.Schema(
  {
    title: { type: String, required: true },
    done: { type: Boolean, default: false },
    userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  },
  { timestamps: true }
);

export const Todo = mongoose.models.Todo || mongoose.model('Todo', TodoSchema);
```

```js
// models/User.js

const UserSchema = new mongoose.Schema({
  name: String,
  email: { type: String, unique: true },
  password: String,
});

export const User = mongoose.models.User || mongoose.model('User', UserSchema);
```

---

## MongoDB CRUD: Create and Read

```jsx
// app/api/todos/route.js

import { connectDB } from '@/lib/db';
import { Todo } from '@/models/Todo';

export async function GET() {
  await connectDB();
  const todos = await Todo.find().sort({ createdAt: -1 });
  return Response.json(todos);
}

export async function POST(request) {
  await connectDB();
  const { title } = await request.json();
  const todo = await Todo.create({ title });
  return Response.json(todo, { status: 201 });
}
```

---

## MongoDB CRUD: Update and Delete

```jsx
// app/api/todos/[id]/route.js

import { connectDB } from '@/lib/db';
import { Todo } from '@/models/Todo';

export async function PUT(request, { params }) {
  await connectDB();
  const body = await request.json();
  const todo = await Todo.findByIdAndUpdate(params.id, body, { new: true });
  if (!todo) return Response.json({ error: 'Not found' }, { status: 404 });
  return Response.json(todo);
}

export async function DELETE(request, { params }) {
  await connectDB();
  const todo = await Todo.findByIdAndDelete(params.id);
  if (!todo) return Response.json({ error: 'Not found' }, { status: 404 });
  return Response.json({ success: true });
}
```

---

## Common Mistakes

- ❌ Committing `.env.local` to git — add to `.gitignore`
- ❌ Creating a new mongoose connection on every request without caching
- ❌ Forgetting `await connectDB()` before queries

---

## Summary

- ✔ **`connectDB()`** with cached connection for serverless safety
- ✔ **Mongoose models** in `models/`
- ✔ Route Handlers call **`Todo.create`**, **`find`**, **`findByIdAndUpdate`**, **`findByIdAndDelete`**

| ← Previous | Next → |
|------------|--------|
| [Route Handlers](./ch07-backend-route-handlers.md) | [Authentication](./ch09-authentication.md) |
