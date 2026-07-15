#!/usr/bin/env python3
"""Backfill Company.domainName in Twenty CRM from live Vercel project URLs.

Fetches all Vercel projects via `vercel project ls --format=json` (paginated),
matches each project name to a venture_id in ventures.csv (by full id or
short prefix, same convention as populate_twenty_ventures.py), then finds
the matching Company in Twenty by ventureId and sets its domainName link.

Requires TWENTY_API_KEY in /Users/acebless/.env and an authenticated `vercel` CLI.
Usage: python3 sync_vercel_domains_to_twenty.py [--dry-run]
"""
import csv
import json
import os
import re
import subprocess
import sys
import time
import requests

ENV_PATH = "/Users/acebless/.env"
CSV_PATH = "/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv"
GRAPHQL_URL = "http://localhost:3002/graphql"
SHORT_ID_RE = re.compile(r"^([A-Za-z]+-\d+)", re.I)

DRY_RUN = "--dry-run" in sys.argv


def load_env():
    env = {}
    with open(ENV_PATH) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def gql(session, query, variables=None, max_retries=8):
    for attempt in range(max_retries):
        resp = session.post(GRAPHQL_URL, json={"query": query, "variables": variables or {}}, timeout=30)
        data = resp.json()
        if "errors" not in data:
            return data["data"]
        if any(e.get("extensions", {}).get("subCode") == "LIMIT_REACHED" for e in data["errors"]):
            time.sleep(min(2 ** attempt, 30))
            continue
        raise RuntimeError(f"GraphQL error: {data['errors']}")
    raise RuntimeError("GraphQL error: rate limit retries exhausted")


def fetch_all_vercel_projects():
    all_projects, next_ts = [], None
    while True:
        cmd = ["vercel", "project", "ls", "--format=json"]
        if next_ts:
            cmd += ["--next", str(next_ts)]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        data = json.loads(result.stdout)
        projs = data.get("projects", [])
        all_projects.extend(projs)
        next_ts = data.get("pagination", {}).get("next")
        if not next_ts or not projs:
            break
    return all_projects


def load_venture_index():
    by_full, by_short = {}, {}
    with open(CSV_PATH, newline="") as f:
        for row in csv.DictReader(f):
            vid = row["venture_id"]
            by_full[vid.lower()] = vid
            m = SHORT_ID_RE.match(vid)
            if m:
                by_short.setdefault(m.group(1).lower(), vid)
    return by_full, by_short


def get_existing_companies(session):
    query = """
    query GetCompanies($after: String) {
      companies(first: 200, after: $after) {
        edges { node { id ventureId domainName { primaryLinkUrl } } }
        pageInfo { hasNextPage endCursor }
      }
    }
    """
    existing = {}
    after = None
    while True:
        data = gql(session, query, {"after": after})
        conn = data["companies"]
        for edge in conn["edges"]:
            n = edge["node"]
            if n.get("ventureId"):
                existing[n["ventureId"]] = n
        if not conn["pageInfo"]["hasNextPage"]:
            break
        after = conn["pageInfo"]["endCursor"]
    return existing


def set_domain(session, company_id, url):
    mutation = """
    mutation UpdateCompany($id: ID!, $input: CompanyUpdateInput!) {
      updateCompany(id: $id, data: $input) { id }
    }
    """
    variables = {"id": company_id, "input": {"domainName": {"primaryLinkUrl": url, "primaryLinkLabel": ""}}}
    gql(session, mutation, variables)


def main():
    env = load_env()
    api_key = env.get("TWENTY_API_KEY")
    if not api_key:
        print("ERROR: TWENTY_API_KEY not found in /Users/acebless/.env")
        sys.exit(1)

    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})

    print("1. Fetching Vercel projects...")
    projects = fetch_all_vercel_projects()
    print(f"   {len(projects)} Vercel projects found")

    print("2. Matching Vercel project names to venture_ids...")
    by_full, by_short = load_venture_index()
    matched = []
    for p in projects:
        name = p["name"]
        url = p.get("latestProductionUrl")
        if not url:
            continue
        m = SHORT_ID_RE.match(name)
        vid = by_full.get(name.lower())
        if not vid and m:
            vid = by_short.get(m.group(1).lower())
        if vid:
            matched.append((vid, url))
    print(f"   {len(matched)} projects matched to ventures")

    print("3. Fetching existing Twenty companies...")
    existing = get_existing_companies(session)
    print(f"   {len(existing)} companies in Twenty")

    print("4. Setting domainName on matched companies...")
    updated, skipped, unmatched_company, failed = 0, 0, 0, 0
    for vid, url in matched:
        short_key = SHORT_ID_RE.match(vid)
        comp = existing.get(vid) or (existing.get(short_key.group(1)) if short_key else None)
        if not comp:
            unmatched_company += 1
            print(f"   NO COMPANY FOUND for {vid}")
            continue
        current = (comp.get("domainName") or {}).get("primaryLinkUrl")
        if current == url:
            skipped += 1
            continue
        if DRY_RUN:
            print(f"   [dry-run] would set {vid} -> {url}")
            updated += 1
            continue
        try:
            set_domain(session, comp["id"], url)
            updated += 1
            time.sleep(0.5)
            if updated % 25 == 0:
                print(f"   ...{updated} updated")
        except Exception as e:
            failed += 1
            print(f"   FAILED {vid}: {e}")

    print(f"\nDone. updated={updated} skipped={skipped} no_company_match={unmatched_company} failed={failed}")


if __name__ == "__main__":
    main()
