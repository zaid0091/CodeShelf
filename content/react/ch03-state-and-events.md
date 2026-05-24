---
title: State & Events
description: useState hook, event handling, synthetic events, and controlled form inputs.
order: 3
tags: [react, state, useState, events, controlled-inputs]
---

# Chapter 3: State & Events

## 3.1 What is state?

**State** is data that changes over time and affects what the UI renders.

> **Definition:** When state updates, React re-runs the component function and reconciles the DOM with the new output.

| Props | State |
|-------|-------|
| Passed from parent | Owned by the component |
| Read-only | Updated via setter function |
| External | Internal |

## 3.2 The useState hook

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+1</button>
      <button onClick={() => setCount(c => c + 1)}>+1 (functional)</button>
    </div>
  );
}
```

### useState return value

| Index | Name | Purpose |
|-------|------|---------|
| 0 | `count` | Current state value |
| 1 | `setCount` | Function to schedule an update |

### Functional updates

When the new state depends on the previous state, use the updater form:

```jsx
setCount(prev => prev + 1);
```

This avoids stale closures in rapid clicks or async callbacks.

### State can hold any type

```jsx
const [user, setUser] = useState(null);
const [items, setItems] = useState([]);
const [form, setForm] = useState({ email: '', password: '' });
const [isOpen, setIsOpen] = useState(false);
```

## 3.3 Immutability rules

React compares state **by reference**. Mutating objects/arrays in place may not trigger a re-render.

```jsx
// ❌ Mutating array
items.push(newItem);
setItems(items);

// ✅ New array reference
setItems([...items, newItem]);

// ❌ Mutating object
form.email = value;
setForm(form);

// ✅ New object reference
setForm({ ...form, email: value });
```

## 3.4 Event handling

React uses **SyntheticEvents** — wrappers around native browser events for cross-browser consistency.

```jsx
function SearchBox() {
  const [query, setQuery] = useState('');

  function handleSubmit(e) {
    e.preventDefault();
    console.log('Searching for:', query);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      <button type="submit">Search</button>
    </form>
  );
}
```

### Common event props

| Prop | Fires when |
|------|------------|
| `onClick` | Mouse click |
| `onChange` | Input value changes |
| `onSubmit` | Form submitted |
| `onKeyDown` | Key pressed |
| `onFocus` / `onBlur` | Focus changes |

### Passing arguments to handlers

```jsx
<button onClick={() => deleteItem(id)}>Delete</button>

// Or with bind (less common)
<button onClick={deleteItem.bind(null, id)}>Delete</button>
```

## 3.5 Controlled inputs

A **controlled component** has its value driven by React state.

```jsx
function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  return (
    <form>
      <label>
        Email
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </label>
      <label>
        Password
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </label>
    </form>
  );
}
```

### Checkbox and select

```jsx
const [agreed, setAgreed] = useState(false);
const [country, setCountry] = useState('us');

<input
  type="checkbox"
  checked={agreed}
  onChange={(e) => setAgreed(e.target.checked)}
/>

<select value={country} onChange={(e) => setCountry(e.target.value)}>
  <option value="us">United States</option>
  <option value="uk">United Kingdom</option>
</select>
```

See [Chapter 9: Forms](./ch09-forms.md) for validation and uncontrolled alternatives.

## 3.6 Multiple state variables vs one object

| Approach | Best for |
|----------|----------|
| Separate `useState` calls | Independent values (count, isOpen) |
| Single object state | Related form fields updated together |
| `useReducer` | Complex state transitions (advanced) |

```jsx
// Separate — simple toggles
const [isLoading, setIsLoading] = useState(false);
const [error, setError] = useState(null);

// Object — forms
const [form, setForm] = useState({ name: '', bio: '' });
const updateField = (field) => (e) =>
  setForm(prev => ({ ...prev, [field]: e.target.value }));
```

## 3.7 Lifting state up (preview)

When two siblings need the same data, move state to their closest common parent.

```jsx
function TemperatureInput({ scale, temperature, onChange }) {
  return (
    <fieldset>
      <legend>Enter temperature in {scale}:</legend>
      <input value={temperature} onChange={(e) => onChange(e.target.value)} />
    </fieldset>
  );
}

function Calculator() {
  const [celsius, setCelsius] = useState('');
  const fahrenheit = celsius ? (parseFloat(celsius) * 9/5 + 32).toFixed(1) : '';

  return (
    <div>
      <TemperatureInput scale="Celsius" temperature={celsius} onChange={setCelsius} />
      <p>Fahrenheit: {fahrenheit}</p>
    </div>
  );
}
```

Full patterns in [Chapter 12](./ch12-patterns-and-architecture.md).

## 3.8 Batching updates

React 18 **automatically batches** multiple `setState` calls in event handlers into one re-render:

```jsx
function handleClick() {
  setCount(c => c + 1);
  setFlag(f => !f);
  // One re-render, not two
}
```

## Exercises

1. **Counter** — Build a counter with increment, decrement, and reset. Prevent count going below zero.
2. **Like button** — Toggle heart icon and count with `useState`.
3. **Registration form** — Controlled inputs for name, email, password. Log values on submit.
4. **Tabs** — State for active tab index; show different panel content per tab.

## Summary

| Topic | Key point |
|-------|-----------|
| `useState` | `[value, setValue] = useState(initial)` |
| Updates | Never mutate; create new objects/arrays |
| Events | `onClick`, `onChange`; call `e.preventDefault()` on forms |
| Controlled inputs | `value` + `onChange` tied to state |

## Next chapter

Continue to [Chapter 4: Lists & Keys](./ch04-lists-and-keys.md).
