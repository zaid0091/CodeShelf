"""Supplemental interview Q&A content for chapter 14."""

CH14_QA = """
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

"""
