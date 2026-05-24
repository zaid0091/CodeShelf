---
title: Interview Preparation
description: Common React interview questions, answers, coding challenges, and system design talking points.
order: 15
tags: [react, interview, preparation, questions]
---

# Chapter 15: Interview Preparation

## 15.1 How React interviews are structured

Typical React interview rounds:

| Round | Focus |
|-------|-------|
| Fundamentals | JSX, state, props, hooks |
| Live coding | Component building, bug fixes |
| Architecture | State design, performance, testing |
| Behavioral | Teamwork, trade-offs, past projects |

Review [Chapters 1–14](./ch00-course-overview.md) and practice explaining concepts out loud.

## 15.2 Core concepts Q&A

### What is React?

React is a JavaScript library for building UIs with a component-based, declarative model. It updates the DOM efficiently using a virtual DOM and reconciliation.

### What is JSX?

JSX is syntax sugar for `React.createElement()`. It lets you write HTML-like markup in JavaScript, compiled to function calls.

### Props vs state?

| Props | State |
|-------|-------|
| Passed from parent | Internal to component |
| Read-only | Updated via setter |
| External configuration | Triggers re-render on change |

### What is the Virtual DOM?

A lightweight in-memory representation of the UI. On state change, React diffs the new virtual tree against the previous one and applies minimal updates to the real DOM.

## 15.3 Hooks interview questions

### Explain useState

Returns `[value, setValue]`. Updates schedule a re-render. Use functional updates when next state depends on previous.

### Explain useEffect

Runs side effects after render. Dependency array controls re-runs. Return cleanup for subscriptions, timers, abort controllers.

### Why can't hooks be conditional?

React tracks hooks by call order. Conditional hooks would break the association between hook calls and state slots.

### useRef vs useState?

`useRef` updates `.current` without re-render — DOM refs, mutable values. `useState` triggers re-render when updated.

### When useMemo vs useCallback?

`useMemo` caches a **value**; `useCallback` caches a **function**. Both help when referential stability matters for memoized children.

See [Chapter 6](./ch06-hooks-deep-dive.md).

## 15.4 Lifecycle and rendering

### What causes a re-render?

- State change in component
- Parent re-render (prop reference change)
- Context value change consumed by component

### What is React.memo?

Higher-order component that skips re-render if props shallowly equal previous props.

### Keys in lists — why?

Keys identify list items across renders so React can match, add, remove, and reorder efficiently without resetting component state incorrectly.

## 15.5 Common coding challenges

### 1. Counter with increment/decrement

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <button onClick={() => setCount(c => c - 1)}>-</button>
      <span>{count}</span>
      <button onClick={() => setCount(c => c + 1)}>+</button>
    </div>
  );
}
```

### 2. Debounced search input

```jsx
function useDebounce(value, delay) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(id);
  }, [value, delay]);
  return debounced;
}
```

### 3. Toggle accordion

Track `openId` in parent; pass `isOpen` and `onToggle` to each item.

### 4. Fetch and display list

Model loading, error, and data states. Mention abort on unmount.

## 15.6 Architecture questions

### How do you manage global state?

Start with colocated `useState`, lift when needed, Context for theme/auth, React Query for server data, Redux/Zustand only when complexity warrants it.

### Prop drilling — solutions?

Context, composition (children), custom hooks, or state library.

### How do you optimize performance?

Measure with Profiler first; then `memo`, `useMemo`, `useCallback`, code splitting, virtualization.

## 15.7 React 18+ topics

| Feature | One-line answer |
|---------|-----------------|
| Concurrent rendering | Interruptible rendering for smoother UX |
| Automatic batching | Multiple setStates batch in more scenarios |
| `useTransition` | Mark updates as non-urgent |
| `useDeferredValue` | Defer updating derived expensive UI |
| Strict Mode double effects | Dev-only stress test for cleanup |

## 15.8 Testing questions

### How do you test React components?

React Testing Library — render component, query by role/label, simulate user events, assert visible outcomes. Mock network at boundary.

### What not to test?

Implementation details, internal state, third-party library internals.

See [Chapter 13](./ch13-testing.md).

## 15.9 Tricky questions

### setState is async — what does that mean?

Updates are batched and applied before next paint. Reading state immediately after `setState` may show old value — use functional updater or `useEffect` to react to new state.

### Index as key — when is it OK?

Static lists that never reorder, filter, or insert in the middle. Prefer stable ids otherwise.

### Controlled vs uncontrolled?

Controlled: React owns value via state. Uncontrolled: DOM owns value; read with ref.

## 15.10 System design (frontend)

Be ready to discuss:

- Folder structure for a medium SPA
- Auth flow (token storage, refresh, protected routes)
- Caching strategy with React Query
- Error boundaries and fallback UI
- Code splitting by route

```text
Example: "Design a product listing page"
→ Route + React Query for paginated fetch
→ Skeleton loading, error retry
→ Filter state in URL search params
→ Memoized ProductCard list
→ Lazy-loaded detail modal
```

## 15.11 Behavioral tips

- Explain **trade-offs**, not just one solution
- Mention **accessibility** and **error handling** unprompted
- Walk through your **thinking** during live coding
- Ask clarifying questions before coding

## 15.12 Practice plan (1 week)

| Day | Activity |
|-----|----------|
| 1 | Review Ch 1–4; rebuild counter + todo without notes |
| 2 | Review Ch 5–7; explain useEffect and Context aloud |
| 3 | Review Ch 8–10; sketch routed app with fetch |
| 4 | Review Ch 11–13; memo exercise + one RTL test |
| 5 | Mock interview: 2 coding + 5 conceptual questions |
| 6 | Review this chapter; weak areas from mock |
| 7 | Light review; rest before real interview |

## 15.13 Quick reference cheat sheet

```text
Hooks:     useState, useEffect, useContext, useRef, useMemo, useCallback
Routing:   BrowserRouter, Routes, Route, Link, useParams, useNavigate
Data:      fetch + loading/error/data OR useQuery/useMutation
Forms:     Controlled value + onChange; validate on submit
Lists:     map + stable key
Perf:      Profiler → memo, lazy, Suspense
Test:      RTL + userEvent + getByRole
```

## Exercises

1. **Mock interview** — Record yourself answering "Explain useEffect" in under 2 minutes.
2. **Live code** — Implement debounced search against a public API in 25 minutes.
3. **Whiteboard** — Draw component tree for an e-commerce checkout flow.
4. **Flashcards** — Write 20 Q&A cards from sections 15.2–15.9.

## Summary

| Preparation | Action |
|-------------|--------|
| Concepts | Props, state, hooks, rendering model |
| Coding | Counter, lists, fetch, forms |
| Architecture | State layers, Context, React Query |
| Soft skills | Trade-offs, clarity, a11y awareness |

## Course complete

Congratulations on finishing the React course! Return to the [Course Overview](./ch00-course-overview.md) for the full chapter index, or revisit any chapter for deeper study.
