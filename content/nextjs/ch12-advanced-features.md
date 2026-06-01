---
title: Advanced Next.js Features
description: Middleware, NextResponse rewrites, Edge runtime, internationalization, and Google login with NextAuth.js
order: 12
tags: [nextjs, middleware, edge, i18n, nextauth]
---

# Section 12 — Advanced Next.js Features

> **Difficulty:** Advanced · **Time:** 90 min · **Prerequisites:** [Section 11](./ch11-server-actions.md)

---

## Learning Outcome

- ✔ Write **middleware** for auth and redirects
- ✔ **Rewrite** requests with `NextResponse`
- ✔ Understand **Edge runtime**
- ✔ Add **i18n** and **Google login** with NextAuth.js

---

## Understanding Middlewares in Next.js

Middleware runs **before** a request completes — at the edge or Node.

```js
// middleware.js (project root)

import { NextResponse } from 'next/server';

export function middleware(request) {
  const token = request.cookies.get('session')?.value;

  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*', '/profile/:path*'],
};
```

| Use case | Example |
|----------|---------|
| Auth guard | Redirect if no session |
| A/B testing | Rewrite to variant URL |
| Geo routing | Redirect by country header |
| Rate limiting | Block abusive IPs |

---

## Rewrite a Request using NextResponse

**Rewrite** = show content from another path **without** changing the browser URL.

```js
export function middleware(request) {
  if (request.nextUrl.pathname === '/old-blog') {
    return NextResponse.rewrite(new URL('/blog', request.url));
  }
  return NextResponse.next();
}
```

| Method | Browser URL | Content from |
|--------|-------------|--------------|
| `redirect` | Changes | New URL |
| `rewrite` | Stays same | Internal path |

---

## What is Edge Runtime in Next.js?

**Edge** = lightweight JavaScript runtime close to users (CDN locations).

| | Node.js runtime | Edge runtime |
|---|-----------------|--------------|
| **APIs** | Full Node (fs, some npm) | Subset Web APIs |
| **Cold start** | Slower | Faster |
| **Use** | DB drivers, heavy libs | Auth checks, redirects |

```js
export const runtime = 'edge';

export async function GET() {
  return Response.json({ region: process.env.VERCEL_REGION });
}
```

> ⚠️ **Warning:** Mongoose often **does not** run on Edge — use middleware for auth, Node Route Handlers for DB.

---

## Internationalization (i18n) in Next.js

### App Router pattern — `[lang]` segment

```text
app/[lang]/page.js
app/[lang]/about/page.js
```

```jsx
// app/[lang]/layout.js

export async function generateStaticParams() {
  return [{ lang: 'en' }, { lang: 'hi' }];
}

export default function LangLayout({ children, params }) {
  return <div lang={params.lang}>{children}</div>;
}
```

Middleware can redirect `/` → `/en` based on `Accept-Language` header.

### Dictionary files

```json
// dictionaries/en.json
{ "welcome": "Welcome" }
```

```jsx
const dict = await import(`@/dictionaries/${lang}.json`);
return <h1>{dict.welcome}</h1>;
```

---

## Implementing Google Login with NextAuth.js

```bash
npm install next-auth
```

```js
// app/api/auth/[...nextauth]/route.js

import NextAuth from 'next-auth';
import GoogleProvider from 'next-auth/providers/google';

const handler = NextAuth({
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    }),
  ],
  callbacks: {
    async session({ session, token }) {
      session.user.id = token.sub;
      return session;
    },
  },
});

export { handler as GET, handler as POST };
```

```jsx
'use client';

import { signIn, signOut, useSession } from 'next-auth/react';

export function AuthButton() {
  const { data: session } = useSession();
  if (session) {
    return <button onClick={() => signOut()}>Sign out</button>;
  }
  return <button onClick={() => signIn('google')}>Sign in with Google</button>;
}
```

Wrap app with `SessionProvider` in a client layout component.

Set in `.env.local`:

```env
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=random-long-string
```

---

## Summary

- ✔ **Middleware** — auth, redirects, rewrites before render
- ✔ **Edge** — fast, limited runtime for middleware/light APIs
- ✔ **i18n** — `[lang]` routes + dictionaries
- ✔ **NextAuth.js** — OAuth (Google) with minimal setup

| ← Previous | Next → |
|------------|--------|
| [Server Actions](./ch11-server-actions.md) | [TypeScript Tooling](./ch13-typescript-tooling-setup.md) |
