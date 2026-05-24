---
title: File I/O
description: Reading and writing text and binary files, paths, CSV, and JSON
order: 9
tags: [python, files, io]
---

# Chapter 9: File I/O

## 9.1 Opening files

> **Definition:** **File I/O** is reading from and writing to the filesystem. Always prefer `with` to ensure files close automatically.

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
```

| Mode | Meaning |
|------|---------|
| `"r"` | Read (default) |
| `"w"` | Write (truncates) |
| `"a"` | Append |
| `"x"` | Create, fail if exists |
| `"b"` | Binary (`"rb"`, `"wb"`) |
| `"+"` | Read and write |

## 9.2 Reading strategies

```python
with open("data.txt", "r", encoding="utf-8") as f:
    whole = f.read()           # entire file as str

with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()      # list of lines (includes \n)

# Memory-efficient line iteration
with open("large.log", "r", encoding="utf-8") as f:
    for line in f:
        process(line.strip())
```

## 9.3 Writing and appending

```python
lines = ["first\n", "second\n"]

with open("log.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

with open("log.txt", "a", encoding="utf-8") as f:
    f.write("third\n")
```

## 9.4 Path handling with `pathlib`

```python
from pathlib import Path

root = Path("myproject")
config = root / "config" / "settings.json"

config.parent.mkdir(parents=True, exist_ok=True)
config.write_text('{"debug": true}', encoding="utf-8")

if config.exists():
    print(config.read_text(encoding="utf-8"))

for py_file in root.rglob("*.py"):
    print(py_file)
```

Prefer `pathlib.Path` over string paths for cross-platform code.

## 9.5 JSON

```python
import json
from pathlib import Path

data = {"name": "Alice", "scores": [90, 85, 92]}

Path("user.json").write_text(
    json.dumps(data, indent=2),
    encoding="utf-8",
)

loaded = json.loads(Path("user.json").read_text(encoding="utf-8"))
```

| Function | Use |
|----------|-----|
| `json.dumps` / `loads` | String ↔ Python |
| `json.dump` / `load` | File object ↔ Python |

## 9.6 CSV

```python
import csv
from pathlib import Path

rows = [
    ["name", "score"],
    ["Alice", 90],
    ["Bob", 85],
]

with Path("grades.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

with Path("grades.csv").open("r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["score"])
```

## 9.7 Binary files

```python
from pathlib import Path

data = b"\x00\x01\xff"
Path("blob.bin").write_bytes(data)
restored = Path("blob.bin").read_bytes()
```

Use binary mode for images, PDFs, and other non-text formats.

## 9.8 Context managers

Files support the context manager protocol (`__enter__`/`__exit__`). See [Exceptions](./ch10-exceptions.md) for custom context managers.

```python
with open("file.txt") as f:
    data = f.read()
# f.close() called automatically, even on error
```

## 9.9 Error handling for I/O

```python
from pathlib import Path

path = Path("missing.txt")
try:
    text = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
```

## 9.10 Temporary files

```python
import tempfile
from pathlib import Path

with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
    f.write("temp data")
    temp_path = Path(f.name)

temp_path.unlink()  # cleanup
```

## Exercises

1. Write a program that counts lines, words, and characters in a text file.
2. Save a list of dicts to JSON and load it back.
3. Read a CSV and compute the average of a numeric column.
4. Use `pathlib` to copy all `.txt` files from one folder to another.

## Summary

Use `with open()` or `Path` methods, always specify `encoding="utf-8"` for text, and choose JSON/CSV modules for structured data.

## Next chapter

Continue to [Exceptions](./ch10-exceptions.md).
