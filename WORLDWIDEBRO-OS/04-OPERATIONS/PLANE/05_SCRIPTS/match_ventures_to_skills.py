#!/usr/bin/env python3
"""
Venture-to-Skills Matching Engine — Phase 2b
Match ventures to recommended SkillsLLM skills based on sector type.

Usage:
  python3 match_ventures_to_skills.py [--ventures IDS] [--dry-run] [--batch-size N]
"""

import os
import sys
from datetime import datetime
from typing import List, Dict, Optional

from dotenv import load_dotenv
from supabase import create_client


# Mapping: Sector → Preferred Skill Categories
SECTOR_SKILL_MAPPING = {
    "COMM": ["AI Agents", "Code Generation", "CLI Tools"],
    "BW": ["AI Agents", "MCP Servers"],
    "CONS": ["AI Agents", "Code Generation"],
    "TECH": ["CLI Tools", "DevOps", "Code Generation"],
    "FINANCE": ["AI Agents", "Code Generation"],
    "HEALTH": ["AI Agents", "Code Generation"],
    "EDU": ["Code Generation", "AI Agents"],
    "MEDIA": ["Code Generation", "AI Agents"],
}


def get_supabase_client():
    """Initialize Supabase client"""
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY required in .env")
    return create_client(url, key)


def get_ventures(supabase, venture_ids: Optional[List[int]] = None) -> List[dict]:
    """Fetch ventures from Supabase"""
    try:
        query = supabase.table("ventures").select("id,sector,name")
        if venture_ids:
            query = query.in_("id", venture_ids)
        result = query.execute()
        return result.data or []
    except Exception as e:
        print(f"[ERROR] Failed to fetch ventures: {e}")
        return []


def get_skills_by_category(supabase, category: str) -> List[dict]:
    """Fetch skills matching a category"""
    try:
        result = supabase.table("skills").select("id,name,category").eq("category", category).execute()
        return result.data or []
    except Exception as e:
        print(f"[ERROR] Failed to fetch skills for {category}: {e}")
        return []


def match_venture_to_skills(supabase, venture: dict) -> List[Dict]:
    """Match a venture to recommended skills based on sector"""
    venture_id = venture["id"]
    sector = venture.get("sector", "UNKNOWN")

    preferred_categories = SECTOR_SKILL_MAPPING.get(sector, ["AI Agents"])

    recommendations = []

    # Rule-based matching: find skills in preferred categories
    for i, category in enumerate(preferred_categories):
        skills = get_skills_by_category(supabase, category)

        # Higher relevance for earlier categories
        relevance = 1.0 - (i * 0.2)

        for skill in skills[:5]:  # Top 5 per category
            recommendations.append({
                "venture_id": venture_id,
                "skill_id": skill["id"],
                "relevance_score": relevance,
                "recommended_by": "rules",
            })

    print(f"[Match] Venture {venture_id} ({sector}): {len(recommendations)} skills")
    return recommendations


def insert_venture_skills_batch(supabase, recommendations: List[Dict], dry_run: bool = False) -> int:
    """Batch insert venture-skill relationships"""
    if not recommendations:
        return 0

    if dry_run:
        print(f"[DRY-RUN] {len(recommendations)} relationships to insert")
        return len(recommendations)

    try:
        result = supabase.table("venture_skills").upsert(
            recommendations, on_conflict="venture_id,skill_id"
        ).execute()
        inserted = len(result.data) if result.data else 0
        print(f"[DB] Inserted {inserted}")
        return inserted
    except Exception as e:
        print(f"[ERROR] Insert failed: {e}")
        return 0


def main(venture_ids: Optional[str] = None, dry_run: bool = False, batch_size: int = 100):
    """Main matching engine"""

    try:
        supabase = get_supabase_client()
    except ValueError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

    # Parse venture IDs if provided
    parsed_ids = None
    if venture_ids:
        try:
            parsed_ids = [int(v.strip()) for v in venture_ids.split(",")]
        except ValueError:
            print("[ERROR] Invalid venture IDs")
            sys.exit(1)

    print(f"""
    ========================================
    Venture-Skills Matching — Phase 2b
    ========================================
    Started: {datetime.utcnow().isoformat()}
    Ventures: {parsed_ids if parsed_ids else "all"}
    Dry run: {dry_run}
    """)

    ventures = get_ventures(supabase, parsed_ids)
    if not ventures:
        print("[ERROR] No ventures found")
        sys.exit(1)

    print(f"[Info] Matching {len(ventures)} ventures...")

    total_recommendations = 0
    batch = []

    for venture in ventures:
        recommendations = match_venture_to_skills(supabase, venture)
        batch.extend(recommendations)

        if len(batch) >= batch_size:
            inserted = insert_venture_skills_batch(supabase, batch, dry_run=dry_run)
            total_recommendations += inserted
            batch = []

    if batch:
        inserted = insert_venture_skills_batch(supabase, batch, dry_run=dry_run)
        total_recommendations += inserted

    print(f"""
    ========================================
    Matching Complete
    ========================================
    Total recommendations: {total_recommendations}
    Ended: {datetime.utcnow().isoformat()}
    """)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Match ventures to skills")
    parser.add_argument("--ventures", type=str, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--batch-size", type=int, default=100)

    args = parser.parse_args()
    main(venture_ids=args.ventures, dry_run=args.dry_run, batch_size=args.batch_size)
