---
title: Modules and npm
description: ES modules import/export, Node.js modules, package.json, and npm workflows
order: 10
tags: [javascript, modules, npm, package.json, node, import, export]
---

# Chapter 10: Modules and npm

> "Modules turn a pile of scripts into a maintainable system with explicit dependencies."

---

## Table of Contents

1. [Why Modules?](#why-modules?)
2. [Named Exports](#named-exports)
3. [Default Exports](#default-exports)
4. [Import Syntax](#import-syntax)
5. [Module Rules and Strict Mode](#module-rules-and-strict-mode)
6. [Node.js ESM vs CommonJS](#nodejs-esm-vs-commonjs)
7. [package.json Essentials](#packagejson-essentials)
8. [npm Commands](#npm-commands)
9. [Semantic Versioning](#semantic-versioning)
10. [Project Structure](#project-structure)
11. [Bundlers Overview](#bundlers-overview)
12. [Environment Variables](#environment-variables)
13. [Dynamic import in Node](#dynamic-import-in-node)
14. [Common Mistakes](#common-mistakes)
15. [Best Practices](#best-practices)
16. [Interview Points](#interview-points)
17. [Exercises](#exercises)
18. [Chapter Summary](#chapter-summary)

---

## Why Modules?

### Definition

A **module** is a file with its own scope that explicitly exports and imports bindings.

### Why It Matters

Without modules, globals collide — spaghetti script tags.

### How It Works

ES modules are standard in browsers and modern Node.


```js
// utils.js
export function formatDate(d) { return d.toISOString().slice(0, 10); }
```


---

## Named Exports

### Definition

Export multiple bindings by name from one file.

### Why It Matters

Utilities, constants, types.

### How It Works


```js
export const VERSION = "1.0.0";
export class Logger { log(m) { console.log(m); } }
```




---

## Default Exports

### Definition

One **default** export per file — importers choose any name.

### Why It Matters

Main component or config object per file.

### How It Works


```js
export default { apiUrl: "https://api.example.com" };
```




---

## Import Syntax

### Definition

Static `import` is hoisted; bindings are live read-only.

### Why It Matters

Tree-shaking removes unused exports in bundlers.

### How It Works


```js
import config from "./config.js";
import { VERSION, formatDate } from "./utils.js";
import * as utils from "./utils.js";
```




---

## Module Rules and Strict Mode

### Definition

Modules are always strict; top-level vars are module-scoped.

### Why It Matters

Predictable behavior.

### How It Works

Include `.js` extension in browser imports.


```js
// import "./setup.js"; // side effect only
```


---

## Node.js ESM vs CommonJS

### Definition

Node supports **ESM** (`import`) and **CommonJS** (`require`).

### Why It Matters

Legacy npm packages may be CJS only.

### How It Works

Set `"type": "module"` in package.json to enable ESM in `.js` files.


```js
// ESM
import { readFile } from "fs/promises";
// CJS
const fs = require("fs");
```


---

## package.json Essentials

### Definition

Manifest: name, version, scripts, dependencies.

### Why It Matters

npm uses it to install and run projects.

### How It Works


```js
{
  "name": "my-app",
  "type": "module",
  "scripts": { "start": "node index.js" },
  "dependencies": { "lodash-es": "^4.17.21" }
}
```




---

## npm Commands

### Definition

`npm init`, `install`, `run`, `uninstall`, `list`.

### Why It Matters

Ecosystem standard for JavaScript dependencies.

### How It Works


```js
npm init -y
npm install lodash-es
npm run start
```




---

## Semantic Versioning

### Definition

Versions `MAJOR.MINOR.PATCH`; ranges `^` and `~` in package.json.

### Why It Matters

Understand breaking updates.

### How It Works

| Symbol | Meaning |
|--------|--------|
| ^1.2.3 | compatible 1.x |
| ~1.2.3 | compatible 1.2.x |



---

## Project Structure

### Definition

Split `src/`, `api/`, `utils/` with clear imports.

### Why It Matters

Scales with team size.

### How It Works

```text
my-project/
├── package.json
├── src/app.js
└── src/utils/format.js
```



---

## Bundlers Overview

### Definition

Vite, Webpack, Rollup, esbuild bundle modules for browsers.

### Why It Matters

Import npm packages in front-end apps.

### How It Works

| Tool | Use |
|------|-----|
| Vite | Dev + ESM |
| Webpack | Legacy apps |



---

## Environment Variables

### Definition

`process.env` in Node; never commit secrets.

### Why It Matters

API keys from environment.

### How It Works


```js
const key = process.env.API_KEY;
if (!key) throw new Error("API_KEY required");
```




---

## Dynamic import in Node

### Definition

`await import()` for conditional loading.

### Why It Matters

Lazy load heavy modules.

### How It Works


```js
const mod = await import("./heavy.js");
```




---

### Import Syntax — Example 1

```js
// Example 1: practical pattern for import syntax
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


### Import Syntax — Example 2

```js
// Example 2: practical pattern for import syntax
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


### Import Syntax — Example 3

```js
// Example 3: practical pattern for import syntax
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


### Import Syntax — Example 4

```js
// Example 4: practical pattern for import syntax
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


### Import Syntax — Example 5

```js
// Example 5: practical pattern for import syntax
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

### package.json Essentials — Example 1

```js
// Example 1: practical pattern for package.json essentials
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


### package.json Essentials — Example 2

```js
// Example 2: practical pattern for package.json essentials
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


### package.json Essentials — Example 3

```js
// Example 3: practical pattern for package.json essentials
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


### package.json Essentials — Example 4

```js
// Example 4: practical pattern for package.json essentials
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


### package.json Essentials — Example 5

```js
// Example 5: practical pattern for package.json essentials
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

### npm Commands — Example 1

```js
// Example 1: practical pattern for npm commands
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


### npm Commands — Example 2

```js
// Example 2: practical pattern for npm commands
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


### npm Commands — Example 3

```js
// Example 3: practical pattern for npm commands
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


### npm Commands — Example 4

```js
// Example 4: practical pattern for npm commands
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


### npm Commands — Example 5

```js
// Example 5: practical pattern for npm commands
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

### Node.js ESM vs CommonJS — Example 1

```js
// Example 1: practical pattern for node.js esm vs commonjs
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


### Node.js ESM vs CommonJS — Example 2

```js
// Example 2: practical pattern for node.js esm vs commonjs
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


### Node.js ESM vs CommonJS — Example 3

```js
// Example 3: practical pattern for node.js esm vs commonjs
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


### Node.js ESM vs CommonJS — Example 4

```js
// Example 4: practical pattern for node.js esm vs commonjs
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


### Node.js ESM vs CommonJS — Example 5

```js
// Example 5: practical pattern for node.js esm vs commonjs
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

### Mixing default import name wrong

Default can be any name; named must match.


## Best Practices

- Prefer ESM for new Node projects.
- Commit package-lock.json.
- Use npm scripts for tasks.

## Interview Points

### ESM vs CJS?

import/export vs require/module.exports.

### What is package-lock?

Exact dependency tree for reproducible installs.


## Exercises

### Exercise 10.1 — Mini package

npm init, math.js, index.js

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
export const add = (a,b)=>a+b;
```


</details>

### Exercise 10.2 — Scripts

Add dev with node --watch

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
"dev": "node --watch index.js"
```


</details>

### Exercise 10.3 — lodash-es

chunk array

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
import { chunk } from 'lodash-es'; chunk([1,2,3,4,5],2);
```


</details>

### Exercise 10.4 — Refactor modules

config, api, main split

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
import { apiUrl } from './config.js';
```


</details>

### Exercise 10.5 — Named vs default

Export both from calc.js

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
export default multiply; export { add };
```


</details>

### Exercise 10.6 — Side effect import

polyfills.js runs on import

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
import './polyfills.js';
```


</details>

## Chapter Summary

| Topic | Action |
|-------|--------|
| ESM | import/export |
| npm | install & run |
| Lock file | commit |


---

## Next Chapter

Next: **Browser APIs** — fetch, storage, JSON.

---

**⬅️ [Previous: Error Handling](./ch09-error-handling.md)** · **➡️ [Next Chapter: Browser APIs →](./ch11-browser-apis.md)**

---

*Last updated: 2026 | Chapter 10 of the Complete JavaScript Guide*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*

---

## Worked Example 1: Modules and npm

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 1 for Chapter 10
function demo1(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo1({ a: 1, b: 2 }));
console.log(demo1([1, 2, 3]));
console.log(demo1("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 2: Modules and npm

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 2 for Chapter 10
function demo2(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo2({ a: 1, b: 2 }));
console.log(demo2([1, 2, 3]));
console.log(demo2("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 3: Modules and npm

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 3 for Chapter 10
function demo3(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo3({ a: 1, b: 2 }));
console.log(demo3([1, 2, 3]));
console.log(demo3("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 4: Modules and npm

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 4 for Chapter 10
function demo4(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo4({ a: 1, b: 2 }));
console.log(demo4([1, 2, 3]));
console.log(demo4("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 5: Modules and npm

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 5 for Chapter 10
function demo5(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo5({ a: 1, b: 2 }));
console.log(demo5([1, 2, 3]));
console.log(demo5("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 6: Modules and npm

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 6 for Chapter 10
function demo6(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo6({ a: 1, b: 2 }));
console.log(demo6([1, 2, 3]));
console.log(demo6("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 7: Modules and npm

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 7 for Chapter 10
function demo7(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo7({ a: 1, b: 2 }));
console.log(demo7([1, 2, 3]));
console.log(demo7("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 8: Modules and npm

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 8 for Chapter 10
function demo8(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo8({ a: 1, b: 2 }));
console.log(demo8([1, 2, 3]));
console.log(demo8("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 9: Modules and npm

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 9 for Chapter 10
function demo9(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo9({ a: 1, b: 2 }));
console.log(demo9([1, 2, 3]));
console.log(demo9("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 10: Modules and npm

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 10 for Chapter 10
function demo10(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo10({ a: 1, b: 2 }));
console.log(demo10([1, 2, 3]));
console.log(demo10("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 11: Modules and npm

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 11 for Chapter 10
function demo11(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo11({ a: 1, b: 2 }));
console.log(demo11([1, 2, 3]));
console.log(demo11("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 12: Modules and npm

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 12 for Chapter 10
function demo12(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo12({ a: 1, b: 2 }));
console.log(demo12([1, 2, 3]));
console.log(demo12("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.

