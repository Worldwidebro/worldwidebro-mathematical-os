[[STARTHERE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[CLAUDE]]

# Buzz Integration Plan — Company Brain Collaboration Layer

[[STARTHERE]] | [[CLAUDE.md]] | [[REPOSITORY-INTELLIGENCE-SYSTEM.md]]

**Scope:** Deploy Buzz as CP-028 (Collaboration Control Plane) to enable real-time human-AI agent collaboration  
**Updated:** 2026-09-06  
**Authority:** Infrastructure Control Plane (CP-027) + Agent Control Plane (CP-006)

---

## ARCHITECTURE OVERVIEW

**Problem Solved:**
- Repository Intelligence System (Phase 4-6) currently runs autonomously without human visibility
- Agents (AGT-013/014/015) publish to Neo4j silently — humans review results post-facto
- No mechanism for humans to ask clarifying questions during classification/scoring
- No audit trail of decision-making conversations

**Solution:**
Deploy Buzz as a unified workspace where:
1. **Layer 1 (Interactive):** repo-advisor, repo-deep-dive personas review repos in real-time
2. **Layer 2 (Autonomous):** AGT-013/014/015 post findings to Buzz channels, receive human feedback
3. **Humans + Agents:** Collaborate in shared channels with full cryptographic audit trails
4. **Persistence:** Decisions sync back to Neo4j for long-term knowledge graph

---

## DEPLOYMENT ARCHITECTURE

### System Topology

```
Mac Studio (100.87.214.70, 36GB, 12-core M4 Max)
│
├─ Buzz Relay (Rust) :8080
│  ├─ PostgreSQL (full-text search, event log)
│  ├─ Redis (pub/sub for real-time events)
│  └─ S3/MinIO (Blossom protocol media storage)
│
├─ Existing Services
│  ├─ Neo4j :7687/7474 (knowledge graph)
│  ├─ Qdrant :6333 (vector embeddings)
│  ├─ OmniRoute :20128 (model routing)
│  └─ Ollama :11434 (local LLM)
│
└─ Integration Layer
   ├─ buzz-cli (agent JSON workflows)
   ├─ buzz-sync-agent (events → Neo4j)
   └─ MCP bridge (Buzz → agents)
```

### Network Paths

| Component | Port | Location | Notes |
|-----------|------|----------|-------|
| **Buzz Relay** | 8080 | Mac Studio (Docker) | Primary collaboration hub |
| **Buzz Web UI** | 3000 | Mac Studio (Docker) | Human workspace interface |
| **Buzz Admin** | 3001 | Mac Studio (Docker) | Workspace management |
| **PostgreSQL** | 5432 | Mac Studio (Docker, separate from crm-postgres) | Event log storage |
| **Redis** | 6380 | Mac Studio (Docker) | Pub/sub for real-time updates |
| **S3/MinIO** | 9000 | Mac Studio (Docker) | Media attachments, patches |

---

## WORKFLOW INTEGRATION (Phase 4-6: Repository Intelligence)

### Before: Autonomous-Only (Current)

```
904 repos → AGT-013 (classify) → Neo4j
                                   ↓
                          (human reviews later)
```

**Problem:** No conversation. No human input during classification.

### After: Human-AI Collaboration via Buzz

```
904 repos → [Buzz Channel: repo-classification]
              │
              ├─ AGT-013 publishes findings (JSON event)
              │  └─ "EXT-REPO-00042: classified as [capability list]"
              │
              ├─ repo-advisor persona reviews in channel
              │  └─ "This looks like it fits CAP-027 + CAP-031, but why not CAP-015?"
              │
              ├─ AGT-013 responds
              │  └─ "CAP-015 requires X, this repo only has Y. Re-evaluating..."
              │
              ├─ AGT-013 updates classification
              │  └─ Event #2: "EXT-REPO-00042: updated classification"
              │
              └─ buzz-sync-agent publishes to Neo4j
                 └─ Merges classification + audit trail

[Result: Full conversation history in Buzz, final decision + reasoning in Neo4j]
```

### Channel Structure

```
Workspace: company-brain
├─ Channel: repo-classification (AGT-013 phase 4)
│  └─ Events: EXT-REPO-00001..00904 classifications
│     ├─ @repo-advisor reviews
│     ├─ @AGT-013 responds
│     └─ [audit trail: who said what, when, with evidence]
│
├─ Channel: repo-scoring (AGT-014 phase 5)
│  └─ Events: EXT-REPO-00001..00904 scores (10 dimensions)
│     ├─ @repo-deep-dive flags high-risk repos
│     ├─ @AGT-014 explains scoring
│     └─ [conversation flow]
│
├─ Channel: repo-disposition (AGT-015 phase 6)
│  └─ Events: EXT-REPO-00001..00904 disposition decisions
│     ├─ ADOPT / INTEGRATE / FORK / REFERENCE / MONITOR
│     ├─ Human override capability
│     └─ [approval gates, sign-off]
│
└─ Channel: repo-adoption-pipeline (AGT-017 phase 8)
   └─ Events: Sandbox testing, benchmarking, security scanning results
      ├─ Real-time test status
      ├─ Blocker surfacing
      └─ Adoption readiness tracking
```

---

## AGENT INTEGRATION

### AGT-013 (Classifier) → Buzz

**Current behavior:**
```bash
AGT-013 → neo4j_merge_classification() → Neo4j ✅ (silent)
```

**New behavior:**
```bash
AGT-013 → buzz-cli event publish \
  --channel repo-classification \
  --repo-id EXT-REPO-00042 \
  --payload '{
    "primary_capability": "CAP-027",
    "secondary_capabilities": ["CAP-031"],
    "architecture_layer": "Layer 3: Integration",
    "sector_relevance": [{"sector": "SEC-015", "score": 92}],
    "score": 78,
    "tier": "HIGH",
    "reasoning": "..."
  }' \
  → Buzz Channel (human-visible) ✅
  → Neo4j (async sync) ✅
```

### repo-advisor & repo-deep-dive Personas → Buzz

**Activation:**
```
User in Claude Code: "Activate Repository Intelligence Advisor mode"
         ↓
Persona checks: "New 5 unreviewed repos in #repo-classification"
         ↓
Reads Buzz channel via MCP bridge
         ↓
Publishes response: "@AGT-013: Why did you classify this as CAP-027?"
         ↓
AGT-013 sees mention, responds in same thread
```

---

## MCP BRIDGE (fastmcp_server.py Extensions)

**New tools:**

```python
@mcp.tool
def buzz_publish_event(channel: str, event_type: str, payload: dict) -> dict:
    """Publish an event to a Buzz channel (for agents)
    
    Args:
        channel: Buzz channel name (e.g., 'repo-classification')
        event_type: Event type (e.g., 'repo_classified', 'repo_scored')
        payload: Event data (JSON serializable)
    
    Returns:
        Event ID, timestamp, channel reference
    """
    # POST http://100.87.214.70:8080/api/channels/{channel}/events
    # Signed with agent's Nostr key
    pass

@mcp.tool
def buzz_read_channel(channel: str, limit: int = 50) -> list[dict]:
    """Read recent events from a Buzz channel (for personas)
    
    Args:
        channel: Channel name
        limit: Max events to return
    
    Returns:
        List of events with author, timestamp, content, reactions
    """
    # GET http://100.87.214.70:8080/api/channels/{channel}/events
    pass

@mcp.tool
def buzz_sync_to_neo4j(channel: str, event_id: str) -> dict:
    """Sync a completed Buzz conversation to Neo4j knowledge graph
    
    Merges:
    - Final classification/score/disposition
    - Audit trail (conversation thread)
    - Approvals/overrides
    
    Returns:
        Neo4j merge result with node properties + edge references
    """
    # Reads Buzz event + thread
    # Merges into Neo4j with references back to Buzz event IDs
    pass
```

---

## DEPLOYMENT STEPS

### Phase 1: Buzz Infrastructure (Week 1: Sep 6-12)

1. **Clone & Setup** (2h)
   ```bash
   cd /Volumes/LaCie/projects
   git clone https://github.com/block/buzz.git
   cd buzz
   ```

2. **Docker Compose** (2h)
   - Configure `docker-compose.yml` for Mac Studio
   - Mount `/Volumes/LaCie/buzz-data` for PostgreSQL
   - Expose :8080 (relay), :3000 (web), :3001 (admin)
   - Set up Redis on :6380, MinIO on :9000

3. **Network Wiring** (1h)
   - Add Buzz to docker network with existing services
   - Update Tailscale DNS for `buzz.macstudio.local`
   - Test connectivity: `curl http://100.87.214.70:8080/health`

4. **Initial Workspace** (2h)
   - Create workspace: `company-brain`
   - Create channels: repo-classification, repo-scoring, repo-disposition, repo-adoption-pipeline
   - Generate Nostr keys for AGT-013, AGT-014, AGT-015, AGT-017

### Phase 2: Agent Integration (Week 2: Sep 13-19)

1. **MCP Bridge** (4h)
   - Extend `_MCP/fastmcp_server.py` with buzz_* tools
   - Wire Buzz API calls to `/api/channels/{channel}/events`
   - Implement Nostr signing for agent events

2. **AGT-013/014/015 Rewiring** (4h)
   - Modify agent prompts to call `buzz_publish_event()` instead of direct Neo4j
   - Keep Neo4j writes, add Buzz publication
   - Test: Single repo → Buzz channel → human review → Neo4j sync

3. **Persona Integration** (3h)
   - Wire repo-advisor to read from `buzz_read_channel()`
   - Wire repo-deep-dive to monitor repo-scoring channel
   - Test: Persona sees new events, responds in-channel

### Phase 3: Sync & Persistence (Week 2-3: Sep 13-26)

1. **Event Sync Agent** (AGT-019: buzz-sync-agent) (4h)
   - Monitors Buzz channels for "final_decision" events
   - Reads conversation thread (audit trail)
   - Merges into Neo4j with `neo4j_merge_classification()` + Buzz event links

2. **Neo4j Schema Extension** (2h)
   - Add `buzz_event_id` field to ExternalRepository nodes
   - Add `buzz_thread_url` for full conversation reference
   - Add timestamp indices for sync ordering

3. **Bidirectional Sync** (2h)
   - Neo4j → Buzz: When scoring completes, post summary to disposition channel
   - Buzz → Neo4j: When human approves in Buzz, update Neo4j tier/status

---

## SUCCESS CRITERIA

✅ **Phase 1 Complete:**
- Buzz running on Mac Studio, accessible at `http://100.87.214.70:8080`
- Workspaces created, channels visible in web UI
- All services (relay, postgres, redis, minio) healthy

✅ **Phase 2 Complete:**
- AGT-013 publishes classification to Buzz #repo-classification
- repo-advisor persona reads channel, responds in real-time
- MCP bridge tools tested and working
- 5-10 repos run through full classification → Buzz → Neo4j flow

✅ **Phase 3 Complete:**
- buzz-sync-agent runs hourly, merges conversation threads
- Neo4j nodes have `buzz_event_id` + `buzz_thread_url`
- Human reviews in Buzz, approves/overrides, decision syncs to Neo4j
- Audit trail visible: why each repo was classified that way

---

## INTEGRATION WITH REPOSITORY INTELLIGENCE PHASES

| Phase | Current Flow | Buzz Flow | Status |
|-------|---|---|---|
| Phase 1-3 | Autonomous ingestion/normalize/enrich | No change (still autonomous) | ✅ No changes |
| Phase 4: Classify | AGT-013 → Neo4j (silent) | AGT-013 → Buzz channel (visible) + repo-advisor reviews | 🟡 Requires MCP bridge |
| Phase 5: Score | AGT-014 → Neo4j (silent) | AGT-014 → Buzz channel (visible) + repo-deep-dive reviews | 🟡 Requires MCP bridge |
| Phase 6: Disposition | AGT-015 → Neo4j (silent) | AGT-015 → Buzz channel (visible) + human approval gate | 🟡 Requires MCP bridge |
| Phase 7: Graph | buzz-sync-agent → Neo4j | buzz-sync-agent reads completed Buzz threads, merges with audit trail | 🟡 New agent (AGT-019) |
| Phase 8: Adopt | AGT-017 autonomous | AGT-017 publishes progress to repo-adoption-pipeline | 🟡 Optional transparency |
| Phase 9: Awesome | AGT-020 autonomous | No change (summary published to Buzz) | ✅ No changes |

---

## COST & EFFORT ESTIMATE

**Infrastructure:**
- Buzz Relay: ~500MB RAM resident, moderate CPU during events
- PostgreSQL: ~2GB for 100K events
- Redis: ~100MB for pub/sub
- Total: Fits in 36GB Mac Studio with room to spare

**Development:**
- Deployment setup: 6-7 hours
- MCP bridge (buzz_* tools): 4 hours
- Agent rewiring: 4 hours
- Sync agent (AGT-019): 4 hours
- Testing: 5 hours
- **Total: ~23 hours** (3 engineering days)

**Timeline:**
- Week 1 (Sep 6-12): Deploy Buzz, infrastructure wiring
- Week 2 (Sep 13-19): Agent integration, MCP bridge, first test run
- Week 3 (Sep 20-26): Sync, Neo4j integration, full Phase 4-6 test with 50 repos

---

## NEXT STEPS

1. ✅ Decision made: Implement Buzz (this doc)
2. 🟡 Clone Buzz repo, explore docker-compose configuration
3. 🟡 Adapt docker-compose for Mac Studio network
4. 🟡 Deploy Phase 1 infrastructure
5. 🟡 Create MCP bridge tools
6. 🟡 Rewire first agent (AGT-013) as test
7. 🟡 Run Phase 4 (classify) on 10-repo sample with Buzz collaboration
8. 🟡 Expand to full 904-repo Phase 4-6 pipeline

---

**Authority:** CP-027 (Infrastructure) + CP-006 (Agents)  
**Last Updated:** 2026-09-06  
**Status:** 🟡 Ready for implementation  
