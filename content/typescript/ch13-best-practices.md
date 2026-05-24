---
title: Chapter 13 — Best Practices
description: Strict mode, naming, avoiding any, branded types, and team conventions.
order: 13
tags: [typescript, best-practices, strict, conventions]
---


# Chapter 13: Best Practices

> **Writing TypeScript is easy; writing *maintainable* TypeScript requires discipline. This chapter collects professional conventions.**
> Take your time with each section. TypeScript rewards patience — read compiler errors carefully and experiment in a small project as you go.

---


## Table of Contents

1. [Enable strict](#enable-strict)
2. [Compiler Flags Table](#compiler-flags-table)
3. [Boundary Validation](#boundary-validation)
4. [unknown over any](#unknown-over-any)
5. [interface vs type](#interface-vs-type)
6. [Discriminated Unions](#discriminated-unions)
7. [Branded Types](#branded-types)
8. [Avoid Assertion Abuse](#avoid-assertion-abuse)
9. [DTO Patterns](#dto-patterns)
10. [ESLint](#eslint)
11. [Documentation](#documentation)
12. [Code Review Checklist](#code-review-checklist)
13. [Interview Points](#interview-points)
14. [Exercises](#exercises)
15. [Chapter Summary](#chapter-summary)

---

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
<!-- codeshelf:generated-appendix -->

---

## Team conventions document

Maintain a `TYPESCRIPT.md` in the repo covering:

- Required `tsconfig` flags
- `any` policy (forbidden vs escape hatch)
- Validation library at API boundary
- Naming: `interface` vs `type`
- PR checklist for type-related changes

Onboarding improves when conventions are written, not tribal knowledge.

---

## Strict flags — one at a time

On legacy codebases, enable gradually:

1. `strictNullChecks`
2. `noImplicitAny`
3. `strictFunctionTypes`
4. `noUncheckedIndexedAccess`

Fix errors per flag in dedicated PRs so reviews stay focused.

---

## Boundary validation

```typescript
import { z } from "zod";

const UserSchema = z.object({ id: z.string(), name: z.string() });
type User = z.infer<typeof UserSchema>;

function parseUser(raw: unknown): User {
  return UserSchema.parse(raw);
}
```

Types do not validate at runtime — schemas do.

---

## Branded types


```typescript
type UserId = string & { readonly __brand: unique symbol };
type OrderId = string & { readonly __brand: unique symbol };

function userId(id: string): UserId {
  return id as UserId;
}
```


---

## Strict compiler flags explained


| Flag | Effect |
|------|--------|
| `strictNullChecks` | null/undefined not assignable unless in union |
| `noImplicitAny` | Error on implicit any |
| `strictFunctionTypes` | Safer function parameter checking |
| `noUncheckedIndexedAccess` | Indexing may return undefined |


---

## ESLint TypeScript rules


- `@typescript-eslint/no-explicit-any`
- `@typescript-eslint/consistent-type-imports`
- `@typescript-eslint/no-floating-promises`


---

## Code review checklist


1. No new `any` without comment
2. External data validated
3. Public exports typed
4. Unions exhaustive in switch
5. No `@ts-ignore` without ticket link


---

## Incremental strict flags


Enable `strictNullChecks` first, then `noImplicitAny`, then `noUncheckedIndexedAccess` in separate PRs.


---

## ESLint


Use `@typescript-eslint/no-explicit-any` and `@typescript-eslint/no-floating-promises` in CI.


---

## Runtime validation


Use Zod/Valibot at API boundaries — types alone do not validate JSON at runtime.


---

## Definition — Strict mode

> **Definition:** **Strict mode** — A bundle of `tsconfig` flags that enable the strictest practical type checking.


---

## Code review checklist


1. No new `any` without justification comment
2. External JSON validated at boundary
3. Public exports have explicit types
4. Unions exhaustive in `switch`
5. No `@ts-ignore` without ticket link
6. `import type` for type-only imports
7. Tests cover edge cases types cannot catch


---

## Branded types


```typescript
type Cents = number & { readonly __brand: unique symbol };
type Dollars = number & { readonly __brand: unique symbol };
```
Prevents accidentally adding cents to dollars without conversion.


---

## Documentation comments


```typescript
/**
 * Converts cents to a USD display string.
 * @param cents - Integer cents (non-negative)
 */
export function formatUsd(cents: number): string {
  return `$${(cents / 100).toFixed(2)}`;
}
```


---

## Avoid assertion abuse


| Instead of | Prefer |
|------------|--------|
| `x as User` | Validate + type guard |
| `!` non-null assertion | Narrow with `if` |
| `@ts-ignore` | Fix type or narrow scope |


---

## Review Q1

**Q:** First strict flag to enable on legacy code? **A:** Often `strictNullChecks` — highest bug prevention per effort.

---

## Review Q2

**Q:** When is `any` acceptable? **A:** Rarely — migration shims with a ticket and deadline to remove.

---

## Review Q3

**Q:** Types vs runtime validation? **A:** Types compile away; validate JSON at boundaries.

---

## Strict family — expanded


| Flag | What it catches |
|------|-----------------|
| `strictNullChecks` | null/undefined misuse |
| `noImplicitAny` | missing annotations |
| `strictFunctionTypes` | unsafe function assignability |
| `noUncheckedIndexedAccess` | `arr[i]` may be undefined |
| `exactOptionalPropertyTypes` | `undefined` vs missing key |

Enable one per PR on legacy repos.


---

## Scenario — PR type checklist


Before merging TypeScript PRs, verify:

1. `npm run typecheck` passes in CI
2. No new `any` without linked issue
3. External API responses validated
4. Exported public APIs documented
5. Union switches have `never` exhaustiveness
6. Tests cover runtime paths types cannot guard


---

## Scenario — shared types package


Publish `packages/types` in a monorepo so web and API share `User`, `Order`, and API DTOs — one source of truth prevents client/server drift.


---

## Review Q4 — documentation

**Q:** Should you document every type? **A:** Document exported public APIs and non-obvious business types; let obvious inference speak for itself.

---

## Best Practices

- ✅ Treat types as documentation; validate at boundaries.
- ✅ Enable extra strict flags incrementally on mature codebases.

---

## Common Mistakes

Watch for these patterns — they cost hours in real projects.

### Mistake 1: Type assertion spam

`as any` to silence errors

Fix types or use type guards.

---

### Mistake 2: Leaking any

One any poisons inference

Ban explicit any in lint rules.

---

## Interview Points

> **📌 Interview Point 1: strictNullChecks?**

null/undefined not assignable unless in union.

---

> **📌 Interview Point 2: Branded type?**

Nominal-like tag via intersection with unique symbol.

---

## Exercises

Practice with `npx tsc --noEmit` after each exercise.

### Exercise 13.1: strict tsconfig ⭐

**Task:** Enable 3 additional strict flags.

<details><summary>💡 Hint</summary>

incremental adoption.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

Enable `noUncheckedIndexedAccess`, `noImplicitOverride`, and `exactOptionalPropertyTypes` in tsconfig.

</details>

---

### Exercise 13.2: Branded UserId ⭐⭐

**Task:** Prevent mixing id types.

<details><summary>💡 Hint</summary>

branding pattern.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type UserId = string & { readonly __brand: unique symbol };
function toUserId(id: string): UserId { return id as UserId; }
```

</details>

---

### Exercise 13.3: ESLint rule ⭐⭐⭐

**Task:** Add no-explicit-any.

<details><summary>💡 Hint</summary>

tooling.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

Add to ESLint: `@typescript-eslint/no-explicit-any`: error

</details>

---

### Exercise 13.4: DTO update ⭐⭐

**Task:** Partial<Omit<User,'id'>>.

<details><summary>💡 Hint</summary>

utilities.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type UserUpdate = Partial<Omit<User, "id">>;
```

</details>

---

### Exercise 13.5: Review checklist ⭐⭐⭐

**Task:** Write 10-item PR checklist.

<details><summary>💡 Hint</summary>

team process.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

Checklist: no new `any`, validate API JSON, exhaustive switches, no `@ts-ignore` without ticket, export types on public API, etc.

</details>

---

### Exercise 13.6: JSDoc export ⭐⭐

**Task:** Document exported function.

<details><summary>💡 Hint</summary>

IDE help.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
/**
 * Formats a price in USD.
 * @param cents - Amount in cents (integer)
 */
export function formatUsd(cents: number): string {
  return `$${(cents / 100).toFixed(2)}`;
}
```

</details>

---

## Chapter Summary

You covered a lot in this chapter. Here is a concise recap:

- Strict mode + lint + reviews keep codebases healthy.
- Types complement runtime validation.

---

---

## Navigation

**⬅️ [Previous: React with TypeScript](./ch12-react-with-typescript.md)**  
**➡️ [Next: Interview Preparation](./ch14-interview-prep.md)**

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

*Last updated: 2025 | TypeScript course — CodeShelf*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
