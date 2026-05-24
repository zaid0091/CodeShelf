---
title: Testing
description: Testing React components with Vitest, React Testing Library, user events, and async testing patterns.
order: 13
tags: [react, testing, vitest, testing-library, rtl]
---

# Chapter 13: Testing

## 13.1 Why test React apps?

Tests catch regressions, document behavior, and enable confident refactors.

> **Definition:** **React Testing Library (RTL)** encourages tests that resemble how users interact with your app — queries by role, label, and text rather than implementation details.

### Testing pyramid for React

| Layer | Tool | Focus |
|-------|------|-------|
| Unit | Vitest/Jest | Pure functions, hooks |
| Component | RTL | User-visible behavior |
| E2E | Playwright, Cypress | Full flows in browser |

This chapter focuses on **component tests** with Vitest + RTL (Vite default).

## 13.2 Setup

Vite React template with Vitest:

```bash
npm install -D vitest @testing-library/react @testing-library/jest-dom @testing-library/user-event jsdom
```

```js
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    setupFiles: './src/test/setup.js',
  },
});
```

```js
// src/test/setup.js
import '@testing-library/jest-dom';
```

```json
// package.json scripts
"test": "vitest",
"test:run": "vitest run"
```

## 13.3 First component test

```jsx
// Counter.jsx
import { useState } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
    </div>
  );
}
```

```jsx
// Counter.test.jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect } from 'vitest';
import { Counter } from './Counter.jsx';

describe('Counter', () => {
  it('increments count when button clicked', async () => {
    const user = userEvent.setup();
    render(<Counter />);

    expect(screen.getByText('Count: 0')).toBeInTheDocument();

    await user.click(screen.getByRole('button', { name: /increment/i }));

    expect(screen.getByText('Count: 1')).toBeInTheDocument();
  });
});
```

## 13.4 Query priority

RTL recommends accessible queries:

| Priority | Query | Example |
|----------|-------|---------|
| 1 | `getByRole` | `getByRole('button', { name: 'Submit' })` |
| 2 | `getByLabelText` | `getByLabelText('Email')` |
| 3 | `getByPlaceholderText` | `getByPlaceholderText('Search...')` |
| 4 | `getByText` | `getByText('Welcome')` |
| 5 | `getByTestId` | Last resort — `getByTestId('custom-widget')` |

### Query variants

| Method | Behavior |
|--------|----------|
| `getBy*` | Throws if not found |
| `queryBy*` | Returns null if not found |
| `findBy*` | Async — waits for element |

```jsx
expect(screen.queryByText('Error')).not.toBeInTheDocument();
await screen.findByText('Loaded');
```

## 13.5 Testing forms

```jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { LoginForm } from './LoginForm.jsx';

it('submits email and password', async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn();

  render(<LoginForm onSubmit={onSubmit} />);

  await user.type(screen.getByLabelText(/email/i), 'alice@example.com');
  await user.type(screen.getByLabelText(/password/i), 'secret123');
  await user.click(screen.getByRole('button', { name: /log in/i }));

  expect(onSubmit).toHaveBeenCalledWith({
    email: 'alice@example.com',
    password: 'secret123',
  });
});
```

## 13.6 Mocking fetch

```jsx
import { render, screen, waitFor } from '@testing-library/react';
import { UserList } from './UserList.jsx';

beforeEach(() => {
  vi.stubGlobal('fetch', vi.fn());
});

afterEach(() => {
  vi.unstubAllGlobals();
});

it('renders users from API', async () => {
  fetch.mockResolvedValueOnce({
    ok: true,
    json: async () => [{ id: 1, name: 'Alice' }],
  });

  render(<UserList />);

  expect(screen.getByText(/loading/i)).toBeInTheDocument();

  await waitFor(() => {
    expect(screen.getByText('Alice')).toBeInTheDocument();
  });
});
```

## 13.7 Testing with providers

Wrap components that need Context or Router:

```jsx
import { BrowserRouter } from 'react-router-dom';
import { ThemeProvider } from '../context/ThemeContext.jsx';

function renderWithProviders(ui) {
  return render(
    <BrowserRouter>
      <ThemeProvider>
        {ui}
      </ThemeProvider>
    </BrowserRouter>
  );
}

it('navigates to about', async () => {
  const user = userEvent.setup();
  renderWithProviders(<App />);
  await user.click(screen.getByRole('link', { name: /about/i }));
  expect(screen.getByRole('heading', { name: /about us/i })).toBeInTheDocument();
});
```

Extract `renderWithProviders` to `src/test/utils.jsx` for reuse.

## 13.8 Testing hooks

Use `@testing-library/react` `renderHook`:

```jsx
import { renderHook, act } from '@testing-library/react';
import { useCounter } from './useCounter.js';

it('increments counter', () => {
  const { result } = renderHook(() => useCounter());

  act(() => result.current.increment());

  expect(result.current.count).toBe(1);
});
```

## 13.9 What NOT to test

| Avoid | Prefer |
|-------|--------|
| Internal state directly | Visible outcome |
| Implementation (which hook) | User behavior |
| Third-party library internals | Your integration |
| Snapshot-only tests | Meaningful assertions |

```jsx
// ❌ Testing state variable
expect(component.state.count).toBe(1);

// ✅ Testing what user sees
expect(screen.getByText('Count: 1')).toBeInTheDocument();
```

## 13.10 Coverage and CI

```bash
npm run test:run -- --coverage
```

Run tests in CI on every pull request. Aim for meaningful coverage on critical paths, not 100% for its own sake.

## Exercises

1. **Button** — Test disabled state and click handler.
2. **Form validation** — Assert error messages appear for invalid email.
3. **Async list** — Mock fetch; test loading → success and loading → error.
4. **Router** — Test navigation between two routes with RTL.

## Summary

| Topic | Key point |
|-------|-----------|
| RTL | Test like a user |
| Queries | Prefer `getByRole`, `getByLabelText` |
| `userEvent` | Realistic interactions |
| Providers | Wrap Context/Router in tests |
| Mock fetch | Stub global `fetch` with Vitest |

## Next chapter

Continue to [Chapter 14: Best Practices](./ch14-best-practices.md).
