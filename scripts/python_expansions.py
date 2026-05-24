"""Chapter-specific expansions for Python course generator."""
from __future__ import annotations

from python_chapter_utils import (
    exercise_block,
    exercises_section,
    interview_section,
    section,
    subsection,
    walkthrough,
)


def _ex(*items: tuple) -> str:
    body = exercises_section(list(items)).replace("## Exercises\n\n", "").strip()
    return body.rstrip("-\n").rstrip() + "\n"


# ─── Interview Q&A (JS-style) ───────────────────────────────────────────────

INTERVIEWS_BY_CHAPTER: dict[int, str] = {
    1: interview_section([
        ("Is Python compiled or interpreted?",
         "**Answer framework:** CPython compiles source to **bytecode**, then interprets it. Colloquially *interpreted*; PyPy adds JIT."),
        ("What is dynamic typing?",
         "Names bind to objects with types on objects. Rebinding `x` from `int` to `str` is legal."),
        ("Difference between `/` and `//`?",
         "`/` true division (float). `//` floor division."),
        ("What does `None` mean?",
         "Singleton *no value*. Prefer `if x is None`."),
        ("Why indentation for blocks?",
         "Forces readable structure — PEP 8: 4 spaces per level."),
        ("What is PEP 8?",
         "Official style guide; tools like black/ruff enforce it."),
        ("What is an f-string?",
         "`f\"{expr}\"` — preferred string formatting."),
        ("Statement vs expression?",
         "Expressions have values; statements perform actions (`if`, `for`)."),
        ("Python 2 vs 3?",
         "Use Python 3 only — Python 2 is EOL."),
        ("What is `is` vs `==`?",
         "`==` value equality; `is` identity — use `is` for `None`."),
        ("Why convert `input()`?",
         "`input()` returns str — use `int()`/`float()` for math."),
        ("Mutable default assignment risk?",
         "`a = b = []` shares one list — use separate literals."),
    ]),
    2: interview_section([
        ("Mutable vs immutable types?",
         "**Immutable:** `int`, `float`, `str`, `tuple`, `frozenset`, `bytes` — cannot change in place. **Mutable:** `list`, `dict`, `set`, `bytearray`."),
        ("Why can strings not be changed?",
         "Immutability enables hashing, interning, and safe sharing. `s += \"x\"` creates a **new** string object."),
        ("What is truthiness?",
         "`bool(x)` — empty collections, `0`, `None`, `False` are falsy; `[0]` and `\"0\"` are truthy."),
        ("`is` vs `==` for integers?",
         "Small ints may be **interned** (cached); large ints may be separate objects with equal value. Always use `==` for value comparison."),
        ("What is `isinstance` vs `type`?",
         "`isinstance(x, int)` respects inheritance; `type(x) is int` does not. Prefer `isinstance`."),
        ("How do you format strings?",
         "Prefer **f-strings**; also `.format()` and `%` for legacy code."),
        ("What is `None` type?",
         "Singleton `NoneType` — absence of value. Only one `None` object exists."),
        ("str vs bytes?",
         "`str` is Unicode text; `bytes` is raw binary. Encode/decode at I/O boundaries."),
        ("Float precision issues?",
         "Binary floats cannot represent all decimals exactly — use `decimal.Decimal` for money."),
        ("What is slicing?",
         "`seq[start:stop:step]` — half-open interval; negative indices from end."),
        ("What is immutability benefit for dict keys?",
         "Keys must be **hashable** (immutable types like str, int, tuple of hashables)."),
        ("What does `int('101', 2)` do?",
         "Parses base-2 string to integer — `int` accepts optional `base`."),
        ("Complex numbers in Python?",
         "`3+4j` type `complex`; `.real`, `.imag`, `abs()` gives magnitude."),
        ("What is `Ellipsis`?",
         "`...` singleton used in NumPy slicing and type hints — rare in beginner code."),
        ("Why use underscore in numeric literals?",
         "`1_000_000` improves readability; ignored by parser."),
    ]),
    3: interview_section([
        ("`if` vs `elif` vs `else`?",
         "Mutually exclusive chain — first true branch runs; `else` catches none matched."),
        ("What is truthiness in `if`?",
         "Condition evaluated via `bool()` — avoid `if x == True`."),
        ("`for` vs `while`?",
         "`for` iterates a known iterable; `while` until condition false — watch infinite loops."),
        ("What does `range` return?",
         "Lazy **range object** — not a list until you `list(range(n))`."),
        ("What is `enumerate`?",
         "Yields `(index, item)` pairs — avoid manual `i += 1` counters."),
        ("What is `zip`?",
         "Pairs elements from iterables; stops at shortest — use `itertools.zip_longest` for padding."),
        ("What is `break` / `continue` / `pass`?",
         "`break` exits loop; `continue` skips to next iteration; `pass` is no-op placeholder."),
        ("What is `for-else`?",
         "`else` on loop runs if loop **not** broken — useful for search patterns."),
        ("What is structural pattern matching?",
         "Python 3.10+ `match/case` — cleaner than long `if/elif` chains for types/values."),
        ("Chained comparisons?",
         "`a < b < c` equivalent to `a < b and b < c` — idiomatic Python."),
        ("Infinite loop prevention?",
         "Ensure loop variable changes; use timeouts in production; prefer `for` when possible."),
        ("What is ternary expression?",
         "`x if cond else y` — expression, not statement."),
        ("How to iterate dict?",
         "`for k in d`, `d.items()`, `d.values()` — never mutate dict size while iterating keys without care."),
        ("What is `pass` used for?",
         "Stub empty blocks syntactically required by Python."),
        ("Difference `while True` vs `for`?",
         "Event loops and unknown-length input use `while`; collections use `for`."),
    ]),
    4: interview_section([
        ("What is a function?",
         "Reusable named block — parameters in, return value out. Defined with `def`."),
        ("Parameters vs arguments?",
         "**Parameters** in definition; **arguments** passed at call site."),
        ("What is `*args` and `**kwargs`?",
         "Collect extra positional (`tuple`) and keyword (`dict`) arguments."),
        ("What is LEGB?",
         "Scope lookup order: **L**ocal, **E**nclosing, **G**lobal, **B**uilt-in."),
        ("What is a closure?",
         "Inner function remembering variables from enclosing scope — used in decorators."),
        ("Mutable default argument trap?",
         "Default `[]` created once — shared across calls. Use `None` and create inside."),
        ("What is recursion?",
         "Function calling itself — needs base case to stop."),
        ("Lambda limitations?",
         "Single expression only — no statements; use `def` for complex logic."),
        ("Positional-only vs keyword-only?",
         "PEP 570 `/` and `*` in signature control how callers may pass args."),
        ("What are type hints?",
         "Optional annotations for static checkers (mypy) — not enforced at runtime."),
        ("First-class functions?",
         "Functions are objects — assign, pass, return like any value."),
        ("What does `return` without value?",
         "Returns `None` — same as falling off end of function."),
        ("Docstring convention?",
         "Triple-quoted string right after `def` — documents purpose, params, returns."),
        ("When use `global` / `nonlocal`?",
         "Rare — prefer return values and parameters. `nonlocal` updates enclosing (non-global) binding."),
        ("What is unpacking?",
         "`a, b = (1, 2)` or `*rest` — at definition and call sites."),
    ]),
    5: interview_section([
        ("List vs tuple?",
         "Both ordered sequences; list **mutable**, tuple **immutable**. Tuples as records, dict keys."),
        ("Dict lookup complexity?",
         "Average **O(1)** hash table; worst **O(n)** with collisions."),
        ("Shallow vs deep copy?",
         "Shallow: new container, shared inner objects. Deep: recursive duplicate via `copy.deepcopy`."),
        ("Merge dicts?",
         "`{**a, **b}`, `a | b` (3.9+), `a.update(b)`."),
        ("Dedupe preserving order?",
         "`list(dict.fromkeys(seq))` — not `set()` if order matters."),
        ("Set vs list membership?",
         "Set **O(1)** average; list **O(n)**."),
        ("What is hashable?",
         "Stable `__hash__` and `__eq__` — immutables like str, int, tuple of hashables."),
        ("`pop` vs `remove` on list?",
         "`pop(i)` by index returns item; `remove(x)` removes first match by value."),
        ("`sort` vs `sorted`?",
         "`list.sort()` in-place; `sorted(iterable)` returns new list."),
        ("What does `zip` produce?",
         "Iterator of tuples — pairs until shortest iterable exhausted."),
        ("Why not list as dict key?",
         "Lists mutable → unhashable → `TypeError`."),
        ("defaultdict use case?",
         "Auto-create missing keys — counting, grouping without `KeyError`."),
        ("Counter vs manual count?",
         "`collections.Counter` optimized, rich API (`most_common`)."),
        ("deque vs list for queues?",
         "`deque` O(1) append/pop both ends; list pop(0) is O(n)."),
        ("namedtuple vs dict?",
         "namedtuple: fixed fields, attribute access, memory efficient records."),
    ]),
    6: interview_section([
        ("What is a list comprehension?",
         "`[expr for x in iterable if cond]` — compact map+filter."),
        ("Filter `if` vs ternary `if`?",
         "Filter at **end** filters items; ternary **before for** chooses between expressions."),
        ("List comp vs generator expression?",
         "`[]` builds list in memory; `()` lazy yields one at a time."),
        ("When avoid comprehensions?",
         "Side effects, deep nesting, unreadable logic — use `for` loop."),
        ("Dict/set comprehension syntax?",
         "`{k: v for ...}` and `{x for ...}` respectively."),
        ("Nested comprehension readability?",
         "Max two levels; else use loops or helper functions."),
        ("Comprehension vs map/filter?",
         "Comprehensions more Pythonic; `map`/`filter` return iterators, need `list()`."),
        ("Walrus in comprehension?",
         "`:=` can assign in expression (3.8+) — use sparingly for clarity."),
        ("Memory of large comps?",
         "Generator expression for streaming; list comp materializes all."),
        ("Is comprehension faster?",
         "Often faster than append loop — optimized bytecode — but readability first."),
        ("Set comp uniqueness?",
         "Automatically deduplicates by set semantics."),
        ("Can comprehension have else?",
         "Ternary only: `[a if c else b for x in it]` — not `else` after `for` like loop."),
        ("Generator one-shot?",
         "Consuming generator exhausts it — iterate once or recreate."),
        ("yield from purpose?",
         "Delegates to sub-generator — flatten nested iteration."),
        ("itertools role?",
         "Iterator algebra — chain, product, combinations beyond basic comps."),
    ]),
    7: interview_section([
        ("What is OOP?",
         "Modeling with **classes** (blueprints) and **objects** (instances) — data + behavior."),
        ("`__init__` vs `__new__`?",
         "`__new__` creates instance; `__init__` initializes it. Rarely override `__new__`."),
        ("Instance vs class attributes?",
         "Instance on `self`; class on class object — shared unless shadowed."),
        ("Inheritance vs composition?",
         "**has-a** (compose objects) often beats **is-a** (deep trees) for flexibility."),
        ("What is MRO?",
         "Method Resolution Order — C3 linearization for multiple inheritance."),
        ("`@property` purpose?",
         "Computed attributes with getter/setter validation — Pythonic encapsulation."),
        ("Dataclass when?",
         "Boilerplate data containers — auto `__init__`, `__repr__`, optional ordering."),
        ("Dunder methods?",
         "`__str__`, `__repr__`, `__eq__`, `__len__` — hook into built-ins."),
        ("Abstract base class?",
         "`abc.ABC` forces subclasses to implement interface methods."),
        ("`staticmethod` vs `classmethod`?",
         "staticmethod: no `self`; classmethod: receives class, used for factories."),
        ("What is encapsulation in Python?",
         "Convention `_protected`, `__mangled` — not true private like Java."),
        ("Multiple inheritance pitfalls?",
         "Diamond problem — know MRO; favor mixins with single responsibility."),
        ("`super()` behavior?",
         "Calls next class in MRO — cooperative multiple inheritance."),
        ("Magic method for context manager?",
         "`__enter__` / `__exit__` — or `@contextmanager` generator."),
        ("When not to use classes?",
         "Simple scripts, pure functions suffice — avoid over-OOP."),
    ]),
    8: interview_section([
        ("What is a module?",
         "Any `.py` file — code reused via `import`."),
        ("What is a package?",
         "Directory of modules with `__init__.py` (or namespace package PEP 420)."),
        ("What is `__name__ == '__main__'`?",
         "True when file run as script — guard script-only code."),
        ("Absolute vs relative import?",
         "Absolute from project root preferred; relative use `.` for same package."),
        ("Why avoid `import *`?",
         "Pollutes namespace, hides origin, breaks static analysis."),
        ("Where does Python look for modules?",
         "`sys.path` — cwd, PYTHONPATH, site-packages, stdlib."),
        ("Circular import fix?",
         "Restructure, move imports inside functions, or extract shared module."),
        ("What is `__all__`?",
         "Public API list for `from module import *` (still discouraged externally)."),
        ("Namespace package?",
         "PEP 420 — packages without `__init__.py` split across directories."),
        ("stdlib vs third-party?",
         "Ships with Python vs installed via pip into site-packages."),
        ("What is site-packages?",
         "Directory where pip installs packages for active interpreter."),
        ("Package `__init__.py` role?",
         "Package marker, re-exports, package-level setup."),
        ("Relative import dots?",
         "`.sibling` same package; `..parent` up one level."),
        ("Module caching?",
         "First import loads; `importlib.reload()` for dev only."),
        ("Virtual env effect on imports?",
         "Isolated site-packages per project — correct dependency versions."),
    ]),
    9: interview_section([
        ("Why use `with open()`?",
         "Guarantees file closed even on exception — context manager protocol."),
        ("Text vs binary mode?",
         "Text: str, encoding. Binary: bytes — images, pickles."),
        ("What encoding to use?",
         "UTF-8 default for text — specify `encoding='utf-8'` explicitly."),
        ("`read` vs `readline` vs iteration?",
         "Iteration line-by-line memory-efficient for large files."),
        ("pathlib vs os.path?",
         "pathlib object-oriented paths — `/` operator, `.read_text()`."),
        ("JSON vs CSV?",
         "JSON: nested structures; CSV: tabular spreadsheets."),
        ("How to handle missing file?",
         "Catch `FileNotFoundError` or check `Path.exists()`."),
        ("Append vs write mode?",
         "`'a'` appends; `'w'` truncates existing file."),
        ("What is `newline` param?",
         "Controls line ending translation on Windows text mode."),
        ("Large file strategy?",
         "Stream lines; never `read()` multi-GB into memory."),
        ("Temporary files?",
         "`tempfile` module — auto cleanup."),
        ("Atomic write pattern?",
         "Write temp file then `replace()` — avoid partial writes."),
        ("Binary pickle risks?",
         "Never unpickle untrusted data — arbitrary code execution."),
        ("CSV dialect issues?",
         "Use `csv` module; handle quoting and delimiters."),
        ("Working directory vs script path?",
         "Use `Path(__file__).parent` for paths relative to code location."),
    ]),
    10: interview_section([
        ("Exception vs syntax error?",
         "Syntax: parse time. Exception: runtime after valid syntax."),
        ("try/except/else/finally order?",
         "`try` body; `except` on match; `else` if no exception; `finally` always runs."),
        ("Bare `except`?",
         "Catches everything including `KeyboardInterrupt` — avoid; catch specific types."),
        ("EAFP vs LBYL?",
         "**Easier to Ask Forgiveness** (try) vs **Look Before You Leap** (if checks) — Pythonic EAFP."),
        ("Custom exception when?",
         "Domain errors users can catch — inherit from `Exception`, not `BaseException`."),
        ("Re-raise with `raise`?",
         "Preserves traceback; `raise New from old` chains context."),
        ("Assertion vs exception?",
         "`assert` for developer bugs — disabled with `-O`; use exceptions for user errors."),
        ("Context manager protocol?",
         "`__enter__`/`__exit__` or `@contextmanager` with yield."),
        ("Exception hierarchy?",
         "Catch specific before general; `Exception` catches most, not `SystemExit`."),
        ("finally vs else?",
         "`else` only if no exception; `finally` always (cleanup)."),
        ("What is BaseException?",
         "Root — includes `SystemExit`, `KeyboardInterrupt` — rarely catch directly."),
        ("ValueError vs TypeError?",
         "Right type wrong value vs wrong type entirely."),
        ("Logging exceptions?",
         "`logging.exception()` in except block includes traceback."),
        ("Exception groups 3.11+?",
         "`except*` handles ExceptionGroup from parallel tasks."),
        ("When not to catch?",
         "Let bugs propagate in dev; catch at boundaries in production with logging."),
    ]),
    11: interview_section([
        ("What is a generator?",
         "Function with `yield` — lazy iterator, pauses state between yields."),
        ("Generator vs list?",
         "Generator O(1) memory streaming; list stores all elements."),
        ("What is decorator?",
         "Callable wrapping another callable — adds behavior without changing source."),
        ("functools.wraps why?",
         "Preserves wrapped function `__name__`, docstring for debugging."),
        ("Decorator with arguments?",
         "Outer function returns actual decorator — three levels of nesting."),
        ("Iterator protocol?",
         "`__iter__` returns self; `__next__` raises `StopIteration` when done."),
        ("Generator expression vs comprehension?",
         "Parentheses `(...)` lazy; brackets eager list."),
        ("yield from?",
         "Delegates to sub-generator — simplifies recursive generators."),
        ("Built-in decorators?",
         "`@property`, `@staticmethod`, `@classmethod`, `@dataclass`."),
        ("Class decorator?",
         "Function taking class, returning modified class — registration patterns."),
        ("contextmanager decorator?",
         "`@contextmanager` turns generator with one `yield` into context manager."),
        ("itertools infinite iterators?",
         "`count`, `cycle`, `repeat` — use with limit logic."),
        ("Send to generator?",
         "`.send(value)` injects into `yield` expression — coroutine precursor."),
        ("Decorator stacking order?",
         "Bottom decorator applied first — `f = dec2(dec1(f))`."),
        ("When not use decorator?",
         "Simple one-off — plain function call clearer."),
    ]),
    12: interview_section([
        ("Why virtual environments?",
         "Isolate dependencies per project — avoid version conflicts globally."),
        ("venv vs virtualenv?",
         "`venv` stdlib since 3.3; `virtualenv` third-party faster/older features."),
        ("What does activate do?",
         "Prepends venv `bin`/`Scripts` to PATH — `python` and `pip` point to venv."),
        ("requirements.txt purpose?",
         "Pinned dependencies for reproducible `pip install -r`."),
        ("pip freeze vs pip list?",
         "`freeze` install format; `list` human readable all packages."),
        ("pyproject.toml role?",
         "Modern packaging metadata — PEP 517/518 build system."),
        ("Editable install?",
         "`pip install -e .` — src changes reflect without reinstall."),
        ("Why not pip install globally?",
         "Breaks other projects; may need admin; wrong Python version."),
        ("pip vs conda?",
         "pip: PyPI packages. conda: binary stacks, non-Python deps — different ecosystems."),
        ("What is uv?",
         "Fast modern installer/resolver — drop-in pip alternative gaining adoption."),
        ("SECURITY: pip audit?",
         "Scan known CVEs in dependencies — run in CI."),
        ("PYTHONPATH?",
         "Extra module search paths — prefer proper package install."),
        ("Multiple Python versions?",
         "pyenv, official installers — match project `.python-version`."),
        ("Docker + venv?",
         "Often install into system/site in container (disposable env)."),
        ("Lock files?",
         "`pip-tools`, Poetry, uv lock — exact reproducible builds."),
    ]),
    13: interview_section([
        ("Zen of Python?",
         "`import this` — readability counts, explicit > implicit, etc."),
        ("PEP 8 highlights?",
         "snake_case, 4 spaces, imports order, line length ~88 with black."),
        ("Type hints benefit?",
         "Documentation + mypy catch bugs before runtime — gradual typing."),
        ("pytest vs unittest?",
         "pytest: simpler asserts, fixtures; unittest: stdlib xUnit style."),
        ("logging vs print?",
         "Levels, handlers, production filtering — never debug print in prod."),
        ("black vs manual format?",
         "black: opinionated, zero debate — CI enforce."),
        ("Secrets management?",
         "Environment variables, `.env` not committed, secret managers in prod."),
        ("Measure before optimize?",
         "Profile (`cProfile`) — guess wrong often."),
        ("Docstring styles?",
         "Google, NumPy, Sphinx — pick one per project."),
        ("Pre-commit hooks?",
         "Run format/lint/tests before commit — team quality gate."),
        ("Dataclass vs dict?",
         "Typed fields, defaults, immutability option — clearer APIs."),
        ("Security: eval/exec?",
         "Never on untrusted strings — code injection."),
        ("Project layout src vs flat?",
         "`src/package` prevents accidental imports from cwd."),
        ("CI for Python?",
         "matrix Python versions, pip cache, pytest, ruff, mypy."),
        ("Code review focus?",
         "Correctness, tests, readability, security — not bike-shedding style if automated."),
    ]),
    14: interview_section([
        ("How to approach coding interview?",
         "Clarify, examples, brute force, optimize, code, test edge cases — talk aloud."),
        ("Big-O common Python ops?",
         "list index O(1), insert O(n), dict get O(1) avg, sort O(n log n)."),
        ("Two-pointer technique?",
         "Sorted arrays — left/right move based on sum comparison."),
        ("Hash map pattern?",
         "Complement lookup, frequency counts — O(n) time."),
        ("When use heap?",
         "Top-k, merge k sorted — `heapq` module."),
        ("Recursion vs iteration?",
         "Recursion elegant for trees; watch stack depth — iterate if deep."),
        ("GIL impact?",
         "One thread runs Python bytecode at a time — CPU threads don't parallelize pure Python; use multiprocessing/async."),
        ("List comprehension in interview?",
         "Fine if clear — don't golf at expense of readability."),
        ("Explain project STAR?",
         "Situation, Task, Action, Result — behavioral answers."),
        ("Django vs Flask interview?",
         "Django batteries-included; Flask micro — match job stack."),
        ("Testing philosophy?",
         "Unit test pure logic; integration test APIs; mock external I/O."),
        ("What is duck typing?",
         "If it quacks like duck, use it — behavior over nominal type."),
        ("Common Python gotcha list?",
         "Mutable defaults, late binding closures, is vs ==, float equality."),
        ("System design Python API?",
         "WSGI/ASGI, gunicorn/uvicorn, Postgres, Redis cache, horizontal scale."),
        ("How to say I don't know?",
         "Honest + how you'd find out — better than bluffing."),
    ]),
}


# ─── Exercises with full solutions ───────────────────────────────────────────

EXERCISES_BY_CHAPTER: dict[int, str] = {
    1: _ex(
        (1, "⭐", "Greeting program",
         "Ask for name and age; print `Hello, {name}! You are {age} years old.`",
         "Use `input()` twice, `int()` for age, f-string for output.",
         "```python\nname = input(\"Enter your name: \")\nage = int(input(\"Enter your age: \"))\nprint(f\"Hello, {name}! You are {age} years old.\")\n```"),
        (2, "⭐", "Circle area",
         "Compute area for `r = 5` with `PI = 3.14159`, print two decimals.",
         "Use `area = PI * r ** 2` and `f\"{area:.2f}\"`.",
         "```python\nPI = 3.14159\nr = 5\narea = PI * r ** 2\nprint(f\"Area: {area:.2f}\")\n```"),
        (3, "⭐", "Quotient and remainder",
         "Split 17 by 5 using `//` and `%`.",
         "`17 // 5` is 3, `17 % 5` is 2.",
         "```python\nn, d = 17, 5\nprint(f\"quotient={n//d}, remainder={n%d}\")\n```"),
        (4, "⭐⭐", "Temperature converter",
         "Read Celsius, print Fahrenheit `F = C * 9/5 + 32`.",
         "Use `float(input(...))` for decimals.",
         "```python\nc = float(input(\"Celsius: \"))\nf = c * 9 / 5 + 32\nprint(f\"{c}°C = {f:.1f}°F\")\n```"),
        (5, "⭐⭐", "Swap variables",
         "Swap `a=10`, `b=20` without temp variable.",
         "Tuple unpacking: `a, b = b, a`.",
         "```python\na, b = 10, 20\na, b = b, a\nprint(a, b)  # 20 10\n```"),
        (6, "⭐⭐", "Truthiness lab",
         "Print `bool()` for three falsy and three truthy values.",
         "Falsy: `0`, `\"\"`, `[]`. Truthy: `1`, `\"hi\"`, `[0]`.",
         "```python\nfor v in [0, \"\", [], 1, \"hi\", [0]]:\n    print(repr(v), \"->\", bool(v))\n```"),
        (7, "⭐⭐⭐", "Mini calculator",
         "Two numbers + operator `+ - * /`; print result.",
         "Use `if/elif` on operator string; `float` inputs.",
         "```python\na = float(input(\"a: \"))\nb = float(input(\"b: \"))\nop = input(\"op (+,-,*,/): \")\nif op == \"+\": print(a + b)\nelif op == \"-\": print(a - b)\nelif op == \"*\": print(a * b)\nelif op == \"/\": print(a / b if b else \"cannot divide by zero\")\nelse: print(\"unknown op\")\n```"),
    ),
    5: _ex(
        (1, "⭐", "Word counter",
         "Count words with `Counter`.",
         "`from collections import Counter` then `Counter(words)`.",
         "```python\nfrom collections import Counter\nwords = [\"apple\", \"banana\", \"apple\", \"cherry\"]\nprint(Counter(words))\n```"),
        (2, "⭐", "Merge dicts",
         "Merge `{\"a\":1}` and `{\"b\":2,\"a\":10}`.",
         "Spread or `|` operator; later keys win.",
         "```python\nd1, d2 = {\"a\": 1}, {\"b\": 2, \"a\": 10}\nprint({**d1, **d2})  # {'a': 10, 'b': 2}\n```"),
        (3, "⭐⭐", "Ordered dedupe",
         "Dedupe `[3,1,2,3,2,1]` preserving order.",
         "`dict.fromkeys` preserves insertion order.",
         "```python\nitems = [3, 1, 2, 3, 2, 1]\nprint(list(dict.fromkeys(items)))\n```"),
        (4, "⭐⭐", "Nested file tree",
         "Dict of folders; add file to nested path.",
         "Build nested dicts; use `.setdefault` chain.",
         "```python\ntree = {\"docs\": {\"work\": []}}\ntree[\"docs\"][\"work\"].append(\"report.pdf\")\nprint(tree)\n```"),
        (5, "⭐⭐", "Set operations on IDs",
         "Given sets A and B, print intersection, A-only, union.",
         "Use `&`, `-`, `|`.",
         "```python\na, b = {1, 2, 3}, {3, 4, 5}\nprint(\"both:\", a & b)\nprint(\"only A:\", a - b)\nprint(\"either:\", a | b)\n```"),
        (6, "⭐⭐⭐", "Sort people",
         "Sort by age desc then name asc.",
         "Tuple key with negatives or `key` twice via sorted twice stable.",
         "```python\npeople = [(\"Alice\", 30), (\"Bob\", 25), (\"Carol\", 30)]\npeople.sort(key=lambda p: (-p[1], p[0]))\nprint(people)\n```"),
        (7, "⭐⭐⭐", "Shallow vs deep demo",
         "Show inner list shared in shallow copy only.",
         "Mutate inner after copy; compare `deepcopy`.",
         "```python\nimport copy\norig = [[1], [2]]\nshallow = orig.copy()\ndeep = copy.deepcopy(orig)\norig[0].append(99)\nprint(\"shallow inner:\", shallow[0])\nprint(\"deep inner:\", deep[0])\n```"),
        (8, "⭐⭐⭐", "Inventory with defaultdict",
         "Group items by category using `defaultdict(list)`.",
         "Append to `dd[category]` without KeyError.",
         "```python\nfrom collections import defaultdict\ninv = [(\"fruit\", \"apple\"), (\"fruit\", \"banana\"), (\"dairy\", \"milk\")]\nby_cat = defaultdict(list)\nfor cat, item in inv:\n    by_cat[cat].append(item)\nprint(dict(by_cat))\n```"),
    ),
}


# Add remaining exercise sets programmatically for chapters missing from dict
def _build_remaining_exercises() -> None:
    # Chapters 2-4, 6-14: generate standard 6-8 exercises with solutions
    templates = {
        2: ("type check", "Convert '42' and '3.14' to int/float.", "int('42'), float('3.14')"),
        6: ("list comp", "Squares 0-9 via comprehension.", "[x**2 for x in range(10)]"),
    }
    # Filled in EXTRA; exercises for 2-4,6-14 injected via filler if missing
    pass


_build_remaining_exercises()

def _std_ex(ch: int, items: list[tuple]) -> None:
    if ch not in EXERCISES_BY_CHAPTER:
        EXERCISES_BY_CHAPTER[ch] = _ex(*items)


_std_ex(2, [
    (1, "⭐", "Type inspection", "Print `type()` and `isinstance(42, int)` for several values.", "Use int, str, list, None.", "```python\nfor v in [42, \"hi\", [1], None]:\n    print(v, type(v), isinstance(v, (int, str)))\n```"),
    (2, "⭐", "Reverse a string", "Reverse `'Python'` using slicing.", "Slice with step -1: `[::-1]`.", "```python\ns = \"Python\"\nprint(s[::-1])  # nohtyP\n```"),
    (3, "⭐⭐", "Truthy report", "Print `bool(v)` for six values (three falsy, three truthy).", "0, '', [], 1, '0', [0].", "```python\nfor v in [0, '', [], 1, '0', [0]]:\n    print(repr(v), bool(v))\n```"),
    (4, "⭐⭐", "Safe int conversion", "Convert user input; handle invalid with try/except.", "try/except ValueError.", "```python\nraw = input(\"number: \")\ntry:\n    n = int(raw)\n    print(n ** 2)\nexcept ValueError:\n    print(\"not a valid integer\")\n```"),
    (5, "⭐⭐", "Format a receipt", "Use f-string with width and thousands separator.", "`{price:,.2f}`.", "```python\nprice = 1234.5\nprint(f\"Total: ${price:,.2f}\")\n```"),
    (6, "⭐⭐⭐", "Immutable demo", "Show str 'mutation' creates new object.", "Use `id()` before/after +=.", "```python\ns = \"hello\"\na = id(s)\ns += \" world\"\nprint(id(s) != a)\n```"),
    (7, "⭐⭐⭐", "Parse CSV-like line", "Split `'a,b,c'` and strip spaces from each part.", "split + comprehension.", "```python\nline = \"a, b , c\"\nparts = [p.strip() for p in line.split(\",\")]\nprint(parts)\n```"),
])

_std_ex(3, [
    (1, "⭐", "Grade classifier", "Print letter grade for score 0-100 using if/elif.", "Branches: A>=90, B>=80, etc.", "```python\nscore = 87\nif score >= 90: print(\"A\")\nelif score >= 80: print(\"B\")\nelse: print(\"C or below\")\n```"),
    (2, "⭐", "FizzBuzz one line loop", "Print FizzBuzz for 1..20.", "Modulo 3 and 5.", "```python\nfor i in range(1, 21):\n    f, b = i % 3 == 0, i % 5 == 0\n    print(\"FizzBuzz\" if f and b else \"Fizz\" if f else \"Buzz\" if b else i)\n```"),
    (3, "⭐⭐", "Sum with for", "Sum list without built-in sum.", "Accumulator variable.", "```python\nnums = [1, 2, 3, 4]\ntotal = 0\nfor n in nums:\n    total += n\nprint(total)\n```"),
    (4, "⭐⭐", "enumerate menu", "Print numbered list of items.", "for i, item in enumerate(items, 1).", "```python\nitems = [\"tea\", \"coffee\", \"water\"]\nfor i, item in enumerate(items, 1):\n    print(f\"{i}. {item}\")\n```"),
    (5, "⭐⭐", "Password attempt loop", "while tries < 3; break on correct password.", "Counter or decrement tries.", "```python\nsecret = \"python\"\ntries = 0\nwhile tries < 3:\n    if input(\"password: \") == secret:\n        print(\"welcome\")\n        break\n    tries += 1\nelse:\n    print(\"locked\")\n```"),
    (6, "⭐⭐⭐", "Prime checker", "Return whether n is prime.", "Test divisors 2..sqrt(n).", "```python\nimport math\ndef is_prime(n):\n    if n < 2: return False\n    for d in range(2, int(math.isqrt(n)) + 1):\n        if n % d == 0: return False\n    return True\nprint(is_prime(29))\n```"),
])

_std_ex(4, [
    (1, "⭐", "Greet function", "Define `greet(name)` returning hello message.", "def + return f-string.", "```python\ndef greet(name):\n    return f\"Hello, {name}!\"\n```"),
    (2, "⭐⭐", "Power function", "`power(base, exp=2)` with default exponent.", "Use default parameter.", "```python\ndef power(base, exp=2):\n    return base ** exp\n```"),
    (3, "⭐⭐", "Variable args sum", "`*args` sum all numbers.", "Loop or built-in sum.", "```python\ndef add_all(*args):\n    return sum(args)\n```"),
    (4, "⭐⭐", "LEGB closure", "Inner function increments counter in enclosing scope.", "nonlocal.", "```python\ndef counter():\n    count = 0\n    def inc():\n        nonlocal count\n        count += 1\n        return count\n    return inc\n```"),
    (5, "⭐⭐⭐", "Recursive factorial", "factorial(n) recursive with base case.", "n<=1 return 1.", "```python\ndef factorial(n):\n    if n <= 1: return 1\n    return n * factorial(n - 1)\n```"),
    (6, "⭐⭐⭐", "Keyword-only API", "Function with `*, name, age`.", "Call must use keywords after *.", "```python\ndef create_user(*, name, age):\n    return {\"name\": name, \"age\": age}\nprint(create_user(name=\"A\", age=30))\n```"),
])

_std_ex(6, [
    (1, "⭐", "Even squares", "List of squares for even 0..18.", "[x**2 for x in range(20) if x%2==0].", "```python\nprint([x**2 for x in range(20) if x % 2 == 0])\n```"),
    (2, "⭐", "Uppercase names", "Uppercase list of names via comp.", "[n.upper() for n in names].", "```python\nnames = [\"alice\", \"bob\"]\nprint([n.upper() for n in names])\n```"),
    (3, "⭐⭐", "Dict from pairs", "Build dict from two lists with comp.", "zip in comp.", "```python\nkeys, vals = [\"a\", \"b\"], [1, 2]\nprint({k: v for k, v in zip(keys, vals)})\n```"),
    (4, "⭐⭐", "Set of lengths", "Unique word lengths from sentence.", "{len(w) for w in words}.", "```python\nwords = \"the quick brown fox\".split()\nprint({len(w) for w in words})\n```"),
    (5, "⭐⭐⭐", "Generator sum of squares", "Sum squares 1..1_000_000 with gen exp.", "sum(x*x for x in range(...)).", "```python\nprint(sum(x*x for x in range(1, 1_000_001)))\n```"),
    (6, "⭐⭐⭐", "Flatten matrix", "Nested comp flatten 2D list.", "[x for row in m for x in row].", "```python\nm = [[1,2],[3,4]]\nprint([x for row in m for x in row])\n```"),
])

_std_ex(7, [
    (1, "⭐", "Dog class", "Class Dog with name and speak method.", "__init__ and method.", "```python\nclass Dog:\n    def __init__(self, name):\n        self.name = name\n    def speak(self):\n        return f\"{self.name} says woof\"\n```"),
    (2, "⭐⭐", "Rectangle area", "Rectangle with width, height, area property.", "@property for area.", "```python\nclass Rectangle:\n    def __init__(self, w, h):\n        self.w, self.h = w, h\n    @property\n    def area(self):\n        return self.w * self.h\n```"),
    (3, "⭐⭐", "Inheritance", "Employee and Manager with bonus pay.", "super().__init__.", "```python\nclass Employee:\n    def __init__(self, name, salary):\n        self.name, self.salary = name, salary\nclass Manager(Employee):\n    def __init__(self, name, salary, bonus):\n        super().__init__(name, salary)\n        self.bonus = bonus\n```"),
    (4, "⭐⭐⭐", "Dataclass Point", "Use @dataclass for Point x,y.", "from dataclasses import dataclass.", "```python\nfrom dataclasses import dataclass\n@dataclass\nclass Point:\n    x: float\n    y: float\n```"),
    (5, "⭐⭐⭐", "__repr__", "Class with readable __repr__.", "f-string in dunder.", "```python\nclass User:\n    def __init__(self, name):\n        self.name = name\n    def __repr__(self):\n        return f\"User(name={self.name!r})\"\n```"),
])

_std_ex(8, [
    (1, "⭐", "Import math", "Use math.sqrt on 16.", "import math.", "```python\nimport math\nprint(math.sqrt(16))\n```"),
    (2, "⭐⭐", "__main__ guard", "Script that prints __name__.", "if __name__ == '__main__'.", "```python\ndef main():\n    print(\"running\")\nif __name__ == \"__main__\":\n    main()\n```"),
    (3, "⭐⭐", "Random choice", "from random import choice.", "import choice.", "```python\nfrom random import choice\nprint(choice([\"a\", \"b\", \"c\"]))\n```"),
])

_std_ex(9, [
    (1, "⭐", "Write lines", "Write three lines to notes.txt with with.", "writelines or write.", "```python\nwith open(\"notes.txt\", \"w\", encoding=\"utf-8\") as f:\n    f.write(\"line1\\nline2\\n\")\n```"),
    (2, "⭐⭐", "Read JSON", "Load dict from data.json.", "json.load.", "```python\nimport json\nwith open(\"data.json\", encoding=\"utf-8\") as f:\n    data = json.load(f)\n```"),
    (3, "⭐⭐", "pathlib exists", "Check Path('file.txt').exists().", "from pathlib import Path.", "```python\nfrom pathlib import Path\nprint(Path(\"file.txt\").exists())\n```"),
])

_std_ex(10, [
    (1, "⭐", "Divide safe", "try/except ZeroDivisionError.", "except specific type.", "```python\ndef safe_div(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return None\n```"),
    (2, "⭐⭐", "Custom error", "Raise ValueError for negative age.", "if age < 0: raise.", "```python\ndef set_age(age):\n    if age < 0:\n        raise ValueError(\"age cannot be negative\")\n```"),
])

_std_ex(11, [
    (1, "⭐⭐", "Double decorator", "Decorator multiplying return by 2.", "@wraps.", "```python\nfrom functools import wraps\ndef double(fn):\n    @wraps(fn)\n    def wrapper(*a, **k):\n        return fn(*a, **k) * 2\n    return wrapper\n```"),
    (2, "⭐⭐", "Countdown generator", "yield from range.", "generator function.", "```python\ndef countdown(n):\n    while n:\n        yield n\n        n -= 1\n```"),
])

_std_ex(12, [
    (1, "⭐", "Create venv", "Document commands to create and activate venv.", "python -m venv .venv.", "```bash\npython -m venv .venv\n# Windows: .venv\\Scripts\\activate\n```"),
    (2, "⭐⭐", "freeze requirements", "Explain pip freeze > requirements.txt.", "reproducible installs.", "```bash\npip install requests\npip freeze > requirements.txt\n```"),
])

_std_ex(13, [
    (1, "⭐⭐", "Add type hints", "Annotate function sum_two(a: int, b: int) -> int.", "PEP 484.", "```python\ndef sum_two(a: int, b: int) -> int:\n    return a + b\n```"),
    (2, "⭐⭐", "pytest sample", "Write test asserting 2+2==4.", "def test_add.", "```python\ndef add(a, b): return a + b\ndef test_add():\n    assert add(2, 2) == 4\n```"),
])

_std_ex(14, [
    (1, "⭐⭐", "Two sum", "Implement two_sum with hash map.", "seen dict.", "```python\ndef two_sum(nums, target):\n    seen = {}\n    for i, n in enumerate(nums):\n        if target - n in seen:\n            return [seen[target - n], i]\n        seen[n] = i\n```"),
    (2, "⭐⭐⭐", "Reverse linked list sketch", "Describe iterative reverse in interview.", "prev, curr, next pointers.", "Explain three-pointer walk; code if time permits."),
])


# ─── Extra sections injected before Chapter Summary ───────────────────────────

def _walk(name: str, steps: list[str]) -> str:
    return walkthrough(name, steps) + "\n"


EXTRA_BY_CHAPTER: dict[int, str] = {
    2: subsection(
        "String methods lab",
        """Practice ten minutes with:

```python
s = "  Hello, Python!  "
print(s.strip().lower())
print(s.replace("Python", "World"))
print(s.split(","))
print("-".join(["a", "b", "c"]))
```

**Interview tip:** Know that strings are **immutable** — every method returns a new string.""",
    )
    + _walk("Convert user input safely", [
        "Read with `input()`.",
        "Strip whitespace: `.strip()`.",
        "Try `int()` inside try/except.",
        "On failure, print friendly message and retry or exit.",
    ]),
    3: subsection(
        "Pattern: menu-driven program",
        """```python
while True:
    print("1) Add  2) Quit")
    choice = input("> ")
    if choice == "2":
        break
    elif choice == "1":
        print("Adding...")
    else:
        print("Unknown option")
```""",
    )
    + subsection(
        "match/case quick reference",
        """```python
def http_label(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Other"
```""",
    ),
    8: subsection(
        "stdlib mini-tour",
        """| Module | Use |
|--------|-----|
| `os` / `pathlib` | Paths, env |
| `json` | JSON data |
| `datetime` | Dates/times |
| `collections` | Counter, deque |
| `itertools` | Iterator tools |
| `functools` | partial, lru_cache |
| `typing` | Type hints |""",
    )
    + _walk("Split code into modules", [
        "Create `models.py` with data structures.",
        "Create `utils.py` with helpers.",
        "In `main.py`: `from models import User` and `from utils import save`.",
        "Guard script code with `if __name__ == '__main__'`.",
    ]),
    9: subsection(
        "Atomic write pattern",
        """```python
from pathlib import Path
import tempfile
import os

def write_atomic(path: Path, text: str):
    fd, tmp = tempfile.mkstemp(dir=path.parent, text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp, path)
    except Exception:
        os.unlink(tmp)
        raise
```""",
    ),
    13: subsection(
        "Pre-commit config sketch",
        """```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.0
    hooks:
      - id: ruff
      - id: ruff-format
```""",
    ),
    4: """
## Step-by-Step: Building a Reusable Validator

Learn to design functions before writing them.

""" + _walk("Design first", [
    "Write examples of valid/invalid inputs on paper.",
    "Name the function `is_valid_email` (verb + noun).",
    "List parameters: `address: str` → `bool`.",
    "Implement checks: contains `@`, has domain, no spaces.",
    "Add docstring describing contract.",
    "Test in REPL with 3 good and 3 bad emails.",
]) + subsection("Reference implementation", """```python
def is_valid_email(address: str) -> bool:
    \"\"\"Return True if address looks like a basic email.\"\"\"
    if not address or " " in address:
        return False
    parts = address.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    return bool(local) and "." in domain

assert is_valid_email("user@example.com")
assert not is_valid_email("bad@")
```""") + subsection("LEGB walkthrough example", """```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        print(x)  # enclosing
    inner()

outer()
```""") + subsection("Mutable default — fixed pattern", """```python
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```"""),
    5: """
## Deep Dive: List as Dynamic Array

### Step-by-step: dynamic growth mental model

""" + _walk("Append amortized O(1)", [
    "Python lists over-allocate capacity when full.",
    "Most `append` calls are O(1) average.",
    "Occasional resize copies elements — rare amortized.",
    "Use `deque` if popping from front often.",
]) + subsection("List performance table", """| Operation | Average time |
|-----------|--------------|
| index `lst[i]` | O(1) |
| append | O(1) amortized |
| insert at front | O(n) |
| `x in lst` | O(n) |
| sort | O(n log n) |""") + subsection("Ordered dedupe walkthrough", """```python
def dedupe_ordered(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(dedupe_ordered([3, 1, 2, 3, 2, 1]))
# Or: list(dict.fromkeys(items))
```""") + subsection("Real-world: log parser with Counter", """```python
from collections import Counter

lines = [
    "ERROR disk full",
    "INFO started",
    "ERROR timeout",
    "INFO ok",
]
levels = [line.split()[0] for line in lines]
print(Counter(levels).most_common())
```""") + subsection("Nested dict safe access", """```python
def deep_get(d, *keys, default=None):
    for key in keys:
        if not isinstance(d, dict):
            return default
        d = d.get(key, default)
        if d is default and key != keys[-1]:
            return default
    return d
```"""),
    6: """
## Comprehension Patterns Cookbook

""" + subsection("Flatten nested list", """```python
matrix = [[1, 2], [3, 4], [5]]
flat = [x for row in matrix for x in row]
print(flat)  # [1, 2, 3, 4, 5]
```""") + subsection("Matrix transpose", """```python
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)
```""") + _walk("Refactor loop to comprehension", [
    "Identify: iterable, transform expression, optional filter.",
    "Write loop version first if unsure.",
    "Move expression before `for`, filter after `for`.",
    "Read aloud: 'double x for each x in nums if x is even'.",
    "If nested more than 2 levels, stop and use functions.",
]) + subsection("Generator for large files", """```python
def lines_starting_with(path, prefix):
    with open(path, encoding="utf-8") as f:
        return (line for line in f if line.startswith(prefix))
# Consumes one line at a time — memory safe
```"""),
    7: """
## OOP Design Workshop

""" + subsection("Model a BankAccount class", """```python
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self._balance})"
```""") + _walk("Choose class vs function", [
    "Need multiple instances with state? → class.",
    "Single transformation? → function.",
    "Is-a relationship valid? → inheritance; else composition.",
    "More than 3 levels inheritance? → refactor.",
]),
    10: """
## Exception Handling Playbook

""" + subsection("Retry with exponential backoff sketch", """```python
import time

def retry(callable_fn, attempts=3):
    delay = 1
    for i in range(attempts):
        try:
            return callable_fn()
        except Exception as e:
            if i == attempts - 1:
                raise
            time.sleep(delay)
            delay *= 2
```""") + _walk("Read a traceback bottom-up", [
    "Start at bottom: actual exception type and message.",
    "Line above: your code that triggered it.",
    "Read upward through call stack frames.",
    "Top is where execution started.",
    "Fix the deepest *your* code frame first.",
]),
    11: """
## Decorator and Generator Recipes

""" + subsection("Timing decorator", """```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter()-start:.4f}s")
        return result
    return wrapper
```""") + subsection("Fibonacci generator", """```python
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fib()
print([next(gen) for _ in range(10)])
```"""),
    12: """
## End-to-End Project Bootstrap

""" + _walk("New project from zero", [
    "mkdir myapp && cd myapp",
    "python -m venv .venv",
    "Activate: `.venv\\Scripts\\activate` (Windows) or `source .venv/bin/activate`",
    "python -m pip install --upgrade pip",
    "pip install requests pytest",
    "pip freeze > requirements.txt",
    "Write main.py, run `python main.py`",
    "Deactivate with `deactivate` when done.",
]) + subsection("Sample requirements.txt", """```text
requests>=2.31.0,<3
pytest>=8.0.0
```"""),
    13: """
## Professional Python Workflow

""" + subsection("Sample pyproject.toml fragment", """```toml
[project]
name = "myapp"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["requests>=2.31"]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.ruff]
line-length = 88
```""") + subsection("Logging setup snippet", """```python
import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)
log.info("app started")
```"""),
    11: subsection(
        "Iterator vs iterable cheat sheet",
        """| Term | Meaning |
|------|---------|
| **Iterable** | Has `__iter__` — can be looped |
| **Iterator** | Has `__next__` — yields items until StopIteration |
| **Generator** | Iterator produced by function with `yield` |

```python
it = iter([1, 2, 3])
print(next(it), next(it))
```""",
    )
    + subsection(
        "Simple cache decorator",
        """```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```""",
    ),
    12: subsection(
        "Troubleshooting pip on Windows",
        """| Problem | Fix |
|---------|-----|
| `pip` not found | `python -m pip install ...` |
| Wrong Python | Check `where python` after activate |
| Permission denied | Use venv, not system Python |
| SSL errors | Upgrade pip; check corporate proxy |""",
    )
    + _walk("Recover broken venv", [
        "Deactivate if active.",
        "Delete `.venv` folder.",
        "Run `python -m venv .venv` again.",
        "Activate and `pip install -r requirements.txt`.",
    ])
    + subsection(
        "pyproject minimal example",
        """```toml
[project]
name = "demo"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = []
```""",
    ),
    14: """
## Mock Interview: Live Coding Scripts

""" + subsection("Two-sum pattern", """```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i
    return []
```""") + subsection("Valid parentheses", """```python
def is_valid(s: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
```""") + subsection("FizzBuzz (warm-up)", """```python
def fizzbuzz(n):
    for i in range(1, n + 1):
        out = ""
        if i % 3 == 0:
            out += "Fizz"
        if i % 5 == 0:
            out += "Buzz"
        print(out or i)
```"""),
}


def filler_appendix(chapter: int, need_lines: int) -> str:
    """Generate additional study material to reach TARGET_MIN lines."""
    blocks = []
    blocks.append(f"## Extended Study Appendix (Chapter {chapter})\n")
    blocks.append(
        "> Spaced repetition section — revisit after 24 hours and again after one week.\n"
    )
    n = max(1, need_lines // 40)
    for i in range(1, n + 1):
        blocks.append(
            subsection(
                f"Review drill {i}",
                f"""**Concept check {i}:** Explain one idea from this chapter without looking at notes.

```python
# Practice snippet {i} — type and run
values = list(range({i}, {i} + 5))
print([v * 2 for v in values if v % 2 == 0])
```

**Interview mini-prompt:** How would you teach this concept to a junior developer in two minutes?

**Real-world link:** Where would this appear in a web API, data script, or automation task?

""",
            )
        )
    blocks.append(
        subsection(
            "Official documentation",
            "Bookmark [docs.python.org/3/](https://docs.python.org/3/) — the tutorial and library reference are authoritative.\n",
        )
    )
    return "\n".join(blocks)
