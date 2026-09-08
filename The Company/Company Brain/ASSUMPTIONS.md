[[STARTHERE]] | [[REALITY]] | [[CLAIMS]]

# ASSUMPTIONS.md — The System Assumption Ledger

> **Canonical Document ID:** `DOC-ASM-001`  
> **Authority:** Knowledge Control Plane (CP-013) & Executive Governance (CP-006)  
> **Rule:** *An assumption is a liability until converted into evidence.*  
> **Status Taxonomy:** `KNOWN TRUE` | `KNOWN FALSE` | `ASSUMED TRUE` | `UNKNOWN` | `UNTESTED` | `CONTRADICTED` | `EXPIRED`

---

## 1. Active Assumptions Registry

```yaml
ASM-001:
  statement: "700 cataloged ventures represent real operating businesses."
  status: CONTRADICTED
  confidence: 0.0
  evidence:
    - EVD-005 (CLAUDE.md live audit)
    - REALITY.md Section 8 ($0 revenue, 0 customers)
  consequence:
    - Freeze 690 ventures in _REGISTRIES/VENTURE_REGISTRY.yaml to cold archive.
    - Focus 100% of executive bandwidth on Venture #1.

ASM-002:
  statement: "Ollama is running qwen2.5-coder:14b on Mac Studio."
  status: KNOWN FALSE
  confidence: 0.0
  evidence:
    - EVD-006 (civos_litellm config comments confirming Ollama removed 2026-07-17)
  consequence:
    - Update all documentation and registries to reflect native exo MLX runtime.

ASM-003:
  statement: "CLI-Anything is an npm package that generates the cb CLI from schema.yaml."
  status: KNOWN FALSE
  confidence: 0.0
  evidence:
    - EVD-007 (npm 404 for @hkuds/cli-anything; package never existed)
  consequence:
    - Treat _CLI/bin/cb as permanent hand-written Bash orchestrator; stop searching for npm generator.

ASM-004:
  statement: "Running 4 overlapping Docker compose stacks provides high availability."
  status: CONTRADICTED
  confidence: 0.0
  evidence:
    - EVD-005 (Duplicate databases, port confusion, t7shield-neo4j crash-looping)
  consequence:
    - Decommission t7shield, spinup, and buzz stacks; standardize solely on civos_*.

ASM-005:
  statement: "OmniRoute provides active model routing for our coding agents."
  status: CONTRADICTED
  confidence: 0.1
  evidence:
    - EVD-003 (HTTP 401 on all Antigravity MCP tool calls)
    - EVD-004 (omniroute doctor reports all 7 CLIs unconfigured)
  consequence:
    - Generate machine token for Antigravity MCP; run omniroute configure for installed CLIs.

ASM-006:
  statement: "Enterprise customers will pay $5,000–$10,000 for local AI infrastructure audits."
  status: UNTESTED
  confidence: 0.5
  evidence:
    - None (No outbound market offers made)
  consequence:
    - Conduct 5 customer discovery calls before building more automation features.

ASM-007:
  statement: "Native MLX serving (exo) on Mac Studio outperforms Ollama for local coding inference."
  status: KNOWN TRUE
  confidence: 0.9
  evidence:
    - EVD-008 (Mac Studio M4 Max benchmarks with Qwen3.6-35B-A3B-5bit)
  consequence:
    - Maintain exo as primary local inference engine; deprecate all remaining Ollama references.

ASM-008:
  statement: "Our multi-layer ontology improves AI agent reasoning accuracy over raw file search."
  status: UNTESTED
  confidence: 0.4
  evidence:
    - None (No benchmarked evaluation traces in Langfuse)
  consequence:
    - Run A/B eval traces on real coding tasks comparing graph context vs. plain grep.
```

---

## 2. Assumption Review Cadence
- **Weekly Audit (Friday 17:00):** Review all `UNTESTED` and `ASSUMED TRUE` items.
- **Falsification Rule:** If an assumption remains `UNTESTED` for > 30 days without an active experiment, it must be downgraded to `EXPIRED` and stripped from architecture decisions.
