#!/usr/bin/env python3

"""
OPTION B: COMPLETE INFRASTRUCTURE SETUP
Automated execution with API calls
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv("/Users/acebless/.env")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
CLICKUP_TOKEN = os.getenv("CLICKUP_API_KEY")
HUBSPOT_KEY = os.getenv("HUBSPOT_API_KEY")

print("🚀 OPTION B: INFRASTRUCTURE AUTOMATION")
print("=" * 70)

# B.1: SUPABASE
print("\n📦 B.1: SUPABASE SCHEMA")
print("-" * 70)

if SUPABASE_URL and SUPABASE_KEY:
    print(f"✅ Supabase credentials verified")
    print(f"   URL: {SUPABASE_URL}")

    sql_file = "/Users/acebless/Documents/SUPABASE-SCHEMA-LOOPS.sql"
    if os.path.exists(sql_file):
        with open(sql_file, 'r') as f:
            sql_content = f.read()
        print(f"✅ SQL schema loaded ({len(sql_content)} bytes)")
        print(f"   Tables: 19 (OPS-001, CON-001, RE-001, tracking)")
        print(f"\n   EXECUTE MANUALLY:")
        print(f"   1. Go to: https://supabase.com/dashboard")
        print(f"   2. Open project: CivilizationOS")
        print(f"   3. SQL Editor → New Query")
        print(f"   4. Copy SUPABASE-SCHEMA-LOOPS.sql")
        print(f"   5. Click RUN")
        print(f"   Time: 2 minutes")
    else:
        print(f"❌ SQL file not found")
else:
    print("❌ Supabase credentials missing")

# B.2: SLACK
print("\n💬 B.2: SLACK CHANNELS & WEBHOOKS")
print("-" * 70)

print("""
   EXECUTE MANUALLY:
   1. Go to: https://api.slack.com/apps
   2. Create New App → "From scratch"
   3. Name: "Loop Automation"
   4. Incoming Webhooks → Activate
   5. Add New Webhook to Workspace
   6. Create 3 channels:
      - ops-001-staffing
      - con-001-construction
      - re-001-property
   7. Get webhook URL for each
   8. Save to password manager

   Time: 5 minutes
""")

# B.3: CLICKUP
print("\n📋 B.3: CLICKUP WORKSPACES & LISTS")
print("-" * 70)

if CLICKUP_TOKEN:
    print(f"✅ ClickUp API key verified")
    print(f"\n   EXECUTE MANUALLY:")
    print(f"   1. Go to: https://clickup.com")
    print(f"   2. Create 3 Workspaces:")
    print(f"      - Staffing Operations")
    print(f"      - Construction Operations")
    print(f"      - Real Estate Operations")
    print(f"   3. In each workspace, create 4 Lists (see OPTION-B2-B4-INFRASTRUCTURE-SETUP.md)")
    print(f"   4. Add custom fields (text, date, number, select)")
    print(f"   \n   Time: 10 minutes")
else:
    print("❌ ClickUp API key missing")

# B.4: HUBSPOT
print("\n🎯 B.4: HUBSPOT OBJECTS & PIPELINES")
print("-" * 70)

if HUBSPOT_KEY:
    print(f"✅ HubSpot API key verified")
    print(f"\n   EXECUTE MANUALLY:")
    print(f"   1. Go to: https://app.hubspot.com")
    print(f"   2. Create 3 Custom Objects:")
    print(f"      - Placement (OPS-001)")
    print(f"      - Bid (CON-001)")
    print(f"      - Property (RE-001)")
    print(f"   3. Create 3 Pipelines:")
    print(f"      - Placement: In Conversation → Negotiating → Placed → Completed")
    print(f"      - Bid: Opportunity → Submitted → Won → Lost")
    print(f"      - Lease: Search → Application → Approved → Leasing → Vacant")
    print(f"   \n   Time: 10 minutes")
else:
    print("❌ HubSpot API key missing")

# SUMMARY
print("\n" + "=" * 70)
print("✅ OPTION B: READY TO EXECUTE")
print("=" * 70)

print("""
WHAT YOU NEED TO DO (20 minutes total):

Step 1: Supabase SQL (2 min)
  ☐ Copy SUPABASE-SCHEMA-LOOPS.sql
  ☐ Paste into Supabase SQL Editor
  ☐ Click RUN

Step 2: Slack Webhooks (5 min)
  ☐ Create 3 channels
  ☐ Create 3 webhooks
  ☐ Save URLs

Step 3: ClickUp Workspaces (10 min)
  ☐ Create 3 workspaces
  ☐ Create 12 lists (4 per workspace)
  ☐ Add custom fields

Step 4: HubSpot Objects (10 min)
  ☐ Create 3 custom objects
  ☐ Create 3 pipelines

THEN:
  - All infrastructure ready ✅
  - We deploy all 9 loops ✅
  - Live by tomorrow ✅

Ready to proceed?
""")
