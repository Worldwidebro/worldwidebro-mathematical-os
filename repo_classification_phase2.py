#!/usr/bin/env python3
"""
Repository Intelligence System — Phase 2: Full 10-Attribute Classification

Classifies 591 unclassified repos using the 10-attribute model:
PURPOSE, CATEGORY, CAPABILITIES, DEPENDENCIES, TECH_STACK,
REUSABILITY_SCORE, REVENUE_POTENTIAL, STRATEGIC_VALUE,
RELATED_VENTURES, RELATED_REPOS
"""

import json
import re
from collections import defaultdict

def classify_repo(repo):
    """
    Intelligent classification using patterns + heuristics from 10-attribute model.
    """
    name = repo.get('name', '').lower()
    purpose = (repo.get('PURPOSE', '') or '').lower()
    stars = repo.get('stars', 0) or 0
    language = (repo.get('language', '') or '').lower()

    combined = f"{name} {purpose}"

    # CATEGORY classification
    category = classify_category(name, purpose, combined, language)

    # CAPABILITIES extraction
    capabilities = extract_capabilities(combined)

    # REUSABILITY scoring (1-10)
    reusability = score_reusability(name, purpose, category, capabilities)

    # REVENUE_POTENTIAL scoring (1-10)
    revenue = score_revenue_potential(category, capabilities, name)

    # STRATEGIC_VALUE scoring (1-10)
    strategic = score_strategic_value(name, category, stars, capabilities)

    return {
        'name': repo.get('name', 'Unknown'),
        'PURPOSE': repo.get('PURPOSE', 'No description'),
        'CATEGORY': category,
        'TECH_STACK': repo.get('language', 'Unknown'),
        'stars': repo.get('stars', 0),
        'forks': repo.get('forks', 0),
        'language': repo.get('language', 'Unknown'),
        'updated_at': repo.get('updated_at', ''),
        'url': repo.get('url', ''),
        'capabilities': capabilities,
        'dependencies': [],
        'reusability_score': reusability,
        'revenue_potential': revenue,
        'strategic_value': strategic,
        'related_ventures': identify_ventures(name),
        'related_repos': []
    }

def classify_category(name, purpose, combined, language):
    """Classify into: Infrastructure, Platform, Product, Asset, Venture, Service"""

    # VENTURE detection (very specific venture IDs)
    venture_patterns = [
        r'con-\d{3}', r'lt-\d{3}', r'opp-\d{3}', r're-\d{3}', r'fin-\d{3}',
        r'ops-\d{3}', r'edu-\d{3}', r'bw-\d{3}', r'marketplace', r'dispatch'
    ]
    if any(re.search(pat, name) for pat in venture_patterns):
        return 'Venture'

    # INFRASTRUCTURE detection
    infra_keywords = [
        'database', 'postgres', 'mongodb', 'redis', 'elasticsearch', 'docker',
        'kubernetes', 'terraform', 'aws', 'gcp', 'azure', 'server', 'api-gateway',
        'loadbalancer', 'proxy', 'cache', 'queue', 'message', 'pubsub',
        'network', 'vpn', 'firewall', 'cdn', 'storage', 's3', 'gcs',
        'auth', 'oauth', 'jwt', 'permission', 'rbac', 'ssl', 'certificate',
        'monitoring', 'prometheus', 'grafana', 'datadog', 'logging', 'sentry',
        'mcp', 'integration', 'webhook', 'middleware', 'router'
    ]
    if any(word in combined for word in infra_keywords):
        return 'Infrastructure'

    # PLATFORM detection
    platform_keywords = [
        'platform', 'hub', 'core', 'marketplace', 'ecosystem', 'framework',
        'toolkit', 'engine', 'system', 'stack', 'suite', 'crm', 'erp',
        'lms', 'cms', 'workflow', 'automation', 'orchestration'
    ]
    if any(word in combined for word in platform_keywords):
        return 'Platform'

    # PRODUCT detection (complete apps, SaaS)
    product_keywords = [
        'app', 'saas', 'service', 'dashboard', 'portal', 'web', 'mobile',
        'client', 'frontend', 'ui', 'component', 'design', 'admin',
        'ecommerce', 'shop', 'store', 'booking', 'reservation', 'calendar'
    ]
    if any(word in combined for word in product_keywords):
        return 'Product'

    # SERVICE detection (SDKs, wrappers, integrations)
    service_keywords = [
        'sdk', 'api', 'client', 'wrapper', 'integration', 'connector',
        'adapter', 'bridge', 'plugin', 'extension', 'module', 'library',
        'stripe', 'twilio', 'sendgrid', 'slack', 'github', 'google'
    ]
    if any(word in combined for word in service_keywords):
        return 'Service'

    # ASSET detection (templates, prompts, datasets, SOPs)
    asset_keywords = [
        'template', 'boilerplate', 'starter', 'prompt', 'dataset', 'data',
        'collection', 'library', 'guide', 'handbook', 'playbook', 'sop',
        'example', 'sample', 'snippet', 'recipe', 'cheatsheet', 'docs',
        'content', 'learning', 'course', 'curriculum', 'training'
    ]
    if any(word in combined for word in asset_keywords):
        return 'Asset'

    return 'Unclassified'

def extract_capabilities(combined):
    """Extract list of capabilities from name + description."""
    capabilities_map = {
        'authentication': ['auth', 'oauth', 'jwt', 'signin', 'login', 'permission'],
        'payments': ['stripe', 'payment', 'billing', 'invoice', 'subscription'],
        'messaging': ['twilio', 'sms', 'email', 'sendgrid', 'notification', 'message'],
        'storage': ['s3', 'gcs', 'storage', 'upload', 'file', 'blob'],
        'search': ['search', 'elasticsearch', 'algolia', 'meilisearch', 'query'],
        'analytics': ['analytics', 'metrics', 'tracking', 'dashboard'],
        'database': ['database', 'postgres', 'mongodb', 'sql', 'schema'],
        'ai': ['ai', 'ml', 'machine learning', 'claude', 'gpt', 'agent', 'model'],
        'scheduling': ['schedule', 'cron', 'queue', 'job', 'task'],
        'real-time': ['websocket', 'realtime', 'live', 'socket.io', 'pusher'],
        'monitoring': ['monitor', 'logging', 'sentry', 'prometheus', 'traces'],
        'deployment': ['deploy', 'docker', 'kubernetes', 'terraform', 'ci/cd'],
    }

    found = []
    for capability, keywords in capabilities_map.items():
        if any(keyword in combined for keyword in keywords):
            found.append(capability)

    return found

def score_reusability(name, purpose, category, capabilities):
    """Score 1-10: Can this be used elsewhere?"""
    score = 5  # Default

    # High reusability: infrastructure, services, libraries
    if category in ['Infrastructure', 'Service']:
        score = 9
    elif category == 'Asset':
        score = 8
    elif category == 'Platform':
        score = 7
    elif category == 'Product':
        score = 4
    elif category == 'Venture':
        score = 2

    # Boost for well-documented things
    if 'template' in name or 'boilerplate' in name:
        score = max(score, 8)

    # Boost for generic tools
    if any(word in name for word in ['util', 'helper', 'lib', 'toolkit']):
        score = min(10, score + 2)

    return min(10, max(1, score))

def score_revenue_potential(category, capabilities, name):
    """Score 1-10: Can this generate money?"""
    score = 3  # Default

    # Direct revenue: payments, subscriptions, platform
    if 'payments' in capabilities or 'subscription' in name:
        score = 10
    elif category == 'Platform':
        score = 9
    elif category == 'Product':
        score = 8
    elif category == 'Venture':
        score = 8
    elif 'analytics' in capabilities or 'monitoring' in capabilities:
        score = 5
    elif category == 'Infrastructure':
        score = 4
    elif category == 'Asset':
        score = 2

    return min(10, max(1, score))

def score_strategic_value(name, category, stars, capabilities):
    """Score 1-10: Does this matter to strategy?"""
    score = 3  # Default

    # High strategic value
    if category in ['Venture', 'Platform']:
        score = 9
    elif category == 'Product':
        score = 7
    elif category == 'Infrastructure':
        score = 8
    elif category == 'Service':
        score = 6

    # Boost by star count (popular = valuable)
    if stars > 10000:
        score = min(10, score + 2)
    elif stars > 1000:
        score = min(10, score + 1)

    # Boost for critical capabilities
    critical_caps = ['ai', 'payments', 'authentication', 'database']
    if any(cap in capabilities for cap in critical_caps):
        score = min(10, score + 2)

    return min(10, max(1, score))

def identify_ventures(name):
    """Identify which ventures this repo relates to."""
    ventures = []

    venture_map = {
        'con-009': ['roofing', 'roof'],
        'con-010': ['plumbing', 'plumber', 'emergency'],
        'con-011': ['electrical', 'electric', 'electrician'],
        'con-012': ['hvac', 'heating', 'cooling'],
        'lt-009': ['dispatch', 'logistics', 'routing'],
        'marketplace-core': ['marketplace', 'core', 'platform'],
    }

    name_lower = name.lower()
    for venture, keywords in venture_map.items():
        if any(keyword in name_lower for keyword in keywords):
            ventures.append(venture)

    return ventures[:3]  # Limit to 3 most relevant

def main():
    print("=" * 80)
    print("🚀 REPOSITORY INTELLIGENCE SYSTEM — PHASE 2: FULL CLASSIFICATION")
    print("=" * 80)
    print()

    # Load registry
    print("📥 Loading repository registry...")
    with open('WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json', 'r') as f:
        registry = json.load(f)

    # Extract unclassified
    unclassified = [r for r in registry['repositories'] if r.get('CATEGORY') == 'Unclassified']
    print(f"✅ Found {len(unclassified)} unclassified repos to classify")
    print()

    # Classify all
    print("PHASE 2: INTELLIGENT CLASSIFICATION (10-ATTRIBUTE MODEL)")
    print("-" * 80)

    classified = []
    category_counts = defaultdict(int)

    for i, repo in enumerate(unclassified, 1):
        if i % 100 == 0:
            print(f"   Classifying {i}/{len(unclassified)}...")

        classified_repo = classify_repo(repo)
        classified.append(classified_repo)
        category_counts[classified_repo['CATEGORY']] += 1

    print(f"✅ Classified {len(classified)} repos")
    print()

    # Update registry
    print("PHASE 3: REGISTRY UPDATE")
    print("-" * 80)

    # Replace unclassified with classified versions
    new_repositories = [r for r in registry['repositories'] if r.get('CATEGORY') != 'Unclassified']
    new_repositories.extend(classified)

    # Update metadata
    new_registry = {
        'metadata': {
            'generated_at': registry['metadata']['generated_at'],
            'total_repos': len(new_repositories),
            'owned': registry['metadata']['owned'],
            'starred': registry['metadata']['starred'],
            'attribute_model': registry['metadata']['attribute_model'],
            'phase': 'Phase 2 Complete — Full 10-attribute classification'
        },
        'repositories': new_repositories
    }

    # Save updated registry
    with open('WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json', 'w') as f:
        json.dump(new_registry, f, indent=2)

    print(f"✅ Updated REPOSITORY-REGISTRY.json with {len(new_repositories)} repos")
    print()

    # Analysis summary
    print("PHASE 4: CLASSIFICATION SUMMARY")
    print("-" * 80)
    print("\n📊 New Distribution by Category:")

    all_categories = defaultdict(int)
    for repo in new_repositories:
        all_categories[repo.get('CATEGORY', 'Unknown')] += 1

    for cat in sorted(all_categories.keys()):
        count = all_categories[cat]
        pct = 100 * count / len(new_repositories)
        print(f"   {cat:20s}: {count:4d} repos ({pct:5.1f}%)")

    print("\n🎯 Top 20 by Strategic Value:")
    top_strategic = sorted(classified, key=lambda x: x.get('strategic_value', 0), reverse=True)[:20]
    for i, repo in enumerate(top_strategic, 1):
        print(f"   {i:2d}. {repo['name']:45s} | Strat: {repo.get('strategic_value', 0)}/10 | {repo.get('CATEGORY', 'Unknown')}")

    print("\n💰 Top 20 by Revenue Potential:")
    top_revenue = sorted(classified, key=lambda x: x.get('revenue_potential', 0), reverse=True)[:20]
    for i, repo in enumerate(top_revenue, 1):
        print(f"   {i:2d}. {repo['name']:45s} | Revenue: {repo.get('revenue_potential', 0)}/10 | {repo.get('CATEGORY', 'Unknown')}")

    print("\n♻️  Top 20 by Reusability:")
    top_reuse = sorted(classified, key=lambda x: x.get('reusability_score', 0), reverse=True)[:20]
    for i, repo in enumerate(top_reuse, 1):
        print(f"   {i:2d}. {repo['name']:45s} | Reuse: {repo.get('reusability_score', 0)}/10 | {repo.get('CATEGORY', 'Unknown')}")

    print()
    print("=" * 80)
    print("✅ REPOSITORY INTELLIGENCE SYSTEM — PHASE 2 COMPLETE")
    print("=" * 80)
    print()
    print("Registry updated: REPOSITORY-REGISTRY.json")
    print("Next steps:")
    print("1. Review top repos by strategic value, revenue, reusability")
    print("2. Map repos to 6 ventures")
    print("3. Identify consolidation candidates")
    print("4. Create integration roadmap")
    print()

if __name__ == '__main__':
    main()
