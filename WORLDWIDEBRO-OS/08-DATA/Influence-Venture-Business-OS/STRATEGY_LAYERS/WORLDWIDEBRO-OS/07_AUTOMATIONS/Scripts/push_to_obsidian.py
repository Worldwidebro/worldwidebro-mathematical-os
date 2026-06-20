#!/usr/bin/env python3
"""
Push to Obsidian — Convert Deduped Ideas to Atomic Notes

Takes deduped ideas, creates markdown atomic notes in real Obsidian vault (CloudDocs)
Also returns JSON for Supabase ingestion

Usage:
    python push_to_obsidian.py --input ideas_deduped.json --supabase-output supabase_batch.json
    (Vault auto-detected from CloudDocs path)
"""

import json
import sys
import argparse
import re
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List

def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[-\s]+", "-", slug)
    return slug[:50]

def create_markdown_note(idea: Dict[str, Any], note_id: str) -> str:
    """Create markdown atomic note from idea."""
    frontmatter = {
        "id": note_id,
        "source": "instagram",
        "category": idea.get("category", ""),
        "venture_type": idea.get("venture_type_primary", ""),
        "confidence": idea.get("confidence", 0),
        "deal_flow_stage": idea.get("deal_flow_stage", "idea"),
        "created_at": datetime.utcnow().isoformat(),
        "tags": [idea.get("category", ""), idea.get("venture_type_primary", "")],
    }

    frontmatter_str = "---\n"
    for key, value in frontmatter.items():
        if isinstance(value, list):
            frontmatter_str += f"{key}: {json.dumps(value)}\n"
        else:
            frontmatter_str += f"{key}: {value}\n"
    frontmatter_str += "---\n\n"

    body = f"""# {idea.get('idea_text', 'Untitled')[:80]}

## Overview
{idea.get('idea_text', '')}

## Details
- **Category**: {idea.get('category', '')}
- **Venture Type**: {idea.get('venture_type_primary', '')}
- **Confidence**: {idea.get('confidence', 0):.1%}
- **Deal Flow**: {idea.get('deal_flow_stage', '')}

## Entities
- **People**: {', '.join(idea.get('people_mentioned', [])) or 'None'}
- **Tools**: {', '.join(idea.get('tools_mentioned', [])) or 'None'}
- **Monetization**: {idea.get('monetization_angle', 'Not identified')}

## Routing
- **Agents**: {', '.join(idea.get('routable_agents', [])) or 'None'}
- **Next Action**: {idea.get('next_action', 'research')}

## Source
- Processed: {idea.get('processed_at', '')}
- File: {idea.get('source_file', '')}
"""

    return frontmatter_str + body

def push_to_obsidian(ideas: List[Dict[str, Any]], vault_path: str = None) -> List[str]:
    """Write atomic notes to Obsidian vault."""
    if vault_path is None:
        vault_path = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault")

    vault = Path(vault_path)
    if not vault.exists():
        print(f"Vault not found at {vault_path}", file=sys.stderr)
        sys.exit(1)

    ideas_dir = vault / "Instagram_Ideas"
    ideas_dir.mkdir(parents=True, exist_ok=True)

    note_ids = []

    for idea in ideas:
        if idea.get("error") or not idea.get("passed_dedup"):
            continue

        slug = slugify(idea.get("idea_text", "idea")[:60])
        date_str = datetime.utcnow().strftime("%Y-%m-%d")
        note_id = f"{date_str}-{slug}"
        note_path = ideas_dir / f"{note_id}.md"

        markdown = create_markdown_note(idea, note_id)
        with open(note_path, "w") as f:
            f.write(markdown)

        idea["obsidian_note_id"] = note_id
        note_ids.append(note_id)

    return note_ids

def prepare_for_supabase(ideas: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Prepare ideas for Supabase ingestion."""
    supabase_records = []

    for idea in ideas:
        if idea.get("error") or not idea.get("passed_dedup"):
            continue

        record = {
            "source": "instagram",
            "source_url": idea.get("source_file", ""),
            "screenshot_path": idea.get("source_file", ""),
            "idea_text": idea.get("idea_text", ""),
            "category": idea.get("category", ""),
            "extracted_by": idea.get("extracted_by", ""),
            "people_mentioned": idea.get("people_mentioned", []),
            "tools_mentioned": idea.get("tools_mentioned", []),
            "monetization_angle": idea.get("monetization_angle"),
            "confidence": idea.get("confidence", 0),
            "created_at": datetime.utcnow().isoformat(),
            "obsidian_note_id": idea.get("obsidian_note_id", ""),
            "venture_type": idea.get("venture_type_primary", ""),
            "deal_flow_stage": idea.get("deal_flow_stage", ""),
        }
        supabase_records.append(record)

    return supabase_records

def main():
    parser = argparse.ArgumentParser(description="Push ideas to Obsidian + prepare for Supabase")
    parser.add_argument("--input", type=str, required=True, help="Input JSON from dedup")
    parser.add_argument("--obsidian-vault", type=str, default=None, help="Path to Obsidian vault (auto-detected from CloudDocs if not specified)")
    parser.add_argument("--supabase-output", type=str, help="Output JSON for Supabase")

    args = parser.parse_args()

    try:
        with open(args.input, "r") as f:
            dedup_result = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    ideas = dedup_result.get("new_ideas", []) if isinstance(dedup_result, dict) else dedup_result

    print(f"Pushing {len(ideas)} ideas to Obsidian...", file=sys.stderr)
    note_ids = push_to_obsidian(ideas, args.obsidian_vault or None)

    supabase_records = prepare_for_supabase(ideas)

    if args.supabase_output:
        with open(args.supabase_output, "w") as f:
            json.dump(supabase_records, f, indent=2)
        print(f"Saved to: {args.supabase_output}", file=sys.stderr)

    print(f"✅ Done: {len(note_ids)} notes, {len(supabase_records)} records", file=sys.stderr)

if __name__ == "__main__":
    main()
