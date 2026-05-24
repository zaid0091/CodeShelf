---
title: Chapter 12 — React with TypeScript
description: Component props, children, events, hooks, refs, context, and generic components.
order: 12
tags: [typescript, react, hooks, components, jsx]
---


# Chapter 12: React with TypeScript

> **React and TypeScript together catch UI bugs early. This chapter types props, events, hooks, and advanced component patterns.**
> Take your time with each section. TypeScript rewards patience — read compiler errors carefully and experiment in a small project as you go.

---


## Table of Contents

1. [Why TS + React](#why-ts-react)
2. [Component Props](#component-props)
3. [children](#children)
4. [Events](#events)
5. [useState](#usestate)
6. [useReducer](#usereducer)
7. [useRef](#useref)
8. [Context](#context)
9. [Generic Lists](#generic-lists)
10. [forwardRef](#forwardref)
11. [ComponentProps](#componentprops)
12. [Best Practices](#best-practices)
13. [Interview Points](#interview-points)
14. [Exercises](#exercises)
15. [Chapter Summary](#chapter-summary)

---

## 12.1 Why TypeScript + React

React apps benefit from typed props, state, and context — especially as component count grows.

```typescript
interface GreetingProps {
  name: string;
  excited?: boolean;
}

function Greeting({ name, excited = false }: GreetingProps) {
  return <h1>Hello, {name}{excited ? "!" : "."}</h1>;
}
```

> **Definition:** **React with TypeScript** uses `.tsx` files where JSX is typed against React's element and component definitions from `@types/react`.

## 12.2 Setup

```bash
npm create vite@latest my-app -- --template react-ts
cd my-app
npm install
```

| Package | Role |
|---------|------|
| `react`, `react-dom` | Runtime |
| `typescript` | Compiler |
| `@types/react`, `@types/react-dom` | JSX and component types |

Typical Vite `tsconfig.json` fragment:

```json
{
  "compilerOptions": {
    "jsx": "react-jsx",
    "strict": true,
    "moduleResolution": "bundler",
    "noEmit": true
  }
}
```

## 12.3 Typing component props

### Function components

```typescript
type ButtonProps = {
  label: string;
  onClick: () => void;
  disabled?: boolean;
  variant?: "primary" | "secondary";
};

export function Button({
  label,
  onClick,
  disabled = false,
  variant = "primary",
}: ButtonProps) {
  return (
    <button
      type="button"
      className={`btn btn-${variant}`}
      disabled={disabled}
      onClick={onClick}
    >
      {label}
    </button>
  );
}
```

### React.FC — use sparingly

```typescript
// Older pattern — optional; explicit props type is preferred today
const OldStyle: React.FC<{ title: string }> = ({ title, children }) => (
  <div>{title}{children}</div>
);
```

`React.FC` implicitly included `children` and `displayName`; modern code favors plain functions with explicit `children?: React.ReactNode` when needed.

### Extending native element props

```typescript
type InputProps = React.InputHTMLAttributes<HTMLInputElement> & {
  label: string;
  error?: string;
};

function Input({ label, error, id, ...rest }: InputProps) {
  const inputId = id ?? rest.name;
  return (
    <div>
      <label htmlFor={inputId}>{label}</label>
      <input id={inputId} {...rest} />
      {error && <span role="alert">{error}</span>}
    </div>
  );
}
```

Use `ComponentPropsWithoutRef<"button">` or `ComponentProps<typeof Link>` for wrapper components.

## 12.4 Children typing

```typescript
type CardProps = {
  title: string;
  children: React.ReactNode;
};

function Card({ title, children }: CardProps) {
  return (
    <section>
      <h2>{title}</h2>
      {children}
    </section>
  );
}
```

| Type | Use when |
|------|----------|
| `React.ReactNode` | Any renderable content |
| `React.ReactElement` | Single element required |
| `React.ReactChild` | Legacy; prefer ReactNode |
| Render prop | `(data: T) => React.ReactNode` |

```typescript
type ListProps<T> = {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
};

function List<T>({ items, renderItem }: ListProps<T>) {
  return <ul>{items.map((item) => <li key={String(item)}>{renderItem(item)}</li>)}</ul>;
}
```

## 12.5 Event handlers

```typescript
function SearchForm() {
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log(e.target.value);
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="search" onChange={handleChange} />
    </form>
  );
}
```

Common event types:

| Event | Type |
|-------|------|
| Click | `React.MouseEvent<HTMLButtonElement>` |
| Change | `React.ChangeEvent<HTMLInputElement>` |
| Form | `React.FormEvent<HTMLFormElement>` |
| Keyboard | `React.KeyboardEvent<HTMLElement>` |

## 12.6 useState

```typescript
const [count, setCount] = useState(0); // number
const [user, setUser] = useState<User | null>(null);

// Explicit when initial value doesn't carry type
const [items, setItems] = useState<string[]>([]);

// Lazy init
const [state] = useState(() => expensiveInit());
```

### Functional updates

```typescript
setCount((prev) => prev + 1);
```

## 12.7 useReducer

```typescript
type State = { count: number };
type Action =
  | { type: "increment" }
  | { type: "decrement" }
  | { type: "reset"; value: number };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case "increment":
      return { count: state.count + 1 };
    case "decrement":
      return { count: state.count - 1 };
    case "reset":
      return { count: action.value };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });
  return (
    <button type="button" onClick={() => dispatch({ type: "increment" })}>
      {state.count}
    </button>
  );
}
```

## 12.8 useRef

```typescript
const inputRef = useRef<HTMLInputElement>(null);

useEffect(() => {
  inputRef.current?.focus();
}, []);

// Mutable ref (not DOM)
const countRef = useRef(0);
countRef.current += 1;
```

## 12.9 useContext

```typescript
type Theme = "light" | "dark";

type ThemeContextValue = {
  theme: Theme;
  setTheme: (t: Theme) => void;
};

const ThemeContext = createContext<ThemeContextValue | undefined>(undefined);

function useTheme() {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error("useTheme must be used within ThemeProvider");
  return ctx;
}
```

Pattern: custom hook + undefined default forces provider check.

## 12.10 Generic components

```typescript
type SelectProps<T extends string> = {
  value: T;
  options: T[];
  onChange: (value: T) => void;
};

function Select<T extends string>({ value, options, onChange }: SelectProps<T>) {
  return (
    <select value={value} onChange={(e) => onChange(e.target.value as T)}>
      {options.map((opt) => (
        <option key={opt} value={opt}>{opt}</option>
      ))}
    </select>
  );
}
```

## 12.11 forwardRef

```typescript
type ButtonProps = React.ComponentPropsWithoutRef<"button">;

const FancyButton = forwardRef<HTMLButtonElement, ButtonProps>(
  function FancyButton(props, ref) {
    return <button ref={ref} {...props} />;
  }
);
```

React 19+ may allow `ref` as a regular prop — check your React version docs.

## 12.12 Third-party component props

```typescript
import type { ComponentProps } from "react";
import { Link } from "react-router-dom";

type AppLinkProps = ComponentProps<typeof Link> & {
  external?: boolean;
};
```

## 12.13 Common patterns

### Discriminated props

```typescript
type ModalProps =
  | { open: false }
  | { open: true; title: string; onClose: () => void };

function Modal(props: ModalProps) {
  if (!props.open) return null;
  return (
    <dialog open>
      <h2>{props.title}</h2>
      <button type="button" onClick={props.onClose}>Close</button>
    </dialog>
  );
}
```

### Polymorphic components (sketch)

```typescript
type BoxProps<C extends React.ElementType = "div"> = {
  as?: C;
  children: React.ReactNode;
} & React.ComponentPropsWithoutRef<C>;

function Box<C extends React.ElementType = "div">({
  as,
  children,
  ...rest
}: BoxProps<C>) {
  const Component = as ?? "div";
  return <Component {...rest}>{children}</Component>;
}
```

## 12.14 Pitfalls

| Pitfall | Fix |
|---------|-----|
| `any` props | Define interface |
| Wrong event element type | Match handler to element |
| Optional context | Custom hook with guard |
| Inline object props causing rerenders | memo + stable types (separate concern) |
| Importing type as value | `import type` |

> **Key takeaway:** Type props with interfaces, use React's event generics, narrow context with custom hooks, and extend native HTML attribute types when wrapping elements.
<!-- codeshelf:generated-appendix -->

---

## Props — extending HTML elements

```typescript
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "ghost";
}

function Button({ variant = "primary", children, ...rest }: ButtonProps) {
  return <button className={variant} {...rest}>{children}</button>;
}
```

`...rest` forwards `onClick`, `disabled`, `type`, etc. with correct types.

---

## Hooks — typing patterns

| Hook | Pattern |
|------|---------|
| `useState` | `useState<User | null>(null)` |
| `useRef` | `useRef<HTMLInputElement>(null)` |
| `useReducer` | Discriminated union for actions |
| `useContext` | `createContext<T | undefined>` + guard hook |

---

## Typing form events


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


---

## useState and useReducer


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


---

## Generic list component


```typescript
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
  return <ul>{items.map((item) => <li key={String(item)}>{renderItem(item)}</li>)}</ul>;
}
```


---

## forwardRef


```typescript
const Input = forwardRef<HTMLInputElement, InputProps>(function Input(props, ref) {
  return <input ref={ref} {...props} />;
});
```


---

## Children typing


Use `React.ReactNode` for flexible children; `React.ReactElement` when you need a single element.


---

## Discriminated actions


Type `useReducer` actions as a union with a `type` field for safe switches.


---

## Generic components


```typescript
function Select<T extends string>({ options, value, onChange }: {
  options: readonly T[];
  value: T;
  onChange: (v: T) => void;
}) { /* ... */ }
```


---

## Definition — Props

> **Definition:** **Props** — The read-only inputs passed to a React component — typed as an interface.


---

## Props with children


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


---

## useState patterns


```typescript
const [count, setCount] = useState(0);
const [user, setUser] = useState<User | null>(null);
```


---

## Best Practices

- ✅ Define props interfaces; export when reused.
- ✅ Use `ComponentPropsWithoutRef` to extend native elements.

---

## Common Mistakes

Watch for these patterns — they cost hours in real projects.

### Mistake 1: React.FC everywhere

Implicit children issues

Prefer explicit props interface.

---

### Mistake 2: any for event handlers

`onChange={(e: any) =>`

Use `ChangeEvent<HTMLInputElement>`.

---

## Interview Points

> **📌 Interview Point 1: How to type useState?**

Pass initial value or generic: `useState<User | null>(null)`.

---

> **📌 Interview Point 2: children type?**

ReactNode for flexible children.

---

## Exercises

Practice with `npx tsc --noEmit` after each exercise.

### Exercise 12.1: Button props ⭐

**Task:** Extend button with variant prop.

<details><summary>💡 Hint</summary>

HTML attributes.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary";
}
```

</details>

---

### Exercise 12.2: Controlled input ⭐⭐

**Task:** Typed onChange handler.

<details><summary>💡 Hint</summary>

events.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function Input({ value, onChange }: {
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}) {
  return <input value={value} onChange={onChange} />;
}
```

</details>

---

### Exercise 12.3: useReducer ⭐⭐⭐

**Task:** Discriminated action union.

<details><summary>💡 Hint</summary>

redux-style.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
type Action = { type: "inc" } | { type: "add"; n: number };
function reducer(state: number, action: Action): number {
  switch (action.type) {
    case "inc": return state + 1;
    case "add": return state + action.n;
  }
}
```

</details>

---

### Exercise 12.4: Context hook ⭐⭐

**Task:** Typed context + custom hook.

<details><summary>💡 Hint</summary>

null guard.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
const Ctx = createContext<User | null>(null);
function useUser() {
  const u = useContext(Ctx);
  if (!u) throw new Error("No user");
  return u;
}
```

</details>

---

### Exercise 12.5: Generic List ⭐⭐⭐

**Task:** List<T> render prop.

<details><summary>💡 Hint</summary>

generics in UI.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
function List<T>({ items, render }: { items: T[]; render: (item: T) => React.ReactNode }) {
  return <ul>{items.map((item, i) => <li key={i}>{render(item)}</li>)}</ul>;
}
```

</details>

---

### Exercise 12.6: forwardRef input ⭐⭐

**Task:** Ref to input element.

<details><summary>💡 Hint</summary>

forwardRef types.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
const Input = forwardRef<HTMLInputElement, React.InputHTMLAttributes<HTMLInputElement>>(
  (props, ref) => <input ref={ref} {...props} />
);
```

</details>

---

## Chapter Summary

You covered a lot in this chapter. Here is a concise recap:

- Props interfaces, typed events, and hooks prevent UI regressions.
- Generics power reusable list/table components.

---

---

## Navigation

**⬅️ [Previous: Async TypeScript](./ch11-async-typescript.md)**  
**➡️ [Next: Best Practices](./ch13-best-practices.md)**

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

*Last updated: 2025 | TypeScript course — CodeShelf*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
