---
title: Functions
description: Defining functions, parameters, return values, scope, lambdas, and type hints
order: 4
tags: [python, functions, scope]
---

# Chapter 4: Functions

## 4.1 Why functions?

> **Definition:** A **function** is a reusable block of code that performs a task, optionally taking inputs (**parameters**) and returning an output (**return value**).

Functions reduce duplication, improve readability, and enable testing in isolation.

## 4.2 Defining and calling

```python
def greet(name: str) -> str:
    """Return a greeting for name."""
    return f"Hello, {name}!"

message = greet("Alice")
print(message)
```

| Part | Role |
|------|------|
| `def` | Starts function definition |
| Parameters | Names in parentheses |
| Docstring | Documentation string |
| `return` | Sends value back to caller |

## 4.3 Parameters and arguments

```python
def power(base, exponent=2):
    return base ** exponent

power(3)       # 9 — default exponent=2
power(3, 3)    # 27
power(base=2, exponent=5)  # keyword args
```

### Parameter kinds

```python
def demo(pos_only, /, standard, *, kw_only):
    return pos_only, standard, kw_only

demo(1, 2, kw_only=3)
```

| Syntax | Meaning |
|--------|---------|
| `a, b` | Positional or keyword |
| `a, /` | Positional-only (before `/`) |
| `*, x` | Keyword-only (after `*`) |

## 4.4 `*args` and `**kwargs`

```python
def log(*args, **kwargs):
    print("args:", args)      # tuple
    print("kwargs:", kwargs)  # dict

log(1, 2, level="INFO", module="auth")
```

Unpack at call site:

```python
nums = [1, 2, 3]
print(*nums)  # 1 2 3

opts = {"sep": ", ", "end": "!\n"}
print("a", "b", **opts)
```

## 4.5 Return values

```python
def min_max(values):
    return min(values), max(values)  # returns tuple

lo, hi = min_max([3, 1, 4, 1, 5])
```

Functions without `return` implicitly return `None`.

## 4.6 Scope and the LEGB rule

> **Definition:** **Scope** is the region where a name is visible. Python resolves names: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # local
    inner()

outer()
print(x)  # global
```

### `global` and `nonlocal`

```python
count = 0

def increment():
    global count
    count += 1

def make_counter():
    n = 0
    def inner():
        nonlocal n
        n += 1
        return n
    return inner
```

Prefer passing values and returning results over mutating globals.

## 4.7 Lambda functions

```python
square = lambda x: x ** 2
sorted_pairs = sorted([(1, 3), (2, 1)], key=lambda p: p[1])
```

Lambdas are limited to a single expression — use `def` for complex logic.

## 4.8 Type hints

```python
from typing import List, Optional

def average(numbers: List[float]) -> Optional[float]:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
```

Type hints document intent; use `mypy` for static checking. See [Best Practices](./ch13-best-practices.md).

## 4.9 First-class functions

Functions are objects — assign, pass, store in collections:

```python
def shout(s): return s.upper()
def whisper(s): return s.lower()

transformers = [shout, whisper]
for fn in transformers:
    print(fn("Hello"))
```

This enables [decorators](./ch11-decorators-generators.md) and callbacks.

## 4.10 Docstrings and `help()`

```python
def add(a: int, b: int) -> int:
    """Add two integers and return the sum."""
    return a + b

help(add)
print(add.__doc__)
```

## 4.11 Recursion

```python
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

Ensure a base case to avoid `RecursionError`.

## 4.12 Mutable default arguments

```python
# BAD — same list reused every call
def bad(items=[]):
    items.append(1)
    return items

# GOOD
def good(items=None):
    if items is None:
        items = []
    items.append(1)
    return items
```

## Exercises

1. Write `celsius_to_fahrenheit(c)` returning `c * 9/5 + 32`.
2. Create a function accepting `*args` and returning their sum.
3. Implement `is_palindrome(s)` ignoring case and spaces.
4. Add type hints to all three functions above.

## Summary

Functions are the primary unit of reuse in Python. Master parameters, scope, unpacking, and type hints for maintainable code.

## Next chapter

Continue to [Data Structures](./ch05-data-structures.md).
