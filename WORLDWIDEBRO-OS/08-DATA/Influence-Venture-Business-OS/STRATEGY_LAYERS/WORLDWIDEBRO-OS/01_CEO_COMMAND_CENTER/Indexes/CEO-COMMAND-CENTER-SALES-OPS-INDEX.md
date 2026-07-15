# 📑 CEO Command Center — Sales/Ops Index
**Tactical Index for CEO Command Center Sales/Ops Tooling** (renamed 2026-07-03 from
`MASTER-INDEX.md` — this was never a competing master index, just a same-named sales-ops
file; see note below)
**Last Updated:** 2026-05-10  
**Status:** Phase 0 - System Awareness Build

> **Note:** this index is scoped to CEO Command Center sales/ops tooling (ClickUp, deal
> scripts, VAPI calling, OSINT enrichment) and dated 2026-05-10. For the current, broader
> system-wide entry point (4-Orb model + Holdings/OPCO/Tool/Repo layer), see
> `/Users/acebless/Documents/MASTER-INDEX.md`.

---

## 🎯 QUICK NAVIGATION

### I Need to Know
- **What are we building?** → [VENTURE-OPERATIONS-FRAMEWORK.md](VENTURE-OPERATIONS-FRAMEWORK.md)
- **How are we building it?** → [OPERATIONAL-ARCHITECTURE.md](OPERATIONAL-ARCHITECTURE.md)
- **What's our progress?** → [progress.md](progress.md)
- **What are the blockers?** → [BLOCKER-STATUS-SESSION-2.md](BLOCKER-STATUS-SESSION-2.md)
- **What files exist and how do they connect?** → [SYSTEM-INTEGRATION-MAP.md](SYSTEM-INTEGRATION-MAP.md)
- **How ventures/repos/graph connect now?** → [VENTURE-GITHUB-GRAPH-FLOW-MAP.md](VENTURE-GITHUB-GRAPH-FLOW-MAP.md)

### I Need to Execute
- **How do I structure ClickUp?** → [CLICKUP-SETUP-GUIDE.md](CLICKUP-SETUP-GUIDE.md)
- **What's the deal pipeline?** → [CLICKUP-PIPELINE-SETUP.md](CLICKUP-PIPELINE-SETUP.md)
- **What do I say to prospects?** → [DEAL-SCRIPTS-BY-SECTOR.md](DEAL-SCRIPTS-BY-SECTOR.md)
- **How do I reach people?** → [AI-CALLING-SYSTEM-ARCHITECTURE.md](AI-CALLING-SYSTEM-ARCHITECTURE.md)
- **What messaging works by sector?** → [SECTOR-SPECIFIC-MESSAGING.md](SECTOR-SPECIFIC-MESSAGING.md)

### I Need to Set Up Tools
- **How do I enrich contacts?** → [OSINT-ENRICHMENT-INTEGRATION.md](OSINT-ENRICHMENT-INTEGRATION.md)
- **How do I use OpenVolo CRM?** → [OPENVOLO-INTEGRATION-GUIDE.md](OPENVOLO-INTEGRATION-GUIDE.md)
- **How do I run AI agents?** → [AOC-SWARM-RUNNER.md](AOC-SWARM-RUNNER.md)
- **How do I set up VAPI calling?** → [VAPI-API-USAGE.md](VAPI-API-USAGE.md)

### I Need Contact Data
- **What's the contact schema?** → [CONTACT-DATA-TEMPLATE.csv](CONTACT-DATA-TEMPLATE.csv)
- **How do I extract contacts?** → [CONTACT-EXTRACTION-PLAN.md](CONTACT-EXTRACTION-PLAN.md)
- **How do I import to OpenVolo?** → [import_contacts_to_openvolo.py](import_contacts_to_openvolo.py)
- **How do I enrich them?** → [run_osint_enrichment.py](run_osint_enrichment.py)

### I Need Organizational Reference
- **Who are we and what's our structure?** → [ORG-CHART-OPERATIONAL.md](ORG-CHART-OPERATIONAL.md)
- **What do we need to complete?** → [COMPANY-BRAIN-COMPLETION-REPORT.md](COMPANY-BRAIN-COMPLETION-REPORT.md)
- **How do I procure vendors?** → [VENDOR-PROCUREMENT-OS.md](VENDOR-PROCUREMENT-OS.md)
- **How are starred repos becoming the AI operating system?** → [AI-BOSS-HOLDINGS-REPO-OPERATING-SYSTEM.md](AI-BOSS-HOLDINGS-REPO-OPERATING-SYSTEM.md)
- **What is the install priority order?** → [STARRED-REPOS-INSTALLATION-PRIORITY.csv](STARRED-REPOS-INSTALLATION-PRIORITY.csv)
- **What sources feed RAG?** → [RAG-INGESTION-MANIFEST.csv](RAG-INGESTION-MANIFEST.csv)

### I Need Planning Reference
- **What's the overall plan?** → [task_plan.md](task_plan.md)
- **What did we research?** → [findings.md](findings.md)
- **What decisions did we make?** → [PATH-DECISION.md](PATH-DECISION.md)
- **What are the deployment steps?** → [PHASE-1-DEPLOYMENT-GUIDE.md](PHASE-1-DEPLOYMENT-GUIDE.md)

---

## 📂 FILE ORGANIZATION BY CATEGORY

### STRATEGIC (Why We're Doing This)
```
VENTURE-OPERATIONS-FRAMEWORK.md     [880 lines] Architecture + data models
OPERATIONAL-ARCHITECTURE.md          [150 lines] 7-layer system design
COMPANY-BRAIN-COMPLETION-REPORT.md   [200 lines] Intelligence layer definition
ORG-CHART-OPERATIONAL.md             [100 lines] Organizational structure
```

### EXECUTION (How We Do It)
```
CLICKUP-SETUP-GUIDE.md              [300 lines] ClickUp structure
CLICKUP-PIPELINE-SETUP.md           [200 lines] Deal workflow
DEAL-SCRIPTS-BY-SECTOR.md           [400 lines] Sales messaging
SECTOR-SPECIFIC-MESSAGING.md        [350 lines] Industry-specific language
AI-CALLING-SYSTEM-ARCHITECTURE.md   [200 lines] VAPI integration
VENDOR-PROCUREMENT-OS.md            [250 lines] Supplier activation
```

### INTEGRATION (Tools & Systems)
```
OSINT-ENRICHMENT-INTEGRATION.md     [380 lines] Social media enrichment
OPENVOLO-INTEGRATION-GUIDE.md       [400 lines] CRM integration
AOC-SWARM-RUNNER.md                 [350 lines] Agent orchestration
VAPI-API-USAGE.md                   [150 lines] Calling system API
CONTACT-EXTRACTION-PLAN.md          [200 lines] Data extraction process
```

### DATA (Files & Schemas)
```
CONTACT-DATA-TEMPLATE.csv           Template with all contact fields
contacts-extracted.csv              58 imported contacts (v1)
CONTACTS-INITIAL.csv                Original contact source
STARRED-REPOS-INSTALLATION-PRIORITY.csv  664 repo install priority order
STARRED-REPOS-GOVERNANCE.csv        Repo sector/manager/venture governance map
RAG-INGESTION-MANIFEST.csv          Source registry for RAG ingestion
vapi-agent-bella-config.json        VAPI agent configuration template
vapi-agent-swift-config.json        VAPI agent configuration template
package.json                        Node dependencies
```

### CODE (Python Scripts)
```
import_contacts_to_openvolo.py      Bulk contact importer
run_osint_enrichment.py             Contact enrichment pipeline
```

### PLANNING (Progress Tracking)
```
task_plan.md                        Phase-by-phase plan (60% complete)
progress.md                         Session-by-session execution log
findings.md                         Research discoveries
BLOCKER-STATUS-SESSION-2.md         Known issues & resolutions
PATH-DECISION.md                    Decision log (A vs B vs C)
PHASE-1-DEPLOYMENT-GUIDE.md         Deployment checklist
PHASE-1-CHECKLIST.md                Task completion checklist
```

### INTEGRATION MAP (This Session)
```
SYSTEM-INTEGRATION-MAP.md           File relationships & awareness gaps
MASTER-INDEX.md                     This file - central navigation
```

---

## 🔗 FILE DEPENDENCY GRAPH

```
task_plan.md (HIGH LEVEL PLAN)
├─ References: all other files
├─ Feeds: progress.md
└─ Blocks: nothing yet

VENTURE-OPERATIONS-FRAMEWORK.md (ARCHITECTURE)
├─ References: ORG-CHART-OPERATIONAL.md
├─ References: DEAL-SCRIPTS-BY-SECTOR.md
├─ Requires: Contact capabilities (not yet defined)
└─ Requires: Venture completeness scoring (in progress)

ORG-CHART-OPERATIONAL.md
├─ Feeds: AOC-SWARM-RUNNER.md
├─ Feeds: AI-CALLING-SYSTEM-ARCHITECTURE.md
└─ References: positions table (Supabase)

OSINT-ENRICHMENT-INTEGRATION.md
├─ References: OPENVOLO-INTEGRATION-GUIDE.md
├─ References: run_osint_enrichment.py
├─ Feeds: contact enrichment workflow
└─ Target: 58 contacts (done) → 6,000 contacts (pending)

import_contacts_to_openvolo.py
├─ Reads: contacts-extracted.csv
├─ Writes: OpenVolo SQLite
├─ Feeds: run_osint_enrichment.py
└─ Status: 58/58 contacts imported

CLICKUP-SETUP-GUIDE.md
├─ Requires: Contact list (building)
├─ Requires: Venture list (building)
└─ Feeds: deal pipeline workflow

DEAL-SCRIPTS-BY-SECTOR.md
├─ Used by: AI-CALLING-SYSTEM-ARCHITECTURE.md
├─ Used by: VAPI agents (Bella, Swift)
└─ Based on: SECTOR-SPECIFIC-MESSAGING.md
```

---

## 🧠 CURRENT STATE SNAPSHOT

### What We Have ✅
- 687 ventures in Supabase (product data complete)
- 58 contacts imported to OpenVolo
- 58 contacts enriched with tier classification
- 29 organizational positions defined
- Full architecture documented (10,000+ lines)
- Sales scripts for 16 sectors
- OSINT tools ready for deployment
- VAPI calling system configured
- ClickUp structure planned

### What We're Building 🔄
- **Phase 0:** System integration & awareness (THIS WEEK)
- **Phase 1.1:** Venture completeness baseline (THIS WEEK)
- **Phase 1.2:** Contact capability assessment (via your calls)
- **Phase 1.3:** Network expansion (2nd/3rd degree mapping)
- **Phase 2:** Matching engine (contact → venture assignment)
- **Phase 3:** Execution (outreach campaigns + deal tracking)

### What's Missing ❌
- Obsidian knowledge base (not set up)
- Graphify network visualization (not deployed)
- RAG intelligence layer (not integrated)
- Contact capability graph (not built)
- Relationship mapping between contacts (not documented)
- 2,000 + 4,000 contacts (you'll gather these)
- Venture completeness baseline (we'll build this)

---

## 📊 SYSTEM COMPONENTS STATUS

| Component | Status | Location | Next Step |
|-----------|--------|----------|-----------|
| Strategic docs | ✅ 100% | ~/Documents/*.md | Keep updated |
| Execution docs | ✅ 100% | ~/Documents/*.md | Implement in ClickUp |
| Integration docs | ✅ 100% | ~/Documents/*.md | Deploy tools |
| Contact import | ✅ 100% | OpenVolo SQLite | Enrich 6,000 more |
| Contact enrichment | ✅ 58/58 | run_osint_enrichment.py | Scale to 6,000 |
| Org chart | ✅ 100% | Supabase positions | Assign people |
| ClickUp structure | 🔄 20% | Planned in guide | Build this week |
| Deal scripts | ✅ 100% | DEAL-SCRIPTS-BY-SECTOR.md | Use in agents |
| VAPI config | ✅ 100% | vapi-agent-*.json | Deploy agents |
| Venture data | ✅ 100% | Supabase | Build completeness baseline |
| **System awareness** | ❌ 0% | SYSTEM-INTEGRATION-MAP.md | **BUILD THIS WEEK** |
| Obsidian vault | ❌ 0% | ~/Obsidian/ | **SET UP THIS WEEK** |
| Graph DB | ❌ 0% | (Neo4j/TypeDB) | **PLAN THIS WEEK** |
| RAG system | ❌ 0% | (LlamaIndex) | **PLAN THIS WEEK** |

---

## 🚀 THIS WEEK'S WORK

### TASK 1: Cross-Reference All Files ⏳
- [ ] Add links in VENTURE-OPERATIONS-FRAMEWORK.md to related docs
- [ ] Add links in ORG-CHART-OPERATIONAL.md to agent/calling docs
- [ ] Add links in DEAL-SCRIPTS-BY-SECTOR.md to messaging docs
- [ ] Verify every file knows what uses it

### TASK 2: Inventory Starred Repos 📋
**NEED YOUR INPUT:** What repos do you have starred on GitHub?
- Run: `gh api "user/starred" --paginate --jq '.[] | .name'`
- Or browse: https://github.com/stars/[yourname]
- Tell me which ones directly enable this system

### TASK 3: Set Up Obsidian 🧠
- [ ] Create vault at ~/Obsidian/Worldwidebro
- [ ] Create folder structure (Ventures/, Contacts/, Departments/, Systems/)
- [ ] Link all markdown files
- [ ] Set up templates for venture and contact notes

### TASK 4: Understand Graphify 📊
**NEED YOUR INPUT:** Do you already have Graphify set up?
- If yes: How is it configured? What graphs exist?
- If no: Should we use web version or local? (https://github.com/calesthio/Crucix)

### TASK 5: Plan RAG Integration 🤖
- [ ] Determine: LlamaIndex vs LangChain
- [ ] Determine: Vector DB (Pinecone, Weaviate, Supabase pgvector)
- [ ] Write integration spec

### TASK 6: Prepare for Contact Gathering 📞
**YOUR PART:**
- [ ] Identify 2,000 contacts (Source A)
- [ ] Identify 4,000 contacts (Source B)
- [ ] Prepare calling script: "What do you do? What's your expertise?"
- [ ] Document responses in structured format

---

## 🎯 SUCCESS DEFINITION

When Phase 0 is complete:

✅ All files know about each other (cross-referenced)  
✅ Obsidian vault is live and indexed  
✅ Graphify shows contacts + 712 ventures (595 aligned repos + 258 infrastructure repos + 20 sector agents + 16 sector managers)  
✅ RAG system can answer "Who can fill CEO role?"  
✅ You've identified 6,000 incoming contacts  
✅ Contact capability schema is defined  

**Then we proceed to Phase 1 execution.**

---

## 📞 YOUR NEXT MOVE

**Before I build anything else:**

1. **Tell me about your starred repos**
   - What GitHub repos do you have starred?
   - Which ones directly enable this system?

2. **Tell me about Obsidian/Graphify status**
   - Do you have Obsidian set up already?
   - Do you have Graphify running?
   - Or should we build from scratch?

3. **Tell me about the 6,000 contacts**
   - Source A: Where are the 2,000 contacts?
   - Source B: Where are the 4,000 contacts?
   - What fields do they have (name only? email? title?)?

Once you answer these 3 questions, I can:
- Build the Obsidian integration
- Deploy Graphify with your data
- Set up the RAG layer
- Prepare for your contact enrichment calls

**Sound good?**
