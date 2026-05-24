---
title: Asynchronous JavaScript
description: Callbacks, promises, async/await, and the event loop explained
order: 7
tags: [javascript, async, promises, async-await, event-loop, callbacks]
---

# Chapter 7: Asynchronous JavaScript

## 7.1 Sync vs async

> **Definition:** **Synchronous** code runs line by line, blocking until each operation finishes. **Asynchronous** code starts an operation and continues; a callback or promise handles the result later.

```javascript
// Synchronous
console.log("1");
console.log("2");

// Asynchronous
console.log("1");
setTimeout(() => console.log("2"), 0);
console.log("3");
// Output: 1, 3, 2
```

| Sync | Async |
|------|-------|
| Predictable order | Non-blocking I/O |
| Blocks UI / server | Timers, fetch, file reads |
| Simple mental model | Requires promises/async patterns |

## 7.2 Callbacks

```javascript
function fetchData(callback) {
  setTimeout(() => {
    callback(null, { id: 1, name: "Alice" });
  }, 1000);
}

fetchData((err, data) => {
  if (err) return console.error(err);
  console.log(data);
});
```

### Callback hell (anti-pattern)

```javascript
getUser(1, (err, user) => {
  if (err) return handle(err);
  getOrders(user.id, (err, orders) => {
    if (err) return handle(err);
    getDetails(orders[0].id, (err, detail) => {
      // deeply nested...
    });
  });
});
```

Promises and `async`/`await` solve this. See sections 7.4–7.5.

## 7.3 The event loop

```text
┌───────────────────────────┐
│        Call Stack         │  ← runs sync code
└───────────────────────────┘
            ↓
┌───────────────────────────┐
│     Web APIs / Node       │  ← setTimeout, fetch, fs
└───────────────────────────┘
            ↓
┌───────────────────────────┐
│      Callback Queue       │  ← macrotasks (setTimeout)
└───────────────────────────┘
            ↓
┌───────────────────────────┐
│    Microtask Queue        │  ← Promise.then (runs before next macrotask)
└───────────────────────────┘
```

```javascript
console.log("start");

setTimeout(() => console.log("timeout"), 0);

Promise.resolve().then(() => console.log("promise"));

console.log("end");

// start → end → promise → timeout
```

## 7.4 Promises

> **Definition:** A **Promise** represents a value that may be available now, later, or never. It is in one of three states: `pending`, `fulfilled`, or `rejected`.

```javascript
const p = new Promise((resolve, reject) => {
  const ok = true;
  if (ok) resolve("success");
  else reject(new Error("failed"));
});

p.then((value) => console.log(value))
 .catch((err) => console.error(err.message))
 .finally(() => console.log("cleanup"));
```

### Promise chaining

```javascript
fetchUser(1)
  .then((user) => fetchOrders(user.id))
  .then((orders) => orders[0])
  .then((order) => console.log(order))
  .catch((err) => console.error(err));
```

### Static methods

| Method | Purpose |
|--------|---------|
| `Promise.resolve(x)` | Fulfilled promise with `x` |
| `Promise.reject(err)` | Rejected promise |
| `Promise.all([...])` | Wait for all; fail fast on first reject |
| `Promise.allSettled([...])` | Wait for all; never rejects |
| `Promise.race([...])` | First settled wins |
| `Promise.any([...])` | First fulfilled wins |

```javascript
const [user, posts] = await Promise.all([
  fetchUser(),
  fetchPosts(),
]);
```

## 7.5 `async` / `await`

```javascript
async function loadDashboard(userId) {
  try {
    const user = await fetchUser(userId);
    const orders = await fetchOrders(user.id);
    return { user, orders };
  } catch (err) {
    console.error("Dashboard failed:", err);
    throw err;
  }
}

loadDashboard(1).then(console.log);
```

| Rule | Detail |
|------|--------|
| `async` functions always return a Promise | Even `return 42` → `Promise.resolve(42)` |
| `await` pauses only inside `async` | Top-level `await` allowed in ES modules |
| Use `try/catch` | Same as sync error handling |

### Sequential vs parallel

```javascript
// Sequential (slower)
const a = await fetchA();
const b = await fetchB();

// Parallel (faster when independent)
const [a, b] = await Promise.all([fetchA(), fetchB()]);
```

## 7.6 Converting callbacks to promises

```javascript
const { promisify } = require("util");
const fs = require("fs");
const readFile = promisify(fs.readFile);

// Manual wrapper
function readFilePromise(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, "utf8", (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}
```

## 7.7 `fetch` API (browser / modern Node)

```javascript
async function getUsers() {
  const response = await fetch("https://api.example.com/users");

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }

  const users = await response.json();
  return users;
}
```

More in [Chapter 11: Browser APIs](./ch11-browser-apis.md).

## 7.8 Common mistakes

```javascript
// Mistake: forEach does not await
async function bad() {
  ids.forEach(async (id) => {
    await process(id); // not awaited by forEach
  });
}

// Fix: for...of or Promise.all
async function good() {
  await Promise.all(ids.map((id) => process(id)));
}

// Mistake: floating promise (no catch)
async function risky() {
  doSomething(); // missing await — errors may be unhandled
}
```

## 7.9 Error handling in async code

```javascript
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

See [Chapter 9: Error Handling](./ch09-error-handling.md).

## 7.10 Chapter summary

| Pattern | Use when |
|---------|----------|
| Callback | Legacy APIs, simple one-off |
| Promise | Composable async pipelines |
| `async/await` | Readable sequential async code |
| `Promise.all` | Parallel independent tasks |
| Event loop | Debug order of logs |

## Exercises

### Exercise 7.1 — Delay helper

Write `delay(ms)` returning a Promise that resolves after `ms` milliseconds.

### Exercise 7.2 — Retry

Implement `fetchWithRetry(url, retries = 3)` that retries on failure with 500ms delay between attempts.

### Exercise 7.3 — Event loop quiz

Predict output, then run:

```javascript
console.log("A");
setTimeout(() => console.log("B"), 0);
Promise.resolve().then(() => console.log("C"));
console.log("D");
```

### Exercise 7.4 — Parallel limit

Fetch URLs from an array three at a time (batch with `Promise.all`, not all at once).

---

**Previous:** [Chapter 6: ES6+ Modern Features](./ch06-es6-modern-features.md) · **Next:** [Chapter 8: DOM & Events](./ch08-dom-and-events.md)
