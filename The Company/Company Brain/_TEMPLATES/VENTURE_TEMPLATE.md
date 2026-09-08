---
id: TPL-VEN-001
title: "Template: Master Venture Specification"
type: template
category: venture
tags: [template, venture, reality, commercial, business-model]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_TEMPLATES/README|Templates Gallery]] | [[REALITY]] | [[23-VENTURES/23-VENTURES|Ventures]] | [[ECONOMIC-REALITY]]

# VENTURE.md Template — Master Venture Specification

```yaml
# ==============================================================================
# 1. IDENTITY
# ==============================================================================
id: "VEN-001"
venture_id: "VEN-001"
name: "Venture Name"
legal_name: "WorldwideBro Venture LLC"
brand_name: "Brand Name"
aliases: ["ShortAlias", "CodeName"]
slug: "venture-name"
type: "SAAS" # SAAS | MARKETPLACE | SERVICES | ECOMMERCE | LOGISTICS | CAPITAL | HARDWARE
status: "BUILDING" # IDEA | DISCOVERY | VALIDATING | BUILDING | PRELAUNCH | LIVE | REVENUE | GROWING | PROFITABLE | STALLED | DORMANT | PAUSED | ACQUIRED | MERGED | SOLD | CLOSED | KILLED | ARCHIVED
lifecycle_stage: "SEED"
founded_date: "2026-01-01"
incorporation_date: ""
jurisdiction: "Delaware, USA"
headquarters: "Remote / New York"
operating_regions: ["US-East", "Global"]

# ==============================================================================
# 2. REALITY CLASSIFICATION (Governed by REALITY.md)
# ==============================================================================
reality:
  classification: "SPECULATIVE" # OPERATING | SPECULATIVE
  evidence_level: "UNVERIFIED"  # VERIFIED | HIGH | MODERATE | UNVERIFIED
  verified: false
  last_verified: "2026-09-05"
  verification_source: ""
  commercial_status: "NO_REVENUE" # REVENUE_GENERATING | PILOT | NO_REVENUE
  operating_status: "BUILDING"    # FULLY_OPERATIONAL | PARTIAL | INACTIVE
  revenue_status: "ZERO"         # PROFITABLE | BREAKEVEN | BURNING | ZERO
  customer_status: "NO_CUSTOMERS"# PAYING | SIGNED_LOI | DEMO | NO_CUSTOMERS

# ==============================================================================
# 3. THESIS
# ==============================================================================
thesis:
  problem: "Concise description of the acute commercial pain point."
  customer: "Specific ideal customer profile suffering this pain."
  solution: "The automated, high-margin software/service solution."
  why_now: "Market or technological inflection point enabling this today."
  value_proposition: "Quantified economic return for the customer."
  differentiation: "Why competitors or incumbents cannot easily copy."
  unfair_advantage: "Proprietary internal capability, data, or network leverage."
  business_model: "Direct monetization mechanics."
  growth_thesis: "Primary distribution and customer acquisition loops."
  exit_thesis: "Strategic buyers, holding dividend, or recapitalization."

# ==============================================================================
# 4. PROBLEM SPECIFICATION
# ==============================================================================
problem:
  problem_id: "PRB-001"
  description: "Detailed description of the operational or economic bottleneck."
  affected_customer: "Roles or business sizes directly impacted."
  severity: "CRITICAL" # CRITICAL | HIGH | MEDIUM | LOW
  frequency: "DAILY"    # HOURLY | DAILY | WEEKLY | MONTHLY | OCCASIONAL
  current_solution: "Inefficient manual workflows, spreadsheets, or overpriced SaaS."
  cost_of_problem: "$10,000+/year in wasted labor or missed opportunities."
  willingness_to_pay: "$500 - $2,500/mo"
  evidence: "Interviews, industry benchmarks, or internal operational pain."

# ==============================================================================
# 5. CUSTOMER & TRACTION
# ==============================================================================
customers:
  icp: "Target company profile, ARR, headcount, and tech stack."
  personas: ["Operations Director", "Dispatch Manager", "Managing Partner"]
  segments: ["Mid-market B2B", "Specialized Logistics"]
  industries: ["Healthcare", "Transportation", "Construction"]
  geographies: ["United States"]
  buyer: "Executive with budget authority"
  decision_maker: "Founder / VP Ops"
  champion: "Daily end-user"
traction:
  leads: 0
  prospects: 0
  qualified: 0
  demos: 0
  proposals: 0
  pilots: 0
  customers: 0
  paying_customers: 0
  churned_customers: 0

# ==============================================================================
# 6. PRODUCT & CAPABILITIES
# ==============================================================================
product:
  product_id: "PRD-001"
  name: "Product Platform"
  category: "Enterprise Dispatch Software"
  description: "Web application and automated engine powering the service."
  capabilities: ["CAP-009", "CAP-AUTHENTICATION", "CAP-PAYMENTS"]
  features: ["Automated intake", "Live GPS tracking", "Instant invoice generation"]
  integrations: ["Stripe", "Twilio", "PostgreSQL", "Google Maps"]
  dependencies: ["Trigger.dev", "Vercel", "Tailscale"]
  roadmap: "Feature release schedule."
  maturity: "ALPHA" # PROTOTYPE | ALPHA | BETA | GA
  mvp: true
  production: false

# ==============================================================================
# 7. BUSINESS MODEL & MONETIZATION
# ==============================================================================
business_model:
  model: "TRANSACTION_AND_SAAS" # SAAS | MARKETPLACE | TRANSACTION | RETAINER | SERVICES
  monetization: "Per-dispatch fee + Monthly base platform fee"
  pricing: "$150/mo base + $15 per dispatch"
  packaging: ["Starter", "Professional", "Enterprise"]
  contract_type: "MONTH_TO_MONTH" # ANNUAL | MULTI_YEAR | MONTH_TO_MONTH | USAGE
  billing_frequency: "MONTHLY"
  average_contract_value: 3500 # Annual ACV in USD
  recurring: true
  services: false
  software: true
  marketplace: false
  transaction_fee: 0.05

# ==============================================================================
# 8. REVENUE & UNIT ECONOMICS
# ==============================================================================
revenue:
  current: 0.00
  mrr: 0.00
  arr: 0.00
  last_30_days: 0.00
  last_90_days: 0.00
  lifetime: 0.00
  gross_margin: 0.85
  contribution_margin: 0.70
  revenue_per_customer: 0.00
unit_economics:
  cac: 250.00
  ltv: 4500.00
  ltv_cac: 18.0
  payback_period_months: 1.5
  churn_monthly: 0.02
  retention_annual: 0.90

# ==============================================================================
# 9. MARKET & COMPETITION
# ==============================================================================
market:
  industry: "Specialized Logistics"
  tam: "$15B"
  sam: "$1.8B"
  som: "$45M"
  market_growth: "12% CAGR"
  regulations: ["HIPAA", "DOT", "OSHA"]
competition:
  direct: ["Competitor A", "Competitor B"]
  indirect: ["In-house staff using email and spreadsheets"]
  substitutes: ["General couriers (Uber Direct, DoorDash Drive)"]
  do_nothing_alternative: "Manual pen-and-paper tracking"
  competitive_advantage: "Fully automated dispatch with local-first AI edge agents."

# ==============================================================================
# 10. TEAM & CAPITAL
# ==============================================================================
team:
  founders: ["Operator"]
  key_people: []
  contractors: []
  hiring_needs: []
capital:
  bootstrapped: true
  invested: 0.00
  debt: 0.00
  grants: 0.00
  total_raised: 0.00
  runway_months: 99
  burn_monthly: 0.00

# ==============================================================================
# 11. REPOSITORIES & DIGITAL ASSETS
# ==============================================================================
repositories:
  - repo_id: "OWN-PRIV-0002"
    github_url: "https://github.com/Worldwidebro/lt-005-medical-courier-dispatch"
    purpose: "Primary application frontend and dispatch API"
    production: true
    status: "ACTIVE"

digital:
  domains: ["DOM-0001"]
  urls: ["URL-0001"]
  sites: ["SITE-0001"]
```

---

## Template Context & Registries
- Master Gallery: [[_TEMPLATES/README|Templates Gallery]]
- Master Ventures Hub: [[23-VENTURES/23-VENTURES]]
- Ground Truth Protocol: [[REALITY]]
- Canonical Venture Registry: [[_REGISTRIES/VENTURE_REGISTRY.yaml]]
