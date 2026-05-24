---
title: Chapter 5 — Generics
description: Generic functions, classes, constraints, default type parameters, and reusable typed patterns.
order: 5
tags: [typescript, generics, constraints, patterns]
---

# Chapter 5: Generics

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

## Practice Exercise — Chapter 5

```text
Exercise 5.1: Repository sketch
  a) Interface Repository<T extends { id: string }> with findById, save, delete.
  b) Implement InMemoryRepository<T> with a Map.
  c) Test with User and Product types.

Exercise 5.2: Constraints
  a) Write max<T extends number | string>(a: T, b: T): T using comparison.
  b) Write pluck<T, K extends keyof T>(items: T[], key: K): T[K][].

Exercise 5.3: Defaults
  a) type ApiResult<T = void, E = string> for success/error union.
  b) Use default void for mutations that return no data.

Exercise 5.4: compose
  a) Implement compose<A, B, C>(f: (b: B) => C, g: (a: A) => B): (a: A) => C.
  b) Chain three functions with inferred types end-to-end.
```

Next: [Chapter 6 — Utility Types](./ch06-utility-types.md).
