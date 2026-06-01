---
title: Next.js Full-Stack Course Overview
description: Complete Next.js syllabus — routing, rendering, data, backend, MongoDB, auth, server actions, and production deployment
order: 0
tags: [nextjs, overview, course, full-stack, app-router]
---

# Next.js Full-Stack Course

> From your first `create-next-app` to a production-ready full-stack app with MongoDB, authentication, and deployment.

## Prerequisites

| Skill | Why it matters |
|-------|----------------|
| **HTML, CSS, JavaScript** | Foundation for React and Next.js |
| **React basics** | Components, props, state, hooks |
| **Terminal & npm** | Running dev servers and installing packages |

New to React? Start with the [React course](../react/ch00-course-overview.md) first.

## Course syllabus

### Section 1 — Introduction to Next.js

| Chapter | Topics |
|---------|--------|
| [Ch 1](./ch01-introduction-to-nextjs.md) | Syllabus, What is Next.js?, First app, React vs Next.js |

### Section 2 — Routing in Next.js

| Chapter | Topics |
|---------|--------|
| [Ch 2](./ch02-routing-in-nextjs.md) | App Router, layouts, nested routes, dynamic routes, catch-all, metadata, 404, route groups, private routes |

### Section 3 — Rendering Paradigms

| Chapter | Topics |
|---------|--------|
| [Ch 3](./ch03-rendering-paradigms.md) | SSR, CSR, static vs dynamic, SSG, ISR, server/client components, hydration |

### Section 4 — Data Fetching & State

| Chapter | Topics |
|---------|--------|
| [Ch 4](./ch04-data-fetching-and-state.md) | App Router data fetching, RSC, hooks, Context, Redux |

### Section 5 — Error Handling

| Chapter | Topics |
|---------|--------|
| [Ch 5](./ch05-error-handling.md) | `error.js`, recovery, nested errors, client exceptions, global errors |

### Section 6 — Styling

| Chapter | Topics |
|---------|--------|
| [Ch 6](./ch06-styling-in-nextjs.md) | CSS, CSS Modules, SCSS, Tailwind v4, image optimization |

### Section 7 — Backend (Route Handlers)

| Chapter | Topics |
|---------|--------|
| [Ch 7](./ch07-backend-route-handlers.md) | GET/POST/PUT/DELETE, dynamic handlers, request object, Todo API |

### Section 8 — MongoDB

| Chapter | Topics |
|---------|--------|
| [Ch 8](./ch08-mongodb-in-nextjs.md) | Connection, Mongoose models, CRUD |

### Section 9 — Authentication

| Chapter | Topics |
|---------|--------|
| [Ch 9](./ch09-authentication.md) | Register, login, cookies, sessions, protected routes, bcrypt |

### Section 10 — Deployment

| Chapter | Topics |
|---------|--------|
| [Ch 10](./ch10-deployment-and-production.md) | Deploy prep, environment variables, custom domain |

### Section 11 — Server Actions

| Chapter | Topics |
|---------|--------|
| [Ch 11](./ch11-server-actions.md) | Server Actions, `useActionState`, Zod validation, forms |

### Section 12 — Advanced Features

| Chapter | Topics |
|---------|--------|
| [Ch 12](./ch12-advanced-features.md) | Middleware, rewrites, Edge runtime, i18n, NextAuth |

### Section 13 — TypeScript & Tooling

| Chapter | Topics |
|---------|--------|
| [Ch 13](./ch13-typescript-tooling-setup.md) | ESLint, Prettier, lint-staged, Husky |

---

## What you will build

Across the course you will build a **Todo app** that grows into a full-stack product:

1. Static pages and routing
2. Server-rendered data
3. REST API with Route Handlers
4. MongoDB persistence
5. User registration, login, and protected todos
6. Server Actions for forms
7. Production deployment

## Recommended timeline

```text
Week 1–2:  Ch 1–3   Routing + rendering fundamentals
Week 3:    Ch 4–5   Data fetching + errors
Week 4:    Ch 6–8   Styling + backend + database
Week 5:    Ch 9–11  Auth + deploy + server actions
Week 6:    Ch 12–13 Advanced + tooling polish
```

## Quick start

```bash
npx create-next-app@latest my-todo-app
cd my-todo-app
npm run dev
```

**Start here →** [Section 1: Introduction](./ch01-introduction-to-nextjs.md)
