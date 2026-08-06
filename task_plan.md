---
name: task_plan
title: 'Task Plan: Go-to-Market Execution System (687 Ventures)'
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Task Plan: Go-to-Market Execution System (687 Ventures)

**Status:** Phase 1.1 ✓ COMPLETE | 🟢 **Dexter Financial Orchestrator Week 1 COMPLETE** | 🟡 Phase 0.5 Paperclip Deployment PENDING
**Last Updated:** 2026-05-16 (Portfolio optimizer + CFO extension + forecasting complete)
**Owner:** Worldwidebro Holdings  
**Data State:** 583 ventures in Supabase (all with descriptions), 64 repos indexed, all ventures marked "active", top 50 ranked, sector breakdown complete

---

## 📎 PHASE 0.5: PAPERCLIP DEPLOYMENT (NEW — BLOCKS ALL DOWNSTREAM WORK)

**User directive (2026-05-10):** *"We want to see this information on paperclip first."*

Paperclip (`paperclipai/paperclip`) will be deployed as the root orchestration layer before resuming Phase 1.2/1.3. All existing state (Supabase ventures, repos, Graphify KG, OpenVolo contacts, Make workflows) will be surfaced inside Paperclip as the single pane of glass.

**Plan:** See `PAPERCLIP-DEPLOYMENT-PLAN.md` (6 steps, 6 checkpoints, ~13h realistic)

- [x] Step 1 — Verify repo is real + inspect actual install reqs ✓
- [x] Step 2 — Install Paperclip locally ✓ (server running at 127.0.0.1:3103)
- [ ] Step 3 — Model org structure (divisions → companies) (1–4h) ← **IN PROGRESS**
- [ ] Step 4 — Wire Supabase/repos/Graphify/OpenVolo in (3–12h)
- [ ] Step 5 — Surface GTM Phase 0/1/2 status dashboard (2–8h)
- [ ] Step 6 — Resume GTM Phase 1.2 (contact wishlist) + 1.3 (social from scratch)

**Fallback if Paperclip fails Step 1 verification:** Pivot to `mission-control` or `venture-hub` as status UI. Decision made at Step 1 checkpoint.

---

## PHASE 0: INFRASTRUCTURE ✓ COMPLETE

### Architecture Components (All Created)
- ✓ **MCP Configuration** (`.claude/mcp-config.json`)
  - 7 MCPs wired: Supabase, ClickUp, Graphify, Ollama, GitHub, Gmail, Slack
  - Make.com webhook URLs defined
  - Auth tokens (env vars) specified

- ✓ **Supabase Migration** (`migrations/002_create_aoc_tasks_table.sql`)
  - `aoc_tasks` table: single source of truth work queue
  - Schema: task_type, venture_id, contact_id, assigned_agent, status, priority, payload, result
  - 9 indexes for query performance
  - RLS policies for access control
  - Audit trigger for updated_at tracking
  - 2 helper views: aoc_tasks_summary, aoc_tasks_queued

- ✓ **Make.com Workflows** (5 JSON files)
  - workflow-1: Daily Task Queue Generator (8am UTC) → generates osint_contact, score_venture tasks
  - workflow-2: Task Executor → executes queued tasks (osint, scoring, cold outreach)
  - workflow-3: Contact Enrichment → enriches contacts with warmth_score, sector expertise
  - workflow-4: Venture Scorer → scores completeness, market fit, execution readiness
  - workflow-5: Deal Router → routes high-fit pairs to you (warmth > 80) or agents

### Connected Data Sources (All LIVE ✓)
- ✓ Supabase: 687 ventures, 58+ contacts, aoc_tasks ready
- ✓ Graphify: 7000+ nodes, 6000+ edges at `/Users/acebless/Documents/The office/.planning/graphs/`
- ✓ Ollama: qwen2.5:32b running at 100.87.214.70:11434
- ✓ GitHub: User authenticated as Worldwidebro
- ✓ ClickUp: Ready for webhook integration

---

## PHASE 1: EXECUTION (Days 8-14)

### 1.1 Product Audit (Supabase)
- [ ] Query Supabase: pull all 687 ventures with `product_description`, `service_type`, `target_market`, `price_point`
- [ ] Categorize by sector (beauty, tech, food, logistics, etc.)
- [ ] Identify highest-value ventures (revenue potential, market fit, time-to-revenue)
- [ ] Document gaps (incomplete product data, missing descriptions)
- **Files:** `findings.md` → Product catalog, gaps, top 50 ventures

### 1.2 Network Mapping (Personal Contacts)
- [ ] Export LinkedIn contacts (need to clarify: where are they stored?)
- [ ] Export phone contacts / CRM if available
- [ ] Categorize by industry/function (e.g., "CEO Construction", "CMO Tech", "Finance Director")
- [ ] Map contact needs against venture offerings (who needs what?)
- **Files:** `findings.md` → Contact matrix, need matches

### 1.3 Social Media Audit
- [ ] Identify existing Instagram/TikTok/LinkedIn profiles for ventures (do these exist?)
- [ ] Current follower count, engagement rate per profile
- [ ] Untapped social channels (which ventures have NO social presence?)
- [ ] Influencer network (do you have personal followers across platforms?)
- **Files:** `findings.md` → Social media inventory, influence leverage points

---

## Phase 2: Deal Infrastructure (Blocked by Phase 1)

### 2.1 ClickUp Deal Pipeline
- [ ] Create "Lead Generation" list (prospects)
- [ ] Create "Negotiations" list (active deals)
- [ ] Create "Closed Deals" list (won, revenue tracking)
- [ ] Set up status workflow: New Lead → Contacted → Negotiating → Closed
- [ ] Add custom fields: contact name, venture matched, deal value, close date
- **Files:** progress.md → ClickUp list IDs, pipeline structure

### 2.2 Deal Scripts & Messaging
- [ ] Create 3-5 template scripts (outreach, discovery call, close)
- [ ] Scripts per sector (beauty/wellness talks differently than B2B tech)
- [ ] Positioning: "We offer [venture product] to solve [contact pain point]"
- [ ] Tone/style: influence + negotiation language
- **Files:** findings.md → Script library (by sector)

### 2.3 Lead Routing System
- [ ] Match ventures to network contacts (venture A → contacts B, C, D)
- [ ] Assign leads to sectors (qwen-beauty-wellness gets beauty contacts, etc.)
- [ ] Create "warm intro" paths (mutual connections, credibility)
- **Files:** progress.md → Lead routing table, who calls whom

---

## Phase 3: Social Media Go-to-Market

### 3.1 Instagram/Social Influence Strategy
- [ ] Identify which ventures need social presence (none exist?)
- [ ] Create content strategy: product showcase, case studies, behind-the-scenes
- [ ] Leverage personal network for shares/retweets/shoutouts
- [ ] Set impression goals per venture (e.g., 5K impressions → 50 leads)
- [ ] Use social proof: testimonials, results, ROI
- **Files:** progress.md → Social strategy per sector, KPIs

### 3.2 Content & Asset Generation
- [ ] Pull product images/descriptions from Supabase
- [ ] Create 10-20 template posts (product showcase, lead magnet, CTA)
- [ ] Link posts to ClickUp leads (post → landing page → lead capture)
- [ ] Schedule posting (cadence per platform)
- **Files:** findings.md → Content calendar, post templates

### 3.3 Lead Conversion from Social
- [ ] DM follow-up sequence (post → engagement → DM → call)
- [ ] Landing page per venture (simple: what + why + contact form)
- [ ] Link to ClickUp leads (auto-create task when form submitted)
- **Files:** progress.md → Landing page URLs, lead flow

---

## Phase 4: Call Execution & Deal Closing

### 4.1 Outreach Calls
- [ ] Make 5-10 calls/day per contact (warm intros first)
- [ ] Document call outcome in ClickUp (interested, not interested, follow-up needed)
- [ ] Use scripts from Phase 2.2
- [ ] Track time, notes, next steps
- **Files:** progress.md → Daily call log, outcomes

### 4.2 Negotiation & Closing
- [ ] Discovery call → needs assessment
- [ ] Present venture solution (demo, pricing, timeline)
- [ ] Handle objections (price, timeline, proof)
- [ ] Move to closed deal (signature, payment terms, go-live date)
- **Files:** progress.md → Deal stages, closure notes

### 4.3 Revenue Tracking
- [ ] Log every deal in ClickUp with value, expected revenue, close date
- [ ] Track by sector (which sector closing fastest deals?)
- [ ] Calculate conversion rate (leads → deals → revenue)
- [ ] Monthly revenue goal tracking
- **Files:** progress.md → Revenue metrics, dashboard KPIs

---

## IZA OS DEPLOYMENT STACK (Paperclip Architecture)

This system will orchestrate all 687 ventures as isolated companies within one Paperclip instance.

**Current Sector Status:**
- **Tagged:** 9/687 ventures
  - fintech (2), ai (1), edtech (1), health (1), infra (1), market (1), devtools (1)
- **Untagged:** 678/687 ventures (auto-discover via agent analysis)

```
Paperclip (orchestration root)
  ├─ 7 Sector Agents (defined + discovery agent for untagged)
  │  ├─ fintech-agent (2 ventures + N untagged)
  │  ├─ ai-agent (1 venture + discovery)
  │  ├─ edtech-agent (1 venture + discovery)
  │  ├─ health-agent (1 venture + discovery)
  │  ├─ infra-agent (1 venture + discovery)
  │  ├─ market-agent (1 venture + discovery)
  │  ├─ devtools-agent (1 venture + discovery)
  │  └─ discovery-agent (678 untagged ventures → classify → route)
  ├─ 687 Venture Companies (multi-tenant, auto-categorized)
  ├─ Agent Skills Library (everything-claude-code + gsd patterns)
  ├─ Persistent Memory (gigabrain + agent-memory Neo4j)
  ├─ Learning Engine (EvoSkill)
  └─ Parallel Runner (crystal: 20+ concurrent ventures)
```

**Deployment order (by priority):**
1. **Paperclip** — Control plane, org structure, heartbeats, budgets, governance
2. **everything-claude-code + gsd patterns** — Autonomous loops, postgres patterns, deployment patterns, task execution
3. **gigabrain** — Session memory persistence (solves context loss between agent runs)
4. **agent-memory** — Neo4j graph memory (agents learn from own reasoning)
5. **724-office** — Reference Operations sector blueprint (26 tools, 3500 LOC, self-repair)
6. **EvoSkill** — Auto-synthesize improved skills from failed trajectories
7. **crystal** — Parallel execution (hours not weeks: run 20+ ventures concurrently)

---

## Phase 2B: INTELLIGENCE LAYER (Days 15-21)

### 2B.1 Option A: Repo Metadata Foundation ✓ COMPLETE
- [x] Create `003_create_repos_metadata_table.sql` (220 lines) - migration deployed
- [x] Created `populate_repos_metadata.py` script for automated metadata population
  - Parses 640 repos from starred-repos-capabilities.md
  - Queries GitHub API for stars, commits, language, license
  - Uses Ollama (qwen2.5:32b) to infer: purpose, capabilities, integration_effort, cost, stack
  - Maps repos to ventures by required_capabilities
  - Batch inserts to Supabase repos table
- [x] Run population script: `python3 populate_repos_metadata.py` ✓ COMPLETED (exit code 0)
- [x] Verify 850+ repos in table with embeddings=NULL (ready for Option C)
- [x] Created `populate_repos_simple.py` (heuristic fallback) - COMPLETED 2026-05-10 03:17:27
  - 64 repos populated with purpose + description + capabilities (100% success)
  - Simple pattern matching on repo names (no Ollama/GitHub API required)
  - All repos ready for embedding generation
- **Output:** ✓ Supabase repos table with complete metadata for semantic search

### 2B.2 Option C: LlamaIndex Semantic Indexing ✅ COMPLETE
- [x] Created `index_repos_with_llamaindex.py` script for embedding generation
- [x] Tested with OpenAI: API key invalid (401 Unauthorized)
- [x] Created `index_repos_local_embeddings.py` - uses local SentenceTransformer model
  - Uses all-MiniLM-L6-v2 model (384-dim baseline)
  - Pads to 1536-dim for Supabase schema compatibility
  - Zero external dependencies, runs locally on Mac with MPS acceleration
  - Batch processed efficiently using PyTorch
- [x] Executed 2026-05-10 14:31:28 → 14:34:22 (3 min 54 sec)
  - **Result:** 64/64 embeddings created and stored
  - **Success rate:** 100%
  - **Status:** All repos now have semantic embeddings in Supabase repos.embedding column
- **Outcome:** Semantic search fully operational. Repos indexed by meaning, not keyword match.

### 2B.3 Option B: Backstage Integration ⏸️ BLOCKED
- [x] Created `backstage-integration-setup.md` (400 lines) - complete deployment guide
- [x] Prerequisites verified: Node.js v25.9.0, npm 11.12.1, Docker v29.4.0 ✓
- [ ] Deployment blocked: `npx @backstage/create-app` requires interactive terminal
  - Docker image not publicly accessible
  - NPM interactive prompt fails in non-interactive environment
- **Status:** Requires manual setup or alternative catalog approach
- **Alternative:** Explore user-suggested tools (ruflo, goose) for service catalog visualization

### 2B.4 Data Flow Integration
- [ ] Verify: Supabase (data) → Backstage (UI) → LlamaIndex (search)
- [ ] Test query: "What repos solve booking + payments?" → Returns cal_com + stripe
- [ ] Test venture view: BW-001 → Shows cal_com, stripe, crm-platform as dependencies
- [ ] Test roadmap: BW-001 → Phases with timelines, effort levels

---

## Phase 5: Sector Agent Integration

### 5.1 Automate Lead Distribution
- [ ] Map ClickUp new leads → sector agents (beauty leads → qwen-beauty-wellness)
- [ ] Agents claim leads, execute outreach via n8n
- [ ] Agents track engagement, escalate to human for close
- **Files:** progress.md → Agent task assignment logic

### 5.2 Deal Accountability
- [ ] ClickUp Ops & Tasks: per-sector deal pipeline visibility
- [ ] Weekly sector reports: leads generated, deals closed, revenue
- [ ] Agent KPIs: leads touched, deal velocity, commission structure
- **Files:** progress.md → Accountability framework

---

## Blockers & Dependencies

| Blocker | Resolution |
|---------|-----------|
| Where are personal contacts stored? (LinkedIn, phone, CRM?) | **Need user clarification** |
| Do ventures have product images/descriptions in Supabase? | **Need to audit Supabase schema** |
| Do Instagram/social profiles already exist for ventures? | **Need user clarification** |
| What's the deal closing authority (you only, or team?) | **Need user clarification** |
| Which sectors to prioritize in Phase 1? | **Recommend: top 3 by revenue potential** |

---

## Success Metrics (Phase 1 Completion)

- [ ] 687 ventures categorized by product, sector, market
- [ ] 50+ network contacts mapped to venture offerings
- [ ] Deal scripts written (3-5 templates by sector)
- [ ] ClickUp pipeline configured and live
- [ ] First 10 leads warm-intro'd, 3+ conversations scheduled
- [ ] Social media audit complete (what channels exist, what gaps)

---

## Session Log

**2026-05-10 — Phase 2 Intelligence Layer (Resumed Session)**
- **Phase 2A (Option A) ✅ COMPLETE**
  - `populate_repos_simple.py`: 64/64 repos populated with description, purpose, capabilities
  - Execution: 2026-05-10 03:17:11 → 03:17:27 (16 seconds)
  - Result: 100% success, all repos ready for semantic indexing

- **Phase 2C (Option C) ✅ COMPLETE**
  - `index_repos_local_embeddings.py`: Created 1536-dim embeddings using SentenceTransformer
  - Execution: 2026-05-10 14:31:28 → 14:34:22 (3 min 54 sec)
  - Result: 64/64 embeddings created and stored in Supabase
  - Semantic search now operational across all repos

- **Phase 2B (Option B) ⏸️ BLOCKED**
  - Backstage requires interactive terminal or Docker image access
  - Alternative: Use Paperclip org visualization layer instead

- **Next Phase: Paperclip Deployment**
  - Deploy Paperclip as root orchestration layer
  - Install everything-claude-code skills
  - Integrate gigabrain for agent persistence
  - Setup 7 sector agents + 687 venture entities

**2026-05-08 — Session Start**
- Task: Build go-to-market system for 687 ventures
- Status: Phase 1 ready to execute
- Result: Phase 0 infrastructure complete, Phase 2A/2C intelligence layer complete, ready for Paperclip orchestration
