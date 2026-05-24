---
title: Data Structures
description: Lists, tuples, dictionaries, sets, slicing, copying, sorting, and collections
order: 5
tags: [python, lists, dicts, sets]
---

# Chapter 5: Data Structures

> **Programs work with collections. Choose the right structure — list, tuple, dict, or set — for clarity and performance.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [What Is a Data Structure?](#what-is-a-data-structure)
2. [Choosing the Right Structure](#choosing-the-right-structure)
3. [Lists](#lists)
4. [List Methods Reference](#list-methods-reference)
5. [Slicing Sequences](#slicing-sequences)
6. [Tuples](#tuples)
7. [Dictionaries](#dictionaries)
8. [Dictionary Methods and Patterns](#dictionary-methods-and-patterns)
9. [Sets](#sets)
10. [Set Operations](#set-operations)
11. [Nested Structures](#nested-structures)
12. [Copying: Shallow vs Deep](#copying-shallow-vs-deep)
13. [Sorting Data](#sorting-data)
14. [The collections Module](#the-collections-module)
15. [Best Practices](#best-practices)
16. [Common Mistakes](#common-mistakes)
17. [Interview Points](#interview-points)
18. [Exercises](#exercises)
19. [Chapter Summary](#chapter-summary)

---

## What Is a Data Structure?

> **Definition:** A **data structure** is how you organize multiple values in memory (list, dict, set, tuple).

### Why it matters

The right structure makes code simpler and faster.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
users = [{'id':1,'name':'Ada'}]
print(users[0]['name'])
```


---

## Choosing the Right Structure

> **Definition:** Use **list** for ordered sequences, **dict** for lookups by key, **set** for uniqueness, **tuple** for fixed records.

### Why it matters

Pick based on operations you need most.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
tags = {'python', 'web'}
order = ['first', 'second']
lookup = {'ada': 98}
```


---

## Lists

> **Definition:** Ordered, mutable sequences in `[...]`.

### Why it matters

Workhorse collection type.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
nums = [1,2,3]
nums.append(4)
print(nums[0], nums[-1])
```


---

## List Methods Reference

> **Definition:** Common methods: `.append`, `.extend`, `.insert`, `.pop`, `.sort`, `.reverse`.

### Why it matters

Most list methods mutate in place.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
items = [3,1,2]
items.sort()
print(items)
```


---

## Slicing Sequences

> **Definition:** `seq[start:stop:step]` extracts sub-sequences; stop is exclusive.

### Why it matters

Works on lists, tuples, and strings.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
a = [0,1,2,3,4]
print(a[1:4], a[::-1])
```


---

## Tuples

> **Definition:** Ordered, **immutable** sequences in `(...)`.

### Why it matters

Records, dict keys, return multiple values.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
point = (10, 20)
x, y = point
```


---

## Dictionaries

> **Definition:** Hash map: unique keys → values.

### Why it matters

Fast lookup by key.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
user = {'name':'Sam','role':'admin'}
print(user.get('phone', 'n/a'))
```


---

## Dictionary Methods and Patterns

> **Definition:** Use `.get`, `.items`, `.setdefault`, and `.update` for safe, clear dict code.

### Why it matters

Iterate with `.items()` when you need both key and value.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
counts = {}
for word in ['a','b','a']:
    counts[word] = counts.get(word, 0) + 1
```


---

## Sets

> **Definition:** Unordered collection of **unique** hashable items.

### Why it matters

Membership and deduplication.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
tags = {'py','web','py'}
print(tags, len(tags))
```


---

## Set Operations

> **Definition:** Union `|`, intersection `&`, difference `-`.

### Why it matters

Compare categories without nested loops.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
a, b = {1,2}, {2,3}
print(a & b, a | b)
```


---

## Nested Structures

> **Definition:** Lists of dicts, dicts of lists — model real JSON-like data.

### Why it matters

Access with chained `[][]` carefully.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
data = {'users':[{'id':1}]}
print(data['users'][0]['id'])
```


---

## Copying: Shallow vs Deep

> **Definition:** Assignment copies reference. `copy.copy` shallow; `copy.deepcopy` recursive.

### Why it matters

Nested mutations need deep copy.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import copy
a = [[1]]
b = copy.deepcopy(a)
a[0][0] = 9
print(b)
```


---

## Sorting Data

> **Definition:** `sorted(iterable)` returns new list; `.sort()` mutates list in place.

### Why it matters

Pass `key=` for custom order.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
print(sorted(['banana','apple'], key=len))
```


---

## The collections Module

> **Definition:** Specialized containers: `Counter`, `defaultdict`, `deque`.

### Why it matters

Stdlib batteries for common patterns.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
from collections import Counter
print(Counter('abracadabra').most_common(2))
```


---

## Best Practices

### Guidelines

- Use `.get()` on dicts for optional keys
- Choose tuple for fixed records


---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Shallow copy nested list | Shared inner objects | Use `deepcopy` |


---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: List vs tuple?**

Both ordered sequences; list **mutable**, tuple **immutable**. Tuples as records, dict keys.

---

> **📌 Interview Point 2: Dict lookup complexity?**

Average **O(1)** hash table; worst **O(n)** with collisions.

---

> **📌 Interview Point 3: Shallow vs deep copy?**

Shallow: new container, shared inner objects. Deep: recursive duplicate via `copy.deepcopy`.

---

> **📌 Interview Point 4: Merge dicts?**

`{**a, **b}`, `a | b` (3.9+), `a.update(b)`.

---

> **📌 Interview Point 5: Dedupe preserving order?**

`list(dict.fromkeys(seq))` — not `set()` if order matters.

---

> **📌 Interview Point 6: Set vs list membership?**

Set **O(1)** average; list **O(n)**.

---

> **📌 Interview Point 7: What is hashable?**

Stable `__hash__` and `__eq__` — immutables like str, int, tuple of hashables.

---

> **📌 Interview Point 8: `pop` vs `remove` on list?**

`pop(i)` by index returns item; `remove(x)` removes first match by value.

---

> **📌 Interview Point 9: `sort` vs `sorted`?**

`list.sort()` in-place; `sorted(iterable)` returns new list.

---

> **📌 Interview Point 10: What does `zip` produce?**

Iterator of tuples — pairs until shortest iterable exhausted.

---

> **📌 Interview Point 11: Why not list as dict key?**

Lists mutable → unhashable → `TypeError`.

---

> **📌 Interview Point 12: defaultdict use case?**

Auto-create missing keys — counting, grouping without `KeyError`.

---

> **📌 Interview Point 13: Counter vs manual count?**

`collections.Counter` optimized, rich API (`most_common`).

---

> **📌 Interview Point 14: deque vs list for queues?**

`deque` O(1) append/pop both ends; list pop(0) is O(n).

---

> **📌 Interview Point 15: namedtuple vs dict?**

namedtuple: fixed fields, attribute access, memory efficient records.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Word counter ⭐

**Task:** Count words with `Counter`.

<details>
<summary>💡 Hint (click to reveal)</summary>

`from collections import Counter` then `Counter(words)`.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
from collections import Counter
words = ["apple", "banana", "apple", "cherry"]
print(Counter(words))
```

</details>

---

### Exercise 2: Merge dicts ⭐

**Task:** Merge `{"a":1}` and `{"b":2,"a":10}`.

<details>
<summary>💡 Hint (click to reveal)</summary>

Spread or `|` operator; later keys win.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
d1, d2 = {"a": 1}, {"b": 2, "a": 10}
print({**d1, **d2})  # {'a': 10, 'b': 2}
```

</details>

---

### Exercise 3: Ordered dedupe ⭐⭐

**Task:** Dedupe `[3,1,2,3,2,1]` preserving order.

<details>
<summary>💡 Hint (click to reveal)</summary>

`dict.fromkeys` preserves insertion order.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
items = [3, 1, 2, 3, 2, 1]
print(list(dict.fromkeys(items)))
```

</details>

---

### Exercise 4: Nested file tree ⭐⭐

**Task:** Dict of folders; add file to nested path.

<details>
<summary>💡 Hint (click to reveal)</summary>

Build nested dicts; use `.setdefault` chain.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
tree = {"docs": {"work": []}}
tree["docs"]["work"].append("report.pdf")
print(tree)
```

</details>

---

### Exercise 5: Set operations on IDs ⭐⭐

**Task:** Given sets A and B, print intersection, A-only, union.

<details>
<summary>💡 Hint (click to reveal)</summary>

Use `&`, `-`, `|`.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
a, b = {1, 2, 3}, {3, 4, 5}
print("both:", a & b)
print("only A:", a - b)
print("either:", a | b)
```

</details>

---

### Exercise 6: Sort people ⭐⭐⭐

**Task:** Sort by age desc then name asc.

<details>
<summary>💡 Hint (click to reveal)</summary>

Tuple key with negatives or `key` twice via sorted twice stable.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
people = [("Alice", 30), ("Bob", 25), ("Carol", 30)]
people.sort(key=lambda p: (-p[1], p[0]))
print(people)
```

</details>

---

### Exercise 7: Shallow vs deep demo ⭐⭐⭐

**Task:** Show inner list shared in shallow copy only.

<details>
<summary>💡 Hint (click to reveal)</summary>

Mutate inner after copy; compare `deepcopy`.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
import copy
orig = [[1], [2]]
shallow = orig.copy()
deep = copy.deepcopy(orig)
orig[0].append(99)
print("shallow inner:", shallow[0])
print("deep inner:", deep[0])
```

</details>

---

### Exercise 8: Inventory with defaultdict ⭐⭐⭐

**Task:** Group items by category using `defaultdict(list)`.

<details>
<summary>💡 Hint (click to reveal)</summary>

Append to `dd[category]` without KeyError.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
from collections import defaultdict
inv = [("fruit", "apple"), ("fruit", "banana"), ("dairy", "milk")]
by_cat = defaultdict(list)
for cat, item in inv:
    by_cat[cat].append(item)
print(dict(by_cat))
```

</details>


## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **list** | Ordered mutable sequence |
| **tuple** | Ordered immutable record |
| **dict** | Key-value hash map |
| **set** | Unique unordered items |
| **copy** | Shallow vs deep for nested data |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**⬅️ [Previous: Functions](./ch04-functions.md)**

**➡️ [Next: Comprehensions →](./ch06-comprehensions.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
