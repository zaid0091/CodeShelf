---
title: Functions
description: Defining functions, parameters, return values, scope, lambdas, recursion, and type hints
order: 4
tags: [python, functions, scope]
---

# Chapter 4: Functions

> **Functions are the primary way to organize logic. Learn parameters, scope, and patterns that scale from scripts to large applications.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [Why Functions Exist](#why-functions-exist)
2. [Defining and Calling Functions](#defining-and-calling-functions)
3. [Parameters vs Arguments](#parameters-vs-arguments)
4. [Return Values](#return-values)
5. [Default Parameters](#default-parameters)
6. [Keyword Arguments](#keyword-arguments)
7. [Positional-Only and Keyword-Only Parameters](#positional-only-and-keyword-only-parameters)
8. [*args and **kwargs](#args-and-kwargs)
9. [Unpacking at the Call Site](#unpacking-at-the-call-site)
10. [Scope and the LEGB Rule](#scope-and-the-legb-rule)
11. [global and nonlocal](#global-and-nonlocal)
12. [Lambda Functions](#lambda-functions)
13. [Type Hints](#type-hints)
14. [Docstrings and help()](#docstrings-and-help)
15. [First-Class Functions](#first-class-functions)
16. [Recursion](#recursion)
17. [Mutable Default Arguments](#mutable-default-arguments)
18. [Best Practices](#best-practices)
19. [Common Mistakes](#common-mistakes)
20. [Interview Points](#interview-points)
21. [Exercises](#exercises)
22. [Chapter Summary](#chapter-summary)

---

## Why Functions Exist

> **Definition:** Functions group reusable logic under a name — **Don't Repeat Yourself**.

### Why it matters

Change behavior in one place instead of many copy-pasted blocks.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def area(w, h):
    return w * h
print(area(3, 4), area(5, 2))
```


---

## Defining and Calling Functions

> **Definition:** Define with `def name(params):` and call with `name(args)`.

### Why it matters

Definition creates the function; call executes it.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def greet(name):
    return f'Hi, {name}'
print(greet('Sam'))
```


---

## Parameters vs Arguments

> **Definition:** **Parameters** appear in the `def` line; **arguments** are values you pass at the call.

### Why it matters

Positional arguments match parameters in order.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def power(base, exp):
    return base ** exp
print(power(2, 8))
```


---

## Return Values

> **Definition:** `return` sends a value back; omitting it returns `None`.

### Why it matters

Return early to simplify logic.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def abs_val(n):
    if n < 0:
        return -n
    return n
```


---

## Default Parameters

> **Definition:** Defaults apply when an argument is omitted.

### Why it matters

Defaults evaluate once at definition — avoid mutable defaults.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def greet(name, greeting='Hello'):
    return f'{greeting}, {name}'
```


---

## Keyword Arguments

> **Definition:** Pass `name=value` to skip order.

### Why it matters

Improves readability for many parameters.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
greet(name='Ada', greeting='Hi')
```


---

## Positional-Only and Keyword-Only Parameters

> **Definition:** `/` marks positional-only parameters; `*` starts keyword-only parameters (PEP 570).

### Why it matters

Library APIs use this to prevent breaking changes.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def f(a, b, /, c, *, d):
    return a+b+c+d
```


---

## *args and **kwargs

> **Definition:** `*args` collects extra positional tuple; `**kwargs` extra keyword dict.

### Why it matters

Used in wrappers and decorators.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def log(*args, **kwargs):
    print(args, kwargs)
```


---

## Unpacking at the Call Site

> **Definition:** `*sequence` and `**mapping` spread into positional and keyword arguments.

### Why it matters

Useful when arguments live in collections.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def f(a, b):
    return a+b
print(f(**{'a':1,'b':2}))
```


---

## Scope and the LEGB Rule

> **Definition:** Python looks up names: **L**ocal, **E**nclosing, **G**lobal, **B**uilt-in.

### Why it matters

Assignments create or update bindings in the innermost relevant scope.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
x = 'global'
def outer():
    x = 'enclosing'
    def inner():
        print(x)
    inner()
outer()
```


---

## global and nonlocal

> **Definition:** `global` updates a module-level name; `nonlocal` updates a variable in an enclosing function.

### Why it matters

Prefer passing values explicitly when possible.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def counter():
    n = 0
    def inc():
        nonlocal n
        n += 1
        return n
    return inc
```


---

## Lambda Functions

> **Definition:** `lambda args: expression` creates a small anonymous function.

### Why it matters

Use for short callbacks; use `def` for anything complex.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
nums = [1,2,3]
print(list(map(lambda x: x*x, nums)))
```


---

## Type Hints

> **Definition:** Annotations like `def f(x: int) -> str:` help static checkers.

### Why it matters

Not enforced at runtime in standard Python.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def slugify(text: str) -> str:
    return text.lower().replace(' ', '-')
```


---

## Docstrings and help()

> **Definition:** A string literal right after `def` is the **docstring** — documentation for `help()` and IDEs.

### Why it matters

Describe parameters, return value, and raised errors.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def add(a, b):
    '''Return the sum of a and b.'''
    return a + b
help(add)
```


---

## First-Class Functions

> **Definition:** Functions are objects — assign, store in lists, pass as arguments.

### Why it matters

Enables functional patterns.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def apply(fn, x):
    return fn(x)
print(apply(lambda v: v+1, 10))
```


---

## Recursion

> **Definition:** A function calls itself with a smaller problem until a base case.

### Why it matters

Use when problem is naturally recursive (trees).

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def fact(n):
    return 1 if n <= 1 else n * fact(n-1)
```


---

## Mutable Default Arguments

> **Definition:** Default values like `[]` are created **once** at function definition time.

### Why it matters

Shared mutable defaults cause bugs across calls.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def bad(x, items=[]):
    items.append(x)
    return items
print(bad(1), bad(2))  # surprise!
def good(x, items=None):
    if items is None: items = []
    items.append(x)
    return items
```


---

## Best Practices

### Guidelines

- Never use mutable default arguments
- Keep functions small and named clearly


---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Mutable default `def f(x=[])` | Shared list across calls | Use `None` and create inside |


---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: What is a function?**

Reusable named block — parameters in, return value out. Defined with `def`.

---

> **📌 Interview Point 2: Parameters vs arguments?**

**Parameters** in definition; **arguments** passed at call site.

---

> **📌 Interview Point 3: What is `*args` and `**kwargs`?**

Collect extra positional (`tuple`) and keyword (`dict`) arguments.

---

> **📌 Interview Point 4: What is LEGB?**

Scope lookup order: **L**ocal, **E**nclosing, **G**lobal, **B**uilt-in.

---

> **📌 Interview Point 5: What is a closure?**

Inner function remembering variables from enclosing scope — used in decorators.

---

> **📌 Interview Point 6: Mutable default argument trap?**

Default `[]` created once — shared across calls. Use `None` and create inside.

---

> **📌 Interview Point 7: What is recursion?**

Function calling itself — needs base case to stop.

---

> **📌 Interview Point 8: Lambda limitations?**

Single expression only — no statements; use `def` for complex logic.

---

> **📌 Interview Point 9: Positional-only vs keyword-only?**

PEP 570 `/` and `*` in signature control how callers may pass args.

---

> **📌 Interview Point 10: What are type hints?**

Optional annotations for static checkers (mypy) — not enforced at runtime.

---

> **📌 Interview Point 11: First-class functions?**

Functions are objects — assign, pass, return like any value.

---

> **📌 Interview Point 12: What does `return` without value?**

Returns `None` — same as falling off end of function.

---

> **📌 Interview Point 13: Docstring convention?**

Triple-quoted string right after `def` — documents purpose, params, returns.

---

> **📌 Interview Point 14: When use `global` / `nonlocal`?**

Rare — prefer return values and parameters. `nonlocal` updates enclosing (non-global) binding.

---

> **📌 Interview Point 15: What is unpacking?**

`a, b = (1, 2)` or `*rest` — at definition and call sites.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Greet function ⭐

**Task:** Define `greet(name)` returning hello message.

<details>
<summary>💡 Hint (click to reveal)</summary>

def + return f-string.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def greet(name):
    return f"Hello, {name}!"
```

</details>

---

### Exercise 2: Power function ⭐⭐

**Task:** `power(base, exp=2)` with default exponent.

<details>
<summary>💡 Hint (click to reveal)</summary>

Use default parameter.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def power(base, exp=2):
    return base ** exp
```

</details>

---

### Exercise 3: Variable args sum ⭐⭐

**Task:** `*args` sum all numbers.

<details>
<summary>💡 Hint (click to reveal)</summary>

Loop or built-in sum.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def add_all(*args):
    return sum(args)
```

</details>

---

### Exercise 4: LEGB closure ⭐⭐

**Task:** Inner function increments counter in enclosing scope.

<details>
<summary>💡 Hint (click to reveal)</summary>

nonlocal.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
```

</details>

---

### Exercise 5: Recursive factorial ⭐⭐⭐

**Task:** factorial(n) recursive with base case.

<details>
<summary>💡 Hint (click to reveal)</summary>

n<=1 return 1.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)
```

</details>

---

### Exercise 6: Keyword-only API ⭐⭐⭐

**Task:** Function with `*, name, age`.

<details>
<summary>💡 Hint (click to reveal)</summary>

Call must use keywords after *.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def create_user(*, name, age):
    return {"name": name, "age": age}
print(create_user(name="A", age=30))
```

</details>


## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **def** | Reusable named blocks with return |
| **Parameters** | Positional, keyword, defaults, * and ** |
| **Scope** | LEGB lookup order |
| **Closures** | Inner functions capture enclosing names |
| **Type hints** | Optional static checking with mypy |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**⬅️ [Previous: Control Flow](./ch03-control-flow.md)**

**➡️ [Next: Data Structures →](./ch05-data-structures.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
