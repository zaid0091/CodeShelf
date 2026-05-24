---
title: Chapter 4 — Functions
description: Function types, optional/default/rest params, overloads, and higher-order functions.
order: 4
tags: [typescript, functions, overloads, parameters]
---


# Chapter 4: Functions

> **Functions are the heart of TypeScript programs. This chapter covers typing parameters, return types, overloads, `this`, and async functions.**
> Take your time with each section. TypeScript rewards patience — read compiler errors carefully and experiment in a small project as you go.

---


## Table of Contents

1. [Function Type Syntax](#function-type-syntax)
2. [Optional Parameters](#optional-parameters)
3. [Default Parameters](#default-parameters)
4. [Rest Parameters](#rest-parameters)
5. [Return Types](#return-types)
6. [Function Overloads](#function-overloads)
7. [Generic Functions Preview](#generic-functions-preview)
8. [Higher-Order Functions](#higher-order-functions)
9. [this Typing](#this-typing)
10. [Async Functions](#async-functions)
11. [Best Practices](#best-practices)
12. [Common Mistakes](#common-mistakes)
13. [Interview Points](#interview-points)
14. [Exercises](#exercises)
15. [Chapter Summary](#chapter-summary)

---

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
<!-- codeshelf:generated-appendix -->

---

### Inferring callback parameters

Contextual typing infers parameter types in `arr.map(x => x * 2)`.

---

## Function types — reading signatures

```typescript
type SearchFn = (query: string, limit?: number) => string[];
```

Read it aloud: "A function that takes a string and optional number, and returns an array of strings."

Optional parameters must come **after** required ones.

---

## Overloads — real-world parse example

```typescript
function parse(input: string): string;
function parse(input: number): number;
function parse(input: string | number): string | number {
  if (typeof input === "string") return input.trim();
  return Math.round(input);
}
```

Callers get precise return types; one implementation handles all cases.

---

## Contextual typing — callbacks

```typescript
const nums = [1, 2, 3];
const doubled = nums.map((n) => n * 2); // n inferred as number
```

The expected type of the callback parameter flows **down** from `map`'s definition.

---

## Function types as values


```typescript
type BinaryOp = (a: number, b: number) => number;
const add: BinaryOp = (a, b) => a + b;

type StringMapper = (s: string) => string;
const shout: StringMapper = (s) => s.toUpperCase();
```


---

## Overload patterns


```typescript
function createElement(tag: "div"): HTMLDivElement;
function createElement(tag: "span"): HTMLSpanElement;
function createElement(tag: string): HTMLElement;
function createElement(tag: string): HTMLElement {
  return document.createElement(tag);
}
```

Implementation signature must be compatible with all overloads.


---

## Async function typing


```typescript
async function loadConfig(path: string): Promise<AppConfig> {
  const raw = await readFile(path, "utf8");
  return JSON.parse(raw) as AppConfig; // prefer validation
}

type AwaitedConfig = Awaited<ReturnType<typeof loadConfig>>;
```


---

## Optional and default parameters


```typescript
function greet(name: string, greeting: string = "Hello"): string {
  return `${greeting}, ${name}`;
}

function connect(host: string, port?: number): void {
  const p = port ?? 443;
  console.log(host, p);
}
```

| Parameter | Syntax | Notes |
|-----------|--------|-------|
| Optional | `name?: T` | May be `undefined` |
| Default | `name = value` | Inferred type from default |
| Rest | `...args: T[]` | Collects remaining arguments |


---

## Higher-order functions


```typescript
function map<T, U>(items: T[], fn: (item: T) => U): U[] {
  return items.map(fn);
}

function filter<T>(items: T[], pred: (item: T) => boolean): T[] {
  return items.filter(pred);
}
```


---

## this parameter types


```typescript
interface Clickable {
  label: string;
  onClick(this: Clickable, e: Event): void;
}
```

Use arrow properties in classes when you need lexical `this` in React handlers.


---

## Currying and composition


```typescript
const curry =
  <A, B, C>(fn: (a: A, b: B) => C) =>
  (a: A) =>
  (b: B) =>
    fn(a, b);

const add = (a: number, b: number) => a + b;
const add5 = curry(add)(5);
console.log(add5(3)); // 8
```


---

## Optional chaining with callbacks


```typescript
function onReady(cb?: () => void) {
  cb?.();
}
```


---

## Rest parameters with tuples


```typescript
function logAll(level: "info" | "error", ...messages: string[]) {
  messages.forEach((m) => console[level](m));
}
```


---

## Function overload pitfalls


Keep overloads **simple**. If you need many shapes, consider a single options object:

```typescript
interface FormatOptions {
  value: string | number | boolean;
  locale?: string;
}
function format(opts: FormatOptions): string { /* ... */ }
```


---

## Definition — Function signature

> **Definition:** **Function signature** — The list of parameter types and the return type — the contract callers must satisfy.


---

## Step-by-step — overload design


1. List each way callers invoke the function.
2. Write one overload signature per shape.
3. Write one implementation that accepts the union of inputs.
4. Narrow inside the implementation with `typeof` or discriminant checks.


---

## Practice — event handler types


```typescript
type ClickHandler = (event: MouseEvent) => void;
type KeyHandler = (event: KeyboardEvent) => void;

function on(element: HTMLElement, event: "click", handler: ClickHandler): void;
function on(element: HTMLElement, event: "keydown", handler: KeyHandler): void;
function on(element: HTMLElement, event: string, handler: (e: Event) => void): void {
  element.addEventListener(event, handler as EventListener);
}
```


---

## Common interview — optional vs default


| Feature | Syntax | When absent |
|---------|--------|-------------|
| Optional | `x?: number` | `undefined` |
| Default | `x = 0` | uses default value |

Optional parameters must follow required parameters.


---

## Rest and spread typing


```typescript
function merge<T extends object, U extends object>(a: T, b: U): T & U {
  return { ...a, ...b };
}
```


---

## Review Q1 — optional parameters

**Q:** Can optional parameters come before required ones? **A:** No — required parameters must come first.

---

## Review Q2 — return type

**Q:** When should you annotate return types on exported functions? **A:** When the API is public or inference might widen unexpectedly.

---

## Best Practices

- ✅ Annotate parameters; let return types be inferred only when obvious internally.
- ✅ Use overloads sparingly for call-signature differences.
- ✅ Prefer rest params over `arguments` object.

---

## Common Mistakes

Watch for these patterns — they cost hours in real projects.

### Mistake 1: Optional before required

`function f(a?: number, b: string)`

Put required parameters first.

---

### Mistake 2: Wrong overload implementation

Implementation signature not compatible with overloads

Ensure impl accepts all overload cases.

---

### Mistake 3: Using `Function` type

`let fn: Function`

Use specific function types or generics.

---

## Interview Points

> **📌 Interview Point 1: What are function overloads?**

Multiple call signatures, one implementation.

---

> **📌 Interview Point 2: Covariance/contrariance basics?**

Parameters are checked contravariantly under strictFunctionTypes.

---

## Exercises

Practice with `npx tsc --noEmit` after each exercise.

### Exercise 4.1: Overload pair ⭐

**Task:** Write overloads for `format(value: number): string` and `format(value: boolean): string`.

<details><summary>💡 Hint</summary>

One implementation.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function format(value: number): string;
function format(value: boolean): string;
function format(value: number | boolean): string {
  return String(value);
}
```

</details>

---

### Exercise 4.2: Rest sum ⭐⭐

**Task:** Typed rest parameters summing numbers.

<details><summary>💡 Hint</summary>

Use `...nums: number[]`.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function sum(...nums: number[]): number {
  return nums.reduce((a, b) => a + b, 0);
}
```

</details>

---

### Exercise 4.3: HOF filter ⭐⭐⭐

**Task:** Type `filterItems<T>` with predicate.

<details><summary>💡 Hint</summary>

Generics in Chapter 5.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function filterItems<T>(items: T[], pred: (item: T) => boolean): T[] {
  return items.filter(pred);
}
```

</details>

---

### Exercise 4.4: Async fetch ⭐⭐

**Task:** Type `loadUser(id: string): Promise<User>`.

<details><summary>💡 Hint</summary>

Promise generic.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
interface User { id: string; name: string }

async function loadUser(id: string): Promise<User> {
  const res = await fetch(`/api/users/${id}`);
  return res.json() as User; // production: validate
}
```

</details>

---

### Exercise 4.5: this in method ⭐⭐⭐

**Task:** Class method vs arrow property for callbacks.

<details><summary>💡 Hint</summary>

Chapter 7.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
class Counter {
  count = 0;
  increment = () => { this.count += 1; }; // lexical this
}
```

</details>

---

### Exercise 4.6: Explicit return ⭐⭐

**Task:** Export function with explicit return type.

<details><summary>💡 Hint</summary>

Public API clarity.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
export function parseId(raw: string): number | null {
  const n = Number(raw);
  return Number.isNaN(n) ? null : n;
}
```

</details>

---

## Chapter Summary

You covered a lot in this chapter. Here is a concise recap:

- Optional/default/rest parameters; overloads; async `Promise<T>`.
- Strict function types affect callback assignability.

---

---

## Navigation

**⬅️ [Previous: Interfaces and Type Aliases](./ch03-interfaces-and-type-aliases.md)**  
**➡️ [Next: Generics](./ch05-generics.md)**

---

*Last updated: 2025 | TypeScript course — CodeShelf*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
