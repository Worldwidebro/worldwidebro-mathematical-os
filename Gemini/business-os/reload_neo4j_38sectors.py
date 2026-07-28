#!/usr/bin/env python3
"""
Neo4j Reload Script for Worldwidebro Holdings AI OS
Reads the master AUTO-ALIGNMENT-712.json registry to reload/sync 
the 38 sectors and 884 ventures with their repository relationships.
"""

import os
import json
import sys
from pathlib import Path
from neo4j import GraphDatabase

# Local Configuration
ALIGNMENT_FILE = "/Users/acebless/Documents/.claude/worktrees/agent-ac65ac3629807bab2/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/STRATEGY_LAYERS/WORLDWIDEBRO-OS/07_AUTOMATIONS/Configs/AUTO-ALIGNMENT-712.json"
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "ventures2026")

class Neo4jReloader:
    def __init__(self, alignment_path: str, uri: str, user: str, password: str):
        self.alignment_path = Path(alignment_path)
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.upserted_ventures = 0
        self.upserted_repos = 0
        self.errors = 0

    def load_alignment_data(self) -> dict:
        """Loads and parses the master alignment file."""
        if not self.alignment_path.exists():
            print(f"❌ Master alignment file not found at: {self.alignment_path}")
            sys.exit(1)
        with open(self.alignment_path, 'r') as f:
            return json.load(f)

    def initialize_schema(self, session):
        """Creates unique constraints to prevent duplicate node creation."""
        print("🧱 Initializing Neo4j Constraints...")
        # Constraint for Venture
        session.run("CREATE CONSTRAINT venture_id IF NOT EXISTS FOR (v:Venture) REQUIRE v.id IS UNIQUE")
        # Constraint for Repository
        session.run("CREATE CONSTRAINT repository_url IF NOT EXISTS FOR (r:Repository) REQUIRE r.url IS UNIQUE")
        print("✅ Constraints initialized.")

    def run_reload(self):
        """Executes the ingestion pipeline."""
        data = self.load_alignment_data()
        alignments = data.get("alignments", [])
        print(f"📦 Loaded {len(alignments)} venture records from alignment index.")

        with self.driver.session() as session:
            self.initialize_schema(session)

            print("🔄 Ingesting ventures and mapping repositories...")
            for idx, item in enumerate(alignments):
                v_id_full = item.get("venture_id", "")
                if not v_id_full:
                    continue

                # Parse short Venture ID (e.g., 'FIN-001' from 'FIN-001-GenixBank-Lite')
                parts = v_id_full.split("-")
                if len(parts) >= 2:
                    v_short_id = f"{parts[0]}-{parts[1]}"
                else:
                    v_short_id = v_id_full

                v_name = item.get("venture_name", v_id_full)
                v_sector = item.get("sector", "Unknown")
                v_uuid = item.get("uuid", "")
                v_repo_url = item.get("owned_repo_url", "")

                try:
                    # 1. Merge the Venture Node
                    cypher_venture = """
                    MERGE (v:Venture {id: $id})
                    SET
                      v.name = $name,
                      v.sector = $sector,
                      v.uuid = $uuid,
                      v.status = $status
                    RETURN v
                    """
                    # Determine active state for core targets
                    is_active = any(active_tag in v_short_id.lower() for active_tag in [
                        'con-001', 'lt-005', 'ops-staff-001', 'ec-001', 'ec-112', 're-001', 
                        'fin-006', 'fin-009', 'fin-021', 'fin-033'
                    ])
                    status = "active" if is_active else "pending"

                    session.run(
                        cypher_venture,
                        id=v_short_id,
                        name=v_name,
                        sector=v_sector,
                        uuid=v_uuid,
                        status=status
                    )
                    self.upserted_ventures += 1

                    # 2. Merge primary owned repository and link it
                    if v_repo_url:
                        repo_name = v_repo_url.split("/")[-1]
                        cypher_repo = """
                        MERGE (r:Repository {url: $url})
                        SET r.name = $name
                        WITH r
                        MATCH (v:Venture {id: $venture_id})
                        MERGE (v)-[:HAS_REPOSITORY {type: 'primary'}]->(r)
                        """
                        session.run(
                            cypher_repo,
                            url=v_repo_url,
                            name=repo_name,
                            venture_id=v_short_id
                        )
                        self.upserted_repos += 1

                    # 3. Merge secondary auto-matched repositories
                    for match in item.get("auto_matched_repos", []):
                        m_url = match.get("url")
                        m_name = match.get("name")
                        if m_url and m_url != v_repo_url:
                            cypher_match = """
                            MERGE (r:Repository {url: $url})
                            SET r.name = $name
                            WITH r
                            MATCH (v:Venture {id: $venture_id})
                            MERGE (v)-[:HAS_REPOSITORY {type: 'matched', score: $score}]->(r)
                            """
                            session.run(
                                cypher_match,
                                url=m_url,
                                name=m_name,
                                venture_id=v_short_id,
                                score=match.get("score", 0.5)
                            )
                            self.upserted_repos += 1

                except Exception as e:
                    print(f"❌ Error ingesting {v_short_id}: {e}")
                    self.errors += 1

                if idx > 0 and idx % 100 == 0:
                    print(f"   Progress: {idx}/{len(alignments)} ventures processed.")

        print("\nIngestion Completed Summary:")
        print(f"   ✓ Total Ventures Synced: {self.upserted_ventures}")
        print(f"   ✓ Total Repos Linked: {self.upserted_repos}")
        print(f"   ✓ Total Errors: {self.errors}")

    def close(self):
        self.driver.close()

if __name__ == "__main__":
    reloader = Neo4jReloader(ALIGNMENT_FILE, NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)
    try:
        reloader.run_reload()
    finally:
        reloader.close()
