---
id: TPL-URL-001
title: "Template: Canonical URL Endpoint Record"
type: template
category: url-asset
tags: [template, url, asset, routing, cdn]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_TEMPLATES/README|Templates Gallery]] | [[_TEMPLATES/DOMAIN_TEMPLATE|Domain Template]] | [[_TEMPLATES/SITE_TEMPLATE|Site Template]] | [[23-VENTURES/23-VENTURES|Ventures]]

# URL.md Template — Canonical URL Asset Record

```yaml
id: "URL-0001"
url_id: "URL-0001"
url: "https://lt-005-medical-courier-dispatch.vercel.app"
normalized_url: "https://lt-005-medical-courier-dispatch.vercel.app"
canonical_url: "https://healthroute.app"
domain: "vercel.app"
subdomain: "lt-005-medical-courier-dispatch"
protocol: "https"
port: 443
path: "/"

# Asset Type & Role
type: "APP" # DOMAIN | SUBDOMAIN | WEBSITE | LANDING_PAGE | APP | API | DOCS | SHOP | CHECKOUT | PORTAL | DASHBOARD | LOGIN | REDIRECT
status: "LIVE" # UNKNOWN | UNREGISTERED | REGISTERED | PARKED | REDIRECT | LIVE | DEAD | EXPIRED | BROKEN | PRIVATE

# Ownership & Attribution
ownership:
  owner: "WorldwideBro"
  venture_id: "LT-005"
  site_id: "SITE-0001"
  brand_id: "BRD-0001"

# Technical & Infrastructure
technical:
  hosting: "Vercel"
  serverless_region: "iad1"
  cdn: "Vercel Edge Network"
  ssl: true
  tls_version: "TLS 1.3"
  http_status: 200
  technologies: ["Next.js", "React", "TailwindCSS"]

# Graph Relationships
relationships:
  belongs_to_venture: "LT-005"
  deploys_from_repo: "OWN-PRIV-0002"
  hosts_site: "SITE-0001"
  redirects_to: ""
```

---

## Template Context & Registries
- Master Gallery: [[_TEMPLATES/README|Templates Gallery]]
- Canonical URLs Registry: `_REGISTRIES/domain_registry.json`
- Associated Venture Hub: [[23-VENTURES/23-VENTURES]]
