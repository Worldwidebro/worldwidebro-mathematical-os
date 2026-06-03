#!/usr/bin/env python3
"""
Export knowledge graph from Supabase to Obsidian-compatible JSON
Allows Dataview queries to display live graph data in Obsidian dashboard

Usage:
  python3 obsidian_graph_sync.py                              # Use env vars
  python3 obsidian_graph_sync.py <url> <key>                 # Pass credentials
  python3 obsidian_graph_sync.py --help                       # Show help
"""

import os
import sys
import json
import re
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple

OBSIDIAN_VAULT = "/Users/acebless/Documents"
GRAPH_DATA_FILE = f"{OBSIDIAN_VAULT}/.planning/graph-data.json"
ALIGNMENT_DATA_FILE = f"{OBSIDIAN_VAULT}/.planning/venture-hub-alignment.json"
ENRICHED_VENTURES_FILE = f"{OBSIDIAN_VAULT}/ventures_enriched_option_b.json"
VENTURE_DEPENDENCIES_FILE = f"{OBSIDIAN_VAULT}/ventures_dependencies.json"
BRIDGE_CSV = f"{OBSIDIAN_VAULT}/venture-hub/registries/venture_uuid_slug_bridge.csv"


def normalize_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (name or "").lower())


def count_graph_entities(
    venture_uuid: str,
    venture_name: str,
    owned_slug: str,
    graph_entities: List[dict],
) -> int:
    norm_name = normalize_name(venture_name)
    hits = 0
    for entity in graph_entities:
        vid = (entity or {}).get("venture_id") or ""
        if vid == venture_uuid:
            hits += 1
            continue
        ename = normalize_name(entity.get("name", ""))
        if norm_name and ename and (norm_name in ename or ename in norm_name):
            hits += 1
            continue
        blob = f"{entity.get('name', '')} {entity.get('description', '')}".lower()
        if owned_slug and owned_slug.lower() in blob:
            hits += 1
    return hits


def load_bridge_by_uuid() -> Dict[str, dict]:
    if not os.path.exists(BRIDGE_CSV):
        return {}
    import csv
    with open(BRIDGE_CSV, newline="", encoding="utf-8") as f:
        return {row["venture_uuid"]: row for row in csv.DictReader(f) if row.get("venture_uuid")}


def get_credentials() -> Tuple[Optional[str], Optional[str]]:
    """Load Supabase credentials from env, .env file, or CLI args"""
    # Try CLI arguments
    if len(sys.argv) >= 3:
        return sys.argv[1], sys.argv[2]

    # Try environment variables
    url = os.getenv("SUPABASE_URL", "")
    key = os.getenv("SUPABASE_KEY", "")
    if url and key:
        return url, key

    # Try .env file
    env_file = f"{OBSIDIAN_VAULT}/.env"
    if os.path.exists(env_file):
        try:
            with open(env_file) as f:
                for line in f:
                    if line.startswith("SUPABASE_URL="):
                        url = line.split("=", 1)[1].strip()
                    elif line.startswith("SUPABASE_KEY="):
                        key = line.split("=", 1)[1].strip()
        except Exception:
            pass
        if url and key:
            return url, key

    return None, None


SUPABASE_URL, SUPABASE_KEY = get_credentials()


def fetch_graph_data() -> Dict[str, Any]:
    """Fetch entities and relationships from Supabase"""
    if not SUPABASE_URL or not SUPABASE_KEY:
        return {"entities": [], "relationships": [], "status": "no_credentials"}

    try:
        from supabase import create_client
        client = create_client(SUPABASE_URL, SUPABASE_KEY)

        # Fetch all entities
        entities_resp = client.table("graph_entities").select("*").execute()
        entities = entities_resp.data if entities_resp.data else []

        # Fetch all relationships
        rels_resp = client.table("graph_relationships").select("*").execute()
        relationships = rels_resp.data if rels_resp.data else []

        return {
            "entities": entities,
            "relationships": relationships,
            "status": "success",
            "synced_at": datetime.utcnow().isoformat(),
            "entity_count": len(entities),
            "relationship_count": len(relationships),
        }

    except Exception as e:
        return {
            "entities": [],
            "relationships": [],
            "status": f"error: {str(e)}",
            "synced_at": datetime.utcnow().isoformat(),
        }


def export_to_obsidian(graph_data: Dict) -> str:
    """Export graph data to JSON in Obsidian vault"""
    os.makedirs(os.path.dirname(GRAPH_DATA_FILE), exist_ok=True)

    with open(GRAPH_DATA_FILE, "w") as f:
        json.dump(graph_data, f, indent=2)

    return GRAPH_DATA_FILE


def load_local_json(path: str, fallback: Dict[str, Any]) -> Dict[str, Any]:
    """Load JSON from disk, return fallback on missing/invalid file."""
    if not os.path.exists(path):
        return fallback
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception:
        return fallback


def fetch_supabase_repo_names() -> List[str]:
    """Fetch repo names from Supabase repositories + repos tables for coverage checks."""
    if not SUPABASE_URL or not SUPABASE_KEY:
        return []

    try:
        from supabase import create_client

        client = create_client(SUPABASE_URL, SUPABASE_KEY)
        names: List[str] = []
        seen = set()

        for table in ("repositories", "repos"):
            try:
                resp = client.table(table).select("name,full_name").execute()
                rows = resp.data if resp.data else []
            except Exception:
                rows = []
            for repo in rows:
                for field in ("name", "full_name"):
                    value = (repo or {}).get(field)
                    if not value:
                        continue
                    key = str(value).strip().lower()
                    if key and key not in seen:
                        seen.add(key)
                        names.append(str(value).strip())
        return names
    except Exception:
        return []


def build_alignment_report(graph_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Build single-source alignment status:
    ventures (UUID/name) + required repos + graph linkage + repo coverage.
    """
    enriched = load_local_json(ENRICHED_VENTURES_FILE, {"ventures": []})
    dependencies = load_local_json(VENTURE_DEPENDENCIES_FILE, {"dependencies": {}})
    ventures = enriched.get("ventures", []) or []
    deps_map = dependencies.get("dependencies", {}) or {}

    graph_entities = graph_data.get("entities", []) or []
    bridge_by_uuid = load_bridge_by_uuid()

    supabase_repo_names = fetch_supabase_repo_names()
    supabase_repo_names_lower = {name.lower() for name in supabase_repo_names}

    aligned = []
    mismatched = []

    for venture in ventures:
        venture_id = (venture or {}).get("venture_id")
        venture_name = (venture or {}).get("venture_name", "Unknown")
        dependency = deps_map.get(venture_id, {})
        required_repos = dependency.get("required_repos", []) or []
        bridge = bridge_by_uuid.get(venture_id, {})
        owned_slug = bridge.get("owned_repo_slug") or (venture or {}).get("owned_repo_slug") or ""

        graph_entity_count = count_graph_entities(
            venture_id,
            venture_name,
            owned_slug,
            graph_entities,
        )
        graph_connected = graph_entity_count > 0

        matched_required_repos = [
            repo for repo in required_repos if str(repo).lower() in supabase_repo_names_lower
        ]
        missing_required_repos = [
            repo for repo in required_repos if str(repo).lower() not in supabase_repo_names_lower
        ]

        venture_record = {
            "venture_id": venture_id,
            "venture_name": venture_name,
            "sector": (venture or {}).get("sector", "unknown"),
            "required_repos": required_repos,
            "top_repo_1": (venture or {}).get("top_repo_1"),
            "owned_repo_slug": owned_slug,
            "owned_repo_found": bridge.get("owned_gap_status") == "matched" or bool(owned_slug),
            "graph_entity_count": graph_entity_count,
            "graph_connected": graph_connected,
            "matched_required_repos": matched_required_repos,
            "missing_required_repos": missing_required_repos,
            "repo_coverage_pct": (
                round((len(matched_required_repos) / len(required_repos)) * 100, 2)
                if required_repos
                else 100.0
            ),
            "alignment_status": (
                "aligned"
                if graph_connected and len(missing_required_repos) == 0
                else "needs_attention"
            ),
        }

        aligned.append(venture_record)
        if venture_record["alignment_status"] != "aligned":
            mismatched.append(venture_record)

    return {
        "status": "success",
        "generated_at": datetime.utcnow().isoformat(),
        "source_files": {
            "ventures": ENRICHED_VENTURES_FILE,
            "dependencies": VENTURE_DEPENDENCIES_FILE,
            "graph_data": GRAPH_DATA_FILE,
        },
        "summary": {
            "total_ventures": len(ventures),
            "ventures_aligned": sum(1 for v in aligned if v["alignment_status"] == "aligned"),
            "ventures_needing_attention": len(mismatched),
            "ventures_with_graph_entities": sum(1 for v in aligned if v["graph_connected"]),
            "ventures_with_owned_repo": sum(
                1 for v in aligned if v.get("owned_repo_found") in (True, "yes", "matched")
            ),
            "supabase_repo_count": len(supabase_repo_names),
            "supabase_repositories_count": len(supabase_repo_names),
        },
        "ventures": aligned,
        "mismatches": mismatched[:200],
    }


def export_alignment_to_obsidian(alignment_data: Dict[str, Any]) -> str:
    """Export venture-hub alignment data to JSON in Obsidian vault."""
    os.makedirs(os.path.dirname(ALIGNMENT_DATA_FILE), exist_ok=True)
    with open(ALIGNMENT_DATA_FILE, "w") as f:
        json.dump(alignment_data, f, indent=2)
    return ALIGNMENT_DATA_FILE


def format_graph_summary(graph_data: Dict) -> str:
    """Format summary for console output"""
    entities = graph_data.get("entities", [])
    relationships = graph_data.get("relationships", [])

    summary = f"""
📊 Knowledge Graph Export
{'='*60}
Entities: {len(entities)}
Relationships: {len(relationships)}
Status: {graph_data.get('status', 'unknown')}
File: {GRAPH_DATA_FILE}

Entity Types:
"""

    # Count by type
    type_counts: Dict[str, int] = {}
    for entity in entities:
        etype = entity.get("entity_type", "unknown")
        type_counts[etype] = type_counts.get(etype, 0) + 1

    for etype, count in sorted(type_counts.items()):
        summary += f"  - {etype}: {count}\n"

    summary += f"\nRelationship Types:\n"
    rel_counts: Dict[str, int] = {}
    for rel in relationships:
        rtype = rel.get("relation_type", "unknown")
        rel_counts[rtype] = rel_counts.get(rtype, 0) + 1

    for rtype, count in sorted(rel_counts.items()):
        summary += f"  - {rtype}: {count}\n"

    summary += f"{'='*60}\n"
    return summary


def main():
    """Sync graph to Obsidian"""
    print("\n🔄 Syncing knowledge graph to Obsidian...")

    if not SUPABASE_URL or not SUPABASE_KEY:
        print(f"\n⚠️  Supabase credentials not found!")
        print(f"\nTo provide credentials, use ONE of these methods:")
        print(f"\n1. Environment variables:")
        print(f"   export SUPABASE_URL='<your-url>'")
        print(f"   export SUPABASE_KEY='<your-key>'")
        print(f"   python3 obsidian_graph_sync.py")
        print(f"\n2. CLI arguments:")
        print(f"   python3 obsidian_graph_sync.py <url> <key>")
        print(f"\n3. Create .env file at: /Users/acebless/Documents/.env")
        print(f"   SUPABASE_URL=<your-url>")
        print(f"   SUPABASE_KEY=<your-key>")
        print(f"   python3 obsidian_graph_sync.py")
        sys.exit(1)

    # Fetch from Supabase
    graph_data = fetch_graph_data()

    # Export to JSON
    filepath = export_to_obsidian(graph_data)
    alignment_data = build_alignment_report(graph_data)
    alignment_filepath = export_alignment_to_obsidian(alignment_data)

    # Show summary
    print(format_graph_summary(graph_data))

    if graph_data.get("status") == "success":
        print(f"✅ Graph exported to: {filepath}")
        print(f"✅ Alignment exported to: {alignment_filepath}")
        print(f"\n📊 Obsidian Dashboard:")
        print(f"  - Open: KNOWLEDGE-GRAPH-DASHBOARD.md")
        print(f"  - Dataview queries automatically load from: {GRAPH_DATA_FILE}")
        print(f"  - Venture alignment data at: {ALIGNMENT_DATA_FILE}")
        print(f"  - Run this script anytime to refresh the data")
        print(f"\n🔗 Venture Hub Alignment Summary:")
        summary = alignment_data.get("summary", {})
        print(f"  - Total ventures: {summary.get('total_ventures', 0)}")
        print(f"  - Aligned ventures: {summary.get('ventures_aligned', 0)}")
        print(f"  - Needs attention: {summary.get('ventures_needing_attention', 0)}")
    else:
        print(f"⚠️  {graph_data.get('status')}")


if __name__ == "__main__":
    main()
