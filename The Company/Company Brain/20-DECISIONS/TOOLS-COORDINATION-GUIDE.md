[[STARTHERE]] | [[20-DECISIONS/README|Decisions Index]] | [[REALITY]]

# Tools Coordination Guide — How Each Chat Works Together

**Purpose:** Map the workflow for using graft, Playwright, Firecrawl, context7, and Bash to execute audits and build the 789-venture system

---

## THE COORDINATION MODEL

```
                    WORKFLOW REQUEST
                           ↓
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
    RESEARCH            UNDERSTAND          BUILD
    (context7)          (graft)            (Bash/Claude)
        ↓                  ↓                  ↓
   Documentation       Code Graph        Implementation
   Libraries           Dependencies       Infrastructure
   APIs                Patterns           Commits
        ↓                  ↓                  ↓
        └──────────────────┼──────────────────┘
                           ↓
                    TEST & VERIFY
                    (Playwright)
                           ↓
                    EXTRACT & PARSE
                    (Firecrawl)
                           ↓
                   DOCUMENT & COMMIT
                    (Bash/Claude)
```

---

## WORKFLOW 1: AUDIT A VENTURE (Weekly Audit Workflow)

**Goal:** Run 12-layer audit on OPS-001 venture

**Steps:**

### Phase 1: Understand Current State (Graft)

```bash
# Step 1: Map the repo structure
graft map --max-dirs 10

# Step 2: Find audit-related code
graft ask "where is the audit system defined" --source

# Step 3: Find venture registration code
graft ask "how do we register a new venture" --source

# Step 4: Find customer journey flow (e.g., for staffing)
graft ask "how does an employer request workers" --source
```

**Output:** Understand code structure, patterns, data model

---

### Phase 2: Research Required Integrations (context7)

```bash
# Step 1: Get latest Stripe documentation
/context7-auto-research → Search for "Stripe payment webhook integration"

# Step 2: Get latest Supabase docs
/context7-auto-research → Search for "Supabase row-level security audit"

# Step 3: Get latest Twilio docs (for CALLCENTER)
/context7-auto-research → Search for "Twilio IVR call routing"
```

**Output:** Latest API patterns, best practices, breaking changes

---

### Phase 3: Test the Venture Live (Playwright)

```javascript
// /tmp/playwright-audit-ops-001.js
// Test: Employer → Request → Worker → Payment

const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false, slowMo: 100 });
  const page = await browser.newPage();

  const BASE_URL = 'https://ops-staff-001-staffing.vercel.app';

  try {
    // Layer 1-2: Identity & UX
    await page.goto(BASE_URL);
    console.log('✅ Page loaded:', await page.title());
    
    // Layer 3: Lead capture
    await page.click('button:has-text("Request Workers")');
    console.log('✅ Lead form opened');
    
    // Layer 4: Pipeline
    await page.fill('input[name="company_name"]', 'Test Corp');
    await page.fill('input[name="job_title"]', 'Electrician');
    await page.click('button:has-text("Submit")');
    console.log('✅ Job request submitted');
    
    // Layer 9: Payments
    await page.goto(`${BASE_URL}/dashboard`);
    const invoices = await page.locator('[data-test="invoice"]').count();
    console.log(`✅ Found ${invoices} invoices`);
    
    // Layer 12: End-to-end proof
    console.log('✅ VERIFIED: Can complete employer → job → worker flow');
    
  } catch (error) {
    console.error('❌ BLOCKED at:', error.message);
  } finally {
    await browser.close();
  }
})();
```

**Run:** `cd ~/.claude/skills/playwright-skill && node run.js /tmp/playwright-audit-ops-001.js`

**Output:** Transaction screenshots, error states, blocker identification

---

### Phase 4: Extract & Parse Data (Firecrawl)

```bash
# Step 1: Deep-scrape the OPS-001 deployed site
/firecrawl-scraper → URL: https://ops-staff-001-staffing.vercel.app
                      Extract: All form fields, API endpoints, database schema hints

# Step 2: Parse API documentation (if exists)
/firecrawl-scraper → URL: https://ops-staff-001-staffing.vercel.app/api/docs
                      Extract: Endpoint list, authentication requirements
```

**Output:** Content structure, forms, missing elements

---

### Phase 5: Document Findings (Claude + Bash)

```bash
# Step 1: Update REALITY.md with audit results
# (Manual: Add findings to 00-CONSTITUTION/REALITY.md)

# Step 2: Commit
git add 00-CONSTITUTION/REALITY.md
git commit -m "audit: OPS-001 weekly audit - layers 1-12 assessed"
```

---

## WORKFLOW 2: BUILD A MISSING VENTURE FEATURE (Engineering Workflow)

**Goal:** Build missing payment webhook for CON-001

**Steps:**

### Phase 1: Understand Existing Patterns (Graft)

```bash
# Step 1: Find existing payment handler
graft ask "how do we handle Stripe payments" --source

# Step 2: Find webhook pattern
graft grep "webhook" --in "src/"

# Step 3: See who handles webhooks
graft callers "handleWebhook" --direction in --depth 2

# Step 4: Understand full payment flow
graft callers "Stripe" --direction out --depth all
```

**Output:** Code patterns, existing implementations to copy

---

### Phase 2: Research Latest Patterns (context7)

```bash
/context7-auto-research → "Stripe webhook best practices 2026"
/context7-auto-research → "Next.js API route webhook handling"
```

**Output:** Latest security best practices, error handling patterns

---

### Phase 3: Implement & Test (Claude + Bash + Playwright)

```bash
# Step 1: Write the webhook endpoint
# (Claude writes code, you review)

# Step 2: Commit
git add src/pages/api/webhooks/stripe.ts
git commit -m "feat: Add Stripe payment webhook for CON-001"

# Step 3: Test the webhook (Playwright)
# /tmp/playwright-test-webhook.js
const browser = await chromium.launch({ headless: false });
const page = await browser.newPage();
// Simulate Stripe webhook → verify database update
```

---

### Phase 4: Verify in Production (Firecrawl)

```bash
/firecrawl-scraper → URL: https://con-001-construction.vercel.app/api/webhooks/stripe
                      Verify: Returns 200, accepts POST
```

---

## WORKFLOW 3: PORTFOLIO AUDIT (Monthly 50-Venture Audit)

**Goal:** Audit top 50 ventures simultaneously

### Parallel Execution (10 engineers × 5 ventures each)

**Engineer 1:**
```
graft map --in "repos/ventures/1-5/"           # Understand structure
/firecrawl-scraper → [5 URLs]                   # Extract content
Playwright tests → [5 transactions]             # Test flows
→ Update ventures_audits.csv
```

**Engineer 2–10:** (Same pattern, different ventures)

**Consolidation:**
```bash
git add ventures_audits.csv
git commit -m "audit: Sep monthly portfolio review - 50 ventures assessed"
```

---

## TOOL DEPENDENCY MATRIX

| Tool | Input From | Output To | When Used |
|------|-----------|-----------|-----------|
| **graft** | Codebase | Playwright, Claude | Understand patterns (always first) |
| **context7** | External docs | Claude implementation | Research latest best practices |
| **Playwright** | URLs | Firecrawl, REALITY.md | Test transactions end-to-end |
| **Firecrawl** | URLs | REALITY.md, Bash scripts | Extract content, verify structure |
| **Bash/Claude** | All tools | GitHub commits | Document & ship results |

---

## DECISION TREE: Which Tool To Use?

```
START
├─ "I need to understand the codebase"
│  → graft map
│
├─ "Where is [pattern/behavior]"
│  → graft ask "<question>" --source
│
├─ "I need all occurrences of [symbol]"
│  → graft grep "<symbol>"
│
├─ "What breaks if I change [symbol]"
│  → graft callers "<symbol>" --depth all
│
├─ "I need latest docs for [library]"
│  → /context7-auto-research
│
├─ "Does this venture work end-to-end?"
│  → Playwright (test transaction)
│
├─ "What content is on this page?"
│  → Firecrawl (scrape + parse)
│
├─ "I found a bug, how do I fix it?"
│  → graft ask "<symptom>" → Playwright (reproduce) → Claude (code) → Bash (commit)
│
└─ "I'm building a new feature"
   → graft (patterns) → context7 (docs) → Claude (code) → Playwright (test) → Bash (commit)
```

---

## SAMPLE SESSION: Audit LT-005 (Start to Finish)

**Time: Monday 9 AM, 90 minutes**

### 9:00–9:15: Understand (Graft)

```bash
graft map                                    # 2 min: Repo overview
graft ask "how do medical facilities order deliveries" --source  # 3 min
graft ask "how is payment processed" --source  # 3 min
graft callers "Supabase" --direction out     # 5 min: See all DB interactions
```

**Output:** Understand code structure, data flow, payment flow

---

### 9:15–9:30: Research (context7)

```bash
/context7-auto-research → "Stripe webhook v2026"
/context7-auto-research → "Supabase vector search for route optimization"
```

**Output:** Latest patterns for payment + routing

---

### 9:30–9:60: Test (Playwright)

```javascript
// /tmp/playwright-audit-lt005.js
// Complete flow: facility → request → dispatch → delivery → payment

const browser = await chromium.launch({ headless: false });
const page = await browser.newPage();

// 1. Navigate to site
await page.goto('https://healthroute-courier.vercel.app');

// 2. Test customer request
await page.click('[data-test="request-delivery"]');
await page.fill('[name="pickup"]', '123 Main St');
await page.fill('[name="dropoff"]', '456 Oak Ave');
await page.click('[data-test="submit"]');

// 3. Verify dispatcher sees it
const orders = await page.locator('[data-test="order"]').count();
console.log(`✅ Dispatcher sees ${orders} pending orders`);

// 4. Verify payment
const paid = await page.locator('[data-test="paid-badge"]').count();
console.log(`✅ ${paid} orders paid`);
```

**Run:** `cd ~/.claude/skills/playwright-skill && node run.js /tmp/playwright-audit-lt005.js`

**Output:** Screenshots showing each layer working

---

### 10:00–10:15: Parse & Verify (Firecrawl)

```bash
/firecrawl-scraper → https://healthroute-courier.vercel.app
                     Extract all forms, API endpoints, schema hints
```

**Output:** Confirm no missing pages/forms

---

### 10:15–10:30: Document (Bash)

```bash
# Update REALITY.md
# Commit audit results

git add 00-CONSTITUTION/REALITY.md
git commit -m "audit: LT-005 weekly - all 12 layers verified, payment webhook working"
```

---

## INTEGRATION WITH OPERATIONS

### Daily Standup (No tools needed)

"Did we close any deals?" → Check Supabase directly via CLI

---

### Weekly Audit (Graft → Playwright → Firecrawl → Bash)

Monday 9 AM: Run 5 ventures through full workflow above

---

### Monthly Portfolio (Parallel Graft + Playwright for 50 ventures)

1st Monday: 10 engineers, 5 ventures each

---

### Quarterly Board (Analysis of all Graft + Playwright results)

Each quarter: Synthesize 12 weeks of audit data

---

## KEY PRINCIPLES

1. **Always start with Graft** if working in codebase
   - Understand patterns first, implement second
   - Don't guess at code structure

2. **Use context7 before implementing**
   - Latest docs prevent tech-debt decisions
   - Check for breaking changes

3. **Playwright = proof**
   - Screenshots are evidence
   - Transaction flows are the truth

4. **Firecrawl = verification**
   - Ensure deployed site matches code
   - Catch missing UI elements

5. **Document everything**
   - Every audit → REALITY.md update
   - Every commit → evidence of what changed

---

## EXAMPLE: "Is OPS-001 Production Ready?"

**Question answered by coordinated tools:**

```
1. graft ask "what's the complete employer → payment flow" --source
   → Understand code structure

2. Playwright test → https://ops-staff-001-staffing.vercel.app
   → Run full transaction end-to-end
   → Capture: form submission, job creation, worker assignment, payment

3. Firecrawl scrape → Extract all forms, endpoints
   → Verify: No broken links, all pages accessible

4. Update REALITY.md with Layer 1–12 scores
   → Commit evidence

Result: "OPS-001 is 95% ready. Only blocker: 8 uncommitted files."
```

---

**Owner:** Operations + Engineering  
**Authority:** CP-033 (Execution)  
**Review date:** 2026-09-16 (after first week of coordinated use)
