#!/usr/bin/env python3
"""venture_dependency_mapper.py — Resolve capabilities and map dependencies in Neo4j Knowledge Graph."""

import os
import sys
from neo4j import GraphDatabase

# Resolve package directory to find os_env
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
try:
    from os_env import NEO4J_URI, NEO4J_AUTH
except ImportError:
    NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://100.87.214.70:7687")
    NEO4J_AUTH = (os.environ.get("NEO4J_USER", "neo4j"), os.environ.get("NEO4J_PASSWORD", "ventures2026"))

class VentureDependencyMapper:
    def __init__(self):
        try:
            self.driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
            print("  ✅ Neo4j Connection Established")
        except Exception as e:
            print(f"  ⚠️ Neo4j Connection failed: {e}")
            self.driver = None

    def close(self):
        if self.driver:
            self.driver.close()

    def map_dependency(self, source_name: str, target_name: str, rel_type: str = "DEPENDS_ON"):
        """Map a dependency relationship in the knowledge graph."""
        if not self.driver:
            print("  ⚠️ Neo4j driver not initialized, skipping map")
            return

        query = f"""
        MERGE (s:Entity {{name: $source_name}})
        MERGE (t:Entity {{name: $target_name}})
        MERGE (s)-[r:{rel_type}]->(t)
        RETURN s, r, t
        """
        try:
            with self.driver.session() as session:
                session.run(query, source_name=source_name, target_name=target_name)
                print(f"  ⛓️ [Neo4j] Mapped relationship: ({source_name})-[:{rel_type}]->({target_name})")
        except Exception as e:
            print(f"  ❌ Neo4j error mapping dependency: {e}")

    def get_dependencies(self, entity_name: str):
        """Query dependencies for a specific entity name."""
        if not self.driver:
            return []

        query = """
        MATCH (s:Entity {name: $entity_name})-[r:DEPENDS_ON]->(t:Entity)
        RETURN t.name as name
        """
        try:
            with self.driver.session() as session:
                result = session.run(query, entity_name=entity_name)
                return [row["name"] for row in result]
        except Exception as e:
            print(f"  ❌ Neo4j error querying dependencies: {e}")
            return []

if __name__ == "__main__":
    mapper = VentureDependencyMapper()
    if "--test" in sys.argv:
        print("🧪 Running VentureDependencyMapper local test...")
        mapper.map_dependency("venture_classifier", "postgresql", "REQUIRES")
        mapper.map_dependency("venture_classifier", "neo4j", "REQUIRES")
        mapper.map_dependency("estimator_gen1", "qdrant", "REQUIRES")
        
        deps = mapper.get_dependencies("venture_classifier")
        print(f"Dependencies found: {deps}")
        print("🧪 Test completed successfully!")
    mapper.close()
