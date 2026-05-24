---
title: Chapter 14 — Interview Preparation
description: Common TypeScript interview questions, whiteboard challenges, and study strategies.
order: 14
tags: [typescript, interview, qa]
---


# Chapter 14: Interview Preparation

> **This capstone chapter consolidates interview topics across the course with sample answers and practice challenges.**
> Take your time with each section. TypeScript rewards patience — read compiler errors carefully and experiment in a small project as you go.

---


## Table of Contents

1. [How to Use This Chapter](#how-to-use-this-chapter)
2. [Core Concepts Q&A](#core-concepts-qa)
3. [Generics and Utilities Q&A](#generics-and-utilities-qa)
4. [Narrowing and Unions Q&A](#narrowing-and-unions-qa)
5. [Tooling Q&A](#tooling-qa)
6. [React TS Q&A](#react-ts-qa)
7. [Whiteboard Challenges](#whiteboard-challenges)
8. [Behavioral Tips](#behavioral-tips)
9. [Study Plan](#study-plan)
10. [Interview Points](#interview-points)
11. [Exercises](#exercises)
12. [Chapter Summary](#chapter-summary)

---

## 14.1 How to use this chapter

Each question includes a **short answer** (what you'd say in 30 seconds) and a **deep answer** (follow-up detail). Practice out loud and tie answers to projects you've built.

Related chapters are linked for review before interviews.

---

## Q1: What is TypeScript and how does it differ from JavaScript?

**Short answer:** TypeScript is a typed superset of JavaScript that compiles to JavaScript. It adds static types and tooling; runtime behavior matches JS after compilation.

**Deep answer:** Types are erased at emit time. TS provides interfaces, enums, generics, and compile-time checking. JS runs directly; TS requires a compile or transpile step (tsc, Babel, esbuild, swc). Every valid JS program is valid TS, enabling gradual migration.

**Review:** [Chapter 1](./ch01-introduction.md)

---

## Q2: What is type inference?

**Short answer:** The compiler automatically deduces types when you don't write annotations, like inferring `number` from `let x = 5`.

**Deep answer:** Inference applies to variables, function return types (in some positions), generic type parameters, and contextual typing (e.g., callback parameter types from `Array.map`). Explicit annotations are still needed for function parameters in standalone functions and when inference would be too wide (`("a" as const)` vs `string`).

**Review:** [Chapter 2](./ch02-types-and-primitives.md)

---

## Q3: What is the difference between `any` and `unknown`?

**Short answer:** Both accept any value, but `unknown` requires narrowing before use; `any` disables checking.

**Deep answer:** `any` is contagious — assigning `any` to a typed variable bypasses checks. `unknown` is the type-safe top type: you must use typeof, instanceof, type guards, or validation before operations. Prefer `unknown` for JSON.parse, user input, and third-party data.

**Review:** [Chapter 2](./ch02-types-and-primitives.md)

---

## Q4: What is the difference between `interface` and `type`?

**Short answer:** Both describe shapes; `interface` supports declaration merging and `extends`; `type` supports unions, tuples, and advanced mapped types.

**Deep answer:** For object-only shapes they're often interchangeable. Teams use `interface` for public object contracts and `type` for unions (`A | B`), utility compositions, and conditional types. Interfaces have slightly better error messages in some edge cases with extends chains.

**Review:** [Chapter 3](./ch03-interfaces-and-type-aliases.md)

---

## Q5: Explain structural typing.

**Short answer:** TypeScript matches types by shape, not by name — if it has the required properties, it's compatible.

**Deep answer:** Duck typing at compile time. `NamedPoint` with `{ x, y, name }` can be passed where `{ x, y }` is expected. Excess property checking applies to object literals directly. This differs from nominal typing (Java classes) unless you use branding patterns.

**Review:** [Chapter 3](./ch03-interfaces-and-type-aliases.md)

---

## Q6: What are generics and why use them?

**Short answer:** Generics parameterize types so functions and data structures work with many types while preserving type relationships.

**Deep answer:** Example: `function identity<T>(x: T): T`. Constraints use `extends` — `T extends HasLength`. Defaults: `T = string`. Used in arrays, Promises, React hooks, repositories. Inference usually picks `T` from arguments; explicit `<T>` when needed.

**Review:** [Chapter 5](./ch05-generics.md)

---

## Q7: What is type narrowing?

**Short answer:** Refining a union to a specific type inside a conditional branch using checks like `typeof`, `instanceof`, or discriminant properties.

**Deep answer:** Control-flow analysis tracks narrowing across if/else, switch, return, and throw. User-defined type guards: `function isFish(p: Pet): p is Fish`. Discriminated unions with `kind` or `type` field enable exhaustive switch with `never`.

**Review:** [Chapter 8](./ch08-type-narrowing.md)

---

## Q8: What is a discriminated union?

**Short answer:** A union of object types sharing a literal property (discriminant) so TypeScript can narrow in switch/if.

**Deep answer:** Example: `{ type: 'success', data: T } | { type: 'error', error: E }`. Pattern matching style without runtime library. Combine with `assertNever` in default case for compile-time exhaustiveness when new variants are added.

**Review:** [Chapter 8](./ch08-type-narrowing.md)

---

## Q9: Explain `Partial`, `Pick`, and `Omit`.

**Short answer:** Utility types that transform object types — make all optional, select keys, or remove keys.

**Deep answer:** `Partial<User>` for PATCH updates. `Pick<User, 'id' | 'name'>` for list views. `Omit<User, 'password'>` for safe public types. Implemented as mapped types internally. Chain: `Partial<Omit<T, 'id'>>`.

**Review:** [Chapter 6](./ch06-utility-types.md)

---

## Q10: What is `never` used for?

**Short answer:** Represents values that never occur — functions that always throw or infinite loops, and exhaustiveness checking.

**Deep answer:** In a switch over a union, assigning the default variable to `never` errors if a case is missing. `never` absorbs unions (`T | never` → `T`). Distinct from `void` which means "no useful return."

**Review:** [Chapter 2](./ch02-types-and-primitives.md), [Chapter 8](./ch08-type-narrowing.md)

---

## Q11: What does `strictNullChecks` do?

**Short answer:** Makes `null` and `undefined` separate types that aren't assignable to other types unless explicitly included in a union.

**Deep answer:** Prevents `user.name` when `user` might be null. Use optional chaining `?.` and nullish coalescing `??`. Optional properties `email?: string` mean `string | undefined`. Biggest upgrade from loose JS habits.

**Review:** [Chapter 2](./ch02-types-and-primitives.md), [Chapter 13](./ch13-best-practices.md)

---

## Q12: How do you type async functions?

**Short answer:** Return `Promise<T>` explicitly for exported functions; use `async/await` which wraps returns in Promise.

**Deep answer:** `async function f(): Promise<User>`. `Awaited<ReturnType<typeof f>>` extracts resolved type. Handle errors with typed custom errors or Result unions. Avoid untyped `response.json()` — validate as `unknown`.

**Review:** [Chapter 11](./ch11-async-typescript.md)

---

## Q13: What is `as const`?

**Short answer:** Assertion that narrows literals to readonly literal types instead of widening to `string` or `number`.

**Deep answer:** `const routes = { home: '/' } as const` → `{ readonly home: "/" }`. Arrays become readonly tuples. Used with `keyof typeof` and indexed access for enum-like objects without runtime enums.

**Review:** [Chapter 9](./ch09-enums-and-literals.md)

---

## Q14: Function overloads vs union parameters?

**Short answer:** Overloads give different call signatures for one implementation; unions are simpler when behavior is unified.

**Deep answer:** Overloads: multiple signature lines + one implementation body. Good when return type depends on input literally (`string` vs `number`). When logic is shared, `(x: string | number)` with narrowing is cleaner. Overloads don't create runtime dispatch — compile-time only.

**Review:** [Chapter 4](./ch04-functions.md)

---

## Q15: How do you type React component props?

**Short answer:** Define an interface or type for props; destructure in function parameters; use `React.ReactNode` for children.

**Deep answer:** Extend `React.ComponentPropsWithoutRef<'button'>` for wrappers. Events: `React.ChangeEvent<HTMLInputElement>`. Generic components: `List<T>`. Context: custom hook with undefined check. Prefer explicit props over `React.FC`.

**Review:** [Chapter 12](./ch12-react-with-typescript.md)

---

## Q16: What is declaration merging?

**Short answer:** Two declarations with the same `interface` name merge into one — not possible with `type`.

**Deep answer:** Used to augment global or module types (`interface Window { myApp: ... }`). Ambient `.d.ts` files for untyped libraries. Prefer module augmentation over patching when extending third-party types.

**Review:** [Chapter 3](./ch03-interfaces-and-type-aliases.md), [Chapter 10](./ch10-modules-and-config.md)

---

## Q17: What is `keyof` and how is it used?

**Short answer:** `keyof T` produces a union of property names of `T`.

**Deep answer:** Used in `Pick`, `Omit`, typed `getProperty(obj, key)`, and mapped types. With generics: `function pluck<T, K extends keyof T>(obj: T, key: K): T[K]`. Combined with `typeof` for const objects.

**Review:** [Chapter 5](./ch05-generics.md), [Chapter 6](./ch06-utility-types.md)

---

## Q18: Covariance and contravariance (advanced)

**Short answer:** TypeScript checks function parameters contravariantly under strictFunctionTypes — you can't assign a narrower-parameter function to a wider-parameter slot unsafely.

**Deep answer:** Return types are covariant (narrower return OK in some positions). Arrays are covariant in TS (historical) — can bite with `Dog[]` vs `Animal[]`. Understanding helps explain assignability errors in callbacks.

**Review:** [Chapter 4](./ch04-functions.md)

---

## Q19: How would you migrate a large JS codebase to TS?

**Short answer:** Enable `allowJs`, rename files incrementally, start with `strict` false then tighten, add types at boundaries first.

**Deep answer:** Order: tsconfig → leaf utilities → shared types → API layer → UI. Use `// @ts-check` in JS files. Avoid mass `any`. Track strict flags incrementally (`strictNullChecks` first). Codemods for imports. CI `tsc --noEmit` on every PR.

**Review:** [Chapter 1](./ch01-introduction.md), [Chapter 13](./ch13-best-practices.md)

---

## Q20: Design a type-safe API client (system design)

**Short answer:** Generic methods, unknown at parse boundary, validated schemas, discriminated Result type, typed errors.

**Deep answer:**

```typescript
type ApiResult<T> =
  | { ok: true; data: T }
  | { ok: false; status: number; error: string };

async function get<T>(
  path: string,
  schema: { parse: (u: unknown) => T }
): Promise<ApiResult<T>> {
  try {
    const res = await fetch(path);
    const raw: unknown = await res.json();
    if (!res.ok) return { ok: false, status: res.status, error: String(raw) };
    return { ok: true, data: schema.parse(raw) };
  } catch (e) {
    return { ok: false, status: 0, error: "Network error" };
  }
}
```

Discuss auth headers, retry, timeout, and OpenAPI/codegen as scale increases.

**Review:** [Chapter 11](./ch11-async-typescript.md)

---

## 14.2 Whiteboard challenges

```text
1. Implement deepPartial<T> (one or two levels).
2. Type-safe event emitter: on(event, handler), emit(event, payload).
3. flatten union: Flatten<{ a: 1 } | { b: 2 }> → { a: 1; b: 2 } (advanced).
4. Type-safe Object.keys wrapper.
5. Implement tuple type Append<T, U> for [...T, U].
```

## 14.3 Behavioral tips

| Tip | Detail |
|-----|--------|
| Think aloud | Explain tradeoffs (interface vs type) |
| Use examples | Draw discriminated union on whiteboard |
| Mention strict mode | Shows production awareness |
| Admit unknowns | "I'd validate against TS handbook / codebase conventions" |
| Connect to experience | "We used Zod at the API boundary on my last project" |

> **Key takeaway:** Interviewers test fundamentals — inference, unions, generics, narrowing, and practical strictness — not obscure type gymnastics. Link answers to real bugs prevented and code maintainability.

## Back to course index

Return to [Course Overview](./ch00-course-overview.md) for the full chapter list.
<!-- codeshelf:generated-appendix -->

---

## How to answer 'Why TypeScript?'

Structure your answer in three parts:

1. **Problem:** Dynamic JS allows silent bugs in large codebases.
2. **Solution:** Compile-time types + IDE tooling catch errors early.
3. **Proof:** One real bug you prevented (wrong property, null access, bad refactor).

Avoid saying only "it's industry standard" — interviewers want reasoning.

---

## Mock interview rubric

| Score | You demonstrate |
|-------|-----------------|
| 1 | Syntax only |
| 2 | Correct definitions |
| 3 | Trade-offs (any vs unknown, enum vs union) |
| 4 | Real project examples |
| 5 | System design + validation at boundaries |

---

## Core interview questions (detailed answers)

### Q1: What is TypeScript and why use it?

**Short answer:** A typed superset of JavaScript that compiles to JS for early error detection and better tooling.

**Deep answer:** TypeScript adds optional static typing, interfaces, enums, and modern ECMAScript features via compilation. Teams adopt it to reduce production bugs, improve refactor safety, and document APIs. Types erase at runtime — there is no performance penalty from annotations themselves.

```typescript
// Compile-time safety
function add(a: number, b: number): number {
  return a + b;
}
add(1, "2"); // Error before deploy
```

---

### Q2: What is the difference between `any` and `unknown`?

| | `any` | `unknown` |
|---|-------|-----------|
| Assign in | Anything | Anything |
| Assign out | No check | Must narrow first |
| Safe default | No | Yes |

```typescript
let a: any = 1;
let b: number = a; // allowed — dangerous

let u: unknown = 1;
let n: number = u; // Error — must narrow
if (typeof u === "number") n = u;
```

---

### Q3: Explain type inference.

The compiler deduces types when you omit annotations:

```typescript
const x = [1, 2, 3]; // number[]
let y = "hi"; // string
```

Inference uses:

- Initializer types
- Return flow in functions
- Contextual typing (e.g. callback parameters)

---

### Q4: What are union and intersection types?

**Union (`|`):** value is **one of** the types.

```typescript
type Id = string | number;
```

**Intersection (`&`):** value must satisfy **all** types.

```typescript
type Employee = Person & { employeeId: string };
```

---

### Q5: What is a discriminated union?

Members share a literal field (discriminant) for narrowing:

```typescript
type Result =
  | { ok: true; data: string }
  | { ok: false; error: string };

function handle(r: Result) {
  if (r.ok) console.log(r.data);
  else console.log(r.error);
}
```

---

### Q6: What is a type predicate?

A function that narrows types for the compiler:

```typescript
function isString(x: unknown): x is string {
  return typeof x === "string";
}
```

---

### Q7: What is `never` used for?

Functions that never return, and exhaustiveness checks:

```typescript
function assertNever(x: never): never {
  throw new Error(`Unexpected: ${x}`);
}
```

---

### Q8: interface vs type alias?

- **interface:** object shapes, extends, declaration merging
- **type:** unions, tuples, mapped/conditional types

---

### Q9: What is structural typing?

Types match by shape, not name:

```typescript
interface Point { x: number; y: number }
function log(p: { x: number; y: number }) {
  console.log(p.x);
}
const pt: Point = { x: 1, y: 2 };
log(pt); // OK
```

---

### Q10: What does `strict` enable?

`strict` turns on a family of checks including:

- `strictNullChecks`
- `strictFunctionTypes`
- `strictBindCallApply`
- `strictPropertyInitialization`
- `noImplicitAny`
- `noImplicitThis`
- `alwaysStrict`

---

### Q11: What is `Pick` / `Omit` / `Partial`?

Utility types that transform object types:

```typescript
type User = { id: string; name: string; email: string };
type Preview = Pick<User, "id" | "name">;
type Update = Partial<Omit<User, "id">>;
```

---

### Q12: How do generics work?

Type parameters let APIs stay reusable and typed:

```typescript
function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

Constraints limit `T`:

```typescript
function len<T extends { length: number }>(x: T): number {
  return x.length;
}
```

---

### Q13: What is `ReturnType`?

Extracts a function's return type:

```typescript
function createUser() {
  return { id: "1", name: "Ada" };
}
type User = ReturnType<typeof createUser>;
```

---

### Q14: How do you type `Promise` and `async`?

```typescript
async function fetchId(): Promise<string> {
  return "abc";
}
```

Use `Awaited` for nested promises.

---

### Q15: How do you type React props?

```typescript
interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
}

function Button({ label, onClick, disabled }: ButtonProps) {
  return (
    <button disabled={disabled} onClick={onClick}>
      {label}
    </button>
  );
}
```

---

## Whiteboard challenges

### Challenge 1: Implement `DeepPartial<T>` (recursive)

Sketch a mapped type that makes all properties optional recursively for plain objects.

### Challenge 2: Event emitter types

Design `on(event, handler)` and `emit(event, payload)` so event names map to payload types.

### Challenge 3: Tuple to union

Convert `['a', 'b', 'c']` type to `'a' | 'b' | 'c'`.

### Challenge 4: Exclude properties by type

Given `User`, create a type without function-valued properties.

### Challenge 5: Promise timeout wrapper

Type a function `withTimeout<T>(p: Promise<T>, ms: number): Promise<T>`.

---

## Behavioral interview tips

- Explain **trade-offs**, not only syntax.
- Mention **runtime validation** at system boundaries.
- Describe a bug TypeScript caught in a real project.
- Admit when you would choose JavaScript (small scripts).
- Show curiosity about compiler options and team conventions.

---

## 30-day study plan

| Week | Focus | Chapters |
|------|-------|----------|
| 1 | Foundations | 1–3 |
| 2 | Functions & generics | 4–6 |
| 3 | OOP & narrowing | 7–9 |
| 4 | Tooling & React | 10–12 |
| 5 | Practice & interviews | 13–14 |

Daily: 45 min reading, 45 min coding exercises, 15 min flashcards.

## Answer structure


Use **Problem → TypeScript tool → Outcome** when answering behavioral questions.


---

## Whiteboard tips


Start with concrete usage, then generalize to the type definition. Narrate trade-offs.


---

## STAR method for TS stories


- **Situation:** Large React codebase, frequent null errors
- **Task:** Introduce strictNullChecks
- **Action:** Enabled flag, fixed modules incrementally, added CI `tsc --noEmit`
- **Result:** Fewer production incidents, faster onboarding


---

## Review Q1

**Q:** How to answer 'Is TypeScript worth it?' **A:** Trade-off: upfront cost vs fewer bugs, better refactors, IDE support — cite team size and codebase age.

---

## Best Practices

- ✅ Explain trade-offs, not buzzwords.
- ✅ Link answers to bugs prevented in real projects.

---

## Common Mistakes

Watch for these patterns — they cost hours in real projects.

### Mistake 1: Memorizing only syntax

Cannot explain why unknown > any

Study rationale and examples.

---

### Mistake 2: Ignoring JavaScript fundamentals

Cannot explain event loop but knows Pick<Omit>

Balance TS with JS depth.

---

## Interview Points

> **📌 Interview Point 1: Most common TS question?**

Often: difference any vs unknown, or what is generics.

---

> **📌 Interview Point 2: How to answer system design with TS?**

Mention API contracts, shared types, validation at boundaries.

---

## Exercises

Practice with `npx tsc --noEmit` after each exercise.

### Exercise 14.1: Flashcards ⭐

**Task:** Write 20 flashcards from this chapter.

<details><summary>💡 Hint</summary>

spaced repetition.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

Create 20 flashcards from Q&A sections; review daily with spaced repetition.

</details>

---

### Exercise 14.2: Mock interview ⭐⭐

**Task:** Pair practice 45 minutes.

<details><summary>💡 Hint</summary>

explain aloud.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

Pair with a friend: alternate asking and answering for 45 minutes without notes.

</details>

---

### Exercise 14.3: Whiteboard deepPartial ⭐⭐⭐

**Task:** Sketch recursive Partial type.

<details><summary>💡 Hint</summary>

advanced.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type DeepPartial<T> = {
  [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K];
};
```

</details>

---

### Exercise 14.4: Implement get ⭐⭐

**Task:** Type-safe API client sketch.

<details><summary>💡 Hint</summary>

generics + unknown.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

Sketch `get<T>(path, parser)` returning `ApiResult<T>` with unknown JSON and runtime parse function.

</details>

---

### Exercise 14.5: Narrowing live ⭐⭐⭐

**Task:** Given union code, narrate narrowing steps.

<details><summary>💡 Hint</summary>

Chapter 8.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

Narrate each branch: typeof, discriminant check, default never.

</details>

---

### Exercise 14.6: strict flags ⭐⭐

**Task:** List strict family and one benefit each.

<details><summary>💡 Hint</summary>

Chapter 10/13.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

List: strictNullChecks, noImplicitAny, strictFunctionTypes, strictBindCallApply, strictPropertyInitialization, noImplicitThis, alwaysStrict.

</details>

---

## Chapter Summary

You covered a lot in this chapter. Here is a concise recap:

- Interviewers test inference, unions, generics, narrowing, and pragmatic strictness.
- Practice explaining out loud.

---

---

## Navigation

**⬅️ [Previous: Best Practices](./ch13-best-practices.md)**  

---
## Quick glossary (review)

- **TypeScript** — Typed superset of JavaScript that compiles to JS.
- **Inference** — Compiler deduces types without explicit annotations.
- **Union** — Value may be one of several types: `A | B`.
- **Narrowing** — Refining a union to a specific type in a branch.
- **Generic** — Type parameter for reusable APIs.
- **Interface** — Named object shape contract.

*Last updated: 2025 | TypeScript course — CodeShelf*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
