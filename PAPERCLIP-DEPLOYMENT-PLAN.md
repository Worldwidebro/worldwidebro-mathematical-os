---
name: PAPERCLIP-DEPLOYMENT-PLAN
title: 📎 PAPERCLIP DEPLOYMENT PLAN
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# 📎 PAPERCLIP DEPLOYMENT PLAN

**Status:** 🟡 Plan drafted — awaiting user approval before Step 1
**Created:** 2026-05-10
**Owner:** Worldwidebro Holdings
**Blocks:** GTM Phase 1.2, 1.3, 2+ (all downstream work routes through Paperclip)
**Target Repo:** `paperclipai/paperclip` (Node + React, MIT, multi-tenant agent-fleet control plane)

---

## 🎯 Goal

Deploy Paperclip as the root orchestration layer so that the **existing Go-to-Market system state** (383–583 ventures in Supabase, 64 indexed repos, 5 Make.com workflows, org chart, Graphify KG, OpenVolo contacts) is **visible and operated from inside Paperclip** before further Phase 1.2/1.3 execution.

User directive (2026-05-10): *"we want to see this information on paperclip first."*

---

## ⚠️ Trust Caveats (read before Step 1)

Web research on Paperclip returned details that must be **independently verified** before install — some signals suggest LLM hallucination:

| Claim from research | Risk |
|---|---|
| "Latest release v2026.416.0 June 2026" | Future date — implausible |
| "31k–62k GitHub stars" | 2× variance — likely fabricated |
| `npx paperclipai onboard --yes` one-liner | Convenient — verify before trusting |
| "Embedded DB by default, no Postgres required" | Verify against actual README |

**Mitigation:** Step 1 is repo verification. No code runs until we have read the actual README from the actual repo.

---

## 🧭 Deployment Sequence (6 Steps, 6 Checkpoints)

### ✅ STEP 0 — Environment Readiness Verified
- [x] Node v25.9.0, npm 11.12.1, pnpm 10.24.0
- [x] Docker 29.4.0
- [x] PostgreSQL 15.17 client (Supabase hosted is production DB)
- [x] Redis CLI 8.6.2
- [x] Port 3100 free (Paperclip's default UI port)
- [ ] ⚠️ Caveat: Node 25 is bleeding-edge / non-LTS — may need to downgrade to Node 20 LTS if Paperclip's engines field requires it

---

### 🔲 STEP 1 — Verify Paperclip Repo Is Real & Inspect Install Path
**Checkpoint output:** A short findings note in `findings.md` answering:
1. Does `github.com/paperclipai/paperclip` exist and is it public?
2. What does the actual README say for install, required services, Node version?
3. What is the actual latest commit date / release? (Filters out hallucinated dates.)
4. What is the license?
5. Does the repo model "companies" (tenants) as a first-class entity? Is there a schema doc?

**🛑 Abort-to-fallback criteria (any one triggers pivot):**
- Last commit > 6 months ago (project abandoned)
- README < 100 lines or is a stub (no real project)
- License is not OSS-compatible (MIT/Apache/BSD/AGPL acceptable; proprietary/no-license not)
- No multi-tenant / "company" / "organization" entity visible in repo source or docs
- Repo requires paid cloud service to function (not truly self-hostable)

**Tools:** `gh repo view`, `curl` on raw README, clone to a throwaway dir (`/tmp/paperclip-inspect`).
**Time:** 10–20 min.
**User action:** Review findings note, approve Step 2 (or pivot per fallback section).

---

### 🔲 STEP 2 — Install Paperclip Locally
**Install path (pick one after Step 1 findings):**
- **Option A — Clone + pnpm:** `git clone → pnpm install → pnpm dev` (preferred — gives code visibility)
- **Option B — NPX onboard:** `npx paperclipai onboard --yes` (fast, opaque)
- **Option C — Docker:** `docker build` from clone (best if production config is goal)

**Install location:** `/Users/acebless/Documents/paperclip/` (top-level, peer to `mission-control/` and `iza-os-rag-system/`)

**⚠️ Install-path recommendation:** Prefer Option A (clone + pnpm) over Option C (Docker). Paperclip spawns Docker sandboxes for agents; running Paperclip itself in Docker requires either Docker-in-Docker or mounting `/var/run/docker.sock`, both of which have security and setup cost. Bare-metal install avoids this entirely.

**Node version handling:** If Paperclip's `engines` field requires Node < 25, switch locally (not globally) using either:
- `nvm install 20 && nvm use 20` (project-scoped via `.nvmrc`)
- `volta pin node@20` (auto-switch on `cd` into the dir)

Do NOT change the system Node — other tools depend on it.

**🔐 Secrets — generate scoped keys, do NOT reuse production:**
- Create **new** Anthropic + OpenAI API keys specifically for Paperclip (separate from existing project keys)
- Set tight spend limits on each key before first run ($20–50 cap)
- Rationale: freshly-cloned code running untrusted agent loops should not have production-grade credentials. If something goes sideways in Step 2–5, the blast radius is bounded.
- User confirms key creation + spend cap before Step 2 install.

**Config applied:**
- Port: 3100 (confirmed free)
- DB: Start with embedded (fastest to first-run); migrate to Supabase Postgres in Step 5
- Secrets: `.env.local` with **new scoped keys** (see above)
- **NOT configured yet:** external auth, reverse proxy, PM2 — deferred to post-wiring

**🧹 Rollback (if Step 2 wedges the system):**
```bash
rm -rf /Users/acebless/Documents/paperclip/
rm -rf ~/.npm/_npx/*paperclip*
rm -rf ~/.cache/pnpm/*paperclip*
docker ps -a | grep paperclip | awk '{print $1}' | xargs -r docker rm -f
docker images | grep paperclip | awk '{print $3}' | xargs -r docker rmi -f
```

**Deliverables:**
- Paperclip reachable at `http://localhost:3100`
- Login works, blank workspace visible
- Entry added to `progress.md` with commit SHA installed

**Time:** 30–90 min depending on install path and dependency issues.
**User action:** Log in, confirm UI loads. Approve Step 3.

---

### 🔲 STEP 3 — Model the Org Structure (Tenants/Companies)
**Goal:** Create the Paperclip entity hierarchy that mirrors your legal/operational reality.

Proposed hierarchy (to be confirmed against actual Paperclip data model in Step 1):

```
Worldwidebro Holdings (root tenant)
├── Division 1 — Beauty & Wellness
│   └── BW-001 Lash Extension Studio (company)
├── Division 2 — Construction & Logistics
│   └── CON-001 Ace Construction (company)
├── Division 3 — Financial Services
│   └── FIN-036 Arbitrage Nexus Platform (company)
├── Division 4 — Technology & AI
│   └── (flagship tech ventures)
├── Division 5 — E-Commerce & Retail
├── Shared Services (cross-cutting agents, skills, memory)
└── Venture Hub Inc (dashboard/meta company)
```

**Seeding approach:**
- Manually create 3 flagship companies (BW-001, CON-001, FIN-036) to validate the model
- Defer bulk-loading all 583 ventures to Step 4 (scripted import)

**Deliverables:**
- Org chart visible in Paperclip UI
- 3 flagship tenants exist with goals, budgets, agent slots
- `findings.md` updated with Paperclip's actual entity schema

**Time:** 1–2 hours.
**User action:** Review org structure. Approve Step 4.

---

### 🔲 STEP 4 — Wire Existing Data In

**⚠️ PREREQUISITE DECISION — resolve the 337-venture import gap first:**

Your status summary flagged 337 ventures failed import (batches returning 400 with unknown schema constraint). Before Step 4 imports into Paperclip, decide:

- **(a) Import current ~583 into Paperclip now; fix the 337 later.** Faster to dashboard. But Paperclip carries the same blind spot forward.
- **(b) Fix the 337 failed batches first (debug one failing batch, identify constraint, re-run), then import full 712.** Cleaner end-state. Adds 1–4 hours before Paperclip data wiring.

**Also reconcile venture counts before Step 4:** Status summary says 383; task_plan.md says 583; progress.md says 708; findings.md §Phase 1.1 says "583 (was 383 estimate)." Single authoritative query against Supabase needed; result logged to `findings.md` before any import script runs.

**Data sources to connect:**

| Source | Target in Paperclip | Method | Records |
|---|---|---|---|
| Supabase `ventures` table | Companies / sub-tenants | Custom import script | 383–708 (reconcile first) |
| Supabase `repos` table | Agent skills / tools catalog | Custom import script | 64 |
| Graphify knowledge graph | Relationship overlay | MCP bridge or batch export | 7k nodes / 6k edges |
| OpenVolo `contacts` | Contact roster per company | SQLite → Paperclip API | 58 |
| Make.com workflow definitions | Automation playbooks | Manual registration | 5 |
| `aoc_tasks` queue | Task queue visibility | Polling webhook or view | 5264 |

**Risk management:**
- Start with **read-only mirrors** (Paperclip shows data; Supabase remains source of truth)
- Promote to bidirectional sync only after end-to-end read works
- No destructive migrations — existing systems keep working

**Deliverables:**
- Script: `scripts/paperclip-import-ventures.ts` (idempotent, re-runnable)
- Script: `scripts/paperclip-import-repos.ts`
- Script: `scripts/paperclip-import-contacts.ts`
- All 583 ventures visible in Paperclip UI under correct division

**Time:** 3–6 hours (write + test scripts + debug schema mismatches).
**User action:** Spot-check 5 random ventures in UI — correct division, correct metadata. Approve Step 5.

---

### 🔲 STEP 5 — Surface "GTM System Status" Dashboard
**Goal:** The exact status you pasted (Phase 0/1/2 progress, import stats, blockers) is visible as a Paperclip view.

**Approach — pick one based on Paperclip's actual capabilities (known after Step 1):**
- **A.** Native dashboard widgets if Paperclip supports custom views
- **B.** A "meta-company" called "Go-to-Market System" whose goals, heartbeats, and budgets reflect Phase progress
- **C.** Markdown embed / iframe from existing `mission-control` if Paperclip supports it
- **D.** Custom React page added to Paperclip UI (requires fork — most work, most control)

**Dashboard content (mirrors your status summary):**
- Phase 0 Infrastructure — ✅ done (7 MCPs, 5 workflows, Supabase, Graphify, Ollama, ClickUp)
- Phase 1.1 Product Audit — ✅ done (583 ventures ranked, top 50 identified)
- Phase 1.2 Network Mapping — 🔄 redefined: venture-needs → contact wishlist
- Phase 1.3 Social Audit — 🔄 redefined: profile creation from scratch
- Phase 2A/2C Intelligence Layer — ✅ done (64 repos embedded)
- Phase 2B Backstage — ⏸️ superseded by Paperclip
- Import completeness — ⚠️ 337 ventures unloaded (schema constraint unresolved)

**Deliverables:**
- Dashboard/view live in Paperclip UI
- Screenshot added to `progress.md`

**Time:** 2–4 hours.
**User action:** Verify status is legible and accurate. Approve Step 6.

---

### 🔲 STEP 6 — Unblock GTM Phases 1.2 & 1.3
Once Paperclip is live with the status surfaced, resume GTM per the Oct 10 redefined framing:

- **Phase 1.2 (Network Mapping):** Analyze 583 ventures → derive top contact **archetypes** needed (e.g., "NC-licensed GC," "Charlotte salon landlord," "Shopify agency owner in beauty vertical"). I produce the wishlist; you supply names from your network (you confirmed unlimited access). Output lives in Paperclip under each company.
- **Phase 1.3 (Social Audit, recast as Social Creation):** Per-venture social identity plan — handle strategy, content pillars, launch sequence across IG/TikTok/LinkedIn. Output lives in Paperclip per company.
- **Phase 2+:** ClickUp pipeline, deal scripts, lead routing — now driven from Paperclip as the source of truth.

**Time:** Ongoing (multi-session).
**User action:** Execute outreach; I execute analysis + content planning.

---

## 🪜 Ordered Decision Points (Where I'll Stop and Ask)

| # | Decision | Where |
|---|---|---|
| 1 | Is the repo real + what are real install reqs? | End of Step 1 |
| 2 | Which install path (clone vs npx vs docker)? | Start of Step 2 |
| 3 | Org structure shape — does the proposed division hierarchy match your legal entities? | Start of Step 3 |
| 4 | Read-only mirror vs. bidirectional sync for Supabase? | Start of Step 4 |
| 5 | Dashboard approach — native widget vs meta-company vs custom React? | Start of Step 5 |
| 6 | Which GTM phase to resume first after Paperclip live? | Start of Step 6 |

---

## 🔻 Fallback If Paperclip Turns Out Wrong

If Step 1 reveals `paperclipai/paperclip` is abandoned, private, or doesn't match description:

- **Fallback A:** Evaluate `agencyenterprise/paperclip-ai`
- **Fallback B:** Use existing `mission-control` (Next.js) as the orchestration UI. Adds 5–10 new route/page components; reuses WorkspaceDashboard + AgentActivityDashboard scaffolding. Fastest to value (4–8 hours total vs 15–30 for Paperclip).
- **Fallback C:** Extend `venture-hub` dashboard since it's already deployed to Vercel. ⚠️ **Auth prerequisite:** venture-hub is public. GTM status + contact wishlist must not be exposed. Fallback C requires confirming (or adding) auth middleware before use.

I will **recommend** a fallback at the end of Step 1 findings — not auto-pivot.

---

## 📁 Artifacts This Plan Will Produce

| File | Purpose |
|---|---|
| `findings.md` § Paperclip Research | Step 1 verification output |
| `paperclip/` | Installed repo (Step 2) |
| `scripts/paperclip-import-*.ts` | Data wiring (Step 4) |
| `progress.md` | Session log entries per step |
| `task_plan.md` | Updated sequencing (this file) |
| `PAPERCLIP-DEPLOYMENT-PLAN.md` | This plan (living doc) |

---

## ⏱ Total Estimated Time

| Step | Optimistic | Realistic | Pessimistic |
|---|---|---|---|
| 1 Verify | 10m | 20m | 1h |
| 2 Install | 30m | 90m | 4h |
| 3 Org model | 1h | 2h | 4h |
| 4 Wire data | 3h | 6h | 12h |
| 5 Dashboard | 2h | 4h | 8h |
| 6 Resume GTM | ongoing | ongoing | ongoing |
| **Total to "status visible in Paperclip"** | **~7h** | **~13h** | **~29h** |

---

**NEXT ACTION:** Approve this plan (or request changes), then I begin Step 1 (repo verification — no installs, no risk).
