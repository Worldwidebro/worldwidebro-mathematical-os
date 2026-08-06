---
name: TAGGING-STANDARD
title: Tagging Standard for 712 Ventures
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Tagging Standard for 712 Ventures

**Version**: 1.0  
**Updated**: 2026-07-30  
**Applies To**: Every venture, every document, every request, every Hermes agent query  
**Purpose**: Machine-readable identifiers so 712 ventures sync without ambiguity

---

## Venture ID Format

`[SECTOR]-[NUMBER]`

```
CON-001 (ACE Construction)
LT-005  (Logistics)
FIN-012 (Finance)
MED-003 (Medical)
```

---

## Status Tags (Fixed Vocabulary)

```
[NOT_STARTED]  |  [IN_PROGRESS]  |  [BLOCKED]  |  [TESTING]  |  [READY]  
[DEPLOYED]     |  [LIVE]         |  [FAILED]   |  [ARCHIVED]
```

---

## Action Tags

```
[BUILD]  |  [TEST]  |  [DEPLOY]  |  [CONNECT]  |  [AUDIT]  |  [FIX]  
[REFACTOR]  |  [CONFIGURE]  |  [MONITOR]  |  [REVIEW]
```

---

## Priority Tags

```
[P0]  CRITICAL   (Revenue at risk, security issue, venture down)
[P1]  HIGH       (Launch blocker, compliance required)
[P2]  MEDIUM     (v1.1 feature, nice to have)
[P3]  LOW        (Future improvement)
[P4]  NICE       (Best-effort, speculative)
```

---

## Every Venture Document Header

```markdown
[Venture]       CON-001
[Sector]        Construction
[Status]        LIVE
[Owner]         Name
[Updated]       2026-07-30
[Confidence]    VERIFIED | ESTIMATED | ASSUMED | UNCONFIRMED
[Source]        SUPABASE, GITHUB, VERCEL
```

---

## Hermes Agent Query Format (MANDATORY)

```
[TYPE]          VENTURE_CONNECTION | CAPABILITY_MAP | AUDIT | etc.
[VENTURE]       CON-001
[ACTION]        CONNECT | BUILD | TEST | AUDIT | FIX
[OBJECTIVE]     One-liner: what should happen when done?
[DEPENDENCIES]  venture:LT-012, capability:payment-processing
[BLOCKERS]      What's preventing this? (or "None")
[PRIORITY]      P0 | P1 | P2 | P3 | P4
[TIMELINE]      By 2026-08-01 (or "ASAP")
[SUCCESS]       How do we know this worked?
[OUTPUT]        What should Hermes deliver? (Code | Plan | Report)
[NEXT]          What happens after this?
```

---

## Example Hermes Query

```
[TYPE] VENTURE_CONNECTION
[VENTURE] CON-042
[ACTION] CONNECT
[OBJECTIVE] Enable form submissions to create CRM leads
[DEPENDENCIES] CON-042 Jotform account (ready), CRM API (ready)
[BLOCKERS] None
[PRIORITY] P1
[TIMELINE] 2026-08-01
[SUCCESS] Create 5 test leads, verify in admin
[OUTPUT] Code + runbook link
[NEXT] Configure Stripe webhook
```

Hermes parses this → Loads CON-042 context + lead-capture docs → Executes

---

## GitHub Issues (Same Tags)

```
Title: [CON-001] [ACTION: DEPLOY] Payment webhook integration

Labels:
  venture:con-001
  action:deploy
  priority:p1
  status:in_progress
  sector:construction

Body:
[Venture]      CON-001
[Objective]    Enable payment processing via Stripe
[Dependencies] Stripe API (ready), webhook handler (ready)
[Success]      Process $100 test transaction, verify in DB
```

---

## Venture Registry (Source of Truth)

One file listing all 712 ventures with metadata:

`VENTURE-REGISTRY.json`

```json
{
  "ventures": [
    {
      "venture_id": "CON-001",
      "name": "ACE Construction",
      "sector": "construction",
      "status": "LIVE",
      "stage": "MVP",
      "owner": "Antwuan Johns",
      "revenue_monthly": { "value": 2500, "confidence": "VERIFIED" },
      "created": "2026-06-15",
      "updated": "2026-07-30",
      "repos": ["worldwidebro/con-ventures:con-001-ace-construction"],
      "deployment_url": "https://con-001.vercel.app",
      "capabilities": ["lead-capture", "invoicing", "payments"],
      "dependencies": [],
      "blockers": [],
      "tags": ["construction", "smb", "b2b"]
    }
    // ... 711 more
  ]
}
```

Hermes loads this first for any query.

---

## Benefits

✅ **Search**: `[VENTURE] CON-001 [PRIORITY] P0` finds all critical issues  
✅ **Automation**: GitHub Actions trigger on tags (deploy if `[STATUS] READY`)  
✅ **Hermes**: Agent knows exactly which context to load (0 clarifications needed)  
✅ **Reports**: Count ventures by status, sector, priority  
✅ **Monitoring**: Track progress across 712 ventures in one table
