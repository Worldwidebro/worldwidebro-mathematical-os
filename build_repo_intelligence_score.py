#!/usr/bin/env python3
"""
build_repo_intelligence_score.py — the harmony layer.

Combines the outputs of the existing Repository-Intelligence tools into ONE unified
100-point score per repo, implementing the 8-dimension framework:

    Strategic Importance (0-20)  Capability Depth (0-15)   Ecosystem Fit (0-15)
    Production Readiness (0-15)  Agent-Native (0-10)       Business Value (0-10)
    Differentiation (0-10)       Maintenance Risk (-5..0)

This script INVENTS no data. Every sub-score is derived from a signal another tool
already produced, so fixing/rerunning an upstream tool automatically improves the score:

    scan_repositories.py          -> REPOSITORY-REGISTRY.json      (stars, forks, language, category)
    repo_classification_phase2.py -> strategic_value / revenue_potential / reusability_score
    build_repo_summaries.py       -> repo-summaries.json           (scores{}, high_value)
    build_execution_readiness.py  -> execution-readiness.csv       (dockerized, manifest, license, archived)
    build_capability_catalog.py   -> capabilities-catalog.json     (capability -> repos, rarity)
    build_used_by_ventures.py     -> repo-used-by-ventures.json    (used_by_ventures, match_count)

Outputs:
    repo-intelligence-scores.json   full per-repo breakdown + metadata + tier summary
    repo-intelligence-leaderboard.csv   ranked flat table for quick review

Usage:
    python3 build_repo_intelligence_score.py            # score everything
    python3 build_repo_intelligence_score.py --top 25   # score + print top 25
"""
import argparse
import csv
import json
import math
import os
import re
from collections import defaultdict
from datetime import date, datetime, timezone

DOCS = "/Users/acebless/Documents"
REGISTRY = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json"
SUMMARIES = f"{DOCS}/repo-summaries.json"
READINESS = f"{DOCS}/execution-readiness.csv"
CAP_CATALOG = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries/capabilities-catalog.json"
USED_BY = f"{DOCS}/repo-used-by-ventures.json"

OUT_JSON = f"{DOCS}/repo-intelligence-scores.json"
OUT_CSV = f"{DOCS}/repo-intelligence-leaderboard.csv"

# AI/agent-native capability signals (drive the Agent-Native dimension)
AGENT_CAPS = {"ai", "agent", "mcp", "llm", "rag", "embeddings", "vector-search"}


def _norm_cap(cap):
    """Match build_capability_catalog.py's normalization so rarity lookups line up:
    lowercase, collapse whitespace/underscores to single hyphen."""
    c = re.sub(r"[\s_]+", "-", (cap or "").strip().lower())
    return re.sub(r"-+", "-", c).strip("-")


def _load_json(path, default=None):
    if not os.path.exists(path):
        print(f"  [warn] missing: {path} (dimension using it will score 0)")
        return default if default is not None else {}
    with open(path) as f:
        return json.load(f)


def load_registry():
    """name -> registry record (the spine; every scored repo comes from here)."""
    d = _load_json(REGISTRY, {"repositories": []})
    return {r["name"]: r for r in d.get("repositories", [])}, d.get("metadata", {})


def load_summaries():
    """name -> summary record (has curated scores{} + high_value)."""
    d = _load_json(SUMMARIES, {"summaries": {}})
    return d.get("summaries", {})


def load_readiness():
    """repo_name -> readiness row (deployability flags)."""
    out = {}
    if not os.path.exists(READINESS):
        print(f"  [warn] missing: {READINESS} (Production Readiness will score 0)")
        return out
    with open(READINESS) as f:
        for row in csv.DictReader(f):
            out[row["repo_name"]] = row
    return out


def load_capability_index():
    """Build name -> set(caps) and cap -> rarity(repo_count) from the catalog."""
    d = _load_json(CAP_CATALOG, {"capabilities": []})
    repo_to_caps = defaultdict(set)
    cap_rarity = {}
    for cap in d.get("capabilities", []):
        cap_rarity[cap["name"]] = cap.get("repo_count", 0)
        for repo in cap.get("repos", []):
            repo_to_caps[repo].add(cap["name"])
    return repo_to_caps, cap_rarity


def load_used_by():
    """name -> used_by record (venture linkage)."""
    return _load_json(USED_BY, {})


def _truthy(v):
    return str(v).strip().lower() in ("true", "1", "yes")


def _stars(rec):
    return rec.get("stars") or 0


def _caps_for(name, rec, repo_to_caps, summaries):
    """Union of capabilities from all sources (registry, catalog, summaries)."""
    caps = set(rec.get("capabilities") or [])
    caps |= repo_to_caps.get(name, set())
    s = summaries.get(name)
    if s:
        caps |= set(s.get("capabilities") or [])
    return {_norm_cap(c) for c in caps if c}


# --------------------------- dimension scorers ---------------------------

def score_strategic(rec, summaries, name):
    """0-20. From strategic_value (1-10), doubled. Prefer curated summary score."""
    s = summaries.get(name)
    sv = (s.get("scores", {}).get("strategic") if s else None)
    if sv is None:
        sv = rec.get("strategic_value") or 0
    return max(0, min(20, round(sv * 2)))


def score_capability_depth(caps):
    """0-15. Breadth of distinct capabilities (5 caps => full marks)."""
    return max(0, min(15, len(caps) * 3))


def score_ecosystem_fit(readiness_row, caps):
    """0-15. MCP-compatible + packaged + capability breadth = integrates with the stack."""
    score = 0
    if readiness_row:
        if _truthy(readiness_row.get("mcp_compatible")):
            score += 7
        if _truthy(readiness_row.get("has_package_manifest")):
            score += 4
    # capability breadth contributes the remainder
    score += min(4, len(caps))
    return max(0, min(15, score))


def score_production(readiness_row):
    """0-15. Concrete deployability flags."""
    if not readiness_row:
        return 0
    score = 0
    if _truthy(readiness_row.get("dockerized")):
        score += 5
    if _truthy(readiness_row.get("has_package_manifest")):
        score += 4
    if _truthy(readiness_row.get("has_license")):
        score += 3
    if _truthy(readiness_row.get("production_ready")):
        score += 3
    return max(0, min(15, score))


def score_agent_native(caps):
    """0-10. Does it advance autonomous agents? Presence of AI/agent/mcp caps."""
    hits = caps & AGENT_CAPS
    return max(0, min(10, len(hits) * 4))


def score_business(rec, summaries, name):
    """0-10. From revenue_potential (1-10). Prefer curated summary score."""
    s = summaries.get(name)
    rv = (s.get("scores", {}).get("revenue") if s else None)
    if rv is None:
        rv = rec.get("revenue_potential") or 0
    return max(0, min(10, round(rv)))


def score_differentiation(rec, caps, cap_rarity):
    """0-10. Popularity (log stars) + capability rarity (uncommon caps = differentiated)."""
    stars = _stars(rec)
    pop = min(6, math.log10(stars + 1) * 1.5) if stars > 0 else 0  # 0..6
    # rarity: caps present in <=25 repos are distinctive
    rare = sum(1 for c in caps if 0 < cap_rarity.get(c, 999) <= 25)
    rare_score = min(4, rare * 2)
    return max(0, min(10, round(pop + rare_score)))


def score_risk(rec, readiness_row):
    """-5..0. Penalties: archived, stale, unlicensed."""
    penalty = 0
    if readiness_row:
        if _truthy(readiness_row.get("archived")):
            penalty -= 3
        if not _truthy(readiness_row.get("has_license")):
            penalty -= 1
        last = readiness_row.get("last_push", "")
        if last:
            try:
                dt = datetime.fromisoformat(last.replace("Z", "+00:00"))
                days = (datetime.now(timezone.utc) - dt).days
                if days > 730:
                    penalty -= 2
                elif days > 365:
                    penalty -= 1
            except ValueError:
                pass
    return max(-5, penalty)


def tier(total):
    if total >= 85:
        return "S — Core Infrastructure"
    if total >= 70:
        return "A — Major Subsystem"
    if total >= 55:
        return "B — Useful Tool"
    if total >= 40:
        return "C — Nice-to-have"
    return "D — Experimental/Retire"


def build(top=None):
    print("=" * 78)
    print("REPOSITORY INTELLIGENCE — UNIFIED 100-POINT SCORE")
    print("=" * 78)
    registry, reg_meta = load_registry()
    summaries = load_summaries()
    readiness = load_readiness()
    repo_to_caps, cap_rarity = load_capability_index()
    used_by = load_used_by()
    print(f"  registry: {len(registry)} repos | summaries: {len(summaries)} | "
          f"readiness: {len(readiness)} | capability-index: {len(repo_to_caps)} repos")
    if registry:
        cov = 100 * len(readiness) / len(registry)
        print(f"  [coverage] execution-readiness.csv covers {len(readiness)}/{len(registry)} "
              f"repos ({cov:.0f}%). Repos without a readiness row score 0 on Production "
              f"Readiness & part of Ecosystem Fit — low scores there may mean 'not yet checked', "
              f"not 'not deployable'. Run build_execution_readiness.py on more repos to raise coverage.")

    scored = []
    for name, rec in registry.items():
        caps = _caps_for(name, rec, repo_to_caps, summaries)
        rrow = readiness.get(name)
        dims = {
            "strategic_importance": score_strategic(rec, summaries, name),
            "capability_depth": score_capability_depth(caps),
            "ecosystem_fit": score_ecosystem_fit(rrow, caps),
            "production_readiness": score_production(rrow),
            "agent_native": score_agent_native(caps),
            "business_value": score_business(rec, summaries, name),
            "differentiation": score_differentiation(rec, caps, cap_rarity),
            "maintenance_risk": score_risk(rec, rrow),
        }
        total = max(0, min(100, sum(dims.values())))
        ub = used_by.get(name, {})
        scored.append({
            "name": name,
            "total_score": total,
            "tier": tier(total),
            "category": rec.get("CATEGORY", "Unknown"),
            "stars": _stars(rec),
            "language": rec.get("language", "Unknown"),
            "capabilities": sorted(caps),
            "used_by_ventures": ub.get("used_by_ventures", []),
            "venture_match_count": ub.get("match_count", 0),
            "dimensions": dims,
            "url": rec.get("url", ""),
        })

    scored.sort(key=lambda x: x["total_score"], reverse=True)

    tier_counts = defaultdict(int)
    for r in scored:
        tier_counts[r["tier"]] += 1
    avg = round(sum(r["total_score"] for r in scored) / len(scored), 1) if scored else 0

    out = {
        "metadata": {
            "generated_date": date.today().isoformat(),
            "total_repos_scored": len(scored),
            "average_score": avg,
            "registry_generated_at": reg_meta.get("generated_at", ""),
            "framework": {
                "strategic_importance": 20, "capability_depth": 15, "ecosystem_fit": 15,
                "production_readiness": 15, "agent_native": 10, "business_value": 10,
                "differentiation": 10, "maintenance_risk": -5,
            },
            "sources": [
                "REPOSITORY-REGISTRY.json", "repo-summaries.json", "execution-readiness.csv",
                "capabilities-catalog.json", "repo-used-by-ventures.json",
            ],
            "tier_distribution": dict(tier_counts),
        },
        "repositories": scored,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)

    fields = ["rank", "name", "total_score", "tier", "category", "stars", "language",
              "venture_match_count", "strategic_importance", "capability_depth",
              "ecosystem_fit", "production_readiness", "agent_native", "business_value",
              "differentiation", "maintenance_risk", "url"]
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for i, r in enumerate(scored, 1):
            row = {"rank": i, "name": r["name"], "total_score": r["total_score"],
                   "tier": r["tier"], "category": r["category"], "stars": r["stars"],
                   "language": r["language"], "venture_match_count": r["venture_match_count"],
                   "url": r["url"]}
            row.update(r["dimensions"])
            w.writerow(row)

    print(f"\n  wrote {OUT_JSON}")
    print(f"  wrote {OUT_CSV}")
    print(f"  scored {len(scored)} repos | average {avg}/100")
    print("\n  Tier distribution:")
    for t in sorted(tier_counts):
        print(f"    {t:32s}: {tier_counts[t]:5d}")

    if top:
        print(f"\n  Top {top} by unified score:")
        print(f"    {'#':>3}  {'score':>5}  {'repo':40s}  tier")
        for i, r in enumerate(scored[:top], 1):
            print(f"    {i:>3}  {r['total_score']:>5}  {r['name'][:40]:40s}  {r['tier']}")
    print("=" * 78)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=None)
    a = ap.parse_args()
    build(top=a.top)
