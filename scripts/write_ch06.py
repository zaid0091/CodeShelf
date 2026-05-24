"""Chapter 6 content builder."""
from generate_ch06_14 import (
    FOOTER,
    block,
    best_practices,
    build_chapter,
    code,
    exercises,
    interview_qa,
    mistakes,
    pad_section,
    sec,
)


def write_ch06() -> str:
    sections = [
        sec(
            "Why ES6+ Matters",
            "**ES6** (ECMAScript 2015) is the landmark update: `let`/`const`, arrows, classes, modules, destructuring, Promises, and more.",
            "Modern codebases assume ES6+. Without it, React, Vue, and Node tooling are hard to read.",
            "TC39 ships yearly updates (ES2017 `async/await`, ES2020 `?.`/`??`, ES2022 private fields).",
            code('''
const user = { name: "Alice" };
const { name } = user; // destructuring — everywhere in modern JS
'''),
            "> See [Chapter 1](./ch01-javascript-basics.md), [Chapter 4](./ch04-functions.md), [Chapter 5](./ch05-arrays-and-objects.md).",
        ),
        sec(
            "History of ECMAScript",
            "**ECMAScript** is the spec; **JavaScript** is the implementation in browsers and Node.",
            'Interviewers ask "What is ES6?" — a **spec version**, not a new language.',
            "1995: created in ~10 days. 2015: ES6. 2016+: yearly releases.",
            "```text\n1995 Mocha → LiveScript → JavaScript\n2015 ES6 (biggest release)\n2017 async/await\n2020 ?. ??\n```",
        ),
        sec(
            "let and const Review",
            "**`let`** is block-scoped and reassignable. **`const`** cannot be reassigned; object contents may still mutate.",
            "Fixes `var` hoisting and function-scope leaks.",
            "Default to `const`; use `let` when reassigning. Never `var`.",
            code('''
const MAX = 100;
let count = 0;
count++;
const cfg = { theme: "light" };
cfg.theme = "dark"; // OK
'''),
            "| | var | let | const |\n|---|---|---|---|\n| Scope | function | block | block |",
        ),
        sec(
            "Arrow Functions Deep Dive",
            "**Arrow functions** use `=>` and inherit **lexical `this`** from the enclosing scope.",
            "Cleaner callbacks; avoid when you need dynamic `this` or `new`.",
            "`(a, b) => a + b` or `(a) => { return a; }`",
            code('''
const nums = [1, 2, 3];
const doubled = nums.map((n) => n * 2);

const timer = {
  seconds: 0,
  start() {
    setInterval(() => {
      this.seconds++; // arrow keeps 'this' as timer
    }, 1000);
  },
};
'''),
        ),
        sec(
            "Template Literals",
            "Strings with backticks support `${expression}` and multiple lines.",
            "Readable HTML/JSON templates without `+` concatenation.",
            "Escape backticks with `\\``.",
            code('''
const name = "Alice";
const msg = `Hello, ${name}!`;
const html = `<p class="user">${name}</p>`;
'''),
        ),
        sec(
            "Tagged Template Literals",
            "A **tag** function receives string segments and values: `` tag`Hello ${name}` ``.",
            "i18n, styled-components, HTML escaping.",
            "First argument: array of string parts; rest: interpolated values.",
            code('''
function escape(strings, ...values) {
  return strings.reduce((acc, s, i) => acc + s + (values[i] ?? ""), "");
}
const safe = escape`<b>${userInput}</b>`;
'''),
        ),
        sec(
            "Destructuring Arrays",
            "Unpack array elements into variables: `const [a, b] = arr`.",
            "Swap, skip elements, defaults, rest.",
            code('''
const [first, , third] = [1, 2, 3];
const [head, ...rest] = [1, 2, 3];
let x = 1, y = 2;
[x, y] = [y, x];
'''),
        ),
        sec(
            "Destructuring Objects",
            "Unpack properties by name; rename and default.",
            "API responses and function options.",
            code('''
const { id, name, role = "viewer" } = user;
function connect({ host = "localhost", port = 3000 } = {}) {}
'''),
        ),
        sec(
            "Spread and Rest",
            "**Spread** expands iterables; **rest** collects remaining items.",
            "Immutable updates and variadic functions.",
            code('''
const merged = { ...defaults, ...overrides };
const all = [...a, ...b];
function sum(...nums) { return nums.reduce((a, b) => a + b, 0); }
'''),
        ),
        sec(
            "Enhanced Object Literals",
            "Shorthand properties, method syntax, computed keys.",
            "Less boilerplate in factories.",
            code('''
const id = 1, role = "admin";
const user = {
  id,
  role,
  greet() { return `Hi ${this.role}`; },
  ["key_" + id]: true,
};
'''),
        ),
        sec(
            "Default Parameters",
            "Parameters default when argument is `undefined`.",
            "Self-documenting function signatures.",
            code('''
function createPage(title, layout = "default", published = false) {
  return { title, layout, published };
}
'''),
        ),
        sec(
            "ES6 Classes",
            "`class` is syntactic sugar over prototypes — [Chapter 12](./ch12-oop-prototypes.md).",
            "Familiar OOP syntax for teams.",
            code('''
class Animal {
  constructor(name) { this.name = name; }
  speak() { return `${this.name} makes a sound`; }
}
class Dog extends Animal {
  speak() { return `${this.name} barks`; }
}
'''),
        ),
        sec(
            "Static Methods and Fields",
            "`static` members belong to the class, not instances.",
            "Utilities and constants.",
            code('''
class IdGenerator {
  static #next = 1;
  static create() { return this.#next++; }
}
'''),
        ),
        sec(
            "Private Class Fields",
            "`#field` is truly private (ES2022).",
            "Encapsulation without `_` conventions.",
            code('''
class Wallet {
  #balance = 0;
  deposit(n) { this.#balance += n; }
  get balance() { return this.#balance; }
}
'''),
        ),
        sec(
            "Getters and Setters",
            "Accessor properties run functions on get/set.",
            "Validation and computed properties.",
            code('''
class Circle {
  constructor(r) { this._r = r; }
  get area() { return Math.PI * this._r ** 2; }
  set radius(r) {
    if (r <= 0) throw new Error("invalid");
    this._r = r;
  }
}
'''),
        ),
        sec(
            "ES Modules — Export",
            "Each file is a module; `export` exposes bindings.",
            "Explicit public API per file.",
            code('''
export const PI = 3.14159;
export function add(a, b) { return a + b; }
export default function multiply(a, b) { return a * b; }
'''),
        ),
        sec(
            "ES Modules — Import",
            "`import` creates live read-only bindings.",
            "Static analysis enables tree-shaking.",
            code('''
import multiply, { PI, add } from "./math.js";
import * as math from "./math.js";
'''),
            "Browser: `<script type=\"module\" src=\"app.js\"></script>`. Node: [Chapter 10](./ch10-modules-and-npm.md).",
        ),
        sec(
            "Dynamic import",
            "`import(path)` returns a Promise — load on demand.",
            "Code splitting and lazy routes.",
            code('''
const mod = await import("./heavy-chart.js");
mod.render(data);
'''),
        ),
        sec(
            "Map and Set",
            "`Set` = unique values. `Map` = any keys.",
            "Deduplication and object-key caches.",
            code('''
const tags = new Set(["js", "web", "js"]);
const cache = new Map();
cache.set({ id: 1 }, "Alice");
'''),
            "| | Object | Map |\n|---|--------|-----|\n| Keys | string/Symbol | any |",
        ),
        sec(
            "WeakMap and WeakSet",
            "Weak references; keys can be garbage-collected.",
            "Metadata on DOM nodes without leaks.",
            code('''
const wm = new WeakMap();
let el = document.createElement("div");
wm.set(el, { clicks: 0 });
'''),
        ),
        sec(
            "Symbol",
            "Unique primitive for property keys.",
            "`Symbol.iterator` powers `for...of`.",
            code('''
const id = Symbol("id");
const obj = { [id]: 42, name: "x" };
'''),
        ),
        sec(
            "Iterators",
            "Objects with `next()` returning `{ value, done }`.",
            "Custom iteration protocols.",
            code('''
const counter = {
  n: 0,
  [Symbol.iterator]() {
    return {
      next: () => ({ value: this.n++, done: this.n > 3 }),
    };
  },
};
'''),
        ),
        sec(
            "Generators",
            "`function*` yields values and pauses.",
            "Infinite sequences, async iterators (advanced).",
            code('''
function* range(start, end) {
  for (let i = start; i <= end; i++) yield i;
}
[...range(1, 5)]; // [1,2,3,4,5]
'''),
        ),
        sec(
            "Optional Chaining",
            "`?.` stops at `null`/`undefined`.",
            "Safe deep property access.",
            code('''
const city = user?.address?.city;
const result = api?.fetch?.();
'''),
        ),
        sec(
            "Nullish Coalescing",
            "`??` defaults only for `null`/`undefined`.",
            "Unlike `||`, preserves `0` and `""`.",
            code('''
const port = config.port ?? 3000;
const title = data?.title ?? "Untitled";
'''),
        ),
        sec(
            "Object and Array Helpers",
            "Spread, `Object.assign`, `Object.hasOwn`, `structuredClone`, `flatMap`.",
            "Modern data manipulation.",
            code('''
Object.hasOwn(obj, "key");
const copy = structuredClone(deep);
posts.flatMap((p) => p.tags);
'''),
        ),
        sec(
            "BigInt",
            "Arbitrary-precision integers: `123n`.",
            "IDs larger than Number.MAX_SAFE_INTEGER.",
            code('''
const big = 9007199254740991n + 1n;
'''),
        ),
        sec(
            "Promises — Introduction",
            "A **Promise** represents async completion — pending, fulfilled, rejected.",
            "Bridge to [Chapter 7](./ch07-asynchronous-javascript.md).",
            code('''
const p = new Promise((resolve, reject) => {
  setTimeout(() => resolve("done"), 500);
});
p.then(console.log).catch(console.error);
'''),
        ),
    ]
    toc = [s["title"] for s in sections] + [
        "Common Mistakes",
        "Best Practices",
        "Interview Points",
        "Exercises",
        "Chapter Summary",
    ]
    body = build_chapter(
        {
            "title": "ES6+ Modern Features",
            "description": "ES modules, classes, template literals, Map, Set, and other ES2015+ syntax",
            "order": 6,
            "tags": "[javascript, es6, modules, classes, map, set, template-literals]",
            "heading": "ES6+ Modern Features",
        },
        '"ES2015 did not just add syntax — it gave JavaScript a modern vocabulary for building real applications."',
        toc,
        sections,
        [
            "Template Literals",
            "Destructuring Objects",
            "Spread and Rest",
            "ES6 Classes",
            "Map and Set",
            "Generators",
            "Arrow Functions Deep Dive",
            "Promises — Introduction",
        ],
        6,
    )
    body += mistakes([
        ("Using var", "Use let/const only."),
        ("Arrow as object method needing this", "Use regular method syntax."),
        ("|| instead of ??", "Use ?? for defaults when 0 or '' are valid."),
        ("Wrong import names", "Named imports must match export names."),
    ])
    body += best_practices([
        "Prefer const; let when reassigning.",
        "Use destructuring for options objects.",
        "Use Map/Set for appropriate data shapes.",
        "Use modules for file organization.",
        "Learn prototypes in Chapter 12 even when using class.",
    ])
    body += interview_qa([
        ("class vs prototype?", "class is sugar; methods on prototype chain."),
        ("Map vs Object?", "Map: any keys, .size, no key coercion surprises."),
        ("?? vs ||?", "?? only null/undefined; || all falsy."),
        ("Can you reassign const object?", "Yes mutate properties; no rebind variable."),
        ("What is temporal dead zone?", "let/const inaccessible before declaration line."),
    ])
    body += exercises(6, [
        ("Template email", "buildWelcomeEmail({ name, plan })", code('''
function buildWelcomeEmail({ name, plan }) {
  return {
    subject: `Welcome to ${plan}, ${name}!`,
    body: `Hi ${name},\\nThanks for joining ${plan}.`,
  };
}
''')),
        ("Rectangle class", "area, perimeter getters, toString", code('''
class Rectangle {
  constructor(w, h) { this.width = w; this.height = h; }
  get area() { return this.width * this.height; }
  get perimeter() { return 2 * (this.width + this.height); }
  toString() { return `Rectangle ${this.width}x${this.height}`; }
}
''')),
        ("Module split", "calc.js exports", code('''
export const add = (a, b) => a + b;
export default (op, a, b) => op === "+" ? a + b : a - b;
''')),
        ("Unique tags", "flatMap + Set", code('''
const unique = [...new Set(posts.flatMap((p) => p.tags))];
''')),
        ("mergeConfig", "spread + defaults", code('''
function mergeConfig(user = {}, defaults = {}) {
  return { ...defaults, ...user };
}
''')),
        ("range generator", "function* range", code('''
function* range(a, b) { for (let i = a; i <= b; i++) yield i; }
''')),
    ])
    body += """
## Chapter Summary

| Feature | When |
|---------|------|
| Template literals | Strings with variables |
| Destructuring / spread | Unpack and merge |
| Classes | OOP-style APIs |
| Modules | Multi-file projects |
| Map / Set | Special collections |
| ?. / ?? | Safe access and defaults |

"""
    body += FOOTER.format(
        prev_title="Arrays & Objects",
        prev_file="ch05-arrays-and-objects.md",
        next_blurb="Next: **Asynchronous JavaScript** — event loop, Promises, async/await.",
        next_title="Asynchronous JavaScript",
        next_file="ch07-asynchronous-javascript.md",
        num=6,
    )
    return body
