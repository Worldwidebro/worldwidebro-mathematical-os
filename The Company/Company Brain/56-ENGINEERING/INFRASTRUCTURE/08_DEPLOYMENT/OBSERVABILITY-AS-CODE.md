---
id: DOC-08-DEP-016
aliases: ['OBSERVABILITY-AS-CODE']
tags: ['deployment', 'observability-as-code', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/08_DEPLOYMENT/DEPLOYMENT|DEPLOYMENT]] | [[_REGISTRIES/infrastructure_dependency_registry.json]]

# Observability-as-Code (OaC) Layer

> **Authority:** CP-027 | **Standard:** NIST SP 800-204C | **Status:** ACTIVE

## NIST SP 800-204C Separation
Observability concerns are codified into version-controlled declarations:
- Declarative Grafana dashboard definitions (`dashboards.json`).
- Prometheus alerting thresholds (`alerts.yml`).
- OpenTelemetry span instrumentation rules.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/08_DEPLOYMENT/DEPLOYMENT|DEPLOYMENT]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/infrastructure_dependency_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]]
- [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/SECURITY-INFRASTRUCTURE|SECURITY-INFRASTRUCTURE]]
- [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/FAILOVER|FAILOVER]]
- [[_REGISTRIES/infrastructure_dependency_registry.json|infrastructure_dependency_registry.json]]
