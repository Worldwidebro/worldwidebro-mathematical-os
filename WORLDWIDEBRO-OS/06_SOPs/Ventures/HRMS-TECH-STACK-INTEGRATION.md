# HRMS Payroll SaaS - Technical Stack Integration Plan

**Venture**: HRMS (Payroll SaaS)
**Target Launch**: Week 3 (2026-05-27)
**Current Date**: 2026-05-16
**Status**: Phase 1 - Unblock HRMS + High-Impact Sectors

## Chosen Stack (4 Repos + Supabase)

### 1. Thunderbolt (Authentication + Security)
- **Role**: Core security, JWT auth, session management, credential encryption
- **Capabilities**: api, authentication, dashboard, database, knowledge-graph, security
- **Integration**: Auth middleware, token validation, permission system
- **Priority**: P0 - blocks payroll system security
- **GitHub**: https://github.com/[thunderbolt-repo]

### 2. Stripe (Payment Processing)
- **Role**: Salary disbursement, payroll payment routing, reconciliation
- **Capabilities**: api, payment, security, monitoring
- **Integration**: Webhook handlers, payout scheduling, fraud detection
- **Priority**: P0 - blocks payroll execution
- **Status**: Third-party SaaS (requires API key integration)

### 3. Mission-Control (Workspace + Dashboard)
- **Role**: Team management UI, payroll dashboard, real-time monitoring
- **Capabilities**: api, authentication, dashboard, database, knowledge-graph, monitoring, pitch, security, workspace
- **Integration**: Workspace creation, employee directory sync, dashboard widgets
- **Priority**: P1 - blocks MVP UI
- **GitHub**: https://github.com/[mission-control-repo]

### 4. OpenSRE (Monitoring + Observability)
- **Role**: Production monitoring, uptime tracking, alert system
- **Capabilities**: api, authentication, construction, dashboard, database, knowledge-graph, monitoring, security, simulation, workspace
- **Integration**: Metrics collection, alert routing to Slack
- **Priority**: P1 - blocks production readiness
- **GitHub**: https://github.com/[opensre-repo]

### 5. Supabase (Database + Backend)
- **Role**: Persistent storage, auth provider, real-time sync, API layer
- **Tables Required**: 
  - ventures (already synced)
  - employees (new)
  - payrolls (new)
  - payouts (new)
  - audit_logs (new)
  - integrations (new)

## Integration Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    HRMS Frontend (UI)                    │
│              (Mission-Control Workspace)                │
└──────────────────┬──────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────┐
│              API Layer (Thunderbolt)                     │
│         Authentication • Authorization • Routing         │
└──────────┬──────────────────────────────┬────────────────┘
           │                              │
    ┌──────▼──────────┐          ┌────────▼──────────┐
    │   Supabase      │          │  Stripe Webhooks  │
    │   ├─ employees  │          │  ├─ payouts sent  │
    │   ├─ payrolls   │          │  ├─ failures      │
    │   ├─ payouts    │          │  └─ reconcile     │
    │   └─ audit_logs │          └───────────────────┘
    └──────┬──────────┘
           │
    ┌──────▼──────────────────────────┐
    │  Monitoring (OpenSRE)           │
    │  ├─ API latency                 │
    │  ├─ Payment failures            │
    │  ├─ Database health             │
    │  └─ Alert → Slack               │
    └────────────────────────────────┘
```

## Supabase Schema (New Tables for HRMS)

```sql
-- Employees table
CREATE TABLE employees (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL REFERENCES ventures(id),
  email TEXT NOT NULL UNIQUE,
  full_name TEXT NOT NULL,
  department TEXT,
  salary_base DECIMAL(12,2),
  salary_currency TEXT DEFAULT 'USD',
  pay_frequency TEXT DEFAULT 'monthly', -- monthly, bi-weekly, weekly
  bank_account_id TEXT, -- Stripe bank account ID
  status TEXT DEFAULT 'active', -- active, inactive, terminated
  employment_start_date DATE,
  employment_end_date DATE,
  metadata JSONB,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Payrolls table
CREATE TABLE payrolls (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL REFERENCES ventures(id),
  period_start DATE NOT NULL,
  period_end DATE NOT NULL,
  status TEXT DEFAULT 'draft', -- draft, approved, processing, completed, failed
  total_gross DECIMAL(12,2),
  total_deductions DECIMAL(12,2),
  total_net DECIMAL(12,2),
  payment_method TEXT DEFAULT 'stripe',
  metadata JSONB,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Payouts table
CREATE TABLE payouts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  payroll_id UUID NOT NULL REFERENCES payrolls(id),
  employee_id UUID NOT NULL REFERENCES employees(id),
  gross_amount DECIMAL(12,2) NOT NULL,
  deductions DECIMAL(12,2),
  net_amount DECIMAL(12,2) NOT NULL,
  stripe_payout_id TEXT,
  status TEXT DEFAULT 'pending', -- pending, processing, completed, failed
  stripe_status TEXT,
  error_message TEXT,
  attempted_at TIMESTAMP,
  completed_at TIMESTAMP,
  metadata JSONB,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Audit logs table
CREATE TABLE audit_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL REFERENCES ventures(id),
  action TEXT NOT NULL,
  user_id TEXT,
  resource_type TEXT,
  resource_id TEXT,
  changes JSONB,
  metadata JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Integrations table
CREATE TABLE integrations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL REFERENCES ventures(id),
  integration_type TEXT NOT NULL, -- stripe, slack, github, etc
  api_key_encrypted TEXT,
  config JSONB,
  status TEXT DEFAULT 'active',
  last_sync TIMESTAMP,
  error_count INT DEFAULT 0,
  last_error TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Enable RLS on all tables
ALTER TABLE employees ENABLE ROW LEVEL SECURITY;
ALTER TABLE payrolls ENABLE ROW LEVEL SECURITY;
ALTER TABLE payouts ENABLE ROW LEVEL SECURITY;
ALTER TABLE audit_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE integrations ENABLE ROW LEVEL SECURITY;

-- Create indexes for performance
CREATE INDEX idx_employees_venture ON employees(venture_id);
CREATE INDEX idx_employees_email ON employees(email);
CREATE INDEX idx_payrolls_venture ON payrolls(venture_id);
CREATE INDEX idx_payrolls_status ON payrolls(status);
CREATE INDEX idx_payouts_payroll ON payouts(payroll_id);
CREATE INDEX idx_payouts_status ON payouts(status);
CREATE INDEX idx_audit_logs_venture ON audit_logs(venture_id);
CREATE INDEX idx_integrations_venture ON integrations(venture_id);
```

## Integration Tasks (Week 1-2)

### Task 1: Deploy Supabase Schema
- [ ] Apply migrations to create 5 new tables
- [ ] Set up RLS policies for employee data isolation
- [ ] Create audit triggers for compliance
- [ ] Verify indexes for query performance

### Task 2: Thunderbolt Auth Integration
- [ ] Deploy Thunderbolt as auth middleware
- [ ] Configure JWT token generation
- [ ] Set up session management
- [ ] Create permission matrix (admin, manager, employee, finance)
- [ ] Integrate with Supabase auth

### Task 3: Mission-Control Workspace Setup
- [ ] Deploy Mission-Control instance
- [ ] Create HRMS workspace in MC
- [ ] Connect Supabase datasource
- [ ] Build dashboard widgets:
  - [ ] Current payroll status
  - [ ] Employee roster
  - [ ] Pending payouts
  - [ ] Recent audit log
- [ ] Add real-time sync via Supabase subscriptions

### Task 4: Stripe Payment Integration
- [ ] Register Stripe account
- [ ] Create webhook endpoints:
  - [ ] `/webhooks/stripe/payout_completed`
  - [ ] `/webhooks/stripe/payout_failed`
  - [ ] `/webhooks/stripe/payout_reversed`
- [ ] Build payout scheduler (cron-based or edge function)
- [ ] Implement retry logic for failed payouts
- [ ] Create reconciliation report

### Task 5: OpenSRE Monitoring
- [ ] Deploy OpenSRE for HRMS cluster
- [ ] Create dashboards for:
  - [ ] API response times (target <100ms)
  - [ ] Payout success rate (target 99.9%)
  - [ ] Database connection pool health
  - [ ] Payment processing latency
- [ ] Set up alerts:
  - [ ] Payout failure rate > 5%
  - [ ] API error rate > 1%
  - [ ] Database CPU > 80%
- [ ] Route critical alerts to Slack #hrms-alerts

### Task 6: Slack Integration
- [ ] Connect Supabase to Slack via webhooks
- [ ] Post payroll status updates to #hrms
- [ ] Post critical alerts to #hrms-alerts
- [ ] Enable bi-directional sync (Slack → Supabase for approvals)

## Success Criteria

**Week 1 Milestones (by 2026-05-23)**
- [ ] Supabase schema deployed and tested
- [ ] Thunderbolt auth working (login/logout)
- [ ] Mission-Control dashboard displaying test data
- [ ] Stripe webhooks receiving events

**Week 2 Milestones (by 2026-05-27)**
- [ ] End-to-end payroll flow working (employee → payroll → payout)
- [ ] Payment success rate >95% on test data
- [ ] OpenSRE alerts firing correctly
- [ ] Audit logs capturing all actions
- [ ] Manual payroll processing tested with 10 test employees

**Week 3 Launch (by 2026-06-02)**
- [ ] Production Stripe account activated
- [ ] All 4 repos in production
- [ ] Load test at 100 concurrent users
- [ ] Security audit passed (Thunderbolt)
- [ ] Compliance audit passed (audit logs)

## Deployment Timeline

| Week | Task | Owner | Status |
|------|------|-------|--------|
| W1 (5/16-5/23) | Supabase Schema + Auth | Backend | Not Started |
| W1 (5/16-5/23) | Mission-Control Setup | Frontend | Not Started |
| W1 (5/16-5/23) | Stripe Webhooks | Payments | Not Started |
| W2 (5/23-5/27) | Integration Testing | QA | Not Started |
| W2 (5/23-5/27) | OpenSRE Monitoring | DevOps | Not Started |
| W3 (5/27-6/02) | Production Launch | All | Not Started |

## Rollback Plan

If any component fails:
1. **Thunderbolt down** → Fall back to Supabase built-in auth (1 hour to switch)
2. **Stripe down** → Queue payouts in Supabase, retry when Stripe recovers
3. **Mission-Control down** → Use direct Supabase API (CLI commands for payroll)
4. **OpenSRE down** → Manual monitoring via Supabase dashboard (24 hours acceptable)

## Next Steps

1. ✅ Architecture approved
2. ⏳ Create integration code for Thunderbolt auth
3. ⏳ Deploy Supabase migrations
4. ⏳ Build Mission-Control HRMS workspace
5. ⏳ Set up Stripe webhook handlers
6. ⏳ Configure OpenSRE dashboards
