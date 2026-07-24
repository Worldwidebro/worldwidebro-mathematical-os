# Vex Engine Roadmap — Execution Layer Expansion

## Phase 1: Multi-Venture Support (Week 1-2)

### 1.1 Extend Dashboard to Show 5 Ventures

**Current:** Single venture (CON-001) hardcoded  
**Target:** Dashboard shows all 5 ventures in selector dropdown

```tsx
// vex-engine/src/app/page.tsx
<VentureSelector ventures={['CON-001', 'CON-002', 'CON-003', 'CON-004', 'CON-005']} />

// Filters all data by selected venture:
const leads = await getLeads(selectedVenture);
const deals = await getDeals(selectedVenture);
const revenue = await getRevenue(selectedVenture);
```

### 1.2 Add Venture Execution Tabs

Each venture gets its own execution pipeline view:

```
📊 Dashboard (all ventures MRR rollup)
  ├─ CON-001: Ace Construction
  │   ├─ Lead Capture: 12 this week
  │   ├─ Active Deals: 3 ($8.5K)
  │   ├─ Pending Proposals: 2
  │   └─ Actions Needed: 1 (review SOP)
  ├─ CON-002: [similar]
  ├─ CON-003: [similar]
  ├─ CON-004: [similar]
  └─ CON-005: [similar]
```

### 1.3 Extend Supabase Schema

Add columns to track multi-venture execution:

```sql
-- venture_leads
ALTER TABLE venture_leads ADD COLUMN venture_id TEXT;
ALTER TABLE venture_leads ADD COLUMN stage TEXT; -- 'lead' | 'researched' | 'contacted' | 'meeting_scheduled' | 'proposal_sent' | 'won' | 'lost'

-- Add indexes
CREATE INDEX idx_venture_leads_venture_id ON venture_leads(venture_id);
CREATE INDEX idx_venture_leads_stage ON venture_leads(stage);

-- venture_operations (new table)
CREATE TABLE venture_operations (
  id UUID PRIMARY KEY,
  venture_id TEXT NOT NULL,
  operation_type TEXT, -- 'lead_captured' | 'meeting_scheduled' | 'proposal_sent' | 'payment_received' | 'document_uploaded'
  data JSONB,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);
```

---

## Phase 2: Document Retrieval (Week 2-3)

### 2.1 Add PDF Upload Endpoint

```typescript
// vex-engine/src/pages/api/upload.ts
POST /api/upload
Body: { venture_id, document_type, file: File }

Response:
{
  document_id: "doc_xyz",
  venture_id: "CON-001",
  type: "SOP", // 'SOP' | 'Contract' | 'Spec' | 'Quote'
  pages: 12,
  status: "indexed"
}
```

### 2.2 Integrate PageIndex

```python
# vex-engine/scripts/index_documents.py
from pageindex import PageIndex

class VentureDocumentIndexer:
    def __init__(self):
        self.indexer = PageIndex()
    
    def index_pdf(self, venture_id: str, pdf_path: str) -> dict:
        """Parse PDF into tree structure"""
        tree = self.indexer.build_tree(pdf_path)
        
        # Store in Supabase
        supabase.table('venture_documents').insert({
            'venture_id': venture_id,
            'tree_index': tree,
            'status': 'indexed'
        })
        
        return tree
    
    def retrieve(self, venture_id: str, query: str) -> list:
        """Reasoning-based retrieval over document tree"""
        # Use LLM to reason through tree
        sections = self.indexer.search(tree, query)
        return sections
```

### 2.3 Wire PageIndex to Agents

Agent retrieves SOP before executing:

```python
# Agent: Deal Intake
@agent.action('execute_deal')
async def execute_deal(venture_id: str, deal_data: dict):
    # 1. Retrieve relevant SOP section
    sop = document_indexer.retrieve(
        venture_id,
        "compliance requirements for quotes"
    )
    
    # 2. Extract compliance rules
    rules = llm.extract_rules(sop['content'])
    
    # 3. Apply to deal
    validated_deal = validate_deal(deal_data, rules)
    
    # 4. Execute
    return execute_stripe_payment(validated_deal)
```

---

## Phase 3: Event-Driven Workflows (Week 3-4)

### 3.1 Add NATS Event Bus

```typescript
// vex-engine/src/lib/events.ts
import { NatsConnection } from 'nats';

export const events = {
  lead_captured: (venture_id: string, lead: object) => 
    nats.publish(`venture.${venture_id}.lead.captured`, lead),
  
  meeting_scheduled: (venture_id: string, meeting: object) =>
    nats.publish(`venture.${venture_id}.meeting.scheduled`, meeting),
  
  document_uploaded: (venture_id: string, doc: object) =>
    nats.publish(`venture.${venture_id}.document.uploaded`, doc),
};
```

### 3.2 Wire Events to Workflows

```typescript
// Lead created → Research Agent wakes up
nats.subscribe('venture.*.lead.captured', async (msg) => {
  const { venture_id, lead } = JSON.parse(msg.data);
  await agents.research.run(venture_id, lead);
});

// Research complete → Outreach Agent wakes up
nats.subscribe('venture.*.research.complete', async (msg) => {
  const { venture_id, lead } = JSON.parse(msg.data);
  await agents.outreach.run(venture_id, lead);
});

// Outreach complete → Meeting scheduled
nats.subscribe('venture.*.outreach.complete', async (msg) => {
  const { venture_id, meeting } = JSON.parse(msg.data);
  await events.meeting_scheduled(venture_id, meeting);
});
```

---

## Success Criteria

**Week 1:** Multi-venture dashboard live, 5 ventures visible  
**Week 2:** PDF upload + PageIndex indexing working  
**Week 3:** Event bus live, 1 venture auto-closes deals  
**Week 4:** 5 ventures running, combined MRR visible  
