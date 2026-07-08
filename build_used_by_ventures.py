#!/usr/bin/env python3
"""
build_used_by_ventures.py — compute real used_by_ventures links per repo. Neither
starred_repos_with_capabilities.csv (700 repos, no used_by_ventures column at all) nor
any other file in this repo actually computes this join; this fills that gap using data
that already exists (doesn't invent a new capability vocabulary).

Naive "any capability overlaps" join is degenerate: e.g. 500-AI-Agents-Projects (caps:
agent, llm) matches 422/712 ventures on loose overlap because llm/dashboard are
near-universal venture needs. Strict-subset join (repo's capability set must be a SUBSET
of the venture's declared capability set — the venture needs everything the repo offers)
gives a meaningful, non-degenerate result instead: 141 ventures for that same repo.

Input:
  repo-capabilities-backfill.json  -> {"repos": {repo_name: [capability, ...]}}
  venture-capabilities-proposed.csv -> rows of venture_id,capability

Output: repo-used-by-ventures.json
  {repo_name: {"capabilities": [...], "used_by_ventures": [...], "match_count": N}}
"""
import csv
import json
from collections import defaultdict

DOCS = "/Users/acebless/Documents"
REPO_CAPS = f"{DOCS}/repo-capabilities-backfill.json"
VENTURE_CAPS_CSV = f"{DOCS}/venture-capabilities-proposed.csv"
OUT = f"{DOCS}/repo-used-by-ventures.json"


def main():
    repo_caps = json.load(open(REPO_CAPS))["repos"]

    venture_caps = defaultdict(set)
    with open(VENTURE_CAPS_CSV) as f:
        for row in csv.DictReader(f):
            venture_caps[row["venture_id"]].add(row["capability"])

    result = {}
    match_counts = []
    for repo, caps in repo_caps.items():
        cap_set = set(caps)
        matches = sorted(
            vid for vid, vcaps in venture_caps.items() if cap_set.issubset(vcaps)
        )
        result[repo] = {
            "capabilities": caps,
            "used_by_ventures": matches,
            "match_count": len(matches),
        }
        match_counts.append(len(matches))

    with open(OUT, "w") as f:
        json.dump(result, f, indent=2)

    zero_match = sum(1 for c in match_counts if c == 0)
    print(f"Repos processed: {len(result)}")
    print(f"Ventures with declared capabilities: {len(venture_caps)}")
    print(f"Repos with zero venture matches (capability too rare/specific): {zero_match}")
    print(f"Avg matches per repo: {sum(match_counts)/len(match_counts):.1f}")
    print(f"Written to {OUT}")


if __name__ == "__main__":
    main()
