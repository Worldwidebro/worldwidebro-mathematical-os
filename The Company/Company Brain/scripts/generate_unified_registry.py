#!/usr/bin/env python3
"""
Generate Unified Ventures + Repos Registry

Aggregates:
- 789 ventures by sector with status, repos, deployment
- 177 code repos with capability mapping & dependencies
- 618 templates with usage
- Interconnections between all entities

Output: UNIFIED_REGISTRY.md (single source of truth)
"""

import os
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any
from collections import defaultdict

REGISTRY_DIR = Path("/Users/acebless/Documents/The Company/Company Brain/_REGISTRIES")
CANONICAL_DIR = REGISTRY_DIR / "CANONICAL"


def load_yaml(path: Path) -> Dict:
    """Load YAML registry"""
    if not path.exists():
        return {}
    with open(path) as f:
        return yaml.safe_load(f) or {}


def load_json(path: Path) -> Dict:
    """Load JSON registry"""
    if not path.exists():
        return {}
    with open(path) as f:
        return json.load(f)


def generate_unified_registry():
    """Generate complete unified registry"""

    print("📦 Loading registries...")

    # Load all registries
    ventures_by_sector = load_yaml(REGISTRY_DIR / "ventures-by-sector.yaml")
    repos_by_sector = load_yaml(REGISTRY_DIR / "repositories-by-sector.yaml")
    repos_canonical = load_yaml(CANONICAL_DIR / "REPOSITORY_REGISTRY.yaml")
    capabilities = load_yaml(CANONICAL_DIR / "CAPABILITY_REGISTRY.yaml")
    sites = load_yaml(CANONICAL_DIR / "SITES_REGISTRY.yaml")
    repo_deps = load_json(CANONICAL_DIR / "OWNED_REPO_DEPENDENCIES.json")
    repo_code = load_json(CANONICAL_DIR / "OWNED_REPO_CODE_REALITY.json")

    # Build aggregations
    venture_count = 0
    repo_count = 0
    template_count = 618
    sector_summary = []
    venture_details = []
    repo_details = []
    deployed_ventures = []
    revenue_ventures = []

    print("📊 Aggregating ventures...")

    # Process ventures by sector
    sectors = ventures_by_sector.get("ventures", {})
    for sector_code, sector_data in sectors.items():
        sector_name = sector_data.get("description", "")
        opco = sector_data.get("opco", "")
        ventures = sector_data.get("ventures", {})

        sector_venture_count = len(ventures)
        venture_count += sector_venture_count

        # Find deployed ventures in this sector
        deployed_in_sector = 0
        revenue_in_sector = 0

        for venture_id, venture_info in ventures.items():
            status = venture_info.get("status", "planned")
            deployment = venture_info.get("deployment", "")

            # Check if deployed
            if "vercel" in deployment.lower() or status in [
                "operating",
                "OPERATING_VALIDATING",
            ]:
                deployed_in_sector += 1
                deployed_ventures.append(
                    {
                        "id": venture_id,
                        "name": venture_info.get("name"),
                        "sector": sector_code,
                        "status": status,
                    }
                )

            # Check if revenue-generating
            if status in ["operating", "OPERATING_VALIDATING", "validating"]:
                revenue_in_sector += 1
                revenue_ventures.append(
                    {
                        "id": venture_id,
                        "name": venture_info.get("name"),
                        "sector": sector_code,
                        "status": status,
                    }
                )

            # Build venture detail
            venture_details.append(
                {
                    "id": venture_id,
                    "name": venture_info.get("name"),
                    "sector": sector_code,
                    "sector_name": sector_name,
                    "status": status,
                    "repo": venture_info.get("repository", ""),
                    "deployment": deployment,
                    "repo_count": venture_info.get("repo_count", 0),
                }
            )

        sector_summary.append(
            {
                "code": sector_code,
                "name": sector_name,
                "opco": opco,
                "total_ventures": sector_venture_count,
                "deployed": deployed_in_sector,
                "revenue_ready": revenue_in_sector,
            }
        )

    print("📚 Aggregating repositories...")

    # Process repositories
    all_repos = repos_canonical.get("repositories", {})
    for repo_id, repo_info in all_repos.items():
        repo_count += 1

        # Find capabilities
        repo_capabilities = capabilities.get("repositories", {}).get(repo_id, {})
        primary_cap = repo_capabilities.get("primary_capability", "")
        secondary_caps = repo_capabilities.get("secondary_capabilities", [])

        # Find dependencies
        dependencies = repo_deps.get(repo_id, {}).get("dependencies", [])

        # Find code reality
        code_info = repo_code.get(repo_id, {})

        repo_details.append(
            {
                "id": repo_id,
                "name": repo_info.get("name", repo_id),
                "description": repo_info.get("description", ""),
                "language": repo_info.get("language", ""),
                "primary_capability": primary_cap,
                "secondary_capabilities": secondary_caps,
                "dependencies": dependencies,
                "has_code": code_info.get("has_code", False),
                "stars": repo_info.get("stars", 0),
                "contributors": code_info.get("contributors", 0),
            }
        )

    print("✍️  Writing unified registry...")

    # Generate markdown output
    output = []
    output.append("# Worldwidebro Unified Registry")
    output.append(
        f"\n**Last Updated:** {ventures_by_sector.get('metadata', {}).get('created_at', 'N/A')}"
    )
    output.append(f"\n**Authority:** Single Source of Truth for Ventures + Repos + Ecosystem\n")

    # Summary statistics
    output.append("## 📊 Portfolio Summary\n")
    output.append("| Metric | Count |")
    output.append("|--------|-------|")
    output.append(f"| Total Ventures | {venture_count} |")
    output.append(f"| Operating/Deployed | {len(deployed_ventures)} |")
    output.append(f"| Revenue-Ready | {len(revenue_ventures)} |")
    output.append(f"| Total Sectors | {len(sector_summary)} |")
    output.append(f"| Code Repositories | {repo_count} |")
    output.append(f"| Template Repositories | {template_count} |")
    output.append(f"| **Total Assets** | **{venture_count + repo_count + template_count}** |\n")

    # Sector summary
    output.append("## 🏢 Sectors Summary\n")
    output.append("| Sector | OpCo | Ventures | Deployed | Revenue-Ready |")
    output.append("|--------|------|----------|----------|---------------|")
    for sector in sorted(sector_summary, key=lambda x: x["total_ventures"], reverse=True):
        output.append(
            f"| {sector['code']} {sector['name'][:30]} | {sector['opco']} | "
            f"{sector['total_ventures']} | {sector['deployed']} | {sector['revenue_ready']} |"
        )
    output.append("")

    # Deployed ventures
    output.append("## 🚀 Deployed/Operating Ventures\n")
    for venture in sorted(deployed_ventures, key=lambda x: x["sector"]):
        output.append(
            f"- **{venture['id']}** ({venture['sector']}) - {venture['name']} - {venture['status']}"
        )
    output.append("")

    # Revenue-ready ventures
    output.append("## 💰 Revenue-Ready Ventures\n")
    for venture in sorted(revenue_ventures, key=lambda x: x["sector"]):
        output.append(
            f"- **{venture['id']}** ({venture['sector']}) - {venture['name']} - {venture['status']}"
        )
    output.append("")

    # Repositories by capability
    output.append("## 📚 Repositories by Primary Capability\n")
    repos_by_cap = defaultdict(list)
    for repo in repo_details:
        cap = repo["primary_capability"] or "UNCATEGORIZED"
        repos_by_cap[cap].append(repo)

    for capability in sorted(repos_by_cap.keys()):
        repos = repos_by_cap[capability]
        output.append(f"\n### {capability} ({len(repos)} repos)\n")
        for repo in sorted(repos, key=lambda x: x["id"]):
            lang = f" [{repo['language']}]" if repo["language"] else ""
            output.append(
                f"- **{repo['id']}**{lang} - {repo['name'][:50]}\n"
                f"  - Deps: {len(repo['dependencies'])} | Code: {'✅' if repo['has_code'] else '❌'} | "
                f"Stars: {repo['stars']}"
            )

    # All ventures (detailed)
    output.append("\n\n## 🗂️ All Ventures by Sector\n")
    ventures_by_sector_code = defaultdict(list)
    for venture in venture_details:
        ventures_by_sector_code[venture["sector"]].append(venture)

    for sector_code in sorted(ventures_by_sector_code.keys()):
        sector_name = ventures_by_sector_code[sector_code][0]["sector_name"]
        ventures = ventures_by_sector_code[sector_code]

        output.append(f"\n### {sector_code}: {sector_name} ({len(ventures)} ventures)\n")

        for venture in sorted(ventures, key=lambda x: x["id"]):
            status_emoji = (
                "🟢"
                if venture["status"] in ["operating", "OPERATING_VALIDATING"]
                else "🟡" if venture["status"] == "validating" else "⚪"
            )
            deployment_str = f" → {venture['deployment']}" if venture["deployment"] else ""
            repo_str = f" | Repo: {venture['repo']}" if venture["repo"] else ""

            output.append(
                f"{status_emoji} **{venture['id']}** - {venture['name']}{deployment_str}{repo_str}"
            )

    # Write output
    output_path = (
        Path("/Users/acebless/Documents/The Company/Company Brain")
        / "UNIFIED_REGISTRY.md"
    )
    with open(output_path, "w") as f:
        f.write("\n".join(output))

    print(f"✅ Registry generated: {output_path}")
    print(f"\n📈 Final Stats:")
    print(f"   - Ventures: {venture_count}")
    print(f"   - Deployed: {len(deployed_ventures)}")
    print(f"   - Revenue-Ready: {len(revenue_ventures)}")
    print(f"   - Repositories: {repo_count}")
    print(f"   - Sectors: {len(sector_summary)}")
    print(f"   - Total Assets: {venture_count + repo_count + template_count}")

    return output_path


if __name__ == "__main__":
    generate_unified_registry()
