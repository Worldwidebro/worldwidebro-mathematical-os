#!/usr/bin/env python3
"""
Complete RAG Pipeline: Document Preprocessing → LightRAG → Supabase Sync
Integrates: RAG-Anything alternative + LightRAG + Supabase persistence
Ready for Week 0 document ingestion
"""

import os
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

from rag_document_preprocessor import DocumentPreprocessor, ProcessedDocument
from lightrag_demo import LightRAGGraph
from lightrag_supabase_sync import LightRAGSupabaseSync


@dataclass
class PipelineResult:
    """Complete pipeline execution result"""
    documents_processed: int
    entities_extracted: int
    relationships_extracted: int
    entities_synced: int
    relationships_synced: int
    ventures_indexed: int
    execution_time: float
    status: str


class RAGPipeline:
    """Complete RAG pipeline: preprocess → extract → persist"""

    def __init__(self):
        self.preprocessor = DocumentPreprocessor(chunk_size=512)
        self.sync = LightRAGSupabaseSync()
        self.results = []

    def process_document(self, filepath: str, venture_id: Optional[str] = None) -> Dict:
        """
        Process single document through complete pipeline
        Returns: extraction results with entity/relationship counts
        """
        print(f"\n📥 Processing: {filepath}")

        # Step 1: Preprocess (format conversion)
        processed_doc = self.preprocessor.process_file(filepath)
        if not processed_doc:
            return {"error": f"Could not process {filepath}"}

        print(f"   ✓ Preprocessed ({processed_doc.format})")
        print(f"     Text: {len(processed_doc.text)} chars → {len(processed_doc.chunks)} chunks")

        # Step 2: Ingest to LightRAG (entity extraction)
        result = self.sync.ingest_document(
            doc_text=processed_doc.text,
            doc_id=processed_doc.doc_id,
            venture_id=venture_id
        )

        print(f"   ✓ Extracted entities & relationships")
        print(f"     Entities: {result['entities_extracted']}")
        print(f"     Relationships: {result['relationships_extracted']}")

        # Step 3: Track venture mapping
        if venture_id:
            for entity in result.get("entities", []):
                self.sync.map_entity_to_venture(entity["name"], venture_id)

        return result

    def process_bulk_documents(self, documents: List[Dict]) -> List[Dict]:
        """
        Process multiple documents with venture mappings
        Each document: {"filepath": str, "venture_id": str}
        """
        results = []

        for doc in documents:
            result = self.process_document(
                filepath=doc.get("filepath"),
                venture_id=doc.get("venture_id")
            )
            results.append(result)

        return results

    def sync_to_supabase(self) -> Dict:
        """Step 4: Persist graph to Supabase"""
        print(f"\n🔄 Syncing to Supabase...")
        return self.sync.sync_all()

    def query_agent(self, query_type: str, **kwargs) -> Dict:
        """Step 5: Query interface for agents"""
        from lightrag_agent_queries import AgentQueryInterface

        query = AgentQueryInterface(self.sync)

        if query_type == "venture_context":
            return query.query_venture_context(kwargs.get("venture_id")).results[0]
        elif query_type == "venture_metrics":
            return query.query_venture_metrics(kwargs.get("venture_id")).results
        elif query_type == "venture_risks":
            return query.query_venture_risks(kwargs.get("venture_id")).results
        elif query_type == "decisions":
            return query.query_venture_decisions(kwargs.get("venture_id")).results

        return {}

    def get_pipeline_status(self) -> Dict:
        """Report full pipeline status"""
        graph_stats = self.sync.graph.stats()
        sync_stats = self.sync.get_sync_status()

        return {
            "documents_processed": len(self.preprocessor.processed),
            "graph_entities": graph_stats["total_entities"],
            "graph_relationships": graph_stats["total_relationships"],
            "synced_entities": sync_stats["synced_entities"],
            "synced_relationships": sync_stats["synced_relationships"],
            "supabase_connected": sync_stats["supabase_connected"],
            "entity_mappings": sync_stats["entity_mappings"]
        }


def demo_complete_pipeline():
    """Demo: Full pipeline from documents to agent queries"""
    import tempfile

    pipeline = RAGPipeline()

    print(f"\n🚀 RAG Complete Pipeline Demo (Document → LightRAG → Supabase → Agents)")
    print(f"{'='*70}\n")

    # Create sample documents
    sample_docs = [
        {
            "venture_id": "venture_hrms_001",
            "filename": "hrms_metrics.txt",
            "content": """
HRMS Payroll Platform - May 14 Report
====================================

Venture Owner: Worldwidebro Holdings
Status: ACTIVE

Financial Metrics (As of May 14):
- Customer Acquisition Cost (CAC): $120
- Lifetime Value (LTV): $500
- Return on Investment (ROI): 75%
- Survival Metric: 72/100
- Gross Margin: 65%
- Monthly Churn Rate: 8%
- Runway: 18 months

Latest CEO Decision: SCALE
- Capital Allocated: $50,000
- Execution Plan: Lead search + SMS campaigns
- Target: 500 new leads, 120 calls

Risks: High churn rate, platform competition
Benefits: Strong LTV, recurring revenue model
            """
        },
        {
            "venture_id": "venture_ai_002",
            "filename": "ai_saas_decision.json",
            "content": """{
  "venture": {
    "name": "AI SaaS Assistant",
    "owner": "Worldwidebro Holdings",
    "status": "ACTIVE",
    "decision": {
      "type": "COMPOUND",
      "capital_allocated": 100000,
      "date": "2026-05-14",
      "rationale": "Strong growth trajectory with 85% ROI"
    },
    "metrics": {
      "roi": 85,
      "survival_metric": 65,
      "cac": 150,
      "ltv": 600,
      "margin": 68
    },
    "risks": [
      "Market saturation threat",
      "AI model accuracy degradation"
    ],
    "execution": [
      "Email campaigns",
      "LinkedIn outreach",
      "Call scheduling"
    ]
  }
}"""
        },
        {
            "venture_id": "venture_marketplace_003",
            "filename": "marketplace_crisis.csv",
            "content": """venture_id,metric,value,status,date
venture_marketplace_003,survival_metric,28,CRITICAL,2026-05-14
venture_marketplace_003,roi,-15,NEGATIVE,2026-05-14
venture_marketplace_003,cac,180,HIGH,2026-05-14
venture_marketplace_003,ltv,200,LOW,2026-05-14
venture_marketplace_003,runway_weeks,6,CRITICAL,2026-05-14
venture_marketplace_003,decision,OPTIMIZE,APPROVED,2026-05-14
venture_marketplace_003,capital_allocated,25000,EMERGENCY,2026-05-14
venture_marketplace_003,risk_channel_blocker,true,ESCALATED,2026-05-14"""
        }
    ]

    # Write samples to temp directory
    tmpdir = tempfile.mkdtemp()
    document_mappings = []

    for doc in sample_docs:
        filepath = os.path.join(tmpdir, doc["filename"])
        with open(filepath, "w") as f:
            f.write(doc["content"])

        document_mappings.append({
            "filepath": filepath,
            "venture_id": doc["venture_id"]
        })

    # Step 1: Preprocess all documents
    print("📋 STEP 1: Document Preprocessing")
    print("-" * 70)
    results = pipeline.process_bulk_documents(document_mappings)

    # Step 2: Show extraction results
    print(f"\n📊 STEP 2: Entity Extraction Results")
    print("-" * 70)
    total_entities = sum(r.get("entities_extracted", 0) for r in results)
    total_relationships = sum(r.get("relationships_extracted", 0) for r in results)
    print(f"✓ Total Entities: {total_entities}")
    print(f"✓ Total Relationships: {total_relationships}")

    # Step 3: Sync to Supabase
    print(f"\n💾 STEP 3: Supabase Sync")
    print("-" * 70)
    sync_result = pipeline.sync_to_supabase()
    print(f"✓ Entities Synced: {sync_result['entities_synced']}")
    print(f"✓ Relationships Synced: {sync_result['relationships_synced']}")
    print(f"✓ Ventures Indexed: {len(sync_result['ventures'])}")

    # Step 4: Query via agents
    print(f"\n🤖 STEP 4: Agent Queries")
    print("-" * 70)

    print(f"\nCEO Query: Venture context for HRMS")
    context = pipeline.query_agent("venture_context", venture_id="venture_hrms_001")
    print(f"  • Entities: {context.get('total_entities')}")
    print(f"  • Relationships: {context.get('total_relationships')}")

    print(f"\nCFO Query: Metrics for AI SaaS")
    metrics = pipeline.query_agent("venture_metrics", venture_id="venture_ai_002")
    print(f"  • Metrics found: {len(metrics)}")

    print(f"\nCTO Query: Risks for Marketplace")
    risks = pipeline.query_agent("venture_risks", venture_id="venture_marketplace_003")
    print(f"  • Risks identified: {len(risks)}")

    # Step 5: Pipeline status
    print(f"\n{'='*70}")
    print(f"📈 Pipeline Status")
    print("-" * 70)
    status = pipeline.get_pipeline_status()
    print(f"  Documents Processed: {status['documents_processed']}")
    print(f"  Graph Entities: {status['graph_entities']}")
    print(f"  Graph Relationships: {status['graph_relationships']}")
    print(f"  Synced Entities: {status['synced_entities']}")
    print(f"  Supabase Connected: {status['supabase_connected']}")

    print(f"\n{'='*70}")
    print(f"✅ RAG Pipeline Complete")
    print(f"   Document → Preprocess → Extract → Sync → Query")
    print(f"   Ready for Week 0 autonomous business cycles")

    # Cleanup
    import shutil
    shutil.rmtree(tmpdir)

    return pipeline


if __name__ == "__main__":
    pipeline = demo_complete_pipeline()
