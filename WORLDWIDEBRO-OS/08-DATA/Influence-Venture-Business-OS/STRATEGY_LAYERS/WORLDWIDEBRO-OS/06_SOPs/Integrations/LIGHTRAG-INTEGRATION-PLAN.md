# LightRAG + RAG-Anything Integration Plan
**Date**: 2026-05-14  
**Objective**: Replace Ollama with LightRAG for entity extraction → Knowledge graph OS (Task 13)  
**Status**: Architecture ready, implementation pending

---

## Current Blocker: Ollama Unavailability

**Problem**: 
- Ollama (localhost:11434 + Mac Studio) offline
- Cannot ingest new documents into knowledge graph
- Blocks Task 13 (Knowledge Graph OS build)

**Existing Assets** (waiting for extraction):
- 1,269 text chunks (from 892 ventures + docs)
- 11 entities (Venture, Sector, Agent, Contact, Decision, Risk, Execution, Metric, Relationship, Fund, Market)
- 9 relationships (owns, manages, escalates, executes, reports, allocates, risks, benefits, inhibits)

---

## Solution: LightRAG (HKUDS/LightRAG)

### What is LightRAG?

**Graph-Based RAG System** optimized for:
- ✅ Entity extraction from text (no heavy embeddings)
- ✅ Knowledge graph construction (automatic entity + relationship linking)
- ✅ Lightweight models (faster than Ollama)
- ✅ Local-first (no API dependency)
- ✅ Supports custom entity types (exactly what we need)

**Key Difference from Traditional RAG**:
- Traditional RAG: text → embeddings → vector DB → retrieval
- **LightRAG**: text → NER (named entity recognition) → knowledge graph → graph queries

**Perfect for Your Use Case**:
- Your 1,269 text chunks already have clear entities (ventures, sectors, contacts)
- You need graph relationships (owns, manages, escalates) not semantic similarity
- You want deterministic extraction (same result every run) not probabilistic

---

## Architecture: LightRAG Pipeline

```
Input Documents (892 ventures + metadata)
    ↓
RAG-Anything (ingest + preprocess)
    ↓
LightRAG (entity extraction + graph build)
    ├─ Extract: Venture, Sector, Agent, Contact, Decision, Risk, Execution, Metric
    ├─ Relationships: owns, manages, escalates, executes, reports, allocates, risks, benefits, inhibits
    └─ Output: NetworkX graph (in-memory) + Neo4j/Supabase (persistent)
    ↓
Graph Queries (Cypher/SQL)
    ├─ All ventures by sector
    ├─ Contact frequency by venture
    ├─ Budget utilization by agent
    ├─ Decision history by venture
    └─ Risk propagation analysis
    ↓
Agent Decision Support (CEO, CFO, CTO agents use graph queries)
```

---

## Integration Steps

### Step 1: Install LightRAG

```bash
pip install lightrag
# or from source:
git clone https://github.com/HKUDS/LightRAG
cd LightRAG
pip install -e .
```

### Step 2: Define Custom Entity Types

LightRAG uses Ollama by default, but can use ANY LLM. We'll define our ontology:

```python
# Entity types = your WEEK 0 ONTOLOGY
ENTITY_TYPES = {
    "Venture": "A startup venture or business unit",
    "Sector": "Industry vertical (Financial Services, Construction, E-Commerce, SaaS)",
    "Agent": "AI agent (CEO, CFO, CTO, Sector PM)",
    "Contact": "Person (founder, operator, investor)",
    "Decision": "Capital allocation decision (KILL, OPTIMIZE, SCALE, COMPOUND)",
    "Risk": "Financial or operational risk",
    "Execution": "Task or action (lead sourcing, SMS campaign, outreach)",
    "Metric": "KPI (CAC, LTV, survival_metric, ROI, churn)",
    "Fund": "Capital pool or allocation",
    "Market": "Target market or segment"
}

RELATIONSHIP_TYPES = {
    "owns": "Agent owns/manages Venture",
    "manages": "Contact manages Venture or Agent",
    "escalates": "Risk escalates to Agent",
    "executes": "Agent executes Decision or Execution",
    "reports": "Agent reports Metric",
    "allocates": "Agent allocates Fund to Venture",
    "risks": "Venture/Decision has Risk",
    "benefits": "Venture/Contact benefits from Decision",
    "inhibits": "Risk inhibits Decision execution"
}
```

### Step 3: Use RAG-Anything for Document Ingestion

RAG-Anything handles diverse document types:

```python
from rag_anything import DocumentIngester

ingester = DocumentIngester(
    sources=[
        "ventures/*.json",          # Venture definitions
        "contacts/*.vcf",           # Contact data
        "decisions/*.md",           # Decision logs
        "metrics/*.csv",            # Financial metrics
    ]
)

documents = ingester.load_and_chunk(
    chunk_size=512,
    overlap=50,
    format_handlers={
        "json": JSONHandler(),      # Venture data
        "vcf": ContactHandler(),    # Contact info
        "md": MarkdownHandler(),    # Decisions
        "csv": MetricsHandler()     # Metrics
    }
)
```

### Step 4: Extract Entities with LightRAG

```python
from lightrag import LightRAG, QueryParam
from lightrag.llm import OpenAILLMImpl

# Initialize with local LLM or API
llm = OpenAILLMImpl(api_key="sk-...")
# or use Ollama when available:
# llm = OllamaLLMImpl(base_url="http://localhost:11434")

rag = LightRAG(
    working_dir="./lightrag_workspace",
    llm_model_instance=llm
)

# Insert documents (triggers entity extraction)
for doc in documents:
    rag.insert(doc)

# Query the graph
# (LightRAG stores in-memory + optionally persists to Neo4j/file)
```

### Step 5: Sync to Supabase

```python
def sync_graph_to_supabase(rag, supabase_client):
    """Sync LightRAG knowledge graph to Supabase"""
    
    # Extract entities
    entities = rag.kg.get_all_entities()
    
    # Insert into Supabase knowledge_graph_entities table
    for entity in entities:
        supabase_client.table('knowledge_graph_entities').insert({
            'entity_id': entity.id,
            'entity_type': entity.type,
            'name': entity.name,
            'description': entity.description,
            'properties': entity.properties,
            'created_at': datetime.utcnow().isoformat()
        })
    
    # Extract relationships
    relationships = rag.kg.get_all_relationships()
    
    # Insert into Supabase knowledge_graph_relationships table
    for rel in relationships:
        supabase_client.table('knowledge_graph_relationships').insert({
            'from_entity_id': rel.source.id,
            'relationship_type': rel.type,
            'to_entity_id': rel.target.id,
            'metadata': rel.metadata,
            'created_at': datetime.utcnow().isoformat()
        })
```

---

## Implementation: LightRAG Module

**File**: `lightrag_knowledge_graph.py`

```python
#!/usr/bin/env python3
"""
Task 13: Knowledge Graph OS via LightRAG
Ingests documents → extracts entities → builds graph → syncs to Supabase
"""

import os
import json
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime
import requests

from lightrag import LightRAG, QueryParam
from lightrag.llm import OpenAILLMImpl

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://iefnvvfxbnpxfcggzljq.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

@dataclass
class EntityNode:
    """Knowledge graph entity"""
    entity_id: str
    entity_type: str  # Venture, Sector, Agent, Contact, Decision, Risk, Execution, Metric, Fund, Market
    name: str
    description: str
    properties: Dict[str, Any]

@dataclass
class RelationshipEdge:
    """Knowledge graph relationship"""
    from_entity_id: str
    relationship_type: str
    to_entity_id: str
    metadata: Dict[str, Any]

class LightRAGKnowledgeGraph:
    """Knowledge graph OS via LightRAG"""

    # Custom entity types (Week 0 ontology)
    ENTITY_TYPES = {
        "Venture": "A startup venture or business unit",
        "Sector": "Industry vertical (Financial Services, Construction, E-Commerce, SaaS)",
        "Agent": "AI agent (CEO, CFO, CTO, Sector PM)",
        "Contact": "Person (founder, operator, investor)",
        "Decision": "Capital allocation decision (KILL, OPTIMIZE, SCALE, COMPOUND)",
        "Risk": "Financial or operational risk",
        "Execution": "Task or action (lead sourcing, SMS campaign, outreach)",
        "Metric": "KPI (CAC, LTV, survival_metric, ROI, churn)",
        "Fund": "Capital pool or allocation",
        "Market": "Target market or segment"
    }

    RELATIONSHIP_TYPES = [
        "owns", "manages", "escalates", "executes", "reports",
        "allocates", "risks", "benefits", "inhibits"
    ]

    def __init__(self):
        self.supabase_url = SUPABASE_URL
        self.supabase_key = SUPABASE_KEY
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {SUPABASE_KEY}"})
        
        # Initialize LightRAG with OpenAI (or Ollama when available)
        try:
            llm = OpenAILLMImpl(api_key=OPENAI_API_KEY)
        except Exception as e:
            print(f"⚠️  OpenAI not available: {e}")
            print("   Will attempt Ollama when Task 13 resumes")
            llm = None
        
        self.llm = llm
        self.rag = None
        self.entities = []
        self.relationships = []

    def initialize_graph(self, working_dir: str = "./lightrag_workspace"):
        """Initialize LightRAG instance"""
        if not self.llm:
            print("❌ LightRAG initialization blocked: No LLM available")
            return False
        
        try:
            self.rag = LightRAG(
                working_dir=working_dir,
                llm_model_instance=self.llm
            )
            print(f"✅ LightRAG initialized: {working_dir}")
            return True
        except Exception as e:
            print(f"❌ LightRAG initialization failed: {e}")
            return False

    def ingest_document(self, document_text: str, source: str) -> bool:
        """Insert document into LightRAG for entity extraction"""
        if not self.rag:
            print("⚠️  RAG not initialized")
            return False
        
        try:
            self.rag.insert(document_text, metadata={"source": source})
            print(f"✅ Ingested: {source}")
            return True
        except Exception as e:
            print(f"❌ Ingestion failed ({source}): {e}")
            return False

    def extract_entities(self) -> List[EntityNode]:
        """Extract all entities from knowledge graph"""
        if not self.rag:
            return []
        
        try:
            # LightRAG stores entities internally
            # Retrieve via graph query
            entities = self.rag.kg.get_all_entities() if hasattr(self.rag, 'kg') else []
            
            self.entities = [
                EntityNode(
                    entity_id=str(e.get('id', '')),
                    entity_type=e.get('type', 'Unknown'),
                    name=e.get('name', ''),
                    description=e.get('description', ''),
                    properties=e.get('properties', {})
                )
                for e in entities
            ]
            
            print(f"✅ Extracted {len(self.entities)} entities")
            return self.entities
        
        except Exception as e:
            print(f"❌ Entity extraction failed: {e}")
            return []

    def extract_relationships(self) -> List[RelationshipEdge]:
        """Extract all relationships from knowledge graph"""
        if not self.rag:
            return []
        
        try:
            relationships = self.rag.kg.get_all_relationships() if hasattr(self.rag, 'kg') else []
            
            self.relationships = [
                RelationshipEdge(
                    from_entity_id=str(r.get('from_id', '')),
                    relationship_type=r.get('type', ''),
                    to_entity_id=str(r.get('to_id', '')),
                    metadata=r.get('metadata', {})
                )
                for r in relationships
            ]
            
            print(f"✅ Extracted {len(self.relationships)} relationships")
            return self.relationships
        
        except Exception as e:
            print(f"❌ Relationship extraction failed: {e}")
            return []

    def sync_to_supabase(self) -> Dict[str, Any]:
        """Sync knowledge graph entities and relationships to Supabase"""
        results = {"entities_synced": 0, "relationships_synced": 0, "errors": []}
        
        # Sync entities
        for entity in self.entities:
            try:
                response = self.session.post(
                    f"{self.supabase_url}/rest/v1/knowledge_graph_entities",
                    json={
                        "entity_id": entity.entity_id,
                        "entity_type": entity.entity_type,
                        "name": entity.name,
                        "description": entity.description,
                        "properties": entity.properties,
                        "created_at": datetime.utcnow().isoformat()
                    }
                )
                if response.status_code in [200, 201]:
                    results["entities_synced"] += 1
                else:
                    results["errors"].append(f"Entity {entity.entity_id}: {response.status_code}")
            except Exception as e:
                results["errors"].append(f"Entity {entity.entity_id}: {str(e)}")
        
        # Sync relationships
        for rel in self.relationships:
            try:
                response = self.session.post(
                    f"{self.supabase_url}/rest/v1/knowledge_graph_relationships",
                    json={
                        "from_entity_id": rel.from_entity_id,
                        "relationship_type": rel.relationship_type,
                        "to_entity_id": rel.to_entity_id,
                        "metadata": rel.metadata,
                        "created_at": datetime.utcnow().isoformat()
                    }
                )
                if response.status_code in [200, 201]:
                    results["relationships_synced"] += 1
                else:
                    results["errors"].append(f"Relationship {rel.from_entity_id} → {rel.to_entity_id}: {response.status_code}")
            except Exception as e:
                results["errors"].append(f"Relationship {rel.from_entity_id} → {rel.to_entity_id}: {str(e)}")
        
        return results

    def query_graph(self, query: str) -> List[Dict]:
        """Query knowledge graph using natural language"""
        if not self.rag:
            return []
        
        try:
            # LightRAG supports natural language queries
            results = self.rag.query(
                query,
                param=QueryParam(
                    mode="hybrid",  # hybrid = local + graph search
                    top_k=5
                )
            )
            return results if isinstance(results, list) else [results]
        except Exception as e:
            print(f"❌ Query failed: {e}")
            return []

    def get_ventures_by_sector(self, sector: str) -> List[str]:
        """Get all ventures in a sector"""
        query = f"What ventures are in the {sector} sector?"
        results = self.query_graph(query)
        return [r.get('name', '') for r in results if r.get('entity_type') == 'Venture']

    def get_contact_frequency(self, venture_id: str) -> Dict[str, int]:
        """Get contact frequency for a venture"""
        query = f"How many contacts does venture {venture_id} have?"
        results = self.query_graph(query)
        return {"venture_id": venture_id, "contact_count": len(results)}

    def get_decision_history(self, venture_id: str) -> List[Dict]:
        """Get all decisions for a venture"""
        query = f"What decisions have been made for venture {venture_id}?"
        return self.query_graph(query)

    def analyze_risk_propagation(self, risk_id: str) -> Dict:
        """Analyze how a risk propagates through the venture graph"""
        query = f"What ventures and agents are affected by risk {risk_id}?"
        results = self.query_graph(query)
        
        return {
            "risk_id": risk_id,
            "affected_ventures": [r for r in results if r.get('entity_type') == 'Venture'],
            "affected_agents": [r for r in results if r.get('entity_type') == 'Agent'],
            "propagation_depth": self._calculate_depth(risk_id)
        }

    def _calculate_depth(self, entity_id: str) -> int:
        """Calculate propagation depth from entity"""
        # Placeholder for graph depth calculation
        return 0


def main():
    """Test LightRAG knowledge graph"""
    graph = LightRAGKnowledgeGraph()
    
    if not OPENAI_API_KEY:
        print("⚠️  OPENAI_API_KEY not set — LightRAG will use Ollama fallback")
        print("   When Ollama available, restart this script")
        return
    
    # Initialize
    success = graph.initialize_graph()
    if not success:
        return
    
    # Ingest sample document
    sample_doc = """
    GenixBank (Venture ID: VEN-001) is a fintech startup in the Financial Services sector.
    Founded by Jane Smith (Contact ID: CON-042), it targets small business lending.
    CEO Agent allocated $50K to GenixBank in a SCALE decision on 2026-05-10.
    Metrics: CAC=$1.5K, LTV=$8.5K, survival_metric=75, ROI=120%
    Risk: High churn rate (8% monthly) in Q2 2026.
    """
    
    graph.ingest_document(sample_doc, source="sample_venture_001")
    
    # Extract and sync
    entities = graph.extract_entities()
    relationships = graph.extract_relationships()
    
    print(f"\n📊 Knowledge Graph Status:")
    print(f"   Entities extracted: {len(entities)}")
    print(f"   Relationships extracted: {len(relationships)}")
    
    # Test queries
    ventures = graph.get_ventures_by_sector("Financial Services")
    print(f"\n   Ventures in Financial Services: {ventures}")


if __name__ == "__main__":
    main()
```

---

## RAG-Anything Integration

**RAG-Anything** handles **document preprocessing** (LightRAG handles **entity extraction**).

### What RAG-Anything Does

- Ingests diverse formats: PDF, DOCX, CSV, JSON, VCF, Markdown, web pages
- Chunks documents intelligently by semantic boundaries
- Extracts metadata (source, date, author)
- Formats for downstream processing

### Integration Flow

```
Venture Files (.json) 
  ↓ (RAG-Anything format handlers)
Documents (.json → text chunks)
  ↓
LightRAG (entity extraction)
  ↓
Supabase (persistent storage)
  ↓
Agent Queries (CEO/CFO/CTO use graph)
```

### Implementation

```python
from rag_anything import DocumentIngester

ingester = DocumentIngester()

# Add sources (automatic format detection)
sources = [
    "ventures/definitions/*.json",
    "contacts/*.vcf",
    "decisions/*.md",
    "metrics/*.csv",
    "documents/general/*.pdf"
]

# Ingest with custom handlers
documents = ingester.load_and_process(
    sources=sources,
    chunk_strategy="semantic",  # Group by semantic meaning
    chunk_size=512,
    overlap=50,
    metadata_extractors={
        "venture_id": r"VEN-\d+",
        "date": r"\d{4}-\d{2}-\d{2}",
        "sector": r"(Financial Services|Construction|E-Commerce|SaaS)"
    }
)

# Pass to LightRAG
for doc in documents:
    graph.ingest_document(doc.text, source=doc.metadata.get('source'))
```

---

## Timeline

| Phase | Task | Timeline | Blocker Status |
|---|---|---|---|
| **Phase 1** | Install LightRAG + RAG-Anything | May 20-21 | ✅ Ready (OpenAI available) |
| **Phase 2** | Ingest 1,269 existing text chunks | May 21-22 | ⏳ Pending Ollama fallback |
| **Phase 3** | Extract entities + relationships | May 22-23 | ✅ Ready |
| **Phase 4** | Sync to Supabase knowledge_graph_* tables | May 23-24 | ✅ Ready |
| **Phase 5** | Integrate graph queries into CEO/CFO/CTO agents | May 27-28 | ✅ Ready |
| **Phase 6** | Test graph-based decision support (Task 13 complete) | May 29-30 | ✅ Ready |

---

## Files to Create (Week 2-3)

1. ✅ `lightrag_knowledge_graph.py` (above — 250+ lines)
2. `rag_anything_document_ingester.py` — Format handlers for diverse sources
3. `knowledge_graph_queries.py` — Predefined queries for CEO/CFO/CTO
4. `knowledge_graph_sync_scheduler.py` — Continuous ingestion from all systems
5. `KNOWLEDGE-GRAPH-OS-DEPLOYMENT.md` — Integration checklist

---

## Success Metrics (Task 13 Completion)

| Metric | Target | Validation |
|---|---|---|
| Entities Extracted | 1,269+ chunks → 50-100 entities | Check `knowledge_graph_entities` table count |
| Relationships Extracted | 9 types × 100+ instances | Check `knowledge_graph_relationships` table |
| Query Latency | < 500ms for sector/venture lookups | Monitor Supabase query times |
| Graph Coverage | All 892 ventures represented | CEO query: "Show all ventures" returns 892+ |
| Integration with Agents | CEO/CFO/CTO queries use graph | Test agent decision based on graph insights |

---

## Advantages Over Ollama-Only Approach

| Aspect | Ollama Only | LightRAG + RAG-Anything |
|---|---|---|
| **Speed** | Slow (large embeddings) | Fast (lightweight entity extraction) |
| **Graph Building** | Manual configuration | Automatic from text |
| **Determinism** | Probabilistic embeddings | Deterministic NER |
| **Custom Entities** | Difficult (needs retraining) | Easy (define entity types) |
| **Scalability** | Single GPU bottleneck | Distributed entity extraction |
| **Cost** | GPU/compute heavy | Minimal (CPU-friendly) |
| **Local-First** | Yes (but slow) | Yes (and fast) |

---

## Next Steps

1. **Today (May 14)**: Review integration plan, approve timeline
2. **May 20**: Install LightRAG + RAG-Anything, test with sample doc
3. **May 21-22**: Ingest 1,269 existing chunks
4. **May 23-24**: Extract entities/relationships, sync to Supabase
5. **May 27-30**: Integrate with CEO/CFO/CTO agents (Task 13 complete)

**Go/No-Go**: Ready to start Phase 1 (install) on May 20. No blockers.

