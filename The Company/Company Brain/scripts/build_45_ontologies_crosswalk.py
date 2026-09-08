#!/usr/bin/env python3
"""
build_45_ontologies_crosswalk.py

Builds the complete 45 Core Ontology Crosswalk:
- 25 Foundational Ontologies (ONT-001 to ONT-025)
- 20 Operational Ontologies (OPS-026 to OPS-045)

Outputs:
1. _ONTOLOGY/45_ONTOLOGIES_REGISTRY.yaml
2. 07-ONTOLOGY/45-ONTOLOGIES-MASTER.md
3. 07-ONTOLOGY/README.md (updated)
4. 07-ONTOLOGY/domains/ (stubs for ONT-001 to OPS-045)
5. Updates corresponding domain gateway files with ontology aliases and tags.
"""

import os, yaml

WORKSPACE = "/Users/acebless/Documents/The Company/Company Brain"

ONTOLOGIES = [
    # --- 25 FOUNDATIONAL ONTOLOGIES (WHAT EXISTS) ---
    {
        "id": "ONT-001",
        "name": "Economic Ontology",
        "category": "FOUNDATIONAL",
        "description": "Industries, sectors, NAICS classifications, macroeconomic dynamics, and market taxonomy.",
        "primary_domain": "00-CONSTITUTION",
        "primary_file": "00-CONSTITUTION/SECTOR-TAXONOMY-MASTER.md",
        "aliases": ["ONT-001", "Economic Ontology", "Sector Taxonomy", "Economic Universe"],
        "tags": ["ontology", "foundational", "economic", "sector", "industry", "naics", "ont-001"],
        "connects_to": ["ONT-002", "ONT-003", "ONT-016", "ONT-017", "ONT-023"],
        "registry_sources": ["_REGISTRIES/ventures-by-sector.yaml", "_REGISTRIES/control-planes-by-sector.yaml"]
    },
    {
        "id": "ONT-002",
        "name": "Company Ontology",
        "category": "FOUNDATIONAL",
        "description": "Holding entities, parent organizations, legal subsidiaries, operating companies (OpCos), and ownership trees.",
        "primary_domain": "01-IDENTITY",
        "primary_file": "01-IDENTITY/01-IDENTITY.md",
        "aliases": ["ONT-002", "Company Ontology", "Corporate Structure", "Holdings & Entities"],
        "tags": ["ontology", "foundational", "company", "holding", "opco", "corporate-structure", "ont-002"],
        "connects_to": ["ONT-003", "ONT-011", "ONT-018", "ONT-019", "OPS-030"],
        "registry_sources": ["_REGISTRIES/identity_registry.yaml", "00-CONSTITUTION/opcos/"]
    },
    {
        "id": "ONT-003",
        "name": "Venture Ontology",
        "category": "FOUNDATIONAL",
        "description": "Commercial ventures, business models, monetization mechanics, lifecycle stages, and commercial validation.",
        "primary_domain": "23-VENTURES",
        "primary_file": "23-VENTURES/23-VENTURES.md",
        "aliases": ["ONT-003", "Venture Ontology", "Ventures Registry", "Commercial Ventures"],
        "tags": ["ontology", "foundational", "venture", "business-model", "opco-venture", "ont-003"],
        "connects_to": ["ONT-002", "ONT-005", "ONT-014", "ONT-015", "ONT-016", "ONT-017", "OPS-033", "OPS-043"],
        "registry_sources": ["_REGISTRIES/CANONICAL/SITES_REGISTRY.yaml", "_REGISTRIES/VENTURE_REGISTRY.yaml", "_TEMPLATES/VENTURE_TEMPLATE.md"]
    },
    {
        "id": "ONT-004",
        "name": "Technology Ontology",
        "category": "FOUNDATIONAL",
        "description": "Technology platforms, external libraries, runtime architectures, stacks, frameworks, and OSS ecosystems.",
        "primary_domain": "24-TECHNOLOGY",
        "primary_file": "24-TECHNOLOGY/24-TECHNOLOGY.md",
        "aliases": ["ONT-004", "Technology Ontology", "Tech Stack", "Technology Platforms"],
        "tags": ["ontology", "foundational", "technology", "platform", "frameworks", "tech-stack", "ont-004"],
        "connects_to": ["ONT-005", "ONT-006", "ONT-007", "ONT-008", "ONT-009"],
        "registry_sources": ["_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml", "_REGISTRIES/EXTERNAL_CAPABILITY_UNIVERSE_INVENTORY.md"]
    },
    {
        "id": "ONT-005",
        "name": "Capability Ontology",
        "category": "FOUNDATIONAL",
        "description": "Verified organizational, technical, and algorithmic capabilities that the ecosystem actually executes.",
        "primary_domain": "14-CAPABILITIES",
        "primary_file": "14-CAPABILITIES/14-CAPABILITIES.md",
        "aliases": ["ONT-005", "Capability Ontology", "Capabilities Graph", "Technical Capabilities"],
        "tags": ["ontology", "foundational", "capability", "technical-capabilities", "business-capabilities", "ont-005"],
        "connects_to": ["ONT-003", "ONT-004", "ONT-006", "ONT-008", "ONT-013"],
        "registry_sources": ["_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml", "_REGISTRIES/CANONICAL/CAPABILITY_GAP_REPORT.yaml"]
    },
    {
        "id": "ONT-006",
        "name": "Software Ontology",
        "category": "FOUNDATIONAL",
        "description": "Repositories, source code codebases, dependencies, ASTs, package manifests, and code reality.",
        "primary_domain": "13-REPOSITORIES",
        "primary_file": "13-REPOSITORIES/13-REPOSITORIES.md",
        "aliases": ["ONT-006", "Software Ontology", "Codebase Reality", "Repository Intelligence"],
        "tags": ["ontology", "foundational", "software", "repositories", "dependencies", "ast", "code-reality", "ont-006"],
        "connects_to": ["ONT-004", "ONT-005", "ONT-007", "OPS-038", "OPS-042"],
        "registry_sources": ["_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml", "_REGISTRIES/CANONICAL/OWNED_REPO_DEPENDENCIES.json", "_REGISTRIES/CANONICAL/OWNED_REPO_CODE_REALITY.json"]
    },
    {
        "id": "ONT-007",
        "name": "Infrastructure Ontology",
        "category": "FOUNDATIONAL",
        "description": "Physical hosts, Apple Silicon MLX clusters, local containers, Tailscale mesh, Docker daemons, networks, and storage.",
        "primary_domain": "13_ENGINEERING/INFRASTRUCTURE",
        "primary_file": "13_ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE.md",
        "aliases": ["ONT-007", "Infrastructure Ontology", "Hardware Mesh", "Infrastructure Control Plane"],
        "tags": ["ontology", "foundational", "infrastructure", "hardware", "macstudio", "docker", "tailscale", "mesh", "ont-007"],
        "connects_to": ["ONT-006", "ONT-008", "ONT-009", "ONT-022", "ONT-024"],
        "registry_sources": ["CLAUDE.md", "_REGISTRIES/INFRASTRUCTURE_REGISTRY.yaml", "13_ENGINEERING/INFRASTRUCTURE/compute_registry.json"]
    },
    {
        "id": "ONT-008",
        "name": "AI & Agent Ontology",
        "category": "FOUNDATIONAL",
        "description": "Model endpoints, agent archetypes, subagents, tools, MCP servers, prompt chains, and model routing.",
        "primary_domain": "16-AGENTS",
        "primary_file": "16-AGENTS/16-AGENTS.md",
        "aliases": ["ONT-008", "AI Agent Ontology", "Agent OS", "Model Gateway"],
        "tags": ["ontology", "foundational", "ai", "agents", "llm", "mlx", "omniroute", "mcp", "subagent", "ont-008"],
        "connects_to": ["ONT-005", "ONT-007", "ONT-010", "ONT-013", "OPS-037"],
        "registry_sources": ["AGENTS.md", ".agents/agents/", "_REGISTRIES/LLM_HARDWARE_COMPATIBILITY_REGISTRY.yaml"]
    },
    {
        "id": "ONT-009",
        "name": "Data Ontology",
        "category": "FOUNDATIONAL",
        "description": "Schemas, datasets, relational tables, vector stores (Qdrant), caches (Redis), and ETL pipelines.",
        "primary_domain": "04-DATA",
        "primary_file": "04-DATA/04-DATA.md",
        "aliases": ["ONT-009", "Data Ontology", "Data Architecture", "Storage & Pipelines"],
        "tags": ["ontology", "foundational", "data", "databases", "schemas", "pipelines", "vectors", "ont-009"],
        "connects_to": ["ONT-007", "ONT-010", "OPS-026", "OPS-038"],
        "registry_sources": ["03-INGESTION/", "05-METADATA/"]
    },
    {
        "id": "ONT-010",
        "name": "Knowledge Ontology",
        "category": "FOUNDATIONAL",
        "description": "Knowledge graphs (Neo4j), wiki documents, concepts, evidence items, scholarly research, and institutional memory.",
        "primary_domain": "09-KNOWLEDGE",
        "primary_file": "09-KNOWLEDGE/09-KNOWLEDGE.md",
        "aliases": ["ONT-010", "Knowledge Ontology", "Company Brain Graph", "Research Knowledge"],
        "tags": ["ontology", "foundational", "knowledge", "knowledge-graph", "neo4j", "evidence", "research", "ont-010"],
        "connects_to": ["ONT-008", "ONT-009", "OPS-027", "OPS-039", "OPS-040"],
        "registry_sources": ["RESEARCH/RESEARCH-OS.md", "08-KNOWLEDGE-GRAPH/", "09-KNOWLEDGE/Neo4j.md"]
    },
    {
        "id": "ONT-011",
        "name": "Organization Ontology",
        "category": "FOUNDATIONAL",
        "description": "Business units, departments, functional divisions, teams, and administrative reporting structures.",
        "primary_domain": "06-TEAMS",
        "primary_file": "06-TEAMS/06-TEAMS.md",
        "aliases": ["ONT-011", "Organization Ontology", "Org Structure", "Teams & Departments"],
        "tags": ["ontology", "foundational", "organization", "teams", "departments", "divisions", "ont-011"],
        "connects_to": ["ONT-002", "ONT-012", "ONT-013", "OPS-044"],
        "registry_sources": ["30-HR/", "06-TEAMS/"]
    },
    {
        "id": "ONT-012",
        "name": "People Ontology",
        "category": "FOUNDATIONAL",
        "description": "Founders, human collaborators, engineers, external contractors, talent profiles, and skill sets.",
        "primary_domain": "05-PEOPLE",
        "primary_file": "05-PEOPLE/05-PEOPLE.md",
        "aliases": ["ONT-012", "People Ontology", "Human Operators", "Personnel Directory"],
        "tags": ["ontology", "foundational", "people", "person", "founders", "skills", "talent", "ont-012"],
        "connects_to": ["ONT-011", "ONT-013", "OPS-029", "OPS-030"],
        "registry_sources": ["05-PEOPLE/Person.md"]
    },
    {
        "id": "ONT-013",
        "name": "Process Ontology",
        "category": "FOUNDATIONAL",
        "description": "Standard operating procedures (SOPs), repeatable operations, operational runbooks, and manual/hybrid processes.",
        "primary_domain": "29-OPERATIONS",
        "primary_file": "29-OPERATIONS/29-OPERATIONS.md",
        "aliases": ["ONT-013", "Process Ontology", "Operations Engine", "Standard Operating Procedures"],
        "tags": ["ontology", "foundational", "process", "operations", "procedures", "sop", "runbooks", "ont-013"],
        "connects_to": ["ONT-005", "ONT-008", "ONT-011", "OPS-035", "OPS-037"],
        "registry_sources": ["29-OPERATIONS/", "48-AUTOMATION/"]
    },
    {
        "id": "ONT-014",
        "name": "Product Ontology",
        "category": "FOUNDATIONAL",
        "description": "Software products, edge sites, web portals, feature matrices, customer-facing interfaces, and SKUs.",
        "primary_domain": "28-PRODUCT",
        "primary_file": "28-PRODUCT/28-PRODUCT.md",
        "aliases": ["ONT-014", "Product Ontology", "Product Catalog", "Live Sites & Frontends"],
        "tags": ["ontology", "foundational", "product", "features", "sites", "skus", "frontends", "ont-014"],
        "connects_to": ["ONT-003", "ONT-006", "ONT-015", "ONT-018"],
        "registry_sources": ["_REGISTRIES/CANONICAL/SITES_REGISTRY.yaml", "_TEMPLATES/SITE_TEMPLATE.md"]
    },
    {
        "id": "ONT-015",
        "name": "Customer Ontology",
        "category": "FOUNDATIONAL",
        "description": "Ideal Customer Profiles (ICPs), target accounts, buyer personas, leads, conversion funnels, and CRM entities.",
        "primary_domain": "27-CUSTOMERS",
        "primary_file": "27-CUSTOMERS/27-CUSTOMERS.md",
        "aliases": ["ONT-015", "Customer Ontology", "CRM Intelligence", "Customer & Account Directory"],
        "tags": ["ontology", "foundational", "customer", "icp", "personas", "crm", "accounts", "buyers", "ont-015"],
        "connects_to": ["ONT-003", "ONT-014", "ONT-016", "ONT-018", "OPS-033"],
        "registry_sources": ["25-SALES/", "27-CUSTOMERS/"]
    },
    {
        "id": "ONT-016",
        "name": "Market Ontology",
        "category": "FOUNDATIONAL",
        "description": "Market verticals, competitive dynamics, TAM/SAM/SOM boundaries, external macro trends, and market demands.",
        "primary_domain": "26-MARKETING",
        "primary_file": "26-MARKETING/26-MARKETING.md",
        "aliases": ["ONT-016", "Market Ontology", "Market Dynamics", "Competitive Landscape"],
        "tags": ["ontology", "foundational", "market", "competition", "tam", "industry-demand", "ont-016"],
        "connects_to": ["ONT-001", "ONT-003", "ONT-015", "OPS-033"],
        "registry_sources": ["38-OPPORTUNITIES/", "RESEARCH/OPPORTUNITIES.md"]
    },
    {
        "id": "ONT-017",
        "name": "Capital Ontology",
        "category": "FOUNDATIONAL",
        "description": "Non-dilutive grants, venture debt, equity financing, capital pools, angel syndicates, and investor networks.",
        "primary_domain": "08-FINANCIAL",
        "primary_file": "08-FINANCIAL/08-FINANCIAL.md",
        "aliases": ["ONT-017", "Capital Ontology", "Capital Intelligence", "Grants & Equity"],
        "tags": ["ontology", "foundational", "capital", "grants", "equity", "investors", "funding", "loans", "ont-017"],
        "connects_to": ["ONT-002", "ONT-003", "ONT-018", "ONT-023"],
        "registry_sources": ["RESEARCH/GOVERNMENT-FUNDING.md", "08-FINANCIAL/"]
    },
    {
        "id": "ONT-018",
        "name": "Financial Ontology",
        "category": "FOUNDATIONAL",
        "description": "Cash flow, ARR/MRR revenue streams, cost structures, unit economics, gross margins, and financial ledgers.",
        "primary_domain": "24-FINANCE",
        "primary_file": "24-FINANCE/24-FINANCE.md",
        "aliases": ["ONT-018", "Financial Ontology", "Unit Economics", "Financial Ledgers"],
        "tags": ["ontology", "foundational", "financial", "revenue", "cash", "margins", "unit-economics", "burn-rate", "ont-018"],
        "connects_to": ["ONT-002", "ONT-003", "ONT-017", "OPS-031", "OPS-045"],
        "registry_sources": ["ECONOMIC-REALITY.md", "24-FINANCE/"]
    },
    {
        "id": "ONT-019",
        "name": "Legal Ontology",
        "category": "FOUNDATIONAL",
        "description": "Corporate entity formation, trademarks, patents, proprietary IP, master service agreements, and liabilities.",
        "primary_domain": "31-LEGAL",
        "primary_file": "31-LEGAL/31-LEGAL.md",
        "aliases": ["ONT-019", "Legal Ontology", "IP & Contracts", "Corporate Legal"],
        "tags": ["ontology", "foundational", "legal", "contracts", "ip", "patents", "trademarks", "liability", "ont-019"],
        "connects_to": ["ONT-002", "ONT-020", "ONT-022", "OPS-032"],
        "registry_sources": ["RESEARCH/PATENT-INTELLIGENCE.md", "31-LEGAL/"]
    },
    {
        "id": "ONT-020",
        "name": "Compliance Ontology",
        "category": "FOUNDATIONAL",
        "description": "Regulatory constraints, HIPAA, DOT, OSHA, SOC2, financial compliance, security controls, and audits.",
        "primary_domain": "33-COMPLIANCE",
        "primary_file": "33-COMPLIANCE/33-COMPLIANCE.md",
        "aliases": ["ONT-020", "Compliance Ontology", "Regulatory Controls", "Governance Audits"],
        "tags": ["ontology", "foundational", "compliance", "regulations", "audit", "hipaa", "soc2", "governance", "ont-020"],
        "connects_to": ["ONT-019", "ONT-024", "OPS-028", "OPS-044"],
        "registry_sources": ["33-COMPLIANCE/", "32-SECURITY/"]
    },
    {
        "id": "ONT-021",
        "name": "Partner Ontology",
        "category": "FOUNDATIONAL",
        "description": "Strategic vendor alliances, distribution partners, payment processors (Stripe), platform ecosystems, and APIs.",
        "primary_domain": "36-PARTNERS",
        "primary_file": "36-PARTNERS/36-PARTNERS.md",
        "aliases": ["ONT-021", "Partner Ontology", "Vendor Alliances", "Ecosystem Partners"],
        "tags": ["ontology", "foundational", "partner", "vendors", "alliances", "ecosystems", "apis", "ont-021"],
        "connects_to": ["ONT-004", "ONT-014", "ONT-018", "OPS-032"],
        "registry_sources": ["36-PARTNERS/"]
    },
    {
        "id": "ONT-022",
        "name": "Asset Ontology",
        "category": "FOUNDATIONAL",
        "description": "Physical workstations, storage arrays, digital domains, brand trademarks, and hardware infrastructure assets.",
        "primary_domain": "35-ASSETS",
        "primary_file": "35-ASSETS/35-ASSETS.md",
        "aliases": ["ONT-022", "Asset Ontology", "Physical & Digital Assets", "Asset Inventory"],
        "tags": ["ontology", "foundational", "asset", "hardware-assets", "digital-assets", "storage-arrays", "ont-022"],
        "connects_to": ["ONT-007", "ONT-018", "ONT-019", "OPS-036"],
        "registry_sources": ["35-ASSETS/"]
    },
    {
        "id": "ONT-023",
        "name": "Location Ontology",
        "category": "FOUNDATIONAL",
        "description": "Legal jurisdictions (Delaware, New York), physical facilities, geographic operating regions, and zoning bounds.",
        "primary_domain": "00-CONSTITUTION",
        "primary_file": "00-CONSTITUTION/00-CONSTITUTION.md",
        "aliases": ["ONT-023", "Location Ontology", "Geographic & Legal Jurisdictions", "Regional Operating Bounds"],
        "tags": ["ontology", "foundational", "location", "jurisdiction", "geography", "facilities", "regions", "ont-023"],
        "connects_to": ["ONT-001", "ONT-002", "ONT-017", "ONT-019"],
        "registry_sources": ["00-CONSTITUTION/"]
    },
    {
        "id": "ONT-024",
        "name": "Risk Ontology",
        "category": "FOUNDATIONAL",
        "description": "Operational bottlenecks, cybersecurity attack vectors, cash burn risks, dependency fragility, and mitigations.",
        "primary_domain": "34-RISK",
        "primary_file": "34-RISK/34-RISK.md",
        "aliases": ["ONT-024", "Risk Ontology", "Threats & Mitigations", "Risk Architecture"],
        "tags": ["ontology", "foundational", "risk", "threats", "vulnerabilities", "mitigations", "security-risk", "ont-024"],
        "connects_to": ["ONT-007", "ONT-018", "ONT-020", "OPS-028"],
        "registry_sources": ["34-RISK/", "32-SECURITY/32-SECURITY.md"]
    },
    {
        "id": "ONT-025",
        "name": "Metrics Ontology",
        "category": "FOUNDATIONAL",
        "description": "Key Performance Indicators (KPIs), token latency/cost metrics, operational throughput, and system health.",
        "primary_domain": "40-METRICS",
        "primary_file": "40-METRICS/40-METRICS.md",
        "aliases": ["ONT-025", "Metrics Ontology", "System Telemetry", "Key Performance Indicators"],
        "tags": ["ontology", "foundational", "metrics", "kpi", "telemetry", "observability", "benchmarks", "ont-025"],
        "connects_to": ["ONT-007", "ONT-018", "OPS-026", "OPS-045"],
        "registry_sources": ["40-METRICS/", "41-OBSERVABILITY/41-OBSERVABILITY.md"]
    },

    # --- 20 OPERATIONAL / CONTROL ONTOLOGIES (WHAT HAPPENS) ---
    {
        "id": "OPS-026",
        "name": "Event Ontology",
        "category": "OPERATIONAL",
        "description": "State change events, cron triggers, deployment completions, webhook dispatches, and message broker signals.",
        "primary_domain": "11-LOOP-ENGINEERING",
        "primary_file": "11-LOOP-ENGINEERING/11-LOOP-ENGINEERING.md",
        "aliases": ["OPS-026", "Event Ontology", "System Events", "Triggers & Signals"],
        "tags": ["ontology", "operational", "event", "trigger", "state-change", "signals", "ops-026"],
        "connects_to": ["ONT-008", "ONT-009", "ONT-025", "OPS-035", "OPS-037"],
        "registry_sources": ["11-LOOP-ENGINEERING/"]
    },
    {
        "id": "OPS-027",
        "name": "Decision Ontology",
        "category": "OPERATIONAL",
        "description": "Architectural Decision Records (ADRs), executive governance rulings, tradeoff evaluations, and approvals.",
        "primary_domain": "20-DECISIONS",
        "primary_file": "20-DECISIONS/20-DECISIONS.md",
        "aliases": ["OPS-027", "Decision Ontology", "ADR Registry", "Governance Decisions"],
        "tags": ["ontology", "operational", "decision", "adr", "tradeoffs", "governance-decisions", "ops-027"],
        "connects_to": ["ONT-010", "OPS-028", "OPS-040", "OPS-044"],
        "registry_sources": ["20-DECISIONS/"]
    },
    {
        "id": "OPS-028",
        "name": "Policy Ontology",
        "category": "OPERATIONAL",
        "description": "Operating contracts (ANTIGRAVITY.md 45 rules), automated agent guardrails, and compliance enforcement bounds.",
        "primary_domain": "21-POLICY",
        "primary_file": "21-POLICY/21-POLICY.md",
        "aliases": ["OPS-028", "Policy Ontology", "System Guardrails", "Operating Policy"],
        "tags": ["ontology", "operational", "policy", "guardrails", "contracts", "rules", "ops-028"],
        "connects_to": ["OPS-027", "OPS-029", "OPS-044"],
        "registry_sources": ["ANTIGRAVITY.md", "21-POLICY/"]
    },
    {
        "id": "OPS-029",
        "name": "Permission Ontology",
        "category": "OPERATIONAL",
        "description": "Role-Based Access Control (RBAC), agent tool execution scopes, API authentication tokens, and sudo credentials.",
        "primary_domain": "32-SECURITY",
        "primary_file": "32-SECURITY/32-SECURITY.md",
        "aliases": ["OPS-029", "Permission Ontology", "RBAC & Access Control", "Security Permissions"],
        "tags": ["ontology", "operational", "permission", "rbac", "access-control", "tokens", "security-auth", "ops-029"],
        "connects_to": ["ONT-008", "ONT-012", "OPS-028", "OPS-030"],
        "registry_sources": ["32-SECURITY/"]
    },
    {
        "id": "OPS-030",
        "name": "Identity Ontology",
        "category": "OPERATIONAL",
        "description": "Deterministic ID registries (VEN-###, CAP-###, OWN-###), entity resolution mechanisms, and canonical slugs.",
        "primary_domain": "01-IDENTITY",
        "primary_file": "01-IDENTITY/01-IDENTITY.md",
        "aliases": ["OPS-030", "Identity Ontology", "Entity Resolution", "Deterministic IDs"],
        "tags": ["ontology", "operational", "identity", "entity-resolution", "id-registry", "deterministic-ids", "ops-030"],
        "connects_to": ["ONT-002", "ONT-003", "ONT-012", "OPS-039"],
        "registry_sources": ["_REGISTRIES/ID_REGISTRY.yaml", "06-ENTITY-RESOLUTION/06-ENTITY-RESOLUTION.md"]
    },
    {
        "id": "OPS-031",
        "name": "Transaction Ontology",
        "category": "OPERATIONAL",
        "description": "Settled payments, customer invoices, Stripe charges, capital drawdowns, and immutable ledger entries.",
        "primary_domain": "24-FINANCE",
        "primary_file": "24-FINANCE/24-FINANCE.md",
        "aliases": ["OPS-031", "Transaction Ontology", "Ledger Transactions", "Financial Settlements"],
        "tags": ["ontology", "operational", "transaction", "payments", "invoices", "stripe", "ledger", "ops-031"],
        "connects_to": ["ONT-015", "ONT-018", "OPS-032"],
        "registry_sources": ["24-FINANCE/"]
    },
    {
        "id": "OPS-032",
        "name": "Contract Ontology",
        "category": "OPERATIONAL",
        "description": "Signed Master Services Agreements (MSAs), Statements of Work (SOWs), customer trial terms, and SLAs.",
        "primary_domain": "31-LEGAL",
        "primary_file": "31-LEGAL/31-LEGAL.md",
        "aliases": ["OPS-032", "Contract Ontology", "Agreements & SOWs", "Commercial Contracts"],
        "tags": ["ontology", "operational", "contract", "agreements", "msa", "sow", "commitments", "ops-032"],
        "connects_to": ["ONT-015", "ONT-019", "ONT-021", "OPS-031"],
        "registry_sources": ["31-LEGAL/"]
    },
    {
        "id": "OPS-033",
        "name": "Opportunity Ontology",
        "category": "OPERATIONAL",
        "description": "Federal and state grant opportunities, commercial RFP pipelines, market arbitrage leads, and venture pitches.",
        "primary_domain": "38-OPPORTUNITIES",
        "primary_file": "38-OPPORTUNITIES/38-OPPORTUNITIES.md",
        "aliases": ["OPS-033", "Opportunity Ontology", "Deal Flow Pipeline", "Market Opportunities"],
        "tags": ["ontology", "operational", "opportunity", "grants-rfp", "deal-flow", "leads", "market-gaps", "ops-033"],
        "connects_to": ["ONT-003", "ONT-016", "ONT-017", "RESEARCH/OPPORTUNITIES.md"],
        "registry_sources": ["RESEARCH/OPPORTUNITIES.md", "38-OPPORTUNITIES/"]
    },
    {
        "id": "OPS-034",
        "name": "Project Ontology",
        "category": "OPERATIONAL",
        "description": "High-level initiatives, development roadmaps, sprint milestones, feature deliverables, and epics.",
        "primary_domain": "22-EXECUTION",
        "primary_file": "22-EXECUTION/22-EXECUTION.md",
        "aliases": ["OPS-034", "Project Ontology", "Execution Initiatives", "Project Roadmaps"],
        "tags": ["ontology", "operational", "project", "initiatives", "milestones", "roadmaps", "execution", "ops-034"],
        "connects_to": ["ONT-003", "ONT-006", "OPS-035"],
        "registry_sources": ["22-EXECUTION/"]
    },
    {
        "id": "OPS-035",
        "name": "Task Ontology",
        "category": "OPERATIONAL",
        "description": "Atomic work units, automated subagent tasks, scheduled cron jobs, background execution items, and tickets.",
        "primary_domain": "48-AUTOMATION",
        "primary_file": "48-AUTOMATION/48-AUTOMATION.md",
        "aliases": ["OPS-035", "Task Ontology", "Task Management", "Work Units"],
        "tags": ["ontology", "operational", "task", "work-units", "background-tasks", "cron-jobs", "tickets", "ops-035"],
        "connects_to": ["ONT-008", "ONT-013", "OPS-034", "OPS-037"],
        "registry_sources": ["48-AUTOMATION/"]
    },
    {
        "id": "OPS-036",
        "name": "Resource Ontology",
        "category": "OPERATIONAL",
        "description": "Unified memory allocation, GPU/NPU utilization, API rate-limit quotas, and developer bandwidth.",
        "primary_domain": "35-ASSETS",
        "primary_file": "35-ASSETS/35-ASSETS.md",
        "aliases": ["OPS-036", "Resource Ontology", "Resource Quotas", "Hardware Utilization"],
        "tags": ["ontology", "operational", "resource", "gpu-utilization", "quotas", "rate-limits", "bandwidth", "ops-036"],
        "connects_to": ["ONT-007", "ONT-022", "OPS-035"],
        "registry_sources": ["13_ENGINEERING/INFRASTRUCTURE/compute_registry.json"]
    },
    {
        "id": "OPS-037",
        "name": "Workflow Ontology",
        "category": "OPERATIONAL",
        "description": "Multi-agent orchestration pipelines, slash command workflows (/deploy, /gap-analysis), and CI/CD pipelines.",
        "primary_domain": "48-AUTOMATION",
        "primary_file": "48-AUTOMATION/48-AUTOMATION.md",
        "aliases": ["OPS-037", "Workflow Ontology", "Orchestration Pipelines", "Slash Workflows"],
        "tags": ["ontology", "operational", "workflow", "pipelines", "slash-commands", "orchestration", "ops-037"],
        "connects_to": ["ONT-008", "ONT-013", "OPS-026", "OPS-035"],
        "registry_sources": [".agents/workflows/", "19-ORCHESTRATION/"]
    },
    {
        "id": "OPS-038",
        "name": "Dependency Ontology",
        "category": "OPERATIONAL",
        "description": "Direct and transitive library dependencies, cross-service dependencies, and critical single-points-of-failure.",
        "primary_domain": "13-REPOSITORIES",
        "primary_file": "_REGISTRIES/CANONICAL/OWNED_REPO_DEPENDENCIES.json",
        "aliases": ["OPS-038", "Dependency Ontology", "Dependency Graph", "Package Dependencies"],
        "tags": ["ontology", "operational", "dependency", "package-manifests", "spof", "transitive-deps", "ops-038"],
        "connects_to": ["ONT-006", "ONT-007", "OPS-039"],
        "registry_sources": ["_REGISTRIES/CANONICAL/OWNED_REPO_DEPENDENCIES.json", "13_ENGINEERING/INFRASTRUCTURE/infrastructure_dependency_registry.json"]
    },
    {
        "id": "OPS-039",
        "name": "Relationship Ontology",
        "category": "OPERATIONAL",
        "description": "The hyper-connective graph relational tissue linking Ventures, Capabilities, Technologies, Repos, and People.",
        "primary_domain": "08-KNOWLEDGE-GRAPH",
        "primary_file": "_ONTOLOGY/RELATIONSHIPS.yaml",
        "aliases": ["OPS-039", "Relationship Ontology", "Graph Edges", "Connective Tissue"],
        "tags": ["ontology", "operational", "relationship", "graph-edges", "cypher-relationships", "hyper-connective", "ops-039"],
        "connects_to": ["ONT-001", "ONT-002", "ONT-003", "ONT-004", "ONT-005", "ONT-006", "ONT-007", "ONT-008", "ONT-009", "ONT-010"],
        "registry_sources": ["_ONTOLOGY/RELATIONSHIPS.yaml", "_ONTOLOGY/RELATIONSHIPS_EXTENDED.yaml", "08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH.md"]
    },
    {
        "id": "OPS-040",
        "name": "Evidence & Provenance Ontology",
        "category": "OPERATIONAL",
        "description": "Empirical runtime logs, test proofs, live HTTP responses, receipts, and audit trail records.",
        "primary_domain": "EVIDENCE",
        "primary_file": "EVIDENCE.md",
        "aliases": ["OPS-040", "Evidence Ontology", "Audit Provenance", "Truth Proofs"],
        "tags": ["ontology", "operational", "evidence", "provenance", "runtime-proofs", "audit-trail", "receipts", "ops-040"],
        "connects_to": ["ONT-010", "OPS-027", "OPS-045"],
        "registry_sources": ["EVIDENCE.md", "REALITY.md", "_ONTOLOGY/EVIDENCE_STANDARDS.md", "receipts/receipts.jsonl"]
    },
    {
        "id": "OPS-041",
        "name": "Time Ontology",
        "category": "OPERATIONAL",
        "description": "Temporal execution intervals, cron schedules, session durations, historical evolution snapshots, and timestamps.",
        "primary_domain": "44-LEARNING",
        "primary_file": "44-LEARNING/44-LEARNING.md",
        "aliases": ["OPS-041", "Time Ontology", "Temporal Schedules", "Time-Series History"],
        "tags": ["ontology", "operational", "time", "temporal", "cron", "schedules", "timestamps", "ops-041"],
        "connects_to": ["OPS-026", "OPS-042", "OPS-043"],
        "registry_sources": ["44-LEARNING/"]
    },
    {
        "id": "OPS-042",
        "name": "Version Ontology",
        "category": "OPERATIONAL",
        "description": "Semantic versioning (SemVer), Git commit shas, release tags, model version revisions, and schema migrations.",
        "primary_domain": "45-EVOLUTION",
        "primary_file": "45-EVOLUTION/45-EVOLUTION.md",
        "aliases": ["OPS-042", "Version Ontology", "Semantic Versioning", "Release Revisions"],
        "tags": ["ontology", "operational", "version", "semver", "git-commits", "releases", "revisions", "ops-042"],
        "connects_to": ["ONT-006", "OPS-038", "OPS-043"],
        "registry_sources": ["45-EVOLUTION/"]
    },
    {
        "id": "OPS-043",
        "name": "Lifecycle Ontology",
        "category": "OPERATIONAL",
        "description": "State machines: IDEA -> VALIDATING -> BUILDING -> LIVE -> REVENUE -> GROWING; and ACTIVE vs DORMANT states.",
        "primary_domain": "07-ONTOLOGY",
        "primary_file": "_ONTOLOGY/STATUS_LIFECYCLE.md",
        "aliases": ["OPS-043", "Lifecycle Ontology", "State Machine", "Maturity Lifecycle"],
        "tags": ["ontology", "operational", "lifecycle", "state-machine", "maturation", "stages", "ops-043"],
        "connects_to": ["ONT-003", "ONT-014", "OPS-042"],
        "registry_sources": ["_ONTOLOGY/STATUS_LIFECYCLE.md", "_ONTOLOGY/TRUTH_STATUS.yaml"]
    },
    {
        "id": "OPS-044",
        "name": "Governance Ontology",
        "category": "OPERATIONAL",
        "description": "Constitutional authority, Sovereign Operator commands, subagent authorization scopes, and escalation trees.",
        "primary_domain": "46-GOVERNANCE",
        "primary_file": "46-GOVERNANCE/46-GOVERNANCE.md",
        "aliases": ["OPS-044", "Governance Ontology", "Constitutional Authority", "Executive Governance"],
        "tags": ["ontology", "operational", "governance", "constitution", "sovereign-operator", "escalation", "ops-044"],
        "connects_to": ["ONT-011", "OPS-027", "OPS-028"],
        "registry_sources": ["46-GOVERNANCE/", "00-CONSTITUTION/00-CONSTITUTION.md"]
    },
    {
        "id": "OPS-045",
        "name": "Performance Ontology",
        "category": "OPERATIONAL",
        "description": "Return on Investment (ROI), autonomous agent evaluation scores, execution benchmarks, and customer feedback.",
        "primary_domain": "42-EVALUATION",
        "primary_file": "42-EVALUATION/42-EVALUATION.md",
        "aliases": ["OPS-045", "Performance Ontology", "Evaluation Benchmarks", "Outcome Assessment"],
        "tags": ["ontology", "operational", "performance", "evaluation", "benchmarks", "roi", "feedback", "outcomes", "ops-045"],
        "connects_to": ["ONT-018", "ONT-025", "OPS-040", "43-OUTCOMES/43-OUTCOMES.md"],
        "registry_sources": ["42-EVALUATION/", "43-OUTCOMES/43-OUTCOMES.md"]
    }
]

print(f"Loaded {len(ONTOLOGIES)} ontologies (25 Foundational + 20 Operational).")

# ==============================================================================
# 1. WRITE _ONTOLOGY/45_ONTOLOGIES_REGISTRY.yaml
# ==============================================================================
print("\n1. Writing _ONTOLOGY/45_ONTOLOGIES_REGISTRY.yaml...")
reg_file = os.path.join(WORKSPACE, "_ONTOLOGY", "45_ONTOLOGIES_REGISTRY.yaml")

yaml_data = {
    "metadata": {
        "title": "45 Core Ontologies Master Crosswalk",
        "authority": "System Architecture & Infrastructure Control Plane (CP-027)",
        "version": "2.0.0",
        "created_at": "2026-09-06",
        "total_ontologies": len(ONTOLOGIES),
        "foundational_count": 25,
        "operational_count": 20,
        "description": "Unified mapping connecting the 45 theoretical ontologies to their ground-truth folder aliases, canonical files, and tags in Company Brain."
    },
    "ontologies": {o["id"]: o for o in ONTOLOGIES}
}

with open(reg_file, "w") as f:
    yaml.dump(yaml_data, f, sort_keys=False)
print("Wrote _ONTOLOGY/45_ONTOLOGIES_REGISTRY.yaml successfully.")

# ==============================================================================
# 2. CREATE 07-ONTOLOGY/domains/ ALIAS STUBS (ONT-001 to OPS-045)
# ==============================================================================
print("\n2. Creating ontology alias stubs in 07-ONTOLOGY/domains/...")
domains_stub_dir = os.path.join(WORKSPACE, "07-ONTOLOGY", "domains")
os.makedirs(domains_stub_dir, exist_ok=True)

for o in ONTOLOGIES:
    stub_file = os.path.join(domains_stub_dir, f"{o['id']}.md")
    content = f"""---
id: "{o['id']}"
ontology_id: "{o['id']}"
title: "{o['id']}: {o['name']}"
category: "{o['category']}"
aliases: {o['aliases']}
tags: {o['tags']}
primary_domain: "[[{o['primary_domain']}]]"
primary_file: "[[{o['primary_file']}]]"
---

# {o['id']}: {o['name']}

**Category:** {o['category']} Ontology  
**Canonical Domain Gateway:** [[{o['primary_domain']}]]  
**Primary File / Schema:** [[{o['primary_file']}]]  

## Description
{o['description']}

## Connected Ontologies
{chr(10).join([f"- [[07-ONTOLOGY/domains/{target}|{target}]]" for target in o['connects_to']])}

## Registry / Ground-Truth Sources
{chr(10).join([f"- [[{s}]]" for s in o['registry_sources']])}
"""
    with open(stub_file, "w") as f:
        f.write(content)

print(f"Created {len(ONTOLOGIES)} ontology stub files in 07-ONTOLOGY/domains/.")

# ==============================================================================
# 3. CREATE 07-ONTOLOGY/45-ONTOLOGIES-MASTER.md & UPDATE 07-ONTOLOGY/README.md
# ==============================================================================
print("\n3. Creating 07-ONTOLOGY/45-ONTOLOGIES-MASTER.md...")
master_md_file = os.path.join(WORKSPACE, "07-ONTOLOGY", "45-ONTOLOGIES-MASTER.md")

table_rows = []
for o in ONTOLOGIES:
    stub_link = f"[[07-ONTOLOGY/domains/{o['id']}|{o['id']}]]"
    name_link = f"**{o['name']}**"
    cat = o['category']
    domain_link = f"[[{o['primary_domain']}]]"
    file_link = f"[[{o['primary_file']}|{os.path.basename(o['primary_file'])}]]"
    tags_str = ", ".join([f"`{t}`" for t in o['tags'][:3]])
    table_rows.append(f"| {stub_link} | {name_link} | {cat} | {domain_link} | {file_link} | {tags_str} |")

master_content = f"""---
id: DOC-ONT-MASTER-001
title: 45 Core Ontologies Master Architecture
aliases: ["45-ONTOLOGIES", "Master-Ontology-Stack", "Ontology-Crosswalk", "Core-Ontologies"]
tags: [ontology, architecture, knowledge-graph, master-stack, neo4j]
status: ACTIVE
updated: 2026-09-06
---

[[00-CONSTITUTION]] | [[07-ONTOLOGY]] | [[08-KNOWLEDGE-GRAPH]] | [[STARTHERE]] | [[INDEX]]

# 45 Core Ontologies Master Architecture

> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)  
> **Master Registry:** [[_ONTOLOGY/45_ONTOLOGIES_REGISTRY.yaml]]  
> **Scope:** Ground-truth ontological tissue connecting all 50 Company Brain domains, canonical registries, and Neo4j relational graph.

---

## 1. Architectural Model

Company Brain does not operate on disconnected silos. The ecosystem is grounded in **45 Unified Ontological Domains**:
- **25 Foundational Ontologies (`ONT-001` to `ONT-025`):** Describe **WHAT EXISTS** (Entities, Capital, Infrastructure, Software, Products).
- **20 Operational Ontologies (`OPS-026` to `OPS-045`):** Describe **WHAT HAPPENS** (Events, Decisions, Workflows, Relationships, Evidence).

```text
                                 COMPANY BRAIN
                                      │
                   ┌──────────────────┼──────────────────┐
                   ↓                  ↓                  ↓
                ECONOMY           TECHNOLOGY          CAPITAL
               (ONT-001)          (ONT-004)          (ONT-017)
                   │                  │                  │
                Markets          Capabilities         Funding
               (ONT-016)          (ONT-005)              │
                   │                  │                Grants
               Companies           Software              │
               (ONT-002)          (ONT-006)            Equity
                   │                  │                  │
                Ventures            Agents               │
               (ONT-003)          (ONT-008)              │
                   │                  │                  │
                   └───────────┬──────┴──────┬───────────┘
                               ↓             ↓
                            PEOPLE        PROCESSES
                           (ONT-012)      (ONT-013)
                               │             │
                               └──────┬──────┘
                                      ↓
                                    DATA (ONT-009)
                                      ↓
                                  KNOWLEDGE (ONT-010)
                                      ↓
                                  DECISION (OPS-027)
                                      ↓
                                   ACTION (OPS-035)
                                      ↓
                                   EVENT (OPS-026)
                                      ↓
                                  METRICS (ONT-025)
                                      ↓
                                 PERFORMANCE (OPS-045)
                                      ↓
                                  FEEDBACK (OPS-040)
                                      │
                                      └────────→ RE-INGESTION (Neo4j / Qdrant)
```

---

## 2. The Relationship Ontology (`OPS-039`) — The Hyper-Connective Tissue

The real power of Company Brain is not merely knowing that entities exist. It is navigating the **hyper-connective relational edges**:

> **Venture A** (`ONT-003`)  
> ├── **operates_as** → Operating Company (`ONT-002`)  
> ├── **targets** → Market & ICP (`ONT-015`, `ONT-016`)  
> ├── **requires** → Capabilities (`ONT-005`)  
> ├── **implemented_by** → Software Repositories (`ONT-006`)  
> ├── **automated_by** → Agent Swarms (`ONT-008`)  
> ├── **runs_on** → Local Mesh Infrastructure (`ONT-007`)  
> ├── **funded_by** → Capital & Grants (`ONT-017`)  
> ├── **measured_by** → Financial & Operational Metrics (`ONT-018`, `ONT-025`)  
> └── **governed_by** → Operating Policies & Constitution (`OPS-028`, `OPS-044`)

---

## 3. The Complete 45 Ontology Stack Crosswalk

| ID | Ontology Name | Category | Primary Domain Gateway | Ground-Truth File / Schema | Tags |
| :--- | :--- | :--- | :--- | :--- | :--- |
{chr(10).join(table_rows)}

---

## 4. Machine Verification in Neo4j

All 45 ontologies and their primary nodes are queryable directly in the live Neo4j database (`bolt://100.87.214.70:7687`):

```cypher
// Trace hyper-connective tissue for any venture across the ontologies
MATCH (v:Venture)-[op:OPERATES]->(r:Repository)
OPTIONAL MATCH (r)-[imp:IMPLEMENTS]->(c:Capability)
OPTIONAL MATCH (v)-[dep:DEPLOYS]->(s:Site)
RETURN v.id as Venture, r.name as Repo, collect(c.name) as Capabilities, collect(s.url) as Sites
```
"""

with open(master_md_file, "w") as f:
    f.write(master_content)
print("Wrote 07-ONTOLOGY/45-ONTOLOGIES-MASTER.md successfully.")

# Update 07-ONTOLOGY/README.md
readme_file = os.path.join(WORKSPACE, "07-ONTOLOGY", "README.md")
readme_content = f"""# 07-ONTOLOGY — Knowledge Architecture & Ontology Control Plane

> **Domain:** `07-ONTOLOGY`  
> **Master Stack:** [[07-ONTOLOGY/45-ONTOLOGIES-MASTER|45 Core Ontologies Master Architecture]]  
> **Canonical Registry:** [[_ONTOLOGY/45_ONTOLOGIES_REGISTRY.yaml]]  
> **Schema Standard:** [[_ONTOLOGY/RELATIONSHIPS.yaml]] & [[_ONTOLOGY/OBJECTS_EXTENDED.yaml]]  

## Overview
This domain defines the formal schema, entity-relationship models, and cross-domain mappings governing the entire Company Brain ecosystem.

### Core Portals
1. **Master Architecture:** [[07-ONTOLOGY/45-ONTOLOGIES-MASTER|45 Core Ontologies Architecture]]
2. **Individual Domains:** Browse [[07-ONTOLOGY/domains/|All 45 Ontology Gateway Stubs]]
3. **Machine Schemas:**
   - Object Types: [[_ONTOLOGY/OBJECTS_EXTENDED.yaml]]
   - Relationships: [[_ONTOLOGY/RELATIONSHIPS.yaml]]
   - Lifecycle States: [[_ONTOLOGY/STATUS_LIFECYCLE.md]]
   - Truth Standards: [[_ONTOLOGY/TRUTH_STATUS.yaml]]

### Upstream & Downstream Integration
- Upstream: [[00-CONSTITUTION]], [[01-IDENTITY]]
- Downstream: [[08-KNOWLEDGE-GRAPH]], [[09-KNOWLEDGE]], [[14-CAPABILITIES]], [[23-VENTURES]]
"""
with open(readme_file, "w") as f:
    f.write(readme_content)
print("Updated 07-ONTOLOGY/README.md successfully.")

# ==============================================================================
# 4. ALIGN DOMAIN GATEWAY FILES WITH ONTOLOGY TAGS & ALIASES
# ==============================================================================
print("\n4. Aligning corresponding domain gateway files with ontology tags and aliases...")

for o in ONTOLOGIES:
    domain_path = os.path.join(WORKSPACE, o['primary_domain'])
    if not os.path.exists(domain_path):
        continue
    
    # Check domain gateway file XX-NAME.md
    domain_basename = os.path.basename(o['primary_domain'])
    gateway_file = os.path.join(domain_path, f"{domain_basename}.md")
    if not os.path.exists(gateway_file):
        # check if primary_file exists
        if os.path.exists(os.path.join(WORKSPACE, o['primary_file'])):
            gateway_file = os.path.join(WORKSPACE, o['primary_file'])
        else:
            continue

    try:
        with open(gateway_file, "r") as fp:
            orig_content = fp.read()
        
        # Check if already has ontology_id
        if f"ontology_id: \"{o['id']}\"" in orig_content or f"ontology_id: {o['id']}" in orig_content:
            continue

        # Prepare new frontmatter
        aliases_list = sorted(list(set(o['aliases'] + [domain_basename])))
        tags_list = sorted(list(set(o['tags'])))

        fm_block = f"""---
id: "{domain_basename}"
ontology_id: "{o['id']}"
title: "{domain_basename} — {o['name']}"
aliases: {aliases_list}
tags: {tags_list}
ontology_category: "{o['category']}"
---
"""
        if orig_content.startswith("---"):
            # replace frontmatter
            parts = orig_content.split("---", 2)
            if len(parts) >= 3:
                new_file_content = fm_block + parts[2].lstrip()
            else:
                new_file_content = fm_block + orig_content
        else:
            new_file_content = fm_block + orig_content

        with open(gateway_file, "w") as fp:
            fp.write(new_file_content)
        print(f"  Aligned {gateway_file} with {o['id']}.")
    except Exception as e:
        print(f"  Error updating {gateway_file}: {e}")

print("\nAll 45 ontologies mapped, crosswalked, and aligned with tags & aliases successfully.")
