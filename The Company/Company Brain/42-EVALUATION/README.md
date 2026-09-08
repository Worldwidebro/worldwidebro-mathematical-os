---
id: DOMAIN-42-GATEWAY
title: "42-EVALUATION — Master Evaluation & Verification Architecture"
aliases: ["42-EVALUATION", "Evaluation Hub", "_eval", "evals", "Evaluation Benchmarks"]
tags: [evaluation, benchmarks, models, agents, verification, receipts, accuracy, swe-bench]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[_EVAL/README|Operational Evaluation Hub (_EVAL)]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|Master Control]] | [[42-EVALUATION/42-EVALUATION|42-EVALUATION Domain]] | [[REALITY]]

# 42-EVALUATION — Master Evaluation & Verification Architecture

> **Authority:** Performance & Quality Control Plane ([[CP-028]])  
> **Master Operating Contract:** [[ANTIGRAVITY.md]] (Rule 3: Strictly zero fake completion)  
> **Operational Filesystem Harness:** [[_EVAL/README|_EVAL/README.md]]  
> **Target Gateway:** [[42-EVALUATION/42-EVALUATION|42-EVALUATION.md]]  
> **System Shorthand / Alias:** `_eval`  
> **Status:** 🟢 ACTIVE — Operational Evaluation Hub (2026-09-06)

---

## 1. Executive Summary
The **Evaluation Domain** (`42-EVALUATION`, aliased as `_eval`) is the empirical verification layer of Company Brain. It validates whether AI models, routing agents, autonomous loop executions, software code, and business tools meet rigorous accuracy, latency, cost, and reliability thresholds before, during, and after production execution.

```text
┌─────────────────────────┐       ┌─────────────────────────┐
│  22-EXECUTION PIPELINE  │ ────► │  42-EVALUATION GATEWAY  │
│  (Tasks, Loops, Tools)  │       │ (Benchmarks, Receipts)  │
└─────────────────────────┘       └────────────┬────────────┘
                                               │
                      ┌────────────────────────┴────────────────────────┐
                      ▼                                                 ▼
        ┌───────────────────────────┐                     ┌───────────────────────────┐
        │   43-OUTCOMES ANALYSIS    │                     │   44-LEARNING FEEDBACK    │
        │ (Business Impact, Value)  │                     │ (Prompt Tuning, Heuristics)│
        └───────────────────────────┘                     └───────────────────────────┘
```

---

## 2. Four Pillars of Evaluation

### Pillar 1: Model Benchmarks & Inference Ground Truth
Evaluates frontier and local models served via [[_INFRASTRUCTURE/omniroute/README|OmniRoute]] and LiteLLM against empirical benchmarks per [[37-RESEARCH/AI-RESEARCH]]:
- **SWE-bench Verified:** Autonomous software engineering problem resolution (> 35% resolution threshold).
- **LiveCodeBench:** Uncontaminated, real-world Python/TypeScript algorithmic accuracy (> 45% pass@1).
- **AgentBench:** Complex multi-step tool invocation, error recovery, and environment interaction (> 70% success).
- **GPQA Diamond:** Graduate-level scientific reasoning and deep factual fidelity (> 55% zero-shot).
- **Needle-in-a-Haystack:** 128k+ multi-turn context retrieval (100% across all quadrants).
- **Primary Domain:** [[17-MODELS/17-MODELS|17-MODELS]] & [[37-RESEARCH/AI-RESEARCH|AI-RESEARCH.md]]

### Pillar 2: Agent Verification & Routing Scoring
Validates autonomous agents across all 3 autonomy tiers:
- **L1 (Human Propose):** Verifies report completeness and structured schema output.
- **L2 (Monitored Execution):** Shadow-tests retries, error budgets, and tool call accuracy.
- **L3 (Autonomous Execution):** Continuous automated guardrails and financial limit checks.
- **Dedicated Eval Agents:**
  - [[16-AGENTS/AGT-009-education-eval|AGT-009 (Education Eval Agent)]] — Measures curriculum alignment, quiz difficulty calibration, student comprehension metrics, and outcome analytics.
  - [[node/plans/course-generation-loop|Course Generation Loop]] — 7-step autonomous educational production pipeline.
- **Primary Domain:** [[16-AGENTS/README|16-AGENTS Hub]] & [[_REGISTRIES/agents/README|Agents Registry]]

### Pillar 3: Execution Loop Receipt Auditing
Automated cryptographic and telemetry audit of raw execution logs:
- **Receipt Streams:** [[receipts/receipts.jsonl]] and [[review-receipts/receipts.jsonl]].
- **Evaluated Parameters:** Request IDs, tool call validity, cost per step, execution duration, and signer verification.
- **Loop Integration:** Feeds directly into [[_PIPELINES/learning/README|Learning Pipeline (Stage 09)]] and [[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING|55-LOOP-ENGINEERING]].

### Pillar 4: Tool & Capability Evaluation
Evaluates external software packages, SaaS vendors, and internal libraries:
- **Tool Assessment Framework:** Governed by [[.agents/skills/testing-tool-evaluator/SKILL|testing-tool-evaluator skill]].
- **Evaluation Criteria:** Functional fit, total cost of ownership (TCO), vendor API stability, security attack surface, and maintenance toil.
- **Capabilities Matrix:** Grounded in [[14-CAPABILITIES/CAPABILITIES_INDEX|14-CAPABILITIES]].

---

## 3. Upstream & Downstream Integration Flow
- **Upstream (Inputs):**
  - Execution runtime: [[22-EXECUTION/22-EXECUTION]]
  - Loop orchestration: [[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING]] & [[fractal]]
  - Infrastructure runtime: [[56-ENGINEERING/README]] & [[CLAUDE.md]]
- **Downstream (Outputs):**
  - Outcome quantification: [[43-OUTCOMES/43-OUTCOMES]]
  - Knowledge extraction & memory updates: [[44-LEARNING/44-LEARNING]] & [[10-MEMORY/10-MEMORY]]
  - Evolutionary updates: [[45-EVOLUTION/45-EVOLUTION]]
- **Governance & Master Control:**
  - Master Control: [[50-MASTER-CONTROL/50-MASTER-CONTROL]] & [[50-MASTER-CONTROL/CONTROL_MATRIX]]
  - Operating Contract: [[ANTIGRAVITY.md]]
