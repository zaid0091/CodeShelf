---
title: Types & Interfaces
description: Core TypeScript type system concepts
order: 2
tags: [types, interfaces]
---

# Types & Interfaces

TypeScript's type system is its core strength. Here are the essentials for quick revision.

## Primitive Types

```typescript
let name: string = "Alice";
let age: number = 30;
let active: boolean = true;
let nothing: null = null;
let notDefined: undefined = undefined;
```

## Arrays & Tuples

```typescript
let numbers: number[] = [1, 2, 3];
let tuple: [string, number] = ["Alice", 30];
```

## Interfaces

Define the shape of an object:

```typescript
interface User {
  id: number;
  name: string;
  email?: string; // optional
}

const user: User = { id: 1, name: "Alice" };
```

## Type Aliases

```typescript
type ID = string | number;
type Status = "pending" | "active" | "archived";

type Point = {
  x: number;
  y: number;
};
```

## Union & Intersection

```typescript
// Union — one of several types
type Result = string | number;

// Intersection — combine types
type Employee = Person & { employeeId: number };
```

## Type vs Interface

| Feature | Interface | Type Alias |
|---------|-----------|------------|
| Extends | `extends` keyword | Intersection `&` |
| Declaration merging | Yes | No |
| Unions/primitives | No | Yes |

Use **interfaces** for object shapes; use **types** for unions, primitives, and complex compositions.
