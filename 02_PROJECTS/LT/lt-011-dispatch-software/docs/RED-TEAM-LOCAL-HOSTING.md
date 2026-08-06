# Red Team Audit: Bypassing the Cloud for Local Mac Studio Hosting

This document analyzes why our system is not yet 100% locally self-hosted, provides a containerization roadmap utilizing `diegosouzapw/OmniRoute`, and audits the role-based data isolation of our portals.

---

## 1. Red Team: Why the System Isn't Local Yet (The Bottlenecks)

Currently, the architecture has three primary external dependencies:
1.  **Database Layer:** We rely on Supabase Cloud (`cyhzilqldouzgynacqpe.supabase.co`) for transaction records.
2.  **LLM Reasoning Gateway:** `LLMGateway` routes calls to external Gemini/OpenAI cloud endpoints.
3.  **Hosting & Distribution:** Static assets and serverless functions are deployed to Vercel.

### Bypassing Cloud Dependencies (The Target State)
We can host the entire system locally inside a Docker network on the Mac Studio:

```text
                        MAC STUDIO LOCALHOST
 ┌───────────────────────────────────────────────────────────────┐
 │                                                               │
 │  [ OmniRoute Gateway ] ──► [ Local Ollama (Llama 3 70B) ]     │
 │          ▲                                                    │
 │          │ (Local LLM requests)                               │
 │   [ API Server ]                                              │
 │    (Port 4005) ──────────────────┐                            │
 │          ▲                       ▼                            │
 │          │ (REST Fetches)   [ Local Postgres ] (Port 5432)    │
 │          ▼                  [ Local Neo4j ] (Port 7687)       │
 │   [ Portals (NGINX) ]                                         │
 │    (Port 8085)                                                │
 └───────────────────────────────────────────────────────────────┘
```

*   **Database:** Run local PostgreSQL and Neo4j containers on the Mac Studio.
*   **LLM Engine (OmniRoute):** Deploy `OmniRoute` locally. It pools accounts, compresses tokens, and serves a local OpenAI-compatible endpoint (`http://localhost:20128/v1`) pointing to local Ollama/Llama.cpp models.
*   **Hosting:** Deploy portals and the API service inside NGINX and Node Docker containers.

---

## 2. Local Docker Compose Architecture (`docker-compose.yml`)

We can spin up the entire infrastructure locally using this compose specification:

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15
    ports:
      - "5432:5432"
    environment:
      POSTGRES_DB: dispatch_os
      POSTGRES_PASSWORD: localpassword
    volumes:
      - pgdata:/var/lib/postgresql/data

  neo4j:
    image: neo4j:5.12
    ports:
      - "7474:7474"
      - "7687:7687"
    environment:
      NEO4J_AUTH: neo4j/localpassword
    volumes:
      - neo4jdata:/data

  omniroute:
    image: diegosouzapw/omniroute:latest
    ports:
      - "20128:20128"
    environment:
      - PORT=20128
      - DATABASE_URL=sqlite:////app/data/omniroute.db
    volumes:
      - omniroutedata:/app/data

  api-server:
    build: ./services/api
    ports:
      - "4005:4005"
    environment:
      - PORT=4005
      - SUPABASE_URL=http://postgres:5432/dispatch_os
      - SUPABASE_KEY=service_role_key
      - OPENAI_API_BASE=http://omniroute:20128/v1
    depends_on:
      - postgres
      - neo4j
      - omniroute

  nginx-portals:
    image: nginx:alpine
    ports:
      - "8085:80"
    volumes:
      - ./apps:/usr/share/nginx/html
    depends_on:
      - api-server

volumes:
  pgdata:
  neo4jdata:
  omniroutedata:
```

---

## 3. Portal Data Isolation Audit (Dispatcher vs. Driver/Call Center)

Our portal layouts strictly segregate high-risk financial data from operational execution data:

### A. Dispatcher Panel (Admin View)
*   **Access Route:** `/apps/dispatch-web/index.html`
*   **Data Exposed:** 
    *   *Load Board Tab:* Access to Tender IDs, carrier base rates, and active bids.
    *   *Finance Tab:* Displays total client invoicing pay, internal carrier payout costs, and computed gross margin spreads (e.g. `+$215.00` profit).
    *   *System Control:* Can trigger dispatches, overwrite rates, and override AI decisions.

### B. Driver App & Employee Call Center Panel (Worker View)
*   **Access Route:** `/apps/driver-app/index.html`
*   **Data Exposed:** 
    *   *Route Details only:* Origin and destination addresses, pickup/delivery times, and GPS telemetry indicators.
    *   *No Spread Visibility:* Drivers can only see their specific payout contract (e.g. `+$120.00` earnings), and call center employees do not see the client invoicing spread, protecting holding margins from disclosure.
