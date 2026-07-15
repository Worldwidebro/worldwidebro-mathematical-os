#!/usr/bin/env python3
"""
load_graph_stack.py — Ingest venture/repo data into the local graph stack.

Targets the colima-hosted services:
  - Neo4j   (bolt://localhost:7687)  ventures + sectors + repos + relationships
  - Qdrant  (http://localhost:6333)  repo semantic vectors (Ollama nomic-embed-text)
  - Redis   (localhost:6379)         run metadata + cached counts

Sources (source of truth = CSV, not GitHub API):
  - venture-hub/ventures-master.csv         (712 ventures)
  - venture-hub/MASTER-REPO-REGISTRY.csv    (985 repos, mapped to ventures)

Usage:
  python3 load_graph_stack.py            # full load
  python3 load_graph_stack.py --limit 100  # cap repo embeddings (faster smoke test)
"""
import csv
import sys
import json
import time
import argparse
import datetime as dt
from concurrent.futures import ThreadPoolExecutor

import requests
import redis
from neo4j import GraphDatabase

BASE = "/Users/acebless/Documents"
VH = f"{BASE}/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/INFRASTRUCTURE_LAYERS/venture-hub"
VENTURES_CSV = f"{VH}/ventures-master.csv"
REPOS_CSV = f"{VH}/MASTER-REPO-REGISTRY.csv"

NEO4J_URI = "bolt://100.87.214.70:7687"
NEO4J_AUTH = ("neo4j", "ventures2026")
QDRANT = "http://100.87.214.70:6333"
OLLAMA = "http://100.87.214.70:11434/api/embeddings"
EMBED_MODEL = "nomic-embed-text"
EMBED_DIM = 768
COLLECTION = "repositories"


def log(msg):
    print(f"[{dt.datetime.now():%H:%M:%S}] {msg}", flush=True)


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ---------------------------------------------------------------- Neo4j
def load_neo4j(ventures, repos):
    drv = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
    with drv.session() as s:
        s.run("CREATE CONSTRAINT venture_id IF NOT EXISTS "
              "FOR (v:Venture) REQUIRE v.id IS UNIQUE")
        s.run("CREATE CONSTRAINT repo_name IF NOT EXISTS "
              "FOR (r:Repo) REQUIRE r.name IS UNIQUE")
        s.run("CREATE CONSTRAINT sector_name IF NOT EXISTS "
              "FOR (x:Sector) REQUIRE x.name IS UNIQUE")

        # Ventures + sectors
        s.run("""
        UNWIND $rows AS row
        MERGE (v:Venture {id: row.venture_id})
          SET v.name = row.name, v.stage = row.stage, v.status = row.status,
              v.repository_url = row.repository_url
        WITH v, row WHERE row.sector IS NOT NULL AND row.sector <> ''
        MERGE (sct:Sector {name: row.sector})
        MERGE (v)-[:IN_SECTOR]->(sct)
        """, rows=[{k: (r.get(k) or "") for k in
                    ("venture_id", "name", "sector", "stage", "status", "repository_url")}
                   for r in ventures])

        # Repos + BELONGS_TO
        s.run("""
        UNWIND $rows AS row
        MERGE (r:Repo {name: row.repo_name})
          SET r.description = row.description, r.role = row.company_role,
              r.status = row.status, r.health_score = row.health_score,
              r.url = row.repository_url, r.lifecycle_stage = coalesce(r.lifecycle_stage,'Candidate')
        WITH r, row WHERE row.venture_id IS NOT NULL AND row.venture_id <> ''
        MATCH (v:Venture {id: row.venture_id})
        MERGE (r)-[:BELONGS_TO]->(v)
        """, rows=[{k: (r.get(k) or "") for k in
                    ("repo_name", "description", "company_role", "status",
                     "health_score", "repository_url", "venture_id")}
                   for r in repos])

        counts = {
            "ventures": s.run("MATCH (v:Venture) RETURN count(v) AS c").single()["c"],
            "repos": s.run("MATCH (r:Repo) RETURN count(r) AS c").single()["c"],
            "sectors": s.run("MATCH (x:Sector) RETURN count(x) AS c").single()["c"],
            "rels": s.run("MATCH ()-[x]->() RETURN count(x) AS c").single()["c"],
        }
    drv.close()
    return counts


# ---------------------------------------------------------------- Qdrant
def embed(text):
    r = requests.post(OLLAMA, json={"model": EMBED_MODEL, "prompt": text[:2000]}, timeout=60)
    r.raise_for_status()
    return r.json()["embedding"]


def ensure_collection():
    requests.delete(f"{QDRANT}/collections/{COLLECTION}")
    requests.put(f"{QDRANT}/collections/{COLLECTION}", json={
        "vectors": {"size": EMBED_DIM, "distance": "Cosine"}
    }).raise_for_status()


def load_qdrant(repos, limit):
    ensure_collection()
    rows = [r for r in repos if (r.get("description") or "").strip()][:limit]
    log(f"Qdrant: embedding {len(rows)} repos via {EMBED_MODEL} ...")

    def make_point(i_r):
        i, r = i_r
        text = f"{r['repo_name']}. {r.get('description','')}. sector={r.get('sector','')}"
        return {
            "id": i,
            "vector": embed(text),
            "payload": {
                "name": r["repo_name"],
                "sector": r.get("sector", ""),
                "venture_id": r.get("venture_id", ""),
                "role": r.get("company_role", ""),
                "lifecycle_stage": "Candidate",
            },
        }

    points, done = [], 0
    with ThreadPoolExecutor(max_workers=6) as ex:
        for pt in ex.map(make_point, enumerate(rows)):
            points.append(pt)
            done += 1
            if done % 100 == 0:
                log(f"  embedded {done}/{len(rows)}")
            if len(points) >= 128:
                requests.put(f"{QDRANT}/collections/{COLLECTION}/points",
                             json={"points": points}).raise_for_status()
                points = []
    if points:
        requests.put(f"{QDRANT}/collections/{COLLECTION}/points",
                     json={"points": points}).raise_for_status()

    info = requests.get(f"{QDRANT}/collections/{COLLECTION}").json()["result"]
    return info["points_count"]


def qdrant_search(query):
    vec = embed(query)
    r = requests.post(f"{QDRANT}/collections/{COLLECTION}/points/search",
                      json={"vector": vec, "limit": 5, "with_payload": True})
    return r.json()["result"]


# ---------------------------------------------------------------- Redis
def cache_redis(stats):
    r = redis.Redis(host="localhost", port=6379, decode_responses=True)
    r.set("graphstack:last_run", dt.datetime.now().isoformat())
    r.set("graphstack:stats", json.dumps(stats))
    r.hset("graphstack:counts", mapping={k: str(v) for k, v in stats.items()})
    return r.dbsize()


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=10**9,
                    help="cap number of repos embedded into Qdrant")
    args = ap.parse_args()

    t0 = time.time()
    ventures = read_csv(VENTURES_CSV)
    repos = read_csv(REPOS_CSV)
    log(f"Loaded CSVs: {len(ventures)} ventures, {len(repos)} repos")

    log("→ Neo4j ...")
    ncounts = load_neo4j(ventures, repos)
    log(f"  Neo4j: {ncounts}")

    log("→ Qdrant ...")
    qcount = load_qdrant(repos, args.limit)
    log(f"  Qdrant: {qcount} vectors in '{COLLECTION}'")

    stats = {**ncounts, "qdrant_vectors": qcount,
             "elapsed_s": round(time.time() - t0, 1)}
    keys = cache_redis(stats)
    log(f"  Redis: cached stats, dbsize={keys}")

    log("→ Smoke-test semantic search: 'payroll and HR automation'")
    for hit in qdrant_search("payroll and HR automation"):
        log(f"    {hit['score']:.3f}  {hit['payload']['name']}  [{hit['payload']['sector']}]")

    log(f"DONE in {stats['elapsed_s']}s — data is flowing.")


if __name__ == "__main__":
    main()
