#!/usr/bin/env python3
"""
Company Brain Graph-Native Ingestion Pipeline
Convert YAML registries → Neo4j graph-native architecture
Authority: Phase 2 Graph-Native Migration
"""

import asyncio
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml
from neo4j import AsyncDriver, AsyncSession, Record
from neo4j import asyncio as neo4j_async


class GraphIngestionPipeline:
    """Orchestrates YAML → Neo4j migration with provenance tracking and contradiction detection."""

    def __init__(self, neo4j_uri: str, neo4j_user: str, neo4j_password: str):
        """Initialize Neo4j driver."""
        self.driver: AsyncDriver = neo4j_async.AsyncDriver(
            neo4j_uri, auth=(neo4j_user, neo4j_password)
        )
        self.entities_created = 0
        self.entities_updated = 0
        self.contradictions_detected = 0
        self.audit_events: List[Dict[str, Any]] = []

    async def close(self) -> None:
        """Close Neo4j connection."""
        await self.driver.close()

    def sha256(self, data: str) -> str:
        """Compute SHA256 hash for provenance tracking."""
        return hashlib.sha256(data.encode()).hexdigest()

    async def create_source_node(
        self, session: AsyncSession, title: str, path: str, entity_type: str
    ) -> str:
        """Create (:Source) node and return SHA256."""
        file_content = Path(path).read_text()
        sha256 = self.sha256(file_content)

        query = """
        MERGE (s:Source {sha256: $sha256})
        ON CREATE SET
            s.title = $title,
            s.type = $entity_type,
            s.date = datetime(),
            s.url = $path,
            s.raw_path = $path,
            s.metadata = $metadata
        RETURN s.sha256 AS sha256
        """

        result = await session.run(
            query,
            {
                "sha256": sha256,
                "title": title,
                "entity_type": entity_type,
                "path": path,
                "metadata": json.dumps({"format": "yaml"}),
            },
        )

        record = await result.single()
        return record["sha256"] if record else sha256

    async def merge_sector(
        self, session: AsyncSession, entity: Dict[str, Any], source_sha: str
    ) -> Optional[Record]:
        """Merge sector entity into graph."""
        query = """
        MERGE (sector:Entity:Sector {entity_id: $entity_id})
        ON CREATE SET
            sector.name = $name,
            sector.type = "Sector",
            sector.confidence = 0.8,
            sector.contested = false,
            sector.needs_review = false,
            sector.source_count = 1,
            sector.created = datetime(),
            sector.updated = datetime(),
            sector.description = $description,
            sector.sector_id = $sector_id
        ON MATCH SET
            sector.updated = datetime(),
            sector.source_count = sector.source_count + 1,
            sector.needs_review = CASE WHEN sector.source_count < 2 THEN true ELSE false END

        MERGE (source:Source {sha256: $source_sha256})
        MERGE (sector)-[:DERIVED_FROM]->(source)

        RETURN sector.entity_id AS id, sector.source_count AS sources,
               CASE WHEN sector.source_count = 1 THEN "created" ELSE "updated" END AS action
        """

        result = await session.run(
            query,
            {
                "entity_id": entity.get("entity_id"),
                "name": entity.get("name"),
                "description": entity.get("description", ""),
                "sector_id": entity.get("sector_id"),
                "source_sha256": source_sha,
            },
        )

        return await result.single()

    async def merge_venture(
        self, session: AsyncSession, entity: Dict[str, Any], source_sha: str
    ) -> Optional[Record]:
        """Merge venture entity into graph."""
        query = """
        MERGE (venture:Entity:Venture {entity_id: $entity_id})
        ON CREATE SET
            venture.name = $name,
            venture.type = "Venture",
            venture.confidence = 0.8,
            venture.contested = false,
            venture.needs_review = false,
            venture.source_count = 1,
            venture.created = datetime(),
            venture.updated = datetime(),
            venture.ref_id = $ref_id,
            venture.sector = $sector,
            venture.status = $status
        ON MATCH SET
            venture.updated = datetime(),
            venture.source_count = venture.source_count + 1,
            venture.needs_review = CASE WHEN venture.source_count < 2 THEN true ELSE false END

        MERGE (source:Source {sha256: $source_sha256})
        MERGE (venture)-[:DERIVED_FROM]->(source)

        RETURN venture.entity_id AS id, venture.source_count AS sources,
               CASE WHEN venture.source_count = 1 THEN "created" ELSE "updated" END AS action
        """

        result = await session.run(
            query,
            {
                "entity_id": entity.get("entity_id"),
                "name": entity.get("name"),
                "ref_id": entity.get("ref_id"),
                "sector": entity.get("sector"),
                "status": entity.get("status", "unknown"),
                "source_sha256": source_sha,
            },
        )

        return await result.single()

    async def verify_integrity_gates(self, session: AsyncSession) -> Dict[str, int]:
        """Run all integrity gates after bulk ingestion."""
        gates = {}

        # Gate 1: Dangling references
        result = await session.run(
            "MATCH (s:Source)-[r:MENTIONS]->(e) WHERE NOT e:Entity RETURN COUNT(*) AS count"
        )
        record = await result.single()
        gates["dangling_references"] = record["count"] if record else 0

        # Gate 2: Provenance completeness
        result = await session.run(
            "MATCH (e:Entity) WHERE NOT (e)-[:DERIVED_FROM]->(:Source) RETURN COUNT(*) AS count"
        )
        record = await result.single()
        gates["missing_provenance"] = record["count"] if record else 0

        # Gate 3: Contradiction consistency
        result = await session.run(
            "MATCH (e:Entity)-[c:CONTRADICTS]->() WHERE NOT e.contested RETURN COUNT(*) AS count"
        )
        record = await result.single()
        gates["inconsistent_contradictions"] = record["count"] if record else 0

        # Gate 4: Orphan detection
        result = await session.run(
            "MATCH (e:Entity) WHERE NOT ()-[:RELATES|:MENTIONS|:SUPPORTS|:DEPENDS_ON|:USES]->(e) RETURN COUNT(*) AS count"
        )
        record = await result.single()
        gates["isolated_entities"] = record["count"] if record else 0

        return gates

    async def ingest_yaml_registry(
        self, yaml_path: str, entity_type: str, merger_func
    ) -> Dict[str, Any]:
        """Ingest YAML registry file into Neo4j."""
        async with await self.driver.session() as session:
            # Create source node
            source_sha = await self.create_source_node(
                session, f"{Path(yaml_path).name}", yaml_path, entity_type
            )

            # Load YAML
            yaml_data = yaml.safe_load(Path(yaml_path).read_text())
            entities = yaml_data.get("entities", []) if isinstance(yaml_data, dict) else []

            # Merge each entity
            created = 0
            updated = 0
            for entity in entities:
                result = await merger_func(session, entity, source_sha)
                if result:
                    if result["action"] == "created":
                        created += 1
                    else:
                        updated += 1

            self.entities_created += created
            self.entities_updated += updated

            # Verify gates
            gates = await self.verify_integrity_gates(session)

            # Log event
            event = {
                "timestamp": datetime.now().isoformat(),
                "action": "ingest_registry",
                "entity_type": entity_type,
                "source": Path(yaml_path).name,
                "source_sha": source_sha,
                "entities_created": created,
                "entities_updated": updated,
                "integrity_gates": gates,
            }
            self.audit_events.append(event)

            return event

    async def run_migration(self, registries: Dict[str, tuple]) -> Dict[str, Any]:
        """Execute full migration pipeline.

        Args:
            registries: {entity_type: (yaml_path, merger_func)}
        """
        print("🚀 Starting Phase 2 Graph-Native Migration...")

        for entity_type, (yaml_path, merger_func) in registries.items():
            print(f"\n📦 Ingesting {entity_type}...")
            result = await self.ingest_yaml_registry(yaml_path, entity_type, merger_func)
            print(
                f"  ✅ Created: {result['entities_created']}, "
                f"Updated: {result['entities_updated']}"
            )
            print(f"  🔍 Integrity gates: {result['integrity_gates']}")

        # Final report
        report = {
            "timestamp": datetime.now().isoformat(),
            "status": "COMPLETE",
            "total_entities_created": self.entities_created,
            "total_entities_updated": self.entities_updated,
            "total_contradictions": self.contradictions_detected,
            "audit_events": self.audit_events,
        }

        print("\n" + "=" * 80)
        print("📊 MIGRATION COMPLETE")
        print("=" * 80)
        print(json.dumps(report, indent=2))

        return report


async def main():
    """Example usage: migrate key registries."""
    # Neo4j connection (from CLAUDE.md)
    neo4j_uri = "bolt://100.87.214.70:7687"
    neo4j_user = "neo4j"
    neo4j_password = "changeme"  # TODO: Use Bitwarden

    # Initialize pipeline
    pipeline = GraphIngestionPipeline(neo4j_uri, neo4j_user, neo4j_password)

    try:
        # Define registries to ingest (entity_type: (yaml_path, merger_func))
        registries = {
            "sector": (
                "/Volumes/LaCie/Company-Brain/_REGISTRIES/CANONICAL/SECTOR_INDEX.yaml",
                pipeline.merge_sector,
            ),
            "venture": (
                "/Volumes/LaCie/Company-Brain/_REGISTRIES/CANONICAL/ventures-by-sector.yaml",
                pipeline.merge_venture,
            ),
            # Add more registries as needed
        }

        # Run migration
        report = await pipeline.run_migration(registries)

        # Save report
        report_path = Path(
            "/Volumes/LaCie/Company-Brain/_REFERENCE/PHASE2-MIGRATION-REPORT.json"
        )
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2))

        print(f"\n📄 Report saved to: {report_path}")

    finally:
        await pipeline.close()


if __name__ == "__main__":
    asyncio.run(main())
