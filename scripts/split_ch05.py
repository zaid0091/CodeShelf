"""Extract Chapter 5 markdown from parent transcript and split into 7 parts."""
import json
import os
import re
import sys

TRANSCRIPT = r"C:\Users\User\.cursor\projects\d-Mydocs-CodeShelf\agent-transcripts\f807f7a5-2787-40b5-87b0-c4c6c8e68d3f\f807f7a5-2787-40b5-87b0-c4c6c8e68d3f.jsonl"
OUT_DIR = r"d:\Mydocs\CodeShelf\scripts"

SPLITS = [
    ("_ch05_part1.md", "## 1. What is an Array?", "### Transforming"),
    ("_ch05_part2.md", "### Transforming", "## 5. What is an Object?"),
    ("_ch05_part3.md", "## 5. What is an Object?", "## 10. Destructuring"),
    ("_ch05_part4.md", "## 10. Destructuring", "## 13. Nested Arrays and Objects"),
    ("_ch05_part5.md", "## 13. Nested Arrays and Objects", "## 16. Common Mistakes Developers Make"),
    ("_ch05_part6.md", "## 16. Common Mistakes Developers Make", "## 20. Exercises"),
    ("_ch05_part7.md", "## 20. Exercises", None),
]

PART7_FOOTER = """---

**Previous:** [Chapter 4: Functions](./ch04-functions.md) · **Next:** [Chapter 6: ES6+ Modern Features](./ch06-es6-modern-features.md)

**➡️ [Next Chapter: ES6+ Modern Features →](./ch06-es6-modern-features.md)"""


def extract_md() -> str:
    with open(TRANSCRIPT, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            if obj.get("role") != "user":
                continue
            text = obj["message"]["content"][0]["text"]
            if "use this content" not in text:
                continue
            if "Chapter 5: Arrays and Objects" not in text and "order: 5" not in text:
                continue
            if "What is an Array" not in text:
                continue
            m = re.search(r"```md\n(.*?)```\"", text, re.DOTALL)
            if not m:
                m = re.search(r"```md\n(.*)", text, re.DOTALL)
            if not m:
                m = re.search(r'```md id="[^"]*"\n(.*?)```', text, re.DOTALL)
            if not m:
                raise SystemExit("Could not find ```md block in Chapter 5 message")
            md = m.group(1)
            if md.endswith("```"):
                md = md[:-3].rstrip()
            return md
    raise SystemExit(
        "Chapter 5 message not found in transcript. "
        "Send 'use this content' with the full Chapter 5 markdown first."
    )


def slice_content(body: str, start: str, end: str | None) -> str:
    i = body.index(start)
    if end is None:
        chunk = body[i:]
    else:
        j = body.index(end, i + 1)
        chunk = body[i:j].rstrip() + "\n"
    chunk = re.sub(r"<!--\s*CH05_PART\d+\s*-->\s*\n?", "", chunk)
    chunk = re.sub(
        r">\s*➡️\s*\*\*Next Chapter: Asynchronous JavaScript.*?\*\*",
        "",
        chunk,
        flags=re.DOTALL,
    )
    chunk = re.sub(
        r">\s*➡️\s*\*\*Next Chapter: Objects and Prototypes.*?\*\*",
        "",
        chunk,
        flags=re.DOTALL,
    )
    chunk = chunk.replace("```javascript", "```js")
    return chunk.rstrip() + "\n"


def main() -> None:
    full = extract_md()
    start_body = full.index("## 1. What is an Array?")
    body = full[start_body:]

    counts: dict[str, int] = {}
    for filename, start, end in SPLITS:
        chunk = slice_content(body, start, end)
        if filename == "_ch05_part7.md":
            chunk = chunk.rstrip() + "\n\n" + PART7_FOOTER + "\n"
        path = os.path.join(OUT_DIR, filename)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(chunk)
        counts[filename] = chunk.count("\n") + (0 if chunk.endswith("\n") else 1)

    print("Line counts:")
    for name, n in counts.items():
        print(f"  {name}: {n}")
    print(f"  TOTAL: {sum(counts.values())}")


if __name__ == "__main__":
    main()
