#!/usr/bin/env python3
"""
Venture Operations—Autonomous System Initializer
Creates ClickUp list, custom fields, and tests watcher connection

---
created: 2026-06-02T00:00:00Z
last_edited: 2026-06-02T00:00:00Z
edited_by: Claude Haiku 4.5
version: 1.0
---
"""

import os
import sys
import requests
import json
from dotenv import load_dotenv

load_dotenv()

CLICKUP_API_KEY = os.getenv("CLICKUP_API_KEY")
CLICKUP_WORKSPACE = os.getenv("CLICKUP_WORKSPACE", "9013677375")
CLICKUP_API_URL = "https://api.clickup.com/api/v2"

HEADERS = {
    "Authorization": CLICKUP_API_KEY,
    "Content-Type": "application/json",
}


class VentureOpsInitializer:
    def __init__(self, api_key: str, workspace_id: str):
        self.api_key = api_key
        self.workspace_id = workspace_id

    def create_list(self) -> str:
        """Create 'Venture Operations—Autonomous' list"""
        try:
            url = f"{CLICKUP_API_URL}/space/{self.workspace_id}/list"
            payload = {
                "name": "Venture Operations—Autonomous",
                "content": "Autonomous venture task execution & orchestration",
                "due_date": None,
                "due_date_time": None,
                "priority": None,
                "assignee": None,
                "status": "active",
            }

            response = requests.post(url, headers=HEADERS, json=payload)
            response.raise_for_status()

            list_data = response.json()
            list_id = list_data.get("id")
            print(f"✅ Created list: {list_id}")
            return list_id

        except requests.exceptions.HTTPError as e:
            if "already exists" in str(e).lower():
                print("⚠️  List already exists, fetching existing list ID...")
                return self.get_list_id()
            else:
                print(f"❌ Failed to create list: {e}")
                return None

    def get_list_id(self) -> str:
        """Get existing list ID by name"""
        try:
            url = f"{CLICKUP_API_URL}/space/{self.workspace_id}/list"
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()

            lists = response.json().get("lists", [])
            for lst in lists:
                if lst.get("name") == "Venture Operations—Autonomous":
                    print(f"✅ Found existing list: {lst['id']}")
                    return lst["id"]

            print("❌ List not found")
            return None

        except Exception as e:
            print(f"❌ Failed to fetch list: {e}")
            return None

    def add_statuses(self, list_id: str) -> bool:
        """Add status workflow"""
        try:
            url = f"{CLICKUP_API_URL}/list/{list_id}"
            payload = {
                "statuses": [
                    {"status": "pending", "color": "#FFA500", "type": "open"},
                    {"status": "in_progress", "color": "#4169E1", "type": "open"},
                    {"status": "success", "color": "#32CD32", "type": "closed"},
                    {"status": "failed", "color": "#FF4500", "type": "closed"},
                    {"status": "warning", "color": "#FFD700", "type": "open"},
                ]
            }

            response = requests.put(url, headers=HEADERS, json=payload)
            response.raise_for_status()
            print("✅ Added statuses: pending, in_progress, success, failed, warning")
            return True

        except Exception as e:
            print(f"⚠️  Statuses may already exist: {e}")
            return True

    def add_custom_fields(self, list_id: str) -> dict:
        """Add custom fields for task types"""
        field_ids = {}

        try:
            # Global fields
            global_fields = [
                {"name": "venture_id", "type": "text", "required": True},
                {
                    "name": "task_type",
                    "type": "drop",
                    "type_config": {
                        "options": [
                            {"name": "DEPLOY"},
                            {"name": "MIGRATE"},
                            {"name": "INTEGRATE"},
                            {"name": "TEST"},
                            {"name": "SYNC"},
                            {"name": "DOCUMENT"},
                            {"name": "MONITOR"},
                            {"name": "BACKUP"},
                            {"name": "ONBOARD"},
                            {"name": "REPORT"},
                            {"name": "SCALE"},
                            {"name": "INCIDENT"},
                        ]
                    },
                    "required": True,
                },
            ]

            # Task-specific fields
            task_fields = {
                "DEPLOY": [
                    {
                        "name": "deployment_target",
                        "type": "drop",
                        "type_config": {
                            "options": [
                                {"name": "staging"},
                                {"name": "prod"},
                            ]
                        },
                    },
                    {"name": "version", "type": "text"},
                ],
                "MIGRATE": [
                    {"name": "migration_name", "type": "text"},
                    {"name": "migration_sql", "type": "textarea"},
                    {"name": "is_production", "type": "checkbox"},
                    {"name": "rollback_plan", "type": "text"},
                ],
                "INTEGRATE": [
                    {"name": "service", "type": "text"},
                    {"name": "credentials_vault_key", "type": "text"},
                ],
                "TEST": [
                    {
                        "name": "test_suite",
                        "type": "drop",
                        "type_config": {
                            "options": [
                                {"name": "e2e"},
                                {"name": "unit"},
                                {"name": "integration"},
                                {"name": "smoke"},
                            ]
                        },
                    },
                    {"name": "failures", "type": "text"},
                ],
                "SYNC": [
                    {
                        "name": "data_source",
                        "type": "drop",
                        "type_config": {
                            "options": [
                                {"name": "GitHub"},
                                {"name": "Supabase"},
                                {"name": "Obsidian"},
                            ]
                        },
                    }
                ],
                "DOCUMENT": [
                    {
                        "name": "doc_type",
                        "type": "drop",
                        "type_config": {
                            "options": [
                                {"name": "README"},
                                {"name": "API"},
                                {"name": "architecture"},
                                {"name": "deployment"},
                            ]
                        },
                    }
                ],
                "MONITOR": [
                    {
                        "name": "metric_type",
                        "type": "drop",
                        "type_config": {
                            "options": [
                                {"name": "uptime"},
                                {"name": "latency"},
                                {"name": "error_rate"},
                                {"name": "cpu"},
                                {"name": "memory"},
                            ]
                        },
                    },
                    {"name": "threshold", "type": "number"},
                ],
                "BACKUP": [
                    {
                        "name": "backup_type",
                        "type": "drop",
                        "type_config": {
                            "options": [
                                {"name": "full"},
                                {"name": "incremental"},
                            ]
                        },
                    },
                    {"name": "target_storage", "type": "text"},
                ],
                "ONBOARD": [
                    {"name": "folder_created", "type": "checkbox"},
                    {"name": "db_initialized", "type": "checkbox"},
                    {"name": "repo_created", "type": "checkbox"},
                ],
                "REPORT": [
                    {
                        "name": "report_type",
                        "type": "drop",
                        "type_config": {
                            "options": [
                                {"name": "weekly"},
                                {"name": "monthly"},
                            ]
                        },
                    },
                    {"name": "metrics_list", "type": "text"},
                ],
                "SCALE": [
                    {
                        "name": "scale_target",
                        "type": "drop",
                        "type_config": {
                            "options": [
                                {"name": "database"},
                                {"name": "compute"},
                                {"name": "storage"},
                            ]
                        },
                    },
                    {"name": "new_capacity", "type": "text"},
                ],
                "INCIDENT": [
                    {
                        "name": "severity",
                        "type": "drop",
                        "type_config": {
                            "options": [
                                {"name": "critical"},
                                {"name": "high"},
                                {"name": "medium"},
                            ]
                        },
                    },
                    {"name": "description", "type": "text"},
                    {"name": "assigned_to", "type": "text"},
                ],
            }

            # Add global fields
            for field in global_fields:
                field_id = self._create_custom_field(list_id, field)
                if field_id:
                    field_ids[field["name"]] = field_id

            # Add task-specific fields
            for task_type, fields in task_fields.items():
                for field in fields:
                    field_id = self._create_custom_field(list_id, field)
                    if field_id:
                        field_ids[f"{task_type}_{field['name']}"] = field_id

            print(f"✅ Added {len(field_ids)} custom fields")
            return field_ids

        except Exception as e:
            print(f"⚠️  Error adding custom fields: {e}")
            return field_ids

    def _create_custom_field(self, list_id: str, field: dict) -> str:
        """Create a single custom field"""
        try:
            url = f"{CLICKUP_API_URL}/list/{list_id}/field"
            response = requests.post(url, headers=HEADERS, json=field)
            response.raise_for_status()
            field_data = response.json()
            return field_data.get("id")
        except Exception as e:
            print(f"  ⚠️  Skipping {field['name']}: {e}")
            return None

    def test_connection(self, list_id: str) -> bool:
        """Test that list is accessible"""
        try:
            url = f"{CLICKUP_API_URL}/list/{list_id}"
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            print(f"✅ ClickUp connection verified")
            return True
        except Exception as e:
            print(f"❌ ClickUp connection failed: {e}")
            return False

    def run(self) -> str:
        """Run full initialization"""
        if not CLICKUP_API_KEY:
            print("❌ CLICKUP_API_KEY not found in .env")
            print("Set CLICKUP_API_KEY in .env and try again")
            return None

        print("🚀 Initializing Venture Operations—Autonomous system...\n")

        # Create list
        list_id = self.get_list_id() or self.create_list()
        if not list_id:
            print("❌ Failed to create/find list")
            return None

        # Add statuses
        self.add_statuses(list_id)

        # Add custom fields
        self.add_custom_fields(list_id)

        # Test connection
        if self.test_connection(list_id):
            print(f"\n✅ Setup complete!")
            print(f"\nSave this to .env:")
            print(f"CLICKUP_LIST_VENTURE_OPS={list_id}")
            return list_id
        else:
            print("\n⚠️  Setup created but connection test failed")
            return list_id


def main():
    init = VentureOpsInitializer(CLICKUP_API_KEY, CLICKUP_WORKSPACE)
    list_id = init.run()

    if list_id:
        print(f"\nNext steps:")
        print(f"1. Add CLICKUP_LIST_VENTURE_OPS={list_id} to .env")
        print(f"2. Start task watcher: python task-watcher.py")
        print(f"3. Create test task in ClickUp")
        print(f"4. Watch logs: tail -f /var/log/venture-ops/task-watcher.log")


if __name__ == "__main__":
    main()
