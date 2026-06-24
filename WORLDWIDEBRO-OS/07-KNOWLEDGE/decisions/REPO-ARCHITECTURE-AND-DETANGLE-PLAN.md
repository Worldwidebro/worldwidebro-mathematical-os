# Repository Architecture & Detangle Plan (2026-06-22)

## The core lesson: two structures, two ALTITUDES — they nest, they don't compete

You have been mixing two different things that operate at different levels:

| | WORLDWIDEBRO-OS (00-COMMAND..10-STATUS) | Production repo (app/backend/infra/ai/...) |
|---|---|---|
| Altitude | **Company** — coordinates MANY products | **One product** — internals of a single app |
| Contains | governance, portfolio, registries, knowledge, docs, DATA | code: frontend, backend, api, infra, tests |
| "Code"? | mostly docs + data + registries (coordination) | actual product source code |
| How many | ONE | one PER venture (712 of them) |

**They align by nesting, not by replacing each other:**

```
WORLDWIDEBRO-OS  (company OS, 1 repo, 1 remote)
   └─ 08-DATA/registries/repositories.csv  ->  points to (by remote URL)
        ec-051-ai-email-marketing   (own repo) -> app/ backend/ infra/ ai/ tests/ ...
        genixbank-financial-system  (own repo) -> app/ backend/ infra/ ai/ tests/ ...
        the-office                  (own repo) -> ...
```

The company OS does NOT contain product code. It **registers** product repos and coordinates
them. Each product repo internally uses the production 10-system structure you described.

## Mapping the production 10 systems onto the company OS

| Production system (per product) | Company-level home (WORLDWIDEBRO-OS) |
|---|---|
| Application (frontend/backend/api) | lives IN each venture repo; 03-PORTFOLIO registers it |
| Infrastructure (docker/k8s/terraform) | 06-TECHNOLOGY/infrastructure (shared) + per-product |
| Data (db/migrations/schemas) | 08-DATA (company registries/graph) + per-product db |
| AI/Intelligence (agents/prompts/models) | 05-AGENTS (company agents) + per-product |
| API/Integration (services/webhooks) | 06-TECHNOLOGY (shared connectors) |
| Auth & Security | 00-DIRECTIVES (policy) + per-product impl |
| Automation (cron/jobs/queues) | 06-TECHNOLOGY/automations |
| Observability (logs/metrics/alerts) | 09-DASHBOARDS + 10-STATUS |
| Documentation | 07-KNOWLEDGE |
| Testing | lives IN each venture repo |
| Config / Build / CI-CD / Versioning | per-repo (.github/, etc.) — NOT company level |

## Current wiring (the problem)

- `~/Documents` is a git repo with **4 unrelated remotes** (Applyingforjobs, clip,
  iza-os-financial-core, Worldwidebro) — 4 products' remotes accidentally on one folder.
- **74 nested git repos** inside it: own products, third-party tools, vendored plugins.
- A **parallel writer commits to the same branch**, recreating moved folders.
- Duplicates: `design-system` cloned 3x; two genixbank repos.

## Detangle plan (proper repo lesson, applied)

### 1. Decide what `~/Documents` IS
**Recommended:** `~/Documents` is a **workspace**, NOT a git repo. The git repo is
`WORLDWIDEBRO-OS/` (the company OS) with **ONE** remote -> `Worldwidebro/Worldwidebro.git`.
(Alternative: keep Documents as the repo but strip to 1 remote.)

### 2. Three buckets for the 74 nested repos
- **Own products** (Worldwidebro/* + Crucix) -> stay independent repos with their own remotes;
  **register** each in `08-DATA/registries/repositories.csv` with a new `remote_url` column.
  Do NOT commit their code into the OS repo.
- **Third-party tools** (anthropic-sdk, langgraph, vllm, ComfyUI, magika, nanoGPT, LightRAG,
  obsidian plugins...) -> these are DEPENDENCIES. gitignore them; record in 06-TECHNOLOGY with URL.
  Never commit vendored code into your repo.
- **Duplicates** -> collapse: one `design-system`; reconcile the two genixbank repos.

### 3. Strip the 4 remotes to 1
The OS repo should push to exactly one home. The other 3 belong to their own product repos.

### 4. The "wire" = registry row -> remote URL
`repositories.csv` gains `remote_url`. That single column IS how the company OS connects to
product code without containing it. Agents act on the registry; the registry points to the repo.

## The one-line lesson
**A company OS is not a code repo. It is a registry of code repos.**
Monorepo the *coordination* (docs, data, registries). Keep each *product* its own repo.
Never vendor third-party code into either. The link between them is a URL in a registry, not a
folder nested inside a folder.
