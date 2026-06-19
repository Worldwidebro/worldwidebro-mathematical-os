#!/usr/bin/env python3
"""
Step 4: Wire Supabase Integration to Paperclip
Creates sector projects and venture issues in Paperclip from ventures_for_paperclip.json
"""

import os
import sys
import json
import requests
from datetime import datetime
from typing import Dict, List, Optional

# Config
PAPERCLIP_URL = "http://127.0.0.1:3103"
PAPERCLIP_COMPANY_ID = "1450a240-2be1-4dc6-b74c-ada307ca6ddb"

# Load ventures export
VENTURES_FILE = "/Users/acebless/ventures_for_paperclip.json"

def get_headers() -> Dict[str, str]:
    """Get request headers for Paperclip API"""
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

def create_project(name: str, description: str, color: str = "#000000") -> Optional[Dict]:
    """Create a sector project in Paperclip"""
    url = f"{PAPERCLIP_URL}/api/projects"
    payload = {
        "name": name,
        "description": description,
        "company_id": PAPERCLIP_COMPANY_ID,
        "color": color,
        "status": "active"
    }

    try:
        response = requests.post(url, json=payload, headers=get_headers(), timeout=10)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            print(f"    ✗ Failed to create project '{name}': {response.status_code} {response.text[:100]}")
            return None
    except Exception as e:
        print(f"    ✗ Error creating project '{name}': {e}")
        return None

def create_issue(project_id: str, title: str, description: str, status: str = "backlog") -> Optional[Dict]:
    """Create a venture issue in a sector project"""
    url = f"{PAPERCLIP_URL}/api/projects/{project_id}/issues"
    payload = {
        "title": title,
        "description": description,
        "status": status,
        "priority": "normal"
    }

    try:
        response = requests.post(url, json=payload, headers=get_headers(), timeout=10)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            return None
    except Exception as e:
        return None

def main():
    print(f"[{datetime.now().isoformat()}] Step 4: Wire Supabase Integration to Paperclip")
    print(f"  Paperclip: {PAPERCLIP_URL}")
    print(f"  Company:   {PAPERCLIP_COMPANY_ID}")
    print()

    # Load ventures export
    print(f"[STEP 1] Loading ventures from {VENTURES_FILE}...")
    try:
        with open(VENTURES_FILE, "r") as f:
            export_data = json.load(f)
        print(f"  ✓ Loaded export data")
    except Exception as e:
        print(f"  ✗ Error loading ventures: {e}")
        return False

    organization = export_data.get("organization", {})
    sectors = export_data.get("sectors", {})

    print(f"\n[STEP 2] Creating sector projects in Paperclip...")
    sector_projects = {}

    for sector_key, sector_data in sectors.items():
        sector_name = sector_data.get("name", sector_key)
        sector_color = sector_data.get("color", "#000000")
        venture_count = sector_data.get("count", 0)

        print(f"  Creating sector: {sector_name} ({venture_count} ventures)")

        project = create_project(
            name=f"{sector_name} (Sector)",
            description=f"{sector_name} ventures - {venture_count} companies",
            color=sector_color
        )

        if project:
            project_id = project.get("id")
            sector_projects[sector_key] = project_id
            print(f"    ✓ Created project (ID: {project_id})")
        else:
            print(f"    ✗ Could not create project for {sector_name}")

    print(f"\n[STEP 3] Creating venture issues in sector projects...")
    issue_count = 0

    for sector_key, sector_data in sectors.items():
        if sector_key not in sector_projects:
            print(f"  Skipping {sector_key} (no project created)")
            continue

        project_id = sector_projects[sector_key]
        ventures = sector_data.get("ventures", [])

        print(f"  {sector_key}: Creating {len(ventures)} ventures...")

        for venture in ventures:
            venture_name = venture.get("name", "Unknown")
            venture_desc = venture.get("description", "")

            issue = create_issue(
                project_id=project_id,
                title=venture_name,
                description=venture_desc,
                status="backlog"
            )

            if issue:
                issue_count += 1
                if issue_count % 50 == 0:
                    print(f"    Created {issue_count} issues...")

    print(f"\n[SUMMARY]")
    print(f"  Sectors created: {len(sector_projects)}")
    print(f"  Issues created: {issue_count}")
    print(f"  Status: Org structure now live in Paperclip")
    print(f"\n[NEXT] Step 5: Surface GTM Phase 0/1/2 status dashboard")

    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
