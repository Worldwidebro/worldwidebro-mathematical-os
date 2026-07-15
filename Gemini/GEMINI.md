# GEMINI.md

This file defines the project schema, tech stack, and execution rules for the Gemini CLI and general coding agents maintaining the Operations Control Dashboard.

## Tech Stack
- **Frontend**: Pure HTML5 (semantic structure), Vanilla CSS3 (glassmorphic layout grid, theme variables), and JavaScript (dynamic state filters, localStorage bookmarks).
- **Backend**: Python 3.11+ using standard `http.server`, `zipfile`, `shutil`, `csv`, and `reportlab` (PDF rendering).
- **Control Plane Gateway**: Model Context Protocol (MCP) server listening on port `8001`.

## File Schema
- **[index.html](file:///Users/acebless/Documents/Gemini/index.html)**: Core layout, navigation tabs, statistics panels, search boxes, and tables.
- **[style.css](file:///Users/acebless/Documents/Gemini/style.css)**: Holds theme CSS variables (default dark/light), grids, cards, tables, and responsive media queries.
- **[app.js](file:///Users/acebless/Documents/Gemini/app.js)**: State engine, static resources database, localStorage sync, and REST API fetch wrapper.
- **[server.py](file:///Users/acebless/Documents/Gemini/server.py)**: Operational server backend running on port `8000`.
- **[README.md](file:///Users/acebless/Documents/Gemini/README.md)**: Main user documentation and resources list.
- **[registry/](file:///Users/acebless/Documents/Gemini/registry)**: Folder hosting YAML catalogs (`repositories.yaml`, `capabilities.yaml`, `agents.yaml`, `integrations.yaml`).
- **[services/](file:///Users/acebless/Documents/Gemini/services)**: Folder hosting MCP server bindings (`mcp_gateway.py`) and graph builders (`capability_graph.py`).

## Operations Backend API
The Python backend exposes the following endpoints:
- `GET /api/capabilities`: Serves capability registries (`capabilities-catalog.json` and `capability_vocabulary.json`).
- `GET /api/repositories`: Serves the list of active repositories parsed from `repositories.csv`.
- `GET /api/registry/repositories`: Serves parsed `repositories.yaml` YAML database content.
- `GET /api/registry/capabilities`: Serves parsed `capabilities.yaml` YAML database content.
- `GET /api/registry/agents`: Serves parsed `agents.yaml` YAML database content.
- `GET /api/registry/integrations`: Serves parsed `integrations.yaml` YAML database content.
- `GET /api/graph/data`: Re-compiles capabilities with `capability_graph.py` and returns integrations maps.
- `POST /api/zip`: Archives folders within `/Users/acebless/Documents/` (arg: `{"path": "relative/path"}`).
- `POST /api/move`: Moves files safely (args: `{"src": "source", "dest": "destination"}`).
- `POST /api/pdf`: Compiles the active system capabilities registry into `/Gemini/reports/capabilities_report.pdf` using ReportLab.
- `POST /api/audit`: Performs regulatory compliance auditing on campaign script manifests against ad rules (arg: `{"campaign": "folder_name"}`).

## Environment & Tracing Setup
For tracing with LangGraph/Deep Agents, export these variables to route tracing to the centralized Langfuse instance and connect to the unified graph database:
```bash
export LANGFUSE_HOST="http://100.87.214.70:3003"
export LANGFUSE_PUBLIC_KEY="pk-lf-..."
export LANGFUSE_SECRET_KEY="sk-lf-..."
export NEO4J_URI="bolt://100.87.214.70:7687"
export NEO4J_USERNAME="neo4j"
export NEO4J_PASSWORD="ventures2026"
export OLLAMA_HOST="http://100.87.214.70:11434"
```

## Unified AI OS Infrastructure (Mac Studio Node: 100.87.214.70)
The Mac Studio acts as the primary AI infrastructure brain. The services are consolidated as follows:
- **Models & Reasoning**:
  - **Ollama**: Native host on port `11434` (OLLAMA_HOST=0.0.0.0, models mapped from `/Volumes/LaCie/ollama/models`)
  - **LiteLLM Gateway**: Docker container `civos_litellm` on port `4000` (bridges Ollama and Anthropic APIs)
  - **Open WebUI**: Docker container `civos_webui` on port `3010`
- **Memory & Databases**:
  - **PostgreSQL**: Native host on port `5432` (databases: `iza_os_ventures`, `iza_os_core`, `iza_os_intelligence`, `twenty`, `litellm`, `langfuse`)
  - **Qdrant Vector DB**: Docker container `civos_qdrant` on port `6333`
  - **Neo4j Knowledge Graph**: Docker container `civos_neo4j` on ports `7474` (HTTP) and `7687` (Bolt) (Credentials: `neo4j/ventures2026`)
- **Observability & Tracing**:
  - **Langfuse**: Docker container `civos_langfuse` on port `3003` (connected to PostgreSQL database `langfuse`)
- **Operations & Automation**:
  - **Twenty CRM**: Docker container `civos_twenty` on port `3004` (shared database `twenty`)
  - **n8n**: Docker container `n8n` on port `5678`
  - **MCPJungle**: Docker container `civos_mcpjungle` on port `8787` (MCP registry + proxy)
  - **NocoDB**: Docker container `civos_nocodb` on port `8090`
  - **MinIO Object Storage**: Docker container `civos_minio` on port `9000` / Console `9001`
  - **Changedetection.io**: Docker container `civos_changedetection` on port `5001`

## IZA OS Capability Map Map Hierarchy
The control plane maps dependencies sequentially:
```text
Repository -> Capability -> Skill -> Agent -> Workflow -> Venture -> Revenue Model
```

The system categories are divided into 10 layers:
1. **LOCAL AI**: Private model runtimes (Ollama, GPT4All, LocalAI, Lemonade).
2. **CODE INTELLIGENCE**: Code graph analyzer scan tools (GitNexus, CodeGraph, SocratiCode).
3. **AI EMPLOYEES**: Collaborative agent workspaces (OpenHuman, AionUI, EigEnt).
4. **APP FACTORY**: Low-code app builders (Dyad, Claudable).
5. **DATA MEMORY**: Markdown vaults and indices (Obsidian Second Brain, LlamaIndex).
6. **AUTOMATION**: Workflow engines (n8n, Camunda, Activepieces).
7. **INFRASTRUCTURE**: Cost-free cloud emulation (LocalStack).
8. **SECURITY**: AI pen-tester suites (METATRON).
9. **VOICE**: Voice dictation and transcribers (Meetily, Pindrop).
10. **COMPUTER VISION**: Object-detection CCTV parsing (Frigate, VERT).

## Developer Guidelines
1. **No Backend Resetting**: Always check if a background task is running on port 8000 before attempting to spawn `server.py` to prevent address conflicts.
2. **Compile Verification**: After editing `server.py`, compile check it using:
   ```bash
   python3 -m py_compile server.py
   ```
3. **Vanilla Alignment**: Keep styling and structure in pure CSS and native DOM APIs. Do not install Tailwind or React unless explicitly requested.
4. **Data Integrity**: Never truncate or delete the original resources in `app.js` or `README.md`. Appends and additions are allowed.

## Implemented Agent Skills & Capability Integrations
To support the 100-Graph IZA OS Graph Engine, the following workspace skills are installed under `/.agents/skills/`:
- **[gitnexus-cli](file:///Users/acebless/Documents/.agents/skills/gitnexus-cli)**: Powers static dependency and call-graph indexing (maps to the `repository_scanner` tool in [mcp_gateway.py](file:///Users/acebless/Documents/Gemini/services/mcp_gateway.py#L67)).
- **[neo4j-cypher-skill](file:///Users/acebless/Documents/.agents/skills/neo4j-cypher-skill)** & **[neo4j-graphrag-skill](file:///Users/acebless/Documents/.agents/skills/neo4j-graphrag-skill)**: Provide natural language translation to Cypher and execute GraphRAG patterns inside Neo4j (maps to `sync_obsidian_graph` and custom query gateways in [execution_gateway.py](file:///Users/acebless/Documents/Gemini/services/execution_gateway.py)).
- **[qdrant-clients-sdk](file:///Users/acebless/Documents/.agents/skills/qdrant-clients-sdk)**: Manages local vector embedding memory layer connections using Qdrant (backing RAG searches across repositories).

## AI Venture OS Spawner & Registries
To support the AI Venture Operating System, the following core directories and spawner scripts are implemented:
- **[create_venture.py](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/05-AGENTS/create_venture.py)**: CLI Spawner script that takes `--name`, `--sector`, `--location`, `--target`, and `--revenue` to automatically build venture directories, resolve capabilites from Neo4j, write local agent configs, merge nodes into Neo4j, update PostgreSQL, and rebuild VEX site bundles.
- **[capability_registry.yaml](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/capability_registry.yaml)**: Maps capability targets (RAG, inventory, payments, crm) to their implementing open-source and local repositories.
- **[sector_registry.yaml](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/sector_registry.yaml)**: Outlines default capabilities, OpCos, and agent configurations.
- **[workflow_registry.yaml](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/workflow_registry.yaml)**: Defines steps for repeatable execution workflows.
- **[output_registry.yaml](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/output_registry.yaml)**: Manages output formats and export options (PDF, HTML, MP4).
- **[neo4j_schema.cypher](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/knowledge_graph/neo4j_schema.cypher)**: Cypher definitions for expanded database labels and constraints.
- **[lead_intelligence/](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/lead_intelligence)**: Folder hosting lead acquisition configurations including `sector_sources.yaml` (data targets per sector), `scraper_registry.yaml` (crawler repo mappings), and `enrichment_pipeline.yaml` (Twenty CRM ingestion pipelines).
- **[agent_tools_registry.yaml](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/agent_tools_registry.yaml)**: Maps specialized utility tools (such as OfficeCLI, CubeSandbox, Meetily, Claude-video) to target agent roles and execution layers.
- **[sector_subverticals.yaml](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/sector_subverticals.yaml)**: Taxonomy registry detailing sub-vertical metadata, default monetization structures, and required capability lists for venture creation.
- **[venture_monetization_upgrades.md](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/venture_monetization_upgrades.md)**: Details progressive upgrade monetization maps (v1 content, v2 services, v3 SaaS) for the closest-to-revenue MVP ventures.
- **[portfolio_metrics_scorecard.yaml](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/portfolio_metrics_scorecard.yaml)**: Dictionary database file mapping all 100 success metrics and North Star KPI targets.
- **[portfolio_roadmap.yaml](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/10-STATUS/portfolio_roadmap.yaml)**: 10-point roadmap status registry mapping core Venture Studio OS modules.
- **[system_audits_scorecard.yaml](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/system_audits_scorecard.yaml)**: Scorecard registry tracking 100 system audits and quality checks for the AI OS.
- **[database_routing.yaml](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/database_routing.yaml)**: Configuration mapping local/Studio Tailscale service links and storage endpoints.


