---
title: Deployment and Production
description: Prepare Next.js for production, environment variables, and custom domain setup
order: 10
tags: [nextjs, deployment, vercel, environment]
---

# Section 10 — Deployment and Production

> **Difficulty:** Intermediate · **Time:** 45 min · **Prerequisites:** [Section 9](./ch09-authentication.md)

---

## Learning Outcome

- ✔ Prepare a Next.js app for **production**
- ✔ Manage **environment variables** safely
- ✔ Deploy and attach a **custom domain**

---

## Preparing Our Next App for Deployment

### Pre-deploy checklist

```text
[ ] DEBUG off (Next.js sets NODE_ENV=production on build)
[ ] Environment variables set on hosting platform
[ ] MongoDB Atlas allows hosting IP (or 0.0.0.0/0 for serverless)
[ ] npm run build passes locally
[ ] npm run start tested locally
```

```bash
npm run build
npm run start
```

### Production settings

```js
// next.config.js

module.exports = {
  poweredByHeader: false,
  images: {
    remotePatterns: [/* your CDNs */],
  },
};
```

Use **HTTPS** in production — set secure cookies (`secure: true`).

---

## Managing Environment Variables

| File | Committed? | Use |
|------|------------|-----|
| `.env.local` | No | Local secrets |
| `.env.production` | Usually no | Production overrides |
| `.env.example` | Yes | Template for team |

```env
# .env.example
MONGODB_URI=
JWT_SECRET=
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

**Naming:**

- **`NEXT_PUBLIC_*`** — exposed to browser (API URLs, public keys)
- **No prefix** — server-only (DB URI, JWT secret)

```jsx
// Server only
const secret = process.env.JWT_SECRET;

// Client + server
const url = process.env.NEXT_PUBLIC_APP_URL;
```

> ⚠️ **Warning:** Never put secrets in `NEXT_PUBLIC_` variables.

---

## Custom Domain Setup for Our Next.js Application

### Deploy to Vercel (recommended)

1. Push code to GitHub
2. Import project at [vercel.com](https://vercel.com)
3. Add environment variables in project settings
4. Deploy — each push to `main` can auto-deploy

### Custom domain

1. Vercel dashboard → **Settings** → **Domains**
2. Add `www.yoursite.com`
3. Update DNS at your registrar (A/CNAME records Vercel shows)
4. SSL certificate is automatic

### Other hosts

- **Railway**, **Render**, **Fly.io** — support Node.js and `npm run start`
- **Docker** — use official Node image, run `next start`

---

## Summary

- ✔ Run **`build`** before deploy · test with **`start`**
- ✔ Secrets in host dashboard, not in git
- ✔ **Vercel** + custom domain is the fastest path for Next.js

| ← Previous | Next → |
|------------|--------|
| [Authentication](./ch09-authentication.md) | [Server Actions](./ch11-server-actions.md) |
