[[STARTHERE]] | [[REALITY]] | [[ANTIGRAVITY]] | [[CLAUDE]] | [[INDEX]]

# AGENTS.md — Universal Agent Operating Contract

> **Scope:** Project-Wide AI Agent Operating Guidelines  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)  
> **Master Operating Contract:** [`ANTIGRAVITY.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/ANTIGRAVITY.md)  
> **Infrastructure & Runtime State:** [`CLAUDE.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/CLAUDE.md)  
> **Modular Directives:** [`.agents/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/.agents)

---

## 1. Quick Orientation for Any Agent
You are working within **WorldwideBro / Company Brain**, a distributed company operating system coordinating products, 700+ ventures, 887 owned repositories, 910 starred repositories, canonical registries, and local-first AI infrastructure.

- **Primary Local Infrastructure:** Mac Studio M4 Max (`100.87.214.70`) + LaCie 4TB storage.
- **Mobile Engineering Node:** MacBook Air M-series (`100.121.17.63`) + T7 Shield 2TB.
- **Network Mesh:** Tailscale encrypted interconnect.
- **Knowledge Core:** Neo4j relational graph (`:7687`/`:7474`) & Qdrant semantic vectors (`:6333`).
- **Inference Router:** OmniRoute (`:20128`) & LiteLLM (`:4000`) with native `exo` MLX models.
- **Canonical Source of Truth:** `_REGISTRIES/CANONICAL/` directory.

---

## 2. Mandatory Operational Rules
Every agent operating in this repository must strictly adhere to the **45 Rules** detailed in [`ANTIGRAVITY.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/ANTIGRAVITY.md):

1. **North Star:** Continually move `GOAL → PLAN → REQUIREMENTS → ARCHITECTURE → IMPLEMENTATION → TESTING → DEPLOYMENT → OBSERVABILITY → FEEDBACK → IMPROVEMENT → BUSINESS OUTCOME`.
2. **Reuse First:** Never write new code without searching existing internal code, the 177 verified code-bearing repos, canonical capabilities, or approved external packages.
3. **No Fake Completion:** Never claim "Done", "Fixed", or "Production ready" without executable proof. Only report verified states: `IMPLEMENTED`, `TESTED`, `VERIFIED`, `DEPLOYED`, `OBSERVED`.
4. **No Placeholder Architecture:** Avoid stubs, fake mocks, TODOs, or simulated APIs unless explicitly designated as prototypes.
5. **Git Safety:** Always run `git status && git branch && git diff` before and after changes. Never rewrite history or delete uncommitted work.
6. **Data Integrity:** Never silently overwrite canonical registries in `_REGISTRIES/`. Prefer append, versioned, or merge updates.
7. **Security:** Zero-trust approach. Never commit secrets or expose credentials in code, Markdown, or logs.
8. **Token Efficiency:** Leverage Canonical Knowledge + Retrieval + Targeted Context instead of dumping massive repositories into context.

---

## 3. Modular System Map

```text
/
├── ANTIGRAVITY.md                   # Master operating contract (45 core rules)
├── CLAUDE.md                        # Live-audited infrastructure & runtime state
├── AGENTS.md                        # This file: portable agent orientation
├── BUSINESS-CAPITAL-DATA-ROOM/      # Venture Document OS (22 canonical domains per venture)
│   ├── CON-001/                     # ACE Construction & Contracting LLC
│   ├── LT-011/                      # WorldwideBro Fleet OS LLC
│   ├── LT-005/                      # HealthRoute Logistics LLC
│   ├── OPS-001/                     # WorldwideBro Staffing Ops LLC
│   ├── RE-001/                      # WorldwideBro Holdings LLC
│   └── EXPORTS/                     # Institutional ZIP packages & SHA-256 manifests
├── _TOOLS/                          # Integrated Agent Tooling
│   ├── gstack/                      # Garry Tan gstack (make-pdf, office-hours, sprint review)
│   └── gbrain/                      # Garry Tan gbrain (neural/keyword graph knowledge engine)
├── scripts/                         # Operational CLI wrappers & generators
│   ├── make-pdf                     # Publication-grade vector PDF compiler (gstack engine)
│   ├── gbrain                       # Local-first PGLite knowledge graph CLI
│   └── venture_os_engine.py         # 22-domain multi-format generator & packager
└── .agents/
    ├── rules/                       # Persistent architectural, security, git, and coding rules
    ├── skills/                      # On-demand modular procedural runbooks (SKILL.md)
    ├── workflows/                   # Standardized slash command workflows (/gap-analysis, /deploy, etc.)
    └── agents/                      # Domain-specialized subagent definitions (@architect, @qa, etc.)
```

---

## 4. Universal 22-Domain Venture Document Operating System
Every venture maintained within Company Brain adheres to the 22-domain institutional standard:

1. `01_IDENTITY`: Mission, vision, core values, brand positioning, brand assets
2. `02_STRATEGY`: Strategic plan, competitive advantage, OKRs, gstack office-hours analysis
3. `03_LEGAL`: Articles of organization, operating agreements, certificates of good standing, corporate resolutions
4. `04_OWNERSHIP`: Cap table, equity structure, member registry, voting rights
5. `05_FINANCIAL`: Financial statements, cash flow models, revenue projections, balance sheets (.xlsx + .pdf)
6. `06_MARKET`: TAM/SAM/SOM analysis, target customer profiles, competitive landscape
7. `07_PRODUCT`: Product roadmap, technical architecture, feature specs
8. `08_REVENUE`: Pricing models, revenue streams, sales pipeline, CAC/LTV economics
9. `09_OPERATIONS`: Operating procedures (SOPs), supply chain, logistics, workflows
10. `10_PEOPLE`: Org charts, key personnel profiles, staffing plans, hiring roadmaps
11. `11_ASSETS`: Physical, intellectual, software, and real property inventories
12. `12_COMPLIANCE`: Regulatory filings, licenses, certifications, compliance audits
13. `13_RISK`: Risk register, mitigation plans, insurance coverage, contingency models
14. `14_FUNDING`: Capital history, funding requirements, sources & uses of funds
15. `15_GRANTS`: Grant applications, awards, compliance reporting
16. `16_LOANS`: Debt schedules, promissory notes, amortization tables, lender packages
17. `17_INVESTORS`: Investor updates, pitch decks (16:9 PDF decks), term sheets, due diligence trackers
18. `18_CONTRACTS`: Customer MSAs, vendor agreements, partnerships, NDAs
19. `19_EVIDENCE`: Banking letters, customer testimonials, audit letters, performance proofs
20. `20_DATA_ROOM`: Master index, due diligence checklist, investor access logs
21. `21_REPORTS`: Monthly, quarterly, and annual operational reviews
22. `22_SYSTEM`: Architecture Decision Records (ADRs), QA test matrices, system guidelines

---

## 5. Tooling & Automation Contracts

### gstack (`scripts/make-pdf`)
- Engine: Headless Chromium via Playwright + CSS Paged Media + KaTeX + Mermaid.
- Command: `scripts/make-pdf generate <input.md> [output.pdf]`
- Output: Publication-quality vector PDFs matching print specifications with zero manual formatting.

### gbrain (`scripts/gbrain`)
- Engine: Embedded PGLite vector and full-text engine with BM25 keyword matching and hierarchical chunking.
- Commands:
  - `scripts/gbrain query "<search phrase>"`: Rank-retrieves venture records and underwriting metrics.
  - `scripts/gbrain import <dir> --no-embed`: Incrementally updates knowledge graph index.
  - `scripts/gbrain doctor`: Validates engine integrity and storage configuration.

Refer to [`.agents/rules/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/.agents/rules) for granular constraints, and activate specialized skills in [`.agents/skills/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/.agents/skills) when performing specific tasks.
