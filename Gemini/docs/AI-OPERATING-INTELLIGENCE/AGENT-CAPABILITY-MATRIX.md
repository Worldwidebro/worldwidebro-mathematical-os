# Agent Capability Matrix

This document maps all agents in the holdings network to the core capabilities they implement.

---

## 1. Capabilities Mapping Table

| Agent Name | Sector | Core Capability | Associated Repository |
| :--- | :--- | :--- | :--- |
| **network-operations** | Holding | Queue balancing, spawner routes | `Fractal`, `OmniRoute` |
| **capital-allocation** | Holding | Treasury rebalancing | `PyPortfolioOpt` |
| **performance-analytics** | Holding | Performance audits | `Langfuse`, `Metabase` |
| **sourcing-agent** | Staffing | LinkedIn/CV scraping | `Apollo.io`, `HubSpot` |
| **vetting-agent** | Staffing | Background & license check | `Checkr`, `NCLBGC` |
| **placement-agent** | Staffing | Shift scheduling & invoicing | `QuickBooks`, `Twilio` |
| **project-manager** | Construction | Milestone & labor routing | `Procore`, `HubSpot` |
| **estimation-agent** | Construction | Quantity takeoffs & SOWs | `PlanSwift`, `RSMeans` |
| **compliance-agent** | Construction | Permits and licensing | `LUESA`, `OSHA` |
| **acquisition-agent** | Real Estate | Comps & cap rate analysis | `CoStar`, `DocuSign` |
| **property-management** | Real Estate | Lease coordination, maintenance | `AppFolio`, `Stripe` |
| **deal-sourcing** | Real Estate | Refinancing audits | `CoStar`, `Excel` |
| **deal-structuring** | Financial | SPV setups & debt sheets | `Supabase`, `DocuSign` |
| **underwriting** | Financial | Risk score DCF/IRR | `PyPortfolioOpt` |
| **legal** | Operations | Contract generators, review | `DocuSign`, `Westlaw` |
| **accounting** | Operations | Invoices, bookkeeping | `QuickBooks`, `Gusto` |
| **hr** | Operations | Recruiter posts, payroll | `Greenhouse`, `BambooHR` |

---

## 2. Dynamic Discovery
Specialist agents query the Neo4j database using the `:USES` relationship edge to identify which skill fits a given task, ensuring self-healing execution pathways.
