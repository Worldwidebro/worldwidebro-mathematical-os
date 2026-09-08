"""
KG-028: Agent Context Assembly — Build relevant subgraph for any agent
Given agent type + task context → return filtered graph neighborhood
"""

from typing import TypedDict, Optional
from dataclasses import dataclass, asdict
import yaml

try:
    from neo4j import GraphDatabase
except ImportError:
    raise ImportError("neo4j package required: pip install neo4j")


@dataclass
class ContextEntity:
    """Single entity in agent context"""
    entity_id: str
    entity_type: str
    properties: dict
    distance_hops: int
    confidence_score: float


@dataclass
class AgentContext:
    """Complete context for an agent's task"""
    agent_id: str
    focal_entity_id: str
    focal_entity_type: str
    depth_limit: int
    entities: list[ContextEntity]
    relationships: list[dict]
    risks: list[dict]
    opportunities: list[dict]
    metadata: dict


class AgentContextBuilder:
    """Build task-specific subgraph contexts for agents"""

    def __init__(
        self,
        neo4j_uri: str = "bolt://100.87.214.70:7687",
        neo4j_user: str = "neo4j",
        neo4j_password: str = "changeme",
        agent_profiles_path: str = None,
    ):
        """Initialize Neo4j connection and agent profiles"""
        self.neo4j_driver = GraphDatabase.driver(
            neo4j_uri, auth=(neo4j_user, neo4j_password)
        )
        self.agent_profiles = self._load_agent_profiles(agent_profiles_path)

    def close(self):
        """Close Neo4j connection"""
        if self.neo4j_driver:
            self.neo4j_driver.close()

    def build_context(
        self,
        agent_id: str,
        focal_entity_id: str,
        depth: int = 2,
        include_types: list = None,
        exclude_types: list = None,
    ) -> AgentContext:
        """
        Build context for agent by fetching relevant subgraph.

        Args:
            agent_id: Which agent is this for (AGT-001, etc.)
            focal_entity_id: Primary entity (venture, repo, etc.)
            depth: Relationship hop depth (1-3)
            include_types: Entity types to include
            exclude_types: Entity types to exclude

        Returns:
            Complete agent context with entities, relationships, risks, opportunities
        """
        # Get agent profile
        agent_profile = self.agent_profiles.get(agent_id, {})

        # Fetch focal entity
        focal_entity = self._fetch_entity(focal_entity_id)
        if not focal_entity:
            raise ValueError(f"Entity not found: {focal_entity_id}")

        # Fetch neighborhood
        entities, relationships = self._fetch_neighborhood(
            focal_entity_id,
            depth,
            include_types or agent_profile.get("include_types", []),
            exclude_types or agent_profile.get("exclude_types", []),
        )

        # Detect risks
        risks = self._detect_risks(focal_entity_id, entities, relationships)

        # Detect opportunities
        opportunities = self._detect_opportunities(
            focal_entity_id, entities, relationships
        )

        return AgentContext(
            agent_id=agent_id,
            focal_entity_id=focal_entity_id,
            focal_entity_type=focal_entity.get("entity_type", "UNKNOWN"),
            depth_limit=depth,
            entities=entities,
            relationships=relationships,
            risks=risks,
            opportunities=opportunities,
            metadata={
                "query_timestamp": self._timestamp_now(),
                "entity_count": len(entities),
                "relationship_count": len(relationships),
                "risk_count": len(risks),
                "opportunity_count": len(opportunities),
            },
        )

    def _fetch_entity(self, entity_id: str) -> Optional[dict]:
        """Fetch single entity by ID"""
        cypher = f"""
        MATCH (n)
        WHERE n.id = '{entity_id}'
        RETURN
            n.id AS entity_id,
            n.entity_type AS entity_type,
            properties(n) AS properties
        LIMIT 1
        """

        with self.neo4j_driver.session() as session:
            result = session.run(cypher)
            record = result.single()
            if record:
                return dict(record)
        return None

    def _fetch_neighborhood(
        self,
        focal_entity_id: str,
        depth: int = 2,
        include_types: list = None,
        exclude_types: list = None,
    ) -> tuple[list[ContextEntity], list[dict]]:
        """
        Fetch all related entities within N hops.
        Returns: (entities, relationships)
        """
        type_filter = ""
        if include_types:
            types_str = "', '".join(include_types)
            type_filter += f"AND m.entity_type IN ['{types_str}']"
        if exclude_types:
            types_str = "', '".join(exclude_types)
            type_filter += f"AND m.entity_type NOT IN ['{types_str}']"

        cypher = f"""
        MATCH (n)-[*1..{depth}]-(m)
        WHERE n.id = '{focal_entity_id}'
        {type_filter}
        RETURN DISTINCT
            m.id AS entity_id,
            m.entity_type AS entity_type,
            properties(m) AS properties,
            length(shortestPath((n)-[*]-(m))) AS distance
        """

        with self.neo4j_driver.session() as session:
            result = session.run(cypher)
            entities = []
            for record in result:
                entities.append(
                    ContextEntity(
                        entity_id=record["entity_id"],
                        entity_type=record["entity_type"],
                        properties=dict(record.get("properties", {})),
                        distance_hops=record.get("distance", 1),
                        confidence_score=1.0 / (1.0 + record.get("distance", 1)),
                    )
                )

        # Fetch relationships
        cypher_rels = f"""
        MATCH (n)-[r]-(m)
        WHERE n.id = '{focal_entity_id}'
        RETURN
            n.id AS from_id,
            m.id AS to_id,
            type(r) AS relationship_type,
            properties(r) AS properties
        """

        with self.neo4j_driver.session() as session:
            result = session.run(cypher_rels)
            relationships = []
            for record in result:
                relationships.append(
                    {
                        "from_id": record["from_id"],
                        "to_id": record["to_id"],
                        "type": record["relationship_type"],
                        "properties": dict(record.get("properties", {})),
                    }
                )

        return entities, relationships

    def _detect_risks(
        self,
        focal_entity_id: str,
        entities: list[ContextEntity],
        relationships: list[dict],
    ) -> list[dict]:
        """
        Analyze context for risks (dependencies, single-points-of-failure, etc.)
        """
        risks = []

        # Risk 1: High dependency count
        dep_count = len([r for r in relationships if r["type"] == "DEPENDS_ON"])
        if dep_count > 5:
            risks.append(
                {
                    "type": "HIGH_DEPENDENCY",
                    "severity": "MEDIUM",
                    "description": f"{focal_entity_id} has {dep_count} dependencies",
                    "entities_affected": [e.entity_id for e in entities],
                }
            )

        # Risk 2: Single point of failure (critical shared tech)
        shared_tech = self._find_shared_tech(entities, relationships)
        if shared_tech:
            risks.append(
                {
                    "type": "SHARED_TECH_RISK",
                    "severity": "HIGH",
                    "description": f"Shared tech bottleneck: {shared_tech}",
                    "entities_affected": [shared_tech],
                }
            )

        return risks

    def _detect_opportunities(
        self,
        focal_entity_id: str,
        entities: list[ContextEntity],
        relationships: list[dict],
    ) -> list[dict]:
        """
        Analyze context for opportunities (synergies, collaboration, etc.)
        """
        opportunities = []

        # Opportunity 1: Ventures with common capabilities
        common_caps = self._find_common_capabilities(entities)
        if common_caps:
            opportunities.append(
                {
                    "type": "CAPABILITY_SYNERGY",
                    "potential": "HIGH",
                    "description": f"Ventures share capabilities: {', '.join(common_caps[:3])}",
                    "entities_affected": [e.entity_id for e in entities[:5]],
                }
            )

        # Opportunity 2: Potential partnerships
        potential_partners = self._find_potential_partners(entities)
        if potential_partners:
            opportunities.append(
                {
                    "type": "PARTNERSHIP",
                    "potential": "MEDIUM",
                    "description": f"Potential partner ventures: {', '.join(potential_partners[:3])}",
                    "entities_affected": potential_partners[:3],
                }
            )

        return opportunities

    def _find_shared_tech(self, entities: list, relationships: list) -> Optional[str]:
        """Find shared technology that multiple ventures depend on"""
        # Count tech dependencies from relationships
        tech_deps = {}
        for rel in relationships:
            if rel.get("type") == "DEPENDS_ON":
                tech_id = rel.get("to_id")
                if tech_id:
                    tech_deps[tech_id] = tech_deps.get(tech_id, 0) + 1

        # Find the tech with most dependents (bottleneck)
        if tech_deps:
            bottleneck = max(tech_deps.items(), key=lambda x: x[1])
            if bottleneck[1] > 1:  # Shared by 2+ entities
                return bottleneck[0]

        return None

    def _find_common_capabilities(self, entities: list) -> list[str]:
        """Find capabilities shared by multiple entities"""
        if not entities:
            return []

        # Extract capabilities from entity properties
        capability_counts = {}
        for entity in entities:
            if entity.entity_type == "CAPABILITY":
                cap_name = entity.properties.get("name", entity.entity_id)
                capability_counts[cap_name] = capability_counts.get(cap_name, 0) + 1

        # Return capabilities shared by 2+ entities
        common = [cap for cap, count in capability_counts.items() if count >= 2]
        return sorted(common, key=lambda x: capability_counts[x], reverse=True)

    def _find_potential_partners(self, entities: list) -> list[str]:
        """Find ventures that could partner"""
        ventures = [e for e in entities if e.entity_type == "VENTURE"]
        if len(ventures) < 2:
            return []

        # Ventures in same sector/geography are potential partners
        partner_pairs = []
        for i, v1 in enumerate(ventures):
            for v2 in ventures[i + 1:]:
                # Same sector or complementary capabilities → partnership potential
                sector1 = v1.properties.get("sector", "")
                sector2 = v2.properties.get("sector", "")

                if sector1 and sector1 == sector2:
                    partner_pairs.append(v2.entity_id)

        return partner_pairs[:5]  # Top 5

    def _load_agent_profiles(self, path: str = None) -> dict:
        """Load agent profiles YAML with type filters and distance policies"""
        if not path:
            path = (
                "/Users/acebless/Documents/The Company/Company Brain/12-CONTEXT"
                "/agent_profiles.yaml"
            )

        try:
            with open(path, "r") as f:
                return yaml.safe_load(f) or {}
        except FileNotFoundError:
            return {}

    def _timestamp_now(self) -> str:
        """ISO timestamp"""
        from datetime import datetime

        return datetime.now().isoformat()


if __name__ == "__main__":
    # Example usage
    builder = AgentContextBuilder()

    try:
        context = builder.build_context(
            agent_id="AGT-001",
            focal_entity_id="LT-005",  # HealthRoute Medical Courier
            depth=2,
            include_types=["VENTURE", "REPOSITORY", "CAPABILITY"],
        )

        print(f"Agent Context for {context.agent_id}")
        print(f"Focal: {context.focal_entity_id} ({context.focal_entity_type})")
        print(f"Entities: {len(context.entities)}")
        print(f"Relationships: {len(context.relationships)}")
        print(f"Risks: {len(context.risks)}")
        print(f"Opportunities: {len(context.opportunities)}\n")

        if context.entities:
            print("Entities:")
            for e in context.entities[:3]:
                print(f"  - {e.entity_id} (hops: {e.distance_hops}, score: {e.confidence_score:.2f})")

        if context.risks:
            print("\nRisks:")
            for r in context.risks:
                print(f"  - {r['type']}: {r['description']}")

        if context.opportunities:
            print("\nOpportunities:")
            for o in context.opportunities:
                print(f"  - {o['type']}: {o['description']}")

    finally:
        builder.close()
