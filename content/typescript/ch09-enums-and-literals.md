---
title: Chapter 9 — Enums and Literal Types
description: Numeric and string enums, const enums, literal types, union of literals, and as const assertions.
order: 9
tags: [typescript, enums, literals, as-const]
---

# Chapter 9: Enums and Literal Types

## 9.1 Literal types

A literal type is an exact value used as a type:

```typescript
type One = 1;
type Greeting = "hello";
type Yes = true;

let direction: "north" | "east" | "south" | "west" = "north";
// direction = "up"; // ❌
```

Union of literals models fixed sets without runtime objects:

```typescript
type Theme = "light" | "dark" | "system";
type HttpStatus = 200 | 201 | 400 | 404 | 500;
```

> **Definition:** A **literal type** restricts a value to a single string, number, boolean, or bigint literal (or a union of such literals).

## 9.2 When to use literal unions vs enums

| Approach | Runtime cost | Best for |
|----------|--------------|----------|
| Literal union | None | API contracts, props, config keys |
| String enum | Small object | Named constants with reverse lookup needs |
| const object + as const | Object only | JS-friendly constant maps |
| Numeric enum | Object + reverse map | Legacy interop (often avoided) |

Modern TypeScript style often prefers **literal unions** or **`as const` objects** over enums ([Chapter 13](./ch13-best-practices.md)).

## 9.3 Numeric enums

```typescript
enum Direction {
  Up,    // 0
  Down,  // 1
  Left,  // 2
  Right, // 3
}

function move(d: Direction) {
  console.log(d);
}

move(Direction.Up);
```

Explicit values:

```typescript
enum StatusCode {
  OK = 200,
  Created = 201,
  BadRequest = 400,
  NotFound = 404,
}
```

### Reverse mapping (numeric only)

```typescript
enum Color {
  Red,
  Green,
  Blue,
}

Color[0]; // "Red" — numeric enums get reverse mapping
```

String enums do not get reverse mapping.

## 9.4 String enums

```typescript
enum LogLevel {
  Debug = "DEBUG",
  Info = "INFO",
  Warn = "WARN",
  Error = "ERROR",
}
```

Preferred over numeric when serializing to JSON/APIs — values are human-readable.

## 9.5 const enums

Inlined at compile time — no runtime object:

```typescript
const enum Axis {
  X = "X",
  Y = "Y",
}

const a = Axis.X; // emits "X" directly
```

Requires `preserveConstEnums` or inlining depending on build setup. Some bundlers avoid const enums — check your toolchain.

## 9.6 Enum member types

Each member is a subtype of the enum:

```typescript
enum EventType {
  Click = "CLICK",
  Submit = "SUBMIT",
}

function handle(event: EventType) {
  if (event === EventType.Click) {
    // narrowed
  }
}
```

## 9.7 const assertions (`as const`)

Freeze literals to narrow types:

```typescript
const routes = {
  home: "/",
  about: "/about",
  profile: "/profile/:id",
} as const;

type RouteKey = keyof typeof routes;       // "home" | "about" | "profile"
type RoutePath = (typeof routes)[RouteKey]; // "/" | "/about" | "/profile/:id"

const ROUTES = ["/", "/login", "/dashboard"] as const;
type AppRoute = (typeof ROUTES)[number];
```

> **Definition:** **`as const`** is a const assertion that makes properties readonly and infers the narrowest literal types possible.

### Without vs with as const

```typescript
const config1 = { mode: "strict" };
// type: { mode: string }

const config2 = { mode: "strict" } as const;
// type: { readonly mode: "strict" }
```

## 9.8 const object pattern (enum alternative)

```typescript
const UserRole = {
  Admin: "admin",
  Member: "member",
  Guest: "guest",
} as const;

type UserRole = (typeof UserRole)[keyof typeof UserRole];
// "admin" | "member" | "guest"

function authorize(role: UserRole) {
  switch (role) {
    case UserRole.Admin:
      return "full access";
    case UserRole.Member:
      return "limited";
    case UserRole.Guest:
      return "read only";
  }
}
```

Benefits: no enum runtime quirks, tree-shake friendly, works well with `Object.values` when typed carefully.

## 9.9 satisfies operator (TS 4.9+)

Validate shape without widening:

```typescript
type RouteMap = Record<string, `/${string}`>;

const routes = {
  home: "/",
  api: "/api/v1",
} satisfies RouteMap;

// routes.home is "/" not string
// typo keys fail type check
```

## 9.10 Template literal types (preview)

Combine string literals:

```typescript
type EventName = "click" | "focus";
type HandlerName = `on${Capitalize<EventName>}`;
// "onClick" | "onFocus"
```

Powerful for typed event systems and CSS-in-JS.

## 9.11 Enums in discriminated unions

```typescript
const enum OrderStatus {
  Pending = "PENDING",
  Shipped = "SHIPPED",
  Delivered = "DELIVERED",
}

type Order =
  | { status: OrderStatus.Pending; createdAt: Date }
  | { status: OrderStatus.Shipped; trackingId: string }
  | { status: OrderStatus.Delivered; deliveredAt: Date };
```

Often replaced with string literal discriminant for zero enum import.

## 9.12 Declaration merging and ambient enums

Libraries may ship `declare enum` for types only. Rare in application code.

## 9.13 Pitfalls

| Pitfall | Better approach |
|---------|-----------------|
| Numeric enum without values | Use string enum or literals |
| Importing enum type only | `import type { X }` or use literals |
| Heterogeneous enum | Avoid mixing string/number members |
| Large enum objects in bundle | Literal unions or const maps |
| `Object.keys` on enum | Surprising numeric enum behavior |

> **Key takeaway:** Literal unions and `as const` objects cover most "enum" use cases with less runtime baggage. Reach for string enums when you want a named namespace of constants shared across files.

## Practice Exercise — Chapter 9

```text
Exercise 9.1: Theme system
  a) Define type Theme = "light" | "dark" | "system" with as const config object.
  b) Function getResolvedTheme(theme: Theme, systemPref: "light" | "dark"): "light" | "dark".

Exercise 9.2: Enum migration
  a) Start with numeric enum Priority { Low, Medium, High }.
  b) Refactor to string union and const object; compare emitted JS.

Exercise 9.3: satisfies
  a) Type-safe icon map: Record<string, { label: string; path: string }>.
  b) Use satisfies so each entry keeps literal path type.

Exercise 9.4: Discriminant
  a) Notification union: info | warning | error with kind field.
  b) Switch renderNotification without default fall-through bugs.
```

Next: [Chapter 10 — Modules & Config](./ch10-modules-and-config.md).
