# MEMORY-RETRIEVAL — Context Retrieval and Multi-Signal Ranking

[[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[_MEMORY/MEMORY-MODEL|MEMORY-MODEL]] | [[_PROMPTS/03_MEMORY-RETRIEVAL|03_MEMORY-RETRIEVAL]] | [[STARTHERE]]

> **Canonical Document ID:** `MEM-RET-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)

---

## 1. Context Flooding Prevention

A major pathology of naive LLM systems is "context dumping" — stuffing thousands of raw tokens of outdated conversations into the prompt. This causes high token costs, degraded reasoning, hallucination, and loss of attention.

Company Brain uses a **10-Signal Context Ranking Engine**. Only memories scoring above the dynamic relevance threshold ($\tau \ge 0.65$) are injected into working agent context.

---

## 2. The 10-Signal Scoring Heuristic

Each candidate memory node $m$ retrieved from Qdrant or Neo4j is scored by the function:

$$\text{Score}(m, T) = \sum_{i=1}^{10} w_i \cdot S_i(m, T)$$

Where $T$ is the current task, and $w_i$ represents the normalized weight of signal $S_i$:

| Signal | Name | Weight ($w_i$) | Description |
|---|---|---|---|
| $S_1$ | **Relevance** | `0.20` | Dense vector cosine similarity between task embedding and memory embedding |
| $S_2$ | **Recency** | `0.10` | Exponential decay over time: $e^{-\lambda \Delta t}$, favoring recent events |
| $S_3$ | **Importance** | `0.15` | Structural weight (Enterprise > Venture > Project > Ephemeral task) |
| $S_4$ | **Frequency** | `0.05` | Count of historical accesses and successful citations |
| $S_5$ | **Confidence** | `0.15` | Provenance score ($0.0$ to $1.0$) based on empirical backing |
| $S_6$ | **Authority** | `0.10` | Source hierarchy: Sovereign Operator > Runtime Probe > Spec > Chat |
| $S_7$ | **Causal Proximity** | `0.10` | Graph distance to immediate upstream cause or downstream dependency |
| $S_8$ | **Entity Overlap** | `0.05` | Jaccard index of matched entity IDs (`SEC-*`, `VEN-*`, `REP-*`, `CAP-*`) |
| $S_9$ | **Task Similarity** | `0.05` | Historical similarity of task intent to prior episodes |
| $S_{10}$ | **Truth State** | Multiplier | Active/Verified: `1.0`; Probable: `0.8`; Assumed: `0.4`; Stale: `0.2`; Conflicted: `0.0` |

---

## 3. Retrieval Budget & Limits

1. **Max Tokens Allocated for Memory**: $\le 15\%$ of total context window (typically 4,000–8,000 tokens maximum).
2. **Top-K Limit**: Maximum 5 semantic facts, 3 episodic excerpts, and 2 procedural runbooks per prompt.
3. **Graph Radius**: Maximum 2 hops from target entities in Neo4j during associative retrieval.
