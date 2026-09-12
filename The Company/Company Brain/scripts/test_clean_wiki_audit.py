#!/usr/bin/env python3
import os
import re
from pathlib import Path
from collections import defaultdict

COMPANY_DIR = Path(__file__).resolve().parent.parent
BRAIN_DIR = COMPANY_DIR


EXCLUDE_PARTS = {
    "node_modules", ".git", ".venv", "dist", "build", ".next",
    ".cache", ".pytest_cache", "site-packages", "__pycache__"
}

def strip_code_blocks(text):
    # Strip multi-line fenced code blocks ```...``` and ````...````
    text = re.sub(r'```[\s\S]*?```', '', text)
    # Strip inline code `...`
    text = re.sub(r'`[^`\n]+`', '', text)
    return text

WIKI_LINK_PATTERN = re.compile(r'\[\[([^\]|#\n]+)(?:#[^\]|\n]*)?(?:\|[^\]\n]*)?\]\]')

doc_files = []
for root, dirs, files in os.walk(COMPANY_DIR):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_PARTS]
    for f in files:
        if f.endswith(".md"):
            p = Path(root) / f
            doc_files.append(p)

by_stem = defaultdict(list)
for p in doc_files:
    by_stem[p.stem.lower()].append(p)

broken_counts = defaultdict(int)
total_links = 0

for p in doc_files:
    try:
        raw = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    clean = strip_code_blocks(raw)
    for t in WIKI_LINK_PATTERN.findall(clean):
        total_links += 1
        t_clean = t.strip().rstrip('\\')
        if not t_clean:
            continue
        # check resolution
        if (p.parent / f"{t_clean}.md").is_file() or (p.parent / t_clean).is_file():
            continue
        if (BRAIN_DIR / t_clean).exists() or (BRAIN_DIR / f"{t_clean}.md").exists():
            continue
        if t_clean.lower() in by_stem:
            continue
        broken_counts[t_clean] += 1

print(f"Total markdown docs scanned: {len(doc_files)}")
print(f"Total clean wiki links in prose: {total_links}")
print(f"Total distinct broken targets: {len(broken_counts)}")
print("\nTop 30 REAL broken wiki targets:")
for target, count in sorted(broken_counts.items(), key=lambda x: x[1], reverse=True)[:30]:
    print(f"  {count:3d}x  [[{target}]]")
