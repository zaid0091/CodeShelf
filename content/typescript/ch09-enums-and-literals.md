---
title: Chapter 9 — Enums and Literal Types
description: Numeric/string/const enums, literal types, as const, and modern alternatives.
order: 9
tags: [typescript, enums, literals, as-const]
---


# Chapter 9: Enums and Literal Types

> **Literal types and const assertions are often preferable to enums. This chapter compares all approaches.**
> Take your time with each section. TypeScript rewards patience — read compiler errors carefully and experiment in a small project as you go.

---


## Table of Contents

1. [Literal Types](#literal-types)
2. [Union of Literals](#union-of-literals)
3. [Numeric Enums](#numeric-enums)
4. [String Enums](#string-enums)
5. [const enum](#const-enum)
6. [as const](#as-const)
7. [const Object Pattern](#const-object-pattern)
8. [satisfies](#satisfies)
9. [Template Literal Types](#template-literal-types)
10. [Best Practices](#best-practices)
11. [Interview Points](#interview-points)
12. [Exercises](#exercises)
13. [Chapter Summary](#chapter-summary)

---

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
<!-- codeshelf:generated-appendix -->

---

## Choosing enum vs union — decision table

| Need | Prefer |
|------|--------|
| Zero runtime cost | String literal union |
| Iterate all values at runtime | `as const` object or string enum |
| Reverse mapping (name from value) | Numeric enum (rare) |
| API from Java/C# background | String enum for familiarity |

Most new TypeScript codebases default to **union literals** or **`as const` objects**.

---

## Modern alternative to numeric enums

```typescript
const Direction = {
  Up: "UP",
  Down: "DOWN",
} as const;

type Direction = (typeof Direction)[keyof typeof Direction];
```

You get a runtime object **and** a string union type without numeric enum surprises.

---

## satisfies — validate without widening

```typescript
const config = {
  apiUrl: "https://api.example.com",
  retries: 3,
} satisfies { apiUrl: string; retries: number };

// config.apiUrl stays literal type for autocomplete
```

---

## const object vs enum


```typescript
const Status = {
  Pending: "pending",
  Done: "done",
} as const;

type Status = (typeof Status)[keyof typeof Status];
// "pending" | "done"
```

No runtime enum object unless you need reverse mapping.


---

## Numeric vs string enums


```typescript
enum Num { A, B, C } // A=0, B=1 — surprises beginners
enum Str { On = "ON", Off = "OFF" } // clearer at runtime
```


---

## satisfies operator


```typescript
const routes = {
  home: "/",
  about: "/about",
} as const satisfies Record<string, string>;
```


---

## Template literal types


```typescript
type CSSProperty = "margin" | "padding";
type CSSPropertySide = "top" | "left";
type Name = `${CSSProperty}-${CSSPropertySide}`;
// "margin-top" | "margin-left" | ...
```


---

## const object pattern


```typescript
const Status = { Pending: "PENDING", Done: "DONE" } as const;
type Status = (typeof Status)[keyof typeof Status];
```


---

## Template literal types


```typescript
type Event = "click" | "focus";
type Handler = `on${Capitalize<Event>}`;
```


---

## satisfies recap


Use `satisfies` to check a value against a type without widening literals.


---

## Definition — Literal type

> **Definition:** **Literal type** — A type that allows only specific constant values, e.g. `"success" | "error"`.


---

## Numeric enum pitfalls


```typescript
enum Num { A, B } // A=0, B=1 — implicit numbers surprise readers
```

Prefer string unions or `as const` objects for clarity.


---

## as const walkthrough


```typescript
const routes = {
  home: "/",
  profile: "/me",
} as const;

type Route = (typeof routes)[keyof typeof routes]; // "/" | "/me"
```


---

## satisfies example


```typescript
const config = {
  apiUrl: "https://api.example.com",
  retries: 3,
} satisfies { apiUrl: string; retries: number };
```


---

## HTTP status literals


```typescript
type HttpOk = 200 | 201;
type HttpErr = 404 | 500;
type HttpStatus = HttpOk | HttpErr;
```


---

## Migrating from enum


1. List all enum members used in codebase.
2. Create `as const` object + union type.
3. Replace `Enum.Member` with `Object.Member`.
4. Remove enum and delete emitted JS object.


---

## Review Q1

**Q:** Why avoid numeric enums in libraries? **A:** They emit JS objects and can break tree-shaking; unions have zero cost.

---

## Review Q2

**Q:** What does `as const` on an array do? **A:** Makes it `readonly` tuple of literal types.

---

## Review Q3

**Q:** `satisfies` vs type annotation? **A:** `satisfies` checks shape without widening literals.

---

## Review Q4

**Q:** Template literal types use case? **A:** CSS keys, event names, route builders.

---

## Scenario — theme system


```typescript
const Theme = {
  Light: "light",
  Dark: "dark",
  System: "system",
} as const;

type Theme = (typeof Theme)[keyof typeof Theme];

function applyTheme(theme: Theme) {
  document.documentElement.dataset.theme = theme;
}

function cycleTheme(current: Theme): Theme {
  const all: Theme[] = [Theme.Light, Theme.Dark, Theme.System];
  const i = all.indexOf(current);
  return all[(i + 1) % all.length];
}
```

No enum object required — string literals are checked at compile time.


---

## Scenario — route builder types


```typescript
type Locale = "en" | "fr";
type Page = "home" | "about" | "contact";
type LocalizedPath = `/${Locale}/${Page}`;

const paths = {
  enHome: "/en/home",
  frAbout: "/fr/about",
} as const satisfies Record<string, LocalizedPath>;
```


---

## Scenario — discriminant with switch


```typescript
type LoadState =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "done"; data: string[] };

function ui(state: LoadState) {
  switch (state.status) {
    case "idle": return "Click load";
    case "loading": return "Spinner…";
    case "done": return `Items: ${state.data.length}`;
  }
}
```


---

## Best Practices

- ✅ Prefer `as const` objects or union literals over numeric enums.
- ✅ Use string enums when you need runtime object iteration.

---

## Common Mistakes

Watch for these patterns — they cost hours in real projects.

### Mistake 1: Numeric enum surprises

Reverse mapping and unexpected numbers

Prefer string unions.

---

### Mistake 2: const enum pitfalls

Inlining issues across projects

Often use plain union instead.

---

## Interview Points

> **📌 Interview Point 1: enum vs union?**

Unions have no runtime cost; enums emit JS object.

---

> **📌 Interview Point 2: What does as const do?**

Makes values deeply readonly literals.

---

## Exercises

Practice with `npx tsc --noEmit` after each exercise.

### Exercise 9.1: Theme union ⭐

**Task:** Type Theme and switch.

<details><summary>💡 Hint</summary>

Literal union.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type Theme = "light" | "dark";
function themeIcon(t: Theme) {
  switch (t) {
    case "light": return "☀️";
    case "dark": return "🌙";
  }
}
```

</details>

---

### Exercise 9.2: Routes as const ⭐⭐

**Task:** Route map with satisfies.

<details><summary>💡 Hint</summary>

satisfies operator.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
const routes = {
  home: "/",
  about: "/about",
} as const satisfies Record<string, string>;
```

</details>

---

### Exercise 9.3: String enum ⭐⭐⭐

**Task:** OrderStatus string enum.

<details><summary>💡 Hint</summary>

Compare to union.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
enum OrderStatus { Pending = "PENDING", Shipped = "SHIPPED" }
```

</details>

---

### Exercise 9.4: HttpStatus ⭐⭐

**Task:** Union of status codes.

<details><summary>💡 Hint</summary>

Literal numbers.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type HttpStatus = 200 | 404 | 500;
```

</details>

---

### Exercise 9.5: Template literal ⭐⭐⭐

**Task:** Event handler name type.

<details><summary>💡 Hint</summary>

Template literal types.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type EventName = "click" | "focus";
type Handler = `on${Capitalize<EventName>}`;
```

</details>

---

### Exercise 9.6: Migrate enum ⭐⭐

**Task:** Replace numeric enum with const object.

<details><summary>💡 Hint</summary>

Modern pattern.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
const Status = { Idle: 0, Running: 1 } as const;
type Status = (typeof Status)[keyof typeof Status];
```

</details>

---

## Chapter Summary

You covered a lot in this chapter. Here is a concise recap:

- Literal unions are lightweight; enums have runtime representation.
- as const + satisfies are modern defaults.

---

---

## Navigation

**⬅️ [Previous: Type Narrowing](./ch08-type-narrowing.md)**  
**➡️ [Next: Modules and Config](./ch10-modules-and-config.md)**

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
- **Inference** — Compiler deduces types without explicit annotations.
- **Union** — Value may be one of several types: `A | B`.
- **Narrowing** — Refining a union to a specific type in a branch.
- **Generic** — Type parameter for reusable APIs.

*Last updated: 2025 | TypeScript course — CodeShelf*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
