# DealFlowOS Agent Invocation — Quick Reference

**Status:** ✅ Ready to use | **OmniRoute:** Online at http://100.87.214.70:20128

---

## 🚀 Quick Start (3 Steps)

### Step 1: Launch Terminal
Open `dealflow-os.html` in browser → Terminal loads automatically with agent status

### Step 2: Run a Research Agent
```javascript
await dealflowDashboard.launchResearchAgent(
  "What are the top 20 SaaS healthcare companies?"
);
```

### Step 3: Watch Live Terminal
- Research findings stream line-by-line
- Green ✓ for success, red ✗ for errors
- Status updates: RUNNING → COMPLETE

---

## 📋 Agent Invocation Methods

### Via Claude Code (MCP Tools)

```bash
# Check agent status
omniroute_agent_status()

# Research agent
omniroute_invoke_research_agent(
  query="Top SaaS companies in healthcare"
)

# Qualification agent
omniroute_invoke_qualification_agent(
  company_data='{"name": "TechCorp", "revenue": "50M", "employees": 200}'
)

# Outreach agent
omniroute_invoke_outreach_agent(
  qualified_leads='[{"name": "Jane Smith", "company": "TechCorp"}]'
)
```

### Via JavaScript (DealFlowOS Dashboard)

```javascript
// Research
await dealflowDashboard.launchResearchAgent(query, companyContext);

// Qualification
await dealflowDashboard.launchQualificationAgent(companyData);

// Outreach
await dealflowDashboard.launchOutreachAgent(qualifiedLeads, campaignContext);

// Status
console.log(dealflowDashboard.getStatusDisplay());
```

### Via Python (Direct Invocation)

```python
import asyncio
from _MCP.omniroute_agents import OmniRouteClient, DealFlowOSAgents

async def main():
    client = OmniRouteClient()
    agents = DealFlowOSAgents(client)
    
    result = await agents.invoke_research_agent(
        query="Top SaaS companies",
        company_context={"industry": "healthcare"}
    )
    print(result['response'])

asyncio.run(main())
```

---

## 🎯 Six Agents Overview

| # | Agent | Input | Output | Best For |
|---|-------|-------|--------|----------|
| 1️⃣ | **Research** | Query string | Market intel, company data | Gathering data |
| 2️⃣ | **Qualification** | Company object | Score 0-100, decision | Go/no-go decisions |
| 3️⃣ | **Outreach** | Lead array | Email sequences, timing | Drafting campaigns |
| 4️⃣ | **Prospect Sourcing** | ICP object | 20-50 target companies | Building lead lists |
| 5️⃣ | **Deal Analysis** | Deal object | Deal score, risk, probability | Deal health checks |
| 6️⃣ | **Optimization** | Campaign metrics | A/B tests, improvements | Learning from results |

---

## 💾 Input/Output Formats

### Research Agent

**Input:**
```json
{
  "query": "Top SaaS healthcare companies 2026",
  "company_context": {"industry": "healthcare", "stage": "growth"}
}
```

**Output:**
```json
{
  "status": "success",
  "response": "[{company, funding, growth_rate, signals, ...}]"
}
```

### Qualification Agent

**Input:**
```json
{
  "name": "TechCorp",
  "revenue": "50M ARR",
  "employees": 200,
  "industry": "healthcare",
  "signals": ["Series B funding", "hiring growth"]
}
```

**Output:**
```json
{
  "score": 87,
  "fit": 0.92,
  "decision": "QUALIFY",
  "reasons": ["Strong revenue growth", "Aligns with ICP"],
  "next_steps": ["Schedule demo", "Send proposal"]
}
```

### Outreach Agent

**Input:**
```json
{
  "leads": [
    {"name": "Jane Smith", "company": "TechCorp", "role": "VP Sales"},
    {"name": "Bob Johnson", "company": "HealthData Inc", "role": "CRO"}
  ],
  "campaign": {"value_prop": "AI deal flow", "timeline": "Q4 2026"}
}
```

**Output:**
```json
[
  {
    "lead_name": "Jane Smith",
    "email_subject": "Quick question about TechCorp's sales intel",
    "email_body": "Hi Jane,\n\nSaw TechCorp's recent Series B...",
    "timing": "Tuesday 10am ET",
    "followups": ["2 days: gentle follow-up", "5 days: value prop", "10 days: close"]
  }
]
```

---

## ⚙️ Model Selection

Each agent uses an optimized model:

| Agent | Model | Speed | Cost | Reasoning |
|-------|-------|-------|------|-----------|
| Research | qwen-heavy | Slow | $0.015 | Complex analysis |
| Qualification | qwen-fast | Fast | $0.003 | Quick scoring |
| Outreach | default | Medium | $0.008 | Balanced |

Override model in Python layer:
```python
await agents.invoke_research_agent(
    query="...",
    model="default"  # Use faster model if needed
)
```

---

## 📊 Terminal Output Example

```
DealFlowOS Command Center initialized
OmniRoute agents ready for research → qualify → outreach flows
✓ OmniRoute online at http://100.87.214.70:20128

═══════════════════════════════════════════
DealFlowOS Agent Status
═══════════════════════════════════════════
✓ Research Agent: IDLE [2026-09-08 10:32:45]
✓ Qualification Agent: IDLE [2026-09-08 10:31:20]
✓ Outreach Agent: IDLE [2026-09-08 10:30:05]
✓ Prospect Sourcing Agent: IDLE [Never]
✓ Deal Analysis Agent: IDLE [Never]
✓ Outreach Optimization Agent: IDLE [Never]
═══════════════════════════════════════════

> Launch research agent
[Research Agent] Starting research: Top SaaS healthcare companies
Top companies in healthcare sector:
1. Company A - $500M ARR, Series D, 50% YoY growth
2. Company B - $300M ARR, Series C, 35% YoY growth
...
[Research Agent] Complete
```

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Terminal not loading** | Refresh page, check browser console |
| **OmniRoute offline** | SSH to macstudio: `docker restart omniroute` |
| **Model not found** | Add to litellm-config.yaml + restart civos_litellm |
| **Streaming timeout** | Increase timeout in client (default 120s) |
| **JSON parse error** | Validate input JSON format in terminal |
| **Agent running forever** | Check OmniRoute health, restart if needed |

---

## 📈 Performance Metrics

| Agent | Avg Latency | Cost/Run | Input Tokens | Output Tokens |
|-------|-------------|----------|--------------|---------------|
| Research | 3-5s | $0.015 | 500 | 2,000 |
| Qualification | 1-2s | $0.003 | 300 | 1,000 |
| Outreach | 2-3s | $0.008 | 800 | 3,000 |

**Full pipeline cost (research → qualify 50 → outreach 20):** ~$0.50-$1.00

---

## 🎓 Example: Complete Research → Qualify → Outreach Flow

### 1. Research

```python
research = await agents.invoke_research_agent(
    "Top 50 SaaS companies in healthcare with recent funding"
)
# Returns: {..., "response": "[{company, funding, ...}]"}
```

### 2. Qualify Each

```python
companies = json.loads(research['response'])
qualified = []

for company in companies[:20]:  # Sample first 20
    result = await agents.invoke_qualification_agent({
        "name": company["name"],
        "revenue": company.get("revenue"),
        "employees": company.get("employees"),
        "industry": "healthcare"
    })
    data = json.loads(result['response'])
    if data['decision'] == 'QUALIFY':
        qualified.append(company)
```

### 3. Generate Outreach

```python
outreach = await agents.invoke_outreach_agent(
    qualified_leads=qualified[:20],
    campaign_context={
        "value_prop": "AI-powered deal flow",
        "timeline": "Q4 2026",
        "product_focus": ["revenue growth", "cost reduction"]
    }
)
# Returns: {..., "response": "[{lead_name, email_subject, ...}]"}
```

### 4. Execute (External System)

```python
sequences = json.loads(outreach['response'])
for sequence in sequences:
    # Send email to CRM
    # Schedule follow-ups
    # Track opens/clicks
```

---

## 📞 Support

**Issues?** Check:
- `OMNIROUTE_DEALFLOW_INTEGRATION.md` (full integration guide)
- `OMNIROUTE_AGENT_HOOKUP_SUMMARY.md` (technical overview)
- OmniRoute health: http://100.87.214.70:20128

**Need to restart OmniRoute?**
```bash
ssh macstudio
docker ps | grep omniroute
docker restart <container_id>
```

---

**Version:** 1.0 | **Updated:** 2026-09-08 | **Authority:** CP-006 + CP-027
