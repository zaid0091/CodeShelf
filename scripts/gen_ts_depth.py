"""Substantive depth sections (~150+ lines each) for chapters under 800 lines."""

from gen_ts_supplements_all import _sec


def _chapter_block(sections: list[tuple[str, str]]) -> str:
    return "".join(_sec(t, b) for t, b in sections)


# Shared patterns
def _def(term: str, plain: str) -> tuple[str, str]:
    return (
        f"Definition — {term}",
        f"> **Definition:** **{term}** — {plain}\n",
    )

DEPTH: dict[str, str] = {}

DEPTH["ch03-interfaces-and-type-aliases.md"] = _chapter_block([
    _def("Duck typing", "If it walks like a duck and quacks like a duck, TypeScript treats it as a duck — structure matters, not the name of the type."),
    ("Worked example — e-commerce", r"""
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
"""),
])

DEPTH["ch04-functions.md"] = _chapter_block([
    _def("Function signature", "The list of parameter types and the return type — the contract callers must satisfy."),
    ("Step-by-step — overload design", r"""
1. List each way callers invoke the function.
2. Write one overload signature per shape.
3. Write one implementation that accepts the union of inputs.
4. Narrow inside the implementation with `typeof` or discriminant checks.
"""),
    ("Practice — event handler types", r"""
```typescript
type ClickHandler = (event: MouseEvent) => void;
type KeyHandler = (event: KeyboardEvent) => void;

function on(element: HTMLElement, event: "click", handler: ClickHandler): void;
function on(element: HTMLElement, event: "keydown", handler: KeyHandler): void;
function on(element: HTMLElement, event: string, handler: (e: Event) => void): void {
  element.addEventListener(event, handler as EventListener);
}
```
"""),
    ("Common interview — optional vs default", r"""
| Feature | Syntax | When absent |
|---------|--------|-------------|
| Optional | `x?: number` | `undefined` |
| Default | `x = 0` | uses default value |

Optional parameters must follow required parameters.
"""),
])

DEPTH["ch05-generics.md"] = _chapter_block([
    _def("Type parameter", "A placeholder type (often `T`) filled in when you call a generic function or instantiate a generic class."),
    ("Analogy — labeled boxes", r"""
Generics are shipping boxes with **labels** (`T`) instead of writing "box for books" and "box for shoes" as separate functions.

One factory function `box<T>(item: T): T[]` works for any item type.
"""),
    ("Worked example — repository", r"""
```typescript
interface Entity { id: string }

class MemoryRepo<T extends Entity> {
  private store = new Map<string, T>();

  save(entity: T): void {
    this.store.set(entity.id, entity);
  }

  findById(id: string): T | undefined {
    return this.store.get(id);
  }
}
```
"""),
    ("keyof in practice", r"""
```typescript
function pick<T, K extends keyof T>(obj: T, keys: K[]): Pick<T, K> {
  const result = {} as Pick<T, K>;
  for (const key of keys) {
    result[key] = obj[key];
  }
  return result;
}
```
"""),
])

DEPTH["ch06-utility-types.md"] = _chapter_block([
    _def("Utility type", "A built-in generic type transformer provided by TypeScript (e.g. `Partial`, `Pick`)."),
    ("CRUD walkthrough", r"""
From one `User` interface, derive:

- `UserCreate` = `Omit<User, 'id'>`
- `UserUpdate` = `Partial<Omit<User, 'id'>>`
- `UserPublic` = `Pick<User, 'id' | 'name'>`

This avoids three copies of the same field list.
"""),
    ("Exclude / Extract scenarios", r"""
```typescript
type All = string | number | boolean;
type OnlyStrings = Extract<All, string>; // string
type NoStrings = Exclude<All, string>; // number | boolean
```
"""),
    ("Awaited nested promises", r"""
```typescript
type Deep = Promise<Promise<number>>;
type Flat = Awaited<Deep>; // number
```
"""),
])

DEPTH["ch07-classes-and-oop.md"] = _chapter_block([
    _def("Encapsulation", "Hiding internal state so outside code cannot put the object in an invalid state."),
    ("Class diagram — simple hierarchy", r"""
```text
        Animal
           │
           ├── Dog
           └── Cat
```

```typescript
abstract class Animal {
  abstract speak(): string;
}
class Dog extends Animal {
  override speak() { return "woof"; }
}
```
"""),
    ("When not to use classes", r"""
Prefer functions + interfaces when you only transform data. Use classes when you manage lifecycle and invariants (connections, caches, game entities).
"""),
])

DEPTH["ch08-type-narrowing.md"] = _chapter_block([
    _def("Type guard", "An expression that refines a type in a branch — `typeof`, `instanceof`, `in`, or a custom `x is T` predicate."),
    ("Discriminated union — loading state", r"""
```typescript
type State =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: string[] }
  | { status: "error"; message: string };

function render(state: State) {
  switch (state.status) {
    case "idle": return "Press load";
    case "loading": return "Loading…";
    case "success": return state.data.join(", ");
    case "error": return state.message;
  }
}
```
"""),
    ("Type predicate exercise explained", r"""
```typescript
function isError(value: unknown): value is Error {
  return value instanceof Error;
}
```
After `if (isError(e))`, `e` is `Error` inside the block.
"""),
])

DEPTH["ch09-enums-and-literals.md"] = _chapter_block([
    _def("Literal type", 'A type that allows only specific constant values, e.g. `"success" | "error"`.'),
    ("Numeric enum pitfalls", r"""
```typescript
enum Num { A, B } // A=0, B=1 — implicit numbers surprise readers
```

Prefer string unions or `as const` objects for clarity.
"""),
    ("as const walkthrough", r"""
```typescript
const routes = {
  home: "/",
  profile: "/me",
} as const;

type Route = (typeof routes)[keyof typeof routes]; // "/" | "/me"
```
"""),
    ("satisfies example", r"""
```typescript
const config = {
  apiUrl: "https://api.example.com",
  retries: 3,
} satisfies { apiUrl: string; retries: number };
```
"""),
])

DEPTH["ch10-modules-and-config.md"] = _chapter_block([
    _def("Module", "A file that exports values/types and imports from other files — ES modules are the standard."),
    ("tsconfig strict family", r"""
| Flag | Benefit |
|------|---------|
| `strictNullChecks` | Catches null/undefined bugs |
| `noImplicitAny` | Forces explicit types |
| `noUncheckedIndexedAccess` | Indexing may be undefined |
"""),
    ("Barrel file caution", r"""
`index.ts` re-exports can create circular imports. Prefer direct imports in large codebases.
"""),
    ("Vite + TypeScript", r"""
Vite transpiles fast; run `tsc --noEmit` in CI for full type-checking.
"""),
])

DEPTH["ch11-async-typescript.md"] = _chapter_block([
    _def("Promise", "A value that will be available in the future — typed as `Promise<T>` where `T` is the resolved type."),
    ("async/await flow", r"""
```typescript
async function loadUser(id: string): Promise<User> {
  const res = await fetch(`/api/users/${id}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const raw: unknown = await res.json();
  return parseUser(raw); // validate before trust
}
```
"""),
    ("Error handling patterns", r"""
| Pattern | Use when |
|---------|----------|
| try/catch | Simple scripts |
| Result union | Explicit error paths |
| Custom Error subclass | HTTP/API layers |
"""),
])

DEPTH["ch12-react-with-typescript.md"] = _chapter_block([
    _def("Props", "The read-only inputs passed to a React component — typed as an interface."),
    ("Props with children", r"""
```typescript
interface CardProps {
  title: string;
  children: React.ReactNode;
}

function Card({ title, children }: CardProps) {
  return (
    <section>
      <h2>{title}</h2>
      {children}
    </section>
  );
}
```
"""),
    ("useState patterns", r"""
```typescript
const [count, setCount] = useState(0);
const [user, setUser] = useState<User | null>(null);
```
"""),
])

DEPTH["ch13-best-practices.md"] = _chapter_block([
    _def("Strict mode", "A bundle of `tsconfig` flags that enable the strictest practical type checking."),
    ("Code review checklist", r"""
1. No new `any` without justification comment
2. External JSON validated at boundary
3. Public exports have explicit types
4. Unions exhaustive in `switch`
5. No `@ts-ignore` without ticket link
6. `import type` for type-only imports
7. Tests cover edge cases types cannot catch
"""),
    ("Branded types", r"""
```typescript
type Cents = number & { readonly __brand: unique symbol };
type Dollars = number & { readonly __brand: unique symbol };
```
Prevents accidentally adding cents to dollars without conversion.
"""),
])

DEPTH["ch14-interview-prep.md"] = _chapter_block([
    ("STAR method for TS stories", r"""
- **Situation:** Large React codebase, frequent null errors
- **Task:** Introduce strictNullChecks
- **Action:** Enabled flag, fixed modules incrementally, added CI `tsc --noEmit`
- **Result:** Fewer production incidents, faster onboarding
"""),
])

# Expand thin chapters with extra worked examples
for key, extra_sections in {
    "ch09-enums-and-literals.md": [
        ("HTTP status literals", r"""
```typescript
type HttpOk = 200 | 201;
type HttpErr = 404 | 500;
type HttpStatus = HttpOk | HttpErr;
```
"""),
    ],
    "ch10-modules-and-config.md": [
        ("package.json types field", r"""
```json
{
  "name": "my-lib",
  "types": "./dist/index.d.ts",
  "exports": { ".": { "types": "./dist/index.d.ts", "import": "./dist/index.js" } }
}
```
"""),
    ],
    "ch13-best-practices.md": [
        ("Documentation comments", r"""
```typescript
/**
 * Converts cents to a USD display string.
 * @param cents - Integer cents (non-negative)
 */
export function formatUsd(cents: number): string {
  return `$${(cents / 100).toFixed(2)}`;
}
```
"""),
    ],
}.items():
    DEPTH[key] = DEPTH.get(key, "") + _chapter_block(extra_sections)

# Additional depth for chapters targeting 800+ lines
DEPTH["ch04-functions.md"] += _chapter_block([
    ("Rest and spread typing", r"""
```typescript
function merge<T extends object, U extends object>(a: T, b: U): T & U {
  return { ...a, ...b };
}
```
"""),
])

DEPTH["ch05-generics.md"] += _chapter_block([
    ("Inference with generics", r"""
```typescript
const ids = [1, 2, 3];
const firstId = ids.map((n) => n * 2); // number[] — T inferred
```
"""),
    ("Generic constraints — real API", r"""
```typescript
function sortBy<T extends { createdAt: Date }>(items: T[]): T[] {
  return [...items].sort((a, b) => a.createdAt.getTime() - b.createdAt.getTime());
}
```
"""),
    ("Common mistakes", r"""
| Mistake | Fix |
|---------|-----|
| `function f<T = any>` | Default to `unknown` or omit default |
| Too many type params | Use options object type |
| Casting inside generic | Use constraints + narrowing |
"""),
])

DEPTH["ch06-utility-types.md"] += _chapter_block([
    ("Partial for PATCH endpoints", r"""
```typescript
type UserUpdate = Partial<Omit<User, "id" | "createdAt">>;
```
"""),
    ("Parameters and ReturnType", r"""
```typescript
type FetchUser = typeof fetchUser;
type User = Awaited<ReturnType<FetchUser>>;
```
"""),
])

DEPTH["ch07-classes-and-oop.md"] += _chapter_block([
    ("Interface for test doubles", r"""
```typescript
interface Clock { now(): Date }
class SystemClock implements Clock { now() { return new Date(); } }
class FakeClock implements Clock { constructor(private t: Date) {} now() { return this.t; } }
```
"""),
])

DEPTH["ch08-type-narrowing.md"] += _chapter_block([
    ("Truthiness narrowing", r"""
```typescript
function printName(name: string | null | undefined) {
  if (!name) return;
  console.log(name.toUpperCase()); // string
}
```
"""),
])

DEPTH["ch09-enums-and-literals.md"] += _chapter_block([
    ("Migrating from enum", r"""
1. List all enum members used in codebase.
2. Create `as const` object + union type.
3. Replace `Enum.Member` with `Object.Member`.
4. Remove enum and delete emitted JS object.
"""),
])

DEPTH["ch10-modules-and-config.md"] += _chapter_block([
    ("include / exclude", r"""
```json
{
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "**/*.test.ts"]
}
```
"""),
])

DEPTH["ch11-async-typescript.md"] += _chapter_block([
    ("Floating promises", r"""
```typescript
// ❌ ESLint @typescript-eslint/no-floating-promises
saveUser(data);

// ✅
void saveUser(data); // explicit fire-and-forget
// or
await saveUser(data);
```
"""),
])

DEPTH["ch13-best-practices.md"] += _chapter_block([
    ("Avoid assertion abuse", r"""
| Instead of | Prefer |
|------------|--------|
| `x as User` | Validate + type guard |
| `!` non-null assertion | Narrow with `if` |
| `@ts-ignore` | Fix type or narrow scope |
"""),
])


def get_depth(filename: str) -> str:
    return DEPTH.get(filename, "")
