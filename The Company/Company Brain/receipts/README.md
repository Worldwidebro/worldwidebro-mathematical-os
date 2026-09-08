---
id: PORTAL-RECEIPTS-001
title: "receipts/ — Operational Telemetry & Cryptographic Receipt Log"
aliases: ["receipts", "receipts/README", "Receipts Log", "Execution Receipts"]
tags: ["receipts", "telemetry", "audit", "execution", "grading"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[_EVAL/README|Operational Evaluation Hub]] | [[42-EVALUATION/README|42-EVALUATION]] | [[44-LEARNING/44-LEARNING|44-LEARNING]]

# receipts/ — Operational Telemetry & Cryptographic Receipt Log

> **Authority:** Performance & Quality Control Plane ([[50-MASTER-CONTROL/50-MASTER-CONTROL|CP-028]])  
> **Primary Ledger:** `receipts/receipts.jsonl`  
> **Status:** 🟢 ACTIVE — Operational Receipts Stream (2026-09-06)

---

## 1. Executive Summary

The **`receipts/`** directory contains the raw JSON Lines ledger (`receipts.jsonl`) recording cryptographic receipts for all autonomous agent tool executions, subagent dispatches, and pipeline transactions:
- **Timestamp & Trace**: Microsecond-precision ISO-8601 execution stamps.
- **Tool Invocations**: Input payloads, exit codes, and stdout hashes.
- **Resource Consumption**: Input tokens, output tokens, latency, and estimated dollar costs.
- **Signer Identity**: Subagent ID and cryptographic verification signatures.
- **Evaluation**: Graded continuously by [[_EVAL/README|Operational Evaluation Hub]].
