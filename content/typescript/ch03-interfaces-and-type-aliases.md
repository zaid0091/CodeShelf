---
title: Chapter 3 — Interfaces and Type Aliases
description: Object shapes with interfaces and type aliases, extends, intersection, and when to use each.
order: 3
tags: [typescript, interfaces, types, extends, intersection]
---


# Chapter 3: Interfaces and Type Aliases

> **Real apps model users, products, and API payloads. This chapter teaches how to describe object shapes with interfaces and type aliases, compose them, and understand structural typing.**
> Take your time with each section. TypeScript rewards patience — read compiler errors carefully and experiment in a small project as you go.

---


## Table of Contents

1. [Describing Object Shapes](#describing-object-shapes)
2. [Interfaces](#interfaces)
3. [Optional and Readonly](#optional-and-readonly)
4. [Index Signatures](#index-signatures)
5. [Type Aliases for Objects](#type-aliases-for-objects)
6. [Interface vs Type Alias](#interface-vs-type-alias)
7. [Extending Interfaces](#extending-interfaces)
8. [Intersection Types](#intersection-types)
9. [Structural Typing](#structural-typing)
10. [Excess Property Checking](#excess-property-checking)
11. [Declaration Merging](#declaration-merging)
12. [API Models](#api-models)
13. [Best Practices](#best-practices)
14. [Common Mistakes](#common-mistakes)
15. [Interview Points](#interview-points)
16. [Exercises](#exercises)
17. [Chapter Summary](#chapter-summary)

---

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
<!-- codeshelf:generated-appendix -->

---

### Callable interfaces

Interfaces can describe functions: `(x: number) => void`.

---

### Extending multiple interfaces

`interface A extends B, C` inherits all members.

---

## Modeling a blog — end-to-end

```typescript
interface Author {
  id: string;
  displayName: string;
}

interface Post {
  id: string;
  title: string;
  body: string;
  authorId: string;
  publishedAt?: string;
  tags: readonly string[];
}

interface PostWithAuthor extends Post {
  author: Author;
}
```

This pattern mirrors APIs: base entity + joined data for detail views.

---

## interface vs type — decision flowchart

```text
Need a union or tuple alias?     → type
Need mapped/conditional type?    → type
Public object API for a library? → interface (extend/merge friendly)
Combining two object shapes?     → type A & B OR interface extends
```

Both work for object shapes. Pick one style per project and stay consistent.

---

## Index signatures — dynamic keys

```typescript
interface ScoresByPlayer {
  [playerId: string]: number;
}

const board: ScoresByPlayer = {};
board["p1"] = 10;
// board["p1"] = "ten"; // Error
```

Use when keys are not known at compile time but values share one type.

---

## Declaration merging — power and caution

```typescript
interface Window {
  myAppVersion?: string;
}
```

TypeScript merges this with the global `Window` interface. Helpful for globals; confusing if overused. Prefer explicit modules over augmenting globals when possible.

---

## Real-world interface design


Design interfaces from **consumer needs** (what code reads) not database columns alone.

```typescript
interface Address {
  line1: string;
  line2?: string;
  city: string;
  postalCode: string;
  country: string;
}

interface Customer {
  id: string;
  email: string;
  displayName: string;
  shippingAddress: Address;
  billingAddress?: Address;
}
```

### Optional vs nullable

| Syntax | Meaning |
|--------|---------|
| `prop?: T` | May be missing or `undefined` |
| `prop: T \| null` | Must be present but may be `null` |
| `prop?: T \| null` | May be missing, `undefined`, or `null` |


---

## Composition patterns


```typescript
interface Timestamps {
  createdAt: Date;
  updatedAt: Date;
}

interface SoftDelete {
  deletedAt: Date | null;
}

interface Article extends Timestamps, SoftDelete {
  id: string;
  title: string;
  body: string;
}
```

Use `extends` for named hierarchies; use `&` when combining independent concerns.


---

## Excess property checking — explained


```typescript
interface Point { x: number; y: number }

const p = { x: 1, y: 2, label: "a" }; // inferred with label
function draw(pt: Point) { console.log(pt.x); }
draw(p); // OK — variable may have extras

draw({ x: 1, y: 2, label: "a" }); // Error on excess 'label'
```

**Why?** Catch typos in object literals at call sites.


---

## Mapped types preview


```typescript
type ReadonlyUser = { readonly [K in keyof User]: User[K] };
```
See [Chapter 6 — Utility Types](./ch06-utility-types.md).


---

## Definition — Duck typing

> **Definition:** **Duck typing** — If it walks like a duck and quacks like a duck, TypeScript treats it as a duck — structure matters, not the name of the type.


---

## Worked example — e-commerce


```typescript
interface Product {
  sku: string;
  title: string;
  priceCents: number;
}

interface CartLine {
  product: Product;
  quantity: number;
}

function lineTotal(line: CartLine): number {
  return line.product.priceCents * line.quantity;
}
```

Walk through: `CartLine` **contains** a `Product` — composition without inheritance.


---

## Best Practices

- ✅ Use `interface` for public object contracts; `type` for unions and utilities.
- ✅ Centralize shared models in `types/` or `models/`.
- ✅ Mark only truly optional fields with `?`.
- ✅ Prefer composition (`extends` / `&`) over copy-paste fields.

---

## Common Mistakes

Watch for these patterns — they cost hours in real projects.

### Mistake 1: Duplicating shapes

Copying the same fields in ten interfaces

Extract `BaseEntity` and extend.

---

### Mistake 2: interface for unions

`interface Status = 'a' | 'b'`

Use `type Status = 'a' | 'b'`.

---

### Mistake 3: any in index signatures

`[key: string]: any`

Use `unknown` or a specific value type.

---

### Mistake 4: Fighting excess property checks

Random extra keys on inline literals

Assign to a variable first or fix the target type.

---

## Interview Points

> **📌 Interview Point 1: interface vs type?**

Both describe shapes; `interface` can merge and extends cleanly; `type` supports unions and advanced types.

---

> **📌 Interview Point 2: What is structural typing?**

Types match by shape, not by name — duck typing at compile time.

---

> **📌 Interview Point 3: What is excess property checking?**

Inline object literals cannot have unknown properties when assigned to a type.

---

> **📌 Interview Point 4: extends vs intersection?**

Similar for objects; conflicts in `&` can become `never` on a property.

---

## Exercises

Practice with `npx tsc --noEmit` after each exercise.

### Exercise 3.1: E-commerce Product ⭐

**Task:** Define `Product` and extend to `DigitalProduct`.

<details><summary>💡 Hint</summary>

Use `extends`.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
interface Product {
  id: string;
  name: string;
  price: number;
}

interface DigitalProduct extends Product {
  downloadUrl: string;
  fileSizeMb: number;
}
```

</details>

---

### Exercise 3.2: Soft delete entity ⭐⭐

**Task:** Combine `HasTimestamps` and `HasSoftDelete` with `&`.

<details><summary>💡 Hint</summary>

Intersection types.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
interface HasTimestamps {
  createdAt: Date;
  updatedAt: Date;
}

interface HasSoftDelete {
  deletedAt: Date | null;
}

type AuditableEntity = HasTimestamps & HasSoftDelete & { id: string };
```

</details>

---

### Exercise 3.3: Structural typing ⭐⭐⭐

**Task:** Pass extra property via variable vs inline literal.

<details><summary>💡 Hint</summary>

See excess property error.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
interface Point { x: number; y: number }

const extra = { x: 1, y: 2, label: "origin" };
function draw(p: Point) { console.log(p.x, p.y); }
draw(extra); // OK via variable

// draw({ x: 1, y: 2, label: "a" }); // excess property error on literal
```

</details>

---

### Exercise 3.4: ApiResult union ⭐⭐

**Task:** Model success and failure variants.

<details><summary>💡 Hint</summary>

Preview Chapter 8.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type ApiResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };
```

</details>

---

### Exercise 3.5: Pick preview ⭐⭐⭐

**Task:** Create `ProductSummary` with Pick.

<details><summary>💡 Hint</summary>

Chapter 6 utilities.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type ProductSummary = Pick<Product, "id" | "name" | "price">;
```

</details>

---

### Exercise 3.6: Readonly API model ⭐⭐

**Task:** Make `createdAt` readonly on an interface.

<details><summary>💡 Hint</summary>

readonly modifier.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
interface ApiModel {
  readonly createdAt: string;
  name: string;
}
```

</details>

---

## Chapter Summary

You covered a lot in this chapter. Here is a concise recap:

- Interfaces and type aliases document object contracts.
- Extend or intersect to compose; structural typing matches by shape.
- Optional `?`, `readonly`, and index signatures model real APIs.

---

---

## Navigation

**⬅️ [Previous: Types and Primitives](./ch02-types-and-primitives.md)**  
**➡️ [Next: Functions](./ch04-functions.md)**

---

*Last updated: 2025 | TypeScript course — CodeShelf*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
