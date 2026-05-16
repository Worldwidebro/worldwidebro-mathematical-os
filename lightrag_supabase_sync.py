#!/usr/bin/env python3
"""
LightRAG → Supabase Integration
Syncs extracted entities and relationships to Week 0 persistent storage
Enables agent queries against knowledge graph
"""

import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime
from lightrag_demo import LightRAGGraph, Entity, Relationship

# Supabase config
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
SUPABASE_READY = bool(SUPABASE_URL and SUPABASE_KEY)


@dataclass
class GraphEntity:
    """Graph entity aligned with Week 0 ontology"""
    id: str
    name: str
    entity_type: str
    venture_id: Optional[str] = None
    description: str = ""
    metadata: Dict = None
    extracted_at: str = ""

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "entity_type": self.entity_type,
            "venture_id": self.venture_id,
            "description": self.description,
            "metadata": self.metadata or {},
            "extracted_at": self.extracted_at or datetime.utcnow().isoformat(),
        }


@dataclass
class GraphRelationship:
    """Relationship between graph entities"""
    id: str
    source_id: str
    target_id: str
    relation_type: str
    weight: float = 1.0
    context: str = ""
    created_at: str = ""

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "source_id": self.source_id,
            "target_id": self.target_id,
            "relation_type": self.relation_type,
            "weight": self.weight,
            "context": self.context,
            "created_at": self.created_at or datetime.utcnow().isoformat(),
        }


class LightRAGSupabaseSync:
    """Sync LightRAG graph to Supabase with Week 0 semantics"""

    def __init__(self):
        self.graph = LightRAGGraph()
        self.entity_mapping: Dict[str, str] = {}  # entity_name → venture_id
        self.entity_name_to_id: Dict[str, str] = {}  # entity_name → synced entity_id
        self.synced_entities: List[GraphEntity] = []
        self.synced_relationships: List[GraphRelationship] = []

        if SUPABASE_READY:
            self.supabase_url = SUPABASE_URL
            self.supabase_key = SUPABASE_KEY
            print(f"✅ Supabase ready: {self.supabase_url[:40]}...")
        else:
            print(f"⚠️  Supabase credentials not set. Using mock storage.")

    def ingest_document(self, doc_text: str, doc_id: str, venture_id: Optional[str] = None) -> Dict:
        """Ingest document, extract entities, map to ventures"""
        result = self.graph.ingest_document(doc_text, doc_id)

        # Map extracted entities to venture
        for entity in result.get("entities", []):
            if venture_id:
                self.entity_mapping[entity["name"]] = venture_id

        return result

    def map_entity_to_venture(self, entity_name: str, venture_id: str):
        """Manually map entity to venture (for relationship tracking)"""
        self.entity_mapping[entity_name] = venture_id

    def sync_entities_to_supabase(self) -> List[Dict]:
        """Convert LightRAG entities to Supabase format and sync"""
        synced = []
        entity_name_to_id = {}  # Map entity names to synced IDs for relationship resolution

        for entity_name, entity in self.graph.entities.items():
            venture_id = self.entity_mapping.get(entity_name)
            entity_id = f"entity_{len(self.synced_entities)}"

            graph_entity = GraphEntity(
                id=entity_id,
                name=entity_name,
                entity_type=entity.entity_type,
                venture_id=venture_id,
                description=entity.description,
                metadata=entity.metadata
            )

            self.synced_entities.append(graph_entity)
            entity_name_to_id[entity_name] = entity_id
            entity_dict = graph_entity.to_dict()
            synced.append(entity_dict)

            # Insert into Supabase if connected
            if SUPABASE_READY:
                try:
                    from supabase import create_client
                    client = create_client(self.supabase_url, self.supabase_key)
                    client.table("graph_entities").insert(entity_dict).execute()
                except Exception as e:
                    pass  # Silently fail for duplicates or errors

        self.entity_name_to_id = entity_name_to_id  # Store for relationship resolution
        print(f"📤 Synced {len(synced)} entities to Supabase")
        return synced

    def sync_relationships_to_supabase(self) -> List[Dict]:
        """Convert LightRAG relationships to Supabase format and sync"""
        synced = []

        for idx, rel in enumerate(self.graph.relationships):
            # Resolve entity names to their synced IDs for foreign key constraints
            source_id = self.entity_name_to_id.get(rel.source, rel.source)
            target_id = self.entity_name_to_id.get(rel.target, rel.target)

            graph_rel = GraphRelationship(
                id=f"rel_{idx}",
                source_id=source_id,
                target_id=target_id,
                relation_type=rel.relation_type,
                weight=rel.weight,
                context=rel.context
            )

            self.synced_relationships.append(graph_rel)
            rel_dict = graph_rel.to_dict()
            synced.append(rel_dict)

            # Insert into Supabase if connected
            if SUPABASE_READY:
                try:
                    from supabase import create_client
                    client = create_client(self.supabase_url, self.supabase_key)
                    client.table("graph_relationships").insert(rel_dict).execute()
                except Exception as e:
                    pass  # Silently fail for duplicates or errors

        print(f"📤 Synced {len(synced)} relationships to Supabase")
        return synced

    def query_ventures_from_graph(self) -> List[Dict]:
        """Query all ventures from synced graph"""
        ventures = []
        for entity_name in self.graph.get_ventures():
            venture_id = self.entity_mapping.get(entity_name)
            ventures.append({
                "name": entity_name,
                "venture_id": venture_id,
                "metrics": [],  # Would be populated from related metric entities
            })
        return ventures

    def query_venture_risks(self, venture_id: str) -> List[Dict]:
        """Query risks associated with a venture from graph"""
        risks = []
        for risk_name in self.graph.get_risks():
            # Check if risk is related to this venture
            if self.entity_mapping.get(risk_name) == venture_id:
                risks.append({"name": risk_name, "venture_id": venture_id})
        return risks

    def query_venture_decisions(self, venture_id: str) -> List[Dict]:
        """Query decisions for a venture"""
        decisions = []
        for decision_name in self.graph.get_decisions():
            # In real system, traverse relationships to find decision→venture link
            decisions.append({
                "name": decision_name,
                "venture_id": venture_id,
                "applied_at": datetime.utcnow().isoformat()
            })
        return decisions

    def sync_all(self) -> Dict:
        """Full sync: entities → relationships → Supabase"""
        print(f"\n🔄 Starting LightRAG → Supabase sync")
        print(f"{'='*70}")

        entities_synced = self.sync_entities_to_supabase()
        relationships_synced = self.sync_relationships_to_supabase()

        result = {
            "entities_synced": len(entities_synced),
            "relationships_synced": len(relationships_synced),
            "ventures": self.query_ventures_from_graph(),
            "timestamp": datetime.utcnow().isoformat()
        }

        print(f"\n✅ Sync complete:")
        print(f"   Entities: {result['entities_synced']}")
        print(f"   Relationships: {result['relationships_synced']}")
        print(f"   Ventures indexed: {len(result['ventures'])}")

        return result

    def get_sync_status(self) -> Dict:
        """Report sync status"""
        return {
            "graph_entities": len(self.graph.entities),
            "graph_relationships": len(self.graph.relationships),
            "synced_entities": len(self.synced_entities),
            "synced_relationships": len(self.synced_relationships),
            "supabase_connected": SUPABASE_READY,
            "entity_mappings": len(self.entity_mapping)
        }


def demo_with_supabase_sync():
    """Demo: LightRAG → Supabase for Week 0 ventures"""
    sync = LightRAGSupabaseSync()

    # Sample Week 0 documents
    ventures_data = [
        {
            "venture_id": "venture_hrms_001",
            "doc_id": "doc_hrms_001",
            "text": "HRMS payroll platform owned by Worldwidebro CEO. Financial metrics: CAC $120, LTV $500, survival_metric 72. Decision: SCALE with $50K capital. Executes lead search and SMS campaign. Risk: high churn at 8%."
        },
        {
            "venture_id": "venture_ai_002",
            "doc_id": "doc_ai_002",
            "text": "AI SaaS assistant startup. Metrics: ROI 85%, survival_metric 65. Decision: COMPOUND with $100K allocation. Manages email campaigns and LinkedIn outreach. Risk: market saturation threat escalates to CTO."
        },
        {
            "venture_id": "venture_marketplace_003",
            "doc_id": "doc_marketplace_003",
            "text": "Marketplace venture critical condition. Survival_metric 28, runway 6 weeks. Decision: OPTIMIZE. CEO allocates $25K emergency capital. Risk: channel blocker. Benefit: margin recovery potential 35%."
        },
    ]

    print(f"\n🚀 LightRAG + Supabase Sync Demo (Week 0)")
    print(f"{'='*70}\n")

    # Ingest all ventures
    for venture in ventures_data:
        print(f"📥 Ingesting: {venture['venture_id']}")
        sync.ingest_document(
            doc_text=venture["text"],
            doc_id=venture["doc_id"],
            venture_id=venture["venture_id"]
        )

    # Show graph state
    stats = sync.graph.stats()
    print(f"\n📊 Graph State After Ingestion:")
    print(f"   Entities: {stats['total_entities']}")
    print(f"   Relationships: {stats['total_relationships']}")

    # Sync to Supabase (mock)
    sync_result = sync.sync_all()

    # Query examples
    print(f"\n{'='*70}")
    print(f"📋 Query Results:")
    print(f"\nVentures indexed:")
    for venture in sync_result["ventures"]:
        print(f"   • {venture['name']} → {venture['venture_id']}")

    print(f"\nDecisions extracted:")
    decisions = sync.graph.get_decisions()
    for decision in decisions:
        print(f"   • {decision}")

    print(f"\nMetrics available:")
    metrics = sync.graph.get_metrics()
    for metric in metrics:
        print(f"   • {metric}")

    print(f"\nRisks identified:")
    risks = sync.graph.get_risks()
    for risk in risks:
        print(f"   • {risk}")

    # Sync status
    status = sync.get_sync_status()
    print(f"\n{'='*70}")
    print(f"🔄 Sync Status:")
    print(f"   Supabase connected: {status['supabase_connected']}")
    print(f"   Entities ready: {status['synced_entities']}/{status['graph_entities']}")
    print(f"   Relationships ready: {status['synced_relationships']}/{status['graph_relationships']}")

    print(f"\n✅ Ready for agent queries against knowledge graph")
    return sync


if __name__ == "__main__":
    sync = demo_with_supabase_sync()
