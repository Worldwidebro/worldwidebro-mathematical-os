---
references:
  - [[REPOSITORY-REGISTRY]]
  - [[../../INFRASTRUCTURE_LAYERS/REPOSITORY-INTELLIGENCE-SYSTEM]]
---

# Repository Layer Strategy: Owned vs Starred by Venture

**Execution Date:** 2026-06-11  
**Analysis:** 1,592 repos (858 owned + 734 starred)  
**Objective:** Strategic allocation of repos across 4 layers for 6 ventures  

---

## QUICK REFERENCE: 4 LAYERS

| Layer | Count | Owned | Starred | Strategy |
|-------|-------|-------|---------|----------|
| **Infrastructure** | 24 | 3 | 21 | Use OWNED, complement with STARRED |
| **Service** | 68 | 18 | 50 | Use OWNED wrappers, wrap STARRED SDKs |
| **Product** | 307 | 120 | 187 | Use OWNED ventures, reference STARRED |
| **Asset** | 602 | 250 | 352 | Merge OWNED + STARRED practices |
| **UNCLASSIFIED** | 591 | 400 | 191 | Classify & route to layer |

---

## LAYER 1: INFRASTRUCTURE (24 repos)

### Priority: OWNED > STARRED (Integration Critical)

**Use OWNED Infrastructure:**
- graphify (custom graph visualization)
- iza-os-vector-database (custom vector storage)
- postgres-mcp (PostgreSQL integration)
- Supabase + SUPABASE-SCHEMA-LOOPS (19 tables - core data)

**Complement with STARRED Infrastructure:**
- Prometheus (monitoring)
- Grafana (dashboards)
- Qdrant (vector search)
- Coolify (self-hosted deployment)

**For All 6 Ventures:** Shared infrastructure layer
- Supabase schema (SUPABASE-SCHEMA-LOOPS)
- Monitoring stack (Prometheus + Grafana)
- Vector search (Qdrant or Chroma)
- Custom integrations (graphify, postgres-mcp)

---

## LAYER 2: SERVICE (68 repos)

### Priority: OWNED > STARRED OFFICIAL (Wrap for Consistency)

**Use OWNED Service Wrappers:**
- iza-os-integrations (custom integration layer)
- shared-kernels (auth, Stripe, Supabase)
- iza-os-api-gateway-bot (API gateway + routing)
- iza-os-third-party-apis (third-party management)

**Wrap STARRED Official SDKs:**
- stripe-sdk → wrapped by shared-kernels
- twilio-sdk → wrap for hotline/SMS
- sendgrid → wrap for email
- google-maps → wrap for geolocation

**Venture-Specific Service Usage:**
```
marketplace-core
├─ shared-kernels (auth, Stripe, Supabase)
├─ iza-os-api-gateway-bot (API routing)
└─ Email wrapper (SendGrid)

CON-009 (Roofing)
├─ Via marketplace-core (all services)
└─ Maps wrapper (project location)

CON-010 (Plumbing 24/7)
├─ Via marketplace-core
├─ Twilio wrapper (hotline)
└─ Smart dispatch wrapper

CON-011 (Electrical)
├─ Via marketplace-core
└─ Compliance service wrapper

CON-012 (HVAC)
├─ Via marketplace-core
└─ Weather API wrapper (seasonal pricing)

LT-009 (Dispatch SaaS)
├─ iza-os-api-gateway-bot (core)
├─ Twilio wrapper (SMS/phone)
└─ Google Maps wrapper (routing)
```

---

## LAYER 3: PRODUCT (307 repos)

### Priority: OWNED ≥ STARRED (Leverage Existing)

**Use OWNED Venture Products:**
- marketplace-core (shared platform for all 6)
- con-009-roofing-company (roofing marketplace)
- con-010-plumbing-services (plumbing 24/7)
- con-011-electrical-services (electrical services)
- con-012-hvac-services (HVAC + maintenance)
- lt-009-hvac-technician-dispatch (dispatch platform)
- iza-os-platform-core (unified platform infrastructure)

**Reference STARRED Product Examples (Don't Copy):**
- Next.js templates (frontend patterns)
- Stripe billing examples (subscription logic)
- Twilio marketplace (communication patterns)
- Component libraries (UI patterns)

**Build Strategy:**
1. Use marketplace-core as foundation
2. Plug in venture-specific OWNED repos
3. Reference STARRED for missing features
4. Never rebuild what you own

---

## LAYER 4: ASSET (602 repos)

### Priority: OWNED + STARRED MERGED (Compose Best)

**Use OWNED Assets:**
- Operational playbooks (business processes)
- Prompt libraries (AI instructions)
- Dataset collections (venture data)
- Deployment templates (your patterns)
- SOP documentation (standard procedures)

**Leverage STARRED Assets:**
- Prompt engineering templates (OpenAI, Anthropic)
- Business process templates (HubSpot, Stripe)
- Dataset formats (Hugging Face, Kaggle)
- Infrastructure-as-Code templates (Terraform)
- Documentation templates (README generators)

**Composition Model:**
```
FINAL = OWNED + BEST PRACTICES FROM STARRED

For each asset type:
1. Start with OWNED (if exists)
2. Compare to STARRED best practice
3. Merge: Keep your customizations + adopt better patterns
4. Version control the merged result
5. Share across all ventures
```

---

## LAYER 5: UNCLASSIFIED (591 repos)

### Action: Classify & Route

**Classification Process:**
1. Determine category using 10-attribute model
2. Assess relevance to 6 ventures
3. Route to proper layer above
4. Or archive if not relevant

**Expected Breakdown:**
- ~100 repos → Infrastructure
- ~50 repos → Service
- ~100 repos → Product
- ~150 repos → Asset
- ~191 repos → Archive/Low-priority

---

## EXECUTION ROADMAP

### Week 1: Deploy Known Repos
```
✅ Deploy marketplace-core
   ├─ Uses: OWNED infrastructure (Supabase, graphify)
   ├─ Uses: OWNED services (auth, payments, integrations)
   └─ Uses: OWNED assets (deployment templates)

✅ Deploy 6 ventures on marketplace-core
   ├─ con-009, con-010, con-011, con-012, lt-009
   └─ Each uses: shared infrastructure + services + assets

✅ Apply operational playbooks
   ├─ Security checklists (OWNED)
   ├─ Deployment procedures (OWNED)
   └─ Onboarding templates (OWNED)
```

### Week 2: Classify & Fill Gaps
```
⏳ Classify 591 unclassified repos
├─ Identify repos that fill infrastructure gaps
├─ Identify repos that fill service gaps
├─ Identify repos that fill product gaps
└─ Identify repos that fill asset gaps

⏳ Integrate newly classified repos
├─ Add to appropriate layers
├─ Update venture-specific dependencies
└─ Test integration
```

### Week 3: Optimize & Merge
```
⏳ Review STARRED best practices
├─ Compare OWNED services to STARRED alternatives
├─ Merge improvements back to OWNED
├─ Update version control
└─ Share across ventures
```

---

## TARGET CODE REUSE

```
marketplace-core Composition:
├─ 10% New code (venture customization)
├─ 40% OWNED code (existing services + infrastructure)
└─ 50% STARRED code (battle-tested open source)

RESULT: 90% reuse rate
        Faster to market, higher quality, lower maintenance cost
```

---

## Decision Summary

✅ Infrastructure: Own your databases and integration points, use community tools for monitoring/visualization  
✅ Services: Own the wrappers (consistency), use official SDKs underneath  
✅ Products: Leverage your existing ventures, don't rebuild  
✅ Assets: Merge your playbooks with community best practices  

**Outcome:** 1,592 repos strategically allocated across 6 ventures for 90%+ code reuse.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
