from gen_ts_common import fm, welcome, toc, summary, best_practices
from gen_ts_chapters import mistakes, interviews, exercises, nav, deep_dive_sections, GENERATED_APPENDIX
from gen_ts_extra import get_extra


def build() -> str:
    return (
        fm(
            "Chapter 1 — Introduction to TypeScript",
            "What TypeScript is, installation, your first program, and how it compares to JavaScript.",
            1,
            ["typescript", "basics", "setup", "javascript"],
        )
        + welcome(
            "Chapter 1: Introduction to TypeScript",
            "Welcome to TypeScript! This chapter explains what it is, why teams adopt it, how to install the compiler, and how to run your first typed program.",
        )
        + toc(
            [
                "What is TypeScript?",
                "A Short History",
                "Why Use TypeScript?",
                "TypeScript vs JavaScript",
                "How TypeScript Works (Compile Pipeline)",
                "Type Erasure",
                "Who Uses TypeScript?",
                "Prerequisites",
                "Installation and Setup",
                "Project Structure",
                "Your First TypeScript Program",
                "Type Annotations and Inference",
                "The TypeScript Compiler (tsc)",
                "tsconfig.json Essentials",
                "Running TypeScript in Development",
                "TypeScript in the Ecosystem",
                "Gradual Adoption and Migration",
                "Reading Compiler Errors",
                "Best Practices",
                "Common Mistakes",
                "Interview Points",
                "Exercises",
                "Chapter Summary",
            ]
        )
        + BODY
        + GENERATED_APPENDIX
        + "\n"
        + deep_dive_sections(1, get_extra("ch01-introduction.md"))
        + best_practices(
            [
                "Install TypeScript per-project (`npm i -D typescript`), not only globally.",
                "Enable `strict: true` in `tsconfig.json` from day one on new projects.",
                "Treat compiler errors as feedback — fix them before silencing with `@ts-ignore`.",
                "Learn JavaScript fundamentals first; TypeScript is a layer on top.",
                "Use `npx tsc --noEmit` in CI to type-check without emitting files.",
                "Prefer local `src/` and `dist/` separation so you never edit generated JS by hand.",
                "Commit `tsconfig.json` and lockfile; document Node version in README.",
            ]
        )
        + mistakes(
            [
                (
                    "Expecting types at runtime",
                    "```typescript\n// ❌ This does not exist at runtime:\nif (typeof user === 'User') { }\n```",
                    "Types are erased when compiling. Use `typeof` for JS primitives, or validation libraries for API data.",
                ),
                (
                    "Installing only globally",
                    "```bash\n# ❌ Team members may have different tsc versions\ntsc --version\n```",
                    "```bash\n# ✅ Pin version in package.json\nnpm install --save-dev typescript\nnpx tsc --version\n```",
                ),
                (
                    "Disabling strict to silence errors",
                    "```json\n{ \"compilerOptions\": { \"strict\": false } }\n```",
                    "Fix root causes. Disabling strict hides bugs you will pay for in production.",
                ),
                (
                    "Using `any` immediately",
                    "```typescript\nlet data: any = fetchSomething();\n```",
                    "Use `unknown` and narrow, or define an interface for the response shape.",
                ),
                (
                    "Not reading the full error message",
                    "Copying only the first line of a TS error into a search engine.",
                    "Read the full chain — TypeScript often shows *why* a type failed across multiple lines.",
                ),
            ]
        )
        + interviews(
            [
                (
                    "What is TypeScript?",
                    "**Answer:** TypeScript is a statically typed superset of JavaScript developed by Microsoft. It adds optional type annotations and compile-time checking, then compiles to plain JavaScript that runs anywhere JS runs.",
                ),
                (
                    "Is TypeScript a separate runtime?",
                    "**Answer:** No. There is no TypeScript VM. The `tsc` compiler (or a bundler like esbuild/Vite) removes types and emits JavaScript.",
                ),
                (
                    "What does 'superset' mean?",
                    "**Answer:** Every valid JavaScript program is valid TypeScript. You can rename `.js` to `.ts` and add types incrementally.",
                ),
                (
                    "What is type erasure?",
                    "**Answer:** Types exist only at compile time. They are stripped from output JS, so there is zero runtime type overhead from annotations.",
                ),
                (
                    "Why do companies adopt TypeScript?",
                    "**Answer:** Fewer runtime bugs, safer refactors, better IDE support, clearer contracts between modules, and easier onboarding on large codebases.",
                ),
                (
                    "TypeScript vs JSDoc typing?",
                    "**Answer:** JSDoc with `// @ts-check` types JavaScript files without renaming. TypeScript `.ts` files give stronger, first-class syntax. Many teams use both during migration.",
                ),
            ]
        )
        + exercises(
            1,
            [
                (
                    "Project setup",
                    "Create `my-ts-hello`, run `npm init -y`, install TypeScript locally, run `npx tsc --init`, and add `src/index.ts` with a typed `Product` interface and a `formatPrice` function.",
                    "Set `rootDir` to `./src` and `outDir` to `./dist` in tsconfig.",
                ),
                (
                    "JS vs TS comparison",
                    "Write `add(a, b)` in a `.js` file and call `add(1, '2')`. Port to `.ts` with `number` parameters and observe the compile error.",
                    "Run `node` on JS; run `tsc` then `node dist/...` on TS.",
                ),
                (
                    "Inference experiment",
                    "Declare `const items = [1, 2, 3]` and `let label = 'active'` without annotations. Hover types in the editor. Then try `let label = 'active' as string` vs literal type.",
                    "See Chapter 2 for literal types.",
                ),
                (
                    "Reading errors",
                    "Define `interface Book { title: string; pages: number }` and pass `{ title: 'TS' }` to a function expecting `Book`. Copy the full error and fix the object.",
                    "Missing property errors list the required keys.",
                ),
                (
                    "Watch mode",
                    "Run `npx tsc --watch` in one terminal and `node dist/index.js` in another. Change a type and see recompile.",
                    "Use `--noEmit` if you only want type-checking.",
                ),
                (
                    "Strict optional",
                    "Enable `strict` and write a function with `name?: string`. Try `console.log(name.length)` and fix with optional chaining.",
                    "Preview of null safety from Chapter 2.",
                ),
            ]
        )
        + summary(
            [
                "**TypeScript** adds static types to JavaScript and compiles to JS.",
                "Types are **erased** at runtime — no TS virtual machine.",
                "Install per-project, enable **`strict`**, use **`src/` → `dist/`** layout.",
                "**Inference** reduces boilerplate; annotate when unclear or public API.",
                "**Compiler errors** are your friend — read them fully.",
                "Next: primitive types, `unknown`, unions — [Chapter 2](./ch02-types-and-primitives.md).",
            ]
        )
        + nav(None, ("ch02-types-and-primitives.md", "Types and Primitives"))
    )


BODY = r'''
## What is TypeScript?

### Definition

**TypeScript** is a programming language built by extending JavaScript with an optional **static type system**. You write `.ts` (or `.tsx` for React) files, the compiler checks types, then outputs `.js` that runs in browsers, Node.js, Deno, Bun, and anywhere JavaScript runs.

Think of it in layers:

```text
┌────────────────────────────────────────┐
│  Your code:  TypeScript (.ts / .tsx)   │
│  - types, interfaces, generics         │
├────────────────────────────────────────┤
│  Compiler:  tsc / bundler              │
│  - type-check + transpile              │
├────────────────────────────────────────┤
│  Output:     JavaScript (.js)          │
│  - runs on any JS engine               │
└────────────────────────────────────────┘
```

> **Definition:** A **static type system** checks types **before** the program runs (at compile time), catching many bugs in the editor or CI instead of in production.

### Why does TypeScript exist?

JavaScript is **dynamically typed**: a variable can hold any value, and type errors often appear only when code runs:

```javascript
function getLength(x) {
  return x.length;
}
getLength(42); // Runtime: undefined behavior — numbers have no .length
```

TypeScript lets you document and enforce expectations:

```typescript
function getLength(x: string | unknown[]) {
  return x.length;
}
getLength(42); // Compile error: number is not assignable
```

---

## A Short History

Understanding where TypeScript came from helps you understand why the ecosystem looks the way it does today.

### The timeline

```text
📅 2012
   └── Microsoft announces TypeScript at BUILD conference.
       Anders Hejlsberg (creator of C#) leads the team.
       Goal: scale JavaScript for large applications.

📅 2014
   └── TypeScript 1.0 — classes, modules, generics ship.

📅 2016
   └── DefinitelyTyped explodes — @types/* for npm packages.
       Angular 2 chooses TypeScript as default language.

📅 2018
   └── TypeScript 3.0 — project references, improved control-flow analysis.

📅 2020
   └── TypeScript 4.0 — variadic tuples, labeled tuple elements.

📅 2023+
   └── TS 5.x — faster compiler, decorators, const type parameters.
       TypeScript is one of the most loved languages on Stack Overflow surveys.
```

| Year | Event |
|------|--------|
| 2012 | Microsoft announces TypeScript; Anders Hejlsberg leads the team |
| 2014 | TypeScript 1.0 — classes, modules, generics |
| 2016 | `@types` packages on DefinitelyTyped grow rapidly |
| 2018 | TypeScript 3.0 — project references, improved inference |
| 2020 | TypeScript 4.0 — variadic tuples, labeled tuples |
| 2023+ | TS 5.x — decorators, `const` type parameters, faster compiler |

TypeScript does not replace ECMAScript — it **tracks** modern JavaScript and lets you use new syntax while targeting older runtimes via `target` in `tsconfig.json`.

### Open source and governance

TypeScript is **open source** (Apache 2.0). The compiler, language service, and documentation live on GitHub. Breaking changes go through design reviews; the team publishes a [roadmap](https://github.com/microsoft/TypeScript/wiki/Roadmap) so teams can plan upgrades.

---

## Why Use TypeScript?

### Catch bugs early

```typescript
interface User {
  id: number;
  name: string;
}

function greet(user: User) {
  return `Hello, ${user.name}`;
}

greet({ id: 1, name: "Ada", age: 30 });
// ❌ Error: 'age' does not exist in type 'User'
```

### Better editor experience

When types are known, your IDE can:

- Autocomplete property and method names
- Show documentation on hover
- Rename symbols safely across files
- Find all references accurately

### Safer refactoring

Renaming `userId` to `accountId` across 200 files is risky in plain JS. With types, the compiler lists every broken call site.

### Living documentation

Types describe contracts between modules — often clearer than comments that drift out of date.

### Gradual adoption

You can migrate one file at a time. JavaScript files can coexist via `allowJs` and `// @ts-check`.

---

## TypeScript vs JavaScript

| Aspect | JavaScript | TypeScript |
|--------|------------|------------|
| File extension | `.js`, `.mjs`, `.cjs` | `.ts`, `.tsx` |
| Type checking | Runtime only (or none) | Primarily compile time |
| Execution | Direct in browser/Node | Compile or bundle first (or `ts-node` in dev) |
| Interfaces / enums | Not built-in | First-class |
| Learning curve | Lower at start | Higher upfront, pays off in teams |

### Same language, extra safety

```typescript
// TypeScript source
const multiply = (a: number, b: number): number => a * b;

// Emitted JavaScript (types removed)
const multiply = (a, b) => a * b;
```

### When JavaScript is enough

- One-off scripts under ~100 lines
- Quick prototypes where speed beats safety
- Environments forbidding a build step

### When TypeScript shines

- Teams of 2+ on long-lived codebases
- Complex APIs (REST, GraphQL, forms)
- React/Vue/Angular applications
- Libraries needing clear public APIs

---

## How TypeScript Works (Compile Pipeline)

```text
  .ts files  ──►  Parser  ──►  AST  ──►  Type checker  ──►  Emitter  ──►  .js
                        │                    │
                        │                    └── errors stop emit (default)
                        └── also reports syntax errors
```

1. **Parse** source into an AST (Abstract Syntax Tree).
2. **Bind** symbols (variables, types, modules).
3. **Type-check** expressions against declared types.
4. **Emit** JavaScript (and `.d.ts` declaration files if configured).

---

## Type Erasure

> **Definition:** **Type erasure** means all type annotations, interfaces, and type-only imports are **removed** from the output JavaScript. They never exist at runtime.

```typescript
type UserId = string;
interface User { id: UserId; name: string; }
const u: User = { id: "1", name: "Ada" };
```

Compiles to something like:

```javascript
const u = { id: "1", name: "Ada" };
```

Implications:

- You cannot use `instanceof` on interfaces.
- Runtime validation (Zod, io-ts, manual guards) is still needed for external data.
- Generics are also erased — `Array<string>` becomes `Array` at runtime.

---

## Who Uses TypeScript?

| Organization / Project | Notes |
|------------------------|--------|
| Microsoft | Created TS; VS Code is written in TypeScript |
| Google | Angular is TypeScript-first |
| Meta | Large React codebases widely use TS |
| Netflix, Airbnb, Slack | Scale and maintainability |
| Open source | React, Vue 3, Deno, many npm packages ship `.d.ts` types |

---

## Prerequisites

Before this course, you should be comfortable with:

| Skill | Why |
|-------|-----|
| JavaScript basics | Syntax, functions, objects, arrays |
| ES6+ | Arrow functions, destructuring, modules |
| Node.js & npm | Install compiler, run scripts |
| HTML/CSS (optional) | Context for browser examples |

This course assumes you have completed or are reading the **CodeShelf JavaScript** track in parallel.

---

## Installation and Setup

### Prerequisites

- **Node.js** 18 LTS or newer (includes npm)
- **Editor** with TypeScript support (VS Code / Cursor recommended)

### Global install (optional)

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

### Minimal tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "NodeNext",
    "strict": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "esModuleInterop": true,
    "skipLibCheck": true
  },
  "include": ["src/**/*"]
}
```

Full options are covered in [Chapter 10 — Modules and Config](./ch10-modules-and-config.md).

---

## Project Structure

```text
my-ts-app/
├── package.json
├── package-lock.json
├── tsconfig.json
├── src/
│   └── index.ts
└── dist/              ← generated; add to .gitignore
    └── index.js
```

| File / folder | Purpose |
|---------------|---------|
| `src/` | Your TypeScript source |
| `dist/` | Compiler output (do not edit by hand) |
| `tsconfig.json` | Compiler options |
| `node_modules/` | Dependencies (gitignored) |

---

## Your First TypeScript Program

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

### Line-by-line breakdown

| Part | Meaning |
|------|---------|
| `interface User` | Describes required shape of a user object |
| `user: User` | Parameter must match the interface |
| `: string` after `)` | Function must return a string |
| `const currentUser: User` | Explicit type (inference would work here too) |

---

## Type Annotations and Inference

> **Definition:** A **type annotation** explicitly names a type. **Type inference** lets the compiler deduce types from values.

```typescript
// Explicit annotation
let count: number = 0;

// Inference (preferred when obvious)
let countInferred = 0; // number

// Annotation when no initializer
let score: number;

// Narrow literal union
let status: "pending" | "done" = "pending";
```

| Situation | Recommendation |
|-----------|----------------|
| Obvious literals | Let inference work |
| Function parameters | Annotate (required in `.ts` unless from context) |
| Public exports | Annotate return types for API clarity |
| `any` creeping in | Add explicit types |

---

## The TypeScript Compiler (tsc)

| Command | Effect |
|---------|--------|
| `npx tsc` | Compile once using `tsconfig.json` |
| `npx tsc --watch` | Recompile on file changes |
| `npx tsc --noEmit` | Type-check only, no output |
| `npx tsc --showConfig` | Print resolved config |

### Flags worth knowing early

| Flag | Meaning |
|------|---------|
| `--strict` | Enable all strict type-checking options |
| `--target ES2020` | JavaScript version to emit |
| `--module NodeNext` | Module system for Node ESM |
| `--skipLibCheck` | Skip checking `.d.ts` in node_modules (faster) |

---

## tsconfig.json Essentials

The `tsconfig.json` file controls how TypeScript compiles your project.

```json
{
  "compilerOptions": {
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "forceConsistentCasingInFileNames": true
  }
}
```

| Option | Why it matters |
|--------|----------------|
| `strict` | Catches the most common bugs |
| `rootDir` / `outDir` | Clean source vs output separation |
| `include` / `exclude` | Which files to compile |
| `moduleResolution` | How imports resolve |

---

## Running TypeScript in Development

### ts-node (quick experiments)

```bash
npm install --save-dev ts-node
npx ts-node src/index.ts
```

### Watch workflow

```bash
# Terminal 1
npx tsc --watch

# Terminal 2
node dist/index.js
```

### Production

Always compile to JavaScript or use a bundler (Vite, esbuild, webpack) that understands TypeScript.

---

## TypeScript in the Ecosystem

| Layer | Role of TypeScript |
|-------|-------------------|
| React | `.tsx` components, typed props — [Ch 12](./ch12-react-with-typescript.md) |
| Node.js | Typed handlers, env, database models |
| Deno / Bun | Native TS support |
| Testing | Vitest/Jest with types |
| APIs | Shared types between front-end and back-end |

---

## Gradual Adoption and Migration

Strategies for existing JavaScript projects:

1. Rename `.js` → `.ts` file by file.
2. Enable `allowJs: true` and `checkJs: true`.
3. Add `// @ts-check` at top of critical `.js` files.
4. Start with `strict: false`, then tighten flags over sprints.
5. Type boundaries first (API clients, database models).

```json
{
  "compilerOptions": {
    "allowJs": true,
    "checkJs": true
  }
}
```

---

## Reading Compiler Errors

TypeScript errors follow a pattern:

```text
src/index.ts:10:5 - error TS2345: Argument of type 'X' is not assignable to parameter of type 'Y'.
```

Tips:

1. Read from the **bottom** of a long error chain — the root cause is often last.
2. Click the error in VS Code to jump to the line.
3. Hover red squiggles for quick fixes.
4. Search `TS2345` only after reading the human message.

### Example: possibly undefined

```typescript
function printLength(s?: string) {
  console.log(s.length); // ❌ 's' is possibly 'undefined'
}

function printLengthSafe(s?: string) {
  console.log(s?.length ?? 0); // ✅
}
```

### Example: missing module types

```bash
npm install --save-dev @types/node
```

---

## What TypeScript is NOT

| Myth | Reality |
|------|---------|
| A new runtime | Compiles to JS |
| Required for React | Optional but recommended at scale |
| Slower at runtime | Types are erased |
| A replacement for JS | You must know JavaScript |

---

'''
