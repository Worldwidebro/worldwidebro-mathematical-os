# CON-001 Automation Stack — Cost Breakdown

## Current Software (Already Paying)

| Tool | Cost/Mo | Purpose | Keep? |
|------|---------|---------|-------|
| Procore | $500 | Project mgmt | ✅ Yes |
| QuickBooks Contractor | $80 | Job costing, invoicing | ✅ Yes |
| PlanSwift | $99 | Estimating, takeoffs | ✅ Yes |
| Houzz Pro | $299 | Lead gen + portfolio | ✅ Yes |
| Angi (Angie's List) | $300-$500 | Home improvement leads | ✅ Yes |
| Google Ads | $1K-$3K | Local search | ✅ Yes |
| Bluebeam Revu | $30/yr | PDF markup | ✅ Yes |
| Slack | $0 (free) | Team comms | ✅ Yes |
| Zoom | $15 | Meetings | ✅ Yes |
| **SUBTOTAL** | **$2,400-$4,400/mo** | | |

---

## New Automation Stack (8 Loops)

### Option A: Low-Cost Open Source (Self-Hosted)

| Component | Tool | Cost/Mo | Notes |
|-----------|------|---------|-------|
| **Workflow Engine** | n8n (self-hosted) | $0 | 1 VPS ($10-20/mo) |
| **Browser Automation** | Playwright | $0 | Open source |
| **OCR** | PaddleOCR | $0 | Open source |
| **CRM** (Optional) | Twenty CRM (self-hosted) | $0 | Replaces Salesforce, not needed yet |
| **AI Agents** | LangGraph + Claude API | $50-100 | API calls only (pay per use) |
| **Scheduling** | Cal.com (self-hosted) | $0 | Open source |
| **Internal Dashboard** | NocoDB or Appsmith | $0 | Self-hosted |
| **Document Processing** | LlamaParse | $0-20 | Free tier covers most; paid if heavy use |
| **Observability** | Grafana (self-hosted) | $0 | Open source |
| **VPS for self-hosted** | Render/Railway | $10-20 | 1 VPS for n8n + 20 other services |
| **SUBTOTAL** | | **$60-140/mo** | |

### Option B: Low/Medium Friction (Managed Services)

| Component | Tool | Cost/Mo | Notes |
|-----------|------|---------|-------|
| **Workflow Engine** | Zapier | $50-100 | Easy, not as powerful as n8n |
| **OR** | Make/Integromat | $10-99 | Slightly cheaper, more features than Zapier |
| **OCR** | Cloudinary/AWS Textract | $5-50 | Pay per document |
| **AI Agents** | Claude API (Anthropic) | $50-200 | Pay per token/API call |
| **CRM** (Optional) | HubSpot Free | $0 | 1M contact free tier |
| **Dashboard** | Retool/Budibase | $25-50 | Low-code dashboards |
| **SUBTOTAL** | | **$140-500/mo** | Depends on usage |

### Option C: Premium Managed (Least Setup Burden)

| Component | Tool | Cost/Mo | Notes |
|-----------|------|---------|-------|
| **Automation** | Zapier Pro | $250-500 | Fully managed, many integrations |
| **AI Agents** | Claude API + consulting | $500-1000 | Custom agent development |
| **OCR** | AWS Textract | $20-100 | Production-grade |
| **CRM** | HubSpot Professional | $500-1500 | Full features, support |
| **Dashboard** | Retool/Budibase | $50-100 | Managed hosting |
| **SUBTOTAL** | | **$1,320-3,200/mo** | Highest hands-off |

---

## Implementation Effort & Cost

| Phase | Task | Effort | Cost (if hiring) |
|-------|------|--------|------------------|
| **Phase 1: Setup** | Wire Procore + QB + PlanSwift APIs | 40 hrs | $2K-4K |
| **Phase 2: Build Loops** | 8 loops (lead intake, estimator, bid coord, PM, procurement, acct, compliance, exec) | 120 hrs | $6K-12K |
| **Phase 3: Test** | End-to-end testing, edge cases | 40 hrs | $2K-4K |
| **Phase 4: Deploy** | Production setup, monitoring, runbooks | 20 hrs | $1K-2K |
| **Phase 5: Training** | Teach team how to use + monitor | 10 hrs | $500-1K |
| **TOTAL IMPLEMENTATION** | | **230 hrs** | **$11.5K-23K** |

---

## Total Annual Cost Comparison

### Scenario 1: Open Source (Self-Hosted)

```
Current software:    $2,400 × 12 = $28,800/yr
New automation:      $100 × 12   = $1,200/yr
Implementation:      One-time    = $15K (mid-range)
────────────────────────────────────
TOTAL YEAR 1:                      $45K
TOTAL YEAR 2+:                     $30K/yr (just software)
```

### Scenario 2: Managed Services (Zapier + Claude)

```
Current software:    $2,400 × 12 = $28,800/yr
New automation:      $300 × 12   = $3,600/yr
Implementation:      One-time    = $15K
────────────────────────────────────
TOTAL YEAR 1:                      $47.4K
TOTAL YEAR 2+:                     $32.4K/yr
```

### Scenario 3: Premium Managed (Full Service)

```
Current software:    $2,400 × 12 = $28,800/yr
New automation:      $2,000 × 12 = $24,000/yr
Implementation:      One-time    = $20K
────────────────────────────────────
TOTAL YEAR 1:                      $72.8K
TOTAL YEAR 2+:                     $52.8K/yr
```

---

## Recommended Path: Scenario 1 (Open Source)

**Why:**
- Lowest total cost ($45K Year 1, $30K ongoing)
- Full control (no vendor lock-in)
- Can scale infinitely
- Same capabilities as premium options
- VPS ($10-20/mo) runs 20+ open-source services

**Tools to Use:**

| Loop | Tool | Cost |
|------|------|------|
| Workflow Orchestration | n8n (self-hosted) | $0 |
| Browser Automation | Playwright | $0 |
| OCR | PaddleOCR | $0 |
| AI Agents | LangGraph + Claude API | $50-100/mo |
| CRM | Twenty CRM (self-hosted) | $0 |
| Dashboard | NocoDB | $0 |
| Scheduling | Cal.com (self-hosted) | $0 |
| Observability | Grafana | $0 |
| Infrastructure | 1 VPS | $10-20/mo |

---

## ROI Calculation

**If CON-001 reaches targets:** $56K-$147K/month net profit

**Automation saves ~10-15 hrs/week of manual work:**
- Lead intake manually → 2 hrs/week
- Estimate generation → 4 hrs/week
- Invoice/payment tracking → 3 hrs/week
- Team coordination → 4 hrs/week
- Reporting → 2 hrs/week
- **Total: 15 hrs/week saved**

**Annual value of 15 hrs/week at $100/hr labor:**
- $100 × 15 × 52 = **$78K/year saved in labor**

**ROI:**
- Investment Year 1: $45K
- Savings Year 1: $78K
- **Net Gain Year 1: $33K** ✅

---

## Systems You Can Drop

Once automation is live:
- ❌ Manual lead tracking (now automated by Lead Intake Agent)
- ❌ Manual estimate generation (Estimator Agent handles)
- ❌ Manual invoice reminders (Accounting Agent tracks)
- ❌ Daily status meetings (Executive Agent sends briefing)

**Potential savings: $500-$2K/month in labor + faster turnaround**

---

## What to Do Now

### Immediate (This Week):
1. Pick Scenario 1 (recommended)
2. Spin up 1 VPS ($10-20/mo for 2 years = $240-480)
3. Install n8n + Grafana on VPS
4. Wire Procore + QB APIs

### Week 2-3:
5. Build Loop 1 (Lead Intake) → test with 1 lead
6. Deploy + monitor

### Week 4+:
7. Build Loop 2-8 iteratively (1 per week)

**Total Time to "real and live" with automation: 30-45 days**
