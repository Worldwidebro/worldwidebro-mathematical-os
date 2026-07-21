#!/usr/bin/env python3
"""
Wire tags from REPOSITORY-REGISTRY.json into Neo4j.
MERGE each repo with monetization, software_type, opco, pricing.
"""

import json
from pathlib import Path
from neo4j import GraphDatabase

class Neo4jTagger:
    def __init__(self, registry_path: str, neo4j_uri: str = "bolt://localhost:7687", neo4j_user: str = "neo4j", neo4j_password: str = "ventures2026"):
        self.registry_path = Path(registry_path)
        self.driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))
        self.registry = self._load_registry()
        self.upserted = 0
        self.failed = 0

    def _load_registry(self) -> dict:
        with open(self.registry_path) as f:
            return json.load(f)

    def upsert_repo_tags(self):
        """MERGE all repos into Neo4j with tags."""
        repos = self.registry.get("repositories", [])
        print(f"🔄 Syncing {len(repos)} repos to Neo4j...\n")

        with self.driver.session() as session:
            for i, repo in enumerate(repos):
                if i % 100 == 0:
                    print(f"Progress: {i}/{len(repos)}")

                try:
                    self._upsert_repo(session, repo)
                    self.upserted += 1
                except Exception as e:
                    print(f"❌ Failed to upsert {repo.get('name')}: {e}")
                    self.failed += 1

        print(f"\n✅ Neo4j sync complete!")
        print(f"   Upserted: {self.upserted}")
        print(f"   Failed: {self.failed}")

    def _upsert_repo(self, session, repo: dict):
        """MERGE a single repo with tags."""
        cypher = """
        MERGE (r:Repository {name: $name})
        SET
          r.url = $url,
          r.monetization = $monetization,
          r.software_type = $software_type,
          r.opco = $opco,
          r.pricing = $pricing
        RETURN r
        """

        session.run(
            cypher,
            name=repo.get("name"),
            url=repo.get("url"),
            monetization=repo.get("monetization", "Unknown"),
            software_type=repo.get("software_type", "Unknown"),
            opco=repo.get("opco", "Unknown"),
            pricing=repo.get("pricing", "Unknown")
        )

    def close(self):
        self.driver.close()

if __name__ == "__main__":
    registry = Path("/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json")
    tagger = Neo4jTagger(str(registry))
    tagger.upsert_repo_tags()
    tagger.close()
