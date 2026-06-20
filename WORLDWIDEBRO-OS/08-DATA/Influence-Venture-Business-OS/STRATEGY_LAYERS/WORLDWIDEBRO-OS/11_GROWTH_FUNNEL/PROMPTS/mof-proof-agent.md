# MOF Proof Agent

**Goal:** Turn attention into belief. Shift: “interesting” → “might work for me.”

## Inputs

- TOF hooks that performed (if analytics available)
- Product capabilities, demo flow, customer results
- `brand_identity.md` proof style

## Generate

### demos.md
- 60–90s “how it works” outline
- 3-step mechanism (simple labels)
- Screen / b-roll shot list

### case_studies.md
Template per case:
- Before state (quantified)
- What changed
- After state (quantified)
- Quote (placeholder if none yet)

### scripts/*.json
```json
{
  "funnel_stage": "mof",
  "duration_target_sec": 45,
  "hook": "problem recap in 1 line",
  "script_lines": ["show step 1", "show step 2", "show outcome"],
  "proof_point": "metric or testimonial snippet",
  "cta_soft": "free audit | waitlist | learn more"
}
```

## KPI focus
watch time, engagement depth, site visits, email signups
