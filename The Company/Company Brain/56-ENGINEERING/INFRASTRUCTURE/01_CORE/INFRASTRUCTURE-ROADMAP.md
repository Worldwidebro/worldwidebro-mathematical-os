---
id: DOC-01-ROAD-001
aliases: ['INFRASTRUCTURE-ROADMAP']
tags: ['roadmap', 'milestones', 'evolution', 'core']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]] | [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]

# Infrastructure Engineering Roadmap

> **Authority:** CP-027  
> **Status:** ACTIVE  
> **Updated:** 2026-09-05

## Phase 1: Clean Up Clutter & Fix Dead Weight (Week 1)
- [x] Audit live running state across Docker contexts (`CLAUDE.md`).
- [ ] Decommission `t7shield-neo4j-1` crash-looping container.
- [ ] Consolidate Mac Studio Docker containers to single canonical compose file.
- [ ] Fix LiteLLM broken embeddings route.
- [ ] Connect LiteLLM callback to Langfuse on port 3003.

## Phase 2: Complete Canonical Declarations (Week 2)
- [x] Establish complete 12-domain `56-ENGINEERING/INFRASTRUCTURE/` subsystem.
- [x] Emit all 23 machine-readable JSON registries in `_REGISTRIES/`.
- [ ] Implement automated drift detection script (`scripts/audit_infra_drift.py`).

## Phase 3: NIST SP 800-204C DevSecOps Automation (Week 3)
- [ ] Implement Policy-as-Code rules via Conftest/Rego in `08_DEPLOYMENT/`.
- [ ] Implement Observability-as-Code Grafana dashboard provisioning.
- [ ] Automate daily backup snapshot verification to LaCie and T7 Shield.

## Phase 4: High Availability & Failover Readiness (Week 4)
- [ ] Configure automatic failover route from Mac Studio to MacBook Air.
- [ ] Conduct chaos testing simulating Mac Studio offline state.

## Connected Documents & Registries
- Core Subsystem Hub: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Reality Verification: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE-REALITY|INFRASTRUCTURE-REALITY.md]]
- Infrastructure Registry: [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]
- Compute Architecture: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Storage Architecture: [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- Network Architecture: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
