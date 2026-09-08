---
id: REG-AGENTS-HUB
title: "Canonical Agents Registry Index"
aliases: ["Agents Registry", "_REGISTRIES/agents"]
tags: [registry, agents, routing-agents, yaml-specs]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[16-AGENTS/README|16-AGENTS]] | [[_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml|Capabilities]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|Master Control]]

# Canonical Agents Registry

Canonical directory of routing and execution agent specifications across Company Brain.

## Registered Routing Agents

| Agent ID | YAML Specification | Routing Key | Purpose | Obsidian Gateway |
|:---|:---|:---|:---|:---|
| `AGT-001` | `AGT-001-venture-pm.yaml` | `venture-pm` | Venture Project Management & Milestone Tracking | [[16-AGENTS/AGT-001-venture-pm]] |
| `AGT-002` | `AGT-002-financial.yaml` | `financial` | Revenue Activation & Financial Modeling | [[16-AGENTS/AGT-002-financial]] |
| `AGT-003` | `AGT-003-technical.yaml` | `technical` | Infrastructure & Technical Orchestration | [[16-AGENTS/AGT-003-technical]] |
| `AGT-004` | `AGT-004-sales.yaml` | `sales` | Sales Qualification & Outbound Pipeline | [[16-AGENTS/AGT-004-sales]] |
| `AGT-005` | `AGT-005-operations.yaml` | `operations` | Operations Automation & Workflow Routing | [[16-AGENTS/AGT-005-operations]] |
| `AGT-006` | `AGT-006-education-teacher.yaml` | `education-teacher` | Curriculum Planning & Presentation Deck Scaffolding | [[16-AGENTS/AGT-006-education-teacher]] |
| `AGT-007` | `AGT-007-education-peer.yaml` | `education-peer` | Student Collaboration & Peer Discussion Prompts | [[16-AGENTS/AGT-007-education-peer]] |
| `AGT-008` | `AGT-008-education-content.yaml` | `education-content` | Quiz Item Banking & Interactive Widget Design | [[16-AGENTS/AGT-008-education-content]] |
| `AGT-009` | `AGT-009-education-eval.yaml` | `education-eval` | Assessment Scoring, Outcomes & Learning Analytics | [[16-AGENTS/AGT-009-education-eval]] |

---

## Schema Standard
Agent specifications are stored in YAML format defining `agent_id`, `routing_key`, `type`, `autonomy_levels`, `capabilities_implemented`, `cost_model`, and `control_plane_mappings`.
