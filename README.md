# CodeShelf

A premium, interactive personal documentation and notes platform for developers to study, track progress, and run code — built with React 19, TypeScript, Vite, and Tailwind CSS v4.

---

## 🌟 Premium Features

CodeShelf is packed with advanced learning and study enhancements:

*   **📈 Visual Progress Dashboard** — Auto-tracks completed chapters, active reading streaks, milestones, and provides visual circular progress gauges.
*   **🎮 Dynamic System Roadmap** — Replaces static course lists with winding coordinate SVG node graphs that light up green as chapters are read. Includes a layout toggle to return to classic list views.
*   **💻 In-Browser JS/Python Playgrounds** — Execute code snippets directly on any chapter page using an interactive terminal (compiled via Pyodide WASM for Python and standard sandboxes for JavaScript).
*   **✏️ Sidebar Summary Drawer** — A slide-over notebook widget allowing readers to take, edit, and auto-save notes per chapter in `localStorage`.
*   **🎨 Sentence Highlighting** — Click-and-drag text selection tool allowing readers to overlay yellow, green, or blue highlights that persist across page reloads.
*   **🎉 Milestone Confetti** — Dynamic full-screen SVG confetti explosions triggered on 100% course completion or streak milestone achievements (7 or 30 days).
*   **🖨️ Export Formats** — Directly download notes as `.md` files or compile to PDFs. Custom print stylesheets hide interactive side-panels and swap overlay highlights for clean underlines.
*   **🏷️ Dynamic Tab Titles** — Updates browser tab titles dynamically (`Chapter Title | CodeShelf`) and restores default values on unmount.
*   **🎨 Theme-Aware Branding** — Hand-crafted vector logo mark and horizontal typography lockups that dynamically shift dark/light colors according to the system theme.

---

## 🚀 Getting Started

To spin up CodeShelf locally:

```bash
# Install dependencies
npm install

# Run the development server
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

---

## 📝 Writing Notes

Create a markdown file in the `content/` folder structure:

```text
content/
├── typescript/
│   ├── ch00-course-overview.md
│   └── ch01-types.md
├── javascript/
├── react/
├── python/
└── django/
```

### Frontmatter Schema

Each markdown file requires YAML frontmatter to index metadata:

```yaml
---
title: Chapter 1: Types & Declarations
description: Core type systems and primitive definitions
order: 1
---

# Types & Declarations

Your content here...
```

| Field | Required | Description |
| :--- | :--- | :--- |
| `title` | **Yes** | Displays in the sidebar and navigation breadcrumbs |
| `description` | No | Appears inside global search results |
| `order` | No | Sort sequence index within the course track (default: 99) |

*To add a new track, create a subfolder in `content/` and register its unique ID under `TOPIC_LABELS` in [content.ts](file:///d:/Mydocs/CodeShelf/src/lib/content.ts).*

---

## 📁 Project Structure

```text
src/
├── components/     # Reusable UI elements (Sidebar, Roadmap, CodePlayground, etc.)
├── hooks/          # Custom state hooks (Theme, Lenis, DocumentTitles, ScrollTracker)
├── layouts/        # Layout shells (DocsLayout, Dashboard)
├── lib/            # Utilities (Progress Tracking, Highlight Sync, Flashcard Parsing)
├── pages/          # Full Route Views (HomePage, DocPage, DashboardPage)
content/            # Core Markdown source files
public/             # Static brand logo PNGs, favicons, and icons
```

---

## 🛠️ Tech Stack

*   **Core**: [React 19](https://react.dev/) + [TypeScript](https://www.typescriptlang.org/) + [Vite 8](https://vite.dev/)
*   **Styles**: [Tailwind CSS v4](https://tailwindcss.com/) + Custom Vanilla CSS variables
*   **Syntax & Markdown**: [react-markdown](https://github.com/remarkjs/react-markdown) + [remark-gfm](https://github.com/remarkjs/remark-gfm) + [rehype-highlight](https://github.com/rehypejs/rehype-highlight)
*   **Playgrounds**: [Pyodide](https://pyodide.org/) (In-Browser WASM compilation)
*   **Smooth Scrolling**: [Lenis](https://lenis.darkroom.engineering/)
