---
title: Chapter 3 — Interfaces and Type Aliases
description: Object shapes with interfaces and type aliases, extends, intersection, and when to use each.
order: 3
tags: [typescript, interfaces, types, extends, intersection]
---

# Chapter 3: Interfaces and Type Aliases

## 3.1 Describing object shapes

Real applications model entities — users, products, API payloads. TypeScript describes **structure**, not class names (structural typing).

```typescript
const user = {
  id: 1,
  name: "Lin",
  email: "lin@example.com",
};

// Inline type (fine for one-off)
function greet(u: { name: string; email: string }) {
  return `Hi ${u.name}`;
}
```

For reuse, use **interfaces** or **type aliases**.

> **Definition:** An **interface** declares a contract for object shapes — property names, types, and optional/required members. Interfaces can be extended and merged.

> **Definition:** A **type alias** assigns a name to any type — objects, unions, tuples, primitives, or intersections.

## 3.2 Interfaces

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  role?: "admin" | "member"; // optional
  readonly createdAt: Date;   // cannot reassign after init
}

const admin: User = {
  id: 1,
  name: "Ada",
  email: "ada@example.com",
  createdAt: new Date(),
};

// admin.createdAt = new Date(); // ❌ readonly
```

### Optional and readonly modifiers

| Modifier | Syntax | Effect |
|----------|--------|--------|
| Optional | `prop?: T` | Property may be absent or `undefined` |
| Readonly | `readonly prop: T` | Cannot assign after object creation |
| Required (utility) | `Required<T>` | Makes all props required — [Ch 6](./ch06-utility-types.md) |

### Index signatures

When keys are dynamic but values share a type:

```typescript
interface StringDictionary {
  [key: string]: string;
}

const locales: StringDictionary = {
  en: "Hello",
  fr: "Bonjour",
};
```

### Call and construct signatures

Interfaces can describe functions and classes:

```typescript
interface Logger {
  (message: string): void;           // callable
  level: "info" | "error";
}

interface Timestamped {
  createdAt: Date;
}

interface UserConstructor {
  new (name: string): User;
}
```

## 3.3 Type aliases for objects

```typescript
type User = {
  id: number;
  name: string;
  email: string;
};

type Point = {
  x: number;
  y: number;
};
```

For pure object shapes, `interface` and `type` are often interchangeable. Differences matter for unions and advanced composition (below).

## 3.4 Interface vs type alias — when to use which

| Feature | Interface | Type alias |
|---------|-----------|------------|
| Object shapes | ✅ | ✅ |
| Union types | ❌ | ✅ `type A = B \| C` |
| Tuple types | ❌ | ✅ |
| Mapped / conditional types | ❌ | ✅ |
| Declaration merging | ✅ | ❌ |
| extends (inheritance) | ✅ `extends` | ✅ `&` intersection |
| Performance (large libs) | Slightly better for checks | Fine for most apps |

**Team conventions:**

- Use **interface** for public object contracts (API models, React props) — extensible via merging.
- Use **type** for unions, tuples, and utility compositions.

> **Key takeaway:** Prefer `interface` for object-only shapes unless you need unions or advanced type logic — then use `type`.

## 3.5 Extending interfaces

```typescript
interface Person {
  name: string;
  age: number;
}

interface Employee extends Person {
  employeeId: string;
  department: string;
}

const dev: Employee = {
  name: "Sam",
  age: 28,
  employeeId: "E-100",
  department: "Engineering",
};
```

Multiple inheritance:

```typescript
interface Timestamped {
  createdAt: Date;
  updatedAt: Date;
}

interface Auditable extends Person, Timestamped {
  createdBy: string;
}
```

## 3.6 Intersection types (`&`)

> **Definition:** An **intersection** combines multiple types — a value must satisfy **all** of them.

```typescript
type Person = {
  name: string;
  age: number;
};

type Employed = {
  company: string;
  title: string;
};

type Employee = Person & Employed;

const worker: Employee = {
  name: "Jordan",
  age: 32,
  company: "Acme",
  title: "Designer",
};
```

### Interface extend vs intersection

```typescript
// These are equivalent for object shapes:
interface A extends B, C {}
type A = B & C;
```

### Conflicting properties

If two intersected types declare the same property with incompatible types, you get `never` on that property:

```typescript
type A = { id: string };
type B = { id: number };
type Bad = A & B;
// Bad['id'] is never
```

## 3.7 Structural typing (duck typing)

TypeScript matches types by **shape**, not declaration name:

```typescript
interface Point2D {
  x: number;
  y: number;
}

interface NamedPoint {
  x: number;
  y: number;
  name: string;
}

function distance(p: Point2D) {
  return Math.hypot(p.x, p.y);
}

const labeled: NamedPoint = { x: 3, y: 4, name: "origin" };
distance(labeled); // ✅ extra properties OK when passing in
```

### Excess property checking

Direct object literals get stricter checks:

```typescript
distance({ x: 1, y: 2, name: "p" }); // ❌ 'name' does not exist on Point2D
```

Workaround: assign to a variable first, or use spread from a typed source.

## 3.8 Extending with generics (preview)

```typescript
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

interface PaginatedResponse<T> extends ApiResponse<T[]> {
  page: number;
  totalPages: number;
}

type UserList = PaginatedResponse<User>;
```

Full generic patterns in [Chapter 5](./ch05-generics.md).

## 3.9 Declaration merging (interfaces only)

```typescript
interface Window {
  customApp?: { version: string };
}

// Later in another file (or ambient .d.ts):
interface Window {
  theme: "light" | "dark";
}

// Window now has both customApp and theme
```

Use sparingly — mainly for augmenting third-party types.

## 3.10 Utility patterns with object types

### Pick specific keys manually

```typescript
type UserPreview = Pick<User, "id" | "name">;
```

See [Chapter 6](./ch06-utility-types.md) for `Pick`, `Omit`, `Partial`, etc.

### Making all properties optional for updates

```typescript
type UserUpdate = Partial<User>;
```

### Readonly views

```typescript
type ReadonlyUser = Readonly<User>;
```

## 3.11 Real-world example — API models

```typescript
interface BaseEntity {
  id: string;
  createdAt: string;
  updatedAt: string;
}

interface Author extends BaseEntity {
  name: string;
  bio?: string;
}

interface Post extends BaseEntity {
  title: string;
  body: string;
  authorId: string;
  published: boolean;
}

interface PostWithAuthor extends Post {
  author: Author;
}

async function fetchPost(id: string): Promise<PostWithAuthor> {
  const res = await fetch(`/api/posts/${id}`);
  return res.json() as PostWithAuthor;
}
```

## 3.12 Common mistakes

| Mistake | Fix |
|---------|-----|
| Duplicating shapes in every file | Shared `types/` or `models/` module |
| Using `interface` for union of literals | Use `type Status = "a" \| "b"` |
| Optional everything | Only mark truly optional fields |
| `{ [key: string]: any }` | Narrow value type or use `unknown` |
| Conflicting intersections | Resolve property types explicitly |

> **Key takeaway:** Interfaces and type aliases document object contracts. Extend or intersect to compose models. Rely on structural typing — if it has the right shape, it fits.

## Practice Exercise — Chapter 3

```text
Exercise 3.1: E-commerce models
  a) Define interface Product with id, name, price, tags?: string[].
  b) Extend to DigitalProduct with downloadUrl.
  c) Create type ProductSummary = Pick<Product, "id" | "name" | "price">.

Exercise 3.2: Intersection
  a) Define types HasTimestamps and HasSoftDelete.
  b) Combine into SoftDeletableEntity with intersection.
  c) Instantiate one object satisfying all fields.

Exercise 3.3: Structural typing
  a) Write function printCoords({ x, y }: { x: number; y: number }).
  b) Pass an object with extra property via a variable — confirm it works.
  c) Pass inline literal with extra property — observe excess property error.

Exercise 3.4: API layer
  a) Model ApiError { code: string; message: string }.
  b) Model ApiSuccess<T> { ok: true; data: T } and ApiFailure { ok: false; error: ApiError }.
  c) Union into ApiResult<T> for typed fetch wrapper (preview of narrowing in Ch 8).
```

Next: [Chapter 4 — Functions](./ch04-functions.md).
