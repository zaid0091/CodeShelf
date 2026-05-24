---
title: Chapter 2 — Types and Primitives
description: Primitive types, arrays, tuples, any, unknown, void, never, and type annotations in TypeScript.
order: 2
tags: [typescript, types, primitives, any, unknown]
---

# Chapter 2: Types and Primitives

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

## Practice Exercise — Chapter 2

```text
Exercise 2.1: Annotations
  a) Declare variables for a username (string), score (number), and premium (boolean).
  b) Create a readonly tuple [string, number] for [productName, price].
  c) Write a function that accepts string | number and returns string.

Exercise 2.2: unknown vs any
  a) Write fetchData(): unknown that returns JSON.parse result.
  b) Show the compile error when accessing .id directly.
  c) Narrow with typeof/in checks before use.

Exercise 2.3: never
  a) Define type Theme = "light" | "dark".
  b) Write getThemeLabel(theme: Theme): string with a switch.
  c) Add "system" to Theme — fix the exhaustiveness error in default.

Exercise 2.4: null safety
  a) Model a User with optional phone: string | undefined.
  b) Write formatPhone that returns "N/A" when missing.
  c) Enable strict mode and fix any null-related errors.
```

Continue to [Chapter 3 — Interfaces & Type Aliases](./ch03-interfaces-and-type-aliases.md) for object shapes and composition.
