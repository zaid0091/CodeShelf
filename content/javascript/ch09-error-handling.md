---
title: Error Handling
description: try/catch/finally, throwing errors, custom error classes, and async error patterns
order: 9
tags: [javascript, errors, try-catch, exceptions, debugging]
---

# Chapter 9: Error Handling

> "Errors are not enemies — unhandled errors are. Learn to catch, classify, and recover."

---

## Table of Contents

1. [What is an Error?](#what-is-an-error?)
2. [Built-in Error Types](#built-in-error-types)
3. [try catch finally](#try-catch-finally)
4. [Throwing Errors](#throwing-errors)
5. [Custom Error Classes](#custom-error-classes)
6. [Errors in Promises and async](#errors-in-promises-and-async)
7. [Unhandled Rejections](#unhandled-rejections)
8. [Defensive Programming](#defensive-programming)
9. [Error Handling Strategies](#error-handling-strategies)
10. [Debugging with DevTools](#debugging-with-devtools)
11. [Logging Best Practices](#logging-best-practices)
12. [Global Error Handlers](#global-error-handlers)
13. [Common Mistakes](#common-mistakes)
14. [Best Practices](#best-practices)
15. [Interview Points](#interview-points)
16. [Exercises](#exercises)
17. [Chapter Summary](#chapter-summary)

---

## What is an Error?

### Definition

An **error** is an exceptional condition that interrupts normal control flow. Uncaught errors appear in the console and may halt scripts.

### Why It Matters

Networks fail, JSON is malformed, users submit invalid data.

### How It Works

JavaScript throws **exception objects** with `name` and `message`.


```js
const obj = null;
// obj.name; // TypeError
```


---

## Built-in Error Types

### Definition

`Error`, `SyntaxError`, `ReferenceError`, `TypeError`, `RangeError`, `URIError` cover most cases.

### Why It Matters

Branch recovery logic with `instanceof`.

### How It Works

Each has a `stack` trace in modern engines.


```js
try {
  JSON.parse("{ invalid");
} catch (err) {
  console.log(err.name); // SyntaxError
}
```


---

## try catch finally

### Definition

`try` runs risky code; `catch` handles errors; `finally` always runs for cleanup.

### Why It Matters

Parse config, call APIs, release resources.

### How It Works

`finally` runs even if `try` returns.


```js
try {
  return JSON.parse(json);
} catch (e) {
  return defaults;
} finally {
  hideSpinner();
}
```


---

## Throwing Errors

### Definition

`throw` raises an exception — use for truly exceptional cases, not normal flow.

### Why It Matters

Signal invalid input early — fail fast.

### How It Works

Can throw any value; prefer `Error` objects.


```js
function withdraw(balance, amount) {
  if (amount > balance) throw new Error("Insufficient funds");
  return balance - amount;
}
```


---

## Custom Error Classes

### Definition

Extend `Error` with `class ValidationError extends Error` for typed handling.

### Why It Matters

API layers return errors consumers can distinguish.

### How It Works

Set `this.name` in constructor.


```js
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
  }
}
```


---

## Errors in Promises and async

### Definition

Rejections propagate through `.catch`; `await` throws into `try/catch`.

### Why It Matters

Same mental model as sync once you use async/await.

### How It Works

See [Chapter 7](./ch07-asynchronous-javascript.md).


```js
async function main() {
  try {
    const data = await fetchData();
  } catch (err) {
    showError(err.message);
  }
}
```


---

## Unhandled Rejections

### Definition

Promise rejected without handler triggers `unhandledrejection`.

### Why It Matters

Production monitoring hooks.

### How It Works

Always end chains with `.catch` or try/catch.


```js
window.addEventListener("unhandledrejection", (e) => {
  console.error(e.reason);
});
```


---

## Defensive Programming

### Definition

Validate inputs, use guards, optional chaining — prevent errors before they happen.

### Why It Matters

Cheaper than try/catch everywhere.

### How It Works

Assert in development only.


```js
function getLength(value) {
  if (value == null) return 0;
  if (typeof value === "string" || Array.isArray(value)) return value.length;
  throw new TypeError("Expected string or array");
}
```


---

## Error Handling Strategies

### Definition

Fail fast, recover with defaults, log-and-continue, global handlers — pick per layer.

### Why It Matters

UI shows friendly message; server logs details.

### How It Works

Never swallow errors silently without logging.


```js
async function api(path) {
  const res = await fetch(path);
  if (!res.ok) throw new HttpError(res.statusText, res.status);
  return res.json();
}
```


---

## Debugging with DevTools

### Definition

`debugger` statement, breakpoints, watch expressions, stack traces.

### Why It Matters

Find root cause faster than `console.log` alone.

### How It Works

Use Sources panel in Chrome/Edge/Firefox.


```js
function complex(x) {
  debugger; // pauses when DevTools open
  return x * 2;
}
console.trace("here");
```


---

## Logging Best Practices

### Definition

Structured logs with context; levels error/warn/info.

### Why It Matters

Production needs correlation IDs.

### How It Works

Never log passwords or tokens.


```js
console.error("[API]", { path, status, requestId });
```


---

## Global Error Handlers

### Definition

`window.onerror` and `unhandledrejection` catch last-resort failures.

### Why It Matters

Telemetry services (Sentry, etc.).

### How It Works

Cannot recover all cases — some errors are fatal.


```js
window.onerror = (msg, url, line) => {
  report({ msg, url, line });
};
```


---

### try catch finally — Example 1

```js
// Example 1: practical pattern for try catch finally
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


### try catch finally — Example 2

```js
// Example 2: practical pattern for try catch finally
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


### try catch finally — Example 3

```js
// Example 3: practical pattern for try catch finally
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


### try catch finally — Example 4

```js
// Example 4: practical pattern for try catch finally
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


### try catch finally — Example 5

```js
// Example 5: practical pattern for try catch finally
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

### Custom Error Classes — Example 1

```js
// Example 1: practical pattern for custom error classes
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


### Custom Error Classes — Example 2

```js
// Example 2: practical pattern for custom error classes
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


### Custom Error Classes — Example 3

```js
// Example 3: practical pattern for custom error classes
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


### Custom Error Classes — Example 4

```js
// Example 4: practical pattern for custom error classes
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


### Custom Error Classes — Example 5

```js
// Example 5: practical pattern for custom error classes
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

### Errors in Promises and async — Example 1

```js
// Example 1: practical pattern for errors in promises and async
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


### Errors in Promises and async — Example 2

```js
// Example 2: practical pattern for errors in promises and async
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


### Errors in Promises and async — Example 3

```js
// Example 3: practical pattern for errors in promises and async
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


### Errors in Promises and async — Example 4

```js
// Example 4: practical pattern for errors in promises and async
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


### Errors in Promises and async — Example 5

```js
// Example 5: practical pattern for errors in promises and async
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

### Defensive Programming — Example 1

```js
// Example 1: practical pattern for defensive programming
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


### Defensive Programming — Example 2

```js
// Example 2: practical pattern for defensive programming
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


### Defensive Programming — Example 3

```js
// Example 3: practical pattern for defensive programming
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


### Defensive Programming — Example 4

```js
// Example 4: practical pattern for defensive programming
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


### Defensive Programming — Example 5

```js
// Example 5: practical pattern for defensive programming
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

### Empty catch blocks

Hides bugs — log or rethrow.

### throw string

Use `Error` objects for stacks.


## Best Practices

- Use specific error types.
- try/catch at boundaries (I/O, parse).
- Use finally for cleanup.

## Interview Points

### try vs throw?

try handles; throw creates.

### finally without catch?

Yes — cleanup still runs.


## Exercises

### Exercise 9.1 — Safe parse

`safeJsonParse(str, fallback)`

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
function safeJsonParse(s, fb) { try { return JSON.parse(s); } catch { return fb; } }
```


</details>

### Exercise 9.2 — NotFoundError

Custom error with resource field.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
class NotFoundError extends Error { constructor(r) { super(`Not found: ${r}`); this.resource = r; } }
```


</details>

### Exercise 9.3 — toResult

Return {ok,value} or {ok:false,error}.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
async function toResult(p) { try { return { ok: true, value: await p }; } catch (e) { return { ok: false, error: e }; } }
```


</details>

### Exercise 9.4 — Validation

Collect all field errors.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
throw new ValidationError('email invalid', 'email');
```


</details>

### Exercise 9.5 — Rethrow

Log then throw for caller.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
catch(e) { log(e); throw e; }
```


</details>

### Exercise 9.6 — instanceof chain

Handle ValidationError vs Error.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
if (e instanceof ValidationError) ...
```


</details>

## Chapter Summary

| Practice | Why |
|----------|-----|
| Typed errors | Branching |
| Boundaries | I/O only |
| No silent catch | Debuggable |


---

## Next Chapter

Next: organize code with **modules and npm**.

---

**⬅️ [Previous: DOM and Events](./ch08-dom-and-events.md)** · **➡️ [Next Chapter: Modules and npm →](./ch10-modules-and-npm.md)**

---

*Last updated: 2026 | Chapter 9 of the Complete JavaScript Guide*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*

---

## Worked Example 1: Error Handling

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
// Worked example 1 for Chapter 9
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

## Worked Example 2: Error Handling

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
// Worked example 2 for Chapter 9
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

## Worked Example 3: Error Handling

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
// Worked example 3 for Chapter 9
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

## Worked Example 4: Error Handling

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
// Worked example 4 for Chapter 9
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


---

## Worked Example 5: Error Handling

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
// Worked example 5 for Chapter 9
function demo5(input) {
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

console.log(demo5({ a: 1, b: 2 }));
console.log(demo5([1, 2, 3]));
console.log(demo5("test"));
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

## Worked Example 6: Error Handling

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
// Worked example 6 for Chapter 9
function demo6(input) {
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

console.log(demo6({ a: 1, b: 2 }));
console.log(demo6([1, 2, 3]));
console.log(demo6("test"));
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

## Worked Example 7: Error Handling

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
// Worked example 7 for Chapter 9
function demo7(input) {
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

console.log(demo7({ a: 1, b: 2 }));
console.log(demo7([1, 2, 3]));
console.log(demo7("test"));
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

## Worked Example 8: Error Handling

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
// Worked example 8 for Chapter 9
function demo8(input) {
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

console.log(demo8({ a: 1, b: 2 }));
console.log(demo8([1, 2, 3]));
console.log(demo8("test"));
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

## Worked Example 9: Error Handling

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
// Worked example 9 for Chapter 9
function demo9(input) {
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

console.log(demo9({ a: 1, b: 2 }));
console.log(demo9([1, 2, 3]));
console.log(demo9("test"));
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

## Worked Example 10: Error Handling

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
// Worked example 10 for Chapter 9
function demo10(input) {
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

console.log(demo10({ a: 1, b: 2 }));
console.log(demo10([1, 2, 3]));
console.log(demo10("test"));
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

## Worked Example 11: Error Handling

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
// Worked example 11 for Chapter 9
function demo11(input) {
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

console.log(demo11({ a: 1, b: 2 }));
console.log(demo11([1, 2, 3]));
console.log(demo11("test"));
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

## Worked Example 12: Error Handling

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
// Worked example 12 for Chapter 9
function demo12(input) {
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

console.log(demo12({ a: 1, b: 2 }));
console.log(demo12([1, 2, 3]));
console.log(demo12("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.

