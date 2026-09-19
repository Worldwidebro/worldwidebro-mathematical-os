---
id: VEX-PORTAL-HUB
title: "VEX — WorldwideBro Flagship Brand & CommandCenter Operating System"
aliases: ["VEX", "vex", "vex-hero-site", "vex-hero-site/_index", "Worldwidebro-Vex", "VEX-SITE"]
tags: [vex, command-center, portal, frontend, brand]
status: ACTIVE
updated: 2026-09-19
---

[[STARTHERE]] | [[INDEX]] | [[REALITY]] | [[ANTIGRAVITY]] | [[23-VENTURES/README|23-VENTURES]] | [[VEX-DEPLOYMENT-READY]]

# VEX — Flagship Brand & CommandCenter Operating System

> **Canonical Repository:** [`23-VENTURES/Worldwidebro-Vex`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/23-VENTURES/Worldwidebro-Vex)  
> **Deployment Status:** Ready for Vercel deployment ([[VEX-DEPLOYMENT-READY]])  
> **AST Code Graph:** 1,583 symbols, 2,318 edges, 91 clusters, 45 flows indexed in [[scripts/gitnexus|GitNexus]]  
> **Authority:** Sovereign Operator & Commercial Operations (CP-001 / CP-006)

---

## 1. Executive Summary

**VEX** is the public front door, flagship hero experience, and sovereign Command Center for **WorldwideBro Group**, coordinating:
1. **Public Showcase:** Hero video experience, holding-company model, venture studio operating system, and founder advisory path.
2. **CommandCenter Dashboard:** Real-time Supabase-backed metric telemetry across revenue, active agents, running tasks, and Stripe billing.
3. **Public Portfolio Generation:** Automated script generating `portfolio.public.json` to keep sensitive corporate data out of client bundles.

---

## 2. Core Documentation & Architecture Links

- **Main Repository README:** [[23-VENTURES/Worldwidebro-Vex/README|Worldwidebro-Vex README]]
- **CommandCenter Architecture v2:** [[23-VENTURES/Worldwidebro-Vex/VEX-COMMAND-CENTER-ARCHITECTURE-V2|Command Center Architecture v2]]
- **System Architecture:** [[23-VENTURES/Worldwidebro-Vex/VEX-ARCHITECTURE|VEX Architecture]]
- **Deployment Status:** [[VEX-DEPLOYMENT-READY|VEX Deployment Guide]]
- **September 9 Wiring:** [[23-VENTURES/Worldwidebro-Vex/VEX-WIRING-DEPLOYMENT-SEP-9|Wiring Deployment]] & [[23-VENTURES/Worldwidebro-Vex/WIRING-INTEGRATION-COMPLETE-SEP-9|Wiring Complete]]
- **Agentic Build Plan:** [[23-VENTURES/Worldwidebro-Vex/AGENTIC-BUILD-PLAN|Agentic Build Plan]]
- **Gap Analysis:** [[23-VENTURES/Worldwidebro-Vex/COMMAND-CENTER-GAP-ANALYSIS|Command Center Gap Analysis]]
- **VEX Specifications:** [[_REFERENCE/VEX-TAB-SPECIFICATIONS.yaml]], [[_REFERENCE/VEX-DASHBOARD-PRD]], [[_REFERENCE/VEX-DASHBOARD-TRD]], [[_REFERENCE/VEX-UI-UX-DESIGN]], [[_REFERENCE/VEX-APPFLOW]]

---

## 3. Local Development & Verification

```bash
cd "23-VENTURES/Worldwidebro-Vex"
npm install
npm run generate:data
npm run dev
# Serves local dev on http://localhost:3000
```
```bash
# Query AST symbol dependencies with GitNexus
./scripts/gitnexus context Dashboard -r Worldwidebro-Vex
```
