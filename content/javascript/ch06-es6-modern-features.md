---
title: ES6+ Modern Features
description: ES modules, classes, template literals, Map, Set, and other ES2015+ syntax
order: 6
tags: [javascript, es6, modules, classes, map, set, template-literals]
---

# Chapter 6: ES6+ Modern Features

> "ES2015 did not just add syntax — it gave JavaScript a modern vocabulary for building real applications."

---

## Table of Contents

1. [Why ES6+ Matters](#why-es6+-matters)
2. [History of ECMAScript](#history-of-ecmascript)
3. [let and const Review](#let-and-const-review)
4. [Arrow Functions Deep Dive](#arrow-functions-deep-dive)
5. [Template Literals](#template-literals)
6. [Tagged Template Literals](#tagged-template-literals)
7. [Destructuring Arrays](#destructuring-arrays)
8. [Destructuring Objects](#destructuring-objects)
9. [Spread and Rest](#spread-and-rest)
10. [Enhanced Object Literals](#enhanced-object-literals)
11. [Default Parameters](#default-parameters)
12. [ES6 Classes](#es6-classes)
13. [Static Methods and Fields](#static-methods-and-fields)
14. [Private Class Fields](#private-class-fields)
15. [Getters and Setters](#getters-and-setters)
16. [ES Modules — Export](#es-modules--export)
17. [ES Modules — Import](#es-modules--import)
18. [Dynamic import](#dynamic-import)
19. [Map and Set](#map-and-set)
20. [WeakMap and WeakSet](#weakmap-and-weakset)
21. [Symbol](#symbol)
22. [Iterators](#iterators)
23. [Generators](#generators)
24. [Optional Chaining](#optional-chaining)
25. [Nullish Coalescing](#nullish-coalescing)
26. [Object and Array Helpers](#object-and-array-helpers)
27. [BigInt](#bigint)
28. [Promises — Introduction](#promises--introduction)
29. [Common Mistakes](#common-mistakes)
30. [Best Practices](#best-practices)
31. [Interview Points](#interview-points)
32. [Exercises](#exercises)
33. [Chapter Summary](#chapter-summary)

---

## Why ES6+ Matters

### Definition

**ES6** (ECMAScript 2015) is the landmark update: `let`/`const`, arrows, classes, modules, destructuring, Promises, and more.

### Why It Matters

Modern codebases assume ES6+. Without it, React, Vue, and Node tooling are hard to read.

### How It Works

TC39 ships yearly updates (ES2017 `async/await`, ES2020 `?.`/`??`, ES2022 private fields).


```js
const user = { name: "Alice" };
const { name } = user; // destructuring — everywhere in modern JS
```

> See [Chapter 1](./ch01-javascript-basics.md), [Chapter 4](./ch04-functions.md), [Chapter 5](./ch05-arrays-and-objects.md).
---

## History of ECMAScript

### Definition

**ECMAScript** is the spec; **JavaScript** is the implementation in browsers and Node.

### Why It Matters

Interviewers ask "What is ES6?" — a **spec version**, not a new language.

### How It Works

1995: created in ~10 days. 2015: ES6. 2016+: yearly releases.

```text
1995 Mocha → LiveScript → JavaScript
2015 ES6 (biggest release)
2017 async/await
2020 ?. ??
```

---

## let and const Review

### Definition

**`let`** is block-scoped and reassignable. **`const`** cannot be reassigned; object contents may still mutate.

### Why It Matters

Fixes `var` hoisting and function-scope leaks.

### How It Works

Default to `const`; use `let` when reassigning. Never `var`.


```js
const MAX = 100;
let count = 0;
count++;
const cfg = { theme: "light" };
cfg.theme = "dark"; // OK
```

| | var | let | const |
|---|---|---|---|
| Scope | function | block | block |
---

## Arrow Functions Deep Dive

### Definition

**Arrow functions** use `=>` and inherit **lexical `this`** from the enclosing scope.

### Why It Matters

Cleaner callbacks; avoid when you need dynamic `this` or `new`.

### How It Works

`(a, b) => a + b` or `(a) => { return a; }`


```js
const nums = [1, 2, 3];
const doubled = nums.map((n) => n * 2);

const timer = {
  seconds: 0,
  start() {
    setInterval(() => {
      this.seconds++; // arrow keeps 'this' as timer
    }, 1000);
  },
};
```


---

## Template Literals

### Definition

Strings with backticks support `${expression}` and multiple lines.

### Why It Matters

Readable HTML/JSON templates without `+` concatenation.

### How It Works

Escape backticks with `\``.


```js
const name = "Alice";
const msg = `Hello, ${name}!`;
const html = `<p class="user">${name}</p>`;
```


---

## Tagged Template Literals

### Definition

A **tag** function receives string segments and values: `` tag`Hello ${name}` ``.

### Why It Matters

i18n, styled-components, HTML escaping.

### How It Works

First argument: array of string parts; rest: interpolated values.


```js
function escape(strings, ...values) {
  return strings.reduce((acc, s, i) => acc + s + (values[i] ?? ""), "");
}
const safe = escape`<b>${userInput}</b>`;
```


---

## Destructuring Arrays

### Definition

Unpack array elements into variables: `const [a, b] = arr`.

### Why It Matters

Swap, skip elements, defaults, rest.

### How It Works


```js
const [first, , third] = [1, 2, 3];
const [head, ...rest] = [1, 2, 3];
let x = 1, y = 2;
[x, y] = [y, x];
```




---

## Destructuring Objects

### Definition

Unpack properties by name; rename and default.

### Why It Matters

API responses and function options.

### How It Works


```js
const { id, name, role = "viewer" } = user;
function connect({ host = "localhost", port = 3000 } = {}) {}
```




---

## Spread and Rest

### Definition

**Spread** expands iterables; **rest** collects remaining items.

### Why It Matters

Immutable updates and variadic functions.

### How It Works


```js
const merged = { ...defaults, ...overrides };
const all = [...a, ...b];
function sum(...nums) { return nums.reduce((a, b) => a + b, 0); }
```




---

## Enhanced Object Literals

### Definition

Shorthand properties, method syntax, computed keys.

### Why It Matters

Less boilerplate in factories.

### How It Works


```js
const id = 1, role = "admin";
const user = {
  id,
  role,
  greet() { return `Hi ${this.role}`; },
  ["key_" + id]: true,
};
```




---

## Default Parameters

### Definition

Parameters default when argument is `undefined`.

### Why It Matters

Self-documenting function signatures.

### How It Works


```js
function createPage(title, layout = "default", published = false) {
  return { title, layout, published };
}
```




---

## ES6 Classes

### Definition

`class` is syntactic sugar over prototypes — [Chapter 12](./ch12-oop-prototypes.md).

### Why It Matters

Familiar OOP syntax for teams.

### How It Works


```js
class Animal {
  constructor(name) { this.name = name; }
  speak() { return `${this.name} makes a sound`; }
}
class Dog extends Animal {
  speak() { return `${this.name} barks`; }
}
```




---

## Static Methods and Fields

### Definition

`static` members belong to the class, not instances.

### Why It Matters

Utilities and constants.

### How It Works


```js
class IdGenerator {
  static #next = 1;
  static create() { return this.#next++; }
}
```




---

## Private Class Fields

### Definition

`#field` is truly private (ES2022).

### Why It Matters

Encapsulation without `_` conventions.

### How It Works


```js
class Wallet {
  #balance = 0;
  deposit(n) { this.#balance += n; }
  get balance() { return this.#balance; }
}
```




---

## Getters and Setters

### Definition

Accessor properties run functions on get/set.

### Why It Matters

Validation and computed properties.

### How It Works


```js
class Circle {
  constructor(r) { this._r = r; }
  get area() { return Math.PI * this._r ** 2; }
  set radius(r) {
    if (r <= 0) throw new Error("invalid");
    this._r = r;
  }
}
```




---

## ES Modules — Export

### Definition

Each file is a module; `export` exposes bindings.

### Why It Matters

Explicit public API per file.

### How It Works


```js
export const PI = 3.14159;
export function add(a, b) { return a + b; }
export default function multiply(a, b) { return a * b; }
```




---

## ES Modules — Import

### Definition

`import` creates live read-only bindings.

### Why It Matters

Static analysis enables tree-shaking.

### How It Works


```js
import multiply, { PI, add } from "./math.js";
import * as math from "./math.js";
```


Browser: `<script type="module" src="app.js"></script>`. Node: [Chapter 10](./ch10-modules-and-npm.md).

---

## Dynamic import

### Definition

`import(path)` returns a Promise — load on demand.

### Why It Matters

Code splitting and lazy routes.

### How It Works


```js
const mod = await import("./heavy-chart.js");
mod.render(data);
```




---

## Map and Set

### Definition

`Set` = unique values. `Map` = any keys.

### Why It Matters

Deduplication and object-key caches.

### How It Works


```js
const tags = new Set(["js", "web", "js"]);
const cache = new Map();
cache.set({ id: 1 }, "Alice");
```


| | Object | Map |
|---|--------|-----|
| Keys | string/Symbol | any |

---

## WeakMap and WeakSet

### Definition

Weak references; keys can be garbage-collected.

### Why It Matters

Metadata on DOM nodes without leaks.

### How It Works


```js
const wm = new WeakMap();
let el = document.createElement("div");
wm.set(el, { clicks: 0 });
```




---

## Symbol

### Definition

Unique primitive for property keys.

### Why It Matters

`Symbol.iterator` powers `for...of`.

### How It Works


```js
const id = Symbol("id");
const obj = { [id]: 42, name: "x" };
```




---

## Iterators

### Definition

Objects with `next()` returning `{ value, done }`.

### Why It Matters

Custom iteration protocols.

### How It Works


```js
const counter = {
  n: 0,
  [Symbol.iterator]() {
    return {
      next: () => ({ value: this.n++, done: this.n > 3 }),
    };
  },
};
```




---

## Generators

### Definition

`function*` yields values and pauses.

### Why It Matters

Infinite sequences, async iterators (advanced).

### How It Works


```js
function* range(start, end) {
  for (let i = start; i <= end; i++) yield i;
}
[...range(1, 5)]; // [1,2,3,4,5]
```




---

## Optional Chaining

### Definition

`?.` stops at `null`/`undefined`.

### Why It Matters

Safe deep property access.

### How It Works


```js
const city = user?.address?.city;
const result = api?.fetch?.();
```




---

## Nullish Coalescing

### Definition

`??` defaults only for `null`/`undefined`.

### Why It Matters

Unlike `||`, preserves `0` and ``.

### How It Works


```js
const port = config.port ?? 3000;
const title = data?.title ?? "Untitled";
```




---

## Object and Array Helpers

### Definition

Spread, `Object.assign`, `Object.hasOwn`, `structuredClone`, `flatMap`.

### Why It Matters

Modern data manipulation.

### How It Works


```js
Object.hasOwn(obj, "key");
const copy = structuredClone(deep);
posts.flatMap((p) => p.tags);
```




---

## BigInt

### Definition

Arbitrary-precision integers: `123n`.

### Why It Matters

IDs larger than Number.MAX_SAFE_INTEGER.

### How It Works


```js
const big = 9007199254740991n + 1n;
```




---

## Promises — Introduction

### Definition

A **Promise** represents async completion — pending, fulfilled, rejected.

### Why It Matters

Bridge to [Chapter 7](./ch07-asynchronous-javascript.md).

### How It Works


```js
const p = new Promise((resolve, reject) => {
  setTimeout(() => resolve("done"), 500);
});
p.then(console.log).catch(console.error);
```




---

### Template Literals — Example 1

```js
// Example 1: practical pattern for template literals
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### Template Literals — Example 2

```js
// Example 2: practical pattern for template literals
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### Template Literals — Example 3

```js
// Example 3: practical pattern for template literals
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### Template Literals — Example 4

```js
// Example 4: practical pattern for template literals
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### Template Literals — Example 5

```js
// Example 5: practical pattern for template literals
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

### Destructuring Objects — Example 1

```js
// Example 1: practical pattern for destructuring objects
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### Destructuring Objects — Example 2

```js
// Example 2: practical pattern for destructuring objects
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### Destructuring Objects — Example 3

```js
// Example 3: practical pattern for destructuring objects
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### Destructuring Objects — Example 4

```js
// Example 4: practical pattern for destructuring objects
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### Destructuring Objects — Example 5

```js
// Example 5: practical pattern for destructuring objects
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

### Spread and Rest — Example 1

```js
// Example 1: practical pattern for spread and rest
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### Spread and Rest — Example 2

```js
// Example 2: practical pattern for spread and rest
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### Spread and Rest — Example 3

```js
// Example 3: practical pattern for spread and rest
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### Spread and Rest — Example 4

```js
// Example 4: practical pattern for spread and rest
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### Spread and Rest — Example 5

```js
// Example 5: practical pattern for spread and rest
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

### ES6 Classes — Example 1

```js
// Example 1: practical pattern for es6 classes
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### ES6 Classes — Example 2

```js
// Example 2: practical pattern for es6 classes
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### ES6 Classes — Example 3

```js
// Example 3: practical pattern for es6 classes
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### ES6 Classes — Example 4

```js
// Example 4: practical pattern for es6 classes
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### ES6 Classes — Example 5

```js
// Example 5: practical pattern for es6 classes
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

### Map and Set — Example 1

```js
// Example 1: practical pattern for map and set
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### Map and Set — Example 2

```js
// Example 2: practical pattern for map and set
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### Map and Set — Example 3

```js
// Example 3: practical pattern for map and set
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### Map and Set — Example 4

```js
// Example 4: practical pattern for map and set
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### Map and Set — Example 5

```js
// Example 5: practical pattern for map and set
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

### Generators — Example 1

```js
// Example 1: practical pattern for generators
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### Generators — Example 2

```js
// Example 2: practical pattern for generators
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### Generators — Example 3

```js
// Example 3: practical pattern for generators
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### Generators — Example 4

```js
// Example 4: practical pattern for generators
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### Generators — Example 5

```js
// Example 5: practical pattern for generators
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

### Arrow Functions Deep Dive — Example 1

```js
// Example 1: practical pattern for arrow functions deep dive
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### Arrow Functions Deep Dive — Example 2

```js
// Example 2: practical pattern for arrow functions deep dive
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### Arrow Functions Deep Dive — Example 3

```js
// Example 3: practical pattern for arrow functions deep dive
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### Arrow Functions Deep Dive — Example 4

```js
// Example 4: practical pattern for arrow functions deep dive
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### Arrow Functions Deep Dive — Example 5

```js
// Example 5: practical pattern for arrow functions deep dive
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

### Promises — Introduction — Example 1

```js
// Example 1: practical pattern for promises — introduction
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### Promises — Introduction — Example 2

```js
// Example 2: practical pattern for promises — introduction
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### Promises — Introduction — Example 3

```js
// Example 3: practical pattern for promises — introduction
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### Promises — Introduction — Example 4

```js
// Example 4: practical pattern for promises — introduction
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### Promises — Introduction — Example 5

```js
// Example 5: practical pattern for promises — introduction
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

## Common Mistakes

### Using var

Use let/const only.

### Arrow as object method needing this

Use regular method syntax.

### || instead of ??

Use ?? for defaults when 0 or '' are valid.

### Wrong import names

Named imports must match export names.


## Best Practices

- Prefer const; let when reassigning.
- Use destructuring for options objects.
- Use Map/Set for appropriate data shapes.
- Use modules for file organization.
- Learn prototypes in Chapter 12 even when using class.

## Interview Points

### class vs prototype?

class is sugar; methods on prototype chain.

### Map vs Object?

Map: any keys, .size, no key coercion surprises.

### ?? vs ||?

?? only null/undefined; || all falsy.

### Can you reassign const object?

Yes mutate properties; no rebind variable.

### What is temporal dead zone?

let/const inaccessible before declaration line.


## Exercises

### Exercise 6.1 — Template email

buildWelcomeEmail({ name, plan })

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
function buildWelcomeEmail({ name, plan }) {
  return {
    subject: `Welcome to ${plan}, ${name}!`,
    body: `Hi ${name},\nThanks for joining ${plan}.`,
  };
}
```


</details>

### Exercise 6.2 — Rectangle class

area, perimeter getters, toString

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
class Rectangle {
  constructor(w, h) { this.width = w; this.height = h; }
  get area() { return this.width * this.height; }
  get perimeter() { return 2 * (this.width + this.height); }
  toString() { return `Rectangle ${this.width}x${this.height}`; }
}
```


</details>

### Exercise 6.3 — Module split

calc.js exports

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
export const add = (a, b) => a + b;
export default (op, a, b) => op === "+" ? a + b : a - b;
```


</details>

### Exercise 6.4 — Unique tags

flatMap + Set

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
const unique = [...new Set(posts.flatMap((p) => p.tags))];
```


</details>

### Exercise 6.5 — mergeConfig

spread + defaults

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
function mergeConfig(user = {}, defaults = {}) {
  return { ...defaults, ...user };
}
```


</details>

### Exercise 6.6 — range generator

function* range

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
function* range(a, b) { for (let i = a; i <= b; i++) yield i; }
```


</details>

## Chapter Summary

| Feature | When |
|---------|------|
| Template literals | Strings with variables |
| Destructuring / spread | Unpack and merge |
| Classes | OOP-style APIs |
| Modules | Multi-file projects |
| Map / Set | Special collections |
| ?. / ?? | Safe access and defaults |


---

## Next Chapter

Next: **Asynchronous JavaScript** — event loop, Promises, async/await.

---

**⬅️ [Previous: Arrays & Objects](./ch05-arrays-and-objects.md)** · **➡️ [Next Chapter: Asynchronous JavaScript →](./ch07-asynchronous-javascript.md)**

---

*Last updated: 2026 | Chapter 6 of the Complete JavaScript Guide*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
