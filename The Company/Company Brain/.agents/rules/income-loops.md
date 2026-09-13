# Universal Income Loops Rule — Company Brain

> **Authority:** CP-002, CP-027, Rule 1-3  
> **Master Reference:** `55-LOOP-ENGINEERING/COMPANY_INCOME_LOOPS_ARCHITECTURE.md`

## 1. Architectural Separation
- **State Belongs to Database & Company Brain:** Postgres / Supabase owns relational entities; Neo4j owns ontology/relationships; Qdrant owns embeddings.
- **Action Belongs to n8n:** n8n workflows are stateless action executors. They never act as the source of truth.
- **Decision Belongs to Agents:** OmniRoute and AI models reason, classify, score, and decide next actions.
- **Exceptions Belong to Humans:** Unresolved errors, SLA breaches, and compliance hazards drop into the Dead-Letter Queue for human intervention.

## 2. The 16-Stage Income Conveyor Belt
1. Market Signal → 2. Prospecting → 3. Lead Capture → 4. Qualification → 5. Sales Conversation → 6. Quote / Proposal → 7. Close / Contract → 8. Customer Onboarding → 9. Fulfillment → 10. Billing → 11. Collection → 12. Retention → 13. Expansion → 14. Referral → 15. Cash / Profit → 16. Reinvestment.

## 3. Workflow Assembly Over Inventory Sprawl
- **Do Not Deploy 4,343 Workflows Raw:** Treat external workflow libraries (such as `Zie619/n8n-workflows`) as a component capability catalog.
- Assemble candidate workflows into the **27 Closed-Loop Feedback Circuits** and ~120 modular building blocks.
- Prioritize loops according to the **25-Stage Rollout Matrix** (Priority 1: Lead Acquisition through Priority 10: Unified Data/CRM).

## 4. Mandatory 5-Circuit Sub-Loop Requirement
Every automated stage in any revenue loop must implement:
1. `[Success Loop]`: State transition & downstream event emit.
2. `[Failure Loop]`: Structured error payload capture.
3. `[Retry Loop]`: Exponential backoff with jitter (max 3 tries).
4. `[Telemetry Loop]`: Execution time, API status, and unit cost logging.
5. `[Human Escalation Loop]`: Urgent notification to operator dispatch on SLA breach or unrecoverable error.
