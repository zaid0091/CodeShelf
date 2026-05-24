---
title: Control Flow
description: Conditionals, loops, break/continue, else clauses, and structural pattern matching
order: 3
tags: [python, control-flow, loops]
---

# Chapter 3: Control Flow

## 3.1 Conditional statements

> **Definition:** **Control flow** determines which statements run based on conditions or repetition.

```python
age = 20

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

| Construct | Purpose |
|-----------|---------|
| `if` | Run block when condition is truthy |
| `elif` | Additional conditions (else-if) |
| `else` | Fallback when all conditions fail |

### Ternary expression

```python
status = "adult" if age >= 18 else "minor"
```

### Chained comparisons

```python
x = 15
if 10 < x < 20:
    print("x is between 10 and 20")
```

## 3.2 Truthiness in conditions

```python
name = ""
if name:
    print("Hello")
else:
    print("Name required")  # runs — empty string is falsy

items = [1, 2, 3]
if items:
    print(f"{len(items)} items")
```

Avoid `if x == True` — use `if x:` or `if x is True` when you need exact boolean.

## 3.3 The `for` loop

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)
```

> **Definition:** `range(stop)` or `range(start, stop, step)` produces a lazy sequence of integers — memory-efficient for large ranges.

### `enumerate` and `zip`

```python
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)

names = ["Alice", "Bob"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

See [Functions](./ch04-functions.md) for more on `zip` and iteration.

## 3.4 The `while` loop

```python
count = 3
while count > 0:
    print(count)
    count -= 1
print("Done")
```

Use `while` when the number of iterations is unknown upfront.

## 3.5 `break`, `continue`, and `pass`

```python
for n in range(10):
    if n == 3:
        continue  # skip rest of iteration
    if n == 7:
        break     # exit loop entirely
    print(n)
```

| Statement | Effect |
|-----------|--------|
| `break` | Exit the innermost loop |
| `continue` | Skip to next iteration |
| `pass` | No-op placeholder |

```python
# pass — useful for empty stubs
class Todo:
    pass
```

## 3.6 `else` on loops

The `else` clause runs when the loop completes without `break`:

```python
for n in [2, 4, 6, 8]:
    if n % 2 != 0:
        print("Found odd")
        break
else:
    print("All even")  # runs if no break
```

## 3.7 Structural pattern matching (Python 3.10+)

```python
def handle_command(command):
    match command.split():
        case ["quit"]:
            return "Goodbye"
        case ["load", filename]:
            return f"Loading {filename}"
        case ["save", filename]:
            return f"Saving {filename}"
        case _:
            return "Unknown command"

handle_command("load data.csv")
```

| Pattern | Matches |
|---------|---------|
| `case x:` | Any value bound to `x` |
| `case [a, b]:` | Sequence of length 2 |
| `case {"key": val}:` | Dict with required key |
| `case _:` | Wildcard (default) |

## 3.8 Nested control flow

```python
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
```

Keep nesting shallow — extract inner logic into [functions](./ch04-functions.md) when it grows.

## 3.9 Common patterns

### Accumulator

```python
total = 0
for n in [1, 2, 3, 4, 5]:
    total += n
```

### Search

```python
target = "banana"
found = False
for item in fruits:
    if item == target:
        found = True
        break
```

List comprehensions (see [Comprehensions](./ch06-comprehensions.md)) often replace simple loops:

```python
squares = [x ** 2 for x in range(10)]
```

## 3.10 Infinite loops and safety

```python
while True:
    cmd = input("> ")
    if cmd == "quit":
        break
```

Always ensure a `break` or condition change to avoid hanging programs.

## Exercises

1. Write a program that prints FizzBuzz for 1–30 (`Fizz` if divisible by 3, `Buzz` by 5, `FizzBuzz` by both).
2. Use `enumerate` to print index and value for `["red", "green", "blue"]`.
3. Rewrite a `for` loop that sums even numbers using `continue`.
4. (3.10+) Use `match`/`case` to classify HTTP status codes: 2xx success, 4xx client error, 5xx server error.

## Summary

Conditionals branch logic; `for` and `while` repeat it. Master `break`/`continue`, loop `else`, and pattern matching for readable, idiomatic Python.

## Next chapter

Continue to [Functions](./ch04-functions.md).
