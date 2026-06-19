#!/usr/bin/env python3
"""
Dedup Against LightRAG — Semantic Deduplication via Supabase

Takes classified ideas, checks against Supabase/LightRAG
Only passes ideas where cosine similarity < 0.95

Usage:
    python dedup_against_lightrag.py --input ideas_classified.json --output ideas_deduped.json
"""

import json
import sys
import argparse
from typing import Dict, Any, List
from datetime import datetime

def check_duplicate(idea: Dict[str, Any]) -> tuple[bool, float]:
    """
    Check if idea already exists in LightRAG/Supabase.
    Returns (is_duplicate, similarity_score)

    TODO: Wire to Supabase semantic search on lightrag_embedding
    """
    return False, 0.0

def dedup_ideas(ideas: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Process ideas through dedup filter."""
    results = {
        "new_ideas": [],
        "duplicates": [],
        "total_processed": len(ideas),
        "processed_at": datetime.utcnow().isoformat(),
    }

    for idea in ideas:
        if idea.get("error"):
            continue

        is_dup, similarity = check_duplicate(idea)

        if is_dup:
            idea["duplicate_similarity"] = similarity
            results["duplicates"].append(idea)
        else:
            idea["passed_dedup"] = True
            results["new_ideas"].append(idea)

    results["new_ideas_count"] = len(results["new_ideas"])
    results["duplicates_count"] = len(results["duplicates"])

    return results

def main():
    parser = argparse.ArgumentParser(description="Dedup ideas against LightRAG")
    parser.add_argument("--input", type=str, required=True, help="Input JSON from extraction_agent")
    parser.add_argument("--output", type=str, help="Output JSON (default: stdout)")
    parser.add_argument("--similarity-threshold", type=float, default=0.95, help="Cosine similarity threshold")

    args = parser.parse_args()

    try:
        with open(args.input, "r") as f:
            ideas = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    ideas_list = ideas if isinstance(ideas, list) else [ideas]
    deduped = dedup_ideas(ideas_list)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(deduped, f, indent=2)
        print(f"Saved to: {args.output}", file=sys.stderr)
        print(f"New: {deduped['new_ideas_count']}, Duplicates: {deduped['duplicates_count']}", file=sys.stderr)
    else:
        print(json.dumps(deduped, indent=2))

if __name__ == "__main__":
    main()
