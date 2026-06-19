# Advanced Obsidian Knowledge Graph Stack

**Enterprise-grade semantic knowledge graph for your 712-venture OS**

Related: [[DASHBOARD-INDEX]] | [[skill-execution-framework]] | [[DASHBOARD-SETUP-GUIDE]]

---

## 🏗️ Complete Stack Architecture

```
Obsidian Vault (Local)
│
├── Core Visualization Layer
│   ├── Dataview (structured queries)
│   ├── Excalidraw (visual diagrams)
│   └── obsidian-graph (semantic navigation)
│
├── Link Intelligence Layer
│   ├── Semantic Linker (auto-link suggestions)
│   ├── Minder Nexus (ontology + typed relationships)
│   └── Vault Weaver (orphan detection + optimization)
│
└── Backend Intelligence Layer
    ├── PostgreSQL (relational store)
    ├── pgvector (semantic embeddings)
    ├── Neo4j (graph database)
    └── MCP (API layer)
```

---

## 📦 Layer 1: Visualization (Obsidian Plugins)

### Dataview
**Status:** ✅ Already using in dashboards
**Purpose:** Structured data queries over markdown
**Usage in Project:**
- [[SKILL-PROGRESS-DASHBOARD]] blocks 1-6
- [[SKILL-PROGRESS-BY-SECTOR]] sector tables
- Real-time queries from DuckDB

---

### Excalidraw
**Status:** 📦 Install via Community Plugins
**Purpose:** Visual architecture diagrams
**Use Cases:**
- 31-sector relationship diagram
- 14-phase skill execution workflow
- Venture dependency graphs
- Team organizational charts

**Get Started:**
1. Open Obsidian → Settings → Community Plugins
2. Search "Excalidraw" → Install
3. Create new note: `ARCHITECTURE-DIAGRAM.md`
4. Insert: `![[ARCHITECTURE-DIAGRAM.excalidraw]]`

---

### obsidian-graph
**Status:** 📦 Install from [GitHub](https://github.com/drewburchfield/obsidian-graph)
**Purpose:** AI-powered semantic search + relationship discovery
**Features:**
- Semantic search across vault
- Hub detection (finds central nodes)
- Orphan detection (finds disconnected notes)
- Multi-hop graph traversal
- MCP-compatible API

---

## 🔗 Layer 2: Link Intelligence (Obsidian Plugins)

### Semantic Linker
**Status:** 📦 Community Plugin
**Purpose:** Auto-suggest missing wiki links
**How it helps:** When writing about ventures, automatically suggests linking to:
- [[SKILL-PROGRESS-DASHBOARD]]
- [[venture-health.json]]
- [[sector_progress.sql]]

---

### Minder Nexus
**Status:** 📦 Community Plugin
**Purpose:** Typed relationships (ontology)
**Usage:** Replace generic links with typed relationships:

```markdown
# Venture Hub

uses:: [[DuckDB]]
depends_on:: [[Supabase]]
implements:: [[skill-execution-framework]]
tracks:: [[SKILL-PROGRESS-DASHBOARD]]
feeds_data_to:: [[Grafana]]
```

**Relationship Types:**
- uses, depends_on, implements, tracks, feeds_data_to, owned_by, manages, requires, triggers, references

---

### Vault Weaver
**Status:** 📦 Community Plugin
**Purpose:** Vault optimization
**Finds:**
- Broken links
- Orphan notes (unlinked)
- Duplicate content
- Missing graph connections

**Weekly Workflow:**
1. Run Vault Weaver scan
2. Review orphans
3. Fix broken links
4. Consolidate duplicates

---

## 🗄️ Layer 3: Backend Intelligence

### PostgreSQL Setup

**Installation (Mac):**
```bash
brew install postgresql
brew services start postgresql
createdb worldwidebro_os
```

**Create schema:**
```sql
CREATE TABLE entities (
  entity_id UUID PRIMARY KEY,
  entity_type VARCHAR(50),
  entity_name VARCHAR(255),
  description TEXT,
  metadata JSONB,
  created_at TIMESTAMP
);

CREATE TABLE relationships (
  relationship_id UUID PRIMARY KEY,
  source_id UUID REFERENCES entities,
  target_id UUID REFERENCES entities,
  relationship_type VARCHAR(100),
  strength FLOAT,
  metadata JSONB,
  created_at TIMESTAMP
);

CREATE INDEX idx_entity_type ON entities(entity_type);
CREATE INDEX idx_relationship_type ON relationships(relationship_type);
```

---

### pgvector Setup

**Installation:**
```bash
# In PostgreSQL
CREATE EXTENSION vector;

ALTER TABLE entities ADD COLUMN embedding vector(1536);

CREATE INDEX ON entities USING ivfflat (embedding vector_cosine_ops);
```

**Semantic search:**
```sql
SELECT entity_name, 1 - (embedding <=> query_embedding) as similarity
FROM entities
WHERE entity_type = 'skill'
ORDER BY similarity DESC
LIMIT 10;
```

---

### Neo4j Setup (Optional)

**Docker installation:**
```bash
docker run --restart unless-stopped \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/password \
  neo4j:latest
```

**Access:** http://localhost:7474

**Create graph model:**
```cypher
CREATE (v:Venture {id: 'SAAS-001', name: 'Venture Name'})
CREATE (s:Sector {id: 'SaaS', name: 'SaaS & Software'})
CREATE (sk:Skill {id: '/plan', phase: 4})
CREATE (v)-[:belongs_to_sector]->(s)
CREATE (v)-[:requires_skill]->(sk)
```

---

### MCP Server (API Layer)

**Endpoints for Claude integration:**
```
POST /mcp/graph/search
  → semantic search across vault

POST /mcp/graph/traverse
  → multi-hop relationship traversal

POST /mcp/entities/list
  → list entities by type

POST /mcp/relationships/find
  → find relationships between entities
```

---

## 🔄 Integration with Your Dashboard

### Connect Dashboards to Graph

**Update [[DASHBOARD-INDEX]] metadata:**
```markdown
entity_type: hub
entity_id: dashboard-index
manages:: [[SKILL-PROGRESS-DASHBOARD]], [[SKILL-PROGRESS-BY-SECTOR]]
depends_on:: [[skill-execution-framework]]
feeds_data_to:: [[Grafana]]
```

### Sync DuckDB → Neo4j

**Create sync script:**
```python
# sync_duckdb_to_neo4j.py
import duckdb
from neo4j import GraphDatabase

def sync_ventures():
    duckdb_conn = duckdb.connect('worldwidebro_os.duckdb')
    ventures = duckdb_conn.execute(
        "SELECT venture_id, venture_name, sector FROM ventures"
    ).fetchall()
    
    driver = GraphDatabase.driver("bolt://localhost:7687")
    with driver.session() as session:
        for venture_id, name, sector in ventures:
            session.run(
                "CREATE (v:Venture {id: $id, name: $name, sector: $sector})",
                id=venture_id, name=name, sector=sector
            )

sync_ventures()
```

**Run weekly:**
```bash
python3 sync_duckdb_to_neo4j.py
```

---

## 🚀 Installation Checklist

### Phase 1: Obsidian Plugins (1 hour)
- [ ] Install Dataview (built-in)
- [ ] Install Excalidraw
- [ ] Install obsidian-graph
- [ ] Install Semantic Linker
- [ ] Install Minder Nexus
- [ ] Install Vault Weaver

### Phase 2: PostgreSQL + pgvector (2 hours)
- [ ] Install PostgreSQL
- [ ] Create worldwidebro_os database
- [ ] Create entities + relationships tables
- [ ] Install pgvector extension
- [ ] Create vector indexes

### Phase 3: Neo4j (Optional, 2 hours)
- [ ] Docker: neo4j:latest
- [ ] Verify http://localhost:7474 loads
- [ ] Create venture/sector/skill nodes
- [ ] Test queries

### Phase 4: MCP Integration (2 hours)
- [ ] Setup obsidian-graph MCP server
- [ ] Test endpoints
- [ ] Connect to Claude Code

### Phase 5: Sync Automation (1 hour)
- [ ] Create sync script: DuckDB → Neo4j
- [ ] Create sync script: Obsidian → PostgreSQL
- [ ] Schedule weekly via cron

**Total time: 8 hours for complete stack**

---

## 📈 What This Unlocks

**Current State:**
- ✅ 5-node wiki graph (manual links)
- ✅ 6 Dataview blocks (structured queries)
- ✅ 2 Grafana dashboards (metrics)
- ✅ 5-min refresh cycle

**With Full Stack:**
- 🚀 Semantic search across vault
- 🚀 Auto-discovered relationships
- 🚀 Ontology-based queries (typed relationships)
- 🚀 Graph visualization (Neo4j + obsidian-graph)
- 🚀 Orphan detection (unused docs)
- 🚀 Hub detection (central nodes)
- 🚀 Multi-hop traversal (complex queries)
- 🚀 PostgreSQL backups (reliable)
- 🚀 MCP API (agents can query)

**Use Cases:**
- Find skills used by >50% of ventures
- Discover ventures in overlapping sectors
- Identify underutilized capabilities
- Find broken relationship chains
- Detect orphaned documentation

---

## 🔗 Related Dashboards

- [[DASHBOARD-INDEX]] (central hub)
- [[SKILL-PROGRESS-DASHBOARD]] (overview)
- [[SKILL-PROGRESS-BY-SECTOR]] (details)
- [[skill-execution-framework]] (framework)
- [[DASHBOARD-SETUP-GUIDE]] (operations)

---

## ⏱️ Quick Timeline

**Week 1:** Install plugins + run Vault Weaver scan
**Week 2:** Setup PostgreSQL + start entity sync
**Week 3:** Optional Neo4j deployment
**Week 4:** MCP API layer + test queries

Start with Phase 1 (plugins only) — they're free and immediately useful.
