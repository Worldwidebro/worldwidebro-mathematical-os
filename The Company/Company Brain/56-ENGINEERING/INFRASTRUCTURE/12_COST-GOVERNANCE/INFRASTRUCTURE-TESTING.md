---
id: DOC-INFRA-TEST-001
aliases: ['INFRASTRUCTURE-TESTING']
tags: ['testing', 'verification', 'qa']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Infrastructure Verification & Testing Suites

> **Authority:** CP-027 & CP-042  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Automated Test Suites
- End-to-end routing validation via FastMCP tool `test_e2e()`.
- Model response latency checks via `_CLI/bin/cb test models`.

## 2. Connected Documents
- Validation Protocols: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-VALIDATION|INFRASTRUCTURE-VALIDATION.md]]
- FastMCP Server: [FastMCP Server](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_MCP/fastmcp_server.py)
- Testing Domain: [[42-EVALUATION/42-EVALUATION|42-EVALUATION]]
