---
title: Routing in Next.js
description: App Router, layouts, nested routes, dynamic and catch-all routes, metadata, 404, route groups, and private routes
order: 2
tags: [nextjs, routing, app-router, layouts, metadata]
---

# Section 2 — Routing in Next.js

> **Difficulty:** Beginner–Intermediate · **Time:** 90–120 min · **Prerequisites:** [Section 1](./ch01-introduction-to-nextjs.md)

---

## Learning Outcome

By the end of this section you will:

- ✔ Create routes with the **App Router**
- ✔ Use **`layout.js`** and **`page.js`** correctly
- ✔ Build **nested**, **dynamic**, and **catch-all** routes
- ✔ Add **metadata**, custom **404**, **route groups**, and **private routes**

---

## Creating Routes with the App Router

> **Rule:** In the `app/` folder, each **`page.js`** file creates a **public URL**.

```text
app/page.js              →  /
app/about/page.js        →  /about
app/blog/page.js         →  /blog
app/blog/[slug]/page.js  →  /blog/anything
```

```jsx
// app/about/page.js

export default function AboutPage() {
  return <h1>About us</h1>;
}
```

Navigate with **`Link`** (no full page reload):

```jsx
import Link from 'next/link';

<Link href="/about">About</Link>
```

---

## Understanding Layouts: layout.js and page.js

| File | Role |
|------|------|
| **`page.js`** | Unique UI for that URL — **required** for a route to exist |
| **`layout.js`** | Shared UI that **wraps** child routes — persists on navigation |

```jsx
// app/layout.js — root layout (required once)

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <header>My Site</header>
        {children}
        <footer>© 2026</footer>
      </body>
    </html>
  );
}
```

```jsx
// app/page.js

export default function Home() {
  return <h1>Home</h1>;
}
```

> ⚠️ **Warning:** Root layout must include `<html>` and `<body>` tags.

---

## Nested Routing with App Router

Nested folders = nested URLs **and** nested layouts.

```text
app/dashboard/layout.js     ← wraps all /dashboard/*
app/dashboard/page.js       ← /dashboard
app/dashboard/settings/page.js  ← /dashboard/settings
```

```jsx
// app/dashboard/layout.js

export default function DashboardLayout({ children }) {
  return (
    <div className="dashboard">
      <aside>Sidebar</aside>
      <main>{children}</main>
    </div>
  );
}
```

When you go from `/dashboard` → `/dashboard/settings`, the **sidebar stays** — only `{children}` swaps.

---

## Dynamic Routes and Route Groups

### Dynamic routes — `[param]`

```text
app/products/[id]/page.js   →  /products/1, /products/2, ...
```

```jsx
export default function ProductPage({ params }) {
  const { id } = params;
  return <h1>Product {id}</h1>;
}
```

### Route groups — `(folder)`

Parentheses **do not** appear in the URL. Use them to organize code or share layouts.

```text
app/(marketing)/about/page.js   →  /about
app/(shop)/cart/page.js         →  /cart
```

```text
app/
├── (marketing)/
│   ├── layout.js      ← marketing layout
│   └── pricing/page.js
└── (shop)/
    ├── layout.js      ← shop layout
    └── products/page.js
```

---

## Catch-All and Optional Routes

| Syntax | Matches | Example |
|--------|---------|---------|
| `[...slug]` | **One or more** segments | `/docs/a/b` → `['a','b']` |
| `[[...slug]]` | **Zero or more** segments | `/docs` works too |

```jsx
// app/docs/[[...slug]]/page.js

export default function DocsPage({ params }) {
  const { slug } = params;

  if (!slug) return <h1>Docs Home</h1>;

  return <h1>Page: {slug.join('/')}</h1>;
}
```

> 💡 **Tip:** `slug` is an **array**, not a string. Use `slug.join('/')` to display the path.

---

## Building Reusable Layouts using layout.js

Extract shared chrome once; every child route inherits it.

```jsx
// app/(main)/layout.js

import { Navbar } from '@/components/Navbar';

export default function MainLayout({ children }) {
  return (
    <>
      <Navbar />
      <div className="container">{children}</div>
    </>
  );
}
```

**Nested layouts** stack — root layout wraps dashboard layout wraps page.

---

## Metadata API in Next.js

SEO titles and descriptions without `<head>` in every file.

### Static metadata

```jsx
// app/about/page.js

export const metadata = {
  title: 'About Us',
  description: 'Learn about our company',
};

export default function AboutPage() {
  return <h1>About</h1>;
}
```

### Dynamic metadata

```jsx
export async function generateMetadata({ params }) {
  const post = await getPost(params.slug);
  return {
    title: post.title,
    description: post.excerpt,
  };
}
```

### Root defaults

```jsx
// app/layout.js

export const metadata = {
  title: { default: 'My App', template: '%s | My App' },
  description: 'Best todo app',
};
```

---

## Custom 404 Page in Next.js

```jsx
// app/not-found.js — global 404

import Link from 'next/link';

export default function NotFound() {
  return (
    <div>
      <h1>404 — Page not found</h1>
      <Link href="/">Go home</Link>
    </div>
  );
}
```

Trigger from a page when data is missing:

```jsx
import { notFound } from 'next/navigation';

export default async function PostPage({ params }) {
  const post = await getPost(params.slug);
  if (!post) notFound();
  return <article>{post.title}</article>;
}
```

Segment-specific 404: add `not-found.js` inside that folder (e.g. `app/blog/not-found.js`).

---

## What are Route Groups?

Route groups use **`(name)`** folders to:

1. **Organize** files without changing URLs
2. Apply **different layouts** to different sections
3. Keep **clean folder structure** in large apps

They are **invisible** in the browser address bar.

---

## What are Private Routes?

Folders or files starting with **`_`** are **private** — not turned into routes.

```text
app/dashboard/_components/Sidebar.jsx   ← not a URL
app/_utils/helpers.js                   ← not a URL
```

Use private folders for:

- Components only used in that section
- Utility modules
- Colocated styles

> 💡 **Tip:** This is different from **auth-protected** routes. For login walls, use middleware or server-side session checks (Section 9).

---

## Common Mistakes

- ❌ Using `<a href="/">` for internal links — use `<Link href="/">`
- ❌ Forgetting `page.js` — folder alone does not create a route
- ❌ `[...slug]` on `/blog` when `/blog` should work — use `[[...slug]]`
- ❌ Treating catch-all `slug` as a string — it's an **array**

---

## Summary

- ✔ **`page.js`** = route UI · **`layout.js`** = shared wrapper
- ✔ **`[id]`** = one dynamic segment · **`[...slug]`** = many · **`[[...slug]]`** = optional many
- ✔ **`(group)`** organizes without affecting URLs · **`_folder`** stays private
- ✔ **`metadata`** and **`not-found.js`** handle SEO and 404s

| ← Previous | Next → |
|------------|--------|
| [Introduction](./ch01-introduction-to-nextjs.md) | [Rendering Paradigms](./ch03-rendering-paradigms.md) |
