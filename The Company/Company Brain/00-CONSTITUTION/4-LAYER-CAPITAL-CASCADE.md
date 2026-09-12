---
id: DOC-FIN-CASCADE-001
title: The 4-Layer Capital Cascade
aliases: ["4-LAYER-CAPITAL-CASCADE", "Capital Cascade", "4 Layer Capital Cascade", "Capital Architecture"]
tags: [finance, capital, cascade, constitution, ventures]
status: ACTIVE
authority: "CP-001 / CP-027"
updated: 2026-09-12
---

[[STARTHERE]] | [[REALITY]] | [[00-CONSTITUTION/master-private-firm-ontology|MASTER-ONTOLOGY]] | [[24-FINANCE]] | [[INDEX]]

# The 4-Layer Capital Cascade

The **4-Layer Capital Cascade** is WorldwideBro’s non-dilutive capital structuring discipline. It governs how ventures fund operations, acquire assets, scale software, and return liquidity to the Master Trust.

```mermaid
graph TD
    L1[Layer 1: Customer Cash Flow & Pre-payments<br/>0% Cost of Capital / 0% Equity Dilution]
    L2[Layer 2: Non-Dilutive Grants & Subsidies<br/>Federal, State, Municipal, Energy Transition]
    L3[Layer 3: Asset-Backed Debt & Equipment Leasing<br/>Senior Secured, Accounts Receivable, Fleet Liens]
    L4[Layer 4: Institutional & Strategic Equity<br/>Holding Company Level Only / Sovereign Capital]

    L1 -->|Exhaust First| L2
    L2 -->|Exhaust Second| L3
    L3 -->|Exhaust Third| L4

    classDef l1 fill:#dcfce7,stroke:#22c55e,stroke-width:2px;
    classDef l2 fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    classDef l3 fill:#fef08a,stroke:#eab308,stroke-width:2px;
    classDef l4 fill:#fee2e2,stroke:#ef4444,stroke-width:2px;

    class L1 l1;
    class L2 l2;
    class L3 l3;
    class L4 l4;
```

---

## The Four Layers Explained

### Layer 1: Customer Cash Flow & Working Capital
- **Mandate:** Ventures must fund daily burn through customer receipts, milestone deposits, retainer pre-payments, and platform transaction fees.
- **Rule:** Never take debt or sell equity to fund payroll or basic software operating expenses.

### Layer 2: Non-Dilutive Grants & Public Funding
- **Mandate:** Federal grants (SBIR, STTR, DOT, DOE, ARPA), state innovation vouchers, and municipal workforce training subsidies.
- **Registries:** Tracked in `_REGISTRIES/CANONICAL/GRANT_OPPORTUNITY_REGISTRY.yaml`.

### Layer 3: Asset-Backed Debt & Equipment Facilities
- **Mandate:** Heavy equipment, fleet vehicles, and datacenter hardware are financed via collateralized senior debt or equipment lease lines.
- **Protection:** Debt is strictly siloed in Asset Holding LLCs with no recourse to the Master Trust or Operating Company IP.

### Layer 4: Holding Company Equity & Sovereign Capital
- **Mandate:** Permanent capital and minority strategic equity only at the Holdings or parent vehicle level.
- **Rule:** Operating subsidiaries remain 100% owned or controlled by WorldwideBro.
