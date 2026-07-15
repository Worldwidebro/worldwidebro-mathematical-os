#!/usr/bin/env python3
"""
build_notes_rag.py — RAG over Ace's curated notes.

Embeds scoped markdown notes into a Qdrant `notes` collection using the
already-running local stack:
  - Qdrant  http://localhost:6333   (vector store)
  - Ollama  http://localhost:11434  (nomic-embed-text, 768-dim)

Scope (chosen 2026-06-26): curated knowledge + venture data, repo/vendor noise excluded.

Usage:
  python3 build_notes_rag.py --build              # full ingest (chunk + embed + upsert)
  python3 build_notes_rag.py --build --limit 200  # smoke test on first 200 files
  python3 build_notes_rag.py --query "QUESTION"   # semantic search
  python3 build_notes_rag.py --query "Q" --folder 07-KNOWLEDGE  # filter to a folder
"""
import argparse
import hashlib
import os
import sys
import time

import requests

DOCS = "/Users/acebless/Documents"
QDRANT = "http://localhost:6333"
OLLAMA = "http://localhost:11434/api/embeddings"
EMBED_MODEL = "nomic-embed-text"
COLLECTION = "notes"
DIM = 768

# Scoped roots (relative to DOCS). Each is tagged as its top-level `folder`.
SCOPE = [
    "WORLDWIDEBRO-OS/07-KNOWLEDGE",
    "WORLDWIDEBRO-OS/04-OPERATIONS",
    "WORLDWIDEBRO-OS/02-GOVERNANCE",
    "WORLDWIDEBRO-OS/03-PORTFOLIO",
    "WORLDWIDEBRO-OS/08-DATA",
    "WORLDWIDEBRO-OS/00-DIRECTIVES",
    "WORLDWIDEBRO-OS/05-AGENTS",
    "_career",
]
EXCLUDE = ("/node_modules/", "/.git/", "/.venv/", "/venv/", "/site-packages/")

CHUNK_WORDS = 400
OVERLAP_WORDS = 60


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def collect_files(limit=None):
    out = []
    # loose root-level vault notes
    for name in os.listdir(DOCS):
        p = os.path.join(DOCS, name)
        if os.path.isfile(p) and name.endswith(".md"):
            out.append((p, "ROOT"))
    for root_rel in SCOPE:
        base = os.path.join(DOCS, root_rel)
        if not os.path.isdir(base):
            continue
        folder = os.path.basename(root_rel)
        for dirpath, _, files in os.walk(base):
            if any(x in dirpath + "/" for x in EXCLUDE):
                continue
            for f in files:
                if f.endswith(".md"):
                    out.append((os.path.join(dirpath, f), folder))
    out.sort()
    if limit:
        out = out[:limit]
    return out


def title_of(path, text):
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s[2:].strip()
    return os.path.basename(path)[:-3]


def chunk_words(text):
    words = text.split()
    if len(words) <= CHUNK_WORDS:
        return [text] if words else []
    chunks, i = [], 0
    step = CHUNK_WORDS - OVERLAP_WORDS
    while i < len(words):
        chunks.append(" ".join(words[i:i + CHUNK_WORDS]))
        i += step
    return chunks


def embed(text):
    r = requests.post(OLLAMA, json={"model": EMBED_MODEL, "prompt": text}, timeout=120)
    r.raise_for_status()
    return r.json()["embedding"]


def ensure_collection(recreate=False):
    if recreate:
        requests.delete(f"{QDRANT}/collections/{COLLECTION}")
    exists = requests.get(f"{QDRANT}/collections/{COLLECTION}").status_code == 200
    if not exists:
        requests.put(f"{QDRANT}/collections/{COLLECTION}", json={
            "vectors": {"size": DIM, "distance": "Cosine"}
        }).raise_for_status()


def point_id(path, idx):
    h = hashlib.sha1(f"{path}#{idx}".encode()).hexdigest()
    return int(h[:15], 16)  # stable numeric id


def build(limit=None, recreate=True):
    ensure_collection(recreate=recreate)
    files = collect_files(limit)
    log(f"scope: {len(files)} files -> embedding via {EMBED_MODEL}")
    batch, total, t0 = [], 0, time.time()
    for fi, (path, folder) in enumerate(files):
        try:
            text = open(path, encoding="utf-8", errors="ignore").read()
        except Exception:
            continue
        if not text.strip():
            continue
        title = title_of(path, text)
        rel = os.path.relpath(path, DOCS)
        for ci, ch in enumerate(chunk_words(text)):
            try:
                vec = embed(f"{title}\n\n{ch}")
            except Exception as e:
                log(f"  embed fail {rel}#{ci}: {e}")
                continue
            batch.append({
                "id": point_id(path, ci),
                "vector": vec,
                "payload": {"path": rel, "title": title, "folder": folder,
                            "chunk": ci, "text": ch[:1500]},
            })
            total += 1
            if len(batch) >= 128:
                requests.put(f"{QDRANT}/collections/{COLLECTION}/points",
                             json={"points": batch}).raise_for_status()
                batch = []
        if (fi + 1) % 200 == 0:
            log(f"  {fi+1}/{len(files)} files, {total} vectors, {time.time()-t0:.0f}s")
    if batch:
        requests.put(f"{QDRANT}/collections/{COLLECTION}/points",
                     json={"points": batch}).raise_for_status()
    info = requests.get(f"{QDRANT}/collections/{COLLECTION}").json()["result"]
    log(f"done: {info['points_count']} vectors in '{COLLECTION}' ({time.time()-t0:.0f}s)")
    return total


def query(q, folder=None, n=6):
    vec = embed(q)
    body = {"vector": vec, "limit": n, "with_payload": True}
    if folder:
        body["filter"] = {"must": [{"key": "folder", "match": {"value": folder}}]}
    r = requests.post(f"{QDRANT}/collections/{COLLECTION}/points/search", json=body)
    r.raise_for_status()
    for hit in r.json()["result"]:
        p = hit["payload"]
        print(f"\n[{hit['score']:.3f}] {p['title']}  ({p['folder']})")
        print(f"  {p['path']}")
        snippet = p["text"][:240].replace("\n", " ")
        print(f"  {snippet}...")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--query", type=str)
    ap.add_argument("--folder", type=str, default=None)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--append", action="store_true", help="don't recreate collection")
    a = ap.parse_args()
    if a.build:
        build(limit=a.limit, recreate=not a.append)
    elif a.query:
        query(a.query, folder=a.folder)
    else:
        ap.print_help()
