---
title: React Router
description: Client-side routing with React Router — Routes, Link, useParams, nested routes, and navigation hooks.
order: 8
tags: [react, router, routing, navigation, spa]
---

# Chapter 8: React Router

## 8.1 Why client-side routing?

Traditional multi-page apps reload the full HTML on every navigation. **Single-page applications (SPAs)** update the URL and swap components without a full page refresh.

> **Definition:** React Router maps URL paths to React components and keeps the UI in sync with the browser history API.

## 8.2 Installation and setup

```bash
npm install react-router-dom
```

```jsx
// main.jsx
import { BrowserRouter } from 'react-router-dom';
import App from './App.jsx';

createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
```

| Router | Use case |
|--------|----------|
| `BrowserRouter` | Clean URLs (`/about`) — needs server fallback |
| `HashRouter` | URLs with `#` — static hosting without config |

## 8.3 Basic routes

```jsx
import { Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home.jsx';
import About from './pages/About.jsx';
import NotFound from './pages/NotFound.jsx';

function App() {
  return (
    <>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </>
  );
}
```

### Link vs anchor

| | `<Link to="...">` | `<a href="...">` |
|---|-------------------|------------------|
| Navigation | Client-side, no reload | Full page reload |
| SPA | ✅ | ❌ |
| External URLs | ❌ | ✅ |

Use `<a>` for external links; `<Link>` for internal routes.

## 8.4 Dynamic routes and useParams

```jsx
// Route definition
<Route path="/posts/:postId" element={<PostDetail />} />

// PostDetail.jsx
import { useParams, Link } from 'react-router-dom';

function PostDetail() {
  const { postId } = useParams();

  return (
    <article>
      <h1>Post #{postId}</h1>
      <Link to="/posts">← Back to posts</Link>
    </article>
  );
}
```

### Optional and splat params

```jsx
<Route path="/files/*" element={<Files />} />
// useParams() → { '*': 'docs/readme.md' }

<Route path="/users/:userId?" element={<UserProfile />} />
// userId may be undefined
```

## 8.5 Nested routes and layouts

```jsx
import { Outlet } from 'react-router-dom';

function DashboardLayout() {
  return (
    <div className="dashboard">
      <aside>
        <Link to="/dashboard">Overview</Link>
        <Link to="/dashboard/settings">Settings</Link>
      </aside>
      <main>
        <Outlet />  {/* Child route renders here */}
      </main>
    </div>
  );
}

// Routes
<Route path="/dashboard" element={<DashboardLayout />}>
  <Route index element={<DashboardHome />} />
  <Route path="settings" element={<Settings />} />
</Route>
```

| URL | Renders |
|-----|---------|
| `/dashboard` | Layout + DashboardHome |
| `/dashboard/settings` | Layout + Settings |

## 8.6 Navigation hooks

```jsx
import { useNavigate, useLocation, useSearchParams } from 'react-router-dom';

function LoginForm() {
  const navigate = useNavigate();
  const location = useLocation();

  function handleSuccess() {
    const from = location.state?.from?.pathname || '/';
    navigate(from, { replace: true });
  }

  return <form onSubmit={handleSuccess}>...</form>;
}

function ProductFilters() {
  const [searchParams, setSearchParams] = useSearchParams();
  const category = searchParams.get('category') || 'all';

  function setCategory(cat) {
    setSearchParams({ category: cat });
  }

  return (
    <div>
      <button onClick={() => setCategory('books')}>Books</button>
      <p>Showing: {category}</p>
    </div>
  );
}
```

| Hook | Returns |
|------|---------|
| `useNavigate()` | Function to programmatically navigate |
| `useLocation()` | Current location object (`pathname`, `state`) |
| `useSearchParams()` | URL query string as `URLSearchParams` |
| `useParams()` | Dynamic segment values |

## 8.7 Protected routes

```jsx
import { Navigate, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext.jsx';

function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();
  const location = useLocation();

  if (loading) return <p>Loading...</p>;
  if (!user) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return children;
}

// Usage
<Route
  path="/dashboard"
  element={
    <ProtectedRoute>
      <DashboardLayout />
    </ProtectedRoute>
  }
/>
```

## 8.8 Route loaders (React Router v6.4+)

Data routers can fetch before render:

```jsx
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: '/posts/:id',
    element: <PostDetail />,
    loader: async ({ params }) => {
      const res = await fetch(`/api/posts/${params.id}`);
      return res.json();
    },
  },
]);

// In component
import { useLoaderData } from 'react-router-dom';

function PostDetail() {
  const post = useLoaderData();
  return <h1>{post.title}</h1>;
}
```

## 8.9 Deployment note

For `BrowserRouter`, configure your host to serve `index.html` for all routes (SPA fallback). Vite preview and most platforms support this via rewrite rules.

## Exercises

1. **Multi-page app** — Create Home, About, Contact pages with shared nav.
2. **Blog routes** — `/posts` list and `/posts/:slug` detail with `useParams`.
3. **Nested dashboard** — Layout with sidebar; nested settings and profile routes.
4. **Protected route** — Redirect unauthenticated users to `/login`.

## Summary

| Topic | Key point |
|-------|-----------|
| `BrowserRouter` | Wrap app for routing |
| `Routes` / `Route` | Map paths to elements |
| `Link` | Client-side navigation |
| `useParams` | Read dynamic URL segments |
| `Outlet` | Render nested child routes |

## Next chapter

Continue to [Chapter 9: Forms](./ch09-forms.md).
