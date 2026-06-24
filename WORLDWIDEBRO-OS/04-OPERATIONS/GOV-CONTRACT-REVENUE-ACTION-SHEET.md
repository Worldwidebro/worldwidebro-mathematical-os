# Government Contract Revenue — Action Sheet

**Goal:** First dollar from construction (CON-009 roofing / CON-011 electrical) by
**subcontracting to NC general contractors who already win federal work**, while
starting SAM.gov registration to prime later.

**The honest bottleneck:** Everything below is calls and forms. The system work is
done. Money starts the moment you contact GC #1.

---

## LANE 1 — Subcontract to NC GCs (fastest dollar, no SAM.gov needed)

These are real primes pulled from USASpending into Supabase `gov_awards` (98 NC
federal construction awards, $372M total). The ones below are NC-local repeat
winners who actively use subcontractors.

### Monday Call List (verified contacts)

| # | GC | City | Why | Action | Contact |
|---|----|------|-----|--------|---------|
| 1 | **SYNCON LLC** | Chesapeake VA (covers N. NC) | 6 awards · SDVOSB · **has sub signup page** | Fill pre-qual form → call estimating | ☎ (757) 351-0770 · synconllc.com/subcontractors |
| 2 | **HICAPS Inc** | Greensboro NC | 3 awards · builds sub packages for SB/SDVOSB goals | Call → ask for prequalification/estimating | 600 N. Regional Rd, Greensboro · hicaps.com |
| 3 | **Group III Management** | Kinston NC | 2 awards · NC + upstate SC GC | Call, offer trade capacity | ☎ (252) 527-3333 · groupiiimgt.com/contact |
| 4 | **Riley Contracting Group** | Cary NC | 4 awards · veteran-owned | Contact page, offer crews | rileycontracting.com/contact · PO Box 4948, Cary |
| 5 | **CMC Building Inc** | Raleigh/Wilmington NC | 5 awards (steadiest pipeline) · 1989, fed/state/local | Contact form → ask to join sub network | cmcbuildinginc.com |

> Full 98-prime list lives in Supabase `gov_awards`. Re-run the loop anytime to
> refresh: `python3 WORLDWIDEBRO-OS/04-OPERATIONS/loops/04-USASPENDING-CONTRACTS.py`

### The Pitch (email or phone — swap in your trade)

> "I'm a Charlotte-based [roofing / electrical] subcontractor with crews available
> for your federal and commercial NC projects. I saw you're active on regional
> [VA/DoD] construction. Can I get added to your pre-qualified subcontractor list
> for upcoming bids?"

---

## LANE 3 — SAM.gov registration (long game, start in parallel, ~2–3 weeks)

So you can bid as a **prime**, not just sub:

1. Get a **UEI** at sam.gov (free; replaces old DUNS)
2. Complete **entity registration** — Winners Circle WC LLC info, bank, NAICS
   238160 (roofing), 238210 (electrical), 236220 (commercial bldg)
3. Finish **Reps & Certs**; apply for **small-business / SDVOSB** set-asides if eligible
4. Add `SAM_GOV_API_KEY` to `.env` → the `05-SAM-OPPORTUNITIES.py` loop turns open
   RFPs into a biddable feed

---

## System Status (done — no more infra needed)

- ✅ `04-USASPENDING-CONTRACTS.py` — LIVE, pulled 98 NC awards → `gov_awards`
- ⏳ `05-SAM-OPPORTUNITIES.py` — ready, blocked only on `SAM_GOV_API_KEY`
- ✅ Supabase tables: `gov_awards`, `gov_opportunities`
- ✅ Branch: `2026-06-19-os-consolidation`, loops at `04-OPERATIONS/loops/`

---

## CLOSE-OUT CHECKLIST (what's left — all on you)

**This week (Lane 1 — money):**
- [ ] Call/sign up with SYNCON (sub form) — #1
- [ ] Call HICAPS estimating — #2
- [ ] Call Group III (252) 527-3333 — #3
- [ ] Contact Riley + CMC via web forms — #4, #5
- [ ] Decide trade to lead with: roofing (CON-009) or electrical (CON-011)
- [ ] Confirm crew/sub source + your markup rate before quoting

**This week (Lane 3 — setup, parallel):**
- [ ] Get UEI at sam.gov
- [ ] Start entity registration (NAICS 238160 / 238210 / 236220)
- [ ] Once you have a SAM API key → add `SAM_GOV_API_KEY` to `.env`, run loop 05

**Optional (only if you want the pipeline to auto-sell):**
- [ ] Wire loop `02-SEND-EMAILS.py` to real email (Resend) — currently mock
- [ ] Build loop 06: push `gov_awards` primes to HubSpot as companies for tracking

**Status to update when done:** mark first GC contacted, first bid invite, first job.

> You can close this chat. Nothing technical is blocking — the next move is a phone call.
