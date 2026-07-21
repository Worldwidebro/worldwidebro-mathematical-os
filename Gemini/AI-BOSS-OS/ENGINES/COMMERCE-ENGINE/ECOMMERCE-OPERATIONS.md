# Ecommerce Operations: Sourcing & Logistics SOPs

This document defines the processes for procurement, sourcing, sample testing, and dropship/POD integrations for physical products in the Worldwidebro brand layer.

---

## 1. Sourcing Pipeline

When a physical product opportunity scores > 75 on validation, we trigger the sourcing agent:

```text
Identify Opportunity ➔ Supplier Sourcing (Alibaba/1688) ➔ Sample Request ➔ QA Test ➔ Production & Fulfillment Setup
```

### Sourcing Guidelines
- **Supplier Criteria**: Alibaba Gold Supplier or 1688 Verified Manufacturer. Minimum 3 years active. Transaction history > $100K.
- **RFQ Process**: Send standard RFQ asking for MOQ (Minimum Order Quantity), unit pricing tiers, and custom branding setup costs.
- **Sourcing 1688.com**: Leverage local shipping agents in China to purchase directly from 1688 to reduce unit cost by 30% compared to Alibaba.

---

## 2. Sample Verification & QA

We require all supplier samples to be shipped to the Worldwidebro operations office for QA testing. The inspector checks:
- **Material Quality**: Durability, stitching (if apparel/bags), paper thickness (if planner), plastic thickness (if desk gear).
- **Packaging Integrity**: Ensure the box survives a 1-meter drop test.
- **Custom Logo Placement**: Alignment, resolution, and print quality.

---

## 3. Fulfillment Strategy

- **Phase 1 (Validation)**: Dropshipping / Print-on-Demand (POD) via Printful or Printify. Low risk, zero inventory holding costs.
- **Phase 2 (Scaling)**: Bulk manufacturing, custom private label packaging, and fulfillment via Amazon FBA or local 3PL warehouse.
- **Inventory Trigger Rule**: Auto-reorder when warehouse stock level is < 20 days of average sales volume.
