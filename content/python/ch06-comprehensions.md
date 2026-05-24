---
title: Comprehensions
description: List, dict, and set comprehensions plus generator expressions
order: 6
tags: [python, comprehensions, generators]
---

# Chapter 6: Comprehensions

## 6.1 What are comprehensions?

> **Definition:** A **comprehension** is a concise syntax for building collections from iterables, often replacing multi-line [loops](./ch03-control-flow.md).

Comprehensions are idiomatic Python — readable when kept simple.

## 6.2 List comprehensions

```python
squares = [x ** 2 for x in range(10)]

evens = [x for x in range(20) if x % 2 == 0]

matrix = [[i * j for j in range(3)] for i in range(3)]
```

### Syntax

```text
[expression for item in iterable if condition]
```

| Part | Required |
|------|----------|
| `expression` | Yes — value stored |
| `for item in iterable` | Yes |
| `if condition` | No — filter |

## 6.3 Dict comprehensions

```python
squares = {x: x ** 2 for x in range(6)}

word = "hello"
freq = {char: word.count(char) for char in set(word)}

# Invert a dict (values must be unique)
original = {"a": 1, "b": 2}
inverted = {v: k for k, v in original.items()}
```

Syntax: `{key_expr: value_expr for item in iterable if condition}`

## 6.4 Set comprehensions

```python
unique_lengths = {len(word) for word in ["hi", "hello", "hey", "hi"]}
# {2, 3, 5}
```

Syntax: `{expression for item in iterable if condition}`

## 6.5 Generator expressions

> **Definition:** A **generator expression** uses parentheses and produces items lazily — one at a time, without building the full list in memory.

```python
squares_gen = (x ** 2 for x in range(1_000_000))

sum(x ** 2 for x in range(100))
max(len(w) for w in words)

# Consume once
list(squares_gen)
```

| Feature | List comp `[...]` | Generator `(...)` |
|---------|-------------------|-------------------|
| Memory | Stores all items | Lazy, one item |
| Reusable | Yes | Exhausted after one pass |
| Speed for small data | Similar | Similar |
| Large datasets | Can be expensive | Preferred |

See [Decorators & Generators](./ch11-decorators-generators.md) for generator functions.

## 6.6 Nested comprehensions

```python
flat = [x for row in matrix for x in row]

pairs = [(x, y) for x in range(3) for y in range(3)]
```

Read left-to-right like nested loops — outer `for` first.

## 6.7 Conditional expressions in comprehensions

```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
```

Do not confuse with filter `if` at the end:

```python
# filter
[x for x in range(10) if x % 2 == 0]

# ternary in expression
["even" if x % 2 == 0 else "odd" for x in range(10)]
```

## 6.8 When NOT to use comprehensions

Avoid comprehensions when:

- Logic exceeds one line or two
- Side effects are needed (I/O, mutations)
- Readability suffers

```python
# Prefer a loop for clarity
results = []
for user in users:
    if user.is_active:
        results.append(format_user(user))
```

## 6.9 Comprehensions vs map/filter

```python
nums = [1, 2, 3, 4, 5]

# comprehension
squares = [n ** 2 for n in nums if n % 2 == 1]

# map + filter
squares = list(map(lambda n: n ** 2, filter(lambda n: n % 2 == 1, nums)))
```

Comprehensions are usually clearer in Python codebases.

## 6.10 Walrus operator in comprehensions (3.8+)

```python
data = ["hello", "world", "hi"]
filtered = [last for word in data if (last := word[-1]) in "aeiou"]
```

Use sparingly — only when it avoids duplicate computation.

## Exercises

1. Build a list of squares for even numbers 0–20.
2. Create a dict mapping each word in a sentence to its length.
3. Flatten `[[1, 2], [3], [4, 5, 6]]` with a comprehension.
4. Use a generator expression to sum cubes of numbers 1–1000 without building a list.

## Summary

Comprehensions express collection-building in one line. Use list/dict/set comps for small transforms; generator expressions for large or streaming data.

## Next chapter

Continue to [OOP](./ch07-oop.md).
