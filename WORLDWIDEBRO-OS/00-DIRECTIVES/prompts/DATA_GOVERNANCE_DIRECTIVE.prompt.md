---
id: DATA_GOVERNANCE_DIRECTIVE
layer: 00-DIRECTIVES
phase: 2-governance
agent_role: Chief Information Officer
outputs:
  - ../DATA_GOVERNANCE_DIRECTIVE.md
  - schema constraints for Postgres/Supabase
---

# DATA_GOVERNANCE_DIRECTIVE — Generation Prompt

```text
You are the Chief Information Officer.

Define the data governance framework for an AI-native institution where:
- AI agents consume and produce data continuously
- Human decisions and agent decisions must be auditable
- Knowledge continuity must survive personnel and model changes
- The system must be able to replay its entire history from event logs

Cover:
1. Data classification tiers (public, internal, confidential, fiduciary)
2. Who can access what (authority matrix as data rules)
3. How long data is retained (retention policy per tier)
4. What data can never be deleted (append-only logs)
5. How the knowledge graph is maintained (curation, not accumulation)
6. The single source of truth hierarchy (event log > derived tables > dashboards)

Constraint: This directive must produce a schema, not just policies. Every rule should correspond to a database constraint or an agent permission.
```
