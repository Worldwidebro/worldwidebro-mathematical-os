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
from datetime import datetime
from typing import List, Dict, Any, Optional

OBSIDIAN_VAULT = "/Users/acebless/Documents"
GRAPH_DATA_FILE = f"{OBSIDIAN_VAULT}/.planning/graph-data.json"


def get_credentials() -> tuple[Optional[str], Optional[str]]:
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

    # Show summary
    print(format_graph_summary(graph_data))

    if graph_data.get("status") == "success":
        print(f"✅ Graph exported to: {filepath}")
        print(f"\n📊 Obsidian Dashboard:")
        print(f"  - Open: KNOWLEDGE-GRAPH-DASHBOARD.md")
        print(f"  - Dataview queries automatically load from: {GRAPH_DATA_FILE}")
        print(f"  - Run this script anytime to refresh the data")
    else:
        print(f"⚠️  {graph_data.get('status')}")


if __name__ == "__main__":
    main()
