# Blockers to Completion & Starred Repositories Guide

This report maps the current blockers preventing your 5 core operating ventures from running, lists the YAGNI-compliant (Ponytail) checklist to solve them, and highlights the roles of your starred repositories (including `plasma-ai/fractal` and `awesome-n8n-templates`).

---

## 1. What is Stopping Us from Completion? (The Blockers)

To get the ventures fully automated and running under the **Fractal / Agent OS** loop, the following components are currently blocking execution:

### ⚠️ Blocker 1: Missing LLM API Credentials (The Execution Block)
*   **The Problem**: Running the Fractal agent node (`fractal node start` inside `.fractal-venv`) or the agent runners (`agent_runner.py`) requires an active `ANTHROPIC_API_KEY` and `OPENAI_API_KEY` exported in the environment. Without these keys, the LLM calls fail.
*   **Ponytail Solution**: Configure a local proxy or fallback to a local model (via Ollama on port `11434`) inside `OmniRoute` (port `20128`) to act as a zero-cost model router when API keys are unavailable.

### ⚠️ Blocker 2: Hardcoded Forms Endpoint Port Mismatch
*   **The Problem**: The static HTML form templates (like `/con-001-ace-construction/calculator.html` and `/ops-staff-001-staffing/clients.html`) have form actions hardcoded to fetch `http://localhost:8000/api/leads`. However, your operational API gateway server (`server.py`) runs on port **`8085`**!
*   **Ponytail Solution**: Update the Javascript fetch links in the HTML files to target relative endpoints (`/api/leads`) or matching environment ports.

### ⚠️ Blocker 3: Missing n8n Webhook Forwarder in API Gateway
*   **The Problem**: Currently, `server.py` captures waitlist leads and writes them to a local CSV (`waitlist_leads.csv`), but it does not forward them to your n8n instance webhooks. The n8n automation loops are bypassed.
*   **Ponytail Solution**: Add a simple HTTP request dispatch node inside `server.py`'s `handle_post_leads` to forward payloads directly to `http://localhost:5678/webhook/con-001-intake` if the n8n instance is active.

### ⚠️ Blocker 4: Unprepared Database Schema Tables
*   **The Problem**: The database tables required by the Fractal spawner (`venture_readiness`) and Staffing (`candidates`) are not fully migrated/created in your local Postgres/Supabase instance.
*   **Ponytail Solution**: Run a single, unified SQL migration file (`schema.sql`) to prepare the tables in one command.

---

## 2. Checklist to Complete the Loop (Ponytail / YAGNI Style)

To unblock the system with the **minimum amount of clean code** (no speculative abstractions), execute this checklist:

- [ ] **Infrastructure & Ports Alignment**
  - [ ] Update `con-001` waitlist submission fetch URL to point to relative `/api/leads` instead of port `8000`.
  - [ ] Update `ops-staff-001` client/worker forms to post to `/api/leads`.
  - [ ] Add n8n forwarder in `server.py` line 560:
    ```python
    import urllib.request
    # Forward lead to n8n webhook asynchronously or with try/except
    try:
        req = urllib.request.Request(
            f"http://localhost:5678/webhook/{venture_id}-intake",
            data=json.dumps(body).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        urllib.request.urlopen(req, timeout=1)
    except Exception:
        pass  # Fail silently to avoid blocking local CSV backup writes
    ```

- [ ] **Database Schemas Seeding**
  - [ ] Run the SQL setup inside your PostgreSQL client to initialize the schemas:
    ```sql
    CREATE TABLE IF NOT EXISTS venture_readiness (
        id VARCHAR(50) PRIMARY KEY,
        name VARCHAR(255),
        sector VARCHAR(100),
        status VARCHAR(50),
        readiness_score INT,
        blockers TEXT
    );
    ```

- [ ] **OmniRoute Fallback to Local Models**
  - [ ] Update `/OmniRoute/config` to default to `ollama/llama3` or `local/mistral` on port `11434` if `ANTHROPIC_API_KEY` is not present in `.env`.

---

## 3. What Starred Repos Help Us?

The repositories you starred or referenced provide the critical architectural components to solve these blocks:

### 1. `plasma-ai/fractal`
*   **Role**: **Hierarchical Task Allocation**.
*   **How it helps**: Fractal structures the Root-to-OpCo agent loops. Instead of writing custom python code for every new venture agent, we load `root.md` and use the Fractal CLI to spawn nodes. Each child node runs asynchronously and writes its results back to the shared memory file (`ventures_readiness.json`).

### 2. `awesome-n8n-templates`
*   **Role**: **Rapid Integration Webhooks**.
*   **How it helps**: It provides pre-made workflow nodes. We can import the qualifying template `Qualifying Appointment Requests with AI.json` directly into your n8n dashboard, connect it to the `/api/leads` forwarder, and let n8n handle the database writes to Supabase.

### 3. `awesome-ai-agents`
*   **Role**: **Agent Execution Sandboxes**.
*   **How it helps**: Shows how to run code generators securely (like running the driver route optimization scripts or tax deductions scanner) using standard E2B or Docker sandbox environments, shielding your primary system.
