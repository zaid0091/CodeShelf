---
title: Chapter 1 — Introduction to TypeScript
description: What TypeScript is, installation, your first program, and how it compares to JavaScript.
order: 1
tags: [typescript, basics, setup, javascript]
---

# Chapter 1: Introduction to TypeScript

## 1.1 What is TypeScript?

JavaScript powers the web — browsers, servers, mobile apps, and desktop tools. It is dynamically typed: variables can hold any value, and type errors often appear only when the program runs.

TypeScript adds an optional **static type system** on top of JavaScript. You write `.ts` files (or `.tsx` for React), run-rate compiler checks types, then emits plain `.js` that runs anywhere JavaScript runs.

```text
┌─────────────────────────────────────────────────────────┐
│                    TypeScript workflow                   │
├─────────────────────────────────────────────────────────┤
│  You write:     app.ts  (types + modern JS syntax)       │
│       ↓                                                  │
│  tsc compiles:  type-check + transpile to target JS      │
│       ↓                                                  │
│  You run:       app.js  (in Node, browser, or bundler)   │
└─────────────────────────────────────────────────────────┘
```

> **Definition:** TypeScript is a **typed superset of JavaScript** developed by Microsoft. "Superset" means every valid JavaScript program is valid TypeScript — you can rename `.js` to `.ts` and gradually add types.

### Who uses TypeScript?

| Company / Project | Why |
|-------------------|-----|
| Microsoft | Created TypeScript; uses it in VS Code |
| Google | Angular is TypeScript-first |
| Meta | React teams widely adopt TS for large codebases |
| Netflix, Airbnb, Slack | Scale and maintainability |

### What TypeScript is NOT

| Myth | Reality |
|------|---------|
| A new runtime | It compiles away — no TS VM |
| Required for React/Vue | Optional but strongly recommended at scale |
| Slower at runtime | Types are erased; emitted JS performance is the same |
| A replacement for learning JS | You must know JavaScript first |

## 1.2 Why use TypeScript?

### Catch bugs before production

```typescript
function getUserAge(user: { name: string; age: number }) {
  return user.age;
}

// Error at compile time — 'age' might be undefined in your mental model,
// but TS catches typos and wrong types immediately:
getUserAge({ name: "Ada", age: "30" }); // ❌ Type 'string' is not assignable to type 'number'
```

### Better editor experience

When types are known, your IDE can:

- Autocomplete property names and method signatures
- Show inline documentation from JSDoc and types
- Rename symbols safely across files
- Highlight unreachable code and unused variables

### Safer refactoring

Large codebases change constantly. Types act as living documentation and guardrails when you rename APIs or restructure modules.

### Gradual adoption

You can migrate file-by-file. Use `// @ts-check` in JS files or `allowJs` in `tsconfig.json` to mix typed and untyped code in one project.

> **Key takeaway:** TypeScript trades a compile step for fewer runtime surprises, clearer contracts between modules, and a dramatically better editing experience.

## 1.3 TypeScript vs JavaScript

| Aspect | JavaScript | TypeScript |
|--------|------------|------------|
| File extension | `.js`, `.mjs`, `.cjs` | `.ts`, `.tsx` |
| Type checking | Runtime only (or none) | Compile time + optional strict checks |
| Execution | Direct in browser/Node | Must compile (or use ts-node in dev) |
| New syntax | Depends on engine/bundler | Can use newer syntax; tsc downlevels |
| Interfaces / enums | Not built-in | First-class language features |
| Learning curve | Lower initially | Higher upfront, pays off in teams |

### Same runtime, extra layer

```typescript
// TypeScript source
const multiply = (a: number, b: number): number => a * b;

// Emitted JavaScript (types removed)
const multiply = (a, b) => a * b;
```

Type annotations exist only for the compiler. They never appear in the output JavaScript.

### When to stick with JavaScript

- Small scripts or one-off automation
- Prototypes where speed of iteration beats safety
- Libraries targeting zero build step for consumers (some still ship `.d.ts` separately)

### When TypeScript shines

- Teams of two or more on a long-lived codebase
- APIs with complex data shapes (forms, REST, GraphQL)
- React/Vue/Angular applications with many components
- Libraries where public API clarity matters

## 1.4 Installation and setup

### Prerequisites

- **Node.js** 18+ (includes npm)
- A code editor with TypeScript support (VS Code / Cursor recommended)

### Install TypeScript globally (optional)

```bash
npm install -g typescript
tsc --version
```

### Project-local install (recommended)

```bash
mkdir my-ts-app && cd my-ts-app
npm init -y
npm install --save-dev typescript
npx tsc --init
```

This creates `tsconfig.json` — covered in depth in [Chapter 10](./ch10-modules-and-config.md).

### Minimal tsconfig for learning

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "NodeNext",
    "strict": true,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src/**/*"]
}
```

### Project layout

```text
my-ts-app/
├── package.json
├── tsconfig.json
├── src/
│   └── index.ts
└── dist/          ← generated by tsc
    └── index.js
```

## 1.5 Your first TypeScript program

Create `src/index.ts`:

```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

function greet(user: User): string {
  return `Hello, ${user.name}! Your email is ${user.email}.`;
}

const currentUser: User = {
  id: 1,
  name: "Grace Hopper",
  email: "grace@example.com",
};

console.log(greet(currentUser));
```

Compile and run:

```bash
npx tsc
node dist/index.js
```

Expected output:

```text
Hello, Grace Hopper! Your email is grace@example.com.
```

### Breakdown of the example

| Line / concept | Purpose |
|----------------|---------|
| `interface User` | Describes the shape of a user object |
| `user: User` | Parameter must match the interface |
| `: string` return type | Function must return a string |
| `const currentUser: User` | Explicit annotation (inference would work here too) |

### Introducing type inference

TypeScript often infers types without annotations:

```typescript
const count = 42;           // inferred as number
const label = "active";     // inferred as string
const items = [1, 2, 3];      // inferred as number[]

// Explicit when inference is too wide or unclear:
let status: "pending" | "done" = "pending";
```

> **Definition:** **Type inference** is the compiler's ability to deduce types from values and context, reducing the need for manual annotations.

## 1.6 The TypeScript compiler (`tsc`)

Common commands:

| Command | Effect |
|---------|--------|
| `npx tsc` | Compile once using tsconfig.json |
| `npx tsc --watch` | Recompile on file changes |
| `npx tsc --noEmit` | Type-check only, no output files |
| `npx tsc src/index.ts` | Compile single file (ignores tsconfig unless specified) |

### Compiler flags worth knowing early

| Flag | Meaning |
|------|---------|
| `--strict` | Enables all strict type-checking options |
| `--target ES2020` | JavaScript version to emit |
| `--module NodeNext` | Module system for output |
| `--skipLibCheck` | Skip type checking of declaration files (faster builds) |

## 1.7 Running TypeScript in development

For quick experiments:

```bash
npm install --save-dev ts-node
npx ts-node src/index.ts
```

For production, always compile to JavaScript or use a bundler (esbuild, Vite, webpack) that handles TypeScript.

### Watch mode workflow

```bash
# Terminal 1: continuous compile
npx tsc --watch

# Terminal 2: run output
node dist/index.js
```

## 1.8 Common errors beginners see

### Error: Object is possibly 'undefined'

```typescript
function printLength(s?: string) {
  console.log(s.length); // ❌ 's' is possibly 'undefined'
}

function printLengthSafe(s?: string) {
  console.log(s?.length ?? 0); // ✅ optional chaining + nullish coalescing
}
```

### Error: Type 'X' is not assignable to type 'Y'

This is TypeScript protecting you from incompatible values. Read the error message — it usually names both types and the property that failed.

### Error: Cannot find module

Often means missing types:

```bash
npm install --save-dev @types/node
```

## 1.9 TypeScript in the ecosystem

| Layer | TypeScript role |
|-------|-----------------|
| React | `.tsx` components, typed props and hooks → [Ch 12](./ch12-react-with-typescript.md) |
| Node.js | Typed request handlers, env config, DB models |
| Deno / Bun | First-class TypeScript support |
| Testing | Jest/Vitest with `@types/jest` or built-in types |

Next chapters build the type system from the ground up:

- [Chapter 2 — Types & Primitives](./ch02-types-and-primitives.md)
- [Chapter 3 — Interfaces & Type Aliases](./ch03-interfaces-and-type-aliases.md)

> **Key takeaway:** TypeScript is JavaScript plus static types. Install it per-project, enable `strict`, write `.ts` files, compile with `tsc`, and treat compiler errors as feedback — not annoyances.

## Practice Exercise — Chapter 1

```text
Exercise 1.1: Setup
  a) Create a new folder and initialize npm.
  b) Install TypeScript locally and run `npx tsc --init`.
  c) Add src/index.ts with a typed function that formats a product title and price.

Exercise 1.2: Compare JS vs TS
  a) Write a JavaScript function that adds two values.
  b) Port it to TypeScript with number parameters and return type.
  c) Intentionally pass a string — observe the compile error.

Exercise 1.3: Type inference
  a) Declare three variables without type annotations (array, object, boolean).
  b) Hover in the editor or use `tsc --noEmit` to confirm inferred types.
  c) Change one value so inference would become too wide; add an explicit type.

Exercise 1.4: Reading errors
  a) Create an interface `Book` with title and pages.
  b) Pass an object missing `pages` to a function expecting `Book`.
  c) Write down the exact error message and fix the object.
```

Answers and deeper typing rules begin in [Chapter 2](./ch02-types-and-primitives.md).
