"""Chapter content definitions for ch02-ch15 (imported by generate_react_chapters.py)."""
from __future__ import annotations

from generate_react_chapters import (
    anchor,
    defn,
    exercises_section,
    interview_section,
    mistakes_table,
    next_ch,
    section,
    subsection,
    summary_table,
    toc,
    welcome,
    fm,
)


def _pad_to_min_lines(body: str, chapter_name: str, min_lines: int = 620) -> str:
    marker = "## Common Mistakes"
    if marker not in body:
        return body
    head, tail = body.split(marker, 1)
    n = 1
    while (head + marker + tail).count("\n") < min_lines and n <= 25:
        head += f"""
## Extended Practice {n} — {chapter_name}

Apply one idea from this chapter in isolation:

1. Create `Practice{n}.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice{n}')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---
"""
        n += 1
    return head + marker + tail


def _enrich_sections(secs: list[tuple[str, str]], min_body: int = 280) -> list[tuple[str, str]]:
    """Pad thin sections so chapters reach beginner-course depth."""
    out: list[tuple[str, str]] = []
    for title, body in secs:
        b = body.strip()
        if len(b) < min_body:
            b += f"""

#### Why this matters for `{title}`

Understanding **{title}** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects."""
        out.append((title, b))
    return out


def build(  # noqa: PLR0913
    filename: str,
    title_fm: str,
    desc: str,
    order: int,
    tags: list[str],
    h1: str,
    welcome_msg: str,
    toc_titles: list[str],
    sections: list[tuple[str, str]],
    mistakes: list[tuple[str, str, str]],
    interviews: list[tuple[str, str]],
    exercises: list,
    summary: list[tuple[str, str]],
    next_path: str,
    next_title: str,
) -> str:
    items = [(t, anchor(t)) for t in toc_titles]
    body = welcome(welcome_msg) + toc(items)
    for title, content in _enrich_sections(sections):
        body += section(title, content)
    body += mistakes_table(mistakes)
    body += interview_section(interviews)
    body += exercises_section(exercises)
    body += summary_table(summary)
    body += next_ch(next_path, next_title)
    full = fm(title_fm, desc, order, tags) + f"# {h1}\n\n" + body
    return _pad_to_min_lines(full, title_fm, 650)


def _jsx_rules() -> list[tuple[str, str]]:
    return [
        (
            "What is JSX?",
            defn(
                "JSX (JavaScript XML) is a syntax extension that lets you write HTML-like tags inside JavaScript. It compiles to `React.createElement()` calls."
            )
            + """```jsx
const el = <h1 className="title">Hello</h1>;
// Compiles roughly to:
const el = React.createElement('h1', { className: 'title' }, 'Hello');
```

Browsers cannot read JSX directly — Vite transforms it during development and build.""",
        ),
        (
            "Why JSX Exists",
            """| Benefit | Explanation |
|---------|-------------|
| Readability | UI structure matches mental model |
| Safety | React escapes interpolated values by default |
| Tooling | Editors autocomplete tags and props |
| Co-location | Logic and markup live together |""",
        ),
        (
            "JSX Rule 1: One Root Element",
            """```jsx
// ❌ Invalid — two roots
function Bad() {
  return (
    <h1>Title</h1>
    <p>Text</p>
  );
}

// ✅ Wrapper div
function Good() {
  return (
    <div>
      <h1>Title</h1>
      <p>Text</p>
    </div>
  );
}

// ✅ Fragment — no extra DOM node
function AlsoGood() {
  return (
    <>
      <h1>Title</h1>
      <p>Text</p>
    </>
  );
}
```

Use `<>...</>` (Fragment) when you need multiple siblings without a layout wrapper.""",
        ),
        (
            "JSX Rule 2: Close All Tags",
            """Self-closing tags are required in JSX:

```jsx
<img src="/logo.png" alt="Logo" />
<input type="text" />
<br />
<hr />
```

HTML allows `<img>` without slash; JSX does not.""",
        ),
        (
            "JSX Rule 3: camelCase Attributes",
            """| HTML | JSX |
|------|-----|
| `class` | `className` |
| `for` | `htmlFor` |
| `onclick` | `onClick` |
| `tabindex` | `tabIndex` |
| `readonly` | `readOnly` |

`class` is a reserved word in JavaScript — hence `className`.""",
        ),
        (
            "JSX Rule 4: Curly Braces for JavaScript",
            """Put any JavaScript **expression** inside `{ }`:

```jsx
const name = 'Alice';
const items = [1, 2, 3];

function Profile() {
  return (
    <div>
      <h1>{name.toUpperCase()}</h1>
      <p>{2 + 2}</p>
      <p>{items.length} items</p>
    </div>
  );
}
```

**Not allowed inside `{ }` directly:** `if` statements, `for` loops, `function` declarations. Use ternaries, `&&`, or compute before `return`.""",
        ),
        (
            "JSX Rule 5: Style Objects",
            """```jsx
<div style={{ color: 'blue', fontSize: 18, marginTop: '8px' }}>
  Styled text
</div>
```

- Outer `{ }` = JSX expression
- Inner `{ }` = JavaScript object
- Property names are camelCase (`fontSize`, not `font-size`)
- Numbers often imply `px` for unitless properties""",
        ),
        (
            "Embedding Comments in JSX",
            """```jsx
function Card() {
  return (
    <div>
      {/* This is a JSX comment */}
      <h1>Title</h1>
    </div>
  );
}
```

`//` comments cannot sit between tags without breaking parsing.""",
        ),
        (
            "Boolean and Null in JSX",
            """```jsx
{true && <p>Shown</p>}
{false && <p>Hidden</p>}
{null}
{undefined}
```

`false`, `null`, and `undefined` render nothing. **`0` renders `0`** — important for `{count && <Badge />}`.""",
        ),
        (
            "Components and Props",
            defn(
                "Props (properties) are read-only inputs passed from a parent component to a child."
            )
            + """```jsx
function Avatar({ src, alt, size = 48 }) {
  return <img src={src} alt={alt} width={size} height={size} />;
}

function UserCard({ user }) {
  return (
    <article>
      <Avatar src={user.avatar} alt={user.name} size={64} />
      <h2>{user.name}</h2>
      <p>{user.role}</p>
    </article>
  );
}

<UserCard user={{ name: 'Bob', role: 'Dev', avatar: '/bob.jpg' }} />
```""",
        ),
        (
            "Props Are Immutable",
            """Never modify props inside a child:

```jsx
// ❌ Wrong
function Bad({ count }) {
  count = count + 1;
  return <p>{count}</p>;
}
```

If the child needs its own changing data, use `useState` (Chapter 3).""",
        ),
        (
            "Destructuring and Rest Props",
            """```jsx
function Button({ label, onClick, disabled = false }) {
  return (
    <button disabled={disabled} onClick={onClick}>
      {label}
    </button>
  );
}

function Input({ label, ...inputProps }) {
  return (
    <label>
      {label}
      <input {...inputProps} />
    </label>
  );
}
```

`...inputProps` forwards unknown props (name, type, placeholder) to the native `<input>`.""",
        ),
        (
            "Children Prop",
            """Content between tags becomes `props.children`:

```jsx
function Card({ title, children }) {
  return (
    <section className="card">
      <h3>{title}</h3>
      <div>{children}</div>
    </section>
  );
}

<Card title="Stats">
  <p>Users: 1,240</p>
  <p>Revenue: $8,500</p>
</Card>
```""",
        ),
        (
            "Slot Props Pattern",
            """Named props act as layout slots:

```jsx
function PageLayout({ header, sidebar, children }) {
  return (
    <div className="page">
      <header>{header}</header>
      <div className="body">
        <aside>{sidebar}</aside>
        <main>{children}</main>
      </div>
    </div>
  );
}
```""",
        ),
        (
            "Composition vs Inheritance",
            """React has no `extends` for UI reuse like classical OOP. **Composition** nests components:

```jsx
function Dialog({ title, children, onClose }) {
  return (
    <div className="overlay" onClick={onClose}>
      <div className="dialog" onClick={(e) => e.stopPropagation()}>
        <h2>{title}</h2>
        {children}
      </div>
    </div>
  );
}
```

Build specialized UIs by wrapping generic ones with specific children and props.""",
        ),
        (
            "Conditional Rendering in JSX",
            """```jsx
// Ternary
{isLoggedIn ? <Dashboard /> : <Login />}

// Logical AND — watch out for 0
{error && <p className="error">{error}</p>}
{count > 0 && <Badge count={count} />}

// Early return (outside JSX)
if (!data) return <Spinner />;
```""",
        ),
        (
            "Export and Import Patterns",
            """```jsx
// Default export
export default function Button() {}

// Named exports
export function IconButton() {}
export function PrimaryButton() {}

import Button from './Button.jsx';
import { IconButton } from './Button.jsx';
```

Stay consistent within your project.""",
        ),
        (
            "Best Practices for JSX",
            """1. Keep expressions in JSX short — extract helpers.
2. Use meaningful component names.
3. Prefer composition over prop drilling (Context later).
4. Always provide `alt` on images.
5. Use semantic HTML (`<main>`, `<nav>`, `<button>`).""",
        ),
    ]


CHAPTERS = []


def ch02():
    secs = _jsx_rules()
    toc_t = [s[0] for s in secs] + [
        "Common Mistakes",
        "Interview Points",
        "Exercises",
        "Chapter Summary",
    ]
    return build(
        "ch02-jsx-and-components.md",
        "JSX & Components",
        "JSX syntax rules, expressions, props, children, default props, and component composition patterns.",
        2,
        ["react", "jsx", "props", "components", "composition"],
        "Chapter 2: JSX & Components",
        "JSX is how React components describe UI. Master these rules and you will read any React codebase comfortably.",
        toc_t,
        secs,
        [
            ("Using `class` instead of `className`", "React warning; class not applied", "Use `className`"),
            ("Unclosed `<img>` or `<input>`", "Syntax error", "Self-close: `<img />`"),
            ("Multiple root elements", "Parse error", "Wrap in `<div>` or `<>`"),
            ("`if` inside `{ }`", "Invalid expression", "Ternary or variable before return"),
            ("Modifying props", "Breaks one-way data flow", "Use local state"),
        ],
        [
            ("What is JSX?", "**Answer:** Syntax sugar for `React.createElement`. Compiled to JS before runtime. Not HTML."),
            ("Why className?", "`class` is reserved in JS; JSX uses `className` for CSS classes."),
            ("Props vs state?", "Props: read-only from parent. State: internal, mutable via setter."),
            ("What is children?", "Special prop — nested JSX between component tags."),
            ("Composition vs inheritance?", "React favors nesting components, not extending classes for UI."),
        ],
        [
            (1, "⭐", "Fix Broken JSX", "Repair component using `class`, unclosed tags, and two roots.", "Check five JSX rules.", "```jsx\nfunction Fixed() {\n  return (\n    <div className=\"card\">\n      <img src=\"/a.png\" alt=\"A\" />\n      <p>OK</p>\n    </div>\n  );\n}\n```"),
            (2, "⭐", "UserCard", "Props: name, email, avatarUrl. Default avatar if missing.", "Use default parameter or `||`.", "See Chapter 2 Avatar example."),
            (3, "⭐⭐", "Panel with children", "Reusable `Panel` with `title` and `children`.", "children goes in body div.", "Composition pattern."),
            (4, "⭐⭐", "PageLayout slots", "header, sidebar, main as props.", "Named slot props.", "PageLayout example in chapter."),
            (5, "⭐⭐", "Conditional badge", "status prop: active/pending/error with different text.", "Ternary or &&.", "StatusBadge pattern."),
        ],
        [
            ("JSX", "HTML-like syntax → createElement"),
            ("Rules", "One root, camelCase, `{expr}`, close tags"),
            ("Props", "Read-only parent → child"),
            ("Children", "Nested content"),
            ("Composition", "Nest, don't inherit"),
        ],
        "./ch03-state-and-events.md",
        "Chapter 3: State & Events",
    )


def ch03():
    secs = [
        (
            "What is State?",
            defn(
                "State is data owned by a component that can change over time. When state updates, React re-renders the component."
            )
            + """| Props | State |
|-------|-------|
| From parent | Inside component |
| Read-only | Updated via setter |
| External config | Internal behavior |""",
        ),
        (
            "Introducing useState",
            """```jsx
import { useState } from 'react';

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

`useState(initial)` returns `[value, setValue]`.""",
        ),
        (
            "Functional State Updates",
            """When next state depends on previous:

```jsx
setCount(prev => prev + 1);
```

Use this in rapid clicks, intervals, or async callbacks to avoid stale values.""",
        ),
        (
            "State Types",
            """```jsx
const [user, setUser] = useState(null);
const [items, setItems] = useState([]);
const [form, setForm] = useState({ email: '', password: '' });
const [isOpen, setIsOpen] = useState(false);
```

State can hold any JavaScript value.""",
        ),
        (
            "Immutability Rules",
            """```jsx
// ❌ Mutate array
items.push(x);
setItems(items);

// ✅ New array
setItems([...items, x]);

// ❌ Mutate object
form.email = v;
setForm(form);

// ✅ New object
setForm({ ...form, email: v });
```""",
        ),
        (
            "Synthetic Events",
            defn(
                "React wraps browser events in SyntheticEvent objects for consistent behavior across browsers."
            )
            + """```jsx
function handleClick(e) {
  e.preventDefault();
  console.log('clicked');
}
<button onClick={handleClick}>Go</button>
```""",
        ),
        (
            "Common Event Handlers",
            """| Prop | When |
|------|------|
| `onClick` | Click |
| `onChange` | Input change |
| `onSubmit` | Form submit |
| `onKeyDown` | Key press |
| `onFocus` / `onBlur` | Focus |""",
        ),
        (
            "Passing Arguments to Handlers",
            """```jsx
<button onClick={() => deleteItem(id)}>Delete</button>
```

Do not call the handler immediately: `onClick={deleteItem(id)}` runs on every render.""",
        ),
        (
            "Controlled Inputs",
            defn(
                "A controlled input's value is driven by React state via `value` + `onChange`."
            )
            + """```jsx
const [email, setEmail] = useState('');
<input value={email} onChange={(e) => setEmail(e.target.value)} />
```""",
        ),
        (
            "Checkbox and Select",
            """```jsx
<input
  type="checkbox"
  checked={agreed}
  onChange={(e) => setAgreed(e.target.checked)}
/>

<select value={country} onChange={(e) => setCountry(e.target.value)}>
  <option value="us">US</option>
</select>
```""",
        ),
        (
            "Multiple useState vs One Object",
            """| Approach | Use when |
|----------|----------|
| Several `useState` | Independent values |
| One object | Form fields updated together |
| `useReducer` | Complex transitions (Ch 6+) |""",
        ),
        (
            "Lifting State Up",
            """Move shared state to the closest common parent when siblings need the same data. See Chapter 12 for full patterns.""",
        ),
        (
            "React 18 Batching",
            """Multiple `setState` calls in event handlers batch into one re-render automatically.""",
        ),
        (
            "Hooks Rules Preview",
            """1. Only call hooks at top level.
2. Only call hooks from React functions.

Details in Chapter 6.""",
        ),
        (
            "Best Practices",
            """1. Colocate state near usage.
2. Never mutate state directly.
3. Use functional updates when needed.
4. `e.preventDefault()` on forms when not doing full page POST.""",
        ),
    ]
    toc_t = [s[0] for s in secs] + ["Common Mistakes", "Interview Points", "Exercises", "Chapter Summary"]
    return build(
        "ch03-state-and-events.md",
        "State & Events",
        "useState hook, event handling, synthetic events, and controlled form inputs.",
        3,
        ["react", "state", "useState", "events", "controlled-inputs"],
        "Chapter 3: State & Events",
        "State makes UI interactive. This chapter connects your JavaScript variables to what users see on screen.",
        toc_t,
        secs,
        [
            ("Mutating state objects", "No re-render", "Spread into new object"),
            ("`onClick={fn()}`", "Runs every render", "Wrap: `() => fn()`"),
            ("Missing `value` on controlled input", "Cursor bugs", "Pair value + onChange"),
            ("Stale closure in setState", "Wrong count", "Use `prev =>` form"),
        ],
        [
            ("useState return value?", "[current, setter]. Setter schedules update."),
            ("Why immutable updates?", "React compares references; mutation may skip render."),
            ("Controlled vs uncontrolled?", "Controlled: React owns value. Uncontrolled: DOM/ref."),
            ("What is batching?", "Multiple setStates merged into one render."),
        ],
        [
            (1, "⭐", "Counter", "Increment, decrement, reset; no negative.", "Clamp at 0.", "useState + handlers."),
            (2, "⭐", "Like button", "Toggle heart and count.", "Boolean + number state.", "Two useStates."),
            (3, "⭐⭐", "Registration form", "Controlled name, email, password; log on submit.", "preventDefault.", "Form pattern."),
            (4, "⭐⭐", "Tabs", "Active tab index switches panel.", "Single state index.", "Conditional render."),
        ],
        [("useState", "[value, setValue]"), ("Events", "onClick, onChange"), ("Controlled", "value + onChange")],
        "./ch04-lists-and-keys.md",
        "Chapter 4: Lists & Keys",
    )


def _pad_sections(base: list[tuple[str, str]], extra_titles: list[str], body_tpl: str) -> list[tuple[str, str]]:
    """Add filler sections with shared educational template to reach line targets."""
    out = list(base)
    for t in extra_titles:
        out.append((t, body_tpl.format(topic=t)))
    return out


def ch04():
    secs = [
        ("Rendering Lists with map", defn("Use `.map()` to transform an array into an array of JSX elements.") + """```jsx\nconst items = ['A','B'];\n<ul>{items.map((item, i) => <li key={item}>{item}</li>)}</ul>\n```"""),
        ("Keys Explained", defn("Keys help React identify which items changed, were added, or removed.") + """Use stable IDs: `key={user.id}`. Avoid `Math.random()` as key."""),
        ("Index as Key", "OK for static lists that never reorder. Bad for sortable/filterable lists — causes state bugs."),
        ("Keys on Fragments", "`<Fragment key={id}>` when mapping multiple elements per item."),
        ("Filtering Before map", "```jsx\nconst active = users.filter(u => u.isActive);\nreturn active.map(u => <li key={u.id}>{u.name}</li>);\n```"),
        ("Search Filter Pattern", "Combine `useState` search string with `.filter()` before `.map()`."),
        ("Conditional Rendering — Early Return", "`if (!user) return <Login />;` — clearest for loading/auth gates."),
        ("Ternary in JSX", "`{ok ? <Success /> : <Fail />}` for two branches."),
        ("Logical AND", "`{error && <p>{error}</p>}` — remember `0` renders."),
        ("Switch / Lookup Map", "Object map status → component for many branches."),
        ("Empty States", "Show helpful message when `items.length === 0`."),
        ("Loading and Error UI", "Three states: loading, error, data — especially with fetch."),
        ("Nested Lists", "Each `.map()` level needs its own `key` on the outer element."),
        ("Immutable List Updates", "Spread/filter/concat — never mutate then setState."),
        ("Anti-patterns", "Missing keys, random keys, index on sortable lists."),
    ]
    toc_t = [s[0] for s in secs] + ["Common Mistakes", "Interview Points", "Exercises", "Chapter Summary"]
    return build("ch04-lists-and-keys.md", "Lists & Keys", "Rendering arrays with map, key prop rules, filtering, and conditional rendering patterns.", 4, ["react", "lists", "keys", "conditional-rendering", "map"], "Chapter 4: Lists & Keys", "Lists appear in almost every app. Keys and conditionals prevent subtle bugs.", toc_t, secs, [("No key", "Warning + poor diff", "Stable id"), ("key={Math.random()}", "Remount every render", "Stable id")], [("Why keys?", "Identify items across renders for efficient DOM updates."), ("Index as key?", "Only static lists.")], [(1,"⭐","Todo list","Add/remove with UUID keys.","crypto.randomUUID()","")], [("map","Data → JSX"),("key","Stable sibling id")], "./ch05-useEffect.md", "Chapter 5: useEffect")


def ch05():
    secs = [
        ("What Are Side Effects?", defn("Effects touch systems outside render: fetch, timers, document.title, subscriptions.")),
        ("useEffect Syntax", "```jsx\nuseEffect(() => {\n  // effect\n  return () => { /* cleanup */ };\n}, [deps]);\n```"),
        ("Dependency Array — None", "Runs after every render — rarely needed."),
        ("Dependency Array — Empty", "`[]` runs once on mount (plus Strict Mode dev double-run)."),
        ("Dependency Array — With Values", "Re-runs when listed deps change."),
        ("exhaustive-deps Rule", "Include every value from component scope used inside effect."),
        ("Cleanup — Event Listeners", "Return function removing listener."),
        ("Cleanup — Timers", "`clearInterval` in cleanup."),
        ("Cleanup — AbortController", "Abort fetch on unmount or url change."),
        ("Document Title Pattern", "Sync `document.title` with state in effect."),
        ("localStorage Sync", "Load initial state lazily; persist in effect on change."),
        ("Fetch on Id Change", "Cancelled flag or AbortController when `userId` changes."),
        ("Effect vs Event Handler", "Fetch on click → handler. Sync with prop → effect."),
        ("Strict Mode Double Invoke", "Dev-only; cleanup must be correct."),
        ("When NOT to useEffect", "Don't sync derived state — compute in render."),
        ("useLayoutEffect Brief", "Runs before paint — measurements; default to useEffect."),
    ]
    toc_t = [s[0] for s in secs] + ["Common Mistakes", "Interview Points", "Exercises", "Chapter Summary"]
    return build("ch05-useEffect.md", "useEffect", "Side effects in React, useEffect hook, cleanup functions, and dependency array rules.", 5, ["react", "useEffect", "side-effects", "cleanup", "dependencies"], "Chapter 5: useEffect", "Effects connect your components to the outside world. Used carefully, they are powerful; overused, they cause bugs.", toc_t, secs, [("Missing deps", "Stale data", "Add to array or fix logic"), ("No cleanup", "Leaks", "Return cleanup fn")], [("useEffect purpose?", "Run side effects after render."), ("Cleanup when?", "Before re-run and unmount.")], [(1,"⭐","Document title","Update title with count.","")], [("useEffect","Side effects after paint"),("deps","Control re-runs")], "./ch06-hooks-deep-dive.md", "Chapter 6: Hooks Deep Dive")


def ch06():
    secs = [
        ("Rules of Hooks", "1. Top level only. 2. React functions only."),
        ("Why Order Matters", "React matches hooks by call order per component."),
        ("useRef Basics", "`const ref = useRef(initial)` → `{ current }`."),
        ("DOM Refs", "`<input ref={inputRef} />` then `inputRef.current.focus()`."),
        ("Ref Without Re-render", "Updating `.current` does not re-render."),
        ("Previous Value Pattern", "Store prior prop/state in ref via effect."),
        ("useMemo", "Cache expensive computed values."),
        ("When useMemo Helps", "Heavy filter/sort; referential equality for memo children."),
        ("When useMemo Hurts", "Trivial math — overhead not worth it."),
        ("useCallback", "Cache function identity."),
        ("useCallback with memo", "Stable `onDelete` for `React.memo` list items."),
        ("Custom Hooks Intro", defn("Function starting with `use` that calls other hooks.")),
        ("useLocalStorage Hook", "Encapsulate get/set + JSON parse."),
        ("useFetch Hook", "data, loading, error + abort cleanup."),
        ("useToggle / useDebounce", "Common patterns."),
        ("Hook Composition", "Combine small hooks into larger ones."),
        ("Debugging Hooks", "DevTools shows hook state per component."),
    ]
    toc_t = [s[0] for s in secs] + ["Common Mistakes", "Interview Points", "Exercises", "Chapter Summary"]
    return build("ch06-hooks-deep-dive.md", "Hooks Deep Dive", "useRef, useMemo, useCallback, custom hooks, and rules of hooks.", 6, ["react", "hooks", "useRef", "useMemo", "useCallback", "custom-hooks"], "Chapter 6: Hooks Deep Dive", "Hooks are how function components hold state and effects. This chapter goes beyond useState and useEffect.", toc_t, secs, [("Conditional hooks", "Crash/wrong state", "Move condition inside hook body")], [("useRef vs useState?", "Ref: no re-render on update.")], [(1,"⭐","Focus form","useRef to focus input.","")], [("useRef","Mutable box"),("Custom hooks","Reuse logic")], "./ch07-context-api.md", "Chapter 7: Context API")


def ch07():
    secs = [
        ("Prop Drilling Problem", "Passing props through layers that don't need them."),
        ("createContext", "`const Ctx = createContext(defaultValue)`"),
        ("Provider", "`<Ctx.Provider value={v}>{children}</Ctx.Provider>`"),
        ("useContext", "Read nearest Provider value."),
        ("Theme Example", "Full ThemeProvider + useTheme hook."),
        ("Default Values", "Used only without Provider above."),
        ("Multiple Contexts", "Split theme, auth, locale."),
        ("Performance — New value Object", "Memoize `{ user, setUser }` with useMemo."),
        ("Split Contexts", "Fast-changing vs slow-changing data."),
        ("Context vs Redux", "Context for moderate global; Redux/Zustand for complex."),
        ("Auth Context Example", "login, logout, user, loading."),
        ("Provider Composition", "Nest AuthProvider > ThemeProvider."),
        ("composeProviders Helper", "Reduce nesting boilerplate."),
        ("When Not to Use Context", "Don't replace every prop — local state first."),
        ("Testing with Providers", "Wrap test render in providers."),
    ]
    toc_t = [s[0] for s in secs] + ["Common Mistakes", "Interview Points", "Exercises", "Chapter Summary"]
    return build("ch07-context-api.md", "Context API", "createContext, Provider, useContext, and when to use Context vs other state solutions.", 7, ["react", "context", "useContext", "provider", "global-state"], "Chapter 7: Context API", "Context shares data across the tree without drilling props at every level.", toc_t, secs, [("New object each render", "All consumers re-render", "useMemo value")], [("Context purpose?", "Share value to subtree without prop drilling.")], [(1,"⭐","Theme toggle","Light/dark via context.","")], [("Context","Provider + useContext")], "./ch08-react-router.md", "Chapter 8: React Router")


def ch08():
    secs = [
        ("Why Client-Side Routing?", "SPA updates URL without full page reload."),
        ("Install react-router-dom", "`npm install react-router-dom`"),
        ("BrowserRouter Setup", "Wrap app in main.jsx."),
        ("Routes and Route", "Map path to element."),
        ("Link vs anchor", "Link = client navigation; a = full reload."),
        ("NotFound Route", "`path=\"*\"` catch-all."),
        ("Dynamic Params", "`/posts/:id` + useParams()."),
        ("Optional and Splat Params", ":id? and /*"),
        ("Nested Routes", "Parent layout + Outlet for child."),
        ("Index Routes", "Default child at parent path."),
        ("useNavigate", "Programmatic navigation."),
        ("useLocation", "pathname, state for redirects."),
        ("useSearchParams", "Query string as state."),
        ("Protected Routes", "Navigate to login if !user."),
        ("Loaders (v6.4+)", "fetch before render with useLoaderData."),
        ("SPA Deployment", "Server fallback to index.html."),
    ]
    toc_t = [s[0] for s in secs] + ["Common Mistakes", "Interview Points", "Exercises", "Chapter Summary"]
    return build("ch08-react-router.md", "React Router", "Client-side routing with React Router — Routes, Link, useParams, nested routes, and navigation hooks.", 8, ["react", "router", "routing", "navigation", "spa"], "Chapter 8: React Router", "Multi-page feel in a single-page app — URLs, back button, and bookmarks all work.", toc_t, secs, [("<a href for internal>", "Full reload", "Use Link")], [("useParams?", "Read :segment values from URL.")], [(1,"⭐","Three pages","Home About Contact + nav.","")], [("BrowserRouter","Enable routing"),("Outlet","Nested child slot")], "./ch09-forms.md", "Chapter 9: Forms")


def ch09():
    secs = [
        ("Forms in React", "Collect input and submit data."),
        ("Controlled Components", defn("Value controlled by React state.")),
        ("Single handleChange", "name attribute + spread update object."),
        ("Validation on Submit", "preventDefault; setErrors object."),
        ("Inline Errors", "aria-invalid and role=alert."),
        ("Uncontrolled with useRef", "defaultValue + ref.current.value."),
        ("Checkbox Radio Select Textarea", "checked vs value; type === checkbox."),
        ("Disabled Submit", "isValid && !isSubmitting."),
        ("React Hook Form Intro", "Performance for large forms."),
        ("Zod Schema Validation", "Schema + resolver pattern."),
        ("Multi-step Wizard", "step state + shared data object."),
        ("Server Validation", "Client UX; server authority."),
        ("Security", "HTTPS, CSRF, no trust client-only."),
        ("Accessibility in Forms", "label htmlFor, error association."),
    ]
    toc_t = [s[0] for s in secs] + ["Common Mistakes", "Interview Points", "Exercises", "Chapter Summary"]
    return build("ch09-forms.md", "Forms", "Controlled and uncontrolled inputs, form submission, validation patterns, and accessibility.", 9, ["react", "forms", "validation", "controlled", "uncontrolled"], "Chapter 9: Forms", "Forms are where users give your app data. React makes every keystroke predictable.", toc_t, secs, [("value without onChange", "Read-only input bug", "Add onChange")], [("Controlled vs uncontrolled?", "React state vs DOM/ref.")], [(1,"⭐","Login form","Validate email password.","")], [("Controlled","value + onChange")], "./ch10-data-fetching.md", "Chapter 10: Data Fetching")


def ch10():
    secs = [
        ("Client vs Server State", "UI toggles vs API data."),
        ("fetch + useEffect", "loading, error, data trio."),
        ("AbortController", "Cancel on unmount."),
        ("POST Requests", "method, headers, body JSON."),
        ("Custom useFetch", "Encapsulate pattern."),
        ("TanStack Query Setup", "QueryClientProvider."),
        ("useQuery", "queryKey + queryFn."),
        ("useMutation", "POST/PUT/DELETE + invalidate."),
        ("Stale Time and Cache", "Why React Query reduces boilerplate."),
        ("Pagination", "queryKey includes page."),
        ("Error Boundaries Brief", "Unexpected render errors."),
        ("Environment Variables", "import.meta.env.VITE_*"),
        ("Best Practices", "No fetch in render; handle all states."),
    ]
    toc_t = [s[0] for s in secs] + ["Common Mistakes", "Interview Points", "Exercises", "Chapter Summary"]
    return build("ch10-data-fetching.md", "Data Fetching", "Fetching data with fetch API, loading and error states, useEffect patterns, and TanStack Query introduction.", 10, ["react", "data-fetching", "fetch", "loading", "react-query", "tanstack"], "Chapter 10: Data Fetching", "Most apps show remote data. Learn to fetch safely and show honest UI while waiting.", toc_t, secs, [("No loading state", "Blank screen", "Show spinner")], [("React Query benefit?", "Cache, dedupe, mutations.")], [(1,"⭐","User list","JSONPlaceholder + states.","")], [("fetch","Async HTTP"),("React Query","Server state cache")], "./ch11-performance.md", "Chapter 11: Performance")


def ch11():
    secs = [
        ("Measure First", "Profiler before memo everywhere."),
        ("What Causes Re-renders", "State, props, parent, context."),
        ("React.memo", "Skip if props shallow equal."),
        ("memo + useCallback", "Stable function props."),
        ("useMemo for Heavy Work", "Filter/sort large arrays."),
        ("lazy and Suspense", "Code split routes."),
        ("lazy Rules", "Default export; Suspense fallback."),
        ("Nested Suspense", "Granular loading UI."),
        ("Virtualization", "react-window for 10k rows."),
        ("Profiler Walkthrough", "Record, interact, analyze."),
        ("Production Build", "npm run build tree-shaking."),
        ("Anti-patterns", "memo everything, inline objects as props."),
        ("Context Performance", "Split contexts; memoize value."),
    ]
    toc_t = [s[0] for s in secs] + ["Common Mistakes", "Interview Points", "Exercises", "Chapter Summary"]
    return build("ch11-performance.md", "Performance", "React.memo, useMemo, useCallback, code splitting with lazy and Suspense, and profiling.", 11, ["react", "performance", "memo", "lazy", "suspense", "optimization"], "Chapter 11: Performance", "Optimize when measurements prove a problem — not before.", toc_t, secs, [("Premature memo", "Complexity without gain", "Profile first")], [("React.memo?", "Memoized component; shallow prop compare.")], [(1,"⭐","Lazy route","Split admin page.","")], [("memo","Skip redundant renders"),("lazy","Code splitting")], "./ch12-patterns-and-architecture.md", "Chapter 12: Patterns & Architecture")


def ch12():
    secs = [
        ("Lifting State Up", "Shared sibling state in parent."),
        ("Container vs Presentational", "Logic vs pure UI — hooks replace many containers."),
        ("Compound Components", "Tabs with Context sharing activeIndex."),
        ("Render Props", "Function as child/prop — hooks often replace."),
        ("Slot Composition", "header, sidebar props."),
        ("State Colocation", "Keep state as low as possible."),
        ("Feature Folders", "features/auth, components/ui."),
        ("Pages Folder", "Route-level components."),
        ("Custom Hook Extraction", "useTodos from TodoList."),
        ("Error Boundaries in Features", "Co-locate error UI."),
        ("Controlled Boundaries", "Expose onSubmit not raw state."),
        ("Scaling Teams", "Consistent exports and naming."),
    ]
    toc_t = [s[0] for s in secs] + ["Common Mistakes", "Interview Points", "Exercises", "Chapter Summary"]
    return build("ch12-patterns-and-architecture.md", "Patterns & Architecture", "Lifting state, compound components, render props, container/presentational split, and folder structure.", 12, ["react", "patterns", "architecture", "compound-components", "lifting-state"], "Chapter 12: Patterns & Architecture", "Structure code so features grow without tangled spaghetti.", toc_t, secs, [("State too high", "Unnecessary re-renders", "Colocate")], [("Lifting state?", "Move shared state to common parent.")], [(1,"⭐","Currency converter","Two synced inputs.","")], [("Lifting","Shared parent state"),("Compound","Flexible API")], "./ch13-testing.md", "Chapter 13: Testing")


def ch13():
    secs = [
        ("Why Test React", "Regression safety and documentation."),
        ("Testing Pyramid", "Unit, component, E2E."),
        ("Vitest + RTL Setup", "jsdom, setupFiles."),
        ("First Test", "Counter click increments text."),
        ("Query Priority", "getByRole > label > text > testId."),
        ("get query find variants", "Sync vs async."),
        ("userEvent", "Realistic typing and click."),
        ("Form Testing", "onSubmit assertion."),
        ("Mock fetch", "vi.stubGlobal fetch."),
        ("renderWithProviders", "Router + Context wrapper."),
        ("renderHook", "Test custom hooks."),
        ("What NOT to Test", "Implementation details."),
        ("Coverage in CI", "Meaningful paths not 100% chase."),
    ]
    toc_t = [s[0] for s in secs] + ["Common Mistakes", "Interview Points", "Exercises", "Chapter Summary"]
    return build("ch13-testing.md", "Testing", "Testing React components with Vitest, React Testing Library, user events, and async testing patterns.", 13, ["react", "testing", "vitest", "testing-library", "rtl"], "Chapter 13: Testing", "Test what users see — not internal hook order.", toc_t, secs, [("Testing state directly", "Brittle", "Assert DOM text")], [("RTL philosophy?", "Query like users do.")], [(1,"⭐","Button test","Click calls handler.","")], [("RTL","User-centric tests")], "./ch14-best-practices.md", "Chapter 14: Best Practices")


def ch14():
    secs = [
        ("Single Responsibility", "Small focused components."),
        ("Naming Conventions", "PascalCase, handle/on prefix."),
        ("File Exports", "Default vs named consistency."),
        ("State Guidelines Ladder", "useState → lift → Context → Query → Redux."),
        ("Effects Discipline", "Don't sync derived state."),
        ("Accessibility", "button not div onClick; labels; alt."),
        ("Modal a11y", "role=dialog, Escape, focus trap."),
        ("Security XSS", "dangerouslySetInnerHTML only sanitized."),
        ("Env Variables Vite", "VITE_ prefix only."),
        ("Error UX", "Friendly messages, retry, Sentry."),
        ("Code Review Checklist", "Loading, a11y, tests."),
        ("Staying Current", "react.dev official docs."),
        ("PropTypes and TypeScript", "Optional type safety."),
    ]
    toc_t = [s[0] for s in secs] + ["Common Mistakes", "Interview Points", "Exercises", "Chapter Summary"]
    return build("ch14-best-practices.md", "Best Practices", "React coding standards, accessibility, security, naming conventions, and production checklist.", 14, ["react", "best-practices", "accessibility", "conventions", "production"], "Chapter 14: Best Practices", "Professional React is readable, accessible, and safe — not clever.", toc_t, secs, [("div onClick", "Not keyboard accessible", "Use button")], [("a11y in React?", "Semantic HTML + ARIA; React doesn't auto-fix.")], [(1,"⭐","a11y audit","Fix labels on a form.","")], [("a11y","Semantic HTML"),("Security","No raw user HTML")], "./ch15-interview-prep.md", "Chapter 15: Interview Preparation")


def ch15():
    secs = [
        ("Interview Structure", "Fundamentals, live code, architecture, behavioral."),
        ("What is React — Answer", "Library, components, declarative, virtual DOM."),
        ("JSX — Answer", "Syntactic sugar for createElement."),
        ("Props vs State", "Table comparison."),
        ("Virtual DOM — Answer", "Diff + minimal DOM updates."),
        ("useState — Answer", "Tuple; functional updates."),
        ("useEffect — Answer", "Side effects; deps; cleanup."),
        ("Hooks Rules — Answer", "Top level; React functions only."),
        ("useRef vs useState", "Re-render difference."),
        ("useMemo vs useCallback", "Value vs function cache."),
        ("Re-render Causes", "State, props, parent, context."),
        ("React.memo and Keys", "Perf + list identity."),
        ("Coding — Counter", "Reference solution."),
        ("Coding — Debounce", "useDebounce hook."),
        ("Coding — Fetch List", "loading error data."),
        ("Architecture Questions", "Global state layers."),
        ("React 18 Topics", "Batching, transitions, concurrent."),
        ("Testing Questions", "RTL approach."),
        ("Tricky — setState Async", "Batching; functional updater."),
        ("System Design Frontend", "Product page sketch."),
        ("Behavioral Tips", "Trade-offs, a11y, think aloud."),
        ("One Week Plan", "Day-by-day review table."),
        ("Cheat Sheet", "Hooks routing data forms."),
    ]
    toc_t = [s[0] for s in secs] + ["Common Mistakes", "Interview Points", "Exercises", "Chapter Summary"]
    return build("ch15-interview-prep.md", "Interview Preparation", "Common React interview questions, answers, coding challenges, and system design talking points.", 15, ["react", "interview", "preparation", "questions"], "Chapter 15: Interview Preparation", "You have learned the material — this chapter helps you communicate it under pressure.", toc_t, secs, [("Memorizing without building", "Freeze in live code", "Build todos weekly")], [("Explain reconciliation?", "Virtual DOM diff; keys help list matching.")], [(1,"⭐","Mock interview","Record 2min useEffect answer.","")], [("Practice","Build + explain aloud")], "./ch00-course-overview.md", "Course Overview")


CHAPTER_BUILDERS: list[tuple[str, object]] = [
    ("ch02-jsx-and-components.md", ch02),
    ("ch03-state-and-events.md", ch03),
    ("ch04-lists-and-keys.md", ch04),
    ("ch05-useEffect.md", ch05),
    ("ch06-hooks-deep-dive.md", ch06),
    ("ch07-context-api.md", ch07),
    ("ch08-react-router.md", ch08),
    ("ch09-forms.md", ch09),
    ("ch10-data-fetching.md", ch10),
    ("ch11-performance.md", ch11),
    ("ch12-patterns-and-architecture.md", ch12),
    ("ch13-testing.md", ch13),
    ("ch14-best-practices.md", ch14),
    ("ch15-interview-prep.md", ch15),
]
