# Runbook: Neo4j Agent Discovery Broken

**Status:** Agent matching returns empty results. Only YAML fallback working.

**MTTR:** 10-30 minutes | **Severity:** High | **Owned By:** Knowledge Graph Team

---

## Symptoms

**Operational Impact:**
- `/api/orchestrator/find-best-agents` returns empty array
- Agent matching shows "using fallback YAML registry" in logs
- Leaderboard queries return no results
- Capability matching shows 0% coverage

**Monitoring Alerts:**
- Neo4j query timeout (> 5s for agent discovery)
- Neo4j connection errors in logs
- Cypher query errors in browser (http://100.87.214.70:7474)

**User Reports:**
- "Orchestrator can't find any agents for my task"
- "Fallback YAML working but Neo4j is slow"
- "Discovery always returns 'unknown capability'"

---

## Root Cause Analysis

### Step 1: Check Neo4j Connectivity
```bash
# SSH to Mac Studio
ssh macstudio

# Test connection via CLI
curl -u neo4j:changeme http://100.87.214.70:7474/browser/

# Expected: HTML response (not error)
# Check Docker status
docker ps | grep neo4j

# Check Neo4j logs
docker logs neo4j 2>&1 | tail -50
```

**Findings:**
- [ ] Container running, port responding → Neo4j accessible
- [ ] Container crashed or not running → restart needed
- [ ] Port not responding → network/firewall issue
- [ ] High memory usage in logs → out of memory, needs restart

### Step 2: Check Neo4j Database Integrity
```bash
# Connect via browser at http://100.87.214.70:7474
# Username: neo4j, Password: changeme

# Run health check
CALL dbms.diagnostics.diagnosticQuery('systemConsistency')
YIELD data WITH data.status as status
RETURN status;

# Expected: 'OK' or 'PASSED'
# If: 'FAILED' → database corruption, see Step 2b below
```

**Via CLI:**
```bash
curl -u neo4j:changeme -X POST http://100.87.214.70:7474/db/neo4j/tx \
  -H "Content-Type: application/json" \
  -d '{"statements":[{"statement":"CALL dbms.diagnostics.diagnosticQuery(\"systemConsistency\")"}]}'
```

**If Failed — Step 2b: Restore from Backup**
```bash
# Neo4j backups stored in Docker volume
docker exec neo4j ls -lh /backups/

# If corruption detected, restore latest backup:
docker stop neo4j
docker run --rm -v neo4j_data:/data -v neo4j_backups:/backups \
  neo4j:latest neo4j-admin restore --from-path=/backups/neo4j-backup-YYYYMMDD.tar --force

docker start neo4j
# Wait 30s for startup, then re-run health check
```

### Step 3: Check Agent Nodes and Indexes
```cypher
// Count agent nodes in graph
MATCH (a:Agent) RETURN count(a) as agent_count;
// Expected: > 300 agents

// Check if capability indexes exist
SHOW INDEXES;
// Expected: index on Agent.id, Capability.id, Skill.id

// Check if constraint violated
MATCH (a:Agent) WHERE a.id IS NULL RETURN count(a);
// Expected: 0 (all agents must have ID)
```

**Via CLI:**
```bash
curl -u neo4j:changeme -X POST http://100.87.214.70:7474/db/neo4j/tx \
  -H "Content-Type: application/json" \
  -d '{"statements":[{"statement":"MATCH (a:Agent) RETURN count(a) as count"}]}'
```

**Findings:**
- [ ] agent_count = 0 → no agents loaded, check ETL step
- [ ] agent_count > 300 → agents present, check indexes
- [ ] Indexes missing → create indexes (see Step 3b below)
- [ ] NULL ids found → data corruption, needs cleanup

**Step 3b: Create Indexes (if missing)**
```cypher
CREATE INDEX agent_id_index IF NOT EXISTS FOR (a:Agent) ON (a.id);
CREATE INDEX capability_id_index IF NOT EXISTS FOR (c:Capability) ON (c.id);
CREATE INDEX skill_id_index IF NOT EXISTS FOR (s:Skill) ON (s.id);
CREATE CONSTRAINT agent_id_unique IF NOT EXISTS FOR (a:Agent) REQUIRE a.id IS UNIQUE;
```

### Step 4: Check Agent Discovery Query
```cypher
// Test the discovery query (simplified)
MATCH (c:Capability {ref_id: "CAP-001"})
OPTIONAL MATCH (a:Agent)-[r:HAS_CAPABILITY]->(c)
WHERE r.proficiency >= 0.7
RETURN a.name, a.success_rate, a.roi_multiple
LIMIT 5;

// Expected: Returns 1-3 agents with high proficiency
// If: Returns empty → capability node missing or no relationships
```

**Findings:**
- [ ] Query returns results → graph OK, issue in application
- [ ] Query returns empty → missing capability nodes or HAS_CAPABILITY relationships
- [ ] Query timeout (>5s) → index issue or graph too large, see Step 4b

**Step 4b: Check Query Performance**
```cypher
// Show query plan (expensive operation)
PROFILE MATCH (c:Capability {ref_id: "CAP-001"})
OPTIONAL MATCH (a:Agent)-[r:HAS_CAPABILITY]->(c)
WHERE r.proficiency >= 0.7
RETURN a.name, a.success_rate, a.roi_multiple
LIMIT 5;

// Look for "DB Hits" in output
// If > 50,000 DB Hits → queries inefficient, need better indexes
```

### Step 5: Check YAML Fallback Registry
```bash
# If Neo4j is down but YAML fallback is working:
ls -lh _REGISTRIES/CANONICAL/AGENT_REGISTRY.yaml

# Check if YAML registry is up-to-date
head -50 _REGISTRIES/CANONICAL/AGENT_REGISTRY.yaml | grep "last_updated"
# Compare to Neo4j last_sync_timestamp in database

# If YAML is stale (>1 week old), the fallback is serving stale data
```

---

## Immediate Action

### Option 1: Restart Neo4j Container (Low risk)
```bash
ssh macstudio

# Graceful restart
docker restart neo4j

# Wait 30 seconds for startup
sleep 30

# Verify running
docker ps | grep neo4j
curl -u neo4j:changeme http://100.87.214.70:7474/browser/ > /dev/null && echo "Neo4j OK"
```

### Option 2: Switch to YAML Fallback (Immediate relief)
```bash
# In OmniRoute config
orchestrator:
  agent_discovery_mode: 'yaml_only'  # Temporarily disable Neo4j
  # Set back to 'neo4j_with_fallback' after Neo4j fixed

# Restart OmniRoute
docker-compose -f services/omniroute/docker-compose.yml restart omniroute
```

### Option 3: Full Reindex (if indexes corrupted)
```bash
ssh macstudio

# Connect to Neo4j and rebuild indexes
docker exec neo4j cypher-shell -u neo4j -p changeme <<EOF
DROP INDEX agent_id_index IF EXISTS;
DROP INDEX capability_id_index IF EXISTS;
DROP INDEX skill_id_index IF EXISTS;
DROP CONSTRAINT agent_id_unique IF EXISTS;

CREATE INDEX agent_id_index FOR (a:Agent) ON (a.id);
CREATE INDEX capability_id_index FOR (c:Capability) ON (c.id);
CREATE INDEX skill_id_index FOR (s:Skill) ON (s.id);
CREATE CONSTRAINT agent_id_unique FOR (a:Agent) REQUIRE a.id IS UNIQUE;
EOF

# Wait 2-3 minutes for index creation
sleep 180

# Verify indexes
docker exec neo4j cypher-shell -u neo4j -p changeme "SHOW INDEXES;"
```

---

## Resolution

### Step 1: Identify Root Cause (from analysis above)

**If:** Neo4j container crashed
- Action: Restart container (Option 1 above)
- Root cause: Typically memory pressure or disk space

**If:** Database corruption
- Action: Restore from latest backup (Step 2b above)
- Root cause: Unclean shutdown or data anomaly
- Prevention: Enable WAL (write-ahead logging)

**If:** Missing agent nodes
- Action: Re-run ETL pipeline to reload AGENT_REGISTRY into Neo4j
- Root cause: ETL job failed or never ran

**If:** Index corruption
- Action: Rebuild indexes (Option 3 above)
- Root cause: Large data insertion without index awareness, or Neo4j crash during indexing

### Step 2: Sync Agent Data from YAML to Neo4j
```bash
# Run the YAML→Neo4j migration pipeline
cd _PIPELINES/yaml-to-neo4j
python3 migrate_agents.py --registry _REGISTRIES/CANONICAL/AGENT_REGISTRY.yaml

# Expected output:
# - Loaded 318 agents from YAML
# - Created XXX new Agent nodes
# - Updated XXX existing nodes
# - Migration complete
```

### Step 3: Re-Run Agent Discovery Query
```bash
# Test discovery endpoint
curl -s -X POST http://100.87.214.70:20128/api/orchestrator/find-best-agents \
  -H "Content-Type: application/json" \
  -d '{
    "task_id": "TEST-001",
    "description": "test query",
    "required_capabilities": ["CAP-001", "CAP-002"],
    "venture": "OPS-001",
    "budget": 500,
    "min_success_rate": 0.7
  }' | jq .

# Expected: Returns top 3 agents with scores
```

---

## Recovery

### Step 1: Verify Discovery Working
```bash
# Run full discovery test
curl -s -X POST http://100.87.214.70:20128/api/orchestrator/find-best-agents \
  -H "Content-Type: application/json" \
  -d '{
    "task_id": "RECOVERY-TEST",
    "description": "recovery verification",
    "required_capabilities": ["CAP-050", "CAP-051", "CAP-052"],
    "venture": "LT-005",
    "budget": 1000
  }' | jq '.agents | length'

# Expected: > 0 (should find agents)
```

### Step 2: Check Neo4j Query Performance
```cypher
// Verify indexes are working
CALL db.indexes() YIELD name, state RETURN name, state;

// Run slowest query to verify performance
PROFILE MATCH (c:Capability)
OPTIONAL MATCH (a:Agent)-[r:HAS_CAPABILITY]->(c)
RETURN a, c, r
LIMIT 100;
```

### Step 3: Enable Neo4j Monitoring
```yaml
# In docker-compose for Neo4j
neo4j:
  environment:
    NEO4J_dbms_memory_heap_initial_size: 4G
    NEO4J_dbms_memory_heap_max_size: 4G
    NEO4J_dbms_querylog_enabled: 'true'
    NEO4J_dbms_querylog_threshold: 1000ms  # Log queries > 1 second
```

---

## Prevention

### 1. Add Discovery Query Health Checks
```javascript
// Periodic health check (every 5 min)
async function checkAgentDiscovery() {
  const result = await neo4j.query(`
    MATCH (c:Capability) 
    OPTIONAL MATCH (a:Agent)-[HAS_CAPABILITY]->(c)
    RETURN count(distinct a) as agent_count, count(distinct c) as cap_count
  `);
  
  if (result.agent_count < 300) {
    logger.warn('Neo4j discovery degraded: only ' + result.agent_count + ' agents');
    switchToYamlFallback();
  }
}
```

### 2. Set Up Automated Index Rebuilds
```bash
# Cron job: Weekly index rebuild (low traffic window, 3am UTC)
0 3 * * 0 /opt/scripts/rebuild-neo4j-indexes.sh
```

### 3. Enable Continuous Backups
```bash
# Daily snapshot backups
0 2 * * * docker exec neo4j neo4j-admin dump --to=/backups/neo4j-backup-$(date +\%Y\%m\%d).tar
```

### 4. Add Neo4j Resource Limits
```yaml
# docker-compose.yml
neo4j:
  mem_limit: 8g
  memswap_limit: 8g
  pids_limit: 500
  # Alert if memory > 80%
```

### 5. Monitor Discovery Latency
```sql
-- Track discovery query performance
CREATE TABLE discovery_queries (
  timestamp TIMESTAMP DEFAULT NOW(),
  capability_id VARCHAR,
  agent_count INT,
  query_duration_ms INT,
  source TEXT ('neo4j' | 'yaml_fallback')
);

-- Alert if avg latency > 2s or fallback used > 5% of time
```

---

**Related Runbooks:**
- [[ORCHESTRATOR-TASK-STALLED]] (when task hangs due to bad agent match)
- [[DATABASE-POOL-EXHAUSTED]] (if Neo4j queries exhaust connections)

**Owned By:** Knowledge Graph Team  
**Escalation:** If discovery broken > 10 min, page knowledge graph oncall
