#!/usr/bin/env python3
"""
build_funding_ledger.py — aggregate GRANTS.md, FUNDING.md, and TAX.md across venture repos
into one consolidated, easy-to-scan report. Answers "can we easily see the grants/credit/
loans/funding of each business" without opening 50 separate repos.

Same GraphQL-batching approach as build_venture_completion_ledger.py.

Output: funding-ledger.json
Usage: python3 build_funding_ledger.py --prefix comm- [--limit N] [--batch-size N]
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
OUT = f"{DOCS}/funding-ledger.json"
GRAPHQL_URL = "https://api.github.com/graphql"
OWNER = "Worldwidebro"


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def token():
    t = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10).stdout.strip()
    if not t.startswith(("gho_", "ghp_", "github_pat_")):
        raise SystemExit("no valid gh token — run `gh auth login` first")
    return t


def matching_repos(prefix, limit=0):
    with open(REGISTRY) as f:
        data = json.load(f)
    names = [
        r["name"] for r in data["repositories"]
        if r["url"].startswith(f"https://github.com/{OWNER}/") and r["name"].lower().startswith(prefix.lower())
    ]
    return names[:limit] if limit else names


def build_batch_query(repo_names):
    parts = []
    for i, name in enumerate(repo_names):
        safe = f"r{i}"
        parts.append(
            f'{safe}: repository(owner: "{OWNER}", name: "{name}") {{ '
            f'grants: object(expression: "HEAD:GRANTS.md") {{ ... on Blob {{ text }} }} '
            f'funding: object(expression: "HEAD:FUNDING.md") {{ ... on Blob {{ text }} }} '
            f'tax: object(expression: "HEAD:TAX.md") {{ ... on Blob {{ text }} }} '
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


def extract_matched_programs(grants_text):
    """Pull the 'Matched Grant & Loan Programs' table rows out of a GRANTS.md."""
    if not grants_text:
        return []
    rows = re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(\$[\d,]+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$",
                       grants_text, re.MULTILINE)
    return [
        {"program": r[0], "agency": r[1], "max_amount": r[2], "type": r[3], "status": r[4]}
        for r in rows if r[0].lower() != "program"
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prefix", default="", help="only repos starting with this prefix, e.g. comm-")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--batch-size", type=int, default=40)
    args = ap.parse_args()

    headers = {"Authorization": f"bearer {token()}"}
    names = matching_repos(args.prefix, args.limit)
    log(f"Aggregating funding docs across {len(names)} repos (prefix='{args.prefix}') in batches of {args.batch_size}...")

    ledger = {}
    for i in range(0, len(names), args.batch_size):
        batch = names[i : i + args.batch_size]
        log(f"  batch {i // args.batch_size + 1}: repos {i + 1}-{i + len(batch)}")
        result = fetch_batch(batch, headers)
        data = result.get("data") or {}
        for j, name in enumerate(batch):
            alias = data.get(f"r{j}") or {}
            grants_text = (alias.get("grants") or {}).get("text")
            funding_text = (alias.get("funding") or {}).get("text")
            tax_text = (alias.get("tax") or {}).get("text")
            if not (grants_text or funding_text or tax_text):
                continue
            ledger[name] = {
                "matched_grant_programs": extract_matched_programs(grants_text),
                "has_grants_doc": bool(grants_text),
                "has_funding_doc": bool(funding_text),
                "has_tax_doc": bool(tax_text),
            }
        time.sleep(1)

    output = {
        "generated_at": subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True).stdout.strip(),
        "prefix": args.prefix,
        "total_repos_checked": len(names),
        "repos_with_funding_docs": len(ledger),
        "ventures": ledger,
    }
    with open(OUT, "w") as f:
        json.dump(output, f, indent=2)

    log(f"\nDone: {len(ledger)}/{len(names)} repos had funding docs")
    log(f"Written to {OUT}")

    # quick signal: how many have IDENTICAL matched-program sets (= templated, not researched)
    from collections import Counter
    sigs = Counter(
        tuple(sorted(p["program"] for p in v["matched_grant_programs"]))
        for v in ledger.values() if v["matched_grant_programs"]
    )
    if sigs:
        top_sig, top_count = sigs.most_common(1)[0]
        log(f"Most common grant-program set appears in {top_count}/{len(ledger)} ventures: {top_sig}")
        if top_count > len(ledger) * 0.5:
            log("WARNING: majority share the identical program set — likely templated, not per-venture research")


if __name__ == "__main__":
    main()
