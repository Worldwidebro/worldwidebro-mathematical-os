---
id: RES-SRC-001
title: "SOURCE-REGISTRY — Canonical Intelligence Sources & Data Feeds"
tags: [research, sources, feeds, apis, ingestion, registry]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[37-RESEARCH/README|37-RESEARCH]] | [[02-SOURCES/02-SOURCES|Sources]] | [[03-INGESTION/03-INGESTION|Ingestion]]

# SOURCE-REGISTRY.md — Canonical External Data Source Registry

> **Authority:** Research Control Plane (CP-013)  
> **Standard:** ISO 8000 / Dublin Core Provenance Standard  
> **Schema:** Entity ID `SRC-*`

```yaml
sources:
  SRC-CENSUS:
    name: "U.S. Census Bureau"
    class: "GOVERNMENT"
    description: "Official federal economic census, business dynamics, annual business surveys, and county business patterns."
    domains: ["business", "demographics", "economics", "industry_stats"]
    authority: "PRIMARY"
    api: true
    endpoint: "https://api.census.gov/data"
    key_datasets:
      - "Economic Census (Establishments, sales, payroll to county level)"
      - "Annual Integrated Economic Survey (AIES)"
      - "Business Dynamics Statistics (BDS - firm size, age, entry/exit)"
      - "Nonemployer Statistics (Solopreneurs & independent contractors)"
      - "County Business Patterns (CBP)"

  SRC-BLS:
    name: "U.S. Bureau of Labor Statistics"
    class: "GOVERNMENT"
    description: "Labor economics, employment, occupational wages, CPI, PPI, and productivity metrics."
    domains: ["labor", "wages", "employment", "inflation", "productivity"]
    authority: "PRIMARY"
    api: true
    endpoint: "https://api.bls.gov/publicAPI/v2/timeseries/data/"
    key_datasets:
      - "Occupational Employment and Wage Statistics (OEWS)"
      - "Job Openings and Labor Turnover Survey (JOLTS)"
      - "Consumer Price Index (CPI) & Producer Price Index (PPI)"
      - "Employment Projections by Industry & Occupation"

  SRC-BEA:
    name: "U.S. Bureau of Economic Analysis"
    class: "GOVERNMENT"
    description: "National income, GDP by industry, corporate profits, and regional economic accounts."
    domains: ["GDP", "income", "industry_output", "corporate_profits"]
    authority: "PRIMARY"
    api: true
    endpoint: "https://apps.bea.gov/api/data"
    key_datasets:
      - "Gross Domestic Product by Industry"
      - "Corporate Profits by Industry"
      - "Regional Economic Accounts (State & County GDP, Personal Income)"

  SRC-FRED:
    name: "Federal Reserve Economic Data (St. Louis Fed)"
    class: "ECONOMIC"
    description: "Over 800,000 macroeconomic and financial time-series from 100+ global sources."
    domains: ["macroeconomics", "interest_rates", "credit", "money_supply", "banking"]
    authority: "HIGH"
    api: true
    endpoint: "https://api.stlouisfed.org/fred/"
    key_datasets:
      - "Fed Funds Rate, SOFR, Treasury Yield Curves"
      - "M2 Money Supply & Commercial Bank Credit"
      - "Consumer Credit Outstanding & Delinquency Rates"
      - "Housing Starts, Case-Shiller Home Price Index"

  SRC-SEC:
    name: "U.S. Securities and Exchange Commission (EDGAR)"
    class: "GOVERNMENT"
    description: "Mandated regulatory disclosures, financials, 10-K, 10-Q, 8-K, and insider transactions."
    domains: ["public_companies", "filings", "financial_statements", "material_events"]
    authority: "PRIMARY"
    api: true
    endpoint: "https://data.sec.gov/api/xbrl/"
    key_datasets:
      - "Company Facts & Financial Statements (XBRL)"
      - "Form 10-K (Annual audited reports & risk factors)"
      - "Form 8-K (Unscheduled material events & corporate changes)"
      - "Form 4 (Insider transactions & officer equity ownership)"

  SRC-SBIR:
    name: "Small Business Innovation Research (SBIR.gov)"
    class: "GOVERNMENT"
    description: "Non-dilutive federal R&D solicitations, awards, participating agencies, and commercialization records."
    domains: ["research", "funding", "deep_tech", "commercialization"]
    authority: "PRIMARY"
    api: true
    endpoint: "https://api.sbir.gov/v1/"
    key_datasets:
      - "Open Solicitations by Agency (DoD, NIH, NSF, DoE, NASA)"
      - "Historical Awardees & Funding Amounts"
      - "Technology Area Taxonomies"

  SRC-GRANTS:
    name: "Grants.gov"
    class: "GOVERNMENT"
    description: "Central federal clearinghouse for all discretionary grants across 26 federal grant-making agencies."
    domains: ["grants", "federal_funding", "research_grants"]
    authority: "PRIMARY"
    api: true
    endpoint: "https://api.grants.gov/v1/"
    key_datasets:
      - "Forecasted & Synopsized Grant Solicitations"
      - "Agency Funding Instruments & Eligibility Matrices"

  SRC-USASPENDING:
    name: "USAspending.gov"
    class: "GOVERNMENT"
    description: "Official open data source for federal spending, prime contracts, subawards, and agency budgets."
    domains: ["federal_awards", "procurement", "contracts", "subcontracts"]
    authority: "PRIMARY"
    api: true
    endpoint: "https://api.usaspending.gov/api/v2/"
    key_datasets:
      - "Federal Contract Awards & Modifications (FPDS feed)"
      - "Prime Awardee Vendor Registries"
      - "Subcontract Spending & Small Business Set-Asides"

  SRC-ARXIV:
    name: "arXiv (Cornell University)"
    class: "RESEARCH"
    description: "Open-access scientific archive of preprints in computer science, AI, math, and quantitative biology."
    domains: ["AI", "machine_learning", "computer_science", "physics"]
    authority: "PREPRINT"
    api: true
    endpoint: "http://export.arxiv.org/api/query"
    key_datasets:
      - "cs.AI (Artificial Intelligence)"
      - "cs.LG (Learning)"
      - "cs.CL (Computation and Language / LLMs)"
      - "cs.RO (Robotics)"

  SRC-OPENALEX:
    name: "OpenAlex"
    class: "RESEARCH"
    description: "Massive open research knowledge graph cataloging 250M+ works, authors, institutions, and funders."
    domains: ["scholarly_graph", "citations", "authors", "institutions"]
    authority: "HIGH"
    api: true
    endpoint: "https://api.openalex.org/"
    key_datasets:
      - "Scholarly citation network & author graphs"
      - "Funder-to-paper mapping"
      - "Concept hierarchies & institution affiliations"

  SRC-SEMANTIC-SCHOLAR:
    name: "Semantic Scholar (Allen Institute for AI)"
    class: "RESEARCH"
    description: "AI-powered scholarly search engine extracting key findings, influential citations, and TLDR summaries."
    domains: ["scholarly_search", "influential_citations", "recommendations"]
    authority: "HIGH"
    api: true
    endpoint: "https://api.semanticscholar.org/graph/v1/"
    key_datasets:
      - "Influential Citation Counts"
      - "Paper Embedding Graphs (SPECTER)"
      - "TLDR Automated Summaries"

  SRC-HUGGINGFACE:
    name: "Hugging Face"
    class: "AI"
    description: "Central repository for open-source AI models, datasets, model cards, evaluations, and daily papers."
    domains: ["models", "datasets", "spaces", "benchmarks", "papers"]
    authority: "HIGH"
    api: true
    endpoint: "https://huggingface.co/api/"
    key_datasets:
      - "Model Hub (Architectures, weights, quantizations)"
      - "Dataset Hub (Pretraining, SFT, DPO corpuses)"
      - "Open LLM Leaderboard & Benchmarks"
      - "HF Daily Papers Community"

  SRC-AI-INDEX:
    name: "Stanford Institute for Human-Centered AI (HAI)"
    class: "RESEARCH"
    description: "Annual rigorous benchmark report on global AI capabilities, investment, economics, and technical trends."
    domains: ["AI_economics", "investment", "adoption", "capability_frontier"]
    authority: "HIGH"
    api: false
    endpoint: "https://hai.stanford.edu/research/ai-index-report"
    key_datasets:
      - "Training Compute & Cost Trajectories"
      - "Corporate Investment in Generative AI"
      - "Global AI Policy & Legislation Tracking"
```

---

## Connected Subsystems & Ingestion
- **Research OS:** [[37-RESEARCH/RESEARCH-OS]]
- **Data Sources Domain:** [[02-SOURCES/02-SOURCES]]
- **Ingestion Pipeline:** [[03-INGESTION/03-INGESTION]] • [[_PIPELINES/ingestion/README]]
- **External Universe:** [[_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml]]
