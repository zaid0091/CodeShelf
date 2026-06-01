---
title: Introduction to Next.js
description: Course syllabus, what Next.js is, creating your first app, and how it differs from React
order: 1
tags: [nextjs, introduction, create-next-app, react]
---

# Section 1 — Introduction to Next.js

> **Difficulty:** Beginner · **Time:** 30–40 min · **Prerequisites:** Basic React knowledge

---

## Learning Outcome

By the end of this section you will:

- ✔ Understand the **full course roadmap**
- ✔ Explain **what Next.js is** and why teams use it
- ✔ Create and run your **first Next.js app**
- ✔ Compare **React.js vs Next.js** clearly

---

## Next.js Course Syllabus

This course has **13 sections** — from routing basics to production auth and tooling:

| # | Section | You will learn |
|---|---------|----------------|
| 1 | Introduction | What Next.js is, first app, vs React |
| 2 | Routing | App Router, layouts, dynamic & catch-all routes |
| 3 | Rendering | SSR, CSR, SSG, ISR, hydration |
| 4 | Data & state | Fetching in App Router, hooks, Redux |
| 5 | Errors | `error.js`, recovery, global errors |
| 6 | Styling | CSS, modules, SCSS, Tailwind v4, images |
| 7 | Backend | Route Handlers, REST Todo API |
| 8 | MongoDB | Mongoose, CRUD |
| 9 | Auth | Register, login, cookies, sessions |
| 10 | Deployment | Env vars, production, custom domain |
| 11 | Server Actions | Forms, Zod, `useActionState` |
| 12 | Advanced | Middleware, Edge, i18n, NextAuth |
| 13 | Tooling | ESLint, Prettier, Husky |

Work through chapters **in order** — later sections build on earlier ones.

---

## What is Next.js?

> **Definition:** Next.js is a **React framework** for building full-stack web applications. It adds routing, server rendering, API routes, optimizations, and deployment workflows on top of React.

**Simple analogy:**

- **React** = engine
- **Next.js** = complete car (engine + wheels + steering + safety)

### What you get out of the box

| Feature | Benefit |
|---------|---------|
| File-based routing | Folders in `app/` become URLs |
| Server Components | Faster pages, less JavaScript in browser |
| Route Handlers | Backend API in same project |
| Image & font optimization | Better performance automatically |
| Built-in CSS support | Global CSS, modules, Tailwind |
| Easy deployment | Especially on Vercel |

Next.js is maintained by **Vercel** and is one of the most popular ways to ship React apps in production.

---

## Creating Our First Next.js App

### Step 1 — Run the installer

```bash
npx create-next-app@latest my-todo-app
```

### Step 2 — Answer the prompts

| Question | Recommended |
|----------|-------------|
| TypeScript? | Yes (industry standard) or No for this course's JS examples |
| ESLint? | Yes |
| Tailwind CSS? | Yes |
| `src/` directory? | Optional |
| App Router? | **Yes** (required for this course) |
| Turbopack? | Yes (faster dev) |

### Step 3 — Start development

```bash
cd my-todo-app
npm run dev
```

Open **http://localhost:3000** — you should see the default Next.js welcome page.

### Project structure (important folders)

```text
my-todo-app/
├── app/                 ← routes live here (App Router)
│   ├── layout.js        ← root layout (wraps all pages)
│   ├── page.js          ← home page → /
│   └── globals.css      ← global styles
├── public/              ← static files (images, favicon)
├── next.config.js       ← Next.js settings
├── package.json
└── .env.local           ← secrets (create later, never commit)
```

### Your first edit

```jsx
// app/page.js

export default function Home() {
  return (
    <main>
      <h1>My Todo App</h1>
      <p>Next.js is running!</p>
    </main>
  );
}
```

Save the file — the browser **hot-reloads** automatically.

### Useful commands

```bash
npm run dev      # development
npm run build    # production build
npm run start    # run production build locally
npm run lint     # check code quality
```

---

## Difference Between React.js and Next.js

| Topic | React.js | Next.js |
|-------|----------|---------|
| **Type** | UI library | Full framework |
| **Routing** | Add React Router yourself | Built-in (`app/` folders) |
| **Rendering** | Mostly client-side | Server + client (your choice) |
| **API / backend** | Separate server project | Route Handlers in same repo |
| **SEO** | Harder for SPAs | Server HTML helps SEO |
| **Setup** | Vite + manual config | `create-next-app` |
| **Learning curve** | Smaller core | More concepts, faster shipping |

### When to use which?

**Use React alone (e.g. Vite)** when:

- Building a widget embedded in another site
- You want maximum control and minimal opinions
- Backend is completely separate and team knows that stack

**Use Next.js** when:

- Building a full website or SaaS product
- You need SEO and fast first paint
- You want one repo for frontend + API
- You are learning modern full-stack React

> 💡 **Tip:** Learn React first, then Next.js. This course assumes you know components, props, and `useState`.

### Code comparison — same page

**React (Vite) — you wire routing:**

```jsx
// You need react-router-dom, main.jsx setup, etc.
function Home() {
  return <h1>Hello</h1>;
}
```

**Next.js — file = route:**

```jsx
// app/page.js — automatically served at /
export default function Home() {
  return <h1>Hello</h1>;
}
```

---

## Common Mistakes

- ❌ Choosing **Pages Router** instead of **App Router** during setup — this course uses App Router only
- ❌ Confusing Next.js with Node.js — Next.js is a **framework**; Node.js is the **runtime**
- ❌ Putting pages outside `app/` — they will not become routes

---

## Summary

- ✔ This course has **13 sections** ending with production tooling
- ✔ **Next.js** = React + routing + server features + full-stack tools
- ✔ Create apps with **`npx create-next-app@latest`**
- ✔ **React** handles UI; **Next.js** handles how that UI is delivered and connected to backends

| ← Previous | Next → |
|------------|--------|
| [Course Overview](./ch00-course-overview.md) | [Routing in Next.js](./ch02-routing-in-nextjs.md) |
