---
title: Data Structures
description: Lists, tuples, dictionaries, sets, slicing, and collection methods
order: 5
tags: [python, lists, dicts, sets]
---

# Chapter 5: Data Structures

## 5.1 Overview

> **Definition:** A **data structure** organizes and stores data so it can be accessed and modified efficiently.

| Type | Ordered | Mutable | Duplicates | Syntax |
|------|---------|---------|------------|--------|
| `list` | Yes | Yes | Yes | `[1, 2]` |
| `tuple` | Yes | No | Yes | `(1, 2)` |
| `dict` | Yes* | Yes | Keys unique | `{"a": 1}` |
| `set` | No | Yes | No | `{1, 2}` |

*Dict insertion order is preserved (Python 3.7+).

Review [Data Types](./ch02-data-types.md) for scalar types.

## 5.2 Lists

```python
nums = [1, 2, 3]
nums.append(4)
nums.extend([5, 6])
nums.insert(0, 0)
last = nums.pop()
nums.remove(2)
nums.sort()
nums.reverse()
```

### Slicing

```python
data = [0, 1, 2, 3, 4, 5]
data[1:4]    # [1, 2, 3]
data[:3]     # [0, 1, 2]
data[::2]    # every second element
data[::-1]   # reversed copy
```

Slicing returns a **new** list — the original is unchanged.

### List methods reference

| Method | Effect |
|--------|--------|
| `append(x)` | Add one item at end |
| `extend(iterable)` | Add all items |
| `insert(i, x)` | Insert at index |
| `remove(x)` | Remove first matching value |
| `pop([i])` | Remove and return item |
| `clear()` | Remove all |
| `index(x)` | First index of value |
| `count(x)` | Count occurrences |

## 5.3 Tuples

```python
point = (10, 20)
x, y = point  # unpacking

single = (42,)  # trailing comma for one-element tuple
empty = ()
```

Use tuples for fixed records, dict keys, and return values from [functions](./ch04-functions.md).

## 5.4 Dictionaries

> **Definition:** A **dictionary** maps hashable keys to values — average O(1) lookup.

```python
user = {"name": "Alice", "age": 30}
user["email"] = "alice@example.com"
user.get("phone", "N/A")
del user["age"]

for key, value in user.items():
    print(key, value)
```

### Useful methods

```python
d = {"a": 1, "b": 2}
d.keys()
d.values()
d.items()
d.update({"c": 3})
d.pop("a", None)
```

### Dictionary comprehension preview

```python
squares = {x: x ** 2 for x in range(5)}
```

See [Comprehensions](./ch06-comprehensions.md).

## 5.5 Sets

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b   # union: {1, 2, 3, 4, 5}
a & b   # intersection: {3}
a - b   # difference: {1, 2}
a ^ b   # symmetric difference: {1, 2, 4, 5}

tags = {"python", "web", "python"}
len(tags)  # 2 — duplicates removed
```

Sets require hashable elements (no lists inside sets).

## 5.6 Nested structures

```python
students = [
    {"name": "Alice", "grades": [90, 85]},
    {"name": "Bob", "grades": [78, 92]},
]

students[0]["grades"].append(88)
```

## 5.7 Copying: shallow vs deep

```python
import copy

original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)

original[0].append(99)
# shallow[0] also changed; deep[0] unchanged
```

| Method | Behavior |
|--------|----------|
| `=` | Same object reference |
| `.copy()` / `list()` | Shallow copy |
| `copy.deepcopy()` | Recursive copy |

## 5.8 Sorting

```python
nums = [3, 1, 4, 1, 5]
sorted(nums)           # new list
nums.sort()            # in-place

people = [("Alice", 30), ("Bob", 25)]
sorted(people, key=lambda p: p[1])
```

## 5.9 `collections` module highlights

```python
from collections import defaultdict, Counter, deque

dd = defaultdict(list)
dd["fruits"].append("apple")

counts = Counter("abracadabra")
# Counter({'a': 5, 'b': 2, ...})

queue = deque([1, 2, 3])
queue.appendleft(0)
```

## 5.10 Choosing the right structure

| Need | Use |
|------|-----|
| Ordered mutable sequence | `list` |
| Fixed record / hashable key | `tuple` |
| Key-value lookup | `dict` |
| Unique membership / set math | `set` |
| Fast append/pop from both ends | `deque` |

## Exercises

1. Given `words = ["apple", "banana", "apple", "cherry"]`, count occurrences with `Counter`.
2. Merge two dicts: `{"a": 1}` and `{"b": 2}` (use `{**d1, **d2}` or `.update()`).
3. Remove duplicates from a list while preserving order (hint: `dict.fromkeys`).
4. Build a nested dict representing a simple file tree.

## Summary

Lists, tuples, dicts, and sets are the core containers in Python. Pick the right one for mutability, ordering, and lookup patterns.

## Next chapter

Continue to [Comprehensions](./ch06-comprehensions.md).
