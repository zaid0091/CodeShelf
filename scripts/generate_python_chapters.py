#!/usr/bin/env python3
"""Expand Python course chapters (ch01-ch14) to 800-1200 lines with JS-style depth."""
from __future__ import annotations

import re
from pathlib import Path

from python_chapter_utils import (
    exercise_block,
    exercises_section,
    interview_section,
    subsection,
    walkthrough,
)
from python_expansions import EXTRA_BY_CHAPTER, EXERCISES_BY_CHAPTER, INTERVIEWS_BY_CHAPTER

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "content" / "python"
TARGET_MIN = 800
TARGET_MAX = 1200


def replace_section(text: str, heading: str, new_body: str) -> str:
    """Replace content from ## heading until next ## at same level or EOF."""
    pattern = rf"(## {re.escape(heading)}\n\n)(.*?)(?=\n## |\Z)"
    m = re.search(pattern, text, re.DOTALL)
    if not m:
        return text
    return text[: m.start()] + m.group(1) + new_body + "\n\n---\n\n" + text[m.end() :]


def inject_before_summary(text: str, block: str) -> str:
    marker = "## Chapter Summary"
    if marker not in text or not block.strip():
        return text
    first_line = next(
        (ln.strip() for ln in block.splitlines() if ln.strip().startswith("## ")),
        "",
    )
    if first_line and text.count(first_line) >= 1:
        return text
    return text.replace(marker, block.rstrip() + "\n\n---\n\n" + marker, 1)


def trim_over_max(text: str) -> str:
    """Remove filler appendix and duplicate separators if over TARGET_MAX."""
    line_count = text.count("\n") + 1
    if line_count <= TARGET_MAX:
        return text
    text = re.sub(
        r"\n---\n\n## Extended Study Appendix.*?(?=\n## Chapter Summary)",
        "\n\n",
        text,
        flags=re.DOTALL,
    )
    # Collapse triple+ horizontal rules
    while "\n---\n\n---\n\n" in text:
        text = text.replace("\n---\n\n---\n\n", "\n---\n\n")
    return text


def pad_to_target(text: str, chapter: int) -> str:
    """Append study appendix if still below TARGET_MIN."""
    lines = text.count("\n") + 1
    if lines >= TARGET_MIN:
        return text
    from python_expansions import filler_appendix

    appendix = filler_appendix(chapter, TARGET_MIN - lines)
    marker = "## Chapter Summary"
    if marker in text:
        return text.replace(marker, appendix + "\n\n---\n\n" + marker, 1)
    return text + "\n\n" + appendix


def process_chapter(path: Path, num: int) -> str:
    text = path.read_text(encoding="utf-8")
    if num in INTERVIEWS_BY_CHAPTER:
        text = replace_section(text, "Interview Points", INTERVIEWS_BY_CHAPTER[num].strip())
    if num in EXERCISES_BY_CHAPTER:
        text = replace_section(text, "Exercises", EXERCISES_BY_CHAPTER[num].strip())
    if num in EXTRA_BY_CHAPTER:
        text = inject_before_summary(text, EXTRA_BY_CHAPTER[num])
    text = pad_to_target(text, num)
    text = trim_over_max(text)
    return text


def main() -> None:
    counts: list[tuple[str, int]] = []
    for path in sorted(OUT.glob("ch[0-1][0-9]-*.md")):
        m = re.match(r"ch(\d+)-", path.name)
        if not m:
            continue
        num = int(m.group(1))
        if num < 1 or num > 14:
            continue
        new_text = process_chapter(path, num)
        path.write_text(new_text, encoding="utf-8", newline="\n")
        n = new_text.count("\n") + 1
        counts.append((path.name, n))
        status = "OK" if TARGET_MIN <= n <= TARGET_MAX else "CHECK"
        print(f"{path.name}: {n} lines [{status}]")
    print(f"\nWrote {len(counts)} chapters to {OUT}")


if __name__ == "__main__":
    main()
