# MEMORY-CONTRADICTIONS — Conflict Detection and Reconciliation

[[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[_MEMORY/MEMORY-QUALITY|MEMORY-QUALITY]] | [[REALITY]] | [[STARTHERE]]

> **Canonical Document ID:** `MEM-CONTR-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)

---

## 1. Conflict Types

Contradictions in a multi-agent, distributed environment arise across six major boundaries:

1. **New Fact vs Old Fact**: e.g., Old note says "Ollama decommissioned", but live session launched Ollama `:11434`.
2. **New Decision vs Old Decision**: e.g., Previous sprint selected PostgreSQL for vectors, new ADR selects Qdrant.
3. **Current State vs Documentation**: e.g., README claims 22 deployments live, but Vercel API shows 14 active.
4. **Registry vs Runtime Reality**: e.g., `service_registry.json` lists container running, but `docker ps` returns empty.
5. **Claim vs Empirical Evidence**: e.g., PR claims "feature complete", but unit test fails with exit code 1.
6. **Plan vs Implementation**: e.g., Implementation plan states Node.js, implementation wrote Python script.

---

## 2. Detection Mechanism

When a candidate memory $m_{new}$ is proposed:
1. Semantic search queries Qdrant for existing memories with $\text{cosine\_sim}(m_{new}, m_{existing}) \ge 0.85$.
2. If the semantic entity matches but assertion values diverge (e.g., status, port, IP, ownership), a **Contradiction Alert** is triggered.
3. Both nodes are marked with state `CONFLICTED`.

---

## 3. Reconciliation Protocol

1. **Automatic Resolution**: If $m_{new}$ possesses higher provenance authority (e.g. Runtime Probe vs Stale Markdown), $m_{new}$ is marked `VERIFIED` and $m_{old}$ is marked `SUPERSEDED` or `DISPROVEN`.
2. **Escalation**: If both memories possess identical provenance tier (e.g., conflicting operator statements), the contradiction is logged to `REALITY.md` under **Known Contradictions** and flagged to the operator for immediate resolution.
