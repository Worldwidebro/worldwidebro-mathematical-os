# Delegation Rules: Handoff Protocols Across the Network

## Core Principle
Every venture must delegate work to at least 2 other ventures. Delegation is not optional—it's the core value creation mechanism. We prioritize open-source, free, or self-hosted tools; we can always find a solution that doesn't cost.

---

## 1. Fiduciary Spending & Approval Limits

Every transaction, commitment, or invoice request follows a strict authorization matrix:
- **Automatic Approved (< $1,000)**: Deployed automatically by specialist or venture agents within standard operational parameters.
- **Director Review ($1,000 to $10,000)**: Requires signature from the Sector Director Agent (CFO/CFO-supervised directors).
- **Human Principal Review (> $10,000)**: Suspends execution and escalates to the human principal. Includes legal entity formations, DBA registrations, and capital injections.

---

## 2. Command Line Safeguards

Specialist and developer agents must run terminal operations under strict sandbox constraints:
- **Prohibited**: Bypassing sandbox security without explicit user confirmation.
- **Allowed**: Git staging (`git add`, `git commit`), Node building (`npm run dev`), Python compilation (`python3 -m py_compile`), and database lookups.

---

## 3. Runaway Cost Circuit Breakers

To protect the corporate treasury, the runner monitors API expenditure hourly:
- **Hour Spend Cap**: If any single agent pipeline spends more than **$5.00** in a single hour, the system freezes the thread, revokes the token, logs the status as `blocked`, and alerts the human operator.
- **Consecutive Errors**: If an agent experiences more than **3 consecutive errors** on the same execution loop, it freezes execution and escalates.

---

## 4. Delegation Triggers & SLA Timelines

- **STA → CON (Labor)**: Sourcing SLA < 24 hours; contractor deployment < 48 hours. base billing invoiced at **30-40% markup**.
- **CON → RE (Assets)**: Asset handoff logged within 24 hours of completion. Margin captured: 25-35%.
- **RE → FIN (Deals)**: Financing needs routed within 48 hours of lead identification. Fee: 1-2% advisory.
- **FIN → INVESTMENT (Capital)**: Investment memo delivered within 72 hours. Target: 15-20% carry.
- **OPS → ALL (Back-office)**: Tickets routed and answered within 24 hours. Markup: 5-10%.

---

## 5. Monday Launch Checklist (Verification Sequence)

To validate the delegation network on Monday morning, agents must verify each stage:

```text
    [CON-001 Opportunity] ──→ [STA-001 Pick Up] ──→ [Vet & Compliance] ──→ [Supabase Ledger & Neo4j]
    Create trade: electrician   Accept assignment    Verify license (NCLBGC)   Log transaction & captured margin
```

1. **Neo4j Provisioning**: Execute `/Users/acebless/Documents/Gemini/business-os/neo4j-schema.cypher` to initialize vertices.
2. **Supabase Schema Creation**: Execute `/Users/acebless/Documents/Gemini/business-os/supabase-schema.sql` to setup database tables.
3. **Takeoff Opportunity Generation**:
   - `CON-001` creates an `Opportunity` node (`trade: electrician`, `value: 5000`).
4. **STA Assignment & Matching**:
   - `STA-001` queries opportunities, accepts assignment, and runs compliance verification against `compliance_records` (verify license, background checks).
5. **Ledger Posting**:
   - Create a `transaction` in Supabase with `transaction_type: 'labor_invoice'` and update the Neo4j `margin_captured` property on the edge.
6. **Dashboard Validation**:
   - Open `/network/delegation/completed` in the VEX dashboard to check that the transaction logs are rendered.
