#!/usr/bin/env python3
"""
ClickUp Batch Setup: Create sector folders + lists in AI Boss Hub
Generates folders for all 18 sectors, then creates ventures in each

Run with: python3 clickup-batch-setup.py
Requires: CLICKUP_API_TOKEN env var
"""

import os
import json
import requests
from typing import Dict

# Configuration
WORKSPACE_ID = "9013677375"
AI_BOSS_HUB_SPACE_ID = "90133020094"
API_BASE = "https://api.clickup.com/api/v3"

# Sector configuration (from Supabase validation)
SECTORS = {
    "E-Commerce": 218,
    "Operations": 132,
    "Emerging": 100,
    "Community": 100,
    "Specialized": 100,
    "Technology": 93,
    "Beauty-Wellness": 80,
    "Education": 80,
    "Financial": 72,
    "Food-Hospitality": 70,
    "Software-Technology": 60,
    "Fitness-Sports": 50,
    "Professional-Services": 50,
    "Logistics-Transport": 30,
    "Education-Training": 30,
    "Media-Content": 21,
    "Construction": 20,
    "Real-Estate": 2,
}

def get_headers():
    """Get ClickUp API headers"""
    token = os.getenv('CLICKUP_API_TOKEN')
    if not token:
        raise ValueError("CLICKUP_API_TOKEN environment variable not set")
    return {
        "Authorization": token,
        "Content-Type": "application/json"
    }

def create_folder(sector_name: str, venture_count: int) -> Dict:
    """Create a folder for a sector"""
    headers = get_headers()
    url = f"{API_BASE}/space/{AI_BOSS_HUB_SPACE_ID}/folder"

    payload = {
        "name": f"{sector_name} ({venture_count})"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code in [200, 201]:
        data = response.json()
        folder_id = data['folder']['id']
        print(f"✅ Created folder: {sector_name} ({venture_count} ventures)")
        return {"sector": sector_name, "folder_id": folder_id, "venture_count": venture_count}
    else:
        print(f"❌ Failed to create folder {sector_name}: {response.status_code}")
        return None

def create_list_in_folder(folder_id: str, list_name: str = "Ventures") -> Dict:
    """Create a list within a folder"""
    headers = get_headers()
    url = f"{API_BASE}/folder/{folder_id}/list"

    payload = {
        "name": list_name
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code in [200, 201]:
        data = response.json()
        list_id = data['list']['id']
        return {"list_id": list_id, "list_name": list_name}
    else:
        print(f"❌ Failed to create list in folder {folder_id}: {response.status_code}")
        return None

def main():
    """Main execution"""
    print("🚀 ClickUp Batch Setup: Create Sector Folders & Lists")
    print("=" * 60)

    folder_map = {}

    # Create folders for each sector
    for sector_name, venture_count in SECTORS.items():
        try:
            folder_data = create_folder(sector_name, venture_count)
            if folder_data:
                list_data = create_list_in_folder(folder_data['folder_id'])
                if list_data:
                    folder_map[sector_name] = {
                        "folder_id": folder_data['folder_id'],
                        "list_id": list_data['list_id'],
                        "venture_count": venture_count
                    }
        except Exception as e:
            print(f"❌ Error creating folder for {sector_name}: {str(e)}")

    # Save folder mapping
    output_file = '/Users/acebless/Documents/CLICKUP-RESTRUCTURING/sector-folder-mapping.json'
    with open(output_file, 'w') as f:
        json.dump(folder_map, f, indent=2)

    print(f"\n✅ Setup complete!")
    print(f"✅ Created {len(folder_map)} sector folders")
    print(f"✅ Saved mapping to: sector-folder-mapping.json")

if __name__ == "__main__":
    main()
