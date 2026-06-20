#!/usr/bin/env python3
"""
COMPREHENSIVE MAPPING SYSTEM
Maps 1559 repos (855 owned + 704 starred) against 773 ventures
Prevents vendor lock-in by identifying which repos to use for each venture
"""

import csv
import json
import os
from pathlib import Path
from collections import defaultdict

def load_owned_repos():
    """Load 855 owned repos from The office/repos.json"""
    try:
        with open('/Users/acebless/Documents/The office/repos.json', 'r') as f:
            data = json.load(f)
            return data if isinstance(data, list) else data.get('repos', [])
    except Exception as e:
        print(f"⚠️  Could not load owned repos: {e}")
        return []

def load_starred_repos():
    """Load 704 starred repos from starred_repos_with_capabilities.csv"""
    repos = []
    try:
        with open('/Users/acebless/Documents/starred_repos_with_capabilities.csv', 'r') as f:
            reader = csv.DictReader(f)
            repos = list(reader)
    except Exception as e:
        print(f"⚠️  Could not load starred repos: {e}")
    return repos

def load_ventures():
    """Load 773 ventures from ventures-master.csv"""
    ventures = []
    try:
        with open('/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/venture-hub/ventures-master.csv', 'r') as f:
            reader = csv.DictReader(f)
            ventures = list(reader)
    except Exception as e:
        print(f"⚠️  Could not load ventures: {e}")
    return ventures

def score_repo_venture_relevance(repo, venture):
    """Score how relevant a repo is to a venture (0-100)"""
    score = 50  # baseline

    # Extract data safely
    if isinstance(repo, dict):
        repo_name = (repo.get('name', '') or '').lower()
        repo_desc = (repo.get('description', '') or '').lower()
        repo_topics = repo.get('topics', []) or []
    else:
        repo_name = str(repo).lower()
        repo_desc = ''
        repo_topics = []

    venture_name = (venture.get('name', '') or '').lower()
    venture_sector = (venture.get('sector', '') or '').lower()

    # Sector match (+25)
    if venture_sector and venture_sector in repo_name:
        score += 25
    if venture_sector and venture_sector in repo_desc:
        score += 15

    # Name/keyword overlap (+30)
    venture_words = set(venture_name.split())
    repo_words = set((repo_name + " " + repo_desc).split())
    common = len(venture_words & repo_words)
    score += min(common * 10, 30)

    # Topic match (+15)
    if repo_topics and any(t in venture_name for t in repo_topics):
        score += 15

    return min(max(score, 0), 100)

def build_mapping(owned_repos, starred_repos, ventures):
    """Build complete repo-venture mapping"""

    print("\n" + "=" * 80)
    print("MAPPING: 1559 Repos → 773 Ventures")
    print("=" * 80)

    venture_mappings = []
    repo_usage_count = defaultdict(int)

    # For each venture, find relevant repos
    for i, venture in enumerate(ventures, 1):
        if i % 100 == 0:
            print(f"  [{i}/{len(ventures)}] Processing ventures...")

        venture_id = venture.get('venture_id', 'UNKNOWN')
        venture_name = venture.get('name', '')
        sector = venture.get('sector', '')

        # Score repos
        all_scores = []

        # Score owned repos
        for repo in owned_repos:
            score = score_repo_venture_relevance(repo, venture)
            if score >= 30:
                repo_name = repo.get('name', repo) if isinstance(repo, dict) else str(repo)
                all_scores.append({
                    'name': repo_name,
                    'score': score,
                    'type': 'owned',
                    'url': repo.get('url', '') if isinstance(repo, dict) else ''
                })
                repo_usage_count[repo_name] += 1

        # Score starred repos
        for repo in starred_repos:
            score = score_repo_venture_relevance(repo, venture)
            if score >= 30:
                repo_name = repo.get('repo_name', repo.get('name', '')) if isinstance(repo, dict) else str(repo)
                all_scores.append({
                    'name': repo_name,
                    'score': score,
                    'type': 'starred',
                    'url': repo.get('url', '') if isinstance(repo, dict) else ''
                })
                repo_usage_count[repo_name] += 1

        # Top 10 matches
        top_matches = sorted(all_scores, key=lambda x: x['score'], reverse=True)[:10]

        if top_matches:
            venture_mappings.append({
                'venture_id': venture_id,
                'venture_name': venture_name,
                'sector': sector,
                'matching_repos': top_matches,
                'match_count': len(top_matches),
                'coverage_score': top_matches[0]['score'] if top_matches else 0
            })

    return venture_mappings, dict(repo_usage_count)

def main():
    print("=" * 80)
    print("REPOSITORY-VENTURE MAPPING SYSTEM")
    print("Anti-vendor-lock-in: Map all repos to ventures")
    print("=" * 80)

    # Load data
    print("\n📦 Loading data...")
    owned_repos = load_owned_repos()
    starred_repos = load_starred_repos()
    ventures = load_ventures()

    print(f"  ✅ Owned repos: {len(owned_repos)}")
    print(f"  ✅ Starred repos: {len(starred_repos)}")
    print(f"  ✅ Ventures: {len(ventures)}")

    if not ventures:
        print("⚠️  No ventures loaded. Exiting.")
        return

    # Build mapping
    print("\n🔗 Building mappings...")
    venture_mappings, repo_usage = build_mapping(owned_repos, starred_repos, ventures)

    # Save results
    output_mapping = '/Users/acebless/Documents/repo_venture_mapping.json'
    with open(output_mapping, 'w') as f:
        json.dump({
            'total_owned_repos': len(owned_repos),
            'total_starred_repos': len(starred_repos),
            'total_ventures': len(ventures),
            'total_mappings': len(venture_mappings),
            'venture_mappings': venture_mappings
        }, f, indent=2)

    print(f"\n✅ Saved: {output_mapping}")
    print(f"✅ Mapped {len(venture_mappings)} ventures")

    # Top repos by usage
    print(f"\n📊 Most useful repos (used in most ventures):")
    top_repos = sorted(repo_usage.items(), key=lambda x: -x[1])[:10]
    for repo, count in top_repos:
        print(f"  {count:>2} ventures → {repo[:40]}")

    # Sample mapping
    print(f"\n🎯 Sample mappings (first 3 TECH ventures):")
    tech_mappings = [m for m in venture_mappings if 'TECH-' in m['venture_id']]
    for vm in tech_mappings[:3]:
        print(f"\n  {vm['venture_id']}: {vm['venture_name']}")
        print(f"    Coverage score: {vm['coverage_score']}/100")
        for match in vm.get('matching_repos', [])[:3]:
            print(f"    → {match['name']:<35} ({match['score']}/100) [{match['type']}]")

    print("\n" + "=" * 80)
    print("✅ MAPPING COMPLETE - Ready for decision engine")
    print("=" * 80)

if __name__ == '__main__':
    main()
