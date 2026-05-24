---
title: Exceptions
description: try/except, raising errors, custom exceptions, and context managers
order: 10
tags: [python, exceptions, errors]
---

# Chapter 10: Exceptions

## 10.1 What are exceptions?

> **Definition:** An **exception** is an event that disrupts normal program flow. Python uses **try/except** blocks to handle errors gracefully instead of crashing.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Unhandled exceptions propagate up the call stack and terminate the program with a traceback.

## 10.2 try / except / else / finally

```python
def read_number(path):
    try:
        value = int(open(path).read().strip())
    except FileNotFoundError:
        print("File missing")
        return None
    except ValueError:
        print("Not a valid integer")
        return None
    else:
        print("Read succeeded")
        return value
    finally:
        print("Cleanup runs always")
```

| Clause | Runs when |
|--------|-----------|
| `try` | Body that may raise |
| `except` | Matching exception caught |
| `else` | No exception in `try` |
| `finally` | Always (cleanup) |

## 10.3 Catching multiple exceptions

```python
try:
    process(data)
except (TypeError, ValueError) as e:
    print(f"Bad data: {e}")
except Exception as e:
    print(f"Unexpected: {e}")
```

Catch specific exceptions first; avoid bare `except:` — use `except Exception:` if you need a broad handler.

## 10.4 Raising exceptions

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise InsufficientFundsError("Not enough balance")
    return balance - amount
```

Use `raise` to signal invalid state or failed preconditions.

## 10.5 Custom exception classes

```python
class AppError(Exception):
    """Base for application errors."""

class ValidationError(AppError):
    def __init__(self, field, message):
        self.field = field
        super().__init__(message)

raise ValidationError("email", "Invalid format")
```

Inherit from `Exception` (or a project base) and add attributes as needed.

## 10.6 Exception hierarchy (common)

| Exception | Typical cause |
|-----------|---------------|
| `ValueError` | Wrong value, right type |
| `TypeError` | Wrong type |
| `KeyError` | Missing dict key |
| `IndexError` | Invalid sequence index |
| `FileNotFoundError` | Missing file |
| `AttributeError` | Missing attribute |
| `ZeroDivisionError` | Division by zero |

See [File I/O](./ch09-file-io.md) for file-related errors.

## 10.7 Re-raising with `raise from`

```python
try:
    config = json.loads(raw)
except json.JSONDecodeError as e:
    raise ConfigError("Invalid config file") from e
```

Preserves the original traceback chain for debugging.

## 10.8 Assertions

```python
def divide(a, b):
    assert b != 0, "divisor must be non-zero"
    return a / b
```

Assertions are for programmer errors and may be disabled with `python -O`. Do not use for user input validation.

## 10.9 Context managers

```python
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        return False  # do not suppress exceptions

with Timer() as t:
    do_work()
print(t.elapsed)
```

`contextlib.contextmanager` simplifies this — see [Decorators & Generators](./ch11-decorators-generators.md).

```python
from contextlib import contextmanager

@contextmanager
def temp_file(suffix):
    path = create_temp(suffix)
    try:
        yield path
    finally:
        path.unlink()
```

## 10.10 EAFP vs LBYL

| Style | Meaning | Python preference |
|-------|---------|-------------------|
| EAFP | Easier to Ask Forgiveness than Permission | Preferred |
| LBYL | Look Before You Leap | Use when check is cheap |

```python
# EAFP
try:
    value = data[key]
except KeyError:
    value = default

# LBYL
value = data[key] if key in data else default
# or: value = data.get(key, default)
```

## Exercises

1. Write a function that divides two numbers and handles `ZeroDivisionError`.
2. Create `InvalidAgeError` raised when age is negative or over 150.
3. Implement a context manager that prints "Starting" and "Done" around a block.
4. Refactor file-reading code to use try/except for `FileNotFoundError` and `PermissionError`.

## Summary

Exceptions separate error handling from happy-path logic. Catch specific types, raise meaningful errors, and use `finally` or context managers for cleanup.

## Next chapter

Continue to [Decorators & Generators](./ch11-decorators-generators.md).
