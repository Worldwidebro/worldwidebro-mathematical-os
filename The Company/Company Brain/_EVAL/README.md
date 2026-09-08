---
id: EVAL-OPERATIONAL-HUB
title: "_EVAL — Operational Evaluation Harness & Benchmarking Gateway"
aliases: ["_EVAL", "Evaluation Harness", "System Verification Hub", "Operational Evals", "_EVAL/README"]
tags: ["evaluation", "benchmarks", "swe-bench", "utopia", "agents", "receipts", "testing", "verification"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[42-EVALUATION/README|42-EVALUATION Master]] | [[42-EVALUATION/42-EVALUATION|42-EVALUATION Domain]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|Master Control]] | [[CLAUDE]] | [[REALITY]]

# _EVAL — Operational Evaluation Harness & Benchmarking Gateway

> **Authority:** Performance & Quality Control Plane ([[CP-028]])  
> **Master Operating Contract:** [[ANTIGRAVITY.md]] (Rule 3: Strictly zero fake completion — all claims must be proven by reproducible execution)  
> **Macro Architectural Domain:** [[42-EVALUATION/README|42-EVALUATION Master Gateway]]  
> **Live Runtime State:** [[CLAUDE.md]]  
> **Status:** 🟢 ACTIVE — Operational Evaluation Hub (2026-09-06)

---

## 1. Executive Summary

The **`_EVAL`** subsystem is the empirical verification laboratory, benchmark testbed, and capability evaluation ground of Company Brain. While [[42-EVALUATION/README|42-EVALUATION]] establishes the high-level evaluation doctrine, `_EVAL/` serves as the runtime operational filesystem housing:
1. **Evaluated External Systems & Reference World Models** (e.g., [[_EVAL/utopia/README|Utopia Enterprise World Model]]).
2. **Standardized Model Benchmark Criteria** (SWE-bench Verified, LiveCodeBench, AgentBench, GPQA Diamond).
3. **Autonomous Agent Evaluation Harnesses** ([[16-AGENTS/AGT-009-education-eval|AGT-009]], [[node/plans/course-generation-loop|Course Generation Loop]]).
4. **Execution Receipt Grading Pipelines** ([[receipts/receipts.jsonl]], [[review-receipts/receipts.jsonl]]).
5. **Specialized Quality Assurance & Testing Skills Fleet** (17 dedicated testing agents in `.agents/skills/`).

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               42-EVALUATION / _EVAL HARNESS                             │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
         ┌──────────────────┬───────────────┴───────────────┬──────────────────┐
         ▼                  ▼                               ▼                  ▼
┌─────────────────┐┌─────────────────┐             ┌─────────────────┐┌─────────────────┐
│ MODEL BENCHMARK ││ EVALUATED CORE  │             │ AGENT & LOOP    ││ RECEIPT GRADING │
│   EVALUATION    ││ (Utopia Model)  │             │   EVALUATION    ││    TELEMETRY    │
├─────────────────┤├─────────────────┤             ├─────────────────┤├─────────────────┤
│ • SWE-bench     ││ • Bitemporal DB │             │ • AGT-009 Eval  ││ • Receipts JSONL│
│ • LiveCodeBench ││ • 21 ADR Records│             │ • 7-Step Loops  ││ • Tool Auditing │
│ • AgentBench    ││ • Execution Gate│             │ • Output Schema ││ • Token Cost    │
│ • GPQA Diamond  ││ • Tantivy / PG  │             │ • Hallucination ││ • Signatures    │
└─────────────────┘└─────────────────┘             └─────────────────┘└─────────────────┘
         │                  │                               │                  │
         └──────────────────┴───────────────┬───────────────┴──────────────────┘
                                            ▼
                           ┌─────────────────────────────────┐
                           │   17-SKILL TESTING & QA FLEET   │
                           │ (.agents/skills/testing-*, QA)  │
                           └─────────────────────────────────┘
```

---

## 2. Pillar 1: Model Benchmarks & Inference Ground Truth

Models served across local nodes (Mac Studio `:20128` / `:11434`, MacBook Air) and cloud providers are evaluated against standardized empirical benchmarks documented in [[37-RESEARCH/AI-RESEARCH|AI-RESEARCH.md]] and [[17-MODELS/17-MODELS|17-MODELS]]:

| Benchmark Suite | Focus Area | Minimum Target Threshold | Operational Harness / Source |
|---|---|---|---|
| **SWE-bench Verified** | End-to-end GitHub issue solving & patch synthesis | $\ge 35\%$ resolution | SWE-bench testbed & git patch verification |
| **LiveCodeBench** | Contamination-free algorithmic Python / TypeScript | $\ge 45\%$ pass@1 | LeetCode / AtCoder real-time problem set |
| **AgentBench** | Multi-turn tool calling, error recovery, shell execution | $\ge 70\%$ task completion | Operating system, DB, and web navigation envs |
| **GPQA Diamond** | PhD-level scientific, chemical, and mathematical reasoning | $\ge 55\%$ zero-shot accuracy | Google / NYU Google Research benchmark set |
| **Needle-in-a-Haystack** | 128k+ token multi-turn retrieval fidelity | $100\%$ all quadrants | Context length stress testing suite |

---

## 3. Pillar 2: Evaluated Systems — Utopia Enterprise World Model (`_EVAL/utopia`)

The `_EVAL/utopia/` directory contains the complete codebase and architectural evaluation candidate for **Utopia** (`deeplethe/utopia`), cataloged under `EXT-KNOW-003` in [[_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml|EXTERNAL_CAPABILITY_UNIVERSE.yaml]]:

### 3.1 Core Documentation & Ingestion Architecture
- **Master Repository Gateway**: [[_EVAL/utopia/README|Utopia Master README]] — Complete overview of the bitemporal Rust world model.
- **Ingestion Pipeline**: `_EVAL/utopia/docs/pipeline.md` — Five-stage document transformation pipeline converting raw PDFs/docs into bitemporal knowledge graphs.
- **Document Ingest Spec**: `_EVAL/utopia/web/src/docs/ingest.md` — Format handlers for PDF, DOCX, XLSX, Markdown, HTML, and S3 sync.
- **MCP Streaming Server**: `_EVAL/utopia/web/src/docs/mcp.md` — Fast read-only MCP tools over Streamable HTTP.
- **Performance Benchmarks**: `_EVAL/utopia/scripts/bench/README.md` — Ingestion throughput and graph retrieval latency tests.

### 3.2 Architectural Decision Records (ADR 0001 – 0021)
All 21 decision records in `_EVAL/utopia/docs/decisions/` provide concrete engineering solutions evaluated for Company Brain integration:

| ADR ID | Decision Record Title | Target Status | Company Brain Evaluation & Extraction Plan |
|---|---|---|---|
| **ADR 0001** | [Ontology import and governance](_EVAL/utopia/docs/decisions/0001-ontology-import-and-governance.md) | In progress | Validates schema constraints against [[07-ONTOLOGY/README|07-ONTOLOGY]]. |
| **ADR 0002** | [Reasoning engine](_EVAL/utopia/docs/decisions/0002-reasoning-engine.md) | Built (R0/R1) | R0 consistency checker and R1 derivation engine for Neo4j. |
| **ADR 0003** | [Ontology grows out of the corpus](_EVAL/utopia/docs/decisions/0003-ontology-growth-loop.md) | Built | Autonomous extraction loop expanding schemas from unparsed documents. |
| **ADR 0004** | [Language follows the reader](_EVAL/utopia/docs/decisions/0004-language-and-localization.md) | Built | Multi-lingual terminology extraction and localized error models. |
| **ADR 0005** | [The alert center](_EVAL/utopia/docs/decisions/0005-alert-center.md) | Built | Systemic conflict detection and unparseable document alerts. |
| **ADR 0006** | [Ontology scale and prompt budget](_EVAL/utopia/docs/decisions/0006-ontology-scale-and-the-prompt.md) | Built | Token budget allocation (24,000 chars) for prompt context schemas. |
| **ADR 0007** | [Counting decides relations](_EVAL/utopia/docs/decisions/0007-who-decides-what-becomes-a-relation.md) | Built | Relation promotion thresholds (`MIN_DOCS = 2`, `MIN_SIGNALS = 3`). |
| **ADR 0008** | [Ontology packs as cold start](_EVAL/utopia/docs/decisions/0008-ontology-packs-as-cold-start.md) | Built | Embedded cold-start packs (schema.org, W3C Org, PROV-O, FOAF, IOF Core). |
| **ADR 0009** | [Undecided type stays empty](_EVAL/utopia/docs/decisions/0009-no-type-is-a-type.md) | Implemented | Prevents speculative type hallucination in graph extraction. |
| **ADR 0010** | [Unnamed relation stays empty](_EVAL/utopia/docs/decisions/0010-no-relation-is-no-relation.md) | Implemented | Prohibits generic fallback edges (`related_to`); preserves exact predicate surface. |
| **ADR 0011** | [A mapping is configuration](_EVAL/utopia/docs/decisions/0011-a-mapping-is-not-a-fact.md) | Implemented | Separates ingestion configuration from ground truth assertions. |
| **ADR 0012** | [Ontology is a contract](_EVAL/utopia/docs/decisions/0012-the-ontology-is-a-contract-not-a-suggestion.md) | Implemented | Drops edge violations from 57% to 4%; strict constraint validation. |
| **ADR 0013** | [A source hands over history](_EVAL/utopia/docs/decisions/0013-a-source-should-hand-over-its-history.md) | Implemented | Bitemporal sync for GitHub, Jira, and Notion changelogs. |
| **ADR 0014** | [Identity from person, scope from token](_EVAL/utopia/docs/decisions/0014-identity-from-the-person-scope-from-the-token.md) | Implemented | Zero-trust token-scoped FastMCP read/write access. |
| **ADR 0015** | [Recorded sentence waits for a nod](_EVAL/utopia/docs/decisions/0015-recording-a-sentence-is-not-asserting-a-fact.md) | Implemented | Pending memory facts queue requiring agent/human validation. |
| **ADR 0016** | [Close open seams before cutting new ones](_EVAL/utopia/docs/decisions/0016-close-the-open-seams-before-cutting-new-ones.md) | In progress | Disciplined architectural hardening and debt remediation. |
| **ADR 0017** | [Contradiction points upstream](_EVAL/utopia/docs/decisions/0017-a-contradiction-points-upstream.md) | Implemented | Contested edge visual alerts and blocked derivation signals. |
| **ADR 0018** | [Lakehouse is one protocol away](_EVAL/utopia/docs/decisions/0018-the-lakehouse-is-one-protocol-away.md) | Implemented | Unified Apache Trino integration for Iceberg, Delta Lake, and Snowflake. |
| **ADR 0019** | [The second clock can be rewound](_EVAL/utopia/docs/decisions/0019-the-second-clock-can-be-rewound.md) | Implemented | Bitemporal `held_at` (valid time) and `as_of` (system transaction time). |
| **ADR 0020** | [An auditor reads it without us](_EVAL/utopia/docs/decisions/0020-an-auditor-reads-it-without-us.md) | Implemented | Standard RDF Turtle / JSON-LD export streaming endpoint. |
| **ADR 0021** | [Rule reads attributes and concludes a type](_EVAL/utopia/docs/decisions/0021-a-rule-reads-attributes-and-concludes-a-type.md) | Planned | Attribute-driven dynamic type derivation rules. |

### 3.3 Target Extraction Action Plan
As mapped in [[09-KNOWLEDGE/Utopia-World-Model|Utopia World Model Specification]]:
1. **Bitemporal Neo4j Schema**: Extract Utopia's `valid_from`, `valid_to`, `tx_from`, and `tx_to` timestamp conventions into Company Brain's Cypher schemas (`_ONTOLOGY/`).
2. **Autonomous Execution Gate**: Port Utopia's `AgentExecutionGate` pattern into [[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING|Fractal Loop Orchestration]] to enforce financial circuit-breakers on L2/L3 agents.

---

## 4. Pillar 3: Agent Output & Curriculum Verification

Autonomous agent outputs are evaluated across rigorous verification pipelines:
- **Dedicated Agent Evaluator**: [[16-AGENTS/AGT-009-education-eval|AGT-009 (Education Eval Agent)]]:
  - Assesses curriculum fidelity, quiz difficulty progression, readability indices (Flesch-Kincaid), and learning outcome attainment.
- **Loop Plan Evaluation**: [[node/plans/course-generation-loop|Course Generation Loop]]:
  - Evaluates outputs across 7 structured stages (`01-topic-selection`, `02-curriculum-design`, `03-lesson-authoring`, `04-code-examples`, `05-quiz-generation`, `06-asset-linking`, `07-analytics-setup`).
  - Automated criteria: Zero hallucinated URLs, valid JSON/YAML syntax, strict alignment with [[_INFRASTRUCTURE/supabase-education-schema.sql]].

---

## 5. Pillar 4: Execution Receipt Auditing & Grading

The execution receipt subsystem provides cryptographic auditability for all autonomous actions:
- **Receipt Streams**:
  - Raw operational receipts: [[receipts/receipts.jsonl]]
  - Quality review receipts: [[review-receipts/receipts.jsonl]]
- **Automated Grading Criteria**:
  1. **Execution Validity**: Verified tool call exit codes (`exit_code: 0`).
  2. **Latency Efficiency**: Execution duration per subagent task step ($< 5000\text{ms}$ target).
  3. **Financial / Token Budget**: Input tokens, output tokens, and dollar cost within allocated guardrails.
  4. **Cryptographic Signatures**: Agent identity and timestamp integrity checks.
  5. **Feedback Routing**: Feeds directly into [[_PIPELINES/learning/README|Learning Pipeline]] and [[44-LEARNING/44-LEARNING]].

---

## 6. Pillar 5: Specialized Testing & QA Skills Fleet (17 Skills)

Located in `.agents/skills/`, these 17 specialized skills provide automated evaluation capabilities:

| Skill Directory | Specialist Persona | Evaluation Focus |
|---|---|---|
| `testing` | Master QA Governor | Orchestrates test execution, coverage gating, and verification standards. |
| `testing-api-tester` | API Testing Specialist | REST/GraphQL/MCP validation, payload schemas, and load benchmarking. |
| `testing-evidence-collector` | Visual Evidence Collector | Screenshot proof, non-fungible artifacts, and UI state verification. |
| `testing-reality-checker` | Reality Auditor | Enforces Rule 3 (zero fake completion) and denies unverified approvals. |
| `testing-performance-benchmarker` | Performance Benchmarker | Latency profiling, memory leak detection, and throughput optimization. |
| `testing-test-automation-engineer` | Test Automation Engineer | Playwright and Cypress end-to-end resilient test automation suites. |
| `testing-test-results-analyzer` | Results Analyzer | Flaky test detection, failure clustering, and actionable test analytics. |
| `testing-tool-evaluator` | Tool & Package Evaluator | Evaluates external open-source candidates and SaaS vendors for adoption. |
| `testing-workflow-optimizer` | Workflow Optimizer | Identifies pipeline bottlenecks, toilsome loops, and automation waste. |
| `specialized-model-qa` | Model QA Specialist | Regression testing, prompt drift detection, and factual fidelity grading. |
| `gis-qa-engineer` | Geospatial QA Engineer | Coordinate reference system (CRS) accuracy, vector topology, and raster integrity. |
| `security-compliance-auditor` | Compliance Auditor | SOC 2, ISO 27001, HIPAA, and GDPR audit trails and evidence gathering. |
| `security-penetration-tester` | Penetration Tester | Automated vulnerability scanning, privilege escalation checks, and attack surface audits. |
| `security-threat-detection-engineer` | Threat Detection Engineer | SIEM rule evaluation, alert tuning, and MITRE ATT&CK coverage validation. |
| `security-appsec-engineer` | Application Security Engineer | SAST/DAST pipelines, dependency vulnerability scans, and secure code review. |
| `security-cloud-security-architect` | Cloud Security Architect | IAM role boundaries, zero-trust network configurations, and least-privilege checks. |
| `design-ui-finish-gate-reviewer` | UI Finish Gate Reviewer | Hard gate against generic interfaces; visual fidelity, contrast, and layout audits. |

---

## 7. Operational Verification Commands

```bash
# 1. Run Vault-Wide Integrity and Link Audit
cd "/Users/acebless/Documents/The Company/Company Brain"
bash audit.sh

# 2. Inspect Execution Receipts for Anomalies
tail -n 20 receipts/receipts.jsonl | jq '{timestamp: .created_at, tool: .tool_calls[0].name, status: .status}'

# 3. Test Local Model Latency via OmniRoute
curl -X POST http://100.87.214.70:20128/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen2.5-coder:7b", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 10}'
```

---

## 8. Bidirectional Navigation

- **Upstream Architecture**: [[42-EVALUATION/README|42-EVALUATION Master Gateway]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|Master Control]]
- **Evaluated System**: [[_EVAL/utopia/README|Utopia Enterprise World Model]] | [[09-KNOWLEDGE/Utopia-World-Model|Utopia Documentation Note]]
- **Inference Runtime**: [[_INFRASTRUCTURE/README|Operational Infrastructure]] | [[_INFRASTRUCTURE/omniroute/README|OmniRoute Gateway]]
- **Execution & Learning**: [[receipts/receipts.jsonl]] | [[_PIPELINES/learning/README|Learning Pipeline]] | [[44-LEARNING/44-LEARNING]]
