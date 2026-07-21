# Intelligence Flow and Decision Engine Architecture

This document defines the routing logic and workflows that control how tasks are evaluated, routed, and executed within the **AI-BOSS-OS** integration layer.

## 1. End-to-End Routing Logic

Requests originating from Hermes agents pass through the **Decision Engine** to determine whether to apply standard single-model execution or multi-model council debate.

```text
                  [ Hermes Agent Request ]
                             |
                             v
                 +-----------------------+
                 |    Decision Engine    |
                 +-----------+-----------+
                             |
                     Is High Importance?
                             |
              +--------------+--------------+
              | No                          | Yes
              v                             v
      +---------------+             +---------------+
      |   OmniRoute   |             |  LLM Council  |
      +-------+-------+             +-------+-------+
              |                             |
              v                             v
      [ Single Model ]              [ Multi-Model ]
      (e.g. Claude 3.5)             (Debate & Rank)
              |                             |
              v                             v
      +---------------+             +---------------+
      |  Execution    |             | Consensus Met?|
      +---------------+             +-------+-------+
                                            |
                                    +-------+-------+
                                    | Yes           | No
                                    v               v
                             +-------------+ +-------------+
                             |   Execute   | |   Escalate  |
                             |  Decision   | |  to Human   |
                             +-------------+ +-------------+
```

---

## 2. Decision Engine Classifications

The Decision Engine evaluates incoming agent commands based on defined criteria:

### 2.1 Normal Tasks
- **Characteristics**: Low financial risk, easily reversible, routine code modifications, database checks, or web scraping.
- **Routing**: Forwarded directly to `OmniRoute` using standard `auto/*` tags.
- **Example**: *"Update the footer styling in index.html"* or *"Index the repository using GitNexus."*

### 2.2 High-Importance Decisions
- **Characteristics**: Actions involving irreversible changes, capital investment, codebase architecture restructuring, or policy updates.
- **Routing**: Routed to the `LLM Council` associated with that domain.
- **Example**: *"Authorize the acquisition of target database tools"* or *"Approve security compliance policy updates."*

---

## 3. Step-by-Step Executions

### Normal Task Execution Flow
1. **Request**: Hermes agent posts request: *"Scan the codebase for unused CSS tags."*
2. **Evaluation**: Decision Engine classifies task as `LOW` risk.
3. **Dispatch**: Request routed to `OmniRoute` with `model: auto/coding`.
4. **Resolution**: OmniRoute executes request on the most cost-effective coding model.
5. **Callback**: The results are returned to Hermes to complete the step.

### High-Importance Decision Flow
1. **Request**: Hermes agent CFO requests: *"Allocate $50,000 for server infrastructure upgrade."*
2. **Evaluation**: Decision Engine classifies task as `HIGH` risk (financial threshold exceeded).
3. **Dispatch**: Request routed to the `finance` LLM Council.
4. **Consensus**: Members debate, review, and grade the action. The Chairman synthesizes the debate transcript and scores the proposal at `91%` (exceeding the `80%` threshold).
5. **Execution**: Decision Engine registers the approval node inside the Neo4j knowledge graph and returns the approval token to Hermes.
6. **Execution Logging**: Hermes executes the transaction, recording details in PostgreSQL for auditing.
