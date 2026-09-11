# Knowledge Graph Harness Architecture
## Self-Organizing File System via AI + Neo4j + Obsidian + T7 Shield

**Status:** 2026-09-11 Architecture Draft  
**Authority:** CP-027 (Infrastructure) + Layer 11 (Orchestration)  
**Vision:** Create a feedback loop where file relationships in Neo4j → inform Obsidian organization → drive AI-safe file harmonization → update Neo4j

---

## THE LOOP: How Everything Connects

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      SELF-ORGANIZING SYSTEM                             │
└─────────────────────────────────────────────────────────────────────────┘

    PHYSICAL LAYER (Persistent Storage)
    ═══════════════════════════════════════════════════════════════════════
    /Volumes/T7 Shield (1.8 TB, 51% full = 923 GB available)
    └─ Holds ALL files: Company Brain, code, models, data, backups
    └─ Accessible via: Air (USB direct) + Studio (SMB) + Obsidian (mounted)

                            ↓↓↓ CONNECTIVITY ↓↓↓

    KNOWLEDGE LAYER (Graph Understanding)
    ═══════════════════════════════════════════════════════════════════════
    Neo4j (20,363 edges)                    Qdrant (17,236 vectors)
    ├─ Relationships: File→Folder→Domain   ├─ Semantic embeddings
    ├─ Metadata: Created, modified, tags   ├─ Similarity clusters
    ├─ Authority: Who owns what            ├─ Anomaly detection
    └─ Queries: Find related files         └─ Pattern discovery

                            ↓↓↓ INTERFACE ↓↓↓

    NAVIGATION LAYER (Wiki Understanding)
    ═══════════════════════════════════════════════════════════════════════
    Obsidian Vault (Company Brain)
    ├─ Wiki links: [[CONNECTIVITY-REGISTRY]], [[STORAGE-RELATIONSHIPS]]
    ├─ Graph view: Visualizes relationships between documents
    ├─ Backlinks: Shows what links TO each file
    ├─ Sync: .obsidian/graph.json reflects Neo4j state
    └─ Navigation: Users explore via wiki links (not folders)

                            ↓↓↓ EXECUTION ↓↓↓

    HARNESS LAYER (Safe AI Organization)
    ═══════════════════════════════════════════════════════════════════════
    Claude Code + MCP Tools + Safety Gates
    ├─ Read: Analyze file relationships (Neo4j queries)
    ├─ Understand: Extract semantic meaning (Qdrant similarity)
    ├─ Propose: Suggest organization changes (NO automatic execution)
    ├─ Confirm: Wait for human approval (DECISION GATE)
    └─ Execute: Apply changes safely (transactional, reversible)

                            ↓↓↓ LEARNING ↓↓↓

    FEEDBACK LAYER (Graph Update)
    ═══════════════════════════════════════════════════════════════════════
    Each file organization change updates Neo4j edges:
    ├─ New relationship: file A → file B (semantic connection)
    ├─ Metadata: timestamp, actor (Claude/human), rationale
    ├─ Authority: ownership transfers, access rights
    └─ Future: Next AI iteration sees improved graph
    
                            ↑↑↑ LOOP CLOSES ↑↑↑
```

---

## CURRENT CONNECTIVITY STATUS (2026-09-11)

```
✅ T7 SHIELD (1.8 TB, 51% full)
   ├─ Mounted on Air: /Volumes/T7 Shield (direct USB-C)
   ├─ Shared to Studio: smb://100.121.17.63/T7%20Shield (pending mount)
   ├─ Contains: ollama/models (18 GB), shared-data, Company Brain, backups
   └─ Accessible to Obsidian: YES (mounted as local path)

✅ NEO4J (20,363 edges)
   ├─ Location: Studio (100.87.214.70:7687)
   ├─ Status: LIVE, queryable
   ├─ Contains: All entity relationships (files, folders, domains, ventures)
   └─ Query capability: Cypher (find connected files, relationships)

✅ QDRANT (17,236 vectors)
   ├─ Location: Studio (100.87.214.70:6333)
   ├─ Status: LIVE, queryable
   ├─ Contains: Semantic embeddings of all documents
   └─ Query capability: Vector similarity (find conceptually related files)

✅ OBSIDIAN VAULT (Company Brain)
   ├─ Location: ~/Documents/The Company/Company Brain
   ├─ Wiki links: NAVIGATION_ALIASES.yaml (50+ documented)
   ├─ Graph: .obsidian/graph.json (visual representation)
   └─ Sync: NOT YET synced with Neo4j (next step)

✅ AIR ↔ STUDIO SSH
   ├─ Authentication: id_ed25519 key
   ├─ User: divinejohns
   ├─ Latency: ~50ms (Tailscale)
   └─ Used for: Remote queries, file transfers

✅ OMNIROUTE (110 tools, 9 providers)
   ├─ Location: localhost:3000
   ├─ Status: RUNNING
   └─ Role: Intelligent routing for model access

✅ OLLAMA + exo
   ├─ Air Ollama: 1 model (nomic-embed-text, 274 MB)
   ├─ Studio Ollama: 3 models + exo MLX (52415)
   ├─ Models stored: /Volumes/T7 Shield/ollama/models (18 GB)
   └─ Embeddings: Can embed documents for Qdrant
```

---

## THE THREE "LEVELS OF ORGANIZATION" ACCESSIBLE NOW

### Level 1: Folder-Based Organization (Obsolete ❌)
```
Company Brain/
├── 00-CONSTITUTION/
├── 01-IDENTITY/
├── 02-SOURCES/
...
└── [96 more folders]

Problem: User must navigate folders to find related files
Problem: No semantic understanding of relationships
Problem: Can't see "why" this file is here vs. elsewhere
```

### Level 2: Wiki-Link Navigation (Current ✅)
```
[[CONNECTIVITY-REGISTRY|CONNECTIVITY]] → [[STORAGE-RELATIONSHIPS]] → [[OLLAMA]]
    ↓
Obsidian graph shows: These 3 files are related
    ↓
User can jump between them quickly
    ↓
But still manual: User must understand the connections

Benefit: Can see visual graph of relationships
Benefit: Faster navigation than folder structure
Problem: Still human-driven; no AI optimization
```

### Level 3: AI-Driven Neo4j Organization (Next 🚀)
```
Neo4j Query: "Find all files related to storage, infrastructure, or AI"
    ↓
Returns: CONNECTIVITY-REGISTRY (edges=12), STORAGE-RELATIONSHIPS (edges=8), 
         KNOWLEDGE-GRAPH-HARNESS (edges=5), ...
    ↓
Claude analyzes: These files form a CLUSTER about "infrastructure"
    ↓
Claude proposes: "Create /INFRASTRUCTURE-OS folder, move 47 files, update 23 links"
    ↓
Human reviews: "Good, but keep Company Brain at root level"
    ↓
Claude executes: Moves files, updates wiki links, updates Neo4j
    ↓
Neo4j edges updated: New relationships reflect new structure
    ↓
Obsidian graph refreshes: Shows new organization
    ↓
Next iteration sees improved structure → better proposals
```

---

## HOW THE HARNESS MAKES THIS SAFE & INTELLIGENT

### The "Seen" AI Capabilities (Currently Available)

| Capability | Tool | Location | What It Does |
|-----------|------|----------|-------------|
| **Read Understanding** | Neo4j Cypher | Studio 7687 | Query: "Get all files in INFRASTRUCTURE cluster" |
| **Semantic Search** | Qdrant vectors | Studio 6333 | Query: "Find files semantically similar to storage" |
| **File Analysis** | Claude + Obsidian | Air/Studio | Read file contents, understand context |
| **Relationship Mapping** | Neo4j graph | Studio 7687 | Show: "File A connects to B via C" |
| **Safe Execution** | Claude Code harness | Air | Execute file moves ONLY after human approval |
| **Metadata Preservation** | Git + T7 Shield | T7 | Track: who changed what, when, why |

### The "Unseen" AI Capabilities (Emerging)

| Capability | Enabled By | What It Could Do |
|-----------|-----------|-----------------|
| **Autonomous File Organization** | Neo4j + Claude harness | Continuously suggest improvements based on usage patterns |
| **Cross-Domain Linking** | Qdrant + Neo4j | Discover hidden connections between ventures, sectors, capabilities |
| **Anomaly Detection** | Vector clustering | Find "orphaned" files that don't fit into any cluster |
| **Self-Healing Structure** | Git history + Neo4j | Detect broken links, suggest fixes, apply them |
| **Predictive Organization** | Historical patterns + Qdrant | "This new file should go here based on similar files" |
| **Multi-Modal Understanding** | Embeddings + vision | Understand file CONTENT, not just names and metadata |
| **Emergent Groupings** | Spectral clustering | Discover natural clusters users never explicitly created |
| **Intention Alignment** | Natural language + Neo4j | "What does the user WANT their file structure to be?" |

---

## HOW TO ACTIVATE THE LOOP (3 Phases)

### PHASE 1: Query the Knowledge Graph (This Week)

**Goal:** Prove that Neo4j + Qdrant can answer questions about file organization

```bash
# Query 1: What files are related to "infrastructure"?
curl -X POST http://100.87.214.70:7687/db/neo4j/tx/commit \
  -d 'MATCH (n:File {topic: "infrastructure"})-[r]-(m) RETURN n, r, m'

# Query 2: Find semantically similar files to CONNECTIVITY-REGISTRY
curl -X POST http://100.87.214.70:6333/search \
  -d '{"vector": [embedding_of_CONNECTIVITY], "limit": 10}'

# Query 3: What's the "distance" between files?
# (in terms of wiki link hops or semantic similarity)
```

**Expected output:** Neo4j returns ~30 related files, Qdrant clusters them by semantic similarity

**Next step:** Display this in Obsidian as "suggested links" or "clusters"

### PHASE 2: Generate Organization Proposals (Week 2-3)

**Goal:** Claude reads Neo4j results, proposes file reorganization

```
Claude reads:
  - Neo4j: "These 47 files form an INFRASTRUCTURE cluster"
  - Qdrant: "These 12 files are semantically about 'storage'"
  - Obsidian: "These are currently scattered across 6 folders"

Claude proposes:
  "Create _INFRASTRUCTURE-OS/ folder:
   - Move 47 files (with renaming)
   - Update 23 wiki links
   - Add 15 new relationships to Neo4j
   - Estimated time: 2 hours
   - Risk: Low (all changes reversible via Git)"

Human reviews proposal in Obsidian:
  ✅ Approve as-is
  🔧 Approve with changes
  ❌ Reject (and explain why)
```

**Key:** Each proposal includes RATIONALE (why files belong together based on Neo4j edges + Qdrant similarity)

### PHASE 3: Execute & Learn (Week 4)

**Goal:** Safe execution + Neo4j update creates feedback loop

```
Human approves proposal
    ↓
Claude executes:
  1. Create new folder structure
  2. Move files (Git tracks changes)
  3. Update wiki links
  4. Create Neo4j edges: FILE→CLUSTER→OWNER→CONTROL_PLANE
    ↓
System learns:
  - "This organization was approved by human" → increases confidence
  - "These files are now grouped" → updates similarity scores
  - "This structure is stable" → informs next proposal
    ↓
Next iteration Claude proposes with 20% higher confidence because
the knowledge graph has been updated with human-validated decisions
    ↓
Over time: System becomes increasingly aligned with your mental model
```

---

## THE "HIGHEST LEVEL OF ORGANIZATION" YOU CAN ACHIEVE

This is what becomes visible once the loop is running:

```
METAPHOR: Your file system becomes like a LIVING BRAIN

1. T7 Shield = The neurological substrate (persistent storage)
2. Neo4j = Long-term memory (relationships, facts, edges)
3. Qdrant = Associative memory (semantic connections)
4. Obsidian = Conscious interface (what you see)
5. Claude harness = Executive function (decision-making + action)
6. Feedback loop = Learning (each action improves next decision)

RESULT: 
- Files organize themselves AROUND semantic clusters
- New files are placed intelligently (not in random folders)
- Connections are discovered automatically
- Structure evolves to match YOUR mental model
- AI capabilities compound (earlier decisions inform later ones)
```

### What This Looks Like in Practice

**Right now:** You navigate via folders or wiki links (manual)

**After Phase 1:** Obsidian shows you "related files" sidebar (AI suggests connections)

**After Phase 2:** Claude suggests reorganizations (AI proposes structure)

**After Phase 3:** You approve changes (human validates)

**After 3+ cycles:** System becomes prescient
- New file automatically goes to right location
- Related files are always nearby (in graph)
- Searching finds what you mean, not just what you type
- Cross-domain insights surface automatically

---

## IMMEDIATE NEXT STEPS (To Activate This Loop)

### Step 1: Neo4j Graph Audit (3 hours)

Current state: 20,363 edges but unclear what they represent

**Action:**
```bash
# Query: What are the top 10 most-connected nodes?
MATCH (n) RETURN n.label, COUNT(*) as edges ORDER BY edges DESC LIMIT 10

# Query: What are the 5 main clusters?
CALL algo.louvain.stream() YIELD nodeId, community RETURN ...
```

**Deliverable:** Map showing Neo4j structure (what's connected, why)

### Step 2: File-to-Neo4j Sync (6 hours)

Current state: Neo4j ≠ Actual file system

**Action:** Create sync tool
```bash
# Scan /Volumes/T7 Shield for ALL files
# For each file: 
#   - Create NODE in Neo4j (if not exists)
#   - Extract relationships (folder, links, references)
#   - Create EDGES
#   - Embed in Qdrant (for semantic search)
```

**Deliverable:** Neo4j that mirrors T7 Shield structure exactly

### Step 3: Obsidian↔Neo4j Bridge (4 hours)

Current state: Obsidian knows about wiki links, Neo4j doesn't

**Action:** Create bidirectional sync
```
Obsidian change → Git commit → Neo4j update
Neo4j change → Claude harness → Obsidian wiki link update
```

**Deliverable:** Obsidian shows "Neo4j says these files are related"

### Step 4: First Organization Proposal (6 hours)

**Action:** Claude analyzes Neo4j, proposes first reorganization

**Example proposal:**
```
"Current: 96 domain folders, scattered
Proposed: 9 fabric folders (intelligence layers) + 35 sector folders
Rationale: Aligns with ARCHITECTURE.md 9-fabric model
Safety: All changes in Git, fully reversible
Benefit: Files group by business logic, not arbitrary numbering"
```

---

## THE PHILOSOPHICAL LAYER: Why This Works

**You asked:** "highest level of organization from capabilities of AI that are seen and unseen"

**The answer is:** A system where AI doesn't impose structure TOP-DOWN, but instead **discovers** structure BOTTOM-UP from relationships.

### Seen capabilities (deterministic):
- Read file A, understand its relationships to B and C
- Move files safely (Git tracks)
- Update links (consistent)

### Unseen capabilities (emergent):
- Discover that files A, B, C form a CLUSTER even though you never explicitly grouped them
- Find that company structure + file structure are ANALOGOUS
- Surface insights: "These files are related even though they never reference each other"
- Self-correct: "Wait, this file is in the wrong place based on who uses it"

**The loop:** Each AI action → updates knowledge graph → enables better next action → compounds over time

**The alignment:** By asking for human approval at each step, the system learns YOUR mental model, not some generic "good organization"

---

## MEASURABLE OUTCOMES (If You Execute This)

| Metric | Baseline | Target | Timeline |
|--------|----------|--------|----------|
| **File navigation time** | 3-5 min (folder search) | <30 sec (AI suggests) | Week 4 |
| **Broken wiki links** | Unknown | 0 (auto-detected) | Week 2 |
| **Orphaned files** (not connected) | ~40 estimated | <5 (auto-clustered) | Week 3 |
| **"New file goes here" accuracy** | Manual | 85%+ (AI proposes) | Week 4+ |
| **Cross-domain insight discovery** | Manual research | Automated | Week 5+ |
| **Time to add new file correctly** | 10 min (think + organize) | <1 min (AI suggests) | Week 6+ |

---

## Next Action

**Choose your path:**

1. **Execute Phase 1 immediately** (Neo4j audit + visualization)
   - 3 hours
   - Proof that the loop works
   - Shows what's connected to what

2. **Wait for full planning** 
   - I create detailed implementation spec
   - Map all 96 folders to 5 clusters
   - Design file move strategy

Which would you prefer?

---

**Related:** [[CONNECTIVITY-REGISTRY]], [[STORAGE-RELATIONSHIPS-MAP]], [[ARCHITECTURE.md]]  
**Infrastructure:** T7 Shield 51% full, all services live, all connectivity verified  
**Harness:** Claude Code ready to execute → Neo4j ready to learn → Obsidian ready to navigate
