---
title: React Containerization
description: Containerizing React applications for development with hot-reloading (Vite/Webpack) and production using multi-stage builds and Nginx routing configs.
order: 6
tags: [docker, react, javascript, typescript, nginx, production]
---

# Chapter 6: React Containerization

> **Learn how to set up React container workflows — configuring hot-reloading for local Vite development and using multi-stage builds with Nginx for production.**

---

## Table of Contents

1. [Development vs Production Workflows](#development-vs-production-workflows)
2. [Development Setup (Vite + Hot-Reloading)](#development-setup-vite--hot-reloading)
3. [The File-Watching (Chokidar) Problem](#the-file-watching-chokidar-problem)
4. [Production Setup (Multi-Stage Build + Nginx)](#production-setup-multi-stage-build--nginx)
5. [Configuring Nginx for Client-Side Routing](#configuring-nginx-for-client-side-routing)
6. [Best Practices](#best-practices)
7. [Common Mistakes](#common-mistakes)
8. [Interview Points](#interview-points)
9. [Exercises](#exercises)
10. [Chapter Summary](#chapter-summary)

---

## Development vs Production Workflows

When containerizing React applications, the requirements for development and production are polar opposites:

- **In Development:** We need Node.js runtime, devDependencies, hot-module replacement (HMR), and file mounts to sync code changes instantly.
- **In Production:** We do not need Node.js or source code. We need static compiled assets (HTML, CSS, JS) served efficiently via a high-performance web server like Nginx.

---

## Development Setup (Vite + Hot-Reloading)

Here is a standard development Dockerfile for a React application built with Vite:

```dockerfile
# Dockerfile.dev
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

# Source code is mounted at runtime via volumes, but copy files as fallback
COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
```

### Local Dev Compose Setup
To ensure hot-reloading works, we mount our local repository into `/app` inside the container:

```yaml
# docker-compose.dev.yml
version: '3.8'

services:
  frontend:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "5173:5173"
    volumes:
      - .:/app
      - /app/node_modules # Anonymous volume prevents overwriting container node_modules
    environment:
      - CHOKIDAR_USEPOLLING=true # Enables file watching inside virtual filesystems
```

---

## The File-Watching (Chokidar) Problem

If you mount code using Docker volumes (especially when running Docker Desktop on Windows/macOS with virtualized file systems), Vite's hot-module reloading might not detect code changes on the host.

### Fix: Enable Watch Polling
Modify your `vite.config.ts` (or `vite.config.js`) to enable polling under the `server.watch` options:

```typescript
// vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    watch: {
      usePolling: true, // Force polling to detect changes in container mounts
    },
    host: true, // Need to listen on 0.0.0.0 for docker mapping
    port: 5173,
  },
})
```

---

## Production Setup (Multi-Stage Build + Nginx)

For production, we compile assets and throw away the Node environment, copying static assets to Nginx:

```dockerfile
# ==========================================
# Stage 1: Build static assets
# ==========================================
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci --silent
COPY . .
RUN npm run build # Creates 'dist/' directory

# ==========================================
# Stage 2: Serve using Nginx
# ==========================================
FROM nginx:1.25-alpine
# Copy compiled output to Nginx default folder
COPY --from=build /app/dist /usr/share/nginx/html
# Copy Nginx config for routing fallbacks
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## Configuring Nginx for Client-Side Routing

If you are using client-side routing libraries like **React Router**, reloading pages other than the home page (e.g., `localhost/dashboard`) in an Nginx container returns a **404 Not Found** error. This is because Nginx searches for a physical file named `/dashboard` which does not exist.

### Fix: Custom `nginx.conf`
We configure Nginx to fall back to `index.html` for any unmatched requests:

```nginx
# nginx.conf
server {
    listen 80;
    server_name localhost;

    location / {
        root /usr/share/nginx/html;
        index index.html index.htm;
        # Try serving the file, then directory, then fallback to index.html
        try_files $uri $uri/ /index.html;
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root /usr/share/nginx/html;
    }
}
```

---

## Best Practices

- **Use `npm ci`:** In your Dockerfile build stages, use `npm ci` (clean install) instead of `npm install`. It is faster, deterministic, and enforces consistent package versions.
- **Bind to `0.0.0.0`:** Vite/Webpack dev servers must bind to `0.0.0.0` (all interfaces) rather than `localhost`/`127.0.0.1` so that port mapping works outside the container.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Overwriting container packages | Mounting `.` to `/app` overrides `/app/node_modules` inside the container with the host's folder, breaking builds if OS architectures differ | Add an anonymous volume `- /app/node_modules` in the `volumes` list of your `docker-compose.yml`. |
| Leaving React dev server in prod | Slow runtime performance, massive image sizes, leaks development configurations | Always use multi-stage builds and serve files statically with Nginx. |

---

## Interview Points

> **📌 Interview Point 1: Why does reloading a page in a Dockerized React app return a 404 in Nginx, and how do you fix it?**
> Client-side routers (React Router) manage URLs in the browser. Nginx expects those URLs to correspond to physical files. Setting `try_files $uri $uri/ /index.html` tells Nginx to route all unmatched traffic to `index.html` so the React router can take over.

> **📌 Interview Point 2: Why do we add `/app/node_modules` as an anonymous volume in development?**
> It tells Docker to preserve the `node_modules` directory created inside the container during the `npm install` build step, preventing it from being overwritten by your host's local folders during bind mount synchronization.

---

## Exercises

### Exercise 1: Configure Vite for Docker ⭐
**Task:** Edit the following config snippet so that Vite is accessible when running inside a Docker container.

```javascript
// vite.config.js
export default {
  server: {
    // What configuration goes here?
  }
}
```

<details>
<summary>💡 Hint (click to reveal)</summary>
Set `host` to true (or `"0.0.0.0"`) and expose the port.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```javascript
export default {
  server: {
    host: true, // Or '0.0.0.0'
    port: 5173,
    watch: {
      usePolling: true
    }
  }
}
```
</details>

---

## Chapter Summary

- **Development React** requires bind mounts and anonymous `node_modules` volumes.
- **Production React** uses multi-stage builds and serves compiled assets via Nginx.
- Configure Nginx with **`try_files`** to support React Router client-side routing.

---

## Previous / Next Chapter

**⬅️ [Previous: Django Containerization](./ch05-django-containerization.md)**

**➡️ [Next: Volumes & Networks](./ch07-volumes-and-networks.md)**

---

*Chapter 6 of the Docker & Containerization Guide | CodeShelf*
