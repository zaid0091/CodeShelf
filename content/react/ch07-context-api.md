---
title: Context API
description: createContext, Provider, useContext, and when to use Context vs other state solutions.
order: 7
tags: [react, context, useContext, provider, global-state]
---

# Chapter 7: Context API

## 7.1 The prop drilling problem

When many nested components need the same data, passing props through every level is tedious.

```text
App (user)
 └── Layout (user)
      └── Sidebar (user)
           └── UserMenu (user)  ← finally uses it
```

**Prop drilling** — passing props through components that do not need them.

> **Definition:** Context lets you share values across the component tree without explicit prop passing at every level.

## 7.2 Creating context

```jsx
import { createContext, useContext, useState } from 'react';

const ThemeContext = createContext(null);

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  const value = {
    theme,
    toggleTheme: () => setTheme(t => (t === 'light' ? 'dark' : 'light')),
  };

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
}
```

### Three steps

| Step | API |
|------|-----|
| 1. Create | `createContext(defaultValue)` |
| 2. Provide | `<Context.Provider value={...}>` |
| 3. Consume | `useContext(Context)` |

## 7.3 Wiring the provider

```jsx
// main.jsx
import { ThemeProvider } from './context/ThemeContext.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ThemeProvider>
      <App />
    </ThemeProvider>
  </StrictMode>
);
```

```jsx
// Any nested component
import { useTheme } from '../context/ThemeContext.jsx';

function Header() {
  const { theme, toggleTheme } = useTheme();

  return (
    <header className={`header header-${theme}`}>
      <button onClick={toggleTheme}>Switch to {theme === 'light' ? 'dark' : 'light'}</button>
    </header>
  );
}
```

## 7.4 Default values

```jsx
const AuthContext = createContext({
  user: null,
  login: () => {},
  logout: () => {},
});
```

Default is used only when **no Provider** exists above. Prefer explicit Provider in app root.

## 7.5 Multiple contexts

Split unrelated concerns into separate contexts to limit re-renders.

```jsx
<AuthProvider>
  <ThemeProvider>
    <CartProvider>
      <App />
    </CartProvider>
  </ThemeProvider>
</AuthProvider>
```

| Context | Typical data |
|---------|--------------|
| Auth | User, token, login/logout |
| Theme | Colors, dark mode |
| Locale | Language, translations |
| Cart | Items, totals |

## 7.6 Performance considerations

When Provider `value` changes, **all consumers re-render**.

```jsx
// ❌ New object every render — all consumers re-render
function AppProvider({ children }) {
  const [user, setUser] = useState(null);
  return (
    <AuthContext.Provider value={{ user, setUser }}>
      {children}
    </AuthContext.Provider>
  );
}

// ✅ Memoize value
function AppProvider({ children }) {
  const [user, setUser] = useState(null);
  const value = useMemo(() => ({ user, setUser }), [user]);
  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}
```

Split fast-changing and slow-changing data into separate contexts when needed.

## 7.7 Context vs alternatives

| Solution | Best for |
|----------|----------|
| **Props** | Local, parent → child data |
| **Context** | Theme, auth, locale — moderate update frequency |
| **useState + lifting** | Shared state between few siblings |
| **Zustand / Redux** | Large apps, complex state, devtools |
| **React Query** | Server/async data (see Ch 10) |

Context is **not** a replacement for a full state manager in large apps.

## 7.8 Auth context example

```jsx
const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/me')
      .then(res => res.ok ? res.json() : null)
      .then(setUser)
      .finally(() => setLoading(false));
  }, []);

  const login = async (credentials) => {
    const res = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(credentials),
    });
    const data = await res.json();
    setUser(data.user);
  };

  const logout = () => setUser(null);

  const value = useMemo(
    () => ({ user, loading, login, logout, isAuthenticated: !!user }),
    [user, loading]
  );

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth requires AuthProvider');
  return ctx;
}
```

## 7.9 Compound provider pattern

```jsx
function AppProviders({ children }) {
  return (
    <AuthProvider>
      <ThemeProvider>
        {children}
      </ThemeProvider>
    </AuthProvider>
  );
}
```

Or compose with a helper:

```jsx
function composeProviders(...providers) {
  return ({ children }) =>
    providers.reduceRight(
      (acc, Provider) => <Provider>{acc}</Provider>,
      children
    );
}

const AllProviders = composeProviders(AuthProvider, ThemeProvider);
```

## Exercises

1. **Theme context** — Implement light/dark theme affecting CSS variables or class on `<body>`.
2. **Auth guard** — Create `ProtectedRoute` that redirects if `!user`.
3. **Split contexts** — Separate `UserContext` and `SettingsContext`; verify fewer re-renders.
4. **Custom hook** — Export `useTheme()` with error if used outside provider.

## Summary

| Topic | Key point |
|-------|-----------|
| Problem | Prop drilling through many layers |
| `createContext` | Creates context object |
| `Provider` | Supplies value to subtree |
| `useContext` | Reads nearest provider value |
| Performance | Memoize value; split contexts |

## Next chapter

Continue to [Chapter 8: React Router](./ch08-react-router.md).
