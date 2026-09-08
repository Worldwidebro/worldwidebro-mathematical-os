#!/usr/bin/env python3
"""
Company Brain — Master Capability Solutions Generator & Link Weaver (CAP-001 to CAP-300)
Authority: System Architecture & Capability Control Plane (CP-027)

Combines all data tiers, generates 300 standardized solution documents,
updates CAPABILITY_SOLUTION_MATRIX.json, and rebuilds CAPABILITIES_INDEX.md.
"""

import os
import json
import sys
from pathlib import Path

# Add current dir to import path
CURR_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CURR_DIR))

from data_tier1_2 import TIER_1_AND_2
from data_tier3_4 import TIER_3_AND_4
from data_tier5_6 import TIER_5_AND_6
from data_tier7_8_9 import TIER_7_8_AND_9

SOLUTIONS_DIR = CURR_DIR / "solutions"
SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)

def render_solution_markdown(cap_data) -> str:
    cid, name, category, sector, sector_title, desc, probs, sols, rels, tags = cap_data
    
    tags_str = ", ".join(f"'{t}'" for t in tags)
    probs_list = "\n".join(f"- {p}" for p in probs)
    sols_list = "\n".join(f"- **{s}**" for s in sols)
    rels_list = "\n".join(f"- [[14-CAPABILITIES/solutions/{r}|{r}]]" for r in rels)
    
    md = f"""---
id: {cid}
name: {name}
sector: {sector}
category: {category}
status: ACTIVE
updated: 2026-09-06
tags: [{tags_str}]
---

[[STARTHERE]] | [[14-CAPABILITIES/14-CAPABILITIES|14-CAPABILITIES]] | [[14-CAPABILITIES/CAPABILITIES_INDEX|CAPABILITIES_INDEX]] | [[_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml|CAPABILITY_REGISTRY]] | [[SECTORS/{sector}|{sector.split("-")[0]}-{sector.split("-")[1]}]]

# {cid}: {name}

> **Authority:** System Architecture & Capability Control Plane (CP-027)  
> **Sector:** [[SECTORS/{sector}|{sector}: {sector_title}]]  
> **Status:** ACTIVE — Audited 2026-09-06  
> **Category:** {category}

---

## 1. Overview & Scope
{desc}

---

## 2. Problem Statement
Ventures operating without `{cid}` typically encounter:
{probs_list}

---

## 3. Solution Space & Reference Tooling
Recommended tooling from internal platforms and the 904 Starred External Capability Universe:
{sols_list}

---

## 4. Implementation Path
1. **Assess**: Evaluate current venture state, data contracts, and technical debt against `{cid}` requirements.
2. **Select**: Choose appropriate tooling and integration patterns from the verified capability stack.
3. **Implement**: Deploy runtime primitives, wire configuration, and establish operational boundaries.
4. **Test**: Execute automated test harness, mutation checks, and security validation.
5. **Deploy**: Release to staging and production through standard CI/CD deployment pipelines.
6. **Observe**: Monitor telemetry, latency, error budgets, and venture business outcome metrics.

---

## 5. Sector & Venture Applications
- **Primary Sector:** [[SECTORS/{sector}|{sector_title}]]
- **Connected Venturing Portfolios:** [[AI-PROJECTS/README|AI-PROJECTS Hub]], [[23-VENTURES]]
- **Autonomous Multi-Agent Systems:** [[AI-BRAIN/README|AI-BRAIN Core]], [[16-AGENTS/README|16-AGENTS]]

---

## 6. Related Capabilities
{rels_list}
"""
    return md

def main():
    print("=" * 70)
    print("COMPANY BRAIN: BUILDING ALL 300 CAPABILITIES")
    print("=" * 70)
    
    all_caps = TIER_1_AND_2 + TIER_3_AND_4 + TIER_5_AND_6 + TIER_7_8_AND_9
    print(f"Total capability records loaded: {len(all_caps)}")
    assert len(all_caps) == 300, f"Expected exactly 300 capabilities, found {len(all_caps)}"
    
    # 1. Generate all 300 solution files
    print("\n[1/3] Generating 300 capability solution documents in solutions/...")
    matrix_dict = {}
    index_rows = []
    
    for cap in all_caps:
        cid, name, category, sector, sector_title, desc, probs, sols, rels, tags = cap
        file_path = SOLUTIONS_DIR / f"{cid}.md"
        content = render_solution_markdown(cap)
        with open(file_path, "w", encoding="utf-8") as fp:
            fp.write(content)
        
        matrix_dict[cid] = {
            "id": cid,
            "name": name,
            "category": category,
            "sector": sector,
            "sector_title": sector_title,
            "description": desc,
            "solutions": sols,
            "related": rels,
            "tags": tags,
            "status": "ACTIVE"
        }
        
        index_rows.append(
            f"| **`{cid}`** | {name} | {desc} | [[SECTORS/{sector}|{sector.split('-')[0]}-{sector.split('-')[1]}]] | [[14-CAPABILITIES/solutions/{cid}|{cid} Document]] |"
        )
    print(f"  -> Successfully generated {len(all_caps)} markdown documents.")

    # 2. Update CAPABILITY_SOLUTION_MATRIX.json
    print("\n[2/3] Writing 14-CAPABILITIES/CAPABILITY_SOLUTION_MATRIX.json...")
    matrix_file = CURR_DIR / "CAPABILITY_SOLUTION_MATRIX.json"
    with open(matrix_file, "w", encoding="utf-8") as fp:
        json.dump(matrix_dict, fp, indent=2)
    print(f"  -> Saved {len(matrix_dict)} structured capability records to {matrix_file.name}")

    # 3. Rebuild 14-CAPABILITIES/CAPABILITIES_INDEX.md
    print("\n[3/3] Rebuilding 14-CAPABILITIES/CAPABILITIES_INDEX.md...")
    index_file = CURR_DIR / "CAPABILITIES_INDEX.md"
    
    index_content = f"""---
id: DOC-CAP-INDEX-001
aliases: ["CAPABILITIES-INDEX", "Capability Solutions Index", "Canonical Capabilities Catalog"]
tags: ["capabilities", "solutions", "catalog", "matrix", "architecture"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[14-CAPABILITIES/14-CAPABILITIES|14-CAPABILITIES]] | [[14-CAPABILITIES/README|README]] | [[_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml|CAPABILITY_REGISTRY]] | [[AI-PROJECTS]]

# Canonical Capability Solutions Master Index (CAP-001 to CAP-300)

> **Authority:** System Architecture & Capability Control Plane (CP-027)  
> **Master Registries:**
> - [[14-CAPABILITIES/CAPABILITY_SOLUTION_MATRIX.json|CAPABILITY_SOLUTION_MATRIX.json]]
> - [[_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml|CANONICAL CAPABILITY_REGISTRY.yaml]]
> - [[_REGISTRIES/CANONICAL/CAPABILITY_GAP_MATRIX.yaml|CAPABILITY_GAP_MATRIX.yaml]]
> - [[_REGISTRIES/CANONICAL/CAPABILITY_GAP_REPORT.yaml|CAPABILITY_GAP_REPORT.yaml]]
> - [[_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml|EXTERNAL_CAPABILITY_UNIVERSE.yaml]]
> - [[_INFRASTRUCTURE/STARRED_REPOS_CAPABILITY_PHASES|STARRED_REPOS_CAPABILITY_PHASES.md]]
> - [[_TEMPLATES/Capability|Capability Template]]

---

## 1. Capability Portfolio Overview
This catalog indexes all **300 modular capability solutions** supporting Company Brain corporate operations, autonomous software ventures, and infrastructure pipelines. Every capability is fully specified with standardized frontmatter, problem definitions, reference solutions from the 904 Starred External Universe, implementation paths, and bidirectional wikilinks.

---

## 2. Capability Tier Breakdown
1. **Tier 1 (`CAP-001` - `CAP-035`):** Core Architecture & Platform Engineering (35 Capabilities)
2. **Tier 2 (`CAP-036` - `CAP-070`):** Data Engineering & Knowledge Systems (35 Capabilities)
3. **Tier 3 (`CAP-071` - `CAP-105`):** Autonomous Agents & AI Reasoning (35 Capabilities)
4. **Tier 4 (`CAP-106` - `CAP-140`):** Software Engineering & Delivery (35 Capabilities)
5. **Tier 5 (`CAP-141` - `CAP-175`):** Cybersecurity & Zero Trust Architecture (35 Capabilities)
6. **Tier 6 (`CAP-176` - `CAP-210`):** FinTech, Commerce & Monetization (35 Capabilities)
7. **Tier 7 (`CAP-211` - `CAP-240`):** Operations, Supply Chain & Logistics (30 Capabilities)
8. **Tier 8 (`CAP-241` - `CAP-275`):** Sector Verticals & Specialized Domains (35 Capabilities)
9. **Tier 9 (`CAP-276` - `CAP-300`):** Corporate Governance, Strategy & Execution (25 Capabilities)

---

## 3. Complete Capability Inventory (CAP-001 to CAP-300)

| Capability ID | Capability Name | Description / Scope | Primary Sector Anchor | Solution Specification |
|---|---|---|---|---|
""" + "\n".join(index_rows) + "\n"

    with open(index_file, "w", encoding="utf-8") as fp:
        fp.write(index_content)
    print(f"  -> Rebuilt {index_file.name} with 300 fully specified rows.")
    
    print("\n" + "=" * 70)
    print("SUCCESS: 300 CAPABILITY NODES COMPILED AND LINKED")
    print("=" * 70)

if __name__ == "__main__":
    main()
