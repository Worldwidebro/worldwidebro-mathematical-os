# STAFFING (STA) Industry Playbook

## Core Mission
Be the primary labor engine for the entire Worldwidebro network. We capture margin by sourcing, vetting, and deploying talent faster and cheaper than external agencies.

## Who We Need (Inputs)
- **CONSTRUCTION**: Provides project scopes and contractor role requirements.
- **REAL ESTATE**: Provides property manager and maintenance technician roles.
- **HOSPITALITY/HEALTHCARE**: Provides high-volume, short-term staffing needs.
- **OPS**: Provides payroll processing and compliance legal templates.

## Who We Serve (Outputs)
- **ALL SECTORS**: We supply vetted, insured, compliant labor to any venture that generates a `labor_sourcing` delegation request.

## Delegation Handoff Rules
1. **Receive Request**: CON/RE/HOSP posts role → STA receives via `/network/opportunities`.
2. **Vet (SLA < 24h)**: Run automated license (NCLBGC), insurance, and background checks.
3. **Deploy (SLA < 48h)**: Assign contractor, generate work order.
4. **Invoice**: Bill requesting venture at **30-40% markup** on base labor rate.
5. **Log**: Record `margin_captured` in Neo4j, create `transaction` in Supabase.

## KPI Targets
- Placement Velocity: < 48 hours
- Gross Margin: > 35%
- Compliance Pass Rate: 100%

---

## Operational Workflows
All venture onboarding and marketing operations must align with the [Standardized Operational Framework](file:///Users/acebless/Documents/Gemini/business-os/STANDARDIZED-OPERATIONAL-FRAMEWORK.md):
- **Recruiter Onboarding Checklist**: [Staffing Onboarding Framework](file:///Users/acebless/Documents/Gemini/business-os/STANDARDIZED-OPERATIONAL-FRAMEWORK.md#d-staffing-agency-sta-001)
- **Customer Sourcing & Sales**: [Staffing Sourcing Campaign](file:///Users/acebless/Documents/Gemini/business-os/STANDARDIZED-OPERATIONAL-FRAMEWORK.md#customer-acquisition-campaign-3)
- **AI Automation Team**: Managed by the [Venture AI Agent Matrix](file:///Users/acebless/Documents/Gemini/business-os/STANDARDIZED-OPERATIONAL-FRAMEWORK.md#4-venture-ai-agent-matrix)
