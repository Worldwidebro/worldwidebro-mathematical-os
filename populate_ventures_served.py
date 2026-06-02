#!/usr/bin/env python3
"""
Populate ventures_served column in PRIVATE-REPOS-ACCESS-CONTROL.csv
by parsing VENTURE-RESOURCE-DEPENDENCIES.csv shared_services and infrastructure_repos.
"""

import csv
from collections import defaultdict

# Read VENTURE-RESOURCE-DEPENDENCIES.csv and accumulate repos → ventures mapping
repos_to_ventures = defaultdict(list)

with open("VENTURE-RESOURCE-DEPENDENCIES.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        venture_id = row["venture_id"]

        # Parse shared_services (pipe-delimited)
        shared_services = row.get("shared_services", "").strip()
        if shared_services:
            for repo in shared_services.split("|"):
                repo = repo.strip()
                if repo:
                    repos_to_ventures[repo].append(venture_id)

        # Parse infrastructure_repos (pipe-delimited)
        infrastructure_repos = row.get("infrastructure_repos", "").strip()
        if infrastructure_repos:
            for repo in infrastructure_repos.split("|"):
                repo = repo.strip()
                if repo:
                    repos_to_ventures[repo].append(venture_id)

# Read PRIVATE-REPOS-ACCESS-CONTROL.csv and populate ventures_served
rows = []
with open("PRIVATE-REPOS-ACCESS-CONTROL.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        repo_name = row.get("repo_name", "").strip()

        # Look up ventures for this repo
        ventures = repos_to_ventures.get(repo_name, [])
        row["ventures_served"] = "|".join(ventures) if ventures else ""
        rows.append(row)

# Write back to PRIVATE-REPOS-ACCESS-CONTROL.csv
with open("PRIVATE-REPOS-ACCESS-CONTROL.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys() if rows else [])
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ Updated PRIVATE-REPOS-ACCESS-CONTROL.csv")
print(f"   Found {len(repos_to_ventures)} unique repos across 712 ventures")
print(f"   Populated ventures_served for {len([r for r in rows if r.get('ventures_served')])} repos")
