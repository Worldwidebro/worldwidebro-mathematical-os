---
id: DOC-08-DEP-018
aliases: ['POLICY-AS-CODE']
tags: ['deployment', 'policy-as-code', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/08_DEPLOYMENT/DEPLOYMENT|DEPLOYMENT]] | [[_REGISTRIES/infrastructure_dependency_registry.json]]

# Policy-as-Code (PaC) Layer

> **Authority:** CP-027 | **Standard:** NIST SP 800-204C | **Status:** ACTIVE

## NIST SP 800-204C Separation
Policy-as-Code operates independently of resource provisioning. Guardrails are evaluated using OPA (Open Policy Agent) and Conftest:
- Rule 1: No containers run as root user.
- Rule 2: No public ports exposed on local hosts.
- Rule 3: All persistent databases must mount to `/Volumes/LaCie`.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/08_DEPLOYMENT/DEPLOYMENT|DEPLOYMENT]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/infrastructure_dependency_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]]
- [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/SECURITY-INFRASTRUCTURE|SECURITY-INFRASTRUCTURE]]
- [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/FAILOVER|FAILOVER]]
- [[_REGISTRIES/infrastructure_dependency_registry.json|infrastructure_dependency_registry.json]]
