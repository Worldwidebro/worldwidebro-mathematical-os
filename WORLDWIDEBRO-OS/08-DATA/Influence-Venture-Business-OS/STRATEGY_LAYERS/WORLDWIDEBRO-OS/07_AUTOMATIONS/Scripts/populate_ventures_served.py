#!/usr/bin/env python3
"""Populate ventures_served from ventures_with_capabilities.csv"""

import csv
from collections import defaultdict

print("[TASK 2] Populate ventures_served\n")

repos_to_ventures = defaultdict(set)
venture_count = 0

core_repos = {"civilization-os", "venture-hub", "mission-control", "iza-os-rag-system",
              "the-office", "venture-factory-core", "bw-001-up-next-web"}

print("[*] Reading ventures_with_capabilities.csv...")
try:
    with open("/Users/acebless/Documents/venture-hub/ventures_with_capabilities.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            venture_id = row.get("venture_id", "").strip()
            if venture_id:
                venture_count += 1
                for i in range(1, 4):
                    repo = row.get(f"top_repo_{i}", "").strip()
                    if repo and repo in core_repos:
                        repos_to_ventures[repo].add(venture_id)

    print(f"[✓] Found {venture_count} ventures, {len(repos_to_ventures)} unique core repos")
except FileNotFoundError:
    print("  ⚠️  ventures_with_capabilities.csv not found, using core repos only")
    repos_to_ventures = {repo: set() for repo in core_repos}

print("[*] Updating PRIVATE-REPOS-ACCESS-CONTROL.csv...")
fieldnames = ["repo_id", "owner", "ventures_served"]
rows = []

for repo_id in sorted(core_repos):
    ventures = sorted(repos_to_ventures.get(repo_id, set()))
    rows.append({
        "repo_id": repo_id,
        "owner": "Worldwidebro",
        "ventures_served": "|".join(ventures) if ventures else ""
    })

with open("/Users/acebless/Documents/PRIVATE-REPOS-ACCESS-CONTROL.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"[✓] Created PRIVATE-REPOS-ACCESS-CONTROL.csv with {len(rows)} repos\n")
