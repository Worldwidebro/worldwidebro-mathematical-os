#!/usr/bin/env python3
"""
Test/Dry-run version of Supabase → Notion sync
Shows what would sync without needing real credentials
"""

import json
from datetime import datetime

# Sample venture data (from Supabase schema)
SAMPLE_VENTURES = [
    {
        "venture_id": "v-001",
        "name": "HRMS Payroll SaaS",
        "status": "active",
        "stage": "mvp",
        "sector": "HR Tech",
        "revenue_ytd": 3500,
        "costs_mom": 1200,
        "owner_id": "team-payroll",
        "business_model": "B2B SaaS"
    },
    {
        "venture_id": "v-002",
        "name": "Lash Extension Studio",
        "status": "validation",
        "stage": "pre-launch",
        "sector": "Beauty",
        "revenue_ytd": 0,
        "costs_mom": 500,
        "owner_id": "team-beauty",
        "business_model": "B2C Marketplace"
    },
    {
        "venture_id": "v-003",
        "name": "Construction AI Tools",
        "status": "idea",
        "stage": "pre-launch",
        "sector": "Construction",
        "revenue_ytd": 0,
        "costs_mom": 0,
        "owner_id": "team-construction",
        "business_model": "B2B SaaS"
    }
]

SAMPLE_LOOP_LOGS = [
    {
        "execution_id": "loop-001",
        "venture_id": "v-001",
        "loop_type": "launch",
        "status": "completed",
        "progress_pct": 100,
        "started_at": "2026-06-10T08:00:00Z",
        "completed_at": "2026-06-11T16:30:00Z"
    },
    {
        "execution_id": "loop-002",
        "venture_id": "v-002",
        "loop_type": "validation",
        "status": "in_progress",
        "progress_pct": 45,
        "started_at": "2026-06-11T09:00:00Z",
        "completed_at": None
    }
]

SAMPLE_HEALTH_SCORES = [
    {
        "venture_id": "v-001",
        "health_score": 8.5,
        "readiness_stage": "Scale",
        "mRR": 3500,
        "cAC_ltv_ratio": 0.95,
        "last_updated": "2026-06-11T12:00:00Z"
    },
    {
        "venture_id": "v-002",
        "health_score": 4.2,
        "readiness_stage": "MVP",
        "mRR": 0,
        "cAC_ltv_ratio": 0.0,
        "last_updated": "2026-06-11T12:00:00Z"
    }
]

def map_status(supabase_status):
    status_map = {
        "active": "Revenue",
        "validation": "Validation",
        "mvp": "MVP",
        "idea": "Idea",
        "growth": "Growth",
    }
    return status_map.get(supabase_status.lower(), "Idea") if supabase_status else "Idea"

def map_stage(supabase_stage):
    stage_map = {
        "pre-launch": "Pre-Launch",
        "mvp": "MVP",
        "beta": "Beta",
        "launch": "Launch",
        "scale": "Scale",
    }
    return stage_map.get(supabase_stage.lower(), "Pre-Launch") if supabase_stage else "Pre-Launch"

def build_notion_payload(venture):
    """Show what Notion payload would look like"""
    return {
        "Venture Name": venture.get("name"),
        "Status": map_status(venture.get("status")),
        "Stage": map_stage(venture.get("stage")),
        "Revenue": venture.get("revenue_ytd") or 0,
        "Costs": venture.get("costs_mom") or 0,
        "Owner": venture.get("owner_id"),
        "Sector": venture.get("sector"),
        "ICP": venture.get("business_model")
    }

def test_sync():
    print("🧪 DRY-RUN: Supabase → Notion Sync Test")
    print(f"📅 {datetime.now().isoformat()}\n")

    print(f"📥 Sample ventures: {len(SAMPLE_VENTURES)}\n")

    for i, venture in enumerate(SAMPLE_VENTURES, 1):
        print(f"--- Venture {i} ---")
        print(f"Name: {venture['name']}")

        notion_payload = build_notion_payload(venture)
        print(f"\nNotion Entry:")
        for key, value in notion_payload.items():
            print(f"  {key}: {value}")
        print()

    print("="*50)
    print(f"✅ Would create: {len(SAMPLE_VENTURES)} ventures in Notion")
    print("="*50)
    print("\n📋 To run the real sync:")
    print("   1. Update .env with real Supabase + Notion tokens")
    print("   2. Run: python3 sync_ventures_to_notion.py")
    print("\n📖 See NOTION-SYNC-SETUP.md for details")

if __name__ == "__main__":
    test_sync()
