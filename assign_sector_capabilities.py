#!/usr/bin/env python3
"""
Assign sector-specific and domain-specific capabilities to all 618 ventures.
Maps business sectors/domains to semantic capabilities from SocratiCode inventory.
"""

import json
import os
import requests
from dotenv import load_dotenv

load_dotenv("/Users/acebless/Documents/.env")

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

# Sector-to-capability mapping based on domain needs
SECTOR_CAPABILITIES = {
    "hrms": ["api", "database", "authentication", "dashboard", "monitoring", "security"],
    "ai": ["api", "database", "knowledge-graph", "monitoring"],
    "con": ["api", "database", "construction", "workspace", "dashboard"],
    "devtools": ["api", "database", "authentication", "dashboard", "monitoring"],
    "edtech": ["api", "database", "dashboard", "workspace", "authentication"],
    "fintech": ["api", "database", "authentication", "security", "monitoring", "payment"],
    "health": ["api", "database", "security", "monitoring", "authentication"],
    "infra": ["api", "database", "monitoring", "security", "authentication"],
    "market": ["api", "database", "dashboard", "portfolio", "authentication"],
    "re": ["api", "database", "dashboard", "portfolio", "workspace"],
    "pitch": ["api", "database", "pitch", "dashboard", "portfolio"],
    "simulation": ["api", "database", "simulation", "knowledge-graph"],
}

# Domain keywords for additional capability inference
DOMAIN_KEYWORDS = {
    "authentication": ["auth", "login", "identity", "sso", "oauth", "credentials", "2fa"],
    "dashboard": ["dashboard", "analytics", "visualiz", "report", "chart", "metric"],
    "knowledge-graph": ["knowledge", "graph", "semantic", "ontology", "rag", "llm"],
    "monitoring": ["monitor", "alert", "metrics", "observ", "logging", "metric"],
    "security": ["security", "encrypt", "auth", "compliance", "audit", "forensic"],
    "payment": ["payment", "billing", "invoice", "transaction", "stripe", "paypal"],
    "portfolio": ["portfolio", "listing", "catalog", "inventory", "project"],
    "construction": ["construction", "build", "project", "site", "contractor"],
    "workspace": ["collab", "workspace", "team", "kanban", "task", "project management"],
    "simulation": ["simulation", "model", "forecast", "scenario"],
}

def get_ventures(limit=1000):
    """Fetch ventures from Supabase with pagination"""
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }

    ventures = []
    offset = 0

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
            print(f"  📥 Fetched {len(ventures)} ventures...")
        except Exception as e:
            print(f"  ❌ Error: {e}")
            break

    return ventures

def infer_capabilities(venture):
    """Infer capabilities based on sector and business_domain"""
    sector = venture.get('sector', 'market').lower()
    business_domain = (venture.get('business_domain', '') or '').lower()

    # Start with sector-based capabilities
    caps = set(SECTOR_CAPABILITIES.get(sector, ["api", "database"]))

    # Add domain-based capabilities
    for capability, keywords in DOMAIN_KEYWORDS.items():
        if any(kw in business_domain for kw in keywords):
            caps.add(capability)

    # Ensure base capabilities always present
    caps.add("api")
    caps.add("database")

    return sorted(list(caps))

def update_venture_capabilities(venture_id, capabilities):
    """Update venture's metadata with required_capabilities"""
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }

    # Prepare update payload
    metadata = {"required_capabilities": capabilities}
    update_data = {"metadata": metadata}

    try:
        response = requests.patch(
            f"{SUPABASE_URL}/rest/v1/ventures?id=eq.{venture_id}",
            headers=headers,
            json=update_data
        )
        return response.status_code in [200, 204]
    except Exception as e:
        print(f"  ❌ Error updating venture {venture_id}: {e}")
        return False

print("\n" + "="*80)
print("ASSIGN SECTOR CAPABILITIES TO ALL VENTURES")
print("="*80 + "\n")

print("📥 Fetching all ventures...")
ventures = get_ventures()
print(f"✅ Loaded {len(ventures)} ventures\n")

print("🔄 Inferring and assigning capabilities...")
success = 0
updated_by_sector = {}

for i, venture in enumerate(ventures):
    venture_id = venture.get('id')
    sector = venture.get('sector', 'market')
    capabilities = infer_capabilities(venture)

    if update_venture_capabilities(venture_id, capabilities):
        success += 1
        updated_by_sector[sector] = updated_by_sector.get(sector, 0) + 1

    if (i + 1) % 100 == 0:
        print(f"  ✅ Processed {i+1}/{len(ventures)} ventures ({success} updated)")

print(f"\n✅ Successfully updated {success}/{len(ventures)} ventures")

# Show distribution by sector
print("\n📊 Updates by sector:")
for sector in sorted(updated_by_sector.keys()):
    count = updated_by_sector[sector]
    caps = SECTOR_CAPABILITIES.get(sector, ["api", "database"])
    print(f"  {sector:<15} {count:>3} ventures → {len(caps)} capabilities: {', '.join(caps)}")

print("\n" + "="*80)
print("✅ CAPABILITY ASSIGNMENT COMPLETE")
print("="*80 + "\n")
