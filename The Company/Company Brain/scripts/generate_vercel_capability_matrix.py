"""Generate VERCEL_CAPABILITY_DEPLOYMENT_MATRIX.json and Markdown alignment."""

import json
from pathlib import Path

# Load updated allVercelSites.json
sites_path = Path("Worldwidebro-Vex/src/data/allVercelSites.json")
sites = json.load(open(sites_path))

# Mapping from venture/sector to specific starred repos & deployment plans
CAPABILITY_ATTACHMENTS = {
    "OPS-001": {
        "sector": "STAFFING & WORKFORCE",
        "distance_to_cash": "Immediate (< 24h)",
        "attached_starred_repos": [
            {
                "repo": "ever-co/ever-gauzy",
                "role": "Open-source ATS & HRM platform",
                "action": "Ingests applicant submissions from Vercel front door into local PostgreSQL candidate pool."
            },
            {
                "repo": "unclecode/crawl4ai",
                "role": "Autonomous job board scraper",
                "action": "Scrapes warehouse/distribution job listings in Charlotte to feed high-demand requisition pipeline."
            },
            {
                "repo": "twentyhq/twenty",
                "role": "Open-source Salesforce CRM alternative",
                "action": "Tracks corporate staffing contracts, bill rates, and markup margins."
            },
            {
                "repo": "Jakeschincariol/linkedin-agent-skill",
                "role": "Claude automated LinkedIn outbound",
                "action": "Executes 21 hook formulas to message Charlotte operations and hiring managers."
            },
            {
                "repo": "n8n-io/n8n",
                "role": "Workflow automation",
                "action": "Fires candidate SMS/email confirmations and sends background check forms via webhook."
            }
        ],
        "deployment_stack": "Next.js Frontend (Vercel) + PostgreSQL / Gauzy ATS (Mac Studio Docker)",
        "pipeline_plan": "Candidate submits resume on Vercel -> Webhook fires n8n -> Gauzy ATS registers candidate -> Decision Engine matches trade license -> Twenty CRM notifies recruiter."
    },
    "LT-005": {
        "sector": "HEALTHCARE LOGISTICS & MEDICAL COURIER",
        "distance_to_cash": "Immediate (< 24h)",
        "attached_starred_repos": [
            {
                "repo": "Mahanaicoach/google-maps-scraper-kit",
                "role": "Local Google Maps clinic scraper",
                "action": "Extracts contacts for 150+ hospital labs, dialysis centers, and urgent care clinics across Charlotte."
            },
            {
                "repo": "n8n-io/n8n",
                "role": "Visual webhook engine",
                "action": "Receives STAT specimen pickup requests from HealthRoute portal and dispatches directly to LT-011."
            },
            {
                "repo": "opendatalab/MinerU",
                "role": "Document/Manifest OCR",
                "action": "Parses laboratory specimen manifests and chain-of-custody transfer slips."
            },
            {
                "repo": "browser-use/browser-use",
                "role": "Headless browser RPA",
                "action": "Automates scheduled pickup bookings on hospital portal interfaces that lack open REST APIs."
            }
        ],
        "deployment_stack": "Next.js Frontend (Vercel) + LT-011 Dispatch Engine (Local API) + SQLite/PGLite",
        "pipeline_plan": "Clinic manager books STAT pickup on HealthRoute Vercel portal -> n8n validates temperature constraints -> LT-011 assigns closest courier -> Proof-of-delivery PDF generated via Stirling-PDF."
    },
    "LT-011": {
        "sector": "TRANSPORTATION & FLEET MANAGEMENT",
        "distance_to_cash": "Direct (< 48h)",
        "attached_starred_repos": [
            {
                "repo": "openobserve/openobserve",
                "role": "Rust telemetry & trace logger",
                "action": "Tracks real-time GPS telemetry, deadhead mileage reduction, and driver transit spans."
            },
            {
                "repo": "bilawalsidhu/gods-eye-view",
                "role": "Browser satellite & geospatial visualizer",
                "action": "Renders real-time multi-mode vehicle movements on VEX fleet map."
            },
            {
                "repo": "jsvine/pdfplumber",
                "role": "Rate sheet table parser",
                "action": "Parses rate confirmations and bills of lading from freight brokers."
            }
        ],
        "deployment_stack": "Next.js Frontend (Vercel) + OpenObserve (:5080) + OSRM Routing Engine",
        "pipeline_plan": "Carrier logs into CarrierDispatch -> System ingests rate con PDF -> Calculates optimal multi-stop route -> Live tracking link shared with shipper."
    },
    "CON-001": {
        "sector": "COMMERCIAL CONSTRUCTION & CONTRACTING",
        "distance_to_cash": "Direct (< 48h)",
        "attached_starred_repos": [
            {
                "repo": "typesense/typesense",
                "role": "In-memory fast catalog search",
                "action": "Sub-millisecond search over building material catalogs, equipment rentals, and trade contractor rates."
            },
            {
                "repo": "twentyhq/twenty",
                "role": "Commercial CRM",
                "action": "Tracks commercial GC bids, subcontractor agreements, and project change orders."
            },
            {
                "repo": "garrytan/gstack",
                "role": "PDF prospectus and quote generator",
                "action": "Compiles professional vector PDF project estimate proposals and AIA payment schedules."
            }
        ],
        "deployment_stack": "Next.js Frontend (Vercel) + Typesense (:8108) + Supabase",
        "pipeline_plan": "Commercial GC submits scope of work on ConstructionOS -> Typesense matches trade packages -> Twenty CRM logs opportunity -> gstack generates quote PDF."
    },
    "CALLCENTER": {
        "sector": "OMNICHANNEL AI COMMUNICATIONS",
        "distance_to_cash": "Immediate (< 24h)",
        "attached_starred_repos": [
            {
                "repo": "chatwoot/chatwoot",
                "role": "Omnichannel customer support desk",
                "action": "Consolidates live chat, SMS, and email queues into a single shared inbox."
            },
            {
                "repo": "czlonkowski/n8n-mcp",
                "role": "n8n MCP bridge",
                "action": "Allows AI agents to programmatically read and answer inbound customer tickets."
            },
            {
                "repo": "Zackriya-Solutions/meetily",
                "role": "Fast Whisper live transcription",
                "action": "Transcribes incoming Twilio calls in real time for sentiment and lead capture."
            }
        ],
        "deployment_stack": "Next.js Frontend (Vercel) + Chatwoot + Twilio Voice Webhooks + OmniRoute",
        "pipeline_plan": "Customer calls or chats on portal -> Twilio routes audio to Meetily Whisper -> OmniRoute classifies intent -> Chatwoot assigns ticket to closer or auto-resolves."
    },
    "RE-001": {
        "sector": "REAL ESTATE & HOLDINGS",
        "distance_to_cash": "Direct (< 48h)",
        "attached_starred_repos": [
            {
                "repo": "CloakHQ/CloakBrowser",
                "role": "Stealth Chromium RPA",
                "action": "Scrapes county tax assessor portals and GIS parcel registries without Cloudflare IP blocking."
            },
            {
                "repo": "Stirling-Tools/Stirling-PDF",
                "role": "Document room suite",
                "action": "Redacts, OCRs, and merges institutional loan packets (SBA 504) on-premise."
            },
            {
                "repo": "garrytan/gstack",
                "role": "Prospectus compiler",
                "action": "Compiles publication-grade 16:9 investor pitch decks and data room packages."
            }
        ],
        "deployment_stack": "Next.js Frontend (Vercel) + Stirling-PDF (:8080) + gstack",
        "pipeline_plan": "Property address entered -> CloakBrowser fetches county tax and deed history -> Financial model generated -> gstack outputs bank presentation."
    },
    "COMM": {
        "sector": "COMMUNITY IMPACT & CIVIC AI",
        "distance_to_cash": "Grant / Civic Funding",
        "attached_starred_repos": [
            {
                "repo": "n8n-io/self-hosted-ai-starter-kit",
                "role": "Turnkey local AI stack",
                "action": "Powers community Q&A agents using local Ollama models on Mac Studio."
            },
            {
                "repo": "knadh/listmonk",
                "role": "High-performance newsletter & notification system",
                "action": "Sends community alerts, veteran benefits bulletins, and event notifications."
            },
            {
                "repo": "coollabsio/coolify",
                "role": "Self-hosted PaaS",
                "action": "Hosts lightweight civic web apps on internal mesh at zero hosting cost."
            }
        ],
        "deployment_stack": "Next.js on Vercel + Local Ollama / Listmonk",
        "pipeline_plan": "Community member asks for assistance on portal -> Local Ollama agent answers -> If human case manager needed, Listmonk notifies staff."
    },
    "FIN": {
        "sector": "FINTECH & TAX AI",
        "distance_to_cash": "Direct (< 48h)",
        "attached_starred_repos": [
            {
                "repo": "Open-Finance-Lab/AgenticTrading",
                "role": "Multi-agent financial engine",
                "action": "Executes quantitative portfolio and crypto tax reconciliation models."
            },
            {
                "repo": "Noisyxl/brier",
                "role": "Cryptographic prediction receipt ledger",
                "action": "Maintains immutable audit log of tax optimization and deduction assessments."
            }
        ],
        "deployment_stack": "Next.js on Vercel + Python Financial Engines",
        "pipeline_plan": "User inputs tax scenario -> Decision Engine categorizes deductions -> System generates tax strategy memo."
    },
    "EC": {
        "sector": "E-COMMERCE & BRANDS",
        "distance_to_cash": "Direct (< 48h)",
        "attached_starred_repos": [
            {
                "repo": "mutonby/openshorts",
                "role": "Viral 9:16 short video generator",
                "action": "Automates product demo clips and social media reels."
            },
            {
                "repo": "MengTo/threeui",
                "role": "Interactive 3D component catalog",
                "action": "Renders interactive 3D product previews on Kosmic Kitty storefront."
            }
        ],
        "deployment_stack": "Next.js on Vercel + Shopify/Stripe API",
        "pipeline_plan": "Customer browses 3D interactive storefront -> Adds to cart -> Stripe webhook processes checkout."
    },
    "DEFAULT": {
        "sector": "CORE OPERATING INFRASTRUCTURE",
        "distance_to_cash": "Infrastructure Core",
        "attached_starred_repos": [
            {
                "repo": "openobserve/openobserve",
                "role": "Telemetry & logs",
                "action": "Collects frontend performance metrics and errors."
            },
            {
                "repo": "DietrichGebert/ponytail",
                "role": "Anti-bloat guardrail",
                "action": "Prevents redundant dependencies on web endpoints."
            }
        ],
        "deployment_stack": "Next.js on Vercel",
        "pipeline_plan": "Provides foundational web hosting and user interface access."
    }
}

matrix = []
for s in sites:
    vid = s.get("venture_id", "UNASSIGNED")
    sec = vid.split("-")[0] if "-" in vid else vid
    
    config = CAPABILITY_ATTACHMENTS.get(vid) or CAPABILITY_ATTACHMENTS.get(sec) or CAPABILITY_ATTACHMENTS["DEFAULT"]
    
    matrix_entry = {
        "site_id": s.get("id"),
        "site_name": s.get("name"),
        "venture_id": vid,
        "url": s.get("url"),
        "http_status": s.get("http_status"),
        "is_live": s.get("is_live", False),
        "latency_ms": s.get("latency_ms"),
        "sector": config["sector"],
        "distance_to_cash": config["distance_to_cash"],
        "deployment_stack": config["deployment_stack"],
        "pipeline_plan": config["pipeline_plan"],
        "attached_starred_repos": config["attached_starred_repos"]
    }
    matrix.append(matrix_entry)

# Save JSON
out_json_path = Path("The Company/Company Brain/_REGISTRIES/CANONICAL/VERCEL_CAPABILITY_DEPLOYMENT_MATRIX.json")
with open(out_json_path, "w") as f:
    json.dump(matrix, f, indent=2)

print(f"Generated {out_json_path} with {len(matrix)} mapped deployments.")
