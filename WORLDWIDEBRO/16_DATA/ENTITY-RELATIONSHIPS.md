---
name: entity-relationships
description: VEX graph backbone — all entity types and their relationships
metadata:
  type: reference
  version: 1.0
  status: active
  last_updated: 2026-08-07
---

# VEX Entity Relationships
**The graph backbone — all other layers hang off this.**

## VENTURE

```yaml
VENTURE
  ├── BELONGS_TO → SECTOR
  ├── OPERATED_BY → OPCO
  ├── IMPLEMENTS → CAPABILITY
  ├── REQUIRES → TECHNOLOGY
  ├── DEPENDS_ON → VENTURE (transitive)
  ├── MEASURED_BY → KPI
  ├── HAS_RISK → RISK
  ├── BLOCKED_BY → BLOCKER
  ├── REQUIRES_APPROVAL → APPROVAL_GATE
  └── GENERATES → REVENUE
```

Properties: `id`, `name`, `status` (active|blocked|completed), `readiness_score`, `last_audit`, `created_at`, `updated_at`

## CAPABILITY

```yaml
CAPABILITY
  ├── IMPLEMENTED_BY → REPOSITORY
  ├── PROVIDED_BY → AGENT
  ├── REQUIRES_SKILL → SKILL
  ├── DEPENDS_ON → CAPABILITY
  ├── ENABLES → WORKFLOW
  └── MEASURED_BY → KPI
```

Properties: `id`, `name`, `type`, `maturity_level`, `verified`, `last_verified_at`

## REPOSITORY

```yaml
REPOSITORY
  ├── BELONGS_TO → SECTOR
  ├── CONTAINS → CODE
  ├── IMPLEMENTS → CAPABILITY
  ├── DEPENDS_ON → PACKAGE
  ├── HAS_AUTHOR → PERSON
  ├── HAS_MAINTAINER → PERSON
  ├── HAS_API → API_ENDPOINT
  ├── EXPOSES → TOOL
  ├── REQUIRES_SKILL → SKILL
  ├── IS_ALIVE → BOOLEAN
  └── HAS_RISK → SECURITY_RISK
```

Properties: `github_url` (UNIQUE), `name`, `language`, `last_commit`, `stars`, `is_alive`, `vulnerability_count`

## AGENT

```yaml
AGENT
  ├── HAS_ROLE → ROLE
  ├── IMPLEMENTS_WORKFLOW → WORKFLOW
  ├── CAN_ACCESS_TOOL → TOOL
  ├── REQUIRES_PERMISSION → PERMISSION
  ├── EXECUTES_TASK → TASK
  ├── PRODUCES_EVENT → EVENT
  ├── READS_FROM → DATA_SOURCE
  ├── WRITES_TO → DATA_SINK
  ├── QUERIES → KNOWLEDGE_GRAPH
  ├── RETRIEVES_FROM → VECTOR_INDEX
  └── LEARNS_FROM → FEEDBACK
```

Properties: `id`, `name`, `type`, `status`, `last_execution`, `error_count`

## WORKFLOW

```yaml
WORKFLOW
  ├── TRIGGERED_BY → EVENT
  ├── SCHEDULED_BY → TRIGGER
  ├── EXECUTES_STEP → TASK (ordered)
  ├── ROUTES_TO → AGENT
  ├── DEPENDS_ON → WORKFLOW
  ├── USES_TOOL → TOOL
  ├── READS → DATA
  ├── WRITES → DATA
  ├── EMITS → EVENT
  ├── MEASURES → KPI
  └── BLOCKS_ON → APPROVAL
```

Properties: `id`, `name`, `status`, `last_run`, `success_rate`, `avg_duration_ms`

## BLOCKER

```yaml
BLOCKER
  ├── AFFECTS_VENTURE → VENTURE
  ├── BLOCKED_BY → CAPABILITY (missing)
  ├── BLOCKED_BY → PERSON (approval)
  ├── BLOCKED_BY → RISK (security/business)
  ├── REQUIRES_DECISION → DECISION
  └── ESTIMATED_IMPACT → REVENUE_LOSS
```

Properties: `id`, `title`, `severity` (critical|high|medium|low), `created_at`, `resolved_at`, `impact_usd`

## SKILL

```yaml
SKILL
  ├── SOLVES_PROBLEM → PROBLEM
  ├── REQUIRED_FOR → CAPABILITY
  ├── TAUGHT_IN → COURSE
  ├── PRACTICED_IN → VENTURE
  └── MEASURED_BY → COMPETENCY_SCORE
```

Properties: `id`, `name`, `category`, `proficiency_required`, `last_practiced`

## TECHNOLOGY

```yaml
TECHNOLOGY
  ├── USED_IN → REPOSITORY
  ├── ENABLES → CAPABILITY
  ├── BLOCKS → CAPABILITY
  ├── REQUIRES_SKILL → SKILL
  ├── HAS_VERSION → VERSION
  ├── HAS_VULNERABILITY → CVE
  └── REPLACES → TECHNOLOGY (deprecated)
```

Properties: `id`, `name`, `category`, `current_version`, `eol_date`, `is_deprecated`

## EVENT

```yaml
EVENT
  ├── CREATED_BY → AGENT
  ├── TRIGGERED_BY → TRIGGER
  ├── CAUSED_BY → ACTION
  ├── AFFECTS → ENTITY (polymorphic)
  ├── PRODUCES_FEEDBACK → FEEDBACK
  ├── VALID_FROM → TIMESTAMP
  ├── VALID_TO → TIMESTAMP
  └── EVIDENCED_BY → TRACE_ID
```

Properties: `id`, `type`, `created_at`, `payload` (JSON), `trace_id`

## DECISION

```yaml
DECISION
  ├── MADE_BY → AGENT
  ├── AFFECTS → VENTURE
  ├── REQUIRES_APPROVAL → APPROVAL_GATE
  ├── BASED_ON → EVIDENCE
  ├── PRODUCES_ACTION → ACTION
  ├── IMPACTS_KPI → KPI
  └── CONFIDENCE → SCORE (0-1)
```

Properties: `id`, `title`, `confidence_score`, `made_at`, `approved_at`, `status`

## APPROVAL_GATE

```yaml
APPROVAL_GATE
  ├── REQUIRES_ROLE → ROLE
  ├── REQUIRES_SIGNATURE → PERSON
  ├── TIMEOUT → DURATION
  ├── ESCALATES_TO → ROLE
  └── DECISION_LOG → EVENT[]
```

Properties: `id`, `name`, `required_role`, `timeout_hours`, `status`

---

## Temporal Properties (All Entities)

Every relationship edge should include:
- `valid_from` (timestamp entity became true)
- `valid_to` (timestamp entity ended; NULL = current)
- `source` (where this came from: "manual" | "agent" | "system")
- `confidence` (0-1 score)
