#!/usr/bin/env python3
"""
LOOP 1: Fetch Leads from 4 Sources
Run: /loop python3 loops/01-FETCH-LEADS.py --every 4h

Fetches leads from:
- SAM.gov (Federal Contracts API)
- USAspending.gov (Federal Spending API)
- Angi (Home Services Leads)
- HomeAdvisor (Partner API - optional)

Stores in Supabase leads table
Deduplicates by email
Reports count added per source
"""

import os
import sys
import requests
from datetime import datetime
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SAMGOV_API_KEY = os.getenv("SAMGOV_API_KEY", "")
ANGI_API_KEY = os.getenv("ANGI_API_KEY", "")
HOMEADVISOR_API_KEY = os.getenv("HOMEADVISOR_API_KEY", "")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ SUPABASE_URL or SUPABASE_KEY not in .env")
    sys.exit(1)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_existing_emails():
    """Get all existing emails to avoid duplicates"""
    try:
        response = supabase.table("leads").select("email").execute()
        return {lead["email"] for lead in response.data if lead.get("email")}
    except:
        return set()

def add_lead(source, email, phone, zip_code, title=""):
    """Add lead to Supabase"""
    try:
        supabase.table("leads").insert({
            "source": source,
            "email": email,
            "phone": phone,
            "zip": zip_code,
            "title": title,
            "status": "new"
        }).execute()
        return True
    except Exception as e:
        print(f"    Error adding {email}: {e}")
        return False

def fetch_samgov_leads():
    """Fetch from SAM.gov Opportunities API"""
    try:
        if not SAMGOV_API_KEY:
            print("    ⚠️  SAMGOV_API_KEY not set, skipping")
            return []

        url = "https://api.sam.gov/opportunities/v2/search"
        params = {
            "api_key": SAMGOV_API_KEY,
            "limit": 10,
            "postedFrom": "01/01/2024",
            "postedTo": "12/31/2024",
            "title": "electrical"
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        leads = []
        for opp in data.get("opportunities", []):
            email = opp.get("contact", {}).get("email", f"contact+{opp.get('id')}@sam.gov")
            leads.append({
                "email": email,
                "phone": opp.get("contact", {}).get("phone", "N/A"),
                "zip": opp.get("zip", "00000"),
                "title": opp.get("title", "Federal Opportunity")
            })
        return leads
    except Exception as e:
        print(f"    Error fetching SAM.gov: {e}")
        return []

def fetch_usaspending_leads():
    """Fetch from USAspending.gov API"""
    try:
        url = "https://api.usaspending.gov/api/v2/search/awards"
        params = {
            "keyword": "electrical",
            "award_type": "contract",
            "limit": 10
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        leads = []
        for award in data.get("results", []):
            email = award.get("recipient_email", f"recipient+{award.get('id')}@usaspending.gov")
            leads.append({
                "email": email,
                "phone": award.get("recipient_phone", "N/A"),
                "zip": award.get("recipient_zip", "00000"),
                "title": award.get("description", "Federal Award")
            })
        return leads
    except Exception as e:
        print(f"    Error fetching USAspending: {e}")
        return []

def fetch_angi_leads():
    """Fetch from Angi (via webhook setup)"""
    try:
        if not ANGI_API_KEY:
            print("    ℹ️  ANGI_API_KEY not set, skipping")
            return []

        print("    ℹ️  Angi uses webhook (receives leads, not polls)")
        return []
    except Exception as e:
        print(f"    Error with Angi setup: {e}")
        return []

def fetch_homeadvisor_leads():
    """Fetch from HomeAdvisor (partner API)"""
    try:
        if not HOMEADVISOR_API_KEY:
            print("    ℹ️  HOMEADVISOR_API_KEY not set (partner only)")
            return []

        print("    ℹ️  HomeAdvisor requires partnership agreement")
        return []
    except Exception as e:
        print(f"    Error with HomeAdvisor: {e}")
        return []

def fetch_leads_from_sources():
    """Fetch from all 4 sources"""
    all_leads = {}

    print("  📍 SAM.gov: Fetching...")
    all_leads["samgov"] = fetch_samgov_leads()

    print("  📍 USAspending: Fetching...")
    all_leads["usaspending"] = fetch_usaspending_leads()

    print("  📍 Angi: Fetching...")
    all_leads["angi"] = fetch_angi_leads()

    print("  📍 HomeAdvisor: Fetching...")
    all_leads["homeadvisor"] = fetch_homeadvisor_leads()

    return all_leads

def main():
    print(f"\n{'='*60}")
    print(f"LOOP 1: FETCH LEADS [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    print(f"{'='*60}\n")

    existing_emails = get_existing_emails()
    print(f"📊 Existing leads in database: {len(existing_emails)}\n")

    total_added = 0
    print("🔄 Fetching from all sources...\n")

    all_leads = fetch_leads_from_sources()

    print("\n💾 Adding leads to Supabase...\n")

    for source, leads in all_leads.items():
        added = 0
        for lead in leads:
            if lead["email"] not in existing_emails:
                if add_lead(
                    source,
                    lead["email"],
                    lead["phone"],
                    lead["zip"],
                    lead.get("title", "")
                ):
                    added += 1
                    existing_emails.add(lead["email"])
        print(f"  ✅ {source.upper()}: Added {added}/{len(leads)}")
        total_added += added

    print(f"\n{'='*60}")
    print(f"✅ TOTAL LEADS ADDED: {total_added}")
    print(f"📊 Total in database: {len(existing_emails)}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
