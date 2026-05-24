---
title: Python Best Practices
description: PEP 8, typing, testing basics, logging, and project layout
order: 13
tags: [python, best-practices, pep8]
---

# Chapter 13: Python Best Practices

## 13.1 Readability counts

The Zen of Python (`import this`) emphasizes clarity. Code is read more often than written — optimize for the reader.

## 13.2 PEP 8 style guide

| Rule | Example |
|------|---------|
| 4 spaces for indent | Never tabs mixed with spaces |
| `snake_case` functions/vars | `calculate_total` |
| `PascalCase` classes | `BankAccount` |
| `UPPER_SNAKE` constants | `MAX_RETRIES = 3` |
| Two blank lines between top-level defs | Classes and functions |
| Max line length ~88–99 | Black formatter default |

```python
# Good
def fetch_user(user_id: int) -> dict:
    return api.get(f"/users/{user_id}")

# Avoid
def FetchUser(UserID):
    return api.get("/users/"+str(UserID))
```

Use **ruff** or **flake8** locally; **black** or **ruff format** for formatting.

## 13.3 Type hints and static analysis

```python
from typing import Sequence

def average(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("empty sequence")
    return sum(values) / len(values)
```

Run `mypy` or `pyright` in CI. See [Functions](./ch04-functions.md).

## 13.4 Project layout

```text
myproject/
├── pyproject.toml
├── README.md
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
└── tests/
    ├── __init__.py
    └── test_utils.py
```

| Pattern | Benefit |
|---------|---------|
| `src/` layout | Avoid accidental imports from cwd |
| Separate `tests/` | Clear test discovery |
| Package in subfolder | Installable distribution |

## 13.5 Testing with pytest

```python
# tests/test_utils.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

```bash
pip install pytest
pytest
pytest -v tests/test_utils.py
```

| Practice | Why |
|----------|-----|
| One assert focus per test | Easier failures |
| Descriptive test names | `test_empty_list_raises` |
| Fixtures for setup | Reusable test data |

## 13.6 Logging vs print

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.debug("Detailed debug info")
logger.info("Server started")
logger.warning("Deprecated API used")
logger.error("Failed to connect")
```

Use `logging` in libraries and apps; reserve `print` for scripts and CLI output.

## 13.7 Configuration and secrets

```python
import os
from pathlib import Path

DEBUG = os.getenv("DEBUG", "false").lower() == "true"
DATABASE_URL = os.environ["DATABASE_URL"]  # required
```

- Load secrets from environment variables or `.env` (with `python-dotenv`)
- Never commit API keys or passwords
- See [Virtual Environments & pip](./ch12-virtual-env-pip.md)

## 13.8 Error handling discipline

- Catch specific [exceptions](./ch10-exceptions.md)
- Fail fast on programmer errors (`assert` sparingly)
- Return meaningful error messages to users
- Log stack traces server-side, not client-side

## 13.9 Documentation

- Module-level docstrings for public packages
- README with install, run, and test instructions
- Type hints as inline documentation

## 13.10 Performance tips (when needed)

```python
# Profile before optimizing
import cProfile
cProfile.run("main()")

# Common wins
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive(n):
    ...
```

Measure first; prefer algorithmic improvements over micro-optimizations.

## Exercises

1. Run `ruff check` or `flake8` on a small script and fix style issues.
2. Add type hints to three functions and run `mypy`.
3. Write two pytest tests for a function you wrote earlier.
4. Replace `print` debugging with `logging` in a small script.

## Summary

Follow PEP 8, type and test your code, structure projects consistently, and use logging and env-based config for production readiness.

## Next chapter

Continue to [Interview Preparation](./ch14-interview-prep.md).
