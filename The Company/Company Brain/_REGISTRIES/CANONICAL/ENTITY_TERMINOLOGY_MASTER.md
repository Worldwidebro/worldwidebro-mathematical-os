# ENTITY TERMINOLOGY & HIERARCHY
## Complete Glossary of 150-Entity Ecosystem

---

## 1. ENTITY ATTRIBUTES (35-Attribute Standard)

Every entity in the system is defined by these 35 core attributes:

| Attribute | Definition | Example |
|-----------|-----------|---------|
| **entity_id** | Unique identifier (ENT-001 to ENT-150) | ENT-001 |
| **entity_number** | Sequential numeric identifier | 1 |
| **entity_name** | Legal name / DBA | "Founder" |
| **entity_type** | Category of legal structure | INDIVIDUAL, TRUST, LLC, C-CORP, PARTNERSHIP, SPV, ESTATE_VEHICLE, FUND |
| **entity_class** | Role in the hierarchy | FOUNDER, TRUSTEE, HOLDING, OPERATING, VENTURE, ADVISORY, CAPITAL |
| **layer_id** | Position in 12-layer architecture (1-12) | 1 |
| **layer_name** | Name of the layer | "FOUNDER / FAMILY OWNERSHIP" |
| **parent_entity_id** | Direct parent in ownership hierarchy | ENT-001 (if parent is founder) |
| **ultimate_owner** | Top-level owner | "Founder" |
| **beneficial_owner** | Entity that benefits from profits | "Family Beneficiaries" |
| **tax_classification** | IRS tax entity type | INDIVIDUAL, TRUST, LLC, C-CORP, S-CORP, GRANTOR_TRUST, PARTNERSHIP |
| **state_of_formation** | Where entity was legally created | NC (North Carolina) |
| **jurisdiction** | Legal jurisdiction (US, specific state) | US |
| **purpose** | Why entity exists | "Ultimate human owner" |
| **asset_types** | What assets it holds | Personal Estate Equity, Master HoldCo Equity |
| **revenue_streams** | Money sources | Executive Distributions, Trust Distributions |
| **bank_accounts** | Where cash is held | Mercury Trust Account, First Citizens |
| **contracts** | Governing legal documents | Operating Agreements, Trust Agreements |
| **licenses** | Required permits/authorities | Fiduciary Authority, Real Estate License |
| **employees** | Number of people employed | 0, 1, 3, etc. |
| **vendors** | Suppliers / service providers | Trustee Advisory, Insurance Brokers |
| **customers** | Revenue-generating clients | (empty if holding company) |
| **IP_owned** | Intellectual property held | WorldwideBro Trademarks, Patents |
| **insurance** | Coverage policies | Umbrella Personal Policy ($5M) |
| **debt** | Liabilities | None, Personal Mortgages, Commercial Loans |
| **equity** | Ownership percentage | 100% Primary Equity, 100% Ownership |
| **cash_flow** | Money pattern | Net Capital Accumulation, Pass-Through |
| **distributions** | Money paid out | Personal Withdrawals, K-1 to Beneficiaries |
| **tax_obligations** | Filing requirements | Form 1040, Form 1041, Form 1065, Form 1120-S |
| **related_entities** | Cross-references | ENT-001, ENT-002, etc. |
| **upstream_entities** | Parent structure | ENT-001 (founder) |
| **downstream_entities** | Children entities | ENT-031, ENT-034, etc. |
| **status** | Current state | ACTIVE, INACTIVE, PLANNED, DISSOLVED |
| **formation_status** | Legal setup state | FORMED, PENDING, DISSOLVED |
| **CPA_owner** | Accounting authority | Worldwidebro Central Accounting Office (Node 143) |
| **legal_owner** | Legal authority | Worldwidebro Legal & Trust Protector Office (Node 11) |
| **venture_id** | Linked venture (if operating) | OPS-001, LT-005, null (if holding) |

---

## 2. ENTITY TYPES (9 Categories)

### **INDIVIDUAL**
- Legal person (human)
- Example: ENT-001 "Founder"
- Tax Filing: Form 1040
- Liability: Personal guarantee capability
- Can own: businesses, trusts, property

### **TRUST**
- Legal arrangement for holding assets
- **Subtypes:**
  - **GRANTOR_TRUST** — Founder retains control, passes through to beneficiaries
    - Example: ENT-003 "Family Ownership Trust"
  - **IRREVOCABLE_TRUST** — Locked in, cannot be changed (tax benefits)
    - Example: ENT-005, ENT-016, ENT-017
  - **REVOCABLE_LIVING_TRUST** — Flexible during grantor's life
    - Example: ENT-004
  - **GENERATION_SKIPPING_TRUST** — Multi-generational transfer
- Purpose: Hold assets, manage distributions, avoid probate

### **LLC** (Limited Liability Company)
- Private business entity
- Owners: "Members" (people or other entities)
- Liability: Shielded (members not personally liable)
- Tax Filing: Form 1065 or elect as C/S-Corp
- Examples: ENT-031, ENT-032, ENT-034, ENT-035

### **C-CORP** (C Corporation)
- Large business entity, double taxation
- Tax Filing: Form 1120
- Used for: Large operations, external investors

### **S-CORP** (S Corporation)
- Small/medium business, pass-through taxation
- Tax Filing: Form 1120-S
- Shareholders: ≤100

### **PARTNERSHIP**
- Joint venture between 2+ entities
- Owners: "Partners"
- Tax Filing: Form 1065

### **SPV** (Special Purpose Vehicle)
- Single-purpose holding entity
- Owns: One specific asset
- Example: ENT-093 "Warehouse SPV #1"
- Purpose: Liability isolation

### **ESTATE_VEHICLE**
- Holds personal assets during lifetime
- Example: ENT-002 "Founder Personal Estate"

### **FUND** (Investment Fund)
- Pools capital from investors
- Example: ENT-131 "Capital Fund One"

---

## 3. ENTITY CLASSES (6 Roles)

| Class | Role | Authority | Scope | Example |
|-------|------|-----------|-------|---------|
| **FOUNDER** | Ultimate decision authority | Create/modify/dissolve entities | ENT-001-015 | ENT-001 (Antwuan Johns) |
| **TRUSTEE** | Manages trust assets for beneficiaries | Duty of care, loyalty, prudence | ENT-148 | Professional trustee |
| **HOLDING** | Owns other entities | Set policy, allocate capital | ENT-031-045 | Master HoldCo |
| **OPERATING** | Runs actual business | Hire, fire, sign contracts | ENT-046-138 | LT-005 Courier |
| **VENTURE** | Individual business unit | Daily operations, team management | Mapped to venture_id | OPS-001, LT-005 |
| **ADVISORY** | Professional advice/governance | Recommend, approve, audit | ENT-141-150 | Legal, CPA, Trustees |

---

## 4. ENTITY LAYERS (12 Tiers)

| Layer | Name | Range | Count | Purpose |
|-------|------|-------|-------|---------|
| **1** | FOUNDER / FAMILY OWNERSHIP | ENT-001-015 | 15 | Ultimate ownership, succession |
| **2** | ESTATE / SUCCESSION | ENT-016-030 | 15 | Trusts for wealth transfer |
| **3** | MASTER HOLDING STRUCTURE | ENT-031-045 | 15 | Strategic HoldCos |
| **4** | OPERATING COMPANY LAYER | ENT-046-065 | 20 | Sector OpCos |
| **5** | LOGISTICS / DISPATCH | ENT-066-080 | 15 | Transportation, courier ops |
| **6** | HEALTHCARE / MEDICAL | ENT-081-090 | 10 | Medical courier services |
| **7** | REAL ESTATE EMPIRE | ENT-091-110 | 20 | Property holdings, SPVs |
| **8** | CONSTRUCTION / FIELD | ENT-111-118 | 8 | Construction ops |
| **9** | TECHNOLOGY / IP / BRAIN | ENT-119-130 | 12 | Software IP, platforms |
| **10** | INVESTMENT / CAPITAL | ENT-131-140 | 10 | Trading, treasury, funds |
| **11** | FAMILY OFFICE / ADMIN | ENT-141-145 | 5 | Central governance |
| **12** | CHARITY / FOUNDATION | ENT-146-150 | 5 | Charitable giving |

---

## 5. ENTITY RELATIONSHIPS

### **Upstream** (Parent)
- Who owns this entity?
- Example: ENT-003 (Family Trust) ← owned by ← ENT-001 (Founder)

### **Downstream** (Children)
- What does this entity own?
- Example: ENT-031 (Master HoldCo) → owns → ENT-032, ENT-034, ENT-035, etc.

### **Sibling**
- Same parent, different entities
- Example: ENT-032, ENT-034, ENT-035 all owned by ENT-031

### **Cross-Link** (Advisory)
- Service relationship, not ownership
- Example: ENT-145 (Legal) serves ENT-031 (Master HoldCo)

---

## 6. TAX FILING MATRIX

| Entity Type | Tax Classification | Form Filed | Who Pays |
|-------------|-------------------|-----------|---------|
| Individual | INDIVIDUAL | Form 1040 | Founder |
| Trust | GRANTOR_TRUST | Form 1040 | Beneficiary |
| Trust | NON-GRANTOR_TRUST | Form 1041 | Trust |
| LLC (default) | PARTNERSHIP | Form 1065 | Members |
| LLC (elected) | C-CORP | Form 1120 | Entity |
| LLC (elected) | S-CORP | Form 1120-S | Shareholders |
| Partnership | PARTNERSHIP | Form 1065 | Partners |
| SPV | (Depends) | Form 1065 or 1041 | Owner |

---

## 7. AUTHORITY LEVELS

| Authority | Who Has It | Can Do | Cannot Do |
|-----------|-----------|---------|----------|
| **SOVEREIGN** | Founder (ENT-001) | Create/modify/dissolve entities, allocate capital | Ignore fiduciary duties, break laws |
| **FIDUCIARY** | Trustees, Advisors | Manage assets, make decisions for beneficiaries | Self-deal without disclosure |
| **HOLDING_EXECUTIVE** | HoldCo CEO | Set policy, allocate to OpCos, hire OpCo CEOs | Operate directly, incur liability |
| **OPERATING** | OpCo CEO | Hire, fire, sign contracts, acquire assets | Exceed capital limits, incur debt |
| **VENTURE_LEADER** | Venture CEO | Daily operations, team management | Commit to major contracts |

---

## 8. LIABILITY SHIELDING

```
LT-005 Driver hits someone
  ↓ (claim against)
LT-005 LLC operating account
  ↓ (insurance covers)
Commercial Liability Policy ($2M)
  ↓ (if insufficient)
Logistics Holdings (ENT-035)
  ↓ (stopped here by LLC protection)
Master HoldCo, Real Estate, Founder assets: SHIELDED
```

---

## 9. CAPITAL FLOW TERMINOLOGY

| Term | Definition |
|------|-----------|
| **Distribution** | Money paid from entity to owner |
| **Dividend** | Money paid from C-Corp to shareholders |
| **Profit Stripping** | Intentional profit transfer via fees/leases |
| **Intercompany Loan** | Entity lends to related entity |
| **Capital Call** | Investor required to contribute cash |
| **Capital Allocation** | HQ decides where to invest (40/50/10 model) |
| **Cash Sweep** | Automatic movement of excess cash to treasury |

---

## 10. FORMATION & STATUS

| Term | Meaning |
|------|---------|
| **FORMED** | Legally exists and is operating |
| **PENDING** | In process, paperwork filed |
| **ACTIVE** | Fully operational |
| **INACTIVE** | Dormant/shell company |
| **DISSOLVED** | Legally terminated |

---

## 11. THE COMPLETE HIERARCHY

```
FOUNDER (ENT-001: Antwuan Johns) — YOU
    ↓
FAMILY TRUSTS (ENT-003, ENT-016, ENT-017, etc.) — 15 entities
    ↓
WORLDWIDEBRO HOLDINGS LLC (ENT-031) — Master HoldCo
    ↓
6 STRATEGIC HOLDCOS:
    ├── ENT-032: Business Holdings (11 sector OpCos, 233 ventures)
    ├── ENT-035: Logistics Holdings (3 sector OpCos, 41 ventures)
    ├── ENT-034: Real Estate Holdings (2 sector OpCos, 19 properties)
    ├── ENT-119: IP & Tech Vault (4 sector OpCos, 466 ventures)
    ├── ENT-036: Capital & Financial (5 sector OpCos, 50 ventures)
    └── ENT-041: Strategy & Discovery (5 sector OpCos, 10 ventures)
    ↓
36 OPERATING COMPANIES (OpCos) — Sector leaders
    ↓
789 VENTURES — Individual operating businesses
```

---

## 12. CRITICAL ENTITY IDs

| ID | Name | Role |
|----|------|------|
| **ENT-001** | Founder | YOU — all authority flows here |
| **ENT-003** | Family Ownership Trust | Master trust — holds all wealth |
| **ENT-031** | WorldwideBro Holdings LLC | Master HoldCo — all strategy |
| **ENT-032** | Business Holdings | 11 sector OpCos |
| **ENT-035** | Logistics Holdings | LT-005, LT-011 (revenue leaders) |
| **ENT-034** | Real Estate Holdings | All property (liability shield) |
| **ENT-119** | IP & Tech Vault | All software, platforms, IP |
| **ENT-145** | Legal Counsel | All legal decisions |
| **ENT-146** | CPA & Tax | All tax decisions |
| **ENT-143** | Central Accounting | Financial operations |

---

**Version:** 1.0  
**Created:** 2026-09-23  
**Authority:** CP-027 (Infrastructure Control Plane)  
**Status:** CANONICAL — Master reference for all entity terminology
