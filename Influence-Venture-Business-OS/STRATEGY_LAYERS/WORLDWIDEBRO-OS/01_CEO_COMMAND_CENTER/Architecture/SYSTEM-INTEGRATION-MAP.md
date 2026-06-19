# 🧠 SYSTEM INTEGRATION MAP
**Status:** Phase 0 - Infrastructure Awareness  
**Date:** 2026-05-10  
**Purpose:** Connect all files, systems, and knowledge graphs into unified operational awareness

---

# 📁 EXISTING FILES & RELATIONSHIPS

## STRATEGIC DOCUMENTS (What We're Building)
```
VENTURE-OPERATIONS-FRAMEWORK.md
├─ REFERENCES: business_ventures (Supabase)
├─ REFERENCES: 58 contacts (OpenVolo)
├─ DEFINES: Role requirements per venture
├─ DEPENDS_ON: Contact capabilities (not yet complete)
└─ OUTPUT: ventures_completeness.csv (to build)

OPERATIONAL-ARCHITECTURE.md
├─ DESCRIBES: 7-layer system stack
├─ REFERENCES: CivilizationOS project
├─ DEPENDS_ON: VENTURE-OPERATIONS-FRAMEWORK
└─ STATUS: Architectural overview only

COMPANY-BRAIN-COMPLETION-REPORT.md
├─ DOCUMENTS: What intelligence layer needs
├─ DEFINES: Gap analysis framework
└─ STATUS: Planning document
```

## EXECUTION DOCUMENTS (How We Execute)
```
ORG-CHART-OPERATIONAL.md
├─ DEFINES: 29 positions (4 exec + 3 managers + 16 AI agents + 6 support)
├─ DEFINES: Authority levels (0-10 scale)
├─ REFERENCES: Supabase positions table
└─ STATUS: Operational structure defined

CLICKUP-SETUP-GUIDE.md
├─ DEFINES: 24 ClickUp lists structure
├─ DEFINES: 5 folder categories
├─ DEFINES: Workflow automation rules
└─ STATUS: Setup guide (not yet implemented)

CLICKUP-PIPELINE-SETUP.md
├─ DEFINES: Deal pipeline workflow
├─ DEFINES: Lead → Close status flow
└─ STATUS: Configuration template ready

DEAL-SCRIPTS-BY-SECTOR.md
├─ TEMPLATES: Outreach scripts (16 sectors)
├─ TEMPLATES: Discovery call scripts
├─ TEMPLATES: Close/negotiation language
└─ STATUS: Message templates ready
```

## INTEGRATION DOCUMENTS (Tools & APIs)
```
OSINT-ENRICHMENT-INTEGRATION.md
├─ DEFINES: Sherlock, Maigret, InstagramOSINT tools
├─ DEFINES: Enrichment pipeline (Tier 1-4)
├─ STATUS: Tool stack ready for deployment

OPENVOLO-INTEGRATION-GUIDE.md
├─ DESCRIBES: OpenVolo CRM (SQLite backend)
├─ STATUS: Running on localhost:3000 (or 3002)
├─ REFERENCES: import_contacts_to_openvolo.py

AOC-SWARM-RUNNER.md
├─ DESCRIBES: Agent orchestration system
├─ DEFINES: 554 available agents (qwen-*)
├─ REFERENCES: 5,264 AOC tasks queue
└─ STATUS: Ready for deployment

AI-CALLING-SYSTEM-ARCHITECTURE.md
├─ DEFINES: VAPI agent calling system
├─ REFERENCES: vapi-agent-*.json configs
└─ STATUS: Architecture ready

SECTOR-SPECIFIC-MESSAGING.md
├─ TEMPLATES: Sales messaging by sector (16 types)
├─ DEFINES: Industry-specific pain points
└─ STATUS: Messaging framework complete
```

## DATA FILES (What We Have)
```
Contacts Data:
├─ contacts-extracted.csv (58 contacts, v1)
├─ CONTACTS-INITIAL.csv (original source)
├─ import_contacts_to_openvolo.py (importer)
├─ run_osint_enrichment.py (enrichment engine)
└─ OpenVolo SQLite (live contacts DB)

Templates:
├─ CONTACT-DATA-TEMPLATE.csv (schema definition)
├─ vapi-agent-bella-config.json (VAPI template)
├─ vapi-agent-swift-config.json (VAPI template)
└─ CONTACT-EXTRACTION-PLAN.md (process definition)

Configuration:
├─ package.json (npm dependencies)
└─ .claude/settings.local.json (Claude Code settings)
```

## TRACKING FILES (Progress)
```
task_plan.md
├─ TRACKS: Phase 1-3 progress
├─ BLOCKS: Phase 2 → Phase 3
├─ STATUS: 60% complete

progress.md
├─ LOGS: Session-by-session execution
├─ STATUS: 6 sessions logged (Session 6 current)
└─ METRICS: 708 ventures, 2 CRM contacts, 0 deals

findings.md
├─ RESEARCH: Product audit findings
├─ RESEARCH: Network analysis findings
├─ STATUS: Research phase in progress

BLOCKER-STATUS-SESSION-2.md
├─ DOCUMENTS: Known blockers
└─ STATUS: Reference for unresolved issues
```

---

# 🔄 MISSING CONNECTIONS (Awareness Gaps)

## Problem 1: Files Don't Reference Each Other
```
VENTURE-OPERATIONS-FRAMEWORK.md
├─ Should reference: ORG-CHART-OPERATIONAL.md (role definitions)
├─ Should reference: DEAL-SCRIPTS-BY-SECTOR.md (outreach templates)
├─ Should reference: CONTACT-DATA-TEMPLATE.csv (contact schema)
└─ Should reference: import_contacts_to_openvolo.py (data pipeline)

OSINT-ENRICHMENT-INTEGRATION.md
├─ Should reference: run_osint_enrichment.py (live implementation)
├─ Should reference: OPENVOLO-INTEGRATION-GUIDE.md (data destination)
└─ Should reference: contacts-extracted.csv (source data)

ORG-CHART-OPERATIONAL.md
├─ Should reference: AOC-SWARM-RUNNER.md (AI agents list)
├─ Should reference: AI-CALLING-SYSTEM-ARCHITECTURE.md (execution layer)
└─ Should reference: CLICKUP-SETUP-GUIDE.md (tracking layer)
```

## Problem 2: No Unified Contact Graph
```
Currently:
├─ 58 contacts in OpenVolo (SQLite)
├─ 0 relationship mapping to ventures
├─ 0 capability assessment per contact
└─ 0 connection to 2,000 + 4,000 waiting contacts

Needed:
├─ Contact → Contact relationships (2nd/3rd degree)
├─ Contact → Venture role matches (capability → need)
├─ Contact → Venture department access (can they decide?)
└─ Contact → Network reach (who do they know?)
```

## Problem 3: No Central Intelligence Hub
```
Currently scattered across:
├─ Supabase (ventures, positions, agents)
├─ OpenVolo (contacts)
├─ ClickUp (deals, tasks)
├─ Local files (markdown, CSV, JSON)
└─ Markdown files (unconnected)

Needed:
├─ Single source of truth for venture requirements
├─ Single source of truth for contact capabilities
├─ Single querying layer (graph DB)
└─ Single visualization (Graphify)
```

---

# 🧠 SYSTEMS TO INTEGRATE

## 1. OBSIDIAN VAULT (Knowledge Base)
**Status:** Not yet set up  
**Purpose:** Central knowledge hub for all venture + contact intelligence

```
Proposed Structure:
Worldwidebro/
├─ Ventures/
│  ├─ Templates/
│  │  └─ [Venture Name]/
│  │     ├─ Overview.md (what, why, financials)
│  │     ├─ Requirements.md (roles, partners needed)
│  │     ├─ Contacts.md (who can fill gaps)
│  │     └─ Blockers.md (what's stopping progress)
│  └─ [SECTOR]/
│     └─ [Venture Name]/ (instance)
├─ Contacts/
│  ├─ Templates/
│  │  └─ [Contact Name]/
│  │     ├─ Profile.md (background, skills)
│  │     ├─ Capabilities.md (what they can do)
│  │     ├─ Network.md (2nd/3rd degree)
│  │     ├─ Ventures.md (which ventures match)
│  │     └─ Conversations.md (outreach history)
│  └─ [Name]/ (instance)
├─ Departments/
│  ├─ CEO (vision, strategy)
│  ├─ COO (operations)
│  ├─ CFO (finance)
│  ├─ Sales (revenue)
│  ├─ Product (development)
│  └─ Operations (execution)
└─ Systems/
   ├─ Governance (trusts, councils)
   ├─ Wealth Structure (dynasty framework)
   ├─ Succession Planning
   └─ Execution Tracking
```

**To Set Up:**
```bash
mkdir -p ~/Obsidian/Worldwidebro
cd ~/Obsidian/Worldwidebro
git init
```

**Obsidian ↔ Claude Integration:**
- Use LlamaIndex to index vault
- Queries: "Which contacts can fill CEO role for ECOM-001?"
- Updates: Auto-sync from Supabase → markdown notes

---

## 2. GRAPHIFY VISUALIZATION (Network Intelligence)
**Status:** Not yet deployed  
**Purpose:** Visual representation of contact-venture-role-opportunity graph

```
Node Types:
├─ Person (58 contacts + 6,000 incoming)
├─ Venture (687)
├─ Role (CEO, COO, CFO, Sales, Product, Ops)
├─ Department
├─ Company (where contacts work)
└─ Opportunity (deals, partnerships)

Edge Types:
├─ Person → Person (knows, introduced_by)
├─ Person → Role (can_fill, interested_in)
├─ Person → Venture (fit, can_access)
├─ Person → Company (works_at, founded)
├─ Venture → Role (needs)
├─ Venture → Department (requires)
└─ Department → Role (governs)

Visualization:
├─ Node color: Warmth score (red=hot, yellow=warm, blue=cold)
├─ Node size: Network reach (size = connections)
├─ Edge thickness: Trust strength (thick = warm intro)
└─ Clusters: Industries, departments, geographic regions
```

**To Set Up:**
```bash
# Install Graphify
npm install -g graphify

# Or use web version
https://github.com/calesthio/Crucix (user mentioned this)
```

---

## 3. RAG SYSTEMS (Intelligence Layer)
**Status:** Ready for integration  
**Purpose:** Extract insights from unstructured data, infer capabilities

```
LlamaIndex Integration:
├─ Index Obsidian vault (venture + contact notes)
├─ Index CSV files (contact metadata)
├─ Index markdown documents (architectural)
└─ Query: "What's the contact capability for role X?"

Query Examples (After RAG Setup):
├─ "Who can fill a CEO role for ECOM-001?"
│  → Searches contact profiles
│  → Ranks by fit score
│  → Returns top 5 matches with reasoning
├─ "What does Scoots Method have access to?"
│  → Searches network relationships
│  → Returns 2nd/3rd degree connections
│  → Identifies adjacent opportunities
└─ "What capabilities are missing for TECH-015?"
   → Searches venture requirements
   → Matches against contact capabilities
   → Flags gaps needing external hire/partnership
```

**To Set Up:**
```bash
pip install llama-index
pip install llama-index-llms-anthropic
pip install llama-index-readers-obsidian
```

---

## 4. MEMORY SYSTEMS (This Conversation)
**Status:** Active  
**Location:** /Users/acebless/.claude/projects/-Users-acebless-Documents/memory/

```
Current Memory:
├─ system-architecture.md (7-layer stack)
├─ user-context.md (Worldwidebro Holdings)
├─ feedback-code.md (coding preferences)
├─ project-state-2026-04-20.md (infrastructure status)
└─ MEMORY.md (index file)

To Add:
├─ system-integration-gaps.md (awareness gaps you found)
├─ contact-capability-schema.md (what you define when gathering names)
├─ venture-requirement-schema.md (what each venture needs)
└─ starred-repos.md (which open-source repos enable this)
```

---

# ⭐ STARRED REPOS & CAPABILITIES

**Need to inventory:**
```
Questions to answer:
1. What GitHub repos do you have starred?
2. Which ones directly enable this system?
3. What open-source tools are already in place?

Likely Candidates (based on your work):
├─ Crucix (relationship mapping + OSINT)
├─ Sherlock (username search)
├─ Maigret (deep dossier)
├─ InstagramOSINT (social profile extraction)
├─ LlamaIndex (RAG + knowledge base)
├─ NetworkX (graph analysis)
├─ Neo4j (knowledge graph DB)
├─ Apify (web scraping + LinkedIn access)
├─ VAPI (voice calling agents)
└─ OpenVolo (CRM running locally)
```

**To Find Your Starred Repos:**
```bash
# Via GitHub CLI (if authenticated)
gh api "user/starred" --paginate --jq '.[] | .name' | sort

# Via git locally (if cloned)
find ~ -maxdepth 3 -name ".git" -type d 2>/dev/null | xargs -I {} dirname {}
```

---

# 🚀 NEXT ACTIONS (In Order)

## PHASE 0.1: FILE AWARENESS (THIS WEEK)
- [ ] Create SYSTEM-INTEGRATION-MAP.md (this file) ✅
- [ ] Add cross-references to all existing markdown files
- [ ] Create central index (MASTER-INDEX.md)
- [ ] Update task_plan.md with file relationships

## PHASE 0.2: OBSIDIAN SETUP (THIS WEEK)
- [ ] Create Obsidian vault at ~/Obsidian/Worldwidebro
- [ ] Set up folder structure (Ventures, Contacts, Departments)
- [ ] Index existing CSV files into templates
- [ ] Link all markdown documents

## PHASE 0.3: GRAPHIFY SETUP (THIS WEEK)
- [ ] Install Graphify or use web version
- [ ] Design node/edge schema (from above)
- [ ] Create initial graph with 58 contacts + 687 ventures
- [ ] Test query: "Who can fill role X?"

## PHASE 0.4: RAG INTEGRATION (NEXT WEEK)
- [ ] Install LlamaIndex + Anthropic connector
- [ ] Index Obsidian vault
- [ ] Index all markdown files
- [ ] Test queries: "What capabilities do we have?"

## PHASE 1: CONTACT GATHERING (YOUR PART)
- [ ] Gather 2,000 contacts (source A)
- [ ] Gather 4,000 contacts (source B)
- [ ] Call each person: "What do you do? Can you help with X?"
- [ ] Document capabilities in structured format

## PHASE 2: SYSTEM EXECUTION (AFTER PHASE 0)
- [ ] Import 6,000 contacts into unified system
- [ ] Run OSINT enrichment (30-60 min parallel)
- [ ] Build contact → venture matching graph
- [ ] Execute outreach campaigns

---

# 📊 SUCCESS METRICS

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Files cross-referenced | 100% | 20% | 🔄 |
| Obsidian vault live | Yes | No | ⏳ |
| Graphify deployed | Yes | No | ⏳ |
| RAG system querying | Yes | No | ⏳ |
| Contact capability defined | Yes | No | ⏳ |
| 6,000 contacts integrated | Yes | 58 | ⏳ |

---

# 🔗 WORKING DOCUMENT

**This is a LIVE REFERENCE.** Update it as:
1. Files are created/deleted
2. Systems come online
3. New connections discovered
4. Capabilities inventory completed

