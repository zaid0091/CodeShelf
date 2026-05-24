---
title: Asynchronous JavaScript
description: Callbacks, promises, async/await, and the event loop explained
order: 7
tags: [javascript, async, promises, async-await, event-loop, callbacks]
---

# Chapter 7: Asynchronous JavaScript

> "The event loop is the heartbeat of JavaScript — understand it once, and async code finally clicks."

---

## Table of Contents

1. [Synchronous vs Asynchronous](#synchronous-vs-asynchronous)
2. [Callbacks](#callbacks)
3. [Callback Hell](#callback-hell)
4. [The Event Loop](#the-event-loop)
5. [Promises](#promises)
6. [Promise Chaining](#promise-chaining)
7. [Promise Static Methods](#promise-static-methods)
8. [async and await](#async-and-await)
9. [Sequential vs Parallel async](#sequential-vs-parallel-async)
10. [Converting Callbacks to Promises](#converting-callbacks-to-promises)
11. [fetch API](#fetch-api)
12. [Error Handling in Async Code](#error-handling-in-async-code)
13. [Timers: setTimeout and setInterval](#timers:-settimeout-and-setinterval)
14. [AbortController](#abortcontroller)
15. [Async Iteration](#async-iteration)
16. [Microtasks vs Macrotasks](#microtasks-vs-macrotasks)
17. [Unhandled Promise Rejections](#unhandled-promise-rejections)
18. [Real-World Async Patterns](#real-world-async-patterns)
19. [Common Mistakes](#common-mistakes)
20. [Best Practices](#best-practices)
21. [Interview Points](#interview-points)
22. [Exercises](#exercises)
23. [Chapter Summary](#chapter-summary)

---

## Synchronous vs Asynchronous

### Definition

**Synchronous** code runs one line at a time and waits for each operation to finish. **Asynchronous** code starts work and continues; results arrive later via callbacks or Promises.

### Why It Matters

Browsers must stay responsive while loading images, calling APIs, or waiting on timers. Node servers handle thousands of connections without blocking threads per request.

### How It Works

Async operations delegate to the environment (browser Web APIs, Node libuv); JavaScript itself is single-threaded.


```js
console.log("1");
setTimeout(() => console.log("2"), 0);
console.log("3");
// 1, 3, 2
```

| Sync | Async |
|------|-------|
| Blocks until done | Non-blocking |
| Simple order | Timers, fetch, I/O |
| CPU-bound loops freeze UI | Needs patterns from this chapter |
---

## Callbacks

### Definition

A **callback** is a function passed to another function to run when async work completes.

### Why It Matters

Original async pattern in Node and browsers; still used in event listeners.

### How It Works

Convention: `callback(err, data)` — error-first style in Node.


```js
function fetchData(callback) {
  setTimeout(() => {
    callback(null, { id: 1, name: "Alice" });
  }, 500);
}

fetchData((err, data) => {
  if (err) return console.error(err);
  console.log(data);
});
```


---

## Callback Hell

### Definition

**Callback hell** is deeply nested callbacks that are hard to read and maintain.

### Why It Matters

Each async step waits on the previous — pyramid of doom.

### How It Works

Fix with Promises, `async/await`, or modular named functions.


```js
// Anti-pattern — hard to maintain
getUser(1, (err, user) => {
  if (err) return handle(err);
  getOrders(user.id, (err, orders) => {
    if (err) return handle(err);
    getDetails(orders[0].id, (err, detail) => {
      // more nesting...
    });
  });
});
```


---

## The Event Loop

### Definition

The **event loop** coordinates the call stack, Web APIs / Node APIs, and task queues so async callbacks run when the stack is empty.

### Why It Matters

Explains why `setTimeout(fn, 0)` does not run immediately and why Promise callbacks run before timers.

### How It Works

Microtasks (Promises) drain before the next macrotask (`setTimeout`, I/O).


```js
console.log("start");
setTimeout(() => console.log("timeout"), 0);
Promise.resolve().then(() => console.log("promise"));
console.log("end");
// start, end, promise, timeout
```

```text
Call Stack → Web APIs → (Microtask Queue) → Macrotask Queue → Event Loop
```
---

## Promises

### Definition

A **Promise** is an object representing a future value — states: `pending`, `fulfilled`, `rejected`.

### Why It Matters

Composable `.then` chains; unified error path with `.catch`.

### How It Works

`new Promise((resolve, reject) => { ... })` — executor runs synchronously.


```js
const p = new Promise((resolve, reject) => {
  const ok = true;
  if (ok) resolve("success");
  else reject(new Error("failed"));
});

p.then((v) => console.log(v))
 .catch((e) => console.error(e.message))
 .finally(() => console.log("done"));
```


---

## Promise Chaining

### Definition

Each `.then` can return a value or another Promise; the chain flattens nested async.

### Why It Matters

Readable pipelines vs callback nesting.

### How It Works

Return Promises from `.then` to wait for inner async.


```js
fetchUser(1)
  .then((user) => fetchOrders(user.id))
  .then((orders) => orders[0])
  .then((order) => console.log(order))
  .catch((err) => console.error(err));
```


---

## Promise Static Methods

### Definition

`Promise.all`, `allSettled`, `race`, `any`, `resolve`, `reject` compose multiple Promises.

### Why It Matters

Parallel requests, timeouts, and batch error handling.

### How It Works

`Promise.all` fails fast on first rejection.


```js
const [user, posts] = await Promise.all([
  fetchUser(),
  fetchPosts(),
]);

const results = await Promise.allSettled([p1, p2, p3]);
```


---

## async and await

### Definition

`async` functions always return a Promise; `await` pauses until a Promise settles.

### Why It Matters

Reads like synchronous code; use `try/catch` for errors.

### How It Works

Top-level `await` allowed in ES modules.


```js
async function loadDashboard(userId) {
  try {
    const user = await fetchUser(userId);
    const orders = await fetchOrders(user.id);
    return { user, orders };
  } catch (err) {
    console.error(err);
    throw err;
  }
}
```


---

## Sequential vs Parallel async

### Definition

Awaiting in sequence is slower when tasks are independent; `Promise.all` runs them in parallel.

### Why It Matters

Dashboard loading: fetch profile and settings together.

### How It Works

Only parallelize when tasks do not depend on each other's results.


```js
// Sequential
const a = await fetchA();
const b = await fetchB();

// Parallel
const [a, b] = await Promise.all([fetchA(), fetchB()]);
```


---

## Converting Callbacks to Promises

### Definition

Wrap callback APIs with `new Promise` or Node's `util.promisify`.

### Why It Matters

Bridge legacy code into modern async/await.

### How It Works

Resolve on success; reject on error.


```js
function readFilePromise(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, "utf8", (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}
```


---

## fetch API

### Definition

**`fetch`** returns a Promise resolving to a `Response` — standard HTTP in browsers and modern Node.

### Why It Matters

Replaces `XMLHttpRequest` for JSON APIs.

### How It Works

Check `response.ok`; parse with `.json()`, `.text()`, etc. See [Chapter 11](./ch11-browser-apis.md).


```js
async function getUsers() {
  const response = await fetch("https://api.example.com/users");
  if (!response.ok) throw new Error(`HTTP ${{response.status}}`);
  return response.json();
}
```


---

## Error Handling in Async Code

### Definition

Use `try/catch` with `await` or `.catch` on Promises; handle HTTP and network errors explicitly.

### Why It Matters

Unhandled rejections crash Node processes and log in browsers.

### How It Works

Always `await` Promises you care about or attach `.catch()`.


```js
async function safeFetch(url) {
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(res.statusText);
    return await res.json();
  } catch (err) {
    return { error: err.message };
  }
}
```


---

## Timers: setTimeout and setInterval

### Definition

`setTimeout` runs once after delay; `setInterval` repeats until cleared with `clearTimeout` / `clearInterval`.

### Why It Matters

Delays, polling, debounce/throttle implementations.

### How It Works

Delays are minimum — not guaranteed exact under load.


```js
const id = setTimeout(() => console.log("later"), 1000);
clearTimeout(id);

const intervalId = setInterval(() => tick(), 1000);
clearInterval(intervalId);
```


---

## AbortController

### Definition

`AbortController` cancels `fetch` and other APIs via `signal`.

### Why It Matters

User navigates away, search-as-you-type cancels stale requests.

### How It Works

Pass `{ signal: controller.signal }` to `fetch`; call `controller.abort()`.


```js
const controller = new AbortController();
fetch("/api/slow", { signal: controller.signal })
  .catch((e) => {
    if (e.name === "AbortError") console.log("Cancelled");
  });
setTimeout(() => controller.abort(), 5000);
```


---

## Async Iteration

### Definition

`for await...of` consumes async iterables; useful for streams.

### Why It Matters

Process large datasets without loading all into memory.

### How It Works

Works with async generators.


```js
async function* fetchPages() {
  let page = 1;
  while (page <= 3) {
    yield await fetchPage(page++);
  }
}

for await (const page of fetchPages()) {
  console.log(page);
}
```


---

## Microtasks vs Macrotasks

### Definition

Promises and `queueMicrotask` use the microtask queue; `setTimeout` and DOM events use macrotasks.

### Why It Matters

Interview favorite — order of console logs.

### How It Works

After each macrotask, the engine drains all microtasks.


```js
queueMicrotask(() => console.log("micro"));
setTimeout(() => console.log("macro"), 0);
```


---

## Unhandled Promise Rejections

### Definition

A rejection without `.catch` becomes an **unhandled rejection**.

### Why It Matters

Log in production; fix floating Promises.

### How It Works

Node: `process.on('unhandledRejection')`; browser: `unhandledrejection` event.


```js
process.on("unhandledRejection", (reason) => {
  console.error("Unhandled:", reason);
});
```


---

## Real-World Async Patterns

### Definition

Retry, timeout, parallel limit, and circuit breaker patterns appear in production APIs.

### Why It Matters

Resilience when networks fail.

### How It Works

Compose small async helpers.


```js
async function delay(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function fetchWithRetry(url, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      const res = await fetch(url);
      if (res.ok) return res.json();
    } catch (e) {
      if (i === retries - 1) throw e;
      await delay(500);
    }
  }
}
```


---

### Promises — Example 1

```js
// Example 1: practical pattern for promises
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


### Promises — Example 2

```js
// Example 2: practical pattern for promises
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


### Promises — Example 3

```js
// Example 3: practical pattern for promises
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


### Promises — Example 4

```js
// Example 4: practical pattern for promises
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


### Promises — Example 5

```js
// Example 5: practical pattern for promises
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

### async and await — Example 1

```js
// Example 1: practical pattern for async and await
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


### async and await — Example 2

```js
// Example 2: practical pattern for async and await
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


### async and await — Example 3

```js
// Example 3: practical pattern for async and await
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


### async and await — Example 4

```js
// Example 4: practical pattern for async and await
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


### async and await — Example 5

```js
// Example 5: practical pattern for async and await
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

### The Event Loop — Example 1

```js
// Example 1: practical pattern for the event loop
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


### The Event Loop — Example 2

```js
// Example 2: practical pattern for the event loop
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


### The Event Loop — Example 3

```js
// Example 3: practical pattern for the event loop
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


### The Event Loop — Example 4

```js
// Example 4: practical pattern for the event loop
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


### The Event Loop — Example 5

```js
// Example 5: practical pattern for the event loop
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

### fetch API — Example 1

```js
// Example 1: practical pattern for fetch api
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


### fetch API — Example 2

```js
// Example 2: practical pattern for fetch api
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


### fetch API — Example 3

```js
// Example 3: practical pattern for fetch api
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


### fetch API — Example 4

```js
// Example 4: practical pattern for fetch api
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


### fetch API — Example 5

```js
// Example 5: practical pattern for fetch api
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

### Real-World Async Patterns — Example 1

```js
// Example 1: practical pattern for real-world async patterns
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


### Real-World Async Patterns — Example 2

```js
// Example 2: practical pattern for real-world async patterns
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


### Real-World Async Patterns — Example 3

```js
// Example 3: practical pattern for real-world async patterns
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


### Real-World Async Patterns — Example 4

```js
// Example 4: practical pattern for real-world async patterns
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


### Real-World Async Patterns — Example 5

```js
// Example 5: practical pattern for real-world async patterns
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

### forEach with async

forEach ignores awaited callbacks — use `for...of` or `Promise.all`.

### Floating promises

Always await or catch Promises you create.

### Sequential when parallel works

Independent fetches should use `Promise.all`.

### Forgetting HTTP errors

`fetch` only rejects on network failure — check `response.ok`.


## Best Practices

- Prefer `async/await` over raw `.then` for readability.
- Use `Promise.all` for independent parallel work.
- Centralize API calls with error handling — [Chapter 9](./ch09-error-handling.md).
- Cancel stale requests with `AbortController`.
- Draw event loop diagrams when debugging order bugs.

## Interview Points

### What is the event loop?

Mechanism that runs the call stack, then microtasks, then macrotasks, repeating.

### Promise vs callback?

Promises are composable, have one error channel, and avoid deep nesting.

### What runs first: setTimeout(0) or Promise?

Promise microtasks run before the next macrotask timer.

### Does async/await block the thread?

It pauses the async function, not the whole program — other tasks can run.


## Exercises

### Exercise 7.1 — Delay helper

Write `delay(ms)` returning a Promise that resolves after `ms` ms.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
const delay = (ms) => new Promise((r) => setTimeout(r, ms));
```


</details>

### Exercise 7.2 — Retry fetch

Implement `fetchWithRetry(url, retries=3)` with 500ms between attempts.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
async function fetchWithRetry(url, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      const res = await fetch(url);
      if (res.ok) return res.json();
      throw new Error(res.statusText);
    } catch (e) {
      if (i === retries - 1) throw e;
      await new Promise((r) => setTimeout(r, 500));
    }
  }
}
```


</details>

### Exercise 7.3 — Event loop quiz

Predict: A, D, C, B for logs A, setTimeout B, Promise C, D.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
// A, D, C, B
```


</details>

### Exercise 7.4 — Parallel limit

Fetch URLs three at a time using batching with Promise.all.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
async function fetchInBatches(urls, size = 3) {
  const results = [];
  for (let i = 0; i < urls.length; i += size) {
    const batch = urls.slice(i, i + size);
    results.push(...(await Promise.all(batch.map((u) => fetch(u).then((r) => r.json())))));
  }
  return results;
}
```


</details>

### Exercise 7.5 — Timeout wrapper

Write `withTimeout(promise, ms)` that rejects if promise takes too long.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
function withTimeout(promise, ms) {
  return Promise.race([
    promise,
    new Promise((_, reject) =>
      setTimeout(() => reject(new Error("Timeout")), ms)
    ),
  ]);
}
```


</details>

### Exercise 7.6 — Promisify

Convert `function legacy(cb) { cb(null, 42); }` to return a Promise.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
function legacy(cb) { setTimeout(() => cb(null, 42), 100); }
const modern = () => new Promise((res, rej) => legacy((e, v) => (e ? rej(e) : res(v))));
```


</details>

## Chapter Summary

| Pattern | Use when |
|---------|----------|
| Callback | Legacy APIs |
| Promise | Composable pipelines |
| async/await | Readable sequential flow |
| Promise.all | Parallel independent tasks |
| Event loop | Debug execution order |


---

## Next Chapter

Next: manipulate pages with the **DOM and events**.

---

**⬅️ [Previous: ES6+ Modern Features](./ch06-es6-modern-features.md)** · **➡️ [Next Chapter: DOM and Events →](./ch08-dom-and-events.md)**

---

*Last updated: 2026 | Chapter 7 of the Complete JavaScript Guide*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*

---

## Worked Example 1: Async JavaScript

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
// Worked example 1 for Chapter 7
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

## Worked Example 2: Async JavaScript

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
// Worked example 2 for Chapter 7
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

## Worked Example 3: Async JavaScript

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
// Worked example 3 for Chapter 7
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

## Worked Example 4: Async JavaScript

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
// Worked example 4 for Chapter 7
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

## Worked Example 5: Async JavaScript

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
// Worked example 5 for Chapter 7
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

