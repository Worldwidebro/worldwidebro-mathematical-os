#!/usr/bin/env python3
"""
Phase 1.1 Product Audit
Query ventures and categorize by sector, value, and completeness
"""
import sys
sys.path.insert(0, '/Users/acebless/.claude/projects/-Users-acebless-Documents')

# Try to import the Supabase client if available
try:
    from supabase import create_client, Client
    url = "https://cyhzilqldouzgynacqpe.supabase.co"
    # Try to get key from various sources
    import os
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_KEY") or ""
    
    if not key:
        print("⚠ No API key found in environment variables")
        print("  Checked: SUPABASE_SERVICE_ROLE_KEY, SUPABASE_KEY")
        print("\nTo set it: export SUPABASE_SERVICE_ROLE_KEY='your-key'")
        sys.exit(1)
    
    client: Client = create_client(url, key)
    
    # Query ventures
    response = client.table("ventures").select("id,name,sector,status,price_point,product_description,target_market").execute()
    
    print(f"✓ Fetched {len(response.data)} ventures")
    
except ImportError:
    print("Supabase client not installed. Using REST API instead...")
    import requests
    import os
    
    # Try reading from .vercel or other config
    config_paths = [
        "/Users/acebless/Documents/.env.local",
        "/Users/acebless/Documents/.env",
        "/Users/acebless/.env",
        "/Users/acebless/.supabase_key"
    ]
    
    key = None
    for path in config_paths:
        try:
            with open(path) as f:
                for line in f:
                    if "SUPABASE_SERVICE_ROLE_KEY" in line:
                        key = line.split("=")[1].strip().strip("'\"")
                        break
        except:
            pass
    
    if not key:
        print("ERROR: Could not find Supabase API key")
        print("Places checked:", config_paths)
        print("\nPlease set: export SUPABASE_SERVICE_ROLE_KEY='your-key'")
        sys.exit(1)
    
    url = "https://cyhzilqldouzgynacqpe.supabase.co/rest/v1/ventures"
    headers = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    
    print(f"Using API key: {key[:20]}...")
    response = requests.get(
        f"{url}?select=*&limit=1000",
        headers=headers,
        timeout=30
    )
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.text)
        sys.exit(1)
    
    ventures = response.json()
    print(f"✓ Fetched {len(ventures)} ventures")
    
    # Analyze
    from collections import defaultdict
    sectors = defaultdict(int)
    statuses = defaultdict(int)
    prices = []
    
    for v in ventures:
        sectors[v.get("sector") or "untagged"] += 1
        statuses[v.get("status") or "unknown"] += 1
        if v.get("price_point"):
            prices.append(v["price_point"])
    
    print("\n" + "="*70)
    print("SECTOR DISTRIBUTION (687 ventures):")
    print("="*70)
    for sector, count in sorted(sectors.items(), key=lambda x: x[1], reverse=True):
        pct = (count / len(ventures)) * 100
        print(f"  {sector:<30} {count:>4} ({pct:>5.1f}%)")
    
    print("\n" + "="*70)
    print("STATUS DISTRIBUTION:")
    print("="*70)
    for status, count in sorted(statuses.items(), key=lambda x: x[1], reverse=True):
        pct = (count / len(ventures)) * 100
        print(f"  {status:<30} {count:>4} ({pct:>5.1f}%)")
    
    if prices:
        print("\n" + "="*70)
        print("PRICING DISTRIBUTION:")
        print("="*70)
        print(f"  With pricing: {len([p for p in prices if p > 0])}")
        print(f"  Average: ${sum(prices)/len(prices):.2f}")
        print(f"  Min: ${min(prices):.2f}")
        print(f"  Max: ${max(prices):.2f}")

