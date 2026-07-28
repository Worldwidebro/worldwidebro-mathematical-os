#!/usr/bin/env python3
"""Import ventures.csv into Twenty CRM as Company records.

Twenty already has a partial import (371/713 companies) with these Company
fields pre-built: ventureId (TEXT, short prefix e.g. "EC-077"), sector
(SELECT, UPPER_SNAKE_CASE), opco (TEXT), ventureStage (SELECT), ventureStatus
(SELECT). This script creates the 342 missing companies and backfills opco /
ventureStage on existing ones where those are blank.

Requires TWENTY_API_KEY in /Users/acebless/.env.
Usage: python3 populate_twenty_ventures.py [--dry-run]
"""
import csv
import os
import re
import sys
import time
import requests

ENV_PATH = "/Users/acebless/.env"
CSV_PATH = "/Users/acebless/Documents/Gemini/business-os/ventures.csv"
BASE_URL = "http://localhost:3002"
GRAPHQL_URL = f"{BASE_URL}/graphql"
METADATA_URL = f"{BASE_URL}/metadata"
REQUIRED_FIELDS = ["ventureId", "sector", "opco", "ventureStage", "ventureStatus", "name"]

DRY_RUN = "--dry-run" in sys.argv

STAGE_MAP = {
    "planned": "PLANNED", "validation": "VALIDATION",
    "mvp": "MVP", "growth": "GROWTH",
}
STATUS_MAP = {
    "planned": "PLANNED", "development": "DEVELOPMENT",
    "validation": "VALIDATION", "active": "ACTIVE",
}
SHORT_ID_RE = re.compile(r"^([A-Z]+-\d+)")


def load_env():
    if not os.path.exists(ENV_PATH):
        return {}
    env = {}
    with open(ENV_PATH) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def gql(session, url, query, variables=None, max_retries=8):
    for attempt in range(max_retries):
        resp = session.post(url, json={"query": query, "variables": variables or {}}, timeout=30)
        data = resp.json()
        if "errors" not in data:
            return data["data"]
        errors = data["errors"]
        if any(e.get("extensions", {}).get("subCode") == "LIMIT_REACHED" for e in errors):
            wait = min(2 ** attempt, 30)
            time.sleep(wait)
            continue
        raise RuntimeError(f"GraphQL error: {errors}")
    raise RuntimeError(f"GraphQL error: rate limit retries exhausted for query")


def get_company_fields(session):
    query = """
    query {
      objects(paging: { first: 200 }) {
        edges {
          node {
            id
            nameSingular
            fields(paging: { first: 200 }) { edges { node { id name type } } }
          }
        }
      }
    }
    """
    data = gql(session, METADATA_URL, query)
    company_edges = [e for e in data["objects"]["edges"] if e["node"]["nameSingular"] == "company"]
    if not company_edges:
        raise RuntimeError("Company object not found in Twenty metadata")
    node = company_edges[0]["node"]
    fields = {e["node"]["name"] for e in node["fields"]["edges"]}
    return fields


def short_id(full_venture_id):
    m = SHORT_ID_RE.match(full_venture_id)
    return m.group(1) if m else full_venture_id


def sector_enum(sector):
    return sector.upper().replace("-", "_")


def load_ventures():
    with open(CSV_PATH, newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["short_id"] = short_id(r["venture_id"])
    return rows


def get_existing_companies(session):
    """Twenty has a mix of two ventureId conventions from earlier partial
    imports: short prefix ("EC-077") and full slug ("BW-001-Lash-..."),
    matching the CSV's short_id or venture_id respectively. Keyed by
    whichever raw string Twenty stored, so callers must check both."""
    query = """
    query GetCompanies($after: String) {
      companies(first: 200, after: $after) {
        edges { node { id ventureId opco ventureStage ventureStatus } }
        pageInfo { hasNextPage endCursor }
      }
    }
    """
    existing = {}
    after = None
    while True:
        data = gql(session, GRAPHQL_URL, query, {"after": after})
        conn = data["companies"]
        for edge in conn["edges"]:
            n = edge["node"]
            if n.get("ventureId"):
                existing[n["ventureId"]] = n
        if not conn["pageInfo"]["hasNextPage"]:
            break
        after = conn["pageInfo"]["endCursor"]
    return existing


def create_company(session, venture):
    mutation = """
    mutation CreateCompany($input: CompanyCreateInput!) {
      createCompany(data: $input) { id name }
    }
    """
    variables = {
        "input": {
            "name": venture["name"],
            "ventureId": venture["venture_id"],
            "sector": sector_enum(venture["sector"]),
            "opco": venture["opco"],
            "ventureStage": STAGE_MAP.get(venture["stage"]),
            "ventureStatus": STATUS_MAP.get(venture["status"]),
        }
    }
    gql(session, GRAPHQL_URL, mutation, variables)


def backfill_company(session, company_id, venture):
    patch = {}
    if not venture["opco"]:
        pass
    else:
        patch["opco"] = venture["opco"]
    if venture["stage"] in STAGE_MAP:
        patch["ventureStage"] = STAGE_MAP[venture["stage"]]
    if not patch:
        return False
    mutation = """
    mutation UpdateCompany($id: ID!, $input: CompanyUpdateInput!) {
      updateCompany(id: $id, data: $input) { id }
    }
    """
    gql(session, GRAPHQL_URL, mutation, {"id": company_id, "input": patch})
    return True


def main():
    env = load_env()
    api_key = env.get("TWENTY_API_KEY") or os.environ.get("TWENTY_API_KEY")
    if not api_key:
        print("ERROR: TWENTY_API_KEY not found in /Users/acebless/.env or environment.")
        sys.exit(1)

    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})

    print("1. Verifying Company schema...")
    fields = get_company_fields(session)
    missing = [f for f in REQUIRED_FIELDS if f not in fields]
    if missing:
        raise RuntimeError(f"Company object is missing required fields: {missing}. Not created automatically.")
    print(f"   All required fields present: {REQUIRED_FIELDS}")

    print("2. Loading ventures.csv...")
    ventures = load_ventures()
    print(f"   {len(ventures)} ventures loaded")

    print("3. Fetching existing companies...")
    existing = get_existing_companies(session)
    print(f"   {len(existing)} companies already in Twenty")

    print("4. Creating missing + backfilling incomplete companies...")
    created, backfilled, skipped, failed = 0, 0, 0, 0
    for v in ventures:
        full_id, sid = v["venture_id"], v["short_id"]
        comp = existing.get(full_id) or existing.get(sid)
        if comp:
            needs_backfill = (not comp.get("opco") and v["opco"]) or (not comp.get("ventureStage") and v["stage"] in STAGE_MAP)
            if not needs_backfill:
                skipped += 1
                continue
            if DRY_RUN:
                print(f"   [dry-run] would backfill {full_id}")
                backfilled += 1
                continue
            try:
                if backfill_company(session, comp["id"], v):
                    backfilled += 1
                    time.sleep(0.5)
                    if backfilled % 25 == 0:
                        print(f"   ...{backfilled} backfilled")
            except Exception as e:
                failed += 1
                print(f"   BACKFILL FAILED {full_id}: {e}")
            continue

        if DRY_RUN:
            print(f"   [dry-run] would create {full_id} ({v['name']})")
            created += 1
            continue
        try:
            create_company(session, v)
            created += 1
            time.sleep(0.5)
            if created % 25 == 0:
                print(f"   ...{created} created")
        except Exception as e:
            failed += 1
            print(f"   CREATE FAILED {full_id}: {e}")

    print(f"\nDone. created={created} backfilled={backfilled} skipped={skipped} failed={failed}")


if __name__ == "__main__":
    main()
