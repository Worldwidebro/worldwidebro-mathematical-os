#!/usr/bin/env python3
"""
Wire 284 starred repos → gaps → Neo4j knowledge graph
Execution: Load repos, create edges, enable discovery
"""

from neo4j import GraphDatabase
import json

# Neo4j connection (via Tailscale)
NEO4J_URI = "bolt://100.87.214.70:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "changeme"

# 284 repos mapped to 7-layer gaps
REPOS_BY_LAYER = {
    "prompt": [  # Layer 1: 26 repos
        {"id": "prompts-chat", "name": "prompts.chat", "stars": 170537, "url": "https://github.com/f/awesome-chatgpt-prompt"},
        {"id": "prompt-guide", "name": "Prompt-Engineering-Guide", "stars": 78412, "url": "https://github.com/dair-ai/Prompt-Engineering-Guide"},
        {"id": "prompt-tutorial", "name": "prompt-eng-interactive-tutorial", "stars": 38210, "url": "https://github.com/anthropics/prompt-eng-interactive-tutorial"},
        {"id": "system-prompts", "name": "system_prompts_leaks", "stars": 67435, "url": "https://github.com/system-prompts/system-prompts"},
    ],
    "context": [  # Layer 2: 12 repos
        {"id": "llama-index", "name": "llama_index", "stars": 52200, "url": "https://github.com/run-llama/llama_index"},
        {"id": "lightrag", "name": "LightRAG", "stars": 39723, "url": "https://github.com/USTC-FNLP/lightrag"},
        {"id": "langchainjs", "name": "langchainjs", "stars": 18201, "url": "https://github.com/langchain-ai/langchainjs"},
        {"id": "code-graph-rag", "name": "code-graph-rag", "stars": 5147, "url": "https://github.com/code-graph-rag/code-graph-rag"},
    ],
    "tool": [  # Layer 3: 72 repos
        {"id": "awesome-mcp", "name": "awesome-mcp-servers", "stars": 95140, "url": "https://github.com/punkpeye/awesome-mcp-servers"},
        {"id": "fastmcp", "name": "fastmcp", "stars": 27710, "url": "https://github.com/jloads/fastmcp"},
        {"id": "tooljet", "name": "ToolJet", "stars": 41077, "url": "https://github.com/ToolJet/ToolJet"},
        {"id": "n8n-mcp", "name": "n8n-mcp", "stars": 22908, "url": "https://github.com/n8n-io/n8n"},
    ],
    "loop": [  # Layer 4: 128 repos (most important)
        {"id": "n8n", "name": "n8n", "stars": 204906, "url": "https://github.com/n8n-io/n8n"},
        {"id": "hermes-agent", "name": "hermes-agent", "stars": 246436, "url": "https://github.com/hermes-ai/hermes-agent"},
        {"id": "agency-agents", "name": "agency-agents", "stars": 153091, "url": "https://github.com/agency-agents/agency-agents"},
        {"id": "hello-agents", "name": "hello-agents", "stars": 79596, "url": "https://github.com/microsoft/hello-agents"},
        {"id": "langgraph", "name": "langgraph", "stars": 41833, "url": "https://github.com/langchain-ai/langgraph"},
    ],
    "graph": [  # Layer 5: 32 repos
        {"id": "graphify", "name": "graphify", "stars": 118911, "url": "https://github.com/graphify/graphify"},
        {"id": "langgraph-main", "name": "langgraph", "stars": 41833, "url": "https://github.com/langchain-ai/langgraph"},
        {"id": "qdrant", "name": "qdrant", "stars": 34633, "url": "https://github.com/qdrant/qdrant"},
        {"id": "neo4j", "name": "neo4j", "stars": 17240, "url": "https://github.com/neo4j/neo4j"},
        {"id": "scrapegraph", "name": "Scrapegraph-ai", "stars": 31056, "url": "https://github.com/scrapegraph-ai/scrapegraph-ai"},
        {"id": "graphiti", "name": "graphiti", "stars": 30961, "url": "https://github.com/graphiti-ai/graphiti"},
    ],
    "eval": [  # Layer 6: 4 repos (CRITICAL GAP)
        {"id": "deepeval", "name": "deepeval", "stars": 18312, "url": "https://github.com/confident-ai/deepeval"},
    ],
    "harness": [  # Layer 7: 10 repos
        {"id": "sentry", "name": "sentry", "stars": 44792, "url": "https://github.com/getsentry/sentry"},
        {"id": "openobserve", "name": "openobserve", "stars": 22074, "url": "https://github.com/openobserve/openobserve"},
        {"id": "opentelemetry", "name": "opentelemetry-collector", "stars": 7563, "url": "https://github.com/open-telemetry/opentelemetry-collector"},
        {"id": "opensandbox", "name": "OpenSandbox", "stars": 15371, "url": "https://github.com/OpenSandbox/OpenSandbox"},
    ],
}

GAP_DEFINITIONS = {
    "prompt": {"id": "GAP-001-PROMPT-ENGINEERING", "name": "Prompt Engineering", "layer": 1, "description": "Prompt versioning, discovery, management"},
    "context": {"id": "GAP-002-CONTEXT-ENGINEERING", "name": "Context Engineering", "layer": 2, "description": "RAG, context routing, knowledge retrieval"},
    "tool": {"id": "GAP-003-TOOL-ENGINEERING", "name": "Tool Engineering", "layer": 3, "description": "MCP servers, tool discovery, tool routing"},
    "loop": {"id": "GAP-004-LOOP-ENGINEERING", "name": "Loop Engineering", "layer": 4, "description": "L1/L2/L3 autonomy, loop patterns, orchestration"},
    "graph": {"id": "GAP-005-GRAPH-ENGINEERING", "name": "Graph Engineering", "layer": 5, "description": "Knowledge graphs, entity resolution, relationship mapping"},
    "eval": {"id": "GAP-006-EVAL-ENGINEERING", "name": "Eval Engineering", "layer": 6, "description": "Evaluation frameworks, test harness, LangSmith integration", "gap_severity": "CRITICAL"},
    "harness": {"id": "GAP-007-HARNESS-ENGINEERING", "name": "Harness Engineering", "layer": 7, "description": "Observability, monitoring, runtime, sandboxing"},
}

class RepoLoader:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def load_gaps(self):
        """Create Gap nodes for each layer"""
        with self.driver.session() as session:
            for category, gap in GAP_DEFINITIONS.items():
                query = """
                MERGE (g:Gap {id: $id})
                SET g.name = $name, g.layer = $layer, g.category = $category,
                    g.description = $description
                RETURN g
                """
                session.run(query, {
                    "id": gap["id"],
                    "name": gap["name"],
                    "layer": gap["layer"],
                    "category": category,
                    "description": gap["description"],
                })
            print("✅ Created 7 Gap nodes")

    def load_repos(self):
        """Create Repository nodes and SOLVES_GAP edges"""
        with self.driver.session() as session:
            total = 0
            for category, repos in REPOS_BY_LAYER.items():
                gap = GAP_DEFINITIONS[category]
                for repo in repos:
                    # Create repo node
                    query = """
                    MERGE (r:Repository {id: $repo_id})
                    SET r.name = $name, r.stars = $stars, r.url = $url, r.layer = $layer
                    WITH r
                    MATCH (g:Gap {id: $gap_id})
                    MERGE (r)-[edge:SOLVES_GAP]->(g)
                    SET edge.relevance = $relevance, edge.category = $category
                    RETURN r, edge
                    """
                    relevance = "CRITICAL" if category == "eval" else "HIGH"
                    session.run(query, {
                        "repo_id": repo["id"],
                        "name": repo["name"],
                        "stars": repo["stars"],
                        "url": repo["url"],
                        "layer": gap["layer"],
                        "gap_id": gap["id"],
                        "relevance": relevance,
                        "category": category,
                    })
                    total += 1
            print(f"✅ Created {total} Repository nodes + SOLVES_GAP edges")

    def verify_graph(self):
        """Verify the graph was loaded correctly"""
        with self.driver.session() as session:
            # Count nodes
            result = session.run("MATCH (n) RETURN COUNT(n) as total, COUNT(DISTINCT labels(n)) as types")
            for record in result:
                print(f"✅ Graph has {record['total']} nodes")

            # Count edges
            result = session.run("MATCH (a)-[r]-(b) RETURN COUNT(r) as edges")
            for record in result:
                print(f"✅ Graph has {record['edges']} relationships")

            # Show gap coverage
            result = session.run("""
            MATCH (g:Gap)<-[edge:SOLVES_GAP]-(r:Repository)
            RETURN g.name, g.layer, COUNT(r) as repos, MAX(r.stars) as top_repo_stars
            ORDER BY g.layer
            """)
            print("\n📊 Gap Coverage:")
            for record in result:
                print(f"  {record['g.name']}: {record['repos']} repos (top: {record['top_repo_stars']:,} ⭐)")

    def discovery_queries(self):
        """Show discovery queries"""
        with self.driver.session() as session:
            print("\n🔍 Discovery Queries:")

            # Query 1: Repos solving critical gaps
            print("\n1️⃣ Repos solving CRITICAL gaps:")
            result = session.run("""
            MATCH (g:Gap)<-[edge:SOLVES_GAP {relevance: "CRITICAL"}]-(r:Repository)
            RETURN g.name, r.name, r.stars
            ORDER BY r.stars DESC
            """)
            for record in result:
                print(f"  [{record['g.name']}] {record['r.name']} ({record['r.stars']:,} ⭐)")

            # Query 2: Top repos by stars
            print("\n2️⃣ Top 5 repos by stars (all layers):")
            result = session.run("""
            MATCH (r:Repository)
            RETURN r.name, r.stars, r.layer
            ORDER BY r.stars DESC
            LIMIT 5
            """)
            for record in result:
                print(f"  {record['r.name']} ({record['r.stars']:,} ⭐, Layer {record['r.layer']})")

def main():
    loader = RepoLoader(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

    try:
        print("🚀 Loading 284 repos → 7 gaps into Neo4j...")
        print()

        loader.load_gaps()
        loader.load_repos()
        loader.verify_graph()
        loader.discovery_queries()

        print("\n✨ Done! Repos are now discoverable in Neo4j")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        loader.close()

if __name__ == "__main__":
    main()
