#!/usr/bin/env python3
"""
scan_all_repos_for_sites.py — check ALL owned repos (not just venture-named ones) for
real site/app signals: index.html, vercel.json, or a package.json with a frontend
framework. Answers "which repos have sites in them we aren't aware of."

Same GraphQL-batching approach as build_venture_completion_ledger.py.

Output: repos-with-sites.json
Usage: python3 scan_all_repos_for_sites.py [--limit N] [--batch-size N]
"""
import argparse
import json
import subprocess
import sys
import time

import requests

DOCS = "/Users/acebless/Documents"
REGISTRY = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json"
OUT = f"{DOCS}/repos-with-sites.json"
GRAPHQL_URL = "https://api.github.com/graphql"
OWNER = "Worldwidebro"


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def token():
    t = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10).stdout.strip()
    if not t.startswith(("gho_", "ghp_", "github_pat_")):
        raise SystemExit("no valid gh token — run `gh auth login` first")
    return t


def owned_repos(limit=0):
    with open(REGISTRY) as f:
        data = json.load(f)
    names = [r["name"] for r in data["repositories"] if r["url"].startswith(f"https://github.com/{OWNER}/")]
    return names[:limit] if limit else names


def build_batch_query(repo_names):
    parts = []
    for i, name in enumerate(repo_names):
        safe = f"r{i}"
        parts.append(
            f'{safe}: repository(owner: "{OWNER}", name: "{name}") {{ '
            f'index: object(expression: "HEAD:index.html") {{ ... on Blob {{ byteSize }} }} '
            f'vercel: object(expression: "HEAD:vercel.json") {{ ... on Blob {{ byteSize }} }} '
            f'pkg: object(expression: "HEAD:package.json") {{ ... on Blob {{ text }} }} '
            f"}}"
        )
    return "query {\n" + "\n".join(parts) + "\n}"


def fetch_batch(repo_names, headers, retries=3):
    query = build_batch_query(repo_names)
    for attempt in range(retries):
        resp = requests.post(GRAPHQL_URL, headers=headers, json={"query": query}, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code in (403, 502, 503):
            wait = 5 * (attempt + 1)
            log(f"  retry in {wait}s (HTTP {resp.status_code})")
            time.sleep(wait)
            continue
        resp.raise_for_status()
    raise RuntimeError(f"failed after {retries} retries")


FRONTEND_MARKERS = ["next", "vite", "react", "vue", "svelte", "astro", "@remix-run"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--batch-size", type=int, default=40)
    args = ap.parse_args()

    headers = {"Authorization": f"bearer {token()}"}
    names = owned_repos(args.limit)
    log(f"Scanning {len(names)} owned repos for site signals in batches of {args.batch_size}...")

    sites = {}
    for i in range(0, len(names), args.batch_size):
        batch = names[i : i + args.batch_size]
        log(f"  batch {i // args.batch_size + 1}: repos {i + 1}-{i + len(batch)}")
        result = fetch_batch(batch, headers)
        data = result.get("data") or {}
        for j, name in enumerate(batch):
            alias = data.get(f"r{j}") or {}
            has_index = bool(alias.get("index"))
            has_vercel = bool(alias.get("vercel"))
            pkg_text = (alias.get("pkg") or {}).get("text") or ""
            frontend_framework = next((m for m in FRONTEND_MARKERS if m in pkg_text.lower()), None)
            if has_index or has_vercel or frontend_framework:
                sites[name] = {
                    "has_index_html": has_index,
                    "has_vercel_json": has_vercel,
                    "frontend_framework": frontend_framework,
                }
        time.sleep(1)

    output = {
        "generated_at": subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True).stdout.strip(),
        "total_owned_repos": len(names),
        "repos_with_site_signals": len(sites),
        "sites": sites,
    }
    with open(OUT, "w") as f:
        json.dump(output, f, indent=2)

    log(f"\nDone: {len(sites)}/{len(names)} repos have a site signal")
    log(f"Written to {OUT}")


if __name__ == "__main__":
    main()
