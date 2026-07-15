#!/usr/bin/env python3
"""
build_readme_corpus.py — Task #3 (Stage 4): README corpus for high-value repos.

Fetches READMEs for the high_value repos (358) via the GitHub API, extracts a
compact readme_summary + keywords, writes readmes.json, and RE-EMBEDS those repos
into the existing Qdrant `repositories` collection with README content included so
semantic search hits architecture/usage, not just metadata.

Reuses the existing local stack (no new vector DB):
  - Ollama nomic-embed (768-dim)   - Qdrant :6333 `repositories`
GitHub token read from /Users/acebless/.env (GITHUB_TOKEN) — never printed.

Usage:
  python3 build_readme_corpus.py                # all high-value repos
  python3 build_readme_corpus.py --limit 10     # smoke test
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from datetime import date

import requests

DOCS = "/Users/acebless/Documents"
SUMMARIES = f"{DOCS}/repo-summaries.json"
ENV = "/Users/acebless/.env"
OUT = f"{DOCS}/readmes.json"
OLLAMA = "http://localhost:11434/api/embeddings"
QDRANT = "http://localhost:6333"
COLLECTION = "repositories"
EMBED_MODEL = "nomic-embed-text"


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def gh_token():
    # Prefer the authenticated gh CLI token (valid gho_ with repo scope);
    # fall back to .env GITHUB_TOKEN if gh is unavailable.
    try:
        t = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10).stdout.strip()
        if t.startswith(("gho_", "ghp_", "github_pat_")):
            return t
    except Exception:
        pass
    for line in open(ENV):
        if line.startswith("GITHUB_TOKEN="):
            v = line.split("=", 1)[1].strip().strip('"')
            if v.startswith(("gho_", "ghp_", "github_pat_")):
                return v
    return None


def owner_repo(url):
    m = re.search(r"github\.com/(?:repos/)?([^/]+)/([^/]+)", url or "")
    if not m:
        return None, None
    return m.group(1), m.group(2).replace(".git", "")


def fetch_readme(owner, repo, token):
    h = {"Accept": "application/vnd.github.raw+json", "Authorization": f"Bearer {token}"}
    r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/readme", headers=h, timeout=30)
    if r.status_code == 200:
        return r.text
    return None


def summarize_readme(text):
    # strip code fences/badges/html, keep first ~1500 chars of prose
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)        # images/badges
    text = re.sub(r"<[^>]+>", "", text)                 # html
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    summary = text[:1500]
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9\-]{3,}", text.lower())
    stop = {"this", "that", "with", "from", "your", "have", "will", "https", "http", "github"}
    freq = {}
    for w in words:
        if w not in stop:
            freq[w] = freq.get(w, 0) + 1
    keywords = [w for w, _ in sorted(freq.items(), key=lambda x: -x[1])[:15]]
    return summary, keywords


def embed(text):
    r = requests.post(OLLAMA, json={"model": EMBED_MODEL, "prompt": text}, timeout=120)
    r.raise_for_status()
    return r.json()["embedding"]


def point_id(name, url):
    return int(hashlib.sha1(f"{name}|{url}".encode()).hexdigest()[:15], 16)


def build(limit=None):
    token = gh_token()
    if not token:
        log("ERROR: no GITHUB_TOKEN in .env")
        return
    summaries = json.load(open(SUMMARIES))["summaries"]
    targets = [r for r in summaries.values() if r["high_value"]]
    if limit:
        targets = targets[:limit]
    log(f"fetching READMEs for {len(targets)} high-value repos")

    corpus, batch, ok, t0 = {}, [], 0, time.time()
    for i, r in enumerate(targets):
        owner, repo = owner_repo(r["url"])
        if not owner:
            continue
        try:
            readme = fetch_readme(owner, repo, token)
        except Exception as e:
            log(f"  fetch fail {r['name']}: {e}")
            continue
        if not readme:
            continue
        summ, keywords = summarize_readme(readme)
        corpus[r["name"]] = {"readme_summary": summ, "keywords": keywords,
                             "fetched_date": date.today().isoformat()}
        ok += 1
        # re-embed with README content for richer semantic search
        try:
            vec = embed(f"{r['name']}\n{r['purpose']}\nREADME: {summ}")
            batch.append({"id": point_id(r["name"], r["url"]), "vector": vec,
                          "payload": {"name": r["name"], "url": r["url"],
                                      "category": r["category"], "purpose": r["purpose"][:500],
                                      "readme_summary": summ[:800], "keywords": keywords,
                                      "high_value": True}})
        except Exception as e:
            log(f"  embed fail {r['name']}: {e}")
        if len(batch) >= 64:
            requests.put(f"{QDRANT}/collections/{COLLECTION}/points", json={"points": batch}).raise_for_status()
            batch = []
        if (i + 1) % 50 == 0:
            log(f"  {i+1}/{len(targets)} done, {ok} READMEs, {time.time()-t0:.0f}s")
    if batch:
        requests.put(f"{QDRANT}/collections/{COLLECTION}/points", json={"points": batch}).raise_for_status()

    meta = {"generated_date": date.today().isoformat(), "fetched": ok, "attempted": len(targets)}
    json.dump({"metadata": meta, "readmes": corpus}, open(OUT, "w"), indent=2)
    log(f"done: {ok}/{len(targets)} READMEs -> {OUT}, re-embedded into Qdrant ({time.time()-t0:.0f}s)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    a = ap.parse_args()
    build(limit=a.limit)
