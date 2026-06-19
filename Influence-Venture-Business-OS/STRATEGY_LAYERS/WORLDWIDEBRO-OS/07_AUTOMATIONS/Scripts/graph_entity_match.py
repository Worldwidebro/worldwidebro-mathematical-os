"""Shared venture ↔ graph entity matching for alignment and Obsidian sync."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

ROOT = Path(__file__).resolve().parents[3]
GRAPH_DATA = ROOT / ".planning" / "graph-data.json"
MERGED_GRAPH = ROOT / "worldwidebro-vault" / "graphify" / "graph.merged-712.json"
KG_GRAPH = ROOT / "ventures-knowledge-graph.json"

# Required-repo names in dependencies that differ from registry short names
REPO_ALIASES: Dict[str, List[str]] = {
    "awesome-osint-for-everything": ["awesome-osint-list", "awesome-osint-for-everything"],
}

SUPABASE_PAGE_SIZE = 1000


def normalize_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (name or "").lower())


def normalize_slug(slug: str) -> str:
    return (slug or "").strip().lower()


def load_json(path: Path, fallback: Any) -> Any:
    if not path.exists():
        return fallback
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return fallback


def load_kg_venture_ids() -> Set[str]:
    data = load_json(KG_GRAPH, {})
    return {n.get("id", "") for n in data.get("nodes", []) if n.get("id")}


def load_merged_slug_index() -> Dict[str, int]:
    """Map normalized slug/id -> hit count stub (presence)."""
    data = load_json(MERGED_GRAPH, {})
    index: Dict[str, int] = {}
    for node in data.get("nodes", []) or []:
        for key in (
            node.get("id"),
            node.get("venture_id"),
            node.get("label"),
        ):
            norm = normalize_slug(str(key or ""))
            if norm:
                index[norm] = index.get(norm, 0) + 1
    return index


def fetch_supabase_graph_entities(url: str, key: str) -> List[dict]:
    if not url or not key:
        return []
    try:
        from supabase import create_client
    except ImportError:
        return []

    client = create_client(url, key)
    entities: List[dict] = []
    offset = 0
    while True:
        try:
            resp = (
                client.table("graph_entities")
                .select("*")
                .range(offset, offset + SUPABASE_PAGE_SIZE - 1)
                .execute()
            )
        except Exception:
            break
        batch = resp.data if resp.data else []
        if not batch:
            break
        entities.extend(batch)
        if len(batch) < SUPABASE_PAGE_SIZE:
            break
        offset += SUPABASE_PAGE_SIZE
    return entities


def load_graph_entities_from_disk() -> List[dict]:
    data = load_json(GRAPH_DATA, {})
    return list(data.get("entities", []) or [])


def count_graph_entities(
    venture_uuid: str,
    venture_name: str,
    owned_slug: str,
    venture_slug: str,
    graph_entities: List[dict],
    kg_ids: Optional[Set[str]] = None,
    merged_index: Optional[Dict[str, int]] = None,
) -> int:
    kg_ids = kg_ids if kg_ids is not None else load_kg_venture_ids()
    merged_index = merged_index if merged_index is not None else load_merged_slug_index()

    hits = 0
    norm_name = normalize_name(venture_name)
    uuid_prefix = f"entity_venture_{venture_uuid}".lower()

    for entity in graph_entities:
        ent = entity or {}
        vid = ent.get("venture_id") or ""
        eid = str(ent.get("id", "")).lower()
        if vid == venture_uuid or (venture_uuid and uuid_prefix in eid):
            hits += 1
            continue
        ename = normalize_name(ent.get("name", ""))
        if norm_name and ename and (norm_name in ename or ename in norm_name):
            hits += 1
            continue
        blob = f"{ent.get('name', '')} {ent.get('description', '')}".lower()
        if owned_slug and owned_slug.lower() in blob:
            hits += 1

    if venture_uuid and venture_uuid in kg_ids:
        hits += 1

    for slug_candidate in (venture_slug, owned_slug):
        norm = normalize_slug(slug_candidate)
        if norm and merged_index.get(norm):
            hits += 1

    return hits


def repo_name_variants(repo: str) -> List[str]:
    base = (repo or "").strip().lower()
    if not base:
        return []
    variants = {base, base.split("/")[-1]}
    for alias in REPO_ALIASES.get(base, []):
        variants.add(alias.lower())
    return list(variants)


def required_repo_satisfied(repo: str, repo_names_lower: Set[str]) -> bool:
    return any(v in repo_names_lower for v in repo_name_variants(repo))


def load_registry_repo_names(root: Path) -> Set[str]:
    """Owned + starred registry short and full names for required-repo coverage."""
    names: Set[str] = set()
    for rel in (
        "venture-hub/registries/github_owned.csv",
        "venture-hub/registries/github_starred.csv",
    ):
        path = root / rel
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                short = (row.get("name") or "").strip().lower()
                owner = (row.get("owner") or "").strip()
                if short:
                    names.add(short)
                if owner and short:
                    names.add(f"{owner}/{short}".lower())
                full = (row.get("name_with_owner") or row.get("full_name") or "").strip().lower()
                if full:
                    names.add(full)
    return names


def build_repo_coverage_index(root: Path, supabase_names: Optional[List[str]] = None) -> Set[str]:
    """Union of GitHub registries and optional Supabase repo tables."""
    index = load_registry_repo_names(root)
    if supabase_names:
        for name in supabase_names:
            key = str(name).strip().lower()
            if key:
                index.add(key)
                if "/" in key:
                    index.add(key.split("/")[-1])
    return index


def alignment_status(
    graph_connected: bool,
    required_repos: List[str],
    repo_names_lower: Set[str],
) -> str:
    missing = [r for r in required_repos if not required_repo_satisfied(r, repo_names_lower)]
    if graph_connected and not missing:
        return "aligned"
    return "needs_attention"


def resolve_data_file(name: str, root: Optional[Path] = None) -> Path:
    base = root or ROOT
    for path in (
        base / name,
        base / "WORLDWIDEBRO-OS" / "08_RESEARCH" / "Ventures-Data" / name,
    ):
        if path.exists():
            return path
    return base / name


def load_bridge_by_uuid(root: Optional[Path] = None) -> Dict[str, dict]:
    base = root or ROOT
    path = base / "venture-hub" / "registries" / "venture_uuid_slug_bridge.csv"
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as f:
        return {row["venture_uuid"]: row for row in csv.DictReader(f) if row.get("venture_uuid")}


def refresh_planning_alignment_file(
    alignment_path: Optional[Path] = None,
    graph_entities: Optional[List[dict]] = None,
    root: Optional[Path] = None,
) -> Dict[str, Any]:
    """Re-score ventures in planning alignment JSON (graph + repo coverage)."""
    from datetime import datetime, timezone

    base = root or ROOT
    path = alignment_path or (base / ".planning" / "venture-hub-alignment.json")
    data = load_json(path, {})
    ventures = data.get("ventures") or []
    if not ventures:
        return data

    entities = graph_entities if graph_entities is not None else load_graph_entities_from_disk()
    kg_ids = load_kg_venture_ids()
    merged_index = load_merged_slug_index()
    bridge = load_bridge_by_uuid(base)
    repo_index = build_repo_coverage_index(base)

    for v in ventures:
        vid = v.get("venture_id", "")
        br = bridge.get(vid, {})
        slug = v.get("venture_slug") or br.get("venture_slug", "")
        owned = v.get("owned_repo_slug") or br.get("owned_repo_slug", "")
        required = v.get("required_repos") or []
        gc = count_graph_entities(
            vid,
            v.get("venture_name", ""),
            owned,
            slug,
            entities,
            kg_ids=kg_ids,
            merged_index=merged_index,
        )
        v["graph_entity_count"] = gc
        v["graph_connected"] = gc > 0
        matched = [r for r in required if required_repo_satisfied(r, repo_index)]
        missing = [r for r in required if not required_repo_satisfied(r, repo_index)]
        v["matched_required_repos"] = matched
        v["missing_required_repos"] = missing
        v["repo_coverage_pct"] = (
            round((len(matched) / len(required)) * 100, 2) if required else 100.0
        )
        v["alignment_status"] = alignment_status(gc > 0, required, repo_index)

    summary = data.setdefault("summary", {})
    summary["ventures_aligned"] = sum(1 for v in ventures if v.get("alignment_status") == "aligned")
    summary["ventures_needing_attention"] = sum(
        1 for v in ventures if v.get("alignment_status") != "aligned"
    )
    summary["ventures_with_graph_entities"] = sum(1 for v in ventures if v.get("graph_connected"))
    data["generated_at"] = datetime.now(timezone.utc).isoformat()
    data["mismatches"] = [v for v in ventures if v.get("alignment_status") != "aligned"][:200]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return data
