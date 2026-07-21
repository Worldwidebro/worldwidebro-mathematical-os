# Company Brain OS - 16 Layers × Tools × Slash Commands

**Mapping:** Each of 16 layers → existing tools/MCPs → slash commands → status

---

## LAYER 1: Identity & Governance (WHOAMI + Charters)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Vision/Mission | WHOAMI.md | — | — | ✅ DONE |
| Corporate Structure | IZA-OS hierarchy | — | — | ✅ DONE |
| Org Chart | OPCO-CHARTERS (6×) | — | — | ⏳ INSTANTIATE |
| Decision Rights | DECISION-FRAMEWORK.md | — | `/architecture-decision-records` | ⏳ BUILD |
| OKRs | Google Sheets | Google Sheets MCP | `/google-workspace-ops` | ⏳ WIRE |
| Risk Register | Neo4j | Neo4j MCP | `/neo4j-graphrag-skill` | ⏳ SEED |

---

## LAYER 2: Knowledge Brain (Obsidian + Qdrant + Neo4j)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Document Mgmt | Obsidian | Obsidian MCP | `/obsidian-second-brain` | ✅ LIVE |
| Semantic Search | Qdrant | Qdrant MCP | `qdrant-clients-sdk` | ✅ LIVE (1,648 vectors) |
| Knowledge Graph | Neo4j | Neo4j MCP | `/neo4j-graphrag-skill` | ⏳ SEED (0 nodes) |
| Playbooks | OPCO-AGENT-SETUP.md | — | `/architecture-decision-records` | ⏳ BUILD |
| SOP Library | GitHub repos (1,639) | GitHub MCP | `/socraticode:codebase-management` | ✅ INDEXED |
| Lessons Learned | Obsidian vault | Obsidian MCP | `/obsidian-second-brain` | ⏳ BUILD |

---

## LAYER 3: Agent Platform (CrewAI + Hermes + agent-teams)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Agent Registry | AGENTS-INVENTORY.json | — | — | ⏳ CREATE |
| Agent Marketplace | GitHub (agents/) | GitHub MCP | `/github-ops` | ⏳ BUILD |
| Prompt Registry | prompt_templates/ | — | `/prompt-optimizer` | ⏳ BUILD |
| Tool Registry | MCP_REGISTRY.json | — | — | ✅ LIVE (17 MCPs) |
| Memory | Memory MCP | Memory MCP | `mcp__plugin_everything-claude-code_memory__*` | ✅ LIVE |
| Task Queue | Supabase | Supabase MCP | `mcp__claude_ai_Supabase__*` | ✅ LIVE |
| Scheduling | n8n | n8n MCP | `/schedule` | ⏳ WIRE |
| Multi-Agent Orchestration | agent-teams:team-lead | — | `/orchestrate` | ✅ READY |
| Agent Permissions | DECISION-FRAMEWORK.md | — | `/architecture-decision-records` | ⏳ BUILD |
| Cost Tracking | Langfuse | Langfuse MCP | (built-in) | ✅ LIVE |

---

## LAYER 4: Workflow Engine (n8n + agent-orchestration)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Visual Workflow Builder | n8n (5678) | n8n MCP | — | ✅ LIVE |
| Conditional Logic | n8n + Hermes | — | `/orchestrate` | ⏳ WIRE |
| Parallel Execution | agent-teams:team-lead | — | `/orchestrate` | ✅ READY |
| Retry Handling | n8n | n8n MCP | — | ✅ BUILT-IN |
| Error Handling | n8n + AOC | — | `agent_operations_center_watcher.py` | ✅ BUILT |
| SLA Monitoring | Prometheus/Grafana | Prometheus MCP | (Grafana MCP) | ⏳ CONFIGURE |
| Scheduled Jobs | n8n | n8n MCP | `/schedule` | ⏳ WIRE |
| Event-Driven Triggers | n8n webhooks | — | — | ✅ READY |
| Approval Workflows | Supabase + n8n | Supabase MCP | (custom workflow) | ⏳ BUILD |

---

## LAYER 5: Decision Engine (Hermes + Neo4j + LLM)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Recommendation Engine | Hermes + Qdrant | Qdrant MCP | `/prompt-engineer` | ⏳ BUILD |
| Scenario Planning | Hermes + Claude | — | `/plan` | ✅ BUILT-IN |
| Cost-Benefit Analysis | Claude + Supabase | Supabase MCP | `/business-analyst` | ⏳ DEPLOY |
| Risk Scoring | Neo4j + Claude | Neo4j MCP | `/threat-modeling-expert` | ⏳ BUILD |
| Decision Logs | Supabase | Supabase MCP | — | ⏳ BUILD (venture_decisions table) |
| Decision Trees | Neo4j | Neo4j MCP | `/neo4j-graphrag-skill` | ⏳ SEED |
| AI Copilots | Claude API + agents | — | `/prompt-engineer` | ✅ READY |

---

## LAYER 6: Operational Intelligence (Grafana + Prometheus + Langfuse)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| KPI Dashboards | Grafana (3001) | Grafana MCP | — | ✅ LIVE (needs data wiring) |
| Health Monitoring | Prometheus (9090) | Prometheus MCP | — | ⏳ CONFIGURE (only self-scraping) |
| Alerts | Grafana + Slack | Slack MCP | `/slack_send_message` | ✅ READY |
| Trends | DuckDB + Grafana | DuckDB (local) | — | ⏳ WIRE |
| Benchmarking | DuckDB analytics | DuckDB | — | ⏳ BUILD |
| Predictive Analytics | Claude + historical data | — | `/data-scientist` | ⏳ BUILD |
| Root Cause Analysis | Langfuse + Claude | Langfuse MCP | `/error-detective` | ✅ READY |

---

## LAYER 7: Customer Intelligence (Twenty CRM + Supabase + HubSpot)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| CRM Integration | Twenty (3002) + HubSpot | HubSpot MCP | `mcp__claude_ai_HubSpot__*` | ⏳ WIRE |
| Customer 360 | Supabase + Neo4j | Supabase MCP | `mcp__claude_ai_Supabase__*` | ⏳ BUILD |
| Segmentation | Claude + Supabase | Supabase MCP | `/business-analyst` | ⏳ BUILD |
| Journey Mapping | Neo4j | Neo4j MCP | `/neo4j-graphrag-skill` | ⏳ BUILD |
| Support History | Supabase | Supabase MCP | — | ✅ READY |
| Satisfaction Tracking | Twenty + Supabase | Supabase MCP | — | ⏳ WIRE |
| Churn Prediction | Claude + historical data | — | `/data-scientist` | ⏳ BUILD |
| Opportunity Scoring | Claude + Supabase | Supabase MCP | `/sales-automator` | ⏳ BUILD |

---

## LAYER 8: Sales OS (Stripe + n8n + marketingskills)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Lead Scoring | Claude + marketingskills | Stripe MCP | `/sales-automator` | ⏳ WIRE |
| Pipeline Management | Supabase + Twenty | Supabase MCP | — | ✅ READY |
| Proposal Generation | Stirling PDF + n8n | (PDF) | — | ⏳ DEPLOY |
| Follow-up Automation | n8n + marketingskills | n8n MCP | `/schedule` | ⏳ WIRE |
| Contract Generation | Stirling PDF (8080) | (PDF) | — | ✅ DEPLOYED |
| Forecasting | DuckDB + Claude | DuckDB | `/data-scientist` | ⏳ BUILD |
| Territory Management | Supabase | Supabase MCP | — | ⏳ BUILD |
| Revenue Attribution | Supabase + Stripe | Stripe MCP | `mcp__claude_ai_Stripe__*` | ⏳ BUILD |

---

## LAYER 9: Marketing OS (marketingskills + n8n + social APIs)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Campaign Management | n8n + marketingskills | n8n MCP | — | ⏳ WIRE |
| Content Calendar | Notion | Notion MCP | — | ✅ READY |
| Social Publishing | SocialClaw MCP (implied) | (implied) | `/social-publishing` | ⏳ DEPLOY |
| SEO Tracking | Claude + search tools | — | `/seo-specialist` | ⏳ BUILD |
| Email Marketing | n8n + Gmail | Gmail MCP | `mcp__claude_ai_Gmail__*` | ⏳ WIRE |
| Attribution | DuckDB + Stripe | Stripe MCP | `/data-scientist` | ⏳ BUILD |
| A/B Testing | Claude + Supabase | Supabase MCP | — | ⏳ BUILD |
| Brand Monitoring | Web scrapers + Claude | — | `/search-specialist` | ⏳ BUILD |

---

## LAYER 10: Product OS (GitHub + Supabase + NocoDB)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Roadmaps | Notion / GitHub | Notion MCP, GitHub MCP | — | ✅ READY |
| Backlogs | GitHub Issues | GitHub MCP | `mcp__plugin_everything-claude-code_github__*` | ✅ LIVE |
| User Research | Supabase | Supabase MCP | — | ⏳ BUILD |
| Feature Flags | Supabase | Supabase MCP | — | ⏳ BUILD |
| Experiments | Claude + Supabase | Supabase MCP | `/design-agent` | ⏳ BUILD |
| Product Analytics | DuckDB + Grafana | DuckDB, Grafana MCP | — | ⏳ WIRE |
| User Feedback | Supabase + Slack | Supabase MCP, Slack MCP | — | ⏳ WIRE |
| Release Management | GitHub | GitHub MCP | `/deploy-with-verification` | ✅ READY |

---

## LAYER 11: Engineering OS (GitHub + CI/CD + Code Analysis)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Repository Registry | REPOSITORY-REGISTRY.json (1,639 repos) | GitHub MCP | `/socraticode:codebase-management` | ✅ LIVE |
| CI/CD | GitHub Actions | GitHub MCP | (implicit) | ✅ READY |
| Testing | pytest + GitHub | GitHub MCP | `/tdd-workflow` | ✅ READY |
| Security Scanning | GitHub Security | GitHub MCP | `/security-scan` | ✅ READY |
| Architecture Docs | Markdown + Mermaid | — | `/architecture-decision-records` | ✅ READY |
| Dependency Mapping | Graphify + SocratiCode | `socraticode` MCP | `/socraticode:codebase-graph` | ✅ LIVE |
| Code Review | Claude Code reviewer | — | `/code-review` | ✅ LIVE |
| Deployments | n8n + GitHub | GitHub MCP, n8n MCP | `/deploy-with-verification` | ✅ READY |

---

## LAYER 12: Financial OS (Stripe + DuckDB + Supabase)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Budgeting | Supabase | Supabase MCP | `/business-analyst` | ⏳ BUILD |
| Forecasting | Claude + DuckDB | DuckDB | `/data-scientist` | ⏳ BUILD |
| Cash Flow | Supabase + DuckDB | Supabase MCP | `/quant-analyst` | ⏳ BUILD |
| AP/AR | Stirling PDF + Supabase | (PDF) | — | ⏳ WIRE |
| Grants/Loans | Manual (Google Sheets) | Google Sheets MCP | `/finance-tracker` | ⏳ BUILD |
| Venture Funding | Supabase + Stripe | Supabase MCP, Stripe MCP | `/quant-analyst` | ⏳ BUILD |
| Unit Economics | DuckDB + Claude | DuckDB | `/business-analyst` | ⏳ BUILD |
| Financial Reporting | DuckDB + Grafana | DuckDB, Grafana MCP | — | ⏳ BUILD |

---

## LAYER 13: HR / Talent OS (Twenty CRM + Supabase + Google Sheets)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Recruiting | Twenty (3002) | — | `/sales-automator` (adapted) | ⏳ WIRE |
| Onboarding | Notion | Notion MCP | — | ⏳ BUILD |
| Learning | Courses (EDU ventures) | — | `/superpowers:continuous-learning` | ⏳ ACTIVATE |
| Skills Matrix | Supabase | Supabase MCP | — | ⏳ BUILD |
| Performance Reviews | Notion / Supabase | Notion MCP, Supabase MCP | — | ⏳ BUILD |
| Compensation | DuckDB + Supabase | Supabase MCP | — | ⏳ BUILD |
| Succession Planning | Neo4j + Claude | Neo4j MCP | — | ⏳ BUILD |

---

## LAYER 14: Infrastructure OS (Docker + Tailscale + Kubernetes)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Servers | Mac Studio + MacBook Air | — | — | ✅ LIVE (Tailscale 100.87.214.70) |
| Container Orchestration | Docker | Docker Hub MCP | — | ✅ LIVE (15 containers) |
| Storage | T7 Shield (2TB) | — | — | ✅ LIVE (754GB used) |
| Secrets | Infisical (8091) | — | `mcp__socraticode_socraticode__*` (implied) | ✅ LIVE |
| Networking | Tailscale VPN | — | — | ✅ LIVE |
| Backups | Cloud storage | — | — | ⏳ BUILD (daily automated) |
| Monitoring | Prometheus (9090) | Prometheus MCP | — | ⏳ WIRE (only self) |
| Disaster Recovery | Supabase auto-backups | Supabase MCP | — | ✅ READY |

---

## LAYER 15: Security OS (Tailscale + Infisical + GitHub)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Identity Management | Tailscale | — | — | ✅ LIVE |
| RBAC | GitHub + Supabase | Supabase MCP | `/architecture-decision-records` | ⏳ IMPLEMENT |
| Audit Logs | Supabase | Supabase MCP | — | ⏳ WIRE (audit_logs table ready) |
| Vulnerability Scanning | GitHub Security | GitHub MCP | `/security-scan` | ✅ LIVE |
| Threat Detection | Claude + logs | — | `/threat-modeling-expert` | ⏳ BUILD |
| Secrets Management | Infisical (8091) | — | — | ✅ LIVE |
| Policy Enforcement | DECISION-FRAMEWORK.md | — | `/architecture-decision-records` | ⏳ BUILD |

---

## LAYER 16: Learning & Continuous Improvement (Obsidian + n8n + Supabase)

| Component | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Retrospectives | Obsidian notes | Obsidian MCP | `/obsidian-second-brain` | ⏳ BUILD (playbook) |
| Experiment Tracking | Supabase | Supabase MCP | — | ⏳ BUILD (experiments table) |
| Best Practices | Obsidian + OPCO charters | Obsidian MCP | `/obsidian-second-brain` | ✅ STARTING |
| Playbook Evolution | GitHub + Obsidian | GitHub MCP, Obsidian MCP | — | ⏳ BUILD (workflow) |
| Skills Development | EDU ventures | — | `/superpowers:continuous-learning` | ⏳ WIRE |
| Lesson Preservation | Obsidian vault | Obsidian MCP | `/obsidian-second-brain` | ⏳ BUILD (template) |

---

## CROSS-SYSTEM CAPABILITIES (All 16 Layers Use These)

| Capability | Tool | MCP | Slash Command | Status |
|-----------|------|-----|---|--------|
| Search | Qdrant (vectors) + Neo4j (graph) | Qdrant MCP, Neo4j MCP | `/socraticode:codebase-search` | ✅ LIVE |
| AI Assistant | Claude API | — | All `/prompt-*`, `/plan`, `/orchestrate` | ✅ LIVE |
| Memory | Memory MCP + Obsidian | Memory MCP, Obsidian MCP | `mcp__plugin_everything-claude-code_memory__*` | ✅ LIVE |
| Notifications | Slack + Grafana alerts | Slack MCP | `/slack_send_message` | ✅ READY |
| Integrations | n8n + 17 MCPs | MCP_REGISTRY.json (17 MCPs) | `/orchestrate` | ✅ LIVE (14 enabled) |
| Permissions | Supabase RLS + GitHub | Supabase MCP, GitHub MCP | `/architecture-decision-records` | ⏳ IMPLEMENT |
| Audit Trail | Supabase audit_logs + Langfuse | Supabase MCP, Langfuse | — | ⏳ WIRE (table exists, not populated) |
| Analytics | DuckDB + Grafana | DuckDB, Grafana MCP | (Grafana dashboards) | ⏳ BUILD/WIRE |
| Automation | n8n + Hermes agents | n8n MCP, (agents) | `/orchestrate`, `/schedule` | ✅ READY (15 containers, 14 agents) |
| APIs | RESTful + GraphQL (implied) | GitHub MCP, Supabase MCP | `/api-design` | ⏳ DOCUMENT |

---

## SUMMARY: Layer Completion Status

| Layer | Name | Status | Critical Path |
|-------|------|--------|---|
| 1 | Identity & Governance | 🟢 60% | Complete DECISION-FRAMEWORK.md |
| 2 | Knowledge Brain | 🟢 70% | Seed Neo4j + index docs |
| 3 | Agent Platform | 🟢 60% | Deploy Hermes + CrewAI |
| 4 | Workflow Engine | 🟢 70% | Wire n8n approval flows |
| 5 | Decision Engine | 🟠 30% | Build Hermes reasoning loops |
| 6 | Operational Intelligence | 🟠 40% | Wire Prometheus + Grafana |
| 7 | Customer Intelligence | 🔴 20% | Build customer 360 view |
| 8 | Sales OS | 🟢 60% | Deploy ventures + wire Stripe |
| 9 | Marketing OS | 🔴 20% | Wire marketingskills + n8n |
| 10 | Product OS | 🟢 60% | Wire experiments + analytics |
| 11 | Engineering OS | 🟢 80% | Already have most pieces |
| 12 | Financial OS | 🔴 10% | Build forecasting engine |
| 13 | HR / Talent OS | 🔴 15% | Implement recruiting + onboarding |
| 14 | Infrastructure OS | 🟢 80% | Improve backups + monitoring |
| 15 | Security OS | 🟢 60% | Implement RBAC + policies |
| 16 | Learning | 🠋 50% | Build retrospective system |

**TOTAL COMPLETION:** ~50% (8/16 layers at 50%+)

**CRITICAL PATH:** Layers 2 → 3 → 4 → 8 (Knowledge → Agents → Workflows → Revenue)

