---
title: Exceptions
description: try/except, raising, custom exceptions, EAFP, and context managers
order: 10
tags: [python, exceptions, errors]
---

# Chapter 10: Exceptions

> **Errors happen. Exceptions let programs recover gracefully instead of crashing silently or confusing users.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [Errors vs Exceptions](#errors-vs-exceptions)
2. [How Exceptions Propagate](#how-exceptions-propagate)
3. [try / except Basics](#try-except-basics)
4. [else and finally Clauses](#else-and-finally-clauses)
5. [Catching Multiple Exceptions](#catching-multiple-exceptions)
6. [Exception Objects and as](#exception-objects-and-as)
7. [Raising Exceptions](#raising-exceptions)
8. [Custom Exception Classes](#custom-exception-classes)
9. [The Exception Hierarchy](#the-exception-hierarchy)
10. [Re-raising and Exception Chaining](#re-raising-and-exception-chaining)
11. [Assertions](#assertions)
12. [EAFP vs LBYL](#eafp-vs-lbyl)
13. [Context Managers](#context-managers)
14. [contextlib Utilities](#contextlib-utilities)
15. [Exceptions in Real Applications](#exceptions-in-real-applications)
16. [Best Practices](#best-practices)
17. [Common Mistakes](#common-mistakes)
18. [Reading Tracebacks](#reading-tracebacks)
19. [Exception Handling in APIs](#exception-handling-in-apis)
20. [Logging Exceptions](#logging-exceptions)
21. [Interview Points](#interview-points)
22. [Exercises](#exercises)
23. [Chapter Summary](#chapter-summary)

---

## Errors vs Exceptions

> **Definition:** **Syntax errors** fail before run; **exceptions** occur at runtime.

### Why it matters

Exceptions can be caught and handled.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
try:
    1/0
except ZeroDivisionError:
    print('handled')
```


---

## How Exceptions Propagate

> **Definition:** Uncaught exceptions bubble up the call stack.

### Why it matters

Tracebacks show the chain.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def inner():
    raise ValueError('bad')
def outer():
    inner()
```


---

## try / except Basics

> **Definition:** Wrap risky code in `try`; handle in `except`.

### Why it matters

Recover or show friendly errors.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
try:
    n = int('x')
except ValueError:
    n = 0
```


---

## else and finally Clauses

> **Definition:** `else` runs if no exception; `finally` always runs.

### Why it matters

Use `finally` for cleanup.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
try:
    f = open('t.txt')
except FileNotFoundError:
    pass
finally:
    print('done')
```


---

## Catching Multiple Exceptions

> **Definition:** Tuple of types or multiple `except` blocks.

### Why it matters

Catch specific types first.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
try:
    risky()
except (ValueError, TypeError) as e:
    print(e)
```


---

## Exception Objects and as

> **Definition:** `except E as e` binds the instance.

### Why it matters

Log `e` or its args.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
try:
    {}
except KeyError as e:
    print(repr(e))
```


---

## Raising Exceptions

> **Definition:** `raise ValueError('msg')` signals errors.

### Why it matters

Validate inputs early.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def withdraw(amount):
    if amount < 0:
        raise ValueError('negative')
```


---

## Custom Exception Classes

> **Definition:** Subclass `Exception` for domain errors.

### Why it matters

Callers catch your type specifically.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class PaymentError(Exception):
    pass
raise PaymentError('declined')
```


---

## The Exception Hierarchy

> **Definition:** Catch `Exception` broadly; subclass for precision.

### Why it matters

Do not catch `BaseException` unless you know why.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
print(issubclass(ValueError, Exception))
```


---

## Re-raising and Exception Chaining

> **Definition:** `raise` from `e` preserves context.

### Why it matters

Debugging across layers.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
try:
    int('x')
except ValueError as e:
    raise RuntimeError('bad input') from e
```


---

## Assertions

> **Definition:** `assert cond, msg` for developer checks (can be disabled with -O).

### Why it matters

Not for user input validation.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
assert 2 + 2 == 4
```


---

## EAFP vs LBYL

> **Definition:** **Easier to ask forgiveness** — try/except; **look before you leap** — check first.

### Why it matters

Python culture prefers EAFP.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
try:
    return d[key]
except KeyError:
    return default
```


---

## Context Managers

> **Definition:** `with` ensures setup/teardown.

### Why it matters

Files, locks, DB connections.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
with open('f.txt') as f:
    use(f)
```


---

## contextlib Utilities

> **Definition:** `contextlib.contextmanager` builds managers from generators.

### Why it matters

Reuse cleanup patterns.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
from contextlib import contextmanager
@contextmanager
def tag(name):
    print(f'<{name}>')
    yield
    print(f'</{name}>')
```


---

## Exceptions in Real Applications

> **Definition:** Map errors to HTTP status or user messages.

### Why it matters

Log stack traces server-side only.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def api_handler():
    try:
        return process()
    except ValidationError as e:
        return {'error': str(e)}, 400
```


---

## Best Practices

### Guidelines

- Catch specific exceptions
- Use finally for cleanup


---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Bare except: | Hides bugs | except Exception as e: |


---

## Reading Tracebacks

> **Definition:** Read **bottom** line first (where it started), then up.

### Why it matters

Search the message and line number.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# practice reading Traceback in REPL
```


---

## Exception Handling in APIs

> **Definition:** Return structured errors; never bare 500 without logging.

### Why it matters

Consistent JSON error shape.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
{'error': {'code': 'NOT_FOUND', 'message': '...'}}
```


---

## Logging Exceptions

> **Definition:** Use `logging.exception` inside `except` to include traceback.

### Why it matters

Better than `print` in production.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import logging
log = logging.getLogger(__name__)
try:
    1/0
except ZeroDivisionError:
    log.exception('failed')
```


---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: Exception vs syntax error?**

Syntax: parse time. Exception: runtime after valid syntax.

---

> **📌 Interview Point 2: try/except/else/finally order?**

`try` body; `except` on match; `else` if no exception; `finally` always runs.

---

> **📌 Interview Point 3: Bare `except`?**

Catches everything including `KeyboardInterrupt` — avoid; catch specific types.

---

> **📌 Interview Point 4: EAFP vs LBYL?**

**Easier to Ask Forgiveness** (try) vs **Look Before You Leap** (if checks) — Pythonic EAFP.

---

> **📌 Interview Point 5: Custom exception when?**

Domain errors users can catch — inherit from `Exception`, not `BaseException`.

---

> **📌 Interview Point 6: Re-raise with `raise`?**

Preserves traceback; `raise New from old` chains context.

---

> **📌 Interview Point 7: Assertion vs exception?**

`assert` for developer bugs — disabled with `-O`; use exceptions for user errors.

---

> **📌 Interview Point 8: Context manager protocol?**

`__enter__`/`__exit__` or `@contextmanager` with yield.

---

> **📌 Interview Point 9: Exception hierarchy?**

Catch specific before general; `Exception` catches most, not `SystemExit`.

---

> **📌 Interview Point 10: finally vs else?**

`else` only if no exception; `finally` always (cleanup).

---

> **📌 Interview Point 11: What is BaseException?**

Root — includes `SystemExit`, `KeyboardInterrupt` — rarely catch directly.

---

> **📌 Interview Point 12: ValueError vs TypeError?**

Right type wrong value vs wrong type entirely.

---

> **📌 Interview Point 13: Logging exceptions?**

`logging.exception()` in except block includes traceback.

---

> **📌 Interview Point 14: Exception groups 3.11+?**

`except*` handles ExceptionGroup from parallel tasks.

---

> **📌 Interview Point 15: When not to catch?**

Let bugs propagate in dev; catch at boundaries in production with logging.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Divide safe ⭐

**Task:** try/except ZeroDivisionError.

<details>
<summary>💡 Hint (click to reveal)</summary>

except specific type.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

</details>

---

### Exercise 2: Custom error ⭐⭐

**Task:** Raise ValueError for negative age.

<details>
<summary>💡 Hint (click to reveal)</summary>

if age < 0: raise.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
```

</details>


## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **try/except** | Handle expected failures |
| **finally** | Always-run cleanup |
| **raise** | Signal errors with types |
| **EAFP** | Try first — Pythonic style |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**⬅️ [Previous: File I/O](./ch09-file-io.md)**

**➡️ [Next: Decorators and Generators →](./ch11-decorators-generators.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
