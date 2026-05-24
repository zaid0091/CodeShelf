---
title: Comprehensions
description: List, dict, and set comprehensions, generator expressions, and when to use loops
order: 6
tags: [python, comprehensions, generators]
---

# Chapter 6: Comprehensions

> **Comprehensions express transforms and filters in one line — idiomatic Python for readable data processing.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [What Are Comprehensions?](#what-are-comprehensions)
2. [Why Comprehensions Exist](#why-comprehensions-exist)
3. [List Comprehensions](#list-comprehensions)
4. [Filtering with if](#filtering-with-if)
5. [Conditional Expressions in Comprehensions](#conditional-expressions-in-comprehensions)
6. [Dict Comprehensions](#dict-comprehensions)
7. [Set Comprehensions](#set-comprehensions)
8. [Generator Expressions](#generator-expressions)
9. [Nested Comprehensions](#nested-comprehensions)
10. [Comprehensions vs Loops](#comprehensions-vs-loops)
11. [Comprehensions vs map and filter](#comprehensions-vs-map-and-filter)
12. [Walrus Operator in Comprehensions](#walrus-operator-in-comprehensions)
13. [Real-World Examples](#real-world-examples)
14. [Performance and Memory](#performance-and-memory)
15. [Best Practices](#best-practices)
16. [Common Mistakes](#common-mistakes)
17. [Debugging Comprehensions](#debugging-comprehensions)
18. [Reading Comprehensions Aloud](#reading-comprehensions-aloud)
19. [Interview Points](#interview-points)
20. [Exercises](#exercises)
21. [Chapter Summary](#chapter-summary)

---

## What Are Comprehensions?

> **Definition:** Comprehensions build collections from iterables in one expression.

### Why it matters

More readable than manual append loops for transforms.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
squares = [n*n for n in range(5)]
print(squares)
```


---

## Why Comprehensions Exist

> **Definition:** They express map/filter logic declaratively.

### Why it matters

Idiomatic Python — reviewers expect them.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
evens = [n for n in range(10) if n % 2 == 0]
```


---

## List Comprehensions

> **Definition:** `[expr for item in iterable if cond]`.

### Why it matters

Filter with trailing `if`; ternary before `for`.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
names = ['ada','bob']
upper = [n.upper() for n in names]
```


---

## Filtering with if

> **Definition:** Trailing `if` keeps items matching a condition.

### Why it matters

Equivalent to filter + list.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
nums = [1,2,3,4,5]
print([n for n in nums if n % 2])
```


---

## Conditional Expressions in Comprehensions

> **Definition:** `[a if cond else b for x in xs]` chooses per item.

### Why it matters

Do not confuse with filter `if`.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
labels = ['even' if n%2==0 else 'odd' for n in range(4)]
```


---

## Dict Comprehensions

> **Definition:** `{k: v for ...}` builds dicts.

### Why it matters

Invert or transform mappings.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
nums = [1,2,3]
print({n: n*n for n in nums})
```


---

## Set Comprehensions

> **Definition:** `{expr for ...}` — unique results.

### Why it matters

Deduplicate while transforming.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
print({len(w) for w in ['hi','hey','yo']})
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

## Nested Comprehensions

> **Definition:** Loops read left-to-right like nested fors.

### Why it matters

Keep depth ≤ 2 for readability.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
matrix = [[1,2],[3,4]]
flat = [x for row in matrix for x in row]
```


---

## Comprehensions vs Loops

> **Definition:** Use comprehension for simple transform/filter; loop for side effects.

### Why it matters

If you need `break`, use a loop.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# side effect -> loop
for u in users:
    send_email(u)
```


---

## Comprehensions vs map and filter

> **Definition:** `map`/`filter` return iterators; comprehensions are more Pythonic.

### Why it matters

Still useful with existing functions.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
print(list(map(str, [1,2,3])))
```


---

## Walrus Operator in Comprehensions

> **Definition:** `:=` assigns inside an expression (3.8+).

### Why it matters

Avoid repeating expensive calls.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import random
nums = [random.random() for _ in range(5)]
filtered = [y for x in nums if (y := round(x,2)) > 0.5]
```


---

## Real-World Examples

> **Definition:** Parse logs, normalize CSV rows, build lookup tables.

### Why it matters

Comprehensions shine in ETL scripts.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
rows = ['1,Ada','2,Bob']
users = {int(r.split(',')[0]): r.split(',')[1] for r in rows}
```


---

## Performance and Memory

> **Definition:** List comps build full list; generators stream.

### Why it matters

Profile before micro-optimizing.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import sys
print(sys.getsizeof([n for n in range(1000)]))
```


---

## Best Practices

### Guidelines

- Prefer generator expressions for large streams
- Do not nest more than two levels


---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Confusing filter if vs ternary | Wrong output | Filter after `for`; ternary before `for` |


---

## Debugging Comprehensions

> **Definition:** Expand to a loop temporarily to print intermediate values.

### Why it matters

Read inside-out: result, condition, source.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# debug version
out = []
for n in range(5):
    if n % 2: out.append(n)
print(out)
```


---

## Reading Comprehensions Aloud

> **Definition:** Say: 'a list of EXPR for ITEM in ITER if COND'.

### Why it matters

Practice decoding others' code.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
result = [c.upper() for c in 'abc' if c != 'b']
```


---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: What is a list comprehension?**

`[expr for x in iterable if cond]` — compact map+filter.

---

> **📌 Interview Point 2: Filter `if` vs ternary `if`?**

Filter at **end** filters items; ternary **before for** chooses between expressions.

---

> **📌 Interview Point 3: List comp vs generator expression?**

`[]` builds list in memory; `()` lazy yields one at a time.

---

> **📌 Interview Point 4: When avoid comprehensions?**

Side effects, deep nesting, unreadable logic — use `for` loop.

---

> **📌 Interview Point 5: Dict/set comprehension syntax?**

`{k: v for ...}` and `{x for ...}` respectively.

---

> **📌 Interview Point 6: Nested comprehension readability?**

Max two levels; else use loops or helper functions.

---

> **📌 Interview Point 7: Comprehension vs map/filter?**

Comprehensions more Pythonic; `map`/`filter` return iterators, need `list()`.

---

> **📌 Interview Point 8: Walrus in comprehension?**

`:=` can assign in expression (3.8+) — use sparingly for clarity.

---

> **📌 Interview Point 9: Memory of large comps?**

Generator expression for streaming; list comp materializes all.

---

> **📌 Interview Point 10: Is comprehension faster?**

Often faster than append loop — optimized bytecode — but readability first.

---

> **📌 Interview Point 11: Set comp uniqueness?**

Automatically deduplicates by set semantics.

---

> **📌 Interview Point 12: Can comprehension have else?**

Ternary only: `[a if c else b for x in it]` — not `else` after `for` like loop.

---

> **📌 Interview Point 13: Generator one-shot?**

Consuming generator exhausts it — iterate once or recreate.

---

> **📌 Interview Point 14: yield from purpose?**

Delegates to sub-generator — flatten nested iteration.

---

> **📌 Interview Point 15: itertools role?**

Iterator algebra — chain, product, combinations beyond basic comps.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Even squares ⭐

**Task:** List of squares for even 0..18.

<details>
<summary>💡 Hint (click to reveal)</summary>

[x**2 for x in range(20) if x%2==0].

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
print([x**2 for x in range(20) if x % 2 == 0])
```

</details>

---

### Exercise 2: Uppercase names ⭐

**Task:** Uppercase list of names via comp.

<details>
<summary>💡 Hint (click to reveal)</summary>

[n.upper() for n in names].

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
names = ["alice", "bob"]
print([n.upper() for n in names])
```

</details>

---

### Exercise 3: Dict from pairs ⭐⭐

**Task:** Build dict from two lists with comp.

<details>
<summary>💡 Hint (click to reveal)</summary>

zip in comp.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
keys, vals = ["a", "b"], [1, 2]
print({k: v for k, v in zip(keys, vals)})
```

</details>

---

### Exercise 4: Set of lengths ⭐⭐

**Task:** Unique word lengths from sentence.

<details>
<summary>💡 Hint (click to reveal)</summary>

{len(w) for w in words}.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
words = "the quick brown fox".split()
print({len(w) for w in words})
```

</details>

---

### Exercise 5: Generator sum of squares ⭐⭐⭐

**Task:** Sum squares 1..1_000_000 with gen exp.

<details>
<summary>💡 Hint (click to reveal)</summary>

sum(x*x for x in range(...)).

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
print(sum(x*x for x in range(1, 1_000_001)))
```

</details>

---

### Exercise 6: Flatten matrix ⭐⭐⭐

**Task:** Nested comp flatten 2D list.

<details>
<summary>💡 Hint (click to reveal)</summary>

[x for row in m for x in row].

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
m = [[1,2],[3,4]]
print([x for row in m for x in row])
```

</details>


## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **List comp** | [expr for x in it if cond] |
| **Filter if** | Trailing if filters items |
| **Ternary if** | Before for chooses expression |
| **Generators** | Lazy () for large data |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**⬅️ [Previous: Data Structures](./ch05-data-structures.md)**

**➡️ [Next: Object-Oriented Programming →](./ch07-oop.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
