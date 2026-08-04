# RealEstateOS Project Specification & Architecture

## System Architecture Overview
RealEstateOS is a platform-scale monorepo system for end-to-end real estate management, asset acquisition, loan origination, property management, syndication, and AI agent automation.

## 35 Monorepo Services Scaffold Layout (Section 11 PRD)
The monorepo architecture spans 35 service & package directories:
1. `services/identity-service` — Auth, User RBAC & JWT issuance
2. `services/organization-service` — Multi-tenant organization contexts
3. `services/property-service` — Property & unit CRUD, asset tracking
4. `services/listing-service` — MLS integration & listing management
5. `services/crm-service` — Investor & buyer CRM, lead pipeline
6. `services/underwriting-service` — Deal financial modeling, cap rates, cash flow
7. `services/valuation-service` — Automated Valuation Model (AVM) & comp analysis
8. `services/mortgage-service` — Loan application & origination engine
9. `services/closing-service` — Escrow, title search, and deal closing
10. `services/lease-service` — E-signature & lease contract generation
11. `services/tenant-service` — Tenant portal, screening & communications
12. `services/rent-collection-service` — Stripe/ACH payment ledger & auto-reminders
13. `services/maintenance-service` — Work orders, contractor triage & dispatch
14. `services/asset-management-service` — NOI optimization, capex & portfolio analytics
15. `services/syndication-service` — Investor portal, equity raising & distributions
16. `services/document-service` — Document storage, OCR parsing & file vault
17. `services/notification-service` — SMS, email & push notification gateway
18. `services/analytics-service` — Business intelligence & executive metrics
19. `services/market-intelligence-service` — Rent estimates & market macro trends
20. `services/inspection-service` — Property condition reports & audit parsing
21. `services/disposition-service` — Asset liquidation & sales channel
22. `services/tax-service` — Property tax appeals & assessment deductions
23. `services/insurance-service` — Risk scoring, policy tracking & claims
24. `services/utility-management-service` — Metering & utility invoice parsing
25. `services/vendor-service` — Contractor network & compliance verification
26. `services/marketing-automation-service` — Campaign management & property flyers
27. `services/e-signature-service` — Digital signature integration stub
28. `services/audit-logging-service` — Activity audit trails & compliance log
29. `services/spatial-service` — GIS, mapping & zoning data analysis
30. `services/construction-service` — Rehab project management & budgeting
31. `services/portfolio-optimization-service` — Yield maximization & balance sheet rebalancing
32. `services/investor-relations-service` — K-1 distribution & waterfall calculations
33. `services/accounting-service` — Double-entry general ledger
34. `services/ai-gateway-service` — LLM execution proxy & agent state manager
35. `apps/api` — Central API Gateway Ingress Controller

## 20 AI Agents Registry (Section 6 PRD)
1. `AcquisitionAgent` — Off-market deal sourcing & web scraping
2. `UnderwritingAgent` — Automated financial modeling & NOI pro-forma
3. `ValuationAgent` — AVM & comparative market analysis
4. `LeadNurtureAgent` — CRM lead qualification & automated outreach
5. `ListingOptimizerAgent` — Listing description generation & media tagging
6. `TenantScreeningAgent` — Credit/background check & verification scoring
7. `LeaseGeneratorAgent` — Contract assembly & custom clause synthesis
8. `RentCollectionAgent` — Payment reminder automation & fee reconciliation
9. `MaintenanceAgent` — Work order triage & emergency routing
10. `VendorDispatchAgent` — Contractor bidding & dispatch management
11. `MortgageUnderwriterAgent` — DTI calculation & pre-approval scoring
12. `TitleEscrowAgent` — Title search verification & lien checking
13. `AssetManagerAgent` — NOI tracking & capex plan optimization
14. `InvestorRelationsAgent` — Distribution waterfall calculation & quarterly updates
15. `InspectionAnalyzerAgent` — Inspection report OCR & repair cost estimation
16. `MarketIntelligenceAgent` — Cap rate trend forecasting & market rent estimation
17. `PropertyTaxAgent` — Assessment appeal evaluation & tax optimization
18. `InsuranceUnderwriterAgent` — Risk scoring & insurance coverage estimation
19. `UtilityAuditAgent` — Utility bill anomaly detection & energy audit
20. `DispositionAgent` — Exit timing analysis & buyer matching

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Monorepo Scaffold | Create 35 service directories with package.json, tsconfig.json & workspace linkage | None | DONE |
| 2 | Shared Types Models | Expand packages/shared-types with user, org, property, listing, loan, agent log models | M1 | DONE |
| 3 | AI Agent Registry | Implement AI agent registry with 20 AI agents & mock execution engine | M2 | DONE |
| 4 | Central API Gateway | Enhance apps/api ingress controller to expose /api/agents and mock service routing | M3 | DONE |
| 5 | Build & E2E Verification | Ensure npm run build passes, GET /api/agents works, POST /api/agents/:name/invoke works, Forensic Audit clean | M4 | DONE |


## Interface Contracts
- GET `/api/agents` -> Returns `200 OK` with list of 20 AI Agents (`AgentMetadata[]`)
- POST `/api/agents/:agentName/invoke` -> Accepts JSON payload, returns `200 OK` with `{ success: true, agentName: string, logs: AgentExecutionLog[], output: Record<string, any> }`
- GET `/api/<service-name>/*` -> Proxies or returns core mock service response with valid JSON data

## Code Layout
- `apps/api/src/index.ts` — API Gateway main entrypoint
- `apps/api/src/routes/agents.ts` — AI Agent endpoints
- `apps/api/src/routes/services.ts` — Core service mock endpoints
- `packages/shared-types/src/index.ts` — Shared TypeScript data models
- `services/*` — 34 domain microservices
