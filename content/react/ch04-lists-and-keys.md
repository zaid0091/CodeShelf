---
title: Lists & Keys
description: Rendering arrays with map, key prop rules, filtering, and conditional rendering patterns.
order: 4
tags: [react, lists, keys, conditional-rendering, map]
---

# Chapter 4: Lists & Keys

## 4.1 Rendering lists

Use JavaScript's `.map()` to transform data into JSX elements.

```jsx
const fruits = ['Apple', 'Banana', 'Cherry'];

function FruitList() {
  return (
    <ul>
      {fruits.map((fruit, index) => (
        <li key={index}>{fruit}</li>
      ))}
    </ul>
  );
}
```

> **Definition:** `.map()` returns a new array. React expects an array of elements when you embed `{items.map(...)}` in JSX.

### Rendering object arrays

```jsx
const users = [
  { id: 1, name: 'Alice', role: 'Admin' },
  { id: 2, name: 'Bob', role: 'Editor' },
  { id: 3, name: 'Carol', role: 'Viewer' },
];

function UserList({ users }) {
  return (
    <section>
      {users.map(user => (
        <UserCard key={user.id} user={user} />
      ))}
    </section>
  );
}

function UserCard({ user }) {
  return (
    <article className="card">
      <h3>{user.name}</h3>
      <span className="badge">{user.role}</span>
    </article>
  );
}
```

## 4.2 Keys — why they matter

**Keys** help React identify which items changed, were added, or removed.

```jsx
{items.map(item => (
  <TodoItem key={item.id} item={item} />
))}
```

| Without stable keys | With stable keys |
|---------------------|------------------|
| Wrong DOM reuse | Correct item updates |
| Lost input focus | Focus preserved |
| Broken animations | Smooth list changes |

### Rules for keys

1. **Unique among siblings** — not globally unique
2. **Stable** — same item → same key across renders
3. **Do not use index** if list can reorder, filter, or insert in the middle

```jsx
// ✅ Best — database id
key={user.id}

// ⚠️ OK — static list that never reorders
key={index}

// ❌ Bad — random each render
key={Math.random()}
```

### Keys on fragments

```jsx
import { Fragment } from 'react';

{rows.map(row => (
  <Fragment key={row.id}>
    <dt>{row.term}</dt>
    <dd>{row.definition}</dd>
  </Fragment>
))}
```

## 4.3 Filtering before mapping

```jsx
function ActiveUsers({ users }) {
  const active = users.filter(u => u.isActive);

  if (active.length === 0) {
    return <p>No active users.</p>;
  }

  return (
    <ul>
      {active.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

### Search filter pattern

```jsx
function ProductList({ products }) {
  const [search, setSearch] = useState('');

  const filtered = products.filter(p =>
    p.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div>
      <input
        value={search}
        onChange={e => setSearch(e.target.value)}
        placeholder="Search products..."
      />
      <ul>
        {filtered.map(product => (
          <li key={product.id}>{product.name} — ${product.price}</li>
        ))}
      </ul>
    </div>
  );
}
```

## 4.4 Conditional rendering

### if / early return

```jsx
function Dashboard({ user }) {
  if (!user) {
    return <p>Please log in.</p>;
  }

  return <h1>Welcome, {user.name}</h1>;
}
```

### Ternary operator

```jsx
{isLoggedIn ? <Dashboard /> : <LoginPage />}
```

### Logical AND (`&&`)

```jsx
{error && <p className="error">{error}</p>}
{items.length > 0 && (
  <ul>{items.map(i => <li key={i.id}>{i.name}</li>)}</ul>
)}
```

> **Caution:** `{count && <Badge />}` renders `0` when count is 0. Use `{count > 0 && ...}` or ternary instead.

### Switch / lookup object

```jsx
const STATUS = {
  idle: <Spinner />,
  success: <CheckIcon />,
  error: <ErrorMessage />,
};

return <div>{STATUS[status] ?? null}</div>;
```

## 4.5 Empty and loading states

```jsx
function DataList({ items, isLoading, error }) {
  if (isLoading) return <p>Loading...</p>;
  if (error) return <p className="error">{error.message}</p>;
  if (items.length === 0) return <p>No results found.</p>;

  return (
    <ul>
      {items.map(item => (
        <li key={item.id}>{item.title}</li>
      ))}
    </ul>
  );
}
```

See [Chapter 10](./ch10-data-fetching.md) for async data patterns.

## 4.6 Nested lists

```jsx
function CategoryList({ categories }) {
  return (
    <ul>
      {categories.map(category => (
        <li key={category.id}>
          <h3>{category.name}</h3>
          <ul>
            {category.products.map(product => (
              <li key={product.id}>{product.name}</li>
            ))}
          </ul>
        </li>
      ))}
    </ul>
  );
}
```

Each level needs its own keys on the mapped element.

## 4.7 Anti-patterns

| Anti-pattern | Problem | Fix |
|--------------|---------|-----|
| `.map()` without `key` | React warning, poor diffing | Add stable `key` |
| `key={index}` on sortable list | Wrong component state | Use item id |
| Mutating array then re-render | Stale UI | Return new array from filter/map |
| `{items.map(...)}` when `items` undefined | Runtime crash | Default `items = []` |

## Exercises

1. **Todo list** — Render todos from state; add/remove items with unique ids (`crypto.randomUUID()`).
2. **Filter** — Add category filter buttons that show subset of products.
3. **Conditional** — Show "Cart empty" vs list of cart items using `&&` and ternary.
4. **Nested** — Render comments grouped by post id with nested `.map()` calls.

## Summary

| Topic | Key point |
|-------|-----------|
| `.map()` | Transform data → JSX list |
| `key` | Stable unique id per sibling |
| Filter | `.filter()` before `.map()` |
| Conditionals | Early return, ternary, `&&`, lookup maps |

## Next chapter

Continue to [Chapter 5: useEffect](./ch05-useEffect.md).
