"""Shared helpers for TypeScript chapter generation."""

def fm(title: str, desc: str, order: int, tags: list[str]) -> str:
    tag_line = ", ".join(tags)
    return f"""---
title: {title}
description: {desc}
order: {order}
tags: [{tag_line}]
---

"""


def welcome(title: str, subtitle: str) -> str:
    return f"""# {title}

> **{subtitle}**
> Take your time with each section. TypeScript rewards patience — read compiler errors carefully and experiment in a small project as you go.

---

"""


def toc(items: list[str]) -> str:
    lines = ["## Table of Contents", ""]
    for i, label in enumerate(items, 1):
        anchor = label.lower()
        anchor = "".join(c if c.isalnum() or c in " -" else "" for c in anchor)
        anchor = anchor.strip().replace(" ", "-").replace("--", "-")
        lines.append(f"{i}. [{label}](#{anchor})")
    lines += ["", "---", ""]
    return "\n".join(lines)


def summary(sections: list[str]) -> str:
    out = ["## Chapter Summary", "", "You covered a lot in this chapter. Here is a concise recap:", ""]
    for s in sections:
        out.append(f"- {s}")
    out += ["", "---", ""]
    return "\n".join(out)


def best_practices(items: list[str]) -> str:
    out = ["## Best Practices", ""]
    for item in items:
        out.append(f"- ✅ {item}")
    out += ["", "---", ""]
    return "\n".join(out)
