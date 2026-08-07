---
name: strategic-directives
description: VEX strategic directives graph — company policy, roadmap, constraints
metadata:
  type: reference
  version: 1.0
  status: active
  last_updated: 2026-08-07
---

# Strategic Directives & Policy Graph

## DIRECTIVE

```yaml
DIRECTIVE
  ├── APPLIES_TO → VENTURE|SECTOR (scope)
  ├── REQUIRES → CAPABILITY (what's needed)
  ├── BLOCKS_UNTIL → DATE (deadline)
  ├── APPROVED_BY → EXECUTIVE (authority)
  ├── MEASURED_BY → KPI (success metric)
  ├── PRIORITY → (critical|high|medium|low)
  ├── STATUS → (active|paused|completed|archived)
  └── ENFORCEMENT → AUTOMATIC|MANUAL|AUDIT
```

Properties: `id`, `title`, `description`, `type` (policy|roadmap|constraint|requirement), `priority`, `created_at`, `expires_at`, `enforcement_mode`

## POLICY

```yaml
POLICY
  ├── DEFINES → CONSTRAINT
  ├── APPLIES_TO → ROLE
  ├── BLOCKS_ACTION → ACTION_TYPE
  ├── REQUIRES_APPROVAL → APPROVAL_GATE
  ├── PENALTY_FOR_VIOLATION → CONSEQUENCE
  └── REVIEWED_BY → EXECUTIVE
```

Properties: `id`, `name`, `category` (compliance|security|financial|operational), `severity`, `last_reviewed`, `next_review`

## ROADMAP

```yaml
ROADMAP
  ├── APPLIES_TO → SECTOR|VENTURE
  ├── DEFINES_PHASE → PHASE (ordered)
  ├── REQUIRES_CAPABILITY → CAPABILITY
  ├── TARGETS_KPI → KPI
  ├── DEADLINE → DATE
  ├── APPROVED_BY → EXECUTIVE
  └── DEPENDS_ON → ROADMAP (transitive)
```

Properties: `id`, `name`, `fiscal_quarter`, `status`, `completion_percent`, `created_at`

## PHASE

```yaml
PHASE
  ├── PART_OF → ROADMAP
  ├── SEQUENCE → NUMBER
  ├── REQUIRES → CAPABILITY
  ├── DEPENDS_ON → PHASE (previous phase)
  ├── TARGET_DATE → DATE
  ├── SUCCESS_CRITERIA → METRIC[]
  └── RESPONSIBLE_PARTY → EXECUTIVE|TEAM
```

Properties: `id`, `name`, `status`, `start_date`, `end_date`, `percent_complete`

## CONSTRAINT

```yaml
CONSTRAINT
  ├── DEFINED_BY → POLICY|DIRECTIVE
  ├── APPLIES_TO → ENTITY_TYPE
  ├── BLOCKS_ACTION → ACTION_TYPE
  ├── THRESHOLD → VALUE
  ├── ESCALATES_IF_VIOLATED → APPROVAL_GATE
  └── ENFORCED_BY → SYSTEM|HUMAN
```

Properties: `id`, `name`, `type` (financial|technical|legal|business), `limit_value`, `unit`, `enforcement`

## Decision Tree: Directive → Venture

```
DIRECTIVE
  ├── PRIORITY: critical
  ├── APPLIES_TO: Sector (Construction)
  ├── REQUIRES: Stripe Payment Integration
  ├── DEADLINE: 2026-09-30
  └── MEASURED_BY: Revenue Processing Success Rate > 99%

                 ↓
            
VENTURE (CON-001)
  ├── REQUIRES: Stripe Payment Integration (inherited)
  ├── DEADLINE: 2026-09-30 (inherited)
  ├── BLOCKED_BY: Missing Stripe Account Setup
  └── STATUS: In Progress

                 ↓
            
CAPABILITY (Payment Processing)
  ├── IMPLEMENTS: Directive requirement
  ├── DEPENDS_ON: Stripe API Integration
  ├── VERIFIED: False
  └── PRIORITY: critical

                 ↓
            
BLOCKER (Stripe Account Not Configured)
  ├── AFFECTS: Payment Processing capability
  ├── ESTIMATED_IMPACT: $50K revenue lost if missed
  ├── REQUIRES_DECISION: Approve budget for setup
  └── SEVERITY: critical
```

## Priority Levels

| Priority | Action | Response Time | Escalation |
|----------|--------|----------------|------------|
| critical | Implement immediately | 24 hours | CEO approval required |
| high | Complete within 2 weeks | 1 week | Director approval |
| medium | Complete within 1 quarter | 1 month | Manager approval |
| low | Backlog | ad-hoc | No approval needed |

## Temporal Properties

Every directive includes:
- `issued_date` (when directive became effective)
- `expires_at` (when directive expires; NULL = permanent)
- `last_reviewed_at` (when last audited)
- `review_interval_days` (frequency of review)
