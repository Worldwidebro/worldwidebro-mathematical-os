---
name: executive-roles
description: VEX executive authority graph — roles, approval gates, escalation chains
metadata:
  type: reference
  version: 1.0
  status: active
  last_updated: 2026-08-07
---

# Executive Roles & Authority Graph

## EXECUTIVE

```yaml
EXECUTIVE
  ├── HAS_ROLE → ROLE
  ├── OVERSEES → VENTURE|SECTOR
  ├── APPROVES → DECISION (approval gate)
  ├── CAN_ESCALATE_TO → EXECUTIVE (next level)
  ├── HAS_AUTHORITY_LEVEL → LEVEL (1-5)
  ├── MANAGES → TEAM
  ├── REPORTS_TO → EXECUTIVE
  └── AVAILABLE_HOURS → NUMBER
```

Properties: `id`, `name`, `email`, `role`, `authority_level` (1=observer, 2=contributor, 3=decision-maker, 4=director, 5=ceo), `active`, `start_date`, `end_date`

## ROLE

```yaml
ROLE
  ├── HAS_RESPONSIBILITY → DOMAIN
  ├── REQUIRES_APPROVAL_FROM → APPROVAL_GATE
  ├── CAN_ACCESS_TOOL → TOOL
  ├── CAN_MODIFY_ENTITY → ENTITY_TYPE
  ├── DELEGATES_TO → ROLE
  └── ESCALATES_TO → ROLE
```

Properties: `id`, `name`, `type` (executive|manager|engineer|operator), `description`, `authority_level`

## APPROVAL_GATE

```yaml
APPROVAL_GATE
  ├── REQUIRES_ROLE → ROLE
  ├── REQUIRES_SIGNATURE → EXECUTIVE
  ├── TIMEOUT → DURATION (hours)
  ├── ESCALATES_TO → EXECUTIVE (if timeout)
  ├── APPLIED_TO → DECISION_TYPE
  └── DECISION_LOG → EVENT[]
```

Properties: `id`, `name`, `required_role`, `timeout_hours`, `status`, `created_at`

## DECISION

```yaml
DECISION
  ├── MADE_BY → EXECUTIVE
  ├── AFFECTS → VENTURE|CAPABILITY
  ├── REQUIRES_APPROVAL → APPROVAL_GATE
  ├── BASED_ON → EVIDENCE
  ├── PRODUCES_ACTION → ACTION
  ├── IMPACTS_KPI → KPI
  ├── STATUS → (pending|approved|rejected|escalated)
  └── CONFIDENCE → SCORE (0-1)
```

Properties: `id`, `title`, `description`, `decision_type`, `made_at`, `approved_at`, `confidence_score`, `rationale`

## Authority Levels

| Level | Role | Authority | Approval Power |
|-------|------|-----------|-----------------|
| 1 | Observer | Read-only | None |
| 2 | Contributor | Propose decisions | None, proposes to Level 3+ |
| 3 | Decision Maker | Approve/reject up to $X | Can approve own decisions |
| 4 | Director | Approve up to $Y, override Level 3 | Can escalate to Level 5 |
| 5 | CEO | Unlimited authority | Final approval |

## Escalation Chains

**Financial Decision** (amount > threshold):
```
Level 3 Contributor
  ↓ (escalates if amount > $10K)
Level 4 Director
  ↓ (escalates if amount > $100K)
Level 5 CEO
```

**Technical Decision** (affects infrastructure):
```
Engineer (Level 2)
  ↓ (escalates if breaking change)
Tech Lead (Level 3)
  ↓ (escalates if downtime risk)
CTO (Level 4)
  ↓ (escalates if mission-critical)
CEO (Level 5)
```

**Venture Launch Decision**:
```
Venture Owner (Level 2-3)
  ↓ (requires approval)
Sector Director (Level 4)
  ↓ (requires sign-off)
CFO (Level 4)
  ↓ (final approval)
CEO (Level 5)
```

## Temporal Properties

Every role assignment includes:
- `valid_from` (timestamp role became active)
- `valid_to` (timestamp role ended; NULL = current)
- `authority_granted_by` (which executive granted this)
- `authority_expires_at` (when to renew)
