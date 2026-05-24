---
title: TypeScript Course Overview
description: Complete TypeScript course — from fundamentals to React, async patterns, and interview prep
order: 0
tags: [typescript, overview]
---

# The Complete TypeScript Course

From JavaScript developer to type-safe professional — every concept explained with examples.

## Course structure

### Part 1: Foundations

| Chapter | Topic |
|---------|--------|
| [Introduction](./ch01-introduction.md) | What TypeScript is, setup, first program, TypeScript vs JavaScript |
| [Types & Primitives](./ch02-types-and-primitives.md) | string, number, boolean, any, unknown, void, never |
| [Interfaces & Type Aliases](./ch03-interfaces-and-type-aliases.md) | Interfaces, type aliases, extends, intersection |

### Part 2: Functions & Generics

| Chapter | Topic |
|---------|--------|
| [Functions](./ch04-functions.md) | Function types, overloads, optional params, rest parameters |
| [Generics](./ch05-generics.md) | Generic functions, constraints, reusable patterns |
| [Utility Types](./ch06-utility-types.md) | Partial, Pick, Omit, Record, ReturnType, and more |

### Part 3: Object-Oriented & Advanced Types

| Chapter | Topic |
|---------|--------|
| [Classes & OOP](./ch07-classes-and-oop.md) | Classes, access modifiers, abstract classes, implements |
| [Type Narrowing](./ch08-type-narrowing.md) | typeof, instanceof, in, discriminated unions |
| [Enums & Literals](./ch09-enums-and-literals.md) | Enums, literal types, const assertions |

### Part 4: Tooling & Real-World Usage

| Chapter | Topic |
|---------|--------|
| [Modules & Config](./ch10-modules-and-config.md) | ES modules, tsconfig.json essentials |
| [Async TypeScript](./ch11-async-typescript.md) | Promises, async/await, error typing |
| [React with TypeScript](./ch12-react-with-typescript.md) | Component props, hooks, events |

### Part 5: Professional Skills

| Chapter | Topic |
|---------|--------|
| [Best Practices](./ch13-best-practices.md) | Strict mode, naming conventions, common mistakes |
| [Interview Preparation](./ch14-interview-prep.md) | 10+ common TypeScript interview Q&A |

## Prerequisites

Before starting this course, you should be comfortable with:

| Skill | Why it matters |
|-------|----------------|
| JavaScript basics | TypeScript is a superset of JS — syntax and runtime behavior are shared |
| ES6+ features | Arrow functions, destructuring, modules, and spread are used throughout |
| Node.js & npm | Needed for installing TypeScript and running the compiler |
| Basic React (optional) | Required only for [Chapter 12](./ch12-react-with-typescript.md) |

## How to use these notes

1. Read **Part 1** first if you are new to TypeScript or coming from plain JavaScript.
2. Work through **Part 2–3** with a small practice project (e.g., a todo app or API client).
3. Configure your editor and `tsconfig.json` using **Part 4** before building real apps.
4. Review **Part 5** before interviews or code reviews on a TypeScript codebase.

## Recommended learning path

```text
Week 1:  Ch 1–3  →  Types, interfaces, first typed project
Week 2:  Ch 4–6  →  Functions, generics, utility types
Week 3:  Ch 7–9  →  Classes, narrowing, enums
Week 4:  Ch 10–12 →  Config, async, React integration
Week 5:  Ch 13–14 →  Best practices + interview prep
```

## Tools you'll use

| Tool | Purpose |
|------|---------|
| `typescript` (npm) | Compiler (`tsc`) that checks types and emits JavaScript |
| VS Code / Cursor | IDE with built-in TypeScript language service |
| `ts-node` | Run TypeScript directly without a separate compile step (dev only) |
| `@types/*` packages | Community type definitions for JavaScript libraries |

## What you'll build (suggested exercises)

Throughout the course, apply concepts in a single growing project:

- **Ch 1–2:** Typed greeting CLI and user profile object
- **Ch 3–4:** API response types and typed fetch helpers
- **Ch 5–6:** Generic data store with Partial updates
- **Ch 7–9:** Domain models with classes and discriminated unions
- **Ch 10–11:** Modular async API client with proper error types
- **Ch 12:** React dashboard consuming your typed API

## Chapter summaries

### [Chapter 1 — Introduction](./ch01-introduction.md)

TypeScript as a typed superset of JavaScript, installation with npm, running `tsc`, and your first typed program. Compares compile-time safety with JavaScript's runtime-only checking.

### [Chapter 2 — Types & Primitives](./ch02-types-and-primitives.md)

Core primitives, arrays, tuples, unions, and the special types `any`, `unknown`, `void`, and `never`. Foundation for everything that follows.

### [Chapter 3 — Interfaces & Type Aliases](./ch03-interfaces-and-type-aliases.md)

Model object shapes, extend and intersect types, and understand structural typing (duck typing at compile time).

### [Chapter 4 — Functions](./ch04-functions.md)

Optional and default parameters, rest args, return types, overloads, and higher-order function typing.

### [Chapter 5 — Generics](./ch05-generics.md)

Write reusable functions and classes with type parameters, constraints, and default generics.

### [Chapter 6 — Utility Types](./ch06-utility-types.md)

Built-in transforms: `Partial`, `Pick`, `Omit`, `Record`, `ReturnType`, `Awaited`, and composition patterns for DTOs.

### [Chapter 7 — Classes & OOP](./ch07-classes-and-oop.md)

Classes with access modifiers, abstract classes, `implements`, static members, and when to prefer interfaces over classes.

### [Chapter 8 — Type Narrowing](./ch08-type-narrowing.md)

Refine unions with `typeof`, `instanceof`, `in`, type guards, and discriminated unions for exhaustive control flow.

### [Chapter 9 — Enums & Literals](./ch09-enums-and-literals.md)

Literal types, string/numeric enums, `as const`, and modern alternatives to runtime enums.

### [Chapter 10 — Modules & Config](./ch10-modules-and-config.md)

ES module imports/exports, path aliases, ambient declarations, and essential `tsconfig.json` options.

### [Chapter 11 — Async TypeScript](./ch11-async-typescript.md)

Typing `Promise`, `async/await`, fetch + JSON validation, error types, and `Promise.all` patterns.

### [Chapter 12 — React with TypeScript](./ch12-react-with-typescript.md)

Component props, events, `useState`, `useReducer`, context, refs, and generic list/table components.

### [Chapter 13 — Best Practices](./ch13-best-practices.md)

Strict compiler flags, naming, avoiding `any`, branded types, and code review checklist.

### [Chapter 14 — Interview Preparation](./ch14-interview-prep.md)

20 common interview questions with short and deep answers, plus whiteboard challenges.

## Related courses in CodeShelf

| Course | Connection |
|--------|------------|
| JavaScript basics | Prerequisite language knowledge |
| React fundamentals | Pairs with Chapter 12 |
| Node / backend topics | Chapters 10–11 apply to server TypeScript |

> **Tip:** Use the sidebar search (`Ctrl+K`) to jump to topics like "generics", "narrowing", or "utility types".

> **Key takeaway:** This course is designed to be read in order, but each chapter is self-contained enough to use as a reference. Bookmark [Chapter 6 — Utility Types](./ch06-utility-types.md) and [Chapter 13 — Best Practices](./ch13-best-practices.md) for day-to-day development.
