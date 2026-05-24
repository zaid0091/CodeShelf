---
title: Modules and npm
description: ES modules import/export, Node.js modules, package.json, and npm workflows
order: 10
tags: [javascript, modules, npm, package.json, node, import, export]
---

# Chapter 10: Modules and npm

## 10.1 Why modules?

> **Definition:** A **module** is a file that exports selected bindings and imports from other files. Modules enable separation of concerns, reuse, and clear dependencies.

Without modules, all code shares one global scope — naming collisions and spaghetti imports result.

## 10.2 ES modules syntax

### Named exports

```javascript
// utils.js
export const VERSION = "1.0.0";

export function formatDate(d) {
  return d.toISOString().slice(0, 10);
}

export class Logger {
  log(msg) { console.log(msg); }
}
```

### Default export (one per file)

```javascript
// config.js
export default {
  apiUrl: "https://api.example.com",
  timeout: 5000,
};
```

### Importing

```javascript
// app.js
import config from "./config.js";
import { VERSION, formatDate } from "./utils.js";
import * as utils from "./utils.js";

console.log(config.apiUrl);
console.log(utils.VERSION);
```

| Pattern | Example |
|---------|---------|
| Named import | `import { x } from "./m.js"` |
| Rename | `import { x as y } from "./m.js"` |
| Default | `import App from "./App.js"` |
| Combined | `import App, { helper } from "./App.js"` |
| Side effect only | `import "./polyfills.js"` |

## 10.3 Module rules

- Imports are hoisted and read-only bindings.
- Paths must include extension in browsers: `./utils.js`.
- `"use strict"` is automatic.
- Top-level variables are module-scoped, not global.

```html
<script type="module" src="main.js"></script>
```

## 10.4 Node.js module systems

| System | Extension / config | Syntax |
|--------|-------------------|--------|
| ESM | `.mjs` or `"type": "module"` in package.json | `import` / `export` |
| CommonJS | `.cjs` or default in older Node | `require` / `module.exports` |

### ESM in Node

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "type": "module"
}
```

```javascript
// index.js
import { readFile } from "fs/promises";

const text = await readFile("./data.txt", "utf8");
console.log(text);
```

### CommonJS (legacy)

```javascript
const fs = require("fs");
const { helper } = require("./helper.cjs");

module.exports = { helper };
```

## 10.5 `package.json` essentials

```json
{
  "name": "codeshelf-demo",
  "version": "1.0.0",
  "description": "Learning project",
  "type": "module",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "node --watch index.js",
    "test": "node --test"
  },
  "keywords": ["javascript", "learning"],
  "author": "You",
  "license": "MIT",
  "dependencies": {
    "lodash-es": "^4.17.21"
  },
  "devDependencies": {
    "prettier": "^3.0.0"
  }
}
```

| Field | Purpose |
|-------|---------|
| `name` | Package identifier |
| `version` | Semver version |
| `main` | Entry point (CJS) |
| `module` / `exports` | ESM entry (modern) |
| `scripts` | `npm run <script>` commands |
| `dependencies` | Runtime packages |
| `devDependencies` | Build/test-only packages |

## 10.6 npm commands

```bash
npm init -y              # create package.json
npm install lodash       # add dependency
npm install -D eslint    # dev dependency
npm uninstall lodash
npm run start
npm list --depth=0
```

### Semantic versioning

| Symbol | Meaning |
|--------|---------|
| `^1.2.3` | Compatible with 1.x (minor/patch) |
| `~1.2.3` | Compatible with 1.2.x |
| `1.2.3` | Exact version |

## 10.7 Importing npm packages

```javascript
// ESM
import _ from "lodash-es";
import { debounce } from "lodash-es";

// Or specific path
import express from "express";
```

```javascript
// CommonJS
const express = require("express");
```

## 10.8 Project structure example

```text
my-project/
├── package.json
├── package-lock.json
├── index.js
├── src/
│   ├── api/
│   │   └── client.js
│   ├── utils/
│   │   └── format.js
│   └── app.js
└── node_modules/    # installed packages (gitignore)
```

```javascript
// src/app.js
import { fetchUsers } from "./api/client.js";
import { formatDate } from "./utils/format.js";
```

## 10.9 Bundlers (overview)

| Tool | Role |
|------|------|
| Vite | Fast dev server, ESM-native |
| Webpack | Mature, highly configurable |
| esbuild | Extremely fast bundling |
| Rollup | Library bundling |

Browser apps often use a bundler; Node scripts often run files directly.

## 10.10 Environment variables

```javascript
// Node — never commit secrets
const apiKey = process.env.API_KEY;

if (!apiKey) {
  throw new Error("API_KEY is required");
}
```

Use `.env` files with packages like `dotenv` in Node projects (add `.env` to `.gitignore`).

## 10.11 Chapter summary

| Topic | Action |
|-------|--------|
| ES modules | `import` / `export` in `.js` with `"type": "module"` |
| npm | `npm init`, `npm install`, `npm run` |
| Lock file | Commit `package-lock.json` for reproducible installs |
| CJS vs ESM | Prefer ESM for new Node projects |

## Exercises

### Exercise 10.1 — Mini package

Initialize a project with `npm init -y`, set `"type": "module"`, create `math.js` and `index.js` that imports and logs results.

### Exercise 10.2 — Scripts

Add `"dev"` script using `node --watch` (Node 18+) and a `"start"` script.

### Exercise 10.3 — Install lodash-es

Install `lodash-es`, import `chunk` and split `[1,2,3,4,5]` into pairs.

### Exercise 10.4 — Refactor

Split a single-file script into `config.js`, `api.js`, and `main.js` with clear exports.

---

**Previous:** [Chapter 9: Error Handling](./ch09-error-handling.md) · **Next:** [Chapter 11: Browser APIs](./ch11-browser-apis.md)
