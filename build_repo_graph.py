#!/usr/bin/env python3
"""
build_repo_graph.py — Task #4: enrich the live Neo4j graph with the Capability +
OPCO/Holding layers that load_graph_stack.py (venture-centric base) lacks.

This is an ENRICHMENT layer, NOT a parallel graph: it reuses the existing `Repo`
and `Venture` labels and only MERGEs (never wipes shared nodes).

Adds (only edges backed by REAL data):
  (Repo)-[:IMPLEMENTS]->(Capability)     from repo-summaries.json (canonical caps)
  (Capability) nodes                     from capability_vocabulary.json (25 canonical)
  (Venture)-[:BELONGS_TO]->(OPCO)        from registries/ventures.csv (opco column)
  (OPCO)-[:BELONGS_TO]->(Entity WC-LLC-001)
  (Entity)-[:BELONGS_TO]->(Entity ...)   up to TRUST-001, from entity-graph.json

KNOWN GAP (documented): (Venture)-[:NEEDS]->(Capability) is NOT built — the only
venture-capability data (venture_capability_map.csv) is UUID-orphaned and the
readable required_capabilities column is empty. retrieve.py bridges venture<->repo
via semantic search instead.

Neo4j: bolt://localhost:7687  (neo4j / ventures2026)

Usage:
  python3 build_repo_graph.py          # enrich
  python3 build_repo_graph.py --stats  # node/edge counts
"""
import argparse
import csv
import json

from neo4j import GraphDatabase

DOCS = "/Users/acebless/Documents"
SUMMARIES = f"{DOCS}/repo-summaries.json"
VOCAB = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries/capability_vocabulary.json"
VENTURES = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv"
ENTITY = f"{DOCS}/company-factory-os/entity-graph.json"

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "ventures2026")


def driver():
    return GraphDatabase.driver(URI, auth=AUTH)


def build():
    summaries = json.load(open(SUMMARIES))["summaries"]
    caps_meta = json.load(open(VOCAB))["canonical"]
    ventures = list(csv.DictReader(open(VENTURES)))
    entities = json.load(open(ENTITY))["entities"]

    d = driver()
    with d.session() as s:
        # Canonical Capability nodes
        for name, meta in caps_meta.items():
            s.run("MERGE (c:Capability {name:$n}) SET c.category=$cat",
                  n=name, cat=meta.get("category", ""))

        # Repo nodes (MERGE — shared with load_graph_stack) + IMPLEMENTS edges
        rows = [{"name": n, "category": r["category"], "language": r["language"],
                 "url": r["url"], "purpose": r["purpose"], "summary": r["summary_text"],
                 "strategic": r["scores"]["strategic"], "revenue": r["scores"]["revenue"],
                 "caps": r["capabilities"]} for n, r in summaries.items()]
        for i in range(0, len(rows), 200):
            s.run("""
            UNWIND $rows AS row
            MERGE (r:Repo {name: row.name})
              SET r.category=row.category, r.language=row.language, r.url=row.url,
                  r.purpose=row.purpose, r.summary=row.summary,
                  r.strategic=row.strategic, r.revenue=row.revenue
            WITH r, row
            UNWIND row.caps AS cap
              MATCH (c:Capability {name: cap})
              MERGE (r)-[:IMPLEMENTS]->(c)
            """, rows=rows[i:i + 200])

        # Entity chain (OPCO/Holding/Trust) from entity-graph.json
        for e in entities:
            s.run("MERGE (x:Entity {id:$id}) SET x.name=$n, x.role=$r, x.structure=$st, x.status=$status",
                  id=e["id"], n=e["name"], r=e["role"], st=e["structure"], status=e["status"])
        for e in entities:
            if e.get("parent"):
                s.run("MATCH (a:Entity {id:$c}),(b:Entity {id:$p}) MERGE (a)-[:BELONGS_TO]->(b)",
                      c=e["id"], p=e["parent"])

        # Venture (MERGE — shared) + BELONGS_TO OPCO
        for v in ventures:
            vid, opco = v["venture_id"], (v.get("opco") or "").strip()
            s.run("MERGE (vn:Venture {id:$id}) SET vn.name=$n, vn.sector=$sec, vn.stage=$stg",
                  id=vid, n=v.get("name", ""), sec=v.get("sector", ""), stg=v.get("stage", ""))
            if opco:
                s.run("MERGE (o:OPCO {id:$o})", o=opco)
                s.run("MATCH (vn:Venture {id:$id}),(o:OPCO {id:$o}) MERGE (vn)-[:BELONGS_TO]->(o)",
                      id=vid, o=opco)
        # All OPCOs roll up to the active operating entity WC-LLC-001 (per entity-graph)
        s.run("MATCH (o:OPCO),(w:Entity {id:'WC-LLC-001'}) MERGE (o)-[:BELONGS_TO]->(w)")

    stats(d)
    d.close()


def stats(d=None):
    own = d is None
    d = d or driver()
    with d.session() as s:
        for label in ["Repo", "Capability", "Venture", "OPCO", "Entity"]:
            n = s.run(f"MATCH (n:{label}) RETURN count(n) AS c").single()["c"]
            print(f"  {label:12} {n}")
        for rel in ["IMPLEMENTS", "BELONGS_TO"]:
            n = s.run(f"MATCH ()-[r:{rel}]->() RETURN count(r) AS c").single()["c"]
            print(f"  [{rel}]   {n}")
    if own:
        d.close()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()
    if a.stats:
        stats()
    else:
        build()
