#!/usr/bin/env python3
"""Generate expanded React course chapters (ch01-ch15)."""
from __future__ import annotations

import re
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "content" / "react"


def fm(title: str, desc: str, order: int, tags: list[str]) -> str:
    t = ", ".join(tags)
    return f"""---
title: {title}
description: {desc}
order: {order}
tags: [{t}]
---

"""


def toc(items: list[str]) -> str:
    lines = ["## Table of Contents\n", "\n"]
    for i, (title, anchor) in enumerate(items, 1):
        lines.append(f"{i}. [{title}](#{anchor})\n")
    lines.append("\n---\n\n")
    return "".join(lines)


def welcome(text: str) -> str:
    return f"> **{text}**\n> Take your time with each section — understanding beats speed.\n\n---\n\n"


def interview_block(n: int, q: str, answer: str) -> str:
    return f"""> **📌 Interview Point {n}: {q}**

{answer}

---

"""


def exercise_block(
    n: int,
    stars: str,
    title: str,
    task: str,
    hint: str,
    solution: str,
) -> str:
    return f"""### Exercise {n}: {title} {stars}

**Task:** {task}

<details>
<summary>💡 Hint (click to reveal)</summary>

{hint}

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

{solution}

</details>

---

"""


def next_ch(path: str, title: str) -> str:
    return f"""## Next Chapter

Continue to [{title}]({path}).

"""


def summary_table(rows: list[tuple[str, str]]) -> str:
    lines = ["## Chapter Summary\n\n", "| Concept | Takeaway |\n", "|---------|----------|\n"]
    for k, v in rows:
        lines.append(f"| **{k}** | {v} |\n")
    lines.append("\n")
    return "".join(lines)


def anchor(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def section(title: str, body: str) -> str:
    return f"## {title}\n\n{body}\n\n---\n\n"


def subsection(title: str, body: str) -> str:
    return f"### {title}\n\n{body}\n\n"


def defn(text: str) -> str:
    return f"> **Definition:** {text}\n\n"


def mistakes_table(rows: list[tuple[str, str, str]]) -> str:
    lines = [
        "## Common Mistakes\n\n",
        "| Mistake | Why it breaks | Fix |\n",
        "|---------|---------------|-----|\n",
    ]
    for m, why, fix in rows:
        lines.append(f"| {m} | {why} | {fix} |\n")
    lines.append("\n---\n\n")
    return "".join(lines)


def interview_section(points: list[tuple[str, str]]) -> str:
    lines = [
        "## Interview Points\n\n",
        "Study these before technical interviews. Practice answering out loud in 60–90 seconds.\n\n---\n\n",
    ]
    for i, (q, a) in enumerate(points, 1):
        lines.append(interview_block(i, q, a))
    return "".join(lines)


def exercises_section(exs: list[tuple]) -> str:
    lines = [
        "## Exercises\n\n",
        "Practice by building small pieces in a Vite React app. Try each exercise before opening solutions.\n\n---\n\n",
    ]
    for ex in exs:
        e = list(ex)
        while len(e) < 6:
            e.append(
                "Build the solution in your Vite project and compare with examples in this chapter."
            )
        lines.append(exercise_block(*e[:6]))
    return "".join(lines)


# ─── Chapter builders ─────────────────────────────────────────────────────────

def ch01() -> str:
    title = "# Chapter 1: Introduction — What is React?\n\n"
    items = [
        ("What is React?", anchor("What is React?")),
        ("Library vs Framework", anchor("Library vs Framework")),
        ("History of React", anchor("History of React")),
        ("Where React Runs", anchor("Where React Runs")),
        ("Prerequisites from JavaScript", anchor("Prerequisites from JavaScript")),
        ("Setting Up with Vite", anchor("Setting Up with Vite")),
        ("Project Structure Explained", anchor("Project Structure Explained")),
        ("The Entry Point main.jsx", anchor("The Entry Point main.jsx")),
        ("Your First Component", anchor("Your First Component")),
        ("Component Naming Rules", anchor("Component Naming Rules")),
        ("Imports and Exports", anchor("Imports and Exports")),
        ("Declarative vs Imperative UI", anchor("Declarative vs Imperative UI")),
        ("Virtual DOM and Reconciliation", anchor("Virtual DOM and Reconciliation")),
        ("React 18 and Beyond", anchor("React 18 and Beyond")),
        ("StrictMode Explained", anchor("StrictMode Explained")),
        ("React Developer Tools", anchor("React Developer Tools")),
        ("React vs Other Tools", anchor("React vs Other Tools")),
        ("The React Ecosystem", anchor("The React Ecosystem")),
        ("Best Practices for Beginners", anchor("Best Practices for Beginners")),
        ("Common Mistakes", anchor("Common Mistakes")),
        ("Interview Points", anchor("Interview Points")),
        ("Exercises", anchor("Exercises")),
        ("Chapter Summary", anchor("Chapter Summary")),
    ]
    body = welcome(
        "Welcome to React! You already know JavaScript — now you will learn how to build interactive user interfaces with components."
    )
    body += toc(items)
    body += section(
        "What is React?",
        defn(
            "React is a JavaScript **library** for building user interfaces. You describe what the screen should look like for a given state, and React updates the browser efficiently when that state changes."
        )
        + subsection(
            "The building-blocks analogy",
            """Think of a website like a house:

- **HTML** is the structure — walls, doors, rooms (headings, paragraphs, forms).
- **CSS** is decoration — paint, furniture layout, lighting (colors, spacing, fonts).
- **JavaScript** is electricity and plumbing — things that **move, respond, and change**.
- **React** is a **smart electrical system** — instead of rewiring every bulb by hand when something changes, you describe the desired setup once and React routes power where needed.

Without React, you often write code like this:

```javascript
const countEl = document.getElementById('count');
const btn = document.getElementById('btn');
let count = 0;
btn.addEventListener('click', () => {
  count++;
  countEl.textContent = count;
});
```

That works for a counter. For a dashboard with dozens of panels, manual DOM updates become fragile. React lets you write:

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+1</button>
    </div>
  );
}
```

You describe the UI as a function of `count`. React figures out which DOM nodes to update.""",
        )
        + subsection(
            "What React is NOT",
            """| Myth | Reality |
|------|---------|
| React is a full framework like Angular | React is a **UI library** — you add routing, data, etc. yourself |
| React replaces HTML/CSS | You still write markup (JSX) and styles |
| React only works with Facebook | React is open source; millions of apps use it |
| You must learn class components first | **Function components + hooks** are the modern standard |""",
        ),
    )
    body += section(
        "Library vs Framework",
        """| | **React (library)** | **Framework (Next.js, Remix, Angular)** |
|---|---------------------|----------------------------------------|
| Scope | UI rendering layer | Routing, data conventions, build opinions |
| Flexibility | High — pick your tools | More structure out of the box |
| Learning curve | Smaller core API | More concepts upfront |
| Best for | SPAs, embedding widgets, learning UI fundamentals | Production apps needing full-stack patterns |

**Next.js** and **Remix** are **frameworks built on React**. You learn React first, then frameworks add file-based routing, server components, and deployment patterns.""",
    )
    body += section(
        "History of React",
        subsection(
            "Timeline",
            """```
2011  — Facebook engineers face slow, complex UIs in News Feed
2013  — React open-sourced at JSConf; "virtual DOM" idea gains attention
2015  — React Native (mobile) announced
2016  — React 15; widespread adoption begins
2017  — React 16 ("Fiber") — rewrite of core engine for smoother updates
2018  — Hooks introduced (useState, useEffect) — functions replace classes for most code
2020  — React 17 — gradual upgrades, no new developer-facing features
2022  — React 18 — concurrent rendering, automatic batching, Strict Mode improvements
2024+ — React 19 — Actions, use(), improved form handling (check react.dev for latest)
```

Understanding this timeline explains why older tutorials show **class components** while modern ones use **hooks**.""",
        ),
    )
    body += section(
        "Where React Runs",
        subsection(
            "In the browser (most common)",
            "Vite or Create React App bundles your components into JavaScript that runs in the user's browser — a **Single Page Application (SPA)**.",
        )
        + subsection(
            "On the server",
            "Next.js and Remix can render React on the server (**SSR**) so users get HTML faster and SEO improves.",
        )
        + subsection(
            "On mobile",
            "**React Native** uses React's component model for iOS and Android apps (different primitives: `<View>` instead of `<div>`).",
        )
        + subsection(
            "Everywhere else",
            "Desktop (Electron), TV apps, documentation sites, design tools — if there is a UI, React may power it.",
        ),
    )
    body += section(
        "Prerequisites from JavaScript",
        """You completed (or are reviewing) the CodeShelf JavaScript course. These skills matter daily in React:

| JavaScript topic | Used in React for |
|------------------|-------------------|
| `const` / `let` | State, bindings |
| Arrow functions | Components, event handlers |
| Destructuring | Props: `function Card({ title })` |
| Template literals | Strings in JSX |
| Arrays + `.map()` | Rendering lists |
| Modules (`import`/`export`) | Splitting components across files |
| Promises / `async` | Data fetching |
| Spread `{...obj}` | Immutable state updates |
| Truthy/falsy | Conditional rendering `{show && <Modal />}` |

If any row feels shaky, pause and review that JavaScript chapter before continuing.""",
    )
    body += section(
        "Setting Up with Vite",
        defn(
            "Vite is a modern build tool that starts a dev server instantly and updates the browser in milliseconds when you save a file (Hot Module Replacement)."
        )
        + subsection(
            "Create a new project",
            """Open a terminal in the folder where you keep projects:

```bash
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install
npm run dev
```

Open the URL printed in the terminal (usually `http://localhost:5173`).

**TypeScript variant:**

```bash
npm create vite@latest my-react-app -- --template react-ts
```

Files use `.tsx` instead of `.jsx`; types help catch mistakes early.""",
        )
        + subsection(
            "Scripts in package.json",
            """| Script | Command | Purpose |
|--------|---------|---------|
| `dev` | `npm run dev` | Local development server |
| `build` | `npm run build` | Production bundle in `dist/` |
| `preview` | `npm run preview` | Preview production build locally |""",
        ),
    )
    body += section(
        "Project Structure Explained",
        """```text
my-react-app/
├── public/              # Static files copied as-is (favicon)
├── src/
│   ├── assets/        # Images/fonts imported in code
│   ├── App.jsx          # Root component of your app
│   ├── App.css          # Styles for App
│   ├── main.jsx         # Entry — mounts React into the page
│   └── index.css        # Global styles
├── index.html           # Single HTML page with <div id="root">
├── package.json         # Dependencies and scripts
└── vite.config.js       # Vite configuration
```

**Rule of thumb:** Put UI in `src/` components, not in `index.html`. The HTML file is a thin shell.""",
    )
    body += section(
        "The Entry Point main.jsx",
        """```jsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

| Piece | Role |
|-------|------|
| `createRoot` | React 18 API — creates a root that supports concurrent features |
| `document.getElementById('root')` | The DOM node from `index.html` |
| `<App />` | Your component tree starts here |
| `StrictMode` | Development-only checks (see below) |

Everything visible in the app is a descendant of `<App />`.""",
    )
    body += section(
        "Your First Component",
        defn(
            "A **component** is a JavaScript function whose name starts with a capital letter and that returns JSX (UI markup)."
        )
        + """```jsx
// src/Welcome.jsx
function Welcome() {
  return (
    <div>
      <h1>Hello, CodeShelf!</h1>
      <p>My first React component.</p>
    </div>
  );
}

export default Welcome;
```

```jsx
// src/App.jsx
import Welcome from './Welcome.jsx'

function App() {
  return (
    <main>
      <Welcome />
    </main>
  )
}

export default App
```

`<Welcome />` looks like HTML but is a **function call** that returns an element description.""",
    )
    body += section(
        "Component Naming Rules",
        """| Rule | Good | Bad |
|------|------|-----|
| PascalCase name | `UserProfile` | `userProfile`, `user-profile` |
| File matches component | `UserProfile.jsx` | `profile.jsx` with `UserProfile` inside |
| Custom components capitalized in JSX | `<Welcome />` | `<welcome />` (browser treats as HTML tag) |
| One main idea per file | `Button.jsx` → `Button` | Five unrelated components in one file |""",
    )
    body += section(
        "Imports and Exports",
        subsection(
            "Default export",
            """```jsx
export default function App() { ... }
import App from './App.jsx'  // name can differ when importing
```""",
        )
        + subsection(
            "Named export",
            """```jsx
export function formatDate(d) { ... }
import { formatDate } from './utils.js'
```""",
        )
        + subsection(
            "Omitting extension",
            "Vite allows `import App from './App'` — both work; be consistent in your project.",
        ),
    )
    body += section(
        "Declarative vs Imperative UI",
        """| Style | You write | Example |
|-------|-----------|---------|
| **Imperative** | Step-by-step DOM instructions | `el.textContent = x` |
| **Declarative** | What UI should look like for state | `return <p>{count}</p>` |

React is **declarative**: you describe the target UI; React reconciles the DOM.""",
    )
    body += section(
        "Virtual DOM and Reconciliation",
        subsection(
            "Virtual DOM",
            "An in-memory tree describing UI. On each update, React builds a new tree and **diffs** it against the previous one.",
        )
        + subsection(
            "Reconciliation",
            "The process of computing minimal DOM changes. **Keys** on lists help React match items correctly (Chapter 4).",
        )
        + subsection(
            "Why you must not mutate state",
            "React detects many changes by **reference**. Mutating an array in place may skip re-renders. Always create new objects/arrays when updating state (Chapter 3).",
        ),
    )
    body += section(
        "React 18 and Beyond",
        """| Feature | Benefit |
|---------|---------|
| Concurrent rendering | Keeps UI responsive during heavy updates |
| Automatic batching | Multiple `setState` calls in more places merge into one render |
| `createRoot` | Required entry API |
| Transitions | Mark updates as low priority (`useTransition`) |

You do not need every feature on day one — they exist as you scale.""",
    )
    body += section(
        "StrictMode Explained",
        """```jsx
<StrictMode>
  <App />
</StrictMode>
```

- Runs **only in development**
- Double-invokes some functions to expose missing cleanup
- Warns about deprecated APIs

Do not remove StrictMode to "fix" double logs — fix the underlying effect cleanup instead.""",
    )
    body += section(
        "React Developer Tools",
        """Install the browser extension **React Developer Tools**:

1. Open your app at `localhost:5173`
2. Open DevTools → **Components** tab
3. Click `App` → see props, hooks state
4. Use **Profiler** later for performance (Chapter 11)

This is as essential as `console.log` for React work.""",
    )
    body += section(
        "React vs Other Tools",
        """| Tool | Notes |
|------|-------|
| **Vue** | Progressive framework; template or JSX-like syntax |
| **Angular** | Full framework with TypeScript-first approach |
| **Svelte** | Compile-time framework; less runtime |
| **jQuery** | DOM utility (pre-component era); not comparable for large apps |

React's job market and ecosystem remain among the largest. Learning React transfers well to React Native and Next.js.""",
    )
    body += section(
        "The React Ecosystem",
        """| Category | Popular choices |
|----------|-----------------|
| Routing | React Router, TanStack Router |
| Server state | TanStack Query |
| Client state | Zustand, Redux Toolkit, Jotai |
| Styling | CSS Modules, Tailwind, styled-components |
| UI kits | shadcn/ui, MUI, Chakra |
| Testing | Vitest + React Testing Library |
| Meta-frameworks | Next.js, Remix |

Learn the **React core** first; add libraries when a real problem appears.""",
    )
    body += section(
        "Best Practices for Beginners",
        """1. **Keep components small** — if a file exceeds ~150 lines, consider splitting.
2. **Colocate files** — styles and tests near the component when possible.
3. **Use function components** — avoid class components in new code.
4. **Read error messages** — React errors often link to docs.
5. **Commit often** — small Git commits make debugging easier.
6. **Build while reading** — type every example yourself.""",
    )
    body += mistakes_table(
        [
            ("`<welcome />` lowercase", "React treats it as HTML element, not your component", "Use `<Welcome />`"),
            ("Forgetting `export default`", "Import fails or imports wrong thing", "Export the component"),
            ("Editing `index.html` for app UI", "Bypasses component system", "Put UI in `src/`"),
            ("Wrong import path", "Module not found error", "Use `./Welcome.jsx` relative paths"),
            ("Putting hooks in `main.jsx`", "Hooks only work in components", "Keep hooks inside components"),
        ]
    )
    body += interview_section(
        [
            (
                "What is React and why use it?",
                "**Answer framework:** React is a JavaScript library for building UIs with reusable components. It uses a declarative model and virtual DOM diffing for efficient updates. Benefits: component reuse, predictable data flow, large ecosystem, strong hiring demand.",
            ),
            (
                "What is the difference between React and Next.js?",
                "React is the UI library. Next.js is a **framework** on top of React adding routing, SSR, API routes, and deployment conventions.",
            ),
            (
                "What is JSX?",
                "JSX is syntax sugar for `React.createElement`. It is compiled to JavaScript before the browser runs it.",
            ),
            (
                "What is the Virtual DOM?",
                "An in-memory representation of UI. React diffs new vs old virtual trees and updates only changed real DOM nodes.",
            ),
            (
                "What does createRoot do?",
                "React 18 entry API that creates a root capable of concurrent rendering, replacing legacy `ReactDOM.render`.",
            ),
            (
                "What is a React component?",
                "A function (or class) that returns UI. Must be capitalized when used in JSX.",
            ),
            (
                "What is StrictMode?",
                "Development-only wrapper that runs extra checks to surface unsafe lifecycles and missing effect cleanup.",
            ),
        ]
    )
    body += exercises_section(
        [
            (
                1,
                "⭐",
                "Scaffold Your App",
                "Create a Vite React app named `codeshelf-hello`. Change the `<title>` in `index.html` and the heading in `App.jsx`.",
                "Use `npm create vite@latest` with the `react` template.",
                "```bash\nnpm create vite@latest codeshelf-hello -- --template react\ncd codeshelf-hello\nnpm install\nnpm run dev\n```",
            ),
            (
                2,
                "⭐",
                "Profile Component",
                "Create `Profile.jsx` with your name, role, and bio. Import and render it inside `App.jsx`.",
                "Default export Profile; import without curly braces.",
                "```jsx\nfunction Profile() {\n  return (\n    <section>\n      <h2>Your Name</h2>\n      <p>Role: Student</p>\n      <p>Bio: Learning React.</p>\n    </section>\n  );\n}\nexport default Profile;\n```",
            ),
            (
                3,
                "⭐⭐",
                "Header and Footer",
                "Add `Header.jsx` and `Footer.jsx`. Compose all three in `App` with a `<main>` between header and footer.",
                "App only assembles; each child owns its markup.",
                "```jsx\nfunction App() {\n  return (\n    <>\n      <Header />\n      <main><Profile /></main>\n      <Footer />\n    </>\n  );\n}\n```",
            ),
            (
                4,
                "⭐⭐",
                "Explore DevTools",
                "Install React DevTools. Find `App` and `Profile` in the tree. Change text in code and watch HMR update.",
                "Components tab shows hierarchy; pencil icon edits props in dev only.",
                "No code — observation exercise. Note which component re-renders when you edit `Profile.jsx`.",
            ),
            (
                5,
                "⭐⭐",
                "Declarative vs Imperative",
                "In comments, rewrite a vanilla JS counter (getElementById) as a React `Counter` component sketch without running it.",
                "Focus on state + JSX instead of manual DOM.",
                "```jsx\n// Imperative: update DOM directly\n// Declarative:\nfunction Counter() {\n  const [n, setN] = useState(0);\n  return <button onClick={() => setN(n + 1)}>{n}</button>;\n}\n```",
            ),
        ]
    )
    body += summary_table(
        [
            ("React", "UI library — components + declarative rendering"),
            ("Vite", "Fast dev server and production builds"),
            ("Component", "Function returning JSX; PascalCase"),
            ("main.jsx", "Mounts `<App />` into `#root`"),
            ("Virtual DOM", "Efficient updates via diffing"),
        ]
    )
    body += next_ch("./ch02-jsx-and-components.md", "Chapter 2: JSX & Components")
    return fm(
        "Introduction — What is React?",
        "React library overview, Vite project setup, project structure, and your first component.",
        1,
        ["react", "introduction", "vite", "components"],
    ) + title + body


# Additional chapter functions ch02-ch15 follow same pattern but shorter in this file;
# we'll append them in parts via exec or extend the file.

def ch00():
    """Light enhancement of course overview."""
    path = OUT / "ch00-course-overview.md"
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    extra = """

---

## What you will build

By the end of this course you will have built mental models and mini-projects covering:

- Interactive UI with **state** and **events**
- Lists, forms, and **data fetching**
- **Routing** and **global state** with Context
- **Performance** and **testing** fundamentals
- **Interview-ready** explanations of hooks and rendering

## Study tips

| Tip | Why |
|-----|-----|
| Type every example | Muscle memory beats copy-paste |
| Use React DevTools | See state and re-renders live |
| Read error messages | React links to docs |
| Build one project across chapters | Concepts stick when reused |

## Time estimate

| Pace | Duration |
|------|----------|
| Part-time (1–2 hrs/day) | 4–6 weeks |
| Full-time focus | 1–2 weeks |

"""
    if "## Study tips" not in existing:
        path.write_text(existing.rstrip() + extra, encoding="utf-8")
    return existing


if __name__ == "__main__":
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from react_chapters_bulk import CHAPTER_BUILDERS

    OUT.mkdir(parents=True, exist_ok=True)
    ch00()

    from react_chapters_bulk import _pad_to_min_lines

    chapters: dict[str, str] = {
        "ch01-introduction.md": _pad_to_min_lines(ch01(), "Introduction", 650)
    }
    for fname, builder in CHAPTER_BUILDERS:
        chapters[fname] = builder()

    for name in sorted(chapters.keys()):
        content = chapters[name]
        (OUT / name).write_text(content, encoding="utf-8")
        print(f"{name}: {len(content.splitlines())} lines")
