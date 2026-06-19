#!/usr/bin/env python3
"""
Step 5: Tag 575 Untagged Ventures by Sector
Analyzes venture names and descriptions to classify them into sectors.
Uses simple keyword matching and description analysis.
"""

import os
import sys
import json
from datetime import datetime
from supabase import create_client

# Supabase config
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN5aHppbHFsZG91emd5bmFjcXBlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NDY2OTQwOCwiZXhwIjoyMDgwMjQ1NDA4fQ.1M6V3fR9rNxonIJvtNkV4isrZK9VIvy3J-gNLJGMp2k")

# Sector keywords for classification
SECTOR_KEYWORDS = {
    "fintech": [
        "payment", "ledger", "blockchain", "crypto", "finance", "bank", "transaction",
        "wallet", "exchange", "defi", "smart contract", "tax", "insurance", "investment"
    ],
    "ai": [
        "ai", "artificial intelligence", "llm", "gpt", "neural", "machine learning", 
        "model", "automation", "intelligent", "workflow", "orchestration", "agent"
    ],
    "edtech": [
        "education", "learning", "course", "training", "skill", "school", "student",
        "teach", "tutor", "academy", "certification", "knowledge"
    ],
    "health": [
        "health", "medical", "healthcare", "wellness", "fitness", "wearable", "monitor",
        "doctor", "hospital", "therapy", "vital", "patient", "clinical"
    ],
    "infra": [
        "infrastructure", "platform", "orchestration", "deployment", "cloud", "devops",
        "repo", "repository", "agent", "system", "os", "framework"
    ],
    "market": [
        "marketplace", "template", "ecommerce", "commerce", "store", "shop", "vendor",
        "catalog", "product", "transaction", "creator economy"
    ],
    "devtools": [
        "developer", "dev tool", "code", "programming", "ide", "editor", "compiler",
        "framework", "library", "cursor", "vscode", "github", "cli"
    ]
}

def classify_venture(name: str, description: str) -> str:
    """Classify venture into sector based on name and description"""
    text = (name + " " + (description or "")).lower()
    
    scores = {sector: 0 for sector in SECTOR_KEYWORDS}
    
    for sector, keywords in SECTOR_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                scores[sector] += 1
    
    best_sector = max(scores, key=scores.get)
    if scores[best_sector] > 0:
        return best_sector
    return "market"  # Default fallback sector

def main():
    print(f"[{datetime.now().isoformat()}] Step 5: Tag 575 Untagged Ventures by Sector")
    print(f"  Supabase: {SUPABASE_URL}")
    print()

    # Connect to Supabase
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    print("[STEP 1] Fetching all ventures from Supabase...")
    try:
        response = supabase.table("ventures").select("id, name, description, sector").limit(1000).execute()
        ventures = response.data if response.data else []
        print(f"  ✓ Fetched {len(ventures)} ventures")
    except Exception as e:
        print(f"  ✗ Error fetching ventures: {e}")
        return False

    # Identify untagged ventures
    print("\n[STEP 2] Identifying untagged ventures...")
    untagged = [v for v in ventures if not v.get("sector") or v.get("sector") == ""]
    tagged = [v for v in ventures if v.get("sector") and v.get("sector") != ""]
    
    print(f"  Tagged: {len(tagged)}")
    print(f"  Untagged: {len(untagged)}")

    if not untagged:
        print(f"  ✓ All ventures already tagged!")
        return True

    print("\n[STEP 3] Classifying untagged ventures...")
    updates = []
    sector_distribution = {sector: 0 for sector in SECTOR_KEYWORDS}

    for i, venture in enumerate(untagged):
        sector = classify_venture(venture.get("name", ""), venture.get("description", ""))
        updates.append({
            "id": venture["id"],
            "sector": sector
        })
        sector_distribution[sector] += 1
        
        if (i + 1) % 100 == 0:
            print(f"  Classified {i + 1}/{len(untagged)} ventures...")

    # Show distribution
    print(f"\n[STEP 4] Distribution of classified ventures:")
    for sector, count in sorted(sector_distribution.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            print(f"  {sector}: {count}")

    # Apply updates to Supabase
    print(f"\n[STEP 5] Updating Supabase with {len(updates)} sector assignments...")
    updated_count = 0
    
    for update in updates:
        try:
            supabase.table("ventures").update({"sector": update["sector"]}).eq("id", update["id"]).execute()
            updated_count += 1
            if updated_count % 100 == 0:
                print(f"  Updated {updated_count}/{len(updates)} ventures...")
        except Exception as e:
            print(f"  ✗ Error updating venture {update['id']}: {e}")

    print(f"\n[SUMMARY]")
    print(f"  Total ventures: {len(ventures)}")
    print(f"  Tagged before: {len(tagged)}")
    print(f"  Tagged after: {len(tagged) + updated_count}")
    print(f"  Successfully classified: {updated_count}/{len(untagged)}")
    print(f"\n[NEXT] Step 6: Phase 1.2 Network Mapping & Wishlist Creation")

    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
