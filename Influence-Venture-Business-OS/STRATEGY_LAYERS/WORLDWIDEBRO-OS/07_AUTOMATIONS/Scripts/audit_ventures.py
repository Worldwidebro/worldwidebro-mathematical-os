#!/usr/bin/env python3
"""
Phase 1.1: Product Audit
Query all 687 ventures from Supabase and categorize by:
- sector (inferred from product description)
- revenue potential (market size × price point × target market)
- execution readiness (product completeness, team, timeline)
"""

import os
import requests
import json
from collections import defaultdict

SUPABASE_URL = "https://cyhzilqldouzgynacqpe.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
}

def query_ventures():
    """Fetch all 687 ventures with key fields"""
    url = f"{SUPABASE_URL}/rest/v1/ventures?select=id,name,product_description,service_type,target_market,price_point,sector,status&limit=1000"
    response = requests.get(url, headers=headers, timeout=30)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return []

def analyze_ventures(ventures):
    """Categorize and score ventures"""
    
    sector_counts = defaultdict(int)
    status_counts = defaultdict(int)
    price_ranges = defaultdict(int)
    
    incomplete_data = []
    high_value = []
    
    for v in ventures:
        sector = v.get("sector") or "untagged"
        status = v.get("status") or "unknown"
        price = v.get("price_point") or 0
        
        sector_counts[sector] += 1
        status_counts[status] += 1
        
        # Classify by price
        if price > 10000:
            price_ranges["enterprise (>$10k)"] += 1
        elif price > 1000:
            price_ranges["mid-market ($1k-$10k)"] += 1
        elif price > 0:
            price_ranges["smb ($0-$1k)"] += 1
        else:
            price_ranges["unknown"] += 1
        
        # Check data completeness
        missing = []
        if not v.get("product_description") or len(str(v.get("product_description", "")).strip()) < 20:
            missing.append("description")
        if not v.get("target_market"):
            missing.append("market")
        if not v.get("price_point"):
            missing.append("pricing")
        if not v.get("sector"):
            missing.append("sector")
        
        if missing:
            incomplete_data.append({
                "id": v.get("id"),
                "name": v.get("name"),
                "missing": missing
            })
        else:
            # Estimate value: enterprise pricing + defined market = likely high-value
            if price > 5000 and v.get("target_market"):
                high_value.append({
                    "id": v.get("id"),
                    "name": v.get("name"),
                    "price": price,
                    "market": v.get("target_market"),
                    "sector": sector
                })
    
    return {
        "total": len(ventures),
        "sector_distribution": dict(sector_counts),
        "status_distribution": dict(status_counts),
        "price_distribution": dict(price_ranges),
        "high_value_count": len(high_value),
        "incomplete_count": len(incomplete_data),
        "high_value_samples": sorted(high_value, key=lambda x: x["price"], reverse=True)[:10],
        "incomplete_samples": incomplete_data[:15]
    }

if __name__ == "__main__":
    print("=" * 80)
    print("PHASE 1.1: PRODUCT AUDIT - VENTURE CATEGORIZATION")
    print("=" * 80)
    
    ventures = query_ventures()
    print(f"\n✓ Fetched {len(ventures)} ventures from Supabase")
    
    analysis = analyze_ventures(ventures)
    
    print(f"\nTotal Ventures: {analysis['total']}")
    print(f"\nSector Distribution:")
    for sector, count in sorted(analysis['sector_distribution'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {sector}: {count}")
    
    print(f"\nStatus Distribution:")
    for status, count in sorted(analysis['status_distribution'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {status}: {count}")
    
    print(f"\nPrice Point Distribution:")
    for range_name, count in sorted(analysis['price_distribution'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {range_name}: {count}")
    
    print(f"\nData Completeness:")
    print(f"  Complete (all fields): {analysis['total'] - analysis['incomplete_count']}")
    print(f"  Incomplete (missing fields): {analysis['incomplete_count']}")
    
    print(f"\nHigh-Value Opportunities (price > $5K):")
    print(f"  Count: {analysis['high_value_count']}")
    print(f"\n  Top 10 Samples:")
    for v in analysis['high_value_samples']:
        print(f"    {v['id']}: {v['name']} (${v['price']}) → {v['market']}")
    
    print(f"\nIncomplete Data Samples (need enrichment):")
    for v in analysis['incomplete_samples']:
        print(f"    {v['id']}: {v['name']} (missing: {', '.join(v['missing'])})")
    
    # Save to file
    with open('/Users/acebless/Documents/product_audit_results.json', 'w') as f:
        json.dump(analysis, f, indent=2)
    
    print("\n✓ Full results saved to product_audit_results.json")
    print("=" * 80)
