#!/usr/bin/env python3
"""
CSV → ClickUp Converter for Cold Call Lists
Maps 5 CSV files to ClickUp workspace structure with venture aliases.
"""

import os, csv, json, argparse
from datetime import datetime, timedelta
from typing import List, Dict
import urllib.request, urllib.error

# ============================================================================
# VENTURE ↔ CLICKUP CORRELATION MAP
# ============================================================================

VENTURE_CONFIG = {
    "OPS-001": {
        "name": "CareerOps Staffing",
        "workspace_id": "9013677375",
        "folder_id": "1000210000000685",
        "list_name": "Sep 11-14 Cold Calls (OPS-001)",
        "deal_value": 2500,
        "csv_file": "calls/OPS-001-FINAL-CALL-LIST.csv",
    },
    "CON-001": {
        "name": "ACE Construction Field OS",
        "workspace_id": "9013677375",
        "folder_id": "901318114591",
        "list_name": "Sep 11-14 Cold Calls (CON-001)",
        "deal_value": 299,
        "csv_file": "calls/CON-001-FINAL-CALL-LIST.csv",
    },
    "LT-005": {
        "name": "HealthRoute Medical Courier",
        "workspace_id": "90141555791",
        "folder_id": "901411978075",
        "list_name": "Sep 11-14 Cold Calls (LT-005)",
        "deal_value": "2000-5000",
        "csv_file": "calls/LT-005-FINAL-CALL-LIST.csv",
    },
    "LT-011": {
        "name": "CarrierDispatch TMS",
        "workspace_id": "9013677375",
        "folder_id": "901317788910",
        "list_name": "Sep 11-14 Cold Calls (LT-011)",
        "deal_value": "500-2000",
        "csv_file": "calls/LT-011-FINAL-CALL-LIST.csv",
    },
    "RE-001": {
        "name": "WorldwideBro Holdings Real Estate",
        "workspace_id": "9013677375",
        "folder_id": "901318114592",
        "list_name": "Sep 11-14 Investor Calls (RE-001)",
        "deal_value": "5000-25000",
        "csv_file": "calls/RE-001-FINAL-CALL-LIST.csv",
    },
}


class ClickUpClient:
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.base_url = "https://api.clickup.com/api/v2"
        self.headers = {
            "Authorization": api_token,
            "Content-Type": "application/json",
        }

    def make_request(self, method: str, endpoint: str, data: Dict = None) -> Dict:
        url = f"{self.base_url}{endpoint}"
        if data:
            data = json.dumps(data).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers=self.headers, method=method)
        try:
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            error_data = json.loads(e.read().decode('utf-8'))
            print(f"❌ API Error {e.code}: {error_data}")
            return None

    def create_list(self, folder_id: str, list_name: str) -> str:
        endpoint = f"/folder/{folder_id}/list"
        response = self.make_request("POST", endpoint, {"name": list_name})
        return response.get("list", {}).get("id") if response else None

    def create_task(self, list_id: str, task_data: Dict) -> str:
        endpoint = f"/list/{list_id}/task"
        response = self.make_request("POST", endpoint, task_data)
        return response.get("task", {}).get("id") if response else None

    def get_or_create_list(self, folder_id: str, list_name: str) -> str:
        endpoint = f"/folder/{folder_id}/list"
        response = self.make_request("GET", endpoint)
        if response and "lists" in response:
            for lst in response["lists"]:
                if lst["name"] == list_name:
                    return lst["id"]
        return self.create_list(folder_id, list_name)


def read_prospect_csv(csv_file: str) -> List[Dict]:
    prospects = []
    if not os.path.exists(csv_file):
        print(f"❌ File not found: {csv_file}")
        return []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            prospects.append(row)
    return prospects


def build_task_data(prospect: Dict, venture_id: str, config: Dict) -> Dict:
    company_name = prospect.get("company_name", "Unknown")
    contact_name = prospect.get("contact_name", "")
    phone = prospect.get("phone", "")
    pain_signal = prospect.get("pain_point_signal", prospect.get("pain_signal", ""))
    task_title = f"Call {company_name} — {pain_signal[:30]}"
    due_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    return {
        "name": task_title[:255],
        "description": f"Prospect: {company_name}\nContact: {contact_name}\nPhone: {phone}\nPain: {pain_signal}\nVenture: {venture_id}",
        "due_date": due_date,
        "priority": 2,
    }


def preview_conversions() -> None:
    print("\n" + "="*80)
    print("PREVIEW: CSV → ClickUp Converter")
    print("="*80 + "\n")
    total_prospects = 0
    for venture_id, config in VENTURE_CONFIG.items():
        prospects = read_prospect_csv(config["csv_file"])
        print(f"📋 {venture_id}: {config['name']}")
        print(f"   Folder: {config['folder_id']}")
        print(f"   Prospects: {len(prospects)}")
        print()
        total_prospects += len(prospects)
    print(f"✅ TOTAL: {total_prospects} tasks ready")
    print("="*80 + "\n")


def deploy_to_clickup(venture_ids: List[str] = None) -> None:
    api_token = os.getenv("CLICKUP_API_TOKEN")
    if not api_token:
        print("❌ CLICKUP_API_TOKEN not set")
        print("   export CLICKUP_API_TOKEN='pk_...'")
        return

    client = ClickUpClient(api_token)
    if venture_ids is None:
        venture_ids = list(VENTURE_CONFIG.keys())

    print("\n" + "="*80)
    print("DEPLOY: Creating ClickUp Tasks from CSV")
    print("="*80 + "\n")

    total_created = 0
    for venture_id in venture_ids:
        if venture_id not in VENTURE_CONFIG:
            print(f"❌ Unknown venture: {venture_id}")
            continue
        config = VENTURE_CONFIG[venture_id]
        prospects = read_prospect_csv(config["csv_file"])
        print(f"📋 {venture_id}: Creating {len(prospects)} tasks...")
        list_id = client.get_or_create_list(config["folder_id"], config["list_name"])
        if not list_id:
            print(f"   ❌ Failed to create/find list")
            continue
        created = 0
        for prospect in prospects:
            task_data = build_task_data(prospect, venture_id, config)
            if client.create_task(list_id, task_data):
                created += 1
        print(f"   ✅ Created: {created}\n")
        total_created += created

    print("="*80)
    print(f"✅ TOTAL CREATED: {total_created}")
    print("="*80 + "\n")


def main():
    parser = argparse.ArgumentParser(description="CSV → ClickUp Converter")
    parser.add_argument("--list-only", action="store_true", help="Preview only")
    parser.add_argument("--create", action="store_true", help="Deploy to ClickUp")
    parser.add_argument("--venture", type=str, help="Specific venture")
    args = parser.parse_args()

    if args.list_only:
        preview_conversions()
    elif args.create:
        venture_ids = [args.venture] if args.venture else None
        deploy_to_clickup(venture_ids)
    else:
        preview_conversions()


if __name__ == "__main__":
    main()
