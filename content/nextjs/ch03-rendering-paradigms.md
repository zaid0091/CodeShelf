---
title: Rendering Paradigms in Next.js
description: SSR, CSR, SSG, ISR, static vs dynamic rendering, server vs client components, and hydration
order: 3
tags: [nextjs, ssr, csr, ssg, isr, hydration, server-components]
---

# Section 3 — Rendering Paradigms in Next.js

> **Difficulty:** Intermediate · **Time:** 60–75 min · **Prerequisites:** [Section 2](./ch02-routing-in-nextjs.md)

---

## Learning Outcome

By the end of this section you will:

- ✔ Explain **SSR, CSR, SSG, and ISR** in plain language
- ✔ Choose **static vs dynamic** rendering
- ✔ Use **Server** and **Client** Components correctly
- ✔ Understand **hydration** and fix common hydration errors

---

## Understanding Different Rendering Paradigms (SSR & CSR)

| Term | Full name | When HTML is built | Where JS runs |
|------|-----------|-------------------|---------------|
| **CSR** | Client-Side Rendering | In the browser | Browser |
| **SSR** | Server-Side Rendering | On each request (server) | Server + browser |
| **SSG** | Static Site Generation | At **build** time | Browser (hydrate) |
| **ISR** | Incremental Static Regeneration | Build + **revalidate** later | Browser (hydrate) |

**Simple analogy:**

- **CSR** — restaurant gives you ingredients; you cook at the table (slow first bite)
- **SSR** — kitchen cooks when you order (fresh every time)
- **SSG** — meal pre-made before doors open (fast, same for everyone until restocked)
- **ISR** — pre-made meals refreshed on a schedule

---

## Static vs Dynamic Rendering

Next.js decides per route whether HTML is **static** or **dynamic**.

| | Static | Dynamic |
|---|--------|---------|
| **When** | Build time (or revalidate) | Each request |
| **Good for** | Blogs, marketing, docs | User dashboards, personalized data |
| **Speed** | Very fast (CDN) | Depends on server |

**Forces dynamic** (examples):

```jsx
// Using cookies, headers, or searchParams in a Server Component
import { cookies } from 'next/headers';

export default async function Page() {
  const session = cookies().get('session');
  // ...
}
```

```js
// app/dashboard/page.js
export const dynamic = 'force-dynamic';
```

**Force static:**

```js
export const dynamic = 'force-static';
```

---

## Static Site Generation (SSG)

Pages built **once** at `npm run build` and served as files.

```jsx
// app/blog/[slug]/page.js

export async function generateStaticParams() {
  const posts = await fetchPosts();
  return posts.map((p) => ({ slug: p.slug }));
}

export default async function PostPage({ params }) {
  const post = await getPost(params.slug);
  return <h1>{post.title}</h1>;
}
```

All slugs from `generateStaticParams` are pre-rendered at build time.

---

## Incremental Static Regeneration (ISR)

Static pages that **refresh** after a time interval without rebuilding the whole site.

```jsx
export const revalidate = 60; // seconds

export default async function Page() {
  const data = await fetch('https://api.example.com/stats', {
    next: { revalidate: 60 },
  }).then((r) => r.json());

  return <p>Views: {data.views}</p>;
}
```

After 60 seconds, the **next visitor** triggers a background refresh.

---

## Server Side vs Client Side Components

| | Server Component (default) | Client Component |
|---|------------------------------|------------------|
| **File** | No directive | `'use client'` at top |
| **Runs on** | Server only | Server + browser |
| **Can use** | `async/await`, DB, secrets | `useState`, `useEffect`, browser APIs |
| **Ships JS?** | No (usually) | Yes |

```jsx
// Server Component — default
export default async function ProductList() {
  const products = await db.products.findMany();
  return <ul>{products.map((p) => <li key={p.id}>{p.name}</li>)}</ul>;
}
```

```jsx
'use client';

import { useState } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

> 💡 **Tip:** Keep `'use client'` at the **leaves** of your tree — small interactive islands, not the whole page.

---

## Hydration Demystified

**Hydration** = React **attaching** event listeners and state to HTML that was already sent from the server.

```text
1. Server sends HTML  →  user sees content fast
2. Browser downloads JS
3. React "hydrates"  →  buttons become clickable
```

Without hydration, server HTML is **static** — clicks on React components would not work.

---

## Why Hydration Error Comes?

Hydration errors mean **server HTML ≠ what client React expected**.

### Common causes

| Cause | Example |
|-------|---------|
| **Different content** | `Date.now()` or `Math.random()` in render |
| **Browser-only APIs** | `window`, `localStorage` in Server Component |
| **Invalid HTML nesting** | `<p>` inside `<p>`, `<div>` inside `<p>` |
| **Extra whitespace** | Extensions modifying DOM |

### Fixes

```jsx
// ❌ Bad — different every render
export default function Time() {
  return <p>{new Date().toString()}</p>;
}

// ✅ Good — client-only
'use client';
import { useEffect, useState } from 'react';

export function Time() {
  const [time, setTime] = useState(null);
  useEffect(() => setTime(new Date().toString()), []);
  if (!time) return <p>Loading...</p>;
  return <p>{time}</p>;
}
```

```jsx
// ✅ Suppress only when intentional (use sparingly)
<p suppressHydrationWarning>{new Date().getFullYear()}</p>
```

---

## Summary

- ✔ **CSR** in browser · **SSR** per request · **SSG** at build · **ISR** = SSG + revalidate
- ✔ Default = **Server Components**; add `'use client'` for interactivity
- ✔ **Hydration** wires up interactivity; mismatches cause errors

| ← Previous | Next → |
|------------|--------|
| [Routing](./ch02-routing-in-nextjs.md) | [Data Fetching](./ch04-data-fetching-and-state.md) |
