---
title: Chapter 13 — Best Practices
description: Strict mode, naming conventions, avoiding any, type organization, and common TypeScript mistakes.
order: 13
tags: [typescript, best-practices, strict, conventions]
---

# Chapter 13: Best Practices

## 13.1 Enable strict mode

Always start with `"strict": true` in `tsconfig.json`. It enables:

| Flag | Effect |
|------|--------|
| `strictNullChecks` | null/undefined are distinct types |
| `strictFunctionTypes` | Safer function parameter checking |
| `strictBindCallApply` | Typed bind/call/apply |
| `strictPropertyInitialization` | Class fields must be initialized |
| `noImplicitAny` | Error on inferred `any` |
| `noImplicitThis` | Error on untyped `this` |
| `alwaysStrict` | Emit `"use strict"` |

Additional flags worth enabling:

```json
{
  "compilerOptions": {
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  }
}
```

> **Definition:** **Strict mode** is a family of compiler options that maximize type safety by rejecting ambiguous or unsafe patterns at compile time.

> **Key takeaway:** Strict mode catches entire categories of bugs. Turning it off to "move faster" usually moves bugs to production instead.

## 13.2 Prefer inference, annotate boundaries

| Annotate | Infer |
|----------|-------|
| Function parameters | Local variables with obvious literals |
| Public/exported function returns | Intermediate calculations |
| Module exports | Private helpers |
| React component props | useState from literal initializer |

```typescript
// Good boundary annotation
export function parseUser(raw: unknown): User {
  // ...
}

// Unnecessary noise
const count: number = 0;
```

## 13.3 Avoid any — use unknown

```typescript
// ❌
function handle(data: any) {
  return data.id;
}

// ✅
function handle(data: unknown) {
  if (isUser(data)) return data.id;
  throw new Error("Invalid");
}
```

Enable ESLint `@typescript-eslint/no-explicit-any` in team projects.

## 13.4 Prefer interfaces for object contracts

```typescript
interface User {
  id: string;
  name: string;
}

type UserId = string;
type Result = { ok: true; data: User } | { ok: false; error: string };
```

Use `type` for unions, tuples, and mapped types ([Chapter 3](./ch03-interfaces-and-type-aliases.md)).

## 13.5 Use const objects over enums (when practical)

```typescript
const Status = {
  Active: "active",
  Archived: "archived",
} as const;

type Status = (typeof Status)[keyof typeof Status];
```

See [Chapter 9](./ch09-enums-and-literals.md).

## 13.6 Organize types

```text
src/
├── types/           # Shared domain types
│   ├── user.ts
│   └── api.ts
├── services/        # Business logic
├── components/      # UI
└── utils/           # Pure helpers
```

| Rule | Reason |
|------|--------|
| Colocate small props types with components | Easier to find |
| Shared domain types in `types/` | Single source of truth |
| Avoid mega `types.ts` | Split by domain |
| Export types with `export type` | Clear value vs type boundary |

## 13.7 Naming conventions

| Item | Convention | Example |
|------|------------|---------|
| Types / interfaces | PascalCase | `UserProfile` |
| Generics | Single letter or descriptive | `T`, `TData` |
| Boolean props | `is`, `has`, `can` prefix | `isLoading` |
| Enum members | PascalCase or UPPER_SNAKE | `LogLevel.Debug` |
| Type guards | `is` / `assert` prefix | `isUser`, `assertIsString` |
| DTO suffix | Create/Update payloads | `CreateUserDto` |

## 13.8 Branded types for nominal safety

Structural typing allows accidental mixing of same-shaped primitives:

```typescript
type UserId = string & { readonly __brand: unique symbol };
type OrderId = string & { readonly __brand: unique symbol };

function userId(id: string): UserId {
  return id as UserId;
}

function getUser(id: UserId) { /* ... */ }

// getUser(orderIdString); // ❌ without cast
getUser(userId("u_123")); // ✅
```

Use for IDs, currency, units — not everywhere.

## 13.9 Discriminated unions over optional fields

```typescript
// ❌ Ambiguous — can both exist or neither
type Response = {
  data?: string;
  error?: string;
};

// ✅ Mutually exclusive
type Response =
  | { status: "success"; data: string }
  | { status: "error"; error: string };
```

## 13.10 Validate external data at the boundary

Parse once at API/database edge; use typed models internally:

```typescript
// boundary: unknown → User
// internal: User everywhere else
```

Libraries: Zod, Valibot, ArkType. Pair with `z.infer<typeof Schema>` for types.

## 13.11 Don't over-use assertions (`as`)

```typescript
// ❌ Lying to the compiler
const user = JSON.parse(raw) as User;

// ✅ Validate or narrow
const data: unknown = JSON.parse(raw);
const user = parseUser(data);
```

Non-null assertion `!` only when you have proof:

```typescript
document.getElementById("root")!; // OK if HTML guaranteed
```

## 13.12 Use utility types before duplicating

```typescript
type UpdateUser = Partial<Omit<User, "id">>;
```

See [Chapter 6](./ch06-utility-types.md).

## 13.13 Common mistakes

| Mistake | Fix |
|---------|-----|
| Type assertion to silence errors | Fix the type or validate |
| `Object`, `Function`, `{}` as types | Use specific shapes |
| Ignoring Promise rejections | Handle errors; type Result |
| Mutable shared typed state | Readonly / immutable patterns |
| Copy-paste interfaces | Share + Pick/Omit |
| `@ts-ignore` | `@ts-expect-error` with comment + ticket |
| Enabling `skipLibCheck` to hide errors | Fix root cause |
| Huge generic abstractions early | YAGNI — concrete first |

## 13.14 Code review checklist

```text
□ strict-compatible changes
□ No new any without justification
□ External data validated
□ Exported APIs have explicit types
□ Unions use discriminant
□ Tests cover edge cases (null, empty array)
□ tsconfig paths consistent with bundler
```

## 13.15 Performance and build hygiene

| Practice | Benefit |
|----------|---------|
| Project references in monorepos | Incremental builds |
| `import type` for type-only | Smaller bundles |
| Avoid barrel file cycles | Faster IDE + tsc |
| `skipLibCheck: true` | Faster CI (acceptable tradeoff) |
| Separate `typecheck` script in CI | Catch errors before merge |

## 13.16 Documentation with types

Types document intent; add JSDoc when behavior isn't obvious:

```typescript
/**
 * Returns active users only. Excludes soft-deleted records.
 * @throws {HttpError} When API returns non-2xx
 */
export async function listActiveUsers(): Promise<User[]> {
  // ...
}
```

`@param` and `@returns` enhance hover info in IDEs.

> **Key takeaway:** Strict config, unknown at boundaries, discriminated unions, utility types, and minimal assertions form the backbone of maintainable TypeScript. Let the compiler work for you — don't fight it with `any` and `@ts-ignore`.

## Practice Exercise — Chapter 13

```text
Exercise 13.1: Audit
  a) Take a small JS module; enable strict and list all new errors.
  b) Fix without any — use unknown + guards.

Exercise 13.2: Refactor union
  a) Replace optional success/error fields with discriminated union.
  b) Update switch/call sites for exhaustiveness.

Exercise 13.3: Branded ID
  a) Add UserId and ProductId brands.
  b) Show compile error when swapped in a function call.

Exercise 13.4: Team standards
  a) Draft 5 ESLint rules for a TS project (@typescript-eslint/*).
  b) Document when type assertion is allowed in your team doc.
```

Next: [Chapter 14 — Interview Preparation](./ch14-interview-prep.md).
