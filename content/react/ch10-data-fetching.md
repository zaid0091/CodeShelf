---
title: Data Fetching
description: Fetching data with fetch API, loading and error states, useEffect patterns, and TanStack Query introduction.
order: 10
tags: [react, data-fetching, fetch, loading, react-query, tanstack]
---

# Chapter 10: Data Fetching

## 10.1 Where data lives

React components need data from APIs, databases, or files. **Server state** (remote data) differs from **client state** (UI toggles, form inputs).

| Client state | Server state |
|--------------|--------------|
| Owned locally | Owned by server |
| Synchronous updates | Async fetch/mutate |
| `useState`, Context | fetch, React Query |

## 10.2 Basic fetch with useEffect

```jsx
import { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    async function loadUser() {
      try {
        setLoading(true);
        setError(null);
        const res = await fetch(`/api/users/${userId}`, {
          signal: controller.signal,
        });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        setUser(data);
      } catch (err) {
        if (err.name !== 'AbortError') setError(err);
      } finally {
        setLoading(false);
      }
    }

    loadUser();
    return () => controller.abort();
  }, [userId]);

  if (loading) return <p>Loading user...</p>;
  if (error) return <p className="error">Error: {error.message}</p>;
  if (!user) return null;

  return (
    <article>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </article>
  );
}
```

### The async state trio

Always model three states:

| State | UI |
|-------|-----|
| `loading` | Spinner, skeleton |
| `error` | Error message, retry button |
| `data` | Success content |

## 10.3 POST requests

```jsx
async function createPost(payload) {
  const res = await fetch('/api/posts', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || 'Failed to create post');
  }

  return res.json();
}

function CreatePostForm() {
  const [title, setTitle] = useState('');
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    setSubmitting(true);
    setError(null);
    try {
      const post = await createPost({ title });
      console.log('Created:', post);
      setTitle('');
    } catch (err) {
      setError(err.message);
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={title} onChange={e => setTitle(e.target.value)} />
      {error && <p className="error">{error}</p>}
      <button disabled={submitting}>{submitting ? 'Saving...' : 'Create'}</button>
    </form>
  );
}
```

## 10.4 Custom useFetch hook (recap)

```jsx
function useFetch(url) {
  const [state, setState] = useState({
    data: null,
    loading: true,
    error: null,
  });

  useEffect(() => {
    let cancelled = false;

    fetch(url)
      .then(r => {
        if (!r.ok) throw new Error(r.statusText);
        return r.json();
      })
      .then(data => {
        if (!cancelled) setState({ data, loading: false, error: null });
      })
      .catch(error => {
        if (!cancelled) setState({ data: null, loading: false, error });
      });

    return () => { cancelled = true; };
  }, [url]);

  return state;
}
```

See [Chapter 6](./ch06-hooks-deep-dive.md) for hook details.

## 10.5 TanStack Query (React Query)

TanStack Query manages caching, refetching, deduplication, and background updates.

```bash
npm install @tanstack/react-query
```

```jsx
// main.jsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient();

createRoot(document.getElementById('root')).render(
  <QueryClientProvider client={queryClient}>
    <App />
  </QueryClientProvider>
);
```

```jsx
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

function PostList() {
  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ['posts'],
    queryFn: () => fetch('/api/posts').then(r => r.json()),
  });

  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <ul>
      {data.map(post => (
        <li key={post.id}>{post.title}</li>
      ))}
      <button onClick={() => refetch()}>Refresh</button>
    </ul>
  );
}

function CreatePost() {
  const queryClient = useQueryClient();

  const mutation = useMutation({
    mutationFn: (newPost) =>
      fetch('/api/posts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newPost),
      }).then(r => r.json()),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['posts'] });
    },
  });

  return (
    <button
      onClick={() => mutation.mutate({ title: 'New Post' })}
      disabled={mutation.isPending}
    >
      {mutation.isPending ? 'Creating...' : 'Add Post'}
    </button>
  );
}
```

### React Query benefits

| Feature | Benefit |
|---------|---------|
| `queryKey` | Cache identity and invalidation |
| Stale-while-revalidate | Show cached data while refetching |
| Deduping | One request for same key |
| `useMutation` | Optimistic updates, rollback |

## 10.6 Pagination pattern

```jsx
function PaginatedUsers() {
  const [page, setPage] = useState(1);

  const { data, isLoading } = useQuery({
    queryKey: ['users', page],
    queryFn: () =>
      fetch(`/api/users?page=${page}`).then(r => r.json()),
    keepPreviousData: true,
  });

  return (
    <div>
      {isLoading && !data ? <p>Loading...</p> : (
        <ul>
          {data.results.map(u => (
            <li key={u.id}>{u.name}</li>
          ))}
        </ul>
      )}
      <button disabled={page === 1} onClick={() => setPage(p => p - 1)}>
        Previous
      </button>
      <button onClick={() => setPage(p => p + 1)}>Next</button>
    </div>
  );
}
```

## 10.7 Error boundaries (brief)

Fetch errors in render should be handled in component state. For unexpected render errors, wrap routes in an **Error Boundary** class component or use `react-error-boundary`.

## 10.8 Best practices

- Always handle loading and error UI
- Abort fetches on unmount or dependency change
- Do not fetch in render — use effect, event, or React Query
- Normalize API responses when shapes vary
- Use environment variables for API base URLs (`import.meta.env.VITE_API_URL`)

## Exercises

1. **User list** — Fetch users from JSONPlaceholder; show loading/error/empty states.
2. **Search** — Debounce search input; refetch when query changes.
3. **React Query** — Convert a `useEffect` fetch to `useQuery` with cache invalidation after create.
4. **Retry** — Add a "Try again" button that refetches on error.

## Summary

| Topic | Key point |
|-------|-----------|
| fetch + useEffect | Manual loading/error/data state |
| AbortController | Cancel in-flight requests |
| React Query | Cache, mutations, invalidation |
| queryKey | Identifies cached queries |
| Server state | Separate from UI client state |

## Next chapter

Continue to [Chapter 11: Performance](./ch11-performance.md).
