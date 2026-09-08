# External Integrations

**Analysis Date:** 2026-09-05

## APIs & External Services

**GitHub:**
- Integration type: Webhook ingestion
- Purpose: Route pull requests, issues, and push events to LLM models for analysis
- SDK/Client: httpx (async HTTP client)
- Auth: `GITHUB_TOKEN` environment variable
- Implementation: `_INFRASTRUCTURE/omniroute/omniroute.py` (webhook handler at `/webhooks/github`)

**OmniRoute (Internal AI Gateway):**
- Integration type: Local AI provider abstraction
- Purpose: Route requests to LiteLLM, Ollama, exo (distributed inference)
- API endpoint: http://100.87.214.70:20128
- Dashboard: http://100.87.214.70:20128/dashboard
- Auth: Admin credentials (admin@omniroute.local / _.Thewave12)
- Implementation: CLI commands via `_CLI/bin/cb omniroute`

**LiteLLM (Model Router):**
- Integration type: LLM provider abstraction layer
- Purpose: Centralized model routing with fallback chains
- API endpoint: http://100.87.214.70:4000
- Base URL env: `LITELLM_API_BASE`
- Models routed: qwen-fast (→ claude-haiku fallback), qwen-heavy (→ claude-sonnet fallback)
- Caching: Redis-based exact-match response caching
- Routing strategy: simple-shuffle (round-robin, no scoring)

**Ollama (Local Model Runtime):**
- Status: Replaced by exo (2026-07-17) — legacy integration
- Was used for: qwen2.5-coder:14b, nomic-embed-text
- Marked for cleanup (port 11434 still listed in schema but no active deployment)

**exo (Distributed MLX Inference):**
- Integration type: Native Apple Silicon model serving
- Purpose: Local inference without Ollama overhead
- API endpoint: http://100.87.214.70:52415/v1
- OpenAI-compatible: Yes (v1 endpoint)
- Current model: mlx-community/Qwen3.6-35B-A3B-5bit
- Aliases in LiteLLM: qwen-fast, qwen-heavy

## Data Storage

**Databases:**

**Neo4j (Knowledge Graph):**
- Provider: Docker image neo4j:latest
- Connection: bolt://100.87.214.70:7687
- Web UI: http://100.87.214.70:7474
- Auth: neo4j/changeme (DEFAULT — must change)
- Plugins: apoc
- Memory config: 2GB initial, 4GB max
- Persistence: `/Volumes/LaCie/neo4j/data` + `/Volumes/LaCie/neo4j/logs`
- Purpose: Relationship graph for infrastructure, agents, control planes, capabilities
- Client: neo4j (Python driver)

**Qdrant (Vector Database):**
- Provider: Docker image qdrant/qdrant:latest
- Connection: http://100.87.214.70:6333
- Storage: `/Volumes/LaCie/qdrant/storage` + snapshots
- Purpose: Semantic search + embeddings for venture data, notes, capabilities
- Client: Direct HTTP API (no Python SDK required)
- Collections: notes (15,558 vectors via Ollama nomic-embed-text), ventures

**PostgreSQL (Operational Database):**
- Provider: Docker image postgres:16
- Connection: postgres://admin:changeme@100.87.214.70:5432/infrastructure
- Auth: admin/changeme (DEFAULT — must change)
- Storage: `/Volumes/LaCie/postgres/data` + backups
- Purpose: Infrastructure state, operational logs
- Max connections: 200
- Client: psycopg2 (implied by neo4j/infrastructure scripts)

**File Storage:**
- Local filesystem only: `/Volumes/LaCie/` (4TB external drive)
- No cloud storage detected (S3, GCS, Azure Blob)
- Persistent data: Neo4j, Qdrant, PostgreSQL all store on LaCie drive

**Caching:**
- Redis (implied in LiteLLM config) — exact-match response caching for model calls
- Status: Deployed (confirmed in `_CLI/bin/cb` health checks)
- Port: 6379+

## Authentication & Identity

**Auth Provider:**
- Custom: Each service has hardcoded credentials
- No OAuth/OIDC detected
- Manual credential management required per service

**Service Credentials:**
- Neo4j: `neo4j/changeme` (INSECURE)
- PostgreSQL: `admin/changeme` (INSECURE)
- OmniRoute: `admin@omniroute.local / _.Thewave12`
- Tailscale: Token-based (user's Tailscale account)

## Monitoring & Observability

**Error Tracking:**
- Langfuse - LLM tracing + evaluation platform
  - URL: http://100.87.214.70:3003
  - Status: Running but receiving zero traffic (not wired to LiteLLM callbacks)
  - Purpose: Trace model routing decisions, track costs

**Logs:**
- Structured logging via Python logging module (level configurable via `OMNIROUTE_LOG_LEVEL`)
- Docker Compose logs: `docker logs <container>`
- Neo4j: `/Volumes/LaCie/neo4j/logs`
- Langfuse UI: Traces received at http://100.87.214.70:3003 (if callbacks enabled)

**Dashboards:**
- Grafana (observability dashboard)
  - URL: http://100.87.214.70:3011
  - Status: Running (`t7shield-grafana-1`)
  - Purpose: Metrics visualization (infrastructure-only, not yet connected to application metrics)

## CI/CD & Deployment

**Hosting:**
- Mac Studio M4 (100.87.214.70 over Tailscale SSH)
- No cloud deployment (all services run locally on Mac Studio)
- Failover: Mac Studio is single point of failure

**CI Pipeline:**
- GitHub Actions: `.github/workflows/auto-deploy.yml`
- Status: Configured but not actively used for this codebase
- Deployment model: Manual CLI commands via `_CLI/bin/cb infrastructure deploy`

## Environment Configuration

**Required env vars (at service startup):**
- `NEO4J_AUTH` — Neo4j authentication
- `NEO4J_PLUGINS` — apoc required for advanced queries
- `POSTGRES_DB` — infrastructure database name
- `POSTGRES_USER` + `POSTGRES_PASSWORD` — PostgreSQL auth
- `GITHUB_TOKEN` — GitHub webhook authentication
- `LITELLM_API_BASE` — LiteLLM router endpoint (default: http://localhost:4001)
- `NEO4J_URI` — Neo4j connection string (default: neo4j://localhost:7687)
- `OMNIROUTE_LOG_LEVEL` — Logging verbosity (default: INFO)
- `OMNIROUTE_PORT` — Server port (default: 8000)

**Secrets location:**
- Hardcoded in Docker Compose file (`_INFRASTRUCTURE/docker-compose.yml`) — not recommended for production
- Credentials in `_CLI/bin/cb` (OmniRoute login)
- No `.env` file or secret manager detected

## Webhooks & Callbacks

**Incoming:**
- GitHub webhook handler: `_INFRASTRUCTURE/omniroute/omniroute.py:/webhooks/github`
  - Events: pull_request, issues, push
  - Processing: Routes to LiteLLM models (code-review, analysis)
  - Background task: Async event processing

**Outgoing:**
- LiteLLM → Langfuse (intended but not wired)
  - Callback target: Langfuse at http://100.87.214.70:3003
  - Current status: No callbacks configured (LiteLLM config missing `success_callback`)
- OmniRoute → Neo4j (tracking only — no mutations)

## MCP Integration

**FastMCP Server:**
- File: `_MCP/fastmcp_server.py`
- Framework: FastMCP 4.0.3
- Authority: Infrastructure Control Plane (CP-027)
- Tools exposed: 9 (infrastructure_status, infrastructure_deploy, omniroute_status, neo4j_status, neo4j_wire_ontology, test_e2e, test_models, control_planes_sync, get_sector_info)
- Resources: company_brain_status
- Prompts: setup_company_brain
- Registration: `~/.claude/settings.json` (user scope)
- Python venv: `~/.venv/company-brain` (Python 3.12)

---

*Integration audit: 2026-09-05*
