#!/usr/bin/env python3
"""
Comprehensive Graph Integrity and Awareness Audit v2
Differentiates:
1. Truly Missing Markdown Notes
2. Non-Markdown Data References (.yaml, .json, .csv) that exist vs missing
3. Syntax artifacts (like [[:space:]])
4. Directory links
5. Truly orphaned markdown documents (0 in-links)
6. Disconnected clusters (e.g. The Company vs Company Brain, _TOOLS, BUSINESS-CAPITAL-DATA-ROOM)
"""

import os
import re
import json
from collections import defaultdict
from pathlib import Path

COMPANY_DIR = Path("/Users/acebless/Documents/The Company").resolve()
BRAIN_DIR = COMPANY_DIR / "Company Brain"

WIKI_LINK_PATTERN = re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]')
EXCLUDE_DIRS = {
    ".git", ".venv", "node_modules", "dist", "build", "__pycache__",
    ".cache", ".pytest_cache", ".ruff_cache", "site-packages"
}

def scan_all_files(base_dir):
    all_files = []
    md_files = []
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".tmp")]
        for file in files:
            fp = Path(root) / file
            all_files.append(fp)
            if file.endswith(".md"):
                md_files.append(fp)
    return all_files, md_files

def main():
    print(f"Auditing workspace from: {COMPANY_DIR}")
    all_disk_files, md_files = scan_all_files(COMPANY_DIR)
    print(f"Total files on disk: {len(all_disk_files)} | Markdown files: {len(md_files)}")

    # Index all files on disk
    disk_rel_brain = {}
    disk_rel_company = {}
    md_stem_map = defaultdict(list)
    md_stem_lower = defaultdict(list)
    md_name_lower = defaultdict(list)
    all_disk_name_lower = defaultdict(list)

    for p in all_disk_files:
        name_lower = p.name.lower()
        all_disk_name_lower[name_lower].append(p)
        try:
            rel_b = p.relative_to(BRAIN_DIR).as_posix().lower()
            disk_rel_brain[rel_b] = p
            if rel_b.endswith(".md"):
                disk_rel_brain[rel_b[:-3]] = p
        except ValueError:
            pass
        try:
            rel_c = p.relative_to(COMPANY_DIR).as_posix().lower()
            disk_rel_company[rel_c] = p
            if rel_c.endswith(".md"):
                disk_rel_company[rel_c[:-3]] = p
        except ValueError:
            pass

    for p in md_files:
        stem = p.stem
        md_stem_map[stem].append(p)
        md_stem_lower[stem.lower()].append(p)
        md_name_lower[p.name.lower()].append(p)

    def resolve(target_str, source_file):
        t = target_str.strip()
        if not t:
            return None, "empty"
        if t == ":space:":
            return None, "syntax_error"

        # Check direct relative
        sdir = source_file.parent
        direct = (sdir / t).resolve()
        if direct.is_file():
            return direct, "direct_file"
        if direct.is_dir():
            return direct, "direct_dir"
        direct_md = (sdir / f"{t}.md").resolve()
        if direct_md.is_file():
            return direct_md, "direct_md"

        # Check relative to Brain or Company
        t_low = t.lower()
        if t_low in disk_rel_brain:
            return disk_rel_brain[t_low], "rel_brain"
        if t_low in disk_rel_company:
            return disk_rel_company[t_low], "rel_company"

        # If has extension (.yaml, .json, .csv, etc.)
        if "." in t:
            if t_low in all_disk_name_lower:
                return all_disk_name_lower[t_low][0], "disk_asset"
            return None, "missing_asset"

        # Check by md stem
        if t in md_stem_map:
            return md_stem_map[t][0], "md_stem"
        if t_low in md_stem_lower:
            return md_stem_lower[t_low][0], "md_stem_lower"

        # Check directory relative
        dir_brain = (BRAIN_DIR / t)
        if dir_brain.is_dir():
            return dir_brain, "dir_target"

        return None, "missing_note"

    links_out = defaultdict(set)
    links_in = defaultdict(set)
    missing_notes = defaultdict(int)
    missing_assets = defaultdict(int)
    syntax_errors = defaultdict(int)
    non_md_resolved = defaultdict(int)

    for p in md_files:
        try:
            content = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        wiki_targets = WIKI_LINK_PATTERN.findall(content)
        for t in wiki_targets:
            res, res_type = resolve(t, p)
            if res:
                if res.suffix == ".md":
                    links_out[p].add(res)
                    links_in[res].add(p)
                else:
                    non_md_resolved[str(res)] += 1
            else:
                if res_type == "missing_note":
                    missing_notes[t.strip()] += 1
                elif res_type == "missing_asset":
                    missing_assets[t.strip()] += 1
                elif res_type == "syntax_error":
                    syntax_errors[t.strip()] += 1

    orphaned_mds = [p for p in md_files if len(links_in[p]) == 0]
    dead_end_mds = [p for p in md_files if len(links_out[p]) == 0]
    isolated_mds = [p for p in md_files if len(links_in[p]) == 0 and len(links_out[p]) == 0]

    print("\n" + "="*80)
    print("ACCURATE GRAPH INTEGRITY & LINK RESOLUTION AUDIT")
    print("="*80)
    print(f"Total Markdown Files: {len(md_files)}")
    print(f"Connected Note-to-Note Links: {sum(len(v) for v in links_out.values())}")
    print(f"Valid Non-Markdown Asset References (.yaml, .json, .csv): {sum(non_md_resolved.values())}")
    print(f"Orphaned Markdown Files (0 inbound links): {len(orphaned_mds)} ({len(orphaned_mds)/len(md_files)*100:.1f}%)")
    print(f"Dead-End Markdown Files (0 outbound links): {len(dead_end_mds)} ({len(dead_end_mds)/len(md_files)*100:.1f}%)")
    print(f"Completely Isolated Markdown Files (0 in, 0 out): {len(isolated_mds)} ({len(isolated_mds)/len(md_files)*100:.1f}%)")

    print("\n" + "-"*80)
    print("BREAKDOWN OF UNRESOLVED WIKI REFERENCES")
    print("-"*80)
    print(f"1. Truly Missing Markdown Notes (Distinct): {len(missing_notes)} (Total references: {sum(missing_notes.values())})")
    print(f"2. Missing Data Assets (.yaml/.json/.csv) (Distinct): {len(missing_assets)} (Total references: {sum(missing_assets.values())})")
    print(f"3. Syntax/Regex Formatting Errors (e.g., [[:space:]]): {sum(syntax_errors.values())}")

    print("\nTOP 25 TRULY MISSING MARKDOWN NOTES:")
    for target, count in sorted(missing_notes.items(), key=lambda x: x[1], reverse=True)[:25]:
        print(f"  {count:4d}x  [[{target}]]")

    print("\nTOP 15 MISSING DATA ASSETS:")
    for target, count in sorted(missing_assets.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"  {count:4d}x  [[{target}]]")

    print("\n" + "-"*80)
    print("ISOLATED & ORPHANED CLUSTERS (Where are the disconnected files?)")
    print("-"*80)
    cluster_isolated = defaultdict(int)
    cluster_total = defaultdict(int)
    for p in md_files:
        try:
            rel = p.relative_to(BRAIN_DIR)
            c = "Brain Root" if len(rel.parts) == 1 else f"Brain/{rel.parts[0]}"
        except ValueError:
            rel = p.relative_to(COMPANY_DIR)
            c = "Company Root" if len(rel.parts) == 1 else f"Company/{rel.parts[0]}"
        cluster_total[c] += 1
        if len(links_in[p]) == 0 and len(links_out[p]) == 0:
            cluster_isolated[c] += 1

    print(f"{'Cluster':<35} | {'Total MDs':<10} | {'Isolated (0 in, 0 out)':<22} | {'Isolation %':<10}")
    print("-"*80)
    for c, tot in sorted(cluster_total.items(), key=lambda x: x[1], reverse=True)[:30]:
        iso = cluster_isolated[c]
        pct = (iso / tot) * 100 if tot else 0
        print(f"{c:<35} | {tot:<10} | {iso:<22} | {pct:>9.1f}%")

    # Venture data room specifically
    print("\n" + "-"*80)
    print("BUSINESS-CAPITAL-DATA-ROOM (VENTURES) CONNECTIVITY")
    print("-"*80)
    venture_dirs = defaultdict(lambda: {"files": 0, "in": 0, "out": 0})
    for p in md_files:
        try:
            rel = p.relative_to(BRAIN_DIR / "BUSINESS-CAPITAL-DATA-ROOM")
            if len(rel.parts) > 1:
                v_name = rel.parts[0]
                venture_dirs[v_name]["files"] += 1
                venture_dirs[v_name]["in"] += len(links_in[p])
                venture_dirs[v_name]["out"] += len(links_out[p])
        except ValueError:
            pass

    print(f"{'Venture Directory':<30} | {'Files':<6} | {'In-Links':<8} | {'Out-Links':<9}")
    print("-"*80)
    for v, st in sorted(venture_dirs.items(), key=lambda x: x[1]["files"], reverse=True)[:20]:
        print(f"{v:<30} | {st['files']:<6} | {st['in']:<8} | {st['out']:<9}")

    # The Company Root
    print("\n" + "-"*80)
    print("THE COMPANY ROOT DIRECTORY FILES")
    print("-"*80)
    for f in sorted(COMPANY_DIR.iterdir()):
        if f.name.startswith("."):
            continue
        rel = f.name
        is_dir = f.is_dir()
        size = f.stat().st_size if not is_dir else "-"
        print(f"  {'[DIR] ' if is_dir else '[FILE]'} {rel:<35} (Size: {size})")

if __name__ == "__main__":
    main()
