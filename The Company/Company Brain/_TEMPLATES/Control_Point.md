---
id: TPL-CP-001
title: "Template: Control Point Specification"
type: template
category: control-point
tags: [template, control-point, governance, master-control]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_TEMPLATES/README|Templates Gallery]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|Master Control]] | [[_REGISTRIES/control-points.md|Control Points Registry]]

# Control Point: {{name}}

**Domain:** [[{{domain}}]]  
**Layer:** {{layer}}  
**Status:** {{status}}

## Description

[What does this control point do?]

## Required Components

- **Algorithm:** {{algorithm}}
- **Model:** {{model}}
- **Database:** {{database}}
- **Agent:** {{agent}}
- **Skill:** {{skill}}
- **Tool:** {{tool}}
- **Confidence Scoring:** {{confidence}}
- **Provenance Tracking:** {{provenance}}
- **Audit Log:** {{audit}}

## Current Implementation

- **Repository:** {{repo}}
- **Capability:** {{capability}}
- **Agent:** {{agent_name}}
- **Model:** {{model_name}}
- **Tool:** {{tool_name}}

### Implementation Status

- [ ] Algorithm defined
- [ ] Model trained/selected
- [ ] Database schema created
- [ ] Agent integrated
- [ ] Skill documented
- [ ] Tool configured
- [ ] Testing completed
- [ ] Monitoring enabled

## Inputs

[What data/signals feed into this?]

## Outputs

[What data/signals does this produce?]

## Metrics

- Success rate: {{success_rate}}
- Latency: {{latency}}
- Cost per operation: {{cost}}
- Accuracy: {{accuracy}}

## Dependencies

- Upstream: [[control-point-X]]
- Downstream: [[control-point-Y]]

## Risks

- [Risk 1]
- [Risk 2]

## Last Updated

{{date}}

---

**Tags:** #control-point #{{domain}}

---

## Template Context & Registries
- Master Gallery: [[_TEMPLATES/README|Templates Gallery]]
- Master Control Matrix: [[50-MASTER-CONTROL/CONTROL_MATRIX]]
- Canonical Control Points: [[_REGISTRIES/control-points.md]]
