---
title: Chapter 11 — Async TypeScript
description: Typing Promises, async/await, error handling, fetch responses, and concurrent patterns.
order: 11
tags: [typescript, async, promises, await, fetch]
---

# Chapter 11: Async TypeScript

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

## Practice Exercise — Chapter 11

```text
Exercise 11.1: Typed API client
  a) createClient(baseUrl: string) returning get/post methods.
  b) Generic get<T>(path: string): Promise<T> with parse step.

Exercise 11.2: Result wrapper
  a) Wrap fetch in Result<T, HttpError>.
  b) Caller switches on ok without try/catch.

Exercise 11.3: Parallel loading
  a) Load user, settings, notifications in parallel.
  b) Type destructure tuple from Promise.all.

Exercise 11.4: Retry
  a) async function retry<T>(fn: () => Promise<T>, attempts: number): Promise<T>.
  b) Exponential backoff optional stretch goal.
```

Next: [Chapter 12 — React with TypeScript](./ch12-react-with-typescript.md).
