# Intelligence Layers × Tools × MCPs × Skills Map

**Purpose:** Map existing open-source + MCPs + skills to 10-layer pipeline. Compose, don't build custom.

**Generated:** 2026-06-05

---

## LAYER 0: REALITY (Market Intelligence)

**Open Source:** OpenBB, DuckDB, Metabase

**MCPs:**
- ✅ postman:search (find APIs)
- ✅ mcp__browseros (scrape data)
- ✅ mcp__supabase (store)

**Skills:**
- ✅ postman:run-collection (pull data)

**How:** API → Supabase reality_signals → DuckDB aggregation

**Gap:** ❌ Scheduler (need cron or Temporal)

---

## LAYER 1: SENSING (Data Collection)

**Open Source:** Metabase, Kafka, n8n

**MCPs:**
- ✅ mcp__clickup (tasks)
- ✅ mcp__supabase (customer data)
- ✅ mcp__github (repo signals)
- ✅ mcp__browseros (web signals)

**Skills:**
- ✅ socraticode:codebase-exploration
- ✅ everything-claude-code:github

**How:** GitHub MCP → Socraticode analysis → ClickUp data → Supabase sensed_data

**Gap:** ❌ Scheduler

---

## LAYER 2: INTERPRETATION (Meaning)

**Open Source:** LlamaIndex, LightRAG, Weaviate

**MCPs:**
- ✅ iza-os-rag (semantic search)
- ✅ socraticode (code search)
- ✅ mcp__supabase

**Skills:**
- ✅ iza-os-rag (query index)
- ✅ socraticode:codebase-exploration

**How:** sensed_data → iza-os-rag → Claude analysis → interpretations table

**Gap:** ⚠️ Auto-insight extraction (custom prompt)

---

## LAYER 3: MODELING (System Structure)

**Open Source:** Neo4j, ArangoDB

**MCPs:**
- ✅ socraticode:codebase_graph
- ✅ mcp__github (dependencies)
- ✅ mcp__supabase

**Skills:**
- ✅ socraticode:codebase-exploration

**How:** interpretations → Socraticode graph → models table (JSON)

**Gap:** ⚠️ Neo4j MCP integration

---

## LAYER 4: DESIGN (Solution Architecture)

**Open Source:** Retool, Directus, Figma API

**MCPs:**
- ✅ mcp__vercel (UI)
- ✅ mcp__make (workflows)

**Skills:**
- ✅ frontend-design:frontend-design
- ✅ everything-claude-code:feature-dev

**How:** models → frontend-design → designs table

**Gap:** ⚠️ Figma API MCP

---

## LAYER 5: STRUCTURING (Execution Design)

**Open Source:** n8n, Temporal, Airflow

**MCPs:**
- ✅ mcp__make (workflows)
- ✅ mcp__github (create files)

**Skills:**
- ✅ backend-patterns

**How:** designs → Make scenarios → structures table

**Gap:** ✅ None

---

## LAYER 6: EXECUTION (Action)

**Open Source:** n8n, Temporal, LangChain

**MCPs:**
- ✅ mcp__clickup (create tasks)
- ✅ mcp__make (run workflows)
- ✅ mcp__github (execute code)

**Skills:**
- ✅ everything-claude-code (execute)
- ✅ superpowers:executing-plans

**How:** structures → Make execute → ClickUp track → executions table

**Gap:** ✅ None

---

## LAYER 7: DISTRIBUTION (Reach)

**Open Source:** Matomo, GrowthBook, PostHog

**MCPs:**
- ✅ mcp__slack (announce)
- ✅ mcp__gmail (email)
- ✅ mcp__make (automate)
- ✅ mcp__browseros (track reach)

**Skills:**
- ✅ postman:send-request

**How:** executions → Slack/Gmail announce → Make campaign → distributions table

**Gap:** ⚠️ Analytics API integration

---

## LAYER 8: MONETIZATION (Revenue)

**Open Source:** Stripe, Metabase, Superset

**MCPs:**
- ✅ mcp__stripe (payments)
- ✅ mcp__supabase (store)
- ✅ mcp__make (track)

**Skills:**
- ✅ postman:send-request

**How:** Stripe → DuckDB CAC/LTV → monetizations table

**Gap:** ✅ None

---

## LAYER 9: MEASUREMENT (Performance)

**Open Source:** Metabase, Superset, Grafana

**MCPs:**
- ✅ mcp__supabase (query)
- ✅ mcp__make (schedule)

**Skills:**
- ✅ everything-claude-code:benchmark

**How:** monetizations → DuckDB → Grafana → measurements table

**Gap:** ✅ None

---

## LAYER 10: LEARNING (Improvement)

**Open Source:** LlamaIndex, W&B

**MCPs:**
- ✅ iza-os-rag (search patterns)
- ✅ mcp__supabase (store learnings)
- ✅ mcp__make (automate loop)

**Skills:**
- ✅ superpowers:systematic-debugging

**How:** measurements → iza-os-rag → Claude insight → learnings table

**Gap:** ✅ None

---

## FEEDBACK LOOP (Close the Circle)

**MCPs:**
- ✅ mcp__make (orchestrate)
- ✅ mcp__supabase (update reality)
- ✅ mcp__clickup (update tasks)

**How:** learnings → new reality_signals → start next cycle

---

## Coverage Summary

| Layer | Tools | MCPs | Skills | Complete? |
|-------|-------|------|--------|-----------|
| 0: Reality | ✅ | ✅ | ✅ | ⚠️ Scheduler |
| 1: Sensing | ✅ | ✅ | ✅ | ⚠️ Scheduler |
| 2: Interpretation | ✅ | ✅ | ✅ | ⚠️ Auto-insight |
| 3: Modeling | ✅ | ⚠️ | ✅ | ⚠️ Neo4j |
| 4: Design | ✅ | ✅ | ✅ | ⚠️ Figma |
| 5: Structuring | ✅ | ✅ | ✅ | ✅ |
| 6: Execution | ✅ | ✅ | ✅ | ✅ |
| 7: Distribution | ✅ | ✅ | ✅ | ⚠️ Analytics |
| 8: Monetization | ✅ | ✅ | ✅ | ✅ |
| 9: Measurement | ✅ | ✅ | ✅ | ✅ |
| 10: Learning | ✅ | ✅ | ✅ | ✅ |

---

## What to Build (5 Things)

```
1. Scheduler system
   → Cron or Temporal to run MCPs on schedule
   → Wrap MCPs in Python scripts with schedule decorators

2. Feedback loop automation
   → Make scenario: learnings → new reality_signals
   → Update Supabase automatically

3. Auto-insight extractor
   → Claude prompt: measurements → insights
   → Feed into learnings table

4. Layer-to-layer connectors
   → Temporal workflows connecting layer outputs
   → Simple data transformations

5. Dashboard unification
   → Grafana showing all 10 layers
   → Real-time health metrics
```

---

## What to Use (Everything Else)

✅ All tools listed above  
✅ All MCPs listed above  
✅ All skills listed above  

---

## Implementation (7 Tasks, Not 20)

1. Map MCPs to Supabase tables
2. Create scheduler (Python + cron)
3. Build Make scenarios (layers 5-7)
4. Create Temporal workflows (layer connectors)
5. Build feedback automation (learnings loop)
6. Create Grafana dashboard
7. Test 1 venture end-to-end

**Time: 1-2 weeks (not 6 weeks)**

---

## Key Insight

Don't build custom scripts for each layer.  
Use existing MCPs as "API connectors."  
Build only the 5 connective pieces.  
Everything else already exists.
