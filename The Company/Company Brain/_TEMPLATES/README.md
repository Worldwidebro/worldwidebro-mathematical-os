---
id: TEMPLATES-MASTER-HUB
title: "Templates & Blueprints Gallery"
aliases: ["Templates Gallery", "_TEMPLATES", "Templates Hub"]
tags: [templates, blueprints, scaffolding, governance]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[07-ONTOLOGY/README|Ontology]] | [[46-GOVERNANCE/README|Governance]] | [[REALITY]]

# Templates & Blueprints Gallery

> **Authority:** System Architecture & Governance Control Plane ([[50-MASTER-CONTROL/50-MASTER-CONTROL|CP-027]])  
> **Master Contract:** [[ANTIGRAVITY.md]] | [[REALITY.md]]  
> **Location:** `_TEMPLATES/`  
> **Status:** 🟢 ACTIVE — Canonical Template System (2026-09-06)

---

## 1. Overview
The `_TEMPLATES/` directory contains the authoritative blueprint specifications for creating new entities within Company Brain. All autonomous agents, engineers, and executive processes must instantiate new domains, ventures, capabilities, control points, sites, and web properties strictly conforming to these templates to maintain topological and ontological integrity.

---

## 2. Canonical Blueprint Gallery

| Blueprint Template | Entity Type | Identifier Pattern | Primary Governance / Registry | Description |
|:---|:---|:---|:---|:---|
| [[_TEMPLATES/VENTURE_TEMPLATE\|VENTURE_TEMPLATE.md]] | Master Venture Spec | `VEN-*` / `LT-*` | [[REALITY]] • [[23-VENTURES/23-VENTURES]] • [[_REGISTRIES/VENTURE_REGISTRY.yaml]] | 8-section master commercial specification with mandatory REALITY.md verification gates, unit economics, ICP personas, and traction metrics. |
| [[_TEMPLATES/DOMAIN_TEMPLATE\|DOMAIN_TEMPLATE.md]] | Domain Name Asset | `DOM-*` | `_REGISTRIES/domain_registry.json` • [[56-ENGINEERING/README]] | Canonical asset record for root domains and DNS configurations, registrar ownership, expiration dates, and nameservers. |
| [[_TEMPLATES/SITE_TEMPLATE\|SITE_TEMPLATE.md]] | Digital Property | `SITE-*` | [[_REGISTRIES/CANONICAL/SITES_REGISTRY.yaml|SITES_REGISTRY.yaml]] • [[23-VENTURES/23-VENTURES]] | Canonical web application and portal asset specification detailing hosting (Vercel), frontend/backend stack, routes, and commerce engines. |
| [[_TEMPLATES/URL_TEMPLATE\|URL_TEMPLATE.md]] | Canonical URL Asset | `URL-*` | `_REGISTRIES/domain_registry.json` • [[56-ENGINEERING/README]] | Canonical endpoint record detailing protocol, port, CDN provider, SSL status, and repository-to-deployment bindings. |
| [[_TEMPLATES/Domain\|Domain.md]] | Operating Domain | `00-` to `50-` | [[07-ONTOLOGY/README]] • [[50-MASTER-CONTROL/50-MASTER-CONTROL]] | Functional operating domain gateway specifying concepts, sub-domains, upstream/downstream boundaries, and active control points. |
| [[_TEMPLATES/Capability\|Capability.md]] | Technical Capability | `CAP-*` | [[14-CAPABILITIES/CAPABILITIES_INDEX]] • [[15-SKILLS/README]] | Technical capability definition specifying implementation repositories, API schemas, SLAs (latency, throughput), and testing coverage. |
| [[_TEMPLATES/Control_Point\|Control_Point.md]] | Operational Control Point | `CP-*` | [[_REGISTRIES/control-points.md]] • [[50-MASTER-CONTROL/CONTROL_MATRIX]] | Operational control point requiring all 9 canonical components: Algorithm, Model, Database, Agent, Skill, Tool, Confidence, Provenance, and Audit Log. |

---

## 3. Scaffolding Rules & Guidelines
1. **Never Omit Frontmatter:** Every generated markdown document in the vault must start with a valid YAML frontmatter block containing at minimum `id`, `title`, `tags`, and `status`.
2. **Preserve Mustache Tokens in Blueprints:** Inside `_TEMPLATES/`, all `{{variable}}` placeholders must be preserved for runtime substitution by scaffolding scripts.
3. **Tripartite Link Minimum:** Every new entity instantiated from a template must immediately include at least 3 outbound links (upstream parent, master index, and related capability/registry).
4. **Reality Verification:** Any venture record created from `VENTURE_TEMPLATE.md` must default to `classification: SPECULATIVE` and `evidence_level: UNVERIFIED` until executable proof of revenue or traction is logged per [[REALITY.md]].

---

## 4. Connected Domains & Hubs
- **Constitutional Orientation:** [[STARTHERE]]
- **Master Domain Index:** [[INDEX]]
- **Ontological Foundations:** [[07-ONTOLOGY/README|07-ONTOLOGY]]
- **Governance & Policy:** [[46-GOVERNANCE/README|46-GOVERNANCE]]
- **Master Control Hub:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
- **Technical Capabilities:** [[14-CAPABILITIES/CAPABILITIES_INDEX|14-CAPABILITIES]]
- **Ventures Portfolio:** [[23-VENTURES/23-VENTURES|23-VENTURES]]
