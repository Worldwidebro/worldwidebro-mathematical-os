# LLM Council Governance and Consensus Policies

This document establishes the operational rules, voting methodologies, review protocols, and audit requirements for the **LLM Council** decision-making workflows.

## 1. Council Structure and Formation

A council is a dynamic team of model nodes created to evaluate decisions. It consists of:
- **Members**: A minimum of **three** heterogeneous models (representing at least two different providers, e.g., Anthropic and OpenAI) to prevent single-vendor cognitive biases.
- **Chairman**: A designated model with advanced reasoning capabilities responsible for compiling individual responses and writing the final summary.
- **Threshold**: The percentage consensus score required to auto-approve an action.

---

## 2. Peer Review and Voting Protocols

To ensure objective evaluation, councils use a double-blind peer review methodology:

```text
1. Draft Submission --> 2. Anonymization --> 3. Peer Grading --> 4. Consensus Tally
```

### 2.1 Grading Criteria
Each member scores responses from 1 to 10 based on four categories:
1. **Feasibility**: Can the proposed solution be executed with existing tools?
2. **Security**: Does this introduce risks or expose credentials?
3. **Optimality**: Is this the most resource-efficient path?
4. **Resilience**: Are exceptions and edge cases handled?

### 2.2 Consensus Tally Algorithm
The overall consensus score $C$ is calculated as the average grade across all peer reviews, normalized to a percentage:

\[C = \left( \frac{\sum_{i=1}^{N} S_i}{10 \times N} \right) \times 100\]

Where:
- $S_i$ is the individual score given by a member model to a proposal.
- $N$ is the total number of peer evaluations.

---

## 3. Chairman Synthesis Guidelines

The Chairman model compiles the final executive summary. It must strictly adhere to the following synthesis criteria:

1. **Conflict Resolution**: Highlight any dissenting opinions or risks raised by member models. Do not discard warnings, even if the consensus score is high.
2. **Attribution Neutrality**: Reference ideas by anonymized source labels (e.g., *"Model B raised a critical performance concern..."*) rather than model name.
3. **Execution Blueprint**: Conclude with a clear, step-by-step action plan for Hermes to execute.

---

## 4. Threshold & Escalation Matrix

Depending on the risk level of the decision category, the system applies the following thresholds:

| Decision Category | Example | Consensus Threshold | Action on Success | Action on Failure |
| :--- | :--- | :--- | :--- | :--- |
| **Capital Allocation** | Mergers, investments | `90%` | Auto-dispatches to banking APIs | Holds task, alerts CFO |
| **Architecture Change** | Schema updates, deletions | `80%` | Auto-applies code migration | Suspends branch, alerts CTO |
| **Policy Override** | Security rule updates | `95%` | Writes changes to policy registry | Blocks execution, alerts CEO |
