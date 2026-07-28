# AI Boss OS - Master Handbook

## Purpose

This document serves as the master index and architectural blueprint for the AI Boss OS ecosystem. It provides a comprehensive overview of how all components, systems, and knowledge domains are organized, connected, and maintained. This handbook replaces the previous monolithic approach with a structured, searchable, and scalable knowledge management system.

---

## Overview

The AI Boss OS is designed to manage 700+ ventures across multiple sectors through a unified operating system. The architecture separates concerns into distinct layers:

- **Business Architecture** - Ventures, sectors, capabilities, value streams
- **Domain Architecture** - Bounded contexts and shared models
- **Application Architecture** - APIs, agents, services, workflows
- **Data Architecture** - Schemas, knowledge graph, vectors, ontologies
- **Technology Architecture** - Networking, ports, containers, infrastructure, deployments

This separation enables both humans and AI agents to quickly locate specific information and understand system relationships.

---

## Folder Structure

```
Documents/
│
├── 00_COMMAND_CENTER/          # Control center (this file)
│   ├── MASTER-HANDBOOK.md      # This document
│   ├── CLAUDE.md               # Root configuration
│   ├── NAVIGATION.md           # Folder structure & handoff rules
│   └── WORLDWIDEBRO-OS/        # Master operating system
│
├── 01_STRATEGY/                # Business planning
│   ├── UNIFIED-COMPANY-ROADMAP-2026.md
│   ├── REPOSITORY-INTELLIGENCE-SYSTEM.md
│   └── VENTURE-READINESS-SCORECARD.csv
│
├── 02_PLATFORM/                # Core infrastructure
│   ├── IZA-OS/                 # Knowledge graph + agents
│   ├── Langfuse/               # Observability
│   └── LiteLLM/                # Model routing
│
├── 03_SECTOR_OS/               # Industry-specific implementations
│   ├── CON-ventures/           # Construction
│   │   └── .claude/CLAUDE.md   # Auto-loads for CON work
│   ├── FIN-ventures/           # Finance
│   │   └── .claude/CLAUDE.md   # Auto-loads for FIN work
│   ├── LT-ventures/            # Logistics
│   │   └── .claude/CLAUDE.md   # Auto-loads for LT work
│   └── RE-ventures/            # Real Estate
│       └── .claude/CLAUDE.md   # Auto-loads for RE work
│
├── 04_VENTURES/                # Individual venture code
├── 05_AGENTS/                  # AI agent definitions
├── 06_PRODUCTS/                # The 14 AI products (P1-P14)
├── 07_KNOWLEDGE/               # Knowledge base content
├── 08_DATA/                    # Data management & schemas
│
├── architecture/               # Architecture decisions
│   ├── 01-business/
│   ├── 02-domain/
│   ├── 03-application/
│   ├── 04-data/
│   ├── 05-network/
│   ├── 06-security/
│   ├── 07-deployment/
│   ├── 08-observability/
│   ├── 09-governance/
│   ├── 10-decision-records/
│   ├── 11-diagrams/
│   ├── 12-ontology/
│   ├── 13-topology/
│   ├── 14-sequence-diagrams/
│   ├── 15-state-machines/
│   └── 16-capability-model/
│
├── infrastructure/             # Infrastructure definitions
│   ├── postgres/
│   ├── redis/
│   ├── neo4j/
│   ├── qdrant/
│   ├── minio/
│   ├── rabbitmq/
│   ├── nats/
│   ├── ollama/
│   ├── prometheus/
│   ├── grafana/
│   ├── traefik/
│   ├── nginx/
│   └── vault/
│
├── networking/                 # Network architecture
│   ├── README.md
│   ├── TOPOLOGY.md
│   ├── PORT-REGISTRY.md
│   ├── DNS.md
│   ├── API-GATEWAY.md
│   ├── ZERO-TRUST.md
│   └── ...
│
├── containers/                 # Container definitions
│   ├── docker-compose/
│   ├── kubernetes/
│   ├── base-images/
│   └── volumes/
│
├── deployments/                # Deployment configurations
│   ├── development/
│   ├── staging/
│   ├── production/
│   └── github-actions/
│
├── monitoring/                 # Observability
│   ├── logs/
│   ├── metrics/
│   ├── dashboards/
│   ├── alerts/
│   └── traces/
│
└── security/                   # Security policies
    ├── rbac/
    ├── policies/
    ├── compliance/
    └── incident-response/
```

---

## Auto-Loading Context

Claude Code automatically loads configuration based on folder:

| When you open files in... | Claude loads... | Purpose |
|---------------------------|-----------------|---------|
| `/Documents/03_SECTOR_OS/CON-ventures/` | `.claude/CLAUDE.md` (CON config) | Construction sector context: build/test/deploy rules, API endpoints, cross-sell map |
| `/Documents/03_SECTOR_OS/FIN-ventures/` | `.claude/CLAUDE.md` (FIN config) | Finance sector context: compliance rules, hub-sector data flows, APIs |
| `/Documents/03_SECTOR_OS/LT-ventures/` | `.claude/CLAUDE.md` (LT config) | Logistics sector context: routing, dispatch, cost algorithms, cross-sector dependencies |
| `/Documents/03_SECTOR_OS/RE-ventures/` | `.claude/CLAUDE.md` (RE config) | Real Estate context: valuation, MLS integration, cross-sector dependencies |
| Any folder above 03_SECTOR_OS | Root `.claude/CLAUDE.md` | Root configuration: 4 databases, sources of truth, naming conventions |

**This means:** Context is automatically correct based on where you're working. No manual switching needed.

---

## Configuration Files

### Root Configuration
**File:** `/Users/acebless/.claude/CLAUDE.md`  
**Loaded:** Globally, for all work outside sector folders  
**Contains:**
- Four databases (Supabase, Neo4j, Qdrant, Redis, Langfuse)
- Two invariants (Supabase is source of truth, code changes via Git+PR)
- Three sources of truth (CSV first, then Supabase, then Neo4j)
- Naming conventions (sectors, ventures, branches)
- Skill usage rules
- Emergency commands

### Sector Configurations
**Pattern:** `/Documents/03_SECTOR_OS/{SECTOR}-ventures/.claude/CLAUDE.md`

#### Construction (CON.md)
- Build/test/deploy commands
- P1 Speed-to-Lead API endpoints
- P7 RFP Responder APIs
- Cross-sell goldmine: +$2,594/mo per venture (RE, LOG, FIN)
- Handoff rules for cross-sector dependencies

#### Finance (FIN.md)
- Build/test/deploy + compliance checks
- Hub sector (HIGH PRIORITY data to ALL sectors)
- P1/P7/P10/P14 features
- Audit trail + encryption requirements
- SOX compliance rules

#### Logistics (LT.md)
- Build/test/deploy for dispatch system
- P1/P3/P14 features
- Supply chain optimization
- Serves CON, RE, FIN downstream
- Routing, GPS, cost algorithms

#### Real Estate (RE.md)
- Build/test/deploy for property system
- P1/P8/P10/P14 features
- Cross-sector: RE→FIN (valuation), RE→CON (renovation), RE→LOG (distribution)
- MLS integration, property valuations

### Navigation Configuration
**File:** `/Users/acebless/.claude/NAVIGATION.md`  
**Contains:**
- Numbered folder structure (0-8 layers)
- Decision tree: when to stay in sector vs. escalate
- Cross-sector dependency map
- Handoff checklist with Supabase updates
- Sector-specific entry points

---

## Context Switching

### Scenario 1: Working on CON-001

```bash
# Open any file in CON-ventures folder
cd /Documents/03_SECTOR_OS/CON-ventures/
code con-001/

# Claude automatically loads:
# 1. Root CLAUDE.md (global rules)
# 2. .claude/CLAUDE.md in CON-ventures (construction-specific rules)
# Result: You have build/test/deploy commands, API docs, cross-sell map
```

### Scenario 2: Working on Platform Infrastructure

```bash
# Open platform file
cd /Documents/02_PLATFORM/
code neo4j-config.yaml

# Claude automatically loads:
# 1. Root CLAUDE.md only
# Result: You have database connectivity rules, source of truth rules
```

### Scenario 3: Handoff from CON to RE

```bash
# You're in CON-ventures, need to notify RE team
# Reference: /Documents/.claude/NAVIGATION.md (handoff checklist)
# 1. Update Supabase venture_dependencies table
# 2. Post to Slack #sector-dependencies
# 3. Switch context to RE-ventures folder
# 4. Load RE.md for RE-specific rules
```

---

## System Integration Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        Root CLAUDE.md                        │
│              (Global rules, sources of truth)                │
└────┬─────────────────────────┬──────────────────┬────────────┘
     │                         │                  │
     │                  Sector auto-load          │
     │                         │                  │
  ┌──▼──┐                  ┌───▼────┐       ┌────▼────┐
  │CON  │                  │FIN     │       │LT   RE  │
  │.md  │                  │.md     │       │.md  .md │
  └──┬──┘                  └────┬───┘       └────┬────┘
     │                          │                │
  CON API    Cross-sell map   FIN APIs      LOG+RE APIs
  P1/P7      $2,594/mo        P1/P7/P10     P1/P3/P14
            per venture        P14           P1/P8/P10/P14
```

---

## Data Layer

### Supabase (Relational)
- ventures table (712 rows)
- venture_dependencies (cross-sector links)
- venture_leads (lead capture)
- deal_payments (revenue tracking)

### Neo4j (Knowledge Graph)
- Sector ontology
- Capability relationships
- API endpoint mappings
- Dependency chains

### Qdrant (Vector Search)
- notes collection (15,558 vectors)
- sector_playbooks
- capability embeddings

### Redis (Cache)
- Session data
- Rate limiting
- Real-time metrics

---

## Key Workflows

### When you need to know something...

| Question | Navigate to | File | Purpose |
|----------|-----------|------|---------|
| "How do I build CON-001?" | 03_SECTOR_OS/CON-ventures/ | .claude/CLAUDE.md | Build/test/deploy commands |
| "What's the dependency map?" | 00_COMMAND_CENTER/ | NAVIGATION.md | Cross-sector flows |
| "What port does Qdrant use?" | infrastructure/ | PORT-REGISTRY.md | Centralized port assignments |
| "How do sectors connect?" | architecture/ | 12-ontology/ | Entity relationships |
| "What's the network topology?" | networking/ | TOPOLOGY.md | Physical/logical layout |
| "How are services wired?" | architecture/ | 03-application/ | Runtime interactions |

---

## Maintenance

### Adding new sector

1. Create folder: `/Documents/03_SECTOR_OS/{SECTOR}-ventures/.claude/`
2. Create file: `CLAUDE.md` with build/test/deploy rules
3. Update: `/Documents/.claude/NAVIGATION.md` with handoff rules
4. Update: `/Documents/.claude/CLAUDE.md` if adding new database or invariant

### Updating configuration

1. Edit source file (sector .claude/CLAUDE.md or root CLAUDE.md)
2. Run verification: `ls -la /Documents/03_SECTOR_OS/*/` to confirm all sectors have .claude/CLAUDE.md
3. Test context: Open file in sector folder, verify Claude loads correct config

### Removing redundancy

1. Identify duplicate content (multiple copies of same rule)
2. Keep single source in most relevant location
3. Replace copies with cross-references
4. Update NAVIGATION.md if handoff rules changed

---

## Related Files

- `/Users/acebless/.claude/CLAUDE.md` - Root configuration
- `/Users/acebless/.claude/NAVIGATION.md` - Folder structure & handoff rules
- `/Documents/00_COMMAND_CENTER/WORLDWIDEBRO-OS/` - Master OS
- `/Documents/01_STRATEGY/VENTURE-READINESS-SCORECARD.csv` - Live venture data
- `/Documents/01_STRATEGY/REPOSITORY-INTELLIGENCE-SYSTEM.md` - Repo inventory

---

## Standards

### Configuration File Template

Every sector .claude/CLAUDE.md follows this structure:

```markdown
# {SECTOR}.md — {Full Sector Name}

**Scope:** Build/test/deploy rules for {SECTOR} ventures  
**Sector:** `{SECTOR}` | **Status:** P1, P7, P10, P14  
**Updated:** YYYY-MM-DD

---

## Build/Test/Deploy

### Build
[Build commands]

### Test
[Test commands]

### Deploy
[Deploy commands]

---

## Handoff Rules

✅ **Stay in {SECTOR} if:** [conditions]
🔵 **Cross-sector if:** [conditions]
🚨 **Platform if:** [conditions]

---

## Quick APIs

[API endpoints]

---

## Known Issues

[Blockers and workarounds]

---

**Generated:** YYYY-MM-DD | **Version:** 1.0
```

---

## TODO

- [x] Create sector-specific .claude/CLAUDE.md files
- [x] Move sector configs to auto-load locations
- [x] Create root CLAUDE.md
- [x] Create NAVIGATION.md
- [ ] Migrate existing knowledge into /architecture/ subdirectories
- [ ] Build cross-reference index
- [ ] Create search functionality
- [ ] Set up automated validation
- [ ] Build agent-accessible API for knowledge retrieval

---

**Last Updated:** 2026-07-27  
**Version:** 1.0  
**Maintained By:** Worldwidebro Holdings
