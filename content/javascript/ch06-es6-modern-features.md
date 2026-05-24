---
title: ES6+ Modern Features
description: ES modules, classes, template literals, Map, Set, and other ES2015+ syntax
order: 6
tags: [javascript, es6, modules, classes, map, set, template-literals]
---

# Chapter 6: ES6+ Modern Features

## 6.1 Why ES6 matters

ES2015 (ES6) was the largest update to JavaScript. Modern codebases assume:

- `let` / `const`
- Arrow functions
- Classes
- Modules
- Destructuring, spread, rest
- Promises (see [Chapter 7](./ch07-asynchronous-javascript.md))

## 6.2 Template literals

```javascript
const name = "Alice";
const score = 95;

// Interpolation
const msg = `Hello, ${name}! You scored ${score}.`;

// Multi-line
const html = `
  <article>
    <h2>${name}</h2>
    <p>Score: ${score}</p>
  </article>
`;

// Tagged templates (advanced)
function highlight(strings, ...values) {
  return strings.reduce((acc, str, i) => acc + str + (values[i] ?? ""), "");
}
```

## 6.3 Enhanced object literals

```javascript
const role = "admin";
const id = 1;

const user = {
  id,              // shorthand property
  role,
  greet() {        // shorthand method
    return `Hi, ${this.role}`;
  },
  ["dynamic" + "Key"]: true,
};
```

## 6.4 Classes

> **Definition:** `class` is syntactic sugar over JavaScript's prototype-based inheritance.

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    return `${this.name} makes a sound`;
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);
    this.breed = breed;
  }

  speak() {
    return `${this.name} barks`;
  }
}

const rex = new Dog("Rex", "Lab");
rex.speak(); // "Rex barks"
```

### Static members

```javascript
class MathUtil {
  static PI = 3.14159;
  static circleArea(r) {
    return this.PI * r ** 2;
  }
}
```

### Private fields (ES2022)

```javascript
class BankAccount {
  #balance = 0;

  deposit(amount) {
    this.#balance += amount;
  }

  getBalance() {
    return this.#balance;
  }
}
```

Deep dive: [Chapter 12: OOP & Prototypes](./ch12-oop-prototypes.md).

## 6.5 ES modules

### Exporting

```javascript
// math.js
export const PI = 3.14159;

export function add(a, b) {
  return a + b;
}

export default function multiply(a, b) {
  return a * b;
}
```

### Importing

```javascript
// app.js
import multiply, { PI, add } from "./math.js";

console.log(add(2, 3));
console.log(multiply(2, 3));
```

| Export type | Import syntax |
|-------------|---------------|
| Named | `import { x } from "./m.js"` |
| Default | `import x from "./m.js"` |
| Rename | `import { x as y } from "./m.js"` |
| Namespace | `import * as m from "./m.js"` |

### Dynamic import

```javascript
const module = await import("./heavy.js");
module.run();
```

Browser modules require `type="module"`:

```html
<script type="module" src="app.js"></script>
```

Full npm workflow: [Chapter 10](./ch10-modules-and-npm.md).

## 6.6 `Map` and `Set`

### `Set` — unique values

```javascript
const tags = new Set(["js", "web", "js"]);
tags.add("api");
tags.has("web");     // true
tags.size;           // 3
[...tags];           // ["js", "web", "api"]
```

### `Map` — key-value with any key type

```javascript
const cache = new Map();
cache.set({ id: 1 }, "user data");
cache.set("theme", "dark");

cache.get("theme");
cache.has("theme");
cache.delete("theme");
```

| | Plain object | Map |
|---|--------------|-----|
| Keys | Strings/Symbols | Any |
| Size | Manual | `.size` |
| Iteration order | Mostly insertion* | Guaranteed insertion |
| JSON | Yes | No |

## 6.7 `Symbol`

```javascript
const TYPE = Symbol("type");

const config = {
  [TYPE]: "production",
  url: "https://api.example.com",
};
```

## 6.8 Iterators and generators (overview)

```javascript
function* idGenerator() {
  let id = 1;
  while (true) {
    yield id++;
  }
}

const gen = idGenerator();
gen.next().value; // 1
gen.next().value; // 2
```

## 6.9 Optional chaining and nullish coalescing

```javascript
const street = user?.address?.street;
const port = config.port ?? 3000;

// Combined
const label = response?.data?.title ?? "Untitled";
```

## 6.10 `Array` / `Object` modern helpers

```javascript
const merged = { ...obj1, ...obj2 };
const combined = [...arr1, ...arr2];

Object.assign({}, target, source); // still common in older code

// Object.hasOwn (ES2022) — prefer over hasOwnProperty
Object.hasOwn(obj, "key");
```

## 6.11 `Promise` introduction

```javascript
const p = new Promise((resolve, reject) => {
  setTimeout(() => resolve("done"), 1000);
});

p.then((value) => console.log(value))
 .catch((err) => console.error(err));
```

Full async guide: [Chapter 7](./ch07-asynchronous-javascript.md).

## 6.12 Chapter summary

| Feature | When to use |
|---------|-------------|
| Template literals | Strings with variables or multiline |
| Classes | OOP-style constructors and inheritance |
| Modules | Split code across files |
| Map/Set | Non-string keys or unique collections |
| `?.` / `??` | Safe access and defaults |

## Exercises

### Exercise 6.1 — Template email

Build a `buildWelcomeEmail({ name, plan })` function using a template literal with subject and body.

### Exercise 6.2 — Mini class

Create `class Rectangle` with `width`, `height`, getters `area` and `perimeter`, and `toString()`.

### Exercise 6.3 — Module split

Split `add`, `subtract`, and default `calculate` into `calc.js` and import them in `main.js` (Node with `"type": "module"` or `.mjs`).

### Exercise 6.4 — Unique tags

Given `const posts = [{ tags: ["a","b"] }, { tags: ["b","c"] }]`, return a `Set` (or array) of all unique tags using `flatMap` and `Set`.

---

**Previous:** [Chapter 5: Arrays & Objects](./ch05-arrays-and-objects.md) · **Next:** [Chapter 7: Asynchronous JavaScript](./ch07-asynchronous-javascript.md)
