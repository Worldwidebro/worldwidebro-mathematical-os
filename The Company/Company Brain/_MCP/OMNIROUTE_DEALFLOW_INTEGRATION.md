# OmniRoute + DealFlowOS Integration Guide

**Authority:** Agent Control Plane (CP-006) + Infrastructure Control Plane (CP-027)  
**Status:** ✅ Ready for deployment  
**Date:** 2026-09-08

---

## Overview

This integration connects DealFlowOS AI Command Center to OmniRoute's multi-model inference gateway, enabling six autonomous AI agents for deal flow research, qualification, and outreach.

### Six Agents Available

| Agent | Purpose | Model | Use Case |
|-------|---------|-------|----------|
| **Research Agent** | Gather intelligence | qwen-heavy | Market research, competitor analysis, company intel |
| **Qualification Agent** | Score & qualify leads | qwen-fast | Lead scoring, fit analysis, decision support |
| **Outreach Agent** | Draft personalized sequences | default | Email copy, timing, follow-up cadence |
| **Prospect Sourcing** | Identify target companies | qwen-heavy | ICP-based sourcing, contact discovery |
| **Deal Analysis** | Assess deal health | qwen-fast | Deal scoring, risk assessment, win probability |
| **Outreach Optimization** | Learn from campaign results | qwen-fast | A/B test ideas, timing insights, improvements |

---

## Architecture

```
DealFlowOS Command Center
    ↓
JavaScript Streaming Client (dealflow-omniroute-client.js)
    ↓
OmniRoute API Gateway (http://100.87.214.70:20128)
    ↓
LiteLLM Router → Model Selection
    ↓
Inference Providers:
├─ exo (qwen-fast/qwen-heavy)
├─ Ollama (fallback)
└─ Claude API (high-complexity queries)
```

### Control Planes Involved

- **CP-006 (Agent Control Plane):** Agent routing, selection, autonomy levels
- **CP-027 (Infrastructure Control Plane):** OmniRoute health, model availability
- **CP-029 (Observability):** Langfuse tracing (wired when enabled)

---

## Integration Layers

### Layer 1: Python Backend (`omniroute_agents.py`)

**Purpose:** Async HTTP client + agent invocation logic

**Classes:**
- `OmniRouteClient`: Low-level HTTP client with streaming support
- `DealFlowOSAgents`: Six agent wrappers, status tracking

**Usage:**
```python
from _MCP.omniroute_agents import OmniRouteClient, DealFlowOSAgents

client = OmniRouteClient()
agents = DealFlowOSAgents(client)

# Invoke research agent
result = await agents.invoke_research_agent(
    query="Top SaaS healthcare companies 2026",
    company_context={"industry": "healthcare"}
)

# Get all agent status
status = agents.get_agent_status()
# Returns: {agents: {research_agent: {status, last_run}, ...}, agent_count: 6, online_agents: 6}
```

### Layer 2: MCP Tools (`fastmcp_server.py`)

**Purpose:** Expose agent invocations as MCP tools for Claude Code

**Tools Available:**
- `omniroute_invoke_research_agent(query, company_context, model)`
- `omniroute_invoke_qualification_agent(company_data)`
- `omniroute_invoke_outreach_agent(qualified_leads, campaign_context)`
- `omniroute_agent_status()`

**Usage in Claude Code:**
```
Use the omniroute_invoke_research_agent tool with query="What are top SaaS companies?"
```

### Layer 3: JavaScript Frontend (`dealflow-omniroute-client.js`)

**Purpose:** Streaming client for DealFlowOS dashboard, real-time terminal output

**Classes:**
- `OmniRouteStreamingClient`: Streaming HTTP client with chunk parsing
- `DealFlowOSTerminal`: Live terminal UI, line buffering
- `DealFlowOSAgentDashboard`: Agent orchestration, status display

**Usage in HTML:**
```html
<script src="_MCP/dealflow-omniroute-client.js"></script>

<div id="terminal-container"></div>

<script>
  // Terminal and dashboard created automatically on page load
  
  // Launch research agent
  await dealflowDashboard.launchResearchAgent(
    "What are top SaaS companies in healthcare?",
    {industry: "healthcare"}
  );
  
  // Get agent status
  console.log(dealflowDashboard.getStatusDisplay());
</script>
```

---

## Deployment Steps

### Step 1: Verify OmniRoute is Running

```bash
curl -s http://100.87.214.70:20128/health | jq .
# Should return: {...}
```

### Step 2: Test MCP Tools

Restart Claude Code to pick up new MCP tools:

```bash
# In Claude Code
omniroute_agent_status()
# Should return: {agents: {...}, agent_count: 6, online_agents: 6, ...}
```

### Step 3: Integrate into DealFlowOS Dashboard

In `dealflow-os.html`, add:

```html
<!-- Include streaming client -->
<script src="_MCP/dealflow-omniroute-client.js"></script>

<!-- Add terminal container -->
<div id="terminal-container" style="flex: 1; margin-top: 20px;"></div>

<!-- Hook Launch button to agent invocation -->
<script>
  document.getElementById('launch-btn').addEventListener('click', async () => {
    const query = document.getElementById('search-input').value;
    if (dealflowDashboard) {
      await dealflowDashboard.launchResearchAgent(query);
    }
  });
</script>
```

### Step 4: Configure Model Routing (Optional)

Edit OmniRoute model list if you want to expose additional models to agents:

```bash
ssh macstudio
# Edit: /Users/divinejohns/Iza-OS-Tree-of-Life/ops/infra/litellm-config.yaml
# Add model_list entries for qwen2.5-coder, nomic-embed-text, etc.
docker restart civos_litellm
```

---

## Example: Research → Qualify → Outreach Flow

### 1. Research (Gather Intelligence)

```python
# Agent: Research Agent
research = await agents.invoke_research_agent(
    query="Top 50 SaaS companies in healthcare with recent funding",
    company_context={"sector": "healthcare", "stage": "growth"}
)
# Returns: {status: "success", response: "[{company, funding, growth_rate, ...}]"}
```

### 2. Qualify (Score Companies)

```python
# Parse research results into company list
companies = json.loads(research['response'])

# Agent: Qualification Agent (for each company)
for company in companies[:10]:
    score = await agents.invoke_qualification_agent({
        "name": company["name"],
        "revenue": company.get("revenue"),
        "employees": company.get("employees"),
        "industry": "healthcare",
        "signals": company.get("signals", [])
    })
    # Returns: {status: "success", response: "{score: 92, decision: QUALIFY, ...}"}
```

### 3. Outreach (Draft Sequences)

```python
# Filter qualified leads
qualified = [c for c in scored_companies if c["decision"] == "QUALIFY"]

# Agent: Outreach Agent
outreach = await agents.invoke_outreach_agent(
    qualified_leads=qualified[:20],
    campaign_context={
        "value_prop": "AI-powered healthcare operations",
        "timeline": "Q4 2026",
        "product_focus": ["cost reduction", "compliance"]
    }
)
# Returns: {status: "success", response: "[{lead_name, email_subject, email_body, timing, ...}]"}
```

---

## Streaming Responses to Terminal

The JavaScript client streams responses line-by-line to the DealFlowOS terminal:

```javascript
// Live terminal updates
dealflowTerminal.addLine('[Research Agent] Researching...', 'info');

await dealflowDashboard.launchResearchAgent(query);
// Terminal output:
// [Research Agent] Starting research: ...
// Top companies in healthcare:
// 1. Company A - $500M ARR
// 2. Company B - $300M ARR
// ...
// [Research Agent] Complete
```

---

## Agent Status Polling

Dashboard displays agent status on load and after each run:

```
═══════════════════════════════════════════
DealFlowOS Agent Status
═══════════════════════════════════════════
✓ Research Agent: IDLE [10:32:45 AM]
✓ Qualification Agent: IDLE [10:31:20 AM]
✓ Outreach Agent: IDLE [10:30:05 AM]
✓ Prospect Sourcing Agent: IDLE [Never]
✓ Deal Analysis Agent: IDLE [Never]
✓ Outreach Optimization Agent: IDLE [Never]
═══════════════════════════════════════════
```

---

## Cost & Performance

| Agent | Model | Avg Latency | Est. Cost/Run | Input Tokens | Output Tokens |
|-------|-------|-------------|---------------|--------------|---------------|
| Research | qwen-heavy | 3-5s | ~$0.015 | 500 | 2000 |
| Qualification | qwen-fast | 1-2s | ~$0.003 | 300 | 1000 |
| Outreach | default | 2-3s | ~$0.008 | 800 | 3000 |

**Total cost per full flow (research → qualify 50 → outreach 20):** ~$0.50-$1.00

---

## Troubleshooting

### OmniRoute Offline

```bash
# Check OmniRoute container
ssh macstudio
docker ps | grep omniroute

# If down, restart
docker-compose -f ops/infra/docker-compose.yml up -d omniroute
```

### Model Not Found

```bash
# Check available models in LiteLLM config
curl http://100.87.214.70:4000/v1/models | jq .
# If model missing, add to litellm-config.yaml and restart civos_litellm
```

### Streaming Timeout

```javascript
// Increase timeout in client
client.invokeStream({
  ...options,
  timeout: 120000  // 2 minutes
});
```

### Terminal Not Displaying

```javascript
// Check if container exists
if (!document.getElementById('terminal-container')) {
  console.error('Terminal container not found in DOM');
}
```

---

## Next Steps

1. **Week 1:** Verify all 6 agents are online and responding
2. **Week 2:** Integrate dashboard Launch button → research agent
3. **Week 3:** Add qualify → outreach pipeline
4. **Week 4:** Enable Langfuse tracing for cost/performance monitoring
5. **Week 5:** Implement A/B testing framework for outreach optimization

---

## Files Checklist

- ✅ `_MCP/omniroute_agents.py` - Agent invocation layer
- ✅ `_MCP/fastmcp_server.py` - MCP tools (updated with agent tools)
- ✅ `_MCP/dealflow-omniroute-client.js` - Streaming frontend client
- ✅ `dealflow-os.html` - (update needed: add terminal container, wire Launch button)
- ✅ `_MCP/OMNIROUTE_DEALFLOW_INTEGRATION.md` - This guide

---

## Authority & Governance

**Approval Gate:** Infrastructure Control Plane (CP-027)  
**Deployer:** Engineering team  
**Monitoring:** Langfuse (optional, set up in Phase 2)  
**Runbook:** See [[OmniRoute Deployment Runbook]]
