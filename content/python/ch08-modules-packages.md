---
title: Modules and Packages
description: import styles, __name__, packages, stdlib tour, and project layout
order: 8
tags: [python, modules, packages]
---

# Chapter 8: Modules and Packages

> **Modules split code across files. Packages organize modules into importable trees — essential for real projects.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [Why Modules Matter](#why-modules-matter)
2. [What Is a Module?](#what-is-a-module)
3. [Your First Import](#your-first-import)
4. [Import Styles Compared](#import-styles-compared)
5. [The import Statement Deep Dive](#the-import-statement-deep-dive)
6. [Aliasing and Selective Imports](#aliasing-and-selective-imports)
7. [When to Avoid import *](#when-to-avoid-import)
8. [__name__ and the Script Entry Point](#name-and-the-script-entry-point)
9. [How Python Finds Modules](#how-python-finds-modules)
10. [What Is a Package?](#what-is-a-package)
11. [Package Layout and __init__.py](#package-layout-and-init-py)
12. [Relative vs Absolute Imports](#relative-vs-absolute-imports)
13. [Namespace Packages](#namespace-packages)
14. [The __all__ Public API](#the-all-public-api)
15. [Circular Imports](#circular-imports)
16. [Standard Library Tour](#standard-library-tour)
17. [Third-Party Packages and pip](#third-party-packages-and-pip)
18. [Organizing a Real Project](#organizing-a-real-project)
19. [Best Practices](#best-practices)
20. [Common Mistakes](#common-mistakes)
21. [Interview Points](#interview-points)
22. [Exercises](#exercises)
23. [Chapter Summary](#chapter-summary)

---

## Why Modules Matter

> **Definition:** This section explains **Why Modules Matter** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **why modules matter** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Why Modules Matter
x = chapter_8_demo = True
print("Why Modules Matter", x)
```

### Hands-on: Why Modules Matter

1. State **Why Modules Matter** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## What Is a Module?

> **Definition:** This section explains **What Is a Module?** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **what is a module?** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: What Is a Module?
x = chapter_8_demo = True
print("What Is a Module?", x)
```

### Hands-on: What Is a Module?

1. State **What Is a Module?** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Your First Import

> **Definition:** This section explains **Your First Import** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **your first import** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Your First Import
x = chapter_8_demo = True
print("Your First Import", x)
```

### Hands-on: Your First Import

1. State **Your First Import** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Import Styles Compared

> **Definition:** This section explains **Import Styles Compared** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **import styles compared** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Import Styles Compared
x = chapter_8_demo = True
print("Import Styles Compared", x)
```

### Hands-on: Import Styles Compared

1. State **Import Styles Compared** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## The import Statement Deep Dive

> **Definition:** This section explains **The import Statement Deep Dive** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **the import statement deep dive** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: The import Statement Deep Dive
x = chapter_8_demo = True
print("The import Statement Deep Dive", x)
```

### Hands-on: The import Statement Deep Dive

1. State **The import Statement Deep Dive** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Aliasing and Selective Imports

> **Definition:** This section explains **Aliasing and Selective Imports** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **aliasing and selective imports** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Aliasing and Selective Imports
x = chapter_8_demo = True
print("Aliasing and Selective Imports", x)
```

### Hands-on: Aliasing and Selective Imports

1. State **Aliasing and Selective Imports** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## When to Avoid import *

> **Definition:** This section explains **When to Avoid import *** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **when to avoid import *** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: When to Avoid import *
x = chapter_8_demo = True
print("When to Avoid import *", x)
```

### Hands-on: When to Avoid import *

1. State **When to Avoid import *** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## __name__ and the Script Entry Point

> **Definition:** This section explains **__name__ and the Script Entry Point** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **__name__ and the script entry point** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: __name__ and the Script Entry Point
x = chapter_8_demo = True
print("__name__ and the Script Entry Point", x)
```

### Hands-on: __name__ and the Script Entry Point

1. State **__name__ and the Script Entry Point** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## How Python Finds Modules

> **Definition:** This section explains **How Python Finds Modules** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **how python finds modules** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: How Python Finds Modules
x = chapter_8_demo = True
print("How Python Finds Modules", x)
```

### Hands-on: How Python Finds Modules

1. State **How Python Finds Modules** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## What Is a Package?

> **Definition:** This section explains **What Is a Package?** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **what is a package?** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: What Is a Package?
x = chapter_8_demo = True
print("What Is a Package?", x)
```

### Hands-on: What Is a Package?

1. State **What Is a Package?** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Package Layout and __init__.py

> **Definition:** This section explains **Package Layout and __init__.py** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **package layout and __init__.py** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Package Layout and __init__.py
x = chapter_8_demo = True
print("Package Layout and __init__.py", x)
```

### Hands-on: Package Layout and __init__.py

1. State **Package Layout and __init__.py** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Relative vs Absolute Imports

> **Definition:** This section explains **Relative vs Absolute Imports** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **relative vs absolute imports** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Relative vs Absolute Imports
x = chapter_8_demo = True
print("Relative vs Absolute Imports", x)
```

### Hands-on: Relative vs Absolute Imports

1. State **Relative vs Absolute Imports** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Namespace Packages

> **Definition:** This section explains **Namespace Packages** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **namespace packages** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Namespace Packages
x = chapter_8_demo = True
print("Namespace Packages", x)
```

### Hands-on: Namespace Packages

1. State **Namespace Packages** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## The __all__ Public API

> **Definition:** This section explains **The __all__ Public API** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **the __all__ public api** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: The __all__ Public API
x = chapter_8_demo = True
print("The __all__ Public API", x)
```

### Hands-on: The __all__ Public API

1. State **The __all__ Public API** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Circular Imports

> **Definition:** This section explains **Circular Imports** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **circular imports** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Circular Imports
x = chapter_8_demo = True
print("Circular Imports", x)
```

### Hands-on: Circular Imports

1. State **Circular Imports** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Standard Library Tour

> **Definition:** This section explains **Standard Library Tour** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **standard library tour** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Standard Library Tour
x = chapter_8_demo = True
print("Standard Library Tour", x)
```

### Hands-on: Standard Library Tour

1. State **Standard Library Tour** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Third-Party Packages and pip

> **Definition:** This section explains **Third-Party Packages and pip** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **third-party packages and pip** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Third-Party Packages and pip
x = chapter_8_demo = True
print("Third-Party Packages and pip", x)
```

### Hands-on: Third-Party Packages and pip

1. State **Third-Party Packages and pip** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Organizing a Real Project

> **Definition:** This section explains **Organizing a Real Project** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **organizing a real project** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Organizing a Real Project
x = chapter_8_demo = True
print("Organizing a Real Project", x)
```

### Hands-on: Organizing a Real Project

1. State **Organizing a Real Project** in your own words.
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
x = chapter_8_demo = True
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
x = chapter_8_demo = True
print("Common Mistakes", x)
```

### Hands-on: Common Mistakes

1. State **Common Mistakes** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: What is a module?**

Any `.py` file — code reused via `import`.

---

> **📌 Interview Point 2: What is a package?**

Directory of modules with `__init__.py` (or namespace package PEP 420).

---

> **📌 Interview Point 3: What is `__name__ == '__main__'`?**

True when file run as script — guard script-only code.

---

> **📌 Interview Point 4: Absolute vs relative import?**

Absolute from project root preferred; relative use `.` for same package.

---

> **📌 Interview Point 5: Why avoid `import *`?**

Pollutes namespace, hides origin, breaks static analysis.

---

> **📌 Interview Point 6: Where does Python look for modules?**

`sys.path` — cwd, PYTHONPATH, site-packages, stdlib.

---

> **📌 Interview Point 7: Circular import fix?**

Restructure, move imports inside functions, or extract shared module.

---

> **📌 Interview Point 8: What is `__all__`?**

Public API list for `from module import *` (still discouraged externally).

---

> **📌 Interview Point 9: Namespace package?**

PEP 420 — packages without `__init__.py` split across directories.

---

> **📌 Interview Point 10: stdlib vs third-party?**

Ships with Python vs installed via pip into site-packages.

---

> **📌 Interview Point 11: What is site-packages?**

Directory where pip installs packages for active interpreter.

---

> **📌 Interview Point 12: Package `__init__.py` role?**

Package marker, re-exports, package-level setup.

---

> **📌 Interview Point 13: Relative import dots?**

`.sibling` same package; `..parent` up one level.

---

> **📌 Interview Point 14: Module caching?**

First import loads; `importlib.reload()` for dev only.

---

> **📌 Interview Point 15: Virtual env effect on imports?**

Isolated site-packages per project — correct dependency versions.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Import math ⭐

**Task:** Use math.sqrt on 16.

<details>
<summary>💡 Hint (click to reveal)</summary>

import math.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
import math
print(math.sqrt(16))
```

</details>

---

### Exercise 2: __main__ guard ⭐⭐

**Task:** Script that prints __name__.

<details>
<summary>💡 Hint (click to reveal)</summary>

if __name__ == '__main__'.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def main():
    print("running")
if __name__ == "__main__":
    main()
```

</details>

---

### Exercise 3: Random choice ⭐⭐

**Task:** from random import choice.

<details>
<summary>💡 Hint (click to reveal)</summary>

import choice.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
from random import choice
print(choice(["a", "b", "c"]))
```

</details>


## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **module** | Any .py file you import |
| **package** | Folder of modules with __init__.py |
| **__main__** | Guard script-only code |
| **sys.path** | Module search order |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**⬅️ [Previous: Object-Oriented Programming](./ch07-oop.md)**

**➡️ [Next: File I/O →](./ch09-file-io.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
