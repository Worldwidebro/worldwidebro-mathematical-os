#!/usr/bin/env python3
"""
build_capability_backfill.py — PASS 2: deterministic repo-side capability backfill.

Raises repo canonical-capability coverage from ~10% toward the majority of 1,597 repos
by matching each repo's text signal (name + PURPOSE + TECH_STACK + language + registry
capabilities + README keywords/summary) against the canonical vocabulary (terms + aliases).

Deterministic, local only, no LLM, no new vector DB.

Inputs:
  - WORLDWIDEBRO-OS/.../REFERENCE/REPOSITORY-REGISTRY.json   (1597 repos)
  - repo-summaries.json
  - readmes.json                                             (whatever rows exist; non-blocking)
  - WORLDWIDEBRO-OS/08-DATA/registries/capability_vocabulary.json  (source of truth)

Outputs:
  - repo-capabilities-backfill.json   {metadata:{coverage_before,coverage_after,...}, repos:{name:[caps]}}
  - Neo4j: MERGE (r:Repo {name})-[:IMPLEMENTS]->(c:Capability {name})   (MERGE only, no deletes)

Usage: python3 build_capability_backfill.py
"""
import json
import re
from datetime import date

from neo4j import GraphDatabase

DOCS = "/Users/acebless/Documents"
REGISTRY = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json"
SUMMARIES = f"{DOCS}/repo-summaries.json"
READMES = f"{DOCS}/readmes.json"
VOCAB = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries/capability_vocabulary.json"
OUT = f"{DOCS}/repo-capabilities-backfill.json"
NEO4J_URI, NEO4J_AUTH = "bolt://localhost:7687", ("neo4j", "ventures2026")


def toks(text):
    return [t for t in re.split(r"[^a-z0-9]+", (text or "").lower()) if t]


def load_triggers():
    """canonical term -> list of trigger token-tuples (term + aliases)."""
    v = json.load(open(VOCAB))["canonical"]
    triggers = {}
    for term, meta in v.items():
        phrases = [term] + meta.get("aliases", [])
        triggers[term] = [tuple(toks(p)) for p in phrases if toks(p)]
    return triggers


def matches(blob_tokens, trigger_tuples):
    word_set = set(blob_tokens)
    joined = " " + " ".join(blob_tokens) + " "
    for tt in trigger_tuples:
        if len(tt) == 1:
            if tt[0] in word_set:
                return True
        else:
            if " " + " ".join(tt) + " " in joined:
                return True
    return False


def parse_list(val):
    if isinstance(val, list):
        return val
    if not val or val in ("[]", ""):
        return []
    try:
        return json.loads(val.replace("'", '"'))
    except Exception:
        return [x.strip(" '\"") for x in str(val).strip("[]").split(",") if x.strip()]


def main():
    triggers = load_triggers()
    repos = json.load(open(REGISTRY))["repositories"]
    readmes = {}
    try:
        readmes = json.load(open(READMES)).get("readmes", {})
    except Exception:
        pass

    assigned = {}
    coverage_before = 0  # repos with >=1 canonical cap from EXISTING registry capabilities only
    for r in repos:
        name = r.get("name", "")
        if not name:
            continue
        # baseline signal = existing registry capabilities field
        existing = parse_list(r.get("capabilities"))
        base_caps = {t for t in triggers if matches(toks(" ".join(existing)), triggers[t])}
        if base_caps:
            coverage_before += 1
        # full deterministic blob
        rm = readmes.get(name, {})
        blob = " ".join([
            name or "", r.get("PURPOSE") or "", r.get("TECH_STACK") or "", r.get("language") or "",
            " ".join(existing), " ".join(rm.get("keywords") or []), rm.get("readme_summary") or "",
        ])
        bt = toks(blob)
        caps = sorted(t for t in triggers if matches(bt, triggers[t]))
        if caps:
            assigned[name] = caps

    coverage_after = len(assigned)
    total = len(repos)

    # write Neo4j edges (MERGE only)
    d = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
    rows = [{"name": n, "caps": c} for n, c in assigned.items()]
    with d.session() as s:
        for i in range(0, len(rows), 300):
            s.run("""
            UNWIND $rows AS row
            MERGE (r:Repo {name: row.name})
            WITH r, row
            UNWIND row.caps AS cap
              MERGE (c:Capability {name: cap})
              MERGE (r)-[:IMPLEMENTS]->(c)
            """, rows=rows[i:i + 300])
        edges = s.run("MATCH ()-[x:IMPLEMENTS]->() RETURN count(x) AS c").single()["c"]
        repos_with = s.run("MATCH (r:Repo)-[:IMPLEMENTS]->(:Capability) RETURN count(DISTINCT r) AS c").single()["c"]
    d.close()

    meta = {
        "generated_date": date.today().isoformat(),
        "total_repos": total,
        "coverage_before": coverage_before,
        "coverage_before_pct": round(100 * coverage_before / total, 1),
        "coverage_after": coverage_after,
        "coverage_after_pct": round(100 * coverage_after / total, 1),
        "readmes_used": len(readmes),
        "neo4j_implements_edges": edges,
        "neo4j_repos_with_cap": repos_with,
    }
    json.dump({"metadata": meta, "repos": assigned}, open(OUT, "w"), indent=2)
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
