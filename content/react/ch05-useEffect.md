---
title: useEffect
description: Side effects in React, useEffect hook, cleanup functions, and dependency array rules.
order: 5
tags: [react, useEffect, side-effects, cleanup, dependencies]
---

# Chapter 5: useEffect

## 5.1 What are side effects?

A **side effect** is anything that touches the outside world or happens outside the normal render flow.

| Side effect examples | Not side effects |
|---------------------|------------------|
| Fetching data | Computing derived values |
| Subscribing to WebSocket | Rendering JSX from props |
| Setting `document.title` | Event handlers (usually) |
| Timers (`setInterval`) | Updating state from events |
| Syncing with localStorage | |

> **Definition:** `useEffect` lets you run code **after** React commits changes to the DOM.

## 5.2 Basic syntax

```jsx
import { useState, useEffect } from 'react';

function Page({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(setUser);
  }, [userId]);

  if (!user) return <p>Loading...</p>;
  return <h1>{user.name}</h1>;
}
```

### Anatomy of useEffect

```jsx
useEffect(() => {
  // Effect body — runs after paint
  return () => {
    // Optional cleanup — runs before next effect or unmount
  };
}, [dependency1, dependency2]);
```

| Part | Purpose |
|------|---------|
| Effect function | Code to run after render |
| Cleanup function | Undo subscriptions, timers, listeners |
| Dependency array | Controls when effect re-runs |

## 5.3 Dependency array rules

### No array — runs every render (rarely needed)

```jsx
useEffect(() => {
  console.log('Runs after every render');
});
```

### Empty array `[]` — runs once on mount

```jsx
useEffect(() => {
  document.title = 'My App';
}, []);
```

### With dependencies — runs when deps change

```jsx
useEffect(() => {
  localStorage.setItem('theme', theme);
}, [theme]);
```

### ESLint exhaustive-deps

Always include every value from the component scope that the effect reads. The `react-hooks/exhaustive-deps` rule helps catch missing dependencies.

## 5.4 Cleanup examples

### Event listener

```jsx
useEffect(() => {
  function handleResize() {
    setWidth(window.innerWidth);
  }
  window.addEventListener('resize', handleResize);
  return () => window.removeEventListener('resize', handleResize);
}, []);
```

### Timer

```jsx
useEffect(() => {
  const id = setInterval(() => setSeconds(s => s + 1), 1000);
  return () => clearInterval(id);
}, []);
```

### Abort fetch on unmount

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch(url, { signal: controller.signal })
    .then(res => res.json())
    .then(setData)
    .catch(err => {
      if (err.name !== 'AbortError') setError(err);
    });

  return () => controller.abort();
}, [url]);
```

## 5.5 Common patterns

### Sync document title

```jsx
useEffect(() => {
  document.title = `${count} notifications`;
}, [count]);
```

### Load from localStorage on mount

```jsx
const [settings, setSettings] = useState(() => {
  const saved = localStorage.getItem('settings');
  return saved ? JSON.parse(saved) : defaultSettings;
});

useEffect(() => {
  localStorage.setItem('settings', JSON.stringify(settings));
}, [settings]);
```

### Fetch when id changes

```jsx
useEffect(() => {
  let cancelled = false;

  async function loadPost() {
    setLoading(true);
    const res = await fetch(`/api/posts/${postId}`);
    const data = await res.json();
    if (!cancelled) {
      setPost(data);
      setLoading(false);
    }
  }

  loadPost();
  return () => { cancelled = true; };
}, [postId]);
```

## 5.6 useEffect vs event handlers

| useEffect | Event handler |
|-----------|---------------|
| Runs after render | Runs on user action |
| Sync with external systems | Update state directly |
| Can cause extra network calls if deps wrong | Explicit, on-demand |

**Do not** put data fetching in an effect if it should only happen on button click — use the handler instead.

## 5.7 Strict Mode double invocation

In development, React Strict Mode runs effects twice to surface missing cleanup bugs. Your cleanup must be idempotent.

```jsx
// ✅ Proper cleanup handles double mount
useEffect(() => {
  const sub = subscribe();
  return () => sub.unsubscribe();
}, []);
```

## 5.8 When NOT to use useEffect

```jsx
// ❌ Deriving state in effect
useEffect(() => {
  setFullName(firstName + ' ' + lastName);
}, [firstName, lastName]);

// ✅ Compute during render
const fullName = `${firstName} ${lastName}`;
```

Avoid effects for:

- Transforming data for display
- Handling user events (use handlers)
- Chaining state updates that can be one update

## 5.9 Effect timing: useLayoutEffect (brief)

`useLayoutEffect` fires **before** the browser paints. Use sparingly for DOM measurements that must happen before paint to avoid flicker. Default to `useEffect`.

## Exercises

1. **Document title** — Update `document.title` with the current route or page name.
2. **Clock** — Display live time with `setInterval`; clean up on unmount.
3. **Fetch user** — Load user profile when `userId` prop changes; show loading state.
4. **Theme persist** — Save dark/light theme to `localStorage` and restore on refresh.

## Summary

| Topic | Key point |
|-------|-----------|
| Side effects | External sync: fetch, timers, subscriptions |
| `useEffect(fn, deps)` | Runs after render; deps control re-runs |
| Cleanup | Return function to avoid leaks |
| `[]` | Mount-only; `[x]` when `x` changes |
| Avoid | Deriving state that can be computed in render |

## Next chapter

Continue to [Chapter 6: Hooks Deep Dive](./ch06-hooks-deep-dive.md).
