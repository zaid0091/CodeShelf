---
title: JavaScript Best Practices
description: Code style, performance, security, testing habits, and maintainable patterns
order: 13
tags: [javascript, best-practices, style, security, performance]
---

# Chapter 13: Best Practices

## 13.1 Code style and readability

| Guideline | Example |
|-----------|---------|
| Use `const` by default | `const items = []` |
| Meaningful names | `totalPrice` not `tp` |
| Small functions | One responsibility per function |
| Early returns | Reduce nesting |
| Consistent formatting | Prettier + ESLint |

```javascript
// Prefer
function isValidEmail(email) {
  return typeof email === "string" && email.includes("@");
}

// Avoid deep nesting
function process(user) {
  if (!user) return null;
  if (!user.active) return null;
  return user.profile;
}
```

## 13.2 Avoid common pitfalls

```javascript
// Use === not ==
if (value === null) { /* ... */ }

// Don't use var
// var x = 1;

// Avoid modifying objects you don't own
// Array.prototype.myMethod = ...

// Beware + with strings
const total = Number(a) + Number(b);

// Check array before map
const list = Array.isArray(data) ? data : [];
```

## 13.3 Immutability and state

```javascript
// React / Redux style — new references trigger updates
const nextState = {
  ...state,
  user: { ...state.user, name: "Bob" },
};

// Avoid accidental mutation
function addItem(cart, item) {
  return [...cart, item]; // new array
}
```

## 13.4 Async best practices

```javascript
// Parallel when possible
const [users, settings] = await Promise.all([
  fetchUsers(),
  fetchSettings(),
]);

// Always handle errors
try {
  await save();
} catch (err) {
  reportError(err);
}

// Don't ignore promises
await doWork(); // or .catch() on fire-and-forget with care
```

## 13.5 Security essentials

| Risk | Mitigation |
|------|------------|
| XSS | Use `textContent`, sanitize HTML, CSP headers |
| Injection | Never `eval(userInput)` |
| Secrets in front-end | Don't put API secrets in client JS |
| `innerHTML` | Escape or use trusted templates only |
| Dependencies | `npm audit`, keep packages updated |

```javascript
// Dangerous
element.innerHTML = userComment;

// Safer
element.textContent = userComment;

// If HTML needed — use a trusted sanitizer library
```

## 13.6 Performance tips

```javascript
// Cache DOM queries
const list = document.querySelector("#list");

// DocumentFragment for many inserts
const frag = document.createDocumentFragment();
items.forEach((item) => frag.appendChild(createRow(item)));
list.appendChild(frag);

// Debounce expensive handlers (search, resize)
// Use event delegation for long lists

// Avoid work in tight loops
for (const item of largeArray) {
  // don't query DOM each iteration
}
```

| Technique | When |
|-----------|------|
| Debounce | Wait until user stops typing |
| Throttle | Limit scroll/resize frequency |
| Lazy load | Split code with dynamic `import()` |
| Virtual lists | Thousands of DOM rows |

## 13.7 Module and project organization

```text
src/
├── components/     # UI pieces
├── services/       # API calls
├── utils/          # Pure helpers
├── constants.js
└── main.js
```

- One main export per module when possible.
- Keep side effects in entry files.
- Colocate tests or use `__tests__` folders.

## 13.8 Documentation and types

```javascript
/**
 * @param {number} price
 * @param {number} rate - decimal, e.g. 0.2 for 20%
 * @returns {number}
 */
function addTax(price, rate) {
  return price * (1 + rate);
}
```

Consider TypeScript for large codebases — catches errors at compile time.

## 13.9 Testing mindset

```javascript
// Node built-in test runner (example)
import { test } from "node:test";
import assert from "node:assert";

test("adds numbers", () => {
  assert.equal(add(2, 3), 5);
});
```

| Test type | Focus |
|-----------|-------|
| Unit | Pure functions, utilities |
| Integration | API + DB / modules together |
| E2E | Full user flows (Playwright, Cypress) |

## 13.10 Git and collaboration

- Small, focused commits with clear messages.
- Run linter before push.
- Use PR reviews for knowledge sharing.
- Keep `main` deployable.

## 13.11 Accessibility (a11y)

```html
<button type="button" aria-label="Close dialog">×</button>
```

```javascript
// Manage focus in modals
dialog.showModal();
dialog.querySelector("input")?.focus();
```

- Use semantic HTML (`button`, `nav`, `main`).
- Support keyboard navigation.
- Provide labels for form fields.

## 13.12 Learning habits

1. Read MDN when unsure of an API.
2. Build small projects after each chapter.
3. Read others' code on GitHub.
4. Refactor old exercises with new patterns.
5. Review [Interview Prep](./ch14-interview-prep.md) periodically.

## 13.13 Chapter summary

| Area | Priority |
|------|----------|
| Readability | Names, small functions, `const` |
| Security | No `eval`, careful `innerHTML` |
| Async | `async/await` + error handling |
| Performance | Measure first; optimize hot paths |
| Tooling | ESLint, Prettier, tests |

## Exercises

### Exercise 13.1 — Refactor

Take a nested `if` script from [Chapter 3](./ch03-operators-and-control-flow.md) and refactor with guard clauses.

### Exercise 13.2 — Lint setup

Add ESLint and Prettier to a small Node project; fix all warnings.

### Exercise 13.3 — XSS fix

Given code that sets `innerHTML` from user input, rewrite to be safe.

### Exercise 13.4 — Performance audit

List three optimizations for a todo app that re-renders the entire list on every keystroke.

---

**Previous:** [Chapter 12: OOP & Prototypes](./ch12-oop-prototypes.md) · **Next:** [Chapter 14: Interview Prep](./ch14-interview-prep.md)
