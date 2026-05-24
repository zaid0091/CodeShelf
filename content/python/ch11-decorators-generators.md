---
title: Decorators and Generators
description: yield, iterators, decorators, functools.wraps, itertools, and contextmanager
order: 11
tags: [python, decorators, generators]
---

# Chapter 11: Decorators and Generators

> **Generators stream data lazily; decorators wrap functions to add behavior — two powerful ideas for advanced Python.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [Functions as First-Class Objects](#functions-as-first-class-objects)
2. [Iterables vs Iterators](#iterables-vs-iterators)
3. [The Iterator Protocol](#the-iterator-protocol)
4. [Generator Functions and yield](#generator-functions-and-yield)
5. [Generator Expressions](#generator-expressions)
6. [yield from Delegation](#yield-from-delegation)
7. [Sending Values to Generators](#sending-values-to-generators)
8. [When to Use Generators](#when-to-use-generators)
9. [What Are Decorators?](#what-are-decorators)
10. [Writing Your First Decorator](#writing-your-first-decorator)
11. [Decorators with Arguments](#decorators-with-arguments)
12. [functools.wraps](#functools-wraps)
13. [Stacking Decorators](#stacking-decorators)
14. [Built-in Decorators](#built-in-decorators)
15. [Class Decorators](#class-decorators)
16. [contextlib.contextmanager](#contextlib-contextmanager)
17. [The itertools Module](#the-itertools-module)
18. [Best Practices](#best-practices)
19. [Common Mistakes](#common-mistakes)
20. [functools Beyond Decorators](#functools-beyond-decorators)
21. [More itertools Recipes](#more-itertools-recipes)
22. [Interview Points](#interview-points)
23. [Exercises](#exercises)
24. [Chapter Summary](#chapter-summary)

---

## Functions as First-Class Objects

> **Definition:** Functions can be assigned and passed like any value.

### Why it matters

Foundation for decorators.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def shout(s): return s.upper()
fn = shout
print(fn('hi'))
```


---

## Iterables vs Iterators

> **Definition:** **Iterable** can produce iterator; **iterator** has `__next__`.

### Why it matters

for-loops use iterators under the hood.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
it = iter([1,2])
print(next(it), next(it))
```


---

## The Iterator Protocol

> **Definition:** Implement `__iter__` returning self and `__next__` raising StopIteration.

### Why it matters

Custom sequences and streams.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class Count:
    def __init__(self, n): self.n, self.i = n, 0
    def __iter__(self): return self
    def __next__(self):
        if self.i >= self.n: raise StopIteration
        self.i += 1; return self.i
```


---

## Generator Functions and yield

> **Definition:** `yield` pauses function preserving state.

### Why it matters

Lazy sequences without storing all values.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def gen():
    yield 1
    yield 2
print(list(gen()))
```


---

## Generator Expressions

> **Definition:** `(x for x in it)` like list comp but lazy.

### Why it matters

Pass to `sum`, `max`, etc.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
print(sum(x*x for x in range(1000)))
```


---

## yield from Delegation

> **Definition:** `yield from subgen` delegates to another generator.

### Why it matters

Flatten nested iteration.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def chain(a, b):
    yield from a
    yield from b
```


---

## Sending Values to Generators

> **Definition:** `.send(value)` injects into `yield` expression.

### Why it matters

Coroutine-style generators (advanced).

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def acc():
    total = 0
    while True:
        x = yield total
        if x is not None:
            total += x
g = acc(); next(g); print(g.send(10))
```


---

## When to Use Generators

> **Definition:** Large datasets, pipelines, infinite streams.

### Why it matters

Memory bounded processing.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def read_chunks(path, size=1024):
    with open(path,'rb') as f:
        while chunk := f.read(size):
            yield chunk
```


---

## What Are Decorators?

> **Definition:** Decorators wrap functions to add behavior without changing their code.

### Why it matters

Logging, auth, timing, caching.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def deco(fn):
    def wrapper(*a, **k):
        return fn(*a, **k)
    return wrapper
```


---

## Writing Your First Decorator

> **Definition:** Outer function returns wrapper that calls original.

### Why it matters

Apply with `@deco` above `def`.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def log(fn):
    def wrapper(*a, **k):
        print('call', fn.__name__)
        return fn(*a, **k)
    return wrapper
@log
def add(a,b): return a+b
```


---

## Decorators with Arguments

> **Definition:** Extra outer function returns the decorator.

### Why it matters

Configure decorator behavior.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def repeat(n):
    def deco(fn):
        def wrapper(*a, **k):
            for _ in range(n): fn(*a, **k)
        return wrapper
    return deco
```


---

## functools.wraps

> **Definition:** Copies metadata from wrapped function to wrapper.

### Why it matters

Preserves `__name__` and docstrings.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
from functools import wraps
def deco(fn):
    @wraps(fn)
    def wrapper(*a, **k):
        return fn(*a, **k)
    return wrapper
```


---

## Stacking Decorators

> **Definition:** Applied bottom-up: `@a @b def f` → `a(b(f))`.

### Why it matters

Order matters.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
@dec_a
@dec_b
def f(): pass
```


---

## Built-in Decorators

> **Definition:** `@property`, `@classmethod`, `@staticmethod`.

### Why it matters

Language-supported patterns.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class C:
    @classmethod
    def create(cls):
        return cls()
```


---

## Class Decorators

> **Definition:** Classes can decorate functions or other classes.

### Why it matters

Rare but powerful.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class Tag:
    def __init__(self, t): self.t = t
    def __call__(self, fn):
        return fn
```


---

## contextlib.contextmanager

> **Definition:** Decorator turning generator into context manager.

### Why it matters

Simpler than class-based managers.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
from contextlib import contextmanager
@contextmanager
def opened(path):
    f = open(path)
    try:
        yield f
    finally:
        f.close()
```


---

## The itertools Module

> **Definition:** Iterator algebra: `chain`, `islice`, `groupby`, etc.

### Why it matters

Express combinatorics without nested loops.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
from itertools import islice
print(list(islice(range(10), 3)))
```


---

## Best Practices

### Guidelines

- Always use functools.wraps
- Generators for large data


---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Decorator forgetting return wrapper | Replaces function with None | return wrapper |


---

## functools Beyond Decorators

> **Definition:** `partial`, `lru_cache`, `reduce`.

### Why it matters

Reuse and memoization.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
from functools import lru_cache
@lru_cache
def fib(n):
    return n if n < 2 else fib(n-1)+fib(n-2)
```


---

## More itertools Recipes

> **Definition:** See `itertools` docs recipes section.

### Why it matters

Professional one-liners for streams.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
from itertools import accumulate
print(list(accumulate([1,2,3,4])))
```


---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: What is a generator?**

Function with `yield` — lazy iterator, pauses state between yields.

---

> **📌 Interview Point 2: Generator vs list?**

Generator O(1) memory streaming; list stores all elements.

---

> **📌 Interview Point 3: What is decorator?**

Callable wrapping another callable — adds behavior without changing source.

---

> **📌 Interview Point 4: functools.wraps why?**

Preserves wrapped function `__name__`, docstring for debugging.

---

> **📌 Interview Point 5: Decorator with arguments?**

Outer function returns actual decorator — three levels of nesting.

---

> **📌 Interview Point 6: Iterator protocol?**

`__iter__` returns self; `__next__` raises `StopIteration` when done.

---

> **📌 Interview Point 7: Generator expression vs comprehension?**

Parentheses `(...)` lazy; brackets eager list.

---

> **📌 Interview Point 8: yield from?**

Delegates to sub-generator — simplifies recursive generators.

---

> **📌 Interview Point 9: Built-in decorators?**

`@property`, `@staticmethod`, `@classmethod`, `@dataclass`.

---

> **📌 Interview Point 10: Class decorator?**

Function taking class, returning modified class — registration patterns.

---

> **📌 Interview Point 11: contextmanager decorator?**

`@contextmanager` turns generator with one `yield` into context manager.

---

> **📌 Interview Point 12: itertools infinite iterators?**

`count`, `cycle`, `repeat` — use with limit logic.

---

> **📌 Interview Point 13: Send to generator?**

`.send(value)` injects into `yield` expression — coroutine precursor.

---

> **📌 Interview Point 14: Decorator stacking order?**

Bottom decorator applied first — `f = dec2(dec1(f))`.

---

> **📌 Interview Point 15: When not use decorator?**

Simple one-off — plain function call clearer.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Double decorator ⭐⭐

**Task:** Decorator multiplying return by 2.

<details>
<summary>💡 Hint (click to reveal)</summary>

@wraps.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
from functools import wraps
def double(fn):
    @wraps(fn)
    def wrapper(*a, **k):
        return fn(*a, **k) * 2
    return wrapper
```

</details>

---

### Exercise 2: Countdown generator ⭐⭐

**Task:** yield from range.

<details>
<summary>💡 Hint (click to reveal)</summary>

generator function.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def countdown(n):
    while n:
        yield n
        n -= 1
```

</details>


## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **yield** | Pause function → iterator |
| **decorator** | Callable wrapping callable |
| **wraps** | Preserve metadata |
| **itertools** | Iterator algebra |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**⬅️ [Previous: Exceptions](./ch10-exceptions.md)**

**➡️ [Next: Virtual Environments and pip →](./ch12-virtual-env-pip.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
