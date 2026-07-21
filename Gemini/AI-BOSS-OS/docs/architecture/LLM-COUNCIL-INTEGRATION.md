# LLM Council Integration Architecture

This document details the architecture and operational mechanics of the **LLM Council** within the AI-BOSS-OS, inspired by Andrej Karpathy's consensus reasoning patterns.

## 1. Core Reasoning Workflow

The LLM Council is a multi-model consensus layer designed to resolve highly critical, high-risk operational decisions (e.g., mergers, large capital expenditures, strategic planning revisions). Rather than relying on a single model's reasoning, a panel of diverse models debates and scores solutions.

```text
                  [ User Question ]
                          |
                  +-------v-------+
                  | Council Boss  |
                  +-------+-------+
                          |
        +-----------------+-----------------+
        |                 |                 |
        v                 v                 v
   [ Claude 3.5 ]    [ GPT-4o ]      [ Gemini 1.5 ]  <-- Members draft solutions
        |                 |                 |
        +-----------------+-----------------+
                          |
                          v
               [ Blind Peer Review ]         <-- Members review and grade each other's drafts
                          |
                          v
                [ Chairman Synthesis ]       <-- Chairman reconciles reviews & writes final decision
                          |
                          v
                  [ Final Output ]
```

The process operates in five sequential steps:

1. **Query Distribution**: The Council Manager broads requests to all registered member models.
2. **Drafting (Generation)**: Each model generates a detailed response independently, without visibility into other answers.
3. **Blind Peer Review**: Responses are anonymized (labelled Model A, Model B, Model C) and routed back to the members. Each model evaluates and grades the quality, security, and feasibility of all solutions.
4. **Ranking & Scoring**: The Council Manager tallies peer review grades and ranks responses.
5. **Chairman Synthesis**: The designated Chairman model (typically `claude-3-5-sonnet`) reviews the full debate transcript, resolves conflicting viewpoints, and issues the final executive decision.

---

## 2. Integration & Registries

Councils are defined inside `/AI-CORE/council-registry/council_registry.yaml`. A council registration specifies:
- **Members**: List of participating model engines.
- **Chairman**: The final synthesis agent.
- **Threshold**: The minimum agreement level required to execute the action automatically without manual developer intervention.

Example Registration:
```yaml
councils:
  acquisition:
    members:
      - claude
      - gpt
      - gemini
    chairman:
      claude
    threshold:
      80%
```

---

## 3. Operations & Safety Policies

- **Anonymity Injection**: During peer review, all system metadata and model identifiers are stripped from prompts to prevent bias.
- **Consensus Failure Escalation**: If the calculated consensus score falls below the required threshold (e.g., `< 80%`), the Decision Engine halts execution, generates a variance report, and sends a notification to the developer/operator dashboard for manual review.
