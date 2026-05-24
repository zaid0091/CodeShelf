---
title: JSX & Components
description: JSX syntax rules, expressions, props, children, default props, and component composition patterns.
order: 2
tags: [react, jsx, props, components, composition]
---

# Chapter 2: JSX & Components

## 2.1 What is JSX?

**JSX** (JavaScript XML) is a syntax extension that lets you write HTML-like markup inside JavaScript.

> **Definition:** JSX is syntactic sugar for `React.createElement()`. Browsers do not understand JSX — Vite/Babel compiles it to plain JavaScript.

```jsx
// What you write
const element = <h1 className="title">Hello</h1>;

// What the compiler produces (simplified)
const element = React.createElement('h1', { className: 'title' }, 'Hello');
```

### Why JSX?

| Benefit | Explanation |
|---------|-------------|
| Readable | UI structure looks like HTML |
| Safe | Prevents injection attacks by escaping values |
| Expressive | Mix logic and markup in one place |

## 2.2 JSX rules

### Rule 1: One root element (or Fragment)

```jsx
// ❌ Multiple roots
function Bad() {
  return (
    <h1>Title</h1>
    <p>Paragraph</p>
  );
}

// ✅ Single root
function Good() {
  return (
    <div>
      <h1>Title</h1>
      <p>Paragraph</p>
    </div>
  );
}

// ✅ Fragment — no extra DOM node
function AlsoGood() {
  return (
    <>
      <h1>Title</h1>
      <p>Paragraph</p>
    </>
  );
}
```

### Rule 2: Close all tags

```jsx
<img src="/logo.png" alt="Logo" />
<input type="text" />
<br />
```

### Rule 3: camelCase for DOM properties

| HTML | JSX |
|------|-----|
| `class` | `className` |
| `for` | `htmlFor` |
| `onclick` | `onClick` |
| `tabindex` | `tabIndex` |

### Rule 4: JavaScript expressions in `{ }`

```jsx
const name = 'Alice';
const items = ['React', 'Vite', 'JSX'];

function Profile() {
  return (
    <div>
      <h1>{name.toUpperCase()}</h1>
      <p>{2 + 2}</p>
      <p>{items.length} skills listed</p>
    </div>
  );
}
```

**You cannot use:** `if/else` statements, `for` loops, or `function` declarations directly inside `{ }`. Use ternaries, `.map()`, or compute values before the `return`.

### Rule 5: `style` is an object

```jsx
<div style={{ color: 'blue', fontSize: '18px', marginTop: 8 }}>
  Styled text
</div>
```

Note: property names are camelCase (`fontSize`, not `font-size`).

## 2.3 Components and props

**Props** (properties) are read-only inputs passed from parent to child.

```jsx
function Avatar({ src, alt, size = 48 }) {
  return (
    <img
      src={src}
      alt={alt}
      width={size}
      height={size}
      className="rounded-full"
    />
  );
}

function UserCard({ user }) {
  return (
    <article className="card">
      <Avatar src={user.avatar} alt={user.name} size={64} />
      <h2>{user.name}</h2>
      <p>{user.role}</p>
    </article>
  );
}

// Usage
<UserCard user={{ name: 'Bob', role: 'Developer', avatar: '/bob.jpg' }} />
```

### Props are immutable

Never modify props inside a child component. If you need local changes, use state (Chapter 3).

```jsx
// ❌ Wrong
function Bad({ count }) {
  count = count + 1;
  return <p>{count}</p>;
}
```

### Destructuring props

```jsx
// Inline
function Button({ label, onClick, disabled = false }) { ... }

// With rest spread for forwarding
function Input({ label, ...inputProps }) {
  return (
    <label>
      {label}
      <input {...inputProps} />
    </label>
  );
}
```

## 2.4 Children

The special prop `children` holds content placed between opening and closing tags.

```jsx
function Card({ title, children }) {
  return (
    <section className="card">
      <header><h3>{title}</h3></header>
      <div>{children}</div>
    </section>
  );
}

// Usage
<Card title="Stats">
  <p>Users: 1,240</p>
  <p>Revenue: $8,500</p>
</Card>
```

### Passing JSX as a prop

```jsx
function Layout({ sidebar, content }) {
  return (
    <div className="layout">
      <aside>{sidebar}</aside>
      <main>{content}</main>
    </div>
  );
}

<Layout
  sidebar={<Nav items={links} />}
  content={<Dashboard />}
/>
```

## 2.5 Composition vs inheritance

React favors **composition** — building complex UIs from simple components.

```jsx
function Dialog({ title, children, onClose }) {
  return (
    <div className="dialog-overlay" onClick={onClose}>
      <div className="dialog" onClick={(e) => e.stopPropagation()}>
        <h2>{title}</h2>
        {children}
      </div>
    </div>
  );
}

function ConfirmDialog({ message, onConfirm, onCancel }) {
  return (
    <Dialog title="Confirm" onClose={onCancel}>
      <p>{message}</p>
      <button onClick={onConfirm}>Yes</button>
      <button onClick={onCancel}>No</button>
    </Dialog>
  );
}
```

| Pattern | When to use |
|---------|-------------|
| **Containment** | `children` for generic wrappers (Card, Modal) |
| **Specialization** | Wrap a generic component with specific props |
| **Slot props** | Named props like `header`, `footer` for fixed regions |

## 2.6 Conditional rendering in JSX

```jsx
function StatusBadge({ status }) {
  return (
    <span className={`badge badge-${status}`}>
      {status === 'active' && '● Active'}
      {status === 'pending' && '○ Pending'}
      {status === 'error' && '✕ Error'}
    </span>
  );
}
```

See [Chapter 4](./ch04-lists-and-keys.md) for more patterns with lists and ternaries.

## 2.7 Export patterns

```jsx
// Default export — one main component per file
export default function Button() { ... }

// Named exports — multiple utilities
export function IconButton() { ... }
export function PrimaryButton() { ... }

// Import
import Button from './Button.jsx';
import { IconButton, PrimaryButton } from './Button.jsx';
```

## Exercises

1. **JSX fix** — Fix a component that uses `class`, unclosed `<img>`, and multiple root elements.
2. **UserCard** — Build `UserCard` with props: `name`, `email`, `avatarUrl`. Add default avatar when missing.
3. **Card with children** — Create a reusable `Panel` with `title` prop and `children` for body content.
4. **Composition** — Build `PageLayout` with `header`, `sidebar`, and `main` slot props.

## Summary

| Topic | Key point |
|-------|-----------|
| JSX | HTML-like syntax compiled to `createElement` |
| Rules | One root, camelCase, `{expressions}`, close tags |
| Props | Read-only data flow parent → child |
| Children | Nested content via `props.children` |
| Composition | Prefer nesting components over inheritance |

## Next chapter

Continue to [Chapter 3: State & Events](./ch03-state-and-events.md).
