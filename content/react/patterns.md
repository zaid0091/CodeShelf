---
title: React Patterns
description: Common patterns for building React applications
order: 3
tags: [patterns, architecture]
---

# React Patterns

Production patterns for cleaner, more maintainable React apps.

## Lifting State Up

Share state between siblings via a common parent:

```jsx
function App() {
  const [filter, setFilter] = useState("");

  return (
    <>
      <SearchBar filter={filter} onChange={setFilter} />
      <ItemList filter={filter} />
    </>
  );
}
```

## Composition over Inheritance

```jsx
function Card({ children, title }) {
  return (
    <div className="card">
      {title && <h3>{title}</h3>}
      {children}
    </div>
  );
}

<Card title="User">
  <UserAvatar />
  <UserDetails />
</Card>
```

## Context for Global State

```jsx
const ThemeContext = createContext("light");

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState("light");
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

function ThemedButton() {
  const { theme, setTheme } = useContext(ThemeContext);
  return <button onClick={() => setTheme(t => t === "light" ? "dark" : "light")} />;
}
```

## Controlled vs Uncontrolled Inputs

```jsx
// Controlled — React owns the value
const [email, setEmail] = useState("");
<input value={email} onChange={e => setEmail(e.target.value)} />

// Uncontrolled — DOM owns the value
const ref = useRef();
<input ref={ref} defaultValue="hello" />
// read: ref.current.value
```

## Error Boundaries (Class Component)

```jsx
class ErrorBoundary extends React.Component {
  state = { hasError: false };

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  render() {
    return this.state.hasError
      ? <p>Something went wrong.</p>
      : this.props.children;
  }
}
```
