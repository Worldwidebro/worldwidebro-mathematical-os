#!/usr/bin/env python3
"""
LOOP 3: Score Leads by Source
Run: /loop python3 loops/03-SCORE-LEADS.py --every 24h

Analyzes all leads
Calculates cost per lead by source
Identifies cheapest source
Reports recommendations
"""

import os
import sys
from datetime import datetime, timedelta
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ SUPABASE credentials missing")
    sys.exit(1)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def main():
    print(f"\n{'='*60}")
    print(f"LOOP 3: SCORE LEADS [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    print(f"{'='*60}\n")

    # Get all leads from past 7 days
    try:
        response = supabase.table("leads").select("*").execute()
        all_leads = response.data
    except:
        all_leads = []

    # Group by source
    by_source = {}
    for lead in all_leads:
        source = lead.get("source", "unknown")
        if source not in by_source:
            by_source[source] = []
        by_source[source].append(lead)

    print("📊 LEADS BY SOURCE:\n")

    # Analyze each source
    ad_spend = {
        "homeadvisor": 50,  # Mock: $50 spent on HomeAdvisor
        "angi": 75,
        "samgov": 0
    }

    for source, leads in by_source.items():
        cost = ad_spend.get(source, 0)
        if cost > 0 and len(leads) > 0:
            cost_per_lead = cost / len(leads)
            print(f"  {source.upper()}: {len(leads)} leads | \${cost_per_lead:.2f} cost/lead")
        else:
            print(f"  {source.upper()}: {len(leads)} leads | $0 cost (organic)")

    # Recommendation
    print("\n💡 RECOMMENDATION:")
    if by_source:
        cheapest_source = min(by_source.keys(), key=lambda s: ad_spend.get(s, 0) or 1 if ad_spend.get(s, 0) > 0 else float('inf'))
        print(f"  → Increase budget for {cheapest_source.upper()} (best ROI)")
    else:
        print(f"  → No data yet. Check back tomorrow.")

    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
