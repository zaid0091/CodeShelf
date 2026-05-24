---
title: React Fundamentals
description: Components, JSX, props, and state
order: 1
tags: [basics, components]
---

# React Fundamentals

React is a library for building user interfaces with a component-based architecture.

## Component Basics

```jsx
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}

// Usage
<Greeting name="Alice" />
```

## JSX Rules

- Return a **single root element** (or use a Fragment `<>...</>`)
- Use **className** instead of `class`
- Use **camelCase** for event handlers: `onClick`, `onChange`
- Self-close tags: `<img />`, `<input />`

## Props

```jsx
function Button({ label, variant = "primary", onClick, disabled = false }) {
  return (
    <button
      className={`btn btn-${variant}`}
      onClick={onClick}
      disabled={disabled}
    >
      {label}
    </button>
  );
}
```

## State with useState

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
    </div>
  );
}
```

## Conditional Rendering

```jsx
{isLoggedIn ? <Dashboard /> : <Login />}
{error && <p className="error">{error}</p>}
{items.length > 0 ? (
  <ul>{items.map(item => <li key={item.id}>{item.name}</li>)}</ul>
) : (
  <p>No items found.</p>
)}
```

## Lists & Keys

Always provide a unique `key` when rendering lists:

```jsx
{users.map(user => (
  <UserCard key={user.id} user={user} />
))}
```
