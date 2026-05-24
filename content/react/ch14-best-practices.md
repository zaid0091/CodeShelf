---
title: Best Practices
description: React coding standards, accessibility, security, naming conventions, and production checklist.
order: 14
tags: [react, best-practices, accessibility, conventions, production]
---

# Chapter 14: Best Practices

## 14.1 Component design principles

Write components that are **small, focused, and predictable**.

| Principle | Practice |
|-----------|----------|
| Single responsibility | One component, one job |
| Pure when possible | Same props → same output |
| Colocate related code | Keep hooks, styles, tests near feature |
| Explicit props | Avoid huge prop bags; use composition |

```jsx
// ❌ God component
function Dashboard({ user, posts, comments, settings, notifications, ... }) { ... }

// ✅ Composed
function Dashboard() {
  return (
    <PageLayout>
      <DashboardHeader />
      <DashboardStats />
      <RecentActivity />
    </PageLayout>
  );
}
```

## 14.2 Naming conventions

| Item | Convention | Example |
|------|------------|---------|
| Components | PascalCase | `UserAvatar.jsx` |
| Hooks | camelCase, `use` prefix | `useAuth.js` |
| Event handlers | `handle` + Event | `handleSubmit` |
| Boolean props | `is`, `has`, `should` | `isDisabled` |
| Callback props | `on` + Event | `onChange`, `onDelete` |

```jsx
function SearchBar({ isLoading, onSearch }) {
  function handleKeyDown(e) {
    if (e.key === 'Enter') onSearch(e.target.value);
  }
  ...
}
```

## 14.3 File and export conventions

```jsx
// One primary component per file
export default function Modal({ isOpen, onClose, children }) { ... }

// Co-locate types (TypeScript)
// Modal.tsx + Modal.test.tsx + Modal.module.css
```

Use **named exports** for utilities and hooks; **default export** for page/feature components (team preference may vary — stay consistent).

## 14.4 Keys and lists

Always use stable keys from data ids. Never use random keys or index on reorderable lists. See [Chapter 4](./ch04-lists-and-keys.md).

## 14.5 State management guidelines

```text
1. Local useState     → UI-only, single component
2. Lifted state       → Siblings share data
3. Context            → Theme, auth, locale
4. React Query        → Server/async data
5. Zustand/Redux      → Complex global client state
```

Do not put everything in Context or Redux on day one.

## 14.6 Effects discipline

- Prefer computing values during render over syncing with `useEffect`
- Fetch on user action when appropriate (button click)
- Always clean up subscriptions and abort fetches
- See [Chapter 5](./ch05-useEffect.md)

## 14.7 Accessibility (a11y)

React does not automatically make apps accessible — you must use semantic HTML and ARIA correctly.

```jsx
function Modal({ isOpen, onClose, title, children }) {
  if (!isOpen) return null;

  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
      onKeyDown={(e) => e.key === 'Escape' && onClose()}
    >
      <h2 id="modal-title">{title}</h2>
      {children}
      <button onClick={onClose} aria-label="Close dialog">×</button>
    </div>
  );
}
```

### a11y checklist

| Item | Action |
|------|--------|
| Buttons | Use `<button>`, not `<div onClick>` for actions |
| Forms | Associate `<label htmlFor>` with inputs |
| Images | Meaningful `alt` text |
| Focus | Visible focus styles; trap focus in modals |
| Color | Do not rely on color alone for meaning |

Run [eslint-plugin-jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y) in your project.

## 14.8 Security

| Risk | Mitigation |
|------|------------|
| XSS via `dangerouslySetInnerHTML` | Avoid or sanitize with DOMPurify |
| Exposed API keys | Use env vars; never commit secrets |
| Open redirects | Validate redirect URLs |
| CSRF | Tokens for cookie auth |

```jsx
// ❌ Never render raw user HTML without sanitization
<div dangerouslySetInnerHTML={{ __html: userBio }} />

// ✅ Render text or sanitize first
<p>{userBio}</p>
```

## 14.9 Environment variables (Vite)

```jsx
const apiUrl = import.meta.env.VITE_API_URL;

// .env.local (gitignored)
VITE_API_URL=https://api.example.com
```

Only `VITE_` prefixed vars are exposed to client code.

## 14.10 Error handling UX

- Show friendly error messages, not stack traces
- Offer retry for transient failures
- Log errors to monitoring (Sentry, etc.)
- Use error boundaries for unexpected render crashes

## 14.11 Code review checklist

Before merging:

- [ ] Loading and error states handled
- [ ] No console.log left in production paths
- [ ] Accessible labels and keyboard support
- [ ] No unnecessary re-renders (obvious cases)
- [ ] Tests for critical user flows
- [ ] Types or PropTypes for public components (if team uses them)

## 14.12 Staying current

- Official docs: [react.dev](https://react.dev)
- React RFCs and blog for upcoming features
- Prefer function components and hooks in all new code
- Migrate class components incrementally when touching legacy code

## Exercises

1. **Audit** — Review an old component for a11y issues; fix labels and roles.
2. **Refactor** — Split a 200-line component into 3 focused components.
3. **Env** — Move hardcoded API URL to `VITE_API_URL`.
4. **Checklist** — Run through the code review checklist on your todo app.

## Summary

| Area | Guideline |
|------|-----------|
| Components | Small, composable, single purpose |
| Naming | PascalCase components, `handle`/`on` events |
| State | Colocate; escalate only when needed |
| a11y | Semantic HTML + ARIA + keyboard |
| Security | No raw HTML, no secrets in client |

## Next chapter

Continue to [Chapter 15: Interview Preparation](./ch15-interview-prep.md).
