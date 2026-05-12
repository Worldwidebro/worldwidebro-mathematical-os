# UNIFIED KNOWLEDGE GRAPH OS v1
**Architecture: From Fragmented Repos → Executable Intelligence System**

**Date**: 2026-05-10  
**Status**: Design & Integration Specification  
**Problem**: 640 starred GitHub repos + Obsidian + databases + AI agents exist separately. Need unified ingestion → normalization → routing → execution pipeline.

---

## 🎯 CORE ARCHITECTURE LAYERS

```
[INGESTION LAYER]      ← 640 repos, Obsidian, CSVs, APIs
       ↓ (normalize)
[KNOWLEDGE GRAPH DB]   ← Neo4j/TypeDB stores relationships
       ↓ (api expose)
[GRAPH API LAYER]      ← engraph (Obsidian→API), REST endpoints
       ↓ (understand)
[AI UNDERSTANDING]     ← LlamaIndex RAG + embeddings
       ↓ (decide)
[ORCHESTRATION]        ← CrewAI agents + n8n workflows
       ↓ (execute)
[EXECUTION SYSTEM]     ← Business actions: ventures, deals, tasks
       ↓ (feedback)
[MEASUREMENT]          ← Learn, improve, refine routing rules
```

---

## 🔧 LAYER 1: INGESTION (All Sources Enter Here)

### Input Sources
```
GitHub Repos (640)
  ├─ Metadata: name, description, stars, topics, language
  ├─ Code: structure, functions, dependencies
  └─ Relations: forks, stars, contributors

Obsidian Vault (~200 notes)
  ├─ Ventures/ (product definitions)
  ├─ Contacts/ (people + capabilities)
  └─ Systems/ (architecture + processes)

Local Databases
  ├─ Supabase: ventures (708), positions (29), agents (554)
  └─ OpenVolo: contacts (58+), enrichment metadata

CSV Data
  ├─ contacts-extracted.csv (58 contacts)
  ├─ CONTACT-DATA-TEMPLATE.csv (schema)
  └─ ventures_completeness.csv (to build)
```

### Ingestion Contract (Normalization Schema)
Every input must become:
```json
{
  "source": "github|obsidian|database|csv",
  "type": "repository|note|venture|contact|agent",
  "id": "unique_identifier",
  "name": "Human readable name",
  "description": "What is this?",
  "purpose": "What does this DO for the system?",
  "capabilities": ["list", "of", "what_it_can_do"],
  "dependencies": ["what_it_needs"],
  "relationships": [{"type": "depends_on|enables|relates_to", "target_id": "..."}],
  "metadata": {"custom": "fields"},
  "last_updated": "ISO8601"
}
```

### Tools for Ingestion
- **Apify** → scrape GitHub: repos, readme, dependencies
- **GitHub API** → metadata: stars, topics, language
- **File Watchers** → detect changes to Obsidian, CSVs, local files
- **Supabase SDK** → read ventures, contacts, agents tables
- **OpenVolo API** → read contact enrichment data

---

## 🧠 LAYER 2: KNOWLEDGE GRAPH DB (Relationships)

### Graph Structure (Neo4j / TypeDB)

**Node Types**:
```
(:Repo) {
  name, description, url, language, stars,
  purpose, capabilities, dependencies
}

(:Venture) {
  name, sector, description, revenue_potential,
  required_roles, required_capabilities, status
}

(:Contact) {
  name, phone, email, company,
  capabilities[], network_reach, warmth_score
}

(:Role) {
  title, authority_level, required_skills,
  decision_making_power, department
}

(:Capability) {
  name, category, description,
  repos_providing_this[],
  contacts_with_this[]
}

(:Agent) {
  name, type, model, purpose,
  assigned_sector, status
}

(:Department) {
  name, head, roles[], agents[]
}

(:System) {
  name, layer, purpose,
  repos_enabling_this[], status
}
```

**Edge Types** (Relationships):
```
ENABLES: Repo → Capability (this repo gives you this ability)
PROVIDED_BY: Capability → Repo[] (this capability comes from these repos)
REQUIRES: Venture → Capability[] (this venture needs these abilities)
HAS: Contact → Capability[] (person has these skills)
FILLS: Contact → Role (person can do this role)
ASSIGNED_TO: Agent → Venture (agent handles this venture)
DEPENDS_ON: Repo → Repo (code dependency)
IMPLEMENTS: Repo → System (repo is part of this architecture layer)
REFERENCES: Note → Venture|Contact|System (Obsidian links)
KNOWS: Contact → Contact (network relationship)
NEEDS: Venture → Contact (venture needs to reach this person)
```

### Building the Graph (Week 1)
1. Import 640 repos as nodes + edges (dependencies)
2. Import Obsidian vault notes as nodes + cross-references
3. Import Supabase ventures, contacts, agents
4. Define edges: which repos provide which capabilities?
5. Map edges: which ventures need which capabilities?

---

## 🔗 LAYER 3: GRAPH API (Query & Sync)

### Tools: Ingestion → Query Layer

**engraph** (Primary)
- Turns Obsidian into API endpoint
- Real-time Obsidian ↔ Graph DB sync
- Exposes graph to AI agents for reads/writes
- Query: "Show me ventures that need capability X"

**REST API** (Custom)
```
GET /graph/repos/{id}
  → returns repo + all relationships

GET /graph/capabilities
  → returns capabilities + providers (repos) + consumers (ventures)

GET /graph/search?q=machine_learning
  → searches repos, notes, capabilities by keyword

POST /graph/link
  → add new relationship

GET /venture/{id}/capability-gaps
  → what does this venture need?

GET /contact/{id}/venture-fit
  → which ventures can this person help?
```

### Sync Directions
- **Obsidian → Graph**: When notes change, update graph
- **Graph → Obsidian**: When relationships change, update references
- **Supabase → Graph**: When ventures/contacts/agents change
- **Graph → ClickUp**: When assignments change, update tasks

---

## 🤖 LAYER 4: AI UNDERSTANDING (RAG + Inference)

### LlamaIndex Integration

**Indexing Strategy**:
1. Index all GitHub repo READMEs + descriptions (620 documents)
2. Index Obsidian vault (200 notes)
3. Index architecture documents (40 docs)
4. Index all contact profiles

**Query Engine**:
```python
# What does this system do?
"Summarize what repo X does for business purposes"
→ Returns prose description of capability

# Dependency mapping
"What repos does repo Y depend on?"
→ Returns dependency tree

# Capability inference
"What capabilities does contact X have based on their profile?"
→ Analyzes professional background + network + conversation history

# Venture gap finding
"What gaps exist in venture Z's team?"
→ Matches required roles against available contacts
```

**Embedding Model**:
- Use Claude embeddings (via LlamaIndex Anthropic connector)
- Semantic search: "AI orchestration tools" finds CrewAI, agency-agents, etc.
- Similarity: "Find repos similar to llama_index" → LangChain, LlamaIndex alternatives

---

## ⚙️ LAYER 5: ORCHESTRATION (Decision + Routing)

### CrewAI Agent Roles

```
Agent 1: INGESTION MANAGER
├─ Purpose: Watch for new repos, contacts, ventures
├─ Tools: GitHub API, file watchers, Supabase subscriptions
└─ Output: Normalized entries → graph DB

Agent 2: GRAPH MAPPER
├─ Purpose: Find relationships between things
├─ Query: "Which repos enable which capabilities?"
├─ Query: "Which contacts have which capabilities?"
└─ Output: New edges in graph

Agent 3: CAPABILITY MATCHER
├─ Purpose: Match ventures → contacts → repos
├─ Query: "E-commerce venture needs inventory management"
├─ Match: Contact X has experience, Repo Y provides tool
└─ Output: Assignment + task list

Agent 4: EXECUTION ROUTER
├─ Purpose: Route work to humans or agents
├─ Logic: "If venture is early-stage, escalate to founder"
├─ Logic: "If contact is high-warmth, escalate to sales"
└─ Output: ClickUp tasks + agent assignments

Agent 5: FEEDBACK LOOP
├─ Purpose: Learn from outcomes
├─ Input: "Did contact respond? Did venture close? Why?"
└─ Output: Refined matching scores + routing rules
```

### n8n Workflows (Automation)

```
Workflow 1: GitHub → Graph
  Trigger: New repo starred
  → Fetch metadata
  → Normalize
  → Add to graph
  → Extract capabilities
  → Create nodes for new capabilities
  → Link to ventures that need them

Workflow 2: Obsidian → Graph
  Trigger: Obsidian note updated
  → Parse YAML frontmatter
  → Update graph node
  → Find related contacts/ventures
  → Refresh edges

Workflow 3: Contact Enrichment
  Trigger: New contact added
  → Run OSINT enrichment
  → Extract capabilities from profile
  → Query: "Which ventures need this person?"
  → Auto-create ClickUp tasks

Workflow 4: Deal Routing
  Trigger: New lead in ClickUp
  → Query graph: "Who in our network knows this person?"
  → Find warm intro path
  → Assign to warmest contact
  → Auto-draft email
```

---

## 🎯 LAYER 6: EXECUTION (Business Actions)

### System Outputs (What Actually Happens)

**For Ventures**:
```
Query: "What should we do next for venture ECOM-001?"
System Response:
  1. Venture needs: CEO, COO, Sales Lead, 3 partners
  2. Available in network: Contact A (CFO, not CEO), Contact B (sales)
  3. Recommendation: Contact A → introduce to CEO role, Contact B → lead sales
  4. Auto-created tasks:
     - Reach out to Contact A with CEO role description
     - Reach out to Contact B with sales lead offer
     - Find 2 CEO candidates through 2nd/3rd degree
```

**For Contacts**:
```
Query: "Where should Contact X focus their energy?"
System Response:
  1. Contact X has: Rust expertise, startup experience, network of 500+
  2. Ventures matching: 8 tech startups need CTO
  3. Ventures where contact can open doors: 12 companies in network
  4. Recommendation: Introduce contact to TECH-037 as CTO, TECH-042 as advisor
  5. Value to contact: equity, advisory fees, partnership
```

**For Agents**:
```
Query: "Assign today's work"
System Response:
  - Agent 1: Call 5 warm leads (Contact D, E, F, G, H)
  - Agent 2: Research 3 new venture sectors
  - Agent 3: Enrich 20 new contacts with OSINT
  - Agent 4: Draft emails to 10 potential partners
  - Agent 5: Analyze why 2 deals stalled (feedback learning)
```

---

## 📊 IMPLEMENTATION CHECKLIST (Phase 0 → Phase 1)

### PHASE 0: INFRASTRUCTURE (THIS WEEK)

- [ ] **Neo4j Setup**
  - [ ] Install Neo4j (local or cloud)
  - [ ] Define node + edge schema
  - [ ] Create indexes for queries

- [ ] **Ingestion Pipeline**
  - [ ] GitHub → Graph (import 640 repos)
  - [ ] Obsidian → Graph (import 200 notes)
  - [ ] Supabase → Graph (import ventures, contacts, agents)
  - [ ] CSV → Graph (import 58 contacts + template)

- [ ] **engraph Setup**
  - [ ] Configure Obsidian vault connection
  - [ ] Set up API endpoints
  - [ ] Test Obsidian ↔ Graph sync

- [ ] **LlamaIndex Integration**
  - [ ] Index all repos (620 readmes)
  - [ ] Index Obsidian vault (200 notes)
  - [ ] Index architecture docs (40 docs)
  - [ ] Test semantic search

- [ ] **CrewAI Agents**
  - [ ] Define 5 agent roles (see above)
  - [ ] Set up tools (graph API, n8n, Supabase SDK)
  - [ ] Test agent orchestration

- [ ] **n8n Workflows**
  - [ ] Build Workflow 1 (GitHub → Graph)
  - [ ] Build Workflow 2 (Obsidian → Graph)
  - [ ] Build Workflow 3 (Contact Enrichment)
  - [ ] Build Workflow 4 (Deal Routing)

### PHASE 1: CAPABILITY MAPPING (WEEK 2)

- [ ] **Repo Purpose Mapping**
  - [ ] For each of 640 repos: "What business capability does this provide?"
  - [ ] Tag repos: graph-db, ai-rag, orchestration, osint, monitoring, etc.
  - [ ] Build capabilities index

- [ ] **Venture Requirements**
  - [ ] Pull 708 ventures from Supabase
  - [ ] Define: each venture needs (roles, capabilities, partners)
  - [ ] Calculate completeness score

- [ ] **Contact Capabilities**
  - [ ] Profile 58 existing contacts
  - [ ] Define: each contact has (skills, network, decision-making power)
  - [ ] Calculate fit scores for ventures

- [ ] **Graph Queries (Test)**
  - [ ] "Which repos provide crypto expertise?"
  - [ ] "Which contacts can fill CEO for fintech?"
  - [ ] "What's missing for E-commerce venture?"

### PHASE 2: EXECUTION (WEEK 3+)

- [ ] **Contact Gathering**
  - [ ] User gathers 6,000 contacts (2K + 4K)
  - [ ] System ingests + enriches automatically
  - [ ] Graph updates with new nodes + edges

- [ ] **Matching Engine**
  - [ ] For each venture: rank contacts by fit
  - [ ] For each contact: suggest ventures + roles
  - [ ] Generate routing recommendations

- [ ] **Outreach Automation**
  - [ ] n8n generates emails + ClickUp tasks
  - [ ] Agents make calls + gather responses
  - [ ] System learns from outcomes

---

## 🔥 KEY DIFFERENCES FROM BEFORE

**Old Approach**: "Organize files, cross-reference, then execute"
- Problem: Files stay disconnected, no unified query layer
- Result: Manual navigation, fragmented system

**New Approach**: "Build graph → expose as API → agents query → routes execution"
- Solution: Single source of truth (graph DB), automated routing
- Result: Intelligent system that improves itself through feedback

---

## ✅ SUCCESS METRICS

| Metric | Phase 0 | Phase 1 | Phase 2 |
|--------|---------|---------|---------|
| Repos in graph | 640 | 640 | 640 |
| Capabilities mapped | 0 | 100+ | 200+ |
| Ventures mapped | 0 | 708 | 708 |
| Contacts in graph | 58 | 58 | 6,058 |
| Graph queries working | No | Yes | Yes |
| Automated workflows | 0 | 4 | 5+ |
| Contacts reached | 0 | 5-10 | 1,000+/week |

---

## 🚀 NEXT IMMEDIATE STEPS

1. **Install Neo4j** (choice: local, managed, cloud)
2. **Export data** from Supabase, Obsidian, GitHub
3. **Load graphs** (repos as nodes, contact capabilities as edges)
4. **Build engraph** (Obsidian API layer)
5. **Set up LlamaIndex** (semantic search over all documents)
6. **Deploy CrewAI agents** (5 core roles defined above)
7. **Create n8n workflows** (automated ingestion + routing)

---

## 📁 FILES CREATED THIS SESSION
- UNIFIED-KNOWLEDGE-GRAPH-OS-v1.md (this file)
- all-starred-repos.txt (640 repos)
- starred-repos-full.json (metadata, when fixed)

