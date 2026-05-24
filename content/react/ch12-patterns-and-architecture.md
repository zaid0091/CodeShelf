---
title: Patterns & Architecture
description: Lifting state, compound components, render props, container/presentational split, and folder structure.
order: 12
tags: [react, patterns, architecture, compound-components, lifting-state]
---

# Chapter 12: Patterns & Architecture

Structuring React apps for maintainability and team scale.

## 12.1 Lifting state up

When siblings share data, **lift state** to the closest common ancestor.

```jsx
function TemperatureConverter() {
  const [celsius, setCelsius] = useState('');

  const fahrenheit =
    celsius === '' ? '' : ((parseFloat(celsius) * 9) / 5 + 32).toFixed(1);

  return (
    <div>
      <TemperatureField
        label="Celsius"
        value={celsius}
        onChange={setCelsius}
      />
      <TemperatureField
        label="Fahrenheit"
        value={fahrenheit}
        onChange={(val) => setCelsius(String(((parseFloat(val) - 32) * 5) / 9))}
      />
    </div>
  );
}

function TemperatureField({ label, value, onChange }) {
  return (
    <label>
      {label}
      <input value={value} onChange={(e) => onChange(e.target.value)} />
    </label>
  );
}
```

| Symptom | Solution |
|---------|----------|
| Duplicate state in siblings | Lift to parent |
| Too many props drilled | Context (Ch 7) or composition |
| Complex shared logic | Custom hook (Ch 6) |

## 12.2 Container vs presentational

Separate **data/logic** from **UI**.

```jsx
// Container — fetches and manages state
function UserListContainer() {
  const { data: users, loading, error } = useFetch('/api/users');

  if (loading) return <Spinner />;
  if (error) return <ErrorMessage error={error} />;

  return <UserListView users={users} />;
}

// Presentational — pure UI from props
function UserListView({ users }) {
  return (
    <ul className="user-list">
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

Modern code often uses custom hooks instead of container components:

```jsx
function UserList() {
  const { users, loading, error } = useUsers();
  if (loading) return <Spinner />;
  if (error) return <ErrorMessage error={error} />;
  return <UserListView users={users} />;
}
```

## 12.3 Compound components

Related components share implicit state via Context — flexible API like `<select>` + `<option>`.

```jsx
const TabsContext = createContext(null);

function Tabs({ defaultIndex = 0, children }) {
  const [activeIndex, setActiveIndex] = useState(defaultIndex);
  const value = useMemo(
    () => ({ activeIndex, setActiveIndex }),
    [activeIndex]
  );

  return (
    <TabsContext.Provider value={value}>
      <div className="tabs">{children}</div>
    </TabsContext.Provider>
  );
}

function TabList({ children }) {
  return <div role="tablist">{children}</div>;
}

function Tab({ index, children }) {
  const { activeIndex, setActiveIndex } = useContext(TabsContext);
  const isActive = activeIndex === index;

  return (
    <button
      role="tab"
      aria-selected={isActive}
      onClick={() => setActiveIndex(index)}
    >
      {children}
    </button>
  );
}

function TabPanels({ children }) {
  const { activeIndex } = useContext(TabsContext);
  return <div>{children[activeIndex]}</div>;
}

// Usage — flexible composition
<Tabs defaultIndex={0}>
  <TabList>
    <Tab index={0}>Overview</Tab>
    <Tab index={1}>Settings</Tab>
  </TabList>
  <TabPanels>
    <OverviewPanel />
    <SettingsPanel />
  </TabPanels>
</Tabs>
```

Export as namespace: `Tabs.List`, `Tabs.Tab`, etc.

## 12.4 Render props

Pass a function as a child or prop to share behavior.

```jsx
function MouseTracker({ render }) {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    function handleMove(e) {
      setPosition({ x: e.clientX, y: e.clientY });
    }
    window.addEventListener('mousemove', handleMove);
    return () => window.removeEventListener('mousemove', handleMove);
  }, []);

  return render(position);
}

// Usage
<MouseTracker render={({ x, y }) => (
  <p>Mouse: {x}, {y}</p>
)} />
```

Custom hooks largely replaced render props for reuse, but the pattern still appears in libraries.

## 12.5 Slot composition

Named props for layout regions:

```jsx
function PageLayout({ header, sidebar, children, footer }) {
  return (
    <div className="page">
      <header>{header}</header>
      <div className="body">
        <aside>{sidebar}</aside>
        <main>{children}</main>
      </div>
      <footer>{footer}</footer>
    </div>
  );
}
```

## 12.6 State colocation

Keep state as **close as possible** to where it is used.

```jsx
// ❌ Global modal state for one page
const [isSettingsOpen, setIsSettingsOpen] = useState(false); // in App

// ✅ Colocated in Settings page
function SettingsPage() {
  const [isEditing, setIsEditing] = useState(false);
  ...
}
```

Promote state only when multiple distant components need it.

## 12.7 Folder structure

Common scalable layout:

```text
src/
├── components/       # Shared UI (Button, Modal)
│   └── ui/
├── features/         # Feature modules (auth, cart)
│   └── auth/
│       ├── AuthForm.jsx
│       ├── useAuth.js
│       └── authApi.js
├── hooks/            # Shared custom hooks
├── context/          # Global providers
├── pages/            # Route-level components
├── utils/            # Pure helpers
└── App.jsx
```

| Folder | Contents |
|--------|----------|
| `components/` | Reusable, domain-agnostic UI |
| `features/` | Business logic grouped by feature |
| `pages/` | One component per route |

## 12.8 Controlled vs uncontrolled boundaries

Encapsulate form complexity inside feature components; expose simple callbacks (`onSubmit`) to parents.

## 12.9 Error and loading boundaries

Co-locate error UI with features; use route-level error boundaries for catastrophic failures.

## Exercises

1. **Lift state** — Two inputs that stay in sync (currency converter).
2. **Compound tabs** — Build Tabs with TabList, Tab, TabPanels using Context.
3. **Feature folder** — Reorganize a todo app into `features/todos/`.
4. **Custom hook extraction** — Move fetch logic from component to `useTodos()`.

## Summary

| Pattern | Use when |
|---------|----------|
| Lifting state | Siblings share data |
| Container/presentational | Separate fetch from UI |
| Compound components | Flexible related UI kit |
| Custom hooks | Reuse stateful logic |
| Feature folders | Scale team codebase |

## Next chapter

Continue to [Chapter 13: Testing](./ch13-testing.md).
