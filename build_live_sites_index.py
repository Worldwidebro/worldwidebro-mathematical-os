#!/usr/bin/env python3
"""
build_live_sites_index.py — organized, clickable index of every owned repo that
has real site/app code (index.html, vercel.json, or a detected frontend
framework), cross-referenced to its venture name/sector and known live URL.

Inputs (read-only):
  - repos-with-sites.json          (real code signal per repo)
  - venture-completion-ledger.json (github_repo -> business_name/sector)
  - WORLDWIDEBRO-OS/08-DATA/registries/vercel-projects.json
                                    (authoritative Vercel API project list -> latestProductionUrl;
                                     regenerate with: vercel project ls --json, paginated via
                                     pagination.next, since deployment-urls.csv was found stale
                                     — 14 rows vs 58 actually-live matches via the Vercel API)

Output:
  - LIVE-SITES-INDEX.md  (clickable markdown table, sorted: has live_url first, then by venture name)
"""
import json

OWNER = "Worldwidebro"


def main():
    with open("repos-with-sites.json") as f:
        sites = json.load(f)["sites"]

    with open("venture-completion-ledger.json") as f:
        ledger = json.load(f)["ventures"]

    with open("WORLDWIDEBRO-OS/08-DATA/registries/vercel-projects.json") as f:
        vercel_projects = json.load(f)
    live_url_by_repo_name = {
        p["name"]: p["latestProductionUrl"] for p in vercel_projects if p.get("latestProductionUrl")
    }

    # index ledger by short repo name
    ledger_by_repo = {}
    for v in ledger.values():
        repo = v.get("github_repo", "")
        if repo:
            ledger_by_repo[repo.split("/")[-1].strip().lower()] = v

    rows = []
    for repo_key, signal in sites.items():
        ledger_entry = ledger_by_repo.get(repo_key, {})
        venture_id = ledger_entry.get("business_id", "")
        venture_name = ledger_entry.get("business_name", "")
        sector = ledger_entry.get("sector", "")
        live_url = live_url_by_repo_name.get(repo_key, "")
        rows.append(
            {
                "repo_key": repo_key,
                "github_url": f"https://github.com/{OWNER}/{repo_key}",
                "venture_id": venture_id,
                "venture_name": venture_name,
                "sector": sector,
                "framework": signal.get("frontend_framework") or "-",
                "has_vercel_json": signal.get("has_vercel_json", False),
                "live_url": live_url,
            }
        )

    # sort: rows with a known live_url first, then alphabetically by venture name / repo key
    rows.sort(key=lambda r: (r["live_url"] == "", r["venture_name"] or r["repo_key"]))

    with_live_url = sum(1 for r in rows if r["live_url"])

    lines = [
        "# Live Sites Index",
        "",
        f"Repos with real site/app code (index.html, vercel.json, or a detected frontend "
        f"framework): **{len(rows)}** out of {len(sites)} scanned owned repos with a site signal. "
        f"**{with_live_url}** have a confirmed live URL on record.",
        "",
        "| Repo | Venture | Sector | Framework | Vercel config | Live URL |",
        "|---|---|---|---|---|---|",
    ]
    for r in rows:
        live_cell = f"[{r['live_url']}]({r['live_url']})" if r["live_url"] else "-"
        venture_cell = f"{r['venture_name']} (`{r['venture_id']}`)" if r["venture_id"] else "-"
        lines.append(
            f"| [{r['repo_key']}]({r['github_url']}) | {venture_cell} | {r['sector'] or '-'} "
            f"| {r['framework']} | {'✓' if r['has_vercel_json'] else '-'} | {live_cell} |"
        )

    with open("LIVE-SITES-INDEX.md", "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Wrote LIVE-SITES-INDEX.md: {len(rows)} repos, {with_live_url} with a confirmed live URL")


if __name__ == "__main__":
    main()
