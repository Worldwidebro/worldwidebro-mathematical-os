# Website Architecture

This document defines the sitemap, directory structures, and data sources for the consolidated corporate portal of **Worldwidebro Holdings**.

---

## 1. Core Holding Company (5 Pages)
1. **Home**: Thesis of the delegation network, live system statistics ticker, and CTAs.
2. **About / Mission**: Explanation of the 712 ventures, AI-native automation model, and the Mecklenburg County hub.
3. **The OS (Technology)**: Deep-dive into LiteLLM, Neo4j Graph queries, Qdrant vectors, and the vex dashboard.
4. **Portfolio / Ventures**: Dynamic grid of all active portfolio ventures.
5. **Contact / Partner with Us**: Business lead-capture forms.

---

## 2. Sector Landing Pages (38 Pages)
Each page details the sector's specific playbook, inputs/outputs, and active ventures:
- Staffing
- Construction
- Real Estate
- Financial
- Operations
- Technology
- Hospitality
- Healthcare
- Education
- Media
- Investment
- **Commerce**
- Beauty & Wellness
- Transportation
- **Funding** *(Added)*
- **Community / Non-Profit** *(Added)*

---

## 3. Dynamic Venture Template (1 Template + Live Instances)
- **Venture Template**: Renders dynamic metrics directly from Supabase and Neo4j based on URL parameter (e.g. `/ventures/con-001`):
  *   Venture Name & Metadata
  *   Current Operational Phase
  *   Staging URL & Live KPIs (gross revenue, margin, uptime)
  *   "Request Service" / "Partner with Us" CTA.

---

## 4. Investor & Partner Hub (7 Pages)
- **For Investors**: Treasury reporting, ROI metrics, carry allocation logic.
- **For Partners**: Vendor application forms.
- **For Talent**: Contractor registration portal.
- **Careers**: Active postings for human-in-the-loop and prompt engineers.
- **Impact / ESG**: Social capital highlights from the Community sector.
- **Grants & Incentives**: Application and tracking for Funding opportunities.
- **Workforce Development**: Recruitment tracking for Staffing programs.

---

## 5. Legal & Compliance (4 Pages)
- **Privacy Policy**: Legal compliance guidelines.
- **Terms of Service**: Standard commercial agreements.
- **Security & Data Governance**: Verification checklists for client data trust.
- **Contractor Portal**: Contractor Agreements and NDAs.

---

## 6. Resources & Insights (2 Pages)
- **Insights / Blog**: Case studies on delegation efficiencies.
- **Press / Releases**: Official updates and announcements.
