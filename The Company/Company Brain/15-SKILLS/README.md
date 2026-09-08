[[STARTHERE]] | [[REALITY]] | [[15-SKILLS]] | [[16-AGENTS]] | [[INDEX]]

# 15-SKILLS — Master Skill & Persona Runbook Fleet

> **Canonical Domain ID:** `DOM-015`  
> **Ontology Node:** [[15-SKILLS]]  
> **Linked Control Plane:** Agent Control Plane (CP-006) & Infrastructure Control Plane (CP-027)  
> **Upstream Upstream Repository:** [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) (STAR-1125 / OWN-PUB-0883)  
> **Total Registered Skills:** 285 modular procedural runbooks

---

## System Overview

Skills provide specialized, executable domain procedural instructions and behavioral personas to autonomous agents in Company Brain. 
Each skill is stored in `.agents/skills/<skill-name>/SKILL.md` with structured YAML frontmatter, execution heuristics, quality gates, and deliverables.

### Relationship to Agents
- **Agents (`.agents/agents/` / `16-AGENTS`):** Persistent autonomous actors with tool bindings, system prompts, and memory identities (e.g. [[16-AGENTS/README|16-AGENTS]]).
- **Skills (`.agents/skills/` / `15-SKILLS`):** On-demand domain capabilities and expert operational playbooks loaded dynamically during execution.

---

## Academic, Research & Ethnography (8)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-anthropologist` | [[.agents/skills/academic-anthropologist/SKILL|Anthropologist Agent Personality]] | Expert in cultural systems, rituals, kinship, belief systems, and ethnographic method — builds culturally coherent so... |
| `agency-geographer` | [[.agents/skills/academic-geographer/SKILL|Geographer Agent Personality]] | Expert in physical and human geography, climate systems, cartography, and spatial analysis — builds geographically co... |
| `agency-historian` | [[.agents/skills/academic-historian/SKILL|Historian Agent Personality]] | Expert in historical analysis, periodization, material culture, and historiography — validates historical coherence a... |
| `agency-narratologist` | [[.agents/skills/academic-narratologist/SKILL|Narratologist Agent Personality]] | Expert in narrative theory, story structure, character arcs, and literary analysis — grounds advice in established fr... |
| `agency-organizational-psychologist` | [[.agents/skills/organizational-psychologist/SKILL|Organizational Psychologist Agent]] | Applied organizational psychologist who diagnoses team dynamics, psychological safety, burnout risk, and culture heal... |
| `agency-psychologist` | [[.agents/skills/academic-psychologist/SKILL|Psychologist Agent Personality]] | Expert in human behavior, personality theory, motivation, and cognitive patterns — builds psychologically credible ch... |
| `agency-research-synthesist` | [[.agents/skills/research-synthesist/SKILL|Research Synthesist Agent Personality]] | Expert in literature review, source evaluation, and evidence synthesis — turns a scattered pile of sources into a str... |
| `agency-statistician` | [[.agents/skills/academic-statistician/SKILL|Statistician Agent Personality]] | Expert in quantitative research methodology, experimental design, and statistical inference — pressure-tests claims, ... |

---

## Business Operations, Legal & People (27)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-analytics-reporter` | [[.agents/skills/support-analytics-reporter/SKILL|Analytics Reporter Agent Personality]] | Expert data analyst transforming raw data into actionable business insights. Creates dashboards, performs statistical... |
| `agency-business-strategist` | [[.agents/skills/business-strategist/SKILL|Business Strategist]] | Senior management consulting specialist for competitive analysis, market entry strategy, business model design, growt... |
| `agency-change-management-consultant` | [[.agents/skills/change-management-consultant/SKILL|Change Management Consultant]] | Expert change management specialist using ADKAR, Kotter, and Prosci frameworks to guide organizations through technol... |
| `agency-corporate-training-designer` | [[.agents/skills/corporate-training-designer/SKILL|Corporate Training Designer]] | Expert in enterprise training system design and curriculum development — proficient in training needs analysis, instr... |
| `agency-customer-service` | [[.agents/skills/customer-service/SKILL|Customer Service Agent]] | Friendly, professional customer service specialist for any industry — handling inquiries, complaints, account support... |
| `agency-customer-success-manager` | [[.agents/skills/customer-success-manager/SKILL|Customer Success Manager]] | Strategic customer success specialist for onboarding, health scoring, QBR facilitation, churn prevention, expansion i... |
| `agency-data-consolidation-agent` | [[.agents/skills/data-consolidation-agent/SKILL|Data Consolidation Agent]] | AI agent that consolidates extracted sales data into live reporting dashboards with territory, rep, and pipeline summ... |
| `agency-data-privacy-officer` | [[.agents/skills/data-privacy-officer/SKILL|Data Privacy Officer Agent]] | Corporate data privacy specialist and DPO who builds GDPR, CCPA, and global privacy compliance programs — covering da... |
| `agency-esg-sustainability-officer` | [[.agents/skills/esg-sustainability-officer/SKILL|ESG & Sustainability Officer Agent]] | Corporate sustainability strategist and ESG reporting specialist who builds environmental, social, and governance pro... |
| `agency-executive-summary-generator` | [[.agents/skills/support-executive-summary-generator/SKILL|Executive Summary Generator Agent Personality]] | Consultant-grade AI specialist trained to think and communicate like a senior strategy consultant. Transforms complex... |
| `agency-finance-tracker` | [[.agents/skills/support-finance-tracker/SKILL|Finance Tracker Agent Personality]] | Expert financial analyst and controller specializing in financial planning, budget management, and business performan... |
| `agency-hospitality-guest-services` | [[.agents/skills/hospitality-guest-services/SKILL|Hospitality Guest Services Agent]] | Comprehensive hospitality guest services specialist for hotels, resorts, restaurants, and event venues — covering res... |
| `agency-hr-onboarding` | [[.agents/skills/hr-onboarding/SKILL|HR Onboarding Agent]] | Comprehensive HR onboarding specialist for employee orientation, documentation management, compliance tracking, benef... |
| `agency-infrastructure-maintainer` | [[.agents/skills/support-infrastructure-maintainer/SKILL|Infrastructure Maintainer Agent Personality]] | Expert infrastructure specialist focused on system reliability, performance optimization, and technical operations ma... |
| `agency-legal-billing-time-tracking` | [[.agents/skills/legal-billing-time-tracking/SKILL|Legal Billing & Time Tracking Agent]] | Comprehensive legal billing and time tracking specialist for accurate time capture, invoice generation, billing narra... |
| `agency-legal-client-intake` | [[.agents/skills/legal-client-intake/SKILL|Legal Client Intake Agent]] | Comprehensive legal client intake specialist for qualifying prospects, collecting case information, scheduling consul... |
| `agency-legal-compliance-checker` | [[.agents/skills/support-legal-compliance-checker/SKILL|Legal Compliance Checker Agent Personality]] | Expert legal and compliance specialist ensuring business operations, data handling, and content creation comply with ... |
| `agency-legal-document-review` | [[.agents/skills/legal-document-review/SKILL|Legal Document Review Agent]] | Comprehensive legal document review specialist for contracts, litigation documents, and real estate agreements — summ... |
| `agency-loan-officer-assistant` | [[.agents/skills/loan-officer-assistant/SKILL|Loan Officer Assistant Agent]] | Comprehensive loan officer assistant for mortgage and lending professionals — covering borrower intake, pre-qualifica... |
| `agency-m-a-integration-manager` | [[.agents/skills/ma-integration-manager/SKILL|M&A Integration Manager Agent]] | Mergers and acquisitions integration specialist who designs and executes post-merger integration programs — covering ... |
| `agency-operations-manager` | [[.agents/skills/operations-manager/SKILL|Operations Manager Agent]] | Business operations specialist who applies Lean, Six Sigma, and systems thinking to process mapping, capacity plannin... |
| `agency-real-estate-buyer-seller` | [[.agents/skills/real-estate-buyer-seller/SKILL|Real Estate Buyer & Seller Agent]] | Comprehensive real estate agent assistant for buyer representation, seller representation, listing management, offer ... |
| `agency-recruitment-specialist` | [[.agents/skills/recruitment-specialist/SKILL|Recruitment Specialist Agent]] | Expert recruitment operations and talent acquisition specialist — skilled in China's major hiring platforms, talent a... |
| `agency-report-distribution-agent` | [[.agents/skills/report-distribution-agent/SKILL|Report Distribution Agent]] | AI agent that automates distribution of consolidated sales reports to representatives based on territorial parameters |
| `agency-retail-customer-returns` | [[.agents/skills/retail-customer-returns/SKILL|Retail Customer Returns Agent]] | Comprehensive retail customer returns specialist for processing returns, exchanges, and refunds across in-store, onli... |
| `agency-supply-chain-strategist` | [[.agents/skills/supply-chain-strategist/SKILL|Supply Chain Strategist Agent]] | Expert supply chain management and procurement strategy specialist — skilled in supplier development, strategic sourc... |
| `agency-support-responder` | [[.agents/skills/support-support-responder/SKILL|Support Responder Agent Personality]] | Expert customer support specialist delivering exceptional customer service, issue resolution, and user experience opt... |

---

## Core Platform, Swarm Orchestration & Infra (9)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-agentic-identity-trust-architect` | [[.agents/skills/agentic-identity-trust/SKILL|Agentic Identity & Trust Architect]] | Designs identity, authentication, and trust verification systems for autonomous AI agents operating in multi-agent en... |
| `agency-agents-orchestrator` | [[.agents/skills/agents-orchestrator/SKILL|AgentsOrchestrator Agent Personality]] | Autonomous pipeline manager that orchestrates the entire development workflow. You are the leader of this process. |
| `agency-automation-governance-architect` | [[.agents/skills/automation-governance-architect/SKILL|Automation Governance Architect]] | Governance-first architect for business automations (n8n-first) who audits value, risk, and maintainability before im... |
| `agency-identity-graph-operator` | [[.agents/skills/identity-graph-operator/SKILL|Identity Graph Operator]] | Operates a shared identity graph that multiple AI agents resolve against. Ensures every agent in a multi-agent system... |
| `capability-mapping` | [[.agents/skills/capability-mapping/SKILL|Capability Mapping Skill]] | Maps verified software libraries, components, and tools to business and technical capabilities across the canonical r... |
| `deployment` | [[.agents/skills/deployment/SKILL|Deployment Skill]] | Orchestrates service deployments, container lifecycle, and infrastructure updates across the Mac Studio and local net... |
| `find-skills` | [[.agents/skills/find-skills/SKILL|Find Skills]] | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is... |
| `observability` | [[.agents/skills/observability/SKILL|Observability Skill]] | Monitors metrics, logs, traces, and model routing telemetry across Grafana and Langfuse. Use when debugging performan... |
| `repository-intelligence` | [[.agents/skills/repository-intelligence/SKILL|Repository Intelligence Skill]] | Analyzes, verifies, and catalogs owned and starred repositories across Company Brain using GitHub GraphQL batching, m... |

---

## Design, Creative & Whimsy (10)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-brand-guardian` | [[.agents/skills/design-brand-guardian/SKILL|Brand Guardian Agent Personality]] | Expert brand strategist and guardian specializing in brand identity development, consistency maintenance, and strateg... |
| `agency-image-prompt-engineer` | [[.agents/skills/design-image-prompt-engineer/SKILL|Image Prompt Engineer Agent]] | Expert photography prompt engineer specializing in crafting detailed, evocative prompts for AI image generation. Mast... |
| `agency-inclusive-visuals-specialist` | [[.agents/skills/design-inclusive-visuals-specialist/SKILL|Inclusive Visuals Specialist]] | Representation expert who defeats systemic AI biases to generate culturally accurate, affirming, and non-stereotypica... |
| `agency-persona-walkthrough-specialist` | [[.agents/skills/design-persona-walkthrough/SKILL|Persona Walkthrough Specialist]] | Simulate cognitive walkthroughs of web pages from a defined persona's psychological perspective — captures emotional ... |
| `agency-ui-designer` | [[.agents/skills/design-ui-designer/SKILL|UI Designer Agent Personality]] | Expert UI designer specializing in visual design systems, component libraries, and pixel-perfect interface creation. ... |
| `agency-ui-finish-gate-reviewer` | [[.agents/skills/design-ui-finish-gate-reviewer/SKILL|UI Finish-Gate Reviewer Agent Personality]] | Product-interface reviewer who catches generic, interchangeable UI before it ships by grounding critique in real prod... |
| `agency-ux-architect` | [[.agents/skills/design-ux-architect/SKILL|ArchitectUX Agent Personality]] | Technical architecture and UX specialist who provides developers with solid foundations, CSS systems, and clear imple... |
| `agency-ux-researcher` | [[.agents/skills/design-ux-researcher/SKILL|UX Researcher Agent Personality]] | Expert user experience researcher specializing in user behavior analysis, usability testing, and data-driven design i... |
| `agency-visual-storyteller` | [[.agents/skills/design-visual-storyteller/SKILL|Visual Storyteller Agent]] | Expert visual communication specialist focused on creating compelling visual narratives, multimedia content, and bran... |
| `agency-whimsy-injector` | [[.agents/skills/design-whimsy-injector/SKILL|Whimsy Injector Agent Personality]] | Expert creative specialist focused on adding personality, delight, and playful elements to brand experiences. Creates... |

---

## Engineering, Architecture & Polyglot Systems (63)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-ai-data-remediation-engineer` | [[.agents/skills/engineering-ai-data-remediation-engineer/SKILL|AI Data Remediation Engineer Agent]] | Specialist in self-healing data pipelines — uses air-gapped local SLMs and semantic clustering to automatically detec... |
| `agency-ai-engineer` | [[.agents/skills/engineering-ai-engineer/SKILL|AI Engineer Agent]] | Expert AI/ML engineer specializing in machine learning model development, deployment, and integration into production... |
| `agency-api-platform-engineer` | [[.agents/skills/engineering-api-platform-engineer/SKILL|API Platform Engineer]] | Expert API platform engineer for public and partner APIs — contract-first design (OpenAPI/gRPC), versioning and depre... |
| `agency-autonomous-optimization-architect` | [[.agents/skills/engineering-autonomous-optimization-architect/SKILL|Autonomous Optimization Architect]] | Intelligent system governor that continuously shadow-tests APIs for performance while enforcing strict financial and ... |
| `agency-backend-architect` | [[.agents/skills/engineering-backend-architect/SKILL|Backend Architect Agent Personality]] | Senior backend architect specializing in scalable system design, database architecture, API development, and cloud in... |
| `agency-cms-developer` | [[.agents/skills/engineering-cms-developer/SKILL|CMS Developer]] | Drupal and WordPress specialist for theme development, custom plugins/modules, content architecture, and code-first C... |
| `agency-code-reviewer` | [[.agents/skills/engineering-code-reviewer/SKILL|Code Reviewer Agent]] | Expert code reviewer who provides constructive, actionable feedback focused on correctness, maintainability, security... |
| `agency-codebase-onboarding-engineer` | [[.agents/skills/engineering-codebase-onboarding-engineer/SKILL|Codebase Onboarding Engineer Agent]] | Expert developer onboarding specialist who helps new engineers understand unfamiliar codebases fast by reading source... |
| `agency-data-engineer` | [[.agents/skills/engineering-data-engineer/SKILL|Data Engineer Agent]] | Expert data engineer specializing in building reliable data pipelines, lakehouse architectures, and scalable data inf... |
| `agency-data-visualization-engineer` | [[.agents/skills/engineering-data-visualization-engineer/SKILL|Data Visualization Engineer]] | Expert data visualization engineer — chart-type selection by data and question, perceptually honest encodings, colorb... |
| `agency-database-optimizer` | [[.agents/skills/engineering-database-optimizer/SKILL|Database Optimizer]] | Expert database specialist focusing on schema design, query optimization, indexing strategies, and performance tuning... |
| `agency-database-reliability-engineer` | [[.agents/skills/engineering-database-reliability-engineer/SKILL|Database Reliability Engineer]] | Expert database reliability engineer (DBRE) — high availability and replication, automated failover, backup and point... |
| `agency-desktop-app-engineer` | [[.agents/skills/engineering-desktop-app-engineer/SKILL|Desktop App Engineer]] | Expert desktop application engineer for Electron and Tauri — secure IPC and process isolation, code signing and notar... |
| `agency-developer-tooling-engineer` | [[.agents/skills/engineering-developer-tooling-engineer/SKILL|Developer Tooling Engineer]] | Expert developer-tooling and CLI engineer — building command-line tools and internal developer platforms with great D... |
| `agency-devops-automator` | [[.agents/skills/engineering-devops-automator/SKILL|DevOps Automator Agent Personality]] | Expert DevOps engineer specializing in infrastructure automation, CI/CD pipeline development, and cloud operations |
| `agency-drupal-performance-engineer` | [[.agents/skills/engineering-drupal-performance/SKILL|Drupal Performance Engineer]] | Expert Drupal 10/11 performance engineer specializing in Core Web Vitals, render and dynamic page caching, BigPipe, c... |
| `agency-drupal-shopping-cart-engineer` | [[.agents/skills/engineering-drupal-shopping-cart/SKILL|Drupal Shopping Cart Engineer]] | Expert Drupal e-commerce engineer specializing in Drupal Commerce for product catalog management, payment gateway int... |
| `agency-email-intelligence-engineer` | [[.agents/skills/engineering-email-intelligence-engineer/SKILL|Email Intelligence Engineer Agent]] | Expert in extracting structured, reasoning-ready data from raw email threads for AI agents and automation systems |
| `agency-embedded-firmware-engineer` | [[.agents/skills/engineering-embedded-firmware-engineer/SKILL|Embedded Firmware Engineer]] | Specialist in bare-metal and RTOS firmware - ESP32/ESP-IDF, PlatformIO, Arduino, ARM Cortex-M, STM32 HAL/LL, Nordic n... |
| `agency-feishu-integration-developer` | [[.agents/skills/engineering-feishu-integration-developer/SKILL|Feishu Integration Developer]] | Full-stack integration expert specializing in the Feishu (Lark) Open Platform — proficient in Feishu bots, mini progr... |
| `agency-filament-optimization-specialist` | [[.agents/skills/engineering-filament-optimization-specialist/SKILL|Agent Personality]] | Expert in restructuring and optimizing Filament PHP admin interfaces for maximum usability and efficiency. Focuses on... |
| `agency-finops-engineer` | [[.agents/skills/engineering-finops-engineer/SKILL|FinOps Engineer]] | Expert cloud cost engineer for AWS/GCP/Azure — cost allocation and tagging, rightsizing, commitment planning (reserve... |
| `agency-frontend-developer` | [[.agents/skills/engineering-frontend-developer/SKILL|Frontend Developer Agent Personality]] | Expert frontend developer specializing in modern web technologies, React/Vue/Angular frameworks, UI implementation, a... |
| `agency-gaussdb-expert-engineer` | [[.agents/skills/engineering-gaussdb-expert/SKILL|GaussDB OLTP Expert]] | Expert database specialist focusing on GaussDB OLTP — Huawei's self-developed enterprise-grade relational database (N... |
| `agency-git-workflow-master` | [[.agents/skills/engineering-git-workflow-master/SKILL|Git Workflow Master Agent]] | Expert in Git workflows, branching strategies, and version control best practices including conventional commits, reb... |
| `agency-identity-access-engineer` | [[.agents/skills/engineering-identity-access-engineer/SKILL|Identity & Access Engineer]] | Expert identity engineer for OAuth 2.0/OIDC flows, enterprise SSO (SAML/OIDC) and SCIM provisioning, passkeys/WebAuth... |
| `agency-incident-response-commander` | [[.agents/skills/engineering-incident-response-commander/SKILL|Incident Response Commander Agent]] | Expert incident commander specializing in production incident management, structured response coordination, post-mort... |
| `agency-internationalization-engineer` | [[.agents/skills/engineering-i18n-engineer/SKILL|Internationalization Engineer]] | Expert i18n engineer for ICU MessageFormat, CLDR plural rules, RTL and bidirectional layouts, locale-aware date/numbe... |
| `agency-iot-fleet-engineer` | [[.agents/skills/engineering-iot-fleet-engineer/SKILL|IoT Fleet Engineer]] | Expert IoT and edge fleet engineer — device provisioning and identity, MQTT/telemetry pipelines, staged over-the-air ... |
| `agency-it-service-manager` | [[.agents/skills/engineering-it-service-manager/SKILL|IT Service Manager]] | Expert IT service management specialist using ITIL 4 framework for service catalog design, incident and problem manag... |
| `agency-knowledge-graph-engineer` | [[.agents/skills/engineering-knowledge-graph-engineer/SKILL|Knowledge Graph Engineer Agent]] | Structures information and capabilities into interconnected nodes (entities) and edges (relationships) — enabling dyn... |
| `agency-llm-post-training-engineer` | [[.agents/skills/engineering-llm-post-training-engineer/SKILL|LLM Post-Training Engineer]] | Evidence-driven owner for SFT, preference optimization, RLHF/RLVR, MoE post-training, and the release gates that turn... |
| `agency-lsp-index-engineer` | [[.agents/skills/lsp-index-engineer/SKILL|LSP/Index Engineer Agent Personality]] | Language Server Protocol specialist building unified code intelligence systems through LSP client orchestration and s... |
| `agency-minimal-change-engineer` | [[.agents/skills/engineering-minimal-change-engineer/SKILL|Minimal Change Engineer Agent]] | Engineering specialist focused on minimum-viable diffs — fixes only what was asked, refuses scope creep, prefers thre... |
| `agency-mobile-app-builder` | [[.agents/skills/engineering-mobile-app-builder/SKILL|Mobile App Builder Agent Personality]] | Specialized mobile application developer with expertise in native iOS/Android development and cross-platform frameworks |
| `agency-mobile-release-engineer` | [[.agents/skills/engineering-mobile-release-engineer/SKILL|Mobile Release Engineer]] | Expert mobile release and distribution engineer for iOS and Android — code signing, provisioning, fastlane pipelines,... |
| `agency-multi-agent-systems-architect` | [[.agents/skills/engineering-multi-agent-systems-architect/SKILL|Multi-Agent Systems Architect Agent]] | Systems architect specializing in the design, coordination, and governance of multi-agent AI pipelines — covering top... |
| `agency-network-engineer` | [[.agents/skills/engineering-network-engineer/SKILL|Network Engineer]] | Expert network engineer for Cisco IOS/IOS-XE, Cisco ASA/FTD, Juniper Junos, and Palo Alto PAN-OS routing, switching, ... |
| `agency-orgscript-engineer` | [[.agents/skills/engineering-orgscript-engineer/SKILL|OrgScript Engineer Personality]] | Expert in designing, parsing, and implementing OrgScript grammar, AST validation, and business logic definitions. |
| `agency-payments-billing-engineer` | [[.agents/skills/engineering-payments-billing-engineer/SKILL|Payments & Billing Engineer]] | Expert payments engineer for PSP integrations (Stripe, Adyen, Braintree, PayPal), idempotent payment flows, webhook p... |
| `agency-privacy-engineer` | [[.agents/skills/engineering-privacy-engineer/SKILL|Privacy Engineer]] | Expert privacy engineer who implements privacy in code — PII discovery and classification, data minimization, consent... |
| `agency-prompt-engineer` | [[.agents/skills/engineering-prompt-engineer/SKILL|Prompt Engineer]] | Specialist in crafting, testing, and systematically optimizing prompts for LLMs — turning vague instructions into rel... |
| `agency-rag-pipeline-engineer` | [[.agents/skills/engineering-rag-pipeline-engineer/SKILL|RAG Pipeline Engineer]] | Production RAG specialist focused on chunking strategy, retrieval quality, hybrid search, re-ranking, and eval-driven... |
| `agency-rapid-prototyper` | [[.agents/skills/engineering-rapid-prototyper/SKILL|Rapid Prototyper Agent Personality]] | Specialized in ultra-fast proof-of-concept development and MVP creation using efficient tools and frameworks |
| `agency-realtime-collaboration-engineer` | [[.agents/skills/engineering-realtime-collaboration-engineer/SKILL|Realtime Collaboration Engineer]] | Expert realtime systems engineer for WebSocket/SSE infrastructure, presence, CRDT and OT-based collaborative editing,... |
| `agency-rust-refactoring-specialist` | [[.agents/skills/engineering-rust-refactoring-specialist/SKILL|Rust Refactoring Specialist Agent]] | Expert Rust engineer for repository-scale refactoring, safe renames, module restructuring, duplication removal, panic... |
| `agency-search-relevance-engineer` | [[.agents/skills/engineering-search-relevance-engineer/SKILL|Search Relevance Engineer]] | Expert search engineer for Elasticsearch and OpenSearch — index and analyzer design, BM25 query tuning, hybrid lexica... |
| `agency-section-508-accessibility-specialist` | [[.agents/skills/engineering-section-508-specialist/SKILL|Section 508 Accessibility Specialist]] | Expert U.S. federal Section 508 accessibility engineer (the 508 legal baseline is WCAG 2.0 Level AA; WCAG 2.1/2.2 AA ... |
| `agency-senior-developer` | [[.agents/skills/engineering-senior-developer/SKILL|Developer Agent Personality]] | Premium implementation specialist - Masters Laravel/Livewire/FluxUI, advanced CSS, Three.js integration |
| `agency-software-architect` | [[.agents/skills/engineering-software-architect/SKILL|Software Architect Agent]] | Expert software architect specializing in system design, domain-driven design, architectural patterns, and technical ... |
| `agency-solidity-smart-contract-engineer` | [[.agents/skills/engineering-solidity-smart-contract-engineer/SKILL|Solidity Smart Contract Engineer]] | Expert Solidity developer specializing in EVM smart contract architecture, gas optimization, upgradeable proxy patter... |
| `agency-sre-site-reliability-engineer` | [[.agents/skills/engineering-sre/SKILL|SRE (Site Reliability Engineer) Agent]] | Expert site reliability engineer specializing in SLOs, error budgets, observability, chaos engineering, and toil redu... |
| `agency-technical-writer` | [[.agents/skills/engineering-technical-writer/SKILL|Technical Writer Agent]] | Expert technical writer specializing in developer documentation, API references, README files, and tutorials. Transfo... |
| `agency-terminal-integration-specialist` | [[.agents/skills/terminal-integration-specialist/SKILL|Terminal Integration Specialist]] | Terminal emulation, text rendering optimization, and SwiftTerm integration for modern Swift applications |
| `agency-uswds-developer` | [[.agents/skills/engineering-uswds-developer/SKILL|USWDS Developer]] | Expert U.S. Web Design System frontend developer specializing in USWDS components and design tokens, accessible-by-de... |
| `agency-video-streaming-engineer` | [[.agents/skills/engineering-video-streaming-engineer/SKILL|Video Streaming Engineer]] | Expert video streaming engineer for adaptive bitrate delivery — HLS/DASH packaging, ffmpeg transcode ladders, CMAF lo... |
| `agency-voice-ai-integration-engineer` | [[.agents/skills/engineering-voice-ai-integration-engineer/SKILL|Voice AI Integration Engineer Agent]] | Expert in building end-to-end speech transcription pipelines using Whisper-style models and cloud ASR services — from... |
| `agency-webassembly-engineer` | [[.agents/skills/engineering-webassembly-engineer/SKILL|WebAssembly Engineer]] | Expert WebAssembly engineer — compiling Rust/C++/Go to Wasm, JS interop and the boundary marshalling cost, WASI and s... |
| `agency-wechat-mini-program-developer` | [[.agents/skills/engineering-wechat-mini-program-developer/SKILL|WeChat Mini Program Developer Agent Personality]] | Expert WeChat Mini Program developer specializing in 小程序 development with WXML/WXSS/WXS, WeChat API integration, paym... |
| `agency-wordpress-performance-engineer` | [[.agents/skills/engineering-wordpress-performance/SKILL|WordPress Performance Engineer]] | Expert WordPress performance engineer specializing in Core Web Vitals, object caching (Redis/Memcached), page caching... |
| `agency-wordpress-shopping-cart-engineer` | [[.agents/skills/engineering-wordpress-shopping-cart/SKILL|WordPress Shopping Cart Engineer]] | Expert WordPress e-commerce engineer specializing in WooCommerce for product catalog management, payment gateway inte... |
| `security` | [[.agents/skills/security/SKILL|Security & Compliance Skill]] | Audits code, dependencies, environment configs, and registries for vulnerabilities, secrets leakage, and compliance r... |
| `testing` | [[.agents/skills/testing/SKILL|Testing Skill]] | Governs test execution, validation frameworks, and quality verification across the ecosystem. Use when running unit t... |

---

## Finance, Accounting & Capital Formation (8)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-accounts-payable-agent` | [[.agents/skills/accounts-payable-agent/SKILL|Accounts Payable Agent Personality]] | Autonomous payment processing specialist that executes vendor payments, contractor invoices, and recurring bills acro... |
| `agency-bookkeeper-controller` | [[.agents/skills/finance-bookkeeper-controller/SKILL|Bookkeeper & Controller Agent]] | Expert bookkeeper and controller specializing in day-to-day accounting operations, financial reconciliations, month-e... |
| `agency-chief-financial-officer` | [[.agents/skills/chief-financial-officer/SKILL|Chief Financial Officer Agent]] | Strategic finance executive who governs capital allocation, treasury operations, financial planning, M&A finance, inv... |
| `agency-financial-analyst` | [[.agents/skills/finance-financial-analyst/SKILL|Financial Analyst Agent]] | Expert financial analyst specializing in financial modeling, forecasting, scenario analysis, and data-driven decision... |
| `agency-fp-a-analyst` | [[.agents/skills/finance-fpa-analyst/SKILL|FP&A Analyst Agent]] | Expert Financial Planning & Analysis (FP&A) analyst specializing in budgeting, variance analysis, financial planning,... |
| `agency-grant-writer` | [[.agents/skills/grant-writer/SKILL|Grant Writer]] | Expert grant writing specialist for nonprofits, research institutions, and social enterprises — covering prospect res... |
| `agency-investment-researcher` | [[.agents/skills/finance-investment-researcher/SKILL|Investment Researcher Agent]] | Expert investment researcher specializing in market research, due diligence, portfolio analysis, and asset valuation.... |
| `agency-tax-strategist` | [[.agents/skills/finance-tax-strategist/SKILL|Tax Strategist Agent]] | Expert tax strategist specializing in tax optimization, multi-jurisdictional compliance, transfer pricing, and strate... |

---

## GIS & Geospatial Intelligence (13)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-3d-scene-developer` | [[.agents/skills/gis-3d-scene-developer/SKILL|3DSceneDeveloper Agent Personality]] | Web 3D visualization specialist who creates immersive 3D scenes, terrain models, point cloud visualizations, and inte... |
| `agency-bim-gis-specialist` | [[.agents/skills/gis-bim-specialist/SKILL|BIMGISS Specialist Agent Personality]] | Integration specialist who bridges Building Information Modeling and Geographic Information Systems — Revit/IFC data ... |
| `agency-cartography-designer` | [[.agents/skills/gis-cartography-designer/SKILL|CartographyDesigner Agent Personality]] | Map aesthetics specialist who designs beautiful, readable, and effective maps — color theory, typography, label place... |
| `agency-drone-reality-mapping-specialist` | [[.agents/skills/gis-drone-reality-mapping/SKILL|DroneRealityMapping Agent Personality]] | Photogrammetry and reality capture expert who processes drone imagery into orthomosaics, digital terrain models, poin... |
| `agency-geoai-ml-engineer` | [[.agents/skills/gis-geoai-ml-engineer/SKILL|GeoAIMLEngineer Agent Personality]] | Geospatial machine learning specialist who builds models for feature extraction, object detection, image segmentation... |
| `agency-geoprocessing-specialist` | [[.agents/skills/gis-geoprocessing-specialist/SKILL|GeoprocessingSpecialist Agent Personality]] | ArcPy and Python toolbox expert who automates spatial workflows — builds .pyt toolboxes, Model Builder processes, bat... |
| `agency-gis-analyst` | [[.agents/skills/gis-analyst/SKILL|GISAnalyst Agent Personality]] | Day-to-day GIS operator who creates maps, manages layers, performs spatial queries, and maintains geospatial data int... |
| `agency-gis-qa-engineer` | [[.agents/skills/gis-qa-engineer/SKILL|GISQAEngineer Agent Personality]] | Quality assurance specialist who validates geospatial data integrity — topology checks, metadata audits, CRS consiste... |
| `agency-solution-engineer` | [[.agents/skills/gis-solution-engineer/SKILL|GISSolutionEngineer Agent Personality]] | Hands-on GIS prototype builder who takes strategy from Technical Consultant and turns it into working demos, proof-of... |
| `agency-spatial-data-engineer` | [[.agents/skills/gis-spatial-data-engineer/SKILL|SpatialDataEngineer Agent Personality]] | ETL specialist who transforms messy geospatial data from any source into clean, standardized, production-ready datase... |
| `agency-spatial-data-scientist` | [[.agents/skills/gis-spatial-data-scientist/SKILL|SpatialDataScientist Agent Personality]] | Advanced spatial analytics specialist who applies statistical modeling, spatial econometrics, clustering, and predict... |
| `agency-technical-consultant` | [[.agents/skills/gis-technical-consultant/SKILL|GISTechnicalConsultant Agent Personality]] | Strategic GIS advisor who translates business problems into geospatial solutions — gap analysis, technology roadmaps,... |
| `agency-web-gis-developer` | [[.agents/skills/gis-web-gis-developer/SKILL|WebGISDeveloper Agent Personality]] | Full-stack web GIS engineer who builds interactive mapping applications — MapLibre GL JS, ArcGIS JS API, Leaflet, rea... |

---

## Game Development & Interactive Worlds (21)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-blender-add-on-engineer` | [[.agents/skills/blender-addon-engineer/SKILL|Blender Add-on Engineer Agent Personality]] | Blender tooling specialist - Builds Python add-ons, asset validators, exporters, and pipeline automations that turn r... |
| `agency-economy-designer` | [[.agents/skills/economy-designer/SKILL|Economy Designer Agent Personality]] | Virtual economy architect - Masters currency systems, sources and sinks, monetization modeling, inflation control, an... |
| `agency-game-audio-engineer` | [[.agents/skills/game-audio-engineer/SKILL|Game Audio Engineer Agent Personality]] | Interactive audio specialist - Masters FMOD/Wwise integration, adaptive music systems, spatial audio, and audio perfo... |
| `agency-game-designer` | [[.agents/skills/game-designer/SKILL|Game Designer Agent Personality]] | Systems and mechanics architect - Masters GDD authorship, player psychology, economy balancing, and gameplay loop des... |
| `agency-godot-gameplay-scripter` | [[.agents/skills/godot-gameplay-scripter/SKILL|Godot Gameplay Scripter Agent Personality]] | Composition and signal integrity specialist - Masters GDScript 2.0, C# integration, node-based architecture, and type... |
| `agency-godot-multiplayer-engineer` | [[.agents/skills/godot-multiplayer-engineer/SKILL|Godot Multiplayer Engineer Agent Personality]] | Godot 4 networking specialist - Masters the MultiplayerAPI, scene replication, ENet/WebRTC transport, RPCs, and autho... |
| `agency-godot-shader-developer` | [[.agents/skills/godot-shader-developer/SKILL|Godot Shader Developer Agent Personality]] | Godot 4 visual effects specialist - Masters the Godot Shading Language (GLSL-like), VisualShader editor, CanvasItem a... |
| `agency-level-designer` | [[.agents/skills/level-designer/SKILL|Level Designer Agent Personality]] | Spatial storytelling and flow specialist - Masters layout theory, pacing architecture, encounter design, and environm... |
| `agency-narrative-designer` | [[.agents/skills/narrative-designer/SKILL|Narrative Designer Agent Personality]] | Story systems and dialogue architect - Masters GDD-aligned narrative design, branching dialogue, lore architecture, a... |
| `agency-roblox-avatar-creator` | [[.agents/skills/roblox-avatar-creator/SKILL|Roblox Avatar Creator Agent Personality]] | Roblox UGC and avatar pipeline specialist - Masters Roblox's avatar system, UGC item creation, accessory rigging, tex... |
| `agency-roblox-experience-designer` | [[.agents/skills/roblox-experience-designer/SKILL|Roblox Experience Designer Agent Personality]] | Roblox platform UX and monetization specialist - Masters engagement loop design, DataStore-driven progression, Roblox... |
| `agency-roblox-systems-scripter` | [[.agents/skills/roblox-systems-scripter/SKILL|Roblox Systems Scripter Agent Personality]] | Roblox platform engineering specialist - Masters Luau, the client-server security model, RemoteEvents/RemoteFunctions... |
| `agency-technical-artist` | [[.agents/skills/technical-artist/SKILL|Technical Artist Agent Personality]] | Art-to-engine pipeline specialist - Masters shaders, VFX systems, LOD pipelines, performance budgeting, and cross-eng... |
| `agency-unity-architect` | [[.agents/skills/unity-architect/SKILL|Unity Architect Agent Personality]] | Data-driven modularity specialist - Masters ScriptableObjects, decoupled systems, and single-responsibility component... |
| `agency-unity-editor-tool-developer` | [[.agents/skills/unity-editor-tool-developer/SKILL|Unity Editor Tool Developer Agent Personality]] | Unity editor automation specialist - Masters custom EditorWindows, PropertyDrawers, AssetPostprocessors, ScriptedImpo... |
| `agency-unity-multiplayer-engineer` | [[.agents/skills/unity-multiplayer-engineer/SKILL|Unity Multiplayer Engineer Agent Personality]] | Networked gameplay specialist - Masters Netcode for GameObjects, Unity Gaming Services (Relay/Lobby), client-server a... |
| `agency-unity-shader-graph-artist` | [[.agents/skills/unity-shader-graph-artist/SKILL|Unity Shader Graph Artist Agent Personality]] | Visual effects and material specialist - Masters Unity Shader Graph, HLSL, URP/HDRP rendering pipelines, and custom p... |
| `agency-unreal-multiplayer-architect` | [[.agents/skills/unreal-multiplayer-architect/SKILL|Unreal Multiplayer Architect Agent Personality]] | Unreal Engine networking specialist - Masters Actor replication, GameMode/GameState architecture, server-authoritativ... |
| `agency-unreal-systems-engineer` | [[.agents/skills/unreal-systems-engineer/SKILL|Unreal Systems Engineer Agent Personality]] | Performance and hybrid architecture specialist - Masters C++/Blueprint continuum, Nanite geometry, Lumen GI, and Game... |
| `agency-unreal-technical-artist` | [[.agents/skills/unreal-technical-artist/SKILL|Unreal Technical Artist Agent Personality]] | Unreal Engine visual pipeline specialist - Masters the Material Editor, Niagara VFX, Procedural Content Generation, a... |
| `agency-unreal-world-builder` | [[.agents/skills/unreal-world-builder/SKILL|Unreal World Builder Agent Personality]] | Open-world and environment specialist - Masters UE5 World Partition, Landscape, procedural foliage, HLOD, and large-s... |

---

## Healthcare, Clinical & Life Systems (7)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-aging-parent-care-companion` | [[.agents/skills/healthcare-aging-parent-care-companion/SKILL|Aging Parent Care Companion]] | Compassionate, HIPAA-aligned care coordination and decision-support agent for family caregivers managing an aging par... |
| `agency-clinical-evidence-agent` | [[.agents/skills/healthcare-clinical-evidence-agent/SKILL|Clinical Evidence Agent]] | Evidence standards and clinical credibility framework for AI agents |
| `agency-healthcare-customer-service` | [[.agents/skills/healthcare-customer-service/SKILL|Healthcare Customer Service Agent]] | Empathetic healthcare customer service specialist for patient support, billing inquiries, appointment management, ins... |
| `agency-healthcare-innovation-strategist` | [[.agents/skills/healthcare-innovation-strategist/SKILL|Healthcare Innovation Strategist]] | Strategic narrative architect for healthcare founders operating at |
| `agency-healthcare-marketing-compliance-specialist` | [[.agents/skills/healthcare-marketing-compliance/SKILL|Healthcare Marketing Compliance Specialist]] | Expert in healthcare marketing compliance in China, proficient in the Advertising Law, Medical Advertisement Manageme... |
| `agency-medical-billing-coding-specialist` | [[.agents/skills/medical-billing-coding-specialist/SKILL|Medical Billing & Coding Specialist]] | Expert medical billing and coding specialist for ICD-10-CM/PCS, CPT, and HCPCS coding, claim submission, denial manag... |
| `agency-sovereign-health-systems-agent` | [[.agents/skills/healthcare-sovereign-health-systems-agent/SKILL|Sovereign Health Systems Agent]] | Government health mandate engagement framework for AI agents |

---

## Marketing, Content & Growth (36)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-aeo-foundations-architect` | [[.agents/skills/marketing-aeo-foundations/SKILL|AEO Foundations Architect]] | Expert in AI Engine Optimization infrastructure — implements llms.txt, AI-aware robots.txt, token-budgeted content, s... |
| `agency-agentic-search-optimizer` | [[.agents/skills/marketing-agentic-search-optimizer/SKILL|Agentic Search Optimizer]] | Expert in WebMCP readiness and agentic task completion — audits whether AI agents can actually accomplish tasks on yo... |
| `agency-ai-citation-strategist` | [[.agents/skills/marketing-ai-citation-strategist/SKILL|AI Citation Strategist]] | Expert in AI recommendation engine optimization (AEO/GEO) — audits brand visibility across ChatGPT, Claude, Gemini, a... |
| `agency-app-store-optimizer` | [[.agents/skills/marketing-app-store-optimizer/SKILL|App Store Optimizer Agent Personality]] | Expert app store marketing specialist focused on App Store Optimization (ASO), conversion rate optimization, and app ... |
| `agency-baidu-seo-specialist` | [[.agents/skills/marketing-baidu-seo-specialist/SKILL|Marketing Baidu SEO Specialist]] | Expert Baidu search optimization specialist focused on Chinese search engine ranking, Baidu ecosystem integration, IC... |
| `agency-bilibili-content-strategist` | [[.agents/skills/marketing-bilibili-content-strategist/SKILL|Marketing Bilibili Content Strategist]] | Expert Bilibili marketing specialist focused on UP主 growth, danmaku culture mastery, B站 algorithm optimization, commu... |
| `agency-book-co-author` | [[.agents/skills/marketing-book-co-author/SKILL|Book Co-Author]] | Strategic thought-leadership book collaborator for founders, experts, and operators turning voice notes, fragments, a... |
| `agency-carousel-growth-engine` | [[.agents/skills/marketing-carousel-growth-engine/SKILL|Marketing Carousel Growth Engine]] | Autonomous TikTok and Instagram carousel generation specialist. Analyzes any website URL with Playwright, generates v... |
| `agency-china-e-commerce-operator` | [[.agents/skills/marketing-china-ecommerce-operator/SKILL|Marketing China E-Commerce Operator]] | Expert China e-commerce operations specialist covering Taobao, Tmall, Pinduoduo, and JD ecosystems with deep expertis... |
| `agency-china-market-localization-strategist` | [[.agents/skills/marketing-china-market-localization-strategist/SKILL|China Market Localization Strategist]] | Full-stack China market localization expert who transforms real-time trend signals into executable go-to-market strat... |
| `agency-content-creator` | [[.agents/skills/marketing-content-creator/SKILL|Marketing Content Creator Agent]] | Expert content strategist and creator for multi-platform campaigns. Develops editorial calendars, creates compelling ... |
| `agency-cross-border-e-commerce-specialist` | [[.agents/skills/marketing-cross-border-ecommerce/SKILL|Marketing Cross-Border E-Commerce Specialist]] | Full-funnel cross-border e-commerce strategist covering Amazon, Shopee, Lazada, AliExpress, Temu, and TikTok Shop ope... |
| `agency-douyin-strategist` | [[.agents/skills/marketing-douyin-strategist/SKILL|Marketing Douyin Strategist]] | Short-video marketing expert specializing in the Douyin platform, with deep expertise in recommendation algorithm mec... |
| `agency-email-marketing-strategist` | [[.agents/skills/marketing-email-strategist/SKILL|Email Marketing Strategist]] | Expert email marketing strategist for CRM-driven campaigns, lifecycle automation, segmentation architecture, and deli... |
| `agency-global-podcast-strategist` | [[.agents/skills/marketing-global-podcast-strategist/SKILL|Marketing Global Podcast Strategist]] | Expert podcast growth specialist focused on show positioning, audience development, content strategy, and monetisatio... |
| `agency-growth-hacker` | [[.agents/skills/marketing-growth-hacker/SKILL|Marketing Growth Hacker Agent]] | Expert growth strategist specializing in rapid user acquisition through data-driven experimentation. Develops viral l... |
| `agency-instagram-curator` | [[.agents/skills/marketing-instagram-curator/SKILL|Marketing Instagram Curator]] | Expert Instagram marketing specialist focused on visual storytelling, community building, and multi-format content op... |
| `agency-kuaishou-strategist` | [[.agents/skills/marketing-kuaishou-strategist/SKILL|Marketing Kuaishou Strategist]] | Expert Kuaishou marketing strategist specializing in short-video content for China's lower-tier city markets, live co... |
| `agency-linkedin-content-creator` | [[.agents/skills/marketing-linkedin-content-creator/SKILL|LinkedIn Content Creator]] | Expert LinkedIn content strategist focused on thought leadership, personal brand building, and high-engagement profes... |
| `agency-livestream-commerce-coach` | [[.agents/skills/marketing-livestream-commerce-coach/SKILL|Marketing Livestream Commerce Coach]] | Veteran livestream e-commerce coach specializing in host training and live room operations across Douyin, Kuaishou, T... |
| `agency-multi-platform-publisher` | [[.agents/skills/marketing-multi-platform-publisher/SKILL|Multi-Platform Publisher]] | Expert orchestrator for one-click Chinese blog publishing. Routes a single article to 知乎 / 小红书 / CSDN / B站 / 公众号 / 掘金... |
| `agency-podcast-strategist` | [[.agents/skills/marketing-podcast-strategist/SKILL|Marketing Podcast Strategist]] | Content strategy and operations expert for the Chinese podcast market, with deep expertise in Xiaoyuzhou, Ximalaya, a... |
| `agency-pr-communications-manager` | [[.agents/skills/marketing-pr-communications-manager/SKILL|PR & Communications Manager]] | Strategic public relations and communications specialist for media relations, press releases, crisis communications, ... |
| `agency-private-domain-operator` | [[.agents/skills/marketing-private-domain-operator/SKILL|Marketing Private Domain Operator]] | Expert in building enterprise WeChat (WeCom) private domain ecosystems, with deep expertise in SCRM systems, segmente... |
| `agency-reddit-community-builder` | [[.agents/skills/marketing-reddit-community-builder/SKILL|Marketing Reddit Community Builder]] | Expert Reddit marketing specialist focused on authentic community engagement, value-driven content creation, and long... |
| `agency-seo-specialist` | [[.agents/skills/marketing-seo-specialist/SKILL|Marketing SEO Specialist]] | Expert search engine optimization strategist specializing in technical SEO, content optimization, link authority buil... |
| `agency-short-video-editing-coach` | [[.agents/skills/marketing-short-video-editing-coach/SKILL|Marketing Short-Video Editing Coach]] | Hands-on short-video editing coach covering the full post-production pipeline, with mastery of CapCut Pro, Premiere P... |
| `agency-social-media-strategist` | [[.agents/skills/marketing-social-media-strategist/SKILL|Social Media Strategist Agent]] | Expert social media strategist for LinkedIn, Twitter, and professional platforms. Creates cross-platform campaigns, b... |
| `agency-tiktok-strategist` | [[.agents/skills/marketing-tiktok-strategist/SKILL|Marketing TikTok Strategist]] | Expert TikTok marketing specialist focused on viral content creation, algorithm optimization, and community building.... |
| `agency-twitter-engager` | [[.agents/skills/marketing-twitter-engager/SKILL|Marketing Twitter Engager]] | Expert Twitter marketing specialist focused on real-time engagement, thought leadership building, and community-drive... |
| `agency-video-optimization-specialist` | [[.agents/skills/marketing-video-optimization-specialist/SKILL|Marketing Video Optimization Specialist Agent]] | Video marketing strategist specializing in YouTube algorithm optimization, audience retention, chaptering, thumbnail ... |
| `agency-wechat-official-account-manager` | [[.agents/skills/marketing-wechat-official-account/SKILL|Marketing WeChat Official Account Manager]] | Expert WeChat Official Account (OA) strategist specializing in content marketing, subscriber engagement, and conversi... |
| `agency-weibo-strategist` | [[.agents/skills/marketing-weibo-strategist/SKILL|Marketing Weibo Strategist]] | Full-spectrum operations expert for Sina Weibo, with deep expertise in trending topic mechanics, Super Topic communit... |
| `agency-x-twitter-intelligence-analyst` | [[.agents/skills/marketing-x-twitter-intelligence-analyst/SKILL|Marketing X/Twitter Intelligence Analyst]] | Social intelligence specialist for X/Twitter research, trend detection, account monitoring, and evidence-backed audie... |
| `agency-xiaohongshu-specialist` | [[.agents/skills/marketing-xiaohongshu-specialist/SKILL|Marketing Xiaohongshu Specialist]] | Expert Xiaohongshu marketing specialist focused on lifestyle content, trend-driven strategies, and authentic communit... |
| `agency-zhihu-strategist` | [[.agents/skills/marketing-zhihu-strategist/SKILL|Marketing Zhihu Strategist]] | Expert Zhihu marketing specialist focused on thought leadership, community credibility, and knowledge-driven engageme... |

---

## Official Platform & Infrastructure (VoltAgent) (5)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `official-cloudflare-workers` | [[.agents/skills/official-cloudflare-workers/SKILL|Official Cloudflare Workers Skill]] | Official Cloudflare Workers and edge computing skill covering V8 isolate runtimes, KV storage, D1 SQL, Queues, R2 obj... |
| `official-stripe-integration` | [[.agents/skills/official-stripe-integration/SKILL|Official Stripe Integration Skill]] | Official Stripe payment integration skill covering PaymentIntents, idempotent webhook processing, Checkout Sessions, ... |
| `official-supabase-architecture` | [[.agents/skills/official-supabase-architecture/SKILL|Official Supabase Architecture Skill]] | Official Supabase architecture and database engineering skill covering Row Level Security (RLS), multi-tenant schemas... |
| `official-terraform-iac` | [[.agents/skills/official-terraform-iac/SKILL|Official Terraform & IaC Skill]] | Official Terraform and OpenTofu infrastructure-as-code (IaC) skill covering declarative HCL, remote state locking, mo... |
| `official-trailofbits-appsec` | [[.agents/skills/official-trailofbits-appsec/SKILL|Official Trail of Bits AppSec Skill]] | Official Trail of Bits Application Security (AppSec) skill covering static analysis (Semgrep, CodeQL), cryptographic ... |

---

## Paid Media & Ad Optimization (7)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-ad-creative-strategist` | [[.agents/skills/paid-media-creative-strategist/SKILL|Paid Media Ad Creative Strategist Agent]] | Paid media creative specialist focused on ad copywriting, RSA optimization, asset group design, and creative testing ... |
| `agency-paid-media-auditor` | [[.agents/skills/paid-media-auditor/SKILL|Paid Media Auditor Agent]] | Comprehensive paid media auditor who systematically evaluates Google Ads, Microsoft Ads, and Meta accounts across 200... |
| `agency-paid-social-strategist` | [[.agents/skills/paid-media-paid-social-strategist/SKILL|Paid Media Paid Social Strategist Agent]] | Cross-platform paid social advertising specialist covering Meta (Facebook/Instagram), LinkedIn, TikTok, Pinterest, X,... |
| `agency-ppc-campaign-strategist` | [[.agents/skills/paid-media-ppc-strategist/SKILL|Paid Media PPC Campaign Strategist Agent]] | Senior paid media strategist specializing in large-scale search, shopping, and performance max campaign architecture ... |
| `agency-programmatic-display-buyer` | [[.agents/skills/paid-media-programmatic-buyer/SKILL|Paid Media Programmatic & Display Buyer Agent]] | Display advertising and programmatic media buying specialist covering managed placements, Google Display Network, DV3... |
| `agency-search-query-analyst` | [[.agents/skills/paid-media-search-query-analyst/SKILL|Paid Media Search Query Analyst Agent]] | Specialist in search term analysis, negative keyword architecture, and query-to-intent mapping. Turns raw search quer... |
| `agency-tracking-measurement-specialist` | [[.agents/skills/paid-media-tracking-specialist/SKILL|Paid Media Tracking & Measurement Specialist Agent]] | Expert in conversion tracking architecture, tag management, and attribution modeling across Google Tag Manager, GA4, ... |

---

## Product Strategy & Behavioral Nudge (6)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-behavioral-nudge-engine` | [[.agents/skills/product-behavioral-nudge-engine/SKILL|Behavioral Nudge Engine]] | Behavioral psychology specialist that adapts software interaction cadences and styles to maximize user motivation and... |
| `agency-feedback-synthesizer` | [[.agents/skills/product-feedback-synthesizer/SKILL|Product Feedback Synthesizer Agent]] | Expert in collecting, analyzing, and synthesizing user feedback from multiple channels to extract actionable product ... |
| `agency-product-manager` | [[.agents/skills/product-manager/SKILL|Product Manager Agent]] | Holistic product leader who owns the full product lifecycle — from discovery and strategy through roadmap, stakeholde... |
| `agency-resume-tailor` | [[.agents/skills/resume-tailor/SKILL|Resume Tailor Agent]] | Candidate-side resume optimization specialist who analyzes job descriptions, maps real experience to role requirement... |
| `agency-sprint-prioritizer` | [[.agents/skills/product-sprint-prioritizer/SKILL|Product Sprint Prioritizer Agent]] | Expert product manager specializing in agile sprint planning, feature prioritization, and resource allocation. Focuse... |
| `agency-trend-researcher` | [[.agents/skills/product-trend-researcher/SKILL|Product Trend Researcher Agent]] | Expert market intelligence analyst specializing in identifying emerging trends, competitive analysis, and opportunity... |

---

## Project Management & Delivery Operations (7)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-experiment-tracker` | [[.agents/skills/project-management-experiment-tracker/SKILL|Experiment Tracker Agent Personality]] | Expert project manager specializing in experiment design, execution tracking, and data-driven decision making. Focuse... |
| `agency-jira-workflow-steward` | [[.agents/skills/project-management-jira-workflow-steward/SKILL|Jira Workflow Steward Agent]] | Expert delivery operations specialist who enforces Jira-linked Git workflows, traceable commits, structured pull requ... |
| `agency-meeting-notes-specialist` | [[.agents/skills/project-management-meeting-notes-specialist/SKILL|Meeting Notes Specialist]] | Extract structured decisions, action items, and open questions from meeting transcripts or rough notes into a clean 4... |
| `agency-project-shepherd` | [[.agents/skills/project-management-project-shepherd/SKILL|Project Shepherd Agent Personality]] | Expert project manager specializing in cross-functional project coordination, timeline management, and stakeholder al... |
| `agency-senior-project-manager` | [[.agents/skills/project-manager-senior/SKILL|Project Manager Agent Personality]] | Converts specs to tasks and remembers previous projects. Focused on realistic scope, no background processes, exact s... |
| `agency-studio-operations` | [[.agents/skills/project-management-studio-operations/SKILL|Studio Operations Agent Personality]] | Expert operations manager specializing in day-to-day studio efficiency, process optimization, and resource coordinati... |
| `agency-studio-producer` | [[.agents/skills/project-management-studio-producer/SKILL|Studio Producer Agent Personality]] | Senior strategic leader specializing in high-level creative and technical project orchestration, resource allocation,... |

---

## Sales, Deals & Outbound Pipeline (11)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-account-strategist` | [[.agents/skills/sales-account-strategist/SKILL|Account Strategist Agent]] | Expert post-sale account strategist specializing in land-and-expand execution, stakeholder mapping, QBR facilitation,... |
| `agency-deal-strategist` | [[.agents/skills/sales-deal-strategist/SKILL|Deal Strategist Agent]] | Senior deal strategist specializing in MEDDPICC qualification, competitive positioning, and win planning for complex ... |
| `agency-discovery-coach` | [[.agents/skills/sales-discovery-coach/SKILL|Discovery Coach Agent]] | Coaches sales teams on elite discovery methodology — question design, current-state mapping, gap quantification, and ... |
| `agency-offer-lead-gen-strategist` | [[.agents/skills/sales-offer-lead-gen-strategist/SKILL|Offer & Lead Gen Strategist]] | Top-of-funnel architect who designs irresistible offers and lead magnets that attract qualified buyers at scale. Spec... |
| `agency-outbound-strategist` | [[.agents/skills/sales-outbound-strategist/SKILL|Outbound Strategist Agent]] | Signal-based outbound specialist who designs multi-channel prospecting sequences, defines ICPs, and builds pipeline t... |
| `agency-pipeline-analyst` | [[.agents/skills/sales-pipeline-analyst/SKILL|Pipeline Analyst Agent]] | Revenue operations analyst specializing in pipeline health diagnostics, deal velocity analysis, forecast accuracy, an... |
| `agency-proposal-strategist` | [[.agents/skills/sales-proposal-strategist/SKILL|Proposal Strategist Agent]] | Strategic proposal architect who transforms RFPs and sales opportunities into compelling win narratives. Specializes ... |
| `agency-sales-coach` | [[.agents/skills/sales-coach/SKILL|Sales Coach Agent]] | Expert sales coaching specialist focused on rep development, pipeline review facilitation, call coaching, deal strate... |
| `agency-sales-data-extraction-agent` | [[.agents/skills/sales-data-extraction-agent/SKILL|Sales Data Extraction Agent]] | AI agent specialized in monitoring Excel files and extracting key sales metrics (MTD, YTD, Year End) for internal liv... |
| `agency-sales-engineer` | [[.agents/skills/sales-engineer/SKILL|Sales Engineer Agent]] | Senior pre-sales engineer specializing in technical discovery, demo engineering, POC scoping, competitive battlecards... |
| `agency-sales-outreach` | [[.agents/skills/sales-outreach/SKILL|Sales Outreach Agent]] | Consultative B2B sales outreach specialist for cold prospecting, lead follow-up, objection handling, proposal writing... |

---

## Security, AppSec & Cryptographic Compliance (13)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-ai-generated-code-security-auditor` | [[.agents/skills/security-ai-generated-code-auditor/SKILL|AI-Generated Code Security Auditor]] | Security reviewer for AI-generated and vibe-coded apps — hunts the hardcoded secrets, broken row-level security, and ... |
| `agency-application-security-engineer` | [[.agents/skills/security-appsec-engineer/SKILL|Application Security Engineer]] | AppSec specialist who secures the software development lifecycle through threat modeling, secure code review, SAST/DA... |
| `agency-blockchain-security-auditor` | [[.agents/skills/security-blockchain-security-auditor/SKILL|Blockchain Security Auditor]] | Expert smart contract security auditor specializing in vulnerability detection, formal verification, exploit analysis... |
| `agency-cloud-security-architect` | [[.agents/skills/security-cloud-security-architect/SKILL|Cloud Security Architect]] | Cloud-native security specialist designing zero trust architectures, implementing defense-in-depth across AWS, Azure,... |
| `agency-compliance-auditor` | [[.agents/skills/security-compliance-auditor/SKILL|Compliance Auditor Agent]] | Expert technical compliance auditor specializing in SOC 2, ISO 27001, HIPAA, and PCI-DSS audits — from readiness asse... |
| `agency-incident-responder` | [[.agents/skills/security-incident-responder/SKILL|Incident Responder]] | Digital forensics and incident response specialist who leads breach investigations, contains active threats, coordina... |
| `agency-penetration-tester` | [[.agents/skills/security-penetration-tester/SKILL|Penetration Tester]] | Offensive security specialist conducting authorized penetration tests, red team operations, and vulnerability assessm... |
| `agency-secrets-credential-hygiene-engineer` | [[.agents/skills/security-secrets-credential-engineer/SKILL|Secrets & Credential Hygiene Engineer]] | Owns the full lifecycle of secrets and credentials — detection, prevention, vaulting, rotation, and leak response — s... |
| `agency-security-architect` | [[.agents/skills/security-architect/SKILL|Security Architect Agent]] | Expert security architect specializing in threat modeling, secure-by-design architecture, trust-boundary analysis, de... |
| `agency-senior-secops-engineer` | [[.agents/skills/security-senior-secops/SKILL|Senior SecOps Engineer]] | Defensive application security specialist who scans every code submission for secrets and sensitive data exposure bef... |
| `agency-threat-detection-engineer` | [[.agents/skills/security-threat-detection-engineer/SKILL|Threat Detection Engineer Agent]] | Expert detection engineer specializing in SIEM rule development, MITRE ATT&CK coverage mapping, threat hunting, alert... |
| `agency-threat-intelligence-analyst` | [[.agents/skills/security-threat-intelligence-analyst/SKILL|Threat Intelligence Analyst]] | Cyber threat intelligence specialist who tracks adversary groups, maps attack campaigns to MITRE ATT&CK, produces act... |
| `agency-zk-steward` | [[.agents/skills/zk-steward/SKILL|ZK Steward Agent]] | Knowledge-base steward in the spirit of Niklas Luhmann's Zettelkasten. Default perspective: Luhmann; switches to doma... |

---

## Spatial Computing, XR & 3D (5)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-macos-spatial-metal-engineer` | [[.agents/skills/macos-spatial-metal-engineer/SKILL|macOS Spatial/Metal Engineer Agent Personality]] | Native Swift and Metal specialist building high-performance 3D rendering systems and spatial computing experiences fo... |
| `agency-visionos-spatial-engineer` | [[.agents/skills/visionos-spatial-engineer/SKILL|visionOS Spatial Engineer]] | Native visionOS spatial computing, SwiftUI volumetric interfaces, and Liquid Glass design implementation |
| `agency-xr-cockpit-interaction-specialist` | [[.agents/skills/xr-cockpit-interaction-specialist/SKILL|XR Cockpit Interaction Specialist Agent Personality]] | Specialist in designing and developing immersive cockpit-based control systems for XR environments |
| `agency-xr-immersive-developer` | [[.agents/skills/xr-immersive-developer/SKILL|XR Immersive Developer Agent Personality]] | Expert WebXR and immersive technology developer with specialization in browser-based AR/VR/XR applications |
| `agency-xr-interface-architect` | [[.agents/skills/xr-interface-architect/SKILL|XR Interface Architect Agent Personality]] | Spatial interaction designer and interface strategist for immersive AR/VR/XR environments |

---

## Specialized Domains & Cultural Navigation (20)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-chief-of-staff` | [[.agents/skills/specialized-chief-of-staff/SKILL|Chief of Staff]] | Master coordinator for founders and executives — filters noise, owns processes, enforces consistency, routes decision... |
| `agency-civil-engineer` | [[.agents/skills/specialized-civil-engineer/SKILL|Civil Engineer Agent]] | Expert civil and structural engineer with global standards coverage — Eurocode, DIN, ACI, AISC, ASCE, AS/NZS, CSA, GB... |
| `agency-codebase-archaeologist` | [[.agents/skills/specialized-codebase-archaeologist/SKILL|Codebase Archaeologist Agent Personality]] | Multi-session, multi-tool drift detection specialist who audits codebases touched by several AI coding tools (Claude,... |
| `agency-cultural-intelligence-strategist` | [[.agents/skills/specialized-cultural-intelligence-strategist/SKILL|Cultural Intelligence Strategist]] | CQ specialist that detects invisible exclusion, researches global context, and ensures software resonates authentical... |
| `agency-developer-advocate` | [[.agents/skills/specialized-developer-advocate/SKILL|Developer Advocate Agent]] | Expert developer advocate specializing in building developer communities, creating compelling technical content, opti... |
| `agency-document-generator` | [[.agents/skills/specialized-document-generator/SKILL|Document Generator Agent]] | Expert document creation specialist who generates professional PDF, PPTX, DOCX, and XLSX files using code-based appro... |
| `agency-fedramp-rmf-compliance-engineer` | [[.agents/skills/specialized-fedramp-rmf-compliance/SKILL|FedRAMP & RMF Compliance Engineer]] | Expert FedRAMP and NIST Risk Management Framework compliance engineer specializing in both FedRAMP authorization path... |
| `agency-french-consulting-market-navigator` | [[.agents/skills/specialized-french-consulting-market/SKILL|French Consulting Market Navigator]] | Navigate the French ESN/SI freelance ecosystem — margin models, platform mechanics (Malt, collective.work), portage s... |
| `agency-government-digital-presales-consultant` | [[.agents/skills/government-digital-presales-consultant/SKILL|Government Digital Presales Consultant]] | Presales expert for China's government digital transformation market (ToG), proficient in policy interpretation, solu... |
| `agency-korean-business-navigator` | [[.agents/skills/specialized-korean-business-navigator/SKILL|Your Identity & Memory]] | Korean business culture for foreign professionals — 품의 decision process, nunchi reading, KakaoTalk business etiquette... |
| `agency-language-translator` | [[.agents/skills/language-translator/SKILL|Language Translator]] | Real-time Spanish ↔ English translation specialist with cultural context, regional dialect awareness, travel phrase g... |
| `agency-master-plan-architect` | [[.agents/skills/specialized-master-plan-architect/SKILL|Master Plan Architect & Technical Educator]] | Master planning architect, technical educator, and ruthless plan critic who specializes in deep architectural teachin... |
| `agency-mcp-builder` | [[.agents/skills/specialized-mcp-builder/SKILL|MCP Builder Agent]] | Expert Model Context Protocol developer who designs, builds, and tests MCP servers that extend AI agent capabilities ... |
| `agency-model-qa-specialist` | [[.agents/skills/specialized-model-qa/SKILL|Model QA Specialist]] | Independent model QA expert who audits ML and statistical models end-to-end - from documentation review and data reco... |
| `agency-personal-growth-mentor` | [[.agents/skills/personal-growth-mentor/SKILL|Personal Growth Mentor]] | Cross-domain personal development mentor for goal clarity, habit design, strategic decisions, and accountability with... |
| `agency-pricing-analyst` | [[.agents/skills/specialized-pricing-analyst/SKILL|Pricing Analyst Agent]] | Specialized pricing analyst who develops optimal pricing models through market research, competitor analysis, cost st... |
| `agency-salesforce-architect` | [[.agents/skills/specialized-salesforce-architect/SKILL|Salesforce Architect]] | Solution architecture for Salesforce platform — multi-cloud design, integration patterns, governor limits, deployment... |
| `agency-strategy-duel-agent` | [[.agents/skills/specialized-strategy-duel-agent/SKILL|Strategy Duel Agent]] | Conducts live strategy duels using game theory and the 36 Chinese stratagems |
| `agency-study-abroad-advisor` | [[.agents/skills/study-abroad-advisor/SKILL|Study Abroad Advisor]] | Full-spectrum study abroad planning expert covering the US, UK, Canada, Australia, Europe, Hong Kong, and Singapore —... |
| `agency-workflow-architect` | [[.agents/skills/specialized-workflow-architect/SKILL|Workflow Architect Agent Personality]] | Workflow design specialist who maps complete workflow trees for every system, user journey, and agent interaction — c... |

---

## Testing, QA & Benchmark Verification (9)

| Persona / Skill | Canonical Wiki Link | Description |
| :--- | :--- | :--- |
| `agency-accessibility-auditor` | [[.agents/skills/testing-accessibility-auditor/SKILL|Accessibility Auditor Agent Personality]] | Expert accessibility specialist who audits interfaces against WCAG standards, tests with assistive technologies, and ... |
| `agency-api-tester` | [[.agents/skills/testing-api-tester/SKILL|API Tester Agent Personality]] | Expert API testing specialist focused on comprehensive API validation, performance testing, and quality assurance acr... |
| `agency-evidence-collector` | [[.agents/skills/testing-evidence-collector/SKILL|QA Agent Personality]] | Screenshot-obsessed, fantasy-allergic QA specialist - Default to finding 3-5 issues, requires visual proof for everyt... |
| `agency-performance-benchmarker` | [[.agents/skills/testing-performance-benchmarker/SKILL|Performance Benchmarker Agent Personality]] | Expert performance testing and optimization specialist focused on measuring, analyzing, and improving system performa... |
| `agency-reality-checker` | [[.agents/skills/testing-reality-checker/SKILL|Integration Agent Personality]] | Stops fantasy approvals, evidence-based certification - Default to "NEEDS WORK", requires overwhelming proof for prod... |
| `agency-test-automation-engineer` | [[.agents/skills/testing-test-automation-engineer/SKILL|Test Automation Engineer]] | Expert end-to-end test automation engineer for Playwright and Cypress — resilient selectors, flake elimination, isola... |
| `agency-test-results-analyzer` | [[.agents/skills/testing-test-results-analyzer/SKILL|Test Results Analyzer Agent Personality]] | Expert test analysis specialist focused on comprehensive test result evaluation, quality metrics analysis, and action... |
| `agency-tool-evaluator` | [[.agents/skills/testing-tool-evaluator/SKILL|Tool Evaluator Agent Personality]] | Expert technology assessment specialist focused on evaluating, testing, and recommending tools, software, and platfor... |
| `agency-workflow-optimizer` | [[.agents/skills/testing-workflow-optimizer/SKILL|Workflow Optimizer Agent Personality]] | Expert process improvement specialist focused on analyzing, optimizing, and automating workflows across all business ... |

---
