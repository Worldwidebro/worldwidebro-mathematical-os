# AGENT-MCP-BINDINGS.md
## Which MCPs Each Agent Uses

**Purpose:** Map 8 agents to their MCP dependencies.

---

## AGENT-MCP MATRIX

| Agent | Critical MCPs | Secondary MCPs | Update Frequency |
|-------|---|---|---|
| **Portfolio Manager** | Portfolio, KPI | HubSpot, Slack | Hourly |
| **Deal Scout** | Deal-Flow, Tavily | Crunchbase, HubSpot, Slack | Continuous |
| **Content Amplifier** | Media, Buffer, Beehiiv | Twitter, Postiz, GitHub | Daily |
| **Research** | Qdrant, Tavily | GitHub, Crunchbase, Obsidian, Notion | On-demand |
| **Community Manager** | HubSpot, Slack | Notion, Obsidian, KPI | Real-time |
| **Operator Coordinator** | SOP, HubSpot | Deal-Flow, KPI, Slack | On-demand |
| **Financial Controller** | Stripe, KPI | Google Sheets, Portfolio, Slack | Real-time |
| **Board Secretary** | KPI, Google Sheets | Portfolio, Notion, HubSpot, Slack | Weekly |

---

## AGENT 1: Portfolio Manager Agent

**Purpose:** Monitor 30-50 companies, trigger alerts, optimize health

**MCPs Required:**
- Portfolio MCP (query all companies) - hourly
- KPI MCP (health score calculations) - daily 6 AM
- HubSpot MCP (company contacts, funding status) - on-demand
- Slack MCP (alert CEO) - triggered

**Workflow:**
```
1 hour: Portfolio MCP query → health scores calculated
6 AM: KPI MCP aggregates metrics
If health < 6 months runway → Slack alert
CEO reads alert → decides action
Agent implements (if automated)
```

**Criticality:** ✅ System cannot run without this

---

## AGENT 2: Deal Scout Agent

**Purpose:** Find, score, qualify, match deals to operators

**MCPs Required:**
- Deal-Flow MCP (score & pipeline) - per deal
- Tavily MCP (web search) - continuous
- Crunchbase MCP (company research) - per deal
- HubSpot MCP (operator matching) - per qualified deal
- Slack MCP (notify operator) - when deal ≥ $50K

**Workflow:**
```
Tavily search: "AI agencies in Southeast US"
Crunchbase: Get funding data
Deal-Flow score: 82/100 → qualified
HubSpot match: Best operator = "Alice"
Slack: Notify Alice
Deal pipeline: moves to "proposed"
```

**Criticality:** ✅ System cannot run without this

---

## AGENT 3: Content Amplifier Agent

**Purpose:** Create, process, distribute content

**MCPs Required:**
- Media MCP (transcribe, clip, dub, subtitle)
- Buffer MCP (social scheduling)
- Beehiiv MCP (newsletter)
- Postiz MCP (multi-platform)
- Twitter MCP (post + metrics)

**Workflow:**
```
Raw video → Media MCP
├─ Transcribe
├─ Extract 5 clips
├─ Dub Spanish/Mandarin
└─ Auto-subtitle
Buffer/Beehiiv/Postiz: Schedule across platforms
Twitter: Direct posts
Result: 1 video → 20 pieces across platforms
```

**Criticality:** ⚠️ System degrades without (manual posting)

---

## AGENT 4: Research Agent

**Purpose:** Market research, competitive intelligence

**MCPs Required:**
- Qdrant MCP (semantic search internal knowledge)
- Tavily MCP (web search)
- GitHub MCP (code/trend search)
- Crunchbase MCP (company data)

**Workflow:**
```
Query: "Find automation trends in e-commerce"
Qdrant: Search internal frameworks
Tavily: Web search findings
GitHub: Popular repos + stars
Crunchbase: Market size data
Output: Intelligence report
```

**Criticality:** ⚠️ Optional (can skip for MVP)

---

## AGENT 5: Community Manager Agent

**Purpose:** Engage members, distribute resources, track satisfaction

**MCPs Required:**
- HubSpot MCP (member profiles, interactions)
- Slack MCP (notifications)
- Notion MCP (resource library queries)
- Obsidian MCP (playbook sharing)

**Workflow:**
```
HubSpot: New member joined
Slack: Welcome message
Notion: Share getting-started guide
Track: Engagement metrics
Weekly: Report on engagement
```

**Criticality:** ⚠️ Optional (manual management possible)

---

## AGENT 6: Operator Coordinator Agent

**Purpose:** Assign SOPs, track execution, manage workflows

**MCPs Required:**
- SOP MCP (execute workflows)
- HubSpot MCP (operator details)
- Slack MCP (task assignments)
- Deal-Flow MCP (provide context)

**Workflow:**
```
Deal qualified → Operator assigned
SOP MCP: Execute "Client Onboarding" workflow
HubSpot: Get operator contact info
Slack: Notify operator + provide context
SOP tracking: Monitor step completion
```

**Criticality:** ✅ System cannot run without this

---

## AGENT 7: Financial Controller Agent

**Purpose:** Track revenue, expenses, alerts, forecasting

**MCPs Required:**
- Stripe MCP (real-time payments)
- KPI MCP (MRR calculations)
- Google Sheets MCP (budget tracking)
- Portfolio MCP (company profitability)
- Slack MCP (alerts)

**Workflow:**
```
Real-time: Stripe payment → recorded
Daily 6 AM: KPI MCP calculates MRR
Weekly: Google Sheets budget review
Alert: If revenue down >5% → Slack CEO
Forecast: 6-month cash runway
```

**Criticality:** ✅ System cannot run without this

---

## AGENT 8: Board Secretary Agent

**Purpose:** Prepare governance materials, track decisions

**MCPs Required:**
- KPI MCP (latest metrics)
- Google Sheets MCP (scorecard)
- Portfolio MCP (company summaries)
- Notion MCP (decision tracking)
- HubSpot MCP (investor updates)

**Workflow:**
```
5 days before board: KPI MCP pulls metrics
Portfolio MCP generates summaries
Google Sheets: Create board scorecard
Notion: Record board decisions
HubSpot: Update investor contacts
```

**Criticality:** ⚠️ Optional (manual process possible)

---

## MCP CRITICALITY RANKING

**System cannot run without (5 MCPs):**
1. ✅ Portfolio MCP
2. ✅ KPI MCP
3. ✅ Deal-Flow MCP
4. ✅ HubSpot MCP
5. ✅ Stripe MCP

**System significantly degraded without (4 MCPs):**
6. ⚠️ Slack MCP (notifications fail)
7. ⚠️ SOP MCP (manual task management)
8. ⚠️ Media MCP (manual content processing)
9. ⚠️ Buffer/Beehiiv (manual posting)

**System fully functional without (13 MCPs):**
10. Tavily, Crunchbase, Qdrant, GitHub, Obsidian, Notion, Google Sheets, Postiz, WordPress

---

## STARTUP SEQUENCE

**Order MCPs come online:**
1. Supabase (underlying infrastructure)
2. Portfolio MCP + KPI MCP (metrics engine)
3. Deal-Flow MCP (deal pipeline)
4. HubSpot MCP (relationships)
5. Stripe MCP (revenue)
6. Slack MCP (notifications)
7. All 8 agents online

**Health check (every 30 min):** Each agent tests MCP connectivity

---

## RESULT

**When all 8 agents + 22 MCPs are wired:**

✅ Autonomous system running 24/7  
✅ Decisions made by agents, not humans  
✅ Revenue tracked automatically  
✅ Deals sourced automatically  
✅ Content distributed automatically  
✅ Metrics calculated automatically  
✅ Alerts triggered automatically  
✅ Workflows executed automatically  

---

**System autonomy: 70%+**

