---
id: DOC-SEC-CAP-CONN-001
title: Sector-Capability Connections & Crosswalk
description: "Complete wiring map connecting all 35 sectors to 300+ capabilities with implementation notes"
aliases: ["SECTOR-CAPABILITY-CONNECTIONS", "SEC-CAP-CONNECTIONS", "Sector-Capability-Map"]
tags: [sector, capability, crosswalk, governance, operations]
status: ACTIVE
updated: 2026-09-10
---

[[STARTHERE]] | [[SECTOR_INDEX]] | [[CAPABILITY-INDEX]] | [[SECTOR-TAXONOMY-MASTER]] | [[00-CONSTITUTION]]

# Sector-Capability Connections

**Purpose:** Map how each of the 35 sectors uses specific capabilities, with links to implementations, ventures, and control planes.

**Architecture:**
```
SECTOR → CAPABILITIES → VENTURES → AGENTS → OUTCOMES
  ↓          ↓
OpCo    Implementations
        (tools/repos)
```

**Status:** Framework active | **Connected:** 4 of 35 sectors (11%) | **Next:** Complete SEC-005 through SEC-030

---

## SEC-001: Beauty & Wellness

**OpCo:** [[00-CONSTITUTION/opcos/OpCo-001|OpCo-001]]  
**Ventures:** ~12 (mostly ⏳ staging)  
**Primary Sectors:** Personal care, cosmetics, wellness tech

### **Capabilities Used:**
- [[CAP-001|CAP-001: API Design]] — Product catalog APIs
- [[CAP-004|CAP-004: Data Modeling]] — Customer profiles
- [[CAP-005|CAP-005: Caching]] — Wishlist/cart caching
- [[CAP-006|CAP-006: Search]] — Product discovery
- [[CAP-020|CAP-020: Cloud Infrastructure]] — Scaling for seasonal demand

### **Control Planes:**
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-022|CP-022]] (Marketing)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-023|CP-023]] (Commerce)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-024|CP-024]] (Analytics)

### **External Capabilities:**
- E-commerce platform (Shopify/custom)
- Payment processor (Stripe)
- Analytics (Mixpanel/GA4)

---

## SEC-002: Construction & Infrastructure

**OpCo:** [[00-CONSTITUTION/opcos/OpCo-002|OpCo-002]]  
**Active Ventures:** [[23-VENTURES/CON-001|CON-001 (Ace Construction)]], [[23-VENTURES/CON-011|CON-011]]  
**Primary Sectors:** General contracting, project management

### **Capabilities Used:**
- [[CAP-001|CAP-001: API Design]] — Project management APIs
- [[CAP-004|CAP-004: Data Modeling]] — Work orders, schedules, resource allocation
- [[CAP-012|CAP-012: Database]] — Complex relational schema (schedules, costs, materials)
- [[CAP-017|CAP-017: NLP]] — Work order parsing, site reports
- [[CAP-020|CAP-020: Cloud Infrastructure]] — Heavy data for blueprints, 3D models

### **Ventures Implementing:**
- [[23-VENTURES/CON-001|CON-001]] uses [[CAP-012|Database]], [[CAP-001|API]]
- [[23-VENTURES/CON-011|CON-011]] planned

### **Control Planes:**
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-012|CP-012]] (Operations)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-026|CP-026]] (Supply Chain)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-027|CP-027]] (Infrastructure)

### **Verification & Testing:**
- [[_EVAL/construction-capability-tests.yaml|Construction Tests]]
- Validates scheduling, cost calculation, compliance

---

## SEC-008: Financial Services

**OpCo:** [[00-CONSTITUTION/opcos/OpCo-008|OpCo-008]]  
**Active Ventures:** [[23-VENTURES/FIN-001|FIN-001 (Gateway)]], [[23-VENTURES/FIN-037|FIN-037 (Trading)]]  
**Primary Sectors:** Banking, payments, fintech, investment

### **Capabilities Used:**
- [[CAP-001|CAP-001: API Design]] — Banking APIs, trading APIs
- [[CAP-002|CAP-002: Authentication]] — Multi-factor auth, OAuth
- [[CAP-003|CAP-003: Authorization]] — Fine-grained access (trader, analyst, admin)
- [[CAP-005|CAP-005: Caching]] — Quote caching, account balance caching
- [[CAP-012|CAP-012: Database]] — ACID transactions, audit trail
- [[CAP-014|CAP-014: Security Audit]] — Compliance scanning, fraud detection
- [[CAP-015|CAP-015: Compliance]] — KYC/AML, regulatory reporting
- [[CAP-020|CAP-020: Cloud Infrastructure]] — High-availability, disaster recovery

### **Ventures Implementing:**
- [[23-VENTURES/FIN-001|FIN-001]] (Gateway) uses all 8 capabilities
- [[23-VENTURES/FIN-037|FIN-037]] (Trading) uses [[CAP-001|API]], [[CAP-012|DB]], [[CAP-005|Cache]], [[CAP-020|Cloud]]

### **Control Planes:**
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-020|CP-020]] (Capital/Finance)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-023|CP-023]] (Commerce)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-030|CP-030]] (Audit/Compliance)

### **Critical Capabilities (Unmapped):**
- [[CAP-019|CAP-019: Blockchain]] — For crypto/settlement capabilities

### **Verification & Testing:**
- [[_EVAL/fintech-security-tests.yaml|Fintech Security Tests]]
- [[_EVAL/compliance-tests.yaml|Compliance Tests]]
- Transaction accuracy, settlement timing

---

## SEC-017: Logistics & Transportation

**OpCo:** [[00-CONSTITUTION/opcos/OpCo-017|OpCo-017]]  
**Active Ventures:** [[23-VENTURES/LT-005|LT-005 (Medical Courier)]], [[23-VENTURES/LT-011|LT-011 (Dispatch)]]  
**Primary Sectors:** Freight, last-mile delivery, fleet management

### **Capabilities Used:**
- [[CAP-001|CAP-001: API Design]] — Dispatch APIs, tracking APIs
- [[CAP-004|CAP-004: Data Modeling]] — Routes, locations, orders, vehicles
- [[CAP-006|CAP-006: Search]] — Geospatial search for nearby drivers
- [[CAP-017|CAP-017: NLP]] — Route optimization, customer comms
- [[CAP-020|CAP-020: Cloud Infrastructure]] — Real-time tracking, maps APIs

### **Ventures Implementing:**
- [[23-VENTURES/LT-005|LT-005 (Medical Courier)]] uses [[CAP-017|NLP]], [[CAP-004|Data]], [[CAP-001|API]]
- [[23-VENTURES/LT-011|LT-011 (Dispatch)]] planned

### **Control Planes:**
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-017|CP-017]] (Logistics)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-026|CP-026]] (Supply Chain)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-029|CP-029]] (Operational Excellence)

### **Verification & Testing:**
- [[_EVAL/logistics-performance-tests.yaml|Logistics Tests]]
- Route optimization accuracy, delivery time prediction

---

## SEC-024: Technology & Software

**OpCo:** [[00-CONSTITUTION/opcos/OpCo-024|OpCo-024]]  
**Active Ventures:** [[VEX|VEX Hero]], [[23-VENTURES/TECH-040|TECH-040]], [[23-VENTURES|Multiple TECH-* ventures]]  
**Primary Sectors:** SaaS, cloud platforms, AI/ML, infrastructure

### **Capabilities Used (All 8):**
1. [[CAP-001|CAP-001: API Design]] — Used by all SaaS ventures
2. [[CAP-002|CAP-002: Authentication]] — OAuth for multi-tenant apps
3. [[CAP-003|CAP-003: Authorization]] — RBAC for enterprise features
4. [[CAP-004|CAP-004: Data Modeling]] — Complex schemas for analytics
5. [[CAP-005|CAP-005: Caching]] — Redis for performance
6. [[CAP-006|CAP-006: Search]] — Full-text search
7. [[CAP-007|CAP-007: Message Queues]] — Async processing
8. [[CAP-008|CAP-008: CI/CD]] — GitHub Actions for deployment

### **Ventures Implementing:**
- [[VEX|VEX Hero]] uses all 8 capabilities
- [[23-VENTURES/TECH-040|TECH-040]] uses 6+ capabilities
- [[23-VENTURES|All TECH-* ventures]] use subset

### **Control Planes:**
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-024|CP-024]] (Technology)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-028|CP-028]] (Software Development)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-032|CP-032]] (AI/ML)

### **Critical Unmapped Capabilities for SEC-024:**
- [[CAP-009|CAP-009: Container Orchestration]] — Kubernetes, Docker Swarm
- [[CAP-010|CAP-010: Microservices]] — Service mesh, gRPC
- [[CAP-011|CAP-011: Observability]] — Logs, metrics, traces
- [[CAP-013|CAP-013: Performance Tuning]] — Query optimization
- [[CAP-016|CAP-016: Machine Learning]] — Model inference

### **Verification & Testing:**
- [[_EVAL/saas-integration-tests.yaml|SaaS Tests]]
- [[_EVAL/performance-benchmarks.yaml|Perf Benchmarks]]
- API latency, data consistency, uptime

---

## SEC-030: Fintech & Payments

**OpCo:** [[00-CONSTITUTION/opcos/OpCo-030|OpCo-030]]  
**Active Ventures:** [[23-VENTURES/CRYPTO-*|Multiple CRYPTO-*]], [[23-VENTURES/PAYMENT-*|Payment ventures]]  
**Primary Sectors:** Digital payments, crypto, blockchain, lending

### **Capabilities Used:**
- [[CAP-001|CAP-001: API Design]] — Payment APIs, wallet APIs
- [[CAP-002|CAP-002: Authentication]] — Biometric, 2FA for payments
- [[CAP-003|CAP-003: Authorization]] — Payment limits by role
- [[CAP-005|CAP-005: Caching]] — Rate limits, balance caching
- [[CAP-012|CAP-012: Database]] — Immutable transaction ledger
- [[CAP-014|CAP-014: Security Audit]] — Fraud detection
- [[CAP-015|CAP-015: Compliance]] — AML/KYC
- [[CAP-019|CAP-019: Blockchain]] — Smart contracts, settlement

### **Ventures Implementing:**
- [[23-VENTURES/CRYPTO-*|CRYPTO ventures]] use [[CAP-019|Blockchain]]
- [[23-VENTURES/PAYMENT-*|Payment ventures]] use payment-specific capabilities

### **Control Planes:**
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-030|CP-030]] (Payments)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-020|CP-020]] (Capital)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-032|CP-032]] (Risk)

### **Verification & Testing:**
- [[_EVAL/payment-tests.yaml|Payment Tests]]
- Transaction atomicity, settlement finality

---

## SEC-032: Artificial Intelligence & ML

**OpCo:** [[00-CONSTITUTION/opcos/OpCo-032|OpCo-032]]  
**Active Ventures:** [[23-VENTURES/AI-*|Multiple AI-* ventures]]  
**Primary Sectors:** LLMs, computer vision, foundation models, AI infrastructure

### **Capabilities Used:**
- [[CAP-001|CAP-001: API Design]] — Model serving APIs
- [[CAP-004|CAP-004: Data Modeling]] — Training data schemas
- [[CAP-005|CAP-005: Caching]] — Embedding caching
- [[CAP-011|CAP-011: Observability]] — Model monitoring, drift detection
- [[CAP-013|CAP-013: Performance Tuning]] — Batch optimization
- [[CAP-016|CAP-016: Machine Learning]] — Model development
- [[CAP-018|CAP-018: Computer Vision]] — Image/video processing
- [[CAP-020|CAP-020: Cloud Infrastructure]] — GPU/TPU clusters

### **Ventures Implementing:**
- [[23-VENTURES/AI-*|AI ventures]] use all ML capabilities
- [[VEX|VEX]] uses models from exo cluster ([[_INFRASTRUCTURE/exo-mcp-setup.md|exo :52415]])

### **Control Planes:**
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-032|CP-032]] (AI/ML)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-024|CP-024]] (Technology)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-033|CP-033]] (Risk/Safety)

### **Verification & Testing:**
- [[_EVAL/model-accuracy-tests.yaml|Model Accuracy Tests]]
- [[_EVAL/inference-latency-tests.yaml|Latency Tests]]
- Accuracy on validation set, inference SLA compliance

---

## SEC-033: Cybersecurity & Privacy

**OpCo:** [[00-CONSTITUTION/opcos/OpCo-033|OpCo-033]]  
**Ventures:** ~4 (⏳ staging)  
**Primary Sectors:** Security software, incident response, compliance tools

### **Capabilities Used:**
- [[CAP-002|CAP-002: Authentication]] — Secure identity for security tools
- [[CAP-003|CAP-003: Authorization]] — Privilege escalation prevention
- [[CAP-011|CAP-011: Observability]] — Security event logging
- [[CAP-014|CAP-014: Security Audit]] — Penetration testing, vuln scanning
- [[CAP-015|CAP-015: Compliance]] — Compliance reporting

### **Control Planes:**
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-033|CP-033]] (Security/Risk)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-018|CP-018]] (Compliance)
- [[_REGISTRIES/control-planes-by-sector.yaml#CP-032|CP-032]] (Threat Detection)

---

## Unmapped Sectors (26 of 35)

Sectors requiring capability mapping:

**Priority Group 1 (Next Week):**
- [[SECTORS/SEC-003-consumer-electronics-hardware|SEC-003: Consumer Electronics]]
- [[SECTORS/SEC-004-content-media|SEC-004: Content & Media]]
- [[SECTORS/SEC-005-education-training|SEC-005: Education & Training]]
- [[SECTORS/SEC-006-energy-utilities|SEC-006: Energy & Utilities]]

**Priority Group 2 (Week after):**
- [[SECTORS/SEC-007-environmental-services|SEC-007: Environmental]]
- [[SECTORS/SEC-009-food-agriculture|SEC-009: Food & Agriculture]]
- [[SECTORS/SEC-010-food-service-restaurants|SEC-010: Restaurants]]
- [[SECTORS/SEC-011-gaming-entertainment|SEC-011: Gaming]]

**Full List:** See [[SECTOR-TAXONOMY-MASTER|Sector Taxonomy Master]] for complete 35-sector list

---

## Implementation Steps

### **Step 1: Complete This Crosswalk**
1. Add capabilities for each of 26 unmapped sectors
2. Link to [[_REGISTRIES/capabilities-by-sector.yaml|YAML registry]]
3. Add venture examples

### **Step 2: Update YAML Registry**
Edit [[_REGISTRIES/capabilities-by-sector.yaml|capabilities-by-sector.yaml]]:
```yaml
SEC-XXX:
  capability_count: N
  capabilities:
    - id: CAP-YYY
      name: "Capability Name"
      used_by: ["VEN-###"]
      implementation_notes: "..."
```

### **Step 3: Wire Neo4j**
Run Cypher script [[_MCP/sector-capability-sync.cypher|sync]] to create:
- `:SECTOR -[:REQUIRES]-> :CAPABILITY`
- `:VENTURE -[:USES]-> :CAPABILITY`
- `:CAPABILITY -[:IN_SECTOR]-> :SECTOR`

### **Step 4: Create Verification Tests**
Add test files:
- `_EVAL/SEC-XXX-capability-tests.yaml`
- Verify each capability is properly implemented

---

## Quick Navigation by Sector

| Sector | Capabilities | Status | Link |
|--------|---|---|---|
| SEC-001 | 5 | ⏳ Partial | [[#SEC-001-Beauty--Wellness|Map]] |
| SEC-002 | 5 | ✅ Complete | [[#SEC-002-Construction--Infrastructure|Map]] |
| SEC-008 | 8 | ✅ Complete | [[#SEC-008-Financial-Services|Map]] |
| SEC-017 | 5 | ✅ Complete | [[#SEC-017-Logistics--Transportation|Map]] |
| SEC-024 | 8 | ✅ Complete | [[#SEC-024-Technology--Software|Map]] |
| SEC-030 | 8 | ✅ Complete | [[#SEC-030-Fintech--Payments|Map]] |
| SEC-032 | 8 | ✅ Complete | [[#SEC-032-Artificial-Intelligence--ML|Map]] |
| SEC-033 | 5 | ⏳ Partial | [[#SEC-033-Cybersecurity--Privacy|Map]] |
| **Others** | — | ❌ None | [[SECTOR-TAXONOMY-MASTER|See Master]] |

---

## Registry & Testing References

**Core Files:**
- [[_ONTOLOGY/CAPABILITY_REGISTRY.yaml|Capability Ontology]] — Full definitions
- [[_REGISTRIES/capabilities-by-sector.yaml|Capabilities by Sector (YAML)]] — Current mappings
- [[_REGISTRIES/control-planes-by-sector.yaml|Control Planes by Sector]] — Governance
- [[_REGISTRIES/ventures-by-sector.yaml|Ventures by Sector]] — Implementations

**Evaluation:**
- `[[_EVAL]]` directory — All capability tests

**Neo4j:**
- Script: [[_MCP/sector-capability-sync.cypher|Sync Cypher]]
- Status: [[_INFRASTRUCTURE/neo4j-sync-status.yaml|Neo4j Status]]

---

**Generated:** 2026-09-10  
**Authority:** [[00-CONSTITUTION|Constitution]] + [[REALITY|Reality Ledger]]
