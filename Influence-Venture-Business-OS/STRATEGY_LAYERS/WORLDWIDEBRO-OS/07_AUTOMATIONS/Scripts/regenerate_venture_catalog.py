#!/usr/bin/env python3
"""Rebuild ventures_classification_final.csv and ventures_enriched_option_b.json from live hub exports."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[3]
VENTURES_DATA = ROOT / "WORLDWIDEBRO-OS" / "08_RESEARCH" / "Ventures-Data"
COMBINED = ROOT / "venture-hub" / "docs" / "VENTURE_STARRED_OWNED_REPOS.csv"
CAPABILITIES = VENTURES_DATA / "ventures_with_capabilities.csv"
DEPENDENCIES = VENTURES_DATA / "ventures_dependencies.json"
BRIDGE = ROOT / "venture-hub" / "registries" / "venture_uuid_slug_bridge.csv"

CLASSIFICATION_OUT = [
    ROOT / "ventures_classification_final.csv",
    VENTURES_DATA / "ventures_classification_final.csv",
]
ENRICHED_OUT = [
    ROOT / "ventures_enriched_option_b.json",
    VENTURES_DATA / "ventures_enriched_option_b.json",
]


def load_csv(path: Path) -> List[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_deps() -> Dict[str, dict]:
    if not DEPENDENCIES.exists():
        return {}
    data = json.loads(DEPENDENCIES.read_text(encoding="utf-8"))
    return data.get("dependencies", {}) or {}


def main() -> None:
    if not COMBINED.exists():
        raise SystemExit(f"Missing combined export: {COMBINED}")

    caps_by_id = {}
    if CAPABILITIES.exists():
        for row in load_csv(CAPABILITIES):
            vid = row.get("venture_id", "").strip()
            if vid:
                caps_by_id[vid] = row

    bridge_by_uuid = {}
    if BRIDGE.exists():
        for row in load_csv(BRIDGE):
            uid = row.get("venture_uuid", "").strip()
            if uid:
                bridge_by_uuid[uid] = row

    deps = load_deps()
    combined = load_csv(COMBINED)

    classification_rows: List[dict] = []
    enriched_ventures: List[dict] = []

    for row in combined:
        vid = (row.get("venture_uuid") or "").strip()
        if not vid:
            continue
        name = row.get("venture_name", "").strip()
        sector = row.get("sector", "market").strip() or "market"
        cap = caps_by_id.get(vid, {})
        dep = deps.get(vid, {})
        bridge = bridge_by_uuid.get(vid, {})
        tiers = dep.get("depends_on_tiers") or []
        tier = str(tiers[0]) if tiers else "3"
        top_repo = (cap.get("top_repo_1") or row.get("owned_repo_slug") or "").strip()
        control_type = (dep.get("venture_type") or "platform").upper()
        if control_type == "PLATFORM":
            control_type = "PLATFORM"
        revenue_model = row.get("target_archetype", "system-fees") or "system-fees"
        required_caps = (cap.get("required_capabilities") or "").split("|")
        required_caps = [c.strip() for c in required_caps if c.strip()]

        classification_rows.append({
            "venture_id": vid,
            "venture_name": name,
            "sector": sector,
            "tier": tier,
            "top_repo": top_repo,
            "control_type": control_type,
            "revenue_model": revenue_model,
            "department": sector,
            "business_domain": cap.get("business_domain", ""),
        })

        enriched_ventures.append({
            "venture_id": vid,
            "venture_name": name,
            "sector": sector,
            "venture_slug": row.get("venture_slug") or bridge.get("venture_slug", ""),
            "owned_repo_slug": row.get("owned_repo_slug", ""),
            "required_capabilities": required_caps,
            "capability_match_score": 0.85,
            "matched_repos": {},
            "top_repo_1": top_repo,
            "top_repo_2": cap.get("top_repo_2", ""),
            "top_repo_3": cap.get("top_repo_3", ""),
            "starred_repos_count": int(row.get("starred_repos_count") or 0),
        })

    fieldnames = list(classification_rows[0].keys()) if classification_rows else []
    for out in CLASSIFICATION_OUT:
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(classification_rows)

    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_ventures": len(enriched_ventures),
        "enrichment_method": "regenerated_from_combined_export",
        "ventures": enriched_ventures,
    }
    for out in ENRICHED_OUT:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(f"Wrote {len(classification_rows)} ventures to classification CSV (x{len(CLASSIFICATION_OUT)})")
    print(f"Wrote enriched JSON (x{len(ENRICHED_OUT)})")


if __name__ == "__main__":
    main()
