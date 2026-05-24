# CodeShelf

A personal documentation and notes website for quick revision of programming concepts — built with React, TypeScript, Vite, and Tailwind CSS.

## Features

- **Markdown-based content** — write notes in `.md` files with frontmatter
- **Topic organization** — TypeScript, JavaScript, React, Python, Django, and more
- **Sidebar navigation** with collapsible sections
- **Search** — find notes instantly (Ctrl+K)
- **Dark mode** toggle with persistence
- **Syntax highlighting** and copy-to-clipboard for code blocks
- **Tag system** for cross-topic browsing
- **Fully frontend** — no backend or database required

## Getting Started

```bash
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

## Adding Notes

Create a markdown file in the `content/` folder:

```
content/
├── typescript/
│   ├── introduction.md
│   └── types.md
├── javascript/
├── react/
├── python/
└── django/
```

Each file supports YAML frontmatter:

```yaml
---
title: My Note Title
description: Short description for search results
order: 1
tags: [basics, types]
---

# My Note Title

Your markdown content here...
```

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | Display title in sidebar and page |
| `description` | No | Shown in search results and tag pages |
| `order` | No | Sort order within topic (default: 99) |
| `tags` | No | Tags for cross-topic filtering |

To add a new topic, create a folder under `content/` and register it in `src/lib/content.ts` under `TOPIC_LABELS`.

## Project Structure

```
src/
├── components/     # UI components (Sidebar, SearchBar, CodeBlock, etc.)
├── hooks/          # Custom hooks (theme, search)
├── layouts/        # Page layouts (DocsLayout)
├── lib/            # Content loading and types
├── pages/          # Route pages
content/            # Markdown notes (the actual content)
```

## Build

```bash
npm run build
npm run preview
```

## Tech Stack

- [React 19](https://react.dev/) + [TypeScript](https://www.typescriptlang.org/)
- [Vite](https://vite.dev/)
- [Tailwind CSS v4](https://tailwindcss.com/)
- [react-markdown](https://github.com/remarkjs/react-markdown) + [remark-gfm](https://github.com/remarkjs/remark-gfm)
- [rehype-highlight](https://github.com/rehypejs/rehype-highlight) for syntax highlighting
- [React Router](https://reactrouter.com/) for client-side routing
