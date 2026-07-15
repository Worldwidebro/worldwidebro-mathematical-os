# Sales Scripts — Venture Staffing Operations

Live offer (from ops-staff-001-staffing.vercel.app): temp/contract staffing, direct-hire
recruiting, AI agent deployment, payroll/EOR. <24h avg time to first match, 90-day placement
guarantee. Serves Construction, Logistics, Healthcare, Skilled Trades, Admin.

## Cold call script (60-90 sec, adapt per trade)

> "Hi, this is [Name] with Worldwidebro Staffing — I work with [electrical/commercial GC/HVAC]
> contractors around Charlotte on getting skilled crew fast when you're short-handed. I saw
> [Company] has been hiring [pull from their careers page] — quick question: when you need a
> [electrician/laborer/tech] on a job this week, what's that process look like for you right now?
>
> [Listen]
>
> Got it. We place vetted contract and direct-hire workers in under 24 hours on average, and we
> carry a 90-day placement guarantee, so if it doesn't work out you're not stuck. Would it make
> sense to send over rates for your two or three most common roles, no obligation, so you have it
> on file next time you're in a pinch?"

## Cold email template

> Subject: Faster crew when [Company] is short-handed
>
> Hi [First name],
>
> I work with Charlotte-area [electrical/commercial GC/HVAC] contractors on temp and direct-hire
> staffing — noticed [Company] [specific hook, e.g. "has an active careers page" / "does a lot of
> industrial/warehouse work" / "has been in the Charlotte market since 1999"].
>
> We place vetted skilled-trades and warehouse workers in under 24 hours on average, run a 90-day
> placement guarantee, and can also handle payroll/EOR if you'd rather not carry W-2 overhead on
> temp crew.
>
> Worth 10 minutes to send over rates for your most common roles? No obligation — just good to
> have on file for the next time you're short.
>
> [Name]
> Worldwidebro Staffing

## qualifying questions

1. What's your current timeline for this problem?
2. Who owns this today?
3. What would faster execution be worth?

## engines

| Engine | Ask | Channel |
|--------|-----|---------|
| A — B2G/sub | Add me to prequalified lists | Bid boards + prime prequal |
| B — retainer | 15 min managing this ongoing | LinkedIn + referrals |
| C — productized | Fixed-price quote | Direct outbound + web offer |

## Call list — HIGH priority (source: `staffing_prospects`, all `not_contacted` as of 2026-07-14)

Call these three first — largest / most active hiring signal:

1. **Morris-Jenkins** — (704) 357-0484 — "very large home-services co; constant hiring"
2. **WB Moore Company** — (704) 331-9300 — "explicit careers/employment page"
3. **Michael & Son** — (704) 594-5420 — "high hiring volume"

Then the rest of the HIGH-priority list:

| Company | Sector | Phone | Location | Notes |
|---|---|---|---|---|
| Southside Constructors | Commercial GC | (704) 825-8881 | Charlotte NC | Since 1999, 300+ commercial projects |
| Moser Commercial Construction | Commercial GC | (704) 882-1700 | Indian Trail NC | HBA member |
| ARCO Design/Build Charlotte | Commercial GC (industrial) | (704) 856-3056 | Charlotte NC | Pres. Eric Thompson |
| Evans General Contractors | Commercial GC | — (pull from site) | Charlotte NC | VP Chad Marshall |
| Edifice Inc | Commercial GC (large) | — (pull from site) | Charlotte NC | ENR Top 400 |
| Roby Commercial | Electrical (commercial) | (704) 334-5477 | Charlotte NC | High headcount |
| Recore Electrical Contractors | Electrical (industrial) | (704) 867-1647 | Gastonia NC | Industrial/new-construction |
| Acosta Heating Cooling & Electrical | HVAC + Electrical | (704) 292-6242 | Charlotte NC | Family-owned since 1972 |
| Horne Heating & Air Conditioning | HVAC+Plumbing+Electrical | (704) 321-4173 | Charlotte NC | 40+ yrs |
| Bonded Logistics | Warehouse/3PL | — (pull from site) | Charlotte NC | 200+ employees |
| Distribution Technology | Warehouse/3PL | (704) 587-5587 | Charlotte NC | 1.2M sqft |
| Saddle Creek Logistics | Warehouse/3PL | (704) 454-6300 | Harrisburg NC | Non-union, hires supervisors |

After each call/email, update the row in Supabase `staffing_prospects`:
`update staffing_prospects set status='contacted', last_touch=now() where company='...';`
