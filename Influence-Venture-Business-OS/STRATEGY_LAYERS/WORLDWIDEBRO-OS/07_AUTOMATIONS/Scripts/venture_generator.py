#!/usr/bin/env python3
"""
EC-001 Template Generator — Populate all 686+ ventures using Ollama + qwen2.5:32b
Reads EC-001 as reference, generates sector-specific files for each venture folder.
"""
import json
import os
import re
import sys
from pathlib import Path
from typing import Any
import requests
from datetime import datetime

VAULT = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault"
VENTURES_DIR = VAULT / "07-BUSINESS-STRATEGY" / "ventures"
EC_001_TEMPLATE = VENTURES_DIR / "E-Commerce" / "EC-001-Angels-in-Daylight"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:32b"

# File templates — what goes into each generated folder
FILE_TEMPLATES = {
    "VENTURE.json": {
        "required": True,
        "prompt": "Generate a sector-specific VENTURE.json for {venture_name} in the {sector} sector. Use this as reference: {ec_001_json}. Keep the same structure but adapt all values for a {business_model} business model. Return ONLY valid JSON, no markdown."
    },
    "README.md": {
        "required": True,
        "prompt": "Generate a README.md for {venture_name} ({venture_code}) in {sector}. Reference: {ec_001_readme}. Adapt mission, ICP, first dollar path, and key metrics for a {business_model} business. Use proper Markdown syntax."
    },
    "playbooks/go-to-market.md": {
        "required": True,
        "prompt": "Create a go-to-market playbook for {venture_name} in {sector} with {business_model} model. Include: channels, launch sequence, first 90 days, success metrics."
    },
    "playbooks/unit-economics.md": {
        "required": True,
        "prompt": "Create unit economics playbook for {venture_name} ({business_model}). Include: CAC, LTV, gross margin targets, break-even point, ARR model."
    },
    "dashboards/kpi-tracker.md": {
        "required": True,
        "prompt": "Create KPI tracker dashboard for {venture_name}. Include: weekly MRR, CAC, LTV, churn, NPS, conversion funnels in Dataview format."
    },
    "automations/lead-scoring.md": {
        "required": True,
        "prompt": "Create automated lead scoring system for {venture_name} ({business_model}). Define: lead sources, scoring rules, qualification triggers, handoff to sales."
    },
    "prompts/agent-directive.md": {
        "required": True,
        "prompt": "Write an agent directive for Claude operating {venture_name}. Include: goals, constraints, decision rules, escalation paths, success criteria."
    },
    "data/customer-cohorts.json": {
        "required": True,
        "prompt": "Generate a JSON structure for customer cohorts in {venture_name}. Include: acquisition channel, LTV, churn rate, segment name, ICP attributes. Return valid JSON."
    }
}


def load_ec_001():
    """Load EC-001 template files."""
    with open(EC_001_TEMPLATE / "VENTURE.json") as f:
        venture_json = json.load(f)
    with open(EC_001_TEMPLATE / "README.md") as f:
        readme_md = f.read()
    return venture_json, readme_md


def get_ventures_from_supabase():
    """Fetch venture metadata from Supabase."""
    try:
        from supabase import create_client
        url = os.getenv("SUPABASE_URL", "")
        key = os.getenv("SUPABASE_KEY", "")
        if not url or not key:
            print("⚠️  SUPABASE_URL/KEY not set, using vault folders as source")
            return None

        client = create_client(url, key)
        response = client.table("ventures").select("*").limit(700).execute()
        return {v["id"]: v for v in response.data} if response.data else {}
    except Exception as e:
        print(f"⚠️  Supabase load failed ({e}), using vault folders")
        return None


def discover_ventures():
    """Walk vault and find all venture folders with their metadata."""
    ventures = {}

    for sector_dir in VENTURES_DIR.iterdir():
        if not sector_dir.is_dir() or sector_dir.name.startswith("."):
            continue

        sector = sector_dir.name

        for venture_dir in sector_dir.iterdir():
            if not venture_dir.is_dir() or venture_dir.name.startswith("."):
                continue

            venture_code = venture_dir.name.split("-")[0] if "-" in venture_dir.name else "XX"
            venture_name = "-".join(venture_dir.name.split("-")[1:]) if "-" in venture_dir.name else venture_dir.name

            # Check if files exist
            has_readme = (venture_dir / "README.md").exists()
            has_venture_json = (venture_dir / "VENTURE.json").exists()

            ventures[venture_dir.name] = {
                "path": venture_dir,
                "sector": sector,
                "code": venture_code,
                "name": venture_name.replace("-", " ").title(),
                "missing_files": not (has_readme and has_venture_json),
                "is_template": venture_dir == EC_001_TEMPLATE
            }

    return ventures


def generate_content(venture_name, venture_code, sector, business_model, ec_001_json, ec_001_readme, file_type):
    """Call Ollama to generate content for a file."""
    template = FILE_TEMPLATES.get(file_type, {})
    if not template:
        return None

    prompt = template["prompt"].format(
        venture_name=venture_name,
        venture_code=venture_code,
        sector=sector,
        business_model=business_model,
        ec_001_json=json.dumps(ec_001_json, indent=2)[:500],  # First 500 chars as context
        ec_001_readme=ec_001_readme[:1000]  # First 1000 chars
    )

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=120
        )
        if response.status_code == 200:
            return response.json()["response"].strip()
        else:
            print(f"❌ Ollama error: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Ollama request failed: {e}")
        return None


def create_venture_json(template_json, venture_name, venture_code, sector, business_model):
    """Create VENTURE.json by adapting template."""
    sector_map = {"E-Commerce": "ec", "Financial": "fin", "Software-Tech": "sw",
                  "Beauty-Wellness": "bw", "Food-Hospitality": "fh", "Logistics": "log"}

    venture_json = {
        "code": venture_code,
        "name": venture_name,
        "sector": sector.lower().replace(" ", "-").replace("-", "_"),
        "sector_code": sector_map.get(sector, "xx"),
        "lead_agent": "The Founder",
        "github_repo_url": f"https://github.com/Worldwidebro/{venture_code.lower()}-{venture_name.lower().replace(' ', '-')}",
        "supabase_id": venture_code.lower(),
        "clickup_task_id": "",
        "business_model": business_model,
        "phase": 0,
        "progress_pct": 0,
        "first_dollar_price": 29,
        "first_dollar_product": f"{venture_name} MVP",
        "target_mrr": 5000,
        "target_arpu": 100,
        "target_cac": 25,
        "target_ltv": 300,
        "gross_margin_pct": 60,
        "status": "planning",
        "agent_assigned": "claude-code",
        "vault_path": f"07-BUSINESS-STRATEGY/ventures/{sector}/{venture_code}-{venture_name.replace(' ', '-')}",
        "entity": f"{venture_name} LLC",
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
    return venture_json


def create_readme(venture_name, venture_code, sector, business_model):
    """Generate basic README structure."""
    return f"""---
tags: [venture, {sector.lower().replace(" ", "-")}, {venture_code.lower()}]
sector: {sector}
code: {venture_code}
status: phase-0
phase: 0
updated: {datetime.now().strftime("%Y-%m-%d")}
---

# {venture_code} — {venture_name}

> {business_model} venture in {sector} sector.

**GitHub:** https://github.com/Worldwidebro/{venture_code.lower()}-{venture_name.lower().replace(' ', '-')}
**Sector:** {sector} | **Lead Agent:** The Founder
**Target MRR:** $5,000 | **First Dollar Price:** $29

---

## Mission

{venture_name} is building a {business_model} product/service in the {sector} market.

## ICP (Ideal Customer Profile)

| Attribute | Description |
|-----------|-------------|
| Segment | Primary market segment |
| Value Prop | Key value proposition |
| Channels | Go-to-market channels |
| Trigger | Primary conversion trigger |

## First Dollar Path

1. Define MVP scope
2. Launch to early adopters
3. Iterate on feedback
4. Scale to full market

## Key Files

| File | Purpose |
|------|---------|
| [[{venture_code}-{venture_name.replace(" ", "-")}/VENTURE]] | Machine-readable data |
| [[{venture_code}-{venture_name.replace(" ", "-")}/execution]] | Current phase & blockers |
| [[{venture_code}-{venture_name.replace(" ", "-")}/offer]] | Offer & pricing |
| [[{venture_code}-{venture_name.replace(" ", "-")}/ops]] | Operations & ICP |
| [[{venture_code}-{venture_name.replace(" ", "-")}/growth]] | Growth strategy |
| [[{venture_code}-{venture_name.replace(" ", "-")}/finance]] | Unit economics |
| [[{venture_code}-{venture_name.replace(" ", "-")}/agents]] | Agent assignments |
"""


def generate_venture(venture_path, venture_code, venture_name, sector, ec_001_json, ec_001_readme):
    """Generate all files for a venture."""
    # Skip template
    if venture_path == EC_001_TEMPLATE:
        return 0

    # Check if already complete
    if (venture_path / "README.md").exists() and (venture_path / "VENTURE.json").exists():
        missing = 0
        for file_path in ["playbooks/go-to-market.md", "dashboards/kpi-tracker.md", "automations/lead-scoring.md"]:
            if not (venture_path / file_path).exists():
                missing += 1
        if missing == 0:
            return 0  # Already complete

    print(f"\n📝 {venture_code} — {venture_name}")

    # Determine business model from context (fallback to sector-based guess)
    business_model = "DTC Model"

    files_created = 0

    # Create VENTURE.json
    venture_json = create_venture_json(ec_001_json, venture_name, venture_code, sector, business_model)
    venture_json_path = venture_path / "VENTURE.json"
    with open(venture_json_path, "w") as f:
        json.dump(venture_json, f, indent=2)
    files_created += 1
    print(f"  ✓ VENTURE.json")

    # Create README.md
    readme = create_readme(venture_name, venture_code, sector, business_model)
    readme_path = venture_path / "README.md"
    with open(readme_path, "w") as f:
        f.write(readme)
    files_created += 1
    print(f"  ✓ README.md")

    # Ensure folder structure
    for folder in ["automations", "dashboards", "playbooks", "prompts", "data"]:
        (venture_path / folder).mkdir(exist_ok=True)

    # Generate remaining files using Ollama (optional - use for quality files)
    for file_path in ["playbooks/go-to-market.md", "dashboards/kpi-tracker.md"]:
        file_full_path = venture_path / file_path
        if not file_full_path.exists():
            print(f"  → Generating {file_path}...", end=" ", flush=True)
            content = generate_content(venture_name, venture_code, sector, business_model,
                                      ec_001_json, ec_001_readme, file_path)
            if content:
                file_full_path.parent.mkdir(parents=True, exist_ok=True)
                with open(file_full_path, "w") as f:
                    f.write(content)
                files_created += 1
                print("✓")
            else:
                print("⚠️ skipped (Ollama timeout)")

    return files_created


def main():
    print("🚀 EC-001 Template Generator")
    print("=" * 60)

    if not EC_001_TEMPLATE.exists():
        print(f"❌ Template not found: {EC_001_TEMPLATE}")
        sys.exit(1)

    print(f"✓ EC-001 template found")

    # Load template
    ec_001_json, ec_001_readme = load_ec_001()
    print(f"✓ Loaded EC-001 reference (JSON + README)")

    # Discover ventures
    ventures = discover_ventures()
    total_ventures = len(ventures)
    ventures_needing_files = sum(1 for v in ventures.values() if v["missing_files"] and not v["is_template"])

    print(f"\n📊 Vault State")
    print(f"  Total ventures: {total_ventures}")
    print(f"  Needing file generation: {ventures_needing_files}")
    print(f"  Template: {sum(1 for v in ventures.values() if v['is_template'])} (skipped)")

    # Group by sector
    by_sector = {}
    for v in ventures.values():
        sector = v["sector"]
        if sector not in by_sector:
            by_sector[sector] = {"total": 0, "missing": 0}
        by_sector[sector]["total"] += 1
        if v["missing_files"] and not v["is_template"]:
            by_sector[sector]["missing"] += 1

    print(f"\n📍 By Sector")
    for sector in sorted(by_sector.keys()):
        stats = by_sector[sector]
        print(f"  {sector}: {stats['missing']}/{stats['total']} needing files")

    # Generate
    print(f"\n⏳ Generating files...")
    total_files_created = 0
    ventures_processed = 0

    for venture_code in sorted(ventures.keys()):
        v = ventures[venture_code]
        if v["is_template"]:
            continue

        try:
            files = generate_venture(v["path"], v["code"], v["name"], v["sector"],
                                    ec_001_json, ec_001_readme)
            total_files_created += files
            ventures_processed += 1

            if ventures_processed % 10 == 0:
                print(f"\n  [{ventures_processed}/{ventures_needing_files}]")
        except Exception as e:
            print(f"  ❌ {venture_code}: {e}")

    # Summary
    print(f"\n{'=' * 60}")
    print(f"✅ Generation Complete")
    print(f"  Ventures processed: {ventures_processed}")
    print(f"  Files created: {total_files_created}")
    print(f"  Avg files/venture: {total_files_created / max(ventures_processed, 1):.1f}")


if __name__ == "__main__":
    main()
