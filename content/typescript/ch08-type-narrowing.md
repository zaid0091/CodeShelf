---
title: Chapter 8 — Type Narrowing
description: typeof, instanceof, in, equality, discriminated unions, and type predicates.
order: 8
tags: [typescript, narrowing, type-guards, discriminated-unions]
---


# Chapter 8: Type Narrowing

> **Unions are only useful if you can safely narrow them. This chapter teaches control-flow analysis and user-defined type guards.**
> Take your time with each section. TypeScript rewards patience — read compiler errors carefully and experiment in a small project as you go.

---


## Table of Contents

1. [Why Narrowing](#why-narrowing)
2. [typeof guards](#typeof-guards)
3. [Truthiness](#truthiness)
4. [Equality Narrowing](#equality-narrowing)
5. [instanceof](#instanceof)
6. [in Operator](#in-operator)
7. [Discriminated Unions](#discriminated-unions)
8. [Type Predicates](#type-predicates)
9. [asserts](#asserts)
10. [assertNever](#assertnever)
11. [Best Practices](#best-practices)
12. [Interview Points](#interview-points)
13. [Exercises](#exercises)
14. [Chapter Summary](#chapter-summary)

---

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
<!-- codeshelf:generated-appendix -->

---

## Narrowing — control-flow analysis

TypeScript tracks types through `if`, `switch`, `return`, and `throw`:

```typescript
function printId(id: string | number) {
  if (typeof id === "string") {
    console.log(id.toUpperCase());
    return;
  }
  console.log(id.toFixed(0));
}
```

After the `typeof` check, each branch has a **narrower** type.

---

## Discriminated unions — state machines

```typescript
type RequestState =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: string }
  | { status: "error"; message: string };

function render(state: RequestState) {
  switch (state.status) {
    case "idle": return "Click load";
    case "loading": return "Loading…";
    case "success": return state.data;
    case "error": return state.message;
  }
}
```

The `status` field is the **discriminant** — TypeScript knows which other fields exist in each branch.

---

## Discriminated union — full example


```typescript
type Payment =
  | { method: "card"; last4: string }
  | { method: "paypal"; email: string }
  | { method: "cash" };

function charge(p: Payment): number {
  switch (p.method) {
    case "card":
      return 100;
    case "paypal":
      return 100;
    case "cash":
      return 100;
    default:
      const _x: never = p;
      return _x;
  }
}
```


---

## typeof and truthiness narrowing


```typescript
function print(value: string | number) {
  if (typeof value === "string") {
    console.log(value.toUpperCase());
  } else {
    console.log(value.toFixed(2));
  }
}
```


---

## Type predicates


```typescript
interface Fish { swim: () => void }
interface Bird { fly: () => void }

function isFish(pet: Fish | Bird): pet is Fish {
  return (pet as Fish).swim !== undefined;
}
```


---

## asserts keyword


```typescript
function assertIsNumber(value: unknown): asserts value is number {
  if (typeof value !== "number") throw new Error("Not a number");
}
```


---

## Equality narrowing


```typescript
function example(x: string | number, y: string | number) {
  if (x === y) {
    // x and y narrowed together when comparable
  }
}
```


---

## in operator


```typescript
if ("swim" in pet) pet.swim();
```


---

## Exhaustiveness helper


```typescript
function assertNever(x: never): never {
  throw new Error(`Unexpected: ${JSON.stringify(x)}`);
}
```


---

## Definition — Type guard

> **Definition:** **Type guard** — An expression that refines a type in a branch — `typeof`, `instanceof`, `in`, or a custom `x is T` predicate.


---

## Discriminated union — loading state


```typescript
type State =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: string[] }
  | { status: "error"; message: string };

function render(state: State) {
  switch (state.status) {
    case "idle": return "Press load";
    case "loading": return "Loading…";
    case "success": return state.data.join(", ");
    case "error": return state.message;
  }
}
```


---

## Type predicate exercise explained


```typescript
function isError(value: unknown): value is Error {
  return value instanceof Error;
}
```
After `if (isError(e))`, `e` is `Error` inside the block.


---

## Truthiness narrowing


```typescript
function printName(name: string | null | undefined) {
  if (!name) return;
  console.log(name.toUpperCase()); // string
}
```


---

## Review Q1

**Q:** Does `Array.isArray` narrow? **A:** Yes — narrows to `any[]` in older TS; prefer `Array.isArray` + generic guards for typed arrays.

---

## Review Q2

**Q:** What is exhaustiveness checking? **A:** Assigning the union to `never` in `default` when all cases handled.

---

## Scenario — payment union


```typescript
type Payment =
  | { kind: "card"; last4: string }
  | { kind: "paypal"; email: string }
  | { kind: "invoice"; poNumber: string };

function describe(p: Payment): string {
  switch (p.kind) {
    case "card": return `Card ending ${p.last4}`;
    case "paypal": return `PayPal ${p.email}`;
    case "invoice": return `PO ${p.poNumber}`;
    default:
      return assertNever(p);
  }
}

function assertNever(x: never): never {
  throw new Error(`Unhandled: ${JSON.stringify(x)}`);
}
```


---

## Best Practices

- ✅ Use discriminated unions with a literal `kind` or `type` field.
- ✅ Avoid single boolean flags for complex state — use unions.

---

## Common Mistakes

Watch for these patterns — they cost hours in real projects.

### Mistake 1: Cast instead of narrow

`as User` without checks

Validate then narrow.

---

### Mistake 2: Forgotten default in switch

Missing case when union grows

Use `never` exhaustiveness.

---

## Interview Points

> **📌 Interview Point 1: What is a type predicate?**

`function isUser(x): x is User`.

---

> **📌 Interview Point 2: Discriminated union?**

Union members share a discriminant literal field.

---

## Exercises

Practice with `npx tsc --noEmit` after each exercise.

### Exercise 8.1: typeof pad ⭐

**Task:** Pad string or number.

<details><summary>💡 Hint</summary>

typeof branches.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function pad(value: string | number, len: number): string {
  const s = typeof value === "string" ? value : String(value);
  return s.padStart(len, "0");
}
```

</details>

---

### Exercise 8.2: ApiResult ⭐⭐

**Task:** Handle success vs failure branches.

<details><summary>💡 Hint</summary>

Discriminated union.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type ApiResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };

function handle<T>(r: ApiResult<T>): T {
  if (!r.ok) throw new Error(r.error);
  return r.data;
}
```

</details>

---

### Exercise 8.3: isUser guard ⭐⭐⭐

**Task:** User-defined type guard.

<details><summary>💡 Hint</summary>

predicate syntax.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
interface User { id: string; name: string }
function isUser(x: unknown): x is User {
  return typeof x === "object" && x !== null && "id" in x && "name" in x;
}
```

</details>

---

### Exercise 8.4: assertNever ⭐⭐

**Task:** Add case and fix exhaustiveness.

<details><summary>💡 Hint</summary>

never type.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function assertNever(x: never): never {
  throw new Error(`Unexpected: ${JSON.stringify(x)}`);
}
```

</details>

---

### Exercise 8.5: filter predicate ⭐⭐⭐

**Task:** Array filter with type predicate.

<details><summary>💡 Hint</summary>

T[] narrow.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function isString(x: unknown): x is string {
  return typeof x === "string";
}
const words = ["a", 1, "b"].filter(isString); // string[]
```

</details>

---

### Exercise 8.6: in operator ⭐⭐

**Task:** Fish vs Bird with in.

<details><summary>💡 Hint</summary>

Property check.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
interface Fish { swim(): void }
interface Bird { fly(): void }
function move(pet: Fish | Bird) {
  if ("swim" in pet) pet.swim();
  else pet.fly();
}
```

</details>

---

## Chapter Summary

You covered a lot in this chapter. Here is a concise recap:

- Narrowing refines types within control flow.
- Discriminated unions scale best.

---

---

## Navigation

**⬅️ [Previous: Classes and OOP](./ch07-classes-and-oop.md)**  
**➡️ [Next: Enums and Literals](./ch09-enums-and-literals.md)**

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

*Last updated: 2025 | TypeScript course — CodeShelf*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
