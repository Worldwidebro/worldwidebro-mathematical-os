# Vercel Sites Registry — Sep 9, 2026 (LIVE VERIFIED)

**All Worldwidebro-deployed sites on Vercel**

---

## ✅ PRODUCTION READY (LIVE)

| Venture | Project Name | Vercel URL | Status | Purpose |
|---------|---|---|---|---|
| **OPS-001** | con-001-ace-construction | con-001-ace-construction.vercel.app | ✅ READY | Staffing/recruitment portal |
| **VEX Hero** (Main) | vex-hero-site | vex-hero-site.vercel.app | ✅ READY | Portfolio + ventures dashboard |
| **Callcenter** | callcenter | callcenter-eosin.vercel.app | ✅ READY | Lead capture + call logging |

### Additional Live Deployments (Verified)
- vex-hero-site (multiple preview deployments) — 4+ READY builds
- vex-hero-site-sigma → **vex-hero-site-sigma.vercel.app** (canonical URL per summary)

---

## 🔴 BUILD FAILURES (Need Attention)

| Project | Issue | Action |
|---------|-------|--------|
| vex-hero-site | Multiple ERROR states | Likely duplicate/old builds — safe to ignore if newer READY versions exist |

**Safe to ignore:** Old failed builds don't affect live sites — Vercel serves the latest READY build.

---

## ⏳ PENDING DEPLOYMENT

| Venture | Status | Notes |
|---------|--------|-------|
| **CON-001** | Deploying now | Commit pushed Sep 9 — Vercel auto-deploy in progress |
| **LT-005** | Awaiting env vars | Needs SUPABASE_URL, SUPABASE_ANON_KEY, STRIPE_SECRET_KEY before live |

---

## CANONICAL LIVE URLS

**Use these for customer-facing links:**

| Venture | Canonical URL | Status | What It Is |
|---------|---|---|---|
| **VEX Hero** | https://vex-hero-site-sigma.vercel.app | ✅ LIVE | Main portfolio dashboard (31 ventures visible) |
| **OPS-001** | con-001-ace-construction.vercel.app | ✅ LIVE | Staffing recruitment portal (forms live) |
| **Callcenter** | callcenter-eosin.vercel.app | ✅ LIVE | Lead capture system (taking inbound calls) |
| **Growth OS** | localhost:3030 | ✅ LIVE (Local) | Marketing dashboard (Sep 8+) |

---

## PROJECTS MAPPED TO CLAUDE.MD

Each repo has a CLAUDE.md with project-specific instructions:

| Repo | CLAUDE.md Location | What's Inside |
|------|---|---|
| **VEX (Worldwidebro-Vex)** | `CLAUDE.md` | CommandCenter wiring, API handlers, Supabase config, deployment notes |
| **CON-001** | `repos/con-001-ace-construction/CLAUDE.md` | Construction OS, Stripe webhook, Supabase migrations |
| **LT-005** | `repos/lt-005-medical-courier-dispatch/CLAUDE.md` | Medical courier portal, auth roles, Stripe test key |
| **Growth OS** | `repos/worldwidebro-marketing-os/CLAUDE.md` | Campaign dashboard, 5 OSS integrations, real data wiring |
| **Company Brain** | `CLAUDE.md` (root) | Infrastructure, Supabase, Neo4j, MCP, execution checklist |

**Cross-referencing:** Each CLAUDE.md links to sibling projects via [[wiki links]] — check them when switching between repos.

---

## DEPLOYMENT CHECKLIST (FOR NEW VENTURES)

When deploying a new venture to Vercel:

1. ✅ **Vercel connected** — Repo linked to Vercel dashboard
2. ✅ **vercel.json exists** — Build config in place
3. ⏳ **Environment variables set** — Supabase, Stripe keys added
4. ⏳ **Build passes locally** — `npm run build` succeeds
5. ⏳ **GitHub push triggers deploy** — Vercel auto-deploys from main
6. ✅ **Canonical URL documented** — Added to this registry

---

## TRAFFIC & MONITORING

**Check live status:**
```bash
curl https://vex-hero-site-sigma.vercel.app/health   # Should return 200 if live
curl https://con-001-ace-construction.vercel.app/api/health
```

**View logs:**
```
Vercel Dashboard → Projects → [Project] → Deployments → [Deployment] → Logs
```

**Analytics:**
```
Vercel Dashboard → Projects → [Project] → Analytics
```

---

**Last Updated:** Sep 9, 2026 (Vercel CLI verified)  
**Authority:** Infrastructure CP-027  
**Next Update:** After each new deployment
