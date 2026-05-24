---
title: Modules and Packages
description: import styles, __name__, packages, stdlib tour, and project layout
order: 8
tags: [python, modules, packages]
---

# Chapter 8: Modules and Packages

> **Modules split code across files. Packages organize modules into importable trees — essential for real projects.**

---

## Table of Contents

1. [Why Modules Matter](#why-modules-matter)
2. [What Is a Module?](#what-is-a-module)
3. [Your First Import](#your-first-import)
4. [Import Styles Compared](#import-styles-compared)
5. [The import Statement Deep Dive](#the-import-statement-deep-dive)
6. [Aliasing and Selective Imports](#aliasing-and-selective-imports)
7. [When to Avoid import *](#when-to-avoid-import)
8. [__name__ and the Script Entry Point](#__name__-and-the-script-entry-point)
9. [How Python Finds Modules](#how-python-finds-modules)
10. [What Is a Package?](#what-is-a-package)
11. [Package Layout and __init__.py](#package-layout-and-__init__py)
12. [Relative vs Absolute Imports](#relative-vs-absolute-imports)
13. [Namespace Packages](#namespace-packages)
14. [The __all__ Public API](#the-__all__-public-api)
15. [Circular Imports](#circular-imports)
16. [Standard Library Tour](#standard-library-tour)
17. [Third-Party Packages and pip](#third-party-packages-and-pip)
18. [Organizing a Real Project](#organizing-a-real-project)
19. [Best Practices](#best-practices)
20. [Common Mistakes](#common-mistakes)
21. [Interview Points](#interview-points)
22. [Exercises](#exercises)
23. [Chapter Summary](#chapter-summary)

---

## Why Modules Matter

> **Definition:** A **module** is a single `.py` file containing Python code. Splitting a program into modules keeps files small, names clear, and code reusable across projects.

### Why it matters

Imagine a 3,000-line script that handles users, payments, email, and reports. Changing one feature means scrolling through unrelated code, and two developers editing the same file causes merge conflicts.

Modules let you put each concern in its own file:

```text
myapp/
  users.py
  payments.py
  email_utils.py
  reports.py
  main.py
```

`main.py` imports only what it needs. Teams can own files, tests can target one module, and you can reuse `email_utils.py` in another project.

### How it works

When you write `import users`, Python loads `users.py` once, executes its top-level code, and caches the module object. Later imports reuse the cache.

```python
# main.py
import users

users.register("alice@example.com")
print(users.count_users())
```

---

## What Is a Module?

> **Definition:** Any file ending in `.py` is a module. The module name is the filename without `.py` (e.g. `helpers.py` → module `helpers`).

### Why it matters

Modules are Python's unit of organization. The standard library is a collection of modules (`json`, `pathlib`, `datetime`). Your own code follows the same pattern.

### How it works

Create `greetings.py`:

```python
# greetings.py
def hello(name: str) -> str:
    return f"Hello, {name}!"
```

Another file can import it:

```python
import greetings

print(greetings.hello("World"))  # Hello, World!
```

Top-level code in a module runs **once** on first import:

```python
# config.py
print("Loading config...")
DEBUG = True
```

```python
import config  # prints: Loading config...
import config  # prints nothing — already loaded
```

---

## Your First Import

> **Definition:** The `import` statement loads a module and binds it to a name in your current namespace.

### Why it matters

Without imports, every function would need to live in one file. Imports connect your code to the standard library and to your own modules.

### How it works

```python
import math

print(math.pi)       # 3.141592653589793
print(math.sqrt(16)) # 4.0
```

You can import multiple modules:

```python
import json
import random
import datetime

data = {"ok": True}
print(json.dumps(data))
print(random.randint(1, 6))
print(datetime.date.today())
```

### Tip

Use the module prefix (`math.sqrt`) so readers always know where a name comes from.

---

## Import Styles Compared

> **Definition:** Python supports several import forms: whole module, specific names, aliasing, and (rarely) wildcard imports.

### Why it matters

The style you choose affects readability, namespace pollution, and refactoring safety.

### How it works

| Style | Syntax | When to use |
|-------|--------|-------------|
| Module | `import os` | Default — clear origin of names |
| From | `from os import path` | One or two names used often |
| Alias | `import numpy as np` | Long or conflicting names |
| Wildcard | `from module import *` | Almost never in application code |

```python
# Whole module — preferred default
import os
print(os.getcwd())

# Import specific names
from pathlib import Path
home = Path.home()

# Alias
import datetime as dt
now = dt.datetime.now()
```

---

## The import Statement Deep Dive

> **Definition:** `import` runs the import machinery: search `sys.path`, load bytecode if cached, execute module body, register in `sys.modules`.

### Why it matters

Understanding import order helps debug `ModuleNotFoundError` and circular import issues.

### How it works

```python
import sys

# Where Python looks for modules (simplified)
for entry in sys.path:
    print(entry)
```

Typical search order:

1. Directory containing the script (or current working directory)
2. `PYTHONPATH` directories
3. Standard library
4. `site-packages` (third-party installs)

```python
# Explicit reload during development only
import importlib
import mymodule

importlib.reload(mymodule)
```

### Tip

Do not rely on `reload()` in production — design imports so modules load in a clean order.

---

## Aliasing and Selective Imports

> **Definition:** **Aliasing** renames a module or name at import time. **Selective import** pulls only chosen attributes from a module.

### Why it matters

`from pandas import DataFrame` is shorter than `pandas.DataFrame` everywhere, but too many bare names make code harder to trace.

### How it works

```python
# Alias a module
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.show()

# Selective import
from collections import Counter

words = ["a", "b", "a", "c", "a"]
print(Counter(words))  # Counter({'a': 3, 'b': 1, 'c': 1})

# Alias a name
from datetime import datetime as dt

print(dt.now())
```

### Common pitfall

```python
from datetime import datetime

# Shadows the module name if you also need datetime.timedelta
```

Prefer `import datetime` or alias: `from datetime import datetime as DateTime`.

---

## When to Avoid import *

> **Definition:** `from module import *` injects all public names from `module` into your namespace (or names listed in `module.__all__`).

### Why it matters

Wildcard imports hide where names come from, break static analysis tools, and can overwrite local variables unexpectedly.

### How it works

```python
# bad_style.py
from math import *

def sqrt(x):
    return "custom"

print(sqrt(4))  # Which sqrt? You shadowed math.sqrt
```

Acceptable only in rare cases (e.g. interactive REPL convenience). In projects, be explicit:

```python
from math import sqrt, pi
```

---

## __name__ and the Script Entry Point

> **Definition:** Every module has a `__name__`. When a file is run directly, `__name__ == "__main__"`. When imported, `__name__` is the module name.

### Why it matters

The **main guard** lets the same file work as both a reusable module and a runnable script.

### How it works

```python
# greeter.py
def greet(name: str) -> str:
    return f"Hello, {name}!"


def main() -> None:
    print(greet("CodeShelf"))


if __name__ == "__main__":
    main()
```

```bash
python greeter.py          # runs main()
python -c "import greeter" # does NOT run main()
```

```python
import greeter
print(greeter.__name__)  # "greeter"
```

---

## How Python Finds Modules

> **Definition:** Python searches directories in `sys.path` for a matching module file or package.

### Why it matters

`ModuleNotFoundError` usually means the module is not on `sys.path`, or the name/package layout is wrong.

### How it works

```python
import sys
import os

# Add a project src folder (common pattern)
ROOT = os.path.dirname(__file__)
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

import mypackage  # now finds src/mypackage/
```

For installable projects, use `pip install -e .` instead of manual `sys.path` hacks.

---

## What Is a Package?

> **Definition:** A **package** is a directory of modules plus `__init__.py` (regular package) or a namespace layout (PEP 420). Packages let you organize code hierarchically.

### Why it matters

Large apps need namespaces like `myapp.api.routes` instead of flat filenames.

### How it works

```text
myapp/
  __init__.py
  models.py
  api/
    __init__.py
    routes.py
```

```python
from myapp.api import routes

routes.list_users()
```

---

## Package Layout and __init__.py

> **Definition:** `__init__.py` marks a directory as a package. It can be empty or run setup code and re-export public APIs.

### Why it matters

`__init__.py` controls what importers see at the package level.

### How it works

```python
# myapp/__init__.py
__version__ = "1.0.0"

from .models import User  # re-export for convenience

__all__ = ["User", "__version__"]
```

```python
from myapp import User
print(User)
```

---

## Relative vs Absolute Imports

> **Definition:** **Absolute** imports start from the top-level package (`from myapp.utils import helper`). **Relative** imports use dots (`.`) to refer to siblings or parents within the same package.

### Why it matters

Relative imports keep package internals portable when the top-level name changes.

### How it works

```text
blog/
  __init__.py
  models.py
  api/
    __init__.py
    views.py
```

```python
# blog/api/views.py
from ..models import Post      # parent package
from . import serializers      # same package (if exists)
```

| Import | Meaning |
|--------|---------|
| `from . import x` | Same package |
| `from .. import x` | Parent package |
| `from ...pkg import x` | Two levels up |

Use absolute imports in application entry points when possible; relative imports inside packages are fine.

---

## Namespace Packages

> **Definition:** A **namespace package** (PEP 420) has no `__init__.py` and can span multiple directories on `sys.path`.

### Why it matters

Plugin systems split one logical package across separate install locations.

### How it works

```text
site-packages/
  myplugins/
    plugin_a.py
other_location/
  myplugins/
    plugin_b.py
```

```python
import myplugins.plugin_a
import myplugins.plugin_b
```

Most application code uses regular packages with `__init__.py` — namespace packages are advanced.

---

## The __all__ Public API

> **Definition:** `__all__` is a list of strings naming the public objects a module exports, especially for `from module import *`.

### Why it matters

Documents the intended public surface and limits wildcard imports.

### How it works

```python
# shapes.py
__all__ = ["Circle", "Rectangle"]

class Circle:
    ...

class Rectangle:
    ...

def _helper():
    """Private by convention, not in __all__."""
    ...
```

```python
from shapes import *
# Only Circle and Rectangle enter the namespace
```

Prefer explicit imports over `import *` even when `__all__` is defined.

---

## Circular Imports

> **Definition:** A **circular import** occurs when module A imports B while B imports A (directly or through a chain).

### Why it matters

Python may raise `ImportError` or leave half-initialized modules with missing attributes.

### How it works

**Problem:**

```python
# a.py
import b
x = 1

# b.py
import a
print(a.x)  # may fail if a is not finished loading
```

**Fixes:**

1. Move shared code to a third module `common.py`
2. Import inside a function when needed:

```python
def process():
    import a
    return a.x + 1
```

3. Restructure so dependencies flow one direction only

---

## Standard Library Tour

> **Definition:** Python ships with a large **standard library** — batteries included — so many tasks need no pip install.

### Why it matters

Reinventing CSV parsing or HTTP clients wastes time. Knowing stdlib modules makes you productive.

### How it works

| Module | Purpose |
|--------|---------|
| `os`, `pathlib` | Files and paths |
| `json`, `csv` | Data formats |
| `datetime` | Dates and times |
| `collections` | `Counter`, `defaultdict`, `deque` |
| `itertools` | Iterator tools |
| `functools` | `lru_cache`, `partial` |
| `re` | Regular expressions |
| `urllib.request` | Simple HTTP (use `httpx`/`requests` for complex APIs) |
| `sqlite3` | Embedded database |
| `unittest` / use `pytest` | Testing |

```python
from pathlib import Path
from collections import Counter
import json

text = Path("notes.txt").read_text(encoding="utf-8")
words = text.split()
print(Counter(words).most_common(5))
print(json.dumps({"words": len(words)}, indent=2))
```

Browse [docs.python.org/3/library](https://docs.python.org/3/library/index.html).

---

## Third-Party Packages and pip

> **Definition:** **Third-party** packages are installed with **pip** into `site-packages`, separate from the standard library.

### Why it matters

Real projects depend on Django, requests, pandas, etc. Virtual environments isolate those dependencies per project (see Chapter 12).

### How it works

```bash
python -m pip install requests
```

```python
import requests

response = requests.get("https://httpbin.org/get", timeout=10)
print(response.status_code)
print(response.json())
```

Pin versions in `requirements.txt` for reproducible installs.

---

## Organizing a Real Project

> **Definition:** A maintainable layout separates application code, tests, config, and docs.

### Why it matters

Interviewers and teammates expect predictable structure.

### How it works

```text
myproject/
  pyproject.toml
  README.md
  src/
    myproject/
      __init__.py
      main.py
      services/
        __init__.py
        users.py
  tests/
    test_users.py
```

Run with:

```bash
python -m myproject.main
```

Or install editable: `pip install -e .`

---

## Best Practices

- Prefer `import module` over wildcard imports.
- Use `if __name__ == "__main__":` for script entry points.
- Keep modules focused — one clear responsibility per file.
- Expose a stable API via `__all__` or package `__init__.py` re-exports.
- Avoid circular imports by layering: models → services → views.
- Use absolute imports at the application edge; relative imports inside packages.
- Install projects in editable mode instead of manipulating `sys.path`.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Running a module inside a package without `-m` | Use `python -m package.module` from project root |
| Naming a file `random.py` | Shadows stdlib `random` — rename to `random_utils.py` |
| `from module import *` in libraries | Import explicit names |
| Giant `__init__.py` with heavy imports | Lazy-import or keep `__init__.py` light |
| Circular imports between two models | Extract shared types to `types.py` or `base.py` |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between a module and a package?**

A module is one `.py` file. A package is a directory of modules (usually with `__init__.py`).

---

> **📌 Interview Point 2: What does `if __name__ == "__main__"` do?**

Runs code only when the file is executed directly, not when imported.

---

> **📌 Interview Point 3: How does Python find modules?**

It searches directories in `sys.path` for a matching module or package.

---

> **📌 Interview Point 4: Why avoid `import *`?**

Pollutes namespace, hides origins, breaks tooling, can shadow names.

---

> **📌 Interview Point 5: What is `__all__`?**

List of names exported by `from module import *`; documents public API.

---

## Exercises

### Exercise 1: Import math ⭐

**Task:** Print `math.sqrt(144)`.

<details>
<summary>💡 Hint</summary>

`import math` then call `math.sqrt`.

</details>

<details>
<summary>✅ Solution</summary>

```python
import math
print(math.sqrt(144))  # 12.0
```

</details>

---

### Exercise 2: Main guard ⭐⭐

**Task:** Write `cli.py` with `run()` and a main block that prints `"Starting..."`.

<details>
<summary>✅ Solution</summary>

```python
def run() -> None:
    print("Running app")


def main() -> None:
    print("Starting...")
    run()


if __name__ == "__main__":
    main()
```

</details>

---

### Exercise 3: Package layout ⭐⭐

**Task:** Sketch a folder `shop/` with `__init__.py` and `cart.py` containing `def total(items): return sum(items)`.

<details>
<summary>✅ Solution</summary>

```python
# shop/cart.py
def total(items):
    return sum(items)

# shop/__init__.py
from .cart import total

# main.py
from shop import total
print(total([10, 20, 5]))  # 35
```

</details>

---

## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **module** | One `.py` file of reusable code |
| **package** | Directory of modules, often with `__init__.py` |
| **import** | Loads code once; cached in `sys.modules` |
| **`__main__`** | Guard for script-only execution |
| **`sys.path`** | Search path for imports |
| **pip** | Installs third-party packages |

---

**⬅️ [Previous: Object-Oriented Programming](./ch07-oop.md)**

**➡️ [Next: File I/O →](./ch09-file-io.md)**

---
