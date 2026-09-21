# OPS-001 Staffing OS — Identity & Access Architecture Specification

> **Venture:** OPS-001 (Worldwidebro Staffing LLC / Labor Market OS)  
> **Authority:** Identity & Access Engineering Specialist (`agency-identity-access-engineer`)  
> **Security Baseline:** NIST SP 800-63B (AAL2/AAL3), OAuth 2.1 (draft), OpenID Connect Core 1.0, RFC 7636 (PKCE), RFC 7519 (JWT), SAML 2.0 Core, W3C WebAuthn Level 3  
> **Data Room Classification:** Institutional Technical Specification (Domain 22 — System Architecture)

---

## 1. Executive Summary & Threat Model

Staffing and labor logistics manage high-sensitivity personally identifiable information (PII), banking details, statutory tax filings (Form I-9, W-4, 1099, direct deposit ABA routing numbers), and enterprise commercial terms (client bill rates, markups, and escrow settlements).

The identity system secures five distinct user personas across eight application surfaces:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        OPS-001 FIVE-TIER IDENTITY UNIVERSE                      │
└─────────────────────────────────────────────────────────────────────────────────┘

 1. WORKER (Candidate / Field Laborer)
    ├── Authentication: WebAuthn Passkeys / SMS OTP / Passwordless Magic Link
    ├── Session TTL: 15-minute access token + rotating sliding refresh
    └── Isolation Scope: Strictly sub == worker_id. Zero access to billing spreads or other workers.

 2. EMPLOYER (Client Enterprise / Hiring Manager / AP Dept)
    ├── Authentication: Corporate Email OIDC / SAML 2.0 SP-Initiated SSO (Okta, Azure AD)
    ├── Session TTL: 15-minute access token + 8-hour tenant session
    └── Isolation Scope: tenant_id == req.user.tenant_id. Postgres RLS enforced at data layer.

 3. RECRUITER (Internal Agency Talent Acquisition)
    ├── Authentication: Agency IdP SSO + WebAuthn MFA required
    ├── Session TTL: 15-minute access token + strict IP/device binding
    └── Isolation Scope: System-wide candidate sourcing; read-only on executive margin underwriting.

 4. SUPERVISOR (Field Operations / Shift Check-In)
    ├── Authentication: Mobile Biometrics / PIN session with short 4-hour timeout
    ├── Session TTL: Fast-switch shift session bound to physical job site
    └── Isolation Scope: Scoped strictly to site_id and scheduled shift shift_id.

 5. EXECUTIVE ADMIN (Worldwidebro Operations / Compliance Officer)
    ├── Authentication: Hardware FIDO2/WebAuthn YubiKey + Break-Glass Dual-Control
    ├── Session TTL: 15-minute access token; re-auth required for bank detail changes
    └── Isolation Scope: Global platform governance with immutable append-only audit logging.
```

---

## 2. Threat Modeling Matrix

| Threat / Attack Vector | Target Surface | Impact | Mitigation Enforced |
|---|---|---|---|
| **Cross-Tenant Data Leakage (IDOR)** | Employer Portal / Requisitions | Critical (Exposure of competitors' rates & candidates) | **Tenant context derived exclusively from authenticated token** (`req.user.tenant_id`). Client parameters (`?tenant_id=...`) strictly ignored. Postgres RLS enforced. |
| **Algorithm Confusion (`alg: none` / RS256 vs HS256)** | API Endpoints | Critical (Forged tokens / Account takeover) | **Strict algorithm allowlist** (`['HS256', 'RS256']`). Explicit rejection of `none` and mismatched signature keys. |
| **Token Theft & Replay** | Browser / Mobile Client | High (Impersonation) | **Refresh token rotation (RTR) with reuse detection**. If a spent refresh token is replayed, the entire token family is immediately revoked and a security alert is triggered. |
| **Open Redirect / Auth Code Interception** | OAuth / SAML Callbacks | High (Code interception / CSRF) | **Exact-match redirect URI allowlists**, SHA-256 PKCE (`code_challenge_method: S256`), cryptographically random single-use `state` and `nonce` bound to server-side session. |
| **Worker PII & Banking Exfiltration** | Worker Portal / Payroll API | Critical (Identity theft, bank redirection) | **Direct Deposit ABA routing and SSN masked at the API serialization layer**. Step-up authentication required to alter payout accounts. |
| **Credential Stuffing & Brute Force** | Public Front Door / Login | Medium | **Progressive IP/Account rate limiting** (exponential backoff after 3 failed attempts) and passkey-first passwordless UX. |

---

## 3. Protocol Depth & Architecture Standards

### A. OIDC Authorization Code Flow with PKCE
Every browser and mobile authentication flow follows OAuth 2.1 / RFC 7636:
1. **Client requests auth**: Generates cryptographically secure 32-byte `verifier`, computes SHA-256 `challenge = base64url(sha256(verifier))`, generates random `state` and `nonce`.
2. **IdP Authorization**: User completes authentication at identity provider; redirected back to exact-matched redirect URI with `code` and `state`.
3. **Token Exchange**: Server exchanges `code` and `verifier` for tokens over TLS. Validates `state`, verifies signature, validates `issuer`, `audience`, and unspent `nonce`.

### B. Enterprise SSO (SAML 2.0 & OIDC Federation)
Enterprise clients require federated SSO:
- **SP-Initiated Flow**: Client enters `@enterprisecorp.com`. System detects enterprise domain, routes to configured IdP metadata endpoint.
- **Assertion Validation**: Enforces XML signature verification, checks `AudienceRestriction` matches SP Entity ID, validates `InResponseTo` against active session, and enforces a strict $\pm 180$-second clock skew tolerance.
- **SCIM 2.0 Provisioning**: JIT (Just-In-Time) provisioning on login, and sub-60-second automated deprovisioning when an employee is terminated in Okta or Azure AD.

### C. WebAuthn / FIDO2 Passkeys (Phishing-Resistant Authentication)
Workers and supervisors authenticate via biometric passkeys:
- **Registration**: Server generates random 32-byte challenge, binds to Relying Party ID (`rpID = "staffing.worldwidebro.com"`).
- **Verification**: Browser executes WebAuthn API; server validates signature against stored public key and verifies monotonic `signCount` to detect cloned authenticators.

### D. Data-Layer Tenant Isolation (Postgres RLS)
Tenant isolation is not an application-layer afterthought. It is enforced in SQL:

```sql
-- Enable Row Level Security
ALTER TABLE requisitions ENABLE ROW LEVEL SECURITY;
ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;
ALTER TABLE time_entries ENABLE ROW LEVEL SECURITY;

-- Tenant Isolation Policy
CREATE POLICY tenant_isolation_policy ON requisitions
  USING (tenant_id = NULLIF(current_setting('app.tenant_id', true), '')::uuid);
```

---

## 4. Audit Trail & Compliance (SOC 2 Type II / ISO 27001)

Every authentication and authorization event produces an immutable structured JSON log:

```json
{
  "event_id": "evt_01J8G5Q...",
  "timestamp": "2026-09-21T09:25:00.000Z",
  "event_type": "AUTH_LOGIN_SUCCESS",
  "actor_id": "usr_emp_49201",
  "actor_role": "employer_admin",
  "tenant_id": "tnt_abc_logistics_nc",
  "auth_method": "SAML_SSO",
  "idp_entity_id": "http://www.okta.com/exk92...",
  "client_ip": "198.51.100.42",
  "user_agent": "Mozilla/5.0 ...",
  "resource": "/api/requisitions",
  "status": "SUCCESS"
}
```

Any unauthorized cross-tenant attempt or signature verification failure immediately logs `AUTH_CROSS_TENANT_ATTEMPT` or `AUTH_TOKEN_INVALID` with zero sensitive token material leaked.
