# First Clients — Charlotte Placement Launch (30-Day Plan)

**Goal:** First paid placement within 30 days. Model: **contingency direct-hire**
(client pays only on hire; no comp, payroll, or float). One placed $50–60K hire =
**~$10–12K** at a 20% fee.

> **Reality check:** there is no populated employer list yet. Step 1 is *building*
> the list — it does not exist in the DB (contact tables are near-empty). Treat this
> as the cold-start playbook, not a pull from an existing CRM.

---

## The machine (every link must work)

```
Employers → Job Orders → Candidates → Submittals → Interviews → Hire → Invoice → Cash
```

You are running **two pipelines in parallel** from day one: **demand** (employers
with open roles) and **supply** (candidates ready to place). A placement needs both.

---

## Target sectors (Charlotte) — who hires constantly + pays well

| Sector | Why | Roles to recruit for | Typical base → your fee @20% |
|--------|-----|----------------------|------------------------------|
| Electrical contractors | Chronic shortage, license = premium | Journeyman/master electrician, estimator, PM | $55–85K → $11–17K |
| HVAC | Same, seasonal urgency | Install tech, service tech, controls | $50–75K → $10–15K |
| Plumbing | Same | Journeyman plumber, service tech | $50–75K → $10–15K |
| Commercial construction (GCs) | Constant hiring, project-driven | Superintendent, estimator, PM, foreman | $60–110K → $12–22K |
| Logistics / 3PL / warehouse | High volume, fast decisions | Warehouse supervisor, dispatcher, ops manager | $45–70K → $9–14K |
| Property management | Steady turnover | Maintenance tech, leasing, PM | $40–65K → $8–13K |
| Medical / dental offices | Always short-staffed | Front office, MA, billing, office manager | $40–60K → $8–12K |
| Manufacturing | Skilled roles hard to fill | Maintenance tech, supervisor, QA | $50–75K → $10–15K |

**Start with the trades (electrical/HVAC/plumbing/GC).** Highest pain, highest fees,
owners answer their phones, decisions are fast.

---

## Step 1 — Build the employer list (target: 500, Week 1)

Build a simple sheet: `Company | Owner/Hiring contact | Phone | Email | Sector | Open role? | Last touch | Status`.

Sources (free):
- **Google Maps** — search "electrical contractor Charlotte NC" etc.; pull name/phone/site for each sector. ~50–100 per sector.
- **NC Secretary of State** business search — confirm legal names/registered agents.
- **Indeed / LinkedIn Jobs** — companies *already posting* the roles above = warm demand. Prioritize these.
- **Charlotte Regional Business Alliance** member directory.
- **Trade associations** — Carolinas AGC, ABC Carolinas, local electrical/HVAC chapters.
- **Google Maps reviews / sites** — find the owner's name for personalized outreach.

> Loop back to the website: every employer who fills the **Request Staff** form lands
> in `staffing_client_leads`; every candidate in `staffing_candidate_leads`. Work
> those daily.

## Step 2 — Build the candidate pipeline in parallel (target: 100, Weeks 2–3)

Sources:
- **Indeed resume search** (employer account), **LinkedIn**.
- **Facebook groups** — Charlotte trades/jobs groups; warehouse/driver groups.
- **Trade schools / community colleges** — CPCC, local electrical/HVAC programs (recent grads + instructors who know talent).
- **Referrals** — every candidate knows 3 more. Always ask.
- Each candidate signs the **Candidate Representation** consent before submittal.

---

## Step 3 — Outreach cadence (50 employer touches/day)

A 4-touch sequence per employer over ~8 business days. Multi-channel beats single.

| Day | Touch |
|-----|-------|
| 1 | Call (or voicemail) + same-day email |
| 3 | LinkedIn connect + short note |
| 5 | Second call |
| 8 | "Breakup" email |

Stop the sequence the moment they give you a job order — then go find candidates.

---

## Scripts

### Cold call opener (trades owner)
> "Hi `[Name]`, this is `[You]` with Worldwidebro Staffing here in Charlotte. I'll be
> quick — we place `[electricians/HVAC techs]` with shops like yours, and you only pay
> if you actually hire someone. Are you short anybody right now, or expecting to be?"

- If yes → "Great — what's the role, and what's it pay? I'll get you a couple of
  qualified people this week." (Take the **job order**: role, pay, must-haves,
  start date, who interviews.)
- If no → "No problem. Mind if I check back in a few weeks? And if you know another
  shop that's hiring, I pay referral thank-yous." (Always ask for a referral.)

### Cold email (subject: `Electricians in Charlotte — pay only if you hire`)
> Hi `[Name]`,
>
> I run a Charlotte recruiting desk focused on `[the trades]`. We find and screen
> `[electricians/techs]`, you interview the ones you like, and **you only pay a fee if
> you hire** — with a 90-day replacement guarantee.
>
> If you've got an opening (or will soon), reply with the role and I'll send 2–3
> qualified people this week. No retainer, no risk.
>
> `[You]` · Worldwidebro Staffing · `[phone]`

### LinkedIn note
> Hi `[Name]` — I place `[electricians/HVAC techs]` with Charlotte shops on a
> pay-only-if-you-hire basis. Happy to send a couple of vetted people if you're
> hiring. Open to connecting?

### Voicemail
> "Hi `[Name]`, `[You]` with Worldwidebro Staffing, `[phone]`. We place `[trade]` in
> Charlotte and you only pay if you hire. If you're short anyone, I can get you 2–3
> qualified people this week. `[phone]` — thanks."

### Breakup email
> Hi `[Name]` — I'll stop here so I'm not a pest. If hiring `[trade]` comes up, I can
> turn around 2–3 vetted candidates fast, pay-on-hire only. Keep my number: `[phone]`.

---

## 30-day execution

**Week 1 — Foundation + list**
- Finalize entity + sign-ready **Client Placement Agreement** + **Candidate Representation** (have attorney review).
- Get general-liability + E&O insurance quotes (no workers' comp needed for placement-only).
- Build the 500-employer sheet (prioritize companies already posting the roles).
- Deploy the site (Vercel import + env vars) so inbound forms persist.

**Week 2 — Demand**
- 50 employer touches/day. Goal: **3–5 signed job orders.**
- Start candidate sourcing (Indeed/LinkedIn/FB/schools).

**Week 3 — Supply + submittals**
- Source/screen 100 candidates; sign representation consents.
- Submit 3–5 candidates per open job order. Schedule interviews.

**Week 4 — Close**
- Push interviews → offer → accepted start date.
- **Fill 1 role. Invoice. Get a testimonial.** Then repeat and reinvest into temp-staffing setup (comp, payroll, factoring).

---

## KPIs (track weekly)

| Metric | Week-1 target | Why |
|--------|---------------|-----|
| Employers contacted | 250 | Top of funnel |
| Job orders signed | 3–5 | Demand proof |
| Candidates sourced | 100 | Supply |
| Submittals | 10+ | Throughput |
| Interviews | 5+ | Conversion |
| **Placements** | **1 (by day 30)** | Revenue proof |

The first placement matters more than any feature — it proves employer demand
converts to cash. Once the loop closes once, it's a volume game.

---

## Transition trigger: placement → temp staffing

Graduate into **temp/contract staffing** (recurring markup revenue) only after:
1. 3–5 placements closed (proves you can source + sell), **and**
2. Cash buffer or a **payroll-funding / factoring** line secured (covers the weekly
   payroll-vs-net-30 gap), **and**
3. **Workers' comp** + general liability bound, payroll provider (Gusto/ADP) + EIN +
   NC withholding/unemployment accounts set up, I-9/E-Verify process in place.

Until all three are true, stay placement-only.
