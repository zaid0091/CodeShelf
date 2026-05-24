"""Full exercise solutions for TypeScript chapters 1–14."""

# Each chapter: list of solution markdown strings (one per exercise)

CH01_SOLUTIONS = [
    """```typescript
// src/index.ts
interface Product {
  name: string;
  price: number;
}

function formatPrice(product: Product): string {
  return `${product.name}: $${product.price.toFixed(2)}`;
}

const item: Product = { name: "Notebook", price: 12.5 };
console.log(formatPrice(item));
```

```json
// tsconfig.json (key fields)
{
  "compilerOptions": {
    "strict": true,
    "rootDir": "./src",
    "outDir": "./dist"
  },
  "include": ["src/**/*"]
}
```

Run: `npx tsc && node dist/index.js`""",
    """```javascript
// add.js
function add(a, b) { return a + b; }
console.log(add(1, "2")); // "12" (string concat)
```

```typescript
// add.ts
function add(a: number, b: number): number {
  return a + b;
}
// add(1, "2"); // TS2345: Argument of type 'string' is not assignable to parameter of type 'number'
```""",
    """```typescript
const items = [1, 2, 3]; // inferred: number[]
let label = "active"; // inferred: string (widened)

// Literal preserved with const assertion context:
const status = "active" as const; // "active"

let explicit: string = "active";
```""",
    """```typescript
interface Book {
  title: string;
  pages: number;
}

function printBook(book: Book): void {
  console.log(`${book.title} (${book.pages} pages)`);
}

// Fix: add missing pages
printBook({ title: "TypeScript Handbook", pages: 600 });
```""",
    """```bash
# Terminal 1
npx tsc --watch

# Terminal 2 (after compile)
node dist/index.js
```""",
    """```typescript
function greet(name?: string): void {
  // console.log(name.length); // Error: 'name' is possibly 'undefined'
  console.log(name?.length ?? 0);
}
```""",
]

CH02_SOLUTIONS = [
    """```typescript
const username: string = "ada";
const score: number = 98;
const isPremium: boolean = true;
```""",
    """```typescript
const product: readonly [string, number] = ["Keyboard", 79.99];
// product[1] = 50; // compile error
```""",
    """```typescript
function parseJson(s: string): unknown {
  return JSON.parse(s);
}

function getName(data: unknown): string {
  if (typeof data === "object" && data !== null && "name" in data) {
    const name = (data as { name: unknown }).name;
    if (typeof name === "string") return name;
  }
  return "Unknown";
}
```""",
    """```typescript
type Theme = "light" | "dark" | "system";

function icon(theme: Theme): string {
  switch (theme) {
    case "light": return "☀️";
    case "dark": return "🌙";
    case "system": return "💻";
    default:
      const _exhaustive: never = theme;
      return _exhaustive;
  }
}
// Add "system" to union and default branch — compiler forces update
```""",
    """```typescript
function formatValue(value: string | number): string {
  if (typeof value === "string") return value;
  return value.toFixed(2);
}
```""",
    """```typescript
function formatPhone(phone: string | undefined): string {
  return phone ?? "N/A";
}
```""",
]

CH03_SOLUTIONS = [
    """```typescript
interface Product {
  id: string;
  name: string;
  price: number;
}

interface DigitalProduct extends Product {
  downloadUrl: string;
  fileSizeMb: number;
}
```""",
    """```typescript
interface HasTimestamps {
  createdAt: Date;
  updatedAt: Date;
}

interface HasSoftDelete {
  deletedAt: Date | null;
}

type AuditableEntity = HasTimestamps & HasSoftDelete & { id: string };
```""",
    """```typescript
interface Point { x: number; y: number }

const extra = { x: 1, y: 2, label: "origin" };
function draw(p: Point) { console.log(p.x, p.y); }
draw(extra); // OK via variable

// draw({ x: 1, y: 2, label: "a" }); // excess property error on literal
```""",
    """```typescript
type ApiResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };
```""",
    """```typescript
type ProductSummary = Pick<Product, "id" | "name" | "price">;
```""",
    """```typescript
interface ApiModel {
  readonly createdAt: string;
  name: string;
}
```""",
]

CH04_SOLUTIONS = [
    """```typescript
function format(value: number): string;
function format(value: boolean): string;
function format(value: number | boolean): string {
  return String(value);
}
```""",
    """```typescript
function sum(...nums: number[]): number {
  return nums.reduce((a, b) => a + b, 0);
}
```""",
    """```typescript
function filterItems<T>(items: T[], pred: (item: T) => boolean): T[] {
  return items.filter(pred);
}
```""",
    """```typescript
interface User { id: string; name: string }

async function loadUser(id: string): Promise<User> {
  const res = await fetch(`/api/users/${id}`);
  return res.json() as User; // production: validate
}
```""",
    """```typescript
class Counter {
  count = 0;
  increment = () => { this.count += 1; }; // lexical this
}
```""",
    """```typescript
export function parseId(raw: string): number | null {
  const n = Number(raw);
  return Number.isNaN(n) ? null : n;
}
```""",
]

CH05_SOLUTIONS = [
    """```typescript
function identity<T>(value: T): T {
  return value;
}
```""",
    """```typescript
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
```""",
    """```typescript
class Stack<T> {
  private items: T[] = [];
  push(item: T) { this.items.push(item); }
  pop(): T | undefined { return this.items.pop(); }
}
```""",
    """```typescript
interface ApiResponse<T = unknown> {
  data: T;
  status: number;
}
```""",
    """```typescript
function memoize<A extends unknown[], R>(fn: (...args: A) => R): (...args: A) => R {
  const cache = new Map<string, R>();
  return (...args: A) => {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key)!;
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}
```""",
    """```typescript
function merge<T extends object, U extends object>(a: T, b: U): T & U {
  return { ...a, ...b };
}
```""",
]

CH06_SOLUTIONS = [
    """```typescript
type UserUpdate = Partial<Omit<User, "id">>;
```""",
    """```typescript
type Role = "admin" | "member" | "guest";
type Permissions = Record<Role, string[]>;
```""",
    """```typescript
type P = Promise<Promise<string>>;
type Flat = Awaited<P>; // string
```""",
    """```typescript
type ProductSummary = Pick<Product, "id" | "name" | "price">;
```""",
    """```typescript
type Optional<T> = { [K in keyof T]?: T[K] };
```""",
    """```typescript
function withLog<T extends (...args: never[]) => unknown>(fn: T): T {
  return ((...args: Parameters<T>) => {
    const result = fn(...args);
    console.log("called", fn.name);
    return result;
  }) as T;
}
```""",
]

CH07_SOLUTIONS = [
    """```typescript
class User {
  constructor(public name: string) {}
  greet() { return `Hi, ${this.name}`; }
}
```""",
    """```typescript
abstract class Repository<T extends { id: string }> {
  abstract findById(id: string): Promise<T | null>;
  abstract save(entity: T): Promise<void>;
}
```""",
    """```typescript
interface Logger { log(msg: string): void }
class ConsoleLogger implements Logger {
  log(msg: string) { console.log(msg); }
}
```""",
    """```typescript
class Animal { speak() { return "..."; } }
class Dog extends Animal {
  override speak() { return "woof"; }
}
```""",
    """```typescript
class MathUtils {
  static clamp(n: number, min: number, max: number) {
    return Math.min(max, Math.max(min, n));
  }
}
```""",
    """```typescript
class Queue<T> {
  private items: T[] = [];
  enqueue(item: T) { this.items.push(item); }
  dequeue(): T | undefined { return this.items.shift(); }
}
```""",
]

CH08_SOLUTIONS = [
    """```typescript
function pad(value: string | number, len: number): string {
  const s = typeof value === "string" ? value : String(value);
  return s.padStart(len, "0");
}
```""",
    """```typescript
type ApiResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };

function handle<T>(r: ApiResult<T>): T {
  if (!r.ok) throw new Error(r.error);
  return r.data;
}
```""",
    """```typescript
interface User { id: string; name: string }
function isUser(x: unknown): x is User {
  return typeof x === "object" && x !== null && "id" in x && "name" in x;
}
```""",
    """```typescript
function assertNever(x: never): never {
  throw new Error(`Unexpected: ${JSON.stringify(x)}`);
}
```""",
    """```typescript
function isString(x: unknown): x is string {
  return typeof x === "string";
}
const words = ["a", 1, "b"].filter(isString); // string[]
```""",
    """```typescript
interface Fish { swim(): void }
interface Bird { fly(): void }
function move(pet: Fish | Bird) {
  if ("swim" in pet) pet.swim();
  else pet.fly();
}
```""",
]

CH09_SOLUTIONS = [
    """```typescript
type Theme = "light" | "dark";
function themeIcon(t: Theme) {
  switch (t) {
    case "light": return "☀️";
    case "dark": return "🌙";
  }
}
```""",
    """```typescript
const routes = {
  home: "/",
  about: "/about",
} as const satisfies Record<string, string>;
```""",
    """```typescript
enum OrderStatus { Pending = "PENDING", Shipped = "SHIPPED" }
```""",
    """```typescript
type HttpStatus = 200 | 404 | 500;
```""",
    """```typescript
type EventName = "click" | "focus";
type Handler = `on${Capitalize<EventName>}`;
```""",
    """```typescript
const Status = { Idle: 0, Running: 1 } as const;
type Status = (typeof Status)[keyof typeof Status];
```""",
]

CH10_SOLUTIONS = [
    """```typescript
// utils.ts
export function clamp(n: number, min: number, max: number) { return Math.min(max, Math.max(min, n)); }
// app.ts
import { clamp } from "./utils.js";
```""",
    """```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": { "@/*": ["src/*"] }
  }
}
```""",
    """```typescript
declare module "*.css" {
  const classes: { readonly [key: string]: string };
  export default classes;
}
```""",
    """```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true
  }
}
```""",
    """```typescript
import type { User } from "./models.js";
```""",
    """```json
{
  "compilerOptions": {
    "moduleResolution": "bundler",
    "module": "ESNext"
  }
}
```""",
]

CH11_SOLUTIONS = [
    """```typescript
function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
```""",
    """```typescript
type Result<T> = { ok: true; value: T } | { ok: false; error: Error };
```""",
    """```typescript
function isUser(raw: unknown): raw is { id: string; name: string } {
  return typeof raw === "object" && raw !== null && "id" in raw && "name" in raw;
}
```""",
    """```typescript
const [user, posts] = await Promise.all([fetchUser("1"), fetchPosts("1")]);
```""",
    """```typescript
class HttpError extends Error {
  constructor(public status: number, message: string) {
    super(message);
  }
}
```""",
    """```typescript
async function fetchWithTimeout(url: string, ms: number) {
  const ctrl = new AbortController();
  const id = setTimeout(() => ctrl.abort(), ms);
  try {
    return await fetch(url, { signal: ctrl.signal });
  } finally {
    clearTimeout(id);
  }
}
```""",
]

CH12_SOLUTIONS = [
    """```typescript
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary";
}
```""",
    """```typescript
function Input({ value, onChange }: {
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}) {
  return <input value={value} onChange={onChange} />;
}
```""",
    """```typescript
type Action = { type: "inc" } | { type: "add"; n: number };
function reducer(state: number, action: Action): number {
  switch (action.type) {
    case "inc": return state + 1;
    case "add": return state + action.n;
  }
}
```""",
    """```typescript
const Ctx = createContext<User | null>(null);
function useUser() {
  const u = useContext(Ctx);
  if (!u) throw new Error("No user");
  return u;
}
```""",
    """```typescript
function List<T>({ items, render }: { items: T[]; render: (item: T) => React.ReactNode }) {
  return <ul>{items.map((item, i) => <li key={i}>{render(item)}</li>)}</ul>;
}
```""",
    """```typescript
const Input = forwardRef<HTMLInputElement, React.InputHTMLAttributes<HTMLInputElement>>(
  (props, ref) => <input ref={ref} {...props} />
);
```""",
]

CH13_SOLUTIONS = [
    """Enable `noUncheckedIndexedAccess`, `noImplicitOverride`, and `exactOptionalPropertyTypes` in tsconfig.""",
    """```typescript
type UserId = string & { readonly __brand: unique symbol };
function toUserId(id: string): UserId { return id as UserId; }
```""",
    """Add to ESLint: `@typescript-eslint/no-explicit-any`: error""",
    """```typescript
type UserUpdate = Partial<Omit<User, "id">>;
```""",
    """Checklist: no new `any`, validate API JSON, exhaustive switches, no `@ts-ignore` without ticket, export types on public API, etc.""",
    """```typescript
/**
 * Formats a price in USD.
 * @param cents - Amount in cents (integer)
 */
export function formatUsd(cents: number): string {
  return `$${(cents / 100).toFixed(2)}`;
}
```""",
]

CH14_SOLUTIONS = [
    "Create 20 flashcards from Q&A sections; review daily with spaced repetition.",
    "Pair with a friend: alternate asking and answering for 45 minutes without notes.",
    """```typescript
type DeepPartial<T> = {
  [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K];
};
```""",
    "Sketch `get<T>(path, parser)` returning `ApiResult<T>` with unknown JSON and runtime parse function.",
    "Narrate each branch: typeof, discriminant check, default never.",
    "List: strictNullChecks, noImplicitAny, strictFunctionTypes, strictBindCallApply, strictPropertyInitialization, noImplicitThis, alwaysStrict.",
]

SOLUTIONS_BY_ORDER: dict[int, list[str]] = {
    1: CH01_SOLUTIONS,
    2: CH02_SOLUTIONS,
    3: CH03_SOLUTIONS,
    4: CH04_SOLUTIONS,
    5: CH05_SOLUTIONS,
    6: CH06_SOLUTIONS,
    7: CH07_SOLUTIONS,
    8: CH08_SOLUTIONS,
    9: CH09_SOLUTIONS,
    10: CH10_SOLUTIONS,
    11: CH11_SOLUTIONS,
    12: CH12_SOLUTIONS,
    13: CH13_SOLUTIONS,
    14: CH14_SOLUTIONS,
}


def get_solutions(order: int) -> list[str]:
    return SOLUTIONS_BY_ORDER.get(order, [])
