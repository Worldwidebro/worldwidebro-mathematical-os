#!/usr/bin/env python3
"""
Insert Repo entities and Repo→Venture edges into Supabase knowledge graph.
TASK 3: Add Repo entities to Supabase
"""

import json
import subprocess

SUPABASE_URL = "https://cyhzilqldouzgynacqpe.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN5aHppbHFsZG91emd5bmFjcXBlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NDY2OTQwOCwiZXhwIjoyMDgwMjQ1NDA4fQ.1M6V3fR9rNxonIJvtNkV4isrZK9VIvy3J-gNLJGMp2k"

REPOS = {
    "civilization-os": {
        "owner": "Worldwidebro",
        "type": "core-orchestration",
        "description": "Central OS managing all 687 ventures, agent routing, and knowledge graph"
    },
    "venture-hub": {
        "owner": "Worldwidebro",
        "type": "ui-dashboard",
        "description": "Dashboard UI for venture management, analytics, and operational control"
    },
    "mission-control": {
        "owner": "Worldwidebro",
        "type": "agent-coordination",
        "description": "Agent task coordination, state management, and execution monitoring"
    },
    "iza-os-rag-system": {
        "owner": "Worldwidebro",
        "type": "knowledge-system",
        "description": "RAG system for knowledge graph ingestion, semantic search, and context retrieval"
    },
    "the-office": {
        "owner": "Worldwidebro",
        "type": "communication-hub",
        "description": "Central communication hub for Slack, email, and real-time notifications"
    },
    "venture-factory-core": {
        "owner": "Worldwidebro",
        "type": "venture-engine",
        "description": "Core engine for generating, validating, and launching new ventures"
    },
    "bw-001-up-next-web": {
        "owner": "Worldwidebro",
        "type": "venture-product",
        "description": "Up Next web application - first venture product on the platform"
    }
}

def insert_repos():
    print("[*] Inserting 7 Repo entities into graph_entities...")
    inserted = 0
    for repo_id, repo_data in REPOS.items():
        payload = {
            "name": repo_id,
            "entity_type": "Repo",
            "description": repo_data["description"],
            "metadata": {"owner": repo_data["owner"], "type": repo_data["type"]},
            "venture_id": None
        }
        result = subprocess.run(
            ["curl", "-s", "-X", "POST", f"{SUPABASE_URL}/rest/v1/graph_entities",
             "-H", f"apikey: {SUPABASE_KEY}", "-H", "Content-Type: application/json",
             "-d", json.dumps(payload)],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            inserted += 1
            print(f"  ✅ {repo_id}")
    print(f"[✓] Inserted {inserted}/7 Repo entities\n")

def insert_edges():
    print("[*] Building Repo→Venture edges from PRIVATE-REPOS-ACCESS-CONTROL.csv...")
    repos_to_ventures = {}
    try:
        with open("/Users/acebless/Documents/PRIVATE-REPOS-ACCESS-CONTROL.csv", "r") as f:
            for i, line in enumerate(f.readlines()[1:], 1):
                parts = line.strip().split(",")
                if len(parts) >= 3:
                    repo_id = parts[0].strip()
                    ventures_served = parts[2].strip()
                    if ventures_served and ventures_served != "":
                        for venture_id in ventures_served.split("|"):
                            venture_id = venture_id.strip()
                            if venture_id:
                                repos_to_ventures.setdefault(repo_id, []).append(venture_id)
    except FileNotFoundError:
        print("  ⚠️  PRIVATE-REPOS-ACCESS-CONTROL.csv not found\n")
        return

    edge_count = 0
    for repo_id, venture_ids in repos_to_ventures.items():
        for venture_id in venture_ids:
            sql = f"""
            INSERT INTO graph_relationships (source_entity_id, target_entity_id, relationship_type, created_at)
            VALUES ('{repo_id}', '{venture_id}', 'serves', NOW())
            ON CONFLICT (source_entity_id, target_entity_id, relationship_type) DO NOTHING;
            """
            result = subprocess.run(
                ["curl", "-s", "-X", "POST", f"{SUPABASE_URL}/rest/v1/rpc/exec_sql",
                 "-H", f"apikey: {SUPABASE_KEY}", "-H", "Content-Type: application/json",
                 "-d", json.dumps({"sql": sql})],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                edge_count += 1

    print(f"[✓] Inserted {edge_count} Repo→Venture edges\n")

if __name__ == "__main__":
    print("[TASK 3] Inserting Repo entities and edges to Supabase\n")
    insert_repos()
    insert_edges()
    print("[✓] TASK 3 complete - Repos now in knowledge graph")
