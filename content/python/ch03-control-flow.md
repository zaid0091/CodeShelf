---
title: Control Flow
description: if/elif/else, for and while loops, break, continue, range, enumerate, zip, and match/case
order: 3
tags: [python, control-flow, loops]
---

# Chapter 3: Control Flow

> **Control flow decides which code runs and how often. You will master conditionals, loops, and Pythonic iteration patterns used in every script.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [What Is Control Flow?](#what-is-control-flow)
2. [Boolean Conditions Recap](#boolean-conditions-recap)
3. [The if Statement](#the-if-statement)
4. [elif and else](#elif-and-else)
5. [Ternary Conditional Expressions](#ternary-conditional-expressions)
6. [Chained Comparisons](#chained-comparisons)
7. [Truthiness in Conditions](#truthiness-in-conditions)
8. [The for Loop](#the-for-loop)
9. [The range() Function](#the-range-function)
10. [enumerate() and zip()](#enumerate-and-zip)
11. [The while Loop](#the-while-loop)
12. [break, continue, and pass](#break-continue-and-pass)
13. [else on Loops](#else-on-loops)
14. [Nested Control Flow](#nested-control-flow)
15. [Structural Pattern Matching](#structural-pattern-matching)
16. [Common Loop Patterns](#common-loop-patterns)
17. [Infinite Loops and Safety](#infinite-loops-and-safety)
18. [Best Practices](#best-practices)
19. [Common Mistakes](#common-mistakes)
20. [Interview Points](#interview-points)
21. [Exercises](#exercises)
22. [Chapter Summary](#chapter-summary)

---

## What Is Control Flow?

> **Definition:** **Control flow** decides which lines run, how often, and in what order.

### Why it matters

Without branches and loops, programs cannot respond to input or process collections.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
score = 85
print('pass' if score >= 60 else 'fail')
```


---

## Boolean Conditions Recap

> **Definition:** Conditions use `and`, `or`, `not` and evaluate to `True` or `False`.

### Why it matters

Short-circuiting skips the right side when the result is already known.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
name = ''
if name and name[0] == 'A':
    print('starts with A')
```


---

## The if Statement

> **Definition:** `if condition:` runs a block when the condition is truthy.

### Why it matters

The building block of decision-making.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
age = 20
if age >= 18:
    print('adult')
```


---

## elif and else

> **Definition:** `elif` checks another condition; `else` runs when all prior conditions were false.

### Why it matters

Order from most specific to most general.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
x = 15
if x < 10:
    print('small')
elif x < 20:
    print('medium')
else:
    print('large')
```


---

## Ternary Conditional Expressions

> **Definition:** `value_if_true if condition else value_if_false` chooses between two expressions.

### Why it matters

Use for simple assignments, not multi-line logic.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
status = 'ok' if errors == 0 else 'fail'
```


---

## Chained Comparisons

> **Definition:** `a < b < c` is equivalent to `a < b and b < c`.

### Why it matters

Readable range and bound checks.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
n = 15
print(10 < n < 20)
```


---

## Truthiness in Conditions

> **Definition:** Objects convert to `bool` in `if` — empty collections and zero are falsy.

### Why it matters

Write `if items:` instead of `if len(items) > 0`.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
if []:
    print('never')
if [0]:
    print('runs')
```


---

## The for Loop

> **Definition:** `for item in iterable:` visits each element.

### Why it matters

Preferred when iterating sequences.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
for ch in 'abc':
    print(ch)
```


---

## The range() Function

> **Definition:** `range(n)` or `range(start, stop, step)` yields integers lazily.

### Why it matters

Avoid building huge lists with `list(range(...))` unless needed.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
print(list(range(2, 10, 2)))
```


---

## enumerate() and zip()

> **Definition:** `enumerate` adds indexes; `zip` pairs parallel iterables.

### Why it matters

Cleaner than manual index arithmetic.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
for i, w in enumerate(['a','b']):
    print(i, w)
for a, b in zip([1,2], ['x','y']):
    print(a, b)
```


---

## The while Loop

> **Definition:** Repeats while the condition stays true.

### Why it matters

Update loop variables inside the body to avoid infinite loops.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
n = 3
while n:
    print(n)
    n -= 1
```


---

## break, continue, and pass

> **Definition:** `break` exits the loop; `continue` skips to the next item; `pass` is a no-op placeholder.

### Why it matters

Search loops often `break` when a match is found.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
for n in range(10):
    if n == 5:
        break
    print(n)
```


---

## else on Loops

> **Definition:** A loop `else` runs only if the loop did not `break`.

### Why it matters

Useful for 'not found' patterns.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
for x in [1,2,3]:
    if x == 9:
        break
else:
    print('not found')
```


---

## Nested Control Flow

> **Definition:** Loops and `if` statements can nest inside each other.

### Why it matters

Extract functions when nesting exceeds two levels.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
for row in matrix:
    for val in row:
        if val < 0:
            print('negative', val)
```


---

## Structural Pattern Matching

> **Definition:** `match subject:` / `case pattern:` (Python 3.10+) matches shapes and values.

### Why it matters

Replaces some long `if/elif` chains.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def label(x):
    match x:
        case 0: return 'zero'
        case str(s): return s.upper()
        case _: return 'other'
```


---

## Common Loop Patterns

> **Definition:** Accumulate totals, search, filter, and transform data in loops.

### Why it matters

Know these before reaching for heavy libraries.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
total = sum(x for x in [1,2,3])
print(total)
```


---

## Infinite Loops and Safety

> **Definition:** A `while True` loop needs a clear `break` or exit condition.

### Why it matters

Add timeouts or counters in production systems.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
attempts = 0
while attempts < 3:
    attempts += 1
    print('try', attempts)
```


---

## Best Practices

### Guidelines

- Prefer `for` over `while` when iterating collections
- Avoid deep nesting — extract functions


---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Infinite while | Forgot to update loop variable | Check exit condition |


---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: `if` vs `elif` vs `else`?**

Mutually exclusive chain — first true branch runs; `else` catches none matched.

---

> **📌 Interview Point 2: What is truthiness in `if`?**

Condition evaluated via `bool()` — avoid `if x == True`.

---

> **📌 Interview Point 3: `for` vs `while`?**

`for` iterates a known iterable; `while` until condition false — watch infinite loops.

---

> **📌 Interview Point 4: What does `range` return?**

Lazy **range object** — not a list until you `list(range(n))`.

---

> **📌 Interview Point 5: What is `enumerate`?**

Yields `(index, item)` pairs — avoid manual `i += 1` counters.

---

> **📌 Interview Point 6: What is `zip`?**

Pairs elements from iterables; stops at shortest — use `itertools.zip_longest` for padding.

---

> **📌 Interview Point 7: What is `break` / `continue` / `pass`?**

`break` exits loop; `continue` skips to next iteration; `pass` is no-op placeholder.

---

> **📌 Interview Point 8: What is `for-else`?**

`else` on loop runs if loop **not** broken — useful for search patterns.

---

> **📌 Interview Point 9: What is structural pattern matching?**

Python 3.10+ `match/case` — cleaner than long `if/elif` chains for types/values.

---

> **📌 Interview Point 10: Chained comparisons?**

`a < b < c` equivalent to `a < b and b < c` — idiomatic Python.

---

> **📌 Interview Point 11: Infinite loop prevention?**

Ensure loop variable changes; use timeouts in production; prefer `for` when possible.

---

> **📌 Interview Point 12: What is ternary expression?**

`x if cond else y` — expression, not statement.

---

> **📌 Interview Point 13: How to iterate dict?**

`for k in d`, `d.items()`, `d.values()` — never mutate dict size while iterating keys without care.

---

> **📌 Interview Point 14: What is `pass` used for?**

Stub empty blocks syntactically required by Python.

---

> **📌 Interview Point 15: Difference `while True` vs `for`?**

Event loops and unknown-length input use `while`; collections use `for`.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Grade classifier ⭐

**Task:** Print letter grade for score 0-100 using if/elif.

<details>
<summary>💡 Hint (click to reveal)</summary>

Branches: A>=90, B>=80, etc.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
score = 87
if score >= 90: print("A")
elif score >= 80: print("B")
else: print("C or below")
```

</details>

---

### Exercise 2: FizzBuzz one line loop ⭐

**Task:** Print FizzBuzz for 1..20.

<details>
<summary>💡 Hint (click to reveal)</summary>

Modulo 3 and 5.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
for i in range(1, 21):
    f, b = i % 3 == 0, i % 5 == 0
    print("FizzBuzz" if f and b else "Fizz" if f else "Buzz" if b else i)
```

</details>

---

### Exercise 3: Sum with for ⭐⭐

**Task:** Sum list without built-in sum.

<details>
<summary>💡 Hint (click to reveal)</summary>

Accumulator variable.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
nums = [1, 2, 3, 4]
total = 0
for n in nums:
    total += n
print(total)
```

</details>

---

### Exercise 4: enumerate menu ⭐⭐

**Task:** Print numbered list of items.

<details>
<summary>💡 Hint (click to reveal)</summary>

for i, item in enumerate(items, 1).

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
items = ["tea", "coffee", "water"]
for i, item in enumerate(items, 1):
    print(f"{i}. {item}")
```

</details>

---

### Exercise 5: Password attempt loop ⭐⭐

**Task:** while tries < 3; break on correct password.

<details>
<summary>💡 Hint (click to reveal)</summary>

Counter or decrement tries.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
secret = "python"
tries = 0
while tries < 3:
    if input("password: ") == secret:
        print("welcome")
        break
    tries += 1
else:
    print("locked")
```

</details>

---

### Exercise 6: Prime checker ⭐⭐⭐

**Task:** Return whether n is prime.

<details>
<summary>💡 Hint (click to reveal)</summary>

Test divisors 2..sqrt(n).

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
import math
def is_prime(n):
    if n < 2: return False
    for d in range(2, int(math.isqrt(n)) + 1):
        if n % d == 0: return False
    return True
print(is_prime(29))
```

</details>


## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **if/elif/else** | Branch on boolean conditions |
| **for** | Iterate any iterable |
| **while** | Repeat until condition false |
| **range** | Lazy sequence of numbers |
| **enumerate/zip** | Index pairs and parallel iteration |
| **match/case** | Pattern matching Python 3.10+ |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**⬅️ [Previous: Data Types](./ch02-data-types.md)**

**➡️ [Next: Functions →](./ch04-functions.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
