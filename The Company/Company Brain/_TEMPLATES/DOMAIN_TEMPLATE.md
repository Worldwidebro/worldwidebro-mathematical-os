---
id: TPL-DOM-001
title: "Template: Canonical Domain Asset Record"
type: template
category: domain-asset
tags: [template, domain, asset, infrastructure, dns]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_TEMPLATES/README|Templates Gallery]] | [[_TEMPLATES/SITE_TEMPLATE|Site Template]] | [[_TEMPLATES/URL_TEMPLATE|URL Template]] | [[23-VENTURES/23-VENTURES|Ventures]]

# DOMAINS.md Template — Canonical Domain Asset Record

```yaml
id: "DOM-0001"
domain_id: "DOM-0001"
domain: "healthroute.app"
root_domain: "healthroute.app"
tld: "app"
venture_id: "LT-005"
brand_id: "BRD-0001"

# Ownership & Registrar
ownership:
  owner_entity: "WorldwideBro LLC"
  venture: "LT-005"
  registrar: "Namecheap / Cloudflare / GoDaddy"
  registrar_account: "admin@worldwidebro.com"
  registered_date: "2026-01-15"
  expiration_date: "2027-01-15"
  auto_renew: true
  privacy_protected: true

# Technical DNS & Routing
dns:
  provider: "Cloudflare / Vercel DNS"
  nameservers:
    - "ns1.vercel-dns.com"
    - "ns2.vercel-dns.com"
  status: "ACTIVE" # ACTIVE | PENDING | PARKED | EXPIRED | SUSPENDED

# Relationships
relationships:
  belongs_to_venture: "LT-005"
  hosts_sites:
    - "SITE-0001"
  has_urls:
    - "URL-0001" # apex domain
    - "URL-0002" # app subdomain
```

---

## Template Context & Registries
- Master Gallery: [[_TEMPLATES/README|Templates Gallery]]
- Canonical Domains Registry: `_REGISTRIES/domain_registry.json`
- Associated Venture Hub: [[23-VENTURES/23-VENTURES]]
