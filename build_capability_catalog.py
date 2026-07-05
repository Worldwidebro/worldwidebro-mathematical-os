#!/usr/bin/env python3
"""
build_capability_catalog.py — Product #4: the Capability Catalog (the join key).

Regenerates the two STALE files (capabilities-taxonomy.json = 11 caps;
repos-by-capability.json = opaque `repo_107` ids) into ONE usable catalog that
links each capability to REAL repo names AND ventures.

Sources (both local, no cloud):
  - repo-capabilities-backfill.json           repo name -> canonical capabilities[] (1,597 repos, 71% coverage)
  - registries/venture_capability_map.csv    venture_id -> capability   (3,074 rows)

Output:
  - WORLDWIDEBRO-OS/08-DATA/registries/capabilities-catalog.json

Normalization (Phase 3): lowercase, separator-collapse, + alias map for common dupes.
This is the join layer for: Repository -> Capability -> Venture -> OPCO -> Holding.

Usage:
  python3 build_capability_catalog.py            # build catalog
  python3 build_capability_catalog.py --top 30   # build + print top capabilities
"""
import argparse
import csv
import json
import re
from collections import defaultdict
from datetime import date

DOCS = "/Users/acebless/Documents"
REPO_CAPS_BACKFILL = f"{DOCS}/repo-capabilities-backfill.json"
VENTURE_CAP = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries/venture_capability_map.csv"
VOCAB = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries/capability_vocabulary.json"
OUT = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries/capabilities-catalog.json"


def load_vocab():
    """Canonical vocabulary (single source of truth). Returns (alias->canonical, canonical->meta)."""
    v = json.load(open(VOCAB))["canonical"]
    alias_map = {}
    for canon, meta in v.items():
        alias_map[canon] = canon
        for a in meta.get("aliases", []):
            alias_map[_norm(a)] = canon
    return alias_map, v


def _norm(cap):
    c = re.sub(r"[\s_]+", "-", (cap or "").strip().lower())
    return re.sub(r"-+", "-", c).strip("-")


# Phase 3 normalization: collapse synonyms to one canonical capability via the vocab file.
ALIAS_MAP, CANON = load_vocab()


def normalize(cap):
    return ALIAS_MAP.get(_norm(cap), _norm(cap))


def load_repo_caps():
    """capability -> set(repo names).

    Reads repo-capabilities-backfill.json, not repos-index.json: the backfill
    file already matches repos against the canonical vocab (71% coverage), so
    values are canonical terms directly. repos-index.json's `capabilities` are
    raw GitHub topics (ai, docker, claude-code...) which rarely equal a
    functional venture capability even after alias normalization - that
    mismatch was why only ~10/1205 capabilities used to join both sides.
    """
    d = json.load(open(REPO_CAPS_BACKFILL))
    cap_to_repos = defaultdict(set)
    for name, caps in d["repos"].items():
        for c in caps:
            cap_to_repos[normalize(c)].add(name)
    return cap_to_repos


def load_venture_caps():
    """capability -> set(venture ids)"""
    cap_to_ventures = defaultdict(set)
    with open(VENTURE_CAP) as f:
        for row in csv.DictReader(f):
            cap_to_ventures[normalize(row["capability"])].add(row["venture_id"])
    return cap_to_ventures


def build(top=None):
    repo_caps = load_repo_caps()
    vent_caps = load_venture_caps()
    all_caps = sorted(set(repo_caps) | set(vent_caps))

    catalog = []
    for c in all_caps:
        repos = sorted(repo_caps.get(c, []))
        nv = len(vent_caps.get(c, []))
        sources = []
        if repos:
            sources.append("repos-index")
        if nv:
            sources.append("venture_capability_map")
        catalog.append({
            "name": c,
            "canonical": c in CANON,
            "category": CANON.get(c, {}).get("category", ""),
            "repos": repos,
            "repo_count": len(repos),
            "venture_count": nv,
            "joined": len(repos) > 0 and nv > 0,  # capability bridges repo AND venture
            "sources": sources,
        })

    # rank: capabilities that bridge both sides and have many repos/ventures first
    catalog.sort(key=lambda x: (x["joined"], x["repo_count"] + x["venture_count"]), reverse=True)

    joined = sum(1 for x in catalog if x["joined"])
    out = {
        "metadata": {
            "generated_date": date.today().isoformat(),
            "total_capabilities": len(catalog),
            "joined_capabilities": joined,
            "repo_only": sum(1 for x in catalog if x["repos"] and not x["venture_count"]),
            "venture_only": sum(1 for x in catalog if x["venture_count"] and not x["repos"]),
            "sources": ["repos-index.json", "venture_capability_map.csv"],
            "note": "Repo vocab = GitHub topics (noisy); venture vocab = functional terms. "
                    "'joined' caps are where both sides agree after normalization.",
        },
        "capabilities": catalog,
    }
    json.dump(out, open(OUT, "w"), indent=2)
    m = out["metadata"]
    print(f"wrote {OUT}")
    print(f"  {m['total_capabilities']} capabilities | "
          f"joined(repo+venture)={m['joined_capabilities']} | "
          f"repo_only={m['repo_only']} | venture_only={m['venture_only']}")
    if top:
        print(f"\nTop {top} capabilities (bridging repos<->ventures):")
        for x in catalog[:top]:
            flag = "*" if x["joined"] else " "
            print(f" {flag} {x['name']:<22} repos={x['repo_count']:<4} ventures={x['venture_count']}")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=None)
    a = ap.parse_args()
    build(top=a.top)
