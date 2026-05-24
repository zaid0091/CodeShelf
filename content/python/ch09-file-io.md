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

> **Definition:** Programs read config, logs, and user uploads from disk.

### Why it matters

Persistence survives process restarts.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
from pathlib import Path
p = Path('notes.txt')
print(p.exists())
```


---

## Files vs File Objects

> **Definition:** Open files return **file objects** with `.read()`, `.write()`, `.close()`.

### Why it matters

Always close files — use `with`.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
with open('out.txt','w') as f:
    f.write('hi')
```


---

## Opening Files with open()

> **Definition:** `open(path, mode='r', encoding='utf-8')`.

### Why it matters

Text modes need encoding on Windows.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
with open('data.txt', encoding='utf-8') as f:
    text = f.read()
```


---

## File Modes Explained

> **Definition:** `r` read, `w` write (truncate), `a` append, `x` exclusive create, `b` binary.

### Why it matters

Wrong mode corrupts or truncates data.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
with open('log.txt','a') as f:
    f.write('line\n')
```


---

## The with Statement

> **Definition:** Context manager closes file even on exceptions.

### Why it matters

Preferred over manual `close()`.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
with open('f.txt') as f:
    data = f.read()
```


---

## Reading Text Files

> **Definition:** `.read()`, `.readline()`, `.readlines()` or iterate lines.

### Why it matters

Iterate large files line by line.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
with open('f.txt') as f:
    for line in f:
        print(line.strip())
```


---

## Writing and Appending Text

> **Definition:** `.write()` and `.writelines()`.

### Why it matters

Append mode preserves existing content.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
lines = ['a\n','b\n']
with open('f.txt','w') as f:
    f.writelines(lines)
```


---

## Encoding and Unicode

> **Definition:** Specify `encoding='utf-8'` for text files.

### Why it matters

Avoid mojibake on international text.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
text = 'café'
open('u.txt','w',encoding='utf-8').write(text)
```


---

## Line Endings and newline

> **Definition:** `newline=''` lets Python normalize `\r\n` vs `\n`.

### Why it matters

Important for cross-platform CSV.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import csv
with open('r.csv',newline='') as f:
    rows = list(csv.reader(f))
```


---

## Binary Files

> **Definition:** Mode `rb`/`wb` for images, pickles, compressed data.

### Why it matters

Do not decode binary as text.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
data = b'\x00\x01'
with open('b.bin','wb') as f:
    f.write(data)
```


---

## Path Handling with pathlib

> **Definition:** `Path` objects replace `os.path` string juggling.

### Why it matters

Use `/` operator to join paths.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
from pathlib import Path
root = Path('project')
print(root / 'src' / 'app.py')
```


---

## Working with JSON

> **Definition:** `json.load`/`dump` for files; `loads`/`dumps` for strings.

### Why it matters

JSON keys are always strings.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import json
obj = {'ok': True}
print(json.dumps(obj))
```


---

## Working with CSV

> **Definition:** `csv` module reads/writes tabular text.

### Why it matters

Use `DictReader` for header rows.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import csv
with open('t.csv',newline='') as f:
    print(list(csv.reader(f)))
```


---

## Reading Large Files Efficiently

> **Definition:** Stream line-by-line or in chunks.

### Why it matters

Never `read()` multi-GB files into RAM.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
with open('big.log') as f:
    for i, line in enumerate(f):
        if i > 2: break
        print(line[:80])
```


---

## Copying, Moving, and Deleting

> **Definition:** `shutil.copy`, `Path.rename`, `Path.unlink`.

### Why it matters

Automate file housekeeping.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import shutil
shutil.copy('a.txt', 'backup/a.txt')
```


---

## Temporary Files and Directories

> **Definition:** `tempfile` for safe scratch space.

### Why it matters

Cleaned up automatically.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import tempfile
with tempfile.TemporaryDirectory() as d:
    print(d)
```


---

## Error Handling for I/O

> **Definition:** Catch `FileNotFoundError`, `PermissionError`.

### Why it matters

Tell users what path failed.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
try:
    open('missing.txt')
except FileNotFoundError:
    print('not found')
```


---

## Context Managers Recap

> **Definition:** Objects with `__enter__`/`__exit__` work with `with`.

### Why it matters

Files are the classic example.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class Ctx:
    def __enter__(self): return self
    def __exit__(self, *a): pass
```


---

## Best Practices

### Guidelines

- Always specify UTF-8 for text
- Use pathlib for paths


---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Forgetting encoding on Windows | UnicodeDecodeError | encoding='utf-8' |


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
