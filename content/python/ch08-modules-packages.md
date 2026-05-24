---
title: Modules and Packages
description: Imports, __name__, package layout, and the standard library
order: 8
tags: [python, modules, imports]
---

# Chapter 8: Modules and Packages

## 8.1 Modules

> **Definition:** A **module** is a file containing Python definitions and statements. Importing a module executes it once and caches the result in `sys.modules`.

```python
# math_utils.py
PI = 3.14159

def circle_area(r):
    return PI * r ** 2
```

```python
# main.py
import math_utils
from math_utils import circle_area, PI

print(math_utils.circle_area(5))
print(circle_area(5))
```

## 8.2 Import styles

```python
import os
import json as js
from pathlib import Path
from collections import defaultdict, Counter
from typing import Optional  # typing is stdlib
```

| Style | Example | When |
|-------|---------|------|
| `import mod` | `mod.func()` | Avoid namespace pollution |
| `from mod import x` | `x()` | Short names, few imports |
| `import mod as alias` | `alias.func()` | Long module names |

Avoid `from module import *` — obscures origins and may overwrite names.

## 8.3 `__name__` and script entry point

```python
# greeter.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
```

When run directly, `__name__ == "__main__"`. When imported, `__name__` is the module name.

## 8.4 Packages

> **Definition:** A **package** is a directory containing modules and an `__init__.py` file (Python 3.3+ namespace packages are optional).

```text
myproject/
├── pyproject.toml
├── mypackage/
│   ├── __init__.py
│   ├── core.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
└── tests/
```

```python
from mypackage.core import process
from mypackage.utils.helpers import format_name
```

## 8.5 Relative imports (inside packages)

```python
# mypackage/utils/helpers.py
from ..core import process  # parent package
from .formatting import title_case  # same package
```

Relative imports work only inside packages, not in top-level scripts.

## 8.6 Standard library highlights

| Module | Purpose |
|--------|---------|
| `os` / `pathlib` | Filesystem paths |
| `json` | JSON encode/decode |
| `datetime` | Dates and times |
| `collections` | Specialized containers |
| `itertools` | Iterator tools |
| `functools` | Higher-order functions |
| `re` | Regular expressions |
| `random` | Pseudo-random numbers |
| `urllib` / `http` | HTTP clients (stdlib) |

```python
from pathlib import Path
from datetime import datetime, timezone
import json

data = {"saved_at": datetime.now(timezone.utc).isoformat()}
Path("config.json").write_text(json.dumps(data, indent=2))
```

See [File I/O](./ch09-file-io.md) for reading and writing files.

## 8.7 Third-party packages

Install with pip (see [Virtual Environments & pip](./ch12-virtual-env-pip.md)):

```bash
pip install requests
```

```python
import requests
response = requests.get("https://api.github.com")
response.json()
```

## 8.8 Module search path

Python looks for modules in:

1. Current directory
2. Entries in `PYTHONPATH`
3. Standard library
4. Site-packages (installed packages)

```python
import sys
print(sys.path)
```

## 8.9 `__all__` and public API

```python
# mymodule.py
__all__ = ["public_func", "PUBLIC_CONSTANT"]

def public_func():
    pass

def _internal():
    pass
```

`from mymodule import *` imports only names in `__all__`.

## 8.10 Circular imports

Avoid mutual imports at module top level. Solutions:

- Restructure shared code into a third module
- Import inside functions
- Use type-only imports: `from typing import TYPE_CHECKING`

## Exercises

1. Create a module `geometry.py` with `rectangle_area` and import it from `main.py`.
2. Build a mini-package `tools/` with `__init__.py` and two submodules.
3. Use `pathlib` to list all `.py` files in a directory.
4. Add `if __name__ == "__main__"` guard with a simple CLI to one module.

## Summary

Modules and packages organize code into reusable units. Master import styles, package layout, and the standard library before reaching for third-party deps.

## Next chapter

Continue to [File I/O](./ch09-file-io.md).
