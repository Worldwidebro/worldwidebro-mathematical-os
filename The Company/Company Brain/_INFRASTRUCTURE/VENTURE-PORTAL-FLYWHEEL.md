[[STARTHERE]] | [[REALITY]] | [[23-VENTURES]] | [[16-AGENTS]] | [[15-SKILLS]] | [[INDEX]]

# Autonomous Venturing Flywheel Architecture
## Venture Portal · Company Brain · Agency Agents · Skills Tri-System

> **Canonical Blueprint ID:** `ARCH-FLY-001`  
> **Authority:** Venture Control Plane (CP-005), Agent Control Plane (CP-006), & Infrastructure Control Plane (CP-027)  
> **Primary Repository:** [`Worldwidebro/worldwidebro-venture-portal`](https://github.com/Worldwidebro/worldwidebro-venture-portal) (`OWN-PRIV-0004` / `REP-001`)  
> **Ground Truth:** [[REALITY]] & [[_REGISTRIES/VENTURE_REGISTRY.yaml]]

---

## 1. System Map & Interconnections

The WorldwideBro venture engine operates as a closed-loop economic flywheel. No system exists in isolation:

```
                    ┌────────────────────────────────────────────────────────┐
                    │      Worldwidebro Venture Portal (Public Surface)      │
                    │   789 Ventures Across 35 Sectors (Next.js / Vercel)    │
                    └───────────────────────────┬────────────────────────────┘
                                                │ 1. Demand signals, venture stages
                                                ▼
                    ┌────────────────────────────────────────────────────────┐
                    │          Company Brain (Central Knowledge Core)        │
                    │     Neo4j Graph · Qdrant Vectors · Canonical Registry  │
                    └─────────────┬────────────────────────────▲─────────────┘
                                  │ 2. Task dispatch via       │ 5. Code verification,
                                  │    agents-by-sector.yaml   │    telemetry & stage bump
                                  ▼                            │
                    ┌───────────────────────────┐  Equipped by ┌─────────────────────────────┐
                    │   Agency Agents Fleet     │◄────────────┤  Modular Skills (15-SKILLS)   │
                    │ 280 Personas (Human Roles)│  Playbooks  │ • Agency Agents (Human Roles)│
                    │ Database, Payments, Sales │             │ • VoltAgent (Vendor Stacks)  │
                    │ Fractal Loop Orchestration│             │ • AAS Core (Dynamic MCP)     │
                    └─────────────┬─────────────┘             └─────────────────────────────┘
                                  │
                                  │ 3. Generates codebases, designs & integrations
                                  ▼
                    ┌────────────────────────────────────────────────────────┐
                    │      Active Venture Repositories & Deployments         │
                    │   887 Owned Repositories · Stripe Billing · Vercel     │
                    └───────────────────────────┬────────────────────────────┘
                                                │
                                                └─► 4. Live revenue, usage & products
```

---

## 2. The Four Pillars

| Pillar | System / Repo | Role in Flywheel | Key Artifacts |
| :--- | :--- | :--- | :--- |
| **1. The Showcase** | [`Worldwidebro/worldwidebro-venture-portal`](https://github.com/Worldwidebro/worldwidebro-venture-portal) (`REP-001`) | Public commercial interface displaying 789 ventures, current stages, team members, and live deployment links. | `src/data/portfolio.public.json`, Vercel production deployment |
| **2. The Core** | [`Worldwidebro/worldwidebro-mathematical-os`](https://github.com/Worldwidebro/worldwidebro-mathematical-os) (`Company Brain`) | Central single source of truth: canonical registries, Neo4j relationship graph, ADR logs, and audit infrastructure. | `_REGISTRIES/CANONICAL/`, `16-AGENTS/`, `15-SKILLS/`, `graphify-out/` |
| **3. The Fleet** | [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) + `.agents/agents/` | 280 autonomous specialist personas (e.g. `@architect`, `Database Optimizer`, `Deal Strategist`, `Whimsy Injector`). | `.agents/agents/`, `_REGISTRIES/agents-by-sector.yaml` |
| **4. The Toolkit** | **Skills Tri-System** (`agency-agents` + `VoltAgent` + `sickn33`) | Tri-layer execution playbooks: human deliverable standards, authoritative vendor stacks, and dynamic MCP catalog search. | `.agents/skills/` (285 resident skills), `_MCP/AAS_CORE_MCP_SPEC.md` |

---

## 3. The 5-Phase Autonomous Flywheel

### Phase 1: Intake & Opportunity Definition (Portal ➔ Brain)
- A venture is defined in the Venture Portal portfolio (`FIN-001`, `CON-001`, `LT-005`).
- The portal records initial stage (`planned`), sector taxonomy (`SEC-008`), and commercial thesis.
- Company Brain ingests this into [`_REGISTRIES/VENTURE_REGISTRY.yaml`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_REGISTRIES/VENTURE_REGISTRY.yaml) and establishes nodes in Neo4j.

### Phase 2: Swarm Routing & Capability Mapping (Brain ➔ Agents)
- Company Brain evaluates the venture requirements and consults [`_REGISTRIES/agents-by-sector.yaml`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_REGISTRIES/agents-by-sector.yaml).
- For a financial venture (`FIN`), it provisions `Quantitative Financial Analyst` (`@financial-analyst`) and `Payments & Billing Engineer`.
- Task orchestration is initiated via Fractal loops and OmniRoute routing (`:20128`).

### Phase 3: Playbook Execution (Agents ➔ Skills)
- The allocated agents load specialized playbooks:
  - **Role standards:** `.agents/skills/finance-financial-analyst/SKILL.md` ensures institutional modeling.
  - **Vendor implementation:** `.agents/skills/official-stripe-integration/SKILL.md` enforces idempotent webhook processing.
  - **Database architecture:** `.agents/skills/official-supabase-architecture/SKILL.md` guarantees Row Level Security (RLS).
  - **Unfamiliar tools:** Agent queries AAS Core MCP (`search_skills`) to retrieve exact package patterns on the fly.

### Phase 4: Code Reality & Monetization (Agents ➔ Ventures)
- Agents create and verify codebases in GitHub (`Worldwidebro/<venture-repo>`).
- CI/CD pipelines run automated unit and E2E browser tests.
- Infrastructure is provisioned via Terraform (`official-terraform-iac`), billing is connected to Stripe, and frontends deploy to Vercel.

### Phase 5: Stage Promotion & Public Reflection (Ventures ➔ Portal)
- As code reality is verified (`code_verified: true` in `OWNED_REPO_CODE_REALITY.json`), Company Brain promotes the venture stage:
  $$\text{planned} \longrightarrow \text{validating} \longrightarrow \text{prototype} \longrightarrow \text{mvp} \longrightarrow \text{operating}$$
- An automated sync job serializes the canonical venture state into `portfolio.public.json` in `worldwidebro-venture-portal`.
- The public portal instantly reflects the live working product, customer onboarding flows, and operational proof.

---

## 4. Verification & Audit Heuristics

1. **Rule #3 Compliance (No Fake Completion):** A venture cannot advance to `prototype` or `mvp` without an executable repository, passing tests, and verified terminal proof.
2. **Rule #2 Compliance (Internal Reuse First):** Before creating new venture repositories, agents query the 887 existing owned repositories and canonical skills fleet to reuse existing code.
3. **Continuous Graph Synchronization:** After any venture code change or agent reconfiguration, `graphify update .` updates the Neo4j relational graph and AST indexes.
