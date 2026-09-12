#!/usr/bin/env python3
"""
Deep Diagnostic of Company Documentation Graph & Scatter
Excludes vendor/node_modules/build artifacts. Focuses on:
1. Root Hub navigation & broken links
2. Domain folder connectivity (00-67)
3. Venture Dossiers (BUSINESS-CAPITAL-DATA-ROOM) <-> Repos <-> Root
4. The Company root folder scatter
5. Broken link root-causes and repair candidates
"""

import os
import re
import json
from collections import defaultdict
from pathlib import Path

COMPANY_DIR = Path("/Users/acebless/Documents/The Company").resolve()
BRAIN_DIR = COMPANY_DIR / "Company Brain"

WIKI_LINK_PATTERN = re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]')

EXCLUDE_PARTS = {
    "node_modules", ".git", ".venv", "dist", "build", ".next",
    ".cache", ".pytest_cache", "site-packages", "__pycache__"
}

def is_doc_file(p):
    parts = set(p.parts)
    if parts & EXCLUDE_PARTS:
        return False
    return p.suffix == ".md"

def main():
    # Scan all valid doc files
    doc_files = []
    for root, dirs, files in os.walk(COMPANY_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_PARTS]
        for f in files:
            p = Path(root) / f
            if is_doc_file(p):
                doc_files.append(p)

    print(f"Total curated documentation markdown files: {len(doc_files)}")

    # Index files
    by_stem = defaultdict(list)
    by_rel_brain = {}
    by_rel_company = {}
    for p in doc_files:
        by_stem[p.stem].append(p)
        try:
            rel_b = p.relative_to(BRAIN_DIR).as_posix().lower()
            by_rel_brain[rel_b] = p
            by_rel_brain[rel_b.replace(".md", "")] = p
        except ValueError:
            pass
        try:
            rel_c = p.relative_to(COMPANY_DIR).as_posix().lower()
            by_rel_company[rel_c] = p
            by_rel_company[rel_c.replace(".md", "")] = p
        except ValueError:
            pass

    # Target resolver
    def resolve_target(t, source):
        t = t.strip()
        if not t or t == ":space:":
            return None
        # Clean trailing backslash if any
        t_clean = t.rstrip('\\')
        
        # Direct relative
        cand = (source.parent / t_clean).resolve()
        if cand.is_file():
            return cand
        cand_md = (source.parent / f"{t_clean}.md").resolve()
        if cand_md.is_file():
            return cand_md
        
        # Rel brain / company
        t_low = t_clean.lower()
        if t_low in by_rel_brain:
            return by_rel_brain[t_low]
        if t_low in by_rel_company:
            return by_rel_company[t_low]
            
        # Stem
        if t_clean in by_stem:
            return by_stem[t_clean][0]
        # Stem lower
        for stem, paths in by_stem.items():
            if stem.lower() == t_low:
                return paths[0]
                
        # Check if it is a registry or file on disk with another extension
        disk_cand_b = BRAIN_DIR / t_clean
        if disk_cand_b.is_file() or disk_cand_b.is_dir():
            return disk_cand_b
        disk_cand_c = COMPANY_DIR / t_clean
        if disk_cand_c.is_file() or disk_cand_c.is_dir():
            return disk_cand_c

        return None

    in_links = defaultdict(set)
    out_links = defaultdict(set)
    broken = defaultdict(list)

    for p in doc_files:
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        targets = WIKI_LINK_PATTERN.findall(txt)
        for t in targets:
            res = resolve_target(t, p)
            if res:
                out_links[p].add(res)
                in_links[res].add(p)
            else:
                broken[p].append(t)

    # 1. The Company Root Analysis
    print("\n" + "="*80)
    print("1. THE COMPANY ROOT SCATTER ANALYSIS")
    print("="*80)
    company_root_items = list(COMPANY_DIR.iterdir())
    print(f"Items directly under /The Company: {len(company_root_items)}")
    for item in sorted(company_root_items):
        if item.name.startswith("."):
            continue
        is_d = item.is_dir()
        in_c = len(in_links[item])
        out_c = len(out_links[item])
        print(f"  {'[DIR] ' if is_d else '[FILE]'} {item.name:<35} | In-links: {in_c:2d} | Out-links: {out_c:2d}")

    # 2. Company Brain Root Navigation Analysis
    print("\n" + "="*80)
    print("2. CORE BRAIN HUBS & NAVIGATION STATUS")
    print("="*80)
    core_hubs = [
        "START_HERE.md", "STARTHERE.md", "README.md", "REALITY.md",
        "AGENTS.md", "SECTOR_INDEX.md", "UNIFIED_REGISTRY.md",
        "WIKI_LINK_UPDATES_REQUIRED.md", "SYSTEM-REALITY.md", "PRIORITIES.md"
    ]
    for ch in core_hubs:
        p = BRAIN_DIR / ch
        if p.exists():
            ins = len(in_links[p])
            outs = len(out_links[p])
            brk = len(broken[p])
            print(f"  {ch:<32} | In: {ins:3d} | Out: {outs:3d} | Broken: {brk:2d}")
            if brk > 0:
                print(f"    -> Broken in {ch}: {list(set(broken[p]))[:6]}")

    # 3. Domain Folders (00 through 67)
    print("\n" + "="*80)
    print("3. DOMAIN FOLDERS CONNECTIVITY (00-67)")
    print("="*80)
    domain_dirs = sorted([d for d in BRAIN_DIR.iterdir() if d.is_dir() and re.match(r'^\d{2}[-_]', d.name)])
    print(f"Total numbered domain folders: {len(domain_dirs)}")
    unlinked_domains = []
    for d in domain_dirs:
        readme = d / "README.md"
        has_readme = readme.exists()
        md_files = [f for f in d.rglob("*.md") if is_doc_file(f)]
        d_in = sum(len(in_links[f]) for f in md_files)
        d_out = sum(len(out_links[f]) for f in md_files)
        readme_in = len(in_links[readme]) if has_readme else 0
        if d_in == 0:
            unlinked_domains.append(d.name)
        status = "OK" if d_in > 0 and has_readme else ("NO README" if not has_readme else "ISLAND (0 IN)")
        print(f"  {d.name:<25} | Files: {len(md_files):2d} | Readme: {'Yes' if has_readme else 'NO '} (In: {readme_in:2d}) | Total In: {d_in:3d} | Status: {status}")

    # 4. Venture Dossiers (BUSINESS-CAPITAL-DATA-ROOM)
    print("\n" + "="*80)
    print("4. BUSINESS-CAPITAL-DATA-ROOM (VENTURES) CONNECTIVITY")
    print("="*80)
    v_root = BRAIN_DIR / "BUSINESS-CAPITAL-DATA-ROOM"
    v_dirs = sorted([d for d in v_root.iterdir() if d.is_dir() and not d.name.startswith(".")])
    for vd in v_dirs:
        v_mds = [f for f in vd.rglob("*.md") if is_doc_file(f)]
        v_in = sum(len(in_links[f]) for f in v_mds)
        v_out = sum(len(out_links[f]) for f in v_mds)
        # Check link from STARTHERE or SECTOR_INDEX
        linked_from_root = any(vd.name in (BRAIN_DIR / rf).read_text(errors='ignore') for rf in ["STARTHERE.md", "SECTOR_INDEX.md", "START_HERE.md"])
        print(f"  {vd.name:<20} | Files: {len(v_mds):2d} | Total In: {v_in:3d} | Total Out: {v_out:3d} | Linked from Root Index: {linked_from_root}")

    # 5. Top Broken Targets across all Curated Docs
    all_broken_targets = defaultdict(int)
    for p, targets in broken.items():
        for t in targets:
            all_broken_targets[t] += 1

    print("\n" + "="*80)
    print("5. TOP 25 UNRESOLVED WIKI TARGETS IN CURATED DOCS")
    print("="*80)
    for target, cnt in sorted(all_broken_targets.items(), key=lambda x: x[1], reverse=True)[:25]:
        print(f"  {cnt:3d}x  [[{target}]]")

if __name__ == "__main__":
    main()
