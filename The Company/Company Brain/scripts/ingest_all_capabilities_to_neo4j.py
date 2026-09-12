#!/usr/bin/env python3
"""
Ingest All Capabilities (Business & Technical) into Neo4j
Creates:
- (:Capability {id, name, category, importance, agents})
- (:Repository)-[:IMPLEMENTS]->(:Capability)
- (:Agent)-[:PROVIDES]->(:Capability)
"""

import yaml
import os
from pathlib import Path
from neo4j import GraphDatabase

WORKSPACE = Path("/Users/acebless/Documents/The Company/Company Brain")
CAPS_FILE = WORKSPACE / "_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml"

NEO4J_URI = "bolt://100.87.214.70:7687"
pwd = os.environ.get("NEO4J_PASSWORD", "changeme")
NEO4J_AUTH = ("neo4j", pwd)

def main():
    print(f"Reading capabilities from {CAPS_FILE}...")
    with open(CAPS_FILE) as f:
        data = yaml.safe_load(f)

    biz_caps = data.get("business_capabilities", {})
    tech_caps = data.get("technical_capabilities", {})
    print(f"Found {len(biz_caps)} business capabilities and {len(tech_caps)} technical capabilities.")

    driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
    with driver.session() as session:
        # Ingest business capabilities
        for cid, cinfo in biz_caps.items():
            name = cinfo.get("name", cid)
            cat = cinfo.get("category", "")
            imp = cinfo.get("importance", "")
            agent = str(cinfo.get("agents", ""))
            repo_ids = cinfo.get("implemented_by_repo_ids", [])

            session.run("""
                MERGE (c:Capability {id: $cid})
                SET c.name = $name,
                    c.category = $category,
                    c.importance = $importance,
                    c.type = 'BUSINESS',
                    c.agent = $agent
                WITH c
                UNWIND $repo_ids AS rid
                MATCH (r:Repository {id: rid})
                MERGE (r)-[:IMPLEMENTS]->(c)
            """, cid=cid, name=name, category=cat, importance=imp, agent=agent, repo_ids=repo_ids)

        # Ingest technical capabilities
        for cid, cinfo in tech_caps.items():
            if isinstance(cinfo, dict):
                name = cinfo.get("name", cid)
                repo_count = cinfo.get("repo_count", 0)
                primary_repo = cinfo.get("primary_repo", "")
            else:
                name = str(cid)
                repo_count = 0
                primary_repo = ""

            session.run("""
                MERGE (c:Capability {id: $cid})
                SET c.name = $name,
                    c.type = 'TECHNICAL',
                    c.repo_count = $repo_count
                WITH c
                WHERE $primary_repo <> ''
                MATCH (r:Repository {id: $primary_repo})
                MERGE (r)-[:IMPLEMENTS]->(c)
            """, cid=str(cid), name=str(name), repo_count=repo_count, primary_repo=primary_repo)

        # Count
        cap_count = session.run("MATCH (c:Capability) RETURN count(c) as cnt").single()["cnt"]
        impl_edges = session.run("MATCH ()-[r:IMPLEMENTS]->() RETURN count(r) as cnt").single()["cnt"]
        print("\n=======================================================")
        print(f"Neo4j Capability Graph Ingestion Complete:")
        print(f"  Total Capabilities: {cap_count}")
        print(f"  IMPLEMENTS Edges:   {impl_edges}")
        print("=======================================================")

    driver.close()

if __name__ == "__main__":
    main()
