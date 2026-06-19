#!/usr/bin/env python3
"""
Export all 618 Supabase ventures with semantic capabilities and matched repos to CSV.
Creates: ventures_with_capabilities.csv
"""

import json
import os
import csv
import requests
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv("/Users/acebless/Documents/.env")

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

# Load socraticode profiles
with open("socraticode_profiles.json", "r") as f:
    repos = json.load(f)

def get_ventures():
    """Fetch all ventures from Supabase with pagination"""
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }

    ventures = []
    offset = 0
    limit = 100

    while True:
        try:
            response = requests.get(
                f"{SUPABASE_URL}/rest/v1/ventures?limit={limit}&offset={offset}",
                headers=headers
            )
            batch = response.json()
            if not batch:
                break
            ventures.extend(batch)
            offset += limit
        except Exception as e:
            print(f"Error fetching ventures: {e}")
            break

    return ventures

def extract_capabilities(venture):
    """Extract required_capabilities from venture metadata"""
    metadata = venture.get('metadata') or {}
    if isinstance(metadata, str):
        try:
            metadata = json.loads(metadata)
        except:
            metadata = {}
    return metadata.get('required_capabilities', [])

def match_repos(venture_caps, owned_repos):
    """Match repos to venture based on capability overlap"""
    matches = []
    for repo_name, repo_data in owned_repos.items():
        repo_caps = repo_data.get('capabilities', [])
        overlap = len(set(venture_caps) & set(repo_caps))
        if overlap > 0:
            match_pct = (overlap / max(len(venture_caps), 1)) * 100
            matches.append((repo_name, overlap, match_pct))

    return sorted(matches, key=lambda x: (-x[1], -x[2]))[:3]

print("\n" + "="*80)
print("EXPORT VENTURES WITH SEMANTIC CAPABILITIES")
print("="*80 + "\n")

print("📥 Fetching ventures from Supabase...")
ventures = get_ventures()
print(f"✅ Loaded {len(ventures)} ventures\n")

print("📤 Exporting to CSV...")
with open("ventures_with_capabilities.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "venture_id", "venture_name", "sector", "business_domain",
        "required_capabilities", "capability_count",
        "top_repo_1", "top_repo_1_match_pct",
        "top_repo_2", "top_repo_2_match_pct",
        "top_repo_3", "top_repo_3_match_pct"
    ])

    for venture in ventures:
        venture_id = venture.get('id', '')
        venture_name = venture.get('venture_name', venture.get('name', ''))
        sector = venture.get('sector', '')
        business_domain = venture.get('business_domain', '')

        capabilities = extract_capabilities(venture)
        matches = match_repos(capabilities, repos)

        row = [
            venture_id,
            venture_name,
            sector,
            business_domain,
            "|".join(capabilities),
            len(capabilities)
        ]

        for i in range(3):
            if i < len(matches):
                repo_name, overlap, match_pct = matches[i]
                row.append(repo_name)
                row.append(f"{match_pct:.1f}%")
            else:
                row.append("")
                row.append("")

        writer.writerow(row)

print(f"✅ Exported {len(ventures)} ventures to ventures_with_capabilities.csv\n")

# Summary statistics
print("📊 EXPORT SUMMARY:")
print("-" * 80)

sectors = defaultdict(int)
cap_counts = defaultdict(int)

for venture in ventures:
    sector = venture.get('sector', 'unknown')
    sectors[sector] += 1
    caps = extract_capabilities(venture)
    cap_counts[len(caps)] += 1

print(f"{'Sector':<20} {'Count':<10}")
print("-" * 30)
for sector in sorted(sectors.keys()):
    print(f"{sector:<20} {sectors[sector]:<10}")

print(f"\n{'Capability Count':<20} {'Ventures':<10}")
print("-" * 30)
for count in sorted(cap_counts.keys()):
    print(f"{count:<20} {cap_counts[count]:<10}")

print("\n" + "="*80)
print("✅ EXPORT COMPLETE")
print("="*80 + "\n")
