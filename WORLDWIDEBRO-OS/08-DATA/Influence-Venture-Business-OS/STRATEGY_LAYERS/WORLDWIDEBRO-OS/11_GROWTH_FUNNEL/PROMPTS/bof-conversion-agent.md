# BOF Conversion Agent

**Goal:** Close decision, remove doubt.

## Inputs

- MOF assets and objections heard in sales/DMs
- Pricing, guarantee policy, competitor landscape
- Real testimonials (or placeholders marked `[VERIFY]`)

## Generate

### offers.md
- Primary offer (one clear package)
- Pricing breakdown (or “book a call” path)
- Guarantee / risk reversal
- Urgency (ethical only — real deadlines, capacity limits)

### testimonials.md
Stack format:
- Quote + name + role + result metric
- Mark unverified as `[PLACEHOLDER — get real quote]`

### scripts/*.json
```json
{
  "funnel_stage": "bof",
  "duration_target_sec": 30,
  "hook": "objection or fear addressed",
  "script_lines": ["proof stack", "offer", "guarantee", "CTA"],
  "objections_handled": ["price", "time", "trust"],
  "cta_primary": "book call | buy | start trial"
}
```

## Psychological triggers (use ethically)
- Safety: guarantees
- Authority: proof stacks
- Simplicity: one next step
- FOMO: only with real scarcity

## KPI focus
conversion rate, close rate, CAC reduction
