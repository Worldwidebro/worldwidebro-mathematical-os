#!/usr/bin/env python3
"""
build_venture_capabilities.py — PASS 2 (venture side): usable Venture->Capability link.

The existing venture_capability_map.csv is UUID-keyed and does NOT match the readable
venture ids (9/627 overlap = noise), and required_capabilities is empty. This builds a
deterministic, readable-id Venture->Capability map and loads (Venture)-[:NEEDS]->(Capability)
edges into Neo4j, so the Repo->Capability<-Venture bridge resolves by GRAPH, not semantic guess.

Inputs (local):
  - WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv            (712: venture_id, name, sector)
  - WORLDWIDEBRO-OS/08-DATA/registries/capability_vocabulary.json (25 canonical + aliases)

Outputs:
  - venture-capabilities-proposed.csv   (venture_id, capability — readable ids)
  - Neo4j MERGE (v:Venture {id})-[:NEEDS]->(c:Capability {name})

Usage:
  python3 build_venture_capabilities.py
  python3 build_venture_capabilities.py --no-neo4j   # CSV only
"""
import argparse
import csv
import json
import re

DOCS = "/Users/acebless/Documents"
VENTURES = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv"
VOCAB = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries/capability_vocabulary.json"
OUT = f"{DOCS}/venture-capabilities-proposed.csv"

NEO4J_URI = "bolt://localhost:7687"
NEO4J_AUTH = ("neo4j", "ventures2026")

# Every venture is a digital product/service -> these are universal.
BASELINE = ["api", "database", "authentication", "dashboard", "payments"]

# Sector -> extra canonical capabilities (beyond baseline).
SECTOR_CAPS = {
    "e-commerce": ["payments", "search", "crm", "analytics", "notifications"],
    "operations": ["automation", "scheduling", "analytics", "monitoring"],
    "technology": ["devtools", "automation", "agent", "llm", "api"],
    "software-technology": ["devtools", "automation", "agent", "llm", "api"],
    "community": ["workspace", "notifications", "crm", "search"],
    "emerging": ["agent", "llm", "automation", "analytics"],
    "specialized": ["automation", "analytics", "search"],
    "financial": ["payments", "portfolio", "security", "analytics"],
    "beauty-wellness": ["scheduling", "crm", "payments", "notifications"],
    "education": ["workspace", "search", "analytics", "notifications"],
    "education-training": ["workspace", "search", "analytics", "notifications"],
    "food-hospitality": ["scheduling", "payments", "crm", "notifications"],
    "logistics-transport": ["scheduling", "automation", "monitoring", "analytics"],
    "fitness-sports": ["scheduling", "crm", "payments", "notifications"],
    "professional-services": ["crm", "scheduling", "ocr", "analytics"],
    "media-content": ["search", "analytics", "automation", "notifications"],
    "construction": ["scheduling", "crm", "ocr", "monitoring"],
    "real-estate": ["crm", "search", "scheduling", "payments"],
}


def _norm(s):
    s = re.sub(r"[\s_]+", "-", (s or "").strip().lower())
    return re.sub(r"-+", "-", s).strip("-")


def load_alias_map():
    v = json.load(open(VOCAB))["canonical"]
    m, canon = {}, set(v)
    for c, meta in v.items():
        m[c] = c
        for a in meta.get("aliases", []):
            m[_norm(a)] = c
    return m, canon


def name_caps(name, alias):
    """Match canonical capabilities mentioned in the venture name."""
    toks = re.findall(r"[a-zA-Z]+", (name or "").lower())
    found = []
    for t in toks:
        c = alias.get(_norm(t))
        if c:
            found.append(c)
    n = _norm(name)
    for raw, c in alias.items():
        if "-" in raw and raw in n:
            found.append(c)
    return found


def build(write_neo4j=True):
    alias, canon = load_alias_map()
    rows = list(csv.DictReader(open(VENTURES)))
    mapping = {}  # venture_id -> sorted list of caps
    for r in rows:
        vid = r["venture_id"]
        sector = (r.get("sector") or "").strip().lower()
        caps = set(BASELINE)
        caps.update(SECTOR_CAPS.get(sector, []))
        caps.update(name_caps(r.get("name", ""), alias))
        caps = {c for c in caps if c in canon}
        mapping[vid] = sorted(caps)

    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["venture_id", "capability"])
        for vid, caps in mapping.items():
            for c in caps:
                w.writerow([vid, c])

    total = sum(len(c) for c in mapping.values())
    avg = round(total / max(len(mapping), 1), 1)
    print(f"wrote {OUT}")
    print(f"  ventures={len(mapping)} | venture->capability rows={total} | avg caps/venture={avg}")

    if write_neo4j:
        from neo4j import GraphDatabase
        d = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
        with d.session() as s:
            pairs = [{"v": vid, "c": c} for vid, caps in mapping.items() for c in caps]
            for i in range(0, len(pairs), 500):
                s.run("""
                UNWIND $rows AS row
                MATCH (v:Venture {id: row.v})
                MERGE (c:Capability {name: row.c})
                MERGE (v)-[:NEEDS]->(c)
                """, rows=pairs[i:i + 500])
            needs = s.run("MATCH ()-[r:NEEDS]->() RETURN count(r) AS c").single()["c"]
            ps024 = s.run("MATCH (v:Venture {id:'PS-024-Recruiting-Agency'})-[:NEEDS]->(c) "
                          "RETURN collect(c.name) AS caps").single()["caps"]
            print(f"  Neo4j [NEEDS] edges={needs}")
            print(f"  PS-024-Recruiting-Agency NEEDS: {ps024}")
            print("  --- graph bridge Repo-[:IMPLEMENTS]->Cap<-[:NEEDS]-Venture (sample) ---")
            bridge = s.run("""
                MATCH (r:Repo)-[:IMPLEMENTS]->(c:Capability)<-[:NEEDS]-(v:Venture)
                RETURN v.name AS venture, c.name AS capability, r.name AS repo LIMIT 8
            """)
            n = 0
            for rec in bridge:
                n += 1
                print(f"    {rec['venture']}  --needs--> {rec['capability']} <--implements--  {rec['repo']}")
            if n == 0:
                print("    (no bridge rows yet — repo IMPLEMENTS coverage is thin; "
                      "capability backfill fork will thicken this)")
        d.close()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-neo4j", action="store_true")
    a = ap.parse_args()
    build(write_neo4j=not a.no_neo4j)
