# Revenue Analytics: ROI & Attribution Modeling

This document defines the metrics, mathematical models, and database schemas used to track financial performance and allocate marketing capital.

---

## 1. Core Financial Metrics

We optimize for the following metrics across all commerce channels:

### A. Customer Acquisition Cost (CAC)
- **Formula**:
  \[\text{CAC} = \frac{\text{Total Media Generation & Editing Cost} + \text{Paid Ad Spend}}{\text{Total New Customers acquired}}\]

### B. Customer Lifetime Value (LTV)
- **Formula**:
  \[\text{LTV} = \text{Average Order Value} \times \text{Purchase Frequency} \times \text{Customer Lifespan}\]
- **Target Ratio**: $\text{LTV}:\text{CAC} > 3:1$

### C. Return on Media Spend (ROMS)
- **Formula**:
  \[\text{ROMS} = \frac{\text{Organic & Affiliate Revenue}}{\text{Total Production Cost}}\]
- **Target ROMS**: > 5x (Due to low cost of organic short-form production)

---

## 2. Multi-Touch Attribution Model

To understand which content drives sales, our analytics script uses a **Position-Based (U-Shaped) Attribution Model**:
- **First Touch (40% credit)**: The initial TikTok/Shorts video that introduced the user to Worldwidebro.
- **Middle Touches (20% credit)**: The newsletter issues or community posts the user engaged with.
- **Last Touch (40% credit)**: The specific email or checkout-page link that completed the sale.

This allocation helps identify high-performing hook concepts (First Touch) and high-converting offers (Last Touch).
