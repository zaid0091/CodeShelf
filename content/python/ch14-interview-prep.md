---
title: Python Interview Preparation
description: Common Python interview questions, patterns, and coding challenges
order: 14
tags: [python, interview, career]
---

# Chapter 14: Python Interview Preparation

## 14.1 How to prepare

| Area | Focus |
|------|--------|
| Language fundamentals | Types, control flow, [functions](./ch04-functions.md) |
| Data structures | [Lists, dicts, sets](./ch05-data-structures.md), complexity |
| OOP | [Classes, inheritance](./ch07-oop.md), magic methods |
| Standard library | itertools, collections, pathlib |
| Problem solving | LeetCode easy/medium in Python |

## 14.2 Frequently asked concepts

### List vs tuple vs set vs dict

| Type | Mutable | Ordered | Duplicates | Use case |
|------|---------|---------|------------|----------|
| list | Yes | Yes | Yes | General sequence |
| tuple | No | Yes | Yes | Immutable record |
| set | Yes | No | No | Unique membership |
| dict | Yes | Yes* | Keys unique | Key-value map |

### Shallow vs deep copy

```python
import copy
a = [[1, 2], [3, 4]]
b = a.copy()           # shallow
c = copy.deepcopy(a)   # deep
```

### `*args` and `**kwargs`

Explain packing in function definition and unpacking at call site. See [Functions](./ch04-functions.md).

### GIL (Global Interpreter Lock)

> **Definition:** The **GIL** allows only one thread to execute Python bytecode at a time in CPython — limits CPU-bound multithreading but not I/O-bound work.

Use `multiprocessing` for CPU-bound parallelism; `asyncio` or threads for I/O.

## 14.3 Coding patterns

### Two pointers

```python
def is_palindrome(s: str) -> bool:
    s = "".join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

### Sliding window

```python
def max_sum_subarray(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best
```

### Frequency counter

```python
from collections import Counter

def anagrams(a, b):
    return Counter(a) == Counter(b)
```

## 14.4 Python-specific questions

**Q: What is a decorator?**

A function that wraps another function to extend behavior without modifying its source. See [Decorators & Generators](./ch11-decorators-generators.md).

**Q: Difference between `__str__` and `__repr__`?**

- `__str__` — user-friendly (`str(obj)`)
- `__repr__` — unambiguous, ideally valid Python (`repr(obj)`)

**Q: What are generators?**

Functions using `yield` that produce lazy iterators — memory efficient.

**Q: `is` vs `==`?**

- `==` compares values
- `is` compares identity (same object in memory)

**Q: How does dict lookup work?**

Hash table — O(1) average case; keys must be hashable.

## 14.5 Time complexity cheat sheet

| Operation | list | dict | set |
|-----------|------|------|-----|
| Access by index/key | O(1) | O(1) avg | — |
| Search (membership) | O(n) | O(1) avg | O(1) avg |
| Insert append | O(1)* | O(1) avg | O(1) avg |
| Delete | O(n) | O(1) avg | O(1) avg |

*Amortized for list append.

## 14.6 Common gotchas

```python
# Mutable default
def bad(x, items=[]):
    items.append(x)
    return items

# Late binding closures in loops
funcs = [lambda: i for i in range(3)]
[f() for f in funcs]  # [2, 2, 2] — not [0, 1, 2]

# Fix
funcs = [lambda i=i: i for i in range(3)]
```

## 14.7 System design (Python backend)

Be ready to discuss:

- REST vs GraphQL
- Django/Flask/FastAPI tradeoffs
- Caching (Redis)
- Database indexing and ORM N+1 queries
- Celery for background tasks

Link to [Django course](../django/ch00-course-overview.md) for web-specific prep.

## 14.8 Behavioral tips

- Think aloud during live coding
- Clarify inputs, edge cases, and expected output
- Start with brute force, then optimize
- Write tests for your solution

## 14.9 Practice problems

1. Reverse a linked list (if implementing in Python, use classes).
2. Find the first non-repeating character in a string.
3. Merge two sorted lists.
4. Implement LRU cache with `OrderedDict` or `dict` + linked list.
5. Parse a nested JSON and flatten keys with dot notation.

## 14.10 Resources

| Resource | Type |
|----------|------|
| Official Python docs | Reference |
| LeetCode / HackerRank | Coding practice |
| Real Python articles | Tutorials |
| This course (ch01–ch13) | Structured review |

## Summary

Interview success combines language fluency, algorithm practice, and clear communication. Review core chapters, drill common patterns, and practice explaining tradeoffs out loud.

## Course complete

Return to [Course Overview](./ch00-course-overview.md) or continue with the [Django course](../django/ch00-course-overview.md).
