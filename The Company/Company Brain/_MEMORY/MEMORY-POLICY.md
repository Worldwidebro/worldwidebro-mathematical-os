# MEMORY-POLICY — Governance, Privacy, and Security Directives

[[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[_MEMORY/MEMORY-ARCHITECTURE|MEMORY-ARCHITECTURE]] | [[_MEMORY/MEMORY-QUALITY|MEMORY-QUALITY]] | [[STARTHERE]]

> **Canonical Document ID:** `MEM-POL-001`  
> **Authority:** Security & Governance Control Planes (CP-027, CP-033, CP-016)  
> **Scope:** Project-Wide AI Memory, Embedding Vectors, Vector Databases, and Graph Stores

---

## 1. Zero-Trust Secrets Management

1. **No Credentials in Memory**: Under NO circumstances may passwords, private keys, session tokens, JWTs, API secrets, or OAuth refresh tokens be ingested into Qdrant vectors, Neo4j properties, or Markdown memory files.
2. **Bitwarden Integration (`SEC-BITWARDEN-001`)**: All credentials must be dynamically retrieved at runtime using the Bitwarden CLI (`bw get password` / `bw get item`).
3. **Secret Redaction Filter**: Any log, transcript, or output pipe feeding memory consolidation MUST pass through the automated regex secret sanitization filter before persistence.

---

## 2. Retention & Data Lifecycle Policies

| Memory Tier | Maximum Retention | Storage Backend | Pruning Policy |
|---|---|---|---|
| **Working Memory** | Duration of active task / 24h | Session RAM, Scratch files | Purged on task completion |
| **Episodic Memory** | 90 days (active) / 1 yr (cold) | JSONL Logs, OpenObserve, Git | Compressed after 30d, cold archived after 90d |
| **Semantic Memory** | Indefinite (versioned) | Qdrant (`:6333`), Canonical YAMLs | Decayed or updated upon verification |
| **Procedural Memory** | Indefinite (versioned) | `.agents/skills/`, Markdown SOPs | Git-tracked, reviewed on version changes |
| **Relationship Graph** | Indefinite (versioned) | Neo4j (`:7687`) | Merged, bi-directional, audited weekly |

---

## 3. Privacy & Intellectual Property Safeguards

1. **Commercial Confidentiality**: Venture proprietary algorithms, customer lists, and transaction records must be strictly isolated to their canonical venture scopes.
2. **Local-First Boundary**: High-sensitivity memory embeddings must only be indexed on local nodes (Mac Studio M4 Max / MacBook Air). No raw proprietary embeddings may be exported to untrusted external third-party vector stores without operator authorization.
3. **Egress Guardrails**: OmniRoute inference requests referencing semantic memory nodes must sanitize PII (Personally Identifiable Information) before external cloud LLM transmission.
