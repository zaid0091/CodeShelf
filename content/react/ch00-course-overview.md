---
title: React Course Overview
description: Complete React course — from first component to production patterns, testing, and interview prep
order: 0
tags: [react, overview, course]
---

# The Complete React Course

From absolute beginner to professional — every concept explained with hands-on examples.

## Prerequisites

Before starting this course, you should be comfortable with:

| Skill | Why it matters |
|-------|----------------|
| **HTML & CSS** | React renders UI; you still write markup and styles |
| **JavaScript (ES6+)** | Arrow functions, destructuring, modules, promises |
| **npm / terminal basics** | Installing packages and running dev servers |

If you need a refresher, review the [JavaScript course overview](../javascript/ch00-course-overview.md) — especially [basics](../javascript/ch01-javascript-basics.md), [ES6+ features](../javascript/ch06-es6-modern-features.md), and [async](../javascript/ch07-asynchronous-javascript.md).

## Course structure

### Part 1: Foundations

| Chapter | Topic |
|---------|--------|
| [Introduction — What is React?](./ch01-introduction.md) | Library vs framework, Vite setup, first component |
| [JSX & Components](./ch02-jsx-and-components.md) | JSX rules, props, children, composition |
| [State & Events](./ch03-state-and-events.md) | `useState`, event handlers, controlled inputs |

### Part 2: Rendering & Side Effects

| Chapter | Topic |
|---------|--------|
| [Lists & Keys](./ch04-lists-and-keys.md) | `.map()`, keys, conditional rendering |
| [useEffect](./ch05-useEffect.md) | Side effects, cleanup, dependency arrays |
| [Hooks Deep Dive](./ch06-hooks-deep-dive.md) | `useRef`, `useMemo`, `useCallback`, custom hooks |

### Part 3: App Architecture

| Chapter | Topic |
|---------|--------|
| [Context API](./ch07-context-api.md) | `createContext`, Provider, `useContext` |
| [React Router](./ch08-react-router.md) | Routes, `Link`, `useParams`, nested routes |
| [Forms](./ch09-forms.md) | Controlled vs uncontrolled, validation |

### Part 4: Data & Performance

| Chapter | Topic |
|---------|--------|
| [Data Fetching](./ch10-data-fetching.md) | `fetch`, loading/error states, React Query intro |
| [Performance](./ch11-performance.md) | `memo`, `lazy`, `Suspense` |

### Part 5: Professional React

| Chapter | Topic |
|---------|--------|
| [Patterns & Architecture](./ch12-patterns-and-architecture.md) | Lifting state, compound components, render props |
| [Testing](./ch13-testing.md) | React Testing Library basics |
| [Best Practices](./ch14-best-practices.md) | Folder structure, naming, accessibility |
| [Interview Preparation](./ch15-interview-prep.md) | Common React interview Q&A |

## How to use these notes

1. Read **Part 1** and build a small counter or todo app alongside each chapter.
2. Work through **Part 2–3** to understand hooks, routing, and forms in a multi-page app.
3. Add **data fetching** and **performance** optimizations as your app grows.
4. Review **Part 5** before interviews or code reviews.

## Recommended learning path

```text
Week 1:  Ch 1–4  →  Build a static profile card + interactive counter
Week 2:  Ch 5–7  →  Add API data + theme toggle with Context
Week 3:  Ch 8–10 →  Multi-page app with forms and data fetch
Week 4:  Ch 11–15 → Optimize, test, and prepare for interviews
```

## Tools you will use

| Tool | Purpose |
|------|---------|
| **Vite** | Fast dev server and build tool |
| **React 18+** | UI library with concurrent features |
| **React Router** | Client-side routing |
| **React Testing Library** | Component testing |
| **TanStack Query (React Query)** | Server state management |

## Project ideas to practice

Build these mini-projects as you progress:

1. **Counter & Todo** (Ch 1–4) — state, lists, conditional UI
2. **Weather Dashboard** (Ch 5–7) — `useEffect`, fetch, Context for units (°C/°F)
3. **Blog Reader** (Ch 8–10) — routes, dynamic params, API pagination
4. **E-commerce Product Page** (Ch 11–13) — lazy images, form validation, tests

> **Tip:** Use the sidebar search (`Ctrl+K`) to jump to topics like "useEffect", "keys", or "Context".

## Next chapter

Start with [Chapter 1: Introduction — What is React?](./ch01-introduction.md).
