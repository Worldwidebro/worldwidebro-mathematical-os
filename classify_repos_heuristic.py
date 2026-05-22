#!/usr/bin/env python3
"""
Move 2a Fallback: Heuristic Repo Institutional Classification
Uses repo name, description, language, topics, and activity patterns instead of LLM.
Designed for fast local execution without external API calls.
"""

import os
import json
import re
from datetime import datetime, timedelta
from typing import Optional
import requests

# Environment setup
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

if not all([GITHUB_TOKEN, SUPABASE_URL, SUPABASE_KEY]):
    print("ERROR: Missing required env vars: GITHUB_TOKEN, SUPABASE_URL, SUPABASE_KEY")
    exit(1)

try:
    from supabase import create_client
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
except ImportError:
    print("Installing supabase...")
    os.system("pip install supabase -q")
    from supabase import create_client
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# GitHub headers
gh_headers = {
    'Authorization': f'Bearer {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
    'X-GitHub-Api-Version': '2022-11-28'
}


def fetch_repos(owner_type: str, per_page: int = 100) -> list:
    """Fetch repos from GitHub API with pagination."""
    repos = []
    page = 1

    if owner_type == 'owned':
        endpoint = 'https://api.github.com/user/repos'
    elif owner_type == 'starred':
        endpoint = 'https://api.github.com/user/starred'
    else:
        raise ValueError(f"Invalid owner_type: {owner_type}")

    while True:
        params = {'per_page': per_page, 'page': page, 'sort': 'updated'}
        print(f"  Fetching {owner_type} repos, page {page}...")
        resp = requests.get(endpoint, headers=gh_headers, params=params)

        if resp.status_code != 200:
            print(f"  ERROR: GitHub API returned {resp.status_code}")
            break

        batch = resp.json()
        if not batch:
            break

        for r in batch:
            repos.append({
                'full_name': r['full_name'],
                'description': (r.get('description') or '').lower(),
                'language': (r.get('language') or '').lower(),
                'topics': [t.lower() for t in (r.get('topics') or [])],
                'last_commit_date': r.get('pushed_at', ''),
                'stargazers_count': r.get('stargazers_count', 0),
                'owner_type': owner_type
            })

        page += 1

    return repos


def is_archived(repo: dict) -> bool:
    """Check if repo is archived (no commits in 6+ months)."""
    if not repo['last_commit_date']:
        return True
    try:
        last_commit = datetime.fromisoformat(repo['last_commit_date'].replace('Z', '+00:00'))
        six_months_ago = datetime.now(last_commit.tzinfo) - timedelta(days=180)
        return last_commit < six_months_ago
    except:
        return False


def classify_repo_heuristic(repo: dict) -> dict:
    """
    Classify a repo using heuristic rules based on name, description, language, topics.
    """
    full_name = repo['full_name'].lower()
    desc = repo['description']
    lang = repo['language']
    topics = repo['topics']
    stars = repo['stargazers_count']

    # Combine all text for pattern matching
    all_text = f"{full_name} {desc} {lang} {' '.join(topics)}"

    confidence = 0.5
    function = 'UNCATEGORIZED'
    keywords = []

    # VCC patterns (Venture-Critical Core): production, active, core, live, deployed
    vcc_patterns = [
        r'(production|prod-|prod_|live|deployed|active)',
        r'(core|main|primary)',
        r'(app|platform|saas|service)(?:$|-|_)',
        r'^[a-z0-9]+-app$|^[a-z0-9]+-service$|^[a-z0-9]+-platform$',
    ]
    if any(re.search(p, all_text) for p in vcc_patterns) and not is_archived(repo):
        if 'application' in topics or 'saas' in topics or 'webapp' in topics:
            function = 'VCC'
            confidence = 0.85
            keywords = ['production', 'active', 'core', 'deployed']

    # CI patterns (Capability/Infrastructure): sdk, lib, tool, framework, infra
    ci_patterns = [
        r'(sdk|library|lib)',
        r'(tool|toolkit|utility)',
        r'(framework|engine)',
        r'(infra|infrastructure)',
        r'(cli|command)',
    ]
    if function == 'UNCATEGORIZED' and any(re.search(p, all_text) for p in ci_patterns):
        function = 'CI'
        confidence = 0.8
        keywords = ['library', 'tool', 'framework', 'infrastructure']

    # EXP patterns (Experimental/R&D): poc, experiment, learn, prototype, demo
    exp_patterns = [
        r'(poc|proof.?of.?concept)',
        r'(experiment|experimental)',
        r'(learn|learning|tutorial)',
        r'(prototype|demo)',
        r'(scratch|sandbox)',
    ]
    if function == 'UNCATEGORIZED' and any(re.search(p, all_text) for p in exp_patterns):
        function = 'EXP'
        confidence = 0.75
        keywords = ['experimental', 'prototype', 'learning']

    # ARC patterns (Archived): deprecated, archived, old, legacy, inactive
    if is_archived(repo):
        function = 'ARC'
        confidence = 0.9
        keywords = ['archived', 'inactive', 'old']

    # COMP patterns (Competitive/Intel): competitor, alternative, market analysis
    comp_patterns = [
        r'(competitor|competitive)',
        r'(alternative|similar)',
        r'(market|analysis)',
        r'(comparison|vs\.)',
    ]
    if function == 'UNCATEGORIZED' and any(re.search(p, all_text) for p in comp_patterns):
        function = 'COMP'
        confidence = 0.7
        keywords = ['competitive', 'market', 'alternative']

    # TOOL patterns (Library/Tool): high stars, library/tool keywords
    tool_patterns = [
        r'(library|toolkit|utility)',
        r'(plugin|extension)',
        r'(integration)',
    ]
    if function == 'UNCATEGORIZED' and (any(re.search(p, all_text) for p in tool_patterns) or stars > 50):
        function = 'TOOL'
        confidence = 0.75
        keywords = ['library', 'tool', 'utility']

    # REF patterns (Inspiration/Reference): architecture, design, pattern, example
    ref_patterns = [
        r'(architecture|design)',
        r'(pattern|example)',
        r'(reference|template)',
        r'(starter|boilerplate)',
    ]
    if function == 'UNCATEGORIZED' and any(re.search(p, all_text) for p in ref_patterns):
        function = 'REF'
        confidence = 0.7
        keywords = ['architecture', 'design', 'pattern', 'example']

    # Fallback: TOOL for popular repos
    if function == 'UNCATEGORIZED' and stars > 100:
        function = 'TOOL'
        confidence = 0.6
        keywords = ['popular', 'high-star']

    return {
        'full_name': repo['full_name'],
        'institutional_function': function,
        'confidence': confidence,
        'reasoning_keywords': keywords,
        'suggested_venture': None,
        'is_dependency_of': [],
        'needs_human_review': confidence < 0.7,
        'owner_type': repo['owner_type']
    }


def insert_classifications(classifications: list) -> int:
    """Insert classifications into Supabase."""
    records = []

    for c in classifications:
        record = {
            'full_name': c['full_name'],
            'owner_type': c.get('owner_type', 'owned'),
            'institutional_function': c['institutional_function'],
            'confidence': c['confidence'],
            'reasoning_keywords': c.get('reasoning_keywords', []),
            'suggested_venture': c.get('suggested_venture'),
            'is_dependency_of': c.get('is_dependency_of', []),
            'needs_human_review': c.get('needs_human_review', False),
            'ingest_status': 'pending'
        }
        records.append(record)

    if not records:
        return 0

    try:
        print(f"  Inserting {len(records)} records into Supabase...")
        result = supabase.table('repo_institutional_index').upsert(records).execute()
        print(f"  ✓ Inserted {len(records)} records")
        return len(records)
    except Exception as e:
        print(f"  ERROR inserting records: {e}")
        return 0


def main():
    """Main execution flow."""
    print("\n=== Move 2a Fallback: Heuristic Repo Institutional Classification ===\n")

    # Fetch repos
    print("STEP 1: Fetching Repositories")
    print("Fetching owned repos...")
    owned_repos = fetch_repos('owned')
    print(f"✓ Fetched {len(owned_repos)} owned repos")

    print("Fetching starred repos...")
    starred_repos = fetch_repos('starred')
    print(f"✓ Fetched {len(starred_repos)} starred repos")

    total_repos = len(owned_repos) + len(starred_repos)
    print(f"\nTotal repos to classify: {total_repos}")

    # Classify all repos
    print("\nSTEP 2: Heuristic Classification")
    all_classifications = []

    all_repos = [(r, 'owned') for r in owned_repos] + [(r, 'starred') for r in starred_repos]
    for i, (repo, owner_type) in enumerate(all_repos):
        if (i + 1) % 100 == 0:
            print(f"  Classified {i+1}/{total_repos} repos...")

        classification = classify_repo_heuristic(repo)
        all_classifications.append(classification)

    print(f"\n✓ Total classified: {len(all_classifications)} repos")

    # Insert into Supabase
    print("\nSTEP 3: Storing Classifications in Supabase")
    inserted = insert_classifications(all_classifications)

    # Summary
    print("\n=== Summary ===")
    print(f"Owned repos: {len(owned_repos)}")
    print(f"Starred repos: {len(starred_repos)}")
    print(f"Total classified: {len(all_classifications)}")
    print(f"Total inserted: {inserted}")

    # Statistics by category
    print("\n=== Classification Distribution ===")
    from collections import Counter
    functions = Counter(c['institutional_function'] for c in all_classifications)
    for func in ['VCC', 'CI', 'EXP', 'ARC', 'COMP', 'TOOL', 'REF', 'UNCATEGORIZED']:
        count = functions.get(func, 0)
        print(f"  {func}: {count}")

    # Human review count
    human_review = sum(1 for c in all_classifications if c['needs_human_review'])
    print(f"\n  Repos needing human review (confidence < 0.7): {human_review}")

    print("\n✓ Move 2a Complete (Heuristic)")
    print("  Next: Review repos with needs_human_review=true")
    print("  Then: Set ingest_status='ingested' for VCC repos to trigger deep indexing")


if __name__ == '__main__':
    main()
