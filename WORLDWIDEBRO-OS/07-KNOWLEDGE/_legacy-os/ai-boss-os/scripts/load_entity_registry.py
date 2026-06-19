#!/usr/bin/env python3
"""Load ventures-master.csv into registries/entity_registry/entities.json."""

from __future__ import annotations

import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENTURE_HUB = ROOT.parent / "venture-hub"
VENTURES_CSV = VENTURE_HUB / "ventures-master.csv"
SECTOR_AGENTS = VENTURE_HUB / "registries" / "sector_agents.json"
SECTOR_MAPPING = VENTURE_HUB / "registries" / "sector_code_mapping.json"
OUT_DIR = ROOT / "registries" / "entity_registry"


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def venture_prefix(venture_id: str) -> str:
    return venture_id.split("-", 1)[0].upper()


def resolve_sector_code(
    venture_id: str,
    sector_slug: str,
    prefix_map: dict[str, str],
    legacy_map: dict[str, str],
) -> str:
    prefix = venture_prefix(venture_id)
    if prefix in prefix_map:
        return prefix_map[prefix]
    slug = (sector_slug or "").strip().lower()
    if slug in legacy_map:
        return legacy_map[slug]
    return prefix if len(prefix) <= 6 else "VS"


def github_slug(repository_url: str) -> str | None:
    match = re.search(r"github\.com/Worldwidebro/([^/]+)", repository_url or "")
    return match.group(1) if match else None


def main() -> None:
    if not VENTURES_CSV.exists():
        raise SystemExit(f"Missing source CSV: {VENTURES_CSV}")

    sector_agents = load_json(SECTOR_AGENTS)
    sector_mapping = load_json(SECTOR_MAPPING)
    prefix_map = sector_mapping["venture_id_prefix_to_sector_code"]
    legacy_map = sector_mapping["legacy_sector_slug_to_sector_code"]

    sectors = [
        {
            "sector_code": agent["sector_code"],
            "name": agent["name"],
            "economic_layer": agent["economic_layer"],
            "agent_id": agent["agent_id"],
            "dispatch_status": agent["dispatch_status"],
        }
        for agent in sector_agents["agents"]
    ]
    sector_codes = {s["sector_code"] for s in sectors}

    ventures: list[dict] = []
    edges: list[dict] = []
    unresolved: list[str] = []

    with VENTURES_CSV.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            venture_id = row["venture_id"].strip()
            sector_code = resolve_sector_code(
                venture_id, row.get("sector", ""), prefix_map, legacy_map
            )
            if sector_code not in sector_codes:
                unresolved.append(f"{venture_id} -> {sector_code}")
            repo_url = (row.get("repository_url") or "").strip()
            venture = {
                "venture_id": venture_id,
                "name": row.get("name", "").strip(),
                "sector_code": sector_code,
                "sector_slug": (row.get("sector") or "").strip(),
                "stage": (row.get("stage") or "").strip(),
                "status": (row.get("status") or "").strip(),
                "repository_url": repo_url or None,
                "github_slug": github_slug(repo_url),
                "revenue_ytd": row.get("revenue_ytd") or None,
                "costs_mom": row.get("costs_mom") or None,
                "staff_count": row.get("staff_count") or None,
                "blockers": row.get("blockers") or None,
                "next_action": row.get("next_action") or None,
            }
            ventures.append(venture)
            edges.append(
                {
                    "type": "BELONGS_TO_SECTOR",
                    "from": venture_id,
                    "to": sector_code,
                }
            )

    entities = {
        "version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": {
            "ventures_csv": str(VENTURES_CSV),
            "sector_agents": str(SECTOR_AGENTS),
            "sector_mapping": str(SECTOR_MAPPING),
        },
        "counts": {
            "ventures": len(ventures),
            "sectors": len(sectors),
            "relationships": len(edges),
        },
        "sectors": sectors,
        "ventures": ventures,
    }

    relationships = {
        "version": "1.0.0",
        "generated_at": entities["generated_at"],
        "format": "edge_list",
        "neo4j_sync": "CREATE (v:Venture)-[:BELONGS_TO_SECTOR]->(s:Sector)",
        "edges": edges,
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    entities_path = OUT_DIR / "entities.json"
    relationships_path = OUT_DIR / "relationships.graph"

    with entities_path.open("w", encoding="utf-8") as f:
        json.dump(entities, f, indent=2)
        f.write("\n")

    with relationships_path.open("w", encoding="utf-8") as f:
        json.dump(relationships, f, indent=2)
        f.write("\n")

    print(f"Wrote {entities_path} ({len(ventures)} ventures, {len(sectors)} sectors)")
    print(f"Wrote {relationships_path} ({len(edges)} edges)")
    if unresolved:
        print(f"Warning: {len(unresolved)} ventures mapped to unknown sector codes")
        for item in unresolved[:5]:
            print(f"  {item}")


if __name__ == "__main__":
    main()
