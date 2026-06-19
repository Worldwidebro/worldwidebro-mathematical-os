#!/usr/bin/env python3
"""
LOOP 5: Fetch Open Federal RFPs from SAM.gov
Run: /loop python3 loops/05-SAM-OPPORTUNITIES.py --every 24h

Finds OPEN opportunities (RFPs/solicitations) you can bid on.
- SAM.gov Opportunities API: requires free API key
  Get one: sam.gov account -> Account Details -> API Key
  Then add to .env:  SAM_GOV_API_KEY=your_key_here
- Filters: construction NAICS, posted in last N days
- Stores in Supabase `gov_opportunities` table, deduped by notice id
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
SAM_KEY = os.getenv("SAM_GOV_API_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ SUPABASE_URL or SUPABASE_KEY not in .env")
    sys.exit(1)

if not SAM_KEY:
    print("❌ SAM_GOV_API_KEY not in .env")
    print("   Get a free key: sam.gov -> Account Details -> API Key")
    print("   Then add:  SAM_GOV_API_KEY=your_key_here")
    sys.exit(1)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

API = "https://api.sam.gov/opportunities/v2/search"

# Construction NAICS — roofing, electrical, plumbing, general
NAICS = ["238160", "238210", "238220", "236220", "236118", "238290"]
STATE = "NC"
LOOKBACK_DAYS = 30


def get_existing_ids():
    try:
        resp = supabase.table("gov_opportunities").select("notice_id").execute()
        return {r["notice_id"] for r in resp.data if r.get("notice_id")}
    except Exception:
        return set()


def add_opp(o):
    try:
        supabase.table("gov_opportunities").insert(o).execute()
        return True
    except Exception:
        return False


def fetch_opportunities(naics):
    # SAM.gov wants MM/dd/yyyy dates
    posted_from = (datetime.now() - timedelta(days=LOOKBACK_DAYS)).strftime("%m/%d/%Y")
    posted_to = datetime.now().strftime("%m/%d/%Y")
    params = {
        "api_key": SAM_KEY,
        "naics": naics,
        "state": STATE,
        "postedFrom": posted_from,
        "postedTo": posted_to,
        "limit": 100,
        "ptype": "o,p,k",  # solicitation, presolicitation, combined synopsis
    }
    r = requests.get(API, params=params, timeout=30)
    r.raise_for_status()
    return r.json().get("opportunitiesData", [])


def main():
    print(f"\n{'='*60}")
    print(f"LOOP 5: SAM.GOV OPPORTUNITIES [{datetime.now():%Y-%m-%d %H:%M:%S}]")
    print(f"{'='*60}\n")

    existing = get_existing_ids()
    added = 0

    for naics in NAICS:
        try:
            results = fetch_opportunities(naics)
        except Exception as e:
            print(f"  ⚠️  NAICS {naics} fetch failed: {e}")
            continue

        for o in results:
            nid = o.get("noticeId")
            if not nid or nid in existing:
                continue
            record = {
                "source": "sam.gov",
                "notice_id": nid,
                "title": o.get("title"),
                "naics": naics,
                "agency": o.get("fullParentPathName"),
                "type": o.get("type"),
                "posted_date": o.get("postedDate"),
                "deadline": o.get("responseDeadLine"),
                "url": o.get("uiLink"),
                "status": "new",
            }
            if add_opp(record):
                added += 1
                existing.add(nid)
                print(f"  ✅ [{naics}] {o.get('title')}")

    print(f"\n✅ TOTAL ADDED: {added}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
