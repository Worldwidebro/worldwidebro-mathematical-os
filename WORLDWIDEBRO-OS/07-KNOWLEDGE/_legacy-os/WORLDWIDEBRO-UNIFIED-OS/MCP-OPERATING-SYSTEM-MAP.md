# MCP Operating System Map — WORLDWIDEBRO Holdings

**Purpose:** Blueprint for 30 MCPs wired into a unified operating system.

---

## **LAYER 1: Discovery Layer**
*Find and understand available tools*

| MCP | Purpose | Status |
|-----|---------|--------|
| Awesome MCP Servers (GitHub) | Registry of all MCPs | ✅ Reference |
| Glama MCP Directory | Directory search | ✅ Reference |

**Output:** Inventory of capabilities

---

## **LAYER 2: Claude Skill Layer**
*Commands, agents, skills, hooks*

| Asset | Purpose | Status |
|-------|---------|--------|
| Awesome Claude Code | Skill library | ✅ Reference |
| Awesome Claude Code Agents | Agent patterns | ✅ Reference |

**Output:** Executable workflows

---

## **LAYER 3: IDE Layer**
*Human + AI Interface*

| Tool | Purpose | Status |
|------|---------|--------|
| Cursor | Primary IDE | ✅ In use |
| Cline | VS Code extension | ✅ Available |
| Claude Code | Web interface | ✅ Available |

**Output:** Development workspace

---

## **LAYER 4: Multi-Agent Layer**
*Agent coordination & specialization*

| System | Purpose | Status |
|--------|---------|--------|
| Claude Flow | Sequential workflows | ⏸ Available |
| Claude Squad | Team coordination | ⏸ Available |
| Swarm SDK | Agent teams | ⏸ Available |

**Agents in use:**
- Portfolio Manager Agent (reads Portfolio MCP)
- Deal Scout Agent (reads Deal-Flow MCP)
- Content Amplifier Agent (reads Media MCP)
- Research Agent (reads Tavily, arXiv, Crunchbase)
- Community Manager Agent (reads ClickUp, Slack)
- Operator Coordinator Agent (reads HubSpot, ClickUp)
- Financial Controller Agent (reads Stripe, Supabase)
- Board Secretary Agent (reads Supabase, Gmail)

**Output:** Coordinated execution

---

## **LAYER 5: Core MCP Layer**
*Foundational execution infrastructure*

| MCP | Purpose | Status | Wired To |
|-----|---------|--------|----------|
| GitHub | Code repositories | ✅ Connected | Skill Registry, Deal-Flow |
| PostgreSQL (Supabase) | Database queries | ✅ Connected | All agents |
| Filesystem | File operations | ✅ Available | SOP MCP, Media MCP |
| SQLite | Local analytics | ✅ Available | KPI MCP |
| Git | Version control | ✅ Connected | GitHub MCP |

**Data Flow:**
```
Code Changes → GitHub → Portfolio MCP → Agents
Data Queries → PostgreSQL → KPI MCP → Dashboard
```

**Output:** Execution foundation

---

## **LAYER 6: Business MCP Layer**
*Sales, Marketing, Finance, Operations*

| MCP | Purpose | Status | Input | Output |
|-----|---------|--------|-------|--------|
| **Stripe** | Revenue tracking | ✅ Connected | Payment events | spending_transaction |
| **HubSpot** | CRM + deals | ⏸ Approval pending | Contact/deal data | hubspot_contacts, hubspot_deals |
| **Slack** | Notifications | ✅ Connected | Alerts | Team notifications |
| **Buffer** | Social scheduling | ⏸ Approval pending | Content queue | Posted to Twitter, LinkedIn, Instagram |
| **Beehiiv** | Newsletter | ⏸ Approval pending | Email list | Newsletter sends |
| **Gmail** | Email | ✅ Connected | Inbox | Draft creation |
| **Google Calendar** | Scheduling | ✅ Connected | Calendar | Event creation |

**Data Flow:**
```
Stripe (Revenue) → Supabase → KPI MCP → Dashboard
HubSpot (Deals) → Supabase → Deal-Flow MCP → Scoring → Agents
Slack (Notifications) ← All agents → Team awareness
Buffer/Beehiiv (Content) ← Media MCP ← Content creation
```

**Output:** Business operations network

---

## **LAYER 7: Research Layer**
*Market, competitor, technical research*

| MCP | Purpose | Status | Output |
|-----|---------|--------|--------|
| **Tavily** | Web search | ✅ Connected | Market intel |
| **Crunchbase** | Company research | ⏸ Approval pending | Funding data, competitors |
| **arXiv** | Academic papers | ⏸ Approval pending | Tech trends |
| **Brave Search** | ⏸ Configured | ⏸ Approval pending | General search |

**Data Flow:**
```
Research Query → Tavily → Market insights
                → Crunchbase → Deal scoring
                → arXiv → Tech insights
Research Results → Supabase → Deal-Flow scoring logic
```

**Output:** Research engine

---

## **LAYER 8: Browser Layer**
*Web automation, scraping, testing*

| MCP | Purpose | Status |
|-----|---------|--------|
| Puppeteer | Web automation | ✅ Available |
| Browserbase | Scraping | ✅ Available |

**Purpose:** Automate web interactions for data collection

**Output:** Web worker

---

## **LAYER 9: Memory Layer**
*Persistent knowledge, retrieval, context* ⭐ **CRITICAL GAP**

| Component | Purpose | Status |
|-----------|---------|--------|
| Memory MCP | Persistent memory | ❌ Not configured |
| Qdrant | Vector embeddings | ⏸ Configured, not wired |
| PostgreSQL | Structured knowledge | ✅ Connected |
| GraphRAG | Knowledge graphs | ❌ Not configured |

**Status:** MISSING — Blocking semantic search, context retrieval, institutional memory.

**Output:** Institutional memory (MISSING)

---

## **LAYER 10: Monitoring Layer**
*Cost, token, performance tracking*

| Tool | Purpose | Status |
|------|---------|--------|
| Claude Code Usage | Token tracking | ✅ Available |
| CCFlare | Cost tracking | ✅ Available |
| Custom dashboard | Observability | ⏸ Configured, not built |

**Output:** Observability

---

## **LAYER 11: Commerce Layer**
*Ecommerce, ads, customer acquisition*

| MCP | Purpose | Status |
|-----|---------|--------|
| Shopify | Ecommerce | ❌ Not configured |
| Meta (Ads) | Ad campaigns | ❌ Not configured |
| Klaviyo | Email automation | ❌ Not configured |
| Google Ads | Search ads | ❌ Not configured |
| Indeed | Job board | ✅ Connected |

**Output:** Revenue engine (INCOMPLETE)

---

## **LAYER 12: Proprietary Moat Layer**
*Organizational intelligence & differentiation*

| MCP | Purpose | Status | Reads | Writes |
|-----|---------|--------|-------|--------|
| **Portfolio MCP** | Company health | 🏗️ Ready to build | Stripe, HubSpot, Supabase | portfolio_health |
| **KPI MCP** | Metrics engine | 🏗️ Ready to build | Stripe, HubSpot, Portfolio | metrics_weekly |
| **Deal-Flow MCP** | Pipeline scoring | 🏗️ Ready to build | HubSpot, Tavily, Crunchbase, Qdrant | scored_deals |
| **Media MCP** | Content distribution | 🏗️ Ready to build | Video input | Buffer, Beehiiv, Twitter |
| **SOP MCP** | Process execution | 🏗️ Ready to build | Playbooks | ClickUp tasks |
| **Skills Registry MCP** | Workforce | 🏗️ Ready to build | Agent capabilities | skill_assignments |
| **Research MCP** | Intelligence synthesis | 🏗️ Ready to build | Tavily, Crunchbase, arXiv | research_reports |

**Status:** MISSING 70% OF COMPETITIVE MOAT

**Output:** Business operating system (INCOMPLETE)

---

## **EXECUTION READINESS**

### Day 1 Can Start NOW With (14 connected MCPs):
- Stripe (product creation)
- Twitter (announcements)
- HubSpot (contacts)
- Buffer/Beehiiv (content)
- Slack (notifications)
- ClickUp (task tracking)

### Days 2-14 Need (To avoid manual work):
- Portfolio MCP (track revenue health)
- KPI MCP (daily metrics)
- Deal-Flow MCP (score opportunities)

### Full Autonomy Needs:
- Memory MCP (agent context)
- Skills Registry MCP (workforce optimization)
- SOP MCP (playbook automation)
- Media MCP (multi-channel posting)

---

## **NEXT STEPS**

**Option A: Execute Task #26 Day 1 NOW**
- Takes 30 minutes
- Uses 14 connected MCPs
- Manual metrics tracking (Days 2-14)

**Option B: Build P0 MCPs first, then execute**
- Takes 6-8 hours (Portfolio + KPI + Deal-Flow MCPs)
- Then execute Task #26 with full automation
- Days 2-14 run autonomously

**Recommendation:** Option A (execute now) + build P0 MCPs in parallel (Days 2-7)

---

**Map Version:** 1.0
**Created:** 2026-06-09
**Status:** Ready for execution
