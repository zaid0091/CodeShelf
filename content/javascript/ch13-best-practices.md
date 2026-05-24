---
title: JavaScript Best Practices
description: Code style, performance, security, testing habits, and maintainable patterns
order: 13
tags: [javascript, best-practices, style, security, performance]
---

# Chapter 13: Best Practices

> "Good JavaScript is not clever — it is clear, safe, and boring in the best way."

---

## Table of Contents

1. [Readable Code](#readable-code)
2. [const let and Avoiding var](#const-let-and-avoiding-var)
3. [Strict Equality and Types](#strict-equality-and-types)
4. [Immutability](#immutability)
5. [Async Best Practices](#async-best-practices)
6. [Security XSS and CSRF](#security-xss-and-csrf)
7. [Performance](#performance)
8. [Testing Habits](#testing-habits)
9. [Linting and Formatting](#linting-and-formatting)
10. [Documentation](#documentation)
11. [Git and Code Review](#git-and-code-review)
12. [Common Mistakes](#common-mistakes)
13. [Best Practices](#best-practices)
14. [Interview Points](#interview-points)
15. [Exercises](#exercises)
16. [Chapter Summary](#chapter-summary)

---

## Readable Code

### Definition

Clear names, small functions, early returns — code is read more than written.

### Why It Matters

Team velocity and fewer bugs.

### How It Works


```js
function isValidEmail(email) {
  return typeof email === "string" && email.includes("@");
}
```




---

## const let and Avoiding var

### Definition

Default `const`; `let` when needed; never `var`.

### Why It Matters

Scope safety — [Chapter 1](./ch01-javascript-basics.md).

### How It Works


```js
const items = [];
let count = 0;
```




---

## Strict Equality and Types

### Definition

Use `===`; coerce explicitly when needed.

### Why It Matters

Avoid subtle bugs.

### How It Works


```js
if (value === null) { /* */ }
const total = Number(a) + Number(b);
```




---

## Immutability

### Definition

Spread to copy arrays/objects instead of mutating shared state.

### Why It Matters

React/Redux patterns.

### How It Works


```js
const next = { ...state, user: { ...state.user, name: "Bob" } };
```




---

## Async Best Practices

### Definition

Parallel with Promise.all; always handle errors.

### Why It Matters

Performance and reliability.

### How It Works


```js
const [u, s] = await Promise.all([fetchUsers(), fetchSettings()]);
```




---

## Security XSS and CSRF

### Definition

Escape output; use CSP; httpOnly cookies for sessions.

### Why It Matters

User data in innerHTML is dangerous.

### How It Works

Never eval user input.



---

## Performance

### Definition

Avoid unnecessary DOM work; debounce; lazy load.

### Why It Matters

Fast UX.

### How It Works


```js
// batch DOM updates
```




---

## Testing Habits

### Definition

Test behavior not implementation; use Node test runner or Jest.

### Why It Matters

Confidence to refactor.

### How It Works


```js
import { test } from "node:test";
import assert from "node:assert";
test("adds", () => assert.equal(1+1, 2));
```




---

## Linting and Formatting

### Definition

ESLint catches bugs; Prettier formats consistently.

### Why It Matters

Automate style debates.

### How It Works

Run in CI on every PR.



---

## Documentation

### Definition

JSDoc for public APIs; README for setup.

### Why It Matters

Onboarding new developers.

### How It Works

Document public functions with `@param` and `@returns`.



---

## Git and Code Review

### Definition

Small PRs, descriptive commits, review for logic not style only.

### Why It Matters

Quality gate.

### How It Works

Review for correctness, security, and tests — not bike-shedding style.



---

### Readable Code — Example 1

```js
// Example 1: practical pattern for readable code
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### Readable Code — Example 2

```js
// Example 2: practical pattern for readable code
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### Readable Code — Example 3

```js
// Example 3: practical pattern for readable code
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### Readable Code — Example 4

```js
// Example 4: practical pattern for readable code
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### Readable Code — Example 5

```js
// Example 5: practical pattern for readable code
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

### Immutability — Example 1

```js
// Example 1: practical pattern for immutability
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### Immutability — Example 2

```js
// Example 2: practical pattern for immutability
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### Immutability — Example 3

```js
// Example 3: practical pattern for immutability
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### Immutability — Example 4

```js
// Example 4: practical pattern for immutability
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### Immutability — Example 5

```js
// Example 5: practical pattern for immutability
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

### Security XSS and CSRF — Example 1

```js
// Example 1: practical pattern for security xss and csrf
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### Security XSS and CSRF — Example 2

```js
// Example 2: practical pattern for security xss and csrf
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### Security XSS and CSRF — Example 3

```js
// Example 3: practical pattern for security xss and csrf
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### Security XSS and CSRF — Example 4

```js
// Example 4: practical pattern for security xss and csrf
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### Security XSS and CSRF — Example 5

```js
// Example 5: practical pattern for security xss and csrf
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

### Async Best Practices — Example 1

```js
// Example 1: practical pattern for async best practices
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### Async Best Practices — Example 2

```js
// Example 2: practical pattern for async best practices
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### Async Best Practices — Example 3

```js
// Example 3: practical pattern for async best practices
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### Async Best Practices — Example 4

```js
// Example 4: practical pattern for async best practices
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### Async Best Practices — Example 5

```js
// Example 5: practical pattern for async best practices
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

## Common Mistakes

### Mutating shared state

Use copies.

### console.log in production

Use proper logging.


## Best Practices

- DRY but not premature abstraction.
- Review security on forms.
- Measure before optimizing.

## Interview Points

### Why immutability?

Predictable state updates and change detection.


## Exercises

### Exercise 13.1 — Refactor nested ifs

Early return

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
if (!user) return null;
```


</details>

### Exercise 13.2 — Lint setup

Add eslint config

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
// .eslintrc extends recommended
```


</details>

### Exercise 13.3 — Secure form

textContent not innerHTML

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
el.textContent = userInput;
```


</details>

### Exercise 13.4 — Parallel fetch

Promise.all two APIs

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
await Promise.all([a(),b()]);
```


</details>

### Exercise 13.5 — Test pure function

node:test

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
assert.equal(fn(2),4);
```


</details>

### Exercise 13.6 — Code review checklist

List 5 items

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
// naming, errors, tests, security, edge cases
```


</details>

## Chapter Summary

| Area | Focus |
|------|-------|
| Style | readable |
| Security | XSS |
| Async | errors |


---

## Next Chapter

Final chapter: **interview preparation**.

---

**⬅️ [Previous: OOP and Prototypes](./ch12-oop-prototypes.md)** · **➡️ [Next Chapter: Interview Preparation →](./ch14-interview-prep.md)**

---

*Last updated: 2026 | Chapter 13 of the Complete JavaScript Guide*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*

---

## Worked Example 1: Best Practices

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 1 for Chapter 13
function demo1(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo1({ a: 1, b: 2 }));
console.log(demo1([1, 2, 3]));
console.log(demo1("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 2: Best Practices

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 2 for Chapter 13
function demo2(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo2({ a: 1, b: 2 }));
console.log(demo2([1, 2, 3]));
console.log(demo2("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 3: Best Practices

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 3 for Chapter 13
function demo3(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo3({ a: 1, b: 2 }));
console.log(demo3([1, 2, 3]));
console.log(demo3("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 4: Best Practices

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 4 for Chapter 13
function demo4(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo4({ a: 1, b: 2 }));
console.log(demo4([1, 2, 3]));
console.log(demo4("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.

