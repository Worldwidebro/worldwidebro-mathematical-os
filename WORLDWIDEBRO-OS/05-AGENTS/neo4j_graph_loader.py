#!/usr/bin/env python3
"""Load org.yaml into Neo4j graph. Creates Hermes→Departments→OPCOs→Ventures→Agents."""

import sys
import yaml
from neo4j import GraphDatabase

import os

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "ventures2026")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def load_org(filepath: str):
    """Parse organization.yaml and load into Neo4j."""
    with open(filepath) as f:
        org = yaml.safe_load(f)

    with driver.session() as session:
        # Hermes node
        session.run("""
            MERGE (h:Hermes {id: 'hermes_001'})
            SET h.name = $name, h.title = $title, h.capital_threshold = $threshold
        """, {
            "name": "Hermes",
            "title": org["hermes"]["title"],
            "threshold": org["hermes"]["decision_authority"]["capital_threshold"],
        })

        # Departments
        for dept_key, dept_cfg in org.get("departments", {}).items():
            session.run("""
                MERGE (d:Department {id: $id})
                SET d.code = $code, d.name = $name
                WITH d MATCH (h:Hermes) MERGE (h)-[:COMMANDS]->(d)
            """, {
                "id": f"dept_{dept_key}",
                "code": dept_cfg.get("code"),
                "name": dept_cfg.get("name"),
            })

            # Agents under department
            for team in dept_cfg.get("teams", []):
                for agent in team.get("agents", []):
                    session.run("""
                        MERGE (a:Agent {id: $id})
                        SET a.name = $name, a.team = $team
                        WITH a MATCH (d:Department {id: $dept_id})
                        MERGE (d)-[:EMPLOYS]->(a)
                    """, {
                        "id": agent.get("id"),
                        "name": agent.get("name"),
                        "team": team.get("name"),
                        "dept_id": f"dept_{dept_key}",
                    })

    print("✅ Graph loaded. Query: MATCH (h:Hermes)-[:COMMANDS]->(d) RETURN h, d;")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 neo4j_graph_loader.py org.yaml")
        sys.exit(1)
    try:
        load_org(sys.argv[1])
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        driver.close()
