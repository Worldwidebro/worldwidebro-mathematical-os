#!/usr/bin/env python3
"""
Verify venture-to-repo matching at scale across all 618 ventures.
Shows sector-based distribution, top matching repos, and capability coverage.
"""

import json
import os
from dotenv import load_dotenv
from collections import defaultdict
import requests

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
            matches.append((repo_name, overlap, match_pct, repo_caps))

    return sorted(matches, key=lambda x: (-x[1], -x[2]))[:3]

print("\n" + "="*100)
print("VENTURE-TO-REPO MATCHING VERIFICATION (All 618 Ventures)")
print("="*100)

ventures = get_ventures()
print(f"\n📊 Fetched {len(ventures)} ventures from Supabase")

# Collect statistics by sector
sector_stats = defaultdict(lambda: {"count": 0, "matched": 0, "avg_matches": 0, "repos": defaultdict(int)})
repo_hub_stats = defaultdict(lambda: {"ventures_served": 0, "sectors": set()})
unmatched_ventures = []

total_matches = 0
ventures_with_matches = 0

print("\n🔍 Analyzing venture-to-repo matches by sector...\n")

for venture in ventures:
    sector = venture.get('sector', 'unknown')
    venture_name = venture.get('venture_name', venture.get('name', 'unknown'))
    venture_caps = extract_capabilities(venture)

    sector_stats[sector]["count"] += 1

    if venture_caps:
        matches = match_repos(venture_caps, repos)
        if matches:
            sector_stats[sector]["matched"] += 1
            ventures_with_matches += 1
            total_matches += len(matches)

            for repo_name, overlap, match_pct, repo_caps in matches:
                repo_hub_stats[repo_name]["ventures_served"] += 1
                repo_hub_stats[repo_name]["sectors"].add(sector)
        else:
            unmatched_ventures.append((venture_name, sector, venture_caps))

# Print sector-by-sector analysis
print("📈 SECTOR ANALYSIS:")
print("-" * 100)
print(f"{'Sector':<30} {'Ventures':<12} {'Matched':<12} {'Coverage %':<15} {'Avg Matches/V':<15}")
print("-" * 100)

for sector in sorted(sector_stats.keys()):
    stats = sector_stats[sector]
    coverage = (stats["matched"] / stats["count"] * 100) if stats["count"] > 0 else 0
    avg_matches = (total_matches / ventures_with_matches) if ventures_with_matches > 0 else 0
    print(f"{sector:<30} {stats['count']:<12} {stats['matched']:<12} {coverage:<14.1f}% {avg_matches:<14.1f}")

print("-" * 100)
total_ventures = len(ventures)
overall_coverage = (ventures_with_matches / total_ventures * 100) if total_ventures > 0 else 0
print(f"{'TOTAL':<30} {total_ventures:<12} {ventures_with_matches:<12} {overall_coverage:<14.1f}% {(total_matches/ventures_with_matches if ventures_with_matches > 0 else 0):<14.1f}")

# Print repo hub analysis
print("\n\n🌟 REPO HUB ANALYSIS (Repos serving multiple ventures):")
print("-" * 100)
print(f"{'Repository':<30} {'Ventures Served':<20} {'Sectors':<40}")
print("-" * 100)

for repo_name in sorted(repo_hub_stats.keys(), key=lambda x: -repo_hub_stats[x]["ventures_served"])[:10]:
    stats = repo_hub_stats[repo_name]
    sectors_served = ", ".join(sorted(stats["sectors"]))[:38]
    print(f"{repo_name:<30} {stats['ventures_served']:<20} {sectors_served:<40}")

# Sample ventures from different sectors
print("\n\n📋 SAMPLE VENTURE MATCHES (One per sector):")
print("-" * 100)

shown_sectors = set()
for venture in ventures:
    sector = venture.get('sector', 'unknown')
    if sector in shown_sectors or len(shown_sectors) >= 5:
        continue

    shown_sectors.add(sector)
    venture_name = venture.get('venture_name', venture.get('name', 'unknown'))
    venture_caps = extract_capabilities(venture)
    matches = match_repos(venture_caps, repos)

    if matches:
        print(f"\n✅ {venture_name} ({sector})")
        print(f"   Required Capabilities: {venture_caps}")
        for repo_name, overlap, match_pct, repo_caps in matches:
            print(f"   → {repo_name}: {match_pct:.0f}% match ({overlap}/{len(venture_caps)} capabilities)")

# Capability coverage summary
print("\n\n📊 CAPABILITY COVERAGE SUMMARY:")
print("-" * 100)

all_capabilities = set()
for repo_data in repos.values():
    all_capabilities.update(repo_data.get('capabilities', []))

capability_coverage = defaultdict(int)
for venture in ventures:
    venture_caps = extract_capabilities(venture)
    for cap in venture_caps:
        capability_coverage[cap] += 1

print(f"{'Capability':<30} {'Ventures Using':<20} {'Repos Available':<20}")
print("-" * 100)

for cap in sorted(all_capabilities):
    venture_count = capability_coverage.get(cap, 0)
    repo_count = sum(1 for r in repos.values() if cap in r.get('capabilities', []))
    print(f"{cap:<30} {venture_count:<20} {repo_count:<20}")

print("\n" + "="*100)
print("✅ VERIFICATION COMPLETE")
print("="*100 + "\n")

if unmatched_ventures:
    print(f"⚠️  {len(unmatched_ventures)} ventures with no repo matches (likely missing capability inference):")
    for v_name, sector, caps in unmatched_ventures[:5]:
        print(f"   - {v_name} ({sector}): {caps}")
