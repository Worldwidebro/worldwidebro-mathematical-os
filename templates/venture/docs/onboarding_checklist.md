---
name: templates/venture/docs/onboarding_checklist
title: 'Onboarding & Setup Checklist: {{VENTURE_NAME}} ({{VENTURE_ID}})'
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Onboarding & Setup Checklist: {{VENTURE_NAME}} ({{VENTURE_ID}})

- [ ] **Phase 1: Legal & Structural**
  - [ ] Incorporate tax-entity structure.
  - [ ] Assign Dynasty Trust and Governance Council.
  - [ ] Sign Mutual Synergy Agreement.

- [ ] **Phase 2: Technical Setup**
  - [ ] Mount workspace directories.
  - [ ] Link GitHub repository: `{{GITHUB_URL}}`.
  - [ ] Register credentials in Supabase `agent_credentials`.

- [ ] **Phase 3: Database & Graph Injection**
  - [ ] Verify node creation in Neo4j.
  - [ ] Connect parent OPCO (`{{PARENT_OPCO}}`) capital allocations.
  - [ ] Run test execution cycle (`venture_loop.py`).
