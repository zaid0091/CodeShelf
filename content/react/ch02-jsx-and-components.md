---
title: JSX & Components
description: JSX syntax rules, expressions, props, children, default props, and component composition patterns.
order: 2
tags: [react, jsx, props, components, composition]
---

# Chapter 2: JSX & Components

> **JSX is how React components describe UI. Master these rules and you will read any React codebase comfortably.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [What is JSX?](#what-is-jsx)
2. [Why JSX Exists](#why-jsx-exists)
3. [JSX Rule 1: One Root Element](#jsx-rule-1-one-root-element)
4. [JSX Rule 2: Close All Tags](#jsx-rule-2-close-all-tags)
5. [JSX Rule 3: camelCase Attributes](#jsx-rule-3-camelcase-attributes)
6. [JSX Rule 4: Curly Braces for JavaScript](#jsx-rule-4-curly-braces-for-javascript)
7. [JSX Rule 5: Style Objects](#jsx-rule-5-style-objects)
8. [Embedding Comments in JSX](#embedding-comments-in-jsx)
9. [Boolean and Null in JSX](#boolean-and-null-in-jsx)
10. [Components and Props](#components-and-props)
11. [Props Are Immutable](#props-are-immutable)
12. [Destructuring and Rest Props](#destructuring-and-rest-props)
13. [Children Prop](#children-prop)
14. [Slot Props Pattern](#slot-props-pattern)
15. [Composition vs Inheritance](#composition-vs-inheritance)
16. [Conditional Rendering in JSX](#conditional-rendering-in-jsx)
17. [Export and Import Patterns](#export-and-import-patterns)
18. [Best Practices for JSX](#best-practices-for-jsx)
19. [Common Mistakes](#common-mistakes)
20. [Interview Points](#interview-points)
21. [Exercises](#exercises)
22. [Chapter Summary](#chapter-summary)

---

## What is JSX?

> **Definition:** JSX (JavaScript XML) is a syntax extension that lets you write HTML-like tags inside JavaScript. It compiles to `React.createElement()` calls.

```jsx
const el = <h1 className="title">Hello</h1>;
// Compiles roughly to:
const el = React.createElement('h1', { className: 'title' }, 'Hello');
```

Browsers cannot read JSX directly — Vite transforms it during development and build.

---

## Why JSX Exists

| Benefit | Explanation |
|---------|-------------|
| Readability | UI structure matches mental model |
| Safety | React escapes interpolated values by default |
| Tooling | Editors autocomplete tags and props |
| Co-location | Logic and markup live together |

#### Why this matters for `Why JSX Exists`

Understanding **Why JSX Exists** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## JSX Rule 1: One Root Element

```jsx
// ❌ Invalid — two roots
function Bad() {
  return (
    <h1>Title</h1>
    <p>Text</p>
  );
}

// ✅ Wrapper div
function Good() {
  return (
    <div>
      <h1>Title</h1>
      <p>Text</p>
    </div>
  );
}

// ✅ Fragment — no extra DOM node
function AlsoGood() {
  return (
    <>
      <h1>Title</h1>
      <p>Text</p>
    </>
  );
}
```

Use `<>...</>` (Fragment) when you need multiple siblings without a layout wrapper.

---

## JSX Rule 2: Close All Tags

Self-closing tags are required in JSX:

```jsx
<img src="/logo.png" alt="Logo" />
<input type="text" />
<br />
<hr />
```

HTML allows `<img>` without slash; JSX does not.

#### Why this matters for `JSX Rule 2: Close All Tags`

Understanding **JSX Rule 2: Close All Tags** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## JSX Rule 3: camelCase Attributes

| HTML | JSX |
|------|-----|
| `class` | `className` |
| `for` | `htmlFor` |
| `onclick` | `onClick` |
| `tabindex` | `tabIndex` |
| `readonly` | `readOnly` |

`class` is a reserved word in JavaScript — hence `className`.

#### Why this matters for `JSX Rule 3: camelCase Attributes`

Understanding **JSX Rule 3: camelCase Attributes** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## JSX Rule 4: Curly Braces for JavaScript

Put any JavaScript **expression** inside `{ }`:

```jsx
const name = 'Alice';
const items = [1, 2, 3];

function Profile() {
  return (
    <div>
      <h1>{name.toUpperCase()}</h1>
      <p>{2 + 2}</p>
      <p>{items.length} items</p>
    </div>
  );
}
```

**Not allowed inside `{ }` directly:** `if` statements, `for` loops, `function` declarations. Use ternaries, `&&`, or compute before `return`.

---

## JSX Rule 5: Style Objects

```jsx
<div style={{ color: 'blue', fontSize: 18, marginTop: '8px' }}>
  Styled text
</div>
```

- Outer `{ }` = JSX expression
- Inner `{ }` = JavaScript object
- Property names are camelCase (`fontSize`, not `font-size`)
- Numbers often imply `px` for unitless properties

#### Why this matters for `JSX Rule 5: Style Objects`

Understanding **JSX Rule 5: Style Objects** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Embedding Comments in JSX

```jsx
function Card() {
  return (
    <div>
      {/* This is a JSX comment */}
      <h1>Title</h1>
    </div>
  );
}
```

`//` comments cannot sit between tags without breaking parsing.

#### Why this matters for `Embedding Comments in JSX`

Understanding **Embedding Comments in JSX** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Boolean and Null in JSX

```jsx
{true && <p>Shown</p>}
{false && <p>Hidden</p>}
{null}
{undefined}
```

`false`, `null`, and `undefined` render nothing. **`0` renders `0`** — important for `{count && <Badge />}`.

#### Why this matters for `Boolean and Null in JSX`

Understanding **Boolean and Null in JSX** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Components and Props

> **Definition:** Props (properties) are read-only inputs passed from a parent component to a child.

```jsx
function Avatar({ src, alt, size = 48 }) {
  return <img src={src} alt={alt} width={size} height={size} />;
}

function UserCard({ user }) {
  return (
    <article>
      <Avatar src={user.avatar} alt={user.name} size={64} />
      <h2>{user.name}</h2>
      <p>{user.role}</p>
    </article>
  );
}

<UserCard user={{ name: 'Bob', role: 'Dev', avatar: '/bob.jpg' }} />
```

---

## Props Are Immutable

Never modify props inside a child:

```jsx
// ❌ Wrong
function Bad({ count }) {
  count = count + 1;
  return <p>{count}</p>;
}
```

If the child needs its own changing data, use `useState` (Chapter 3).

#### Why this matters for `Props Are Immutable`

Understanding **Props Are Immutable** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Destructuring and Rest Props

```jsx
function Button({ label, onClick, disabled = false }) {
  return (
    <button disabled={disabled} onClick={onClick}>
      {label}
    </button>
  );
}

function Input({ label, ...inputProps }) {
  return (
    <label>
      {label}
      <input {...inputProps} />
    </label>
  );
}
```

`...inputProps` forwards unknown props (name, type, placeholder) to the native `<input>`.

---

## Children Prop

Content between tags becomes `props.children`:

```jsx
function Card({ title, children }) {
  return (
    <section className="card">
      <h3>{title}</h3>
      <div>{children}</div>
    </section>
  );
}

<Card title="Stats">
  <p>Users: 1,240</p>
  <p>Revenue: $8,500</p>
</Card>
```

---

## Slot Props Pattern

Named props act as layout slots:

```jsx
function PageLayout({ header, sidebar, children }) {
  return (
    <div className="page">
      <header>{header}</header>
      <div className="body">
        <aside>{sidebar}</aside>
        <main>{children}</main>
      </div>
    </div>
  );
}
```

---

## Composition vs Inheritance

React has no `extends` for UI reuse like classical OOP. **Composition** nests components:

```jsx
function Dialog({ title, children, onClose }) {
  return (
    <div className="overlay" onClick={onClose}>
      <div className="dialog" onClick={(e) => e.stopPropagation()}>
        <h2>{title}</h2>
        {children}
      </div>
    </div>
  );
}
```

Build specialized UIs by wrapping generic ones with specific children and props.

---

## Conditional Rendering in JSX

```jsx
// Ternary
{isLoggedIn ? <Dashboard /> : <Login />}

// Logical AND — watch out for 0
{error && <p className="error">{error}</p>}
{count > 0 && <Badge count={count} />}

// Early return (outside JSX)
if (!data) return <Spinner />;
```

#### Why this matters for `Conditional Rendering in JSX`

Understanding **Conditional Rendering in JSX** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Export and Import Patterns

```jsx
// Default export
export default function Button() {}

// Named exports
export function IconButton() {}
export function PrimaryButton() {}

import Button from './Button.jsx';
import { IconButton } from './Button.jsx';
```

Stay consistent within your project.

#### Why this matters for `Export and Import Patterns`

Understanding **Export and Import Patterns** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Best Practices for JSX

1. Keep expressions in JSX short — extract helpers.
2. Use meaningful component names.
3. Prefer composition over prop drilling (Context later).
4. Always provide `alt` on images.
5. Use semantic HTML (`<main>`, `<nav>`, `<button>`).

#### Why this matters for `Best Practices for JSX`

Understanding **Best Practices for JSX** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Common Mistakes

| Mistake | Why it breaks | Fix |
|---------|---------------|-----|
| Using `class` instead of `className` | React warning; class not applied | Use `className` |
| Unclosed `<img>` or `<input>` | Syntax error | Self-close: `<img />` |
| Multiple root elements | Parse error | Wrap in `<div>` or `<>` |
| `if` inside `{ }` | Invalid expression | Ternary or variable before return |
| Modifying props | Breaks one-way data flow | Use local state |

---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: What is JSX?**

**Answer:** Syntax sugar for `React.createElement`. Compiled to JS before runtime. Not HTML.

---

> **📌 Interview Point 2: Why className?**

`class` is reserved in JS; JSX uses `className` for CSS classes.

---

> **📌 Interview Point 3: Props vs state?**

Props: read-only from parent. State: internal, mutable via setter.

---

> **📌 Interview Point 4: What is children?**

Special prop — nested JSX between component tags.

---

> **📌 Interview Point 5: Composition vs inheritance?**

React favors nesting components, not extending classes for UI.

---

## Exercises

Practice by building small pieces in a Vite React app. Try each exercise before opening solutions.

---

### Exercise 1: Fix Broken JSX ⭐

**Task:** Repair component using `class`, unclosed tags, and two roots.

<details>
<summary>💡 Hint (click to reveal)</summary>

Check five JSX rules.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```jsx
function Fixed() {
  return (
    <div className="card">
      <img src="/a.png" alt="A" />
      <p>OK</p>
    </div>
  );
}
```

</details>

---

### Exercise 2: UserCard ⭐

**Task:** Props: name, email, avatarUrl. Default avatar if missing.

<details>
<summary>💡 Hint (click to reveal)</summary>

Use default parameter or `||`.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

See Chapter 2 Avatar example.

</details>

---

### Exercise 3: Panel with children ⭐⭐

**Task:** Reusable `Panel` with `title` and `children`.

<details>
<summary>💡 Hint (click to reveal)</summary>

children goes in body div.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

Composition pattern.

</details>

---

### Exercise 4: PageLayout slots ⭐⭐

**Task:** header, sidebar, main as props.

<details>
<summary>💡 Hint (click to reveal)</summary>

Named slot props.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

PageLayout example in chapter.

</details>

---

### Exercise 5: Conditional badge ⭐⭐

**Task:** status prop: active/pending/error with different text.

<details>
<summary>💡 Hint (click to reveal)</summary>

Ternary or &&.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

StatusBadge pattern.

</details>

---

## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **JSX** | HTML-like syntax → createElement |
| **Rules** | One root, camelCase, `{expr}`, close tags |
| **Props** | Read-only parent → child |
| **Children** | Nested content |
| **Composition** | Nest, don't inherit |

## Next Chapter

Continue to [Chapter 3: State & Events](./ch03-state-and-events.md).

