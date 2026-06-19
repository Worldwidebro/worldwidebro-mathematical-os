#!/usr/bin/env python3
"""
Reclassify ventures from generic sectors to Worldwidebro Holdings taxonomy
"""

import os
from supabase import create_client
from collections import defaultdict

SUPABASE_URL = "https://cyhzilqldouzgynacqpe.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN5aHppbHFsZG91emd5bmFjcXBlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NDY2OTQwOCwiZXhwIjoyMDgwMjQ1NDA4fQ.1M6V3fR9rNxonIJvtNkV4isrZK9VIvy3J-gNLJGMp2k"

# Mapping from generic sectors to Worldwidebro sectors
SECTOR_MAPPING = {
    "e-commerce": "market",
    "operations": "infra",
    "technology": "devtools",
    "emerging": "ai",
    "education": "edtech",
    "community": "market",
    "financial": "fintech",
}

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Fetching ventures from Supabase...")
response = supabase.table("ventures").select("id, name, sector").limit(1000).execute()
ventures = response.data if response.data else []

# Count ventures to reclassify
to_reclassify = [v for v in ventures if v.get("sector") in SECTOR_MAPPING]
print(f"Total ventures: {len(ventures)}")
print(f"Ventures to reclassify: {len(to_reclassify)}")

# Group by current sector
by_sector = defaultdict(list)
for v in to_reclassify:
    by_sector[v["sector"]].append(v)

print("\nReclassification plan:")
for old_sector, ventures_list in sorted(by_sector.items()):
    new_sector = SECTOR_MAPPING[old_sector]
    print(f"  {old_sector} → {new_sector}: {len(ventures_list)} ventures")

# Apply reclassification
print("\nApplying reclassification...")
updated = 0
for v in to_reclassify:
    old_sector = v["sector"]
    new_sector = SECTOR_MAPPING[old_sector]
    try:
        supabase.table("ventures").update({"sector": new_sector}).eq("id", v["id"]).execute()
        updated += 1
        if updated % 100 == 0:
            print(f"  Updated {updated}/{len(to_reclassify)}...")
    except Exception as e:
        print(f"  ✗ Error: {e}")

print(f"\n✓ Reclassified {updated} ventures")
print("\nNew sector distribution:")
response = supabase.table("ventures").select("sector").limit(1000).execute()
ventures = response.data if response.data else []
dist = defaultdict(int)
for v in ventures:
    dist[v.get("sector", "untagged")] += 1

for sector, count in sorted(dist.items(), key=lambda x: x[1], reverse=True):
    print(f"  {sector}: {count}")
