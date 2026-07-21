# Phase 1B: Integrated Execution Blueprint
**Goal:** $1-3K/week revenue from OPS-001 (one venture)  
**Timeline:** 4 days (Tue-Fri)  
**Integration:** n8n → Supabase → Neo4j → Finance Agent → Revenue

---

## ONE Decision Loop (Everything Wired)

```
OPS-001 sends decision
    ↓ [POST to n8n webhook]
n8n Decision-Routing Workflow
    ├→ Log to Supabase (decisions table)
    ├→ Query Neo4j (find department director)
    ├→ Route to Finance Agent (if $<5K, auto-approve)
    └→ Execute: Generate invoice
        ├→ Log to Supabase (invoices table)
        ├→ Update decision status (executed)
        └→ Notify Slack
```

**All pieces exist. Wire them in order.**

---

## 4-Day Execution Plan

### Day 1: Deploy n8n + Load Graph
- **Deploy workflow:** Export `/04-OPERATIONS/IZA-OS/workflows/DECISION-ROUTING-FLOW.json` to n8n (import UI)
  - Use skill: `czlonkowski/n8n-skills@n8n-workflow-patterns`
  - Verify: Mock decision → logged to Supabase ✅
  
- **Load org.yaml to Neo4j:** `python3 neo4j_graph_loader.py organization.yaml`
  - Verify: `MATCH (h:Hermes) RETURN h;` returns node ✅

### Day 2: Build Finance Agent
- **File:** `/05-AGENTS/departments/finance.py`
- **Task:** Read decision from Supabase → generate invoice → log outcome
- **Use skill:** `davila7/claude-code-templates@supabase-postgres-best-practices`
- **Integration:** n8n calls HTTP endpoint `/api/agent/finance/invoice`

### Day 3: Wire Integration Points
- **Venture → n8n webhook:** Add POST to `vex-hero-site/src/api/capability-request.ts`
- **n8n → Finance agent:** Add HTTP call node (already in workflow spec)
- **Test full loop:** Send decision, trace through Supabase logs ✅

### Day 4: Revenue
- **Execute 2-3 real placements** from OPS-001 (74 prospects waiting)
- **Verify:** Supabase shows decisions + invoices (proof of execution)
- **Income:** $300-1,500

---

## Files to Create/Wire

| File | Action | Status |
|------|--------|--------|
| `/05-AGENTS/departments/finance.py` | **CREATE** (invoicing agent) | ❌ |
| `vex-hero-site/src/api/capability-request.ts` | **WIRE** (POST to n8n) | ❌ |
| `n8n/workflows/deployed/decision-routing.json` | **DEPLOY** (from spec) | ❌ |
| `/05-AGENTS/neo4j_graph_loader.py` | **RUN** (load graph) | ✅ Ready |

**Already done:**
- `/04-OPERATIONS/IZA-OS/DECISION-ROUTING-FLOW.json` ✅
- `/04-OPERATIONS/IZA-OS/organization.yaml` ✅
- `/operating_system_schema.sql` ✅

---

## Skills to Use

```bash
npx skills add czlonkowski/n8n-skills@n8n-workflow-patterns
npx skills add davila7/claude-code-templates@supabase-postgres-best-practices
```

---

## Success: Full Loop End-to-End

```json
POST http://n8n-webhook/decision-request

{
  "venture_id": "OPS-001",
  "amount": 500,
  "decision_type": "placement_approval",
  "context": "Candidate matched to shift"
}

↓ [Routed]

Supabase (decisions table):
{
  "decision_id": "dec_2026-07-20_001",
  "venture_id": "OPS-001",
  "status": "executed",
  "authority_routed_to": "auto_approve",
  "created_at": "2026-07-20T15:30:00Z"
}

Supabase (invoices table):
{
  "invoice_id": "inv_2026-07-20_001",
  "venture_id": "OPS-001",
  "amount": 500,
  "line_item": "Staffing placement OPS-001",
  "status": "generated",
  "created_at": "2026-07-20T15:30:30Z"
}

Slack notification: ✅ Decision Executed | OPS-001 | $500 | Invoice generated
```

---

## No Custom Hermes Agent Needed Yet

n8n workflow already routes: `if amount < 5000 then auto_approve else escalate`  
**Only build Hermes later if:**
- Logic becomes complex (ML-based routing, multi-factor decisions)
- Need reasoning over multiple decisions

---

This is the **integration map**. Execute in order.
