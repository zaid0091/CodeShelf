---
title: Hooks Deep Dive
description: useRef, useMemo, useCallback, custom hooks, and rules of hooks.
order: 6
tags: [react, hooks, useRef, useMemo, useCallback, custom-hooks]
---

# Chapter 6: Hooks Deep Dive

## 6.1 Rules of Hooks

All hooks must follow two rules:

1. **Only call hooks at the top level** — not inside loops, conditions, or nested functions.
2. **Only call hooks from React functions** — components or custom hooks.

```jsx
// ❌ Conditional hook
if (loggedIn) {
  useEffect(() => { ... }, []);
}

// ✅ Hook always runs
useEffect(() => {
  if (loggedIn) { ... }
}, [loggedIn]);
```

React relies on call order to associate state with each hook instance.

## 6.2 useRef

`useRef` returns a mutable object `{ current: value }` that **persists across renders** without causing re-renders when updated.

```jsx
import { useRef } from 'react';

function TextInput() {
  const inputRef = useRef(null);

  function focusInput() {
    inputRef.current?.focus();
  }

  return (
    <>
      <input ref={inputRef} type="text" />
      <button onClick={focusInput}>Focus</button>
    </>
  );
}
```

### useRef use cases

| Use case | Example |
|----------|---------|
| DOM access | Focus, scroll, measure element |
| Mutable instance value | Previous prop, timer id |
| Avoid stale closure | Store latest callback in ref |

### Storing previous value

```jsx
function usePrevious(value) {
  const ref = useRef();
  useEffect(() => {
    ref.current = value;
  });
  return ref.current;
}
```

### Ref vs state

| | `useState` | `useRef` |
|---|-----------|----------|
| Update triggers re-render | Yes | No |
| Value in JSX | Yes | Usually no |
| Persist across renders | Yes | Yes |

## 6.3 useMemo

`useMemo` **caches a computed value** between renders when dependencies unchanged.

```jsx
import { useMemo } from 'react';

function ProductList({ products, sortBy }) {
  const sorted = useMemo(() => {
    return [...products].sort((a, b) => a[sortBy] - b[sortBy]);
  }, [products, sortBy]);

  return (
    <ul>
      {sorted.map(p => (
        <li key={p.id}>{p.name}</li>
      ))}
    </ul>
  );
}
```

### When to use useMemo

- Expensive calculations (large arrays, complex filtering)
- Referential equality needed for child `memo` optimization
- **Not** for every simple expression — adds overhead

```jsx
// Usually unnecessary
const doubled = useMemo(() => count * 2, [count]);

// Fine without memo
const doubled = count * 2;
```

## 6.4 useCallback

`useCallback` **caches a function reference** between renders.

```jsx
import { useCallback, useState } from 'react';

function TodoList({ todos, onToggle }) {
  return (
    <ul>
      {todos.map(todo => (
        <TodoItem key={todo.id} todo={todo} onToggle={onToggle} />
      ))}
    </ul>
  );
}

function App() {
  const [todos, setTodos] = useState([]);

  const handleToggle = useCallback((id) => {
    setTodos(prev =>
      prev.map(t => t.id === id ? { ...t, done: !t.done } : t)
    );
  }, []);

  return <TodoList todos={todos} onToggle={handleToggle} />;
}
```

### useCallback vs useMemo

```jsx
const memoizedValue = useMemo(() => compute(a, b), [a, b]);
const memoizedFn = useCallback(() => doSomething(a, b), [a, b]);

// Equivalent:
const memoizedFn = useMemo(() => () => doSomething(a, b), [a, b]);
```

Use `useCallback` when passing callbacks to optimized child components wrapped in `React.memo`.

## 6.5 Custom hooks

A **custom hook** extracts reusable stateful logic. Name must start with `use`.

```jsx
function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    const stored = localStorage.getItem(key);
    return stored ? JSON.parse(stored) : initialValue;
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue];
}

// Usage
function Settings() {
  const [theme, setTheme] = useLocalStorage('theme', 'light');
  return (
    <button onClick={() => setTheme(t => t === 'light' ? 'dark' : 'light')}>
      Toggle theme ({theme})
    </button>
  );
}
```

### useFetch custom hook

```jsx
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);

    fetch(url)
      .then(res => {
        if (!res.ok) throw new Error(res.statusText);
        return res.json();
      })
      .then(json => {
        if (!cancelled) setData(json);
      })
      .catch(err => {
        if (!cancelled) setError(err);
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });

    return () => { cancelled = true; };
  }, [url]);

  return { data, loading, error };
}
```

See [Chapter 10](./ch10-data-fetching.md) for production data patterns.

## 6.6 Hook composition patterns

| Custom hook | Encapsulates |
|-------------|--------------|
| `useToggle` | Boolean state + toggle function |
| `useDebounce` | Delayed value updates for search |
| `useMediaQuery` | Responsive breakpoint matching |
| `useOnClickOutside` | Close dropdown on outside click |

```jsx
function useToggle(initial = false) {
  const [on, setOn] = useState(initial);
  const toggle = useCallback(() => setOn(v => !v), []);
  return [on, toggle];
}
```

## 6.7 Debugging hooks

- React DevTools shows hook state per component
- Log dependency changes when effects fire unexpectedly
- Prefer extracting complex logic into named custom hooks for testability

## Exercises

1. **useRef focus** — Build a form where "Edit" button focuses the first invalid field.
2. **useMemo** — Filter/sort 1000+ items; compare with and without `useMemo` in DevTools Profiler.
3. **useCallback** — Memoize `onDelete` passed to list items; wrap items in `memo`.
4. **Custom hook** — Write `useWindowSize()` returning `{ width, height }`.

## Summary

| Hook | Purpose |
|------|---------|
| `useRef` | Mutable box; DOM refs; no re-render |
| `useMemo` | Cache expensive computed values |
| `useCallback` | Cache function references |
| Custom hooks | Reuse stateful logic across components |

## Next chapter

Continue to [Chapter 7: Context API](./ch07-context-api.md).
