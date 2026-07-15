#!/usr/bin/env python3
"""
Venture Readiness Scorecard v2 — replaces self-reported development_stage
(from each repo's venture.json) with a stage derived from real code signals
(repos-with-sites.json: has_index_html, has_vercel_json, frontend_framework)
plus existing capability_coverage_pct.

Keeps the same weighted formula as v1:
  readiness_pct = 0.35*stage_score + 0.35*capability_coverage_pct
                + 10*entity_formed + 10*has_repo + 10*has_revenue_model
  stage_score: planned=10, validation=35, mvp=65, growth=90

Inputs (read-only):
  - VENTURE-READINESS-SCORECARD.csv   (v1 output: capability_coverage_pct, entity_status, has_repo, has_revenue_model)
  - repos-with-sites.json             (repo short-name -> real code signals)
  - REPOSITORY-REGISTRY.json          (full owned-repo list, for confirmed-negative detection)

repo_key for each venture is derived directly from its own venture_id
(lowercased), which matches real repo slugs 1:1 — not from
venture-completion-ledger.json's business_id/github_repo fields, which are
unreliable (some ventures use an incompatible second schema with no
business_id at all; some repos' own venture.json is a copy-paste clone
pointing at the wrong repo entirely — see the construction-sector clone bug).

Outputs:
  - VENTURE-READINESS-SCORECARD-V2.csv
  - VENTURE-READINESS-SUMMARY-V2.json
"""
import csv
import json

STAGE_SCORE = {"planned": 10, "validation": 35, "mvp": 65, "growth": 90}


def compute_stage(site_signal, capability_coverage_pct, self_reported_stage, repo_key, owned_names):
    """Derive stage from real signals.

    scan_all_repos_for_sites.py already scanned ALL 864 owned repos and only
    recorded entries that had a site signal. So repo_key absent from `sites`
    is a confirmed negative (repo exists, has no site code) if repo_key is in
    owned_names — that's real evidence, not a gap. Only fall back to the
    self-reported stage (unverified) when the repo couldn't be matched to an
    owned repo at all (name mismatch or no repo on record).
    """
    if site_signal is None:
        if repo_key and repo_key in owned_names:
            # confirmed negative: repo scanned, no site/app code found
            if capability_coverage_pct > 0:
                return "validation", True
            return "planned", True
        return self_reported_stage, False  # repo not found in owned registry — unverified

    has_index = bool(site_signal.get("has_index_html"))
    has_vercel = bool(site_signal.get("has_vercel_json"))
    has_framework = bool(site_signal.get("frontend_framework"))

    if capability_coverage_pct >= 50 and (has_vercel or has_index):
        return "growth", True
    if (has_index or has_framework) and has_vercel:
        return "mvp", True
    if has_index or has_framework or capability_coverage_pct > 0:
        return "validation", True
    return "planned", True


def main():
    with open("repos-with-sites.json") as f:
        sites = json.load(f)["sites"]

    with open("WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json") as f:
        registry = json.load(f)
    owned_names = {
        r["name"].lower()
        for r in registry["repositories"]
        if r["url"].startswith("https://github.com/Worldwidebro/")
    }

    rows = []
    with open("VENTURE-READINESS-SCORECARD.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    mismatches = 0
    unverified = 0
    for row in rows:
        vid = row["venture_id"]
        repo_key = vid.lower()
        site_signal = sites.get(repo_key)

        cap_pct = float(row["capability_coverage_pct"])
        self_stage = row["development_stage"]

        computed_stage, verified = compute_stage(site_signal, cap_pct, self_stage, repo_key, owned_names)
        if not verified:
            unverified += 1
        if computed_stage != self_stage:
            mismatches += 1

        stage_score = STAGE_SCORE.get(computed_stage, 10)
        entity_formed = 1 if row["entity_status"] not in ("pending_formation", "", None) else 0
        has_repo = 1 if row["has_repo"] == "True" else 0
        has_revenue_model = 1 if row["has_revenue_model"] == "True" else 0

        readiness_v2 = round(
            0.35 * stage_score
            + 0.35 * cap_pct
            + 10 * entity_formed
            + 10 * has_repo
            + 10 * has_revenue_model,
            1,
        )

        row["repo_key"] = repo_key
        row["stage_verified"] = verified
        row["development_stage_v1_self_reported"] = self_stage
        row["development_stage_v2_computed"] = computed_stage
        row["readiness_pct_v1"] = row["readiness_pct"]
        row["readiness_pct_v2"] = readiness_v2

    # write corrected CSV
    fieldnames = list(rows[0].keys())
    with open("VENTURE-READINESS-SCORECARD-V2.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # aggregate stats
    def tier(pct):
        if pct >= 90:
            return "Revenue / Scale"
        if pct >= 60:
            return "Beta / Launch-ready"
        if pct >= 35:
            return "Building / MVP"
        if pct >= 15:
            return "Planned / Validating"
        return "Idea"

    v1_avg = sum(float(r["readiness_pct_v1"]) for r in rows) / len(rows)
    v2_avg = sum(float(r["readiness_pct_v2"]) for r in rows) / len(rows)

    tiers_v2 = {}
    for r in rows:
        t = tier(float(r["readiness_pct_v2"]))
        tiers_v2[t] = tiers_v2.get(t, 0) + 1

    sector_avg_v2 = {}
    sector_counts = {}
    for r in rows:
        s = r["sector"]
        sector_avg_v2[s] = sector_avg_v2.get(s, 0) + float(r["readiness_pct_v2"])
        sector_counts[s] = sector_counts.get(s, 0) + 1
    sector_avg_v2 = {s: round(v / sector_counts[s], 1) for s, v in sector_avg_v2.items()}
    sector_avg_v2 = dict(sorted(sector_avg_v2.items(), key=lambda x: -x[1]))

    summary = {
        "generated_from": "build_venture_readiness_v2.py",
        "total_ventures": len(rows),
        "ventures_with_verified_stage": len(rows) - unverified,
        "ventures_unverified_stage_fallback": unverified,
        "stage_mismatches_v1_vs_v2": mismatches,
        "portfolio_average_readiness_v1": round(v1_avg, 1),
        "portfolio_average_readiness_v2": round(v2_avg, 1),
        "tier_distribution_v2": tiers_v2,
        "sector_average_readiness_v2": sector_avg_v2,
    }

    with open("VENTURE-READINESS-SUMMARY-V2.json", "w") as f:
        json.dump(summary, f, indent=2)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
