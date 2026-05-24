---
title: JavaScript Course Overview
description: Complete JavaScript course — from fundamentals to modern browser APIs and interview prep
order: 0
tags: [javascript, overview, course]
---

# The Complete JavaScript Course

From absolute beginner to professional — every concept explained with examples and exercises.

## Course structure

### Part 1: Foundations

| Chapter | Topic |
|---------|--------|
| [JavaScript Basics](./ch01-javascript-basics.md) | History, running JS, variables (`let`, `const`, `var`) |
| [Data Types](./ch02-data-types.md) | Primitives, `typeof`, coercion, truthy/falsy |
| [Operators & Control Flow](./ch03-operators-and-control-flow.md) | `if`/`else`, `switch`, loops |

### Part 2: Functions & Data Structures

| Chapter | Topic |
|---------|--------|
| [Functions](./ch04-functions.md) | Declarations, arrows, scope, closures |
| [Arrays & Objects](./ch05-arrays-and-objects.md) | Array methods, destructuring, spread |

### Part 3: Modern JavaScript

| Chapter | Topic |
|---------|--------|
| [ES6+ Modern Features](./ch06-es6-modern-features.md) | Modules, classes, template literals, Map/Set |
| [Asynchronous JavaScript](./ch07-asynchronous-javascript.md) | Callbacks, promises, `async`/`await`, event loop |

### Part 4: Browser & Ecosystem

| Chapter | Topic |
|---------|--------|
| [DOM & Events](./ch08-dom-and-events.md) | Selecting elements, events, delegation |
| [Error Handling](./ch09-error-handling.md) | `try`/`catch`, custom errors |
| [Modules & npm](./ch10-modules-and-npm.md) | `import`/`export`, `package.json` |
| [Browser APIs](./ch11-browser-apis.md) | `fetch`, `localStorage`, JSON |

### Part 5: Advanced Topics

| Chapter | Topic |
|---------|--------|
| [OOP & Prototypes](./ch12-oop-prototypes.md) | Prototypes, `this`, classes |
| [Best Practices](./ch13-best-practices.md) | Style, performance, security |
| [Interview Preparation](./ch14-interview-prep.md) | Common JavaScript interview Q&A |

## Prerequisites

| Skill | Required? | Notes |
|-------|-----------|-------|
| HTML basics | Recommended | Needed for [DOM & Events](./ch08-dom-and-events.md) |
| CSS basics | Optional | Helpful for styling exercises |
| Programming experience | Optional | Course starts from zero |
| Node.js installed | Recommended | For [Modules & npm](./ch10-modules-and-npm.md) |

## How to run JavaScript

| Environment | How to use | Best for |
|-------------|------------|----------|
| Browser DevTools | Press `F12` → Console tab | Quick experiments |
| HTML `<script>` | `<script src="app.js"></script>` | Front-end projects |
| Node.js | `node app.js` in terminal | Back-end, tooling, learning |
| Online REPL | jsbin.com, repl.it | Sharing snippets |

```javascript
// Quick test in any environment
console.log("Hello, JavaScript!");
```

## Learning path

```text
Week 1–2:  Chapters 1–3  (syntax, types, control flow)
Week 3–4:  Chapters 4–5  (functions, arrays, objects)
Week 5–6:  Chapters 6–7  (ES6+, async)
Week 7–8:  Chapters 8–11 (browser, npm, APIs)
Week 9–10: Chapters 12–14 (OOP, best practices, interviews)
```

## How to use these notes

1. Read chapters **in order** — later chapters build on earlier ones.
2. **Type every code example** yourself; do not copy-paste blindly.
3. Complete the **exercises** at the end of each chapter before moving on.
4. Use the sidebar search (`Ctrl+K`) to jump to topics like "closures", "promises", or "destructuring".
5. Revisit [Interview Preparation](./ch14-interview-prep.md) after finishing the full course.

## What you will build (skills, not a single project)

| Skill | Chapter |
|-------|---------|
| Manipulate data with arrays and objects | [ch05](./ch05-arrays-and-objects.md) |
| Fetch data from an API | [ch07](./ch07-asynchronous-javascript.md), [ch11](./ch11-browser-apis.md) |
| Build interactive web pages | [ch08](./ch08-dom-and-events.md) |
| Structure a real project with npm | [ch10](./ch10-modules-and-npm.md) |
| Write maintainable, interview-ready code | [ch13](./ch13-best-practices.md) |

> **Tip:** Keep a personal "JavaScript playground" folder with one `.js` file per chapter. Re-run old exercises when reviewing.

## Key resources

| Resource | URL | Purpose |
|----------|-----|---------|
| MDN Web Docs | developer.mozilla.org/en-US/docs/Web/JavaScript | Authoritative reference |
| ECMAScript spec | tc39.es/ecma262/ | Language specification |
| Node.js docs | nodejs.org/docs | Runtime APIs |
| Can I use | caniuse.com | Browser compatibility |

## Course conventions

- **Code blocks** use modern ES2020+ syntax unless noted otherwise.
- **Numbered sections** (e.g., `3.2`) map to subtopics within a chapter.
- **Internal links** use relative paths: `./ch04-functions.md`.
- **Exercises** appear at the end of each chapter with suggested solutions in collapsible hints where applicable.

## Quick reference — language versions

| Name | Year | Highlights |
|------|------|------------|
| ES5 | 2009 | `strict` mode, JSON support |
| ES6 (ES2015) | 2015 | `let`/`const`, arrows, classes, modules |
| ES2017 | 2017 | `async`/`await` |
| ES2020 | 2020 | Optional chaining `?.`, nullish `??` |
| ES2022 | 2022 | Top-level README, top-level `await` in modules |

Start with [Chapter 1: JavaScript Basics](./ch01-javascript-basics.md) →
