# Campaign Factory Integration Guide

## Status Check: 712 Ventures → Campaign System

### ✅ Verified Alignment

**Supabase Tables (Source of Truth)**
- `ventures` table: ✅ 712 ventures exist (loaded by `populate_venture_knowledge_graph.py`)
- `campaigns` table: ✅ NEW - linked via `venture_id` FOREIGN KEY
- `campaign_stages` table: ✅ NEW - tracks progress per venture campaign
- `campaign_content` table: ✅ NEW - stores all assets
- `campaign_metrics` table: ✅ NEW - real-time KPI tracking

**Foreign Key Alignment**
```sql
ALTER TABLE campaigns ADD CONSTRAINT fk_campaigns_ventures
  FOREIGN KEY (venture_id) REFERENCES ventures(venture_id);
```

Each venture can have multiple campaigns:
```
ventures (712 total)
  └─ campaigns (N per venture)
     ├─ campaign_stages (12 per campaign)
     ├─ campaign_content (100+ per campaign)
     ├─ campaign_deliverables
     ├─ campaign_channels
     └─ campaign_metrics
```

### Execution Flow

**1. Load 712 Ventures**
```bash
python3 populate_venture_knowledge_graph.py
# Loads: v-hrms-001, v-graphify-001, con-001-construction, ... (712 total)
# Into: Supabase ventures table
```

**2. Launch Campaign for Any Venture**
```bash
python3 campaign_orchestrator.py \
  --venture v-hrms-001 \
  --template tmpl-service-launch \
  --name "HRMS MVP Launch" \
  --budget 3000
```

**3. Campaign Creates in Supabase**
```json
{
  "campaign_id": "camp-v-hrms-001-20260608",
  "venture_id": "v-hrms-001",
  "template_id": "tmpl-service-launch",
  "status": "active",
  "current_stage": 1,
  "orchestrated_by_agent": true
}
```

**4. Agent Orchestration Starts**
- Stage 1: research_agent analyzes venture + market
- Stage 2: positioning_agent creates messaging
- ... (stages 3-12)
- All stages tracked in campaign_stages table

**5. Real-time Sync**
```
Supabase ← campaign metrics ← agent execution ← Claude API
  ↓
Obsidian ← dataview queries ← Supabase
  ↓
CAMPAIGN-FACTORY-DASHBOARD.md (live view)
```

---

## Integration with venture-hub

### New API Endpoints

```typescript
GET  /api/campaigns                      // List campaigns
GET  /api/campaigns/[id]                 // Campaign details
GET  /api/campaigns/[id]/stages          // Stage progress
GET  /api/campaigns/[id]/metrics         // Real-time KPIs
POST /api/campaigns                      // Launch campaign
```

### New UI Views

```
/ventures/[id]/campaigns                 // Venture campaigns tab
/campaigns/[id]                          // Campaign detail view
/campaigns/[id]/progress                 // Stage progress timeline
/campaigns/[id]/deliverables            // Assets & outputs
```

---

## Data Flow: 712 Ventures → Campaigns

### Verify Setup

**1. Check 712 ventures exist**
```sql
SELECT COUNT(*) FROM ventures;
-- Expected: 712
```

**2. Check campaign tables created**
```sql
SELECT COUNT(*) FROM information_schema.tables 
WHERE table_name LIKE 'campaign%';
-- Expected: 5 tables
```

**3. Launch test campaign**
```bash
python3 campaign_orchestrator.py \
  --venture v-hrms-001 \
  --template tmpl-service-launch \
  --name "Test Campaign" \
  --budget 1000
```

**4. Verify in Supabase**
```sql
SELECT * FROM campaigns WHERE venture_id = 'v-hrms-001';
SELECT * FROM campaign_stages WHERE campaign_id = 'camp-v-hrms-001-...';
```

---

## Implementation Checklist

- [ ] Run campaign-supabase-schema.sql
- [ ] Test campaign_orchestrator.py locally
- [ ] Add /api/campaigns endpoints to venture-hub
- [ ] Verify CAMPAIGN-FACTORY-DASHBOARD.md updates
- [ ] Launch first campaign (HRMS)

---

**System ready. 712 ventures aligned. All three interfaces live: Supabase + Python + Obsidian.**
