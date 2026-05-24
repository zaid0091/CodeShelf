---
title: Chapter 2 — Types and Primitives
description: Primitive types, arrays, tuples, any, unknown, void, never, and type annotations in TypeScript.
order: 2
tags: [typescript, types, primitives, any, unknown]
---


# Chapter 2: Types and Primitives

> **Every value in TypeScript has a type. This chapter builds your foundation — primitives, arrays, tuples, unions, and the special types `any`, `unknown`, `void`, and `never`.**
> Take your time with each section. TypeScript rewards patience — read compiler errors carefully and experiment in a small project as you go.

---


## Table of Contents

1. [The Type System at a Glance](#the-type-system-at-a-glance)
2. [Primitive Types](#primitive-types)
3. [string, number, boolean](#string-number-boolean)
4. [null and undefined](#null-and-undefined)
5. [Type Annotations vs Inference](#type-annotations-vs-inference)
6. [Arrays](#arrays)
7. [Tuples](#tuples)
8. [The object Type](#the-object-type)
9. [Union Types](#union-types)
10. [any — Escape Hatch](#any-escape-hatch)
11. [unknown — Type-Safe Top Type](#unknown-type-safe-top-type)
12. [void](#void)
13. [never](#never)
14. [Literal Types](#literal-types)
15. [Type Aliases for Primitives](#type-aliases-for-primitives)
16. [Summary Table](#summary-table)
17. [Best Practices](#best-practices)
18. [Common Mistakes](#common-mistakes)
19. [Interview Points](#interview-points)
20. [Exercises](#exercises)
21. [Chapter Summary](#chapter-summary)

---

## 2.1 The type system at a glance

Every value in TypeScript has a type. Types describe **what operations are allowed** on a value and **what shape** complex values must have.

```text
Value          →  Type           →  Allowed operations
──────────────────────────────────────────────────────
42             →  number         →  +, -, *, /, toFixed()
"hello"        →  string         →  .length, .toUpperCase()
true           →  boolean        →  &&, ||, !
[1, 2, 3]        →  number[]       →  .push(), .map()
{ x: 1 }         →  { x: number }  →  .x access
```

> **Definition:** A **type** is a compile-time label describing the set of values a variable, parameter, or expression can hold, and the members available on that value.

This chapter covers **primitive and special types**. Object shapes are covered in [Chapter 3](./ch03-interfaces-and-type-aliases.md).

## 2.2 Primitive types

JavaScript has seven primitive types; TypeScript models them explicitly.

| TypeScript type | JavaScript typeof | Examples |
|-----------------|-------------------|----------|
| `string` | `"string"` | `"hello"`, `'world'`, `` `hi` `` |
| `number` | `"number"` | `42`, `3.14`, `NaN`, `Infinity` |
| `boolean` | `"boolean"` | `true`, `false` |
| `bigint` | `"bigint"` | `100n`, `BigInt(100)` |
| `symbol` | `"symbol"` | `Symbol("id")` |
| `null` | `"object"` (JS quirk) | `null` |
| `undefined` | `"undefined"` | `undefined` |

### string

```typescript
let title: string = "CodeShelf";
let multiline: string = `Line 1
Line 2`;

function shout(msg: string): string {
  return msg.toUpperCase();
}
```

### number

TypeScript uses a single `number` type for integers and floats (IEEE 754 double).

```typescript
let count: number = 10;
let price: number = 19.99;
let hex: number = 0xff;
let binary: number = 0b1010;

// Prefer bigint for very large integers:
let big: bigint = 9007199254740991n;
```

### boolean

```typescript
let isActive: boolean = true;
let hasPermission: boolean = false;

function isAdult(age: number): boolean {
  return age >= 18;
}
```

### null and undefined

Both represent "absence" but mean different things:

| Value | Typical meaning |
|-------|-----------------|
| `undefined` | Not yet assigned, optional property missing |
| `null` | Intentionally empty |

```typescript
let notSet: undefined = undefined;
let empty: null = null;

// With strictNullChecks (default in strict mode):
let name: string = null;      // ❌ unless name: string | null
let nameOrNull: string | null = null; // ✅
```

> **Key takeaway:** With `strictNullChecks`, `null` and `undefined` are not assignable to other types unless you explicitly include them in a union.

## 2.3 Type annotations vs inference

```typescript
// Explicit annotation
let id: number = 1;

// Inference (preferred when obvious)
let idInferred = 1; // number

// Annotation needed when declaration has no initializer
let futureScore: number;

// Annotation needed when you want a wider/narrower type than inference
let direction: "north" | "south" = "north";
```

| Situation | Recommendation |
|-----------|----------------|
| Simple literals | Let inference work |
| Function parameters | Always annotate (or infer from context) |
| Public API / exports | Annotate return types for clarity |
| `any` creeping in | Annotate to force correctness |

## 2.4 Arrays

Two equivalent syntaxes:

```typescript
let nums: number[] = [1, 2, 3];
let tags: Array<string> = ["ts", "js"];

// Readonly arrays
let frozen: readonly number[] = [1, 2, 3];
// frozen.push(4); // ❌
```

### Array methods preserve element type

```typescript
const doubled = [1, 2, 3].map(n => n * 2); // number[]
const names = ["a", "b"].filter(Boolean);   // string[] (with proper guards)
```

## 2.5 Tuples

Fixed-length arrays with typed positions:

```typescript
type Point = [number, number];
const origin: Point = [0, 0];

type HttpResult = [status: number, body: string];
const response: HttpResult = [200, "OK"];

// Optional tuple elements
type OptionalPair = [string, number?];
const pair: OptionalPair = ["only string"];
```

Use tuples when order and length matter (coordinates, `[key, value]` pairs from `Object.entries`).

## 2.6 The `object` type

`object` means any non-primitive value — rarely useful alone:

```typescript
let obj: object = { x: 1 };
let arr: object = [1, 2];
// obj.x; // ❌ Property 'x' does not exist on type 'object'
```

Prefer specific interfaces or type aliases instead ([Chapter 3](./ch03-interfaces-and-type-aliases.md)).

## 2.7 Union types

A value can be one of several types:

```typescript
type Id = string | number;

function printId(id: Id) {
  console.log(`ID: ${id}`);
}

printId(101);
printId("abc-101");
...  // narrowing covered in Chapter 8
```

Common unions:

```typescript
type Status = "pending" | "approved" | "rejected";
type MaybeString = string | null | undefined;
type Result = { ok: true; data: string } | { ok: false; error: string };
```

## 2.8 `any` — escape hatch (avoid)

> **Definition:** **`any`** disables type checking for a value. Anything can be assigned to `any`, and `any` can be assigned to anything.

```typescript
let value: any = 42;
value = "hello";
value.foo.bar(); // No compile error — may crash at runtime!
```

| When people use `any` | Better alternative |
|-----------------------|-------------------|
| Unknown API response | `unknown` + narrowing |
| Dynamic JSON | Validate with zod/io-ts or type guards |
| Migrating legacy JS | `unknown` or gradual typing |

```typescript
// eslint rule @typescript-eslint/no-explicit-any helps teams ban this
```

> **Key takeaway:** Treat `any` as a last resort. It removes TypeScript's benefits for that value and often spreads to neighboring code.

## 2.9 `unknown` — type-safe top type

> **Definition:** **`unknown`** accepts any value but requires you to narrow or assert before use.

```typescript
function parseJson(input: string): unknown {
  return JSON.parse(input);
}

const data = parseJson('{"name":"Ada"}');

// data.name; // ❌ Object is of type 'unknown'

if (typeof data === "object" && data !== null && "name" in data) {
  const name = (data as { name: string }).name;
  console.log(name);
}
```

Comparison:

| | `any` | `unknown` |
|---|-------|-----------|
| Assign anything to it | ✅ | ✅ |
| Assign to other types without check | ✅ | ❌ |
| Call methods / access props | ✅ | ❌ until narrowed |
| Safe default for external data | ❌ | ✅ |

## 2.10 `void`

> **Definition:** **`void`** represents the absence of a **useful return value** — typically `undefined` from functions that only perform side effects.

```typescript
function logMessage(msg: string): void {
  console.log(msg);
  // return undefined; // implicit
}

// void as parameter type (unusual — used in generic constraints)
type VoidFn = () => void;
```

Do not confuse `void` with "returns nothing at runtime" — it often returns `undefined`.

## 2.11 `never`

> **Definition:** **`never`** is the type of values that **never occur** — functions that always throw or never finish.

```typescript
function fail(message: string): never {
  throw new Error(message);
}

function infiniteLoop(): never {
  while (true) {}
}

// Exhaustiveness checking in switch:
type Shape = "circle" | "square";

function area(shape: Shape): number {
  switch (shape) {
    case "circle":
      return Math.PI * 1;
    case "square":
      return 1;
    default:
      const _exhaustive: never = shape;
      throw new Error(`Unhandled shape: ${_exhaustive}`);
  }
}
```

If you add `"triangle"` to `Shape` without updating `area`, TypeScript errors on the `never` assignment.

## 2.12 Literal types

Specific values as types:

```typescript
let one: 1 = 1;
// one = 2; // ❌

type Direction = "north" | "east" | "south" | "west";
let heading: Direction = "north";
```

Literal types combine with unions for enums-like behavior ([Chapter 9](./ch09-enums-and-literals.md)).

## 2.13 Type aliases for primitives

```typescript
type UserId = string;
type Age = number;
type IsVerified = boolean;

function getUser(id: UserId): { id: UserId; age: Age } {
  return { id, age: 30 };
}
```

Semantic aliases document intent; they are structurally identical to their base type (no nominal typing unless branded — see [Chapter 13](./ch13-best-practices.md)).

## 2.14 Summary table — special types

| Type | Meaning | Assignable from | Typical use |
|------|---------|-----------------|-------------|
| `any` | Opt out of checking | Everything | Legacy migration (avoid) |
| `unknown` | Top type, must narrow | Everything | External/untrusted data |
| `void` | No return value | `undefined` | Side-effect functions |
| `never` | Impossible value | Nothing (except never) | Throws, infinite loops, exhaustiveness |
| `null` | Intentional absence | `null` | Nullable fields |
| `undefined` | Missing value | `undefined` | Optional params/props |

> **Key takeaway:** Master `string`, `number`, `boolean`, unions, and arrays first. Reach for `unknown` instead of `any`, understand `void` and `never` for functions and control flow, and always enable `strictNullChecks`.
<!-- codeshelf:generated-appendix -->

---

### Why JavaScript typeof lies about null

`typeof null === 'object'` is a famous JS bug. TypeScript's type system treats `null` separately when `strictNullChecks` is on.

---

### Number is one type

Unlike some languages, TS has no separate `int` / `float` — all are `number` (IEEE 754).

---

### When to use bigint

Use `bigint` when integers exceed `Number.MAX_SAFE_INTEGER` (2^53 - 1).

---

### Readonly vs const

`const x = []` prevents rebinding; `readonly` prevents `push` on the array type.

---

### Optional chaining preview

`obj?.prop` short-circuits on `null`/`undefined` — essential with strict nulls.

---

## Primitives — everyday mental model

Values in TypeScript fall into groups, like sorting items in a warehouse:

| Shelf | Types | Examples |
|-------|-------|----------|
| Text | `string` | `"hello"`, `` `hi` `` |
| Numbers | `number`, `bigint` | `42`, `3.14n` |
| Yes/No | `boolean` | `true`, `false` |
| Empty slots | `null`, `undefined` | intentional vs missing |
| Unique tags | `symbol` | `Symbol("id")` |

With `strictNullChecks`, `null` and `undefined` are **not** interchangeable with other types unless you add them to a union.

---

## Walkthrough — typing a user profile

```typescript
interface UserProfile {
  username: string;
  age: number;
  isVerified: boolean;
  bio?: string; // optional — may be undefined
}

const profile: UserProfile = {
  username: "dev_ada",
  age: 28,
  isVerified: true,
};

// Safe optional access
const text = profile.bio?.toUpperCase() ?? "No bio yet";
```

Line by line:

1. `username: string` — must be text, not a number.
2. `bio?` — key may be missing; value may be `undefined`.
3. `?.` — if `bio` is missing, expression short-circuits to `undefined`.
4. `??` — if left side is `null`/`undefined`, use the right side string.

---

## any vs unknown — story with two doors

- **`any`** is a door with no lock. TypeScript stops checking. Anything goes in or out.
- **`unknown`** is a locked door. You must prove what is inside before using it.

```typescript
function handleInput(raw: unknown) {
  if (typeof raw === "string") {
    console.log(raw.toUpperCase()); // safe — narrowed to string
  }
}
```

Use `unknown` for JSON, `window` extensions, and third-party callbacks you do not control.

---

## never — the empty set

`never` means **no value can exist here**.

```typescript
function fail(msg: string): never {
  throw new Error(msg);
}

type Result = { ok: true } | { ok: false };
function assertOk(r: Result) {
  if (!r.ok) {
    fail("expected success"); // return type never — function does not return normally
  }
}
```

In `switch` on unions, assign `never` in `default` so adding a new union member forces you to update the switch.

---

## Arrays and tuples — when to use which

Use an **array** when all items share one type and length can change:

```typescript
const scores: number[] = [90, 85, 88];
scores.push(92);
```

Use a **tuple** when position matters:

```typescript
type HttpResponse = [status: number, body: string];
const res: HttpResponse = [200, "OK"];
```

| Need | Choose |
|------|--------|
| Homogeneous list | `T[]` |
| Fixed columns (CSV row) | tuple |
| Read-only list | `readonly T[]` |

---

## string — deep dive


### Why strings matter in TypeScript

Strings appear in UI labels, API fields, URLs, and identifiers. TypeScript treats all string literals as type `string` unless you use literal types or `as const`.

```typescript
const greeting: string = "Hello";
const template: string = `User: ${greeting}`;

function truncate(text: string, maxLen: number): string {
  return text.length > maxLen ? text.slice(0, maxLen) + "…" : text;
}
```

| Method | Returns | Example |
|--------|---------|---------|
| `.length` | number | `"hi".length` → 2 |
| `.toUpperCase()` | string | `"a".toUpperCase()` → `"A"` |
| `.includes(sub)` | boolean | `"hello".includes("ell")` |
| `.slice(start, end?)` | string | `"hello".slice(1, 3)` → `"el"` |

### Template literal types (preview)

```typescript
type EventName = "click" | "focus";
type HandlerName = `on${Capitalize<EventName>}`; // "onClick" | "onFocus"
```


---

## number — deep dive


JavaScript numbers are IEEE 754 doubles. TypeScript does not distinguish int vs float.

```typescript
let integer: number = 42;
let float: number = 3.14;
let hex: number = 0xff;
let binary: number = 0b1010;
let octal: number = 0o744;

// Special numeric values
let notANumber: number = NaN;
let infinity: number = Infinity;
```

| Constant | Value | Note |
|----------|-------|------|
| `Number.MAX_SAFE_INTEGER` | 9007199254740991 | Use bigint beyond this |
| `Number.EPSILON` | tiny | Float comparison tolerance |

```typescript
// Prefer Number.isNaN over global isNaN
Number.isNaN(NaN); // true
Number.isNaN("hello"); // false — global isNaN coerces
```


---

## bigint and symbol


### bigint

```typescript
const huge: bigint = 9007199254740992n;
const also = BigInt("9007199254740992");
// Cannot mix bigint and number without conversion
```

### symbol

```typescript
const id: symbol = Symbol("id");
const id2: symbol = Symbol("id");
console.log(id === id2); // false — each Symbol() is unique

const KEY = Symbol("key");
type Obj = { [KEY]: string };
```


---

## Arrays — patterns and pitfalls


```typescript
// Readonly prevents mutation at type level
const ids: readonly number[] = [1, 2, 3];
// ids.push(4); // compile error

// Tuple for fixed structure
type RGB = [number, number, number];
const red: RGB = [255, 0, 0];

// Labeled tuple elements (readable)
type HttpPair = [status: number, body: string];
```

### Common array typing mistakes

```typescript
// ❌ Empty array widens to any[] without context
const bad = [];
bad.push(1);
bad.push("two"); // allowed if any[]

// ✅ Provide context
const good: number[] = [];
// or
const alsoGood = [] as number[];
```


---

## Special types — comparison matrix


| Type | Assign from | Assign to without check | Runtime exists? |
|------|-------------|-------------------------|-----------------|
| `any` | all | all | n/a (checking off) |
| `unknown` | all | none | n/a |
| `void` | undefined | void contexts | yes (undefined) |
| `never` | never | never | n/a |
| `null` | null | only with union | yes |
| `undefined` | undefined | only with union | yes |


---

## Coercion vs types


TypeScript types do **not** change JavaScript coercion. Validate external strings before treating them as numbers.

```typescript
const n: number = Number("42"); // OK
const parsed = parseInt("42px", 10); // 42 — still validate input shape first
```


---

## Best Practices

- ✅ Prefer inference for obvious literals; annotate function parameters.
- ✅ Use `unknown` instead of `any` for external data.
- ✅ Enable `strictNullChecks` and model null with unions.
- ✅ Use `readonly` arrays when data must not mutate.
- ✅ Use literal unions instead of `string` for fixed sets of values.

---

## Common Mistakes

Watch for these patterns — they cost hours in real projects.

### Mistake 1: Using `any` everywhere

`let x: any = getData()`

Use `unknown` and narrow, or define a proper interface.

---

### Mistake 2: Ignoring `undefined` in optional props

`user.email.toLowerCase()` when `email?`

Use optional chaining: `user.email?.toLowerCase()`.

---

### Mistake 3: Confusing `void` with `undefined` only

Thinking `void` means no return at runtime

`void` means ignore return value; callers may still get `undefined`.

---

### Mistake 4: Tuple vs array confusion

`let t: number[] = [1, 'two']`

Use tuples `[number, string]` when positions have different types.

---

### Mistake 5: Widening literal types accidentally

`let d = 'north'; d = 'east'` then assigning invalid direction

Annotate `let d: Direction = 'north'` or use `as const`.

---

## Interview Points

> **📌 Interview Point 1: Difference between `any` and `unknown`?**

`any` disables checking; `unknown` requires narrowing before use.

---

> **📌 Interview Point 2: What is `never` used for?**

Functions that never return, and exhaustiveness checking in switches.

---

> **📌 Interview Point 3: What is a union type?**

A value that can be one of several types: `string | number`.

---

> **📌 Interview Point 4: What is `void`?**

Absence of a useful return value; typically functions that only side-effect.

---

> **📌 Interview Point 5: What is type inference?**

Compiler deduces types from initializers and context.

---

## Exercises

Practice with `npx tsc --noEmit` after each exercise.

### Exercise 2.1: Primitive annotations ⭐

**Task:** Declare username, score, premium flag with correct types.

<details><summary>💡 Hint</summary>

Use `string`, `number`, `boolean`.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
const username: string = "ada";
const score: number = 98;
const isPremium: boolean = true;
```

</details>

---

### Exercise 2.2: Readonly tuple ⭐⭐

**Task:** Create `readonly [string, number]` for product name and price.

<details><summary>💡 Hint</summary>

Tuple syntax with `readonly`.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
const product: readonly [string, number] = ["Keyboard", 79.99];
// product[1] = 50; // compile error
```

</details>

---

### Exercise 2.3: unknown pipeline ⭐⭐⭐

**Task:** Write `parseJson(s: string): unknown` and safely read a `name` property.

<details><summary>💡 Hint</summary>

Use `typeof` and `in` checks.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function parseJson(s: string): unknown {
  return JSON.parse(s);
}

function getName(data: unknown): string {
  if (typeof data === "object" && data !== null && "name" in data) {
    const name = (data as { name: unknown }).name;
    if (typeof name === "string") return name;
  }
  return "Unknown";
}
```

</details>

---

### Exercise 2.4: never exhaustiveness ⭐⭐

**Task:** Add a case to a `Theme` union and fix the `never` error in `default`.

<details><summary>💡 Hint</summary>

Chapter 2 `never` section pattern.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type Theme = "light" | "dark" | "system";

function icon(theme: Theme): string {
  switch (theme) {
    case "light": return "☀️";
    case "dark": return "🌙";
    case "system": return "💻";
    default:
      const _exhaustive: never = theme;
      return _exhaustive;
  }
}
// Add "system" to union and default branch — compiler forces update
```

</details>

---

### Exercise 2.5: Union formatter ⭐⭐⭐

**Task:** Function accepting `string | number` returning string representation.

<details><summary>💡 Hint</summary>

Use `typeof` narrowing.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function formatValue(value: string | number): string {
  if (typeof value === "string") return value;
  return value.toFixed(2);
}
```

</details>

---

### Exercise 2.6: null safety ⭐⭐

**Task:** Model optional phone with `string | undefined` and formatter returning `N/A`.

<details><summary>💡 Hint</summary>

Strict null checks.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function formatPhone(phone: string | undefined): string {
  return phone ?? "N/A";
}
```

</details>

---

## Chapter Summary

You covered a lot in this chapter. Here is a concise recap:

- Primitives: `string`, `number`, `boolean`, `bigint`, `symbol`, `null`, `undefined`.
- Prefer `unknown` over `any`; understand `void` and `never`.
- Arrays use `T[]` or `Array<T>`; tuples fix length and per-index types.
- Unions express multiple possibilities; narrow before use (Chapter 8).

---

---

## Navigation

**⬅️ [Previous: Introduction to TypeScript](./ch01-introduction.md)**  
**➡️ [Next: Interfaces and Type Aliases](./ch03-interfaces-and-type-aliases.md)**

---

*Last updated: 2025 | TypeScript course — CodeShelf*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
