"""Additional reference sections for chapters that need more depth."""

from gen_ts_supplements_all import _sec


def _block(sections: list[tuple[str, str]]) -> str:
    return "".join(_sec(t, b) for t, b in sections)


MORE_BY_FILE: dict[str, str] = {
    "ch02-types-and-primitives.md": _block([
        ("Coercion vs types", r"""
TypeScript types do **not** change JavaScript coercion. Validate external strings before treating them as numbers.

```typescript
const n: number = Number("42"); // OK
const parsed = parseInt("42px", 10); // 42 — still validate input shape first
```
"""),
    ]),
    "ch03-interfaces-and-type-aliases.md": _block([
        ("Mapped types preview", r"""
```typescript
type ReadonlyUser = { readonly [K in keyof User]: User[K] };
```
See [Chapter 6 — Utility Types](./ch06-utility-types.md).
"""),
    ]),
    "ch04-functions.md": _block([
        ("Optional chaining with callbacks", r"""
```typescript
function onReady(cb?: () => void) {
  cb?.();
}
```
"""),
        ("Rest parameters with tuples", r"""
```typescript
function logAll(level: "info" | "error", ...messages: string[]) {
  messages.forEach((m) => console[level](m));
}
```
"""),
        ("Function overload pitfalls", r"""
Keep overloads **simple**. If you need many shapes, consider a single options object:

```typescript
interface FormatOptions {
  value: string | number | boolean;
  locale?: string;
}
function format(opts: FormatOptions): string { /* ... */ }
```
"""),
    ]),
    "ch05-generics.md": _block([
        ("Generic constraints in APIs", r"""
```typescript
interface Identifiable { id: string }
function indexById<T extends Identifiable>(items: T[]): Record<string, T> {
  return Object.fromEntries(items.map((i) => [i.id, i]));
}
```
"""),
        ("Multiple type parameters", r"""
```typescript
function pair<T, U>(first: T, second: U): [T, U] {
  return [first, second];
}
```
"""),
        ("Generic type aliases", r"""
```typescript
type Nullable<T> = T | null;
type ApiResult<T> = { ok: true; data: T } | { ok: false; error: string };
```
"""),
    ]),
    "ch06-utility-types.md": _block([
        ("Combining utilities", r"""
```typescript
type UserPatch = Partial<Pick<User, "name" | "email">>;
```
"""),
        ("ReturnType for wrappers", r"""
```typescript
function withTimestamp<F extends (...args: never[]) => unknown>(fn: F) {
  return (...args: Parameters<F>): ReturnType<F> => {
    console.log(Date.now());
    return fn(...args) as ReturnType<F>;
  };
}
```
"""),
        ("Record for lookup tables", r"""
```typescript
type Role = "admin" | "member";
const permissions: Record<Role, string[]> = {
  admin: ["read", "write", "delete"],
  member: ["read"],
};
```
"""),
    ]),
    "ch07-classes-and-oop.md": _block([
        ("Static factory methods", r"""
```typescript
class User {
  private constructor(public id: string, public name: string) {}
  static create(name: string): User {
    return new User(crypto.randomUUID(), name);
  }
}
```
"""),
        ("Protected members", r"""
Use `protected` when subclasses need access but external code should not.
"""),
        ("Class vs interface", r"""
| Use | Choice |
|-----|--------|
| Data only | `interface` |
| Behavior + state | `class` |
| Contract for class | `implements` |
"""),
    ]),
    "ch08-type-narrowing.md": _block([
        ("Equality narrowing", r"""
```typescript
function example(x: string | number, y: string | number) {
  if (x === y) {
    // x and y narrowed together when comparable
  }
}
```
"""),
        ("in operator", r"""
```typescript
if ("swim" in pet) pet.swim();
```
"""),
        ("Exhaustiveness helper", r"""
```typescript
function assertNever(x: never): never {
  throw new Error(`Unexpected: ${JSON.stringify(x)}`);
}
```
"""),
    ]),
    "ch09-enums-and-literals.md": _block([
        ("const object pattern", r"""
```typescript
const Status = { Pending: "PENDING", Done: "DONE" } as const;
type Status = (typeof Status)[keyof typeof Status];
```
"""),
        ("Template literal types", r"""
```typescript
type Event = "click" | "focus";
type Handler = `on${Capitalize<Event>}`;
```
"""),
        ("satisfies recap", r"""
Use `satisfies` to check a value against a type without widening literals.
"""),
    ]),
    "ch10-modules-and-config.md": _block([
        ("import type", r"""
```typescript
import type { User } from "./models.js";
```
"""),
        ("NodeNext resolution", r"""
For Node ESM, use `"module": "NodeNext"` and include `.js` extensions in import specifiers.
"""),
        ("Declaration files", r"""
Publish `declaration: true` for libraries so consumers get `.d.ts` files.
"""),
    ]),
    "ch11-async-typescript.md": _block([
        ("Result type", r"""
Model errors as data with `{ ok: true; value } | { ok: false; error }` unions.
"""),
        ("Promise.all", r"""
`Promise.all` on a tuple returns a tuple of resolved types — great for parallel fetches.
"""),
        ("void callbacks", r"""
`setTimeout(() => { ... })` callbacks often return `void` — do not mark them `async` unless you handle the floating promise.
"""),
    ]),
    "ch12-react-with-typescript.md": _block([
        ("Children typing", r"""
Use `React.ReactNode` for flexible children; `React.ReactElement` when you need a single element.
"""),
        ("Discriminated actions", r"""
Type `useReducer` actions as a union with a `type` field for safe switches.
"""),
        ("Generic components", r"""
```typescript
function Select<T extends string>({ options, value, onChange }: {
  options: readonly T[];
  value: T;
  onChange: (v: T) => void;
}) { /* ... */ }
```
"""),
    ]),
    "ch13-best-practices.md": _block([
        ("Incremental strict flags", r"""
Enable `strictNullChecks` first, then `noImplicitAny`, then `noUncheckedIndexedAccess` in separate PRs.
"""),
        ("ESLint", r"""
Use `@typescript-eslint/no-explicit-any` and `@typescript-eslint/no-floating-promises` in CI.
"""),
        ("Runtime validation", r"""
Use Zod/Valibot at API boundaries — types alone do not validate JSON at runtime.
"""),
    ]),
    "ch14-interview-prep.md": _block([
        ("Answer structure", r"""
Use **Problem → TypeScript tool → Outcome** when answering behavioral questions.
"""),
        ("Whiteboard tips", r"""
Start with concrete usage, then generalize to the type definition. Narrate trade-offs.
"""),
    ]),
}
