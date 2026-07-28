#!/usr/bin/env python3
"""
Wire Worldwidebro Academy into the knowledge graph.
Creates entities for 30 curriculum layers + relationships to ventures.
"""

import os
import json
import uuid
from datetime import datetime
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# Initialize Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Define Academy 30-layer curriculum
ACADEMY_LAYERS = [
    # Foundation (5)
    {"layer": 1, "name": "Identity & Self-Concept", "category": "Foundation"},
    {"layer": 2, "name": "Emotional Intelligence", "category": "Foundation"},
    {"layer": 3, "name": "Attention Management", "category": "Foundation"},
    {"layer": 4, "name": "Decision-Making", "category": "Foundation"},
    {"layer": 5, "name": "Purpose & Meaning", "category": "Foundation"},

    # Character (10)
    {"layer": 6, "name": "Character", "category": "Character"},
    {"layer": 7, "name": "Thinking", "category": "Character"},
    {"layer": 8, "name": "Communication", "category": "Character"},
    {"layer": 9, "name": "Relationships", "category": "Character"},
    {"layer": 10, "name": "Leadership", "category": "Character"},
    {"layer": 11, "name": "Emotional Maturity", "category": "Character"},
    {"layer": 12, "name": "Adaptability", "category": "Character"},
    {"layer": 13, "name": "Wisdom & Discernment", "category": "Character"},
    {"layer": 14, "name": "Resilience & Courage", "category": "Character"},
    {"layer": 15, "name": "Civics & Community", "category": "Character"},

    # Practical (10)
    {"layer": 16, "name": "Financial Literacy", "category": "Practical"},
    {"layer": 17, "name": "Entrepreneurship", "category": "Practical"},
    {"layer": 18, "name": "Creation & Making", "category": "Practical"},
    {"layer": 19, "name": "Physical Health", "category": "Practical"},
    {"layer": 20, "name": "Digital Intelligence", "category": "Practical"},
    {"layer": 21, "name": "Life Skills", "category": "Practical"},
    {"layer": 22, "name": "Learning How to Learn", "category": "Practical"},
    {"layer": 23, "name": "Work & Career", "category": "Practical"},
    {"layer": 24, "name": "Civic Contribution", "category": "Practical"},
    {"layer": 25, "name": "Technology & Innovation", "category": "Practical"},

    # Applied (5)
    {"layer": 26, "name": "Wealth Creation", "category": "Applied"},
    {"layer": 27, "name": "Influence & Impact", "category": "Applied"},
    {"layer": 28, "name": "Organizational Leadership", "category": "Applied"},
    {"layer": 29, "name": "Mentorship & Teaching", "category": "Applied"},
    {"layer": 30, "name": "Legacy & Contribution", "category": "Applied"},
]

# Define venture → layer mappings
VENTURE_LAYER_MAP = {
    "EDU-006": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 29],
    "EDU-001": [17, 26, 27],
    "EDU-002": [20, 25],
    "EDU-003": [22, 29],
    "EDU-005": [20, 22],
    "EDU-007": [22],
    "EDU-020": [17, 18, 20, 25],
    "EDU-039": [2, 11, 13],
    "EDU-040": [3],
    "HRMS-001": [16, 17, 26],
}

def create_academy_entities():
    """Create Academy layer entities in graph_entities table"""
    print("Creating Academy layer entities...")

    entities = []
    for layer in ACADEMY_LAYERS:
        entity = {
            "id": str(uuid.uuid4()),
            "name": f"Layer {layer['layer']}: {layer['name']}",
            "entity_type": "Academy_Layer",
            "description": f"Worldwidebro Academy - {layer['category']} layer",
            "metadata": {
                "layer_number": layer['layer'],
                "full_name": layer['name'],
                "category": layer['category'],
                "system": "Academy"
            },
            "venture_id": None,
            "extracted_at": datetime.utcnow().isoformat()
        }
        entities.append(entity)

    # Insert in batches
    for i in range(0, len(entities), 100):
        batch = entities[i:i+100]
        response = supabase.table("graph_entities").insert(batch).execute()
        print(f"  ✓ Created {len(batch)} entities (batch {i//100 + 1})")

    print(f"✅ Created {len(entities)} Academy layer entities")
    return entities

def create_academy_relationships():
    """Create relationships between Academy layers and ventures"""
    print("\nCreating Academy → Venture relationships...")

    relationships = []
    for venture_id, layer_nums in VENTURE_LAYER_MAP.items():
        for layer_num in layer_nums:
            layer = next(l for l in ACADEMY_LAYERS if l['layer'] == layer_num)
            rel = {
                "id": str(uuid.uuid4()),
                "source_entity": f"Layer {layer_num}: {layer['name']}",
                "target_entity": venture_id,
                "relationship_type": "powers_venture",
                "weight": 1.0,
                "metadata": {
                    "layer_number": layer_num,
                    "venture_id": venture_id,
                    "system": "Academy → Ventures"
                }
            }
            relationships.append(rel)

    # Insert relationships
    for i in range(0, len(relationships), 100):
        batch = relationships[i:i+100]
        response = supabase.table("graph_relationships").insert(batch).execute()
        print(f"  ✓ Created {len(batch)} relationships (batch {i//100 + 1})")

    print(f"✅ Created {len(relationships)} Academy → Venture relationships")
    return relationships

def main():
    print("=" * 60)
    print("WIRING WORLDWIDEBRO ACADEMY INTO KNOWLEDGE GRAPH")
    print("=" * 60)

    try:
        create_academy_entities()
        create_academy_relationships()

        print("\n" + "=" * 60)
        print("✅ ACADEMY WIRED INTO KNOWLEDGE GRAPH")
        print("=" * 60)
        print("\nNext: Run obsidian_graph_sync.py to update visualization")

    except Exception as e:
        print(f"❌ Error: {e}")
        raise

if __name__ == "__main__":
    main()
