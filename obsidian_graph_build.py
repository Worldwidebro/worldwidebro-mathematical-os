#!/usr/bin/env python3
"""
Build a proper Obsidian knowledge graph using Obsidian Skills
Creates markdown notes + Canvas + wikilinks from Supabase graph
"""

import os
import json
import subprocess
from datetime import datetime
from typing import Dict, List, Optional

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
OBSIDIAN_VAULT = "/Users/acebless/Documents"
GRAPH_DIR = f"{OBSIDIAN_VAULT}/Knowledge Graph"


def fetch_graph_data() -> Dict:
    """Fetch entities and relationships from Supabase"""
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("⚠️  Supabase credentials not configured")
        return {"entities": [], "relationships": []}

    try:
        from supabase import create_client
        client = create_client(SUPABASE_URL, SUPABASE_KEY)

        entities_resp = client.table("graph_entities").select("*").execute()
        rels_resp = client.table("graph_relationships").select("*").execute()

        return {
            "entities": entities_resp.data or [],
            "relationships": rels_resp.data or []
        }
    except Exception as e:
        print(f"❌ Error fetching from Supabase: {e}")
        return {"entities": [], "relationships": []}


def sanitize_filename(text: str) -> str:
    """Convert entity name to valid markdown filename"""
    return text.replace(" ", "_").replace("/", "_").lower()


def create_entity_note(entity: Dict, relationships: List[Dict]) -> str:
    """Create markdown note for an entity with wikilinks to related entities"""

    name = entity["name"]
    entity_type = entity["entity_type"]
    venture_id = entity.get("venture_id", "")
    description = entity.get("description", "")
    metadata = entity.get("metadata", {})

    # Find related entities
    related = {
        "outgoing": [],
        "incoming": []
    }

    for rel in relationships:
        if rel["source_id"] == entity["id"]:
            related["outgoing"].append(rel)
        elif rel["target_id"] == entity["id"]:
            related["incoming"].append(rel)

    # Build markdown content
    content = f"""---
title: {name}
entity_type: {entity_type}
venture_id: {venture_id}
created: {datetime.utcnow().isoformat()}
---

# {name}

**Type**: {entity_type}
**Venture**: {venture_id or "—"}

## Description

{description or "No description available"}

## Metadata

"""

    # Add metadata as properties
    for key, value in metadata.items():
        content += f"- **{key}**: {value}\n"

    # Add relationships as wikilinks
    if related["outgoing"]:
        content += f"\n## Related (Outgoing)\n\n"
        for rel in related["outgoing"]:
            target_name = next(
                (e["name"] for e in fetch_graph_data()["entities"] if e["id"] == rel["target_id"]),
                rel["target_id"]
            )
            content += f"- [[{target_name}]] ({rel['relation_type']})\n"

    if related["incoming"]:
        content += f"\n## Related (Incoming)\n\n"
        for rel in related["incoming"]:
            source_name = next(
                (e["name"] for e in fetch_graph_data()["entities"] if e["id"] == rel["source_id"]),
                rel["source_id"]
            )
            content += f"- [[{source_name}]] ({rel['relation_type']})\n"

    return content


def create_canvas_file(entities: List[Dict], relationships: List[Dict]) -> Dict:
    """Create JSON Canvas showing the knowledge graph visually"""

    canvas = {
        "nodes": [],
        "edges": []
    }

    # Position nodes in a circle
    import math
    n = len(entities)
    radius = 400

    # Map entity ID to node ID
    entity_to_node = {}

    # Create nodes
    for idx, entity in enumerate(entities):
        angle = (idx / n) * 2 * math.pi
        x = math.cos(angle) * radius
        y = math.sin(angle) * radius

        node_id = f"node_{idx}"
        entity_to_node[entity["id"]] = node_id

        # Determine node color by type
        type_colors = {
            "Venture": "#4285F4",      # Blue
            "Decision": "#34A853",     # Green
            "Metric": "#FBBC04",       # Yellow
            "Risk": "#EA4335",         # Red
            "Agent": "#A142F4",        # Purple
        }

        color = type_colors.get(entity["entity_type"], "#999999")

        canvas["nodes"].append({
            "id": node_id,
            "type": "file",
            "file": f"Knowledge Graph/{entity['name']}.md",
            "x": x,
            "y": y,
            "width": 200,
            "height": 100,
            "color": color
        })

    # Create edges for relationships
    for rel in relationships:
        source_node = entity_to_node.get(rel["source_id"])
        target_node = entity_to_node.get(rel["target_id"])

        if source_node and target_node:
            canvas["edges"].append({
                "id": f"edge_{rel.get('id', len(canvas['edges']))}",
                "fromNode": source_node,
                "toNode": target_node,
                "label": rel["relation_type"]
            })

    return canvas


def main():
    """Build complete Obsidian knowledge graph"""

    print("\n🚀 Building Obsidian Knowledge Graph with Obsidian Skills")
    print("="*70)

    # Create graph directory
    os.makedirs(GRAPH_DIR, exist_ok=True)

    # Fetch data
    data = fetch_graph_data()
    entities = data["entities"]
    relationships = data["relationships"]

    if not entities:
        print("❌ No entities found. Run: python3 obsidian_graph_sync.py first")
        return

    print(f"\n📊 Processing {len(entities)} entities and {len(relationships)} relationships\n")

    # Create entity notes
    created_notes = 0
    for entity in entities:
        try:
            note_content = create_entity_note(entity, relationships)
            filename = sanitize_filename(entity["name"])
            filepath = f"{GRAPH_DIR}/{filename}.md"

            with open(filepath, "w") as f:
                f.write(note_content)

            created_notes += 1
            print(f"✅ {entity['name']}")
        except Exception as e:
            print(f"❌ {entity['name']}: {e}")

    print(f"\n✅ Created {created_notes} markdown notes in {GRAPH_DIR}/")

    # Create Canvas file
    try:
        canvas = create_canvas_file(entities, relationships)
        canvas_file = f"{GRAPH_DIR}/Knowledge Graph.canvas"

        with open(canvas_file, "w") as f:
            json.dump(canvas, f, indent=2)

        print(f"✅ Created visual canvas: {canvas_file}")
    except Exception as e:
        print(f"❌ Canvas creation failed: {e}")

    # Create index
    try:
        index_content = f"""---
title: Knowledge Graph Index
type: index
created: {datetime.utcnow().isoformat()}
---

# Knowledge Graph Index

**Total Entities**: {len(entities)}
**Total Relationships**: {len(relationships)}
**Last Generated**: {datetime.utcnow().isoformat()}

## By Entity Type

"""

        # Group by type
        by_type = {}
        for entity in entities:
            etype = entity["entity_type"]
            if etype not in by_type:
                by_type[etype] = []
            by_type[etype].append(entity)

        for etype in sorted(by_type.keys()):
            index_content += f"\n### {etype} ({len(by_type[etype])})\n\n"
            for entity in sorted(by_type[etype], key=lambda e: e["name"]):
                filename = sanitize_filename(entity["name"])
                index_content += f"- [[{entity['name']}]]\n"

        index_file = f"{GRAPH_DIR}/Index.md"
        with open(index_file, "w") as f:
            f.write(index_content)

        print(f"✅ Created index: {index_file}")
    except Exception as e:
        print(f"❌ Index creation failed: {e}")

    print(f"\n{'='*70}")
    print(f"✅ OBSIDIAN KNOWLEDGE GRAPH BUILT")
    print(f"{'='*70}\n")

    print(f"📂 Location: {GRAPH_DIR}")
    print(f"\nIn Obsidian:")
    print(f"  1. Open the 'Knowledge Graph' folder")
    print(f"  2. Click 'Knowledge Graph.canvas' for visual view")
    print(f"  3. Click 'Index.md' for entity listing")
    print(f"  4. Click any entity to explore connections (via wikilinks)")
    print(f"\nEvery entity has:")
    print(f"  - Metadata and description")
    print(f"  - Wikilinks to related entities")
    print(f"  - Type and venture information")
    print(f"  - Visual representation in canvas")


if __name__ == "__main__":
    main()
