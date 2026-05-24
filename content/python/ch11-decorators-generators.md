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

> **Definition:** This section explains **Functions as First-Class Objects** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **functions as first-class objects** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Functions as First-Class Objects
x = chapter_11_demo = True
print("Functions as First-Class Objects", x)
```

### Hands-on: Functions as First-Class Objects

1. State **Functions as First-Class Objects** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Iterables vs Iterators

> **Definition:** This section explains **Iterables vs Iterators** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **iterables vs iterators** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Iterables vs Iterators
x = chapter_11_demo = True
print("Iterables vs Iterators", x)
```

### Hands-on: Iterables vs Iterators

1. State **Iterables vs Iterators** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## The Iterator Protocol

> **Definition:** This section explains **The Iterator Protocol** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **the iterator protocol** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: The Iterator Protocol
x = chapter_11_demo = True
print("The Iterator Protocol", x)
```

### Hands-on: The Iterator Protocol

1. State **The Iterator Protocol** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Generator Functions and yield

> **Definition:** This section explains **Generator Functions and yield** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **generator functions and yield** in scripts, APIs, and data tasks.

### Example

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for x in count_up_to(3):
    print(x)
```

### Hands-on: Generator Functions and yield

1. State **Generator Functions and yield** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Generator Expressions

> **Definition:** This section explains **Generator Expressions** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **generator expressions** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Generator Expressions
x = chapter_11_demo = True
print("Generator Expressions", x)
```

### Hands-on: Generator Expressions

1. State **Generator Expressions** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## yield from Delegation

> **Definition:** This section explains **yield from Delegation** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **yield from delegation** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: yield from Delegation
x = chapter_11_demo = True
print("yield from Delegation", x)
```

### Hands-on: yield from Delegation

1. State **yield from Delegation** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Sending Values to Generators

> **Definition:** This section explains **Sending Values to Generators** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **sending values to generators** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Sending Values to Generators
x = chapter_11_demo = True
print("Sending Values to Generators", x)
```

### Hands-on: Sending Values to Generators

1. State **Sending Values to Generators** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## When to Use Generators

> **Definition:** This section explains **When to Use Generators** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **when to use generators** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: When to Use Generators
x = chapter_11_demo = True
print("When to Use Generators", x)
```

### Hands-on: When to Use Generators

1. State **When to Use Generators** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## What Are Decorators?

> **Definition:** This section explains **What Are Decorators?** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **what are decorators?** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: What Are Decorators?
x = chapter_11_demo = True
print("What Are Decorators?", x)
```

### Hands-on: What Are Decorators?

1. State **What Are Decorators?** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Writing Your First Decorator

> **Definition:** This section explains **Writing Your First Decorator** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **writing your first decorator** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Writing Your First Decorator
x = chapter_11_demo = True
print("Writing Your First Decorator", x)
```

### Hands-on: Writing Your First Decorator

1. State **Writing Your First Decorator** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Decorators with Arguments

> **Definition:** This section explains **Decorators with Arguments** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **decorators with arguments** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Decorators with Arguments
x = chapter_11_demo = True
print("Decorators with Arguments", x)
```

### Hands-on: Decorators with Arguments

1. State **Decorators with Arguments** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## functools.wraps

> **Definition:** This section explains **functools.wraps** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **functools.wraps** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: functools.wraps
x = chapter_11_demo = True
print("functools.wraps", x)
```

### Hands-on: functools.wraps

1. State **functools.wraps** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Stacking Decorators

> **Definition:** This section explains **Stacking Decorators** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **stacking decorators** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Stacking Decorators
x = chapter_11_demo = True
print("Stacking Decorators", x)
```

### Hands-on: Stacking Decorators

1. State **Stacking Decorators** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Built-in Decorators

> **Definition:** This section explains **Built-in Decorators** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **built-in decorators** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Built-in Decorators
x = chapter_11_demo = True
print("Built-in Decorators", x)
```

### Hands-on: Built-in Decorators

1. State **Built-in Decorators** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Class Decorators

> **Definition:** This section explains **Class Decorators** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **class decorators** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Class Decorators
x = chapter_11_demo = True
print("Class Decorators", x)
```

### Hands-on: Class Decorators

1. State **Class Decorators** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## contextlib.contextmanager

> **Definition:** This section explains **contextlib.contextmanager** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **contextlib.contextmanager** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: contextlib.contextmanager
x = chapter_11_demo = True
print("contextlib.contextmanager", x)
```

### Hands-on: contextlib.contextmanager

1. State **contextlib.contextmanager** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## The itertools Module

> **Definition:** This section explains **The itertools Module** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **the itertools module** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: The itertools Module
x = chapter_11_demo = True
print("The itertools Module", x)
```

### Hands-on: The itertools Module

1. State **The itertools Module** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Best Practices

> **Definition:** This section explains **Best Practices** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **best practices** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Best Practices
x = chapter_11_demo = True
print("Best Practices", x)
```

### Hands-on: Best Practices

1. State **Best Practices** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Common Mistakes

> **Definition:** This section explains **Common Mistakes** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **common mistakes** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Common Mistakes
x = chapter_11_demo = True
print("Common Mistakes", x)
```

### Hands-on: Common Mistakes

1. State **Common Mistakes** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## functools Beyond Decorators

> **Definition:** This section explains **functools Beyond Decorators** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **functools beyond decorators** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: functools Beyond Decorators
x = chapter_11_demo = True
print("functools Beyond Decorators", x)
```

### Hands-on: functools Beyond Decorators

1. State **functools Beyond Decorators** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## More itertools Recipes

> **Definition:** This section explains **More itertools Recipes** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **more itertools recipes** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: More itertools Recipes
x = chapter_11_demo = True
print("More itertools Recipes", x)
```

### Hands-on: More itertools Recipes

1. State **More itertools Recipes** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



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
