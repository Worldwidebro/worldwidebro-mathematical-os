#!/usr/bin/env python3
"""
Audit Wiki Links, Broken Targets, and Isolated Files across:
1. /Users/acebless/Documents/The Company
2. /Users/acebless/Documents/The Company/Company Brain
"""

import os
import re
import json
from collections import defaultdict
from pathlib import Path

COMPANY_DIR = Path("/Users/acebless/Documents/The Company").resolve()
BRAIN_DIR = COMPANY_DIR / "Company Brain"

WIKI_LINK_PATTERN = re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]')
MD_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

EXCLUDE_DIRS = {
    ".git", ".venv", "node_modules", "dist", "build", "__pycache__",
    ".cache", ".pytest_cache", ".ruff_cache", "site-packages"
}

def scan_files(base_dir):
    md_files = []
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".tmp")]
        for file in files:
            if file.endswith(".md"):
                full_path = Path(root) / file
                md_files.append(full_path)
    return md_files

def main():
    print(f"Scanning markdown files in:\n  1. {COMPANY_DIR}\n  2. {BRAIN_DIR}")
    all_files = scan_files(COMPANY_DIR)
    print(f"Total markdown files found: {len(all_files)}")

    file_by_stem = defaultdict(list)
    file_by_stem_lower = defaultdict(list)
    file_by_name = defaultdict(list)
    file_by_rel_company = {}
    file_by_rel_brain = {}

    for p in all_files:
        stem = p.stem
        name = p.name
        file_by_stem[stem].append(p)
        file_by_stem_lower[stem.lower()].append(p)
        file_by_name[name.lower()].append(p)

        try:
            rel_c = p.relative_to(COMPANY_DIR).as_posix()
            file_by_rel_company[rel_c.lower()] = p
            file_by_rel_company[rel_c.lower().replace(".md", "")] = p
        except ValueError:
            pass

        try:
            rel_b = p.relative_to(BRAIN_DIR).as_posix()
            file_by_rel_brain[rel_b.lower()] = p
            file_by_rel_brain[rel_b.lower().replace(".md", "")] = p
        except ValueError:
            pass

    def resolve_target(target_str, source_file):
        target_clean = target_str.strip()
        if not target_clean:
            return None

        source_dir = source_file.parent
        direct_rel = (source_dir / target_clean).resolve()
        if direct_rel.is_file():
            return direct_rel
        direct_rel_md = (source_dir / f"{target_clean}.md").resolve()
        if direct_rel_md.is_file():
            return direct_rel_md

        target_lower = target_clean.lower()
        if target_lower in file_by_rel_brain:
            return file_by_rel_brain[target_lower]
        if target_lower in file_by_rel_company:
            return file_by_rel_company[target_lower]

        if target_clean in file_by_stem:
            return file_by_stem[target_clean][0]
        if target_lower in file_by_stem_lower:
            return file_by_stem_lower[target_lower][0]

        if target_lower in file_by_name:
            return file_by_name[target_lower][0]
        if f"{target_lower}.md" in file_by_name:
            return file_by_name[f"{target_lower}.md"][0]

        return None

    links_out = defaultdict(set)
    links_in = defaultdict(set)
    broken_links = defaultdict(list)
    broken_target_counts = defaultdict(int)

    company_root_mds = []
    brain_root_mds = []

    for p in all_files:
        if p.parent == COMPANY_DIR:
            company_root_mds.append(p)
        elif p.parent == BRAIN_DIR:
            brain_root_mds.append(p)

        try:
            content = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        wiki_targets = WIKI_LINK_PATTERN.findall(content)
        for t in wiki_targets:
            t_clean = t.strip()
            if not t_clean:
                continue
            resolved = resolve_target(t_clean, p)
            if resolved:
                links_out[p].add(resolved)
                links_in[resolved].add(p)
            else:
                broken_links[p].append(t_clean)
                broken_target_counts[t_clean] += 1

    orphans_no_in = [p for p in all_files if len(links_in[p]) == 0]
    dead_ends_no_out = [p for p in all_files if len(links_out[p]) == 0]
    isolated = [p for p in all_files if len(links_in[p]) == 0 and len(links_out[p]) == 0]

    cluster_stats = defaultdict(lambda: {"files": 0, "in_links": 0, "out_links": 0, "broken_links": 0})
    
    def get_cluster(p):
        try:
            rel = p.relative_to(BRAIN_DIR)
            parts = rel.parts
            if len(parts) == 1:
                return "Brain Root"
            return f"Brain/{parts[0]}"
        except ValueError:
            try:
                rel = p.relative_to(COMPANY_DIR)
                parts = rel.parts
                if len(parts) == 1:
                    return "Company Root"
                return f"Company/{parts[0]}"
            except ValueError:
                return "External"

    for p in all_files:
        c = get_cluster(p)
        cluster_stats[c]["files"] += 1
        cluster_stats[c]["in_links"] += len(links_in[p])
        cluster_stats[c]["out_links"] += len(links_out[p])
        cluster_stats[c]["broken_links"] += len(broken_links[p])

    print("\n" + "="*80)
    print("GRAPH INTEGRITY & SCATTER AUDIT REPORT")
    print("="*80)
    print(f"Total Markdown Files: {len(all_files)}")
    print(f"Total Connected Links (Edges): {sum(len(v) for v in links_out.values())}")
    print(f"Files with NO Inbound Links (Orphans): {len(orphans_no_in)} ({len(orphans_no_in)/len(all_files)*100:.1f}%)")
    print(f"Files with NO Outbound Links (Dead Ends): {len(dead_ends_no_out)} ({len(dead_ends_no_out)/len(all_files)*100:.1f}%)")
    print(f"Files Completely Isolated (0 in, 0 out): {len(isolated)} ({len(isolated)/len(all_files)*100:.1f}%)")
    print(f"Total Broken Wiki Link Occurrences: {sum(len(v) for v in broken_links.values())}")
    print(f"Distinct Missing Targets: {len(broken_target_counts)}")

    print("\n" + "-"*80)
    print("TOP 30 MOST FREQUENTLY REQUESTED MISSING WIKI TARGETS")
    print("-"*80)
    sorted_broken = sorted(broken_target_counts.items(), key=lambda x: x[1], reverse=True)[:30]
    for target, count in sorted_broken:
        print(f"{count:4d}x  [[{target}]]")

    print("\n" + "-"*80)
    print("TOP 35 CLUSTERS / DIRECTORIES BY FILE COUNT")
    print("-"*80)
    print(f"{'Cluster':<35} | {'Files':<6} | {'In-Links':<8} | {'Out-Links':<9} | {'Broken':<6}")
    print("-"*80)
    for cluster, stats in sorted(cluster_stats.items(), key=lambda x: x[1]["files"], reverse=True)[:35]:
        print(f"{cluster:<35} | {stats['files']:<6} | {stats['in_links']:<8} | {stats['out_links']:<9} | {stats['broken_links']:<6}")

    print("\n" + "-"*80)
    print("THE COMPANY ROOT FILES (Outside Company Brain)")
    print("-"*80)
    for p in sorted(company_root_mds):
        rel = p.relative_to(COMPANY_DIR).as_posix()
        ins = len(links_in[p])
        outs = len(links_out[p])
        brok = len(broken_links[p])
        print(f"  {rel:<35} | In: {ins:2d} | Out: {outs:2d} | Broken: {brok:2d}")

    print("\n" + "-"*80)
    print("KEY BRAIN ROOT FILES")
    print("-"*80)
    key_roots = ["START_HERE.md", "STARTHERE.md", "README.md", "REALITY.md", "AGENTS.md", "SECTOR_INDEX.md", "UNIFIED_REGISTRY.md", "WIKI_LINK_UPDATES_REQUIRED.md"]
    for kr in key_roots:
        p = BRAIN_DIR / kr
        if p.exists():
            ins = len(links_in[p])
            outs = len(links_out[p])
            brok = len(broken_links[p])
            print(f"  {kr:<30} | In: {ins:3d} | Out: {outs:3d} | Broken: {brok:2d}")
            if brok > 0:
                print(f"    -> Top broken in {kr}: {broken_links[p][:5]}")

    report_json = {
        "total_files": len(all_files),
        "total_edges": sum(len(v) for v in links_out.values()),
        "orphan_count": len(orphans_no_in),
        "dead_end_count": len(dead_ends_no_out),
        "isolated_count": len(isolated),
        "top_missing_targets": sorted_broken,
        "clusters": {c: s for c, s in sorted(cluster_stats.items(), key=lambda x: x[1]['files'], reverse=True)},
        "top_broken_files": [
            {"file": str(k.relative_to(COMPANY_DIR)), "broken_count": len(v), "examples": v[:5]}
            for k, v in sorted(broken_links.items(), key=lambda x: len(x[1]), reverse=True)[:30]
        ]
    }

    out_file = BRAIN_DIR / "scripts" / "graph_audit_result.json"
    out_file.write_text(json.dumps(report_json, indent=2))
    print(f"\nDetailed JSON report written to: {out_file}")

if __name__ == "__main__":
    main()
