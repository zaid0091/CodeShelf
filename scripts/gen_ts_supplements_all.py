"""Substantive per-chapter supplemental sections (no repetitive filler)."""

def _sec(title: str, body: str) -> str:
    return f"## {title}\n\n{body}\n\n---\n\n"


SUPPLEMENT_CH02 = "".join([
    _sec("string — deep dive", r"""
### Why strings matter in TypeScript

Strings appear in UI labels, API fields, URLs, and identifiers. TypeScript treats all string literals as type `string` unless you use literal types or `as const`.

```typescript
const greeting: string = "Hello";
const template: string = `User: ${greeting}`;

function truncate(text: string, maxLen: number): string {
  return text.length > maxLen ? text.slice(0, maxLen) + "…" : text;
}
```

| Method | Returns | Example |
|--------|---------|---------|
| `.length` | number | `"hi".length` → 2 |
| `.toUpperCase()` | string | `"a".toUpperCase()` → `"A"` |
| `.includes(sub)` | boolean | `"hello".includes("ell")` |
| `.slice(start, end?)` | string | `"hello".slice(1, 3)` → `"el"` |

### Template literal types (preview)

```typescript
type EventName = "click" | "focus";
type HandlerName = `on${Capitalize<EventName>}`; // "onClick" | "onFocus"
```
"""),
    _sec("number — deep dive", r"""
JavaScript numbers are IEEE 754 doubles. TypeScript does not distinguish int vs float.

```typescript
let integer: number = 42;
let float: number = 3.14;
let hex: number = 0xff;
let binary: number = 0b1010;
let octal: number = 0o744;

// Special numeric values
let notANumber: number = NaN;
let infinity: number = Infinity;
```

| Constant | Value | Note |
|----------|-------|------|
| `Number.MAX_SAFE_INTEGER` | 9007199254740991 | Use bigint beyond this |
| `Number.EPSILON` | tiny | Float comparison tolerance |

```typescript
// Prefer Number.isNaN over global isNaN
Number.isNaN(NaN); // true
Number.isNaN("hello"); // false — global isNaN coerces
```
"""),
    _sec("bigint and symbol", r"""
### bigint

```typescript
const huge: bigint = 9007199254740992n;
const also = BigInt("9007199254740992");
// Cannot mix bigint and number without conversion
```

### symbol

```typescript
const id: symbol = Symbol("id");
const id2: symbol = Symbol("id");
console.log(id === id2); // false — each Symbol() is unique

const KEY = Symbol("key");
type Obj = { [KEY]: string };
```
"""),
    _sec("Arrays — patterns and pitfalls", r"""
```typescript
// Readonly prevents mutation at type level
const ids: readonly number[] = [1, 2, 3];
// ids.push(4); // compile error

// Tuple for fixed structure
type RGB = [number, number, number];
const red: RGB = [255, 0, 0];

// Labeled tuple elements (readable)
type HttpPair = [status: number, body: string];
```

### Common array typing mistakes

```typescript
// ❌ Empty array widens to any[] without context
const bad = [];
bad.push(1);
bad.push("two"); // allowed if any[]

// ✅ Provide context
const good: number[] = [];
// or
const alsoGood = [] as number[];
```
"""),
    _sec("Special types — comparison matrix", r"""
| Type | Assign from | Assign to without check | Runtime exists? |
|------|-------------|-------------------------|-----------------|
| `any` | all | all | n/a (checking off) |
| `unknown` | all | none | n/a |
| `void` | undefined | void contexts | yes (undefined) |
| `never` | never | never | n/a |
| `null` | null | only with union | yes |
| `undefined` | undefined | only with union | yes |
"""),
])

SUPPLEMENT_CH03 = "".join([
    _sec("Real-world interface design", r"""
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
"""),
    _sec("Composition patterns", r"""
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
"""),
    _sec("Excess property checking — explained", r"""
```typescript
interface Point { x: number; y: number }

const p = { x: 1, y: 2, label: "a" }; // inferred with label
function draw(pt: Point) { console.log(pt.x); }
draw(p); // OK — variable may have extras

draw({ x: 1, y: 2, label: "a" }); // Error on excess 'label'
```

**Why?** Catch typos in object literals at call sites.
"""),
])

SUPPLEMENT_CH04_EXTRA = _sec("Currying and composition", r"""
```typescript
const curry =
  <A, B, C>(fn: (a: A, b: B) => C) =>
  (a: A) =>
  (b: B) =>
    fn(a, b);

const add = (a: number, b: number) => a + b;
const add5 = curry(add)(5);
console.log(add5(3)); // 8
```
""")

SUPPLEMENT_CH04 = "".join([
    _sec("Function types as values", r"""
```typescript
type BinaryOp = (a: number, b: number) => number;
const add: BinaryOp = (a, b) => a + b;

type StringMapper = (s: string) => string;
const shout: StringMapper = (s) => s.toUpperCase();
```
"""),
    _sec("Overload patterns", r"""
```typescript
function createElement(tag: "div"): HTMLDivElement;
function createElement(tag: "span"): HTMLSpanElement;
function createElement(tag: string): HTMLElement;
function createElement(tag: string): HTMLElement {
  return document.createElement(tag);
}
```

Implementation signature must be compatible with all overloads.
"""),
    _sec("Async function typing", r"""
```typescript
async function loadConfig(path: string): Promise<AppConfig> {
  const raw = await readFile(path, "utf8");
  return JSON.parse(raw) as AppConfig; // prefer validation
}

type AwaitedConfig = Awaited<ReturnType<typeof loadConfig>>;
```
"""),
    _sec("Optional and default parameters", r"""
```typescript
function greet(name: string, greeting: string = "Hello"): string {
  return `${greeting}, ${name}`;
}

function connect(host: string, port?: number): void {
  const p = port ?? 443;
  console.log(host, p);
}
```

| Parameter | Syntax | Notes |
|-----------|--------|-------|
| Optional | `name?: T` | May be `undefined` |
| Default | `name = value` | Inferred type from default |
| Rest | `...args: T[]` | Collects remaining arguments |
"""),
    _sec("Higher-order functions", r"""
```typescript
function map<T, U>(items: T[], fn: (item: T) => U): U[] {
  return items.map(fn);
}

function filter<T>(items: T[], pred: (item: T) => boolean): T[] {
  return items.filter(pred);
}
```
"""),
    _sec("this parameter types", r"""
```typescript
interface Clickable {
  label: string;
  onClick(this: Clickable, e: Event): void;
}
```

Use arrow properties in classes when you need lexical `this` in React handlers.
"""),
    SUPPLEMENT_CH04_EXTRA,
])

SUPPLEMENT_CH05 = "".join([
    _sec("Generic constraints in practice", r"""
```typescript
interface Identifiable { id: string }

function findById<T extends Identifiable>(items: T[], id: string): T | undefined {
  return items.find((item) => item.id === id);
}
```
"""),
    _sec("Generic defaults", r"""
```typescript
interface ApiResponse<T = unknown> {
  data: T;
  status: number;
}

type UserResponse = ApiResponse<User>;
type UnknownResponse = ApiResponse; // T = unknown
```
"""),
    _sec("Generic Stack class", r"""
```typescript
class Stack<T> {
  private items: T[] = [];
  push(item: T): void { this.items.push(item); }
  pop(): T | undefined { return this.items.pop(); }
  peek(): T | undefined { return this.items[this.items.length - 1]; }
}
```
"""),
    _sec("keyof and typeof constraints", r"""
```typescript
function pluck<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = { id: "1", name: "Ada" };
const n = pluck(user, "name"); // string
```
"""),
    _sec("Conditional types preview", r"""
```typescript
type Unwrap<T> = T extends Promise<infer U> ? U : T;
type A = Unwrap<Promise<string>>; // string
```
"""),
])

SUPPLEMENT_CH06 = "".join([
    _sec("DTO patterns with utilities", r"""
```typescript
interface User {
  id: string;
  name: string;
  email: string;
  role: "admin" | "member";
}

type UserCreate = Omit<User, "id">;
type UserUpdate = Partial<Omit<User, "id">>;
type UserPublic = Pick<User, "id" | "name">;
```
"""),
    _sec("Awaited and Promise utilities", r"""
```typescript
type P = Promise<Promise<string>>;
type Flat = Awaited<P>; // string
```
"""),
    _sec("Exclude, Extract, NonNullable", r"""
```typescript
type T = string | number | null | undefined;
type StringsOnly = Extract<T, string>; // string
type NoNull = Exclude<T, null | undefined>; // string | number
type Def = NonNullable<T>; // string | number
```
"""),
    _sec("ConstructorParameters and InstanceType", r"""
```typescript
class User { constructor(public name: string) {} }
type UserParams = ConstructorParameters<typeof User>; // [name: string]
type UserInstance = InstanceType<typeof User>; // User
```
"""),
    _sec("Building a form model", r"""
```typescript
interface FormState {
  email: string;
  password: string;
  remember: boolean;
}

type FormErrors = Partial<Record<keyof FormState, string>>;
type DirtyFields = Partial<Record<keyof FormState, boolean>>;
```
"""),
])

SUPPLEMENT_CH07 = "".join([
    _sec("Access modifiers — visibility", r"""
| Modifier | Class | Subclass | External |
|----------|-------|----------|----------|
| public | yes | yes | yes |
| protected | yes | yes | no |
| private | yes | no | no |
| # private field | yes | no | no |
"""),
    _sec("Abstract class pattern", r"""
```typescript
abstract class Repository<T extends { id: string }> {
  abstract findById(id: string): Promise<T | null>;
  abstract save(entity: T): Promise<void>;
}
```
"""),
    _sec("Parameter properties", r"""
```typescript
class Point {
  constructor(
    public readonly x: number,
    public readonly y: number,
  ) {}
}
```
"""),
    _sec("implements vs extends", r"""
```typescript
interface Serializable {
  toJSON(): object;
}

class User implements Serializable {
  constructor(public name: string) {}
  toJSON() { return { name: this.name }; }
}
```
"""),
    _sec("override keyword", r"""
```typescript
class Animal {
  speak(): string { return "..."; }
}
class Dog extends Animal {
  override speak(): string { return "woof"; }
}
```
"""),
])

SUPPLEMENT_CH08 = "".join([
    _sec("Discriminated union — full example", r"""
```typescript
type Payment =
  | { method: "card"; last4: string }
  | { method: "paypal"; email: string }
  | { method: "cash" };

function charge(p: Payment): number {
  switch (p.method) {
    case "card":
      return 100;
    case "paypal":
      return 100;
    case "cash":
      return 100;
    default:
      const _x: never = p;
      return _x;
  }
}
```
"""),
    _sec("typeof and truthiness narrowing", r"""
```typescript
function print(value: string | number) {
  if (typeof value === "string") {
    console.log(value.toUpperCase());
  } else {
    console.log(value.toFixed(2));
  }
}
```
"""),
    _sec("Type predicates", r"""
```typescript
interface Fish { swim: () => void }
interface Bird { fly: () => void }

function isFish(pet: Fish | Bird): pet is Fish {
  return (pet as Fish).swim !== undefined;
}
```
"""),
    _sec("asserts keyword", r"""
```typescript
function assertIsNumber(value: unknown): asserts value is number {
  if (typeof value !== "number") throw new Error("Not a number");
}
```
"""),
])

SUPPLEMENT_CH09 = "".join([
    _sec("const object vs enum", r"""
```typescript
const Status = {
  Pending: "pending",
  Done: "done",
} as const;

type Status = (typeof Status)[keyof typeof Status];
// "pending" | "done"
```

No runtime enum object unless you need reverse mapping.
"""),
    _sec("Numeric vs string enums", r"""
```typescript
enum Num { A, B, C } // A=0, B=1 — surprises beginners
enum Str { On = "ON", Off = "OFF" } // clearer at runtime
```
"""),
    _sec("satisfies operator", r"""
```typescript
const routes = {
  home: "/",
  about: "/about",
} as const satisfies Record<string, string>;
```
"""),
    _sec("Template literal types", r"""
```typescript
type CSSProperty = "margin" | "padding";
type CSSPropertySide = "top" | "left";
type Name = `${CSSProperty}-${CSSPropertySide}`;
// "margin-top" | "margin-left" | ...
```
"""),
])

SUPPLEMENT_CH10 = "".join([
    _sec("tsconfig strict family", r"""
```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "exactOptionalPropertyTypes": true
  }
}
```
"""),
    _sec("ESM import/export", r"""
```typescript
// math.ts
export function add(a: number, b: number) { return a + b; }
export default function pi() { return 3.14; }

// app.ts
import pi, { add } from "./math.js";
import type { SomeType } from "./types.js";
```
"""),
    _sec("Path aliases", r"""
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": { "@/*": ["src/*"] }
  }
}
```
"""),
    _sec("Ambient declarations", r"""
```typescript
declare module "*.css" {
  const classes: { readonly [key: string]: string };
  export default classes;
}
```
"""),
])

SUPPLEMENT_CH11 = "".join([
    _sec("Result type pattern", r"""
```typescript
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

async function safeFetch(url: string): Promise<Result<string>> {
  try {
    const res = await fetch(url);
    if (!res.ok) return { ok: false, error: new Error(String(res.status)) };
    return { ok: true, value: await res.text() };
  } catch (e) {
    return { ok: false, error: e instanceof Error ? e : new Error(String(e)) };
  }
}
```
"""),
    _sec("Promise.all typing", r"""
```typescript
const [user, posts] = await Promise.all([
  fetchUser("1"),
  fetchPosts("1"),
] as const);
```
"""),
    _sec("Async generators", r"""
```typescript
async function* streamLines(file: string): AsyncGenerator<string> {
  // yield lines
}
```
"""),
    _sec("AbortController with fetch", r"""
```typescript
async function fetchWithTimeout(url: string, ms: number): Promise<Response> {
  const ctrl = new AbortController();
  const id = setTimeout(() => ctrl.abort(), ms);
  try {
    return await fetch(url, { signal: ctrl.signal });
  } finally {
    clearTimeout(id);
  }
}
```
"""),
])

SUPPLEMENT_CH12 = "".join([
    _sec("Typing form events", r"""
```typescript
import { ChangeEvent, FormEvent } from "react";

function SignupForm() {
  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    console.log(e.target.name, e.target.value);
  };
  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
  };
  return <form onSubmit={handleSubmit}>...</form>;
}
```
"""),
    _sec("useState and useReducer", r"""
```typescript
const [count, setCount] = useState(0);
const [user, setUser] = useState<User | null>(null);

type Action = { type: "inc" } | { type: "add"; n: number };
function reducer(state: number, action: Action): number {
  switch (action.type) {
    case "inc": return state + 1;
    case "add": return state + action.n;
  }
}
```
"""),
    _sec("Generic list component", r"""
```typescript
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
  return <ul>{items.map((item) => <li key={String(item)}>{renderItem(item)}</li>)}</ul>;
}
```
"""),
    _sec("forwardRef", r"""
```typescript
const Input = forwardRef<HTMLInputElement, InputProps>(function Input(props, ref) {
  return <input ref={ref} {...props} />;
});
```
"""),
])

SUPPLEMENT_CH13 = "".join([
    _sec("Branded types", r"""
```typescript
type UserId = string & { readonly __brand: unique symbol };
type OrderId = string & { readonly __brand: unique symbol };

function userId(id: string): UserId {
  return id as UserId;
}
```
"""),
    _sec("Strict compiler flags explained", r"""
| Flag | Effect |
|------|--------|
| `strictNullChecks` | null/undefined not assignable unless in union |
| `noImplicitAny` | Error on implicit any |
| `strictFunctionTypes` | Safer function parameter checking |
| `noUncheckedIndexedAccess` | Indexing may return undefined |
"""),
    _sec("ESLint TypeScript rules", r"""
- `@typescript-eslint/no-explicit-any`
- `@typescript-eslint/consistent-type-imports`
- `@typescript-eslint/no-floating-promises`
"""),
    _sec("Code review checklist", r"""
1. No new `any` without comment
2. External data validated
3. Public exports typed
4. Unions exhaustive in switch
5. No `@ts-ignore` without ticket link
"""),
])

SUPPLEMENT_CH01 = "".join([
    _sec("TypeScript playground — quick experiments", r"""
Open [TypeScript Playground](https://www.typescriptlang.org/play) to try types without a local project.

```typescript
// Shareable links document compiler options
const answer = (a: number, b: number) => a + b;
```

Use **TS → JS** panel to see emitted code and confirm type erasure.
"""),
    _sec("Editor setup — VS Code / Cursor", r"""
| Setting | Recommendation |
|---------|----------------|
| Use workspace TypeScript | "Use Workspace Version" when prompted |
| Format on save | Prettier + ESLint |
| Inlay hints | Enable parameter names for learning |

```json
// .vscode/settings.json (team)
{
  "typescript.tsdk": "node_modules/typescript/lib",
  "editor.formatOnSave": true
}
```
"""),
    _sec("package.json scripts", r"""
```json
{
  "scripts": {
    "build": "tsc",
    "typecheck": "tsc --noEmit",
    "watch": "tsc --watch",
    "start": "node dist/index.js"
  }
}
```

Run `npm run typecheck` in CI on every pull request.
"""),
    _sec("Common compiler error codes", r"""
| Code | Meaning | Fix |
|------|---------|-----|
| TS2322 | Type not assignable | Match expected type or narrow |
| TS2345 | Bad argument | Check parameter types |
| TS2339 | Property missing | Fix name or extend interface |
| TS2532 | Possibly undefined | Add guard or `?.` |
| TS7006 | Implicit any | Add type annotation |
"""),
])

SUPPLEMENTS: dict[str, str] = {
    "ch01-introduction.md": SUPPLEMENT_CH01,
    "ch02-types-and-primitives.md": SUPPLEMENT_CH02,
    "ch03-interfaces-and-type-aliases.md": SUPPLEMENT_CH03,
    "ch04-functions.md": SUPPLEMENT_CH04,
    "ch05-generics.md": SUPPLEMENT_CH05,
    "ch06-utility-types.md": SUPPLEMENT_CH06,
    "ch07-classes-and-oop.md": SUPPLEMENT_CH07,
    "ch08-type-narrowing.md": SUPPLEMENT_CH08,
    "ch09-enums-and-literals.md": SUPPLEMENT_CH09,
    "ch10-modules-and-config.md": SUPPLEMENT_CH10,
    "ch11-async-typescript.md": SUPPLEMENT_CH11,
    "ch12-react-with-typescript.md": SUPPLEMENT_CH12,
    "ch13-best-practices.md": SUPPLEMENT_CH13,
}
