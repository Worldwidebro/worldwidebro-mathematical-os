# MCP Connection Tests — Verification Suite

**Date:** 2026-06-10
**Goal:** Verify all MCPs work with real queries

---

## Test Suite

### 1️⃣ Supabase MCP
**Purpose:** Query venture database

**Test Query:**
```
"Show me all ventures in the Healthcare sector"
```

**Expected Output:**
- List of healthcare ventures
- Fields: id, name, stage, status, mrr

**Try it:** Run in Claude chat and share results

---

### 2️⃣ GitHub MCP
**Purpose:** Repo and issue management

**Test Query:**
```
"List all open issues in my repositories"
```

**Expected Output:**
- Issue title
- Repo name
- Status
- Assigned to

**Try it:** Run in Claude chat and share results

---

### 3️⃣ ClickUp MCP
**Purpose:** Task and pipeline management

**Test Query:**
```
"Show me all tasks in my ClickUp workspace with status 'In Progress'"
```

**Expected Output:**
- Task name
- Priority
- Status
- Assigned team member

**Try it:** Run in Claude chat and share results

---

### 4️⃣ HubSpot MCP
**Purpose:** Sales pipeline and contacts

**Test Query:**
```
"Show me all deals in my HubSpot pipeline with stage 'Negotiation'"
```

**Expected Output:**
- Deal name
- Amount
- Stage
- Owner
- Close date

**Try it:** Run in Claude chat and share results

---

### 5️⃣ Slack MCP
**Purpose:** Post updates, read channels

**Test Query (Safe):**
```
"What channels do I have in my Slack workspace?"
```

**Expected Output:**
- Channel list
- Channel members
- Purpose/description

**Try it:** Run in Claude chat and share results

---

### 6️⃣ Notion MCP
**Purpose:** Access pages and databases

**Test Query:**
```
"Show me all pages in my Notion workspace"
```

**Expected Output:**
- Page titles
- Page IDs
- Last modified date
- Created by

**Try it:** Run in Claude chat and share results

---

### 7️⃣ Tavily MCP
**Purpose:** Web research and competitive intelligence

**Test Query:**
```
"Research the top 3 competitors in the AI automation space in 2026"
```

**Expected Output:**
- Company names
- What they do
- Funding/revenue
- Key differentiators
- Recent news

**Try it:** Run in Claude chat and share results

---

### 8️⃣ Buffer MCP
**Purpose:** Social media scheduling and analytics

**Test Query:**
```
"Show me my recent posts and their engagement stats"
```

**Expected Output:**
- Post title
- Date posted
- Platforms
- Views/engagement
- Best performing platform

**Try it:** Run in Claude chat and share results

---

## How to Run These Tests

### Option 1: Run in This Chat
1. Copy a test query from above
2. Paste it in Claude Code chat
3. See if the MCP returns data
4. Report back with results

### Option 2: Run in Claude Code Interface
1. Open Claude Code
2. Go to a conversation
3. Type the test query
4. Claude will use the appropriate MCP
5. Share the results

### Option 3: Check MCP Status First
```bash
claude mcp list
```

Should show:
```
✔ Connected MCPs:
- supabase
- github
- clickup
- hubspot
- slack
- notion
- tavily
- buffer
```

---

## What We're Verifying

For each MCP, we check:

1. **Connectivity** — Can it establish a connection?
2. **Authentication** — Do the API keys work?
3. **Data Access** — Can it read your actual data?
4. **Response Quality** — Does it return useful information?
5. **Error Handling** — Does it handle failures gracefully?

---

## Success Criteria

✅ **All 8 MCPs should:**
- Connect without errors
- Return real data from your accounts
- Take <5 seconds per query
- Format data readably

---

## If Any Fail

If a test fails, we'll:
1. Check the API key in `.env`
2. Verify the MCP is installed correctly
3. Check for rate limiting or auth issues
4. Re-install if needed

---

## Next Steps (After Testing)

Once all 8 MCPs pass:
1. Add Beehiiv key → complete Phase A ✅
2. Start Phase B: Clip Farming Stack 🚀
3. Build Layer 4 (Clip Detection) — custom agent
4. Integrate Postiz for distribution
