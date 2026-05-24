---
title: Performance
description: React.memo, useMemo, useCallback, code splitting with lazy and Suspense, and profiling.
order: 11
tags: [react, performance, memo, lazy, suspense, optimization]
---

# Chapter 11: Performance

## 11.1 When to optimize

React is fast by default. Optimize **after** measuring, not preemptively.

> **Definition:** Performance work targets unnecessary re-renders, large bundle size, and expensive computations — verified with React DevTools Profiler.

### Optimization priority

```text
1. Fix slow renders (Profiler)
2. Reduce bundle size (lazy loading)
3. Memoize hot paths (memo, useMemo, useCallback)
4. Virtualize long lists (react-window)
```

## 11.2 Understanding re-renders

A component re-renders when:

- Its **state** changes
- Its **props** change (shallow compare)
- Its **parent** re-renders (unless prevented)
- **Context** it consumes changes

```jsx
function Parent() {
  const [count, setCount] = useState(0);
  return (
    <>
      <button onClick={() => setCount(c => c + 1)}>{count}</button>
      <ExpensiveChild data="static" />  {/* Re-renders with Parent */}
    </>
  );
}
```

## 11.3 React.memo

`React.memo` skips re-render if props are shallowly equal.

```jsx
import { memo } from 'react';

const UserRow = memo(function UserRow({ user, onDelete }) {
  console.log('render', user.id);
  return (
    <tr>
      <td>{user.name}</td>
      <td>
        <button onClick={() => onDelete(user.id)}>Delete</button>
      </td>
    </tr>
  );
});
```

### When memo helps

| Helps | Does not help |
|-------|---------------|
| Pure list items with stable props | Component always gets new props |
| Heavy render cost | Cheap components |
| Frequent parent re-renders | Root cause is context/state in same tree |

Pair with `useCallback` for stable function props:

```jsx
const handleDelete = useCallback((id) => {
  setUsers(prev => prev.filter(u => u.id !== id));
}, []);
```

See [Chapter 6](./ch06-hooks-deep-dive.md).

## 11.4 useMemo for expensive work

```jsx
const filteredProducts = useMemo(() => {
  return products
    .filter(p => p.category === category)
    .sort((a, b) => a.price - b.price);
}, [products, category]);
```

Profile before memoizing — simple filters rarely need it.

## 11.5 Code splitting with lazy

Split routes or heavy components into separate JavaScript chunks loaded on demand.

```jsx
import { lazy, Suspense } from 'react';

const AdminDashboard = lazy(() => import('./pages/AdminDashboard.jsx'));
const ChartPanel = lazy(() => import('./components/ChartPanel.jsx'));

function App() {
  return (
    <Suspense fallback={<p>Loading module...</p>}>
      <Routes>
        <Route path="/admin" element={<AdminDashboard />} />
      </Routes>
    </Suspense>
  );
}
```

### lazy() rules

- Must be **default export** in target module
- Wrap in `<Suspense>` with fallback UI
- Can nest Suspense boundaries for granular loading

```jsx
function Dashboard() {
  return (
    <div>
      <Header />  {/* Renders immediately */}
      <Suspense fallback={<ChartSkeleton />}>
        <ChartPanel />
      </Suspense>
    </div>
  );
}
```

## 11.6 Suspense for async UI

React 18+ supports Suspense for data fetching in frameworks like Next.js and with libraries that integrate with Suspense boundaries.

```jsx
<Suspense fallback={<Spinner />}>
  <Comments postId={id} />
</Suspense>
```

In plain Vite SPAs, Suspense is primarily used with `lazy()` imports.

## 11.7 Virtualizing long lists

Rendering 10,000 DOM nodes is slow. **Virtualization** renders only visible rows.

```jsx
import { FixedSizeList } from 'react-window';

function VirtualList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>{items[index].name}</div>
  );

  return (
    <FixedSizeList
      height={400}
      width="100%"
      itemCount={items.length}
      itemSize={35}
    >
      {Row}
    </FixedSizeList>
  );
}
```

Libraries: `react-window`, `@tanstack/react-virtual`.

## 11.8 Profiling with DevTools

1. Open React DevTools → **Profiler** tab
2. Click record, interact with app, stop
3. Inspect flame graph for slow components
4. Enable "Highlight updates" to see re-render scope

| Signal | Action |
|--------|--------|
| Long render time | Memoize, split component, virtualize |
| Many wasted renders | `memo`, stable props, split context |
| Large bundle | `lazy`, analyze with `rollup-plugin-visualizer` |

## 11.9 Production build

```bash
npm run build
npm run preview
```

Vite minifies, tree-shakes, and hashes assets. Check bundle size in build output.

## 11.10 Anti-patterns

| Anti-pattern | Why |
|--------------|-----|
| `memo` everything | Overhead without benefit |
| Inline object/array props | Breaks memo: `style={{ color: 'red' }}` |
| Premature `useMemo` | Adds complexity |
| Huge Context values | All consumers re-render |

```jsx
// ❌ New object every render
<Child config={{ theme: 'dark' }} />

// ✅ Memoize or lift constant
const config = useMemo(() => ({ theme: 'dark' }), []);
<Child config={config} />
```

## Exercises

1. **Profiler** — Find a component that re-renders unnecessarily; fix with `memo`.
2. **Lazy route** — Split a heavy page with `lazy()` and route-level Suspense.
3. **Stable callback** — Pass `useCallback` handler to memoized list items.
4. **Bundle** — Run build and note largest chunks; lazy-load one of them.

## Summary

| Tool | Purpose |
|------|---------|
| `React.memo` | Skip render if props unchanged |
| `useMemo` / `useCallback` | Stable values and functions |
| `lazy` + `Suspense` | Code-split components |
| Profiler | Measure before optimizing |
| Virtualization | Large lists |

## Next chapter

Continue to [Chapter 12: Patterns & Architecture](./ch12-patterns-and-architecture.md).
