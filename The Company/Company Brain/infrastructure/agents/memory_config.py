"""
Neo4j Agent Memory Configuration
Wires short-term, long-term, and reasoning memory to Neo4j
Agents use this to store and retrieve conversation context, entities, and decision traces
"""

from dataclasses import dataclass
from typing import Optional, Dict, Any
import os
from neo4j import GraphDatabase, Session

@dataclass
class MemorySettings:
    """Memory configuration for agents"""

    # Neo4j connection
    neo4j_uri: str = os.getenv("NEO4J_URI", "bolt://100.87.214.70:7687")
    neo4j_user: str = os.getenv("NEO4J_USER", "neo4j")
    neo4j_password: str = os.getenv("NEO4J_PASSWORD", "changeme")

    # OmniRoute connection (for tool execution)
    omniroute_url: str = os.getenv("OMNIROUTE_URL", "http://100.87.214.70:20128")
    omniroute_api_key: str = os.getenv("OMNIROUTE_API_KEY", "")

    # Memory settings
    short_term_ttl_hours: int = 24
    long_term_retention_days: int = 365
    reasoning_retention_days: int = 90

    # Memory types enabled
    enable_short_term: bool = True
    enable_long_term: bool = True
    enable_reasoning: bool = True

    # Confidence settings
    confidence_threshold: float = 0.7
    confidence_decay_per_day: float = 0.05

    # Batch settings
    batch_write_interval_seconds: int = 5
    max_batch_size: int = 100

    # Entity extraction
    entity_extraction_enabled: bool = True
    entity_extraction_model: str = "gliner"  # or "spacy", "llm"

    # Reasoning trace retention
    max_reasoning_traces_per_session: int = 100
    reasoning_summary_enabled: bool = True


class MemoryClient:
    """
    Client for agent memory operations.
    Handles short-term (conversation), long-term (entity), and reasoning memory.
    """

    def __init__(self, settings: MemorySettings):
        self.settings = settings
        self.driver = GraphDatabase.driver(
            settings.neo4j_uri,
            auth=(settings.neo4j_user, settings.neo4j_password)
        )
        self._create_indexes()

    def _create_indexes(self):
        """Create necessary Neo4j indexes for memory queries"""
        with self.driver.session() as session:
            # Short-term memory indexes
            session.run("""
                CREATE INDEX IF NOT EXISTS
                FOR (m:Memory:ShortTerm) ON (m.session_id, m.created_at)
            """)

            # Long-term memory indexes
            session.run("""
                CREATE INDEX IF NOT EXISTS
                FOR (e:Entity) ON (e.type, e.name)
            """)

            # Reasoning trace indexes
            session.run("""
                CREATE INDEX IF NOT EXISTS
                FOR (t:ReasoningTrace) ON (t.agent_id, t.timestamp)
            """)

            # Preference indexes
            session.run("""
                CREATE INDEX IF NOT EXISTS
                FOR (p:Preference) ON (p.entity_id, p.category)
            """)

    async def add_short_term_memory(
        self,
        session_id: str,
        role: str,  # "agent" or "user"
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """Add message to short-term memory"""
        with self.driver.session() as session:
            result = session.run("""
                CREATE (m:Memory:ShortTerm {
                    session_id: $session_id,
                    role: $role,
                    content: $content,
                    created_at: datetime(),
                    ttl_expires: datetime() + duration({hours: $ttl_hours}),
                    metadata: $metadata
                })
                RETURN m.id as id
            """, {
                "session_id": session_id,
                "role": role,
                "content": content,
                "ttl_hours": self.settings.short_term_ttl_hours,
                "metadata": metadata or {}
            })
            return result.single()["id"]

    async def get_short_term_context(self, session_id: str) -> list:
        """Retrieve conversation history for a session"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (m:Memory:ShortTerm {session_id: $session_id})
                WHERE m.ttl_expires > datetime()
                RETURN m.role, m.content, m.created_at
                ORDER BY m.created_at DESC
                LIMIT 50
            """, {"session_id": session_id})
            return [dict(record) for record in result]

    async def add_entity(
        self,
        name: str,
        entity_type: str,  # PERSON, ORGANIZATION, VENTURE, METRIC
        description: Optional[str] = None,
        attributes: Optional[Dict] = None
    ) -> str:
        """Add or merge entity to long-term memory (POLE+O model)"""
        with self.driver.session() as session:
            result = session.run("""
                MERGE (e:Entity {
                    type: $entity_type,
                    name: $name
                })
                SET e.description = $description,
                    e.attributes = $attributes,
                    e.updated_at = datetime()
                RETURN e.id as id
            """, {
                "entity_type": entity_type,
                "name": name,
                "description": description,
                "attributes": attributes or {}
            })
            return result.single()["id"]

    async def add_reasoning_trace(
        self,
        agent_id: str,
        session_id: str,
        decision: str,
        reasoning: str,
        confidence: float,
        outcome: Optional[str] = None
    ) -> str:
        """Log decision trace (for learning + audit)"""
        with self.driver.session() as session:
            result = session.run("""
                CREATE (t:ReasoningTrace {
                    agent_id: $agent_id,
                    session_id: $session_id,
                    decision: $decision,
                    reasoning: $reasoning,
                    confidence: $confidence,
                    outcome: $outcome,
                    timestamp: datetime()
                })
                RETURN t.id as id
            """, {
                "agent_id": agent_id,
                "session_id": session_id,
                "decision": decision,
                "reasoning": reasoning,
                "confidence": confidence,
                "outcome": outcome
            })
            return result.single()["id"]

    async def get_agent_reasoning_history(
        self,
        agent_id: str,
        limit: int = 100
    ) -> list:
        """Retrieve agent's recent decisions for learning"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (t:ReasoningTrace {agent_id: $agent_id})
                RETURN t.decision, t.confidence, t.outcome, t.timestamp
                ORDER BY t.timestamp DESC
                LIMIT $limit
            """, {
                "agent_id": agent_id,
                "limit": limit
            })
            return [dict(record) for record in result]

    async def add_preference(
        self,
        entity_id: str,
        category: str,
        preference: str,
        confidence: float = 0.7
    ):
        """Add preference to entity (learned behavior)"""
        with self.driver.session() as session:
            session.run("""
                MERGE (p:Preference {
                    entity_id: $entity_id,
                    category: $category
                })
                SET p.preference = $preference,
                    p.confidence = $confidence,
                    p.learned_at = datetime()
            """, {
                "entity_id": entity_id,
                "category": category,
                "preference": preference,
                "confidence": confidence
            })

    def close(self):
        """Close Neo4j connection"""
        self.driver.close()


# Initialize globally
_memory_settings = MemorySettings()
memory_client = MemoryClient(_memory_settings)

__all__ = [
    "MemorySettings",
    "MemoryClient",
    "memory_client",
    "_memory_settings",
]
