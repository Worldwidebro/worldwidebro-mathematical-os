#!/usr/bin/env python3
"""
build_venture_completion_ledger.py — aggregate the per-repo venture.json completion
tracking that already exists across the ~496 venture-ID-named owned repos into one
ledger file. Doesn't invent a new schema — collects the fields real repos already
have (completion_percent, status, has_code, has_dashboard, has_payments, next_action).

Uses GitHub's GraphQL API with batched aliased queries (dozens of repos per request)
instead of one REST call per repo, since sequential REST content-fetches hit GitHub's
secondary rate limit after ~30 calls.

Output: venture-completion-ledger.json
Usage: python3 build_venture_completion_ledger.py [--limit N] [--batch-size N]
"""
import argparse
import json
import re
import subprocess
import sys
import time

import requests

DOCS = "/Users/acebless/Documents"
REGISTRY = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json"
OUT = f"{DOCS}/venture-completion-ledger.json"
GRAPHQL_URL = "https://api.github.com/graphql"
OWNER = "Worldwidebro"

VENTURE_PATTERN = re.compile(
    r"^(fin|con|ec|tech|edu|spec|emerging|comm|ops|ps|st|lt|em|re|fh|fs)-\d{3}", re.I
)


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def token():
    t = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10).stdout.strip()
    if not t.startswith(("gho_", "ghp_", "github_pat_")):
        raise SystemExit("no valid gh token — run `gh auth login` first")
    return t


def venture_named_repos(limit=0):
    with open(REGISTRY) as f:
        data = json.load(f)
    names = [
        r["name"]
        for r in data["repositories"]
        if r["url"].startswith(f"https://github.com/{OWNER}/") and VENTURE_PATTERN.match(r["name"])
    ]
    return names[:limit] if limit else names


def build_batch_query(repo_names):
    """One GraphQL query, one alias per repo, fetching venture.json OR VENTURE.json."""
    parts = []
    for i, name in enumerate(repo_names):
        safe = f"r{i}"
        parts.append(
            f'{safe}: repository(owner: "{OWNER}", name: "{name}") {{ '
            f'lower: object(expression: "HEAD:venture.json") {{ ... on Blob {{ text }} }} '
            f'upper: object(expression: "HEAD:VENTURE.json") {{ ... on Blob {{ text }} }} '
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="cap number of repos (0 = all)")
    ap.add_argument("--batch-size", type=int, default=40)
    args = ap.parse_args()

    headers = {"Authorization": f"bearer {token()}"}
    names = venture_named_repos(args.limit)
    log(f"Aggregating venture.json across {len(names)} venture-named repos "
        f"in batches of {args.batch_size}...")

    ledger = {}
    no_file = []
    parse_errors = []

    for i in range(0, len(names), args.batch_size):
        batch = names[i : i + args.batch_size]
        log(f"  batch {i // args.batch_size + 1}: repos {i + 1}-{i + len(batch)}")
        result = fetch_batch(batch, headers)
        data = result.get("data") or {}
        for j, name in enumerate(batch):
            alias = data.get(f"r{j}")
            if not alias:
                no_file.append(name)
                continue
            blob = (alias.get("lower") or {}).get("text") or (alias.get("upper") or {}).get("text")
            if not blob:
                no_file.append(name)
                continue
            try:
                ledger[name] = json.loads(blob)
            except json.JSONDecodeError:
                parse_errors.append(name)
        time.sleep(1)  # stay well under GraphQL secondary rate limits

    output = {
        "generated_at": subprocess.run(
            ["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True
        ).stdout.strip(),
        "total_venture_repos": len(names),
        "with_venture_json": len(ledger),
        "no_venture_json": len(no_file),
        "parse_errors": len(parse_errors),
        "ventures": ledger,
        "repos_without_venture_json": no_file,
        "repos_with_parse_errors": parse_errors,
    }

    with open(OUT, "w") as f:
        json.dump(output, f, indent=2)

    log(f"\nDone: {len(ledger)}/{len(names)} repos had a readable venture.json")
    log(f"Written to {OUT}")

    if ledger:
        completions = [v.get("completion_percent") for v in ledger.values() if isinstance(v.get("completion_percent"), (int, float))]
        has_code = sum(1 for v in ledger.values() if v.get("has_code") is True)
        if completions:
            log(f"Avg completion_percent: {sum(completions)/len(completions):.1f}% (n={len(completions)})")
        log(f"has_code=true: {has_code}/{len(ledger)}")


if __name__ == "__main__":
    main()
