#!/usr/bin/env python3
"""
Auto-Alignment Agent - Match ventures to repos using:
1. Semantic capabilities (where dependencies exist)
2. Sector + language fallback (for all ventures)
3. Ranking by relevance

Replaces manual CSV updates with automated scoring.
"""

import csv
import json
from collections import defaultdict

def load_data():
    ventures = {}
    with open('ventures_classification_final.csv') as f:
        for row in csv.DictReader(f):
            ventures[row['venture_id']] = row

    owned_repos = {}
    with open('venture-hub/registries/github_owned.csv') as f:
        for row in csv.DictReader(f):
            owned_repos[row['name']] = row

    starred_repos = {}
    with open('starred_repos_664.csv') as f:
        for row in csv.DictReader(f):
            starred_repos[row['name']] = row

    return ventures, owned_repos, starred_repos

def extract_language(name):
    """Infer language from repo name."""
    lang_hints = {
        'py': 'Python',
        'js': 'JavaScript',
        'ts': 'TypeScript',
        'go': 'Go',
        'rust': 'Rust',
        'java': 'Java',
    }
    for hint, lang in lang_hints.items():
        if hint in name.lower():
            return lang
    return None

def score_match(venture, repo, repo_type):
    """Score venture-repo match (0-1)."""
    score = 0.0
    details = []

    # Sector + language match (primary signal)
    sector = venture.get('sector', '').lower()
    repo_lang = repo.get('language', '').lower() if repo_type == 'owned' else extract_language(repo.get('name', ''))
    repo_topics = repo.get('topics', '').lower() if repo_type == 'owned' else repo.get('topics', '').lower()

    # If venture top_repo is already set and matches, boost score
    if venture.get('top_repo') == repo.get('name'):
        score += 0.5
        details.append(f"already_top_repo")

    # Language + sector alignment
    if sector and (sector in repo_topics or sector in repo.get('description', '').lower()):
        score += 0.3
        details.append(f"sector_match")

    # Dependencies match (if venture has any)
    venture_deps = venture.get('dependencies', 'none')
    if venture_deps != 'none':
        for dep in venture_deps.split('|'):
            if dep.strip() in repo_topics or dep.strip() in repo.get('description', '').lower():
                score += 0.2
                details.append(f"dep_match_{dep.strip()}")
                break

    return min(score, 1.0), details

def auto_align(ventures, owned_repos, starred_repos):
    """Auto-align all ventures to repos."""
    alignments = []

    for venture_id, venture in ventures.items():
        venture_name = venture.get('venture_name')
        sector = venture.get('sector')

        # Score owned repos
        owned_matches = []
        for repo_name, repo_data in owned_repos.items():
            score, details = score_match(venture, repo_data, 'owned')
            if score > 0.1:
                owned_matches.append({
                    'name': repo_name,
                    'type': 'owned',
                    'score': round(score, 2),
                    'language': repo_data.get('language', 'unknown'),
                    'reasons': details,
                })

        # Score starred repos
        starred_matches = []
        for repo_name, repo_data in starred_repos.items():
            score, details = score_match(venture, repo_data, 'starred')
            if score > 0.1:
                starred_matches.append({
                    'name': repo_name,
                    'type': 'starred',
                    'score': round(score, 2),
                    'owner': repo_data.get('owner', 'unknown'),
                    'reasons': details,
                })

        # Top 3 from each type
        owned_matches = sorted(owned_matches, key=lambda x: x['score'], reverse=True)[:3]
        starred_matches = sorted(starred_matches, key=lambda x: x['score'], reverse=True)[:3]

        all_matches = owned_matches + starred_matches
        all_matches = sorted(all_matches, key=lambda x: x['score'], reverse=True)[:5]

        if all_matches:
            alignments.append({
                'venture_id': venture_id,
                'venture_name': venture_name,
                'sector': sector,
                'current_top_repo': venture.get('top_repo'),
                'auto_matched_repos': all_matches,
                'confidence': round(all_matches[0]['score'] if all_matches else 0, 2),
            })

    return alignments

def main():
    print("Loading venture + repo data...")
    ventures, owned, starred = load_data()

    print(f"Auto-aligning {len(ventures)} ventures to {len(owned) + len(starred)} repos...")
    alignments = auto_align(ventures, owned, starred)

    with open('AUTO-ALIGNMENT-RESULTS.json', 'w') as f:
        json.dump({
            'total_ventures': len(ventures),
            'ventures_with_matches': len(alignments),
            'total_repos': len(owned) + len(starred),
            'timestamp': '2026-06-01',
            'alignments': alignments,
        }, f, indent=2)

    # Summary statistics
    print(f"\n✓ Auto-alignment complete:")
    print(f"  Ventures with matches: {len(alignments)}/{len(ventures)}")
    print(f"  Avg matches per venture: {sum(len(a['auto_matched_repos']) for a in alignments) / len(alignments) if alignments else 0:.1f}")
    print(f"  High confidence (0.8+): {len([a for a in alignments if a['confidence'] >= 0.8])}")
    print(f"\nOutput: AUTO-ALIGNMENT-RESULTS.json")

if __name__ == '__main__':
    main()
