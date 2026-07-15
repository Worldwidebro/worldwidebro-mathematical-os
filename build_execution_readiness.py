#!/usr/bin/env python3
"""
build_execution_readiness.py — Stage 12: deployability flags for high-value repos.

For each high_value repo, query the GitHub API (read-only, via `gh auth token`) to
determine what's actually deployable this week. Local + GitHub API only, no LLM.

Output: execution-readiness.csv
Usage: python3 build_execution_readiness.py [--limit N]
"""
import argparse
import csv
import json
import re
import subprocess
import sys
import time

import requests

DOCS = "/Users/acebless/Documents"
SUMMARIES = f"{DOCS}/repo-summaries.json"
OUT = f"{DOCS}/execution-readiness.csv"
API = "https://api.github.com"

MANIFESTS = ["package.json", "pyproject.toml", "go.mod", "Cargo.toml", "requirements.txt", "pom.xml"]
DOCKER = ["Dockerfile", "docker-compose.yml", "compose.yaml", "docker-compose.yaml"]


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def token():
    try:
        t = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10).stdout.strip()
        if t.startswith(("gho_", "ghp_", "github_pat_")):
            return t
    except Exception:
        pass
    return None


def owner_repo(url):
    m = re.search(r"github\.com/(?:repos/)?([^/]+)/([^/]+)", url or "")
    return (m.group(1), m.group(2).replace(".git", "")) if m else (None, None)


def build(limit=None):
    tok = token()
    if not tok:
        log("ERROR: no usable gh token"); return
    h = {"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json"}
    repos = [r for r in json.load(open(SUMMARIES))["summaries"].values() if r["high_value"]]
    if limit:
        repos = repos[:limit]
    log(f"checking execution readiness for {len(repos)} high-value repos")

    rows, t0 = [], time.time()
    prod = mcp = arch = 0
    for i, r in enumerate(repos):
        owner, repo = owner_repo(r["url"])
        if not owner:
            continue
        try:
            meta = requests.get(f"{API}/repos/{owner}/{repo}", headers=h, timeout=30)
            if meta.status_code != 200:
                continue
            md = meta.json()
            # list root contents once
            root = requests.get(f"{API}/repos/{owner}/{repo}/contents", headers=h, timeout=30)
            files = [f["name"] for f in root.json()] if root.status_code == 200 and isinstance(root.json(), list) else []
        except Exception as e:
            log(f"  fail {r['name']}: {e}"); continue
        dockerized = any(f in files for f in DOCKER)
        has_manifest = any(f in files for f in MANIFESTS)
        topics = " ".join(md.get("topics", [])) + " " + (md.get("description") or "")
        mcp_compat = "mcp" in topics.lower() or "mcp" in r["name"].lower()
        has_license = md.get("license") is not None
        archived = md.get("archived", False)
        production_ready = dockerized and has_manifest and not archived
        prod += production_ready; mcp += mcp_compat; arch += archived
        rows.append({"repo_name": r["name"], "owner": owner, "dockerized": dockerized,
                     "has_package_manifest": has_manifest, "mcp_compatible": mcp_compat,
                     "has_license": has_license, "archived": archived,
                     "last_push": md.get("pushed_at", ""), "production_ready": production_ready})
        if (i + 1) % 50 == 0:
            log(f"  {i+1}/{len(repos)}, {time.time()-t0:.0f}s")

    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["repo_name", "owner", "dockerized", "has_package_manifest",
                                          "mcp_compatible", "has_license", "archived",
                                          "last_push", "production_ready"])
        w.writeheader(); w.writerows(rows)
    log(f"wrote {OUT}: {len(rows)} repos | production_ready={prod} mcp_compatible={mcp} archived={arch}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    a = ap.parse_args()
    build(limit=a.limit)
