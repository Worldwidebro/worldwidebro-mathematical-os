# Odysseus + Hermes Orchestration Layer — Week 1 Plan
**Objective:** Deploy Odysseus AI workspace + Hermes agent coordinator to orchestrate Apify leads pipeline into ClickUp tasks + Slack notifications + Supabase intelligence layer.

**Timeline:** May 12-18, 2026 (parallel execution with 3 blockers)  
**References:** [TASK-10-APIFY-SCRAPERS-DETAILED.md](venture-hub/TASK-10-APIFY-SCRAPERS-DETAILED.md), [APIFY-SCRAPER-CONFIGS.md](venture-hub/APIFY-SCRAPER-CONFIGS.md)

---

## 🎯 WHAT THIS IS

**Layer 1 (Existing):** Apify scrapers → leads flowing to Supabase  
**Layer 2 (New):** Odysseus + Hermes orchestration layer → intelligent task creation + routing

**Flow:**
```
Apify Scraper (job listings)
    ↓ (webhook)
Hermes Agent (decision logic: is this a good lead?)
    ↓ (if yes)
Odysseus Workspace (agent enrichment + prioritization)
    ↓ (if high-value)
ClickUp Task (created with context + links)
    ↓ (in parallel)
Slack Alert (team notified in #leads)
    ↓ (background)
Supabase Insights (lead scored + routed to ventures)
```

---

## 📋 WEEK 1 BLOCKERS (Parallel Execution)

### BLOCKER 1: Odysseus Local Deployment + Configuration
**Owner:** DevOps  
**Duration:** 6-8 hours  
**Dependent on:** Docker, GitHub token (for repo access)

#### Context
Odysseus is a self-hosted AI workspace. We're using it as:
- **Team workspace:** Notes, tasks, calendar, email in one place
- **Agent coordination hub:** Agents post findings; humans review + approve
- **Memory layer:** Venture context, contact history, enrichment rules
- **Integration node:** Orchestrates ClickUp + Slack + Supabase

#### Tasks

1. [ ] Clone Odysseus repo (stable main branch)
   ```bash
   cd ~/
   git clone https://github.com/pewdiepie-archdaemon/odysseus.git odysseus-workspace
   cd odysseus-workspace
   git checkout main
   ```

2. [ ] Review deployment requirements
   - Docker 20.10+, 4-8GB RAM
   - Optional: GPU (NVIDIA/AMD/Apple Metal)
   - Review: `docs/DEPLOYMENT.md`

3. [ ] Create `.env` for Odysseus
   ```bash
   cat > .env << 'EOF'
   ENVIRONMENT=production
   DEBUG=false
   
   # Database (Supabase for persistence)
   DATABASE_URL=sqlite:///./odysseus.db
   
   # LLM Backend
   LLM_BACKEND=ollama
   OLLAMA_BASE_URL=http://localhost:11434
   ANTHROPIC_API_KEY=sk-ant-...
   
   # Integration Keys
   SLACK_BOT_TOKEN=xoxb-...
   CLICKUP_API_KEY=pk_...
   
   # Supabase
   SUPABASE_URL=https://...
   SUPABASE_KEY=eyJ...
   
   # Chroma (vector DB)
   CHROMA_HOST=localhost
   CHROMA_PORT=8000
   
   TZ=America/New_York
   EOF
   ```

4. [ ] Spin up Docker Compose
   ```bash
   docker-compose up -d
   sleep 180
   docker-compose logs -f
   ```

5. [ ] Verify core functionality
   - [ ] Access UI: http://localhost:8000
   - [ ] Chat functional (LLM backend works)
   - [ ] Create test task (ClickUp integration)
   - [ ] Memory stores embeddings (Chroma)

**Success Criteria:**
- Odysseus running, chat works, integrations wired

---

### BLOCKER 2: Hermes Agent Architecture + Spec
**Owner:** Agent Engineering  
**Duration:** 8-10 hours

#### Context
Hermes = **agent orchestration layer** that decides about leads:
- Ingest raw jobs + contacts from Apify
- Score leads (0-100, is this good?)
- Route to appropriate venture
- Create ClickUp task
- Trigger Slack alert

#### Tasks

1. [ ] **Clarify Hermes architecture** (Decision Point)
   - **Option A:** Build custom Python agent (lightweight, controllable)
   - **Option B:** Use existing Hermes framework (heavier setup)
   
   **→ Recommended: Option A (Custom Hermes)**

2. [ ] Create `/Users/acebless/Documents/HERMES-AGENT-SPEC.md`
   ```markdown
   # Hermes Agent Spec
   
   **Purpose:** Orchestrate lead evaluation → ClickUp + Slack
   
   **Inputs:** job {id, title, company, salary, posted_at, url}, contact {name, email, title}
   **Outputs:** score (0-100), venture_id, task_data, slack_routing
   
   **Rules:**
   - IF salary > $50K AND posted < 3 days → HIGH priority, #leads
   - IF salary > $30K OR posted < 7 days → MEDIUM priority, #leads_digest
   - ELSE → LOW priority, batch weekly
   
   **Venture Routing:**
   - roofing → con_009
   - plumbing → con_010
   - hvac → lt_009
   - electrical → con_011
   - else → con_001
   ```

3. [ ] Build Hermes agent in Python
   ```python
   # hermes.py (simplified)
   import anthropic
   from supabase import create_client
   from datetime import datetime, timedelta
   import json
   
   class HermesAgent:
       def __init__(self, supabase_url, supabase_key, claude_api_key):
           self.supabase = create_client(supabase_url, supabase_key)
           self.claude = anthropic.Anthropic(api_key=claude_api_key)
       
       def score_lead(self, job, contact):
           """Score using Claude."""
           prompt = f"Score lead {contact['name']} at {job['company']} ({job['title']}). Return JSON only: {{\"score\": <0-100>, \"reasoning\": \"...\"}}"
           
           response = self.claude.messages.create(
               model="claude-3-5-sonnet-20241022",
               max_tokens=300,
               messages=[{"role": "user", "content": prompt}]
           )
           return json.loads(response.content[0].text)
       
       def route_venture(self, job_title):
           """Route to venture based on job type."""
           title_lower = job_title.lower()
           if "roof" in title_lower: return "con_009"
           if "plumb" in title_lower: return "con_010"
           if "hvac" in title_lower: return "lt_009"
           if "elec" in title_lower: return "con_011"
           return "con_001"
       
       def process_lead(self, job, contact):
           """End-to-end lead processing."""
           score = self.score_lead(job, contact)
           venture_id = self.route_venture(job['title'])
           
           # Log decision
           self.supabase.table("leads_decisions").insert({
               "job_id": job["id"],
               "venture_id": venture_id,
               "lead_score": score['score'],
               "processed_at": datetime.now().isoformat()
           }).execute()
           
           return {"score": score['score'], "venture": venture_id}
   ```

4. [ ] Create webhook `/webhook/apify/jobs` (FastAPI)
   ```python
   @app.post("/webhook/apify/jobs")
   async def ingest_apify_jobs(payload: Request):
       data = await payload.json()
       jobs = data.get("data", {}).get("finalDataset", [])
       
       for job in jobs:
           contact = supabase.table("leads_contacts").select("*").eq("job_id", job["id"]).execute()
           if contact.data:
               hermes.process_lead(job, contact.data[0])
       
       return {"status": "ok", "count": len(jobs)}
   ```

5. [ ] Create Supabase schema
   ```sql
   CREATE TABLE leads_decisions (
       id SERIAL PRIMARY KEY,
       job_id TEXT,
       venture_id TEXT,
       lead_score INT,
       processed_at TIMESTAMP
   );
   ```

**Success Criteria:**
- Hermes spec documented
- Agent processes 10+ leads
- Decisions logged to Supabase

---

### BLOCKER 3: ClickUp + Slack + Supabase Wiring
**Owner:** Integration Engineering  
**Duration:** 6-8 hours

#### Tasks

1. [ ] Wire ClickUp task creation (in Hermes)
   ```python
   def create_clickup_task(self, job, score):
       headers = {"Authorization": self.clickup_api_key}
       task_data = {
           "name": f"Lead: {job['company']} ({score['score']}/100)",
           "priority": 2 if score["score"] > 70 else 3
       }
       response = requests.post(
           f"https://api.clickup.com/api/v2/list/{LIST_ID}/task",
           json=task_data, headers=headers
       )
       return response.json()['id'] if response.status_code == 200 else None
   ```

2. [ ] Wire Slack posting
   ```python
   from slack_sdk import WebClient
   
   def post_slack_alert(self, job, score, task_url):
       if score["score"] < 50: return
       
       client = WebClient(token=self.slack_token)
       client.chat_postMessage(
           channel="C123456",  # #leads channel
           text=f"🎯 {job['title']} @ {job['company']} ({score['score']}/100)"
       )
   ```

3. [ ] Test end-to-end
   - Process 1 lead through Hermes
   - Verify: Supabase decision logged ✓
   - Verify: ClickUp task created ✓
   - Verify: Slack alert posted ✓

**Success Criteria:**
- ClickUp: Tasks created with scores
- Slack: Real-time alerts in #leads
- Supabase: Decisions table populated

---

## 🔄 DATA FLOW

```
Apify Jobs (100-300/day)
    ↓ webhook
Supabase leads_jobs
    ↓ enrichment
Supabase leads_contacts (name, email, title)
    ↓ Hermes scores
Supabase leads_decisions (score, venture)
    ↓ if score > 50
ClickUp Task + Slack Alert
```

---

## 📊 SUCCESS METRICS

| Blocker | Target | Done When |
|---------|--------|-----------|
| Odysseus | Running + configured | Accessible on localhost:8000 |
| Hermes | Agent + webhook working | 10+ leads processed, scored |
| Integration | ClickUp + Slack + Supabase | Tasks created, alerts posted, decisions logged |

---

## 📝 NOTES

- **Hermes decision:** Build custom (Option A) unless you're already using external framework
- **LinkedIn safety:** Use Clearbit/Hunter, not direct scraping (ToS compliant)
- **Costs:** Apify ~$2/day, Clearbit free tier, Hermes = free (Claude API)
- **ClickUp setup:** Pre-create "lead_score" custom field in your list
