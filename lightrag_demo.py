#!/usr/bin/env python3
"""
LightRAG + Supabase Integration Demo
Entity extraction → graph storage → venture insights
"""

import json
from typing import Dict, List, Set, Tuple
from dataclasses import dataclass, asdict
from collections import defaultdict

# LightRAG entity extraction (deterministic NER)
@dataclass
class Entity:
    name: str
    entity_type: str  # Venture, Sector, Agent, Contact, Decision, Risk, Metric, Fund
    description: str = ""
    metadata: Dict = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

@dataclass
class Relationship:
    source: str
    target: str
    relation_type: str  # owns, manages, escalates, executes, reports, allocates, risks, benefits
    weight: float = 1.0
    context: str = ""


class LightRAGGraph:
    """Lightweight graph-based entity extraction (no Ollama needed)"""

    def __init__(self):
        self.entities: Dict[str, Entity] = {}
        self.relationships: List[Relationship] = []
        self.entity_index: Dict[str, Set[str]] = defaultdict(set)  # type → names

    def extract_entities(self, text: str, context_type: str = "general") -> List[Entity]:
        """
        Deterministic NER using pattern matching + predefined entity types
        No LLM required, fully deterministic
        """
        extracted = []

        # Venture patterns
        venture_keywords = ["venture", "startup", "company", "business", "product"]
        for keyword in venture_keywords:
            if keyword in text.lower():
                for word in text.split():
                    if any(marker in word.lower() for marker in ["hrms", "lms", "ai", "saas"]):
                        entity = Entity(
                            name=word.strip(".,;:"),
                            entity_type="Venture",
                            description=f"Identified from context: {text[:100]}",
                            metadata={"source": "pattern_match", "confidence": 0.85}
                        )
                        extracted.append(entity)

        # Decision patterns
        decision_keywords = ["kill", "optimize", "scale", "compound"]
        for keyword in decision_keywords:
            if keyword in text.lower():
                entity = Entity(
                    name=f"Decision_{keyword.upper()}",
                    entity_type="Decision",
                    description=f"CEO decision type identified: {keyword}",
                    metadata={"source": "keyword_match", "confidence": 0.95}
                )
                extracted.append(entity)

        # Metric patterns
        metric_patterns = [
            ("survival_metric", "Metric"),
            ("roi", "Metric"),
            ("cac", "Metric"),
            ("ltv", "Metric"),
            ("churn", "Metric"),
        ]
        for pattern, entity_type in metric_patterns:
            if pattern in text.lower():
                entity = Entity(
                    name=pattern.upper(),
                    entity_type=entity_type,
                    description=f"Financial metric: {pattern}",
                    metadata={"source": "metric_pattern", "confidence": 0.9}
                )
                extracted.append(entity)

        # Risk patterns
        risk_keywords = ["risk", "threat", "blocker", "issue", "critical"]
        for keyword in risk_keywords:
            if keyword in text.lower():
                entity = Entity(
                    name=f"Risk_{keyword.upper()}",
                    entity_type="Risk",
                    description=f"Risk identified: {keyword}",
                    metadata={"source": "risk_pattern", "confidence": 0.8}
                )
                extracted.append(entity)

        return extracted

    def extract_relationships(self, entities: List[Entity], text: str) -> List[Relationship]:
        """
        Extract relationships between entities from context
        Patterns: "X manages Y", "X owns Y", "X escalates to Y"
        """
        relationships = []

        relation_patterns = [
            ("manages", "manages"),
            ("owns", "owns"),
            ("escalates", "escalates"),
            ("executes", "executes"),
            ("reports to", "reports"),
            ("allocates", "allocates"),
            ("risks", "risks"),
            ("benefits", "benefits"),
        ]

        for pattern, rel_type in relation_patterns:
            if pattern in text.lower():
                if len(entities) >= 2:
                    rel = Relationship(
                        source=entities[0].name,
                        target=entities[1].name if len(entities) > 1 else entities[0].name,
                        relation_type=rel_type,
                        weight=0.85,
                        context=text[:80]
                    )
                    relationships.append(rel)

        return relationships

    def ingest_document(self, doc_text: str, doc_id: str) -> Dict:
        """
        Full ingestion pipeline: extract entities → relationships → store
        """
        print(f"\n📄 Ingesting document: {doc_id}")

        entities = self.extract_entities(doc_text)
        print(f"   Extracted {len(entities)} entities")

        relationships = self.extract_relationships(entities, doc_text)
        print(f"   Extracted {len(relationships)} relationships")

        # Store entities
        for entity in entities:
            self.entities[entity.name] = entity
            self.entity_index[entity.entity_type].add(entity.name)

        # Store relationships
        self.relationships.extend(relationships)

        return {
            "doc_id": doc_id,
            "entities_extracted": len(entities),
            "relationships_extracted": len(relationships),
            "entities": [asdict(e) for e in entities],
            "relationships": [asdict(r) for r in relationships]
        }

    def query_graph(self, entity_name: str) -> Dict:
        """Query related entities and relationships"""
        if entity_name not in self.entities:
            return {"error": f"Entity '{entity_name}' not found"}

        entity = self.entities[entity_name]
        related = []

        for rel in self.relationships:
            if rel.source == entity_name:
                related.append({
                    "target": rel.target,
                    "relation": rel.relation_type,
                    "context": rel.context
                })

        return {
            "entity": asdict(entity),
            "related": related,
            "total_relationships": len(related)
        }

    def get_ventures(self) -> List[str]:
        """Get all ventures in graph"""
        return list(self.entity_index.get("Venture", []))

    def get_decisions(self) -> List[str]:
        """Get all decisions in graph"""
        return list(self.entity_index.get("Decision", []))

    def get_metrics(self) -> List[str]:
        """Get all metrics in graph"""
        return list(self.entity_index.get("Metric", []))

    def get_risks(self) -> List[str]:
        """Get all risks in graph"""
        return list(self.entity_index.get("Risk", []))

    def stats(self) -> Dict:
        """Graph statistics"""
        return {
            "total_entities": len(self.entities),
            "total_relationships": len(self.relationships),
            "by_type": dict(self.entity_index),
            "entity_types": list(set(e.entity_type for e in self.entities.values()))
        }


def demo():
    """Demonstrate LightRAG on Week 0 data"""
    graph = LightRAGGraph()

    # Sample documents representing Week 0 decisions
    sample_docs = [
        {
            "id": "venture_001",
            "text": "HRMS venture owned by Worldwidebro. CEO decision: SCALE with $50K allocation. Metrics show ROI 75%, survival_metric 68. Risk: churn rate high at 8%."
        },
        {
            "id": "venture_002",
            "text": "AI SaaS startup manages lead generation. Decision: COMPOUND with $100K capital. CAC $125, LTV $450. Escalates growth risk to CTO. Executes SMS campaign."
        },
        {
            "id": "venture_003",
            "text": "Marketplace platform reports survival_metric critical at 35. Decision: OPTIMIZE focus segment. CEO allocates $25K. Risk: runway 6 weeks only. Benefit: strong margin 42%."
        },
    ]

    print("🚀 LightRAG Knowledge Graph Demo")
    print(f"{'='*70}")

    # Ingest all documents
    ingestion_results = []
    for doc in sample_docs:
        result = graph.ingest_document(doc["text"], doc["id"])
        ingestion_results.append(result)

    # Show statistics
    stats = graph.stats()
    print(f"\n📊 Graph Statistics:")
    print(f"   Total Entities: {stats['total_entities']}")
    print(f"   Total Relationships: {stats['total_relationships']}")
    print(f"   Entity Types: {', '.join(stats['entity_types'])}")

    # Show extracted entities by type
    print(f"\n🏢 Ventures: {graph.get_ventures()}")
    print(f"📋 Decisions: {graph.get_decisions()}")
    print(f"📈 Metrics: {graph.get_metrics()}")
    print(f"⚠️  Risks: {graph.get_risks()}")

    # Demo query
    print(f"\n{'='*70}")
    print(f"Query: Decision_SCALE relationships")
    query_result = graph.query_graph("Decision_SCALE")
    if "error" not in query_result:
        print(f"   Entity: {query_result['entity']['name']} ({query_result['entity']['entity_type']})")
        print(f"   Related: {query_result['total_relationships']} connections")
        for rel in query_result['related']:
            print(f"     → {rel['relation']}: {rel['target']}")

    print(f"\n{'='*70}")
    print(f"✅ LightRAG demo complete. Graph ready for Supabase sync.")
    print(f"\nNext: Map extracted entities to ventures table, store relationships in graph_relationships table")

    return graph


if __name__ == "__main__":
    graph = demo()
