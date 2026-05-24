---
title: Chapter 8 — Type Narrowing
description: Narrow union types with typeof, instanceof, in, equality checks, and discriminated unions.
order: 8
tags: [typescript, narrowing, type-guards, discriminated-unions]
---

# Chapter 8: Type Narrowing

## 8.1 Why narrowing matters

Union types represent multiple possibilities. **Narrowing** refines the type within a branch so TypeScript knows which members are safe to access.

```typescript
function printId(id: string | number) {
  console.log(id.toUpperCase()); // ❌ toUpperCase on string | number
}
```

After a check, the type shrinks:

```typescript
function printId(id: string | number) {
  if (typeof id === "string") {
    console.log(id.toUpperCase()); // id is string
  } else {
    console.log(id.toFixed(2));     // id is number
  }
}
```

> **Definition:** **Type narrowing** is the process by which the compiler reduces a union or broad type to a more specific type based on control-flow analysis.

## 8.2 typeof guards

Works for primitives:

| typeof result | TypeScript narrows to |
|---------------|----------------------|
| `"string"` | string |
| `"number"` | number |
| `"boolean"` | boolean |
| `"bigint"` | bigint |
| `"symbol"` | symbol |
| `"undefined"` | undefined |
| `"object"` | object \| null (caution) |
| `"function"` | function |

```typescript
function padLeft(value: string, padding: string | number) {
  if (typeof padding === "number") {
    return " ".repeat(padding) + value;
  }
  return padding + value;
}
```

**Caution:** `typeof null === "object"` in JavaScript — combine with null checks.

## 8.3 Truthiness narrowing

```typescript
function printName(name: string | null | undefined) {
  if (name) {
    console.log(name.toUpperCase()); // string
  }
}
```

Empty string `""` is falsy — may narrow incorrectly if empty string is valid.

## 8.4 Equality narrowing

```typescript
type Platform = "web" | "mobile" | "desktop";

function setPlatform(p: Platform) {
  if (p === "web") {
    // p is "web"
  }
}

function example(x: string | number, y: string | boolean) {
  if (x === y) {
    // both string here
  }
}
```

## 8.5 instanceof narrowing

For class instances:

```typescript
class Dog {
  bark() { return "woof"; }
}

class Cat {
  meow() { return "meow"; }
}

function speak(pet: Dog | Cat) {
  if (pet instanceof Dog) {
    return pet.bark();
  }
  return pet.meow();
}
```

Works with built-ins: `Date`, `Error`, `Array`, etc.

## 8.6 in operator narrowing

Check property existence on objects:

```typescript
type Fish = { swim: () => void };
type Bird = { fly: () => void };

function move(animal: Fish | Bird) {
  if ("swim" in animal) {
    animal.swim();
  } else {
    animal.fly();
  }
}
```

Useful for union of object types with distinct keys.

## 8.7 Discriminated unions (tagged unions)

> **Definition:** A **discriminated union** is a union of object types sharing a common **discriminant** property (usually `kind`, `type`, or `status`) with literal values.

```typescript
type Circle = { kind: "circle"; radius: number };
type Square = { kind: "square"; side: number };
type Rectangle = { kind: "rectangle"; width: number; height: number };

type Shape = Circle | Square | Rectangle;

function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.side ** 2;
    case "rectangle":
      return shape.width * shape.height;
  }
}
```

TypeScript narrows `shape` in each `case` automatically.

### API result pattern

```typescript
type ApiSuccess<T> = { ok: true; data: T };
type ApiFailure = { ok: false; error: { code: string; message: string } };
type ApiResult<T> = ApiSuccess<T> | ApiFailure;

async function handle<T>(result: ApiResult<T>) {
  if (result.ok) {
    console.log(result.data); // success branch
  } else {
    console.error(result.error.message); // failure branch
  }
}
```

## 8.8 User-defined type guards

Function that returns `predicate is Type`:

```typescript
interface User {
  id: string;
  name: string;
}

function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "name" in value &&
    typeof (value as User).id === "string" &&
    typeof (value as User).name === "string"
  );
}

function process(input: unknown) {
  if (isUser(input)) {
    console.log(input.name); // User
  }
}
```

Return type `value is User` tells the compiler about narrowing.

## 8.9 Assertion functions

```typescript
function assertIsNumber(value: unknown): asserts value is number {
  if (typeof value !== "number") {
    throw new Error("Expected number");
  }
}

function double(n: unknown) {
  assertIsNumber(n);
  return n * 2; // n is number
}
```

## 8.10 Control flow analysis

TypeScript tracks assignments across branches:

```typescript
function example(x: string | number) {
  let val = x;
  if (typeof val === "string") {
    val = val.trim();
    return val.length;
  }
  return val.toFixed(0);
}
```

### Assignments in else

```typescript
let message: string | undefined;
if (Math.random() > 0.5) {
  message = "hello";
} else {
  message = "world";
}
// message is string (not undefined)
```

## 8.11 never for exhaustiveness

```typescript
function assertNever(x: never): never {
  throw new Error(`Unexpected: ${x}`);
}

type Action =
  | { type: "increment"; amount: number }
  | { type: "reset" };

function reducer(state: number, action: Action): number {
  switch (action.type) {
    case "increment":
      return state + action.amount;
    case "reset":
      return 0;
    default:
      return assertNever(action);
  }
}
```

Adding a new action type without handling it causes a compile error.

## 8.12 Narrowing with arrays and filters

```typescript
const mixed: (string | null)[] = ["a", null, "b"];

const strings = mixed.filter((x): x is string => x !== null);
// strings: string[]
```

Without type predicate, filter returns `(string | null)[]`.

## 8.13 Common mistakes

| Mistake | Fix |
|---------|-----|
| Assuming narrowed variable stays narrow | Re-check after async gaps |
| Missing discriminant on union | Add shared literal property |
| Cast instead of guard (`as User`) | Prefer type guard functions |
| typeof for arrays | Use `Array.isArray()` |
| Overlapping union members | Redesign discriminant |

> **Key takeaway:** Use `typeof`, `instanceof`, `in`, and discriminated unions to let the compiler understand your branches. Prefer type guards over blind assertions for `unknown` data.

## Practice Exercise — Chapter 8

```text
Exercise 8.1: Shape calculator
  a) Define Triangle discriminant union member.
  b) Extend area() and verify exhaustiveness with assertNever.

Exercise 8.2: Type guard
  a) isNonEmptyString(value: unknown): value is string.
  b) Use in validateForm before processing.

Exercise 8.3: API results
  a) Model PaginatedResult<T> success vs ErrorResult failure.
  b) Write renderResult that branches on discriminant.

Exercise 8.4: filter predicate
  a) Array<number | undefined | null> → number[] with typed filter.
  b) Compare with and without type predicate.
```

Next: [Chapter 9 — Enums & Literals](./ch09-enums-and-literals.md).
