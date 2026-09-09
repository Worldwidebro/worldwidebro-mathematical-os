#!/usr/bin/env python3
"""
Link Healer: Auto-heal 3,928 dead wiki links via Ollama + OmniRoute.

Strategy:
1. Extract dead links from audit
2. For each dead link: use Ollama to understand context + find target
3. Route batch fixes through OmniRoute
4. Apply via open-knowledge MCP
"""

import json
import subprocess
import re
from pathlib import Path
from typing import Optional
import requests

# Config
OMNIROUTE_URL = "http://localhost:20128"
OLLAMA_URL = "http://localhost:11434"
COMPANY_BRAIN = Path("/Users/acebless/Documents/The Company/Company Brain")
DEAD_LINKS_REPORT = Path.home() / ".claude/projects/-Users-acebless-Documents/1af0cccb-0453-421c-b851-d47c565fdd83/tool-results/mcp-open-knowledge-links-1788914004280.txt"
OUTPUT_FILE = COMPANY_BRAIN / "_SCRIPTS/LINK_HEALING_PLAN.json"

def load_dead_links():
    """Load dead links from audit report."""
    with open(DEAD_LINKS_REPORT) as f:
        data = json.load(f)
    return data.get("deadLinks", [])

def find_candidate_docs(target: str) -> list:
    """Find all docs in Company Brain that could be the target."""
    candidates = []

    # Extract the final segment (e.g., "CAPABILITIES_INDEX" from "14-CAPABILITIES/CAPABILITIES_INDEX")
    target_name = target.split("/")[-1]

    # Search filesystem for matching docs
    for md_file in COMPANY_BRAIN.rglob("*.md"):
        # Match by filename (with or without .md)
        if target_name in md_file.stem or md_file.stem == target_name:
            candidates.append({
                "path": str(md_file.relative_to(COMPANY_BRAIN)),
                "stem": md_file.stem,
                "score": 100 if md_file.stem == target_name else 50
            })

    return sorted(candidates, key=lambda x: x["score"], reverse=True)

def query_ollama_for_resolution(target: str, sources: list, candidates: list) -> dict:
    """Use Ollama to determine the best link target."""

    # Build context from sources
    source_snippets = "\n".join([
        f"- {s['source']}: {s['snippet']}"
        for s in sources[:3]  # First 3 sources for context
    ])

    candidate_list = "\n".join([
        f"- {c['path']} (match score: {c['score']})"
        for c in candidates[:5]  # Top 5 candidates
    ])

    prompt = f"""You are a knowledge graph healer. A wiki link is broken:

BROKEN LINK: [[{target}]]

SOURCES (docs that reference it):
{source_snippets}

CANDIDATE TARGETS (matching docs found):
{candidate_list}

Choose the BEST match or suggest creating a NEW doc. Return JSON:
{{
  "action": "fix" | "create" | "delete",
  "target": "path/to/target.md" (if fix),
  "reason": "why this is the right choice"
}}

Be decisive. If candidates exist, choose the best one. If none fit, suggest creating a doc.
"""

    try:
        resp = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": "qwen2.5-coder",
                "prompt": prompt,
                "stream": False,
            },
            timeout=30
        )
        if resp.status_code == 200:
            output = resp.json()["response"]
            # Extract JSON from response
            match = re.search(r'\{.*\}', output, re.DOTALL)
            if match:
                return json.loads(match.group())
    except Exception as e:
        print(f"⚠️ Ollama error for {target}: {e}")

    # Fallback: pick best candidate
    if candidates:
        return {
            "action": "fix",
            "target": candidates[0]["path"],
            "reason": "Best filesystem match (fallback)"
        }

    return {
        "action": "skip",
        "reason": "No candidates found, manual review needed"
    }

def build_healing_plan():
    """Build complete healing plan for all dead links."""
    dead_links = load_dead_links()
    plan = {
        "total_dead_links": len(dead_links),
        "to_fix": [],
        "to_create": [],
        "to_delete": [],
        "to_review": [],
        "stats": {"fixed": 0, "created": 0, "deleted": 0, "skipped": 0}
    }

    for i, link_group in enumerate(dead_links):
        target = link_group["target"]
        sources = link_group["sources"]

        print(f"\n[{i+1}/{len(dead_links)}] Healing: {target}")
        print(f"  Found in {len(sources)} docs")

        # Find candidates
        candidates = find_candidate_docs(target)
        print(f"  Candidates: {len(candidates)}")

        # Query Ollama
        resolution = query_ollama_for_resolution(target, sources, candidates)

        # Add to plan
        item = {
            "broken_link": target,
            "num_sources": len(sources),
            "action": resolution["action"],
            "target": resolution.get("target"),
            "reason": resolution.get("reason"),
            "sources_sample": [s["source"] for s in sources[:2]]
        }

        if resolution["action"] == "fix":
            plan["to_fix"].append(item)
            plan["stats"]["fixed"] += 1
        elif resolution["action"] == "create":
            plan["to_create"].append(item)
            plan["stats"]["created"] += 1
        elif resolution["action"] == "delete":
            plan["to_delete"].append(item)
            plan["stats"]["deleted"] += 1
        else:
            plan["to_review"].append(item)
            plan["stats"]["skipped"] += 1

    return plan

def save_plan(plan):
    """Save healing plan to file."""
    with open(OUTPUT_FILE, "w") as f:
        json.dump(plan, f, indent=2)
    print(f"\n✅ Healing plan saved to {OUTPUT_FILE}")
    print(f"\nPlan Summary:")
    print(f"  🔧 To Fix: {plan['stats']['fixed']}")
    print(f"  ✨ To Create: {plan['stats']['created']}")
    print(f"  🗑️  To Delete: {plan['stats']['deleted']}")
    print(f"  📋 To Review: {plan['stats']['skipped']}")

if __name__ == "__main__":
    print("🔗 Link Healer — Ollama + OmniRoute")
    print(f"Processing {len(load_dead_links())} dead links...\n")

    plan = build_healing_plan()
    save_plan(plan)
