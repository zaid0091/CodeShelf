---
title: Chapter 10 — Modules and Config
description: ES modules in TypeScript, import/export patterns, path aliases, and tsconfig.json essentials.
order: 10
tags: [typescript, modules, tsconfig, imports]
---

# Chapter 10: Modules and Config

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

## Practice Exercise — Chapter 10

```text
Exercise 10.1: Split modules
  a) Create models/user.ts, services/userService.ts, index.ts barrel.
  b) Import from app.ts with type-only imports where appropriate.

Exercise 10.2: tsconfig
  a) Enable strict + noUncheckedIndexedAccess.
  b) Fix resulting errors in a small array-access example.

Exercise 10.3: Path alias
  a) Configure @/* → src/*.
  b) Move a helper to src/lib/format.ts and import via @/lib/format.

Exercise 10.4: Declaration file
  a) Stub types for fictional untyped npm package "csv-magic".
  b) Import and use in typed wrapper function.
```

Next: [Chapter 11 — Async TypeScript](./ch11-async-typescript.md).
