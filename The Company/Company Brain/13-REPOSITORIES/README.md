[[STARTHERE]] | [[INDEX]] | [[00-CONSTITUTION/control-planes/CP-028|CP-028: Repositories]] | [[00-CONSTITUTION/control-planes/CP-027|CP-027: Infrastructure]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|Master Control]]

# 13-REPOSITORIES

> **Authority:** [[00-CONSTITUTION/control-planes/CP-028|CP-028: Application]]  
> **Governing Framework:** [[00-CONSTITUTION/CONTROL_PLANES_MASTER|Control Planes Master]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]

Repository intelligence, code ownership, quality, and deployment tracking

## Purpose

Maps **893 owned Worldwidebro repositories** + **904 external capability repos** to ventures, capabilities, and deployment infrastructure.

Single source of truth for: code, ownership, quality, dependencies, deployment URLs, and capability provenance.

## Master Registries (Canonical Source)

| Registry | Records | Purpose |
|----------|---------|---------|
| **REPOSITORY_REGISTRY.yaml** | 893 repos | Master inventory: owned repos with code status, language, deployment URLs |
| **OWNED_REPO_CODE_REALITY.json** | 893 repos | Code verification: 177 code-backed vs 618 paperwork templates |
| **OWNED_REPO_DEPENDENCIES.json** | Dependency map | AST extraction: what each repo depends on |
| **COMPLETE-VENTURES-URLS-REPOS.yaml** | 789 ventures | Venture → Repository mapping (which repos serve which ventures) |
| **EXTERNAL_CAPABILITY_UNIVERSE.yaml** | 904 starred | External OSS projects organized by capability layer |
| **UNTAGGED_REPOS.csv** | Uncategorized | Repos needing sector/capability classification |

**Location:** `_REGISTRIES/CANONICAL/`

## Quick Navigation

**Looking for:**
- **A specific venture's repos?** → `COMPLETE-VENTURES-URLS-REPOS.yaml`
- **Code quality of a repo?** → `OWNED_REPO_CODE_REALITY.json`
- **What a repo depends on?** → `OWNED_REPO_DEPENDENCIES.json`
- **External capabilities map?** → `EXTERNAL_CAPABILITY_UNIVERSE.yaml`
- **All 893 Worldwidebro repos?** → `REPOSITORY_REGISTRY.yaml`

## Key Numbers

- **Owned Repositories:** 893 total
  - Code-backed (verified): 177
  - Paperwork templates: 618
- **External Capability Universe:** 904 starred repos
- **Total Stars:** 31.3M+
- **Languages:** 12 primary (Python 31, TypeScript 28, JavaScript 5, Go 5, Rust 4, C++ 3, Shell 4, Markdown 2+)
- **Ventures with Repo Mapping:** 789 / 789 (100%)

## Domain Responsibilities

- [ ] Code ownership tracking
- [ ] Deployment URL registry
- [ ] Language & framework inventory
- [ ] Dependency management
- [ ] Capability extraction via AST
- [ ] Venture → Repository mapping
- [ ] External capability supply chain
- [ ] Repository quality metrics

## Connected Domains

**Upstream (inputs from):**
- [[14-CAPABILITIES]] (what capabilities each repo provides)
- [[01-IDENTITY]] (which ventures own which repos)
- [[22-DEPLOYMENT]] (deployment status & URLs)

**Downstream (outputs to):**
- [[16-AGENTS]] (agents deploy from these repos)
- [[06-INFRASTRUCTURE]] (repo dependency scanning)
- [[40-METRICS]] (code quality metrics)

## Status

🟢 **LIVE** — All master registries populated and synchronized (Sep 15, 2026)

## How to Use This Domain

1. **To understand repo landscape:** Read REPOSITORY_REGISTRY.yaml summary
2. **To map venture→repo:** Query COMPLETE-VENTURES-URLS-REPOS.yaml
3. **To validate code quality:** Check OWNED_REPO_CODE_REALITY.json status
4. **To understand dependencies:** Parse OWNED_REPO_DEPENDENCIES.json
5. **To find external capabilities:** Browse EXTERNAL_CAPABILITY_UNIVERSE.yaml

## Command Center Integration

VEX Dashboard → GitHub Repos Tab displays this data live:
- 5 verified owned repos (CODE_BACKED status)
- 3 top starred external repos
- Programming language distribution
- Filter by verified/owned/starred
- Direct GitHub links

## Core Code-Backed Venture Repositories

| Repository Path | Venture ID | Venture Name | Primary Stack | Codebase Hub |
|:---|:---:|---|---|:---:|
| `repos/ops-staff-001-staffing` | `OPS-001` | WorldwideBro Staffing Ops | Fastify / Next.js / TypeScript | [[repos/ops-staff-001-staffing/README|Codebase Hub]] |
| `repos/lt-005-medical-courier-dispatch` | `LT-005` | HealthRoute Logistics | Express / TypeScript / React | [[repos/lt-005-medical-courier-dispatch/README|Codebase Hub]] |
| `repos/callcenter` | `CALLCENTER` | CallCenter Voice Intelligence | Python / LiveKit / Twilio / Flask | [[repos/callcenter/README|Codebase Hub]] |
| `repos/con-001-ace-construction` | `CON-001` | ACE Construction & Contracting | Next.js / Supabase / TypeScript | [[repos/con-001-ace-construction/README|Codebase Hub]] |
| `repos/lt-011-dispatch-software` | `LT-011` | Fleet OS Dispatch Platform | React / Node.js / TypeScript | [[repos/lt-011-dispatch-software/README|Codebase Hub]] |
| `repos/re-001-worldwidebro-holdings` | `RE-001` | WorldwideBro Holdings PropTech | Next.js / Tailwind / Vercel | [[repos/re-001-worldwidebro-holdings/README|Codebase Hub]] |

---

**Updated:** 2026-09-19 | **Authority:** [[00-CONSTITUTION/control-planes/CP-028|CP-028: Repositories]] | **Links:** [[13-REPOSITORIES.md]] | [[INDEX]] | [[START-HERE-REPOSITORIES]]


## Control Points (3)
| Control Point | Status | Tool | Responsible Role | Plane |
|:---|:---:|:---|:---|:---|
| **Define architecture standards** | 🟡 | `Graft (TOL-000001)` | CTO | Engineering Brain (AST-100) — Software Delivery Discipline |
| **Repository health checks** | 🟡 | `Graft (TOL-000001)` | Engineering Manager | Engineering Brain (AST-100) — Software Delivery Discipline |
| **Code graph generation** | ✅ | `Graft (TOL-000001)` | Tech Lead | Knowledge Fabric — Unified Organizational Knowledge |

*Governed by [[00-CONSTITUTION/control-planes/CP-028|CP-028: Application]] under [[50-MASTER-CONTROL/CONTROL_MATRIX|Control Matrix]].*
