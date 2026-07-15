#!/usr/bin/env python3
"""
retrieve.py — Task #5: the context-engineering retrieval layer.

Turns a business question into a SMALL, relevant context bundle so the model never
sees all 1,597 repos. Fully local (Qdrant + Neo4j + Ollama embed).

Flow:
  question
    -> embed (Ollama nomic-embed)
    -> Qdrant semantic search        -> top-K repos by meaning
    -> Neo4j enrich each repo         -> canonical capabilities (IMPLEMENTS)
    -> Neo4j venture match            -> matching venture(s) -> OPCO -> Holding chain
    -> assemble compact context (~repos x summary + venture/OPCO), capped

Usage:
  python3 retrieve.py "which existing repos support launching a recruiting business?"
  python3 retrieve.py "construction field service scheduling" --k 12
  python3 retrieve.py "..." --json     # machine-readable bundle
"""
import argparse
import json
import re
import sys

import requests
from neo4j import GraphDatabase

from os_env import OLLAMA_EMBED as OLLAMA, OLLAMA_CHAT, EMBED_MODEL, CHAT_MODEL, QDRANT, NEO4J_URI, NEO4J_AUTH

DOCS = "/Users/acebless/Documents"
SUMMARIES = f"{DOCS}/repo-summaries.json"
COLLECTION = "repositories"

STOP = set("which existing repos repo repositories support launching launch a an the for to of and "
           "business that could would help me building build with using our service services "
           "scheduling field job jobs platform agency company app system tool tools software "
           "want need start run manage automate".split())


def embed(text):
    r = requests.post(OLLAMA, json={"model": EMBED_MODEL, "prompt": text}, timeout=120)
    r.raise_for_status()
    return r.json()["embedding"]


def qdrant_search(vec, k):
    body = {"vector": vec, "limit": k, "with_payload": True}
    r = requests.post(f"{QDRANT}/collections/{COLLECTION}/points/search", json=body, timeout=30)
    r.raise_for_status()
    return r.json()["result"]


def repo_caps(session, names):
    rows = session.run(
        "MATCH (r:Repo)-[:IMPLEMENTS]->(c:Capability) WHERE r.name IN $names "
        "RETURN r.name AS name, collect(c.name) AS caps", names=names)
    return {row["name"]: row["caps"] for row in rows}


def match_ventures(session, query, limit=3):
    tokens = [t for t in re.findall(r"[a-zA-Z]+", query.lower()) if t not in STOP and len(t) > 3]
    if not tokens:
        return []
    # rank ventures by how many query tokens they match (most specific first)
    rows = session.run("""
        MATCH (v:Venture)-[:BELONGS_TO]->(o:OPCO)-[:BELONGS_TO]->(:Entity)-[:BELONGS_TO]->(h:Entity)
        WITH v, o, h, size([t IN $toks WHERE toLower(v.name) CONTAINS t OR toLower(v.sector) CONTAINS t]) AS hits
        WHERE hits > 0
        RETURN v.id AS id, v.name AS name, v.sector AS sector, o.id AS opco, h.name AS holding, hits
        ORDER BY hits DESC, v.name LIMIT $lim
    """, toks=tokens, lim=limit)
    return [dict(r) for r in rows]


def retrieve(query, k=12):
    summaries = json.load(open(SUMMARIES))["summaries"]
    vec = embed(query)
    hits = qdrant_search(vec, k)
    names = [h["payload"]["name"] for h in hits]

    d = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
    with d.session() as s:
        caps = repo_caps(s, names)
        ventures = match_ventures(s, query)
    d.close()

    repos = []
    for h in hits:
        p = h["payload"]
        name = p["name"]
        sm = summaries.get(name, {})
        repos.append({
            "name": name,
            "score": round(h["score"], 3),
            "category": p.get("category", ""),
            "capabilities": caps.get(name, []),
            "summary": sm.get("summary_text", p.get("purpose", "")),
            "url": p.get("url", ""),
        })
    return {"query": query, "repos": repos, "ventures": ventures}


def synthesize_answer(bundle, model=CHAT_MODEL):
    """Free local synthesis tier: answer the question from the retrieved
    context using Ollama. Cost-aware pipeline pattern — local model first,
    escalate to Claude only if this returns nothing useful (empty bundle)."""
    if not bundle["repos"] and not bundle["ventures"]:
        return None
    context = render(bundle)
    r = requests.post(OLLAMA_CHAT, json={
        "model": model,
        "messages": [
            {"role": "system", "content": "Answer the business question using only "
             "the retrieved context below. Be concise. If the context doesn't "
             "answer it, say so plainly instead of guessing."},
            {"role": "user", "content": f"{context}\n\nQuestion: {bundle['query']}"},
        ],
        "stream": False,
    }, timeout=120)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


def render(bundle):
    out = [f"# Retrieval context for: {bundle['query']}\n"]
    if bundle["ventures"]:
        out.append("## Matching venture(s) and ownership chain")
        for v in bundle["ventures"]:
            out.append(f"- {v['name']} ({v['id']}, sector={v['sector']}) "
                       f"-> OPCO {v['opco']} -> {v['holding']}")
        out.append("")
    out.append(f"## Top {len(bundle['repos'])} relevant repos (of 1,597)")
    for r in bundle["repos"]:
        caps = ", ".join(r["capabilities"]) if r["capabilities"] else "—"
        out.append(f"- [{r['score']}] {r['name']} ({r['category']}) caps: {caps}\n    {r['summary']}")
    return "\n".join(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="+")
    ap.add_argument("--k", type=int, default=12)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--answer", action="store_true",
                     help="synthesize a plain-English answer locally via Ollama (free)")
    ap.add_argument("--model", default=CHAT_MODEL, help="Ollama chat model for --answer")
    a = ap.parse_args()
    bundle = retrieve(" ".join(a.query), k=a.k)
    if a.json:
        print(json.dumps(bundle, indent=2))
    else:
        text = render(bundle)
        print(text)
        print(f"\n[context size: ~{len(text)//4} tokens vs ~{1597*43} tokens for full registry]",
              file=sys.stderr)
    if a.answer:
        answer = synthesize_answer(bundle, model=a.model)
        print(f"\n## Answer ({a.model}, local/free)\n{answer or '(no context to answer from)'}")
