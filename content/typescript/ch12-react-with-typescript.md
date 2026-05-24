---
title: Chapter 12 — React with TypeScript
description: Typing React components, props, children, events, hooks, refs, and common patterns.
order: 12
tags: [typescript, react, hooks, components, jsx]
---

# Chapter 12: React with TypeScript

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

## Practice Exercise — Chapter 12

```text
Exercise 12.1: UserCard
  a) Props: user (id, name, avatarUrl?), onSelect(id: string).
  b) Optional badge when user.isOnline.

Exercise 12.2: useLocalStorage hook
  a) function useLocalStorage<T>(key: string, initial: T): [T, (v: T) => void].
  b) Use with typed Settings object in a component.

Exercise 12.3: Form
  a) Typed controlled inputs for email/password.
  b) Submit handler with FormEvent; validate before API call.

Exercise 12.4: Generic DataTable
  a) Columns with key, header, render(row).
  b) Table<T> with items: T[] and typed render callbacks.
```

Next: [Chapter 13 — Best Practices](./ch13-best-practices.md).
