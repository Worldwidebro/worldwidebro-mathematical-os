[[STARTHERE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[CLAUDE]]

# Phase 4: Buzz Collaboration Layer Deployment Guide

**Status:** 🟡 Ready to Deploy  
**Authority:** CP-028 (Collaboration Control Plane) + CP-027 (Infrastructure)  
**Timeline:** Week 2-3 (Sep 6-26, 2026)  
**Effort:** ~23 hours total (7h infrastructure + 8h MCP + 8h sync agent)

---

## OVERVIEW

Buzz is the human-AI collaboration layer for Company Brain. It enables:

1. **Real-time collaboration:** Agents publish to Buzz channels; humans review and provide feedback
2. **Audit trails:** Every decision is documented with full conversation history
3. **Knowledge persistence:** Buzz events sync to Neo4j with cryptographic signing
4. **Layer-bridging:** Connects autonomous Phase 4-6 (Repository Intelligence) with human oversight

### Architecture

```
Layer 1 (Interactive)        Layer 2 (Autonomous)       Buzz Workspace         Neo4j Knowledge Graph
─────────────────────        ───────────────────        ───────────────       ──────────────────────
repo-advisor          ←──────  AGT-013 (classify)  ──→  #repo-classification  ──→  [classification nodes]
repo-deep-dive        ←──────  AGT-014 (score)    ──→  #repo-scoring        ──→  [scoring dimensions]
(human review)               AGT-015 (disposition) ──→  #repo-disposition    ──→  [disposition records]
                             AGT-017 (adopt)      ──→  #repo-adoption-pipeline
                                                         ↓
                                                  [AGT-019: buzz-sync-agent]
                                                  (events → Neo4j with audit trail)
```

---

## PHASE 4.1: BUZZ INFRASTRUCTURE (Week 1: Sep 6-12)

**Goal:** Deploy Buzz relay, PostgreSQL, Redis, MinIO on Mac Studio

**Deliverables:**
1. ✅ `_INFRASTRUCTURE/buzz-docker-compose.yml` — Docker Compose configuration
2. ✅ `_INFRASTRUCTURE/init-buzz.sql` — Database initialization (workspaces, channels, schema)
3. ✅ `_INFRASTRUCTURE/deploy-buzz-phase1.sh` — Deployment automation script

### Step-by-Step Deployment

**Step 1: Prepare Environment**

```bash
# SSH to Mac Studio
ssh macstudio

# Verify Docker daemon running
docker ps

# Create data directories (if on local machine)
mkdir -p /Volumes/LaCie/buzz-data/{postgres,redis,minio,relay}
```

**Step 2: Deploy Buzz Services**

```bash
cd /Users/acebless/Documents/The\ Company/Company\ Brain/_INFRASTRUCTURE

# Make deployment script executable
chmod +x deploy-buzz-phase1.sh

# Run deployment
./deploy-buzz-phase1.sh

# Expected output:
# ✅ Services started
# ✅ Buzz Relay responding
# ✅ PostgreSQL ready
# ✅ Redis ready
# ✅ MinIO ready
# ✅ Initial workspace configured
```

**Step 3: Verify Deployment**

```bash
# Check all services running
docker --context macstudio ps | grep buzz

# Expected output:
# buzz_relay         (8080)
# buzz_postgres      (5433)
# buzz_redis         (6380)
# buzz_minio         (9000, 9001)

# Test Buzz Relay health
curl -I http://100.87.214.70:8080/health
# Expected: 200 OK

# Test PostgreSQL
psql -h 100.87.214.70 -p 5433 -U postgres -d buzz -c "SELECT COUNT(*) FROM channels;"
# Expected: 5 rows (repo-classification, repo-scoring, etc.)

# Test Redis
redis-cli -h 100.87.214.70 -p 6380 ping
# Expected: PONG
```

### Success Criteria (Phase 4.1)

- [ ] All 5 containers running (relay, postgres, redis, minio, web)
- [ ] Buzz relay responds to `/health`
- [ ] PostgreSQL accessible on port 5433
- [ ] Redis accessible on port 6380
- [ ] MinIO accessible on port 9000
- [ ] Workspace "company-brain" created
- [ ] 5 channels created (repo-classification, repo-scoring, repo-disposition, repo-adoption-pipeline, general)
- [ ] Initial SQL schema loaded

---

## PHASE 4.2: AGENT INTEGRATION (Week 2: Sep 13-19)

**Goal:** Wire agents to publish events to Buzz channels

**Deliverables:**
1. ✅ `_MCP/buzz_integration.py` — MCP tools for Buzz API (buzz_publish_event, buzz_read_channel, buzz_sync_to_neo4j)
2. 🟡 Agent rewiring — Modify AGT-013/014/015 to publish to Buzz
3. 🟡 Persona activation — repo-advisor and repo-deep-dive monitor channels

### MCP Tools (Already Implemented)

```python
# buzz_integration.py provides:

buzz_publish_event(
    channel: str,
    event_type: str,
    payload: Dict,
    thread_id: Optional[str],
    author: str,
    secret_key: Optional[str]
) -> Dict[event_id, channel, created_at, signature]

buzz_read_channel(
    channel: str,
    limit: int = 50,
    thread_id: Optional[str]
) -> Dict[events]

buzz_sync_to_neo4j(
    channel: str,
    event_id: str,
    neo4j_uri: str,
    neo4j_user: str,
    neo4j_password: str
) -> Dict[status, nodes_merged]

buzz_update_classification(
    repo_id: str,
    channel: str,
    event_id: str,
    primary_capability: str,
    secondary_capabilities: List[str],
    score: int,
    reasoning: str,
    author: str
) -> Dict[event_id, created_at]

buzz_create_agent_key(agent_name: str) -> Dict[public_key, secret_key]
```

### Agent Key Generation

```bash
# Create service keys for each agent (via Buzz API)
for agent in AGT-013 AGT-014 AGT-015 AGT-017 AGT-019; do
    curl -X POST http://100.87.214.70:8080/api/v1/workspaces/company-brain/service-keys \
      -H "Content-Type: application/json" \
      -d "{\"service_name\":\"$agent\"}" \
      | jq '.secret_key' > ~/.env.buzz.$agent
done

# Store in Bitwarden under "Buzz Agent Keys - Company Brain"
```

### Agent Rewiring Pattern

**Before (Phase 4-6 silent):**
```python
# In AGT-013 (classifier)
neo4j_merge_classification(repo_id, classification)  # ← Silent write to Neo4j
```

**After (Phase 4-6 with Buzz):**
```python
# In AGT-013 (classifier)
from _MCP.buzz_integration import buzz_publish_event

# 1. Classify repo
classification = classify_repo(repo)

# 2. Publish to Buzz (visible to humans)
buzz_publish_event(
    channel='repo-classification',
    event_type='repo_classified',
    payload={
        'repo_id': repo['id'],
        'primary_capability': classification['primary'],
        'secondary_capabilities': classification['secondary'],
        'score': classification['score'],
        'reasoning': classification['reasoning']
    },
    author='AGT-013'
)

# 3. Also write to Neo4j (persistence)
neo4j_merge_classification(repo_id, classification)
```

### Persona Monitoring

```python
# In repo-advisor persona (Layer 1 interactive)
from _MCP.buzz_integration import buzz_read_channel

# Monitor repo-classification channel
unreviewed = buzz_read_channel('repo-classification', limit=10)

# For each unreviewed classification, human decides:
# 1. "Looks right, approved" ✅
# 2. "Questions: why CAP-027 and not CAP-015?" → AGT-013 responds
# 3. "Override: should be CAP-015" → AGT-013 updates
```

### Success Criteria (Phase 4.2)

- [ ] MCP tools implemented and registered in ~/.claude/settings.json
- [ ] AGT-013 publishes classification to Buzz (not just Neo4j)
- [ ] repo-advisor reads #repo-classification channel
- [ ] repo-advisor can ask clarifying questions via Buzz
- [ ] AGT-013 responds to human feedback
- [ ] AGT-013 updates classification based on feedback
- [ ] Updated event published as threaded reply
- [ ] Full workflow tested with 5 repos

---

## PHASE 4.3: SYNC & PERSISTENCE (Week 2-3: Sep 13-26)

**Goal:** Persist Buzz events to Neo4j with full audit trail

**Deliverables:**
1. ✅ `_MCP/buzz_sync_agent.py` — AGT-019 (autonomous sync agent)
2. 🟡 Neo4j schema extension — buzz_event_id, buzz_thread_url fields
3. 🟡 Bidirectional sync testing

### Buzz Sync Agent (AGT-019)

The `buzz_sync_agent.py` implements:

```python
class BuzzSyncAgent:
    """
    Autonomous agent that:
    1. Monitors Buzz channels for "final_decision" events
    2. Reads complete conversation threads
    3. Verifies cryptographic signatures
    4. Merges into Neo4j with audit references
    5. Maintains sync state (never double-sync)
    """

    async def sync_channel(channel: str) -> int:
        # Fetch unsync'd events from Buzz
        # Process each event
        # Create Neo4j nodes with references
        # Return count synced

    async def process_event(event, channel) -> bool:
        # Create BuzzEvent node
        # Create relationships (CLASSIFIED_REPO, SCORED_REPO, DISPOSED_REPO)
        # Link to parent ExternalRepository
        # Verify signature

    async def run(interval_seconds=3600):
        # Run indefinitely, syncing every hour
        # Log all operations
        # Handle errors gracefully
```

### Neo4j Schema Extension

```cypher
-- Add Buzz-related fields to ExternalRepository
MATCH (repo:ExternalRepository)
SET repo.buzz_event_id = null,
    repo.buzz_thread_url = null,
    repo.classified_at = null,
    repo.scored_at = null,
    repo.disposition_at = null;

-- Create indexes
CREATE INDEX buzz_event_id IF NOT EXISTS
FOR (repo:ExternalRepository) ON (repo.buzz_event_id);

-- Create BuzzEvent node type
// Nodes created by buzz-sync-agent:
:
  BuzzEvent {
    event_id: UUID,
    channel: 'repo-classification' | 'repo-scoring' | 'repo-disposition' | 'repo-adoption-pipeline',
    event_type: 'repo_classified' | 'repo_classified_updated' | 'repo_scored' | 'repo_disposition' | ...,
    author: 'AGT-013' | 'repo-advisor' | 'human' | ...,
    payload: JSON,
    timestamp: ISO8601,
    signature: HMAC-SHA256,
    synced_at: ISO8601
  }
```

### Running AGT-019 (Buzz Sync Agent)

```bash
# Install dependencies
pip install neo4j requests asyncio

# Run as standalone service
python -m _MCP.buzz_sync_agent

# Expected output:
# 🚀 Starting Buzz Sync Agent (AGT-019)
# Sync interval: 3600s
# Running sync cycle...
# Syncing repo-classification...
# Found 42 events in repo-classification
# ✅ Synced 42/42 events from repo-classification
# Cycle complete: 142 events synced

# To run in background with systemd (production)
# Create /etc/systemd/system/buzz-sync-agent.service
# systemctl start buzz-sync-agent
# systemctl logs buzz-sync-agent
```

### Full Workflow: Event → Buzz → Neo4j

```
1. AGT-013 classifies repo
   └─ buzz_publish_event(channel='repo-classification', payload={...})
      └─ Event published to Buzz ✅
      └─ Event ID: 550e8400-e29b-41d4-a716-446655440000

2. repo-advisor reads channel
   └─ buzz_read_channel('repo-classification', limit=10)
      └─ Human sees: "EXT-REPO-00042 classified as CAP-027"

3. Human asks question (in Buzz channel)
   └─ "@AGT-013: Why not CAP-015?"

4. AGT-013 responds (reads channel, replies)
   └─ buzz_read_channel('repo-classification', limit=50)
      └─ buzz_publish_event(..., thread_id=original_event_id)
         └─ "CAP-015 requires X, this only has Y"

5. AGT-013 updates classification
   └─ buzz_update_classification(..., event_id=original_event_id)
      └─ "Updated: primary_capability = CAP-031"

6. AGT-019 syncs to Neo4j (hourly)
   └─ Reads all events in repo-classification since last sync
   └─ For each event:
      ├─ Creates BuzzEvent node
      ├─ Creates CLASSIFIED_REPO relationship
      ├─ Sets repo.buzz_event_id, repo.classified_at
      ├─ Links repo to parent Capability node
      └─ Stores audit trail (full conversation)

7. Result in Neo4j ✅
   └─ ExternalRepository has full history:
      ├─ buzz_event_id: 550e8400-...
      ├─ classified_at: 2026-09-13T14:32:00Z
      ├─ classification_reasoning: "..."
      └─ Conversation thread available for audit
```

### Success Criteria (Phase 4.3)

- [ ] AGT-019 (buzz-sync-agent) implemented
- [ ] Syncs Buzz events to Neo4j hourly
- [ ] BuzzEvent nodes created with full metadata
- [ ] CLASSIFIED_REPO, SCORED_REPO, DISPOSED_REPO relationships created
- [ ] Cryptographic signatures verified
- [ ] Neo4j audit trail complete (conversation visible)
- [ ] Full end-to-end test: Buzz → Neo4j works correctly
- [ ] No data loss, no duplicate syncs

---

## TROUBLESHOOTING

### Buzz Relay Not Responding

```bash
docker --context macstudio logs buzz_relay | tail -50

# Common issues:
# 1. Database not ready
#    → Check: docker logs buzz_postgres
# 2. Redis not accessible
#    → Check: docker exec buzz_relay redis-cli -h buzz_redis ping
# 3. MinIO bucket not created
#    → Run: docker exec buzz_minio mc mb minio/buzz-media
```

### Events Not Syncing to Neo4j

```bash
# Check AGT-019 logs
journalctl -u buzz-sync-agent -f

# Manually test sync
python -c "
from _MCP.buzz_sync_agent import BuzzSyncAgent
import asyncio

agent = BuzzSyncAgent()
result = asyncio.run(agent.sync_channel('repo-classification'))
print(f'Synced: {result} events')
"

# Check Neo4j for BuzzEvent nodes
cypher-shell -u neo4j -p changeme "MATCH (e:BuzzEvent) RETURN COUNT(e);"
```

### Agent Keys Missing

```bash
# Regenerate keys via API
curl -X POST http://100.87.214.70:8080/api/v1/workspaces/company-brain/service-keys \
  -H "Content-Type: application/json" \
  -d '{"service_name":"AGT-013"}' | jq '.secret_key'

# Store in environment
export BUZZ_AGT013_KEY="<key>"

# Use when publishing
buzz_publish_event(..., secret_key=os.getenv('BUZZ_AGT013_KEY'))
```

---

## INTEGRATION TIMELINE

| Week | Phase | Goal | Status |
|------|-------|------|--------|
| **Sep 6-12** | Infra | Deploy Buzz, PostgreSQL, Redis, MinIO | 🟡 Ready |
| **Sep 13-19** | Agent | MCP bridge, rewire AGT-013/014/015 | 🟡 Queued |
| **Sep 20-26** | Sync | AGT-019 running, full Phase 4-6 test | 🟡 Queued |

---

## FILES CREATED

**Infrastructure:**
- ✅ `_INFRASTRUCTURE/buzz-docker-compose.yml` — Service definitions
- ✅ `_INFRASTRUCTURE/init-buzz.sql` — Database schema + initial data
- ✅ `_INFRASTRUCTURE/deploy-buzz-phase1.sh` — Deployment automation

**MCP Integration:**
- ✅ `_MCP/buzz_integration.py` — buzz_publish_event, buzz_read_channel, buzz_sync_to_neo4j tools
- ✅ `_MCP/buzz_sync_agent.py` — AGT-019 autonomous sync agent

**Documentation:**
- ✅ `_INFRASTRUCTURE/PHASE4-BUZZ-DEPLOYMENT.md` — This file

---

## NEXT STEPS

1. ✅ Deploy Phase 4.1 infrastructure (week of Sep 6)
2. ✅ Create MCP bridge tools (week of Sep 13)
3. ✅ Rewire agents to publish to Buzz (week of Sep 13)
4. ✅ Launch AGT-019 sync agent (week of Sep 20)
5. ✅ Run Phase 4-6 with 50 repos through full Buzz workflow (week of Sep 20)
6. ✅ Expand to 904 repos once validated (week of Sep 27)

---

**Authority:** CP-028 (Collaboration Control Plane) + CP-027 (Infrastructure)  
**Status:** 🟡 Ready for Phase 4.1 deployment  
**Last Updated:** 2026-09-08
