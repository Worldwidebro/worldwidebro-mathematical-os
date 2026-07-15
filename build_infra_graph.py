#!/usr/bin/env python3
"""
build_infra_graph.py — Enrich Neo4j with infrastructure nodes (Docker services,
Ollama, Tailscale, FCC), MCP servers, and Skills. MERGE-only enrichment
that never wipes shared nodes.

Neo4j: bolt://localhost:7687  (neo4j / ventures2026)

Usage:
  python3 build_infra_graph.py          # enrich
  python3 build_infra_graph.py --stats  # node/edge counts
"""
import argparse
import json
import os
from neo4j import GraphDatabase

DOCS = "/Users/acebless/Documents"
URI = "bolt://localhost:7687"
AUTH = ("neo4j", "ventures2026")

# === DATA DEFINITIONS ===

INFRASTRUCTURE = [
    {"name": "Docker Compose", "type": "Infrastructure", "role": "container orchestration", "port": None,
     "capabilities": ["devtools", "automation"]},
    {"name": "Neo4j", "type": "Infrastructure", "role": "knowledge graph database (ventures, repos, capabilities)", "port": 7474,
     "capabilities": ["graph", "database"]},
    {"name": "Redis", "type": "Infrastructure", "role": "caching, pub/sub agent coordination", "port": 6379,
     "capabilities": ["automation"]},
    {"name": "PostgreSQL", "type": "Infrastructure", "role": "relational database for Twenty CRM + data backend", "port": 5432,
     "capabilities": ["database"]},
    {"name": "Qdrant", "type": "Infrastructure", "role": "vector store for semantic search (notes + repositories)", "port": 6333,
     "capabilities": ["search", "rag"]},
    {"name": "Grafana", "type": "Infrastructure", "role": "dashboarding and visualization platform", "port": 3001,
     "capabilities": ["dashboard", "monitoring"]},
    {"name": "LiteLLM", "type": "Infrastructure", "role": "OpenAI-compatible LLM proxy / model router", "port": 4000,
     "capabilities": ["llm"]},
    {"name": "Ollama", "type": "Infrastructure", "role": "local LLM inference + embeddings (nomic-embed, qwen3:8b, qwen2.5:32b)", "port": 11434,
     "capabilities": ["llm", "rag", "agent"]},
    {"name": "Tailscale", "type": "Infrastructure", "role": "VPN network layer connecting all devices and services privately", "port": None,
     "capabilities": ["security", "automation"]},
    {"name": "FCC (Free Claude Code)", "type": "Infrastructure", "role": "local model routing: NVIDIA NIM (DeepSeek V4 Pro) + Ollama (qwen3:8b)", "port": None,
     "capabilities": ["llm", "agent"]},
    {"name": "Twenty CRM", "type": "Infrastructure", "role": "cross-portfolio CRM tracking 712 ventures", "port": 3002,
     "capabilities": ["crm", "portfolio"]},
]

MCP_SERVERS = {
    "airtable":     {"category": "database", "capabilities": ["database"]},
    "clickup":      {"category": "task_management", "capabilities": ["workspace"]},
    "github":       {"category": "repository", "capabilities": ["devtools"]},
    "gmail":        {"category": "communication", "capabilities": ["notifications"]},
    "google_calendar": {"category": "scheduling", "capabilities": ["scheduling"]},
    "google_drive": {"category": "storage", "capabilities": ["workspace"]},
    "graphify":     {"category": "knowledge_graph", "capabilities": ["graph", "search"]},
    "hubspot":      {"category": "crm", "capabilities": ["crm"]},
    "make":         {"category": "automation", "capabilities": ["automation"]},
    "memory":       {"category": "context", "capabilities": ["search", "graph"]},
    "notion":       {"category": "documentation", "capabilities": ["analytics", "database"]},
    "ollama":       {"category": "llm", "capabilities": ["llm", "rag"]},
    "slack":        {"category": "communication", "capabilities": ["notifications"]},
    "stripe":       {"category": "payments", "capabilities": ["payments"]},
    "supabase":     {"category": "database", "capabilities": ["database", "graph"]},
    "tavily":       {"category": "search", "capabilities": ["search"]},
    "vercel":       {"category": "deployment", "capabilities": ["devtools"]},
    "zapier":       {"category": "automation", "capabilities": ["automation", "devtools", "llm", "workspace"]},
}

SKILL_CATEGORIES = [
    {"name": "superpowers-skills", "count": 12, "categories": ["agent", "automation"]},
    {"name": "everything-claude-code", "count": 183, "categories": ["agent", "devtools", "automation", "llm"]},
    {"name": "composio-integrations", "count": 832, "categories": ["automation", "api", "workspace"]},
    {"name": "ui-ux-design", "count": 15, "categories": ["dashboard"]},
    {"name": "taste-design", "count": 12, "categories": ["dashboard", "analytics"]},
    {"name": "anthropic-official", "count": 8, "categories": ["llm", "agent", "automation"]},
    {"name": "claude-mem", "count": 8, "categories": ["search", "graph", "agent"]},
    {"name": "agent-skills", "count": 86, "categories": ["agent", "automation", "analytics"]},
    {"name": "crewai-skills", "count": 4, "categories": ["agent", "automation"]},
    {"name": "brand-voice", "count": 1, "categories": ["workspace"]},
    {"name": "market-research", "count": 1, "categories": ["analytics", "search"]},
    {"name": "lead-intelligence", "count": 1, "categories": ["crm", "search"]},
    {"name": "seo", "count": 1, "categories": ["analytics"]},
    {"name": "content-engine", "count": 1, "categories": ["automation", "workspace"]},
    {"name": "investor-materials", "count": 1, "categories": ["portfolio"]},
    {"name": "knowledge-ops", "count": 1, "categories": ["search", "workspace"]},
    {"name": "video-editing", "count": 1, "categories": ["automation"]},
    {"name": "planning-with-files", "count": 1, "categories": ["agent", "automation"]},
]


def driver():
    return GraphDatabase.driver(URI, auth=AUTH)


def build():
    d = driver()
    with d.session() as s:
        # 1. Infrastructure nodes
        for infra in INFRASTRUCTURE:
            s.run("""
            MERGE (n:Infrastructure {name: $name})
            SET n.type = $type, n.role = $role, n.port = $port
            """, name=infra["name"], type=infra["type"], role=infra["role"], port=infra["port"])
            for cap in infra["capabilities"]:
                s.run("""
                MATCH (n:Infrastructure {name: $name})
                MATCH (c:Capability {name: $cap})
                MERGE (n)-[:PROVIDES]->(c)
                """, name=infra["name"], cap=cap)

        # 2. MCP Server nodes
        for name, meta in MCP_SERVERS.items():
            s.run("""
            MERGE (m:MCP {name: $name})
            SET m.category = $category
            """, name=name, category=meta["category"])
            for cap in meta["capabilities"]:
                s.run("""
                MATCH (m:MCP {name: $name})
                MATCH (c:Capability {name: $cap})
                MERGE (m)-[:PROVIDES]->(c)
                """, name=name, cap=cap)

        # 3. Skill nodes
        for skill in SKILL_CATEGORIES:
            s.run("""
            MERGE (sk:Skill {name: $name})
            SET sk.count = $count
            """, name=skill["name"], count=skill["count"])
            for cat in skill["categories"]:
                s.run("""
                MATCH (sk:Skill {name: $name})
                MATCH (c:Capability {name: $cap})
                MERGE (sk)-[:IMPLEMENTS]->(c)
                """, name=skill["name"], cap=cat)

        # 4. Link Infrastructure → MCP (hosted_by)
        infra_mcp_map = {
            "neo4j": "graphify",
            "ollama": "ollama",
            "postgres": "supabase",
            "litellm": "ollama",
        }
        for infra_name, mcp_name in infra_mcp_map.items():
            s.run("""
            MATCH (i:Infrastructure {name: $infra})
            MATCH (m:MCP {name: $mcp})
            MERGE (m)-[:HOSTED_BY]->(i)
            """, infra=infra_name, mcp=mcp_name)

        # 5. Link MCP → Capabilities for all 27 canonical capabilities
        # Also ensure all canonical capabilities exist
        caps = ["api", "database", "authentication", "dashboard", "monitoring", "portfolio",
                "security", "graph", "payments", "workspace", "construction", "fashion-design",
                "agent", "llm", "mcp", "rag", "search", "scheduling", "notifications", "ocr",
                "crm", "analytics", "machine-learning", "automation", "devtools", "forms",
                "equity-management"]
        for cap in caps:
            s.run("MERGE (c:Capability {name: $cap})", cap=cap)

    stats(d)
    d.close()


def stats(d=None):
    own = d is None
    d = d or driver()
    with d.session() as s:
        for label in ["Infrastructure", "MCP", "Skill", "Capability"]:
            n = s.run(f"MATCH (n:{label}) RETURN count(n) AS c").single()["c"]
            print(f"  {label:16} {n}")
        for rel in ["PROVIDES", "HOSTED_BY", "IMPLEMENTS"]:
            n = s.run(f"MATCH ()-[r:{rel}]->() RETURN count(r) AS c").single()["c"]
            print(f"  [{rel}]   {n}")
    if own:
        d.close()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()
    if a.stats:
        stats()
    else:
        build()
