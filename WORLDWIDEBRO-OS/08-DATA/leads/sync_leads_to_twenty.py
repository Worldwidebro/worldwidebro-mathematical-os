#!/usr/bin/env python3
"""
sync_leads_to_twenty.py
Reads waitlist leads from local CSV and pushes them to the unified Twenty CRM instance.
"""
import os
import csv
import json
import urllib.request
import urllib.error

CSV_FILE = "/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/leads/waitlist_leads.csv"
TWENTY_URL = os.environ.get("TWENTY_API_URL", "http://localhost:3002/api/v1/people")
TWENTY_TOKEN = os.environ.get("TWENTY_API_KEY", "")  # Load from environment


def main():
    if not os.path.exists(CSV_FILE):
        print(f"[*] No leads file found at {CSV_FILE}")
        return

    print(f"[*] Syncing leads from {CSV_FILE} to Twenty CRM...")

    leads = []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads.append(row)

    if not leads:
        print("[*] No leads to sync.")
        return

    # Check for token
    if not TWENTY_TOKEN:
        print("[!] Warning: TWENTY_API_KEY environment variable is empty. Running in dry-run mode.")
        print(f"[*] Dry-run: Would sync {len(leads)} leads to Twenty CRM at {TWENTY_URL}")
        for lead in leads:
            print(f"  - Lead: {lead['email']} (Name: {lead['name']}, Venture: {lead['ventureId']})")
        return

    success_count = 0
    for lead in leads:
        # Build the payload mapping to Twenty Contact/People format
        payload = {
            "email": lead["email"],
            "name": {
                "firstName": lead["name"].split(" ")[0] if lead["name"] else "",
                "lastName": " ".join(lead["name"].split(" ")[1:]) if len(lead["name"].split(" ")) > 1 else ""
            },
            "jobTitle": f"Waitlist Lead ({lead['ventureId']})",
            "metadata": json.loads(lead["metadata"])
        }

        req = urllib.request.Request(
            TWENTY_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {TWENTY_TOKEN}"
            },
            method="POST"
        )

        try:
            with urllib.request.urlopen(req) as res:
                if res.status in (200, 201):
                    success_count += 1
        except urllib.error.HTTPError as e:
            print(f"[!] Failed to sync lead {lead['email']}: HTTP {e.code} - {e.read().decode('utf-8')}")
        except Exception as e:
            print(f"[!] Network error syncing lead {lead['email']}: {str(e)}")

    print(f"[*] Sync complete. Successfully synced {success_count}/{len(leads)} leads to Twenty CRM.")


if __name__ == "__main__":
    main()
