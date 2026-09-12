[[STARTHERE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[CLAUDE]]

# Next Steps: Company Brain Implementation Roadmap

**Date:** 2026-09-06  
**Status:** Architecture Complete, Deployment Ready  
**Scope:** 4-phase rollout (Sep-Dec 2026)

---

## WHAT'S BEEN DELIVERED

✅ **Multi-Layer Platform Architecture** (Complete design)
- 6 complementary systems with clear boundaries
- Synchronization patterns defined
- Control planes established (CP-031 through CP-034)
- Example workflows documented

✅ **Repository Intelligence System** (Phase 4-6 collaboration ready)
- Agency personas created (repo-advisor, repo-deep-dive)
- MCP tools extended (neo4j_query_entities, neo4j_merge_classification, omniroute_route_model)
- Two-layer execution model documented
- Phases 1-3 autonomous, Phases 4-6 collaborative via Buzz

✅ **Buzz Integration** (Infrastructure deployment guide ready)
- Full docker-compose configuration
- Network topology designed
- Channel structure defined
- 7-hour deployment timeline

✅ **Documentation** (5 new architecture documents)
1. COMPANY-BRAIN-ARCHITECTURE.md (783 lines)
2. BUZZ-INTEGRATION-PLAN.md (435 lines)
3. BUZZ-PHASE1-DEPLOYMENT.md (407 lines)
4. REPOSITORY-INTELLIGENCE-SYSTEM.md (updated with Buzz integration)
5. CLAUDE.md (updated with multi-layer architecture)

---

## IMMEDIATE NEXT STEPS (This Week)

### Priority 1: Phase 1 Buzz Deployment (Sep 6-12)
**Effort:** 7 hours | **Owner:** Infrastructure Team

**Steps:**
1. Clone Buzz repository from GitHub
2. Adapt docker-compose.yml for Mac Studio
3. Create /Volumes/LaCie/buzz-data directories
4. Build Buzz relay container (1-2 hours)
5. Deploy all 5 services (relay, postgres, redis, minio, web)
6. Verify health checks + connectivity
7. Create initial workspace + channels
8. Generate Nostr keys for 5 agents

**Success criteria:**
- ✅ Buzz relay responds on :8080
- ✅ Web UI accessible on :3000
- ✅ PostgreSQL, Redis, MinIO healthy
- ✅ All channels created + visible
- ✅ Agent keys generated and stored

**Commands:**
```bash
# Week 1: Follow BUZZ-PHASE1-DEPLOYMENT.md exactly
docker --context macstudio compose -f docker-compose.local.yml up -d
curl http://100.87.214.70:8080/health  # Verify relay
```

### Priority 2: Comp AI CRM & Twenty Evaluation (Start Sep 6, Complete Sep 12)
**Effort:** 4 hours | **Owner:** Architecture Team

**Steps:**
1. Clone trycompai/crm repository
2. Review architecture, agent tools, evidence ledger design
3. Document integration points with Company Brain
4. Clone twentyhq/twenty repository
5. Review CRM objects, custom fields, workflow automation
6. Document integration points with ClickUp + Neo4j
7. Create initial evaluation scorecards for both
8. Identify blocker questions for Phase 2 deployment

**Deliverables:**
- Comp AI CRM evaluation report (1-2 pages)
- Twenty CRM evaluation report (1-2 pages)
- Integration blockers identified
- Deployment dependency list (what's needed before Phase 2)

### Priority 3: Phase 4-6 Repository Intelligence Test Run (Sep 6-12)
**Effort:** 3 hours | **Owner:** Agent Team

**Steps:**
1. Select 10-repo sample from 904 repos
2. Run through Phase 1-3 pipeline (ingest/normalize/enrich)
3. Manually test Phase 4 (AGT-013) classification
4. Publish classification to Buzz (manual JSON event for now)
5. Have repo-advisor persona review in Buzz channel
6. Test buzz-sync-agent → Neo4j sync (manual trigger)
7. Verify full end-to-end flow

**Success criteria:**
- ✅ 10 repos normalized successfully
- ✅ Buzz channel receives classification event
- ✅ repo-advisor can read + respond
- ✅ Event syncs back to Neo4j
- ✅ Full audit trail captured in Buzz

---

## PHASE 2: MCP BRIDGE & AGENT INTEGRATION (Sep 13-19)

**Effort:** 10 hours  
**Deliverables:**
- MCP tools for Buzz (buzz_publish_event, buzz_read_channel, buzz_sync_to_neo4j)
- AGT-013/014/015 rewired to publish to Buzz
- First real test: Phase 4-6 on 50-repo sample
- Buzz threads successfully sync to Neo4j

**Key tasks:**
1. Implement buzz_* MCP tools in fastmcp_server.py
2. Wire AGT-013 to call buzz_publish_event()
3. Wire AGT-014 to call buzz_publish_event()
4. Wire AGT-015 to call buzz_publish_event()
5. Create AGT-019 (buzz-sync-agent) for event-to-Neo4j sync
6. Test Phase 4-6 end-to-end on 50-repo sample
7. Verify Buzz threads + Neo4j audit trail

---

## PHASE 3: BUSINESS OPERATIONS LAYER (Oct 1-31)

**Effort:** ~12 hours (across month)  
**Sequence:**

**Week 1 (Oct 1-7): Twenty Deployment**
- Deploy Twenty on Mac Studio
- Create company, person, deal objects
- Configure custom fields
- Wire Twenty webhooks

**Week 2 (Oct 8-14): ClickUp Integration**
- Create Phase 1 ClickUp workspace
- Set up folder/list structure
- Create first automation: Twenty deal won → ClickUp project
- Test end-to-end

**Week 3 (Oct 15-21): Comp AI CRM Deployment**
- Deploy Comp AI CRM
- Configure research agents
- Wire evidence ledger to Neo4j
- Set up rechecks + scheduling

**Week 4 (Oct 22-31): Cross-System Sync**
- Wire all syncs (Comp AI → Twenty → ClickUp → Neo4j)
- Test discovery flow: Comp AI finds fact → Twenty updated → ClickUp task created
- Create unified dashboard

---

## PHASE 4: FULL INTEGRATION (Dec 1-31)

**Effort:** ~6 hours (spread across month)

**Deliverables:**
- All 6 systems synced + operational
- Repository Intelligence Phase 9 produces ClickUp work
- Unified Neo4j dashboard
- Agent workflows fully operational
- 904-repo adoption pipeline live

---

## IMMEDIATE BLOCKERS TO RESOLVE

### 1. Buzz Build Complexity
**Current:** Rust project requires compilation  
**Risk:** 30-60 min build time  
**Solutions:**
- Option A: Use pre-built Docker image if available
- Option B: Build once on Mac Studio, tag as local image
- Option C: Check if binary releases available on GitHub

### 2. Database Separation
**Current:** Multiple PostgreSQL instances (existing crm-postgres, new buzz_postgres)  
**Risk:** Resource contention, configuration confusion  
**Plan:** Keep separate (different ports: 5432 existing, 5433 for Buzz)

### 3. Agent Key Management
**Current:** Nostr keys for 5 agents need to be generated + stored securely  
**Plan:** Generate during Phase 1, store in ~/.env.buzz (or Bitwarden)

### 4. Comp AI & Twenty Evaluation
**Blocker:** Need to understand exact API contracts before Phase 2  
**Action:** Complete evaluation this week (Sep 6-12)

---

## DECISION POINTS (Requires User Input)

### 1. Start Phase 1 Now?
**Question:** Should we begin Buzz deployment immediately (this week)?  
**Timeline Impact:** Yes = Sep 6-12 complete, Phase 2 ready Oct 1  
**No** = Delayed start, phases slip

**Recommendation:** YES — Buzz is critical path for Repository Intelligence collaboration

### 2. Which Should We Evaluate First: Comp AI or Twenty?
**Question:** Start with intelligence layer or business operations layer?  
**Recommendation:** Start with Comp AI (simpler architecture, fewer moving parts)

### 3. Build Buzz Relay or Use Pre-Built?
**Question:** Build from Rust source or find pre-built image?  
**Recommendation:** Check for pre-built images first (saves 30-60 min)

---

## SUCCESS METRICS

### By End of Phase 1 (Sep 26)
- ✅ Buzz running on Mac Studio
- ✅ Repository Intelligence Phase 4-6 collaborative (50-100 repos tested)
- ✅ Buzz → Neo4j sync working
- ✅ Agent personas actively reviewing in Buzz channels

### By End of Phase 2 (Oct 31)
- ✅ Comp AI CRM researching companies
- ✅ Twenty storing company/person/deal data
- ✅ ClickUp projects auto-created from Twenty deals
- ✅ Cross-system sync working (Comp AI → Twenty → ClickUp → Neo4j)

### By End of Phase 3 (Nov 30)
- ✅ All 6 systems deployed and operational
- ✅ Repository Intelligence Phase 9 producing ClickUp work
- ✅ Agent workflows fully operational across systems

### By End of Phase 4 (Dec 31)
- ✅ 904-repo adoption pipeline live
- ✅ Unified dashboards operational
- ✅ Genuine agentic OS running: research → business logic → execution → collaboration

---

## DOCUMENTATION TO READ

**Order of importance:**

1. **[[COMPANY-BRAIN-ARCHITECTURE.md]]** (This is the blueprint)
   - Read this first to understand the model
   - 15 min read, 1 hr study

2. **[[BUZZ-PHASE1-DEPLOYMENT.md]]** (The immediate task)
   - Step-by-step deployment guide
   - Follow exactly for Phase 1

3. **[[BUZZ-INTEGRATION-PLAN.md]]** (The context)
   - Why Buzz matters and how it fits
   - Reference for Phase 2 planning

4. **[[REPOSITORY-INTELLIGENCE-SYSTEM.md]]** (The workflow)
   - How repos flow through 9 phases
   - Updated with Buzz collaboration model

5. **[[CLAUDE.md]]** (The master reference)
   - Updated with multi-layer architecture
   - Control planes and infrastructure status

---

## RESOURCE REQUIREMENTS

### Computing Resources
- **Buzz stack:** ~1GB RAM resident, ~10GB storage (/Volumes/LaCie/buzz-data)
- **Fits in:** Existing Mac Studio capacity (36GB RAM, 4TB LaCie)

### Team Capacity
- **Week 1:** 14 hours (infrastructure + evaluation)
- **Week 2-4:** Ongoing, ~10 hours/week
- **Can be split:** Infrastructure work ≠ evaluation work

### External Resources
- GitHub access (already have)
- Docker (already have)
- Tailscale (already configured)

---

## GIT STATUS

**Recent commits:**
```
25c624b53 docs: Add multi-layer platform architecture to CLAUDE.md
5825b144b docs: Define Company Brain as integrated multi-layer platform
3eff01b6e docs: Add Buzz Phase 1 deployment guide
e0bc6dca1 feat: Add Buzz as CP-028 Collaboration Control Plane
ca4d4666f docs: Repository Intelligence System architecture with two-layer execution model
```

**Branch:** main  
**Ahead of origin/main:** 40+ commits  
**Status:** All infrastructure docs committed + ready

---

## FINAL CHECKLIST

Before declaring "Ready to implement":

- [ ] Reviewed COMPANY-BRAIN-ARCHITECTURE.md (agree with model)
- [ ] Reviewed BUZZ-PHASE1-DEPLOYMENT.md (ready to execute)
- [ ] Checked Mac Studio has space + resources (/Volumes/LaCie accessible)
- [ ] Docker context configured (docker --context macstudio ps works)
- [ ] Decided on Phase 1 start date
- [ ] Assigned team members to parallel work streams
- [ ] Created ClickUp projects for Phase 1-4 delivery

---

**Status:** ✅ ARCHITECTURE COMPLETE, DEPLOYMENT READY  
**Next Action:** Start Phase 1 Buzz deployment (or confirm start date)  
**Contact:** For any blockers, decisions, or clarifications

This is not a pilot. This is the real architecture for Company Brain.

