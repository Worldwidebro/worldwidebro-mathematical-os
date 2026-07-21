---
execution_metadata:
  venture_id: "FIN-033-AI-Tax-Preparation-Service"
  agent_completed: "AG-CFO"
  department: "Operations & Logistics"
  node: "HW-AIR-01"
  database_link: "DB-POSTGRES:PT-5433"
references:
  - [[FIN-033-AI-Tax-Preparation-Service-CAPABILITY-STATEMENT]]
  - [[FIN-033-AI-Tax-Preparation-Service-DEPARTMENTS-AND-ECOSYSTEM]]
  - [[HOLDINGS-PLAYBOOK]]
---

# FIN Formation & Credential Tracker — Financial

**Sector:** Financial  ·  **Holdings:** Winners Circle WC LLC

---

## 1) ENTITY REGISTRATION
*   **Legal Status:** development (e.g. DBA skin under Winners Circle WC LLC)
*   **EIN:** On file (assigned under parent Winners Circle WC LLC)
*   **IRS PTIN (Preparer Tax Identification Number):** [PTIN or Pending]
*   **State Tax Board Registrations:** North Carolina (Charlotte/Mecklenburg County)

---

## 2) FINANCIAL INFRASTRUCTURE
*   **Plaid Developer API Status:** [Status / Keys configured]
*   **Bookkeeping DB Schema Version:** `v1.2.0` (Postgres `iza_os_ventures` tables)
*   **Billing Engine:** Stripe invoice integrations
*   **ReportLab Engine Path:** `services/report_generator.py` (compiled PDFs)

---

## 3) ECOSYSTEM CHANNELS & DOMAIN LINKS
*   **Bookkeeping Admin Endpoint:** `https://finance.[domain]`
*   **Vector Ledger Store:** Qdrant `ledger_embeddings` collection
*   **Tax Audit API Endpoint:** `https://[id]-tax-engine.vercel.app/api/audit`
