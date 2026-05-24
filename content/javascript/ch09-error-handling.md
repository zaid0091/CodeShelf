---
title: Error Handling
description: try/catch/finally, throwing errors, custom error classes, and async error patterns
order: 9
tags: [javascript, errors, try-catch, exceptions, debugging]
---

# Chapter 9: Error Handling

## 9.1 Errors in JavaScript

> **Definition:** An **error** is an exceptional condition that disrupts normal program flow. Uncaught errors halt execution (in strict mode and most environments) and appear in the console.

```javascript
const obj = null;
// obj.name; // TypeError: Cannot read properties of null
```

### Built-in error types

| Type | Typical cause |
|------|----------------|
| `Error` | Generic base class |
| `SyntaxError` | Invalid syntax |
| `ReferenceError` | Undefined variable |
| `TypeError` | Wrong type operation |
| `RangeError` | Number out of range |
| `URIError` | Invalid URI handling |

```javascript
try {
  JSON.parse("{ invalid");
} catch (err) {
  console.log(err.name);    // SyntaxError
  console.log(err.message);
}
```

## 9.2 `try` / `catch` / `finally`

```javascript
function parseConfig(json) {
  try {
    const config = JSON.parse(json);
    validate(config);
    return config;
  } catch (err) {
    console.error("Config failed:", err.message);
    return getDefaultConfig();
  } finally {
    console.log("parseConfig finished");
  }
}
```

| Block | Role |
|-------|------|
| `try` | Code that might throw |
| `catch` | Handle the error (`catch (err)` or `catch { }`) |
| `finally` | Always runs (cleanup) |

### Re-throwing

```javascript
async function loadUser(id) {
  try {
    return await fetchUser(id);
  } catch (err) {
    logToService(err);
    throw err; // let caller decide UI message
  }
}
```

## 9.3 Throwing errors

```javascript
function withdraw(balance, amount) {
  if (amount <= 0) {
    throw new Error("Amount must be positive");
  }
  if (amount > balance) {
    throw new Error("Insufficient funds");
  }
  return balance - amount;
}
```

Use `throw` for exceptional cases, not normal control flow.

## 9.4 Custom error classes

```javascript
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
  }
}

class HttpError extends Error {
  constructor(message, status) {
    super(message);
    this.name = "HttpError";
    this.status = status;
  }
}

function validateUser(data) {
  if (!data.email?.includes("@")) {
    throw new ValidationError("Invalid email", "email");
  }
}

try {
  validateUser({ email: "bad" });
} catch (err) {
  if (err instanceof ValidationError) {
    console.log(`Field ${err.field}: ${err.message}`);
  } else {
    throw err;
  }
}
```

## 9.5 Errors in promises and async

```javascript
// Promise rejection
fetch("/api")
  .then((r) => r.json())
  .catch((err) => console.error(err));

// async/await
async function main() {
  try {
    const data = await fetchData();
  } catch (err) {
    showError(err.message);
  }
}
```

### Unhandled rejections

```javascript
// Node / browser
process?.on?.("unhandledRejection", (reason) => {
  console.error("Unhandled:", reason);
});

window?.addEventListener?.("unhandledrejection", (e) => {
  console.error(e.reason);
});
```

## 9.6 Defensive programming

```javascript
function getLength(value) {
  if (value == null) return 0;
  if (typeof value === "string" || Array.isArray(value)) {
    return value.length;
  }
  throw new TypeError("Expected string or array");
}

// Assertions (development)
function assert(condition, message) {
  if (!condition) throw new Error(message ?? "Assertion failed");
}
```

## 9.7 Error handling strategies

| Strategy | When |
|----------|------|
| Fail fast | Throw early on invalid input |
| Recover | `catch` and return default |
| Log and continue | Non-critical paths |
| Global handler | Last resort for uncaught errors |

```javascript
// API wrapper pattern
async function api(path, options) {
  const res = await fetch(path, options);
  if (!res.ok) {
    const body = await res.text();
    throw new HttpError(body || res.statusText, res.status);
  }
  return res.json();
}
```

## 9.8 Debugging techniques

```javascript
// debugger statement — pauses in DevTools
function complexLogic(x) {
  debugger;
  return x * 2;
}

console.trace("Call stack here");
console.assert(value > 0, "value must be positive");
```

| DevTools feature | Use |
|------------------|-----|
| Breakpoints | Pause on line |
| Watch | Monitor expressions |
| Network tab | Failed requests |
| Sources | Stack trace navigation |

## 9.9 Chapter summary

| Practice | Reason |
|----------|--------|
| Specific error types | Easier branching with `instanceof` |
| `try/catch` near boundaries | I/O, parsing, user input |
| Don't swallow errors silently | Log or re-throw |
| `finally` for cleanup | Close connections, hide loaders |

## Exercises

### Exercise 9.1 — Safe parse

Write `safeJsonParse(str, fallback)` that returns `fallback` on invalid JSON instead of throwing.

### Exercise 9.2 — Custom error

Create `NotFoundError` with `resource` property. Throw it from `findById(items, id)` when missing.

### Exercise 9.3 — Async wrapper

Write `toResult(promise)` returning `{ ok: true, value }` or `{ ok: false, error }` without throwing.

### Exercise 9.4 — Validation

Build `validateSignup({ email, password })` throwing `ValidationError` with all failed fields collected (bonus: array of errors).

---

**Previous:** [Chapter 8: DOM & Events](./ch08-dom-and-events.md) · **Next:** [Chapter 10: Modules & npm](./ch10-modules-and-npm.md)
