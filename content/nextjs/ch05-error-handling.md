---
title: Error Handling in Next.js
description: error.js, recovery without reload, nested errors, client exceptions, and global-error.js
order: 5
tags: [nextjs, error-handling, error-boundary]
---

# Section 5 — Error Handling in Next.js

> **Difficulty:** Intermediate · **Time:** 45 min · **Prerequisites:** [Section 4](./ch04-data-fetching-and-state.md)

---

## Learning Outcome

- ✔ Use **`error.js`** as a route-level error boundary
- ✔ **Recover** from errors without a hard reload
- ✔ Handle errors in **nested routes** and **client components**
- ✔ Set up **`global-error.js`** for root failures

---

## Error Handling with error.js File

`error.js` wraps a route segment and catches errors in **child** `page.js` or layouts.

```jsx
// app/dashboard/error.js
'use client'; // required

export default function Error({ error, reset }) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <p>{error.message}</p>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
}
```

> ⚠️ **Warning:** `error.js` **must** be a Client Component (`'use client'`).

---

## How to Recover from Errors Without Hard Reload?

The **`reset()`** function re-renders the segment that failed — like trying the route again without refreshing the whole browser tab.

```jsx
<button onClick={() => reset()}>Try again</button>
```

Use this after:

- Failed fetch that might succeed on retry
- Transient API errors
- User-fixed validation issues

---

## Error Handling in Nested Routes

Errors **bubble up** to the nearest `error.js` parent.

```text
app/dashboard/error.js        ← catches errors in /dashboard/*
app/dashboard/settings/page.js
```

If `settings/page.js` throws, `dashboard/error.js` handles it — not the root (unless no closer boundary exists).

Create **granular** boundaries for better UX:

```text
app/shop/error.js
app/shop/checkout/error.js   ← checkout-specific message
```

---

## Handling Client Side Exceptions

Use **try/catch** in event handlers and **`error boundaries`** for render errors.

```jsx
'use client';

export function SaveButton() {
  async function handleSave() {
    try {
      await saveTodo();
    } catch (err) {
      alert(err.message);
    }
  }
  return <button onClick={handleSave}>Save</button>;
}
```

For render-time errors in client trees, `error.js` still applies at the route level.

---

## Global Error Handling in Next.js

When the **root layout** fails, use `global-error.js` at `app/`:

```jsx
// app/global-error.js
'use client';

export default function GlobalError({ error, reset }) {
  return (
    <html>
      <body>
        <h1>Application error</h1>
        <p>{error.message}</p>
        <button onClick={() => reset()}>Try again</button>
      </body>
    </html>
  );
}
```

Must include its own `<html>` and `<body>` because root layout is replaced.

---

## Summary

- ✔ **`error.js`** + **`reset()`** for graceful recovery
- ✔ Errors bubble to the **nearest** boundary
- ✔ **`global-error.js`** for catastrophic root failures

| ← Previous | Next → |
|------------|--------|
| [Data Fetching](./ch04-data-fetching-and-state.md) | [Styling](./ch06-styling-in-nextjs.md) |
