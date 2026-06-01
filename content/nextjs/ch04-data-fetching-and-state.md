---
title: Data Fetching and State Management
description: Fetch data in the App Router, React Server Components, hooks, Context, and Redux integration
order: 4
tags: [nextjs, data-fetching, rsc, hooks, context, redux]
---

# Section 4 — Data Fetching and State Management

> **Difficulty:** Intermediate · **Time:** 60 min · **Prerequisites:** [Section 3](./ch03-rendering-paradigms.md)

---

## Learning Outcome

By the end of this section you will:

- ✔ Fetch data in **Server Components** with `fetch`
- ✔ Use **caching** and **revalidation** options
- ✔ Manage UI state with **hooks** and **Context**
- ✔ Integrate **Redux** when global client state is needed

---

## Data Fetching in the App Router

In Server Components, fetch **directly** in the component — no `useEffect`.

```jsx
// app/posts/page.js

async function getPosts() {
  const res = await fetch('https://jsonplaceholder.typicode.com/posts');
  if (!res.ok) throw new Error('Failed to fetch');
  return res.json();
}

export default async function PostsPage() {
  const posts = await getPosts();

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

### Caching options

```jsx
// Always fresh (no cache)
fetch(url, { cache: 'no-store' });

// Cache forever (default in many cases)
fetch(url, { cache: 'force-cache' });

// Revalidate every 60 seconds (ISR-style)
fetch(url, { next: { revalidate: 60 } });
```

| Option | Use when |
|--------|----------|
| `no-store` | Real-time dashboards, user-specific data |
| `force-cache` | Rarely changing public data |
| `revalidate: N` | Data that can be slightly stale |

---

## Fetching Server-Side Data with React Server Components

Server Components can talk to **databases** and **secrets** safely — code never ships to the browser.

```jsx
// app/todos/page.js
import { connectDB } from '@/lib/db';
import { Todo } from '@/models/Todo';

export default async function TodosPage() {
  await connectDB();
  const todos = await Todo.find().lean();

  return (
    <ul>
      {todos.map((t) => (
        <li key={t._id.toString()}>{t.title}</li>
      ))}
    </ul>
  );
}
```

> ⚠️ **Warning:** Never put database passwords in Client Components — they are visible in the JS bundle.

### Parallel fetching

```jsx
export default async function Dashboard() {
  const [users, stats] = await Promise.all([
    getUsers(),
    getStats(),
  ]);
  return <DashboardView users={users} stats={stats} />;
}
```

---

## Managing State with React Hooks and Context

**Server state** → fetch on server. **UI state** → hooks in Client Components.

```jsx
'use client';

import { useState } from 'react';

export function TodoForm({ onAdd }) {
  const [title, setTitle] = useState('');

  function handleSubmit(e) {
    e.preventDefault();
    onAdd(title);
    setTitle('');
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={title} onChange={(e) => setTitle(e.target.value)} />
      <button type="submit">Add</button>
    </form>
  );
}
```

### Context for shared client state

```jsx
'use client';

import { createContext, useContext, useState } from 'react';

const ThemeContext = createContext(null);

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  return useContext(ThemeContext);
}
```

Wrap in `app/layout.js` (Client Provider component).

---

## Integrating Third-Party Libraries (Redux)

Use Redux when many client components need the **same complex state**.

```bash
npm install @reduxjs/toolkit react-redux
```

```jsx
// lib/store.js
import { configureStore } from '@reduxjs/toolkit';
import todosReducer from './features/todos/todosSlice';

export function makeStore() {
  return configureStore({
    reducer: { todos: todosReducer },
  });
}
```

```jsx
// app/StoreProvider.jsx
'use client';

import { useRef } from 'react';
import { Provider } from 'react-redux';
import { makeStore } from '@/lib/store';

export function StoreProvider({ children }) {
  const storeRef = useRef(null);
  if (!storeRef.current) storeRef.current = makeStore();
  return <Provider store={storeRef.current}>{children}</Provider>;
}
```

> 💡 **Tip:** For many apps, **Server Components + URL search params + Context** is enough. Reach for Redux when state logic becomes hard to follow.

---

## Summary

- ✔ **Server Components** — `async` + `fetch` or DB directly
- ✔ Control freshness with **`cache`** and **`revalidate`**
- ✔ **Client state** — `useState`, Context, or Redux
- ✔ Keep secrets and DB access on the **server**

| ← Previous | Next → |
|------------|--------|
| [Rendering](./ch03-rendering-paradigms.md) | [Error Handling](./ch05-error-handling.md) |
