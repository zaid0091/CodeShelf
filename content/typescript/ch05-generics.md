---
title: Chapter 5 — Generics
description: Generic functions, classes, constraints, defaults, and reusable patterns.
order: 5
tags: [typescript, generics, constraints, patterns]
---


# Chapter 5: Generics

> **Generics let you write reusable code without losing type information. This chapter covers functions, classes, constraints, and common patterns.**
> Take your time with each section. TypeScript rewards patience — read compiler errors carefully and experiment in a small project as you go.

---


## Table of Contents

1. [Why Generics](#why-generics)
2. [Generic Functions](#generic-functions)
3. [Generic Interfaces](#generic-interfaces)
4. [Generic Classes](#generic-classes)
5. [Constraints with extends](#constraints-with-extends)
6. [keyof and getProperty](#keyof-and-getproperty)
7. [Default Type Parameters](#default-type-parameters)
8. [Generic Utilities Preview](#generic-utilities-preview)
9. [Variance Note](#variance-note)
10. [Best Practices](#best-practices)
11. [Common Mistakes](#common-mistakes)
12. [Interview Points](#interview-points)
13. [Exercises](#exercises)
14. [Chapter Summary](#chapter-summary)

---

## 5.1 The problem generics solve

Without generics, you choose between duplication and loss of type information:

```typescript
function wrapString(value: string): { value: string } {
  return { value };
}

function wrapNumber(value: number): { value: number } {
  return { value };
}

// Or lose safety:
function wrapAny(value: any): { value: any } {
  return { value };
}
```

Generics parameterize types — one implementation, many concrete types:

```typescript
function wrap<T>(value: T): { value: T } {
  return { value };
}

const a = wrap("hello"); // { value: string }
const b = wrap(42);      // { value: number }
```

> **Definition:** **Generics** are type parameters (often `T`, `U`, `K`, `V`) that let functions, interfaces, and classes work over a variety of types while preserving relationships between inputs and outputs.

## 5.2 Generic functions

```typescript
function first<T>(items: T[]): T | undefined {
  return items[0];
}

function pair<T, U>(a: T, b: U): [T, U] {
  return [a, b];
}

const head = first(["a", "b"]);     // string | undefined
const p = pair(1, true);            // [number, boolean]
```

### Explicit type arguments

Usually inferred; specify when the compiler cannot:

```typescript
const empty = first<number>([]); // number | undefined
const data = JSON.parse('[]') as unknown;
// const bad = first(data); // might infer wrong — specify:
const nums = first<number>(data as number[]);
```

## 5.3 Generic interfaces and type aliases

```typescript
interface Box<T> {
  value: T;
  getValue(): T;
}

type Result<T, E = Error> =
  | { success: true; data: T }
  | { success: false; error: E };

const ok: Result<string> = { success: true, data: "done" };
```

## 5.4 Generic constraints

Limit `T` to types that satisfy a requirement:

```typescript
interface HasLength {
  length: number;
}

function logLength<T extends HasLength>(item: T): number {
  console.log(item.length);
  return item.length;
}

logLength("hello");     // ✅
logLength([1, 2, 3]);   // ✅
// logLength(42);       // ❌ number has no .length
```

### keyof constraint

```typescript
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = { id: 1, name: "Ada" };
const name = getProperty(user, "name"); // string
// getProperty(user, "age"); // ❌
```

## 5.5 Multiple constraints

```typescript
interface Named {
  name: string;
}

interface Aged {
  age: number;
}

function describe<T extends Named & Aged>(person: T): string {
  return `${person.name} is ${person.age}`;
}
```

## 5.6 Default type parameters

```typescript
interface ApiResponse<T = unknown> {
  data: T;
  status: number;
}

interface Paginated<T, PageSize extends number = 20> {
  items: T[];
  pageSize: PageSize;
}
```

Defaults reduce boilerplate when the common case is known.

## 5.7 Generic classes

```typescript
class Stack<T> {
  private items: T[] = [];

  push(item: T): void {
    this.items.push(item);
  }

  pop(): T | undefined {
    return this.items.pop();
  }

  peek(): T | undefined {
    return this.items[this.items.length - 1];
  }
}

const numStack = new Stack<number>();
numStack.push(1);
```

See [Chapter 7](./ch07-classes-and-oop.md) for access modifiers and inheritance.

## 5.8 Generic utility patterns

### Identity and pipeline

```typescript
const identity = <T>(x: T): T => x;

function pipe<A, B, C>(a: A, ab: (x: A) => B, bc: (x: B) => C): C {
  return bc(ab(a));
}
```

### Memoize (sketch)

```typescript
function memoize<TArgs extends unknown[], TResult>(
  fn: (...args: TArgs) => TResult
): (...args: TArgs) => TResult {
  const cache = new Map<string, TResult>();
  return (...args: TArgs) => {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key)!;
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}
```

### Factory with inference

```typescript
function createStore<T>(initial: T) {
  let state = initial;
  return {
    get: (): T => state,
    set: (next: T): void => {
      state = next;
    },
  };
}

const countStore = createStore(0);
countStore.set(5); // ✅
// countStore.set("x"); // ❌
```

## 5.9 Generics with conditional types (preview)

```typescript
type UnwrapPromise<T> = T extends Promise<infer U> ? U : T;

type A = UnwrapPromise<Promise<string>>; // string
type B = UnwrapPromise<number>;          // number
```

Built-in utilities in [Chapter 6](./ch06-utility-types.md) use similar machinery.

## 5.10 Variance and safety (conceptual)

Generics preserve relationships:

```typescript
function map<T, U>(items: T[], fn: (item: T) => U): U[] {
  return items.map(fn);
}

const lengths = map(["a", "bb"], (s) => s.length); // number[]
```

If `fn` returned `any`, you would lose output typing — avoid `any` in generic callbacks.

## 5.11 Common generic naming conventions

| Parameter | Typical use |
|-----------|-------------|
| `T` | General type |
| `U`, `V` | Second, third type |
| `K` | Key (often `extends string \| number \| symbol`) |
| `V` | Value |
| `E` | Element or Error |
| `P`, `R` | Payload, Response |

## 5.12 Pitfalls

| Pitfall | Solution |
|---------|----------|
| Over-generic simple functions | Use concrete types until reuse is needed |
| `T extends any` | Use `unknown` or proper constraint |
| Too many type params | Split into helper types |
| Generic arrow in `.tsx` | Add trailing comma: `<T,>(x: T) => x` |
| Erasing with `as any` | Fix constraint or overload |

> **Key takeaway:** Generics let you write reusable, type-safe abstractions. Start with simple `<T>` functions, add `extends` constraints when you need property access, and let inference do the work.
<!-- codeshelf:generated-appendix -->

---

## Why generics beat duplication

Without generics you copy-paste the same logic:

```typescript
function firstString(arr: string[]): string | undefined { return arr[0]; }
function firstNumber(arr: number[]): number | undefined { return arr[0]; }
```

With generics, one implementation serves all:

```typescript
function first<T>(arr: T[]): T | undefined { return arr[0]; }
```

The compiler **specializes** `T` per call site — no runtime cost.

---

## Generics — the reusable box

Without generics, you choose between duplication and losing type info:

```typescript
// Loses info:
function firstAny(arr: any[]): any { return arr[0]; }

// Keeps info:
function first<T>(arr: T[]): T | undefined { return arr[0]; }

const n = first([1, 2, 3]); // number | undefined
```

`T` is a **placeholder** filled in when you call the function.

---

## Constraints — generics with rules

```typescript
interface HasLength { length: number }

function logLength<T extends HasLength>(item: T): void {
  console.log(item.length);
}

logLength("hi");
logLength([1, 2]);
// logLength(42); // Error — number has no .length
```

---

## Generic interfaces — API wrappers

```typescript
interface ApiResponse<T> {
  data: T;
  meta: { page: number; total: number };
}

type UserList = ApiResponse<User[]>;
```

---

## Generic constraints in practice


```typescript
interface Identifiable { id: string }

function findById<T extends Identifiable>(items: T[], id: string): T | undefined {
  return items.find((item) => item.id === id);
}
```


---

## Generic defaults


```typescript
interface ApiResponse<T = unknown> {
  data: T;
  status: number;
}

type UserResponse = ApiResponse<User>;
type UnknownResponse = ApiResponse; // T = unknown
```


---

## Generic Stack class


```typescript
class Stack<T> {
  private items: T[] = [];
  push(item: T): void { this.items.push(item); }
  pop(): T | undefined { return this.items.pop(); }
  peek(): T | undefined { return this.items[this.items.length - 1]; }
}
```


---

## keyof and typeof constraints


```typescript
function pluck<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = { id: "1", name: "Ada" };
const n = pluck(user, "name"); // string
```


---

## Conditional types preview


```typescript
type Unwrap<T> = T extends Promise<infer U> ? U : T;
type A = Unwrap<Promise<string>>; // string
```


---

## Generic constraints in APIs


```typescript
interface Identifiable { id: string }
function indexById<T extends Identifiable>(items: T[]): Record<string, T> {
  return Object.fromEntries(items.map((i) => [i.id, i]));
}
```


---

## Multiple type parameters


```typescript
function pair<T, U>(first: T, second: U): [T, U] {
  return [first, second];
}
```


---

## Generic type aliases


```typescript
type Nullable<T> = T | null;
type ApiResult<T> = { ok: true; data: T } | { ok: false; error: string };
```


---

## Definition — Type parameter

> **Definition:** **Type parameter** — A placeholder type (often `T`) filled in when you call a generic function or instantiate a generic class.


---

## Analogy — labeled boxes


Generics are shipping boxes with **labels** (`T`) instead of writing "box for books" and "box for shoes" as separate functions.

One factory function `box<T>(item: T): T[]` works for any item type.


---

## Worked example — repository


```typescript
interface Entity { id: string }

class MemoryRepo<T extends Entity> {
  private store = new Map<string, T>();

  save(entity: T): void {
    this.store.set(entity.id, entity);
  }

  findById(id: string): T | undefined {
    return this.store.get(id);
  }
}
```


---

## keyof in practice


```typescript
function pick<T, K extends keyof T>(obj: T, keys: K[]): Pick<T, K> {
  const result = {} as Pick<T, K>;
  for (const key of keys) {
    result[key] = obj[key];
  }
  return result;
}
```


---

## Inference with generics


```typescript
const ids = [1, 2, 3];
const firstId = ids.map((n) => n * 2); // number[] — T inferred
```


---

## Generic constraints — real API


```typescript
function sortBy<T extends { createdAt: Date }>(items: T[]): T[] {
  return [...items].sort((a, b) => a.createdAt.getTime() - b.createdAt.getTime());
}
```


---

## Common mistakes


| Mistake | Fix |
|---------|-----|
| `function f<T = any>` | Default to `unknown` or omit default |
| Too many type params | Use options object type |
| Casting inside generic | Use constraints + narrowing |


---

## Review Q1

**Q:** Can you use `any` as a generic constraint? **A:** Technically yes, but it defeats the purpose — use `extends unknown` or a meaningful interface.

---

## Review Q2

**Q:** What is `T extends keyof U` used for? **A:** Safe property access — `getProperty(obj, key)` patterns.

---

## Review Q3

**Q:** Do generics exist at runtime? **A:** No — they are erased like all types.

---

## Review Q4

**Q:** What is a default type parameter? **A:** `interface Box<T = string>` uses `string` when `T` is not specified.

---

## Scenario — typed event bus


```typescript
type Events = {
  login: { userId: string };
  logout: { userId: string };
  error: { message: string };
};

class TypedEmitter {
  private listeners: { [K in keyof Events]?: Array<(p: Events[K]) => void> } = {};

  on<K extends keyof Events>(event: K, fn: (payload: Events[K]) => void) {
    (this.listeners[event] ??= []).push(fn);
  }

  emit<K extends keyof Events>(event: K, payload: Events[K]) {
    this.listeners[event]?.forEach((fn) => fn(payload));
  }
}
```


---

## Best Practices

- ✅ Name type parameters meaningfully: `T` ok for one param; use `TItem` in complex APIs.
- ✅ Use constraints instead of `any` inside generics.

---

## Common Mistakes

Watch for these patterns — they cost hours in real projects.

### Mistake 1: Too many type params

`function f<T, U, V, W>`

Simplify or use an options object type.

---

### Mistake 2: Constraint too loose

`T extends object`

Use `extends HasId` or specific interface.

---

## Interview Points

> **📌 Interview Point 1: What is a generic?**

Type parameter placeholder resolved at call site.

---

> **📌 Interview Point 2: What is `extends` in generics?**

Constraint — T must satisfy a shape.

---

## Exercises

Practice with `npx tsc --noEmit` after each exercise.

### Exercise 5.1: identity<T> ⭐

**Task:** Implement generic identity function.

<details><summary>💡 Hint</summary>

Simplest generic.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function identity<T>(value: T): T {
  return value;
}
```

</details>

---

### Exercise 5.2: getProperty ⭐⭐

**Task:** Use `keyof T` safe property access.

<details><summary>💡 Hint</summary>

Constraint pattern.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
```

</details>

---

### Exercise 5.3: Stack class ⭐⭐⭐

**Task:** Generic `Stack<T>` with push/pop.

<details><summary>💡 Hint</summary>

Generic class.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
class Stack<T> {
  private items: T[] = [];
  push(item: T) { this.items.push(item); }
  pop(): T | undefined { return this.items.pop(); }
}
```

</details>

---

### Exercise 5.4: Default generic ⭐⭐

**Task:** ApiResponse with default `T = unknown`.

<details><summary>💡 Hint</summary>

Default type param.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
interface ApiResponse<T = unknown> {
  data: T;
  status: number;
}
```

</details>

---

### Exercise 5.5: Memoize ⭐⭐⭐

**Task:** Typed memoize for unary functions.

<details><summary>💡 Hint</summary>

Higher-order generic.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function memoize<A extends unknown[], R>(fn: (...args: A) => R): (...args: A) => R {
  const cache = new Map<string, R>();
  return (...args: A) => {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key)!;
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}
```

</details>

---

### Exercise 5.6: Constraint merge ⭐⭐

**Task:** T extends A & B.

<details><summary>💡 Hint</summary>

Intersection constraint.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function merge<T extends object, U extends object>(a: T, b: U): T & U {
  return { ...a, ...b };
}
```

</details>

---

## Chapter Summary

You covered a lot in this chapter. Here is a concise recap:

- Generics preserve type information across reuse.
- Constraints limit type parameters safely.

---

---

## Navigation

**⬅️ [Previous: Functions](./ch04-functions.md)**  
**➡️ [Next: Utility Types](./ch06-utility-types.md)**

---

*Last updated: 2025 | TypeScript course — CodeShelf*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
