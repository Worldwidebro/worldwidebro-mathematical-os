# Phase 2 Execution Checklist

**Start Date:** Sep 17, 2026  
**Target Complete:** Oct 1, 2026  
**Authority:** User chose Option B (Graph-Native Refactor immediately)

---

## Pre-Execution (Today)

- [ ] Verify Neo4j connection: `curl -u neo4j:changeme http://100.87.214.70:7474/browser/`
- [ ] Verify Syncthing is syncing (Company-Brain folder should be live on both machines)
- [ ] Clone Phase 2 docs: Ensure all 4 architecture docs are in `_REFERENCE/`
  - [ ] MODEL-ROUTER-ARCHITECTURE.md
  - [ ] TOOL-GATEWAY-PERMISSIONS.md
  - [ ] AUTONOMOUS-LOOP-SPECIFICATION.md
  - [ ] SYSTEM-STATE-MODEL.md

---

## Phase 2a: Schema & Templates (Sep 17–18)

### Day 1: Deploy Neo4j Schema
```bash
# SSH to Mac Studio
ssh macstudio

# Run schema setup
docker exec company-brain-neo4j cypher-shell \
  -u neo4j -p changeme \
  -f /path/to/COMPANY-BRAIN-GRAPH-SCHEMA.cypher
```

- [ ] Schema deployed (all constraints + indexes created)
- [ ] Verify with: `docker exec company-brain-neo4j cypher-shell -u neo4j -p changeme "SHOW CONSTRAINTS"`

### Day 2: Verify Templates
```bash
# Test one template (Sector merge)
docker exec company-brain-neo4j cypher-shell -u neo4j -p changeme \
  'MERGE (s:Entity:Sector {entity_id: "SEC-001-Test"}) 
   RETURN s.entity_id'
```

- [ ] Sector template works
- [ ] Venture template works
- [ ] Relationship template works

---

## Phase 2b: YAML Migration (Sep 19–22)

### Day 1: Migrate Sectors (35 entities)
```bash
# Run ingestion pipeline
python3 _PIPELINES/graph_ingestion_pipeline.py \
  --registries sector \
  --neo4j-uri bolt://100.87.214.70:7687 \
  --neo4j-user neo4j \
  --neo4j-password changeme
```

- [ ] All 35 sectors ingested
- [ ] Verify: `MATCH (s:Entity:Sector) RETURN COUNT(*) AS count` (should be 35)
- [ ] Integrity gates pass (0 dangling references)

### Day 2: Migrate Ventures (789 entities)
```bash
python3 _PIPELINES/graph_ingestion_pipeline.py \
  --registries venture \
  --neo4j-uri bolt://100.87.214.70:7687 \
  --neo4j-user neo4j \
  --neo4j-password changeme
```

- [ ] All 789 ventures ingested
- [ ] Verify: `MATCH (v:Entity:Venture) RETURN COUNT(*) AS count` (should be 789)
- [ ] All 789 ventures linked to sectors via [:RELATES]

### Day 3: Migrate Tools (110 entities)
```bash
python3 _PIPELINES/graph_ingestion_pipeline.py \
  --registries tool \
  ...
```

- [ ] All 110 tools ingested
- [ ] Risk levels assigned (read/write/high-risk)

### Day 4: Migrate Agents + Capabilities (16 + 50+ entities)
```bash
python3 _PIPELINES/graph_ingestion_pipeline.py \
  --registries agent capability \
  ...
```

- [ ] All 16 agents ingested
- [ ] All 50+ capabilities ingested
- [ ] Agents linked to loops via [:EXECUTES]

---

## Phase 2c: Phase 2 Document Ingestion (Sep 23–24)

### Extract Entities from 4 Docs

For each Phase 2 doc:
```bash
# MODEL-ROUTER-ARCHITECTURE.md
# Extract: Model Router (Component), Route 80% to Ollama (Decision)
# Create: (:Component), (:Decision) nodes
# Wire: [:MENTIONS]->(Capability), [:DEPENDS_ON]->(Tool)
```

- [ ] MODEL-ROUTER: Extract Model Router, Route 80%, fallback chain → Neo4j
- [ ] TOOL-GATEWAY: Extract Tier system (READ/WRITE/HIGH-RISK), Permissions → Neo4j
- [ ] AUTONOMOUS-LOOP: Extract 7 steps, heartbeat schedule → (:Loop), (:Step) nodes
- [ ] SYSTEM-STATE: Extract query types, refresh frequency → (:Query) nodes

### Detect Contradictions

```bash
# Example: Autonomous Loop discrepancy
# YAML says: 5 steps (observe, plan, execute, record, learn)
# Phase 2 doc says: 7 steps (observe, understand, plan, execute, verify, record, learn)
# Action: Create [:CONTRADICTS] edge, flag contested: true, preserve both sources
```

- [ ] Contradiction detection: Query for conflicting [:RELATES] edges
- [ ] Manual review: Check CONTRADICTIONS.md for false positives
- [ ] Resolution: Human approval for promotion (or marking superceded)

---

## Phase 2d: Integrity Verification (Sep 25)

### Run All Gates

```bash
# Gate 1: Dangling references (should be 0)
MATCH (s:Source)-[r:MENTIONS]->(e) WHERE NOT e:Entity RETURN COUNT(*)

# Gate 2: Provenance completeness (should be 0)
MATCH (e:Entity) WHERE NOT (e)-[:DERIVED_FROM]->(:Source) RETURN COUNT(*)

# Gate 3: Contradiction consistency (should be 0)
MATCH (e:Entity)-[c:CONTRADICTS]->() WHERE NOT e.contested RETURN COUNT(*)

# Gate 4: Orphan detection (should be < 50)
MATCH (e:Entity) WHERE NOT ()-[:RELATES|:MENTIONS|:SUPPORTS|:DEPENDS_ON|:USES]->(e) 
RETURN COUNT(*)

# Gate 5: Source coverage (should be 14: 10 YAML + 4 Phase 2 docs)
MATCH (s:Source) RETURN COUNT(*)
```

- [ ] Gate 1: 0 dangling references ✅
- [ ] Gate 2: 0 missing provenance ✅
- [ ] Gate 3: 0 inconsistent contradictions ✅
- [ ] Gate 4: < 50 orphans (acceptable for new entities) ✅
- [ ] Gate 5: 14+ sources ✅

### Generate Report

```bash
# Save integrity report
cypher-shell -u neo4j -p changeme -f _REFERENCE/PHASE2-INTEGRITY-GATES.cypher > PHASE2-INTEGRITY-REPORT.txt
```

- [ ] Report generated
- [ ] All gates PASS
- [ ] Commit report to Git

---

## Phase 2e: YAML Retirement (Sep 26–30)

### Archive YAML Registries

```bash
mkdir -p _ARCHIVE/YAML-REGISTRIES-SEP-2026
mv _REGISTRIES/CANONICAL/ventures-by-sector.yaml _ARCHIVE/YAML-REGISTRIES-SEP-2026/
mv _REGISTRIES/CANONICAL/SECTOR_INDEX.yaml _ARCHIVE/YAML-REGISTRIES-SEP-2026/
# ... archive all 10 YAML registries
```

- [ ] All YAML registries archived to `_ARCHIVE/`
- [ ] README created in _ARCHIVE explaining archival date + reason

### Update Documentation

- [ ] Update all references from "see ventures-by-sector.yaml" → "query Neo4j"
- [ ] Update README: "Company Brain is now graph-native (Neo4j)"
- [ ] Create API migration guide (Neo4j queries for common lookups)

### Verify No Code References Old YAML

```bash
grep -r "ventures-by-sector" --include="*.py" --include="*.js" --include="*.sh"
grep -r "SECTOR_INDEX.yaml" --include="*.py" --include="*.js" --include="*.sh"
```

- [ ] No code references old YAML registries
- [ ] All code updated to query Neo4j

---

## Success Criteria

✅ **Entities:** ~3,000 entities (35 + 789 + 110 + 16 + 50+) in Neo4j  
✅ **Provenance:** Every entity traces to (:Source) via [:DERIVED_FROM]  
✅ **Contradictions:** Phase 2 docs vs. YAML detected and preserved  
✅ **Integrity:** All 5 gates pass  
✅ **Relationships:** All YAML relationships converted to [:RELATES] edges  
✅ **Graph Queries:** Neo4j query engine ready for OmniRoute integration  
✅ **Documentation:** API guides written, YAML archived  
✅ **Git:** All changes committed with proper attribution

---

## Rollback Plan (If Needed)

1. **Stop:** Don't delete YAML registries yet
2. **Query:** Export Neo4j to JSON: `CALL apoc.export.json.all('/tmp/company-brain-backup.json')`
3. **Restore:** `MATCH (n) DETACH DELETE n;` then reload from backup
4. **Revert:** Restore YAML registries from _ARCHIVE/

---

## Dependencies & Blockers

| Blocker | Owner | Resolution |
|---------|-------|-----------|
| Neo4j connection unstable | Mac Studio admin | Restart if needed: `docker restart company-brain-neo4j` |
| YAML escaping issues | Dev | Test parser on sample files first |
| Duplicate entity_ids | Dev | Audit ventures-by-sector.yaml before ingestion |
| Phase 2 docs not final | Claude | Use latest committed version (add date to source SHA) |
| Syncthing slow | Ops | File sync can take time; check periodically |

---

## Git Commits

Each phase should have a commit:

```bash
# Day 1
git commit -am "feat(phase-2): Deploy Neo4j schema + constraints + indexes"

# Day 2–3
git commit -am "feat(phase-2): Ingest sectors + ventures (824 entities)"

# Day 4
git commit -am "feat(phase-2): Ingest tools + agents + capabilities (176 entities)"

# Day 5
git commit -am "feat(phase-2): Extract + ingest Phase 2 docs (Model Router, Tool Gateway, Autonomous Loop, System State)"

# Day 6
git commit -am "feat(phase-2): Verify integrity gates (all pass)"

# Day 7
git commit -am "feat(phase-2): Archive YAML registries + update documentation"
```

All commits end with:
```
Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

---

## Next Phase (Post-Migration)

Once Phase 2 is complete:

1. **Phase 2a (Oct 1–7):** Wire OmniRoute to query Neo4j graph
2. **Phase 2b (Oct 8–14):** Implement graph-based agent routing (Model Router via Neo4j)
3. **Phase 2c (Oct 15–21):** Enable contradiction detection in live agents
4. **Phase 3 (Oct 22+):** Financial intelligence layer (Neo4j + Qdrant + PostgreSQL)

---

**Updated:** 2026-09-17  
**Authority:** User's explicit choice: "b" (Graph-Native Refactor immediately)  
**Reference:** [[PHASE-2-GRAPH-NATIVE-MIGRATION]]
