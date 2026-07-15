# NexusDispatch ↔ vex-hero-site Integration Plan

**Scope:** Launch NexusDispatch as unified logistics OS across all 30 LT-ventures  
**Timeline:** This week (2026-07-16 → 2026-07-22)  
**Deployment:** vex-hero-site + venture card updates  

---

## Work Breakdown (3 Parallel Tracks)

### Track 1: NexusDispatch Sector Page

**Deliverables:**
- `vex-hero-site/app/logistics/nexusdispatch/page.mdx` (hero + positioning)
- `vex-hero-site/app/logistics/nexusdispatch/architecture.mdx` (4-tier diagram)
- `vex-hero-site/app/logistics/nexusdispatch/roadmap.mdx` (Phase 1-3 timeline)
- `vex-hero-site/components/nexusdispatch/ArchitectureDiagram.tsx` (interactive diagram)
- `vex-hero-site/components/nexusdispatch/VentureConsolidationMap.tsx` (30 ventures visual)

**Content:**
- Hero: "One AI OS. 30 Logistics Ventures. Infinite Possibilities."
- Problem: Fragmented dispatch systems across verticals
- Solution: Unified orchestration engine (agents, compliance, routing)
- Phase roadmap: Q2 2027 (trucking), Q4 2027 (8 verticals), Q2 2028 (all 30)
- CTA: "Join Beta Fleet" (links to `/beta-signup`)

**Est. Time:** 6 hours

---

### Track 2: Venture Consolidation Manifest

**Deliverables:**
- `vex-hero-site/data/nexusdispatch-ventures.json` (30 venture metadata + module mapping)
- `vex-hero-site/app/logistics/ventures/_components/VentureCard.tsx` (updated card with NexusDispatch badge)
- Updated all 30 venture card frontmatter (status, nexusdispatch_module, phase)

**Data Structure (per venture):**
```json
{
  "id": "LT-001",
  "name": "Truck Dispatch Company",
  "status": "validation",
  "nexusdispatch_module": "trucking",
  "nexusdispatch_phase": "phase_1",
  "featured": true,
  "operations_status": "pilot",
  "metrics": {
    "active_carriers": 0,
    "avg_rpm_improvement": 0,
    "compliance_violations": 0
  }
}
```

**Mapping (30 ventures → modules):**
- **Trucking Module (Phase 1):** LT-001, LT-003, LT-016
- **Last-Mile Module (Phase 2):** LT-004, LT-018, LT-022
- **Field Service Module (Phase 2):** LT-009, LT-010, LT-007
- **Medical/Specialized (Phase 3):** LT-005, LT-030
- **Freight Brokerage (Phase 2):** LT-002, LT-020, LT-026
- **Warehouse/Fulfillment (Phase 3):** LT-021, LT-023, LT-022
- **Fleet/Tracking (Phase 3):** LT-012, LT-027, LT-015
- **Supply Chain (Phase 3):** LT-029, LT-014, LT-028, LT-013
- **Courier/Local (Phase 3):** LT-017, LT-019, LT-024, LT-025, LT-011, LT-006

**Est. Time:** 4 hours

---

### Track 3: Live Status Dashboard

**Deliverables:**
- `vex-hero-site/components/nexusdispatch/StatusDashboard.tsx` (real-time metrics display)
- `vex-hero-site/data/nexusdispatch-metrics.json` (source of truth for KPIs)
- `vex-hero-site/app/logistics/nexusdispatch/status.mdx` (public dashboard page)

**Dashboard Metrics:**
```
┌─────────────────────────────────────────┐
│ NexusDispatch Real-Time Operations      │
├─────────────────────────────────────────┤
│ ✅ Phase 1 MVP Status                   │
│    Week 12 Launch Target: Jan 2027      │
│    Current Progress: Pre-development    │
│                                          │
│ 🚀 Active Fleets Onboarded              │
│    Target: 50 by Q2 2027                │
│    Current: 0 (pre-launch)              │
│                                          │
│ 📈 Average RPM Improvement              │
│    Target: 15% improvement              │
│    Current: N/A (pre-launch)            │
│                                          │
│ 🛡️ Compliance Violations                │
│    Target: 0 violations                 │
│    Current: 0 (pre-launch)              │
│                                          │
│ 💼 Ventures Powered                     │
│    Phase 1: 3 ventures                  │
│    Phase 2: 8 ventures                  │
│    Phase 3: 30 ventures (target)        │
└─────────────────────────────────────────┘
```

**Data Updates (post-launch):**
- Real metrics fed from NexusDispatch backend API
- Staged rollout (initially hardcoded → API-driven by Week 8)

**Est. Time:** 5 hours

---

## Execution Sequence

```
Parallel Development (all 3 tracks simultaneously)

Track 1: Sector Page
  ├─ Write hero content (1h)
  ├─ Create architecture diagram component (2h)
  ├─ Create consolidation map visual (2h)
  └─ Test + polish (1h)

Track 2: Venture Manifest
  ├─ Generate nexusdispatch-ventures.json (1h)
  ├─ Map 30 ventures to modules (1h)
  ├─ Update VentureCard component (1h)
  ├─ Update all 30 venture frontmatter (1h)
  └─ Test card rendering (30m)

Track 3: Status Dashboard
  ├─ Design dashboard layout (1h)
  ├─ Build StatusDashboard component (2h)
  ├─ Create metrics JSON (30m)
  ├─ Wire dashboard to `/status` page (1h)
  └─ Test responsiveness (30m)

Merge & Deploy (Wednesday)
  ├─ Test all links work (30m)
  ├─ Verify venture cards show badges (30m)
  ├─ Verify `/logistics/nexusdispatch` fully renders (30m)
  ├─ Deploy to staging (30m)
  └─ Deploy to production (30m)
```

---

## File Structure (New)

```
vex-hero-site/
├─ app/
│   └─ logistics/
│       ├─ nexusdispatch/
│       │   ├─ page.mdx (hero)
│       │   ├─ architecture.mdx (4-tier diagram)
│       │   ├─ roadmap.mdx (phases)
│       │   └─ status.mdx (live dashboard)
│       └─ ventures/
│           ├─ _components/
│           │   └─ VentureCard.tsx (updated with badge)
│           └─ [id]/
│               └─ page.mdx (30 venture pages, unchanged)
│
├─ components/
│   └─ nexusdispatch/
│       ├─ ArchitectureDiagram.tsx (4-tier visual)
│       ├─ VentureConsolidationMap.tsx (30 ventures)
│       └─ StatusDashboard.tsx (live metrics)
│
└─ data/
    ├─ nexusdispatch-ventures.json (30 venture metadata)
    └─ nexusdispatch-metrics.json (live KPIs)
```

---

## Integration Points

**vex-hero-site Navigation:**
```
Logistics Sector Page
├─ Hero: "NexusDispatch: One OS. 30 Ventures."
├─ Consolidation Map: "See all 30 ventures powered by NexusDispatch"
├─ Architecture: "4-tier system architecture + 8 autonomous agents"
├─ Roadmap: "Phase 1-3 launch timeline"
├─ Status: "Real-time operations dashboard"
└─ CTA: "Join Beta Fleet" → `/beta-signup`

Venture Cards (all 30)
├─ Badge: 🚀 "Powered by NexusDispatch"
├─ Phase: "Phase 1 | Phase 2 | Phase 3"
├─ Module: "Trucking | Last-Mile | Field Service | etc."
└─ Link: Click → `/logistics/nexusdispatch` (consolidated hub)
```

---

## Success Criteria

✅ **By Wednesday EOD:**
- [ ] `/logistics/nexusdispatch` page fully renders (hero + architecture + roadmap)
- [ ] All 30 venture cards display NexusDispatch badge + phase
- [ ] Status dashboard shows Phase 1 metrics (pre-launch state)
- [ ] All links work (venture cards → consolidation hub)
- [ ] Mobile responsive (tested on iPhone + iPad)

✅ **Deployment:**
- [ ] Deployed to staging (URL provided)
- [ ] Stakeholder review completed
- [ ] Deployed to production vex-hero-site

✅ **Analytics:**
- [ ] Track clicks: "/logistics/nexusdispatch" page views
- [ ] Track CTAs: "Join Beta Fleet" conversions
- [ ] Track venture card clicks from consolidated hub

---

## Launch Messaging (Social + Email)

**Headline:** "NexusDispatch: One AI OS Powers 30 Logistics Ventures"

**Body:**
```
We're consolidating our entire logistics portfolio into a single, 
unified operating system powered by AI agents.

From trucking to field service to medical logistics—all 30 ventures 
now run on NexusDispatch:
• 8 autonomous agents (dispatch, compliance, routing, invoicing)
• Real-time optimization
• FMCSA-compliant tracking
• <15 min time-to-book (vs. 45 min manual)

Phase 1 MVP ships Q2 2027 with 50 beta fleets.

Explore the architecture → vex-hero-site.com/logistics/nexusdispatch
```

---

## Blockers & Mitigations

| Blocker | Mitigation |
|---------|-----------|
| Venture data missing/incomplete | Use hardcoded defaults from VENTURE-READINESS-SCORECARD.csv |
| Architecture diagram too complex | Start with simpler boxes → add detail iteratively |
| 30 venture frontmatter outdated | Use data/nexusdispatch-ventures.json as source of truth |
| Mobile rendering issues | Test on real devices + use Playwright E2E |

---

**Owner:** Engineering Lead + PM  
**Status:** Ready to execute  
**ETA:** Wednesday 2026-07-18 EOD
