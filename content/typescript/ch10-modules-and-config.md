---
title: Chapter 10 — Modules and Config
description: ES modules, imports/exports, path aliases, tsconfig.json, and project references.
order: 10
tags: [typescript, modules, tsconfig, imports]
---


# Chapter 10: Modules and Config

> **Modules organize code; tsconfig controls the compiler. This chapter connects both for real projects.**
> Take your time with each section. TypeScript rewards patience — read compiler errors carefully and experiment in a small project as you go.

---


## Table of Contents

1. [ES Modules](#es-modules)
2. [Named and Default Exports](#named-and-default-exports)
3. [import type](#import-type)
4. [Path Aliases](#path-aliases)
5. [Barrel Files](#barrel-files)
6. [tsconfig Structure](#tsconfig-structure)
7. [strict Options](#strict-options)
8. [Project References](#project-references)
9. [Ambient Declarations](#ambient-declarations)
10. [package.json types](#packagejson-types)
11. [Vite + TS](#vite-ts)
12. [Best Practices](#best-practices)
13. [Interview Points](#interview-points)
14. [Exercises](#exercises)
15. [Chapter Summary](#chapter-summary)

---

## 10.1 Modules in TypeScript

TypeScript follows **ECMAScript modules** (ESM). Each file is its own module with its own scope.

```typescript
// math.ts
export function add(a: number, b: number): number {
  return a + b;
}

export const PI = 3.14159;

export default function multiply(a: number, b: number): number {
  return a * b;
}
```

```typescript
// app.ts
import multiply, { add, PI } from "./math.js";

console.log(add(2, 3));
console.log(multiply(2, PI));
```

> **Definition:** A **module** is a file that exports values and can import from other modules. TypeScript resolves types at compile time; bundlers/runtimes resolve paths at execution.

## 10.2 Export patterns

| Pattern | Syntax | Use case |
|---------|--------|----------|
| Named export | `export const x = 1` | Multiple exports per file |
| Default export | `export default fn` | Single main export (components) |
| Re-export | `export { x } from "./x"` | Barrel files |
| Export type | `export type { User }` | Type-only exports (erasable) |
| Namespace | `export namespace Utils {}` | Rare; prefer modules |

### Type-only imports and exports

```typescript
import type { User } from "./models.js";
export type { User, Post } from "./models.js";

import { type User, createUser } from "./users.js"; // inline type import (TS 4.5+)
```

Type-only imports are erased — no runtime import emitted (with `verbatimModuleSyntax` rules apply).

## 10.3 Import paths

```typescript
import { helper } from "./utils/helper.js";   // relative
import fs from "node:fs";                      // Node built-in (NodeNext)
import express from "express";                 // package
import { Button } from "@/components/Button"; // path alias (configured)
```

### Extension notes (Node16/NodeNext)

With `"moduleResolution": "NodeNext"`, relative imports often need `.js` extension in source (pointing to emitted file):

```typescript
import { User } from "./models.js"; // models.ts compiles to models.js
```

Bundlers (Vite, webpack) may allow extensionless paths — follow project convention.

## 10.4 Barrel files (index.ts)

```typescript
// components/index.ts
export { Button } from "./Button.js";
export { Input } from "./Input.js";
export type { ButtonProps } from "./Button.js";
```

```typescript
import { Button, Input } from "./components/index.js";
// or "./components" if resolver allows
```

Avoid deep barrel cycles — they can slow builds and cause circular dependency issues.

## 10.5 tsconfig.json essentials

Generated via `npx tsc --init`. Key sections:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2022", "DOM"],
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### Critical compilerOptions explained

| Option | Purpose |
|--------|---------|
| `target` | ECMAScript version emitted |
| `module` | Module format (CommonJS, ESNext, NodeNext) |
| `moduleResolution` | How imports resolve |
| `strict` | Enables strict family flags |
| `noEmit` | Type-check only (used with bundlers) |
| `jsx` | `react-jsx` for React 17+ |
| `baseUrl` / `paths` | Path aliases |
| `types` | Include ambient types (`node`, `jest`) |
| `allowJs` | Mix JavaScript in project |
| `checkJs` | Type-check JS files |
| `isolatedModules` | Each file transpilable alone (required by Babel/esbuild) |
| `verbatimModuleSyntax` | Enforce type-only imports for erased types |

> **Key takeaway:** Enable `strict`, match `module`/`moduleResolution` to your runtime (NodeNext for Node, bundler for Vite), and use `noEmit` when a bundler handles compilation.

## 10.6 Path aliases

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"]
    }
  }
}
```

Also configure bundler (Vite `resolve.alias`, tsconfig-paths for Node).

## 10.7 Project references (monorepos)

Split large repos:

```json
// packages/shared/tsconfig.json
{
  "compilerOptions": {
    "composite": true,
    "declaration": true,
    "outDir": "./dist"
  }
}

// packages/app/tsconfig.json
{
  "references": [{ "path": "../shared" }]
}
```

Build with `tsc --build`.

## 10.8 include, exclude, files

| Field | Role |
|-------|------|
| `include` | Glob patterns to compile |
| `exclude` | Subtract from include (node_modules excluded by default) |
| `files` | Explicit file list (uncommon) |

## 10.9 Ambient declarations (.d.ts)

When types are missing for a JS library:

```typescript
// types/legacy-lib.d.ts
declare module "legacy-lib" {
  export function doSomething(input: string): number;
}
```

Or install `@types/package-name` from DefinitelyTyped.

## 10.10 triple-slash directives (legacy)

```typescript
/// <reference types="node" />
```

Prefer `import` and `types` in tsconfig over triple-slash in new code.

## 10.11 Common module resolution errors

| Error | Fix |
|-------|-----|
| Cannot find module 'x' | Install package + `@types/x` |
| Relative import needs .js extension | Add `.js` or change moduleResolution |
| Circular dependency | Refactor shared code to third module |
| Type-only used as value | Use `import type` or value import |
| Duplicate identifier | Check barrel re-exports |

## 10.12 Package.json integration

```json
{
  "name": "my-app",
  "type": "module",
  "scripts": {
    "build": "tsc",
    "typecheck": "tsc --noEmit",
    "dev": "tsx watch src/index.ts"
  },
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    }
  }
}
```

`"type": "module"` makes Node treat `.js` as ESM.

## 10.13 Vite + TypeScript (typical frontend)

Vite uses esbuild for transpile; `tsc --noEmit` for type-check:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "noEmit": true
  }
}
```

> **Key takeaway:** Modules organize code; tsconfig aligns compiler with runtime. Treat tsconfig as team contract — review changes in PRs.
<!-- codeshelf:generated-appendix -->

---

## Monorepo layout

```text
packages/
  api/          ← tsconfig, src
  web/          ← references api types
  shared-types/ ← shared interfaces
```

Use **project references** so `tsc -b` builds in dependency order.

---

## Module graph — mental model

```text
app.ts  ──imports──►  user.ts
   │                      │
   └──imports──►  types.ts (import type only)
```

Keep **value imports** for functions/classes and **`import type`** for types to help bundlers tree-shake and avoid circular value dependencies.

---

## tsconfig layers

| File | Purpose |
|------|---------|
| `tsconfig.json` | Root; may reference subprojects |
| `tsconfig.app.json` | App source only |
| `tsconfig.node.json` | Vite config, scripts |

Split configs so editor and CI only check relevant files.

---

## tsconfig strict family


```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "exactOptionalPropertyTypes": true
  }
}
```


---

## ESM import/export


```typescript
// math.ts
export function add(a: number, b: number) { return a + b; }
export default function pi() { return 3.14; }

// app.ts
import pi, { add } from "./math.js";
import type { SomeType } from "./types.js";
```


---

## Path aliases


```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": { "@/*": ["src/*"] }
  }
}
```


---

## Ambient declarations


```typescript
declare module "*.css" {
  const classes: { readonly [key: string]: string };
  export default classes;
}
```


---

## import type


```typescript
import type { User } from "./models.js";
```


---

## NodeNext resolution


For Node ESM, use `"module": "NodeNext"` and include `.js` extensions in import specifiers.


---

## Declaration files


Publish `declaration: true` for libraries so consumers get `.d.ts` files.


---

## Definition — Module

> **Definition:** **Module** — A file that exports values/types and imports from other files — ES modules are the standard.


---

## tsconfig strict family


| Flag | Benefit |
|------|---------|
| `strictNullChecks` | Catches null/undefined bugs |
| `noImplicitAny` | Forces explicit types |
| `noUncheckedIndexedAccess` | Indexing may be undefined |


---

## Barrel file caution


`index.ts` re-exports can create circular imports. Prefer direct imports in large codebases.


---

## Vite + TypeScript


Vite transpiles fast; run `tsc --noEmit` in CI for full type-checking.


---

## package.json types field


```json
{
  "name": "my-lib",
  "types": "./dist/index.d.ts",
  "exports": { ".": { "types": "./dist/index.d.ts", "import": "./dist/index.js" } }
}
```


---

## include / exclude


```json
{
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "**/*.test.ts"]
}
```


---

## Review Q1

**Q:** Why `.js` in import paths with NodeNext? **A:** Node ESM resolves the emitted file extension at runtime.

---

## Review Q2

**Q:** What is `skipLibCheck`? **A:** Skips type-checking of declaration files — faster builds, fewer third-party errors.

---

## Review Q3

**Q:** `isolatedModules`? **A:** Ensures each file can transpile alone — required by Babel/esbuild.

---

## Scenario — library package


```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "NodeNext",
    "declaration": true,
    "declarationMap": true,
    "outDir": "dist",
    "rootDir": "src",
    "strict": true
  },
  "include": ["src"]
}
```

Publish only `dist/` — consumers import types from `.d.ts` files.


---

## Scenario — ambient shims


```typescript
// global.d.ts
declare const __APP_VERSION__: string;

// vite.config defines __APP_VERSION__ at build time
```


---

## Best Practices

- ✅ Use `import type` for type-only imports (erased, helps bundlers).
- ✅ One tsconfig per package in monorepos; use project references.

---

## Common Mistakes

Watch for these patterns — they cost hours in real projects.

### Mistake 1: Barrel file cycles

index.ts re-exports causing circular imports

Import from concrete modules.

---

### Mistake 2: Wrong moduleResolution

Cannot find module in Node ESM

Set NodeNext or bundler per tool.

---

## Interview Points

> **📌 Interview Point 1: What is moduleResolution?**

How TS resolves import paths.

---

> **📌 Interview Point 2: import type vs import?**

type-only imports elided from JS emit.

---

## Exercises

Practice with `npx tsc --noEmit` after each exercise.

### Exercise 10.1: Split modules ⭐

**Task:** Move utils to separate file and import.

<details><summary>💡 Hint</summary>

named exports.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
// utils.ts
export function clamp(n: number, min: number, max: number) { return Math.min(max, Math.max(min, n)); }
// app.ts
import { clamp } from "./utils.js";
```

</details>

---

### Exercise 10.2: Path alias ⭐⭐

**Task:** Configure @/* paths.

<details><summary>💡 Hint</summary>

paths in tsconfig.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": { "@/*": ["src/*"] }
  }
}
```

</details>

---

### Exercise 10.3: declare module ⭐⭐⭐

**Task:** Ambient module for .css imports.

<details><summary>💡 Hint</summary>

shims.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
declare module "*.css" {
  const classes: { readonly [key: string]: string };
  export default classes;
}
```

</details>

---

### Exercise 10.4: strict flags ⭐⭐

**Task:** Document 5 strict flags in tsconfig.

<details><summary>💡 Hint</summary>

strict family.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true
  }
}
```

</details>

---

### Exercise 10.5: type-only import ⭐⭐⭐

**Task:** Refactor to import type.

<details><summary>💡 Hint</summary>

isolatedModules friendly.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
import type { User } from "./models.js";
```

</details>

---

### Exercise 10.6: Vite config ⭐⭐

**Task:** Align moduleResolution bundler.

<details><summary>💡 Hint</summary>

Chapter tooling.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```json
{
  "compilerOptions": {
    "moduleResolution": "bundler",
    "module": "ESNext"
  }
}
```

</details>

---

## Chapter Summary

You covered a lot in this chapter. Here is a concise recap:

- ES modules are standard; tsconfig must match your runtime/bundler.
- Path aliases improve imports.

---

---

## Navigation

**⬅️ [Previous: Enums and Literals](./ch09-enums-and-literals.md)**  
**➡️ [Next: Async TypeScript](./ch11-async-typescript.md)**

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
- **TypeScript** — Typed superset of JavaScript that compiles to JS.
- **Inference** — Compiler deduces types without explicit annotations.
- **Union** — Value may be one of several types: `A | B`.
- **Narrowing** — Refining a union to a specific type in a branch.
- **Generic** — Type parameter for reusable APIs.
- **Interface** — Named object shape contract.
- **Utility type** — Built-in type transformer like `Partial`.

*Last updated: 2025 | TypeScript course — CodeShelf*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
