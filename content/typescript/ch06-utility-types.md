---
title: Chapter 6 — Utility Types
description: Built-in utility types — Partial, Required, Readonly, Pick, Omit, Record, ReturnType, Parameters, and more.
order: 6
tags: [typescript, utility-types, Partial, Pick, Omit, Record]
---

# Chapter 6: Utility Types

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

## Practice Exercise — Chapter 6

```text
Exercise 6.1: Blog API
  a) Define Post with id, title, body, authorId, publishedAt.
  b) CreatePostDto, UpdatePostDto, PostListItem (title + id only).

Exercise 6.2: ReturnType chain
  a) async function loadSettings() { return { theme: "dark", lang: "en" }; }
  b) type Settings = Awaited<ReturnType<typeof loadSettings>>.
  c) Write applySettings(s: Settings): void.

Exercise 6.3: Record
  a) type HttpMethod = "GET" | "POST" | "PUT" | "DELETE".
  b) type RouteHandlers = Record<HttpMethod, (req: Request) => Response>.
  c) Stub one handler object.

Exercise 6.4: Custom utility
  a) Write type DeepPartial<T> (one level is enough for exercise).
  b) Apply to nested interface Settings { ui: { fontSize: number } }.
```

Next: [Chapter 7 — Classes & OOP](./ch07-classes-and-oop.md).
