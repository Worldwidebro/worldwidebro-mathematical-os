#!/usr/bin/env python3
"""
Step 3: Bulk Create Ventures in Paperclip
Models Worldwidebro Holdings org structure:
  - Root: Worldwidebro Holdings
  - 7 Sector Divisions (fintech, ai, edtech, health, infra, market, devtools)
  - 687 Ventures as Issues (tasks) under sectors

Approach: Use Paperclip API to create sector projects + venture issues in bulk
"""

import os
import sys
import json
import requests
from datetime import datetime
from supabase import create_client
import time

# Config
PAPERCLIP_URL = "http://127.0.0.1:3103"
PAPERCLIP_COMPANY_ID = "1450a240-2be1-4dc6-b74c-ada307ca6ddb"  # Default company
JWT_SECRET = "be61d66f9874916de05315e7e4260e9318e5c6ff348aa83b1ccdab8dfe4a1c07"

# Supabase config
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN5aHppbHFsZG91emd5bmFjcXBlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NDY2OTQwOCwiZXhwIjoyMDgwMjQ1NDA4fQ.1M6V3fR9rNxonIJvtNkV4isrZK9VIvy3J-gNLJGMp2k")

# Sectors mapping
SECTORS = {
    "fintech": {"color": "#1E40AF", "description": "Financial Technology"},
    "ai": {"color": "#7C3AED", "description": "Artificial Intelligence"},
    "edtech": {"color": "#DC2626", "description": "Education Technology"},
    "health": {"color": "#059669", "description": "Healthcare"},
    "infra": {"color": "#0891B2", "description": "Infrastructure"},
    "market": {"color": "#F59E0B", "description": "Marketplace"},
    "devtools": {"color": "#6366F1", "description": "Developer Tools"},
}

def main():
    print(f"[{datetime.now().isoformat()}] Step 3: Bulk Create Ventures in Paperclip")
    print(f"  Paperclip: {PAPERCLIP_URL}")
    print(f"  Company:   {PAPERCLIP_COMPANY_ID}")
    print()

    # Step 1: Fetch ventures from Supabase
    print("[STEP 1] Fetching 687 ventures from Supabase...")
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    try:
        response = supabase.table("ventures").select("id, name, description, sector, status").limit(1000).execute()
        ventures = response.data if response.data else []
        print(f"  ✓ Fetched {len(ventures)} ventures")
    except Exception as e:
        print(f"  ✗ Error fetching ventures: {e}")
        return False

    # Step 2: Organize by sector
    print("\n[STEP 2] Organizing ventures by sector...")
    ventures_by_sector = {sector: [] for sector in SECTORS.keys()}
    untagged = []

    for venture in ventures:
        sector = venture.get("sector", "").lower() if venture.get("sector") else None
        if sector in ventures_by_sector:
            ventures_by_sector[sector].append(venture)
        else:
            untagged.append(venture)

    for sector, ventures_list in ventures_by_sector.items():
        print(f"  {sector}: {len(ventures_list)} ventures")
    if untagged:
        print(f"  untagged: {len(untagged)} ventures")

    # Step 3: Create in Paperclip (simulation - would need API auth)
    print("\n[STEP 3] Creating org structure in Paperclip...")
    print(f"  ✓ Would create 7 sector projects")
    print(f"  ✓ Would create {len(ventures)} venture issues")
    print(f"  ✓ Would organize by sector with rollup dashboard")

    print("\n[STEP 4] Export venture data for Paperclip import...")

    # Create export file for manual import / API bulk-create
    export_data = {
        "organization": {
            "name": "Worldwidebro Holdings",
            "description": "Go-to-Market execution system for 687 ventures",
            "created_at": datetime.now().isoformat(),
        },
        "sectors": {},
    }

    for sector, ventures_list in ventures_by_sector.items():
        export_data["sectors"][sector] = {
            "name": SECTORS[sector]["description"],
            "color": SECTORS[sector]["color"],
            "ventures": ventures_list,
            "count": len(ventures_list),
        }

    export_path = "/Users/acebless/ventures_for_paperclip.json"
    with open(export_path, "w") as f:
        json.dump(export_data, f, indent=2, default=str)

    print(f"  ✓ Exported to: {export_path}")
    print(f"  ✓ Ready for Paperclip bulk import")

    # Summary
    print(f"\n[SUMMARY]")
    print(f"  Total ventures: {len(ventures)}")
    print(f"  Tagged: {sum(len(v) for v in ventures_by_sector.values())}")
    print(f"  Untagged: {len(untagged)}")
    print(f"  Export file: {export_path}")
    print(f"\n[NEXT] Step 4: Wire Supabase integration to Paperclip")

    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
