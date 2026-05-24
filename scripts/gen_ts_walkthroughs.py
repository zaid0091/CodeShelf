"""In-depth walkthrough sections (JavaScript ch01 style) per TypeScript chapter."""

from __future__ import annotations


def _w(title: str, body: str) -> str:
    return f"## {title}\n\n{body.strip()}\n\n---\n\n"


# Chapter 1 — additional depth beyond gen_ts_ch01 BODY
WALKTHROUGH_CH01 = "".join([
    _w("Learning path — how to read this course", """
Think of TypeScript as **JavaScript with a safety net**. You already know how to walk (JavaScript); TypeScript adds guardrails so you do not fall off the cliff at runtime.

| Phase | What you do | Outcome |
|-------|-------------|---------|
| Read | One section at a time | Mental model |
| Type | Small `.ts` files in `src/` | Muscle memory |
| Break | Change types on purpose | Read errors |
| Fix | Apply compiler suggestions | Confidence |

> **Tip:** Keep a scratch project open while reading. When a section shows code, paste it and change one line to see what error appears.
"""),
    _w("Analogy — contract vs handshake", """
In plain JavaScript, functions are a **handshake** — you hope the other person (caller) gives you the right shape of data.

In TypeScript, you write a **contract** first:

```typescript
interface Order {
  id: string;
  totalCents: number;
}

function charge(order: Order): void {
  console.log(order.totalCents / 100);
}
```

If someone passes `{ id: 1, total: "free" }`, the compiler stops you **before** users see a broken checkout page.
"""),
    _w("Step-by-step — first project from zero", """
### Step 1: Create the folder

```bash
mkdir codeshelf-ts-hello && cd codeshelf-ts-hello
npm init -y
```

### Step 2: Install TypeScript locally

```bash
npm install --save-dev typescript
npx tsc --init
```

### Step 3: Edit tsconfig.json

Set `rootDir` to `./src`, `outDir` to `./dist`, and `strict` to `true`.

### Step 4: Create src/index.ts

Write a `greet` function with typed parameters.

### Step 5: Compile and run

```bash
npx tsc
node dist/index.js
```

### What can go wrong?

| Problem | Fix |
|---------|-----|
| `Cannot find module` | Check `moduleResolution` matches Node/bundler |
| Empty `dist/` | Fix compile errors first — tsc may not emit |
| `node` runs old code | Re-run `npx tsc` after edits |
"""),
    _w("Tooling comparison — tsc vs bundlers", """
| Tool | Role |
|------|------|
| `tsc` | Official compiler; type-check + emit JS |
| Vite | Dev server + fast transform; uses esbuild for speed |
| esbuild | Extremely fast transpile; limited type-check |
| SWC | Fast Rust-based transform |

**Best practice:** Run `tsc --noEmit` in CI for full type-checking even if Vite handles dev builds.
"""),
    _w("Migration story — one file at a time", """
```text
Week 1: utils.js → utils.ts (add types to exports)
Week 2: api.js → api.ts (define response interfaces)
Week 3: enable strictNullChecks
Week 4: remove allowJs from new code paths
```

Rename files only when you are ready to fix errors in that file. Do not rename the entire repo in one commit unless you have time for a large fix-up PR.
"""),
    _w("Glossary — Chapter 1 terms", """
| Term | Plain English |
|------|----------------|
| Static typing | Types checked before run |
| Superset | All JS is valid TS |
| Type erasure | Types deleted in output |
| Inference | Compiler guesses types |
| Annotation | You write the type explicitly |
| strict | Bundle of safer compiler flags |
| .d.ts | Type description file for JS libraries |
"""),
])

WALKTHROUGH_CH02 = "".join([
    _w("Primitives — everyday mental model", """
Values in TypeScript fall into groups, like sorting items in a warehouse:

| Shelf | Types | Examples |
|-------|-------|----------|
| Text | `string` | `"hello"`, `` `hi` `` |
| Numbers | `number`, `bigint` | `42`, `3.14n` |
| Yes/No | `boolean` | `true`, `false` |
| Empty slots | `null`, `undefined` | intentional vs missing |
| Unique tags | `symbol` | `Symbol("id")` |

With `strictNullChecks`, `null` and `undefined` are **not** interchangeable with other types unless you add them to a union.
"""),
    _w("Walkthrough — typing a user profile", """
```typescript
interface UserProfile {
  username: string;
  age: number;
  isVerified: boolean;
  bio?: string; // optional — may be undefined
}

const profile: UserProfile = {
  username: "dev_ada",
  age: 28,
  isVerified: true,
};

// Safe optional access
const text = profile.bio?.toUpperCase() ?? "No bio yet";
```

Line by line:

1. `username: string` — must be text, not a number.
2. `bio?` — key may be missing; value may be `undefined`.
3. `?.` — if `bio` is missing, expression short-circuits to `undefined`.
4. `??` — if left side is `null`/`undefined`, use the right side string.
"""),
    _w("any vs unknown — story with two doors", """
- **`any`** is a door with no lock. TypeScript stops checking. Anything goes in or out.
- **`unknown`** is a locked door. You must prove what is inside before using it.

```typescript
function handleInput(raw: unknown) {
  if (typeof raw === "string") {
    console.log(raw.toUpperCase()); // safe — narrowed to string
  }
}
```

Use `unknown` for JSON, `window` extensions, and third-party callbacks you do not control.
"""),
    _w("never — the empty set", """
`never` means **no value can exist here**.

```typescript
function fail(msg: string): never {
  throw new Error(msg);
}

type Result = { ok: true } | { ok: false };
function assertOk(r: Result) {
  if (!r.ok) {
    fail("expected success"); // return type never — function does not return normally
  }
}
```

In `switch` on unions, assign `never` in `default` so adding a new union member forces you to update the switch.
"""),
    _w("Arrays and tuples — when to use which", """
Use an **array** when all items share one type and length can change:

```typescript
const scores: number[] = [90, 85, 88];
scores.push(92);
```

Use a **tuple** when position matters:

```typescript
type HttpResponse = [status: number, body: string];
const res: HttpResponse = [200, "OK"];
```

| Need | Choose |
|------|--------|
| Homogeneous list | `T[]` |
| Fixed columns (CSV row) | tuple |
| Read-only list | `readonly T[]` |
"""),
])

WALKTHROUGH_CH03 = "".join([
    _w("Modeling a blog — end-to-end", """
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
"""),
    _w("interface vs type — decision flowchart", """
```text
Need a union or tuple alias?     → type
Need mapped/conditional type?    → type
Public object API for a library? → interface (extend/merge friendly)
Combining two object shapes?     → type A & B OR interface extends
```

Both work for object shapes. Pick one style per project and stay consistent.
"""),
    _w("Index signatures — dynamic keys", """
```typescript
interface ScoresByPlayer {
  [playerId: string]: number;
}

const board: ScoresByPlayer = {};
board["p1"] = 10;
// board["p1"] = "ten"; // Error
```

Use when keys are not known at compile time but values share one type.
"""),
    _w("Declaration merging — power and caution", """
```typescript
interface Window {
  myAppVersion?: string;
}
```

TypeScript merges this with the global `Window` interface. Helpful for globals; confusing if overused. Prefer explicit modules over augmenting globals when possible.
"""),
])

WALKTHROUGH_CH04 = "".join([
    _w("Function types — reading signatures", """
```typescript
type SearchFn = (query: string, limit?: number) => string[];
```

Read it aloud: "A function that takes a string and optional number, and returns an array of strings."

Optional parameters must come **after** required ones.
"""),
    _w("Overloads — real-world parse example", """
```typescript
function parse(input: string): string;
function parse(input: number): number;
function parse(input: string | number): string | number {
  if (typeof input === "string") return input.trim();
  return Math.round(input);
}
```

Callers get precise return types; one implementation handles all cases.
"""),
    _w("Contextual typing — callbacks", """
```typescript
const nums = [1, 2, 3];
const doubled = nums.map((n) => n * 2); // n inferred as number
```

The expected type of the callback parameter flows **down** from `map`'s definition.
"""),
])

WALKTHROUGH_CH05 = "".join([
    _w("Why generics beat duplication", """
Without generics you copy-paste the same logic:

```typescript
function firstString(arr: string[]): string | undefined { return arr[0]; }
function firstNumber(arr: number[]): number | undefined { return arr[0]; }
```

With generics, one implementation serves all:

```typescript
function first<T>(arr: T[]): T | undefined { return arr[0]; }
```

The compiler **specializes** `T` per call site — no runtime cost.
"""),
    _w("Generics — the reusable box", """
Without generics, you choose between duplication and losing type info:

```typescript
// Loses info:
function firstAny(arr: any[]): any { return arr[0]; }

// Keeps info:
function first<T>(arr: T[]): T | undefined { return arr[0]; }

const n = first([1, 2, 3]); // number | undefined
```

`T` is a **placeholder** filled in when you call the function.
"""),
    _w("Constraints — generics with rules", """
```typescript
interface HasLength { length: number }

function logLength<T extends HasLength>(item: T): void {
  console.log(item.length);
}

logLength("hi");
logLength([1, 2]);
// logLength(42); // Error — number has no .length
```
"""),
    _w("Generic interfaces — API wrappers", """
```typescript
interface ApiResponse<T> {
  data: T;
  meta: { page: number; total: number };
}

type UserList = ApiResponse<User[]>;
```
"""),
])

WALKTHROUGH_CH06 = "".join([
    _w("When to reach for each utility", """
| You need | Utility |
|----------|---------|
| Update form (partial fields) | `Partial<T>` |
| Config that cannot change | `Readonly<T>` |
| Public API subset | `Pick<T, keys>` |
| Hide internal fields | `Omit<T, keys>` |
| Dictionary / map | `Record<K, V>` |
| Unwrap function return | `ReturnType<F>` |
| Unwrap Promise | `Awaited<P>` |
"""),
    _w("CRUD types from one source", """
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
"""),
    _w("Utility types — quick reference", """
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
"""),
])

WALKTHROUGH_CH07 = "".join([
    _w("Class design — when to use classes", """
Use classes when you have **state + behavior** that belong together:

```typescript
class ShoppingCart {
  private items: { sku: string; qty: number }[] = [];

  add(sku: string, qty: number) {
    this.items.push({ sku, qty });
  }

  totalItems(): number {
    return this.items.reduce((sum, i) => sum + i.qty, 0);
  }
}
```

For plain data shapes, prefer `interface` + functions.
"""),
    _w("implements vs extends", """
- **`extends`** — inherit implementation from a parent class.
- **`implements`** — promise your class matches an interface shape.

```typescript
interface Serializable { toJSON(): object }

class User implements Serializable {
  constructor(public name: string) {}
  toJSON() { return { name: this.name }; }
}
```
"""),
])

WALKTHROUGH_CH08 = "".join([
    _w("Narrowing — control-flow analysis", """
TypeScript tracks types through `if`, `switch`, `return`, and `throw`:

```typescript
function printId(id: string | number) {
  if (typeof id === "string") {
    console.log(id.toUpperCase());
    return;
  }
  console.log(id.toFixed(0));
}
```

After the `typeof` check, each branch has a **narrower** type.
"""),
    _w("Discriminated unions — state machines", """
```typescript
type RequestState =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: string }
  | { status: "error"; message: string };

function render(state: RequestState) {
  switch (state.status) {
    case "idle": return "Click load";
    case "loading": return "Loading…";
    case "success": return state.data;
    case "error": return state.message;
  }
}
```

The `status` field is the **discriminant** — TypeScript knows which other fields exist in each branch.
"""),
])

WALKTHROUGH_CH09 = "".join([
    _w("Choosing enum vs union — decision table", """
| Need | Prefer |
|------|--------|
| Zero runtime cost | String literal union |
| Iterate all values at runtime | `as const` object or string enum |
| Reverse mapping (name from value) | Numeric enum (rare) |
| API from Java/C# background | String enum for familiarity |

Most new TypeScript codebases default to **union literals** or **`as const` objects**.
"""),
    _w("Modern alternative to numeric enums", """
```typescript
const Direction = {
  Up: "UP",
  Down: "DOWN",
} as const;

type Direction = (typeof Direction)[keyof typeof Direction];
```

You get a runtime object **and** a string union type without numeric enum surprises.
"""),
    _w("satisfies — validate without widening", """
```typescript
const config = {
  apiUrl: "https://api.example.com",
  retries: 3,
} satisfies { apiUrl: string; retries: number };

// config.apiUrl stays literal type for autocomplete
```
"""),
])

WALKTHROUGH_CH10 = "".join([
    _w("Monorepo layout", """
```text
packages/
  api/          ← tsconfig, src
  web/          ← references api types
  shared-types/ ← shared interfaces
```

Use **project references** so `tsc -b` builds in dependency order.
"""),
    _w("Module graph — mental model", """
```text
app.ts  ──imports──►  user.ts
   │                      │
   └──imports──►  types.ts (import type only)
```

Keep **value imports** for functions/classes and **`import type`** for types to help bundlers tree-shake and avoid circular value dependencies.
"""),
    _w("tsconfig layers", """
| File | Purpose |
|------|---------|
| `tsconfig.json` | Root; may reference subprojects |
| `tsconfig.app.json` | App source only |
| `tsconfig.node.json` | Vite config, scripts |

Split configs so editor and CI only check relevant files.
"""),
])

WALKTHROUGH_CH11 = "".join([
    _w("Promise typing — mental model", """
`Promise<T>` is a box that will eventually contain a `T` (or reject).

```typescript
async function fetchCount(): Promise<number> {
  const res = await fetch("/api/count");
  return Number(await res.text());
}
```

The **return type** of an `async` function is always wrapped in `Promise<...>`.
"""),
    _w("Async errors — typed handling", """
```typescript
type Result<T> =
  | { ok: true; value: T }
  | { ok: false; error: Error };

async function loadText(url: string): Promise<Result<string>> {
  try {
    const res = await fetch(url);
    if (!res.ok) return { ok: false, error: new Error(String(res.status)) };
    return { ok: true, value: await res.text() };
  } catch (e) {
    return { ok: false, error: e instanceof Error ? e : new Error(String(e)) };
  }
}
```

Callers must check `ok` before using `value` — the type system enforces it.
"""),
])

WALKTHROUGH_CH12 = "".join([
    _w("Props — extending HTML elements", """
```typescript
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "ghost";
}

function Button({ variant = "primary", children, ...rest }: ButtonProps) {
  return <button className={variant} {...rest}>{children}</button>;
}
```

`...rest` forwards `onClick`, `disabled`, `type`, etc. with correct types.
"""),
    _w("Hooks — typing patterns", """
| Hook | Pattern |
|------|---------|
| `useState` | `useState<User | null>(null)` |
| `useRef` | `useRef<HTMLInputElement>(null)` |
| `useReducer` | Discriminated union for actions |
| `useContext` | `createContext<T | undefined>` + guard hook |
"""),
])

WALKTHROUGH_CH13 = "".join([
    _w("Team conventions document", """
Maintain a `TYPESCRIPT.md` in the repo covering:

- Required `tsconfig` flags
- `any` policy (forbidden vs escape hatch)
- Validation library at API boundary
- Naming: `interface` vs `type`
- PR checklist for type-related changes

Onboarding improves when conventions are written, not tribal knowledge.
"""),
    _w("Strict flags — one at a time", """
On legacy codebases, enable gradually:

1. `strictNullChecks`
2. `noImplicitAny`
3. `strictFunctionTypes`
4. `noUncheckedIndexedAccess`

Fix errors per flag in dedicated PRs so reviews stay focused.
"""),
    _w("Boundary validation", """
```typescript
import { z } from "zod";

const UserSchema = z.object({ id: z.string(), name: z.string() });
type User = z.infer<typeof UserSchema>;

function parseUser(raw: unknown): User {
  return UserSchema.parse(raw);
}
```

Types do not validate at runtime — schemas do.
"""),
])

WALKTHROUGH_CH14 = "".join([
    _w("How to answer 'Why TypeScript?'", """
Structure your answer in three parts:

1. **Problem:** Dynamic JS allows silent bugs in large codebases.
2. **Solution:** Compile-time types + IDE tooling catch errors early.
3. **Proof:** One real bug you prevented (wrong property, null access, bad refactor).

Avoid saying only "it's industry standard" — interviewers want reasoning.
"""),
    _w("Mock interview rubric", """
| Score | You demonstrate |
|-------|-----------------|
| 1 | Syntax only |
| 2 | Correct definitions |
| 3 | Trade-offs (any vs unknown, enum vs union) |
| 4 | Real project examples |
| 5 | System design + validation at boundaries |
"""),
])

WALKTHROUGHS: dict[str, str] = {
    "ch01-introduction.md": WALKTHROUGH_CH01,
    "ch02-types-and-primitives.md": WALKTHROUGH_CH02,
    "ch03-interfaces-and-type-aliases.md": WALKTHROUGH_CH03,
    "ch04-functions.md": WALKTHROUGH_CH04,
    "ch05-generics.md": WALKTHROUGH_CH05,
    "ch06-utility-types.md": WALKTHROUGH_CH06,
    "ch07-classes-and-oop.md": WALKTHROUGH_CH07,
    "ch08-type-narrowing.md": WALKTHROUGH_CH08,
    "ch09-enums-and-literals.md": WALKTHROUGH_CH09,
    "ch10-modules-and-config.md": WALKTHROUGH_CH10,
    "ch11-async-typescript.md": WALKTHROUGH_CH11,
    "ch12-react-with-typescript.md": WALKTHROUGH_CH12,
    "ch13-best-practices.md": WALKTHROUGH_CH13,
    "ch14-interview-prep.md": WALKTHROUGH_CH14,
}


def get_walkthrough(filename: str) -> str:
    return WALKTHROUGHS.get(filename, "")
