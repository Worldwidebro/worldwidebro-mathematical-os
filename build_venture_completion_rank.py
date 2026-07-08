#!/usr/bin/env python3
"""
build_venture_completion_rank.py — normalize venture-completion-ledger.json's two known
schemas (schema A: completion_percent/has_code; schema B: development_stage) into one
ordered ranking. Doesn't invent new completion math — flags schema A's boilerplate
cluster (19/20 CON-* repos share identical copy-pasted venture.json content) instead of
trusting it, and maps schema B's development_stage to an approximate band since it has
no numeric field.

Cross-checked against venture-hub-pi.vercel.app/api/ventures (2026-07-05): that live
dashboard's progress_pct/hasCode are uniform placeholder values (~10-11%, hasCode=false
for everyone sampled) — not usable as a ranking signal, so this ledger is the better
source despite its own schema-A boilerplate problem.

Output: venture-completion-ranked.csv (venture_id, name, sector, band, completion_est,
signal_quality, has_code, has_dashboard, has_payments, notes), sorted by completion_est desc.
"""
import csv
import hashlib
import json

DOCS = "/Users/acebless/Documents"
LEDGER = f"{DOCS}/venture-completion-ledger.json"
OUT = f"{DOCS}/venture-completion-ranked.csv"

STAGE_BAND = {"growth": 85, "mvp": 60, "validation": 25, "planned": 5}


def content_hash(v, ignore=("business_id", "business_name", "github_repo", "dashboard_url", "last_updated")):
    v2 = {k: val for k, val in v.items() if k not in ignore}
    return hashlib.md5(json.dumps(v2, sort_keys=True).encode()).hexdigest()


def main():
    data = json.load(open(LEDGER))
    ventures = data["ventures"]

    # find schema-A boilerplate clusters (identical content across >1 repo) so we can flag them
    schema_a = {k: v for k, v in ventures.items() if "completion_percent" in v}
    a_groups = {}
    for k, v in schema_a.items():
        h = content_hash(v)
        a_groups.setdefault(h, []).append(k)
    boilerplate_repos = {k for names in a_groups.values() if len(names) > 1 for k in names}

    rows = []
    for repo, v in ventures.items():
        if "completion_percent" in v:
            est = v.get("completion_percent", 0)
            quality = "templated-untrusted" if repo in boilerplate_repos else "measured"
            note = "identical venture.json cloned across sibling repos, not repo-specific" if repo in boilerplate_repos else ""
            rows.append({
                "repo": repo,
                "venture_id": v.get("venture_id", ""),
                "name": v.get("name", ""),
                "sector": v.get("sector", ""),
                "band": v.get("status", ""),
                "completion_est": est,
                "signal_quality": quality,
                "has_code": v.get("has_code"),
                "has_dashboard": v.get("has_dashboard"),
                "has_payments": v.get("has_payments"),
                "notes": note,
            })
        elif "development_stage" in v:
            stage = v.get("development_stage", "planned")
            rows.append({
                "repo": repo,
                "venture_id": v.get("business_id", ""),
                "name": v.get("business_name", ""),
                "sector": v.get("sector", ""),
                "band": stage,
                "completion_est": STAGE_BAND.get(stage, 0),
                "signal_quality": "stage-band-estimate",
                "has_code": "",
                "has_dashboard": "",
                "has_payments": "",
                "notes": f"no numeric completion field; banded from development_stage={stage}",
            })

    for repo in data.get("repos_without_venture_json", []):
        rows.append({
            "repo": repo, "venture_id": "", "name": "", "sector": "",
            "band": "no_venture_json", "completion_est": 0,
            "signal_quality": "no-data", "has_code": "", "has_dashboard": "", "has_payments": "",
            "notes": "no venture.json/VENTURE.json file in repo at all",
        })

    rows.sort(key=lambda r: (-r["completion_est"], r["repo"]))

    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    measured = [r for r in rows if r["signal_quality"] == "measured"]
    templated = [r for r in rows if r["signal_quality"] == "templated-untrusted"]
    banded = [r for r in rows if r["signal_quality"] == "stage-band-estimate"]
    nodata = [r for r in rows if r["signal_quality"] == "no-data"]
    print(f"Total rows: {len(rows)}")
    print(f"  measured (trust as-is): {len(measured)}")
    print(f"  templated-untrusted (boilerplate clone, ignore the %): {len(templated)}")
    print(f"  stage-band-estimate (development_stage only): {len(banded)}")
    print(f"  no-data (no venture.json at all): {len(nodata)}")
    print(f"Written to {OUT}")
    print("\nTop 15 by completion_est:")
    for r in rows[:15]:
        print(f"  {r['completion_est']:3d}%  {r['repo']:45s} [{r['signal_quality']}]  {r['notes']}")


if __name__ == "__main__":
    main()
