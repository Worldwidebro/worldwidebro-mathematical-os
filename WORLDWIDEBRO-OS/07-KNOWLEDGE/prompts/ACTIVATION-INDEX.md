# Prompt Library — Activation Index

**Purpose:** Level 4–5 ontological/cybernetic constructs that define operational semantics per module.  
**Principle:** The folder tree is DNA; these prompts are the bone marrow.

## How to use

1. Each `.prompt.md` file contains metadata (layer, phase, inputs, outputs) + the executable prompt body.
2. Run prompts in **Master Activation Sequence** order unless doing targeted module work.
3. Outputs land in the sibling directory (e.g. `00-COMMAND/CURRENT_PRIORITIES.md`), not inside `prompts/`.

## Master activation sequence

| Phase | Week | Prompts | Output artifacts |
|-------|------|---------|------------------|
| **1 Constitution** | 1 | MISSION_VISION_VALUES, OPERATING_PRINCIPLES, NORTH_STAR_METRICS | `00-DIRECTIVES/*.md` |
| **2 Governance** | 1–2 | DATA_GOVERNANCE, DECISION_FRAMEWORK, CAPITAL_ALLOCATION, AGENT_CREATION | `00-DIRECTIVES/*_DIRECTIVE.md` |
| **3 Structure** | 2 | CEO_MANDATE, AGENT_TEMPLATE, CFO_AGENT, VENTURE_PROFILE, SOP_TEMPLATE | `01-EXECUTIVES/`, `05-AGENTS/`, `03-PORTFOLIO/`, `04-OPERATIONS/` |
| **4 Nervous system** | 2–3 | KNOWLEDGE_GRAPH_MEMORY, REPOSITORY_INDEX, PORTFOLIO_STATUS, HOLDINGS_STATUS, CEO_PULSE | `07-KNOWLEDGE/`, `REGISTRIES/`, `08-DATA/registries/`, `09-DASHBOARDS/`, `10-STATUS/` |
| **5 Activation** | 3 | META_CONTROLLER, ROUTING_ENGINE, ESCALATION_POLICY, EXECUTIVE_BRIEFING, CURRENT_PRIORITIES, DECISION_LOG | Daily/weekly live ops |

## Prompt catalog by layer

### 00-COMMAND (`00-COMMAND/prompts/`)

| File | Agent role | Cadence |
|------|------------|---------|
| CURRENT_PRIORITIES | Chief of Staff | Weekly |
| DECISION_LOG | Institutional memory | Append-only, per decision |
| EXECUTIVE_BRIEFING | CEO Agent | Daily |

### 00-DIRECTIVES (`00-DIRECTIVES/prompts/`)

| File | Agent role |
|------|------------|
| MISSION_VISION_VALUES | Constitutional architect |
| OPERATING_PRINCIPLES | COO |
| CAPITAL_ALLOCATION_DIRECTIVE | CFO Agent |
| DATA_GOVERNANCE_DIRECTIVE | CIO |
| AGENT_CREATION_DIRECTIVE | CTO |
| DECISION_FRAMEWORK | Decision architect |
| NORTH_STAR_METRICS | Institutional intelligence |

### 01-EXECUTIVES (`01-EXECUTIVES/prompts/`)

| File | Agent role |
|------|------------|
| CEO_MANDATE | Board / succession design |

### 03-PORTFOLIO (`03-PORTFOLIO/prompts/`)

| File | Agent role |
|------|------------|
| VENTURE_PROFILE_TEMPLATE | Venture profiler |

### 04-OPERATIONS (`04-OPERATIONS/prompts/`)

| File | Agent role |
|------|------------|
| SOP_TEMPLATE | Operations Agent |

### 05-AGENTS (`05-AGENTS/`)

| Path | File | Agent role |
|------|------|------------|
| `templates/` | AGENT_TEMPLATE | Agent factory |
| `executive/` | CFO_AGENT | CFO Agent runtime |
| `orchestration/` | META_CONTROLLER | Agent ecosystem governor |
| `orchestration/` | ROUTING_ENGINE | Work router |
| `orchestration/` | ESCALATION_POLICY | Escalation controller |

### 06-TECHNOLOGY (`06-TECHNOLOGY/prompts/`)

| File | Agent role |
|------|------------|
| STACK_INTEGRATION | Platform integrator (Cursor, Ollama, OpenWebUI, Hermes) |

### 07-KNOWLEDGE (`07-KNOWLEDGE/prompts/`)

| File | Agent role |
|------|------------|
| KNOWLEDGE_GRAPH_MEMORY | Knowledge Graph Controller |

### REGISTRIES (`REGISTRIES/prompts/`)

| File | Agent role |
|------|------------|
| REPOSITORY_INDEX | Repo Classification Agent (RIS L2–L3) |

### 08-DATA (`08-DATA/prompts/`)

| File | Agent role |
|------|------------|
| PORTFOLIO_STATUS | Portfolio Status Aggregator |

### 09-DASHBOARDS (`09-DASHBOARDS/prompts/`)

| File | Agent role |
|------|------------|
| CEO_PULSE_DASHBOARD | Dashboard Generator |

### 10-STATUS (`10-STATUS/prompts/`)

| File | Agent role |
|------|------------|
| HOLDINGS_STATUS | System Health Monitor |

## Integration with Repository Intelligence

- `REGISTRIES/prompts/REPOSITORY_INDEX.prompt.md` → feeds `repo_classification_pilot.py` + LightRAG ingest
- Only `venture_critical_core` + high-confidence starred deps enter full semantic embedding
- See [[REPOSITORY-INTELLIGENCE-LEVELS]] for L1–L7 pipeline

## Stack roles (Hermes, Cursor, Ollama, OpenWebUI)

See `06-TECHNOLOGY/prompts/STACK_INTEGRATION.prompt.md` for how each tool maps to OS layers.
