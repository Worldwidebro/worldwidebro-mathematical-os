#!/usr/bin/env python3
"""
Company Brain FastMCP Server
Exposes infrastructure, agents, and control planes as MCP tools

Authority: Infrastructure Control Plane (CP-027)
Framework: FastMCP (https://github.com/PrefectHQ/fastmcp)
"""

import subprocess
import json
import os
import sys
from pathlib import Path
from typing import Optional
from datetime import datetime

# Try importing fastmcp, provide installation instructions if missing
try:
    from fastmcp import FastMCP
except ImportError:
    print("❌ FastMCP not installed")
    print("Install with: pip install fastmcp")
    print("Docs: https://gofastmcp.com")
    sys.exit(1)

# Initialize MCP server
mcp = FastMCP("Company Brain 🧠")

# Base directory for Company Brain
COMPANY_BRAIN_DIR = Path(__file__).parent.parent


@mcp.tool
def infrastructure_status() -> dict:
    """Check Company Brain infrastructure health (OmniRoute, Neo4j, Qdrant, Ollama)"""
    cmd = ["_CLI/bin/cb", "infrastructure", "status"]
    try:
        result = subprocess.run(
            cmd,
            cwd=COMPANY_BRAIN_DIR,
            capture_output=True,
            text=True,
            timeout=10
        )
        return {
            "status": "success" if result.returncode == 0 else "error",
            "output": result.stdout,
            "error": result.stderr if result.returncode != 0 else None
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool
def infrastructure_deploy(phase: str = "all") -> dict:
    """Deploy Company Brain infrastructure phases

    Phases:
    - all: Deploy all phases (1-4)
    - 1: Databases (Neo4j, Qdrant, PostgreSQL, Redis)
    - 2: Models + OmniRoute configuration
    - 3: Exo distributed inference
    - 4: Observability (Grafana, Langfuse)
    """
    cmd = ["_CLI/bin/cb", "infrastructure", "deploy", f"--phase", phase]
    try:
        result = subprocess.run(
            cmd,
            cwd=COMPANY_BRAIN_DIR,
            capture_output=True,
            text=True,
            timeout=300
        )
        return {
            "status": "success" if result.returncode == 0 else "error",
            "phase": phase,
            "output": result.stdout,
            "error": result.stderr if result.returncode != 0 else None
        }
    except Exception as e:
        return {"status": "error", "phase": phase, "error": str(e)}


@mcp.tool
def omniroute_status() -> dict:
    """Check OmniRoute AI gateway status"""
    try:
        result = subprocess.run(
            ["curl", "-s", "http://100.87.214.70:20128/health"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return {
            "status": "online" if result.returncode == 0 else "offline",
            "response": result.stdout,
            "url": "http://100.87.214.70:20128"
        }
    except Exception as e:
        return {"status": "offline", "error": str(e)}


@mcp.tool
def neo4j_status() -> dict:
    """Check Neo4j knowledge graph health"""
    cmd = ["_CLI/bin/cb", "neo4j", "status"]
    try:
        result = subprocess.run(
            cmd,
            cwd=COMPANY_BRAIN_DIR,
            capture_output=True,
            text=True,
            timeout=10
        )
        return {
            "status": "success" if result.returncode == 0 else "error",
            "output": result.stdout,
            "url": "http://100.87.214.70:7474"
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool
def neo4j_wire_ontology() -> dict:
    """Wire Neo4j ontology - create relationships between control planes"""
    cmd = ["_CLI/bin/cb", "neo4j", "wire-ontology"]
    try:
        result = subprocess.run(
            cmd,
            cwd=COMPANY_BRAIN_DIR,
            capture_output=True,
            text=True,
            timeout=30
        )
        return {
            "status": "success" if result.returncode == 0 else "error",
            "output": result.stdout,
            "error": result.stderr if result.returncode != 0 else None
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool
def test_e2e() -> dict:
    """Run end-to-end infrastructure tests"""
    cmd = ["_CLI/bin/cb", "test", "e2e"]
    try:
        result = subprocess.run(
            cmd,
            cwd=COMPANY_BRAIN_DIR,
            capture_output=True,
            text=True,
            timeout=60
        )
        return {
            "status": "success" if result.returncode == 0 else "error",
            "output": result.stdout,
            "error": result.stderr if result.returncode != 0 else None
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool
def test_models() -> dict:
    """List available models"""
    cmd = ["_CLI/bin/cb", "test", "models"]
    try:
        result = subprocess.run(
            cmd,
            cwd=COMPANY_BRAIN_DIR,
            capture_output=True,
            text=True,
            timeout=10
        )
        return {
            "status": "success" if result.returncode == 0 else "error",
            "output": result.stdout,
            "error": result.stderr if result.returncode != 0 else None
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool
def control_planes_sync() -> dict:
    """Synchronize all 6 control planes (Agents, Models, Knowledge, Financial, Infrastructure, Observability)"""
    cmd = ["_CLI/bin/cb", "control-planes", "sync"]
    try:
        result = subprocess.run(
            cmd,
            cwd=COMPANY_BRAIN_DIR,
            capture_output=True,
            text=True,
            timeout=60
        )
        return {
            "status": "success" if result.returncode == 0 else "error",
            "output": result.stdout,
            "error": result.stderr if result.returncode != 0 else None
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool
def get_sector_info(sector_id: str) -> dict:
    """Get information about a specific sector

    Args:
        sector_id: Sector ID (e.g., 'SEC-001', 'SEC-024', etc.)
    """
    registries_dir = COMPANY_BRAIN_DIR / "_REGISTRIES"
    ventures_file = registries_dir / "ventures-by-sector.yaml"

    if not ventures_file.exists():
        return {"error": f"Registry file not found: {ventures_file}"}

    try:
        import yaml
        with open(ventures_file, 'r') as f:
            data = yaml.safe_load(f)

        sector_data = data.get('ventures', {}).get(sector_id)
        if not sector_data:
            return {"error": f"Sector {sector_id} not found"}

        return {
            "sector_id": sector_id,
            "description": sector_data.get('description'),
            "opco": sector_data.get('opco'),
            "venture_count": sector_data.get('venture_count'),
            "status": "active" if sector_data.get('ventures') else "planning"
        }
    except Exception as e:
        return {"error": str(e)}


@mcp.resource("company-brain://status")
def company_brain_status() -> str:
    """Current Company Brain operational status"""
    status_file = COMPANY_BRAIN_DIR / "ACTIVATION-CHECKLIST-2026-09-02.md"
    if status_file.exists():
        with open(status_file, 'r') as f:
            return f.read()[:2000]  # First 2000 chars
    return "Status file not found"


@mcp.tool
def neo4j_query_entities(entity_type: str = "", limit: int = 50) -> dict:
    """Query Neo4j for entities by type (for Repository Intelligence System)

    Args:
        entity_type: Entity type to query (e.g., 'Capability', 'Venture', 'ExternalRepository')
        limit: Maximum results to return (default 50)

    Returns:
        List of matching entities with properties
    """
    try:
        from neo4j import GraphDatabase

        neo4j_uri = os.environ.get("NEO4J_URI", "bolt://100.87.214.70:7687")
        neo4j_user = os.environ.get("NEO4J_USER", "neo4j")
        neo4j_pass = os.environ.get("NEO4J_PASSWORD", "changeme")

        driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_pass))

        query = f"MATCH (e:{entity_type}) RETURN e LIMIT {limit}"
        with driver.session() as session:
            result = session.run(query)
            entities = [dict(record['e']) for record in result]

        driver.close()
        return {
            "status": "success",
            "entity_type": entity_type,
            "count": len(entities),
            "entities": entities
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool
def neo4j_merge_classification(repo_id: str, classification: dict) -> dict:
    """Merge repository classification into Neo4j knowledge graph

    Args:
        repo_id: Repository ID (e.g., 'EXT-REPO-000001')
        classification: Classification dict with fields like:
            - primary_capability: str
            - secondary_capabilities: [str]
            - architecture_layer: str
            - sector_relevance: [{"sector": str, "score": int}]
            - score: int
            - tier: str (CRITICAL/HIGH/USEFUL/REFERENCE/LOW/ARCHIVE)

    Returns:
        Merge result with updated node properties
    """
    try:
        from neo4j import GraphDatabase

        neo4j_uri = os.environ.get("NEO4J_URI", "bolt://100.87.214.70:7687")
        neo4j_user = os.environ.get("NEO4J_USER", "neo4j")
        neo4j_pass = os.environ.get("NEO4J_PASSWORD", "changeme")

        driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_pass))

        query = f"""
            MATCH (r:ExternalRepository {{repo_id: $repo_id}})
            SET r += $classification
            SET r.classified_at = timestamp()
            RETURN r
        """

        with driver.session() as session:
            result = session.run(query, repo_id=repo_id, classification=classification)
            record = result.single()
            if record:
                merged_node = dict(record['r'])
            else:
                merged_node = None

        driver.close()
        return {
            "status": "success" if merged_node else "not_found",
            "repo_id": repo_id,
            "merged_node": merged_node
        }
    except Exception as e:
        return {"status": "error", "repo_id": repo_id, "error": str(e)}


@mcp.tool
def omniroute_route_model(task_type: str, complexity: int = 5) -> dict:
    """Route to appropriate model via OmniRoute based on task complexity

    Args:
        task_type: Type of task ('classify', 'score', 'disposition', 'adopt')
        complexity: Complexity score (1-10, default 5)

    Returns:
        Recommended model and routing details
    """
    try:
        omniroute_url = os.environ.get("OMNIROUTE_URL", "http://100.87.214.70:20128")

        import subprocess
        result = subprocess.run(
            ["curl", "-s", f"{omniroute_url}/api/route",
             "-d", json.dumps({"task": task_type, "complexity": complexity}),
             "-H", "Content-Type: application/json"],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            data = json.loads(result.stdout)
            return {
                "status": "success",
                "task_type": task_type,
                "complexity": complexity,
                "recommended_model": data.get("model"),
                "provider": data.get("provider"),
                "estimated_cost": data.get("cost")
            }
        else:
            return {
                "status": "error",
                "task_type": task_type,
                "error": "Failed to reach OmniRoute"
            }
    except Exception as e:
        return {"status": "error", "error": str(e)}


# ============================================================================
# Phase 2: Token Measurement, Compression & Ledger Tools
# ============================================================================

@mcp.tool
def measure_tokens(text: str, encoding: str = "cl100k_base") -> dict:
    """Measure exact BPE token counts, character ratio, and baseline cloud cost

    Args:
        text: Input string to tokenize
        encoding: BPE encoding name ('cl100k_base', 'o200k_base', or model name)

    Returns:
        Exact token count, character length, characters per token, and cost estimate
    """
    try:
        from _ENGINE.token_ledger import ledger, CLOUD_INPUT_COST_PER_1K
        tokens = ledger.count_tokens(text, encoding_name=encoding)
        chars = len(text)
        cost_est = (tokens / 1000.0) * CLOUD_INPUT_COST_PER_1K
        return {
            "status": "success",
            "tokens": tokens,
            "characters": chars,
            "chars_per_token": round(chars / max(1, tokens), 2),
            "encoding": encoding,
            "estimated_cloud_input_cost_usd": round(cost_est, 6),
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool
def compress_context(text: str, mode: str = "auto") -> dict:
    """Compress context or prompt using deterministic RTK and Caveman engines

    Args:
        text: Text to compress (tool return, git diff, JSON, or conversational prompt)
        mode: Compression mode ('auto', 'rtk', 'caveman', 'both')

    Returns:
        Compressed text, tokens before/after, percentage reduction, and latency
    """
    try:
        from _ENGINE.compression import UnifiedCompressor
        compressed_text, stats = UnifiedCompressor.compress(text, mode=mode)
        return {
            "status": "success",
            "mode": stats["mode"],
            "compressed_text": compressed_text,
            "original_tokens": stats["original_tokens"],
            "compressed_tokens": stats["compressed_tokens"],
            "tokens_saved": stats["tokens_saved"],
            "savings_pct": stats["savings_pct"],
            "latency_ms": stats["latency_ms"],
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool
def token_ledger_summary() -> dict:
    """Get cumulative Company Brain token usage ledger, savings, and local vs cloud split

    Returns:
        Total transactions, tokens (input/output/cached/local/cloud), and financial savings
    """
    try:
        from _ENGINE.token_ledger import ledger
        return {
            "status": "success",
            "ledger": ledger.get_summary(),
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool
def graph_search_companies(industry: str = "", geography: str = "", revenue_range: str = "") -> dict:
    """Search Neo4j knowledge graph for companies by industry, geography, and revenue range

    Args:
        industry: Industry keyword (e.g., 'technology', 'healthcare', 'finance')
        geography: Geography/region (e.g., 'US', 'EU', 'APAC', 'North America')
        revenue_range: Revenue range (e.g., '1M-10M', '10M-100M', '100M+')

    Returns:
        List of companies matching criteria with properties (name, industry, revenue, location, etc.)
    """
    try:
        from neo4j import GraphDatabase

        neo4j_uri = os.environ.get("NEO4J_URI", "bolt://100.87.214.70:7687")
        neo4j_user = os.environ.get("NEO4J_USER", "neo4j")
        neo4j_pass = os.environ.get("NEO4J_PASSWORD", "changeme")

        driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_pass))

        # Build dynamic Cypher query with optional filters
        where_clauses = []
        params = {}

        if industry:
            where_clauses.append("LOWER(c.industry) CONTAINS LOWER($industry)")
            params["industry"] = industry

        if geography:
            where_clauses.append("LOWER(c.geography) CONTAINS LOWER($geography)")
            params["geography"] = geography

        if revenue_range:
            where_clauses.append("c.revenue_range = $revenue_range")
            params["revenue_range"] = revenue_range

        where_clause = " AND ".join(where_clauses) if where_clauses else "1=1"
        query = f"""
            MATCH (c:Company)
            WHERE {where_clause}
            RETURN c {{
                name: c.name,
                industry: c.industry,
                geography: c.geography,
                revenue_range: c.revenue_range,
                status: c.status,
                created_at: c.created_at
            }} LIMIT 50
        """

        with driver.session() as session:
            result = session.run(query, params)
            companies = [dict(record['c']) for record in result]

        driver.close()
        return {
            "status": "success",
            "query": {
                "industry": industry,
                "geography": geography,
                "revenue_range": revenue_range
            },
            "count": len(companies),
            "companies": companies
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool
def qdrant_search_similar_deals(vector: list, limit: int = 10) -> dict:
    """Search Qdrant for semantically similar deals using vector similarity

    Args:
        vector: Vector embedding (list of floats, typically 384/768 dimensions)
        limit: Maximum number of results to return (default 10)

    Returns:
        List of similar deals with scores (0-1, higher = more similar)
    """
    try:
        import requests

        qdrant_url = os.environ.get("QDRANT_URL", "http://100.87.214.70:6333")
        collection_name = "deals"  # Assumed collection name for deal embeddings

        # Search request payload
        search_request = {
            "vector": vector,
            "limit": limit,
            "with_payload": True,
            "with_vectors": False
        }

        # Execute search
        response = requests.post(
            f"{qdrant_url}/collections/{collection_name}/points/search",
            json=search_request,
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            results = data.get('result', [])

            similar_deals = []
            for item in results:
                deal = {
                    "id": item.get('id'),
                    "score": item.get('score'),
                    "deal_name": item.get('payload', {}).get('deal_name'),
                    "company": item.get('payload', {}).get('company'),
                    "stage": item.get('payload', {}).get('stage'),
                    "amount": item.get('payload', {}).get('amount'),
                    "industry": item.get('payload', {}).get('industry')
                }
                similar_deals.append(deal)

            return {
                "status": "success",
                "collection": collection_name,
                "limit": limit,
                "count": len(similar_deals),
                "deals": similar_deals
            }
        else:
            return {
                "status": "error",
                "error": f"Qdrant returned {response.status_code}",
                "details": response.text
            }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool
def get_agent_status() -> dict:
    """Get operational status of all 6 Company Brain agents

    Returns:
        List of agents with current status (active/idle/error), assigned task,
        processed count, and accuracy score
    """
    try:
        # Agent status can be sourced from:
        # 1. Neo4j Agent nodes with status relationships
        # 2. A status file / JSON registry
        # 3. A heartbeat/monitoring service

        # For now, we'll query Neo4j for Agent nodes and their latest activity
        from neo4j import GraphDatabase

        neo4j_uri = os.environ.get("NEO4J_URI", "bolt://100.87.214.70:7687")
        neo4j_user = os.environ.get("NEO4J_USER", "neo4j")
        neo4j_pass = os.environ.get("NEO4J_PASSWORD", "changeme")

        driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_pass))

        query = """
            MATCH (a:Agent)
            OPTIONAL MATCH (a)-[r:LAST_ACTIVITY]->(t:Task)
            RETURN a {
                id: a.id,
                name: a.name,
                status: a.status,
                capability: a.capability,
                last_activity: r.timestamp,
                processed_count: a.processed_count,
                accuracy_score: a.accuracy_score,
                current_task: t.name
            } as agent
            ORDER BY a.created_at DESC
            LIMIT 6
        """

        with driver.session() as session:
            result = session.run(query)
            agents = []
            for record in result:
                agent = dict(record['agent'])
                agents.append({
                    "id": agent.get('id', 'unknown'),
                    "name": agent.get('name', 'unknown'),
                    "status": agent.get('status', 'unknown'),
                    "capability": agent.get('capability', 'unknown'),
                    "task": agent.get('current_task'),
                    "processed": agent.get('processed_count', 0),
                    "accuracy": agent.get('accuracy_score', 0.0),
                    "last_activity": agent.get('last_activity')
                })

        driver.close()

        if agents:
            return {
                "status": "success",
                "agent_count": len(agents),
                "agents": agents
            }
        else:
            # Fallback: return hardcoded agent list if Neo4j is empty
            return {
                "status": "success",
                "agent_count": 6,
                "agents": [
                    {
                        "id": "AGT-013",
                        "name": "repo-classifier-agent",
                        "status": "idle",
                        "capability": "Repository Classification",
                        "task": None,
                        "processed": 0,
                        "accuracy": 0.0,
                        "last_activity": None
                    },
                    {
                        "id": "AGT-014",
                        "name": "repo-scorer-agent",
                        "status": "idle",
                        "capability": "Repository Scoring",
                        "task": None,
                        "processed": 0,
                        "accuracy": 0.0,
                        "last_activity": None
                    },
                    {
                        "id": "AGT-015",
                        "name": "repo-disposition-agent",
                        "status": "idle",
                        "capability": "Repository Disposition",
                        "task": None,
                        "processed": 0,
                        "accuracy": 0.0,
                        "last_activity": None
                    },
                    {
                        "id": "AGT-017",
                        "name": "repo-adoption-agent",
                        "status": "idle",
                        "capability": "Repository Adoption",
                        "task": None,
                        "processed": 0,
                        "accuracy": 0.0,
                        "last_activity": None
                    },
                    {
                        "id": "AGT-018",
                        "name": "repo-monitor-agent",
                        "status": "idle",
                        "capability": "Repository Monitoring",
                        "task": None,
                        "processed": 0,
                        "accuracy": 0.0,
                        "last_activity": None
                    },
                    {
                        "id": "AGT-019",
                        "name": "buzz-sync-agent",
                        "status": "idle",
                        "capability": "Buzz Event Sync",
                        "task": None,
                        "processed": 0,
                        "accuracy": 0.0,
                        "last_activity": None
                    }
                ]
            }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "fallback": "Unable to query agent status from Neo4j"
        }


@mcp.tool
def omniroute_invoke_research_agent(
    query: str,
    company_context: str = "",
    model: str = "qwen-heavy"
) -> dict:
    """Invoke OmniRoute research agent for deal flow intelligence

    Args:
        query: Research question (e.g., "What are top SaaS healthcare companies?")
        company_context: Optional company/industry context (JSON string)
        model: Model to use (qwen-heavy for research, default for faster)

    Returns:
        Research findings with sources and confidence scores
    """
    try:
        import asyncio
        from _MCP.omniroute_agents import OmniRouteClient, DealFlowOSAgents

        async def run():
            client = OmniRouteClient()
            agents = DealFlowOSAgents(client)
            company_ctx = None
            if company_context:
                try:
                    company_ctx = json.loads(company_context)
                except json.JSONDecodeError:
                    company_ctx = {"raw": company_context}
            return await agents.invoke_research_agent(query, company_ctx)

        return asyncio.run(run())
    except Exception as e:
        return {"status": "error", "error": str(e), "query": query}


@mcp.tool
def omniroute_invoke_qualification_agent(company_data: str) -> dict:
    """Invoke OmniRoute qualification agent to score and qualify leads

    Args:
        company_data: Company information as JSON string
                     {name, revenue, employees, industry, location, signals, ...}

    Returns:
        Qualification score (0-100), fit analysis, decision (QUALIFY/MAYBE/REJECT)
    """
    try:
        import asyncio
        from _MCP.omniroute_agents import OmniRouteClient, DealFlowOSAgents

        async def run():
            client = OmniRouteClient()
            agents = DealFlowOSAgents(client)
            try:
                company = json.loads(company_data)
            except json.JSONDecodeError:
                return {
                    "status": "error",
                    "message": "Invalid JSON in company_data",
                    "company_data": company_data
                }
            return await agents.invoke_qualification_agent(company)

        return asyncio.run(run())
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool
def omniroute_invoke_outreach_agent(
    qualified_leads: str,
    campaign_context: str = ""
) -> dict:
    """Invoke OmniRoute outreach agent to draft personalized sequences

    Args:
        qualified_leads: JSON array of qualified leads
                        [{name, company, role, industry, signals, ...}, ...]
        campaign_context: Optional campaign context (JSON string)
                         {value_prop, product_focus, timeline, ...}

    Returns:
        Outreach sequences with email copy, timing, follow-up cadence
    """
    try:
        import asyncio
        from _MCP.omniroute_agents import OmniRouteClient, DealFlowOSAgents

        async def run():
            client = OmniRouteClient()
            agents = DealFlowOSAgents(client)
            try:
                leads = json.loads(qualified_leads)
                if not isinstance(leads, list):
                    leads = [leads]
            except json.JSONDecodeError:
                return {
                    "status": "error",
                    "message": "Invalid JSON in qualified_leads"
                }

            campaign_ctx = None
            if campaign_context:
                try:
                    campaign_ctx = json.loads(campaign_context)
                except json.JSONDecodeError:
                    campaign_ctx = {"raw": campaign_context}

            return await agents.invoke_outreach_agent(leads, campaign_ctx)

        return asyncio.run(run())
    except Exception as e:
        return {"status": "error", "error": str(e)}




# ============================================================================
# Qdrant Deal Discovery (KG-048 Vector Semantic Search)
# ============================================================================

@mcp.tool
def qdrant_embed_company_profile(company_data: dict) -> dict:
    """Embed company profile using Ollama for semantic search

    Args:
        company_data: Dict with:
          - name: Company name (required)
          - description: Business description
          - industry: Industry/sector
          - location: Geographic location
          - capabilities: List of services/products

    Returns:
        Dict with:
          - status: success/error
          - embedding: 768-dim vector from nomic-embed-text
          - company_name: Name that was embedded
          - timestamp: When embedding was generated
    """
    try:
        from _MCP.qdrant_deal_discovery import get_qdrant_client

        client = get_qdrant_client()
        embedding = client.embed_company_profile(company_data)

        return {
            "status": "success",
            "embedding": embedding,
            "company_name": company_data.get("name"),
            "embedding_model": "nomic-embed-text",
            "vector_dim": len(embedding),
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "company_name": company_data.get("name")
        }


@mcp.tool
def qdrant_search_similar_companies(company_vector: list,
                                    limit: int = 10,
                                    score_threshold: float = 0.5) -> dict:
    """Search for similar companies/deals by vector embedding

    Use this to find comparable deals for deal structuring or market analysis.

    Args:
        company_vector: 768-dim embedding from qdrant_embed_company_profile()
        limit: Max results to return (default 10)
        score_threshold: Min similarity score 0-1 (default 0.5)

    Returns:
        Dict with:
          - status: success/error
          - count: Number of matches found
          - matches: List of similar deals with:
              - deal_id: Qdrant point ID
              - company_name: Name of similar company
              - similarity_pct: 0-100 match score
              - context: Industry, location, deal type, etc.
    """
    try:
        from _MCP.qdrant_deal_discovery import get_qdrant_client

        client = get_qdrant_client()
        matches = client.search_similar_companies(company_vector, limit, score_threshold)

        return {
            "status": "success",
            "count": len(matches),
            "matches": [
                {
                    "deal_id": m.deal_id,
                    "company_name": m.company_name,
                    "similarity_pct": m.similarity_pct,
                    "similarity_score": round(m.score, 4),
                    "context": m.context
                }
                for m in matches
            ],
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "count": 0,
            "matches": []
        }


@mcp.tool
def qdrant_score_deal_similarity(deal_a_id: str, deal_b_id: str) -> dict:
    """Calculate cosine similarity between two deals

    Use this in Deal Structuring Lab to find comparable transactions.

    Args:
        deal_a_id: First deal Qdrant point ID
        deal_b_id: Second deal Qdrant point ID

    Returns:
        Dict with:
          - status: success/error
          - similarity_score: 0-1 (1 = identical)
          - similarity_pct: 0-100
          - interpretation: Human readable similarity level
          - deal_a / deal_b: Company name and deal type
    """
    try:
        from _MCP.qdrant_deal_discovery import get_qdrant_client

        client = get_qdrant_client()
        result = client.score_deal_similarity(deal_a_id, deal_b_id)

        if "error" in result:
            return {
                "status": "error",
                "error": result.get("error"),
                "deal_a_id": deal_a_id,
                "deal_b_id": deal_b_id
            }

        return {
            "status": "success",
            "similarity_score": result.get("similarity_score"),
            "similarity_pct": result.get("similarity_pct"),
            "interpretation": result.get("interpretation"),
            "deal_a": result.get("deal_a"),
            "deal_b": result.get("deal_b"),
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "deal_a_id": deal_a_id,
            "deal_b_id": deal_b_id
        }


@mcp.tool
def qdrant_search_by_text(query_text: str,
                          limit: int = 10,
                          score_threshold: float = 0.5) -> dict:
    """Search for similar deals using natural language query

    Example: "construction companies in Texas" finds all similar companies.

    Args:
        query_text: Natural language search query
        limit: Max results (default 10)
        score_threshold: Min similarity 0-1 (default 0.5)

    Returns:
        Dict with matches list (same format as qdrant_search_similar_companies)
    """
    try:
        from _MCP.qdrant_deal_discovery import get_qdrant_client

        client = get_qdrant_client()
        matches = client.search_by_text(query_text, limit, score_threshold)

        return {
            "status": "success",
            "query": query_text,
            "count": len(matches),
            "matches": [
                {
                    "deal_id": m.deal_id,
                    "company_name": m.company_name,
                    "similarity_pct": m.similarity_pct,
                    "context": m.context
                }
                for m in matches
            ],
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "query": query_text,
            "count": 0,
            "matches": []
        }

@mcp.tool
def omniroute_agent_status() -> dict:
    """Get status of all 6 DealFlowOS agents

    Returns:
        Status of: research, qualification, outreach, prospect sourcing,
                  deal analysis, outreach optimization agents
    """
    try:
        from _MCP.omniroute_agents import DealFlowOSAgents, OmniRouteClient

        client = OmniRouteClient()
        agents = DealFlowOSAgents(client)
        return agents.get_agent_status()
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }


@mcp.prompt
def setup_company_brain() -> str:
    """Prompt for setting up Company Brain infrastructure"""
    return """You are assisting with Company Brain infrastructure setup.

Available control planes:
- CP-006: Agent Control Plane (routing agents to models)
- CP-007: Model Control Plane (model selection, fallback)
- CP-013: Knowledge Control Plane (embeddings, graph)
- CP-020: Financial Control Plane (cost tracking)
- CP-027: Infrastructure Control Plane (databases, services)
- CP-029: Observability (monitoring, tracing)

Available commands via the Company Brain MCP server:
- infrastructure_status(): Check health of all services
- infrastructure_deploy(phase): Deploy databases, models, or observability
- omniroute_status(): Check AI gateway
- neo4j_status(): Check knowledge graph
- test_e2e(): Run integration tests
- control_planes_sync(): Synchronize all 6 planes

Agent Orchestration Tools:
- graph_search_companies(industry, geography, revenue_range): Query companies from knowledge graph
- qdrant_search_similar_deals(vector, limit): Find similar deals via semantic search
- get_agent_status(): Check operational status of all 6 agents

Start by running infrastructure_status() to assess current state."""


if __name__ == "__main__":
    print("🚀 Company Brain FastMCP Server", file=sys.stderr)
    print("=" * 50, file=sys.stderr)
    print("Authority: Infrastructure Control Plane (CP-027)", file=sys.stderr)
    print("Framework: FastMCP (https://gofastmcp.com)", file=sys.stderr)
    print("", file=sys.stderr)
    print("Available tools:", file=sys.stderr)
    print("  # Infrastructure", file=sys.stderr)
    print("  - infrastructure_status()", file=sys.stderr)
    print("  - infrastructure_deploy(phase)", file=sys.stderr)
    print("  - test_e2e()", file=sys.stderr)
    print("  - test_models()", file=sys.stderr)
    print("  # OmniRoute & Neo4j", file=sys.stderr)
    print("  - omniroute_status()", file=sys.stderr)
    print("  - omniroute_route_model(task_type, complexity)", file=sys.stderr)
    print("  - neo4j_status()", file=sys.stderr)
    print("  - neo4j_wire_ontology()", file=sys.stderr)
    print("  - neo4j_query_entities(entity_type, limit)", file=sys.stderr)
    print("  - neo4j_merge_classification(repo_id, classification)", file=sys.stderr)
    print("  # Agent Orchestration (NEW)", file=sys.stderr)
    print("  - graph_search_companies(industry, geography, revenue_range)", file=sys.stderr)
    print("  - qdrant_search_similar_deals(vector, limit)", file=sys.stderr)
    print("  - get_agent_status()", file=sys.stderr)
    print("  # Control Planes", file=sys.stderr)
    print("  - control_planes_sync()", file=sys.stderr)
    print("  - get_sector_info(sector_id)", file=sys.stderr)
    print("  # Phase 2: Token Efficiency & Compression", file=sys.stderr)
    print("  - measure_tokens(text, encoding)", file=sys.stderr)
    print("  - compress_context(text, mode)", file=sys.stderr)
    print("  - token_ledger_summary()", file=sys.stderr)
    print("  # Qdrant Semantic Deal Discovery (KG-048)", file=sys.stderr)
    print("  - qdrant_embed_company_profile(company_data)", file=sys.stderr)
    print("  - qdrant_search_similar_companies(company_vector, limit)", file=sys.stderr)
    print("  - qdrant_score_deal_similarity(deal_a_id, deal_b_id)", file=sys.stderr)
    print("  - qdrant_search_by_text(query_text, limit)", file=sys.stderr)
    print("  # DealFlowOS AI Agents (via OmniRoute)", file=sys.stderr)
    print("  - omniroute_invoke_research_agent(query, company_context)", file=sys.stderr)
    print("  - omniroute_invoke_qualification_agent(company_data)", file=sys.stderr)
    print("  - omniroute_invoke_outreach_agent(qualified_leads, campaign_context)", file=sys.stderr)
    print("  - omniroute_agent_status()", file=sys.stderr)
    print("", file=sys.stderr)
    print("Available resources:", file=sys.stderr)
    print("  - company_brain_status", file=sys.stderr)
    print("", file=sys.stderr)
    print("Available prompts:", file=sys.stderr)
    print("  - setup_company_brain", file=sys.stderr)
    print("", file=sys.stderr)
    print("Starting server on stdio...", file=sys.stderr)
    print("=" * 50, file=sys.stderr)
    mcp.run()

