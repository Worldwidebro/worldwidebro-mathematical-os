---
id: ENG-AUTH-001
title: Unified Zero-Trust Authentication Gateway
aliases: ["UNIFIED_AUTH_GATEWAY", "Auth Gateway", "CRIT-GAP-AUTH", "NetBird WireGuard"]
tags: [auth, security, zero-trust, netbird, infisical, sso]
status: ACTIVE
updated: 2026-09-12
---

[[STARTHERE]] | [[REALITY]] | [[13_ENGINEERING/INFRASTRUCTURE/09_SECURITY/SECURITY|SECURITY]] | [[LOCAL_MODEL_AGENT_STACK_REGISTRY]] | [[INDEX]]

# 🛡️ Unified Zero-Trust Authentication Gateway

**Authority:** CP-027 (System Architecture & Infrastructure)  
**Status:** ✅ `IMPLEMENTED & STANDARDIZED`  
**Gap Resolution:** Resolves Critical Gap 2 (`CRIT-GAP-AUTH`) utilizing starred repository [`netbirdio/netbird`](https://github.com/netbirdio/netbird) (28,809 ★) and `civos_infisical` (:8091).

---

## 1. Zero-Trust Architecture
Rather than isolated `passlib` or `python-jose` instances, all portfolio applications authenticate through an encrypted overlay mesh with Just-In-Time (JIT) credential injection:

```text
               User / Agent Ingress
                        │
                        ▼
       ┌─────────────────────────────────┐
       │   Zero-Trust Overlay Network    │
       │   (Tailscale / NetBird Mesh)    │
       └────────────────┬────────────────┘
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
  ┌──────────────┐              ┌──────────────┐
  │ Supabase OIDC│              │  Infisical   │
  │ (User SSO /  │              │ (JIT Secret  │
  │  JWT Tokens) │              │  Injection)  │
  └──────────────┘              └──────────────┘
```

---

## 2. Standardized Agent & API Auth Contract
All internal services and venture API routes validate Bearer tokens against the centralized Supabase JWT secret or use Infisical ephemeral tokens:

```typescript
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!
);

export async function verifyEnterpriseToken(req: Request) {
  const authHeader = req.headers.get('authorization');
  if (!authHeader?.startsWith('Bearer ')) {
    throw new Error('Missing bearer authentication');
  }

  const token = authHeader.split(' ')[1];
  const { data: { user }, error } = await supabase.auth.getUser(token);
  if (error || !user) {
    throw new Error('Unauthorized zero-trust token');
  }

  return user;
}
```

---

## 3. Deployment Points
- **Secret Manager:** `civos_infisical` running in Docker on Mac Studio (`http://100.87.214.70:8091`).
- **Identity Mesh:** Tailscale encrypted interconnect connecting Mac Studio, MacBook Air, and venture production domains.
