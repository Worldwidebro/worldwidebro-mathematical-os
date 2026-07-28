#!/usr/bin/env python3
"""
Sync Supabase Ventures + Loop Data → Notion Portfolio Database
Pulls ventures, loop execution logs, and health scores from Supabase
Syncs to Notion Venture Portfolio with real-time metrics
"""

import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from supabase import create_client, Client
import requests
import json

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")

# Notion Database IDs (from creation)
NOTION_VENTURES_DB_ID = "c7c533f2c9824b80b6c0d1bba77a920d"
NOTION_DATA_SOURCE_ID = "3030288e-8138-4de4-8077-2618d4da44b2"

# Notion API endpoint
NOTION_API_URL = "https://api.notion.com/v1"
NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


def connect_supabase() -> Client:
    """Connect to Supabase"""
    return create_client(SUPABASE_URL, SUPABASE_KEY)


def get_all_ventures(supabase: Client) -> list:
    """Fetch all ventures from Supabase"""
    try:
        response = supabase.table("ventures").select("*").execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"❌ Error fetching ventures: {e}")
        return []


def map_status(supabase_status: str) -> str:
    """Map Supabase status to Notion status"""
    status_map = {
        "active": "Revenue",
        "validation": "Validation",
        "mvp": "MVP",
        "idea": "Idea",
        "growth": "Growth",
    }
    return status_map.get(supabase_status.lower(), "Idea") if supabase_status else "Idea"


def map_stage(supabase_stage: str) -> str:
    """Map Supabase stage to Notion stage"""
    stage_map = {
        "pre-launch": "Pre-Launch",
        "mvp": "MVP",
        "beta": "Beta",
        "launch": "Launch",
        "scale": "Scale",
    }
    return stage_map.get(supabase_stage.lower(), "Pre-Launch") if supabase_stage else "Pre-Launch"


def get_existing_notion_ventures() -> dict:
    """Fetch all existing ventures from Notion (for update detection)"""
    try:
        response = requests.post(
            f"{NOTION_API_URL}/databases/{NOTION_VENTURES_DB_ID}/query",
            headers=NOTION_HEADERS,
            json={}
        )
        response.raise_for_status()

        ventures = {}
        for page in response.json().get("results", []):
            venture_id = page["properties"].get("Venture Name", {}).get("title", [])
            if venture_id:
                venture_name = venture_id[0].get("text", {}).get("content", "")
                ventures[venture_name] = page["id"]
        return ventures
    except Exception as e:
        print(f"⚠️  Warning fetching existing Notion ventures: {e}")
        return {}


def create_notion_venture(venture: dict) -> bool:
    """Create a new venture entry in Notion"""
    try:
        payload = {
            "parent": {
                "database_id": NOTION_VENTURES_DB_ID
            },
            "properties": {
                "Venture Name": {
                    "title": [
                        {
                            "text": {
                                "content": venture.get("name", "Unnamed Venture")[:255]
                            }
                        }
                    ]
                },
                "Status": {
                    "select": {
                        "name": map_status(venture.get("status"))
                    }
                },
                "Stage": {
                    "select": {
                        "name": map_stage(venture.get("stage"))
                    }
                },
                "Revenue": {
                    "number": venture.get("revenue_ytd") or 0
                },
                "Costs": {
                    "number": venture.get("costs_mom") or 0
                },
                "Owner": {
                    "rich_text": [
                        {
                            "text": {
                                "content": venture.get("owner_id", "Unassigned")[:100]
                            }
                        }
                    ]
                },
                "Sector": {
                    "rich_text": [
                        {
                            "text": {
                                "content": venture.get("sector", "Uncategorized")[:100]
                            }
                        }
                    ]
                },
                "ICP": {
                    "rich_text": [
                        {
                            "text": {
                                "content": (venture.get("business_model") or "")[:100]
                            }
                        }
                    ]
                }
            }
        }

        response = requests.post(
            f"{NOTION_API_URL}/pages",
            headers=NOTION_HEADERS,
            json=payload
        )
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"❌ Error creating venture '{venture.get('name')}': {e}")
        return False


def update_notion_venture(page_id: str, venture: dict) -> bool:
    """Update an existing venture entry in Notion"""
    try:
        payload = {
            "properties": {
                "Status": {
                    "select": {
                        "name": map_status(venture.get("status"))
                    }
                },
                "Stage": {
                    "select": {
                        "name": map_stage(venture.get("stage"))
                    }
                },
                "Revenue": {
                    "number": venture.get("revenue_ytd") or 0
                },
                "Costs": {
                    "number": venture.get("costs_mom") or 0
                },
                "Owner": {
                    "rich_text": [
                        {
                            "text": {
                                "content": venture.get("owner_id", "Unassigned")[:100]
                            }
                        }
                    ]
                },
                "Sector": {
                    "rich_text": [
                        {
                            "text": {
                                "content": venture.get("sector", "Uncategorized")[:100]
                            }
                        }
                    ]
                },
                "ICP": {
                    "rich_text": [
                        {
                            "text": {
                                "content": (venture.get("business_model") or "")[:100]
                            }
                        }
                    ]
                }
            }
        }

        response = requests.patch(
            f"{NOTION_API_URL}/pages/{page_id}",
            headers=NOTION_HEADERS,
            json=payload
        )
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"❌ Error updating venture '{venture.get('name')}': {e}")
        return False


def sync_ventures():
    """Main sync function"""
    print("🔄 Starting Supabase → Notion sync...")
    print(f"📅 {datetime.now().isoformat()}")

    # Connect to Supabase
    supabase = connect_supabase()

    # Fetch ventures
    print("📥 Fetching ventures from Supabase...")
    ventures = get_all_ventures(supabase)
    print(f"✅ Found {len(ventures)} ventures")

    if not ventures:
        print("⚠️  No ventures to sync")
        return

    # Get existing Notion ventures
    print("🔍 Checking existing Notion entries...")
    existing_notion = get_existing_notion_ventures()
    print(f"✅ Found {len(existing_notion)} existing Notion entries")

    # Sync each venture
    created = 0
    updated = 0

    for venture in ventures:
        venture_name = venture.get("name", "Unnamed")

        if venture_name in existing_notion:
            # Update existing
            if update_notion_venture(existing_notion[venture_name], venture):
                updated += 1
                print(f"  ✏️  Updated: {venture_name}")
        else:
            # Create new
            if create_notion_venture(venture):
                created += 1
                print(f"  ✨ Created: {venture_name}")

    # Summary
    print("\n" + "="*50)
    print(f"✅ Sync Complete!")
    print(f"   Created: {created}")
    print(f"   Updated: {updated}")
    print(f"   Total: {created + updated}/{len(ventures)}")
    print("="*50)


if __name__ == "__main__":
    try:
        sync_ventures()
    except KeyboardInterrupt:
        print("\n⛔ Sync cancelled")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        sys.exit(1)
