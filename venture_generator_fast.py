#!/usr/bin/env python3
"""
Fast Venture File Generator — Populate all 116 ventures in seconds.
Creates VENTURE.json + README.md + folder structure for each venture.
"""
import json
import sys
from pathlib import Path
from datetime import datetime

VAULT = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault"
VENTURES_DIR = VAULT / "07-BUSINESS-STRATEGY" / "ventures"
EC_001_TEMPLATE = VENTURES_DIR / "E-Commerce" / "EC-001-Angels-in-Daylight"

SECTOR_MAP = {
    "E-Commerce": "ec",
    "Beauty-Wellness": "bw",
    "Financial": "fin",
    "Software-Tech": "sw",
    "Food-Hospitality": "fh",
    "Logistics": "log",
    "Construction": "con",
    "Community": "com",
    "Education": "edu",
    "Emerging": "emg",
    "Fitness-Sports": "fit",
    "Media-Content": "med",
    "Operations": "ops",
    "Professional-Services": "ps",
    "Specialized": "spec",
    "Technology": "tech"
}

BUSINESS_MODELS_BY_SECTOR = {
    "E-Commerce": "DTC Drop Model",
    "Beauty-Wellness": "Subscription Service",
    "Financial": "SaaS Platform",
    "Software-Tech": "B2B SaaS",
    "Food-Hospitality": "DTC + Events",
    "Logistics": "Logistics Network",
    "Construction": "Project Management",
    "Community": "Membership Platform",
    "Education": "Online Academy",
    "Emerging": "MVP Exploration",
    "Fitness-Sports": "Membership + Digital",
    "Media-Content": "Content Monetization",
    "Operations": "Process Automation",
    "Professional-Services": "Services + Productization",
    "Specialized": "Niche Solution",
    "Technology": "Developer Platform"
}


def load_ec_001():
    """Load EC-001 template."""
    with open(EC_001_TEMPLATE / "VENTURE.json") as f:
        return json.load(f)


def create_venture_json(template, code, name, sector, business_model):
    """Create VENTURE.json from template."""
    sector_code = SECTOR_MAP.get(sector, "xx")

    return {
        "code": code,
        "name": name,
        "sector": sector.lower().replace(" ", "_"),
        "sector_code": sector_code,
        "lead_agent": "The Founder",
        "github_repo_url": f"https://github.com/Worldwidebro/{code.lower()}-{name.lower().replace(' ', '-')}",
        "supabase_id": code.lower(),
        "clickup_task_id": "",
        "business_model": business_model,
        "phase": 0,
        "progress_pct": 0,
        "first_dollar_price": 29,
        "first_dollar_product": f"{name} MVP",
        "target_mrr": 5000,
        "target_arpu": 100,
        "target_cac": 25,
        "target_ltv": 300,
        "gross_margin_pct": 60,
        "status": "planning",
        "agent_assigned": "claude-code",
        "vault_path": f"07-BUSINESS-STRATEGY/ventures/{sector}/{code}-{name.replace(' ', '-')}",
        "entity": f"{name} LLC",
        "state_of_formation": "Wyoming",
        "ein": "",
        "platform": "Shopify",
        "payment": "Stripe",
        "digital_platform": "Gumroad",
        "primary_channel": "Email",
        "secondary_channels": [],
        "sku_count": 1,
        "avg_order_value": 75,
        "tags": [sector.lower().replace(" ", "-")]
    }


def create_readme(code, name, sector, business_model):
    """Create README.md."""
    return f"""---
tags: [venture, {sector.lower().replace(" ", "-")}, {code.lower()}]
sector: {sector}
code: {code}
status: phase-0
phase: 0
updated: {datetime.now().strftime("%Y-%m-%d")}
---

# {code} — {name}

> {business_model} venture in {sector}.

**GitHub:** https://github.com/Worldwidebro/{code.lower()}-{name.lower().replace(' ', '-')}
**Sector:** {sector} | **Lead Agent:** The Founder
**Target MRR:** $5,000 | **First Dollar:** $29

---

## Mission

{name} is a {business_model} business designed to serve the {sector} market.

## ICP (Ideal Customer Profile)

| Attribute | Value |
|-----------|-------|
| Primary Segment | TBD |
| Value Proposition | TBD |
| Acquisition Channel | Email + Content |
| LTV Target | $300 |

## First Dollar Path

1. **MVP Launch** → Validate problem-solution fit
2. **First 10 Customers** → Identify early adopter signals
3. **First $5K MRR** → Prove unit economics work
4. **Scale** → Systemize acquisition + delivery

## Key Metrics

- **CAC:** $25 | **LTV:** $300 | **Ratio:** 12x
- **Gross Margin:** 60% | **Payback Period:** 3 months
- **Target:** $5K MRR by end of Q3

---

## Key Files

| File | Purpose |
|------|---------|
| [[{code}-{name.replace(" ", "-")}/VENTURE]] | Machine-readable metadata |
| [[{code}-{name.replace(" ", "-")}/README]] | This file |
| [[{code}-{name.replace(" ", "-")}/ops]] | Operations + ICP |
| [[{code}-{name.replace(" ", "-")}/finance]] | Unit economics |
| [[{code}-{name.replace(" ", "-")}/growth]] | Growth strategy |

---

**Status:** Planning
**Phase:** 0
**Updated:** {datetime.now().strftime("%Y-%m-%d")}
"""


def create_venture_files(venture_path, code, name, sector):
    """Create all core files for a venture."""
    # Skip template
    if venture_path == EC_001_TEMPLATE:
        return 0

    # Load template once (moved outside to be more efficient)
    template = load_ec_001()
    business_model = BUSINESS_MODELS_BY_SECTOR.get(sector, "B2B Service")

    files_created = 0

    # Create VENTURE.json
    venture_json_path = venture_path / "VENTURE.json"
    if not venture_json_path.exists():
        venture_json = create_venture_json(template, code, name, sector, business_model)
        with open(venture_json_path, "w") as f:
            json.dump(venture_json, f, indent=2)
        files_created += 1

    # Create README.md
    readme_path = venture_path / "README.md"
    if not readme_path.exists():
        readme = create_readme(code, name, sector, business_model)
        with open(readme_path, "w") as f:
            f.write(readme)
        files_created += 1

    # Create folder structure
    for folder in ["automations", "dashboards", "playbooks", "prompts", "data"]:
        (venture_path / folder).mkdir(exist_ok=True)

    return files_created


def discover_and_generate():
    """Walk vault and generate files for all ventures."""
    print("🚀 Fast Venture Generator")
    print("=" * 70)

    total_ventures = 0
    total_created = 0
    ventures_by_sector = {}

    for sector_dir in sorted(VENTURES_DIR.iterdir()):
        if not sector_dir.is_dir() or sector_dir.name.startswith("."):
            continue

        sector = sector_dir.name
        if sector not in ventures_by_sector:
            ventures_by_sector[sector] = {"total": 0, "created": 0}

        for venture_dir in sorted(sector_dir.iterdir()):
            if not venture_dir.is_dir() or venture_dir.name.startswith("."):
                continue

            total_ventures += 1
            ventures_by_sector[sector]["total"] += 1

            # Parse venture code + name
            parts = venture_dir.name.split("-", 1)
            code = parts[0]
            name = parts[1].replace("-", " ").title() if len(parts) > 1 else "Unknown"

            # Skip if already fully populated
            if (venture_dir / "README.md").exists() and (venture_dir / "VENTURE.json").exists():
                continue

            # Generate
            created = create_venture_files(venture_dir, code, name, sector)
            if created > 0:
                total_created += created
                ventures_by_sector[sector]["created"] += 1
                print(f"  {code} — {name[:40]:40s} ✓ {created} files")

    # Summary
    print("\n" + "=" * 70)
    print(f"📊 Generation Complete\n")
    print("Sector Summary:")
    for sector in sorted(ventures_by_sector.keys()):
        stats = ventures_by_sector[sector]
        print(f"  {sector:25s} {stats['created']:3d}/{stats['total']:3d} generated")

    print(f"\n✅ Total Ventures: {total_ventures}")
    print(f"✅ Files Created: {total_created}")


if __name__ == "__main__":
    discover_and_generate()
