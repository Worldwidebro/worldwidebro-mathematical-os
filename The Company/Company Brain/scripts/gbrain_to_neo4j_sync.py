#!/usr/bin/env python3
"""
gbrain → Neo4j Relationship Extraction & Sync

Indexes venture documents in gbrain, extracts entities and relationships,
and syncs to Neo4j knowledge graph.

Flow:
1. Query gbrain for all indexed venture documents
2. Extract entities (Person, Organization, Venture, etc.)
3. Extract relationships (FOUNDED_BY, INVESTED_IN, ADVISES, etc.)
4. Merge into Neo4j with confidence scores
5. Update timestamps for incremental sync

Author: Company Brain Automation
"""

import os
import re
import json
from typing import Optional, Dict, List, Any, Tuple
from datetime import datetime
from dataclasses import dataclass, asdict

from neo4j import GraphDatabase
import httpx
from dotenv import load_dotenv

load_dotenv()

# Configuration
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://100.87.214.70:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "changeme")

GBRAIN_API = os.getenv("GBRAIN_API", "http://localhost:8000")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


@dataclass
class Entity:
    """Extracted entity from document"""

    type: str  # PERSON, ORGANIZATION, VENTURE, etc.
    name: str
    properties: Dict[str, Any]
    confidence: float
    source_venture: str
    section: str


@dataclass
class Relationship:
    """Extracted relationship between entities"""

    source: str
    target: str
    relationship_type: str
    properties: Dict[str, Any]
    confidence: float
    source_venture: str


class GbrainNeo4jSync:
    """Syncs gbrain indexed documents to Neo4j knowledge graph"""

    def __init__(self):
        self.neo4j_driver = GraphDatabase.driver(
            NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD)
        )
        self.http_client = httpx.Client(timeout=30.0)

        # Extraction patterns
        self.patterns = {
            "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "phone": r"\b\+?1?\s*\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}\b",
            "money": r"\$[\d,]+(?:\.\d{2})?|\b[0-9]+(?:K|M|B)\b",
            "date": r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},?\s+\d{4}|\d{4}-\d{2}-\d{2}\b",
        }

    def close(self):
        """Clean up resources"""
        self.neo4j_driver.close()
        self.http_client.close()

    async def sync_all_ventures(self) -> Dict[str, Any]:
        """
        Sync all ventures: gbrain → Neo4j

        Returns:
            {
                "ventures_synced": int,
                "entities_extracted": int,
                "entities_merged": int,
                "relationships_extracted": int,
                "relationships_merged": int,
                "errors": []
            }
        """

        stats = {
            "ventures_synced": 0,
            "entities_extracted": 0,
            "entities_merged": 0,
            "relationships_extracted": 0,
            "relationships_merged": 0,
            "errors": [],
        }

        # Get all ventures from gbrain
        try:
            response = self.http_client.get(
                f"{GBRAIN_API}/ventures", params={"limit": 1000}
            )
            if response.status_code != 200:
                stats["errors"].append(f"Failed to fetch ventures: {response.text}")
                return stats

            ventures = response.json().get("ventures", [])

        except Exception as e:
            stats["errors"].append(f"Error fetching ventures: {e}")
            return stats

        # Process each venture
        for venture_id in ventures:
            try:
                venture_stats = self._sync_venture(venture_id)
                for key, value in venture_stats.items():
                    if key != "errors":
                        stats[key] += value
                    else:
                        stats["errors"].extend(value)

                stats["ventures_synced"] += 1

            except Exception as e:
                stats["errors"].append(f"Error syncing {venture_id}: {e}")

        return stats

    def _sync_venture(self, venture_id: str) -> Dict[str, Any]:
        """Sync single venture: extract → merge"""

        stats = {
            "entities_extracted": 0,
            "entities_merged": 0,
            "relationships_extracted": 0,
            "relationships_merged": 0,
            "errors": [],
        }

        try:
            # Get venture documents from gbrain
            response = self.http_client.get(f"{GBRAIN_API}/ventures/{venture_id}")
            if response.status_code != 200:
                stats["errors"].append(
                    f"{venture_id}: Failed to fetch documents ({response.status_code})"
                )
                return stats

            documents = response.json().get("documents", [])

        except Exception as e:
            stats["errors"].append(f"{venture_id}: Error fetching documents: {e}")
            return stats

        # Extract entities and relationships from documents
        entities: List[Entity] = []
        relationships: List[Relationship] = []

        for doc in documents:
            doc_entities, doc_relationships = self._extract_from_document(
                venture_id, doc
            )
            entities.extend(doc_entities)
            relationships.extend(doc_relationships)

        stats["entities_extracted"] = len(entities)
        stats["relationships_extracted"] = len(relationships)

        # Merge into Neo4j
        for entity in entities:
            try:
                self._merge_entity(entity)
                stats["entities_merged"] += 1
            except Exception as e:
                stats["errors"].append(f"{venture_id}: Error merging entity: {e}")

        for rel in relationships:
            try:
                self._merge_relationship(rel)
                stats["relationships_merged"] += 1
            except Exception as e:
                stats["errors"].append(f"{venture_id}: Error merging relationship: {e}")

        # Update venture sync timestamp
        self._update_venture_sync_timestamp(venture_id)

        return stats

    def _extract_from_document(
        self, venture_id: str, document: Dict
    ) -> Tuple[List[Entity], List[Relationship]]:
        """
        Extract entities and relationships from a single document

        Document structure:
        {
            "id": "doc_id",
            "section": "01_IDENTITY",
            "content": "...",
            "extracted_entities": {...}  # from gbrain
        }
        """

        entities: List[Entity] = []
        relationships: List[Relationship] = []

        content = document.get("content", "")
        section = document.get("section", "unknown")
        extracted = document.get("extracted_entities", {})

        # Use gbrain's pre-extracted entities first
        for entity_type, entity_list in extracted.items():
            for entity_data in entity_list:
                entity = self._parse_entity(
                    entity_type, entity_data, venture_id, section
                )
                if entity:
                    entities.append(entity)

        # Pattern-based extraction for additional context
        for email_match in re.finditer(self.patterns["email"], content):
            email = email_match.group()
            # Try to infer person from context
            entities.append(
                Entity(
                    type="EMAIL",
                    name=email,
                    properties={"email": email},
                    confidence=0.7,
                    source_venture=venture_id,
                    section=section,
                )
            )

        # Extract relationships from extracted entities
        relationships = self._extract_relationships(entities, venture_id, section)

        return entities, relationships

    def _parse_entity(
        self, entity_type: str, entity_data: Dict, venture_id: str, section: str
    ) -> Optional[Entity]:
        """Parse gbrain-extracted entity"""

        entity_map = {
            "person": "PERSON",
            "organization": "ORGANIZATION",
            "venture": "VENTURE",
            "investment": "INVESTMENT",
            "location": "LOCATION",
        }

        neo4j_type = entity_map.get(entity_type.lower())
        if not neo4j_type:
            return None

        return Entity(
            type=neo4j_type,
            name=entity_data.get("name", ""),
            properties=entity_data.get("properties", {}),
            confidence=entity_data.get("confidence", 0.8),
            source_venture=venture_id,
            section=section,
        )

    def _extract_relationships(
        self, entities: List[Entity], venture_id: str, section: str
    ) -> List[Relationship]:
        """Extract relationships between entities"""

        relationships = []

        # Relationship patterns based on section
        if section in ["01_IDENTITY", "02_FOUNDERS"]:
            # Look for founder/founder relationships
            people = [e for e in entities if e.type == "PERSON"]
            if len(people) >= 2:
                for i, person1 in enumerate(people):
                    for person2 in people[i + 1 :]:
                        relationships.append(
                            Relationship(
                                source=person1.name,
                                target=person2.name,
                                relationship_type="CO_FOUNDER",
                                properties={"section": section},
                                confidence=0.7,
                                source_venture=venture_id,
                            )
                        )

        if section in ["05_INVESTORS", "06_CAPITAL"]:
            # Look for investment relationships
            investors = [e for e in entities if e.type == "ORGANIZATION"]
            for investor in investors:
                relationships.append(
                    Relationship(
                        source=investor.name,
                        target=venture_id,
                        relationship_type="INVESTED_IN",
                        properties={"section": section},
                        confidence=0.8,
                        source_venture=venture_id,
                    )
                )

        if section in ["08_ADVISORS", "09_BOARD"]:
            # Look for advisory relationships
            advisors = [e for e in entities if e.type == "PERSON"]
            for advisor in advisors:
                relationships.append(
                    Relationship(
                        source=advisor.name,
                        target=venture_id,
                        relationship_type="ADVISES",
                        properties={"section": section, "role": "ADVISOR"},
                        confidence=0.8,
                        source_venture=venture_id,
                    )
                )

        return relationships

    def _merge_entity(self, entity: Entity):
        """Merge entity into Neo4j"""

        query = f"""
        MERGE (e:{entity.type} {{name: $name}})
        SET e += $properties,
            e.confidence = $confidence,
            e.last_synced = $timestamp,
            e.source_ventures = CASE WHEN e.source_ventures IS NULL
                                  THEN [$venture]
                                  ELSE apoc.coll.union(e.source_ventures, [$venture])
                                  END
        RETURN e
        """

        with self.neo4j_driver.session() as session:
            session.run(
                query,
                name=entity.name,
                properties=entity.properties,
                confidence=entity.confidence,
                venture=entity.source_venture,
                timestamp=datetime.utcnow().isoformat(),
            )

    def _merge_relationship(self, rel: Relationship):
        """Merge relationship into Neo4j"""

        query = f"""
        MATCH (source {{name: $source}})
        MATCH (target {{name: $target}})
        MERGE (source)-[r:{rel.relationship_type}]->(target)
        SET r += $properties,
            r.confidence = $confidence,
            r.last_synced = $timestamp
        RETURN r
        """

        with self.neo4j_driver.session() as session:
            try:
                session.run(
                    query,
                    source=rel.source,
                    target=rel.target,
                    properties=rel.properties,
                    confidence=rel.confidence,
                    timestamp=datetime.utcnow().isoformat(),
                )
            except Exception as e:
                # Nodes may not exist yet; that's okay
                print(f"Skipping relationship {rel.source}->{rel.target}: {e}")

    def _update_venture_sync_timestamp(self, venture_id: str):
        """Update last sync timestamp for venture"""

        query = """
        MATCH (v:VENTURE {id: $venture_id})
        SET v.last_gbrain_sync = $timestamp
        """

        with self.neo4j_driver.session() as session:
            session.run(
                query, venture_id=venture_id, timestamp=datetime.utcnow().isoformat()
            )


def main():
    """Run full sync"""
    import asyncio

    sync = GbrainNeo4jSync()

    try:
        print("Starting gbrain → Neo4j sync...")
        stats = asyncio.run(sync.sync_all_ventures())

        print("\n=== Sync Results ===")
        print(f"Ventures synced: {stats['ventures_synced']}")
        print(f"Entities extracted: {stats['entities_extracted']}")
        print(f"Entities merged: {stats['entities_merged']}")
        print(f"Relationships extracted: {stats['relationships_extracted']}")
        print(f"Relationships merged: {stats['relationships_merged']}")

        if stats["errors"]:
            print(f"\n{len(stats['errors'])} errors:")
            for error in stats["errors"][:10]:  # Show first 10
                print(f"  - {error}")

    finally:
        sync.close()


if __name__ == "__main__":
    main()
