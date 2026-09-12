---
id: TOOL-GSTACK-001
title: GStack — Garry Tan's 23-Role AI Engineering Stack
aliases: ["GStack", "gstack", "garrytan/gstack", "Garry Tan Stack"]
tags: [tools, gstack, workflows, roles, make-pdf]
status: ACTIVE
updated: 2026-09-12
---

[[STARTHERE]] | [[AGENTS]] | [[START-HERE-AGENTS]] | [[16-AGENTS/README|16-AGENTS]] | [[13_ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[INDEX]]

# GStack (`garrytan/gstack`)

**Authority:** CP-006 (Agents) & CP-027 (Infrastructure)  
**Status:** ✅ `INSTALLED & OPERATIONAL` (`_TOOLS/gstack`, publication engine at `scripts/make-pdf`)  
**Repository:** Local clone at `_TOOLS/gstack` with fully installed `node_modules` and compiled CLI tools.

---

## 1. System Overview
GStack is Garry Tan's opinionated agent workflow suite organizing an AI assistant into a specialized 23-member virtual organization. It enforces structured lifecycle workflows: strategy, UX design, engineering review, QA automation, document publishing, and release management.

## 2. Core Modules & Tools
- **Publication Engine (`make-pdf`):** Headless Playwright Chromium + CSS Paged Media + KaTeX + Mermaid vector rendering (`scripts/make-pdf`).
- **Strategic Roles:**
  - `/office-hours`: Founder strategic framing and market thesis stress-testing.
  - `/plan-ceo-review`: Strategic feature feedback and alignment against North Star.
- **Engineering & Review Roles:**
  - `/review`: Rigorous branch code review and git diff inspection.
  - `/qa [url]`: Headless browser testing and DOM validation.
  - `/ship`: Release safety verification and changelog generation.

## 3. CLI Invocations
```bash
./scripts/make-pdf generate <input.md> [output.pdf]    # Render vector print PDF
./scripts/make-pdf preview <input.md>                  # Live HTML browser preview
```
