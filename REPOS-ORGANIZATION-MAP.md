# 🗺️ REPOSITORY ORGANIZATION & CAPABILITY MAP
**Date:** 2026-08-05  
**Total Tracked Repositories:** 1,717 (886 Owned, 831 Starred)  
**Purpose:** Enable autonomous system assembly by indexing capabilities—zero new code, pure wiring from existing repos.

**Core Principle:** These 1,717 repos implement the infrastructure for the **35 Intelligence Types** in [AGENTS.md](AGENTS.md). Query this map to find which repos support each layer of autonomous decision-making.

---

## 📊 Intelligence Stack → Repository Mapping

Your repos are organized into **9 Tiers** that directly support autonomous decisions:

| Tier | Intelligence Type | Uses These Repos | Output |
|---|----|---|---|
| **1: Foundation** | Descriptive | Data storage (Supabase, Neo4j, Qdrant, Redis) | Inventory of what exists |
| **2: Intelligence** | Structural + Semantic | Code parsing (tree-sitter, Joern, LightRAG) | Structured knowledge of how it works + what it means |
| **3: Discovery** | Opportunity + Strategic | OSINT + search (maigret, llama-index, Neo4j queries) | Top opportunities ranked |
| **4: Experimentation** | Experimental + Adaptive | Sandboxing + testing (e2b, k6, Playwright, Phoenix) | Which variant wins |
| **5: Implementation** | Prescriptive | Code gen + orchestration (OpenHands, SWE-agent, langgraph) | Working PR with code |
| **6: Verification** | Risk + Security + Optimization | Testing + security (semgrep, trivy, pytest, Phoenix) | Pass/fail gate |
| **7: Deployment** | Operational | CI/CD + IaC (Vercel, ArgoCD, Terraform) | Live in production |
| **8: Observability** | Real-time + Outcome | Tracing + metrics (Langfuse, prometheus, grafana, loki) | Live performance data |
| **9: Learning** | Compounding + Recursive | Knowledge extraction (LightRAG, Neo4j, Qdrant, llama-index) | Genes/capsules for next cycle |

**The loop:** Tier 9 output → Tier 3 input → intelligence improves over time.

---

## 📋 How to Use This Map

1. **Identify intelligence needed:** What question are you answering? (Refer to [AGENTS.md](AGENTS.md))
2. **Find tier:** Which tier handles that intelligence?
3. **Query this document:** Which category in that tier applies?
4. **Find repos:** What repositories are already starred/owned?
5. **Wire them:** Query, execute, learn—no new code.

**Example:** "Find opportunities for Venture LT-011"
- Intelligence needed: **Opportunity Intelligence**
- Tier: **3 (Discovery)**
- Categories: **OSINT & Enrichment** (maigret) + **Knowledge Graphs** (Neo4j queries)
- Query: `grep "maigret\|Neo4j" | find repos in LT-011 domain`
- Execution: Run maigret enrichment on contacts → Neo4j relationship search → top opportunities
- Output: Top 5 opportunities ranked by fit

---

## 🏢 CLASSIFICATION BY BUSINESS DEPARTMENT
| Department | Core Phase | Representative Repositories | Key Capabilities |
|---|---|---|---|
| **Engineering** | Engineering | AdGuardHome, Antigravity-Manager, CF-Hero, CMSaasStarter... | ci/cd pipelines, container orchestration, credit scoring |
| **Finance & HR** | Revenue | AP2, Bayesian-Credit-Risk-Engine, Kronos, MokerSaaS... | credit scoring, database storage, visual analytics |
| **Legal & Admin** | Engineering | A-Curated-List-of-ML-System-Design-Case-Studies, AFFiNE, AntigravityManager, CodeWiki... | credit scoring, database storage, e-signature |
| **Operations** | Engineering | 300-free-resource-websites, API-mega-list, AiToEarn, AltStore... | credit scoring, database storage, order dispatch |
| **Product & R&D** | Engineering | 12-factor-agents, 500-AI-Agents-Projects, 9router, A2A... | ci/cd pipelines, container orchestration, credit scoring |
| **Sales & Marketing** | Revenue | ai-002-ml-engine, clients, comm-007-youth-leadership-ai, deliv-713-roadrunner-cannabis... | ci/cd pipelines, visual analytics |

## 🔄 CLASSIFICATION BY VENTURE LIFECYCLE PHASE
| Lifecycle Phase | Description | Key Categories | Repos Count |
|---|---|---|---|
| **Discovery** | Market validation, intelligence gathering, OSINT research, and lead sourcing. | AI / RAG Systems, OSINT & Enrichment | 423 |
| **Engineering** | Platform coding, database structuring, orchestration, infrastructure deployment. | Agentic Orchestration, Content & Document Processing, DevOps & Infrastructure, Development Tools, Knowledge Graphs, Specialized Utilities | 999 |
| **Revenue** | Monetization, financial trading, invoicing/billing, video/media marketing. | CRM & Pipeline, Finance & Trading, Video & Media Generation | 174 |
| **Learning** | System monitoring, metrics collection, telemetry analytics, and training loops. | Learning & Training, Monitoring & Observability | 121 |

## 📚 DETAILED CATEGORY INDEX

### AI / RAG Systems (397 Repositories)
| Repository / Path | Type | Department | Phase | Tool Type | Key Capabilities |
|---|---|---|---|---|---|
| `_master-governance` | 🔵 Owned | Product & R&D | Discovery | Platform | utility |
| `arbitrage-nexus` | 🔵 Owned | Product & R&D | Discovery | Application | utility |
| `career-ops` | 🔵 Owned | Product & R&D | Discovery | Application | ci/cd pipelines |
| `claude-workflow-demo` | 🔵 Owned | Product & R&D | Discovery | CLI / Tool | workflow automation |
| `ec-003-hella-scars` | 🔵 Owned | Product & R&D | Discovery | Library | utility |
| `ec-004-godbody-luxuries` | 🔵 Owned | Product & R&D | Discovery | Platform | utility |
| `ec-036-fulfillment-network-ai` | 🔵 Owned | Product & R&D | Discovery | Application | utility |
| `ec-039-visual-search-ai` | 🔵 Owned | Product & R&D | Discovery | Application | utility |
| `ec-063-ai-market-research` | 🔵 Owned | Product & R&D | Discovery | Application | utility |
| `ec-111-tve-fragrance` | 🔵 Owned | Product & R&D | Discovery | Library | utility |
| `edu-022-ai-research-assistant` | 🔵 Owned | Product & R&D | Discovery | Application | utility |
| `em-003-teleportation-research-ai` | 🔵 Owned | Product & R&D | Discovery | Application | utility |
| `enhanced-cursor-rules` | 🔵 Owned | Product & R&D | Discovery | Framework | multi-agent logic |
| `fin-036-arbitrage-nexus-platform` | 🔵 Owned | Product & R&D | Discovery | Application | utility |
| `freeclaudecode` | 🔵 Owned | Product & R&D | Discovery | Application | utility |
| *... and 382 more repositories* | | | | | |

### Agentic Orchestration (119 Repositories)
| Repository / Path | Type | Department | Phase | Tool Type | Key Capabilities |
|---|---|---|---|---|---|
| `agency-agents` | 🔵 Owned | Product & R&D | Engineering | Library | utility |
| `ai-001-ai-command-center` | 🔵 Owned | Product & R&D | Engineering | Framework | visual analytics, multi-agent logic |
| `autonomous-venture-studio` | 🔵 Owned | Product & R&D | Engineering | Framework | multi-agent logic |
| `capital-orchestrator` | 🔵 Owned | Product & R&D | Engineering | Framework | multi-agent logic |
| `civilization-os` | 🔵 Owned | Product & R&D | Engineering | Framework | utility |
| `deployment-orchestrator` | 🔵 Owned | Product & R&D | Engineering | Framework | utility |
| `ec-096-ai-fabric-advisor` | 🔵 Owned | Product & R&D | Engineering | Application | utility |
| `hermes-agent-command-center` | 🔵 Owned | Product & R&D | Engineering | Library | visual analytics |
| `iza-os-agents` | 🔵 Owned | Product & R&D | Engineering | Library | utility |
| `iza-os-ai-orchestration` | 🔵 Owned | Product & R&D | Engineering | Framework | multi-agent logic |
| `iza-os-automation` | 🔵 Owned | Product & R&D | Engineering | Framework | workflow automation, multi-agent logic |
| `iza-os-finance-advisor-orchestration-bot` | 🔵 Owned | Product & R&D | Engineering | Framework | multi-agent logic |
| `iza-os-marketing-automation-orchestration-bot` | 🔵 Owned | Product & R&D | Engineering | Framework | multi-agent logic |
| `iza-os-orchestrator` | 🔵 Owned | Product & R&D | Engineering | Framework | multi-agent logic |
| `iza-os-project-management-orchestration-bot` | 🔵 Owned | Product & R&D | Engineering | Framework | multi-agent logic |
| *... and 104 more repositories* | | | | | |

### CRM & Pipeline (42 Repositories)
| Repository / Path | Type | Department | Phase | Tool Type | Key Capabilities |
|---|---|---|---|---|---|
| `ai-002-ml-engine` | 🔵 Owned | Sales & Marketing | Revenue | Application | ci/cd pipelines |
| `clients` | 🔵 Owned | Sales & Marketing | Revenue | Library | utility |
| `comm-007-youth-leadership-ai` | 🔵 Owned | Sales & Marketing | Revenue | Application | utility |
| `deliv-713-roadrunner-cannabis` | 🔵 Owned | Sales & Marketing | Revenue | Library | visual analytics |
| `ec-038-chatbot-customer-service` | 🔵 Owned | Sales & Marketing | Revenue | Application | utility |
| `ec-060-ai-customer-loyalty` | 🔵 Owned | Sales & Marketing | Revenue | Application | utility |
| `ec-066-ai-customer-journey` | 🔵 Owned | Sales & Marketing | Revenue | Application | utility |
| `ec-074-ai-customer-segmentation` | 🔵 Owned | Sales & Marketing | Revenue | Application | utility |
| `ec-076-ai-sales-forecasting` | 🔵 Owned | Sales & Marketing | Revenue | Application | utility |
| `ec-079-ai-customer-feedback` | 🔵 Owned | Sales & Marketing | Revenue | Platform | utility |
| `ec-085-ai-customer-support` | 🔵 Owned | Sales & Marketing | Revenue | Application | utility |
| `ec-088-ai-customer-community` | 🔵 Owned | Sales & Marketing | Revenue | Application | utility |
| `iza-os-customer-core` | 🔵 Owned | Sales & Marketing | Revenue | Application | utility |
| `iza-os-customer-service-automation-bot` | 🔵 Owned | Sales & Marketing | Revenue | Application | utility |
| `iza-os-customer-service-chatbot-bot` | 🔵 Owned | Sales & Marketing | Revenue | Application | utility |
| *... and 27 more repositories* | | | | | |

### Content & Document Processing (55 Repositories)
| Repository / Path | Type | Department | Phase | Tool Type | Key Capabilities |
|---|---|---|---|---|---|
| `YES-LLC-CONTRACTOR-DELIVERY` | 🔵 Owned | Legal & Admin | Engineering | Application | utility |
| `bw-001-contracts` | 🔵 Owned | Legal & Admin | Engineering | Framework | utility |
| `bw-001-up-next-business` | 🔵 Owned | Legal & Admin | Engineering | Framework | utility |
| `bw-020-ai-nail-design-generator` | 🔵 Owned | Legal & Admin | Engineering | Application | e-signature |
| `design-system` | 🔵 Owned | Legal & Admin | Engineering | Application | e-signature |
| `design-team` | 🔵 Owned | Legal & Admin | Engineering | Library | e-signature |
| `ec-010-jewelry-designer-ai` | 🔵 Owned | Legal & Admin | Engineering | Application | e-signature |
| `ec-012-fashion-designer-ai` | 🔵 Owned | Legal & Admin | Engineering | Application | e-signature |
| `ec-058-ai-packaging-designer` | 🔵 Owned | Legal & Admin | Engineering | Application | e-signature |
| `edu-015-ai-legal-doc-generator` | 🔵 Owned | Legal & Admin | Engineering | Application | utility |
| `email-design-os` | 🔵 Owned | Legal & Admin | Engineering | Application | e-signature |
| `ft-001-core-ledger` | 🔵 Owned | Legal & Admin | Engineering | Application | utility |
| `ft-001-docs` | 🔵 Owned | Legal & Admin | Engineering | Application | utility |
| `iza-os-docs` | 🔵 Owned | Legal & Admin | Engineering | Library | utility |
| `iza-os-legal-core` | 🔵 Owned | Legal & Admin | Engineering | Library | credit scoring |
| *... and 40 more repositories* | | | | | |

### DevOps & Infrastructure (76 Repositories)
| Repository / Path | Type | Department | Phase | Tool Type | Key Capabilities |
|---|---|---|---|---|---|
| `consciousness-deployment-system` | 🔵 Owned | Engineering | Engineering | Library | utility |
| `fh-014-cloud-kitchen` | 🔵 Owned | Engineering | Engineering | Platform | utility |
| `fh-014-cloud-kitchen-` | 🔵 Owned | Engineering | Engineering | Platform | utility |
| `iza-os-deployment-automation-bot` | 🔵 Owned | Engineering | Engineering | Library | utility |
| `iza-os-infrastructure` | 🔵 Owned | Engineering | Engineering | Library | utility |
| `iza-os-platform-core` | 🔵 Owned | Engineering | Engineering | Library | utility |
| `spec-001-ai-auction-house` | 🔵 Owned | Engineering | Engineering | Application | utility |
| `spec-017-smart-agriculture-ai` | 🔵 Owned | Engineering | Engineering | Application | utility |
| `spec-018-ai-personal-shopper` | 🔵 Owned | Engineering | Engineering | Application | utility |
| `spec-019-smart-home-security` | 🔵 Owned | Engineering | Engineering | Application | utility |
| `spec-038-ai-comedy-writer` | 🔵 Owned | Engineering | Engineering | Application | utility |
| `tech-003-cloud-management-ai` | 🔵 Owned | Engineering | Engineering | Platform | utility |
| `tech-035-cloud-management-ai` | 🔵 Owned | Engineering | Engineering | Platform | utility |
| `9001/copyparty` | ⭐ Starred | Engineering | Engineering | Platform | utility |
| `Adembc/lazyssh` | ⭐ Starred | Engineering | Engineering | Platform | utility |
| *... and 61 more repositories* | | | | | |

### Development Tools (48 Repositories)
| Repository / Path | Type | Department | Phase | Tool Type | Key Capabilities |
|---|---|---|---|---|---|
| `ace-ecommerce-templates` | 🔵 Owned | Engineering | Engineering | Boilerplate / Template | utility |
| `ai-venture-studio-template` | 🔵 Owned | Engineering | Engineering | Library | utility |
| `clip` | 🔵 Owned | Engineering | Engineering | Library | utility |
| `comm-040-community-recycling-ai` | 🔵 Owned | Engineering | Engineering | CLI / Tool | utility |
| `ec-098-ai-outfit-builder` | 🔵 Owned | Engineering | Engineering | Application | utility |
| `ec-106-ai-outfit-recycling` | 🔵 Owned | Engineering | Engineering | CLI / Tool | utility |
| `em-004-climate-solutions-ai` | 🔵 Owned | Engineering | Engineering | CLI / Tool | utility |
| `em-029-climate-modeling-ai` | 🔵 Owned | Engineering | Engineering | CLI / Tool | utility |
| `em-041-ai-climate-adaptation` | 🔵 Owned | Engineering | Engineering | CLI / Tool | utility |
| `fin-031-investor-dashboard-builder` | 🔵 Owned | Engineering | Engineering | Application | visual analytics |
| `iza-os-cli` | 🔵 Owned | Engineering | Engineering | Library | utility |
| `iza-os-mcp` | 🔵 Owned | Engineering | Engineering | Library | utility |
| `iza-os-templates` | 🔵 Owned | Engineering | Engineering | Library | utility |
| `mc-019-digital-download-store` | 🔵 Owned | Engineering | Engineering | CLI / Tool | utility |
| `repo-template` | 🔵 Owned | Engineering | Engineering | Boilerplate / Template | utility |
| *... and 33 more repositories* | | | | | |

### Finance & Trading (88 Repositories)
| Repository / Path | Type | Department | Phase | Tool Type | Key Capabilities |
|---|---|---|---|---|---|
| `business-template-marketplace` | 🔵 Owned | Finance & HR | Revenue | Library | utility |
| `bw-018-nail-booking-marketplace` | 🔵 Owned | Finance & HR | Revenue | Application | utility |
| `bw-031-hair-marketplace` | 🔵 Owned | Finance & HR | Revenue | Application | utility |
| `comm-031-community-investment-ai` | 🔵 Owned | Finance & HR | Revenue | Application | utility |
| `divine-johns-portfolio` | 🔵 Owned | Finance & HR | Revenue | Application | utility |
| `ec-005-nwa-products` | 🔵 Owned | Finance & HR | Revenue | Library | utility |
| `ec-048-wholesale-marketplace-ai` | 🔵 Owned | Finance & HR | Revenue | Application | utility |
| `ec-049-rental-marketplace` | 🔵 Owned | Finance & HR | Revenue | Application | utility |
| `ec-051-ai-email-marketing` | 🔵 Owned | Finance & HR | Revenue | Application | utility |
| `ec-067-ai-payment-optimization` | 🔵 Owned | Finance & HR | Revenue | Application | utility |
| `edu-008-branding-templates-marketplace` | 🔵 Owned | Finance & HR | Revenue | Boilerplate / Template | utility |
| `edu-023-personal-finance-coach` | 🔵 Owned | Finance & HR | Revenue | Application | utility |
| `em-015-crypto-trading-ai` | 🔵 Owned | Finance & HR | Revenue | Application | utility |
| `em-043-quantum-communication-ai` | 🔵 Owned | Finance & HR | Revenue | Application | utility |
| `fh-026-gourmet-food-market` | 🔵 Owned | Finance & HR | Revenue | Application | utility |
| *... and 73 more repositories* | | | | | |

### Knowledge Graphs (43 Repositories)
| Repository / Path | Type | Department | Phase | Tool Type | Key Capabilities |
|---|---|---|---|---|---|
| `ec-030-ai-product-photographer` | 🔵 Owned | Product & R&D | Engineering | Framework | utility |
| `ec-053-ai-visual-merchandiser` | 🔵 Owned | Product & R&D | Engineering | Application | utility |
| `em-005-holographic-events-ai` | 🔵 Owned | Product & R&D | Engineering | Framework | utility |
| `fh-033-food-photography-service` | 🔵 Owned | Product & R&D | Engineering | Framework | utility |
| `ht-004-mobile-app` | 🔵 Owned | Product & R&D | Engineering | Application | utility |
| `iza-os-data` | 🔵 Owned | Product & R&D | Engineering | Framework | ci/cd pipelines |
| `iza-os-knowledge-graph` | 🔵 Owned | Product & R&D | Engineering | Framework | utility |
| `maps` | 🔵 Owned | Product & R&D | Engineering | Framework | utility |
| `mc-009-stock-photography` | 🔵 Owned | Product & R&D | Engineering | Framework | utility |
| `obsidian-vault` | 🔵 Owned | Product & R&D | Engineering | Framework | secrets management |
| `pitch-kit` | 🔵 Owned | Product & R&D | Engineering | Application | utility |
| `ps-017-videography-service` | 🔵 Owned | Product & R&D | Engineering | Framework | utility |
| `tech-012-data-visualization-ai` | 🔵 Owned | Product & R&D | Engineering | Application | utility |
| `tech-044-data-visualization-ai` | 🔵 Owned | Product & R&D | Engineering | Application | utility |
| `AykutSarac/jsoncrack.com` | ⭐ Starred | Product & R&D | Engineering | Framework | utility |
| *... and 28 more repositories* | | | | | |

### Learning & Training (67 Repositories)
| Repository / Path | Type | Department | Phase | Tool Type | Key Capabilities |
|---|---|---|---|---|---|
| `bw-004-lash-training-academy` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| `bw-010-online-lash-education` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| `comm-022-job-training-center` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| `comm-026-public-education-ai` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| `ec-083-ai-product-education` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| `edu-010-trade-skills-bootcamp` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| `edu-018-online-course-creator` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| `edu-019-executive-education-program` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| `edu-024-language-learning-ai` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| `edu-026-corporate-training-ai` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| `edu-027-medical-education-ai` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| `edu-028-legal-education-ai` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| `edu-029-music-education-ai` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| `edu-030-art-education-ai` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| `edu-031-physical-education-ai` | 🔵 Owned | Finance & HR | Learning | Application | utility |
| *... and 52 more repositories* | | | | | |

### Monitoring & Observability (54 Repositories)
| Repository / Path | Type | Department | Phase | Tool Type | Key Capabilities |
|---|---|---|---|---|---|
| `comm-006-community-technology-access-ai` | 🔵 Owned | Engineering | Learning | Application | utility |
| `ec-059-ai-logistics-planner` | 🔵 Owned | Engineering | Learning | Application | utility |
| `ec-072-ai-product-cataloger` | 🔵 Owned | Engineering | Learning | Application | utility |
| `em-047-ai-environmental-monitoring` | 🔵 Owned | Engineering | Learning | Application | utility |
| `em-050-ai-archaeology` | 🔵 Owned | Engineering | Learning | Application | utility |
| `iza-os-business` | 🔵 Owned | Engineering | Learning | Library | utility |
| `iza-os-cybersecurity-monitoring-bot` | 🔵 Owned | Engineering | Learning | Library | utility |
| `iza-os-finance-advisor-alerting-bot` | 🔵 Owned | Engineering | Learning | Library | utility |
| `iza-os-finance-advisor-monitoring-bot` | 🔵 Owned | Engineering | Learning | Library | utility |
| `iza-os-infrastructure-monitoring-bot` | 🔵 Owned | Engineering | Learning | Library | utility |
| `iza-os-inventory-management-monitoring-bot` | 🔵 Owned | Engineering | Learning | Application | utility |
| `iza-os-marketing-automation-alerting-bot` | 🔵 Owned | Engineering | Learning | Application | utility |
| `iza-os-marketing-automation-monitoring-bot` | 🔵 Owned | Engineering | Learning | Application | utility |
| `iza-os-monitoring` | 🔵 Owned | Engineering | Learning | Library | utility |
| `iza-os-monitoring-integration` | 🔵 Owned | Engineering | Learning | Library | utility |
| *... and 39 more repositories* | | | | | |

### OSINT & Enrichment (26 Repositories)
| Repository / Path | Type | Department | Phase | Tool Type | Key Capabilities |
|---|---|---|---|---|---|
| `Worldwidebro` | 🔵 Owned | Operations | Discovery | Application | utility |
| `ace-community-impact-templates` | 🔵 Owned | Operations | Discovery | Library | utility |
| `edu-033-social-studies-ai` | 🔵 Owned | Operations | Discovery | Application | utility |
| `fin-028-legal-analyzer-ai` | 🔵 Owned | Operations | Discovery | Application | utility |
| `iza-os-customer-service-social-bot` | 🔵 Owned | Operations | Discovery | Application | utility |
| `ps-016-photography-service` | 🔵 Owned | Operations | Discovery | Framework | utility |
| `ps-020-social-media-management` | 🔵 Owned | Operations | Discovery | Application | utility |
| `tech-014-sentiment-analyzer` | 🔵 Owned | Operations | Discovery | Application | utility |
| `tech-046-sentiment-analyzer` | 🔵 Owned | Operations | Discovery | Application | utility |
| `0x0be/yesitsme` | ⭐ Starred | Operations | Discovery | Library | utility |
| `CallToSta/TG-All-In-One-Tool` | ⭐ Starred | Operations | Discovery | Library | web scraping |
| `GorvGoyl/Clone-Wars` | ⭐ Starred | Operations | Discovery | Library | utility |
| `Ha3MrX/InstaBrute` | ⭐ Starred | Operations | Discovery | Application | utility |
| `cporter202/API-mega-list` | ⭐ Starred | Operations | Discovery | Library | utility |
| `cporter202/automate-faceless-content` | ⭐ Starred | Operations | Discovery | Library | utility |
| *... and 11 more repositories* | | | | | |

### Specialized Utilities (658 Repositories)
| Repository / Path | Type | Department | Phase | Tool Type | Key Capabilities |
|---|---|---|---|---|---|
| `Applyingforjobs` | 🔵 Owned | Operations | Engineering | Library | utility |
| `Avs-Omni-` | 🔵 Owned | Operations | Engineering | Library | utility |
| `OS-001-MATHEMATICAL-OS-REGISTRY` | 🔵 Owned | Operations | Engineering | Application | utility |
| `Resume` | 🔵 Owned | Operations | Engineering | Library | utility |
| `Vex` | 🔵 Owned | Operations | Engineering | Application | utility |
| `acquisition-vehicle-automation` | 🔵 Owned | Operations | Engineering | Library | utility |
| `ai-002-api` | 🔵 Owned | Operations | Engineering | Library | utility |
| `ai-002-web-app` | 🔵 Owned | Operations | Engineering | Application | workflow automation |
| `ai-boss-holdings-v4` | 🔵 Owned | Operations | Engineering | Library | utility |
| `ai-business-commander` | 🔵 Owned | Operations | Engineering | Application | utility |
| `aibossoslandingpage` | 🔵 Owned | Operations | Engineering | Library | utility |
| `avs-omni` | 🔵 Owned | Operations | Engineering | Library | utility |
| `babystepsmatrix1` | 🔵 Owned | Operations | Engineering | Application | utility |
| `billionaire-brain-assistant` | 🔵 Owned | Operations | Engineering | Library | utility |
| `billionaire-consciousness-empire` | 🔵 Owned | Operations | Engineering | Application | utility |
| *... and 643 more repositories* | | | | | |

### Video & Media Generation (44 Repositories)
| Repository / Path | Type | Department | Phase | Tool Type | Key Capabilities |
|---|---|---|---|---|---|
| `avatar-engine` | 🔵 Owned | Product & R&D | Revenue | Library | utility |
| `edu-009-voiceover-script-library` | 🔵 Owned | Product & R&D | Revenue | Library | speech-to-text |
| `em-016-synthetic-media-ai` | 🔵 Owned | Product & R&D | Revenue | Application | utility |
| `fin-012-invoice-factoring-ai` | 🔵 Owned | Product & R&D | Revenue | Application | speech-to-text |
| `iza-os-computer-vision` | 🔵 Owned | Product & R&D | Revenue | Application | utility |
| `iza-os-speech-processing` | 🔵 Owned | Product & R&D | Revenue | Application | utility |
| `mc-006-video-production-company` | 🔵 Owned | Product & R&D | Revenue | Application | utility |
| `mc-010-stock-video` | 🔵 Owned | Product & R&D | Revenue | Application | utility |
| `media-empire-platform` | 🔵 Owned | Product & R&D | Revenue | Library | utility |
| `tech-006-voice-assistant-ai` | 🔵 Owned | Product & R&D | Revenue | Application | speech-to-text |
| `tech-015-image-recognition-ai` | 🔵 Owned | Product & R&D | Revenue | Application | utility |
| `tech-016-video-editor-ai` | 🔵 Owned | Product & R&D | Revenue | Application | utility |
| `tech-017-speech-to-text-ai` | 🔵 Owned | Product & R&D | Revenue | Application | speech-to-text |
| `tech-018-text-to-speech-ai` | 🔵 Owned | Product & R&D | Revenue | Application | utility |
| `tech-038-voice-assistant-ai` | 🔵 Owned | Product & R&D | Revenue | Application | speech-to-text |
| *... and 29 more repositories* | | | | | |