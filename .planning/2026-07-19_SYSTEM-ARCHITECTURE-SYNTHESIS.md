# System Architecture Synthesis - 2026-07-19

Complete problem map, solution order, and file/agent plan from today's session.

---

## SUMMARY: ALL PROBLEMS + SOLUTION ORDER

### Problems Identified Today

**A. Architectural Clarity (SOLVED ✅)**
- Files didn't explain Tech Sector powers all OPCOs
- Solutions: Updated WHOAMI.md, CLAUDE.md; created TECH-SECTOR-CHARTER.md, OPCO-DEPENDENCY-ARCHITECTURE.md

**B. Disk Crisis (BLOCKING) 🚨**
- MacBook Air: 100% full (189GB/228GB, 166MB free)
- Cause: 21GB GitHub repos cloned locally
- Solution: Move repos to T7 canonical location, symlink on Air, free 20GB

**C. Scatteredness (DATA FRAGMENTED)**
- Same data in 2 places: MacBook Air vs T7 Shield
- No canonical location
- No sync mechanism (Air ↔ T7)
- Solution: T7 = source of truth; Air = working copy; n8n Master Sync (6h cadence)

**D. Underutilization (RESOURCES NOT OPTIMIZED)**
- T7 Shield 14_INFRASTRUCTURE (135GB) not used for repos
- MacBook Air (189GB) trying to be primary, full
- Solution: Clear separation: T7 = permanent; Air = working; GitHub = backup

**E. Missing Self-Awareness (SYSTEM CAN'T SEE ITSELF)**
- No health checks, no inventory, no sync status
- No way to know what's safe to delete
- Solution: Build TECH-050 (Venture OS Intelligence Engine) dashboard

**F. File Fragmentation (DOCUMENTATION SCATTERED)**
- Found: IZA-OS-CONSTITUTION.md, SECTOR-MIDDLEMAN-MATRIX.md (today: added 2 new docs)
- Missing: File ownership map, decision framework, agent setup guide
- Solution: Build BUSINESS-ARCHITECTURE-REFERENCE.md, DECISION-FRAMEWORK.md, OPCO-AGENT-SETUP.md

**G. Agent Orchestration Gap (AGENTS DON'T KNOW STRUCTURE)**
- OPCO Agents exist but don't know: dependencies, who to escalate to, what files document their role
- Solution: Wire agents to read dependency files; create agent setup checklist

---

## SOLUTION ORDER (Critical Path)

### TIER 1 (THIS WEEK - Blocks Everything Else)

**1. Disk Crisis Fix (2 hours)**
   - Commit + push local work (iza-os-rag-system, exo)
   - Move 21GB repos to T7 Shield canonical location
   - Create symlinks on Air
   - **Outcome:** Air: 100% → 85% full; T7: repos centralized

**2. Canonical Locations (1 hour)**
   - T7 Shield 14_INFRASTRUCTURE = repos canonical
   - T7 Shield 01_VENTURES = ventures canonical
   - T7 Shield 03_AGENTS = agent code canonical
   - **Outcome:** Single source of truth established

**3. SYSTEM-LOCATIONS.md (1 hour)**
   - T7 vs Air inventory
   - Clear: T7=canonical, Air=working, GitHub=backup
   - **Outcome:** Everyone knows where everything lives

**4. TECH-050 Spec (2 hours)**
   - Define Intelligence Engine (what it monitors, dashboards)
   - **Outcome:** TECH-050 spec written; dashboard can be built

**Tier 1 Total: 6 hours this week**

---

### TIER 2 (NEXT 2 WEEKS - Enables Agent Orchestration)

**5. BUSINESS-ARCHITECTURE-REFERENCE.md (Task #14, 2 hours)**
   - File ownership + decision authority
   - Who owns what, who reads what

**6. DECISION-FRAMEWORK.md (Task #15, 2 hours)**
   - Question → which file? → which agent?
   - Example: "Why is Supabase slow?" → points to file + agent

**7. OPCO-AGENT-SETUP.md (2 hours)**
   - Agent self-configuration guide
   - Each agent knows: dependencies, SLAs, escalation rules

**8. DATA-COMMUNICATION-ARCHITECTURE.md (2 hours)**
   - Data flow between systems
   - Supabase → Neo4j → Qdrant → n8n → agents

**9. SYNC-STRATEGY.md + n8n Master Sync (Task #13, 2 hours)**
   - Air ↔ T7 sync rules (T7 is authority, Air syncs 6h)
   - Conflict resolution

**Tier 2 Total: 10 hours over 2 weeks**

---

### TIER 3 (NEXT MONTH - Operational Excellence)

**10. TECH-050 Dashboard (Tasks #22-23, 8 hours)**
   - Real-time: health, missing capabilities, disk usage, cost allocation, sync status
   - **Outcome:** System fully self-aware

**11. Agent Decision Logs (2 hours)**
   - Audit trail for every agent action

**12. Cost Allocation Dashboard (3 hours)**
   - $/venture, $/OPCO visible

**Tier 3 Total: 13 hours over next month**

---

## WHO ORCHESTRATES (Agent Responsibilities)

### Tech Sector CTO
- **Owns:** CLAUDE.md, TECH-SECTOR-CHARTER.md, OPCO-DEPENDENCY-ARCHITECTURE.md
- **Builds:** TECH-050 spec, data communication architecture
- **Monitors:** System health via TECH-050 dashboard
- **Responsible for:** Infrastructure decisions, SLA management, system reliability

### Each OPCO President (6 agents)
- **Must read:** WHOAMI.md, OPCO-DEPENDENCY-ARCHITECTURE.md, TECH-SECTOR-CHARTER.md, IZA-OS-CONSTITUTION.md
- **Must know:** Dependencies, SLAs (max downtime), escalation path
- **Builds:** Venture pipeline, capability requirements
- **Queries:** TECH-050 dashboard when systems fail

### Hermes (Meta-Controller)
- **Owns:** IZA-OS-CONSTITUTION.md, BUSINESS-ARCHITECTURE-REFERENCE.md
- **Reads:** All files (system-wide view)
- **Coordinates:** Conflicts, capital allocation, strategic pivots

### DevOps / Infrastructure
- **Owns:** SYSTEM-LOCATIONS.md, SYNC-STRATEGY.md
- **Builds:** n8n Master Sync, symlinks, monitoring
- **Monitors:** Air ↔ T7 sync, disk space, repository health

### Data Team
- **Owns:** DATA-COMMUNICATION-ARCHITECTURE.md
- **Builds:** Supabase schema docs, data lineage
- **Monitors:** Data consistency, sync lag

---

## FILE READING ASSIGNMENT

**All Agents Must Know (Governance):**
- WHOAMI.md — What this system is
- IZA-OS-CONSTITUTION.md — Decision authority, escalation rules

**OPCO Presidents Must Know (Dependencies):**
- OPCO-DEPENDENCY-ARCHITECTURE.md — What I depend on, SLAs, impact of outages
- TECH-SECTOR-CHARTER.md — Tech Sector responsibilities
- BUSINESS-ARCHITECTURE-REFERENCE.md — Who to escalate to

**Developers Must Know (Architecture):**
- CLAUDE.md — Operating System layers, platform vs ventures
- DATA-COMMUNICATION-ARCHITECTURE.md — How data flows

**DevOps Must Know (Operations):**
- SYSTEM-LOCATIONS.md — Where everything lives (T7 vs Air vs GitHub)
- SYNC-STRATEGY.md — How Air ↔ T7 sync works

---

## DATA FLOW

```
OPCO Agent Decision (start project)
        ↓
n8n Workflow Triggered
        ↓
Writes to Supabase (T7, source of truth)
        ↓
Syncs to: Neo4j, Qdrant, PostgreSQL
        ↓
TECH-050 Detects Change
        ↓
Alerts via Slack
        ↓
Other agents react (read TECH-050 dashboard)
        ↓
n8n Master Sync (6h): Air ↔ T7 (T7 is authority)
        ↓
GitHub Backup (code pushed upstream)
```

---

## Orchestration Example: Supabase Latency

1. **CON reads** OPCO-DEPENDENCY-ARCHITECTURE.md: "99.5% SLA on Supabase"
2. **CON sees alert** on TECH-050 dashboard: "Supabase latency 500ms (normal: 100ms)"
3. **CON escalates** per IZA-OS-CONSTITUTION.md: Infrastructure issue → Hermes → CTO
4. **CTO reads** TECH-SECTOR-CHARTER.md: "Performance <1s is my job" → optimizes query
5. **TECH-050 updates** dashboard: "Issue resolved, latency 250ms"
6. **CON informed** via Slack: "Fixed by CTO"
7. **Escalation logged** to venture_decisions table (audit trail)

**Files used:** OPCO-DEPENDENCY-ARCHITECTURE.md → IZA-OS-CONSTITUTION.md → TECH-SECTOR-CHARTER.md → TECH-050 dashboard

---

## Pages To Build (Master Checklist)

**THIS WEEK**
- [ ] SYSTEM-LOCATIONS.md — T7 vs Air inventory
- [ ] TECH-050-SPECIFICATION.md — Intelligence Engine spec

**NEXT 2 WEEKS**
- [ ] BUSINESS-ARCHITECTURE-REFERENCE.md (Task #14)
- [ ] DECISION-FRAMEWORK.md (Task #15)
- [ ] OPCO-AGENT-SETUP.md
- [ ] DATA-COMMUNICATION-ARCHITECTURE.md
- [ ] SYNC-STRATEGY.md + n8n Master Sync (Task #13)

**NEXT MONTH**
- [ ] TECH-050 DASHBOARD (Tasks #22-23) — Real-time monitoring

---

## Critical Path (What Enables What)

```
Fix Disk + T7 Canonical
        ↓
SYSTEM-LOCATIONS.md
        ↓
TECH-050 Spec
        ↓
OPCO-AGENT-SETUP.md (agents read files)
        ↓
BUSINESS-ARCHITECTURE-REFERENCE.md + DECISION-FRAMEWORK.md
        ↓
SYNC-STRATEGY.md + n8n Master Sync
        ↓
TECH-050 Dashboard
        ↓
Full Agent Orchestration
```

---

## Success (When Done)

- ✅ Air <80% full; T7 is canonical location
- ✅ All agents can read required files
- ✅ OPCO Presidents know SLAs, escalation paths, what to do when systems fail
- ✅ TECH-050 dashboard live (health, capabilities, cost, sync status)
- ✅ Any problem → agent can find responsible team via DECISION-FRAMEWORK.md
- ✅ No duplicate data (T7 = truth, Air = working copy)
- ✅ New OPCOs onboard in <1 hour via OPCO-AGENT-SETUP.md

---

## Timeline

- **Today/Tomorrow:** Move repos (2h)
- **By Friday:** +SYSTEM-LOCATIONS.md + TECH-050-SPEC.md (3h)
- **Next Week:** +BUSINESS-ARCHITECTURE-REFERENCE.md, DECISION-FRAMEWORK.md (4h)
- **Following Week:** +OPCO-AGENT-SETUP.md, SYNC-STRATEGY.md, n8n Master Sync (4h)
- **August:** +TECH-050 Dashboard, full orchestration (8h)

**Total: 25 hours over 4 weeks**
**By end of July: System knows itself**
**By end of August: Agents orchestrate everything automatically**
