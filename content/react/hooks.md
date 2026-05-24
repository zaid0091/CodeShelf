---
title: React Hooks
description: useEffect, useRef, useMemo, useCallback, and custom hooks
order: 2
tags: [hooks, advanced]
---

# React Hooks

Hooks let you use state and lifecycle features in function components.

## useEffect

Run side effects after render:

```jsx
import { useState, useEffect } from "react";

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(r => r.json())
      .then(setUser);
  }, [userId]); // re-run when userId changes

  // Cleanup (optional)
  useEffect(() => {
    const timer = setInterval(tick, 1000);
    return () => clearInterval(timer); // cleanup on unmount
  }, []);
}
```

## useRef

Persist values across renders without causing re-renders:

```jsx
const inputRef = useRef(null);

const focusInput = () => inputRef.current?.focus();

return <input ref={inputRef} />;
```

## useMemo & useCallback

```jsx
// Memoize expensive computations
const sorted = useMemo(() => items.sort((a, b) => a - b), [items]);

// Memoize callback references (useful with React.memo)
const handleClick = useCallback(() => {
  doSomething(id);
}, [id]);
```

## Custom Hooks

Extract reusable logic:

```jsx
function useLocalStorage(key, initial) {
  const [value, setValue] = useState(() => {
    const stored = localStorage.getItem(key);
    return stored ? JSON.parse(stored) : initial;
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue];
}
```

## Rules of Hooks

1. Only call hooks at the **top level** (not inside loops/conditions)
2. Only call hooks from **React function components** or custom hooks
