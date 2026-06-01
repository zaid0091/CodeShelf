---
title: Industry Level Next.js Project Setup with TypeScript
description: ESLint deep dive, Prettier, lint-staged, and Husky pre-commit hooks for production-grade Next.js projects
order: 13
tags: [nextjs, typescript, eslint, prettier, husky]
---

# Section 13 — Industry Level Next.js Project Setup with TypeScript

> **Difficulty:** Intermediate · **Time:** 60 min · **Prerequisites:** Full course completion recommended

---

## Learning Outcome

- ✔ Configure **ESLint** for Next.js + TypeScript
- ✔ Add **Prettier** for consistent formatting
- ✔ Run checks on staged files with **lint-staged**
- ✔ Block bad commits with **Husky** pre-commit hooks

---

## ESLint Deep Dive with Next.js

`create-next-app` with TypeScript includes ESLint by default.

```json
// .eslintrc.json (example)
{
  "extends": ["next/core-web-vitals", "next/typescript"]
}
```

```bash
npm run lint
```

### Common rules teams enable

| Rule area | Why |
|-----------|-----|
| `no-unused-vars` | Dead code |
| `@typescript-eslint/no-explicit-any` | Type safety |
| `react-hooks/rules-of-hooks` | Correct hook usage |

```bash
npm install -D @typescript-eslint/eslint-plugin @typescript-eslint/parser
```

---

## Using ESLint as Formatter in Next.js

ESLint can fix some issues automatically:

```bash
npx eslint . --fix
```

For full formatting, pair ESLint with **Prettier** (ESLint = logic, Prettier = style).

---

## Prettier Setup in Next.js

```bash
npm install -D prettier eslint-config-prettier
```

```json
// .prettierrc
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5"
}
```

```json
// .eslintrc.json — add last
{
  "extends": ["next/core-web-vitals", "prettier"]
}
```

```json
// package.json
{
  "scripts": {
    "format": "prettier --write ."
  }
}
```

---

## Setting Up Lint-Staged in Next.js

Run linters only on **staged** git files (fast commits).

```bash
npm install -D lint-staged
```

```json
// package.json
{
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": ["eslint --fix", "prettier --write"],
    "*.{json,md,css}": ["prettier --write"]
  }
}
```

---

## Husky Pre-Commit Hook Setup in Next.js

```bash
npm install -D husky
npx husky init
```

```bash
# .husky/pre-commit
npx lint-staged
```

Now every `git commit` runs ESLint + Prettier on changed files. Broken code is caught **before** it reaches the repo.

### Optional: commit message lint

```bash
npm install -D @commitlint/cli @commitlint/config-conventional
```

---

## TypeScript in Next.js (quick reference)

```tsx
// app/todos/page.tsx

interface Todo {
  id: string;
  title: string;
  done: boolean;
}

export default async function TodosPage() {
  const todos: Todo[] = await getTodos();
  return <ul>{todos.map((t) => <li key={t.id}>{t.title}</li>)}</ul>;
}
```

`create-next-app` with TypeScript generates `tsconfig.json` with strict settings — keep **`strict: true`**.

---

## Course Completed

Congratulations — you finished the **Next.js Full-Stack Course**.

### You can now

- ✔ Build routes, layouts, and APIs with the **App Router**
- ✔ Choose **rendering strategies** (SSG, SSR, ISR, client)
- ✔ Connect **MongoDB** and implement **authentication**
- ✔ Use **Server Actions** and **middleware**
- ✔ **Deploy** to production with proper **env** and **tooling**

### Keep learning

| Topic | Next step |
|-------|-----------|
| Testing | Playwright + Vitest for Next.js |
| Caching | Deep dive `unstable_cache`, tags |
| Monorepo | Turborepo + multiple apps |
| Performance | Lighthouse, bundle analyzer |

### Final project idea

Ship your **Todo app** with:

- User auth (email + Google)
- MongoDB persistence
- Protected routes
- Deployed on Vercel with custom domain
- Husky + Prettier on every commit

---

## Summary

- ✔ **ESLint** catches bugs · **Prettier** formats code
- ✔ **lint-staged** + **Husky** = quality gate on every commit
- ✔ **TypeScript** + strict config = safer refactors at scale

| ← Previous | Next → |
|------------|--------|
| [Advanced Features](./ch12-advanced-features.md) | [Course Overview](./ch00-course-overview.md) |
