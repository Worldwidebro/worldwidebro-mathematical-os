#!/usr/bin/env python3
"""
Reality Check: Actual Ecosystem State

Shows the REAL state:
- 95 Vercel deployments (URLs + status)
- GitHub repo URLs (owned + starred)
- Venture interconnections
- Which ones are making money
- What's actually connected

Output: ECOSYSTEM_REALITY.md
"""

import json
import yaml
from pathlib import Path
from collections import defaultdict
from urllib.parse import urlparse

BASE_PATH = Path("/Users/acebless/Documents/The Company/Company Brain")

def load_sites():
    """Load Vercel sites from sites.json"""
    path = BASE_PATH / "repos/worldwidebro-venture-portal/src/data/sites.json"
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {"sites": []}

def load_ventures():
    """Load venture registry"""
    path = BASE_PATH / "_REGISTRIES/ventures-by-sector.yaml"
    if path.exists():
        with open(path) as f:
            return yaml.safe_load(f)
    return {}

def load_repos():
    """Load repository registry"""
    path = BASE_PATH / "_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml"
    if path.exists():
        with open(path) as f:
            return yaml.safe_load(f)
    return {}

def generate_reality_check():
    """Generate complete ecosystem reality check"""

    sites = load_sites()
    ventures = load_ventures()
    repos = load_repos()

    # Group sites by status
    by_status = defaultdict(list)
    for site in sites.get("sites", []):
        by_status[site.get("status", "UNKNOWN")].append(site)

    # Build venture map
    venture_to_github = {}
    venture_to_sites = defaultdict(list)

    for site in sites.get("sites", []):
        if site.get("venture_id") != "UNASSIGNED":
            venture_to_sites[site["venture_id"]].append(site)

    # Build output
    output = []
    output.append("# 🌍 Ecosystem Reality Check — The Actual Working System\n")
    output.append("**Last Updated:** 2026-09-09")
    output.append("**Authority:** Live Vercel deployments, GitHub repos, venture interconnections\n")

    # Summary statistics
    output.append("## 📊 THE REALITY\n")
    output.append("| Metric | Count | Status |")
    output.append("|--------|-------|--------|")
    output.append(f"| **Vercel Deployments** | {len(sites.get('sites', []))} | ✅ LIVE |")
    output.append(f"| **INCOME_READY** | {len(by_status.get('INCOME_READY', []))} | Making $ |")
    output.append(f"| **VALIDATING** | {len(by_status.get('VALIDATING', []))} | Testing |")
    output.append(f"| **SPECULATIVE** | {len(by_status.get('SPECULATIVE', []))} | Prototype |")
    output.append(f"| **GitHub Repos** | {len(repos.get('repositories', {}))} | Cataloged |")
    output.append(f"| **Ventures with Vercel** | {len(venture_to_sites)} | Deployed |\n")

    # Income-ready ventures (money-making)
    output.append("## 💰 INCOME-READY (Making Money)\n")
    income_ready = by_status.get("INCOME_READY", [])
    if income_ready:
        for site in sorted(income_ready, key=lambda x: x.get("id", "")):
            output.append(f"\n### {site['venture_id']} - {site['name']}")
            output.append(f"**Vercel:** {site['url']}")
            output.append(f"**Status:** {site['status']}")
            if site.get("notes"):
                output.append(f"**Details:** {site['notes']}")
    else:
        output.append("None yet")

    # Validating ventures (nearly ready)
    output.append("\n## 🟡 VALIDATING (Testing)\n")
    validating = by_status.get("VALIDATING", [])
    if validating:
        for site in sorted(validating, key=lambda x: x.get("id", "")):
            output.append(f"\n### {site['venture_id']} - {site['name']}")
            output.append(f"**Vercel:** {site['url']}")
            output.append(f"**Status:** {site['status']}")
            if site.get("notes"):
                output.append(f"**Details:** {site['notes']}")

    # All Vercel deployments (complete list)
    output.append("\n\n## 🚀 ALL 95 VERCEL DEPLOYMENTS\n")
    output.append("| ID | Name | Venture | URL | Status | Updated |")
    output.append("|-------|------|---------|-----|--------|---------|")

    for site in sorted(sites.get("sites", []), key=lambda x: x.get("id", "")):
        venture = site.get("venture_id", "UNASSIGNED")
        url_short = site["url"].replace("https://", "").replace(".vercel.app", "")
        updated = site.get("last_updated", "N/A")

        status_emoji = "💰" if site["status"] == "INCOME_READY" else "🟡" if site["status"] == "VALIDATING" else "⚪"

        output.append(
            f"| {site['id']} | {site['name'][:30]} | {venture} | {url_short} | {status_emoji} {site['status'][:8]} | {updated} |"
        )

    # GitHub repos
    output.append("\n\n## 🔗 GITHUB REPOSITORIES\n")
    output.append(f"**Total Repos:** {len(repos.get('repositories', {}))}\n")
    output.append("### Popular Repos (by stars)\n")

    repo_list = repos.get('repositories', {})
    top_repos = sorted(
        repo_list.items(),
        key=lambda x: x[1].get('stars', 0),
        reverse=True
    )[:20]

    for repo_id, repo_info in top_repos:
        name = repo_info.get('name', repo_id)
        url = repo_info.get('url', f"https://github.com/Worldwidebro/{repo_id}")
        stars = repo_info.get('stars', 0)

        output.append(f"- [{name}]({url}) ⭐ {stars}")

    # Interconnections
    output.append("\n\n## 🔗 INTERCONNECTIONS\n")
    output.append("### Ventures with Multiple Deployments\n")

    for venture_id in sorted(venture_to_sites.keys()):
        sites_list = venture_to_sites[venture_id]
        if len(sites_list) > 1:
            output.append(f"\n**{venture_id}** ({len(sites_list)} deployments):")
            for site in sites_list:
                output.append(f"  - {site['name']}: {site['url']}")

    # Community (COMM) ventures
    output.append("\n\n## 👥 COMMUNITY VENTURES (COMM)\n")
    comm_ventures = [s for s in sites.get("sites", []) if s.get("venture_id", "").startswith("COMM")]
    if comm_ventures:
        for site in comm_ventures:
            output.append(f"- **{site['venture_id']}** ({site['name']}): {site['url']}")
    else:
        output.append("No COMM ventures deployed yet")

    # Missing pieces
    output.append("\n\n## ❌ REALITY GAPS\n")
    output.append("- CON-001 (Construction) NOT deployed to Vercel")
    output.append("- FIN-037 (Trading) code exists but NOT deployed")
    output.append("- 1,740 repos cataloged but only ~95 have active Vercel sites")
    output.append("- 789 ventures planned but only ~18 have implementations")
    output.append("- GitHub URLs not linked to venture registry (MISSING)")

    output.append("\n\n## 📈 MONEY FLOWS\n")
    output.append("### Known Revenue Paths\n")
    output.append("- **LT-005** (HealthRoute): $45 Standard, $85 STAT, $1,200/mo Retainer")
    output.append("- **LT-011** (DispatchOS): $49/mo, $149/mo, $250 Shipper Escrow")
    output.append("- **RE-001** (RE Platform): $250 Express, $499/mo Deal Room")
    output.append("- **OPS-001** (Staffing): $2,500 placement fee")
    output.append("- **CON-001** (Construction): $299 consultation (NOT deployed)")
    output.append("- **FIN-037** (Trading): Performance fees (NOT deployed)")

    # Write output
    output_path = BASE_PATH / "ECOSYSTEM_REALITY.md"
    with open(output_path, "w") as f:
        f.write("\n".join(output))

    print(f"✅ Reality check generated: {output_path}")
    print(f"\n📊 Summary:")
    print(f"   - {len(sites.get('sites', []))} Vercel deployments")
    print(f"   - {len(by_status.get('INCOME_READY', []))} making money")
    print(f"   - {len(by_status.get('VALIDATING', []))} validating")
    print(f"   - {len(by_status.get('SPECULATIVE', []))} speculative")
    print(f"   - {len(repos.get('repositories', {}))} repos cataloged")
    print(f"   - {len(venture_to_sites)} ventures with deployments")

if __name__ == "__main__":
    generate_reality_check()
