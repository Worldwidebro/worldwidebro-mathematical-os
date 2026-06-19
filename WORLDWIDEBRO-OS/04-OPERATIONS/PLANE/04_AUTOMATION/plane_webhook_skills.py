#!/usr/bin/env python3
"""
Plane Webhook Integration — Phase 3
Wire SkillsLLM skill recommendations into Plane custom fields.

Usage:
  python3 plane_webhook_skills.py [--ventures IDS] [--dry-run]

Requirements:
  - PLANE_API_KEY in .env
  - PLANE_WORKSPACE_ID in .env
  - venture_skills table populated by Phase 2b
"""

import os
import sys
import json
from datetime import datetime
from typing import List, Dict, Optional

import requests
from dotenv import load_dotenv
from supabase import create_client


def get_clients():
    """Initialize Supabase and Plane clients"""
    load_dotenv()

    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    plane_api_key = os.getenv("PLANE_API_KEY")
    plane_base_url = os.getenv("PLANE_API_BASE_URL", "https://api.plane.so/api/v1")

    if not supabase_url or not supabase_key:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY required in .env")
    if not plane_api_key:
        raise ValueError("PLANE_API_KEY required in .env")

    supabase = create_client(supabase_url, supabase_key)
    return supabase, plane_api_key, plane_base_url


def get_venture_skills(supabase, venture_ids: Optional[List[int]] = None) -> Dict[int, List[dict]]:
    """Fetch venture-to-skills mappings from Supabase"""
    try:
        query = supabase.table("venture_skills").select(
            "venture_id,skill_id,relevance_score,skills(name,category)"
        )

        if venture_ids:
            query = query.in_("venture_id", venture_ids)

        result = query.execute()

        venture_skills_map = {}
        for row in result.data or []:
            venture_id = row["venture_id"]
            skill = {
                "skill_id": row["skill_id"],
                "name": row["skills"]["name"],
                "category": row["skills"]["category"],
                "relevance_score": row["relevance_score"],
            }

            if venture_id not in venture_skills_map:
                venture_skills_map[venture_id] = []

            venture_skills_map[venture_id].append(skill)

        return venture_skills_map

    except Exception as e:
        print(f"[ERROR] Failed to fetch venture skills: {e}")
        return {}


def get_venture_plane_id(supabase, venture_id: int) -> Optional[str]:
    """Get Plane project ID for a venture"""
    try:
        result = supabase.table("ventures").select("id,plane_project_id").eq("id", venture_id).single().execute()

        if result.data and result.data.get("plane_project_id"):
            return result.data["plane_project_id"]

        return str(venture_id)

    except Exception as e:
        print(f"[WARN] Could not get Plane ID for venture {venture_id}: {e}")
        return str(venture_id)


def update_venture_skills_in_plane(
    plane_api_key: str,
    plane_base_url: str,
    workspace_id: str,
    project_id: str,
    skills: List[dict],
    dry_run: bool = False
) -> bool:
    """Update Plane project's 'Recommended Skills' custom field"""

    if dry_run:
        print(f"[DRY-RUN] Would update Plane project {project_id} with {len(skills)} skills")
        return True

    headers = {
        "Authorization": f"Bearer {plane_api_key}",
        "Content-Type": "application/json"
    }

    # Format skills for Plane (top 10 by relevance)
    skills_data = [
        {"name": s["name"], "category": s["category"], "score": s["relevance_score"]}
        for s in sorted(skills, key=lambda x: x["relevance_score"], reverse=True)[:10]
    ]

    try:
        # Update custom field via Plane API
        url = f"{plane_base_url}/workspaces/{workspace_id}/projects/{project_id}/custom-fields"

        payload = {"recommended_skills": json.dumps(skills_data)}

        response = requests.patch(url, json=payload, headers=headers, timeout=10)

        if response.status_code in [200, 201]:
            print(f"[Plane] Updated project {project_id}: {len(skills)} skills")
            return True
        else:
            print(f"[ERROR] Plane API: {response.status_code}")
            return False

    except Exception as e:
        print(f"[ERROR] Failed to update Plane: {e}")
        return False


def main(venture_ids: Optional[str] = None, workspace_id: Optional[str] = None, dry_run: bool = False):
    """Main webhook integration"""

    try:
        supabase, plane_api_key, plane_base_url = get_clients()
    except ValueError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

    parsed_ids = None
    if venture_ids:
        try:
            parsed_ids = [int(v.strip()) for v in venture_ids.split(",")]
        except ValueError:
            print("[ERROR] Invalid venture IDs")
            sys.exit(1)

    if not workspace_id:
        workspace_id = os.getenv("PLANE_WORKSPACE_ID")
        if not workspace_id:
            print("[ERROR] PLANE_WORKSPACE_ID required in .env")
            sys.exit(1)

    print(f"""
    ========================================
    Plane Webhook Integration — Phase 3
    ========================================
    Started: {datetime.utcnow().isoformat()}
    Ventures: {parsed_ids if parsed_ids else "all"}
    Dry run: {dry_run}
    """)

    venture_skills_map = get_venture_skills(supabase, parsed_ids)

    if not venture_skills_map:
        print("[ERROR] No venture-skills mappings found")
        sys.exit(1)

    print(f"[Info] Updating {len(venture_skills_map)} ventures in Plane...")

    updated = 0
    for venture_id, skills in venture_skills_map.items():
        project_id = get_venture_plane_id(supabase, venture_id)

        success = update_venture_skills_in_plane(
            plane_api_key,
            plane_base_url,
            workspace_id,
            project_id,
            skills,
            dry_run=dry_run
        )

        if success:
            updated += 1

    print(f"""
    ========================================
    Webhook Integration Complete
    ========================================
    Ventures updated: {updated}/{len(venture_skills_map)}
    Ended: {datetime.utcnow().isoformat()}
    """)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Wire skills to Plane custom fields")
    parser.add_argument("--ventures", type=str, default=None)
    parser.add_argument("--workspace-id", type=str, default=None)
    parser.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()
    main(venture_ids=args.ventures, workspace_id=args.workspace_id, dry_run=args.dry_run)
