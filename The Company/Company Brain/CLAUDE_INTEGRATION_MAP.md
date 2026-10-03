---
type: integration-architecture
canonical: false
authority: intelligence-platform-layer
version: 1.0
updated_at: 2026-10-02T23:50:00Z
relates_to: CLAUDE_MASTER_ONTOLOGY
---

# CLAUDE_INTEGRATION_MAP — How Claude Fits in Company Brain

**Claude is one component in a multi-layer platform. This map shows the complete integration.**

**Last updated:** 2026-10-02  
**Architecture:** 22-layer cognitive pipeline  
**Status:** Production integration

---

## Layered Architecture

```
                    LAYER 22: COMPANY BRAIN
                    ─────────────────────
                    [Master Orchestration]
                    [Decision Doctrine]
                    [Reality Verification]
                              │
                ┌─────────────┼──────────────┐
                ↓             ↓              ↓
          LAYER 20:      LAYER 21:      LAYER 19:
         KNOWLEDGE      EXECUTION     ORCHESTRATION
         ─────────       ─────────      ──────────
         
        [[Capture]]      [[Transform]]     [[Coordinate]]
         [[Store]]        [[Execute]]       [[Route]]
         [[Retrieve]]     [[Deliver]]       [[Monitor]]
             │              │              │
        ╔════╩════╗      ╔═══╩═══╗     ╔══╩═══╗
        │          │      │       │     │      │
      OBSIDIAN   NEO4J  CLAUDE  MCP  OMNIROUTE
        │          │      │       │     │
        └──────────────────────────────┘
                    │
         ┌──────────┼──────────┐
         ↓          ↓          ↓
    MODELS     PROVIDERS    ROUTING
    ─────      ──────────    ──────
    
    Opus       Anthropic   Smart selection
    Sonnet     OpenAI      Cost optimization
    Haiku      Google      Cache affinity
    Fable      Azure       Failover logic
```

---

## Component Roles

| Component | Layer | Role | Interface |
|-----------|-------|------|-----------|
| **[[CLAUDE]]** | 21 | Intelligence + reasoning | API, Code, Cowork, Web |
| **[[OMNIROUTE]]** | 20 | Model routing + resilience | HTTP proxy, MCP |
| **[[MCP]]** | 20 | Tool protocol | REST, local servers |
| **[[OBSIDIAN]]** | 19 | Knowledge capture | Wiki links, markdown |
| **[[NEO4J]]** | 19 | Relationship graph | Cypher, MCP |
| **[[QDRANT]]** | 19 | Vector retrieval | HTTP, Python SDK |
| **[[DOCKER]]** | 18 | Runtime container | Container API |
| **[[TAILSCALE]]** | 17 | Network fabric | VPN tunnel |
| **[[GITHUB]]** | 16 | Repository intelligence | Git, GitHub API, graft MCP |

---

## Data Flow

### Inbound (User → Claude)

```
User Input (chat, code, API)
        ↓
    [[CLAUDE_CONTEXT]]
        ↓
[Assemble from [[OBSIDIAN]]]
[Assemble from [[NEO4J]]]
[Assemble from [[QDRANT]]]
        ↓
[[CLAUDE_MASTER_ONTOLOGY]]
    (System prompt with Company Brain instructions)
        ↓
[[CLAUDE]]
    (Reasoning + planning)
```

### Outbound (Claude → System)

```
[[CLAUDE]]
    (Generates response + tool calls)
        ↓
    [MCP tool invocation?]
        ├─→ [[MCP]] → Execute tool
        ├─→ [[NEO4J]] → Query/update graph
        ├─→ [[QDRANT]] → Vector search
        ├─→ [[OBSIDIAN]] → Update notes
        └─→ [[GITHUB]] → Git operations
        ↓
[[OMNIROUTE]]
    (Log cost, manage cache affinity)
        ↓
[[REALITY]]
    (Verify outcomes + update state)
        ↓
User receives output
```

---

## Integration Points

### 1. System Prompt Layer
```
.claude/CLAUDE.md
    ↓ [Loaded by Claude Code]
    ↓
[[CLAUDE_MASTER_ONTOLOGY.md]]
    (Company Brain instructions)
    ↓
[[CLAUDE]]
    (Reasoning with full context)
```

**Contains:**
- Company identity + authority
- Operating rules (ANTIGRAVITY)
- Sector taxonomy (35 sectors)
- Control plane references (500 CBPs)
- Architecture diagrams
- Permission/security policies

### 2. Context Assembly
```
User query
    ↓
Claude Code reads:
├─→ [[WHOIAM.md]] (who we are)
├─→ [[WHERE_WE_ARE.md]] (current state)
├─→ [[REALITY.md]] (verified facts)
├─→ Relevant sector doc
├─→ Relevant capability registry
└─→ Recent commits + git history
    ↓
Assembled context
    ↓
[[CLAUDE]]
    (Reasons with full picture)
```

### 3. Tool Discovery
```
Claude: "I need to query the graph"
    ↓
Claude Code discovers:
├─→ [[MCP]] tools available
├─→ Neo4j connection info
├─→ Qdrant vector DB
└─→ GitHub API credentials
    ↓
Claude invokes tool
    ↓
[[NEO4J]] ← Query
[[QDRANT]] ← Vector search
[[GITHUB]] ← Code navigation
    ↓
Results injected into response
```

### 4. Knowledge Graph Loop
```
Claude: "Update the venture status"
    ↓
    [Execute via [[NEO4J]] MCP]
    ↓
Query: MERGE (v:Venture {id: "VEN-001"}) 
       SET v.status = "staging"
       RETURN v
    ↓
[[NEO4J]]
    (Relationship update + audit)
    ↓
Claude:
├─→ Logs decision to Neo4j KG-007
├─→ Records SHA256 provenance
├─→ Updates [[REALITY]]
└─→ Notifies relevant agents
```

### 5. Cost + Routing
```
Claude API call
    ↓
[[OMNIROUTE]]
├─→ Analyze task complexity
├─→ Select model (Haiku vs Opus)
├─→ Check cache affinity
├─→ Route to cache holder if available
├─→ Execute on selected model
├─→ Return cost headers
└─→ Log token usage
    ↓
Cost visible in:
├─→ OmniRoute dashboard
├─→ Budget tracking
└─→ Token economics registry
```

### 6. Verification Loop
```
Claude: "Deployed to staging"
    ↓
[[CLAUDE_REALITY]]
    (Verify layer)
    ├─→ Run health check: `curl /health`
    ├─→ Check monitoring
    ├─→ Query [[NEO4J]] for deployment record
    ├─→ Compare with previous state
    └─→ Confidence score
    ↓
    If confidence < 0.85: Escalate
    If confidence ≥ 0.85: Update [[REALITY]]
    ↓
[[REALITY]] ← Updated fact
```

---

## Example Workflows

### Workflow 1: Feature Development
```
User: "Implement login retry logic"
    ↓
Claude Code:
├─→ Loads .claude/CLAUDE.md
├─→ Reads codebase context
├─→ Loads testing standards
├─→ Checks sector (SEC-XXX) requirements
└─→ Identifies MCP tools available
    ↓
[[CLAUDE]]
├─→ Plans approach
├─→ Creates branch: feature/login-retry
├─→ Writes code (read/edit via file system)
├─→ Runs tests (execute via shell)
├─→ Commits with audit (git)
└─→ Suggests PR
    ↓
Audit trail to [[NEO4J]] KG-007:
├─→ Task ID, venture ID
├─→ Confidence score
├─→ All files modified
├─→ Test results
├─→ Git commit SHA
└─→ Timestamp + provenance
```

### Workflow 2: Decision + Escalation
```
Alert: "Database CPU 95%"
    ↓
Claude: Assess situation
├─→ Query [[NEO4J]] for baseline metrics
├─→ Analyze logs via [[OBSIDIAN]] notes
├─→ Check monitoring dashboard
└─→ Confidence: 0.45 (L1 - too uncertain)
    ↓
Claude: Propose solutions
├─→ "Increase pool size? (requires restart)"
├─→ "Enable read replicas? (20 min setup)"
└─→ "Scale horizontally? (new instances)"
    ↓
User: "Try option 1"
    ↓
Claude: Escalate to L2
├─→ Confidence now 0.72 (approved)
├─→ Execute config change
├─→ Monitor health
└─→ Log decision to [[NEO4J]]
```

### Workflow 3: Learning Loop
```
Task: "Deploy to staging"
    ↓
Claude: Execute (L2 verified)
├─→ Build + test
├─→ Push to staging
├─→ Run smoke tests
├─→ Monitor for errors
└─→ Record result
    ↓
[[REALITY]] ← Updated
[[NEO4J]] ← Logged
    ↓
Learning:
├─→ Success: Confidence +0.02 for next deployment
├─→ Failure: Confidence -0.05, escalate to L1
└─→ Update Laya ML model
    ↓
Next similar task: Confidence adjusted
```

---

## Information Flow Diagram

```
                    ┌─────────────────┐
                    │  USER REQUEST   │
                    └────────┬────────┘
                             │
                ┌────────────┼────────────┐
                ↓            ↓            ↓
          [Load Context]  [Discover   [Check
           from:          Tools:      Policy]
                          
    ├─ WHOIAM       ├─ NEO4J MCP      ├─ ANTGRAVITY
    ├─ WHERE_ARE    ├─ QDRANT MCP     ├─ RESPECT
    ├─ REALITY      ├─ GITHUB MCP     ├─ REALITY
    ├─ Ontologies   ├─ DOCKER MCP     └─ CLAUDE.md
    └─ Registries   └─ Shell tools
                             │
                ┌────────────┼────────────┐
                ↓            ↓            ↓
            [[CLAUDE]]   [[OMNIROUTE]]  [[MCP]]
                │            │            │
                └────────────┼────────────┘
                             │
                    [Execute Tool Call]
                             │
        ┌────────────────────┼────────────────────┐
        ↓                    ↓                    ↓
    [[NEO4J]]           [[GITHUB]]           [[OBSIDIAN]]
    Update/Query        Commit/Push          Update Notes
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                  [[CLAUDE_REALITY]]
                   (Verify + Log)
                             │
                       ┌─────┴─────┐
                       ↓           ↓
                   [[REALITY]]  Confidence
                   Update       Score
```

---

## Key Integration Principles

1. **Single source of truth** — [[REALITY]] is authoritative
2. **Audit everything** — Neo4j KG-007 logs all decisions
3. **Verify claims** — Never trust assertion without test
4. **Cost visible** — Token cost apparent via OmniRoute
5. **Context complete** — Load full system context before reasoning
6. **Permissions enforced** — Respect CLAUDE.md + ANTIGRAVITY rules
7. **Escalation clear** — L0→L1→L2→L3 gates defined
8. **Rollback ready** — Always maintain recovery path

---

## Failure Modes + Recovery

### Claude calls tool, tool fails
```
Claude: "Deploy to production"
    ↓
MCP tool fails: "Network error"
    ↓
Claude: Automatic retry (3x with backoff)
    ↓
Still fails: Escalate
├─→ Log to [[NEO4J]]
├─→ Update [[REALITY]]
├─→ Notify ops team
└─→ Suggest manual intervention
```

### Context conflict
```
Claude: Claims X is true
Reality: Shows Y
    ↓
Drift detected
    ↓
Claude: "My context is stale, re-checking..."
    ↓
Query [[REALITY]] + [[NEO4J]]
    ↓
Acknowledge discrepancy
    ↓
Update reasoning
```

### Tool permission denied
```
Claude: Attempts file write
    ↓
Permission gate: "Path not in whitelist"
    ↓
Claude: Check .claude/CLAUDE.md
    ↓
Path rejected: Propose alternative
    ↓
User: Approve expanded permission
    ↓
Retry with new permission
```

---

## Testing Integration

**Before deploying Claude into new workflow:**

- [ ] Load all relevant context docs
- [ ] Test MCP tool discovery
- [ ] Verify [[REALITY]] queries work
- [ ] Run confidence scoring (Laya)
- [ ] Check audit logging to Neo4j
- [ ] Verify rollback procedures
- [ ] Monitor first 3 runs closely
- [ ] Adjust confidence thresholds if needed

---

**Canonical source:** [[CLAUDE_MASTER_ONTOLOGY]]  
**Related:** All layer docs (OMNIROUTE, OBSIDIAN, NEO4J, etc.)  
**See also:** [[TASK_EXECUTION_MASTER_ONTOLOGY]]


## Hardware & Folder Navigation for [[CLAUDE]]

To ensure Claude (and associated agent frameworks) can easily traverse the physical infrastructure, the integration map explicitly defines connectivity paths:

1. **[[MAC_STUDIO]] Navigation:** Claude can route queries via the alias `ssh macstudio` (configured in ~/.ssh/config) to trigger graph commands on the Neo4j instance running on the Studio.
2. **[[T7_SHIELD]] Navigation:** When instructed to backup or read bulk repositories, Claude will expect to mount and access `/Volumes/T7Shield`.
3. **[[COMPANY_BRAIN]] Folder:** The operational knowledge directory currently resides at `/Users/acebless/Documents/The Company/Company Brain` (on the Mac Air) and syncs to `/Volumes/T7Shield/Company Brain`. Claude uses `[[SYSTEM_CONNECTIVITY_WIRED]]` to resolve these mount points automatically.

