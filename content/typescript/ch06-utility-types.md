---
title: Chapter 6 — Utility Types
description: Partial, Required, Readonly, Pick, Omit, Record, ReturnType, Parameters, Awaited, and more.
order: 6
tags: [typescript, utility-types, Partial, Pick, Omit]
---


# Chapter 6: Utility Types

> **TypeScript ships powerful built-in type transformers. This chapter shows how to derive new types from existing ones — essential for forms, APIs, and DTOs.**
> Take your time with each section. TypeScript rewards patience — read compiler errors carefully and experiment in a small project as you go.

---


## Table of Contents

1. [What Are Utility Types](#what-are-utility-types)
2. [Partial](#partial)
3. [Required](#required)
4. [Readonly](#readonly)
5. [Pick](#pick)
6. [Omit](#omit)
7. [Record](#record)
8. [Exclude and Extract](#exclude-and-extract)
9. [NonNullable](#nonnullable)
10. [ReturnType](#returntype)
11. [Parameters](#parameters)
12. [Awaited](#awaited)
13. [Composition Patterns](#composition-patterns)
14. [Custom Utilities](#custom-utilities)
15. [Best Practices](#best-practices)
16. [Interview Points](#interview-points)
17. [Exercises](#exercises)
18. [Chapter Summary](#chapter-summary)

---

## 6.1 What are utility types?

TypeScript ships **generic type transformations** in the standard library (`lib.d.ts`). They derive new types from existing ones — essential for DTOs, form state, and API layers.

> **Definition:** A **utility type** is a built-in generic alias that transforms properties or structure of a type (make optional, pick keys, extract return types, etc.).

```typescript
interface User {
  id: string;
  name: string;
  email: string;
  password: string;
}

// Create update payload without id or password
type UserUpdate = Partial<Omit<User, "id" | "password">>;
// { name?: string; email?: string }
```

## 6.2 Partial\<T\>

Makes every property optional:

```typescript
interface Todo {
  title: string;
  completed: boolean;
  dueDate: Date;
}

type TodoPatch = Partial<Todo>;
// { title?: string; completed?: boolean; dueDate?: Date }

function updateTodo(id: string, patch: TodoPatch): void {
  // merge patch into existing todo
}
```

Use for PATCH endpoints, settings updates, and immutable reducers.

## 6.3 Required\<T\>

Opposite of `Partial` — all properties required:

```typescript
interface Config {
  host?: string;
  port?: number;
}

type ResolvedConfig = Required<Config>;
// { host: string; port: number }
```

Use after applying defaults to assert completeness.

## 6.4 Readonly\<T\>

Makes all properties readonly (shallow):

```typescript
type ReadonlyUser = Readonly<User>;

const u: ReadonlyUser = { id: "1", name: "Ada", email: "a@x.com", password: "hash" };
// u.name = "x"; // ❌
```

For deep readonly, community types or manual recursive mapped types are needed.

## 6.5 Pick\<T, Keys\>

Select a subset of properties:

```typescript
type UserPublic = Pick<User, "id" | "name">;
// { id: string; name: string }

function toPublic(user: User): UserPublic {
  return { id: user.id, name: user.name };
}
```

## 6.6 Omit\<T, Keys\>

Remove properties:

```typescript
type UserSafe = Omit<User, "password">;
// { id, name, email }

type CreateUser = Omit<User, "id">;
// for POST body before server assigns id
```

### Pick vs Omit

| Use Pick when | Use Omit when |
|---------------|---------------|
| Small public surface | Most fields kept, few excluded |
| Explicit allow-list | Excluding secrets/metadata |

## 6.7 Record\<Keys, Type\>

Build object type from key union:

```typescript
type Role = "admin" | "member" | "guest";

type RolePermissions = Record<Role, string[]>;

const permissions: RolePermissions = {
  admin: ["read", "write", "delete"],
  member: ["read", "write"],
  guest: ["read"],
};
```

Dynamic keys with consistent value type:

```typescript
type StringMap = Record<string, string>;
```

## 6.8 Exclude\<Union, Members\> and Extract\<Union, Members\>

```typescript
type Status = "pending" | "approved" | "rejected" | "draft";

type FinalStatus = Exclude<Status, "draft">;
// "pending" | "approved" | "rejected"

type PositiveStatus = "approved" | "pending";
type GoodStatus = Extract<Status, PositiveStatus>;
// "pending" | "approved"
```

## 6.9 NonNullable\<T\>

Remove `null` and `undefined`:

```typescript
type MaybeName = string | null | undefined;
type Name = NonNullable<MaybeName>; // string
```

## 6.10 ReturnType\<Fn\> and Parameters\<Fn\>

Extract function metadata:

```typescript
function createUser(name: string, age: number) {
  return { id: crypto.randomUUID(), name, age };
}

type NewUser = ReturnType<typeof createUser>;
// { id: string; name: string; age: number }

type CreateUserArgs = Parameters<typeof createUser>;
// [name: string, age: number]
```

Useful for wrapping functions, mocks, and event handlers:

```typescript
type FetchUser = typeof fetchUser;
type FetchUserResult = Awaited<ReturnType<FetchUser>>;
```

## 6.11 Awaited\<T\>

Unwrap Promise types (including nested):

```typescript
type P = Promise<{ data: string }>;
type Data = Awaited<P>; // { data: string }

type Nested = Promise<Promise<number>>;
type N = Awaited<Nested>; // number
```

## 6.12 ConstructorParameters and InstanceType

```typescript
class Database {
  constructor(public url: string, public poolSize: number) {}
  connect() {}
}

type DbArgs = ConstructorParameters<typeof Database>;
// [url: string, poolSize: number]

type DbInstance = InstanceType<typeof Database>;
// Database
```

## 6.13 ThisParameterType and OmitThisParameter

Advanced — for extracting `this` context from functions (rare in app code).

## 6.14 Combining utilities — real patterns

### Form state from model

```typescript
interface Product {
  id: string;
  name: string;
  price: number;
  description: string;
}

type ProductForm = Omit<Product, "id">;
type ProductFormErrors = Partial<Record<keyof ProductForm, string>>;
```

### API layers

```typescript
type Entity = { id: string; createdAt: Date; updatedAt: Date };

type CreateDto<T extends Entity> = Omit<T, keyof Entity>;
type UpdateDto<T extends Entity> = Partial<Omit<T, "id" | "createdAt" | "updatedAt">>;
```

### Nullable pick

```typescript
type Nullable<T> = { [K in keyof T]: T[K] | null };
type PartialNullable<T> = Partial<Nullable<T>>;
```

## 6.15 Custom utility types (mapped types preview)

You can write your own using the same syntax TypeScript uses internally:

```typescript
type Optional<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;

type UserWithOptionalEmail = Optional<User, "email">;
```

```typescript
type Mutable<T> = {
  -readonly [K in keyof T]: T[K];
};
```

## 6.16 Quick reference table

| Utility | Transforms |
|---------|------------|
| `Partial<T>` | All props optional |
| `Required<T>` | All props required |
| `Readonly<T>` | All props readonly |
| `Pick<T, K>` | Subset of keys |
| `Omit<T, K>` | Remove keys |
| `Record<K, V>` | Key union → object |
| `Exclude<U, M>` | Remove from union |
| `Extract<U, M>` | Keep in union |
| `NonNullable<T>` | Drop null/undefined |
| `ReturnType<F>` | Function return type |
| `Parameters<F>` | Function param tuple |
| `Awaited<T>` | Unwrap Promise |
| `InstanceType<C>` | Class instance type |

> **Key takeaway:** Utility types eliminate copy-paste type definitions. Learn `Partial`, `Pick`, `Omit`, and `Record` first — they cover most API and form modeling needs.
<!-- codeshelf:generated-appendix -->

---

## When to reach for each utility

| You need | Utility |
|----------|---------|
| Update form (partial fields) | `Partial<T>` |
| Config that cannot change | `Readonly<T>` |
| Public API subset | `Pick<T, keys>` |
| Hide internal fields | `Omit<T, keys>` |
| Dictionary / map | `Record<K, V>` |
| Unwrap function return | `ReturnType<F>` |
| Unwrap Promise | `Awaited<P>` |

---

## CRUD types from one source

```typescript
interface User {
  id: string;
  email: string;
  name: string;
  role: "admin" | "member";
}

type UserCreate = Omit<User, "id">;
type UserUpdate = Partial<Omit<User, "id">>;
type UserPublic = Pick<User, "id" | "name">;
```

One `User` interface drives create, update, and public DTOs — no duplicated field lists.

---

## Utility types — quick reference

| Utility | Effect |
|---------|--------|
| `Partial<T>` | all optional |
| `Required<T>` | all required |
| `Readonly<T>` | all readonly |
| `Pick<T, K>` | keep keys K |
| `Omit<T, K>` | drop keys K |
| `Record<K, V>` | object map |
| `ReturnType<F>` | function return type |
| `Awaited<P>` | unwrap Promise |

---

## DTO patterns with utilities


```typescript
interface User {
  id: string;
  name: string;
  email: string;
  role: "admin" | "member";
}

type UserCreate = Omit<User, "id">;
type UserUpdate = Partial<Omit<User, "id">>;
type UserPublic = Pick<User, "id" | "name">;
```


---

## Awaited and Promise utilities


```typescript
type P = Promise<Promise<string>>;
type Flat = Awaited<P>; // string
```


---

## Exclude, Extract, NonNullable


```typescript
type T = string | number | null | undefined;
type StringsOnly = Extract<T, string>; // string
type NoNull = Exclude<T, null | undefined>; // string | number
type Def = NonNullable<T>; // string | number
```


---

## ConstructorParameters and InstanceType


```typescript
class User { constructor(public name: string) {} }
type UserParams = ConstructorParameters<typeof User>; // [name: string]
type UserInstance = InstanceType<typeof User>; // User
```


---

## Building a form model


```typescript
interface FormState {
  email: string;
  password: string;
  remember: boolean;
}

type FormErrors = Partial<Record<keyof FormState, string>>;
type DirtyFields = Partial<Record<keyof FormState, boolean>>;
```


---

## Combining utilities


```typescript
type UserPatch = Partial<Pick<User, "name" | "email">>;
```


---

## ReturnType for wrappers


```typescript
function withTimestamp<F extends (...args: never[]) => unknown>(fn: F) {
  return (...args: Parameters<F>): ReturnType<F> => {
    console.log(Date.now());
    return fn(...args) as ReturnType<F>;
  };
}
```


---

## Record for lookup tables


```typescript
type Role = "admin" | "member";
const permissions: Record<Role, string[]> = {
  admin: ["read", "write", "delete"],
  member: ["read"],
};
```


---

## Definition — Utility type

> **Definition:** **Utility type** — A built-in generic type transformer provided by TypeScript (e.g. `Partial`, `Pick`).


---

## CRUD walkthrough


From one `User` interface, derive:

- `UserCreate` = `Omit<User, 'id'>`
- `UserUpdate` = `Partial<Omit<User, 'id'>>`
- `UserPublic` = `Pick<User, 'id' | 'name'>`

This avoids three copies of the same field list.


---

## Exclude / Extract scenarios


```typescript
type All = string | number | boolean;
type OnlyStrings = Extract<All, string>; // string
type NoStrings = Exclude<All, string>; // number | boolean
```


---

## Awaited nested promises


```typescript
type Deep = Promise<Promise<number>>;
type Flat = Awaited<Deep>; // number
```


---

## Partial for PATCH endpoints


```typescript
type UserUpdate = Partial<Omit<User, "id" | "createdAt">>;
```


---

## Parameters and ReturnType


```typescript
type FetchUser = typeof fetchUser;
type User = Awaited<ReturnType<FetchUser>>;
```


---

## Review Q1

**Q:** What is the difference between `Partial` and `?` on each field? **A:** `Partial` transforms an existing type; manual `?` duplicates structure.

---

## Review Q2

**Q:** Can you `Pick` from a union? **A:** Utilities distribute over unions in many cases — test complex types in the playground.

---

## Review Q3

**Q:** What does `Readonly` do to nested objects? **A:** Shallow only — nested objects remain mutable unless you use a deep mapped type.

---

## Scenario — API DTO layers


```typescript
interface User {
  id: string;
  email: string;
  passwordHash: string;
  role: "admin" | "member";
}

type UserCreate = Omit<User, "id" | "passwordHash"> & { password: string };
type UserPublic = Pick<User, "id" | "email">;
type UserAdminView = Omit<User, "passwordHash">;
```

Each layer exposes only what that layer needs.


---

## Scenario — form state types


```typescript
interface SignupForm {
  email: string;
  password: string;
  agree: boolean;
}

type SignupErrors = Partial<Record<keyof SignupForm, string>>;
type DirtyFields = Partial<Record<keyof SignupForm, boolean>>;

function validate(form: SignupForm): SignupErrors {
  const errors: SignupErrors = {};
  if (!form.email.includes("@")) errors.email = "Invalid email";
  if (form.password.length < 8) errors.password = "Too short";
  if (!form.agree) errors.agree = "Required";
  return errors;
}
```


---

## Best Practices

- ✅ Compose utilities: `Partial<Pick<User,'name'>>` for patch DTOs.
- ✅ Prefer utilities over manual duplicate interfaces.

---

## Common Mistakes

Watch for these patterns — they cost hours in real projects.

### Mistake 1: Over-using Pick/Omit

Pick 1 field from huge type repeatedly

Consider domain-specific DTO types.

---

### Mistake 2: Record with any values

`Record<string, any>`

Narrow value type.

---

## Interview Points

> **📌 Interview Point 1: What does Partial do?**

Makes all properties optional.

---

> **📌 Interview Point 2: ReturnType use case?**

Extract function return type for wrappers.

---

## Exercises

Practice with `npx tsc --noEmit` after each exercise.

### Exercise 6.1: Update DTO ⭐

**Task:** Build `UserUpdate` with Partial and Omit id.

<details><summary>💡 Hint</summary>

Composition.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type UserUpdate = Partial<Omit<User, "id">>;
```

</details>

---

### Exercise 6.2: Role map ⭐⭐

**Task:** Record<Role, Permission[]>.

<details><summary>💡 Hint</summary>

Record utility.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type Role = "admin" | "member" | "guest";
type Permissions = Record<Role, string[]>;
```

</details>

---

### Exercise 6.3: Unwrap promise ⭐⭐⭐

**Task:** Use Awaited on nested Promise.

<details><summary>💡 Hint</summary>

Async types.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type P = Promise<Promise<string>>;
type Flat = Awaited<P>; // string
```

</details>

---

### Exercise 6.4: Pick preview card ⭐⭐

**Task:** ProductSummary with Pick.

<details><summary>💡 Hint</summary>

3 fields only.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type ProductSummary = Pick<Product, "id" | "name" | "price">;
```

</details>

---

### Exercise 6.5: Custom Optional ⭐⭐⭐

**Task:** Map properties to optional via mapped type.

<details><summary>💡 Hint</summary>

Advanced.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type Optional<T> = { [K in keyof T]?: T[K] };
```

</details>

---

### Exercise 6.6: ReturnType wrapper ⭐⭐

**Task:** Log wrapper preserving return type.

<details><summary>💡 Hint</summary>

ReturnType<>

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function withLog<T extends (...args: never[]) => unknown>(fn: T): T {
  return ((...args: Parameters<T>) => {
    const result = fn(...args);
    console.log("called", fn.name);
    return result;
  }) as T;
}
```

</details>

---

## Chapter Summary

You covered a lot in this chapter. Here is a concise recap:

- Utility types transform existing types without duplication.
- Essential for CRUD and API layers.

---

---

## Navigation

**⬅️ [Previous: Generics](./ch05-generics.md)**  
**➡️ [Next: Classes and OOP](./ch07-classes-and-oop.md)**

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

*Last updated: 2025 | TypeScript course — CodeShelf*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
