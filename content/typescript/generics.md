---
title: Generics
description: Reusable, type-safe components in TypeScript
order: 3
tags: [generics, advanced]
---

# Generics

Generics let you write reusable code that works with multiple types while keeping full type safety.

## Basic Generic Function

```typescript
function identity<T>(value: T): T {
  return value;
}

const num = identity(42);       // T = number
const str = identity("hello");  // T = string
```

## Generic Interfaces

```typescript
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

type UserResponse = ApiResponse<User>;
type ListResponse = ApiResponse<User[]>;
```

## Constraints

Restrict what types a generic can accept:

```typescript
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = { name: "Alice", age: 30 };
getProperty(user, "name"); // OK
// getProperty(user, "email"); // Error!
```

## Common Patterns

```typescript
// Generic array utility
function first<T>(arr: T[]): T | undefined {
  return arr[0];
}

// Generic class
class Stack<T> {
  private items: T[] = [];
  push(item: T) { this.items.push(item); }
  pop(): T | undefined { return this.items.pop(); }
}
```

## Quick Tip

When a function parameter and return type share a relationship, generics are almost always the right tool.
