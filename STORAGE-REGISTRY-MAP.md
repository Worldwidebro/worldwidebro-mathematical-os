# Storage Registry & Tool Alignment Map

## System Architecture: Where Data Lives & Why

```
OPERATIONAL FLOW:
Ventures (712) → Registries (CSV/JSON) → Graphs (Neo4j/Qdrant) → Agents → Actions
                 ↓                        ↓                       ↓
            T7 Shield             T7 + MacBook       LaCie (backup)
```

---

## T7 SHIELD (1.8TB, 47% used = 860GB) — PRIMARY OPERATING SYSTEM

### 00_COMMAND_CENTER/worldwidebro-os/
**What lives here:**
- `01-BOSS-OS/registries/` — Master registries (CSV/JSON)
  - `VENTURES-CAPABILITIES-MAPPED.csv` (712 ventures × 25 capabilities)
  - `REPOSITORY-REGISTRY.json` (1,639 repos with capabilities)
  - `venture-capabilities-proposed.csv` (join table)
  - `repo-capabilities-backfill.json` (70% coverage)
  - `VENTURE-READINESS-SCORECARD.csv` (readiness 0-100)
- `01-BOSS-OS/infrastructure/data-layer/scripts/`
  - `populate_venture_knowledge_graph.py` (syncs Supabase → Neo4j)
  - `build_repo_rag.py` (embeds repos → Qdrant)
  - `build_capability_catalog.py` (capability taxonomy)

**Why needed:**
- Source of truth for all 712 ventures
- Join tables for repo→venture→capability mappings
- Feeds Neo4j knowledge graph + Qdrant vector search

**Tools that manage this:**
| Tool | Purpose | What it does |
|------|---------|-------------|
| **Graphify** | Repository graph generation | Converts repo data → Neo4j nodes/edges |
| **SocratiCode** | Impact analysis & dependencies | Traces how code changes affect ventures |
| **GitNexus** | Repository visualization | Renders repo dependency graphs |
| **Qdrant** | Vector memory (embeddings) | Stores `repositories` + `notes` collections |
| **Neo4j** | Knowledge graph | Stores 2,618 nodes (ventures/repos/capabilities/skills/MCPs) |

**Sync flow:**
```
CSV files → Python scripts → Supabase → populate_venture_knowledge_graph.py 
→ Neo4j (graph_entities, graph_relationships) + Qdrant (embeddings)
```

---

### 04_AI_MODELS/ + ollama_models/
**What lives here:**
- Ollama model checkpoints (qwen2.5:32b, qwen3:8b, nomic-embed-text)
- exo distributed inference models
- Model weights for local inference

**Why needed:**
- Local inference without cloud API calls (privacy, cost, latency)
- Embeddings for Qdrant (nomic-embed-text: 768-dim vectors)
- Model routing decision engine (OmniRoute uses these)

**Tools that manage this:**
| Tool | Purpose |
|------|---------|
| **Ollama** | Local inference engine (runs models locally) |
| **LiteLLM** | Model routing (task → model selection) |
| **Colibri** | High-performance local inference |
| **exo** | Distributed inference (cluster multiple devices) |

---

### 01-20 (Numbered Operating System Folders)
**What lives here:**
- 01-BOSS-OS (strategy, roadmaps, registries)
- 02-SECTOR-OS (14 sectors: construction, staffing, etc.)
- 03-VENTURES (712 ventures organized by sector)
- 04-OPERATIONS (workflows, SOPs)
- 05-AGENTS (agent definitions, roles)
- 06-TECHNOLOGY (infrastructure, tech stack)
- And 14 more thematic folders

**Why needed:**
- Canonical organization of all 712 ventures
- Sector strategies and operating procedures
- Agent definitions (who does what)
- Technology architecture reference

**Tools that reference this:**
| Tool | Purpose |
|------|---------|
| **Understand Anything** | Repository explanation & onboarding |
| **SocratiCode** | Semantic understanding of folder structures |
| **Graphify** | Maps folder hierarchy → Neo4j entity relationships |

---

## LACIE (3.6TB, 45% used = 1.6TB) — ARCHIVE & BACKUP

### DEVELOPMENT-ECOSYSTEM/ → 46-agents-legacy/
**What lives here:**
- Legacy agent implementations (deprecated)
- Old automation workflows
- Historical agent registry snapshots

**Why needed:**
- Historical reference (what was tried before)
- Fallback if active agents fail
- Training data for agent redesign

**Tools that analyze this:**
| Tool | Purpose |
|------|---------|
| **CrewAI** | Multi-agent orchestration (old version archived here) |
| **Langfuse** | Traces execution history of agents |

---

### RESEARCH-LAB/
**What lives here:**
- Academic papers on AI, ventures, operations
- Research notes on sector strategies
- Competitive analysis archives

**Why needed:**
- Decision support (research precedents)
- Strategic framework validation
- Industry trend analysis

**Tools that use this:**
| Tool | Purpose |
|------|---------|
| **Serena** | Semantic code understanding (applies to research papers) |

---

### ollama-models/ + ollama/
**What lives here:**
- Backup copies of model checkpoints
- Ollama configuration snapshots
- Model version history

**Why needed:**
- Disaster recovery (if T7 Shield fails)
- Model A/B testing (keep old versions)
- Performance baseline comparisons

---

### SecondBrain/
**What lives here:**
- Obsidian vault backup
- Notes, MOCs, knowledge base snapshots
- Daily export of KNOWLEDGE-GRAPH-DASHBOARD.md

**Why needed:**
- Knowledge base persistence (if MacBook Air fails)
- Audit trail of decisions & reasoning
- Reference for future ventures (reuse patterns)

**Tools that sync this:**
| Tool | Purpose |
|------|---------|
| **Neo4j** | Stores knowledge graph that Obsidian visualizes |
| **Qdrant** | `notes` collection (vault notes searchable) |
| **Langfuse** | Logs decision reasoning over time |

---

## MACBOOK AIR (500GB, 98% full) — ACTIVE WORK ONLY

### ~/Documents/ (symlink → T7 Shield/00_COMMAND_CENTER/worldwidebro-os/)
**What lives here:**
- Active Python scripts (populate_venture_knowledge_graph.py, etc.)
- Running DuckDB (worldwidebro_os.duckdb)
- Docker volumes (Neo4j, Qdrant, PostgreSQL, etc.)
- .env (Supabase/GitHub/Anthropic keys)

**Why needed:**
- Direct access to running services
- Fast disk I/O for active development
- DuckDB analytics queries (low latency)

**Tools that use this:**
| Tool | Purpose |
|------|---------|
| **LiteLLM** | Loaded in memory, routing requests |
| **PostgreSQL** | Running locally (TwentyHQ backend) |
| **Neo4j** | Docker container, live queries |
| **Qdrant** | Docker container, vector search |

**PROBLEM: Only 8.5GB free → Need to move caches/backups to LaCie**

---

## Data Flow: From Storage to Agent Decision

```
MacBook Air (active work)
    ↓
WORLDWIDEBRO-OS symlink → T7 Shield/00_COMMAND_CENTER/worldwidebro-os/
    ↓
Registries (CSV/JSON) + Python scripts
    ↓
Supabase (transactional DB)
    ↓
populate_venture_knowledge_graph.py
    ├→ Neo4j (2,618 nodes, 11,134 edges)
    │   ├ Venture nodes (712)
    │   ├ Repository nodes (1,639)
    │   ├ Capability nodes (25)
    │   ├ Skill nodes (296)
    │   └ MCP nodes (40+)
    │
    └→ Qdrant (embeddings)
        ├ repositories collection (1,648 vectors)
        └ notes collection (15,558 vectors)

    ↓
Agents query Neo4j + Qdrant
    ↓
LiteLLM routes to: Ollama (local) / FreeLLMAPI (free) / Claude (paid)
    ↓
Langfuse logs execution + cost + quality
    ↓
Action (create venture, fix bug, write docs, etc.)

    ↓
LaCie backs up: Obsidian vault + old models + decision logs
```

---

## Registry Locations & What Each Contains

| Registry | Location | Format | Rows | Updated | Tool Owner |
|----------|----------|--------|------|---------|-----------|
| VENTURES | T7/01-BOSS-OS/registries/ | CSV + Supabase table | 712 | weekly | Graphify |
| REPOSITORIES | T7/REPOSITORY-REGISTRY.json | JSON + Neo4j | 1,639 | monthly | GitNexus |
| CAPABILITIES | T7/capability_vocabulary.json | JSON + Neo4j | 25 canonical | on-demand | SocratiCode |
| VENTURE→REPO | T7/repo-capabilities-backfill.json | JSON + Neo4j edges | 1,157 joins | monthly | Graphify |
| READINESS | T7/VENTURE-READINESS-SCORECARD.csv | CSV | 712 scores | weekly | LiteLLM (cost-aware routing) |
| SKILLS | T7/SKILL-TAXONOMY.json | JSON + Neo4j | 296 skills | on-demand | CrewAI |
| MCPs | T7/mcp-config.json + MCP_REGISTRY.json | JSON + Neo4j | 40+ MCPs | on-demand | Qdrant (MCP discovery) |
| OPERATIONS | Supabase (skill_executions, venture_skill_roadmap) | Tables | — | real-time | Langfuse (audit trail) |
| KNOWLEDGE GRAPH | Neo4j + LaCie/SecondBrain backup | Cypher nodes/edges | 2,618 nodes | hourly | Neo4j (ACID guarantees) |
| EMBEDDINGS | Qdrant | Vectors (768-dim) | 17,206 vectors | on-demand | Ollama (embeddings engine) |
| DECISION LOGS | Langfuse + LaCie/SecondBrain | Traces + JSON exports | — | real-time | Langfuse (observability) |

---

## Tool Breakdown: How Each Understands the System

### Grouping 1: Data Acquisition & Indexing
| Tool | Input | Output | Why Needed |
|------|-------|--------|-----------|
| **Graphify** | GitHub repos + venture.json | Graph JSON (Neo4j format) | Maps repo→venture relationships at scale |
| **GitNexus** | Local git repos | Dependency graph + visualization | Traces code dependencies across 1,639 repos |
| **SocratiCode** | Repo + folder structure | Semantic index + entity extraction | Understands intent (not just keywords) |
| **RepoMix** | Repo + files | Context packages for LLMs | Prepares manageable prompts for Claude |

### Grouping 2: Knowledge Graph & Memory
| Tool | Input | Output | Why Needed |
|------|-------|--------|-----------|
| **Neo4j** | populate_venture_knowledge_graph.py output | Graph DB (Cypher queryable) | ACID guarantees + complex relationship queries |
| **Qdrant** | Ollama embeddings | Vector DB (semantic search) | Finds similar repos/notes without keyword match |
| **PostgreSQL** | Supabase sync | Normalized OLTP tables | Real-time transactional consistency |
| **Sourcegraph MCP** | Repos + symbols | Symbol map (Go-to-def) | Code navigation at venture scale |

### Grouping 3: Model Inference & Routing
| Tool | Input | Output | Why Needed |
|------|-------|--------|-----------|
| **Ollama** | Models from T7/ollama_models/ | Local inference endpoint | Privacy + low latency (no cloud) |
| **LiteLLM** | Task + context | Routed to: Ollama / FreeLLMAPI / Claude | Cost-aware routing (save $9.2K/month) |
| **FreeLLMAPI** | Request | Free-tier response (15+ providers) | Tier-1: free before paid |
| **exo** | Models + distributed devices | Cluster inference | Scale inference across Mac Studio + MacBook |

### Grouping 4: Observability & Decision Logging
| Tool | Input | Output | Why Needed |
|------|-------|--------|-----------|
| **Langfuse** | Agent execution traces | Cost + latency + quality metrics | Audit trail: what agent did, why, at what cost |
| **Prometheus** | Scrape targets | Metrics time series | System health (disk, memory, API latency) |
| **Grafana** | Prometheus + DuckDB | Dashboards | Real-time KPIs (MRR, venture readiness, etc.) |

### Grouping 5: Multi-Agent Coordination
| Tool | Input | Output | Why Needed |
|------|-------|--------|-----------|
| **CrewAI** | Agent definitions + tasks | Orchestrated execution | Agents coordinate (Agent A feeds output to Agent B) |
| **Stirling PDF** | Document files | Converted/preprocessed | Prep unstructured data for Neo4j ingestion |

---

## Quick Navigation Guide

### "Where does X live?"

| Question | Answer | File | Tool |
|----------|--------|------|------|
| All 712 ventures | T7/01-BOSS-OS/registries/VENTURES-CAPABILITIES-MAPPED.csv | Neo4j query: `MATCH (v:Venture) RETURN v.id, v.name` | Graphify |
| All 1,639 repos | T7/REPOSITORY-REGISTRY.json | Neo4j query: `MATCH (r:Repository) RETURN r` | GitNexus |
| Venture→Repo links | T7/repo-capabilities-backfill.json | Neo4j edges: `MATCH (r:Repository)-[:IMPLEMENTS]->(c:Capability)<-[:NEEDS]-(v:Venture)` | SocratiCode |
| Venture readiness scores | T7/VENTURE-READINESS-SCORECARD.csv | Query: `SELECT * FROM ventures WHERE readiness_pct > 50` | LiteLLM |
| Skills (296 total) | T7/SKILL-TAXONOMY.json | Neo4j: `MATCH (s:Skill) RETURN s.name, s.phase` | CrewAI |
| MCPs (40+ tools) | T7/mcp-config.json + MCP_REGISTRY.json | Neo4j: `MATCH (m:MCP)-[:PROVIDES]->(cap:Capability)` | Qdrant |
| Knowledge graph nodes/edges | MacBook Air Docker Neo4j:7687 | Live Cypher queries | Neo4j |
| Embeddings (semantic search) | MacBook Air Docker Qdrant:6333 | Query: `POST /collections/repositories/points/search` | Qdrant |
| Backup of everything | LaCie/SecondBrain/ | Obsidian sync (daily) | Neo4j + Qdrant |

---

## Storage Action Plan: Free 10GB on MacBook Air

**Run these commands:**
```bash
# Move caches to LaCie (safe to rebuild)
mv ~/.cache /Volumes/LaCie/.cache-backup && ln -s /Volumes/LaCie/.cache-backup ~/.cache

# Move Ollama models (redundant with T7)
mv ~/.ollama /Volumes/LaCie/.ollama-backup && ln -s /Volumes/LaCie/.ollama-backup ~/.ollama

# Move Docker images (can pull again)
mv ~/.docker /Volumes/LaCie/.docker-backup && ln -s /Volumes/LaCie/.docker-backup ~/.docker

# Move Rust builds (can rebuild)
mv ~/.cargo /Volumes/LaCie/.cargo-backup && ln -s /Volumes/LaCie/.cargo-backup ~/.cargo

# Move Xcode caches (safe)
rm -rf ~/Library/Developer/Xcode/DerivedData/*

# Verify new free space
df -h / | grep -E "Filesystem|disk0"
```

**Keep on MacBook Air (do NOT move):**
- `~/.env` (secrets)
- `~/Documents/.venv` (active Python environment)
- `~/Documents/worldwidebro-os` (symlink to T7 Shield)
- Docker containers running (Neo4j, Qdrant, PostgreSQL)

**Expected result:** 8.5GB → ~35-40GB free

---

## Reference Map

**Navigate the system:**
1. **Question about a venture?** → Check `VENTURES-CAPABILITIES-MAPPED.csv` → Query Neo4j
2. **Question about a repo?** → Check `REPOSITORY-REGISTRY.json` → Ask Graphify
3. **Question about connections?** → Check `repo-capabilities-backfill.json` → Query SocratiCode
4. **Question about cost/routing?** → Check `VENTURE-READINESS-SCORECARD.csv` → Ask LiteLLM
5. **Question about what agents did?** → Check Langfuse traces → Look up in LaCie/SecondBrain
6. **Question about similar ventures?** → Search Qdrant `repositories` collection → SocratiCode semantic search
7. **Question about decisions made?** → Check Neo4j knowledge graph + LaCie/Obsidian vault backup

**When in doubt:** Start with the registry on T7 Shield, then drill into the tool that manages it.
