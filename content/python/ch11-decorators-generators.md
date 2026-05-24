---
title: Decorators and Generators
description: Function decorators, generators, iterators, and itertools
order: 11
tags: [python, decorators, generators]
---

# Chapter 11: Decorators and Generators

## 11.1 Iterators

> **Definition:** An **iterator** is an object implementing `__iter__()` and `__next__()`, yielding items one at a time until `StopIteration`.

```python
nums = iter([1, 2, 3])
next(nums)  # 1
next(nums)  # 2
next(nums)  # 3
next(nums)  # StopIteration
```

Lists, dicts, and strings are **iterables** — they produce iterators via `iter()`.

## 11.2 Generator functions

> **Definition:** A **generator function** uses `yield` to produce a lazy sequence, pausing state between yields.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)
```

Generators are iterators — memory-efficient for large or infinite sequences.

## 11.3 Generator expressions

Review [Comprehensions](./ch06-comprehensions.md):

```python
squares = (x ** 2 for x in range(1_000_000))
total = sum(x ** 2 for x in range(100))
```

## 11.4 `yield from`

```python
def chain(*iterables):
    for it in iterables:
        yield from it

list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]
```

Delegates to a sub-iterator or sub-generator.

## 11.5 What are decorators?

> **Definition:** A **decorator** is a callable that takes a function and returns a modified or wrapped function — syntactic sugar for `@decorator` above `def`.

```python
def loud(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@loud
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
# Calling greet
# 'Hello, Alice!'
```

`@loud` is equivalent to `greet = loud(greet)`.

## 11.6 Decorators with arguments

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")
```

## 11.7 Preserving metadata with `functools.wraps`

```python
from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)
    return wrapper
```

Without `@wraps`, `wrapper.__name__` would be `"wrapper"`.

## 11.8 Built-in decorators

| Decorator | Purpose |
|-----------|---------|
| `@property` | Computed attribute |
| `@classmethod` | Class-level method |
| `@staticmethod` | No implicit first arg |
| `@abstractmethod` | Force override (ABC) |

See [OOP](./ch07-oop.md).

## 11.9 Class decorators

```python
def singleton(cls):
    instances = {}
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    pass
```

## 11.10 `contextlib.contextmanager`

```python
from contextlib import contextmanager

@contextmanager
def opened(path, mode="r"):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()
```

Bridges generators and [context managers](./ch10-exceptions.md).

## 11.11 `itertools` highlights

```python
import itertools

list(itertools.islice(countdown(10), 3))
list(itertools.chain([1, 2], [3]))
list(itertools.product([0, 1], repeat=3))[:4]
```

| Function | Use |
|----------|-----|
| `count` | Infinite counter |
| `cycle` | Repeat iterable |
| `islice` | Slice iterator |
| `chain` | Concatenate iterables |
| `product` | Cartesian product |

## 11.12 When to use generators

| Scenario | Use generator |
|----------|---------------|
| Large file line-by-line | Yes |
| Infinite streams | Yes |
| Pipeline of transforms | Yes |
| Need random access / len | No — use list |

## Exercises

1. Write a generator `fibonacci()` yielding Fibonacci numbers (use `islice` to take first 10).
2. Create a `@timer` decorator that prints execution time.
3. Build a decorator `@validate_positive` that checks all numeric args are > 0.
4. Use `yield from` to flatten a nested list `[1, [2, [3, 4]], 5]`.

## Summary

Generators produce lazy sequences; decorators wrap functions to add behavior. Both rely on functions as first-class objects from [Functions](./ch04-functions.md).

## Next chapter

Continue to [Virtual Environments & pip](./ch12-virtual-env-pip.md).
