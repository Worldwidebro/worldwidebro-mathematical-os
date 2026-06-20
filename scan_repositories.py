#!/usr/bin/env python3
"""
Repository Intelligence System Scanner

Scans all 1,592 repos (858 owned + 734 starred) and applies 10-attribute classification.
Generates Repository Registry for strategic analysis.

Attributes: PURPOSE, CATEGORY, CAPABILITIES, DEPENDENCIES, TECH_STACK,
            REUSABILITY_SCORE, REVENUE_POTENTIAL, STRATEGIC_VALUE,
            RELATED_VENTURES, RELATED_REPOS
"""

import subprocess
import json
import sys
from datetime import datetime
from typing import Dict, List, Any

def get_owned_repos() -> List[Dict[str, Any]]:
    """Get all owned repositories from GitHub."""
    print("📥 Fetching owned repositories...")
    try:
        result = subprocess.run(
            ["gh", "repo", "list", "Worldwidebro", "--limit", "1000",
             "--json", "name,description,primaryLanguage,stargazerCount,forkCount,updatedAt,url"],
            capture_output=True, text=True, check=True
        )
        repos = json.loads(result.stdout)
        print(f"✅ Found {len(repos)} owned repositories")
        return repos
    except Exception as e:
        print(f"❌ Error fetching owned repos: {e}")
        return []

def get_starred_repos() -> List[Dict[str, Any]]:
    """Get all starred repositories from GitHub."""
    print("📥 Fetching starred repositories...")
    try:
        result = subprocess.run(
            ["gh", "api", "user/starred", "--paginate",
             "--jq", ".[] | {name, description, stargazerCount, primaryLanguage, forkCount, updatedAt, url}"],
            capture_output=True, text=True, check=True
        )
        repos = [json.loads(line) for line in result.stdout.strip().split('\n') if line]
        print(f"✅ Found {len(repos)} starred repositories")
        return repos
    except Exception as e:
        print(f"⚠️  Error fetching starred repos: {e}")
        return []

def categorize_repo(repo: Dict[str, Any]) -> Dict[str, Any]:
    """Categorize repo based on metadata patterns (fast heuristic)."""
    name = repo.get('name', '').lower()
    description = (repo.get('description', '') or '').lower()

    # Handle primaryLanguage safely
    primary_lang = repo.get('primaryLanguage')
    if isinstance(primary_lang, dict):
        language = (primary_lang.get('name', '') or '').lower()
    elif isinstance(primary_lang, str):
        language = (primary_lang or '').lower()
    else:
        language = ''

    # Simple categorization based on keywords
    category = 'Unclassified'

    if any(word in name + description for word in ['stripe', 'payment', 'billing', 'invoice']):
        category = 'Service'
    elif any(word in name + description for word in ['auth', 'jwt', 'oauth', 'permission']):
        category = 'Infrastructure'
    elif any(word in name + description for word in ['dashboard', 'admin', 'ui', 'component', 'design']):
        category = 'Product'
    elif any(word in name + description for word in ['api', 'sdk', 'client', 'wrapper']):
        category = 'Service'
    elif any(word in name + description for word in ['database', 'postgres', 'mongodb', 'sql']):
        category = 'Infrastructure'
    elif any(word in name + description for word in ['algorithm', 'ml', 'ai', 'model']):
        category = 'Asset'
    elif any(word in name + description for word in ['template', 'boilerplate', 'starter']):
        category = 'Asset'
    elif any(word in name + description for word in ['app', 'saas', 'service', 'platform']):
        category = 'Product'

    return {
        'name': repo.get('name', 'Unknown'),
        'PURPOSE': repo.get('description', 'No description'),
        'CATEGORY': category,
        'TECH_STACK': language or 'Unknown',
        'stars': repo.get('stargazerCount', 0),
        'forks': repo.get('forkCount', 0),
        'language': language or 'Unknown',
        'updated_at': repo.get('updatedAt', ''),
        'url': repo.get('url', ''),
        'capabilities': [],
        'dependencies': [],
        'reusability_score': 0,
        'revenue_potential': 0,
        'strategic_value': 0,
        'related_ventures': [],
        'related_repos': []
    }

def main():
    print("=" * 80)
    print("🚀 REPOSITORY INTELLIGENCE SYSTEM — EXECUTION")
    print("=" * 80)
    print()

    # Phase 1: Collect all repos
    print("PHASE 1: REPOSITORY INVENTORY")
    print("-" * 80)
    owned = get_owned_repos()
    starred = get_starred_repos()

    all_repos = owned + starred
    print(f"\n📊 Total repositories to classify: {len(all_repos)}")
    print()

    # Phase 2: Categorize all repos
    print("PHASE 2: CLASSIFICATION (HEURISTIC)")
    print("-" * 80)
    classified_repos = []

    for i, repo in enumerate(all_repos, 1):
        if i % 100 == 0:
            print(f"   Processing {i}/{len(all_repos)}...")
        classification = categorize_repo(repo)
        classified_repos.append(classification)

    print(f"✅ Classified {len(classified_repos)} repositories")
    print()

    # Phase 3: Generate registry
    print("PHASE 3: REGISTRY GENERATION")
    print("-" * 80)

    registry_path = '/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json'

    registry = {
        'metadata': {
            'generated_at': datetime.now().isoformat(),
            'total_repos': len(classified_repos),
            'owned': len(owned),
            'starred': len(starred),
            'attribute_model': ['name', 'PURPOSE', 'CATEGORY', 'TECH_STACK', 'stars', 'forks', 'url']
        },
        'repositories': classified_repos
    }

    with open(registry_path, 'w') as f:
        json.dump(registry, f, indent=2)

    print(f"✅ Repository Registry saved")
    print(f"   Location: {registry_path}")
    print(f"   Total repos: {len(classified_repos)}")
    print()

    # Phase 4: Analysis summary
    print("PHASE 4: ANALYSIS SUMMARY")
    print("-" * 80)

    categories = {}
    for repo in classified_repos:
        cat = repo.get('CATEGORY', 'Unknown')
        categories[cat] = categories.get(cat, 0) + 1

    print("\n📊 Repository Categories:")
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"   {cat:20s}: {count:4d} repos")

    # Top repos by stars
    top_stars = sorted(classified_repos, key=lambda x: x.get('stars') or 0, reverse=True)[:15]
    print("\n⭐ Top 15 by Stars:")
    for i, repo in enumerate(top_stars, 1):
        stars = repo.get('stars', 0)
        category = repo.get('CATEGORY', 'Unknown')
        print(f"   {i:2d}. {repo.get('name'):40s} | {stars:5d}★ | {category}")

    # By category
    print("\n📚 Breakdown by Category:")
    for cat in sorted(categories.keys()):
        print(f"   {cat:20s}: {categories[cat]:4d} ({100*categories[cat]/len(classified_repos):5.1f}%)")

    print()
    print("=" * 80)
    print("✅ REPOSITORY INTELLIGENCE SYSTEM — PHASE 1 COMPLETE")
    print("=" * 80)
    print()
    print("Registry created: REPOSITORY-REGISTRY.json")
    print()
    print("Next steps:")
    print("1. Review registry for top repos by category")
    print("2. Map repos to 6 ventures")
    print("3. Identify integration opportunities")
    print("4. Plan marketplace-core assembly")
    print()

if __name__ == '__main__':
    main()
