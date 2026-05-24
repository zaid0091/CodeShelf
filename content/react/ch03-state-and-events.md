---
title: State & Events
description: useState hook, event handling, synthetic events, and controlled form inputs.
order: 3
tags: [react, state, useState, events, controlled-inputs]
---

# Chapter 3: State & Events

> **State makes UI interactive. This chapter connects your JavaScript variables to what users see on screen.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [What is State?](#what-is-state)
2. [Introducing useState](#introducing-usestate)
3. [Functional State Updates](#functional-state-updates)
4. [State Types](#state-types)
5. [Immutability Rules](#immutability-rules)
6. [Synthetic Events](#synthetic-events)
7. [Common Event Handlers](#common-event-handlers)
8. [Passing Arguments to Handlers](#passing-arguments-to-handlers)
9. [Controlled Inputs](#controlled-inputs)
10. [Checkbox and Select](#checkbox-and-select)
11. [Multiple useState vs One Object](#multiple-usestate-vs-one-object)
12. [Lifting State Up](#lifting-state-up)
13. [React 18 Batching](#react-18-batching)
14. [Hooks Rules Preview](#hooks-rules-preview)
15. [Best Practices](#best-practices)
16. [Common Mistakes](#common-mistakes)
17. [Interview Points](#interview-points)
18. [Exercises](#exercises)
19. [Chapter Summary](#chapter-summary)

---

## What is State?

> **Definition:** State is data owned by a component that can change over time. When state updates, React re-renders the component.

| Props | State |
|-------|-------|
| From parent | Inside component |
| Read-only | Updated via setter |
| External config | Internal behavior |

#### Why this matters for `What is State?`

Understanding **What is State?** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Introducing useState

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+1</button>
    </div>
  );
}
```

`useState(initial)` returns `[value, setValue]`.

---

## Functional State Updates

When next state depends on previous:

```jsx
setCount(prev => prev + 1);
```

Use this in rapid clicks, intervals, or async callbacks to avoid stale values.

#### Why this matters for `Functional State Updates`

Understanding **Functional State Updates** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## State Types

```jsx
const [user, setUser] = useState(null);
const [items, setItems] = useState([]);
const [form, setForm] = useState({ email: '', password: '' });
const [isOpen, setIsOpen] = useState(false);
```

State can hold any JavaScript value.

#### Why this matters for `State Types`

Understanding **State Types** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Immutability Rules

```jsx
// ❌ Mutate array
items.push(x);
setItems(items);

// ✅ New array
setItems([...items, x]);

// ❌ Mutate object
form.email = v;
setForm(form);

// ✅ New object
setForm({ ...form, email: v });
```

#### Why this matters for `Immutability Rules`

Understanding **Immutability Rules** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Synthetic Events

> **Definition:** React wraps browser events in SyntheticEvent objects for consistent behavior across browsers.

```jsx
function handleClick(e) {
  e.preventDefault();
  console.log('clicked');
}
<button onClick={handleClick}>Go</button>
```

#### Why this matters for `Synthetic Events`

Understanding **Synthetic Events** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Common Event Handlers

| Prop | When |
|------|------|
| `onClick` | Click |
| `onChange` | Input change |
| `onSubmit` | Form submit |
| `onKeyDown` | Key press |
| `onFocus` / `onBlur` | Focus |

#### Why this matters for `Common Event Handlers`

Understanding **Common Event Handlers** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Passing Arguments to Handlers

```jsx
<button onClick={() => deleteItem(id)}>Delete</button>
```

Do not call the handler immediately: `onClick={deleteItem(id)}` runs on every render.

#### Why this matters for `Passing Arguments to Handlers`

Understanding **Passing Arguments to Handlers** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Controlled Inputs

> **Definition:** A controlled input's value is driven by React state via `value` + `onChange`.

```jsx
const [email, setEmail] = useState('');
<input value={email} onChange={(e) => setEmail(e.target.value)} />
```

#### Why this matters for `Controlled Inputs`

Understanding **Controlled Inputs** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Checkbox and Select

```jsx
<input
  type="checkbox"
  checked={agreed}
  onChange={(e) => setAgreed(e.target.checked)}
/>

<select value={country} onChange={(e) => setCountry(e.target.value)}>
  <option value="us">US</option>
</select>
```

#### Why this matters for `Checkbox and Select`

Understanding **Checkbox and Select** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Multiple useState vs One Object

| Approach | Use when |
|----------|----------|
| Several `useState` | Independent values |
| One object | Form fields updated together |
| `useReducer` | Complex transitions (Ch 6+) |

#### Why this matters for `Multiple useState vs One Object`

Understanding **Multiple useState vs One Object** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Lifting State Up

Move shared state to the closest common parent when siblings need the same data. See Chapter 12 for full patterns.

#### Why this matters for `Lifting State Up`

Understanding **Lifting State Up** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## React 18 Batching

Multiple `setState` calls in event handlers batch into one re-render automatically.

#### Why this matters for `React 18 Batching`

Understanding **React 18 Batching** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Hooks Rules Preview

1. Only call hooks at top level.
2. Only call hooks from React functions.

Details in Chapter 6.

#### Why this matters for `Hooks Rules Preview`

Understanding **Hooks Rules Preview** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Best Practices

1. Colocate state near usage.
2. Never mutate state directly.
3. Use functional updates when needed.
4. `e.preventDefault()` on forms when not doing full page POST.

#### Why this matters for `Best Practices`

Understanding **Best Practices** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---


## Extended Practice 1 — State & Events

Apply one idea from this chapter in isolation:

1. Create `Practice1.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice1')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 2 — State & Events

Apply one idea from this chapter in isolation:

1. Create `Practice2.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice2')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 3 — State & Events

Apply one idea from this chapter in isolation:

1. Create `Practice3.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice3')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 4 — State & Events

Apply one idea from this chapter in isolation:

1. Create `Practice4.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice4')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 5 — State & Events

Apply one idea from this chapter in isolation:

1. Create `Practice5.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice5')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---
## Common Mistakes

| Mistake | Why it breaks | Fix |
|---------|---------------|-----|
| Mutating state objects | No re-render | Spread into new object |
| `onClick={fn()}` | Runs every render | Wrap: `() => fn()` |
| Missing `value` on controlled input | Cursor bugs | Pair value + onChange |
| Stale closure in setState | Wrong count | Use `prev =>` form |

---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: useState return value?**

[current, setter]. Setter schedules update.

---

> **📌 Interview Point 2: Why immutable updates?**

React compares references; mutation may skip render.

---

> **📌 Interview Point 3: Controlled vs uncontrolled?**

Controlled: React owns value. Uncontrolled: DOM/ref.

---

> **📌 Interview Point 4: What is batching?**

Multiple setStates merged into one render.

---

## Exercises

Practice by building small pieces in a Vite React app. Try each exercise before opening solutions.

---

### Exercise 1: Counter ⭐

**Task:** Increment, decrement, reset; no negative.

<details>
<summary>💡 Hint (click to reveal)</summary>

Clamp at 0.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

useState + handlers.

</details>

---

### Exercise 2: Like button ⭐

**Task:** Toggle heart and count.

<details>
<summary>💡 Hint (click to reveal)</summary>

Boolean + number state.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

Two useStates.

</details>

---

### Exercise 3: Registration form ⭐⭐

**Task:** Controlled name, email, password; log on submit.

<details>
<summary>💡 Hint (click to reveal)</summary>

preventDefault.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

Form pattern.

</details>

---

### Exercise 4: Tabs ⭐⭐

**Task:** Active tab index switches panel.

<details>
<summary>💡 Hint (click to reveal)</summary>

Single state index.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

Conditional render.

</details>

---

## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **useState** | [value, setValue] |
| **Events** | onClick, onChange |
| **Controlled** | value + onChange |

## Next Chapter

Continue to [Chapter 4: Lists & Keys](./ch04-lists-and-keys.md).

