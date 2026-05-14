"""
640 Starred Repos — Tier-Based Ingestion Strategy for IZA OS

Phasing: 5 phases across May 12-June 30
Each phase builds on previous layer
"""

import asyncio
from datetime import datetime
from typing import Dict, List

# Categorized repo indices by priority tier
TIER_1_CORE = {
    "RAG & Knowledge Graphs": [
        "llama_index", "langchain", "llamaindex-hub", "ragas", "mem0",
        "langgraph", "graphify", "dspy", "vellum-ai", "haystack",
    ],
    "Agent Orchestration": [
        "langgraph", "crewai", "agency-agents", "autogen", "AutoGPT",
        "genai-os", "MetaGPT", "devopsgenie", "EvalAI",
    ],
    "LLM Inference": [
        "vllm", "ollama", "llm", "text-generation-webui", "ollama-cpp",
        "tgi", "mistral", "local-llm",
    ],
}

TIER_2_SUPPORT = {
    "Data Ingestion & Processing": [
        "firecrawl", "crawl4ai", "scrapy", "selenium", "playwright",
        "cheerio", "puppeteer", "jsdom", "unstructured",
    ],
    "Context & Memory Management": [
        "mem0", "embedchain", "pinecone", "weaviate", "milvus",
        "qdrant", "chromadb", "lancedb",
    ],
    "Infrastructure & APIs": [
        "anthropic-sdk-python", "openai-python", "huggingface",
        "replicate", "together", "baseten",
    ],
}

TIER_3_SPECIALIZATION = {
    "Use Case Specific": [
        "Fabric", "maigret", "Claude-OSINT", "docuseal", "ai-for-grant-writing",
        "medplum", "fhir-works-on-aws",
    ],
    "DevOps & Deployment": [
        "kubernetes", "docker", "terraform", "ansible", "helm",
        "argocd", "backstage", "kustomize",
    ],
    "Observability": [
        "prometheus", "grafana", "loki", "sentry", "jaeger",
        "datadog", "elastic",
    ],
}

PHASE_TIMELINE = {
    "Phase 1": {
        "date": "2026-05-12 → 2026-05-15",
        "scope": "Tier 1 Core Stack",
        "repos": 25,
        "goal": "Foundation for agent autonomy",
        "blockers": 4,
    },
    "Phase 2": {
        "date": "2026-05-16 → 2026-05-20",
        "scope": "Tier 2 Support Layer",
        "repos": 40,
        "goal": "Full data pipeline + memory",
        "blockers": 2,
    },
    "Phase 3": {
        "date": "2026-05-21 → 2026-05-27",
        "scope": "Tier 3 Use Cases",
        "repos": 100,
        "goal": "Specialized tools for HRMS + ventures",
        "blockers": 0,
    },
    "Phase 4": {
        "date": "2026-05-28 → 2026-06-10",
        "scope": "DevOps & Infrastructure",
        "repos": 150,
        "goal": "Production deployment pipelines",
        "blockers": 0,
    },
    "Phase 5": {
        "date": "2026-06-11 → 2026-06-30",
        "scope": "Specialization & Optimization",
        "repos": 225,
        "goal": "Full ecosystem optimization",
        "blockers": 0,
    },
}


async def generate_install_order():
    """Generate ordered ingestion plan for 640 repos."""

    print("=" * 80)
    print("640 STARRED REPOS — TIER-BASED INGESTION STRATEGY")
    print("=" * 80)

    print("\n[PHASE 1] TIER 1: CORE STACK — May 12-15")
    print("-" * 80)
    for category, repos in TIER_1_CORE.items():
        print(f"\n  {category} ({len(repos)} repos):")
        for repo in repos[:5]:
            print(f"    - {repo}")
        if len(repos) > 5:
            print(f"    ... +{len(repos)-5} more")

    print("\n\n[PHASE 2] TIER 2: SUPPORT LAYER — May 16-20")
    print("-" * 80)
    for category, repos in TIER_2_SUPPORT.items():
        print(f"\n  {category} ({len(repos)} repos):")
        for repo in repos[:5]:
            print(f"    - {repo}")
        if len(repos) > 5:
            print(f"    ... +{len(repos)-5} more")

    print("\n\n[PHASE 3+] TIER 3: SPECIALIZATION — May 21-30")
    print("-" * 80)
    for category, repos in TIER_3_SPECIALIZATION.items():
        print(f"\n  {category} ({len(repos)} repos):")
        for repo in repos[:3]:
            print(f"    - {repo}")
        if len(repos) > 3:
            print(f"    ... +{len(repos)-3} more")

    print("\n\n[INGESTION STRATEGY]")
    print("-" * 80)
    print("""
    Phase 1 (May 12-15):
      - Priority: Enable agent autonomy
      - Method: Sequential, with dependency tracking
      - Verification: Each repo → test import → verify in RAG
      - Blockers: 4 (resolve in parallel)

    Phase 2 (May 16-20):
      - Priority: Complete data pipeline
      - Method: Parallel ingestion (10 concurrent)
      - Verification: Index size, retrieval latency checks
      - Blockers: 2

    Phase 3+ (May 21-30):
      - Priority: Specialized use cases
      - Method: Batch ingestion (50 at a time)
      - Verification: Category-level smoke tests
      - Blockers: 0

    Total: 640 repos ingested by June 30
    Estimated time: 6 weeks
    Concurrent limit: 10 repos at Phase 2+
    """)

    print("\n[INGESTION INTERFACE]")
    print("-" * 80)
    print("""
    # Single repo
    await hub.ingest_repo_from_github("owner/repo-name")

    # Batch by tier
    await hub.ingest_tier(tier="1", category="RAG & Knowledge Graphs")

    # Full phase (with blockers)
    status = await hub.ingest_phase("1", parallel=False)

    # Monitor
    stats = hub.get_ingestion_stats()  # {repos_ingested, bytes, indexed_count, avg_time}
    """)


if __name__ == "__main__":
    asyncio.run(generate_install_order())
