# WorldwideBro Holding Structure & Dispatch Infrastructure Strategy

## 1. The Core Thesis: Horizontal Infrastructure vs. Vertical Operations
The WorldwideBro portfolio operates on a decoupled structure, separating the **underlying technology primitives** from the **specialized operational companies**.

*   **LT-011 (Horizontal):** Dispatch Infrastructure & Transportation-Operations Platform.
*   **LT-005 (Vertical):** Medical Courier & Healthcare Logistics Operations.

LT-005 is not a software company; it is a specialized medical logistics operator that acts as the "first best customer" for LT-011's technology. LT-011 is not a trucking company; it is a broad dispatch orchestration layer that treats transportation modes (Ground, Marine, Aviation) as configurable resources.

### Architectural Model
```text
                    WORLDWIDEBRO
                         │
                 DISPATCH HOLDING
                         │
                      LT-011
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
    GROUND             MARINE           AVIATION
       │                 │                 │
    LT-005          Marine Ops       Aviation Ops
    Medical
       │
    Healthcare
```

LT-011 builds common primitives (customers, orders, jobs, assets, tracking, billing) while the vertical modules (like LT-005) add specialized entities and regulatory rules.

---

## 2. Multi-Engine Monetization (LT-011)
LT-011 does not rely on a single SaaS subscription. It utilizes a multi-engine monetization map:

| Revenue Engine | Target Audience | Monetization Model |
| :--- | :--- | :--- |
| **Dispatch Software** | Fleet/Operator | Monthly SaaS |
| **Managed Dispatch** | Fleet/Operator | Monthly + Per Job |
| **Transaction Fees** | Operator | $/dispatch or $/trip |
| **Fleet Management** | Fleet Owner | Monthly/vehicle |
| **Route Optimization** | Operator | SaaS / Add-on |
| **Telematics / GPS** | Operator | Per asset / month |
| **API Access** | Enterprise | Usage / API fee |
| **White-label BPO** | Companies | Platform fee + Monthly retainer |
| **Emergency/STAT** | Healthcare/Logistics | Premium transaction fee |

---

## 3. Financial Intelligence Layer (The Company Brain View)
Every venture within the holding company structure must be measurable against a standard set of financial primitives. 

### Core Financial Model
**Gross Revenue → COGS → Gross Profit → OpEx → EBITDA → Cash Flow**

*   **Revenue Categories:** Recurring (SaaS, Managed Service), Transactional (Dispatch, API), Premium (STAT, After-hours), Professional Services (Setup, Integration).
*   **COGS (Direct Costs):** Dispatch labor, Driver/crew payments, Fuel, Vehicle/asset costs, Insurance, API/Software infrastructure, Payment processing.
*   **OpEx (Fixed/Operating Costs):** Sales, Marketing, Admin, Engineering, Support, Compliance, Legal, Management.

### Executive Metrics (Unit Economics)
To answer the core question: *"Where does this company make money, what does it cost to deliver, what capacity exists, what can be charged, and what operational constraint prevents the next dollar of revenue?"*

*   **Jobs/day × average ticket × operating days**
*   **Revenue per asset-hour**
*   **Revenue per dispatcher**
*   **Contribution margin** (Does each incremental transaction make money?)
*   **Payback period** (How quickly CAC is recovered)

For **LT-005**, the north star metric is: *How many medical deliveries/routes/customers can we acquire and service profitably?*
For **LT-011**, the north star metric is: *How many dispatch transactions, fleets, operators, assets, and managed-dispatch customers can this infrastructure support profitably?*

This shared technology and operations layer allows WorldwideBro to scale into new verticals (Marine, Aviation, Construction) without duplicating core infrastructure.
