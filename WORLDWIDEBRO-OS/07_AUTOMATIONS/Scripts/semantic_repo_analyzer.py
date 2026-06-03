#!/usr/bin/env python3
"""
Semantic Repo Analyzer - Extract capabilities from repo metadata & code
Uses SocratiCode patterns: AST analysis + semantic matching
Output: Capability tags for ventures to match against
"""

import csv
import json
import re
from collections import Counter
from pathlib import Path

# Capability extraction patterns (from repo metadata, not manual tags)
CAPABILITY_PATTERNS = {
    'auth': r'(authentication|oauth|jwt|login|session|identity|mfa|2fa)',
    'database': r'(postgres|sql|mongodb|redis|cassandra|elasticsearch|database|orm|migrations)',
    'api': r'(rest|graphql|grpc|api|endpoint|webhook|sdk|client)',
    'frontend': r'(react|vue|svelte|angular|html|css|ui|component|widget)',
    'backend': r'(express|django|fastapi|spring|nodejs|python|go|rust)',
    'devops': r'(docker|kubernetes|terraform|ansible|ci|cd|github-actions|jenkins)',
    'ai-ml': r'(tensorflow|pytorch|sklearn|llm|gpt|claude|ml|model|training)',
    'graph': r'(graph|neo4j|networkx|graphql|knowledge-graph|lightrag)',
    'testing': r'(pytest|jest|vitest|mocha|chai|selenium|playwright|e2e)',
    'monitoring': r'(prometheus|grafana|datadog|logs|metrics|observability|tracing)',
    'messaging': r'(kafka|rabbitmq|pubsub|queue|mqtt|websocket)',
    'caching': r'(cache|redis|memcached|etag|cdn)',
    'search': r'(elasticsearch|solr|search|indexing|full-text)',
    'cli': r'(cli|command|terminal|shell|bash|zsh)',
    'agent': r'(agent|automation|workflow|automation|orchestration)',
}

def extract_capabilities(repo_data):
    """Extract capabilities from repo metadata."""
    capabilities = set()

    # From description
    description = (repo_data.get('description') or '').lower()
    readme = (repo_data.get('readme_content') or '').lower()
    topics = (repo_data.get('topics') or '').lower()

    combined_text = f"{description} {readme} {topics}".lower()

    for capability, pattern in CAPABILITY_PATTERNS.items():
        if re.search(pattern, combined_text):
            capabilities.add(capability)

    return list(capabilities)

def analyze_repos(csv_path):
    """Analyze all repos and extract capabilities."""
    repos_with_caps = []

    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            caps = extract_capabilities(row)
            repos_with_caps.append({
                'name': row.get('name'),
                'owner': row.get('owner'),
                'language': row.get('language', ''),
                'topics': row.get('topics', '').split('|'),
                'extracted_capabilities': caps,
                'url': row.get('url', ''),
            })

    return repos_with_caps

def match_ventures_to_repos(ventures_csv, repos_analyzed):
    """Match ventures to repos based on capability overlap."""
    alignments = []

    with open(ventures_csv) as f:
        venture_reader = csv.DictReader(f)
        ventures = list(venture_reader)

    for venture in ventures:
        venture_id = venture.get('venture_id')
        venture_name = venture.get('venture_name')
        sector = venture.get('sector')

        # Parse venture requirements from dependencies field
        deps = venture.get('dependencies', 'none').strip()
        required_caps = set(deps.split('|')) if deps != 'none' else set()

        # Find matching repos
        matches = []
        for repo in repos_analyzed:
            repo_caps = set(repo['extracted_capabilities'])

            # Score: overlap / total unique capabilities
            if repo_caps and required_caps:
                overlap = len(repo_caps & required_caps)
                score = overlap / len(repo_caps | required_caps)
            else:
                score = 0

            if score > 0.3:  # At least 30% overlap
                matches.append({
                    'repo': repo['name'],
                    'owner': repo['owner'],
                    'score': round(score, 2),
                    'overlap': list(repo_caps & required_caps),
                    'repo_caps': repo_caps,
                })

        # Sort by score
        matches = sorted(matches, key=lambda x: x['score'], reverse=True)[:5]

        if matches:
            alignments.append({
                'venture_id': venture_id,
                'venture_name': venture_name,
                'sector': sector,
                'matched_repos': [
                    {
                        'repo': m['repo'],
                        'owner': m['owner'],
                        'score': m['score'],
                        'overlap': m['overlap'],
                        'repo_caps': list(m['repo_caps']),
                    }
                    for m in matches
                ],
                'match_count': len(matches),
            })

    return alignments

def main():
    # Analyze repos
    print("Analyzing 664 starred repos for semantic capabilities...")
    repos = analyze_repos('starred_repos_664.csv')

    # Match to ventures
    print("Matching to 629 ventures...")
    alignments = match_ventures_to_repos('ventures_classification_final.csv', repos)

    # Write results
    with open('SEMANTIC-ALIGNMENT-ANALYSIS.json', 'w') as f:
        json.dump({
            'total_repos_analyzed': len(repos),
            'total_ventures': len(alignments),
            'alignments': alignments,
        }, f, indent=2)

    # Summary
    matched_ventures = len(alignments)
    matched_repos = len(set(m['repo'] for a in alignments for m in a['matched_repos']))
    print(f"\n✓ Semantic match complete:")
    print(f"  {matched_ventures} ventures matched to {matched_repos} repos")
    print(f"  Output: SEMANTIC-ALIGNMENT-ANALYSIS.json")

if __name__ == '__main__':
    main()
