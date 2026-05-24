---
title: File I/O
description: Reading and writing files, encoding, pathlib, JSON, CSV, and context managers
order: 9
tags: [python, files, io]
---

# Chapter 9: File I/O

> **Programs persist data on disk. Learn safe file handling, paths, and common formats like JSON and CSV.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [Why File I/O Matters](#why-file-i-o-matters)
2. [Files vs File Objects](#files-vs-file-objects)
3. [Opening Files with open()](#opening-files-with-open)
4. [File Modes Explained](#file-modes-explained)
5. [The with Statement](#the-with-statement)
6. [Reading Text Files](#reading-text-files)
7. [Writing and Appending Text](#writing-and-appending-text)
8. [Encoding and Unicode](#encoding-and-unicode)
9. [Line Endings and newline](#line-endings-and-newline)
10. [Binary Files](#binary-files)
11. [Path Handling with pathlib](#path-handling-with-pathlib)
12. [Working with JSON](#working-with-json)
13. [Working with CSV](#working-with-csv)
14. [Reading Large Files Efficiently](#reading-large-files-efficiently)
15. [Copying, Moving, and Deleting](#copying-moving-and-deleting)
16. [Temporary Files and Directories](#temporary-files-and-directories)
17. [Error Handling for I/O](#error-handling-for-i-o)
18. [Context Managers Recap](#context-managers-recap)
19. [Best Practices](#best-practices)
20. [Common Mistakes](#common-mistakes)
21. [Interview Points](#interview-points)
22. [Exercises](#exercises)
23. [Chapter Summary](#chapter-summary)

---

## Why File I/O Matters

> **Definition:** This section explains **Why File I/O Matters** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **why file i/o matters** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Why File I/O Matters
x = chapter_9_demo = True
print("Why File I/O Matters", x)
```

### Hands-on: Why File I/O Matters

1. State **Why File I/O Matters** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Files vs File Objects

> **Definition:** This section explains **Files vs File Objects** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **files vs file objects** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Files vs File Objects
x = chapter_9_demo = True
print("Files vs File Objects", x)
```

### Hands-on: Files vs File Objects

1. State **Files vs File Objects** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Opening Files with open()

> **Definition:** This section explains **Opening Files with open()** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **opening files with open()** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Opening Files with open()
x = chapter_9_demo = True
print("Opening Files with open()", x)
```

### Hands-on: Opening Files with open()

1. State **Opening Files with open()** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## File Modes Explained

> **Definition:** This section explains **File Modes Explained** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **file modes explained** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: File Modes Explained
x = chapter_9_demo = True
print("File Modes Explained", x)
```

### Hands-on: File Modes Explained

1. State **File Modes Explained** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## The with Statement

> **Definition:** This section explains **The with Statement** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **the with statement** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: The with Statement
x = chapter_9_demo = True
print("The with Statement", x)
```

### Hands-on: The with Statement

1. State **The with Statement** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Reading Text Files

> **Definition:** This section explains **Reading Text Files** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **reading text files** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Reading Text Files
x = chapter_9_demo = True
print("Reading Text Files", x)
```

### Hands-on: Reading Text Files

1. State **Reading Text Files** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Writing and Appending Text

> **Definition:** This section explains **Writing and Appending Text** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **writing and appending text** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Writing and Appending Text
x = chapter_9_demo = True
print("Writing and Appending Text", x)
```

### Hands-on: Writing and Appending Text

1. State **Writing and Appending Text** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Encoding and Unicode

> **Definition:** This section explains **Encoding and Unicode** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **encoding and unicode** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Encoding and Unicode
x = chapter_9_demo = True
print("Encoding and Unicode", x)
```

### Hands-on: Encoding and Unicode

1. State **Encoding and Unicode** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Line Endings and newline

> **Definition:** This section explains **Line Endings and newline** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **line endings and newline** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Line Endings and newline
x = chapter_9_demo = True
print("Line Endings and newline", x)
```

### Hands-on: Line Endings and newline

1. State **Line Endings and newline** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Binary Files

> **Definition:** This section explains **Binary Files** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **binary files** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Binary Files
x = chapter_9_demo = True
print("Binary Files", x)
```

### Hands-on: Binary Files

1. State **Binary Files** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Path Handling with pathlib

> **Definition:** This section explains **Path Handling with pathlib** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **path handling with pathlib** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Path Handling with pathlib
x = chapter_9_demo = True
print("Path Handling with pathlib", x)
```

### Hands-on: Path Handling with pathlib

1. State **Path Handling with pathlib** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Working with JSON

> **Definition:** This section explains **Working with JSON** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **working with json** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Working with JSON
x = chapter_9_demo = True
print("Working with JSON", x)
```

### Hands-on: Working with JSON

1. State **Working with JSON** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Working with CSV

> **Definition:** This section explains **Working with CSV** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **working with csv** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Working with CSV
x = chapter_9_demo = True
print("Working with CSV", x)
```

### Hands-on: Working with CSV

1. State **Working with CSV** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Reading Large Files Efficiently

> **Definition:** This section explains **Reading Large Files Efficiently** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **reading large files efficiently** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Reading Large Files Efficiently
x = chapter_9_demo = True
print("Reading Large Files Efficiently", x)
```

### Hands-on: Reading Large Files Efficiently

1. State **Reading Large Files Efficiently** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Copying, Moving, and Deleting

> **Definition:** This section explains **Copying, Moving, and Deleting** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **copying, moving, and deleting** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Copying, Moving, and Deleting
x = chapter_9_demo = True
print("Copying, Moving, and Deleting", x)
```

### Hands-on: Copying, Moving, and Deleting

1. State **Copying, Moving, and Deleting** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Temporary Files and Directories

> **Definition:** This section explains **Temporary Files and Directories** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **temporary files and directories** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Temporary Files and Directories
x = chapter_9_demo = True
print("Temporary Files and Directories", x)
```

### Hands-on: Temporary Files and Directories

1. State **Temporary Files and Directories** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Error Handling for I/O

> **Definition:** This section explains **Error Handling for I/O** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **error handling for i/o** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Error Handling for I/O
x = chapter_9_demo = True
print("Error Handling for I/O", x)
```

### Hands-on: Error Handling for I/O

1. State **Error Handling for I/O** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Context Managers Recap

> **Definition:** This section explains **Context Managers Recap** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **context managers recap** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Context Managers Recap
x = chapter_9_demo = True
print("Context Managers Recap", x)
```

### Hands-on: Context Managers Recap

1. State **Context Managers Recap** in your own words.
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
x = chapter_9_demo = True
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
x = chapter_9_demo = True
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

> **📌 Interview Point 1: Why use `with open()`?**

Guarantees file closed even on exception — context manager protocol.

---

> **📌 Interview Point 2: Text vs binary mode?**

Text: str, encoding. Binary: bytes — images, pickles.

---

> **📌 Interview Point 3: What encoding to use?**

UTF-8 default for text — specify `encoding='utf-8'` explicitly.

---

> **📌 Interview Point 4: `read` vs `readline` vs iteration?**

Iteration line-by-line memory-efficient for large files.

---

> **📌 Interview Point 5: pathlib vs os.path?**

pathlib object-oriented paths — `/` operator, `.read_text()`.

---

> **📌 Interview Point 6: JSON vs CSV?**

JSON: nested structures; CSV: tabular spreadsheets.

---

> **📌 Interview Point 7: How to handle missing file?**

Catch `FileNotFoundError` or check `Path.exists()`.

---

> **📌 Interview Point 8: Append vs write mode?**

`'a'` appends; `'w'` truncates existing file.

---

> **📌 Interview Point 9: What is `newline` param?**

Controls line ending translation on Windows text mode.

---

> **📌 Interview Point 10: Large file strategy?**

Stream lines; never `read()` multi-GB into memory.

---

> **📌 Interview Point 11: Temporary files?**

`tempfile` module — auto cleanup.

---

> **📌 Interview Point 12: Atomic write pattern?**

Write temp file then `replace()` — avoid partial writes.

---

> **📌 Interview Point 13: Binary pickle risks?**

Never unpickle untrusted data — arbitrary code execution.

---

> **📌 Interview Point 14: CSV dialect issues?**

Use `csv` module; handle quoting and delimiters.

---

> **📌 Interview Point 15: Working directory vs script path?**

Use `Path(__file__).parent` for paths relative to code location.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Write lines ⭐

**Task:** Write three lines to notes.txt with with.

<details>
<summary>💡 Hint (click to reveal)</summary>

writelines or write.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("line1\nline2\n")
```

</details>

---

### Exercise 2: Read JSON ⭐⭐

**Task:** Load dict from data.json.

<details>
<summary>💡 Hint (click to reveal)</summary>

json.load.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
import json
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)
```

</details>

---

### Exercise 3: pathlib exists ⭐⭐

**Task:** Check Path('file.txt').exists().

<details>
<summary>💡 Hint (click to reveal)</summary>

from pathlib import Path.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
from pathlib import Path
print(Path("file.txt").exists())
```

</details>


## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **with open** | Auto-close files |
| **encoding** | UTF-8 for text |
| **pathlib** | Object-oriented paths |
| **json/csv** | Structured data formats |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**⬅️ [Previous: Modules and Packages](./ch08-modules-packages.md)**

**➡️ [Next: Exceptions →](./ch10-exceptions.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
