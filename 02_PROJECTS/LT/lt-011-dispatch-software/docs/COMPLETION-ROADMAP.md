# DispatchOS System Completion Roadmap

This document outlines the phases to finalize DispatchOS (LT-011) utilizing local containerized services, OmniRoute AI gateways, Buzz CRM automation, and the Nous Research Hermes skills system.

---

## Phase 1: Local Containerization (Mac Studio Docker Stack)
*   **Postgres & Neo4j Setup:** Start Postgres (port 5432) and Neo4j (port 7687) containers on the Mac Studio.
*   **Database Schema Migration:** Run the migration script against the local Postgres container:
    ```bash
    psql -h localhost -U postgres -d dispatch_os -f db/migrations/001_initial_dispatch_os.sql
    ```
*   **Local Portals (NGINX):** Spin up NGINX to serve the frontends locally on port `8085`.
*   **Network Bridging (Tailscale):** Ensure ports `8085` and `4005` are accessible to your MacBook Air via the Mac Studio's Tailscale IP: `100.87.214.70`.

---

## Phase 2: Local LLM Execution (OmniRoute + Command R)
*   **Ollama Hosting:** Run Ollama on the Mac Studio. Download the **Command R (35B)** model (specialized for structured tool use) or **Llama 3 70B**:
    ```bash
    ollama run command-r
    ```
*   **AI Gateway Routing (OmniRoute):** Configure `OmniRoute` (port 20128) to route incoming OpenAI-compatible calls to Ollama.
*   **Harness Wiring:** Update the backend API environmental config:
    ```env
    OPENAI_API_BASE=http://localhost:20128/v1
    ```
    This redirects all agent LLM prompts from external clouds to the local Mac Studio GPU.

---

## Phase 3: Outbound Prospecting Integration (Buzz CRM)
*   **Campaign Configuration:** Set up target company lists (from `LEADS-AND-CALLS.md`) in Buzz CRM.
*   **Webhook Bindings:** Configure a webhook trigger in Buzz to fire when a lead replies positively or schedules a run.
*   **Order Intake Mapping:** Route the webhook target to the API order route:
    `POST http://localhost:4005/api/orders`
    This converts a closed lead in Buzz directly into a validated draft load inside the dispatch system.

---

## Phase 4: Skills System Deployment (Nous Hermes & Google Antigravity)
*   **Hermes Skills Registration:** Clone the 12 core capabilities from `docs/AGENTS.md` into `~/.hermes/skills/` as executable `SKILL.md` files. This allows the Nous Hermes agent to control the logistics matching loop natively.
*   **Graphify Integration:** Run `/Users/acebless/.local/bin/graphify update .` to keep codebase symbols in sync.

---

## Phase 5: Financial Settlements (Stripe Connect)
*   **Invoicing:** Connect Stripe to charge credit cards and ACH payouts when the Customer Portal completes an invoice.
*   **Driver Payouts:** Integrate Stripe Connect to automatically release the carrier settlement splits (e.g. paying the driver their `$1,285.00` share while retaining the `$215.00` margin).
