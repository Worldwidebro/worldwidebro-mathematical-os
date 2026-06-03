#!/usr/bin/env python3
"""
Sync SocratiCode Profiles to Supabase — Push semantic capabilities to repos table
"""

import json
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv("/Users/acebless/Documents/.env")

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

class SocratiCodeSync:
    """Sync SocratiCode profiles to Supabase repos table"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json"
        })

    def load_profiles(self) -> dict:
        """Load SocratiCode profiles from JSON"""
        try:
            with open("socraticode_profiles.json", "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Failed to load profiles: {e}")
            return {}

    def sync_to_supabase(self, profiles: dict) -> bool:
        """Update existing repo records with semantic capabilities"""
        print(f"📤 Syncing {len(profiles)} repos to Supabase...")

        success_count = 0
        for repo_name, profile in profiles.items():
            languages = profile.get('languages', [])
            update_data = {
                "capabilities": profile.get('capabilities', []),
                "stack": languages if languages else [],
                "indexed_at": datetime.utcnow().isoformat()
            }

            try:
                # Update repos by name filter
                response = self.session.patch(
                    f"{SUPABASE_URL}/rest/v1/repos?name=eq.{repo_name}",
                    json=update_data
                )

                if response.status_code in [200, 204]:
                    success_count += 1
                else:
                    print(f"   ⚠️  {repo_name}: {response.status_code}")
            except Exception as e:
                print(f"   ⚠️  {repo_name}: {e}")

        if success_count == len(profiles):
            print(f"✅ Updated {success_count}/{len(profiles)} repos in Supabase")
            return True
        else:
            print(f"⚠️  Updated {success_count}/{len(profiles)} repos")
            return success_count > 0

    def run(self):
        """Run the sync"""
        print("\n" + "="*80)
        print("SOCRATICODE → SUPABASE SYNC")
        print("="*80 + "\n")

        if not SUPABASE_KEY:
            print("❌ SUPABASE_KEY not set")
            return

        profiles = self.load_profiles()
        if not profiles:
            return

        self.sync_to_supabase(profiles)

        print("\n" + "="*80)
        print("✅ SYNC COMPLETE")
        print("="*80 + "\n")


def main():
    sync = SocratiCodeSync()
    sync.run()


if __name__ == "__main__":
    main()
