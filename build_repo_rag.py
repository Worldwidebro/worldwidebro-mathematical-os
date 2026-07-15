#!/usr/bin/env python3
"""
build_repo_rag.py — RAG over all 1,597 repositories (Stage 8 of the repo-intelligence pipeline).

Embeds the full REPOSITORY-REGISTRY into the Qdrant `repositories` collection using the
already-running LOCAL stack — no cloud, no API key:
  - Qdrant  http://localhost:6333   (vector store, 768-dim Cosine)
  - Ollama  http://localhost:11434  (nomic-embed-text, same model as build_notes_rag.py)

Closes the embeddings gap: registry has 1,597 repos, Qdrant had only 544.

Usage:
  python3 build_repo_rag.py --build                 # full rebuild (all 1,597)
  python3 build_repo_rag.py --build --limit 50      # smoke test
  python3 build_repo_rag.py --query "construction marketplace software"
  python3 build_repo_rag.py --query "agent memory" --category Product
"""
import argparse
import hashlib
import json
import sys
import time

import requests

from os_env import QDRANT, OLLAMA_EMBED as OLLAMA, EMBED_MODEL

REGISTRY = ("/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/"
            "Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json")
COLLECTION = "repositories"
DIM = 768


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def load_repos():
    return json.load(open(REGISTRY))["repositories"]


def owner_of(url):
    # https://github.com/<owner>/<repo>
    parts = (url or "").rstrip("/").split("/")
    return parts[-2] if len(parts) >= 2 else ""


def embed_text(r):
    """Dense text that captures what the repo IS and what it's FOR."""
    caps = r.get("capabilities") or ""
    return (
        f"{r.get('name','')}\n"
        f"Purpose: {r.get('PURPOSE','')}\n"
        f"Category: {r.get('CATEGORY','')}\n"
        f"Tech: {r.get('TECH_STACK','')} ({r.get('language','')})\n"
        f"Capabilities: {caps}"
    )


def embed(text):
    resp = requests.post(OLLAMA, json={"model": EMBED_MODEL, "prompt": text}, timeout=120)
    resp.raise_for_status()
    return resp.json()["embedding"]


def ensure_collection(recreate=False):
    if recreate:
        requests.delete(f"{QDRANT}/collections/{COLLECTION}")
    exists = requests.get(f"{QDRANT}/collections/{COLLECTION}").status_code == 200
    if not exists:
        requests.put(f"{QDRANT}/collections/{COLLECTION}",
                     json={"vectors": {"size": DIM, "distance": "Cosine"}}).raise_for_status()


def point_id(name, url):
    h = hashlib.sha1(f"{name}|{url}".encode()).hexdigest()
    return int(h[:15], 16)


def build(limit=None, recreate=True):
    ensure_collection(recreate=recreate)
    repos = load_repos()
    if limit:
        repos = repos[:limit]
    log(f"embedding {len(repos)} repos via {EMBED_MODEL} -> '{COLLECTION}'")
    batch, total, t0 = [], 0, time.time()
    for i, r in enumerate(repos):
        try:
            vec = embed(embed_text(r))
        except Exception as e:
            log(f"  embed fail {r.get('name')}: {e}")
            continue
        batch.append({
            "id": point_id(r.get("name", ""), r.get("url", "")),
            "vector": vec,
            "payload": {
                "name": r.get("name", ""),
                "owner": owner_of(r.get("url", "")),
                "url": r.get("url", ""),
                "category": r.get("CATEGORY", ""),
                "language": r.get("language", ""),
                "tech_stack": r.get("TECH_STACK", ""),
                "purpose": (r.get("PURPOSE", "") or "")[:500],
                "capabilities": r.get("capabilities", ""),
                "stars": r.get("stars", "0"),
                "reusability_score": r.get("reusability_score", "0"),
                "revenue_potential": r.get("revenue_potential", "0"),
                "strategic_value": r.get("strategic_value", "0"),
            },
        })
        total += 1
        if len(batch) >= 128:
            requests.put(f"{QDRANT}/collections/{COLLECTION}/points",
                         json={"points": batch}).raise_for_status()
            batch = []
        if (i + 1) % 200 == 0:
            log(f"  {i+1}/{len(repos)} repos, {total} vectors, {time.time()-t0:.0f}s")
    if batch:
        requests.put(f"{QDRANT}/collections/{COLLECTION}/points",
                     json={"points": batch}).raise_for_status()
    info = requests.get(f"{QDRANT}/collections/{COLLECTION}").json()["result"]
    log(f"done: {info['points_count']} vectors in '{COLLECTION}' ({time.time()-t0:.0f}s)")
    return total


def query(q, category=None, n=8):
    vec = embed(q)
    body = {"vector": vec, "limit": n, "with_payload": True}
    if category:
        body["filter"] = {"must": [{"key": "category", "match": {"value": category}}]}
    resp = requests.post(f"{QDRANT}/collections/{COLLECTION}/points/search", json=body)
    resp.raise_for_status()
    for hit in resp.json()["result"]:
        p = hit["payload"]
        print(f"\n[{hit['score']:.3f}] {p['name']}  ({p['category']}, {p['language']}) "
              f"★{p['stars']} rev={p['revenue_potential']} reuse={p['reusability_score']}")
        print(f"  {p['url']}")
        print(f"  {(p['purpose'] or '')[:200]}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--query", type=str)
    ap.add_argument("--category", type=str, default=None)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--append", action="store_true", help="don't recreate collection")
    a = ap.parse_args()
    if a.build:
        build(limit=a.limit, recreate=not a.append)
    elif a.query:
        query(a.query, category=a.category)
    else:
        ap.print_help()
