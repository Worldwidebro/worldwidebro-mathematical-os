---
id: TPL-SITE-001
title: "Template: Canonical Site Asset Record"
type: template
category: site-asset
tags: [template, site, asset, web-properties, vercel]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_TEMPLATES/README|Templates Gallery]] | [[_TEMPLATES/DOMAIN_TEMPLATE|Domain Template]] | [[_TEMPLATES/URL_TEMPLATE|URL Template]] | [[23-VENTURES/23-VENTURES|Ventures]]

# SITES.md Template — Canonical Digital Property & Application Record

```yaml
site_id: "SITE-0001"
site_name: "HealthRoute Medical Dispatch Portal"
site_type: "PORTAL" # CORPORATE | MARKETING | ECOMMERCE | SAAS | MARKETPLACE | PORTAL | ADMIN | DASHBOARD | LANDING_PAGE
primary_domain: "lt-005-medical-courier-dispatch.vercel.app"
venture_id: "LT-005"
brand_id: "BRD-0001"
status: "LIVE"

# Architecture & Routes
architecture:
  homepage: "/"
  routes:
    - "/dispatch"
    - "/orders/new"
    - "/tracking/:id"
    - "/invoices"
    - "/api/webhooks/stripe"
  authentication: true
  auth_provider: "NextAuth / Supabase"
  checkout: true

# Business Function & Commerce Engine
business_function: "DELIVERY" # AWARENESS | ACQUISITION | LEAD_GENERATION | QUALIFICATION | SALES | CHECKOUT | PAYMENT | DELIVERY | OPERATIONS
funnel:
  entry_points: ["Landing Page", "Partner Portal"]
  primary_cta: "Book STAT Courier"
  conversion_events: ["Dispatch Created", "Order Paid"]

# Technical Stack
technology:
  frontend: "Next.js 14 / React"
  backend: "Node.js / Next.js Server Actions"
  database: "PostgreSQL (Mac Studio)"
  hosting: "Vercel"
  payments: "Stripe"
  analytics: "None"
  monitoring: "Langfuse / Grafana"

# Live Health
health:
  uptime_pct: 99.9
  ssl_valid: true
  last_http_code: 200
  last_scanned: "2026-09-05"
```

---

## Template Context & Registries
- Master Gallery: [[_TEMPLATES/README|Templates Gallery]]
- Canonical Sites Registry: [[_REGISTRIES/CANONICAL/SITES_REGISTRY.yaml|SITES_REGISTRY.yaml]]
- Associated Venture Hub: [[23-VENTURES/23-VENTURES]]
