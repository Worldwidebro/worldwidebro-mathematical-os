# LT-011 Financial Model Master

## 1. Monetization Map
LT-011 acts as the horizontal infrastructure layer, monetizing through multiple engines rather than a single SaaS tier:

*   **SaaS/Subscription:** Dispatch Software, Fleet Management, Customer Portal (MRR)
*   **Transactional:** Per-dispatch fee, Per-trip fee, Proof-of-delivery (Usage)
*   **Managed Services:** Managed dispatch, Dispatch BPO (Monthly retainer + Job fee)
*   **Premium Services:** After-hours dispatch, Emergency routing (Premium margin)
*   **Infrastructure:** API access, Integrations (Enterprise contracts)

## 2. Unit Economics & Intelligence
*   **Capacity constraint:** How many dispatch transactions and fleets can the infrastructure support before requiring additional cloud/support OpEx?
*   **Target Metrics:** Revenue per transaction, Revenue per fleet, Contribution margin per API call.

## 3. Financial Flow
**Gross Revenue → COGS → Gross Profit → OpEx → EBITDA → Cash Flow**
*   **COGS:** Server/infrastructure (Vercel, OSRM), Maps/GPS API, SMS/Voice (Twilio), Payment processing (Stripe).
*   **OpEx:** Engineering, Sales, Support, Administration.
