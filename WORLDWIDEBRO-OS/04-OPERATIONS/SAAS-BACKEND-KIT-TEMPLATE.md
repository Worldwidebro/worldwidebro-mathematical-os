---
references:
  - [[VENTURE-MASTER]]
  - [[LOOP-FRAMEWORK]]
  - [[ORB-MASTER-CONNECTOR-2026-06-11]]
---

# SaaS Backend Kit — Stack-Agnostic Template

**What this is:** The reusable backend scaffold for any Layer 2 (Skill Monetization) SaaS venture — API + auth + DB + jobs + storage + observability, wired once and cloned per venture. Companion to `[[SERVICE-VENTURE-KIT-TEMPLATE]]` (that one is for labor/service ventures; this one is for software ventures).

**Proven instance:** none built yet — first candidate is HRMS (see `[[hrms-venture-execution]]`).

> **To clone a new venture, swap only the 4 provider choices.** Folder structure and middleware order carry over unchanged.

---

## THE 4 SWAPS (per-venture provider picks)

| Swap | Options | Your new venture |
|------|---------|-------------------|
| **{{AUTH}}** | Clerk / Better Auth / Auth.js / Firebase Auth | 🟦 _________ |
| **{{ORM}}** | Prisma / Drizzle | 🟦 _________ |
| **{{JOBS}}** | BullMQ (self-hosted redis) / Trigger.dev / Inngest (managed) | 🟦 _________ |
| **{{DEPLOY}}** | Railway / Render / Fly.io | 🟦 _________ |

Everything else below (validation, security middleware, logging, monitoring, docs, testing) is fixed — not venture-specific.

---

## FIXED STACK (same every venture)

| Concern | Choice | Why fixed |
|---|---|---|
| Validation | Zod | Most ecosystem overlap with TS inference |
| Security middleware | jwt + rate-limit + cors + helmet + csrf + xss/SQLi guards | Non-negotiable baseline, not a business decision |
| Secrets | `.env` locally → Doppler/Infisical once >1 dev or >1 environment | Swap only triggers on team size, not venture |
| Caching | Redis / Upstash Redis | Needed regardless of {{JOBS}} choice (session/rate-limit store) |
| Storage | S3 / Cloudinary / UploadThing — pick per media type (Cloudinary if image-heavy, S3 default) | |
| Logging | Pino (perf) or Winston (ecosystem) | |
| Monitoring | Sentry (errors) + Better Stack or Grafana (uptime/metrics) | |
| API docs | Swagger or Scalar, generated from route schemas | |
| Testing | Vitest/Jest (unit+integration) + Playwright (e2e) | |
| CI/CD | Docker + GitHub Actions → {{DEPLOY}} | |

---

## FOLDER STRUCTURE (clone as-is)

```
project-root/
├── src/
│   ├── config/                    # env loading, doppler/infisical client, constants
│   │   ├── env.ts
│   │   └── secrets.ts
│   │
│   ├── modules/                    # feature-based, not layer-based
│   │   ├── users/
│   │   │   ├── users.routes.ts     # API routes
│   │   │   ├── users.controller.ts
│   │   │   ├── users.service.ts    # business logic
│   │   │   ├── users.repository.ts # DB access ({{ORM}} queries)
│   │   │   ├── users.schema.ts     # zod validation schemas
│   │   │   └── users.test.ts       # vitest/jest
│   │   ├── auth/
│   │   │   ├── auth.routes.ts
│   │   │   ├── auth.service.ts      # {{AUTH}} adapter
│   │   │   └── auth.schema.ts
│   │   └── ...                     # one folder per domain
│   │
│   ├── middleware/
│   │   ├── auth.middleware.ts       # jwt verify / session check
│   │   ├── rateLimit.middleware.ts
│   │   ├── cors.middleware.ts
│   │   ├── helmet.middleware.ts
│   │   ├── csrf.middleware.ts
│   │   ├── validate.middleware.ts   # generic zod request validator
│   │   └── errorHandler.middleware.ts
│   │
│   ├── db/
│   │   ├── client.ts                # {{ORM}} client instance
│   │   ├── schema/                  # drizzle schema or prisma models
│   │   └── migrations/
│   │
│   ├── cache/
│   │   └── redis.ts
│   │
│   ├── jobs/
│   │   ├── queue.ts                 # {{JOBS}} setup
│   │   └── handlers/
│   │       └── sendEmail.job.ts
│   │
│   ├── storage/
│   │   └── s3.ts                    # or cloudinary.ts / uploadthing.ts
│   │
│   ├── lib/
│   │   ├── logger.ts                # pino/winston instance
│   │   ├── sentry.ts                # monitoring init
│   │   └── response.ts              # standardized API response wrapper
│   │
│   ├── docs/
│   │   └── openapi.ts               # swagger/scalar spec generation
│   │
│   ├── app.ts                       # app assembly (middleware order matters)
│   └── server.ts                    # entrypoint
│
├── tests/
│   ├── unit/
│   ├── integration/                  # hits real db/test containers
│   └── e2e/                          # playwright
│
├── prisma/ (or drizzle/)
│   └── schema.prisma
│
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── .github/workflows/
│   ├── ci.yml                        # lint/test/build on PR
│   └── deploy.yml                    # {{DEPLOY}} deploy
├── playwright.config.ts
├── vitest.config.ts
└── package.json
```

**Design rules baked in:**
- Feature-first modules (not global `controllers/`/`services/`/`models/` split) — auth/validation/business-logic/db co-located per domain.
- Middleware is cross-cutting (security stack) and lives outside modules — wraps every route.
- Infra clients (db, cache, jobs, storage) are thin wrappers injected into services, not reached into directly — makes swapping {{ORM}} or {{JOBS}} a contained change.
- One `response.ts` enforces a single response shape across all routes.

---

## UNIVERSAL FIRST MOVES (any SaaS venture)

1. Pick the 4 swaps above, scaffold folder tree
2. Wire {{AUTH}} + zod validation on the first real route before anything else
3. `.env` first; move to Doppler/Infisical only once a second dev/environment exists
4. Docker Compose locally → GitHub Actions CI → {{DEPLOY}} for first deploy
5. Sentry + Pino wired before first real user traffic, not after an incident

---

## CLONE LOG

| Venture | {{AUTH}} | {{ORM}} | {{JOBS}} | {{DEPLOY}} | Status |
|---|---|---|---|---|---|
| HRMS | _________ | _________ | _________ | _________ | ⬜ Not started |
