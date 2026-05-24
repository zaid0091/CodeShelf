---
title: Introduction — What is React?
description: React library overview, Vite project setup, project structure, and your first component.
order: 1
tags: [react, introduction, vite, components]
---

# Chapter 1: Introduction — What is React?

## 1.1 What is React?

React is a **JavaScript library** for building user interfaces. It was created by Facebook (Meta) in 2013 and is now maintained by Meta and the open-source community.

> **Definition:** React lets you describe what the UI should look like for a given state, and it efficiently updates the DOM when that state changes.

### Library vs framework

| | React (library) | Framework (e.g. Next.js, Angular) |
|---|----------------|-------------------------------------|
| **Scope** | UI layer only | Routing, data, conventions built-in |
| **Flexibility** | You choose router, state, etc. | Opinionated structure |
| **Learning curve** | Smaller core API | More concepts upfront |

React focuses on **components** — reusable pieces of UI that manage their own logic and rendering.

### Why React?

```text
Traditional DOM manipulation:
  document.getElementById('count').textContent = newCount;
  // Manual, error-prone, hard to scale

React declarative approach:
  return <p>Count: {count}</p>;
  // Describe WHAT you want; React handles HOW to update the DOM
```

**Key benefits:**

- **Component-based** — build once, reuse everywhere
- **Declarative** — UI is a function of state
- **Virtual DOM** — efficient updates via diffing
- **Huge ecosystem** — routers, state libs, UI kits, jobs

### Where React is used

- Single-page applications (SPAs)
- Mobile apps (React Native)
- Static sites (Gatsby, Astro + React)
- Full-stack apps (Next.js, Remix)

## 1.2 Setting up with Vite

[Vite](https://vite.dev/) is the recommended way to scaffold a new React project. It provides instant dev server startup and fast hot module replacement (HMR).

### Create a new project

```bash
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install
npm run dev
```

Open the URL shown in the terminal (usually `http://localhost:5173`).

### Project structure

```text
my-react-app/
├── public/           # Static assets (favicon, etc.)
├── src/
│   ├── assets/       # Images, fonts imported in components
│   ├── App.jsx       # Root component
│   ├── App.css       # Styles for App
│   ├── main.jsx      # Entry point — mounts React to the DOM
│   └── index.css     # Global styles
├── index.html        # Single HTML shell
├── package.json
└── vite.config.js
```

### Entry point: `main.jsx`

```jsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

| Piece | Role |
|-------|------|
| `createRoot` | React 18 API — creates a root for concurrent rendering |
| `StrictMode` | Dev-only checks for deprecated APIs and side effects |
| `<App />` | Your top-level component tree starts here |

### TypeScript variant

For TypeScript, use `--template react-ts` and rename files to `.tsx`:

```bash
npm create vite@latest my-react-app -- --template react-ts
```

## 1.3 Your first component

A **component** is a JavaScript function that returns JSX (HTML-like syntax).

```jsx
function Welcome() {
  return (
    <div>
      <h1>Hello, CodeShelf!</h1>
      <p>Welcome to your first React component.</p>
    </div>
  );
}

export default Welcome;
```

Use it inside `App.jsx`:

```jsx
import Welcome from './Welcome.jsx'

function App() {
  return (
    <main>
      <Welcome />
    </main>
  )
}

export default App
```

### Naming rules

| Rule | Example |
|------|---------|
| Component names must be **PascalCase** | `UserCard`, not `userCard` |
| File name usually matches component | `UserCard.jsx` → `function UserCard` |
| One default export per file is common | `export default UserCard` |

### Functional components only

Since React 17+, **function components** are the standard. Class components still exist in legacy code but are not taught in this course.

```jsx
// ✅ Modern — function component
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}

// ❌ Legacy — class component (avoid in new code)
class Greeting extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}!</h1>;
  }
}
```

## 1.4 How React renders

```text
State change  →  React re-runs component function  →  Virtual DOM diff  →  Minimal real DOM update
```

1. You call `setState` or update state via a hook.
2. React re-executes the component function.
3. React compares the new virtual tree with the previous one.
4. Only changed nodes are patched in the browser DOM.

This is why you should **not mutate state directly** — React needs a new value to detect change.

## 1.5 DevTools and debugging

Install [React Developer Tools](https://react.dev/learn/react-developer-tools) for Chrome or Firefox:

- Inspect component tree and props/state
- Highlight re-renders
- Profile performance

In Vite, edits to `.jsx` files hot-reload instantly without losing component state (in most cases).

## 1.6 Common mistakes (beginners)

| Mistake | Fix |
|---------|-----|
| Lowercase component name `<welcome />` | Use PascalCase `<Welcome />` |
| Forgetting to export | Add `export default` or named export |
| Editing `index.html` for UI | Put UI in components under `src/` |
| Import path wrong | Use `./Welcome.jsx` relative to current file |

## Exercises

1. **Scaffold** — Create a Vite React app named `codeshelf-hello`. Change the page title in `index.html`.
2. **First component** — Create `Profile.jsx` showing your name and a short bio. Render it in `App.jsx`.
3. **Multiple components** — Add `Header.jsx` and `Footer.jsx`. Compose all three in `App`.
4. **Explore** — Open React DevTools and find `App` in the component tree.

## Summary

| Concept | Takeaway |
|---------|----------|
| React | UI library based on components and declarative rendering |
| Vite | Fast toolchain for dev and production builds |
| Component | Function returning JSX; name in PascalCase |
| `main.jsx` | Mounts `<App />` into `#root` |

## Next chapter

Continue to [Chapter 2: JSX & Components](./ch02-jsx-and-components.md) to learn JSX syntax, props, and composition.
