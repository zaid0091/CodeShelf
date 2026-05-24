---
title: Async JavaScript
description: Promises, async/await, and handling asynchronous code
order: 2
tags: [async, promises]
---

# Async JavaScript

JavaScript is single-threaded but handles async operations via the event loop.

## Callbacks → Promises → Async/Await

```javascript
// Promise
fetch("/api/users")
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));

// Async/await (preferred)
async function getUsers() {
  try {
    const res = await fetch("/api/users");
    const data = await res.json();
    return data;
  } catch (err) {
    console.error(err);
  }
}
```

## Creating Promises

```javascript
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

async function example() {
  console.log("Start");
  await delay(1000);
  console.log("After 1 second");
}
```

## Promise Utilities

```javascript
// Run in parallel
const [users, posts] = await Promise.all([
  fetch("/api/users").then(r => r.json()),
  fetch("/api/posts").then(r => r.json()),
]);

// First to resolve/reject
const result = await Promise.race([fetchA(), fetchB()]);

// All settled (never rejects)
const results = await Promise.allSettled([p1, p2, p3]);
```

## Event Loop (Quick Recap)

1. **Call stack** — runs synchronous code
2. **Web APIs** — handle timers, fetch, DOM events
3. **Task queue** — callbacks waiting to run
4. **Microtask queue** — Promise callbacks (higher priority)

> Promises and `queueMicrotask` run before the next macrotask (setTimeout, I/O).
