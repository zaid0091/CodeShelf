---
title: Introduction — What is React?
description: React library overview, Vite project setup, project structure, and your first component.
order: 1
tags: [react, introduction, vite, components]
---

# Chapter 1: Introduction — What is React?

> **Welcome to React! You already know JavaScript — now you will learn how to build interactive user interfaces with components.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [What is React?](#what-is-react)
2. [Library vs Framework](#library-vs-framework)
3. [History of React](#history-of-react)
4. [Where React Runs](#where-react-runs)
5. [Prerequisites from JavaScript](#prerequisites-from-javascript)
6. [Setting Up with Vite](#setting-up-with-vite)
7. [Project Structure Explained](#project-structure-explained)
8. [The Entry Point main.jsx](#the-entry-point-main-jsx)
9. [Your First Component](#your-first-component)
10. [Component Naming Rules](#component-naming-rules)
11. [Imports and Exports](#imports-and-exports)
12. [Declarative vs Imperative UI](#declarative-vs-imperative-ui)
13. [Virtual DOM and Reconciliation](#virtual-dom-and-reconciliation)
14. [React 18 and Beyond](#react-18-and-beyond)
15. [StrictMode Explained](#strictmode-explained)
16. [React Developer Tools](#react-developer-tools)
17. [React vs Other Tools](#react-vs-other-tools)
18. [The React Ecosystem](#the-react-ecosystem)
19. [Best Practices for Beginners](#best-practices-for-beginners)
20. [Common Mistakes](#common-mistakes)
21. [Interview Points](#interview-points)
22. [Exercises](#exercises)
23. [Chapter Summary](#chapter-summary)

---

## What is React?

> **Definition:** React is a JavaScript **library** for building user interfaces. You describe what the screen should look like for a given state, and React updates the browser efficiently when that state changes.

### The building-blocks analogy

Think of a website like a house:

- **HTML** is the structure — walls, doors, rooms (headings, paragraphs, forms).
- **CSS** is decoration — paint, furniture layout, lighting (colors, spacing, fonts).
- **JavaScript** is electricity and plumbing — things that **move, respond, and change**.
- **React** is a **smart electrical system** — instead of rewiring every bulb by hand when something changes, you describe the desired setup once and React routes power where needed.

Without React, you often write code like this:

```javascript
const countEl = document.getElementById('count');
const btn = document.getElementById('btn');
let count = 0;
btn.addEventListener('click', () => {
  count++;
  countEl.textContent = count;
});
```

That works for a counter. For a dashboard with dozens of panels, manual DOM updates become fragile. React lets you write:

```jsx
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

You describe the UI as a function of `count`. React figures out which DOM nodes to update.

### What React is NOT

| Myth | Reality |
|------|---------|
| React is a full framework like Angular | React is a **UI library** — you add routing, data, etc. yourself |
| React replaces HTML/CSS | You still write markup (JSX) and styles |
| React only works with Facebook | React is open source; millions of apps use it |
| You must learn class components first | **Function components + hooks** are the modern standard |



---

## Library vs Framework

| | **React (library)** | **Framework (Next.js, Remix, Angular)** |
|---|---------------------|----------------------------------------|
| Scope | UI rendering layer | Routing, data conventions, build opinions |
| Flexibility | High — pick your tools | More structure out of the box |
| Learning curve | Smaller core API | More concepts upfront |
| Best for | SPAs, embedding widgets, learning UI fundamentals | Production apps needing full-stack patterns |

**Next.js** and **Remix** are **frameworks built on React**. You learn React first, then frameworks add file-based routing, server components, and deployment patterns.

---

## History of React

### Timeline

```
2011  — Facebook engineers face slow, complex UIs in News Feed
2013  — React open-sourced at JSConf; "virtual DOM" idea gains attention
2015  — React Native (mobile) announced
2016  — React 15; widespread adoption begins
2017  — React 16 ("Fiber") — rewrite of core engine for smoother updates
2018  — Hooks introduced (useState, useEffect) — functions replace classes for most code
2020  — React 17 — gradual upgrades, no new developer-facing features
2022  — React 18 — concurrent rendering, automatic batching, Strict Mode improvements
2024+ — React 19 — Actions, use(), improved form handling (check react.dev for latest)
```

Understanding this timeline explains why older tutorials show **class components** while modern ones use **hooks**.



---

## Where React Runs

### In the browser (most common)

Vite or Create React App bundles your components into JavaScript that runs in the user's browser — a **Single Page Application (SPA)**.

### On the server

Next.js and Remix can render React on the server (**SSR**) so users get HTML faster and SEO improves.

### On mobile

**React Native** uses React's component model for iOS and Android apps (different primitives: `<View>` instead of `<div>`).

### Everywhere else

Desktop (Electron), TV apps, documentation sites, design tools — if there is a UI, React may power it.



---

## Prerequisites from JavaScript

You completed (or are reviewing) the CodeShelf JavaScript course. These skills matter daily in React:

| JavaScript topic | Used in React for |
|------------------|-------------------|
| `const` / `let` | State, bindings |
| Arrow functions | Components, event handlers |
| Destructuring | Props: `function Card({ title })` |
| Template literals | Strings in JSX |
| Arrays + `.map()` | Rendering lists |
| Modules (`import`/`export`) | Splitting components across files |
| Promises / `async` | Data fetching |
| Spread `{...obj}` | Immutable state updates |
| Truthy/falsy | Conditional rendering `{show && <Modal />}` |

If any row feels shaky, pause and review that JavaScript chapter before continuing.

---

## Setting Up with Vite

> **Definition:** Vite is a modern build tool that starts a dev server instantly and updates the browser in milliseconds when you save a file (Hot Module Replacement).

### Create a new project

Open a terminal in the folder where you keep projects:

```bash
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install
npm run dev
```

Open the URL printed in the terminal (usually `http://localhost:5173`).

**TypeScript variant:**

```bash
npm create vite@latest my-react-app -- --template react-ts
```

Files use `.tsx` instead of `.jsx`; types help catch mistakes early.

### Scripts in package.json

| Script | Command | Purpose |
|--------|---------|---------|
| `dev` | `npm run dev` | Local development server |
| `build` | `npm run build` | Production bundle in `dist/` |
| `preview` | `npm run preview` | Preview production build locally |



---

## Project Structure Explained

```text
my-react-app/
├── public/              # Static files copied as-is (favicon)
├── src/
│   ├── assets/        # Images/fonts imported in code
│   ├── App.jsx          # Root component of your app
│   ├── App.css          # Styles for App
│   ├── main.jsx         # Entry — mounts React into the page
│   └── index.css        # Global styles
├── index.html           # Single HTML page with <div id="root">
├── package.json         # Dependencies and scripts
└── vite.config.js       # Vite configuration
```

**Rule of thumb:** Put UI in `src/` components, not in `index.html`. The HTML file is a thin shell.

---

## The Entry Point main.jsx

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
| `createRoot` | React 18 API — creates a root that supports concurrent features |
| `document.getElementById('root')` | The DOM node from `index.html` |
| `<App />` | Your component tree starts here |
| `StrictMode` | Development-only checks (see below) |

Everything visible in the app is a descendant of `<App />`.

---

## Your First Component

> **Definition:** A **component** is a JavaScript function whose name starts with a capital letter and that returns JSX (UI markup).

```jsx
// src/Welcome.jsx
function Welcome() {
  return (
    <div>
      <h1>Hello, CodeShelf!</h1>
      <p>My first React component.</p>
    </div>
  );
}

export default Welcome;
```

```jsx
// src/App.jsx
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

`<Welcome />` looks like HTML but is a **function call** that returns an element description.

---

## Component Naming Rules

| Rule | Good | Bad |
|------|------|-----|
| PascalCase name | `UserProfile` | `userProfile`, `user-profile` |
| File matches component | `UserProfile.jsx` | `profile.jsx` with `UserProfile` inside |
| Custom components capitalized in JSX | `<Welcome />` | `<welcome />` (browser treats as HTML tag) |
| One main idea per file | `Button.jsx` → `Button` | Five unrelated components in one file |

---

## Imports and Exports

### Default export

```jsx
export default function App() { ... }
import App from './App.jsx'  // name can differ when importing
```

### Named export

```jsx
export function formatDate(d) { ... }
import { formatDate } from './utils.js'
```

### Omitting extension

Vite allows `import App from './App'` — both work; be consistent in your project.



---

## Declarative vs Imperative UI

| Style | You write | Example |
|-------|-----------|---------|
| **Imperative** | Step-by-step DOM instructions | `el.textContent = x` |
| **Declarative** | What UI should look like for state | `return <p>{count}</p>` |

React is **declarative**: you describe the target UI; React reconciles the DOM.

---

## Virtual DOM and Reconciliation

### Virtual DOM

An in-memory tree describing UI. On each update, React builds a new tree and **diffs** it against the previous one.

### Reconciliation

The process of computing minimal DOM changes. **Keys** on lists help React match items correctly (Chapter 4).

### Why you must not mutate state

React detects many changes by **reference**. Mutating an array in place may skip re-renders. Always create new objects/arrays when updating state (Chapter 3).



---

## React 18 and Beyond

| Feature | Benefit |
|---------|---------|
| Concurrent rendering | Keeps UI responsive during heavy updates |
| Automatic batching | Multiple `setState` calls in more places merge into one render |
| `createRoot` | Required entry API |
| Transitions | Mark updates as low priority (`useTransition`) |

You do not need every feature on day one — they exist as you scale.

---

## StrictMode Explained

```jsx
<StrictMode>
  <App />
</StrictMode>
```

- Runs **only in development**
- Double-invokes some functions to expose missing cleanup
- Warns about deprecated APIs

Do not remove StrictMode to "fix" double logs — fix the underlying effect cleanup instead.

---

## React Developer Tools

Install the browser extension **React Developer Tools**:

1. Open your app at `localhost:5173`
2. Open DevTools → **Components** tab
3. Click `App` → see props, hooks state
4. Use **Profiler** later for performance (Chapter 11)

This is as essential as `console.log` for React work.

---

## React vs Other Tools

| Tool | Notes |
|------|-------|
| **Vue** | Progressive framework; template or JSX-like syntax |
| **Angular** | Full framework with TypeScript-first approach |
| **Svelte** | Compile-time framework; less runtime |
| **jQuery** | DOM utility (pre-component era); not comparable for large apps |

React's job market and ecosystem remain among the largest. Learning React transfers well to React Native and Next.js.

---

## The React Ecosystem

| Category | Popular choices |
|----------|-----------------|
| Routing | React Router, TanStack Router |
| Server state | TanStack Query |
| Client state | Zustand, Redux Toolkit, Jotai |
| Styling | CSS Modules, Tailwind, styled-components |
| UI kits | shadcn/ui, MUI, Chakra |
| Testing | Vitest + React Testing Library |
| Meta-frameworks | Next.js, Remix |

Learn the **React core** first; add libraries when a real problem appears.

---

## Best Practices for Beginners

1. **Keep components small** — if a file exceeds ~150 lines, consider splitting.
2. **Colocate files** — styles and tests near the component when possible.
3. **Use function components** — avoid class components in new code.
4. **Read error messages** — React errors often link to docs.
5. **Commit often** — small Git commits make debugging easier.
6. **Build while reading** — type every example yourself.

---

## Common Mistakes

| Mistake | Why it breaks | Fix |
|---------|---------------|-----|
| `<welcome />` lowercase | React treats it as HTML element, not your component | Use `<Welcome />` |
| Forgetting `export default` | Import fails or imports wrong thing | Export the component |
| Editing `index.html` for app UI | Bypasses component system | Put UI in `src/` |
| Wrong import path | Module not found error | Use `./Welcome.jsx` relative paths |
| Putting hooks in `main.jsx` | Hooks only work in components | Keep hooks inside components |

---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: What is React and why use it?**

**Answer framework:** React is a JavaScript library for building UIs with reusable components. It uses a declarative model and virtual DOM diffing for efficient updates. Benefits: component reuse, predictable data flow, large ecosystem, strong hiring demand.

---

> **📌 Interview Point 2: What is the difference between React and Next.js?**

React is the UI library. Next.js is a **framework** on top of React adding routing, SSR, API routes, and deployment conventions.

---

> **📌 Interview Point 3: What is JSX?**

JSX is syntax sugar for `React.createElement`. It is compiled to JavaScript before the browser runs it.

---

> **📌 Interview Point 4: What is the Virtual DOM?**

An in-memory representation of UI. React diffs new vs old virtual trees and updates only changed real DOM nodes.

---

> **📌 Interview Point 5: What does createRoot do?**

React 18 entry API that creates a root capable of concurrent rendering, replacing legacy `ReactDOM.render`.

---

> **📌 Interview Point 6: What is a React component?**

A function (or class) that returns UI. Must be capitalized when used in JSX.

---

> **📌 Interview Point 7: What is StrictMode?**

Development-only wrapper that runs extra checks to surface unsafe lifecycles and missing effect cleanup.

---

## Exercises

Practice by building small pieces in a Vite React app. Try each exercise before opening solutions.

---

### Exercise 1: Scaffold Your App ⭐

**Task:** Create a Vite React app named `codeshelf-hello`. Change the `<title>` in `index.html` and the heading in `App.jsx`.

<details>
<summary>💡 Hint (click to reveal)</summary>

Use `npm create vite@latest` with the `react` template.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```bash
npm create vite@latest codeshelf-hello -- --template react
cd codeshelf-hello
npm install
npm run dev
```

</details>

---

### Exercise 2: Profile Component ⭐

**Task:** Create `Profile.jsx` with your name, role, and bio. Import and render it inside `App.jsx`.

<details>
<summary>💡 Hint (click to reveal)</summary>

Default export Profile; import without curly braces.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```jsx
function Profile() {
  return (
    <section>
      <h2>Your Name</h2>
      <p>Role: Student</p>
      <p>Bio: Learning React.</p>
    </section>
  );
}
export default Profile;
```

</details>

---

### Exercise 3: Header and Footer ⭐⭐

**Task:** Add `Header.jsx` and `Footer.jsx`. Compose all three in `App` with a `<main>` between header and footer.

<details>
<summary>💡 Hint (click to reveal)</summary>

App only assembles; each child owns its markup.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```jsx
function App() {
  return (
    <>
      <Header />
      <main><Profile /></main>
      <Footer />
    </>
  );
}
```

</details>

---

### Exercise 4: Explore DevTools ⭐⭐

**Task:** Install React DevTools. Find `App` and `Profile` in the tree. Change text in code and watch HMR update.

<details>
<summary>💡 Hint (click to reveal)</summary>

Components tab shows hierarchy; pencil icon edits props in dev only.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

No code — observation exercise. Note which component re-renders when you edit `Profile.jsx`.

</details>

---

### Exercise 5: Declarative vs Imperative ⭐⭐

**Task:** In comments, rewrite a vanilla JS counter (getElementById) as a React `Counter` component sketch without running it.

<details>
<summary>💡 Hint (click to reveal)</summary>

Focus on state + JSX instead of manual DOM.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```jsx
// Imperative: update DOM directly
// Declarative:
function Counter() {
  const [n, setN] = useState(0);
  return <button onClick={() => setN(n + 1)}>{n}</button>;
}
```

</details>

---

## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **React** | UI library — components + declarative rendering |
| **Vite** | Fast dev server and production builds |
| **Component** | Function returning JSX; PascalCase |
| **main.jsx** | Mounts `<App />` into `#root` |
| **Virtual DOM** | Efficient updates via diffing |

## Next Chapter

Continue to [Chapter 2: JSX & Components](./ch02-jsx-and-components.md).

