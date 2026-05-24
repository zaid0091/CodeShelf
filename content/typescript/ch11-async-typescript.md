---
title: Chapter 11 — Async TypeScript
description: Promises, async/await, error typing, fetch, and concurrency utilities.
order: 11
tags: [typescript, async, promises, await, fetch]
---


# Chapter 11: Async TypeScript

> **Async code is everywhere. This chapter types Promises, results, errors, and concurrent patterns safely.**
> Take your time with each section. TypeScript rewards patience — read compiler errors carefully and experiment in a small project as you go.

---


## Table of Contents

1. [Promise<T>](#promiset)
2. [async Functions](#async-functions)
3. [Awaited](#awaited)
4. [Typing fetch](#typing-fetch)
5. [Error Types](#error-types)
6. [Result Union](#result-union)
7. [Promise.all](#promiseall)
8. [Async Generators](#async-generators)
9. [void in callbacks](#void-in-callbacks)
10. [AbortController](#abortcontroller)
11. [Best Practices](#best-practices)
12. [Interview Points](#interview-points)
13. [Exercises](#exercises)
14. [Chapter Summary](#chapter-summary)

---

## 11.1 Promises and typing

A `Promise<T>` represents a value of type `T` available later (or an error).

```typescript
function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function fetchNumber(): Promise<number> {
  return Promise.resolve(42);
}
```

> **Definition:** **`Promise<T>`** is a generic type describing the resolved value type `T`. Rejection is not parameterized in the standard type — handle with try/catch or `.catch()`.

## 11.2 async and await

```typescript
async function loadConfig(): Promise<{ theme: string; lang: string }> {
  const res = await fetch("/api/config");
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json() as Promise<{ theme: string; lang: string }>;
}
```

Rules:

- `async` functions always return a `Promise` (wraps non-Promise return values).
- `await` unwraps `Promise<T>` to `T` inside async function.
- Errors reject the returned promise or throw in async body.

```typescript
async function getUser(id: number): Promise<User> {
  // return type Promise<User> — explicit recommended for exports
}
```

## 11.3 Return type inference

```typescript
async function example() {
  return 123; // Promise<number>
}
```

Annotate public APIs:

```typescript
async function example(): Promise<number> {
  return 123;
}
```

## 11.4 Awaited utility

Extract resolved type from nested promises:

```typescript
type ConfigPromise = Promise<{ debug: boolean }>;
type Config = Awaited<ConfigPromise>; // { debug: boolean }

type Nested = Promise<Promise<string>>;
type S = Awaited<Nested>; // string
```

See [Chapter 6](./ch06-utility-types.md).

## 11.5 Typing fetch and JSON

`Response.json()` returns `Promise<any>` — narrow safely:

```typescript
interface User {
  id: string;
  name: string;
}

async function fetchUser(id: string): Promise<User> {
  const res = await fetch(`/api/users/${id}`);
  if (!res.ok) {
    throw new HttpError(res.status, await res.text());
  }
  const data: unknown = await res.json();
  return parseUser(data);
}

function parseUser(data: unknown): User {
  if (
    typeof data === "object" &&
    data !== null &&
    "id" in data &&
    "name" in data &&
    typeof (data as User).id === "string" &&
    typeof (data as User).name === "string"
  ) {
    return data as User;
  }
  throw new Error("Invalid user payload");
}
```

For production, use **Zod**, **Valibot**, or **io-ts** for runtime validation + inferred types.

## 11.6 Custom error types

```typescript
class HttpError extends Error {
  constructor(
    public status: number,
    public body: string
  ) {
    super(`HTTP ${status}`);
    this.name = "HttpError";
  }
}

async function safeFetch(url: string): Promise<Response> {
  const res = await fetch(url);
  if (!res.ok) throw new HttpError(res.status, await res.text());
  return res;
}
```

Narrow in catch:

```typescript
try {
  await safeFetch("/api/x");
} catch (err) {
  if (err instanceof HttpError) {
    console.log(err.status);
  } else {
    throw err;
  }
}
```

## 11.7 Result type pattern (no throw)

```typescript
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

async function tryFetchUser(id: string): Promise<Result<User, HttpError>> {
  try {
    const user = await fetchUser(id);
    return { ok: true, value: user };
  } catch (err) {
    if (err instanceof HttpError) {
      return { ok: false, error: err };
    }
    throw err;
  }
}
```

See discriminated unions in [Chapter 8](./ch08-type-narrowing.md).

## 11.8 Promise combinators

```typescript
async function loadDashboard(): Promise<{
  user: User;
  posts: Post[];
}> {
  const [user, posts] = await Promise.all([
    fetchUser("1"),
    fetchPosts("1"),
  ]);
  return { user, posts };
}

const first = await Promise.race([
  fetchData(),
  timeout(5000),
]);
```

Typing `Promise.all`:

```typescript
const results = await Promise.all([
  fetchUser("1"),
  fetchPosts("1"),
] as const);
// [User, Post[]] when tuple preserved — use satisfies or explicit tuple
```

```typescript
const [user, posts]: [User, Post[]] = await Promise.all([
  fetchUser("1"),
  fetchPosts("1"),
]);
```

## 11.9 Async iterators

```typescript
async function* streamLines(url: string): AsyncGenerator<string> {
  const res = await fetch(url);
  const reader = res.body?.getReader();
  if (!reader) return;

  const decoder = new TextDecoder();
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    yield decoder.decode(value, { stream: true });
  }
}

for await (const chunk of streamLines("/logs")) {
  console.log(chunk);
}
```

## 11.10 void-returning async callbacks

Event handlers often expect `void`, not `Promise<void>`:

```typescript
button.addEventListener("click", () => {
  void saveData(); // explicitly ignore promise
});

// Or wrap:
button.addEventListener("click", () => {
  saveData().catch(console.error);
});
```

## 11.11 AbortController typing

```typescript
async function fetchWithTimeout(
  url: string,
  ms: number
): Promise<Response> {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), ms);

  try {
    return await fetch(url, { signal: controller.signal });
  } finally {
    clearTimeout(id);
  }
}
```

## 11.12 Common mistakes

| Mistake | Fix |
|---------|-----|
| `await` in non-async function | Mark function `async` or use `.then()` |
| Untyped `json()` as truth | Validate `unknown` |
| Floating promises | `void fn()` or await |
| `Promise<any>` everywhere | Generic wrappers |
| Lost narrowing after await | Re-validate mutable state |
| Sequential awaits when parallel OK | `Promise.all` |

> **Key takeaway:** Annotate async function return types as `Promise<T>`. Treat external JSON as `unknown`, validate, then use. Handle errors with typed custom errors or Result unions.
<!-- codeshelf:generated-appendix -->

---

## Promise typing — mental model

`Promise<T>` is a box that will eventually contain a `T` (or reject).

```typescript
async function fetchCount(): Promise<number> {
  const res = await fetch("/api/count");
  return Number(await res.text());
}
```

The **return type** of an `async` function is always wrapped in `Promise<...>`.

---

## Async errors — typed handling

```typescript
type Result<T> =
  | { ok: true; value: T }
  | { ok: false; error: Error };

async function loadText(url: string): Promise<Result<string>> {
  try {
    const res = await fetch(url);
    if (!res.ok) return { ok: false, error: new Error(String(res.status)) };
    return { ok: true, value: await res.text() };
  } catch (e) {
    return { ok: false, error: e instanceof Error ? e : new Error(String(e)) };
  }
}
```

Callers must check `ok` before using `value` — the type system enforces it.

---

## Result type pattern


```typescript
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

async function safeFetch(url: string): Promise<Result<string>> {
  try {
    const res = await fetch(url);
    if (!res.ok) return { ok: false, error: new Error(String(res.status)) };
    return { ok: true, value: await res.text() };
  } catch (e) {
    return { ok: false, error: e instanceof Error ? e : new Error(String(e)) };
  }
}
```


---

## Promise.all typing


```typescript
const [user, posts] = await Promise.all([
  fetchUser("1"),
  fetchPosts("1"),
] as const);
```


---

## Async generators


```typescript
async function* streamLines(file: string): AsyncGenerator<string> {
  // yield lines
}
```


---

## AbortController with fetch


```typescript
async function fetchWithTimeout(url: string, ms: number): Promise<Response> {
  const ctrl = new AbortController();
  const id = setTimeout(() => ctrl.abort(), ms);
  try {
    return await fetch(url, { signal: ctrl.signal });
  } finally {
    clearTimeout(id);
  }
}
```


---

## Result type


Model errors as data with `{ ok: true; value } | { ok: false; error }` unions.


---

## Promise.all


`Promise.all` on a tuple returns a tuple of resolved types — great for parallel fetches.


---

## void callbacks


`setTimeout(() => { ... })` callbacks often return `void` — do not mark them `async` unless you handle the floating promise.


---

## Definition — Promise

> **Definition:** **Promise** — A value that will be available in the future — typed as `Promise<T>` where `T` is the resolved type.


---

## async/await flow


```typescript
async function loadUser(id: string): Promise<User> {
  const res = await fetch(`/api/users/${id}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const raw: unknown = await res.json();
  return parseUser(raw); // validate before trust
}
```


---

## Error handling patterns


| Pattern | Use when |
|---------|----------|
| try/catch | Simple scripts |
| Result union | Explicit error paths |
| Custom Error subclass | HTTP/API layers |


---

## Floating promises


```typescript
// ❌ ESLint @typescript-eslint/no-floating-promises
saveUser(data);

// ✅
void saveUser(data); // explicit fire-and-forget
// or
await saveUser(data);
```


---

## Review Q1

**Q:** Type of `async function f(): number`? **A:** Returns `Promise<number>`, not `number`.

---

## Review Q2

**Q:** `Promise<void>` meaning? **A:** Promise that resolves with no useful value.

---

## Review Q3

**Q:** Should every `fetch` response be typed? **A:** Parse as `unknown`, then validate before treating as domain type.

---

## Scenario — parallel fetch


```typescript
interface User { id: string; name: string }
interface Post { id: string; title: string }

async function loadDashboard(userId: string) {
  const [user, posts] = await Promise.all([
    fetch(`/api/users/${userId}`).then((r) => r.json() as Promise<User>),
    fetch(`/api/users/${userId}/posts`).then((r) => r.json() as Promise<Post[]>),
  ]);
  return { user, posts };
}
```

In production, validate both JSON payloads before use.


---

## Scenario — retry with Result


```typescript
type Result<T> = { ok: true; value: T } | { ok: false; error: Error };

async function retry<T>(fn: () => Promise<T>, times: number): Promise<Result<T>> {
  let last: Error = new Error("unknown");
  for (let i = 0; i < times; i++) {
    try {
      return { ok: true, value: await fn() };
    } catch (e) {
      last = e instanceof Error ? e : new Error(String(e));
    }
  }
  return { ok: false, error: last };
}
```


---

## Best Practices

- ✅ Type the success path and model errors explicitly.
- ✅ Validate JSON at boundaries — types do not exist at runtime.

---

## Common Mistakes

Watch for these patterns — they cost hours in real projects.

### Mistake 1: Promise<any>

Untyped fetch json()

Use unknown + parser or schema.

---

### Mistake 2: Swallowing errors

empty catch blocks

Log or return Result type.

---

## Interview Points

> **📌 Interview Point 1: Awaited utility?**

Unwraps Promise nested in types.

---

> **📌 Interview Point 2: Promise.all typing?**

Tuple of promises becomes tuple of results.

---

## Exercises

Practice with `npx tsc --noEmit` after each exercise.

### Exercise 11.1: delay helper ⭐

**Task:** Promise<void> delay ms.

<details><summary>💡 Hint</summary>

Simple Promise.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
```

</details>

---

### Exercise 11.2: Result type ⭐⭐

**Task:** Success | Failure union.

<details><summary>💡 Hint</summary>

Discriminated union.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type Result<T> = { ok: true; value: T } | { ok: false; error: Error };
```

</details>

---

### Exercise 11.3: fetchUser ⭐⭐⭐

**Task:** Typed JSON parse with guards.

<details><summary>💡 Hint</summary>

unknown pipeline.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function isUser(raw: unknown): raw is { id: string; name: string } {
  return typeof raw === "object" && raw !== null && "id" in raw && "name" in raw;
}
```

</details>

---

### Exercise 11.4: Promise.all ⭐⭐

**Task:** Parallel fetches typed.

<details><summary>💡 Hint</summary>

tuple inference.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
const [user, posts] = await Promise.all([fetchUser("1"), fetchPosts("1")]);
```

</details>

---

### Exercise 11.5: HttpError class ⭐⭐⭐

**Task:** Custom error with status.

<details><summary>💡 Hint</summary>

instanceof narrow.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
class HttpError extends Error {
  constructor(public status: number, message: string) {
    super(message);
  }
}
```

</details>

---

### Exercise 11.6: Abort timeout ⭐⭐

**Task:** AbortController with fetch.

<details><summary>💡 Hint</summary>

optional advanced.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
async function fetchWithTimeout(url: string, ms: number) {
  const ctrl = new AbortController();
  const id = setTimeout(() => ctrl.abort(), ms);
  try {
    return await fetch(url, { signal: ctrl.signal });
  } finally {
    clearTimeout(id);
  }
}
```

</details>

---

## Chapter Summary

You covered a lot in this chapter. Here is a concise recap:

- Async functions return Promise<T>; use Awaited for nested promises.
- Validate external JSON.

---

---

## Navigation

**⬅️ [Previous: Modules and Config](./ch10-modules-and-config.md)**  
**➡️ [Next: React with TypeScript](./ch12-react-with-typescript.md)**

---
## Quick glossary (review)

- **TypeScript** — Typed superset of JavaScript that compiles to JS.
- **Inference** — Compiler deduces types without explicit annotations.
- **Union** — Value may be one of several types: `A | B`.
- **Narrowing** — Refining a union to a specific type in a branch.
- **Generic** — Type parameter for reusable APIs.
- **Interface** — Named object shape contract.
- **Utility type** — Built-in type transformer like `Partial`.
- **Strict mode** — Bundle of safer compiler flags in tsconfig.
- **Type erasure** — Types removed in emitted JavaScript.
- **Declaration file** — `.d.ts` describing types for JS modules.
- **TypeScript** — Typed superset of JavaScript that compiles to JS.
- **Inference** — Compiler deduces types without explicit annotations.
- **Union** — Value may be one of several types: `A | B`.
- **Narrowing** — Refining a union to a specific type in a branch.
- **Generic** — Type parameter for reusable APIs.
- **Interface** — Named object shape contract.
- **Utility type** — Built-in type transformer like `Partial`.
- **Strict mode** — Bundle of safer compiler flags in tsconfig.
- **Type erasure** — Types removed in emitted JavaScript.
- **Declaration file** — `.d.ts` describing types for JS modules.
- **TypeScript** — Typed superset of JavaScript that compiles to JS.
- **Inference** — Compiler deduces types without explicit annotations.
- **Union** — Value may be one of several types: `A | B`.
- **Narrowing** — Refining a union to a specific type in a branch.
- **Generic** — Type parameter for reusable APIs.
- **Interface** — Named object shape contract.
- **Utility type** — Built-in type transformer like `Partial`.
- **Strict mode** — Bundle of safer compiler flags in tsconfig.
- **Type erasure** — Types removed in emitted JavaScript.
- **Declaration file** — `.d.ts` describing types for JS modules.
- **TypeScript** — Typed superset of JavaScript that compiles to JS.
- **Inference** — Compiler deduces types without explicit annotations.
- **Union** — Value may be one of several types: `A | B`.
- **Narrowing** — Refining a union to a specific type in a branch.
- **Generic** — Type parameter for reusable APIs.
- **Interface** — Named object shape contract.
- **Utility type** — Built-in type transformer like `Partial`.
- **Strict mode** — Bundle of safer compiler flags in tsconfig.
- **Type erasure** — Types removed in emitted JavaScript.
- **Declaration file** — `.d.ts` describing types for JS modules.
- **TypeScript** — Typed superset of JavaScript that compiles to JS.
- **Inference** — Compiler deduces types without explicit annotations.
- **Union** — Value may be one of several types: `A | B`.
- **Narrowing** — Refining a union to a specific type in a branch.
- **Generic** — Type parameter for reusable APIs.
- **Interface** — Named object shape contract.
- **Utility type** — Built-in type transformer like `Partial`.
- **Strict mode** — Bundle of safer compiler flags in tsconfig.
- **Type erasure** — Types removed in emitted JavaScript.
- **Declaration file** — `.d.ts` describing types for JS modules.
- **TypeScript** — Typed superset of JavaScript that compiles to JS.
- **Inference** — Compiler deduces types without explicit annotations.
- **Union** — Value may be one of several types: `A | B`.
- **Narrowing** — Refining a union to a specific type in a branch.
- **Generic** — Type parameter for reusable APIs.
- **Interface** — Named object shape contract.
- **Utility type** — Built-in type transformer like `Partial`.
- **Strict mode** — Bundle of safer compiler flags in tsconfig.
- **Type erasure** — Types removed in emitted JavaScript.
- **Declaration file** — `.d.ts` describing types for JS modules.
- **TypeScript** — Typed superset of JavaScript that compiles to JS.

*Last updated: 2025 | TypeScript course — CodeShelf*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
