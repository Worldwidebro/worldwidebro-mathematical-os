#!/usr/bin/env python3
"""
LOOP 4: Fetch Awarded Federal Contracts from USASpending.gov
Run: /loop python3 loops/04-USASPENDING-CONTRACTS.py --every 24h

Finds WHO already won construction contracts in NC (competitors + the buyers).
- USASpending API: no key required, fully open
- Filters: construction NAICS codes, NC place-of-performance, recent awards
- Stores in Supabase `gov_awards` table, deduped by award id
"""

import os
import sys
import requests
from datetime import datetime, timedelta
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ SUPABASE_URL or SUPABASE_KEY not in .env")
    sys.exit(1)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

API = "https://api.usaspending.gov/api/v2/search/spending_by_award/"

# Construction NAICS — roofing, electrical, plumbing, general
NAICS = ["238160", "238210", "238220", "236220", "236118", "238290"]
STATE = "NC"
LOOKBACK_DAYS = 90


def get_existing_ids():
    try:
        resp = supabase.table("gov_awards").select("award_id").execute()
        return {r["award_id"] for r in resp.data if r.get("award_id")}
    except Exception:
        return set()


def add_contract(c):
    try:
        supabase.table("gov_awards").insert(c).execute()
        return True
    except Exception:
        return False


def fetch_awards():
    start = (datetime.now() - timedelta(days=LOOKBACK_DAYS)).strftime("%Y-%m-%d")
    end = datetime.now().strftime("%Y-%m-%d")
    payload = {
        "filters": {
            "award_type_codes": ["A", "B", "C", "D"],  # contract types
            "naics_codes": NAICS,
            "place_of_performance_locations": [{"country": "USA", "state": STATE}],
            "time_period": [{"start_date": start, "end_date": end}],
        },
        "fields": [
            "Award ID", "Recipient Name", "Award Amount",
            "Awarding Agency", "Start Date", "End Date",
            "Place of Performance City Code", "Description",
        ],
        "sort": "Award Amount",
        "order": "desc",
        "limit": 100,
    }
    r = requests.post(API, json=payload, timeout=30)
    r.raise_for_status()
    return r.json().get("results", [])


def main():
    print(f"\n{'='*60}")
    print(f"LOOP 4: USASPENDING CONTRACTS [{datetime.now():%Y-%m-%d %H:%M:%S}]")
    print(f"{'='*60}\n")

    existing = get_existing_ids()
    added = 0

    try:
        results = fetch_awards()
    except Exception as e:
        print(f"❌ USASpending fetch failed: {e}")
        sys.exit(1)

    print(f"  Fetched {len(results)} NC construction awards (last {LOOKBACK_DAYS}d)\n")

    for a in results:
        aid = a.get("Award ID")
        if not aid or aid in existing:
            continue
        record = {
            "source": "usaspending",
            "award_id": aid,
            "recipient": a.get("Recipient Name"),
            "amount": a.get("Award Amount"),
            "agency": a.get("Awarding Agency"),
            "description": (a.get("Description") or "")[:500],
            "start_date": a.get("Start Date"),
            "end_date": a.get("End Date"),
            "status": "new",
        }
        if add_contract(record):
            added += 1
            existing.add(aid)
            print(f"  ✅ ${a.get('Award Amount', 0) or 0:>12,.0f}  {a.get('Recipient Name')}")

    print(f"\n✅ TOTAL ADDED: {added}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
