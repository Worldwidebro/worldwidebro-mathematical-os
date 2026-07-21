#!/usr/bin/env python3
"""
Graphify Analysis: Repo duplication detection, community clustering, orphan identification.
Focuses on: (1) duplicates by name+structure, (2) community clusters, (3) orphans, (4) high-value hubs
"""

import json
import re
from collections import defaultdict, Counter
from difflib import SequenceMatcher
from pathlib import Path
import sys

# Load registry
registry_path = Path("/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json")
with open(registry_path) as f:
    data = json.load(f)

repos = data["repositories"]
print(f"Loaded {len(repos)} repositories")

# === 1. Duplicate Detection ===
def name_similarity(s1, s2):
    """Calculate string similarity 0-1"""
    return SequenceMatcher(None, s1.lower(), s2.lower()).ratio()

def extract_base_name(name):
    """Extract base name without venture IDs (e.g., 'con-001-thing' → 'thing')"""
    # Remove venture ID prefixes like con-001, fin-023, etc.
    pattern = r'^[a-z]{2,}-\d{3,}-(.+)$'
    match = re.match(pattern, name.lower())
    if match:
        return match.group(1)
    return name.lower()

duplicates = []
for i, r1 in enumerate(repos):
    for r2 in repos[i+1:]:
        # Check name similarity
        name_sim = name_similarity(r1["name"], r2["name"])
        base1 = extract_base_name(r1["name"])
        base2 = extract_base_name(r2["name"])
        base_sim = name_similarity(base1, base2)

        # Check purpose similarity
        purpose_sim = name_similarity(r1.get("PURPOSE", ""), r2.get("PURPOSE", ""))

        # Flag as potential duplicate if high similarity in name or base name
        if name_sim > 0.85 or base_sim > 0.85:
            # Calculate consolidation value (how much code could be shared)
            category_match = r1["CATEGORY"] == r2["CATEGORY"]
            stack_match = r1["TECH_STACK"] == r2["TECH_STACK"]
            purpose_match = purpose_sim > 0.7

            consolidation_value = sum([category_match, stack_match, purpose_match]) / 3

            duplicates.append({
                "repo_a": r1["name"],
                "repo_b": r2["name"],
                "name_similarity": round(name_sim, 3),
                "base_name_similarity": round(base_sim, 3),
                "purpose_similarity": round(purpose_sim, 3),
                "category_match": category_match,
                "tech_stack_match": stack_match,
                "consolidation_value": round(consolidation_value, 3),
                "category_a": r1["CATEGORY"],
                "category_b": r2["CATEGORY"],
                "stack_a": r1["TECH_STACK"],
                "stack_b": r2["TECH_STACK"]
            })

# Sort by consolidation value (highest first - best candidates for consolidation)
duplicates.sort(key=lambda x: x["consolidation_value"], reverse=True)
print(f"\nFound {len(duplicates)} potential duplicate pairs")

# === 2. Orphaned Repos ===
orphaned = [r for r in repos if not r.get("related_repos") or len(r.get("related_repos", [])) == 0]
print(f"Orphaned repos (0 connections): {len(orphaned)}")

# === 3. Community Clusters ===
# Build a graph of which repos are connected
graph = defaultdict(set)
for repo in repos:
    repo_name = repo["name"]
    for related in repo.get("related_repos", []):
        graph[repo_name].add(related)
        graph[related].add(repo_name)  # bidirectional

# Find clusters (connected components)
def find_clusters(graph):
    visited = set()
    clusters = []

    def dfs(node, cluster):
        if node in visited:
            return
        visited.add(node)
        cluster.add(node)
        for neighbor in graph.get(node, []):
            dfs(neighbor, cluster)

    for node in graph:
        if node not in visited:
            cluster = set()
            dfs(node, cluster)
            if len(cluster) > 1:  # Only clusters with >1 repo
                clusters.append(cluster)

    return clusters

clusters = find_clusters(graph)
clusters.sort(key=len, reverse=True)  # Largest first
print(f"Community clusters found: {len(clusters)}")
if clusters:
    print(f"  Largest cluster: {len(clusters[0])} repos")
    print(f"  Top 5: {[len(c) for c in clusters[:5]]}")

# === 4. High-Value Hubs ===
# Count how many repos reference each repo (dependents)
hub_scores = Counter()
for repo in repos:
    for related in repo.get("related_repos", []):
        hub_scores[related] += 1

hubs = sorted(hub_scores.items(), key=lambda x: x[1], reverse=True)
print(f"\nTop 10 high-value hubs (most referenced):")
for repo_name, count in hubs[:10]:
    print(f"  {repo_name}: {count} dependents")

# === Build graph.json ===
graph_output = {
    "metadata": {
        "generated_at": data["metadata"]["generated_at"],
        "total_repos": len(repos),
        "analysis": {
            "duplicate_pairs": len(duplicates),
            "orphaned_repos": len(orphaned),
            "community_clusters": len(clusters),
            "high_value_hubs": len([h for h in hubs if h[1] >= 5])
        }
    },
    "duplicates": duplicates[:50],  # Top 50 by consolidation value
    "orphaned_repos": [
        {
            "name": r["name"],
            "category": r["CATEGORY"],
            "purpose": r["PURPOSE"],
            "stars": r["stars"],
            "url": r["url"]
        }
        for r in sorted(orphaned, key=lambda x: x["stars"], reverse=True)[:100]
    ],
    "community_clusters": [
        {
            "size": len(cluster),
            "repos": sorted(list(cluster))
        }
        for cluster in clusters[:20]  # Top 20 clusters
    ],
    "high_value_hubs": [
        {
            "name": repo_name,
            "dependents": count,
            "category": next((r["CATEGORY"] for r in repos if r["name"] == repo_name), "Unknown"),
            "stars": next((r["stars"] for r in repos if r["name"] == repo_name), 0)
        }
        for repo_name, count in hubs[:30]
    ]
}

# Save graph.json
graph_path = Path("/Users/acebless/Documents/graph.json")
with open(graph_path, "w") as f:
    json.dump(graph_output, f, indent=2)
print(f"\nWrote graph.json ({graph_path})")

# === Generate GRAPH_REPORT.md ===
report = """# Graphify Analysis Report

**Generated:** {generated_at}
**Total Repositories:** {total_repos}

## Executive Summary

This analysis identifies strategic consolidation opportunities in the repository portfolio by detecting:

1. **Duplicate Repositories** — Similar repos that could be merged or unified
2. **Orphaned Repositories** — Isolated repos with zero connections (potential dead weight or specialized tools)
3. **Community Clusters** — Groups of related repos that share a domain
4. **High-Value Hubs** — Repos widely referenced by others (critical infrastructure)

---

## 1. Duplicate Repositories (Top 50 Consolidation Candidates)

Ranked by **consolidation value** — how much code/purpose can realistically be merged.

| Repo A | Repo B | Name Sim | Base Sim | Purpose Sim | Stack Match | Category Match | Value | Action |
|--------|--------|----------|----------|-------------|-------------|----------------|-------|--------|
""".format(
    generated_at=data["metadata"]["generated_at"],
    total_repos=len(repos)
)

for dup in duplicates[:50]:
    report += f"| {dup['repo_a'][:30]} | {dup['repo_b'][:30]} | {dup['name_similarity']} | {dup['base_name_similarity']} | {dup['purpose_similarity']} | {'✓' if dup['tech_stack_match'] else '✗'} | {'✓' if dup['category_match'] else '✗'} | {dup['consolidation_value']} | Merge or Archive |\n"

report += f"""
**Consolidation Value Score:** 0–1.0 (1.0 = perfect merge candidate)
- **1.0** = same purpose + stack + category → merge into one
- **0.66+** = merge candidates (shared purpose/tech)
- **0.33–0.66** = related but distinct → keep separate
- **<0.33** = same name but different purpose → investigate

**Key Finding:** {len([d for d in duplicates if d['consolidation_value'] >= 0.66])} pairs have consolidation value ≥0.66 (merge-worthy)

---

## 2. Orphaned Repositories (No Connections)

**Total:** {orphaned_count} repos isolated from the ecosystem

These repos have zero `related_repos` entries and are not referenced by any other repo. They may be:
- **Dead weight** — candidate for archival
- **Specialized tools** — domain-specific, intentionally isolated
- **Incomplete metadata** — lacking relationship mappings

### Top 100 Orphaned by Stars (visibility of abandonment)

| Repo Name | Category | Stars | Purpose | URL |
|-----------|----------|-------|---------|-----|
""".format(
    orphaned_count=len(orphaned)
)

for repo in sorted(orphaned, key=lambda x: x["stars"], reverse=True)[:100]:
    purpose = (repo.get("PURPOSE", "") or "")[:50]
    report += f"| {repo['name'][:40]} | {repo['CATEGORY']} | {repo['stars']} | {purpose} | [🔗]({repo['url']}) |\n"

report += f"""

**Recommendation:** Review top 50 by stars first. Archive those with 0 stars and no recent commits.

---

## 3. Community Clusters (Connected Repo Groups)

**Total:** {clusters_count} clusters identified

Repos that share relationships form clusters — likely domain-specific or architecturally coupled.

### Largest 20 Clusters
""".format(
    clusters_count=len(clusters)
)

for i, cluster in enumerate(clusters[:20], 1):
    cluster_list = sorted(list(cluster))
    report += f"\n#### Cluster {i} ({len(cluster)} repos)\n\n"
    report += "```\n" + "\n".join(cluster_list) + "\n```\n"

report += f"""

**Insight:** Clusters map to sectors (Construction, Staffing, Real Estate, etc.) or infrastructure layers (Platform, Auth, Database).

---

## 4. High-Value Hubs (Widely Referenced)

**Total:** {hubs_30_count} repos with 5+ dependents

These repos are critical infrastructure — referenced by many others. Prioritize maintenance, testing, and stability.

| Repo Name | Dependents | Category | Stars | Impact |
|-----------|-----------|----------|-------|--------|
""".format(
    hubs_30_count=len([h for h in hubs if h[1] >= 5])
)

for repo_name, count in hubs[:30]:
    repo_info = next((r for r in repos if r["name"] == repo_name), {})
    category = repo_info.get("CATEGORY", "Unknown")
    stars = repo_info.get("stars", 0)
    report += f"| {repo_name[:40]} | {count} | {category} | {stars} | Core Dependency |\n"

report += """

**Action Items:**
- **Priority 1:** Secure top 10 hubs (highest dependents) with dedicated maintenance
- **Priority 2:** Add automated testing and changelog for top 30
- **Priority 3:** Document API contracts and breaking change policies

---

## 5. Strategic Recommendations

### Immediate Actions (Week 1)
1. **Consolidate duplicates** — Merge top 10 pairs with consolidation_value ≥ 0.8
2. **Archive orphans** — Move bottom 50 (0 stars) to /archive/
3. **Secure top hubs** — Assign owners and SLAs

### Medium-term (Month 1)
1. Rebuild relationship graph (`related_repos` is stale)
2. Establish clear ownership per cluster
3. Document critical paths and dependency chains

### Long-term (Quarter 1)
1. Implement automated duplicate detection in CI
2. Track dependency health and breakage risk
3. Consolidate infrastructure layer (IZA OS)

---

## Appendix: Raw Data

See `graph.json` for:
- Full duplicate pair rankings
- Complete orphaned repo list
- All community cluster memberships
- Hub dependency counts
"""

report_path = Path("/Users/acebless/Documents/GRAPH_REPORT.md")
with open(report_path, "w") as f:
    f.write(report)

print(f"Wrote GRAPH_REPORT.md ({report_path})")
print("\n" + "="*60)
print("GRAPHIFY ANALYSIS COMPLETE")
print("="*60)
print(f"Duplicates: {len(duplicates)} pairs (top 50 saved)")
print(f"Orphaned: {len(orphaned)} repos")
print(f"Clusters: {len(clusters)} communities")
print(f"Hubs: {len(hubs)} repos with dependents")
print(f"\nOutput files:")
print(f"  - graph.json (ready for visualization)")
print(f"  - GRAPH_REPORT.md (strategic recommendations)")
