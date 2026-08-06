---
name: VENDOR-PROCUREMENT-OS
title: Vendor & Procurement OS
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Vendor & Procurement OS

**Created:** 2026-05-09  
**Status:** Setup complete; ready for real vendor import

---

## Purpose

This is the Accio-style operating layer for GC and venture procurement.

```text
Job / venture need
  -> AI intake
  -> scope classifier
  -> vendor sourcing
  -> bid comparison
  -> approval
  -> work order
  -> execution tracking
  -> payable
  -> vendor score update
```

Supabase remains the source of truth. ClickUp remains the human execution and accountability layer.

---

## Live Sources Verified

| Source | Truth |
|---|---:|
| Supabase project | CivilizationOS / cyhzilqldouzgynacqpe |
| Main venture table | business_ventures |
| Ventures | 708 |
| Positions | 29 |
| Vendors | 0 |
| CRM contacts | 2 |
| CRM deals | 2 |
| AOC tasks | 5,264 |
| Venture tasks | 7,048 before setup insert |
| ClickUp workspace | Antwuan Johns's Workspace / 9013677375 |

`business_ventures_master` is not present in the live Supabase schema. Older docs that reference it are stale.

---

## Vendor Lifecycle

```text
prospect
  -> qualified
  -> quoted
  -> contracted
  -> active
  -> scored
  -> preferred
```

## RFQ Workflow

```text
Need created
  -> scope generated
  -> vendors matched
  -> quotes collected
  -> bid selected
  -> PO / work order issued
  -> execution tracked
  -> payment
  -> score updated
```

## Work Order Workflow

```text
Job request
  -> AI intake
  -> scope classifier
  -> vendor selection
  -> authority approval
  -> ClickUp execution task
  -> Supabase task record
  -> invoice / payment
```

## Payables Workflow

```text
Vendor invoice
  -> completion check
  -> quality approval
  -> finance review
  -> payment status update
  -> vendor score update
```

## Scorecard Rubric

Use a 100-point vendor score:

| Dimension | Points |
|---|---:|
| Quality | 25 |
| Speed / schedule reliability | 20 |
| Communication | 15 |
| Price discipline | 15 |
| Compliance / insurance | 15 |
| Rehire confidence | 10 |

Preferred vendor threshold: 85+.

---

## ClickUp Setup Completed

ClickUp plan limits blocked creation of new lists inside `AI Boss Hub`, so setup tasks were created and closed in the existing `Database & Schema` list.

Completed ClickUp task IDs:

- `86ahcyunc` - Vendor OS: Create operating layer
- `86ahcyung` - Vendor OS: Vendor lifecycle defined
- `86ahcyunh` - Vendor OS: RFQ workflow defined
- `86ahcyunj` - Vendor OS: Work order workflow defined
- `86ahcyunk` - Vendor OS: Payables workflow defined
- `86ahcyunn` - Vendor OS: Scorecard rubric defined
- `86ahcyunp` - Vendor OS: Marketplace research workflow defined
- `86ahcyunr` - Vendor OS: Live data verified

Matching completed rows were inserted into Supabase `venture_tasks` under `business_id = OPS-Procurement-OS`.

---

## Next Real-World Input Needed

The operating layer is ready. The next non-synthetic step is importing real vendors from:

- existing phone/email network
- subcontractor contacts
- Accio / Alibaba research
- Thomasnet
- Amazon Business
- referrals
- local contractor/vendor lists

No fake vendors were inserted. The live `vendors` table remains the clean destination for real supplier records.
