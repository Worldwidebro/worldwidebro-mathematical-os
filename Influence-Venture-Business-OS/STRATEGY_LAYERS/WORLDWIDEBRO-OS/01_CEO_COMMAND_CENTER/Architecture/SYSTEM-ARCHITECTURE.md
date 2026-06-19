# 🧠 End-to-End System Architecture

**Capture → Process → Decide → Execute → Measure → Learn**

---

## System Flow

```
Input Sources          Processing           Execution             Measurement          Learning
───────────────        ──────────────       ───────────           ──────────────       ────────
Chat                   Workflows            N8n Agents            Analytics            Knowledge
Email                  Tasks                AI Decisions          KPIs                 Graph
API                    Knowledge Graph      CRM Actions           Dashboards           Feedback
Forms                  ↓                    Finance Ops           Results              Lessons
Scraping               Decision Rules       Tool Executions       Metrics              Learned
```

---

## 25-50 Core Tables by Layer

### 1️⃣ Identity & Access (3 tables)

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| **Users** | Authentication + authorization | user_id, name, email, role, team_id, permissions, status |
| **Teams** | Organizational units | team_id, name, manager_id, created_at |
| **Permissions** | Role-based access control | permission_id, role, resource, access_level |

---

### 2️⃣ Input Layer (1 table)

Everything entering the system from external sources.

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| **Requests** | Unified input from all sources | request_id, source (chat/email/api/form/scraped), type, content, priority, user_id, created_at, status |

---

### 3️⃣ Workflow Engine (2 tables)

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| **Workflows** | Workflow definitions | workflow_id, name, category, trigger_type, owner_id, status, created_at |
| **WorkflowSteps** | Step sequencing | step_id, workflow_id, step_name, sequence, action_type, config, created_at |

---

### 4️⃣ Task Management (1 table)

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| **Tasks** | Work items spawned by workflows or requests | task_id, request_id, workflow_id, assigned_to, due_date, status, priority, created_at |

---

### 5️⃣ AI / Agent Layer (2 tables)

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| **Agents** | AI agent definitions | agent_id, name, role, capabilities (JSON), tools (JSON), status, model |
| **AgentExecutions** | Actual agent runs | execution_id, agent_id, input, output, duration_ms, result_status, created_at |

---

### 6️⃣ Tools & Integrations (2 tables)

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| **Tools** | Available integrations (N8n nodes, APIs, etc.) | tool_id, name, category, api_endpoint, auth_type, status |
| **Integrations** | Active connections | integration_id, tool_id, team_id, auth_token, connection_status, last_tested |

---

### 7️⃣ Execution & Results (2 tables) ⭐ CRITICAL FOR N8N

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| **Executions** | N8n workflow runs | execution_id, workflow_id, n8n_execution_id, started_at, completed_at, status, duration_ms |
| **Results** | Execution outcomes | result_id, execution_id, output (JSON), errors (JSON), metrics (JSON), created_at |

---

### 8️⃣ CRM / Sales Layer (3 tables)

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| **Leads** | Prospects | lead_id, source, name, email, score, status, estimated_value, created_at |
| **Customers** | Active customers | customer_id, name, email, segment, lifetime_value, created_at |
| **Interactions** | All customer touchpoints | interaction_id, customer_id, type (call/email/meeting), notes, timestamp |

---

### 9️⃣ Finance Layer (3 tables)

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| **Transactions** | All financial movements | transaction_id, amount, category, date, status, description |
| **Budgets** | Spending plans | budget_id, department, allocated, spent, remaining, period |
| **Forecasts** | Predictions vs. actuals | forecast_id, metric, predicted, actual, variance, period |

---

### 🔟 Analytics & Dashboards (2 tables)

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| **KPIs** | Key performance indicators | kpi_id, name, target, actual, status, measurement_date |
| **Dashboards** | Visualization configs | dashboard_id, name, owner_id, widgets (JSON), last_updated |

---

### 1️⃣1️⃣ Knowledge Graph (3 tables) ⭐ ALREADY BUILT

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| **Entities** | Semantic units | entity_id, name, entity_type, attributes (JSON), created_at |
| **Relationships** | Entity connections | relationship_id, source_entity_id, relationship_type, target_entity_id, weight, created_at |
| **Facts** | Extracted statements | fact_id, entity_id, statement, confidence_score, source, created_at |

---

### 1️⃣2️⃣ Memory & Documentation (3 tables)

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| **Documents** | Knowledge base | document_id, title, category, content, owner_id, location, created_at |
| **SOPs** | Standard operating procedures | sop_id, title, owner_id, version, steps (JSON), last_updated |
| **Templates** | Reusable patterns | template_id, type, description, content (JSON), category |

---

### 1️⃣3️⃣ Feedback & Learning (3 tables)

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| **Experiments** | A/B tests + hypotheses | experiment_id, hypothesis, result, metric_improvement, created_at |
| **Feedback** | User ratings + comments | feedback_id, source (user/system), rating (1-5), comments, created_at |
| **LessonsLearned** | Insights from results | lesson_id, description, impact, application, created_at |

---

## Domain-Specific Layers (Per Venture)

Each venture adds specialized modules:

### HRMS (Payroll SaaS)
- **Employees** (id, venture_id, name, salary, status)
- **Payroll** (id, employee_id, period, gross, net, deductions)
- **TimeTracking** (id, employee_id, hours, date)

### Logistics
- **Shipments** (id, venture_id, origin, destination, status)
- **Routes** (id, shipment_id, waypoint, estimated_time)

### Real Estate
- **Properties** (id, venture_id, address, value, status)
- **Leases** (id, property_id, tenant_id, terms)

---

## Critical Path: N8n Integration

To make N8n operational within this system:

```
1. User creates Request (chat/email/API)
   ↓
2. System detects trigger → creates Task
   ↓
3. N8n Workflow fires (via webhook)
   ↓
4. Execution record created in Executions table
   ↓
5. N8n workflow completes → writes to Results table
   ↓
6. Results analyzed → KPI updated
   ↓
7. Lessons Learned → improves next execution
```

**Tables needed first:**
- ✅ Workflows (schema + seed data from N8n)
- ✅ Executions (logs N8n runs)
- ✅ Results (captures outputs)
- ✅ Requests (triggers workflows)
- ✅ Tasks (work items)

**Then layer on:**
- Analytics (KPIs measure impact)
- Knowledge Graph (entities from results)
- Feedback (users rate outputs)

---

## Current State vs. Needed

| Layer | Status | Tables | Action |
|-------|--------|--------|--------|
| Identity | ❌ Missing | Users, Teams, Permissions | Build |
| Input | ❌ Missing | Requests | Build |
| Workflows | ⚠️ Partial | Workflows, WorkflowSteps | Connect N8n |
| Tasks | ❌ Missing | Tasks | Build |
| Agents | ❌ Missing | Agents, AgentExecutions | Build |
| Tools | ❌ Missing | Tools, Integrations | Build |
| **Executions** | ⚠️ Partial | **Executions, Results** | **Build + N8n hook** |
| CRM | ✅ Exists | Leads, Customers, Interactions | Already integrated |
| Finance | ❌ Missing | Transactions, Budgets, Forecasts | Build |
| Analytics | ❌ Missing | KPIs, Dashboards | Build |
| Knowledge Graph | ✅ Live | Entities, Relationships, Facts | Already operational |
| Memory | ❌ Missing | Documents, SOPs, Templates | Build |
| Feedback | ❌ Missing | Experiments, Feedback, LessonsLearned | Build |

---

## Schema Generation SQL

```sql
-- Critical path first (N8n integration)

CREATE TABLE workflows (
  workflow_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  category TEXT,
  trigger_type TEXT,
  owner_id UUID,
  status TEXT DEFAULT 'draft',
  n8n_workflow_id TEXT,
  config JSONB,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

CREATE TABLE executions (
  execution_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  workflow_id UUID REFERENCES workflows(workflow_id),
  n8n_execution_id TEXT,
  input JSONB,
  started_at TIMESTAMP DEFAULT now(),
  completed_at TIMESTAMP,
  status TEXT DEFAULT 'pending',
  duration_ms INTEGER,
  created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE results (
  result_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  execution_id UUID REFERENCES executions(execution_id),
  output JSONB,
  errors JSONB,
  metrics JSONB,
  status TEXT DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE requests (
  request_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  source TEXT NOT NULL,
  type TEXT,
  content TEXT,
  priority TEXT DEFAULT 'normal',
  user_id UUID,
  status TEXT DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE tasks (
  task_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  request_id UUID REFERENCES requests(request_id),
  workflow_id UUID REFERENCES workflows(workflow_id),
  assigned_to UUID,
  due_date DATE,
  status TEXT DEFAULT 'pending',
  priority TEXT DEFAULT 'normal',
  created_at TIMESTAMP DEFAULT now()
);
```

---

## Next Steps

1. **Build critical tables** (Workflows, Executions, Results, Requests, Tasks)
2. **Connect N8n** (webhooks fire on execution completion)
3. **Test end-to-end** (Request → Workflow → Execution → Result)
4. **Add Analytics** (KPIs measure outcomes)
5. **Layer Feedback** (close the learning loop)

---

**Goal**: Transform N8n from isolated workflows into a complete operating system.
