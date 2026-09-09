#!/usr/bin/env python3
"""
Sync gbrain indexed venture documents to Neo4j relationship graph.

When gbrain indexes venture documents, extract entities and relationships,
then sync them to Neo4j as nodes and edges.

Usage:
    python sync_gbrain_to_neo4j.py [--dry-run] [--verbose]
"""

import os
import sys
import json
import re
import hashlib
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Set

# External dependencies
try:
    from neo4j import GraphDatabase
    from neo4j.exceptions import Neo4jError
except ImportError:
    print("ERROR: neo4j-driver not installed. Install with: pip install neo4j")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class GBrainToNeo4jSync:
    """Sync gbrain documents to Neo4j knowledge graph."""

    def __init__(self, neo4j_uri: str = "bolt://localhost:7687", dry_run: bool = False, verbose: bool = False):
        self.neo4j_uri = neo4j_uri
        self.dry_run = dry_run
        self.verbose = verbose
        self.neo4j_driver = None

        # Stats tracking
        self.stats = {
            "ventures_indexed": 0,
            "people_extracted": 0,
            "organizations_extracted": 0,
            "relationships_created": 0,
            "errors": 0,
            "skipped": 0
        }

        if verbose:
            logger.setLevel(logging.DEBUG)

    def connect_neo4j(self):
        """Connect to Neo4j database."""
        try:
            neo4j_password = os.getenv("NEO4J_PASSWORD", "changeme")
            self.neo4j_driver = GraphDatabase.driver(
                self.neo4j_uri,
                auth=("neo4j", neo4j_password),
                encrypted=False
            )
            self.neo4j_driver.verify_connectivity()
            logger.info(f"Connected to Neo4j at {self.neo4j_uri}")
        except Exception as e:
            logger.error(f"Failed to connect to Neo4j: {e}")
            raise

    def close_neo4j(self):
        """Close Neo4j connection."""
        if self.neo4j_driver:
            self.neo4j_driver.close()

    def get_venture_documents(self) -> List[Dict]:
        """Get all indexed venture documents."""
        documents = []
        venture_dir = Path.home() / "Documents/The Company/Company Brain/BUSINESS-CAPITAL-DATA-ROOM"

        if not venture_dir.exists():
            logger.warning(f"Venture directory not found: {venture_dir}")
            return documents

        # Find all markdown files in venture folders
        for md_file in venture_dir.glob("**/[A-Z][A-Z]*-*/[A-Z0-9]*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract venture ID from path (e.g., OPS-001)
                parts = md_file.parts
                venture_id = None
                for part in parts:
                    if re.match(r'^[A-Z]+-\d+$', part):
                        venture_id = part
                        break

                if not venture_id:
                    continue

                documents.append({
                    "venture_id": venture_id,
                    "file": str(md_file),
                    "content": content,
                    "hash": hashlib.sha256(content.encode()).hexdigest()[:16]
                })
            except Exception as e:
                logger.warning(f"Failed to read {md_file}: {e}")
                self.stats["errors"] += 1

        logger.info(f"Found {len(documents)} venture documents")
        return documents

    def extract_entities(self, venture_id: str, content: str) -> Tuple[List[Dict], List[Dict], List[Tuple]]:
        """Extract people, organizations, and relationships."""
        people = []
        organizations = []
        relationships = []

        # Simple regex-based extraction
        founder_patterns = [
            r'(?:Founder|CEO|Founder & CEO)(?:\s*:\s*|\s+)([A-Z][a-z]+ [A-Z][a-z]+)',
            r'(?:by|with|led by)\s+([A-Z][a-z]+ [A-Z][a-z]+)'
        ]

        for pattern in founder_patterns:
            for match in re.finditer(pattern, content):
                name = match.group(1).strip()
                if name and len(name.split()) == 2:
                    person = {"name": name, "role": "founder"}
                    if person not in people:
                        people.append(person)
                        relationships.append((venture_id, "FOUNDED_BY", name))

        # Extract investor names
        investor_pattern = r'(?:Investor|Angel|VC)(?:\s*:\s*|\s+)([A-Z][a-z]+ [A-Z][a-z]+)'
        for match in re.finditer(investor_pattern, content):
            name = match.group(1).strip()
            if name and len(name.split()) == 2:
                person = {"name": name, "role": "investor"}
                if person not in people:
                    people.append(person)
                    relationships.append((venture_id, "INVESTED_IN", name))

        # Extract advisor names
        advisor_pattern = r'(?:Advisor|Adviser)(?:\s*:\s*|\s+)([A-Z][a-z]+ [A-Z][a-z]+)'
        for match in re.finditer(advisor_pattern, content):
            name = match.group(1).strip()
            if name and len(name.split()) == 2:
                person = {"name": name, "role": "advisor"}
                if person not in people:
                    people.append(person)
                    relationships.append((venture_id, "ADVISED_BY", name))

        return people, organizations, relationships

    def sync_venture(self, session, venture: Dict) -> bool:
        """Sync a single venture document to Neo4j."""
        venture_id = venture["venture_id"]
        content = venture["content"]

        try:
            if self.verbose:
                logger.debug(f"Syncing {venture_id}")

            people, orgs, rels = self.extract_entities(venture_id, content)

            if self.dry_run:
                logger.info(f"[DRY-RUN] {venture_id}: {len(people)} people, {len(orgs)} orgs, {len(rels)} relationships")
                return True

            # Create venture node
            session.run("""
                MERGE (v:Venture {id: $venture_id})
                SET v.indexed_by_gbrain = true,
                    v.last_synced = datetime(),
                    v.content_hash = $hash
            """, venture_id=venture_id, hash=venture["hash"])

            # Create person nodes and relationships
            for person in people:
                session.run("""
                    MERGE (p:Person {name: $name})
                    SET p.role = $role
                    WITH p
                    MATCH (v:Venture {id: $venture_id})
                    MERGE (p)-[r:WORKS_ON]->(v)
                    SET r.relationship_type = $relationship_type
                """, name=person["name"], role=person["role"],
                venture_id=venture_id, relationship_type=person["role"])

            self.stats["ventures_indexed"] += 1
            self.stats["people_extracted"] += len(people)
            self.stats["relationships_created"] += len(rels)

            return True

        except Exception as e:
            logger.error(f"Error syncing {venture_id}: {e}")
            self.stats["errors"] += 1
            return False

    def run(self):
        """Execute the sync."""
        try:
            self.connect_neo4j()
            documents = self.get_venture_documents()

            if not documents:
                logger.warning("No venture documents found")
                return

            with self.neo4j_driver.session() as session:
                for doc in documents:
                    self.sync_venture(session, doc)

            self.print_summary()

        finally:
            self.close_neo4j()

    def print_summary(self):
        """Print sync summary."""
        print("\n" + "="*60)
        print("Sync Complete:")
        print("="*60)
        print(f"Ventures indexed:        {self.stats['ventures_indexed']}")
        print(f"People extracted:        {self.stats['people_extracted']}")
        print(f"Organizations extracted: {self.stats['organizations_extracted']}")
        print(f"Relationships created:   {self.stats['relationships_created']}")
        print(f"Errors:                  {self.stats['errors']}")
        if self.dry_run:
            print("\n[DRY-RUN MODE - No data written to Neo4j]")
        print("="*60 + "\n")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Sync gbrain venture documents to Neo4j")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose logging")
    parser.add_argument("--uri", default="bolt://localhost:7687", help="Neo4j URI")

    args = parser.parse_args()
    sync = GBrainToNeo4jSync(neo4j_uri=args.uri, dry_run=args.dry_run, verbose=args.verbose)
    sync.run()


if __name__ == "__main__":
    main()
