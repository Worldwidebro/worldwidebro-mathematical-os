#!/usr/bin/env python3
"""Extract and print all wiki‑style links from START_HERE.md.
"""
import re
import pathlib

START_HERE = pathlib.Path(__file__).parent.parent / "START_HERE.md"
content = START_HERE.read_text(encoding="utf-8")
links = re.findall(r"\[\[([^\]]+)\]\]", content)
print("## Wiki Links in START_HERE.md\n")
for l in links:
    print(f"- {l}")
