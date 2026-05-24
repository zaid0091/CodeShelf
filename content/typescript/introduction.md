---
title: Introduction to TypeScript
description: What TypeScript is and why you'd use it
order: 1
tags: [basics, types]
---

# Introduction to TypeScript

TypeScript is a **typed superset of JavaScript** that compiles to plain JavaScript. It adds optional static typing, classes, and interfaces — helping you catch errors early and write more maintainable code.

## Why TypeScript?

| Benefit | Description |
|---------|-------------|
| Type safety | Catch bugs at compile time, not runtime |
| Better IDE support | Autocomplete, refactoring, inline docs |
| Gradual adoption | Add types incrementally to existing JS projects |
| Modern JS features | Use latest ECMAScript features with downlevel compilation |

## Basic Example

```typescript
function greet(name: string): string {
  return `Hello, ${name}!`;
}

const message = greet("World");
console.log(message);
```

## Key Concepts

- **Static typing** — declare types for variables, parameters, and return values
- **Type inference** — TypeScript infers types when you don't specify them
- **Structural typing** — compatibility is based on shape, not explicit declarations

## Next Steps

Move on to [Types & Interfaces](./types.md) to learn about TypeScript's type system.
