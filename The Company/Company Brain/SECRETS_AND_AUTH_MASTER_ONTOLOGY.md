---
type: infrastructure-control-ontology
canonical: true
authority: security-and-identity-plane
version: 1.0
updated_at: 2026-10-02T00:00:00Z
source_of_truth: true
---

# SECRETS_AND_AUTH_MASTER_ONTOLOGY v1.0 — Security & Identity Control Plane

**The Company Brain must understand credentials without possessing them.**

This ontology models **[SECRETS_AND_AUTH]** as a first-class control plane, separate from but fully integrated with the Company Brain's knowledge graph.

---

## Core Principle: Metadata ≠ Value

```
[SECRET_METADATA]
        ≠
[SECRET_VALUE]
```

**The Company Brain knows:**
- WHAT credential exists (SEC-OMNIROUTE-001)
- WHERE it is stored (macOS Keychain)
- WHO owns it (Infrastructure team)
- WHAT it authorizes (model-routing)
- WHO uses it (Claude Code, OmniRoute, OpenClaw)
- WHEN it expires (90 days)
- STATUS (ACTIVE, ROTATED, EXPIRED, COMPROMISED)

**The Secret Manager possesses:**
- THE ACTUAL SECRET VALUE (never in markdown, graphs, or logs)

---

## [SECRETS_AND_AUTH_COMPLETE_ARCHITECTURE] — 9 Domains

```
[SECRETS_AND_AUTH]

├─ [IDENTITY]
│  ├── [HUMAN_IDENTITY]
│  ├── [SERVICE_IDENTITY]
│  ├── [AGENT_IDENTITY]
│  ├── [APPLICATION_IDENTITY]
│  ├── [MACHINE_IDENTITY]
│  ├── [ORGANIZATION_IDENTITY]
│  └── [WORKLOAD_IDENTITY]
│
├─ [SECRETS]
│  ├── [PASSWORDS]
│  ├── [API_KEYS]
│  ├── [ACCESS_TOKENS]
│  ├── [REFRESH_TOKENS]
│  ├── [SESSION_TOKENS]
│  ├── [OAUTH_CREDENTIALS]
│  ├── [CLIENT_SECRETS]
│  ├── [PRIVATE_KEYS]
│  ├── [SSH_KEYS]
│  ├── [CERTIFICATES]
│  ├── [SIGNING_KEYS]
│  ├── [ENCRYPTION_KEYS]
│  ├── [WEBHOOK_SECRETS]
│  ├── [DATABASE_CREDENTIALS]
│  ├── [SERVICE_CREDENTIALS]
│  └── [RECOVERY_CODES]
│
├─ [AUTHENTICATION]
│  ├── [AUTHENTICATION_METHOD]
│  ├── [PASSWORD_AUTH]
│  ├── [PASSKEY]
│  ├── [MFA]
│  ├── [TOTP]
│  ├── [HARDWARE_KEY]
│  ├── [BIOMETRIC]
│  ├── [OAUTH]
│  ├── [OIDC]
│  ├── [SAML]
│  ├── [SSH_AUTH]
│  ├── [CERTIFICATE_AUTH]
│  └── [WORKLOAD_AUTH]
│
├─ [AUTHORIZATION]
│  ├── [ROLE]
│  ├── [PERMISSION]
│  ├── [SCOPE]
│  ├── [POLICY]
│  ├── [ACCESS_LEVEL]
│  ├── [RESOURCE_ACCESS]
│  ├── [ADMIN_ACCESS]
│  └── [LEAST_PRIVILEGE]
│
├─ [SECRET_STORAGE]
│  ├── [PASSWORD_MANAGER]
│  ├── [SECRET_MANAGER]
│  ├── [KEYCHAIN]
│  ├── [ENVIRONMENT_VARIABLE]
│  ├── [DOCKER_SECRET]
│  ├── [KUBERNETES_SECRET]
│  ├── [CLOUD_SECRET_STORE]
│  ├── [ENCRYPTED_FILE]
│  └── [HARDWARE_SECURITY_MODULE]
│
├─ [SECRET_LIFECYCLE]
│  ├── [GENERATE]
│  ├── [PROVISION]
│  ├── [STORE]
│  ├── [DISTRIBUTE]
│  ├── [USE]
│  ├── [ROTATE]
│  ├── [REVOKE]
│  ├── [EXPIRE]
│  ├── [REPLACE]
│  ├── [ARCHIVE]
│  └── [DESTROY]
│
├─ [SECRET_DISCOVERY]
│  ├── [SECRET_SCAN]
│  ├── [LEAK_DETECTION]
│  ├── [GIT_HISTORY_SCAN]
│  ├── [ENVIRONMENT_SCAN]
│  ├── [CONFIG_SCAN]
│  ├── [LOG_SCAN]
│  ├── [DOCUMENT_SCAN]
│  └── [CODE_SCAN]
│
├─ [AUDIT]
│  ├── [ACCESS_LOG]
│  ├── [AUTH_LOG]
│  ├── [TOKEN_USAGE]
│  ├── [SECRET_ROTATION_LOG]
│  ├── [REVOCATION_LOG]
│  ├── [SECURITY_EVENT]
│  └── [INCIDENT]
│
└─ [REALITY]
   ├── [SECRET_EXISTS]
   ├── [SECRET_LOCATION]
   ├── [SECRET_OWNER]
   ├── [SECRET_STATUS]
   ├── [SECRET_EXPIRATION]
   ├── [ACCESS_VERIFIED]
   ├── [ROTATION_VERIFIED]
   └── [REVOCATION_VERIFIED]
```

---

## [IDENTITY_AUTHENTICATION_FLOW] — The Core Loop

```
[IDENTITY]
    ↓ (Who are you?)
[AUTHENTICATION]
    ↓ (Prove it)
[SESSION]
    ↓ (Logged in)
[AUTHORIZATION]
    ↓ (What are you allowed to do?)
[PERMISSION]
    ↓ (Grant access)
[RESOURCE]
    ↓ (Use the resource)
[AUDIT]
    ↓ (Log the action)
[REALITY]
    ↓ (Record what happened)
[[NEXT_ACTION]] ↺
```

---

## [SECRET_LIFECYCLE_FLOW] — Birth to Death

```
[GENERATE]
    ↓ (Create credential)
[STORE]
    ↓ (Place in secret manager)
[PROVISION]
    ↓ (Distribute to consumers)
[USE]
    ↓ (Authenticate/authorize with it)
[MONITOR]
    ↓ (Watch for expiration/compromise)
[ROTATE]
    ↓ (Replace with new credential)
[REVOKE]
    ↓ (Disable old credential)
[DESTROY]
    ↓ (Securely erase)
[AUDIT]
    ↓ (Log lifecycle)
[[NEXT_CREDENTIAL]] ↺
```

---

## [SECRET_TYPES] — Credential Taxonomy

### [PASSWORDS]
```
├── [HUMAN_PASSWORD]
├── [SERVICE_PASSWORD]
├── [DATABASE_PASSWORD]
├── [ADMIN_PASSWORD]
├── [APPLICATION_PASSWORD]
├── [ROOT_PASSWORD]
└── [RECOVERY_PASSWORD]
```

### [API_KEYS]
```
├── [PROVIDER_API_KEY]
├── [SERVICE_API_KEY]
├── [APPLICATION_API_KEY]
├── [PUBLIC_API_KEY]
├── [PRIVATE_API_KEY]
├── [READ_ONLY_KEY]
└── [ADMIN_KEY]
```

### [TOKENS]
```
├── [ACCESS_TOKEN]
├── [REFRESH_TOKEN]
├── [SESSION_TOKEN]
├── [BEARER_TOKEN]
├── [OAUTH_TOKEN]
├── [JWT]
├── [WEBHOOK_TOKEN]
├── [PERSONAL_ACCESS_TOKEN]
└── [SERVICE_TOKEN]
```

### [KEYS]
```
├── [SSH_PRIVATE_KEY]
├── [SSH_PUBLIC_KEY]
├── [TLS_PRIVATE_KEY]
├── [TLS_CERTIFICATE]
├── [SIGNING_KEY]
├── [ENCRYPTION_KEY]
├── [KMS_KEY]
├── [GPG_KEY]
└── [HARDWARE_KEY]
```

---

## [AUTHENTICATION_METHODS] — How Identity is Proven

```
[AUTHENTICATION_METHOD]

├── [PASSWORD_AUTH]          ← Username + password
├── [PASSKEY]                ← WebAuthn/FIDO2
├── [MFA]                    ← Multi-factor (password + TOTP/hardware)
├── [TOTP]                   ← Time-based one-time password
├── [HARDWARE_KEY]           ← Physical security key
├── [BIOMETRIC]              ← Fingerprint/Face/Iris
├── [OAUTH]                  ← Delegated authorization
├── [OIDC]                   ← Identity delegation
├── [SAML]                   ← Enterprise SSO
├── [SSH_AUTH]               ← SSH key-based auth
├── [CERTIFICATE_AUTH]       ← TLS certificate
└── [WORKLOAD_AUTH]          ← Service-to-service authentication
```

---

## [AUTHENTICATION_VS_AUTHORIZATION] — Critical Distinction

```
AUTHENTICATION (AuthN)
=
"Who are you?"

Response: IDENTITY VERIFIED

Example:
    User provides password
    System checks password matches stored hash
    System creates session token
```

```
AUTHORIZATION (AuthZ)
=
"What are you allowed to do?"

Response: PERMISSION GRANTED or DENIED

Example:
    User (authenticated) requests read access to resource
    System checks if user's role has read permission
    System grants or denies access
```

```
Therefore:

IDENTITY
   ↓
AUTHENTICATION
   ↓
AUTHENTICATED_SESSION
   ↓
AUTHORIZATION
   ↓
PERMISSION
   ↓
ACTION
```

---

## [SECRET_STORAGE_SYSTEMS] — Where Secrets Live

```
[SECRET_STORAGE]

├── [PASSWORD_MANAGER]
│   ├── 1Password
│   ├── Bitwarden
│   ├── LastPass
│   └── KeePass
│
├── [SECRET_MANAGER]
│   ├── AWS Secrets Manager
│   ├── Azure Key Vault
│   ├── Google Secret Manager
│   └── HashiCorp Vault
│
├── [KEYCHAIN]
│   ├── macOS Keychain
│   ├── Windows Credential Manager
│   └── GNOME Keyring
│
├── [ENVIRONMENT_VARIABLE]
│   ├── .env files (NEVER in Git)
│   ├── ~/.bashrc / ~/.zshrc
│   └── Shell environment
│
├── [DOCKER_SECRET]
│   ├── Docker Swarm secrets
│   ├── Docker Compose secrets
│   └── Docker volume mounts
│
├── [KUBERNETES_SECRET]
│   ├── etcd (encrypted)
│   ├── Sealed Secrets
│   └── External Secrets Operator
│
├── [CLOUD_SECRET_STORE]
│   ├── AWS Systems Manager Parameter Store
│   ├── Google Cloud Secret Manager
│   └── Azure Key Vault
│
├── [ENCRYPTED_FILE]
│   ├── Encrypted with age/gpg
│   └── Stored in secure location
│
└── [HARDWARE_SECURITY_MODULE]
    ├── YubiKey
    ├── Nitrokey
    └── Hardware tokens
```

---

## [SECRET_DISCOVERY_FLOW] — Detection & Response

```
[SECRET_DETECTED]
      ↓
[CLASSIFY]
      ├── [FALSE_POSITIVE]
      ├── [PUBLIC_NON_SECRET]
      ├── [TEST_CREDENTIAL]
      ├── [REAL_CREDENTIAL]
      └── [COMPROMISED_CREDENTIAL]
      ↓
[IDENTIFY_PROVIDER]
      ↓
[IDENTIFY_OWNER]
      ↓
[IDENTIFY_CONSUMER]
      ↓
[CHECK_EXPOSURE]
      ↓
[ASSESS_RISK]
      ↓
[REVOKE_IF_NECESSARY]
      ↓
[ROTATE]
      ↓
[REMOVE_FROM_SOURCE]
      ↓
[VERIFY_REMOVAL]
      ↓
[AUDIT]
      ↓
[MONITORING]
```

---

## [CREDENTIAL_REGISTRY_FORMAT] — Metadata Structure

Every credential has metadata (in Company Brain) separate from the value (in Secret Manager):

```yaml
# SECRET_REGISTRY.md entry

secret_id: SEC-OMNIROUTE-001

name: OmniRoute Production API Key

type: API_KEY

provider: OmniRoute

environment: PRODUCTION

owner:
  entity: Infrastructure Team
  role: Infrastructure Owner
  contact: [[INFRASTRUCTURE_OWNER]]

storage:
  system: macOS Keychain
  location: production/omniroute
  encrypted: true

consumers:
  - [[OMNIROUTE]]
  - [[CLAUDE_CODE]]
  - [[OPENCLAW]]
  - [[ANTIGRAVITY]]

permissions:
  - model-routing
  - provider-switching
  - fallback-logic

created_at: UNKNOWN
last_rotated: UNKNOWN
expires_at: UNKNOWN

rotation:
  required: true
  interval: 90_days
  last_scheduled: UNKNOWN

status: ACTIVE

verification:
  exists: VERIFIED
  accessible: VERIFIED
  scope: VERIFIED
  expiration: NOT_TESTED

secret_value:
  stored_elsewhere: true
  exposed_in_company_brain: false

related:
  - [[OMNIROUTE]]
  - [[PROVIDER_AUTH]]
  - [[AUTH_CONNECTIVITY]]
```

**Key rule:** The registry never contains the actual secret value.

---

## [ENVIRONMENT_SEPARATION] — Isolation by Tier

```
[ENVIRONMENT]

├── [LOCAL]
│   └── Dev machine credentials
├── [DEV]
│   └── Development server credentials
├── [TEST]
│   └── Test environment credentials
├── [STAGING]
│   └── Staging environment credentials
├── [PRODUCTION]
│   └── Production credentials (highest security)
└── [DISASTER_RECOVERY]
    └── DR site credentials
```

**Rule:** Never confuse environments.

```
DEV_API_KEY
≠
STAGING_API_KEY
≠
PRODUCTION_API_KEY
```

---

## [DOCKER_SECRET_ONTOLOGY] — Container Credentials

```
[DOCKER]
   ↓
[CONTAINER]
   ↓
[SECRET_INJECTION]
   ├── [ENVIRONMENT_VARIABLE]
   ├── [SECRET_FILE]
   ├── [DOCKER_SECRET]
   └── [EXTERNAL_SECRET_MANAGER]

CORRECT:
    [SECRET_MANAGER]
        ↓
    [SECRET_INJECTION]
        ↓
    [CONTAINER]

WRONG:
    [SECRET]
        ↓
    [docker-compose.yml]
        ↓
    [GIT]
```

---

## [CREDENTIAL_DEPENDENCY_GRAPH] — Impact Analysis

Allows the Company Brain to answer: **"What breaks if this credential expires?"**

```
[SECRET: SEC-OMNIROUTE-001]
   ├── [AUTHENTICATES] → [[OMNIROUTE]]
   ├── [AUTHORIZES] → [MODEL_ROUTING]
   ├── [USED_BY] → [[CLAUDE_CODE]]
   ├── [USED_BY] → [[OPENCLAW]]
   └── [USED_BY] → [[ANTIGRAVITY]]
        ↓
   [[OMNIROUTE]]
        ↓
   [[PROVIDER_ROUTING]]
        ↓
   [[AGENT_SYSTEM]]
        ↓
   [[TASK_EXECUTION]]
        ↓
   [DEPENDENCY_IMPACT]

Result:
    SECRET EXPIRATION
        ↓
    OMNIROUTE FAILS
        ↓
    AGENTS CANNOT ROUTE
        ↓
    TASKS BLOCKED
        ↓
    REVENUE IMPACT
```

---

## [AUTH_CONNECTIVITY_TESTING] — Verification

Every credential should have associated connectivity tests:

```yaml
test_id: AUTH-CONNECTIVITY-001

source: [[CLAUDE_CODE]]
destination: [[OMNIROUTE]]

identity: claude-code-production

auth_method: API_KEY

credential_id: SEC-OMNIROUTE-001

environment: production

expected:
  authentication: PASS
  authorization: PASS
  scope: model-routing
  latency: < 100ms

actual:
  authentication: PASS
  authorization: PASS
  scope: VERIFIED
  latency: 45ms

status: VERIFIED

timestamp: 2026-10-02T12:00:00Z

secret_exposed: false
```

---

## [SECURITY_REALITY] — The Source of Truth

```
[SECURITY_REALITY]

├── [SECRET_METADATA]
│   ├── ID
│   ├── TYPE
│   ├── PROVIDER
│   ├── OWNER
│   ├── CONSUMERS
│   ├── SCOPE
│   ├── STATUS
│   └── EXPIRATION
│
├── [SECRET_VERIFICATION]
│   ├── EXISTS: [VERIFIED | NOT_VERIFIED]
│   ├── ACCESSIBLE: [VERIFIED | NOT_VERIFIED]
│   ├── SCOPE: [VERIFIED | NOT_VERIFIED]
│   ├── EXPIRATION: [NOT_VERIFIED | EXPIRING | EXPIRED]
│   └── ROTATION: [VERIFIED | OVERDUE]
│
├── [SECURITY_EVENTS]
│   ├── CREATED
│   ├── ROTATED
│   ├── REVOKED
│   ├── EXPOSED
│   ├── COMPROMISED
│   └── DESTROYED
│
└── [AUDIT_TRAIL]
    ├── WHO ACCESSED
    ├── WHEN
    ├── WHAT_THEY_DID
    ├── SUCCESS_OR_FAILURE
    └── EVIDENCE
```

---

## [COMPANY_BRAIN_SECURITY_INTEGRATION] — Full Wiring

```
[[WHOAMI]]
    │ (Identity)
    ↓
[[IDENTITY]]
    │ (Who are we?)
    ├── [HUMAN_IDENTITY]
    ├── [SERVICE_IDENTITY]
    ├── [AGENT_IDENTITY]
    └── [WORKLOAD_IDENTITY]
    ↓
[[AUTHENTICATION]]
    │ (How do we prove it?)
    ├── [PASSWORD_AUTH]
    ├── [OAUTH]
    ├── [SAML]
    └── [CERTIFICATE_AUTH]
    ↓
[[SESSION]]
    │ (Am I still logged in?)
    ├── [SESSION_TOKEN]
    ├── [EXPIRATION]
    └── [REVOCATION]
    ↓
[[AUTHORIZATION]]
    │ (What are we allowed to do?)
    ├── [ROLE]
    ├── [PERMISSION]
    └── [SCOPE]
    ↓
[[SECRETS]]
    │ (What credentials exist?)
    ├── [API_KEYS]
    ├── [TOKENS]
    ├── [PASSWORDS]
    └── [CERTIFICATES]
    ↓
[[SECRET_STORAGE]]
    │ (Where are they kept?)
    ├── [KEYCHAIN]
    ├── [SECRET_MANAGER]
    └── [CLOUD_VAULT]
    ↓
[[INFRASTRUCTURE]]
    │ (What systems use them?)
    ├── [[OMNIROUTE]]
    ├── [[NEO4J]]
    ├── [[QDRANT]]
    └── [[DOCKER]]
    ↓
[[APPLICATIONS]]
    │ (What runs on infrastructure?)
    ├── [[CLAUDE_CODE]]
    ├── [[AGENTS]]
    └── [[WORKFLOWS]]
    ↓
[[AUDIT]]
    │ (What happened?)
    ├── [ACCESS_LOG]
    ├── [AUTH_LOG]
    └── [SECURITY_EVENT]
    ↓
[[REALITY]]
    │ (Current verified state)
    ├── [SECRETS_VERIFIED]
    ├── [CREDENTIALS_ACTIVE]
    ├── [ACCESS_CURRENT]
    └── [EXPIRATION_CHECKED]
    ↓
[[NEXT_ACTION]] ↺
```

---

## [GOLDEN_RULE] — Never Do This

**NEVER place these in Company Brain:**

- ❌ Actual API keys
- ❌ Actual passwords
- ❌ Actual tokens
- ❌ Private key material
- ❌ OAuth secrets
- ❌ Database credentials
- ❌ Encryption keys
- ❌ SSH private keys
- ❌ Certificate private keys

**ALWAYS place only metadata:**

- ✅ Credential ID (SEC-001)
- ✅ Credential type (API_KEY)
- ✅ Provider (OmniRoute)
- ✅ Owner (Infrastructure)
- ✅ Consumers (Claude Code, OmniRoute)
- ✅ Scope (model-routing)
- ✅ Status (ACTIVE)
- ✅ Expiration date (or "UNKNOWN")
- ✅ Storage location (macOS Keychain)
- ✅ Verification status (VERIFIED)

---

## [IMPLEMENTATION_ARCHITECTURE]

```
┌─────────────────────────────────────┐
│  [[COMPANY_BRAIN]]                  │
│                                     │
│  ├── [[SECRETS_AND_AUTH]]           │
│  │   ├── [SECRET_REGISTRY]          │
│  │   ├── [CREDENTIAL_REGISTRY]      │
│  │   ├── [IDENTITY_REGISTRY]        │
│  │   ├── [ACCESS_REGISTRY]          │
│  │   ├── [AUTH_CONNECTIVITY_TESTS]  │
│  │   └── [SECURITY_REALITY]         │
│  │                                   │
│  └── [[KNOWLEDGE_GRAPH]]            │
│      (Neo4j relationships)           │
└─────────────────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  [[SECRET_MANAGER]]                 │
│                                     │
│  macOS Keychain                    │
│  (stores actual secret values)      │
│                                     │
│  NEVER exposed to Company Brain     │
└─────────────────────────────────────┘
```

---

**Related:** [[WHOAMI.md]] · [[WHERE_WE_ARE.md]] · [[DATA_FLOW.md]] · [[INFRASTRUCTURE.md]] · [[CROSS_LINK_MASTER_ONTOLOGY.md]] · [[OMNIROUTE_MASTER_ONTOLOGY.md]]

**Security foundation v1.0: Identity, authentication, authorization, and credential management without exposing secrets to the knowledge graph.**

