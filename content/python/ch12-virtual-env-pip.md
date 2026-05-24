---
title: Virtual Environments and pip
description: venv, pip, requirements.txt, PyPI, and dependency management
order: 12
tags: [python, venv, pip]
---

# Chapter 12: Virtual Environments and pip

## 12.1 Why virtual environments?

> **Definition:** A **virtual environment** is an isolated Python installation with its own packages, separate from the system Python.

| Problem without venv | Solution |
|---------------------|----------|
| Package version conflicts | Per-project dependencies |
| Polluting system Python | Isolated site-packages |
| Non-reproducible setups | Lock/requirements files |

## 12.2 Creating a venv

```bash
# Create
python -m venv .venv

# Activate — Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Activate — macOS/Linux
source .venv/bin/activate

# Deactivate
deactivate
```

After activation, `python` and `pip` point to the venv.

## 12.3 pip basics

> **Definition:** **pip** is Python's package installer, fetching packages from [PyPI](https://pypi.org).

```bash
pip install requests
pip install django==5.0
pip install "pytest>=7.0,<8"
pip uninstall requests
pip list
pip show django
```

## 12.4 requirements.txt

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
django==5.0.1
requests>=2.31.0
pytest==7.4.4
```

Pin versions for reproducible deployments.

## 12.5 pyproject.toml (modern projects)

Many projects use `pyproject.toml` with tools like Poetry, Hatch, or uv:

```toml
[project]
name = "myapp"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = [
    "django>=5.0",
    "requests>=2.31",
]

[project.optional-dependencies]
dev = ["pytest", "ruff"]
```

```bash
pip install -e ".[dev]"
```

## 12.6 Editable installs

```bash
pip install -e .
```

Installs the project in "editable" mode — code changes apply without reinstall. Useful during development.

## 12.7 Upgrading and security

```bash
pip install --upgrade pip
pip install --upgrade requests
pip audit  # check known vulnerabilities (pip 22+)
```

Review dependencies regularly; avoid unused packages.

## 12.8 `.gitignore` for Python

```text
.venv/
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.env
```

Never commit virtual environments or secrets.

## 12.9 Multiple Python versions

Tools for managing interpreters:

| Tool | Purpose |
|------|---------|
| `pyenv` | Install/switch Python versions |
| `py -3.12` (Windows launcher) | Run specific version |
| `docker` | Containerized runtime |

```bash
py -3.12 -m venv .venv
```

## 12.10 Common workflow

```bash
python -m venv .venv
source .venv/bin/activate   # or Windows equivalent
pip install -U pip
pip install -r requirements.txt
python manage.py runserver  # or your entry point
```

## 12.11 pip vs conda

| | pip + venv | conda |
|---|------------|-------|
| Ecosystem | PyPI | Conda channels |
| Non-Python deps | Limited | Strong (C libs) |
| Data science | Common with pip | Often conda |

For web dev (Django), pip + venv is standard. See [Django setup](../django/ch02-setup-project-structure.md).

## Exercises

1. Create a venv, activate it, and verify `which python` (or `where python` on Windows).
2. Install `httpx` and write a one-liner to fetch a URL.
3. Generate `requirements.txt` from your venv after installing two packages.
4. Add `.venv/` and `__pycache__/` to a project `.gitignore`.

## Summary

Use one venv per project, pin dependencies, and never install globally unless you know why. pip + requirements.txt is the baseline; `pyproject.toml` scales better.

## Next chapter

Continue to [Best Practices](./ch13-best-practices.md).
