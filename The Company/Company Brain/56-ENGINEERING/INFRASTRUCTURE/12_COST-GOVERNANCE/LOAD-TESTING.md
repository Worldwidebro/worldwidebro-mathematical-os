---
id: DOC-LOAD-TEST-001
aliases: ['LOAD-TESTING']
tags: ['testing', 'performance', 'benchmarks']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Load Testing Suites & Benchmarks

> **Authority:** CP-027  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Load Testing Protocols
- Regular benchmark validation of `qwen2.5-coder:14b` achieving 45 tokens/sec decode throughput.
- Concurrent synthetic prompt generation via `k6` and `curl` against local OmniRoute gateway (`:20128`).

## 2. Connected Documents
- Stress Testing: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/STRESS-TESTING|STRESS-TESTING.md]]
- Performance Engineering: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/PERFORMANCE-ENGINEERING|PERFORMANCE-ENGINEERING.md]]
- LLM Hardware Benchmarks: [LLM Hardware Registry](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_REGISTRIES/LLM_HARDWARE_COMPATIBILITY_REGISTRY.yaml)
