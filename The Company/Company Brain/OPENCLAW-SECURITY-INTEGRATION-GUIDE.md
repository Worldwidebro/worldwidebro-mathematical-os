[[STARTHERE]] | [[REALITY]] | [[16-AGENTS|OpenClaw Security]] | [[INDEX]]

# OpenClaw Security & Integration Guide

**Created:** 2026-09-09  
**Status:** Ready to implement  
**Scope:** Worldwidebro Holdings + 5-venture pilot  

---

## SECURITY ARCHITECTURE (5 Layers)

### Layer 1: Authentication & Identity

**OpenClaw OAuth Flow:**
```
User logs into Venture Portal (CP-011 ClickUp)
    ↓
Redirect to OpenClaw OAuth provider
    ↓
User grants consent for contract generation
    ↓
OpenClaw returns OAuth token + refresh token
    ↓
Your system stores encrypted token in PostgreSQL
    ↓
Token used for: Contract generation, signing, verification
```

**API Key Management (Service Account):**
- Create OpenClaw service account: "worldwidebro-ventures"
- Generate API key (never commit to GitHub)
- Store in: `GitHub Secrets > OPENCLAW_API_KEY`
- Rotate quarterly

**Implementation:**
```yaml
# .github/workflows/openclaw-integration.yml
env:
  OPENCLAW_API_KEY: ${{ secrets.OPENCLAW_API_KEY }}
  OPENCLAW_API_URL: https://openclaw.company-brain.internal/api/v1
  OPENCLAW_CLIENT_ID: ${{ secrets.OPENCLAW_CLIENT_ID }}
  OPENCLAW_CLIENT_SECRET: ${{ secrets.OPENCLAW_CLIENT_SECRET }}
```

---

### Layer 2: Data Transit (TLS 1.3 + HMAC)

**Request Signing:**
```python
import hmac
import hashlib
import json
from datetime import datetime

class OpenClawClient:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
    
    def sign_request(self, method, path, body=None):
        """Generate HMAC-SHA256 signature for OpenClaw API calls"""
        timestamp = datetime.utcnow().isoformat() + "Z"
        
        if body:
            body_str = json.dumps(body, sort_keys=True)
        else:
            body_str = ""
        
        message = f"{method}\n{path}\n{timestamp}\n{body_str}"
        signature = hmac.new(
            self.api_key.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()
        
        return {
            "Authorization": f"Bearer {self.api_key}",
            "X-OpenClaw-Signature": signature,
            "X-OpenClaw-Timestamp": timestamp,
            "Content-Type": "application/json"
        }
    
    def create_contract(self, venture_id, customer_email, template_id):
        """Generate contract from template"""
        path = "/contracts"
        body = {
            "template_id": template_id,
            "parties": [
                {"name": "Worldwidebro Holdings", "email": "legal@worldwidebro.co"},
                {"name": "Customer", "email": customer_email}
            ],
            "metadata": {
                "venture_id": venture_id,
                "created_by": "CP-004",
                "expires_at": (datetime.utcnow() + timedelta(days=30)).isoformat()
            }
        }
        
        headers = self.sign_request("POST", path, body)
        response = requests.post(
            f"{self.api_url}{path}",
            json=body,
            headers=headers,
            verify=True,  # TLS verification
            timeout=30
        )
        
        return response.json()
```

**Webhook Signature Verification:**
```python
def verify_webhook_signature(request, openclaw_secret):
    """Verify webhook from OpenClaw is authentic"""
    signature = request.headers.get("X-OpenClaw-Webhook-Signature")
    timestamp = request.headers.get("X-OpenClaw-Timestamp")
    
    if not signature or not timestamp:
        return False
    
    # Check timestamp is within 5 minutes (prevent replay attacks)
    request_time = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    if abs((datetime.now(timezone.utc) - request_time).total_seconds()) > 300:
        return False
    
    # Verify HMAC signature
    body = request.get_data()
    expected_signature = hmac.new(
        openclaw_secret.encode(),
        f"{timestamp}{body.decode()}".encode(),
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(signature, expected_signature)
```

---

### Layer 3: Data Storage & Encryption

**PostgreSQL Schema (Encrypted Fields):**
```sql
-- contracts table with encrypted sensitive fields
CREATE TABLE contracts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id VARCHAR(20) NOT NULL,  -- CON-001, OPS-001, etc.
  openclaw_contract_id VARCHAR(255) NOT NULL,  -- OpenClaw ID
  customer_email VARCHAR(255) NOT NULL,
  contract_type VARCHAR(100),  -- Customer Agreement, NDA, Conversion Note
  status VARCHAR(50),  -- draft, pending_signature, signed, executed
  
  -- Encrypted fields (pgcrypto)
  customer_name TEXT NOT NULL ENCRYPTED WITH (algorithm = 'aes-256-cbc'),
  document_hash VARCHAR(64) NOT NULL,  -- SHA-256 checksum
  signature_data JSONB ENCRYPTED WITH (algorithm = 'aes-256-cbc'),
  
  created_at TIMESTAMP DEFAULT NOW(),
  signed_at TIMESTAMP,
  expires_at TIMESTAMP,
  
  -- Audit trail
  created_by VARCHAR(50),  -- CP-004, CP-011, Agent ID
  approved_by VARCHAR(50),  -- CP-005 approval gate
  
  -- Neo4j link
  neo4j_id VARCHAR(100),
  
  CONSTRAINT valid_venture CHECK (venture_id ~ '^[A-Z]+-[0-9]{3}$'),
  CONSTRAINT valid_status CHECK (status IN ('draft', 'pending_signature', 'signed', 'executed')),
  INDEX idx_venture_status (venture_id, status),
  INDEX idx_customer_email (customer_email),
  INDEX idx_openclaw_id (openclaw_contract_id)
);

-- Add pgcrypto extension
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

**GitHub Secrets (Encrypted at Rest):**
```bash
# Store these in GitHub Secrets (Settings > Secrets and Variables > Actions)
OPENCLAW_API_KEY=sk_live_xxxxxxxxxxxx
OPENCLAW_CLIENT_ID=oc_client_xxxxxxx
OPENCLAW_CLIENT_SECRET=oc_secret_xxxxxxx
OPENCLAW_WEBHOOK_SECRET=whsec_xxxxxxx
POSTGRES_ENCRYPTION_KEY=<master-key-from-vault>
NEO4J_BOLT_URL=bolt://100.87.214.70:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=<from-vault>
```

**Vault Integration (Air-Gapped Master Key):**
```bash
# Store master encryption key in local Bitwarden vault (never in cloud)
# Access pattern:
# 1. Bitwarden CLI: bw get password "OpenClaw Master Key"
# 2. Export to environment: POSTGRES_ENCRYPTION_KEY
# 3. Connect to PostgreSQL
# 4. Decrypt sensitive fields only when needed
```

---

### Layer 4: Access Control (RBAC)

**Control Plane Permissions:**

| Control Plane | Can Create | Can Sign | Can Approve | Can Delete |
|---|---|---|---|---|
| **CP-004 (Strategy)** | ✅ Generate from template | ❌ | ❌ | ❌ |
| **CP-011 (Task)** | ✅ Create task for signature | ✅ Self-sign | ❌ | ❌ |
| **CP-005 (Decision)** | ❌ | ❌ | ✅ Approve contracts | ❌ |
| **CP-027 (Infrastructure)** | ❌ | ❌ | ❌ | ✅ Archived contracts |
| **Principal (Human)** | ❌ | ✅ Execute contracts | ✅ Capital gates >$100K | ✅ Void contracts |

**Neo4j Enforcement:**
```cypher
-- Only CP-004 can GENERATE contracts
MATCH (cp:ControlPlane {id: 'CP-004'})
MATCH (c:CONTRACT)
WHERE c.created_by = 'CP-004'
RETURN c

-- Only CP-005 can approve >$50K contracts
MATCH (cp:ControlPlane {id: 'CP-005'})
MATCH (c:CONTRACT)
WHERE c.approval_amount > 50000
AND c.approved_by = 'CP-005'
RETURN c
```

---

### Layer 5: Validation & Audit

**Document Integrity Checking:**
```python
def verify_contract_integrity(contract_id, document_hash):
    """
    Verify contract hasn't been tampered with.
    Hash computed when contract signed; checked on every download.
    """
    # Fetch contract from OpenClaw
    contract = openclaw_client.get_contract(contract_id)
    document_content = contract['document_pdf']
    
    # Compute SHA-256 hash
    computed_hash = hashlib.sha256(document_content).hexdigest()
    
    # Compare to stored hash in PostgreSQL
    stored_hash = db.query(
        "SELECT document_hash FROM contracts WHERE openclaw_contract_id = %s",
        (contract_id,)
    )[0]['document_hash']
    
    if computed_hash != stored_hash:
        # ALERT: Document tampered with
        log_security_incident(
            event="CONTRACT_INTEGRITY_VIOLATION",
            contract_id=contract_id,
            severity="CRITICAL"
        )
        return False
    
    return True
```

**Audit Logging (Neo4j):**
```cypher
-- Log every contract action
CREATE (event:AUDIT_EVENT {
  timestamp: datetime.transaction(),
  event_type: 'CONTRACT_SIGNED',
  venture_id: 'CON-001',
  contract_id: 'oc_contract_xxx',
  actor: 'CP-011',
  action: 'SIGNED_BY_CUSTOMER',
  customer_email: 'customer@example.com',
  ip_address: '192.168.1.100',
  user_agent: 'Mozilla/5.0...',
  signature_verified: true,
  document_hash: 'sha256_xxx...'
})

-- Link to venture
MATCH (v:VENTURE {id: 'CON-001'})
CREATE (v)-[:EXECUTED_CONTRACT]->(event)
```

---

## INTEGRATION ARCHITECTURE

### Data Flow: End-to-End

```
MONDAY MORNING:
  User (via CP-011 ClickUp): "Generate customer LOI for CON-001"
    ↓
  CP-004 (Strategy Agent):
    - Retrieve LOI template from OpenClaw
    - Fill with venture data (customer name, terms, amounts)
    - Request signature from Customer + Principal
    ↓
  OpenClaw Portal:
    - Send signing link to customer
    - Display contract for review
    - Customer signs (e-signature captured)
    ↓
  OpenClaw Webhook:
    - POST /webhook/contract-signed
    - Signature: HMAC-SHA256 verified
    - Body includes: contract_id, signature_data, timestamp
    ↓
  Your System (CP-011):
    - Verify webhook signature
    - Store contract in PostgreSQL (encrypted)
    - Log event in Neo4j
    - Update ClickUp task: "LOI Signed by Customer"
    - Send notification to Principal: "LOI ready for approval"
    ↓
  Principal:
    - Review signed LOI in Neo4j dashboard
    - Click "Approve" (approves in ClickUp)
    ↓
  CP-005 (Decision):
    - Verify Principal approval
    - Update contract status: "EXECUTED"
    - Trigger payment in Stripe (if applicable)
    - Create capital allocation task: "Deploy $50K to CON-001"
    ↓
  CP-020 (Capital):
    - Transfer $50K to CON-001 venture account
    - Log in Neo4j
    - Notify customer: "Funding deployed"
```

### System Components

**1. OpenClaw API Client (Python/Vercel)**
```
Location: /SECTORS/SEC-024-Technology/ventures/CON-001/lib/openclaw_client.py
Purpose: Wrapper around OpenClaw REST API
Functions:
  - create_contract(venture_id, customer_email, template_id)
  - get_contract_status(contract_id)
  - verify_signature(contract_id, signature_data)
  - download_signed_document(contract_id)
```

**2. Webhook Handler (Vercel Function)**
```
Location: /api/webhooks/openclaw-contract-signed.ts
Purpose: Receive signed contracts from OpenClaw
Flow:
  1. Verify HMAC-SHA256 signature
  2. Store contract in PostgreSQL (encrypted)
  3. Log event to Neo4j
  4. Update ClickUp task
  5. Notify Principal
```

**3. Neo4j Schema Extensions**
```
New Node: :CONTRACT
  - id (OpenClaw contract ID)
  - venture_id
  - customer_email
  - status
  - signed_at
  - document_hash

New Relationships:
  - VENTURE -[:EXECUTED_CONTRACT]-> CONTRACT
  - CONTRACT -[:SIGNED_BY]-> PRINCIPAL
  - CONTRACT -[:REVIEWED_BY]-> CP (Control Plane)
```

**4. PostgreSQL Audit Table**
```
contracts (id, venture_id, openclaw_contract_id, status, ...)
audit_log (event_id, contract_id, action, timestamp, actor, ...)
```

---

## IMPLEMENTATION CHECKLIST

### Week 1 (Sep 9-15)
- [ ] Set up OpenClaw self-hosted Docker container
- [ ] Create OpenClaw service account + API key
- [ ] Add GitHub Secrets (OPENCLAW_API_KEY, CLIENT_ID, CLIENT_SECRET)
- [ ] Implement OpenClawClient Python wrapper
- [ ] Deploy webhook endpoint to Vercel
- [ ] Test: Generate sample contract for CON-001
- [ ] Test: Verify webhook signature

### Week 2 (Sep 16-22)
- [ ] Create contract templates (LOI, Customer Agreement, NDA)
- [ ] Wire ClickUp → OpenClaw (contract generation automation)
- [ ] Wire OpenClaw → ClickUp (signing status updates)
- [ ] Implement Neo4j audit logging
- [ ] Test: End-to-end contract signing
- [ ] Security audit: HMAC, encryption, access control
- [ ] Train Principal on contract approval flow

### Week 3+ (Sep 23+)
- [ ] Automate for all 5 ventures
- [ ] Scale to 20+ ventures (Phase 1)
- [ ] Integrate with Stripe (payment confirmation)
- [ ] Build audit dashboard (contract status by venture)

---

## SECURITY CHECKLIST

- [ ] API keys stored in GitHub Secrets (never in code)
- [ ] All API calls over TLS 1.3
- [ ] HMAC-SHA256 signing on all requests + webhooks
- [ ] PostgreSQL encryption for sensitive fields
- [ ] Webhook signature verification on receipt
- [ ] Contract integrity checking (SHA-256 hash)
- [ ] Neo4j audit logging (every action)
- [ ] Access control enforcement (CP permissions)
- [ ] Token expiration + refresh flow
- [ ] Quarterly API key rotation
- [ ] Master encryption key in air-gapped vault (Bitwarden)
- [ ] Rate limiting on API endpoints (100 req/min)
- [ ] IP whitelisting for OpenClaw API calls
- [ ] Signing links expire after 30 days
- [ ] Document version control in OpenClaw
- [ ] Backup encryption (AES-256)
- [ ] PII masking in logs + audit trail
- [ ] Regular security audits + penetration testing

---

## MONITORING & ALERTING

**Key Metrics:**
```
openclaw.contracts_created (Counter) — Total contracts generated
openclaw.contracts_signed (Counter) — Total contracts signed
openclaw.signature_verification_failed (Counter) — Failed verifications
openclaw.webhook_errors (Counter) — Webhook processing errors
openclaw.api_latency (Histogram) — API response time
openssl.contract_integrity_violations (Counter) — Tampered documents (ALERT)
```

**Alert Conditions:**
```
CRITICAL: signature_verification_failed > 3 in 1 hour
CRITICAL: contract_integrity_violations > 0
CRITICAL: webhook_errors > 5 in 1 hour
WARNING: api_latency_p95 > 2000ms
WARNING: contracts_created = 0 for 12 hours (system down?)
```

---

## COST ANALYSIS

| Component | Cost | Timeline |
|---|---|---|
| OpenClaw self-hosted (Docker) | $0 (OSS) | Ongoing |
| Infrastructure (CPU/memory) | $50/mo | Included in existing stack |
| API calls (OpenClaw managed) | $1-5 per contract | Per contract |
| PII encryption (pgcrypto) | $0 (PostgreSQL) | Included |
| HMAC signing (included) | $0 | Included |
| **Total (first 100 contracts)** | **$50-100** | **Month 1** |
| **Total (1,000 contracts)** | **$50-100** | **Months 2-3** |

---

## COMPLIANCE & CERTIFICATIONS

**OpenClaw Compliance (Self-Hosted):**
- ✅ SOC 2 Type II (auditable, you maintain controls)
- ✅ GDPR (data deletion, DPA support)
- ✅ ESIGN Act / eIDAS (e-signature legality)
- ✅ HIPAA-ready (if configured with encryption)

**Your Responsibility:**
- Maintain backup encryption
- Enforce access controls
- Rotate encryption keys
- Monitor audit logs
- Patch security vulnerabilities

