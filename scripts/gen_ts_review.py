"""Chapter review Q&A blocks to reach 800+ lines without repetitive filler."""

from gen_ts_supplements_all import _sec


def _block(sections: list[tuple[str, str]]) -> str:
    return "".join(_sec(t, b) for t, b in sections)


REVIEW: dict[str, str] = {
    "ch04-functions.md": _block([
        ("Review Q1 — optional parameters", "**Q:** Can optional parameters come before required ones? **A:** No — required parameters must come first."),
        ("Review Q2 — return type", "**Q:** When should you annotate return types on exported functions? **A:** When the API is public or inference might widen unexpectedly."),
    ]),
    "ch05-generics.md": _block([
        ("Review Q1", "**Q:** Can you use `any` as a generic constraint? **A:** Technically yes, but it defeats the purpose — use `extends unknown` or a meaningful interface."),
        ("Review Q2", "**Q:** What is `T extends keyof U` used for? **A:** Safe property access — `getProperty(obj, key)` patterns."),
        ("Review Q3", "**Q:** Do generics exist at runtime? **A:** No — they are erased like all types."),
        ("Review Q4", "**Q:** What is a default type parameter? **A:** `interface Box<T = string>` uses `string` when `T` is not specified."),
        ("Scenario — typed event bus", r"""
```typescript
type Events = {
  login: { userId: string };
  logout: { userId: string };
  error: { message: string };
};

class TypedEmitter {
  private listeners: { [K in keyof Events]?: Array<(p: Events[K]) => void> } = {};

  on<K extends keyof Events>(event: K, fn: (payload: Events[K]) => void) {
    (this.listeners[event] ??= []).push(fn);
  }

  emit<K extends keyof Events>(event: K, payload: Events[K]) {
    this.listeners[event]?.forEach((fn) => fn(payload));
  }
}
```
"""),
    ]),
    "ch06-utility-types.md": _block([
        ("Review Q1", "**Q:** What is the difference between `Partial` and `?` on each field? **A:** `Partial` transforms an existing type; manual `?` duplicates structure."),
        ("Review Q2", "**Q:** Can you `Pick` from a union? **A:** Utilities distribute over unions in many cases — test complex types in the playground."),
        ("Review Q3", "**Q:** What does `Readonly` do to nested objects? **A:** Shallow only — nested objects remain mutable unless you use a deep mapped type."),
        ("Scenario — API DTO layers", r"""
```typescript
interface User {
  id: string;
  email: string;
  passwordHash: string;
  role: "admin" | "member";
}

type UserCreate = Omit<User, "id" | "passwordHash"> & { password: string };
type UserPublic = Pick<User, "id" | "email">;
type UserAdminView = Omit<User, "passwordHash">;
```

Each layer exposes only what that layer needs.
"""),
        ("Scenario — form state types", r"""
```typescript
interface SignupForm {
  email: string;
  password: string;
  agree: boolean;
}

type SignupErrors = Partial<Record<keyof SignupForm, string>>;
type DirtyFields = Partial<Record<keyof SignupForm, boolean>>;

function validate(form: SignupForm): SignupErrors {
  const errors: SignupErrors = {};
  if (!form.email.includes("@")) errors.email = "Invalid email";
  if (form.password.length < 8) errors.password = "Too short";
  if (!form.agree) errors.agree = "Required";
  return errors;
}
```
"""),
    ]),
    "ch07-classes-and-oop.md": _block([
        ("Review Q1", "**Q:** `private` vs `#private`? **A:** `private` is compile-time only; `#` is true runtime privacy."),
        ("Review Q2", "**Q:** When use `abstract`? **A:** When subclasses must implement specific methods but you share base logic."),
        ("Scenario — domain model", r"""
```typescript
abstract class Entity {
  constructor(public readonly id: string) {}
  abstract validate(): string[];
}

class Order extends Entity {
  constructor(
    id: string,
    public readonly totalCents: number,
    public readonly lines: { sku: string; qty: number }[],
  ) {
    super(id);
  }

  validate() {
    const errors: string[] = [];
    if (this.totalCents < 0) errors.push("Negative total");
    if (this.lines.length === 0) errors.push("Empty order");
    return errors;
  }
}
```
"""),
    ]),
    "ch08-type-narrowing.md": _block([
        ("Review Q1", "**Q:** Does `Array.isArray` narrow? **A:** Yes — narrows to `any[]` in older TS; prefer `Array.isArray` + generic guards for typed arrays."),
        ("Review Q2", "**Q:** What is exhaustiveness checking? **A:** Assigning the union to `never` in `default` when all cases handled."),
        ("Scenario — payment union", r"""
```typescript
type Payment =
  | { kind: "card"; last4: string }
  | { kind: "paypal"; email: string }
  | { kind: "invoice"; poNumber: string };

function describe(p: Payment): string {
  switch (p.kind) {
    case "card": return `Card ending ${p.last4}`;
    case "paypal": return `PayPal ${p.email}`;
    case "invoice": return `PO ${p.poNumber}`;
    default:
      return assertNever(p);
  }
}

function assertNever(x: never): never {
  throw new Error(`Unhandled: ${JSON.stringify(x)}`);
}
```
"""),
    ]),
    "ch09-enums-and-literals.md": _block([
        ("Review Q1", "**Q:** Why avoid numeric enums in libraries? **A:** They emit JS objects and can break tree-shaking; unions have zero cost."),
        ("Review Q2", "**Q:** What does `as const` on an array do? **A:** Makes it `readonly` tuple of literal types."),
        ("Review Q3", "**Q:** `satisfies` vs type annotation? **A:** `satisfies` checks shape without widening literals."),
        ("Review Q4", "**Q:** Template literal types use case? **A:** CSS keys, event names, route builders."),
        ("Scenario — theme system", r"""
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
"""),
        ("Scenario — route builder types", r"""
```typescript
type Locale = "en" | "fr";
type Page = "home" | "about" | "contact";
type LocalizedPath = `/${Locale}/${Page}`;

const paths = {
  enHome: "/en/home",
  frAbout: "/fr/about",
} as const satisfies Record<string, LocalizedPath>;
```
"""),
        ("Scenario — discriminant with switch", r"""
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
"""),
    ]),
    "ch10-modules-and-config.md": _block([
        ("Review Q1", "**Q:** Why `.js` in import paths with NodeNext? **A:** Node ESM resolves the emitted file extension at runtime."),
        ("Review Q2", "**Q:** What is `skipLibCheck`? **A:** Skips type-checking of declaration files — faster builds, fewer third-party errors."),
        ("Review Q3", "**Q:** `isolatedModules`? **A:** Ensures each file can transpile alone — required by Babel/esbuild."),
        ("Scenario — library package", r"""
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "NodeNext",
    "declaration": true,
    "declarationMap": true,
    "outDir": "dist",
    "rootDir": "src",
    "strict": true
  },
  "include": ["src"]
}
```

Publish only `dist/` — consumers import types from `.d.ts` files.
"""),
        ("Scenario — ambient shims", r"""
```typescript
// global.d.ts
declare const __APP_VERSION__: string;

// vite.config defines __APP_VERSION__ at build time
```
"""),
    ]),
    "ch11-async-typescript.md": _block([
        ("Review Q1", "**Q:** Type of `async function f(): number`? **A:** Returns `Promise<number>`, not `number`."),
        ("Review Q2", "**Q:** `Promise<void>` meaning? **A:** Promise that resolves with no useful value."),
        ("Review Q3", "**Q:** Should every `fetch` response be typed? **A:** Parse as `unknown`, then validate before treating as domain type."),
        ("Scenario — parallel fetch", r"""
```typescript
interface User { id: string; name: string }
interface Post { id: string; title: string }

async function loadDashboard(userId: string) {
  const [user, posts] = await Promise.all([
    fetch(`/api/users/${userId}`).then((r) => r.json() as Promise<User>),
    fetch(`/api/users/${userId}/posts`).then((r) => r.json() as Promise<Post[]>),
  ]);
  return { user, posts };
}
```

In production, validate both JSON payloads before use.
"""),
        ("Scenario — retry with Result", r"""
```typescript
type Result<T> = { ok: true; value: T } | { ok: false; error: Error };

async function retry<T>(fn: () => Promise<T>, times: number): Promise<Result<T>> {
  let last: Error = new Error("unknown");
  for (let i = 0; i < times; i++) {
    try {
      return { ok: true, value: await fn() };
    } catch (e) {
      last = e instanceof Error ? e : new Error(String(e));
    }
  }
  return { ok: false, error: last };
}
```
"""),
    ]),
    "ch13-best-practices.md": _block([
        ("Review Q1", "**Q:** First strict flag to enable on legacy code? **A:** Often `strictNullChecks` — highest bug prevention per effort."),
        ("Review Q2", "**Q:** When is `any` acceptable? **A:** Rarely — migration shims with a ticket and deadline to remove."),
        ("Review Q3", "**Q:** Types vs runtime validation? **A:** Types compile away; validate JSON at boundaries."),
        ("Strict family — expanded", r"""
| Flag | What it catches |
|------|-----------------|
| `strictNullChecks` | null/undefined misuse |
| `noImplicitAny` | missing annotations |
| `strictFunctionTypes` | unsafe function assignability |
| `noUncheckedIndexedAccess` | `arr[i]` may be undefined |
| `exactOptionalPropertyTypes` | `undefined` vs missing key |

Enable one per PR on legacy repos.
"""),
        ("Scenario — PR type checklist", r"""
Before merging TypeScript PRs, verify:

1. `npm run typecheck` passes in CI
2. No new `any` without linked issue
3. External API responses validated
4. Exported public APIs documented
5. Union switches have `never` exhaustiveness
6. Tests cover runtime paths types cannot guard
"""),
        ("Scenario — shared types package", r"""
Publish `packages/types` in a monorepo so web and API share `User`, `Order`, and API DTOs — one source of truth prevents client/server drift.
"""),
        ("Review Q4 — documentation", "**Q:** Should you document every type? **A:** Document exported public APIs and non-obvious business types; let obvious inference speak for itself."),
    ]),
    "ch14-interview-prep.md": _block([
        ("Review Q1", "**Q:** How to answer 'Is TypeScript worth it?' **A:** Trade-off: upfront cost vs fewer bugs, better refactors, IDE support — cite team size and codebase age."),
    ]),
}


def get_review(filename: str) -> str:
    return REVIEW.get(filename, "")
