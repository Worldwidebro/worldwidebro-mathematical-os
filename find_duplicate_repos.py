#!/usr/bin/env python3
"""
find_duplicate_repos.py — PASS 3: duplicate / consolidation detector.

Uses Qdrant repo embeddings (read-only) to find near-duplicate repos so the portfolio
can be consolidated. Local only, deterministic, ~0 LLM tokens.

Method: scroll all points, for each run a similarity search; pairs cosine >= THRESHOLD
cluster transitively. Per cluster recommend KEEP (highest strategic/revenue/reuse from
registry, else most stars) and ARCHIVE (the rest).

Output: duplicates-report.json
Usage: python3 find_duplicate_repos.py [--threshold 0.9]
"""
import argparse
import json
from datetime import date

import requests

DOCS = "/Users/acebless/Documents"
REGISTRY = (f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/"
            "REFERENCE/REPOSITORY-REGISTRY.json")
OUT = f"{DOCS}/duplicates-report.json"
QDRANT = "http://localhost:6333"
COLLECTION = "repositories"


def load_scores():
    reps = json.load(open(REGISTRY))["repositories"]
    sc = {}
    for r in reps:
        sc[r.get("name", "")] = (
            int(str(r.get("strategic_value", "0") or "0")) +
            int(str(r.get("revenue_potential", "0") or "0")) +
            int(str(r.get("reusability_score", "0") or "0")),
            int(str(r.get("stars", "0") or "0")),
        )
    return sc


def scroll_all():
    pts, nxt = [], None
    while True:
        body = {"limit": 256, "with_vector": True, "with_payload": True}
        if nxt:
            body["offset"] = nxt
        r = requests.post(f"{QDRANT}/collections/{COLLECTION}/points/scroll", json=body, timeout=60)
        r.raise_for_status()
        res = r.json()["result"]
        pts.extend(res["points"])
        nxt = res.get("next_page_offset")
        if not nxt:
            break
    return pts


def search(vec, k=6):
    body = {"vector": vec, "limit": k, "with_payload": True}
    r = requests.post(f"{QDRANT}/collections/{COLLECTION}/points/search", json=body, timeout=30)
    r.raise_for_status()
    return r.json()["result"]


def build(threshold=0.9):
    scores = load_scores()
    pts = scroll_all()
    print(f"scanning {len(pts)} repo vectors for duplicates (cosine >= {threshold})")

    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        parent[find(a)] = find(b)

    sims = {}
    for p in pts:
        name = p["payload"].get("name", "")
        if not name:
            continue
        for h in search(p["vector"], k=6):
            other = h["payload"].get("name", "")
            if other and other != name and h["score"] >= threshold:
                union(name, other)
                sims[tuple(sorted((name, other)))] = h["score"]

    clusters = {}
    for n in list(parent):
        clusters.setdefault(find(n), []).append(n)
    clusters = {k: v for k, v in clusters.items() if len(v) > 1}

    out_clusters = []
    for members in clusters.values():
        keep = max(members, key=lambda m: scores.get(m, (0, 0)))
        archive = [m for m in members if m != keep]
        pair_scores = [s for (a, b), s in sims.items() if a in members and b in members]
        out_clusters.append({
            "keep": keep, "archive": archive, "size": len(members),
            "avg_similarity": round(sum(pair_scores) / len(pair_scores), 3) if pair_scores else None,
        })
    out_clusters.sort(key=lambda c: c["size"], reverse=True)

    meta = {"generated_date": date.today().isoformat(), "threshold": threshold,
            "clusters": len(out_clusters),
            "repos_in_clusters": sum(c["size"] for c in out_clusters)}
    json.dump({"metadata": meta, "clusters": out_clusters}, open(OUT, "w"), indent=2)
    print(f"wrote {OUT}: {meta['clusters']} clusters, {meta['repos_in_clusters']} repos")
    for c in out_clusters[:5]:
        print(f"  keep {c['keep']}  (archive {len(c['archive'])}, sim {c['avg_similarity']})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--threshold", type=float, default=0.9)
    a = ap.parse_args()
    build(threshold=a.threshold)
