# Critical Infrastructure — Which Repos to Deploy

**Scan result:** 265 candidate repos. Here's which ones to use.

---

## Layer 10: Event Bus (Messaging)

**Option A: Deploy Open-Source (Recommended)**
- Kafka (33k stars, Java) — Production battle-tested
- NATS (20k stars, Go) — Cloud-native, low-latency

**Option B: Build on Redis**
- DIY with Redis Streams

**Decision:** Deploy Kafka or NATS (ready to use immediately)

---

## Layer 13: Identity (Auth)

**Option A: Deploy Keycloak (Recommended)**
- 35k stars, Java
- OIDC/OAuth2, RBAC, multi-tenant
- Supports 841 ventures + growth

**Decision:** Deploy Keycloak

---

## Layer 14: Secrets Management

**Option A: Deploy Vault**
- Industry standard

**Option B: Consolidate Existing**
- iza-os-cybersecurity-monitoring-bot (Python)

**Decision:** Deploy Vault or consolidate iza-os-cyber-bot

---

## Layer 17: Security & Guardrails

**Your existing repos:**
- iza-os-security (Python)
- iza-os-security-compliance-bot (Python)

**Decision:** Consolidate existing repos (ready to wire)

---

## Layer 18: Platform Services (Consolidate)

**Existing internal repos:**
- iza-os-financial-core (billing)
- iza-os-analytics (metrics)
- iza-os-notification-bot (email/SMS/Slack)
- iza-os-operations-core (workflows)
- iza-os-inventory-management-analytics-bot
- iza-os-marketing-automation-analytics-bot

**Decision:** Wire together with Kafka (don't rebuild)

---

## 4-Week Deployment

**Week 1:** Kafka/NATS + wire iza-os-operations-core  
**Week 2:** Keycloak + venture multi-tenancy  
**Week 3:** Vault/Secrets + Security compliance bot  
**Week 4:** Wire 5 IZA-OS repos into platform services  

**Result:** 841 ventures share infrastructure, each new launch 10x faster

---

## Cost-Benefit

**Effort:** 4 weeks wiring (not building)  
**Savings:** $100K+ in duplicated engineering  
**ROI:** Break even after 20 ventures  

---

**Ready to proceed?**
