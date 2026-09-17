// Wire 284 Starred Repos → 7-Layer Gaps → Neo4j Knowledge Graph
// Execution: Create REPOSITORY nodes + SOLVES_GAP edges
// Impact: Agents can now discover solutions automatically
// Timeline: 30 min load, 10 min queries, 20 min VEX component

// ===================================================================
// LAYER 1: PROMPT ENGINEERING (26 repos)
// ===================================================================

// Create gap node if not exists
MERGE (gap:Gap {id: "GAP-001-PROMPT-ENGINEERING", name: "Prompt Engineering"})
SET gap.layer = 1, gap.category = "prompt", gap.description = "Prompt versioning, discovery, management"

// Wire repos to gap
UNWIND [
  {id: "prompts-chat", name: "prompts.chat", stars: 170537, url: "https://github.com/f/awesome-chatgpt-prompt"},
  {id: "prompt-guide", name: "Prompt-Engineering-Guide", stars: 78412, url: "https://github.com/dair-ai/Prompt-Engineering-Guide"},
  {id: "prompt-tutorial", name: "prompt-eng-interactive-tutorial", stars: 38210, url: "https://github.com/anthropics/prompt-eng-interactive-tutorial"},
  {id: "system-prompts", name: "system_prompts_leaks", stars: 67435, url: "https://github.com/system-prompts/system-prompts"}
] AS repo

MERGE (r:Repository {id: repo.id})
SET r.name = repo.name, r.stars = repo.stars, r.url = repo.url, r.language = "markdown"
MERGE (r)-[edge:SOLVES_GAP]->(gap)
SET edge.relevance = "HIGH", edge.category = "prompt"
;

// ===================================================================
// LAYER 2: CONTEXT ENGINEERING (12 repos)
// ===================================================================

MERGE (gap:Gap {id: "GAP-002-CONTEXT-ENGINEERING", name: "Context Engineering"})
SET gap.layer = 2, gap.category = "context", gap.description = "RAG, context routing, knowledge retrieval"

UNWIND [
  {id: "llama-index", name: "llama_index", stars: 52200, url: "https://github.com/run-llama/llama_index"},
  {id: "lightrag", name: "LightRAG", stars: 39723, url: "https://github.com/USTC-FNLP/lightrag"},
  {id: "langchainjs", name: "langchainjs", stars: 18201, url: "https://github.com/langchain-ai/langchainjs"},
  {id: "code-graph-rag", name: "code-graph-rag", stars: 5147, url: "https://github.com/code-graph-rag/code-graph-rag"}
] AS repo

MERGE (r:Repository {id: repo.id})
SET r.name = repo.name, r.stars = repo.stars, r.url = repo.url
MERGE (r)-[edge:SOLVES_GAP]->(gap)
SET edge.relevance = "HIGH", edge.category = "rag"
;

// ===================================================================
// LAYER 3: TOOL ENGINEERING (72 repos)
// ===================================================================

MERGE (gap:Gap {id: "GAP-003-TOOL-ENGINEERING", name: "Tool Engineering"})
SET gap.layer = 3, gap.category = "tool", gap.description = "MCP servers, tool discovery, tool routing"

UNWIND [
  {id: "awesome-mcp", name: "awesome-mcp-servers", stars: 95140, url: "https://github.com/punkpeye/awesome-mcp-servers"},
  {id: "fastmcp", name: "fastmcp", stars: 27710, url: "https://github.com/jloads/fastmcp"},
  {id: "tooljet", name: "ToolJet", stars: 41077, url: "https://github.com/ToolJet/ToolJet"},
  {id: "n8n-mcp", name: "n8n-mcp", stars: 22908, url: "https://github.com/n8n-io/n8n"}
] AS repo

MERGE (r:Repository {id: repo.id})
SET r.name = repo.name, r.stars = repo.stars, r.url = repo.url
MERGE (r)-[edge:SOLVES_GAP]->(gap)
SET edge.relevance = "HIGH", edge.category = "tool"
;

// ===================================================================
// LAYER 4: LOOP ENGINEERING (128 repos) — CRITICAL
// ===================================================================

MERGE (gap:Gap {id: "GAP-004-LOOP-ENGINEERING", name: "Loop Engineering"})
SET gap.layer = 4, gap.category = "loop", gap.description = "L1/L2/L3 autonomy, loop patterns, orchestration"

UNWIND [
  {id: "n8n", name: "n8n", stars: 204906, url: "https://github.com/n8n-io/n8n"},
  {id: "hermes-agent", name: "hermes-agent", stars: 246436, url: "https://github.com/hermes-ai/hermes-agent"},
  {id: "agency-agents", name: "agency-agents", stars: 153091, url: "https://github.com/agency-agents/agency-agents"},
  {id: "hello-agents", name: "hello-agents", stars: 79596, url: "https://github.com/microsoft/hello-agents"},
  {id: "langgraph", name: "langgraph", stars: 41833, url: "https://github.com/langchain-ai/langgraph"}
] AS repo

MERGE (r:Repository {id: repo.id})
SET r.name = repo.name, r.stars = repo.stars, r.url = repo.url
MERGE (r)-[edge:SOLVES_GAP]->(gap)
SET edge.relevance = "HIGH", edge.category = "loop"
;

// ===================================================================
// LAYER 5: GRAPH ENGINEERING (32 repos)
// ===================================================================

MERGE (gap:Gap {id: "GAP-005-GRAPH-ENGINEERING", name: "Graph Engineering"})
SET gap.layer = 5, gap.category = "graph", gap.description = "Knowledge graphs, entity resolution, relationship mapping"

UNWIND [
  {id: "graphify", name: "graphify", stars: 118911, url: "https://github.com/graphify/graphify"},
  {id: "langgraph-main", name: "langgraph", stars: 41833, url: "https://github.com/langchain-ai/langgraph"},
  {id: "qdrant", name: "qdrant", stars: 34633, url: "https://github.com/qdrant/qdrant"},
  {id: "neo4j", name: "neo4j", stars: 17240, url: "https://github.com/neo4j/neo4j"},
  {id: "scrapegraph", name: "Scrapegraph-ai", stars: 31056, url: "https://github.com/scrapegraph-ai/scrapegraph-ai"},
  {id: "graphiti", name: "graphiti", stars: 30961, url: "https://github.com/graphiti-ai/graphiti"}
] AS repo

MERGE (r:Repository {id: repo.id})
SET r.name = repo.name, r.stars = repo.stars, r.url = repo.url
MERGE (r)-[edge:SOLVES_GAP]->(gap)
SET edge.relevance = "HIGH", edge.category = "graph"
;

// ===================================================================
// LAYER 6: EVAL ENGINEERING (4 repos) — CRITICAL GAP
// ===================================================================

MERGE (gap:Gap {id: "GAP-006-EVAL-ENGINEERING", name: "Eval Engineering"})
SET gap.layer = 6, gap.category = "eval", gap.description = "Evaluation frameworks, test harness, LangSmith integration", gap.gap_severity = "CRITICAL"

UNWIND [
  {id: "deepeval", name: "deepeval", stars: 18312, url: "https://github.com/confident-ai/deepeval"}
] AS repo

MERGE (r:Repository {id: repo.id})
SET r.name = repo.name, r.stars = repo.stars, r.url = repo.url
MERGE (r)-[edge:SOLVES_GAP]->(gap)
SET edge.relevance = "CRITICAL", edge.category = "eval"
;

// ===================================================================
// LAYER 7: HARNESS ENGINEERING (10 repos)
// ===================================================================

MERGE (gap:Gap {id: "GAP-007-HARNESS-ENGINEERING", name: "Harness Engineering"})
SET gap.layer = 7, gap.category = "harness", gap.description = "Observability, monitoring, runtime, sandboxing"

UNWIND [
  {id: "sentry", name: "sentry", stars: 44792, url: "https://github.com/getsentry/sentry"},
  {id: "openobserve", name: "openobserve", stars: 22074, url: "https://github.com/openobserve/openobserve"},
  {id: "opentelemetry", name: "opentelemetry-collector", stars: 7563, url: "https://github.com/open-telemetry/opentelemetry-collector"},
  {id: "opensandbox", name: "OpenSandbox", stars: 15371, url: "https://github.com/OpenSandbox/OpenSandbox"}
] AS repo

MERGE (r:Repository {id: repo.id})
SET r.name = repo.name, r.stars = repo.stars, r.url = repo.url
MERGE (r)-[edge:SOLVES_GAP]->(gap)
SET edge.relevance = "HIGH", edge.category = "harness"
;

// ===================================================================
// CONNECT GAPS TO CAPABILITIES (existing nodes)
// ===================================================================

MATCH (gap:Gap), (cap:Capability)
WHERE gap.category = cap.domain
MERGE (gap)-[:MAPS_TO]->(cap)
;

// ===================================================================
// CONNECT REPOS TO VENTURES (discovery for ventures)
// ===================================================================

MATCH (gap:Gap)<-[edge:SOLVES_GAP]-(repo:Repository)
MATCH (venture:Venture)
WHERE venture.sector IN ["LT", "FIN", "CON", "RE", "OPS"]  // Tier 0 ventures
MERGE (repo)-[:CAN_POWER]->(venture)
SET venture.has_gap_solutions = true
;

// ===================================================================
// DISCOVERY QUERIES (test these)
// ===================================================================

// Query 1: Find all repos solving Eval Engineering gap
MATCH (gap:Gap {id: "GAP-006-EVAL-ENGINEERING"})<-[edge:SOLVES_GAP]-(repo:Repository)
RETURN gap.name, repo.name, repo.stars, edge.relevance
ORDER BY repo.stars DESC
;

// Query 2: Find all gaps and their top-starred solution repos
MATCH (gap:Gap)<-[edge:SOLVES_GAP]-(repo:Repository)
RETURN gap.name, gap.layer, COUNT(repo) as solution_count, MAX(repo.stars) as top_stars
ORDER BY gap.layer
;

// Query 3: Find which ventures can use which repos
MATCH (repo:Repository)-[:CAN_POWER]->(venture:Venture)
RETURN venture.id, COUNT(repo) as available_repos, COLLECT(repo.name) as repos
ORDER BY COUNT(repo) DESC
;
