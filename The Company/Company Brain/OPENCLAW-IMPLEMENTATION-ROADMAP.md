# OpenClaw Implementation Roadmap — From Zero to Revenue Loop

**Created:** 2026-09-09  
**Timeline:** 3 weeks to full automation  
**Status:** Ready to execute  

---

## PHASE 1: SECURITY SETUP (Week 1 — Sep 9-15)

### Day 1 (Today, Tuesday Sep 10)

**1. Set up Bitwarden Vault (30 min)**
```bash
# Store master encryption key in local Bitwarden vault (offline)
bw config server http://localhost:8000  # Local Bitwarden instance
bw login  # Login with master password

# Add encryption key
bw create item "OpenClaw Master Key"
  password: <generate 64-char random>
  notes: "Master encryption key for PostgreSQL pgcrypto"
  
# Verify: Never sync to cloud (Bitwarden Online Backup OFF)
```

**2. Store GitHub Secrets (15 min)**
```bash
# Go to GitHub > Settings > Secrets and variables > Actions

# Add these secrets:
OPENCLAW_API_KEY=<from OpenClaw admin portal>
OPENCLAW_CLIENT_ID=<from OpenClaw OAuth app>
OPENCLAW_CLIENT_SECRET=<from OpenClaw OAuth app>
OPENCLAW_WEBHOOK_SECRET=<from OpenClaw webhooks>
POSTGRES_ENCRYPTION_KEY=<from local Bitwarden>
NEO4J_BOLT_URL=bolt://100.87.214.70:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=<verify in local Bitwarden>
```

**3. Set Up PostgreSQL Encryption (15 min)**
```bash
# SSH to your database server
ssh ubuntu@db-server

# Enable pgcrypto extension
psql -U postgres -d company_brain
  CREATE EXTENSION IF NOT EXISTS pgcrypto;
  
# Verify
  SELECT * FROM pg_extension WHERE extname = 'pgcrypto';
  
# Exit
  \q
```

**4. Verify TLS 1.3 (15 min)**
```bash
# Verify your Vercel deployments use TLS 1.3
for venture in CON-001 OPS-001 LT-005 LT-011 RE-001; do
  vercel env list --project=worldwidebro-${venture}
  # Should show: NODE_TLS_VERSION=TLSv1.3
done
```

**Deliverables by EOD:**
- ✅ GitHub Secrets configured
- ✅ PostgreSQL encryption enabled
- ✅ TLS 1.3 verified on all ventures
- ✅ Master encryption key in local Bitwarden (not cloud)

---

### Day 2-3 (Wed-Thu, Sep 11-12)

**5. Create OpenClaw Client Library (2 hours)**

**File:** `/SECTORS/SEC-024-Technology/shared/lib/openclaw-client.py`

```python
import hmac
import hashlib
import json
import requests
import os
from datetime import datetime, timedelta
from typing import Dict, Optional

class OpenClawClient:
    """
    OpenClaw API client with HMAC-SHA256 signing and webhook verification.
    Implements security Layer 2 (TLS 1.3 + HMAC).
    """
    
    def __init__(self):
        self.api_key = os.getenv('OPENCLAW_API_KEY')
        self.client_id = os.getenv('OPENCLAW_CLIENT_ID')
        self.client_secret = os.getenv('OPENCLAW_CLIENT_SECRET')
        self.api_url = os.getenv('OPENCLAW_API_URL', 'https://openclaw.internal/api/v1')
        self.webhook_secret = os.getenv('OPENCLAW_WEBHOOK_SECRET')
        
        if not self.api_key:
            raise ValueError("OPENCLAW_API_KEY not set in environment")
    
    def sign_request(self, method: str, path: str, body: Optional[Dict] = None) -> Dict[str, str]:
        """Generate HMAC-SHA256 signature for request."""
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
    
    def create_contract(
        self,
        venture_id: str,
        customer_email: str,
        template_id: str,
        contract_data: Dict
    ) -> Dict:
        """
        Create a contract from template.
        
        Args:
            venture_id: Venture ID (e.g., "CON-001")
            customer_email: Customer email for signing
            template_id: OpenClaw template ID
            contract_data: Data to fill into template
        
        Returns:
            Contract creation response with signing link
        """
        path = "/contracts"
        body = {
            "template_id": template_id,
            "parties": [
                {
                    "name": "Worldwidebro Holdings",
                    "email": "legal@worldwidebro.co",
                    "role": "issuer"
                },
                {
                    "name": contract_data.get("customer_name", "Customer"),
                    "email": customer_email,
                    "role": "signer"
                }
            ],
            "data": contract_data,
            "metadata": {
                "venture_id": venture_id,
                "created_by": "CP-004",
                "created_at": datetime.utcnow().isoformat(),
                "expires_at": (datetime.utcnow() + timedelta(days=30)).isoformat()
            },
            "webhook_url": f"https://your-domain.com/webhooks/openclaw-contract-signed"
        }
        
        headers = self.sign_request("POST", path, body)
        
        response = requests.post(
            f"{self.api_url}{path}",
            json=body,
            headers=headers,
            verify=True,  # TLS verification
            timeout=30
        )
        
        response.raise_for_status()
        return response.json()
    
    def get_contract_status(self, contract_id: str) -> Dict:
        """Get contract status."""
        path = f"/contracts/{contract_id}"
        headers = self.sign_request("GET", path)
        
        response = requests.get(
            f"{self.api_url}{path}",
            headers=headers,
            verify=True,
            timeout=30
        )
        
        response.raise_for_status()
        return response.json()
    
    def verify_webhook_signature(self, request_headers: Dict, request_body: bytes) -> bool:
        """Verify webhook signature from OpenClaw."""
        signature = request_headers.get("X-OpenClaw-Webhook-Signature")
        timestamp = request_headers.get("X-OpenClaw-Timestamp")
        
        if not signature or not timestamp:
            return False
        
        # Verify timestamp is within 5 minutes (prevent replay attacks)
        try:
            request_time = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            now = datetime.utcnow().replace(tzinfo=request_time.tzinfo)
            if abs((now - request_time).total_seconds()) > 300:
                return False
        except:
            return False
        
        # Verify HMAC signature
        expected_signature = hmac.new(
            self.webhook_secret.encode(),
            f"{timestamp}{request_body.decode()}".encode(),
            hashlib.sha256
        ).hexdigest()
        
        return hmac.compare_digest(signature, expected_signature)
    
    def download_signed_document(self, contract_id: str) -> bytes:
        """Download signed PDF document."""
        path = f"/contracts/{contract_id}/document"
        headers = self.sign_request("GET", path)
        
        response = requests.get(
            f"{self.api_url}{path}",
            headers=headers,
            verify=True,
            timeout=30
        )
        
        response.raise_for_status()
        return response.content
```

**Deliverables:**
- ✅ OpenClaw client library created
- ✅ HMAC signing implemented
- ✅ Webhook verification implemented
- ✅ Error handling + timeout set

**6. Create PostgreSQL Contracts Schema (30 min)**

**File:** `_INFRASTRUCTURE/migrations/001_create_contracts_table.sql`

```sql
-- Enable encryption
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Contracts table
CREATE TABLE contracts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id VARCHAR(20) NOT NULL,
  openclaw_contract_id VARCHAR(255) NOT NULL UNIQUE,
  customer_email VARCHAR(255) NOT NULL,
  customer_name TEXT ENCRYPTED WITH pgcrypto.pgp_sym_encrypt(pgp_key),
  contract_type VARCHAR(100),  -- LOI, Customer Agreement, NDA
  status VARCHAR(50) DEFAULT 'draft',
  
  -- Document integrity
  document_hash VARCHAR(64),  -- SHA-256
  signature_data JSONB ENCRYPTED WITH pgcrypto.pgp_sym_encrypt(pgp_key),
  
  -- Timestamps
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  signed_at TIMESTAMP,
  expires_at TIMESTAMP,
  
  -- Audit
  created_by VARCHAR(50),
  approved_by VARCHAR(50),
  neo4j_id VARCHAR(100),
  
  CONSTRAINT valid_venture CHECK (venture_id ~ '^[A-Z]+-[0-9]{3}$'),
  CONSTRAINT valid_status CHECK (status IN ('draft', 'pending_signature', 'signed', 'executed')),
  INDEX idx_venture_status (venture_id, status),
  INDEX idx_customer_email (customer_email),
  INDEX idx_openclaw_id (openclaw_contract_id)
);

-- Audit log
CREATE TABLE audit_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  contract_id UUID REFERENCES contracts(id),
  event_type VARCHAR(100),  -- CREATED, SIGNED, APPROVED, EXECUTED
  actor VARCHAR(50),
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  details JSONB,
  
  INDEX idx_contract (contract_id),
  INDEX idx_timestamp (timestamp)
);

-- Run migration
psql -U postgres -d company_brain -f 001_create_contracts_table.sql
```

**Deliverables:**
- ✅ Contracts table created
- ✅ Audit log created
- ✅ Encryption enabled
- ✅ Indexes created

**7. Create Webhook Handler (Vercel Function)**

**File:** `/api/webhooks/openclaw-contract-signed.ts`

```typescript
// api/webhooks/openclaw-contract-signed.ts
// Webhook handler for OpenClaw contract signing events

import { NeonQueryFunction } from "@neondatabase/serverless";
import crypto from "crypto";

export default async function handler(req, res) {
  // 1. VERIFY WEBHOOK SIGNATURE
  const signature = req.headers["x-openclaw-webhook-signature"] as string;
  const timestamp = req.headers["x-openclaw-timestamp"] as string;
  
  if (!signature || !timestamp) {
    return res.status(400).json({ error: "Missing signature headers" });
  }
  
  // Verify timestamp (within 5 minutes)
  const requestTime = new Date(timestamp);
  const now = new Date();
  if (Math.abs((now.getTime() - requestTime.getTime()) / 1000) > 300) {
    return res.status(400).json({ error: "Request timestamp expired" });
  }
  
  // Verify HMAC signature
  const body = JSON.stringify(req.body);
  const expectedSignature = crypto
    .createHmac("sha256", process.env.OPENCLAW_WEBHOOK_SECRET!)
    .update(`${timestamp}${body}`)
    .digest("hex");
  
  if (!crypto.timingSafeEqual(signature, expectedSignature)) {
    return res.status(401).json({ error: "Invalid signature" });
  }
  
  // 2. PROCESS WEBHOOK
  const { contract_id, event_type, data } = req.body;
  
  if (event_type !== "contract.signed") {
    return res.status(200).json({ status: "ignored" });
  }
  
  // 3. STORE IN POSTGRESQL (encrypted)
  const sql = neon(process.env.DATABASE_URL!);
  
  try {
    const result = await sql`
      INSERT INTO contracts (
        openclaw_contract_id,
        venture_id,
        customer_email,
        customer_name,
        status,
        document_hash,
        signature_data,
        signed_at
      ) VALUES (
        ${contract_id},
        ${data.venture_id},
        ${data.customer_email},
        pgp_sym_encrypt(${data.customer_name}, ${process.env.POSTGRES_ENCRYPTION_KEY}),
        'signed',
        ${data.document_hash},
        pgp_sym_encrypt(${JSON.stringify(data.signature)}, ${process.env.POSTGRES_ENCRYPTION_KEY}),
        NOW()
      )
      RETURNING id;
    `;
    
    const contractId = result[0].id;
    
    // 4. LOG TO NEO4J
    await logToNeo4j({
      event_type: "CONTRACT_SIGNED",
      contract_id,
      venture_id: data.venture_id,
      customer_email: data.customer_email,
      timestamp: new Date().toISOString()
    });
    
    // 5. UPDATE CLICKUP TASK
    await updateClickUpTask({
      task_name: `${data.venture_id} Contract Signed`,
      status: "COMPLETED",
      custom_fields: {
        customer_email: data.customer_email,
        contract_id,
        signature_verified: true
      }
    });
    
    // 6. NOTIFY PRINCIPAL
    await sendNotification({
      to: process.env.PRINCIPAL_EMAIL,
      subject: `Contract Signed: ${data.venture_id}`,
      body: `${data.customer_email} signed the ${data.venture_id} contract. Ready for approval.`
    });
    
    return res.status(200).json({ status: "processed", contract_id: contractId });
  } catch (error) {
    console.error("Webhook processing error:", error);
    return res.status(500).json({ error: "Processing failed" });
  }
}
```

**Deliverables:**
- ✅ Webhook handler created
- ✅ Signature verification implemented
- ✅ PostgreSQL storage + encryption
- ✅ Neo4j logging
- ✅ Notifications (ClickUp + email)

---

## PHASE 2: INTEGRATION (Week 2 — Sep 16-22)

**8. Create Contract Templates in OpenClaw**

```
Templates to create:
  ├─ LOI_GENERIC.docx (use for all ventures)
  ├─ CUSTOMER_AGREEMENT_CON.docx (construction)
  ├─ STAFFING_PLACEMENT_AGREEMENT.docx (OPS-001)
  ├─ NDA_TEMPLATE.docx (all)
  └─ CONVERSION_NOTE.docx (early investors)

For each template:
  1. Upload to OpenClaw admin portal
  2. Define fillable fields (venture name, customer name, terms, amounts)
  3. Set signing order (Worldwidebro first, customer second)
  4. Configure expiration (30 days)
  5. Copy template_id to GitHub Secrets
```

**9. Wire ClickUp → OpenClaw Integration**

```bash
# When task "Send [VENTURE] Contract to Customer" is created:
# 1. ClickUp webhook fires
# 2. Trigger GitHub Actions workflow
# 3. Extract customer email + venture ID from task
# 4. Call OpenClaw API to generate contract
# 5. Update ClickUp with signing link

# GitHub Action: .github/workflows/generate-contract-on-task.yml
name: Generate Contract on ClickUp Task

on:
  webhook:
    event: task.created
    name_contains: "Send Contract"

jobs:
  generate_contract:
    runs-on: ubuntu-latest
    steps:
      - name: Extract venture + customer from task
        id: extract
        run: |
          venture_id=$(echo "${{ github.event.task.name }}" | grep -oE '[A-Z]+-[0-9]{3}')
          customer_email=$(echo "${{ github.event.task.description }}" | grep -oE '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
          echo "::set-output name=venture_id::$venture_id"
          echo "::set-output name=customer_email::$customer_email"
      
      - name: Generate contract via OpenClaw
        run: |
          python scripts/generate_contract.py \
            --venture_id ${{ steps.extract.outputs.venture_id }} \
            --customer_email ${{ steps.extract.outputs.customer_email }} \
            --template_id ${{ secrets.OPENCLAW_LOI_TEMPLATE_ID }}
      
      - name: Update ClickUp with signing link
        run: |
          curl -X PATCH https://api.clickup.com/api/v2/task/${{ github.event.task.id }} \
            -H "Authorization: ${{ secrets.CLICKUP_API_TOKEN }}" \
            -d '{
              "custom_fields": [{
                "id": "contract_signing_link",
                "value": "${{ env.SIGNING_LINK }}"
              }]
            }'
```

**Deliverables by end of Week 2:**
- ✅ All templates created in OpenClaw
- ✅ ClickUp → OpenClaw integration live
- ✅ Signing links auto-generated
- ✅ Contracts auto-logged to PostgreSQL

---

## PHASE 3: AUTOMATION (Week 3 — Sep 23-30)

**10. End-to-End Revenue Loop Automation**

**Trigger sequence:**
```
MONDAY:
  You make call → Warm lead → Send contract
  └─ ClickUp task: "Send [CON-001] contract to [Mike]"
     └─ GitHub Action triggered
        └─ OpenClaw generates LOI
           └─ Signing link sent to customer
              └─ ClickUp updated with link

THURSDAY:
  Customer signs contract
  └─ OpenClaw webhook fires
     └─ Vercel function receives + verifies
        └─ PostgreSQL stores contract (encrypted)
           └─ Neo4j logged
              └─ ClickUp task updated: "SIGNED"
                 └─ Principal notified: "Ready for approval"

FRIDAY:
  You review + approve
  └─ ClickUp: "Approve CON-001 + deploy $50K"
     └─ CP-005 Decision gate verified
        └─ CP-020 Capital wires $50K
           └─ Neo4j updated
              └─ Notifications sent
                 └─ $50K appears in CON-001 account
```

---

## IMMEDIATE ACTION ITEMS (Start Today)

### TODAY (Sep 10):
- [ ] Store GitHub Secrets (30 min)
- [ ] Enable PostgreSQL encryption (15 min)
- [ ] Verify TLS 1.3 (15 min)
- [ ] Master encryption key in Bitwarden (30 min)

### THIS WEEK (Sep 11-15):
- [ ] Create OpenClaw client library (2 hours)
- [ ] Create PostgreSQL schema (30 min)
- [ ] Create webhook handler (1 hour)
- [ ] Test end-to-end (1 hour)

### NEXT WEEK (Sep 16-22):
- [ ] Create contract templates (2 hours)
- [ ] Wire ClickUp integration (2 hours)
- [ ] Security audit (1 hour)

### FINAL WEEK (Sep 23-30):
- [ ] Full automation testing (2 hours)
- [ ] Train on contract workflow (30 min)
- [ ] Deploy to production (30 min)

---

## SUCCESS CRITERIA

**By Sep 30:**
- ✅ All 5 ventures have contracts generated automatically
- ✅ OpenClaw signatures verified and stored (encrypted)
- ✅ Neo4j audit trail complete
- ✅ Capital deployment triggered by signed contracts
- ✅ $50K+ deployed to ventures based on revenue signals
- ✅ 100+ contracts signed (across all ventures)
- ✅ $10K+ revenue generated

---

## COST & TIMELINE

| Phase | Timeline | Cost | Owner |
|---|---|---|---|
| Security setup | 2 hours | $0 | You + CP-027 |
| Client library | 2 hours | $0 | Claude |
| PostgreSQL | 1 hour | $0 | You |
| Webhook handler | 1 hour | $0 | Claude |
| Templates | 2 hours | $0 | You + CP-024 |
| ClickUp integration | 2 hours | $0 | Claude |
| Testing | 2 hours | $0 | You |
| **TOTAL** | **12 hours** | **$0** | Parallel |

---

## DECISION GATE

**Ready to implement OpenClaw?**

YES → Proceed with Phase 1 today (Sep 10)  
NO → Use manual contracts (Google Docs) for first week, wire up Sep 16+

**Recommendation:** YES. 3 weeks of setup now = 3 months of saved manual work.

