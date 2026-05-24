import json
import re
import os

path = r"C:\Users\User\.cursor\projects\d-Mydocs-CodeShelf\agent-transcripts\7b59d68d-e553-42af-8e33-b71cb97dbd7c\7b59d68d-e553-42af-8e33-b71cb97dbd7c.jsonl"
out_dir = r"d:\Mydocs\CodeShelf\content\drf"
os.makedirs(out_dir, exist_ok=True)

with open(path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        if i != 89:
            continue
        obj = json.loads(line)
        text = obj["message"]["content"][0]["text"]
        if text.startswith("<user_query>"):
            text = text[len("<user_query>") :]
        if text.endswith("</user_query>"):
            text = text[: -len("</user_query>")]
        if text.startswith('"'):
            text = text[1:]
        raw_path = os.path.join(out_dir, "_course_raw.txt")
        with open(raw_path, "w", encoding="utf-8") as o:
            o.write(text)
        print("chars:", len(text))
        print("lines:", text.count("\n"))
        for m in re.finditer(r"Chapter \d+:", text):
            snippet = text[m.start() : m.start() + 100].replace("\n", " ")
            print(m.start(), snippet)
        break
