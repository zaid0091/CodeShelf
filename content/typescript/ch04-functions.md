---
title: Chapter 4 — Functions
description: Function types, optional and default parameters, rest parameters, and overloads in TypeScript.
order: 4
tags: [typescript, functions, overloads, parameters]
---

# Chapter 4: Functions

## 4.1 Function type syntax

Functions are first-class values. TypeScript types their parameters and return values.

```typescript
// Named function
function add(a: number, b: number): number {
  return a + b;
}

// Arrow function
const multiply = (a: number, b: number): number => a * b;

// Function type expression
type BinaryOp = (a: number, b: number) => number;

const subtract: BinaryOp = (a, b) => a - b;
```

> **Definition:** A **function type** describes the callable signature: parameter types (and optional names) plus return type, written as `(params) => ReturnType`.

### Interface for call signatures

```typescript
interface Formatter {
  (value: number): string;
}

const currency: Formatter = (value) => `$${value.toFixed(2)}`;
```

## 4.2 Optional parameters

```typescript
function greet(name: string, title?: string): string {
  return title ? `Hello, ${title} ${name}` : `Hello, ${name}`;
}

greet("Ada");
greet("Ada", "Dr.");
```

| Syntax | Meaning |
|--------|---------|
| `param?: T` | Same as `param: T \| undefined`; may be omitted |
| Required params first | Optional params must follow required ones |

Optional parameters are `T | undefined` — always handle the missing case.

## 4.3 Default parameters

```typescript
function createConnection(host: string, port: number = 5432): void {
  console.log(`Connecting to ${host}:${port}`);
}

createConnection("localhost");      // port 5432
createConnection("db.internal", 3306);
```

Default parameters affect inference:

```typescript
function repeat(text: string, times = 3) {
  // times inferred as number
  return text.repeat(times);
}
```

Optional vs default:

| | Optional `?` | Default `= value` |
|---|--------------|-------------------|
| Omitted call | `undefined` | Uses default |
| Type at call site | `T \| undefined` | Always `T` after default applied |

## 4.4 Rest parameters

Collect remaining arguments into a typed array:

```typescript
function sum(...nums: number[]): number {
  return nums.reduce((acc, n) => acc + n, 0);
}

sum(1, 2, 3, 4); // 10
```

With other parameters:

```typescript
function log(level: string, ...messages: string[]): void {
  console.log(`[${level}]`, ...messages);
}
```

Tuple rest for fixed tail:

```typescript
function zip<T, U>(first: T, ...pairs: [U, U][]): [T, ...[U, U][]] {
  return [first, ...pairs];
}
```

## 4.5 Return type annotations

```typescript
function fetchIds(): Promise<number[]> {
  return Promise.resolve([1, 2, 3]);
}

function parseConfig(raw: string): { host: string; port: number } | null {
  try {
    return JSON.parse(raw);
  } catch {
    return null;
  }
}
```

When to annotate returns:

| Annotate | Skip (infer) |
|----------|--------------|
| Public library APIs | Small local helpers |
| Complex branches | Obvious literal returns |
| When inference widens undesirably | Callbacks in typed contexts |

## 4.6 void vs undefined returns

```typescript
function sideEffect(): void {
  console.log("done");
  return undefined; // OK
  // return 1; // ❌ Type 'number' is not assignable to type 'void'
}

// Stricter alternative — must return undefined explicitly:
function strictSideEffect(): undefined {
  console.log("done");
  return undefined;
}
```

Callback compatibility allows returning a value where `void` is expected (ignoring the return) — see [Chapter 13](./ch13-best-practices.md).

## 4.7 Function overloads

When one function behaves differently based on argument types:

```typescript
function formatInput(input: string): string;
function formatInput(input: number): string;
function formatInput(input: string | number): string {
  if (typeof input === "string") {
    return input.trim();
  }
  return input.toFixed(2);
}

const a = formatInput("  hi  "); // string overload
const b = formatInput(3.14159);  // number overload
```

Rules:

1. Overload **signatures** come first (no body).
2. One **implementation** signature must be compatible with all overloads.
3. Prefer unions + generics when overloads become unwieldy.

### DOM-style overload example

```typescript
function createElement(tag: "div"): HTMLDivElement;
function createElement(tag: "span"): HTMLSpanElement;
function createElement(tag: string): HTMLElement {
  return document.createElement(tag);
}
```

## 4.8 Generic functions (preview)

```typescript
function identity<T>(value: T): T {
  return value;
}

identity(42);    // T = number
identity("hi"); // T = string
```

Deep dive in [Chapter 5](./ch05-generics.md).

## 4.9 Higher-order functions

Functions accepting or returning functions:

```typescript
type Predicate<T> = (item: T) => boolean;

function filterItems<T>(items: T[], predicate: Predicate<T>): T[] {
  return items.filter(predicate);
}

const evens = filterItems([1, 2, 3, 4], (n) => n % 2 === 0);
```

### Typing Array methods

```typescript
const names = ["Ada", "Grace"];
const upper = names.map((name) => name.toUpperCase()); // string[]

interface User { id: number; name: string; }
const users: User[] = [{ id: 1, name: "Lin" }];
const ids = users.map((u) => u.id); // number[]
```

## 4.10 `this` typing

```typescript
interface ClickHandler {
  label: string;
  handleClick(this: ClickHandler, event: MouseEvent): void;
}

const button: ClickHandler = {
  label: "Submit",
  handleClick() {
    console.log(this.label);
  },
};
```

Use arrow functions in classes when you need lexical `this` ([Chapter 7](./ch07-classes-and-oop.md)).

## 4.11 Async functions

```typescript
async function loadUser(id: number): Promise<User> {
  const res = await fetch(`/api/users/${id}`);
  if (!res.ok) throw new Error("Failed");
  return res.json() as User;
}
```

Full async patterns in [Chapter 11](./ch11-async-typescript.md).

## 4.12 Function type aliases vs interfaces

```typescript
type Handler = (event: Event) => void;

    // common for callbacks
interface HandlerFn {
  (event: Event): void;
}

// Both equivalent for simple call signatures
```

## 4.13 Strict function types

With `strictFunctionTypes`, parameter types are checked **contravariantly** for function assignments — a subtle but important safety feature:

```typescript
type Animal = { name: string };
type Dog = Animal & { breed: string };

type LogAnimal = (a: Animal) => void;
type LogDog = (d: Dog) => void;

let logAnimal: LogAnimal = (a) => console.log(a.name);
let logDog: LogDog = (d) => console.log(d.breed);

// logDog = logAnimal; // ✅ safe — Dog is narrower than Animal
// logAnimal = logDog; // ❌ might call with Animal that's not Dog
```

> **Key takeaway:** Type every parameter in public functions; use optional/default/rest parameters intentionally; reach for overloads only when call signatures genuinely differ.

## Practice Exercise — Chapter 4

```text
Exercise 4.1: Calculator
  a) Implement typed add, subtract, multiply, divide (divide returns number | null on /0).
  b) Use a type MathOp = (a: number, b: number) => number | null where needed.

Exercise 4.2: Overloads
  a) Write makeDate(timestamp: number): Date overload.
  b) Write makeDate(y: number, m: number, d: number): Date overload.
  c) Implement with a single body using typeof checks.

Exercise 4.3: Rest & optional
  a) Function buildUrl(path: string, ...query: [string, string][]): string.
  b) Optional trailing locale?: string on formatMessage(key: string, locale?: string).

Exercise 4.4: Higher-order
  a) Generic groupBy<T, K extends string | number>(items: T[], keyFn: (item: T) => K).
  b) Return Record<K, T[]> or Map-like structure.
  c) Test with array of { category: string; value: number }.
```

Continue to [Chapter 5 — Generics](./ch05-generics.md).
