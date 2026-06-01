---
title: Styling in Next.js
description: Global CSS, CSS Modules, SCSS, Tailwind v4 setup, and next/image optimization
order: 6
tags: [nextjs, css, tailwind, scss, images]
---

# Section 6 — Different Ways of Styling in Next.js

> **Difficulty:** Beginner–Intermediate · **Time:** 60 min · **Prerequisites:** [Section 1](./ch01-introduction-to-nextjs.md)

---

## Learning Outcome

- ✔ Add **global CSS** and **CSS Modules**
- ✔ Use **SCSS** in Next.js
- ✔ Set up **Tailwind v4** (new and existing projects)
- ✔ Optimize images with **`next/image`**

---

## Adding Styles in Next.js Apps Using CSS

Import global styles **once** in the root layout:

```jsx
// app/layout.js
import './globals.css';

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
```

```css
/* app/globals.css */
body {
  margin: 0;
  font-family: system-ui, sans-serif;
}
```

---

## Using CSS Modules in Next.js

File name: **`*.module.css`** — classes are **scoped** automatically.

```css
/* components/Card.module.css */
.card {
  padding: 1rem;
  border-radius: 8px;
}
```

```jsx
import styles from './Card.module.css';

export function Card({ children }) {
  return <div className={styles.card}>{children}</div>;
}
```

---

## Using SCSS in Next.js

```bash
npm install sass
```

Rename to `.module.scss` and import the same way:

```scss
/* Card.module.scss */
.card {
  padding: 1rem;
  &:hover {
    background: #f5f5f5;
  }
}
```

Next.js compiles Sass automatically once `sass` is installed.

---

## Setting Up Tailwind v4 in Next.js

**New project** — choose Tailwind when running `create-next-app`.

**Manual setup (Tailwind v4):**

```bash
npm install tailwindcss @tailwindcss/postcss postcss
```

```js
// postcss.config.mjs
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
};
```

```css
/* app/globals.css */
@import 'tailwindcss';
```

---

## Setting Up Tailwind v4 in Existing Next.js Project

1. Install packages (above)
2. Add PostCSS config
3. Replace `@tailwind base/components/utilities` with `@import 'tailwindcss';`
4. Remove old `tailwind.config.js` if migrating from v3 (v4 is CSS-first)

```jsx
export default function Home() {
  return (
    <h1 className="text-3xl font-bold text-blue-600">
      Hello Tailwind v4
    </h1>
  );
}
```

---

## Image Optimization in Next.js

Use **`next/image`** instead of `<img>` for automatic resizing, lazy loading, and modern formats.

```jsx
import Image from 'next/image';

export function Avatar() {
  return (
    <Image
      src="/profile.jpg"
      alt="Profile"
      width={200}
      height={200}
      priority={false}
    />
  );
}
```

Remote images — allow domains in `next.config.js`:

```js
module.exports = {
  images: {
    remotePatterns: [
      { protocol: 'https', hostname: 'images.example.com' },
    ],
  },
};
```

---

## Summary

- ✔ **Global CSS** in root layout · **Modules** for scoped styles
- ✔ **Sass** via `npm install sass`
- ✔ **Tailwind v4** via `@import 'tailwindcss'`
- ✔ **`next/image`** for performance

| ← Previous | Next → |
|------------|--------|
| [Error Handling](./ch05-error-handling.md) | [Backend Route Handlers](./ch07-backend-route-handlers.md) |
