#!/bin/bash
# Auto-sync alignment system - keeps ventures/repos synchronized
# Usage: ./sync_alignment.sh
# Or schedule: 0 6 * * * /path/to/sync_alignment.sh

set -e
cd /Users/acebless/Documents

echo "🔄 WORLDWIDEBRO: Syncing alignment..."
echo ""

# Step 1: Run auto-alignment agent
python3 auto_align_agent.py

# Step 2: Update unified CSVs
python3 << 'EOF'
import csv
import json

# Load auto-alignment results
with open('AUTO-ALIGNMENT-RESULTS.json') as f:
    auto_results = {a['venture_id']: a for a in json.load(f)['alignments']}

# Read ventures
ventures = {}
with open('ventures_classification_final.csv') as f:
    for row in csv.DictReader(f):
        ventures[row['venture_id']] = row

# Update WORLDWIDEBRO-SUPERUNIFIED-4LAYERS.csv
with open('WORLDWIDEBRO-SUPERUNIFIED-4LAYERS.csv', 'w') as out:
    writer = csv.DictWriter(out, fieldnames=[
        'venture_id', 'venture_name', 'sector', 'tier',
        'owned_repos_matched', 'starred_repos_matched',
        'total_repos_matched', 'owned_count', 'starred_count',
        'top_match_confidence'
    ])
    writer.writeheader()

    for venture_id, align_data in auto_results.items():
        owned = [m['name'] for m in align_data['auto_matched_repos'] if m['type'] == 'owned']
        starred = [m['name'] for m in align_data['auto_matched_repos'] if m['type'] == 'starred']

        writer.writerow({
            'venture_id': venture_id,
            'venture_name': align_data['venture_name'],
            'sector': align_data['sector'],
            'tier': ventures[venture_id].get('tier'),
            'owned_repos_matched': '|'.join(owned) if owned else '',
            'starred_repos_matched': '|'.join(starred) if starred else '',
            'total_repos_matched': len(owned) + len(starred),
            'owned_count': len(owned),
            'starred_count': len(starred),
            'top_match_confidence': align_data['confidence'],
        })

print("✓ Updated WORLDWIDEBRO-SUPERUNIFIED-4LAYERS.csv")

# Update WORLDWIDEBRO-REPOS-4LAYERS.csv
repos_to_ventures = {}
with open('venture-hub/registries/github_owned.csv') as f:
    for row in csv.DictReader(f):
        repos_to_ventures[row['name']] = {'type': 'owned', 'language': row.get('language')}

with open('starred_repos_664.csv') as f:
    for row in csv.DictReader(f):
        repos_to_ventures[row['name']] = {'type': 'starred', 'language': row.get('language')}

# Map ventures to repos
repo_ventures = {}
for venture_id, align_data in auto_results.items():
    for match in align_data['auto_matched_repos']:
        repo_name = match['name']
        if repo_name not in repo_ventures:
            repo_ventures[repo_name] = []
        repo_ventures[repo_name].append(venture_id)

with open('WORLDWIDEBRO-REPOS-4LAYERS.csv', 'w') as out:
    writer = csv.DictWriter(out, fieldnames=[
        'repo_name', 'repo_type', 'language',
        'ventures_matched', 'venture_count'
    ])
    writer.writeheader()

    for repo_name, repo_info in repos_to_ventures.items():
        ventures_list = repo_ventures.get(repo_name, [])
        writer.writerow({
            'repo_name': repo_name,
            'repo_type': repo_info['type'],
            'language': repo_info.get('language', ''),
            'ventures_matched': '|'.join(ventures_list) if ventures_list else '',
            'venture_count': len(ventures_list),
        })

print("✓ Updated WORLDWIDEBRO-REPOS-4LAYERS.csv")

EOF

echo ""
echo "✅ Alignment sync complete!"
echo "   Files updated:"
echo "   - WORLDWIDEBRO-SUPERUNIFIED-4LAYERS.csv"
echo "   - WORLDWIDEBRO-REPOS-4LAYERS.csv"
echo "   - AUTO-ALIGNMENT-RESULTS.json"
echo ""
echo "Schedule this with cron:"
echo "   0 6 * * * /Users/acebless/Documents/sync_alignment.sh"
