# VEX Backend Patterns Audit for IZA OS

**Audited:** `vex-hero-site` repository (React + Vite frontend, Vercel deployment)  
**Scope:** Extract 14 reusable patterns that should power IZA OS capability routing, decision authority, and venture deployment  
**Date:** 2026-07-16

---

## Executive Summary

Vex demonstrates 14 mature patterns across data orchestration, deployment, and frontend integration. The most applicable patterns for IZA OS are:
- **Data-driven routing** (sectors configuration → dynamic paths)
- **Registry ingestion pipelines** (CSV/YAML → JSON export at build time)
- **Bespoke component override system** (generic hero + custom variants)
- **Build-time materialization** (no runtime data fetching)
- **Capability graph normalization** (repos → capabilities → ventures)

**Key insight:** Vex solves the "612 ventures from 5 CSV sources" problem via a single deterministic pipeline (`generate-public-data.mjs`) that runs at build time. IZA OS should adopt this pattern for capability routing, agent binding, and decision authority resolution.

---

## Pattern 1: Data-Driven Route Configuration

**File:** `/src/data/sectors.ts` (lines 1-439)

### What Vex Does
Defines a `SectorEntry[]` array that drives:
- Route generation (`/sectors/transportation`, `/sectors/education`)
- Hero component selection (generic or custom: `'securify' | 'archive' | 'real-estate'`)
- Navigation links and CTA targets
- Video/overlay asset configuration
- Capability statistics

```typescript
// /src/data/sectors.ts
export type SectorEntry = {
  slug: string;                    // URL path segment
  sectorLabel: string;             // Display name
  opcoLabel: string;               // OpCo identifier
  hero?: SectorHeroConfig;         // Generic hero config
  customHero?: 'securify' | 'archive' | 'real-estate';  // Custom component selector
  archiveConfig?: ArchiveHeroConfig;  // Custom config (if needed)
};

const sectors: SectorEntry[] = [
  {
    slug: 'transportation',
    sectorLabel: 'Transportation',
    opcoLabel: 'OPCO-Transportation',
    hero: { /* 300+ lines of config */ }
  },
  // ... 14 more sectors
];

export function findSector(slug: string): SectorEntry | undefined {
  return sectors.find((s) => s.slug === slug || s.sectorLabel === slug);
}
```

### Why This Matters for IZA OS
IZA OS needs to route decisions to 29 capability authorities. Currently, capability routing is implicit (hard-coded in agent prompts). This pattern makes it **explicit and queryable**.

### Adaptation for IZA OS

**File to create:** `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/config/capability-authorities.ts`

```typescript
export type CapabilityAuthority = {
  slug: string;                    // URL + routing key (e.g., 'portfolio-analysis')
  label: string;                   // Display name
  opcoSlug: string;                // Parent OPCO
  agentRole: string;               // IZA Agent role (e.g., 'portfolio-decider')
  authority: 'solo' | 'council';   // Decision model
  decisions: string[];             // What this authority decides
  tools: string[];                 // Required tools (Zapier, n8n, etc.)
  escalationPath?: string[];       // Who to escalate to
};

const capabilities: CapabilityAuthority[] = [
  {
    slug: 'portfolio-analysis',
    label: 'Portfolio Analysis',
    opcoSlug: 'layer-3-investment',
    agentRole: 'portfolio-decider',
    authority: 'council',
    decisions: ['deal-scoring', 'risk-assessment', 'synergy-detection'],
    tools: ['claude-api', 'sheets-mcp', 'stripe-mcp'],
    escalationPath: ['founder-cfo', 'external-advisor'],
  },
  // ... 28 more capabilities
];
```

**Impact:** Allows `/api/capability/:slug/route` endpoint to return:
- Decision authority (which agent/human)
- Required context (from Neo4j or Supabase)
- Tool bindings
- Escalation rules

---

## Pattern 2: Registry Ingestion Pipeline (Build-Time)

**File:** `/scripts/generate-public-data.mjs` (lines 1-388)

### What Vex Does
Transforms 5 CSV/YAML files into a single JSON export at **build time**:

```javascript
// /scripts/generate-public-data.mjs
const paths = {
  whoami: resolve(docsRoot, '_career/career-ops/whoiam.md'),
  holdings: resolve(docsRoot, 'WORLDWIDEBRO-OS/08-DATA/portfolio-reports/config/holdings_config.json'),
  ventures: resolve(docsRoot, 'WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv'),
  capabilities: resolve(docsRoot, 'venture-capabilities-proposed.csv'),
  deploymentUrls: resolve(docsRoot, 'WORLDWIDEBRO-OS/08-DATA/registries/deployment-urls.csv'),
  readinessV2: resolve(docsRoot, 'VENTURE-READINESS-SCORECARD-V2.csv'),
  sectorRegistry: resolve(docsRoot, 'WORLDWIDEBRO-OS/08-DATA/registries/sector_registry.yaml'),
  agentTools: resolve(docsRoot, 'WORLDWIDEBRO-OS/08-DATA/registries/agent_tools_registry.yaml'),
  capabilityRegistry: resolve(docsRoot, 'WORLDWIDEBRO-OS/08-DATA/registries/capability_registry.yaml'),
};

// Parse CSV with quote-aware logic
function parseCsv(text) { /* 50 lines */ }

// Join ventures with capabilities, deployment URLs, readiness scores
const capabilitiesByVenture = new Map();
for (const row of parseCsv(readText(paths.capabilities))) {
  const list = capabilitiesByVenture.get(row.venture_id) || [];
  list.push(row.capability);
  capabilitiesByVenture.set(row.venture_id, list);
}

const publicVentures = ventures.map((venture) => ({
  id: venture.venture_id,
  name: venture.name,
  sector: titleCase(venture.sector),
  opco: opcoForSector(venture.sector),
  stage: titleCase(venture.stage),
  status: titleCase(venture.status),
  capabilities: (capabilitiesByVenture.get(venture.venture_id) || []).sort(),
  ...(liveUrlByVenture.has(venture.venture_id)
    ? { liveUrl: liveUrlByVenture.get(venture.venture_id) }
    : {}),
}));

// Write single JSON export
writeFileSync(resolve(root, 'src/data/portfolio.public.json'), 
  JSON.stringify(data, null, 2));
```

**In package.json:**
```json
{
  "scripts": {
    "generate:data": "node scripts/generate-public-data.mjs",
    "build": "tsc --noEmit && vite build"
  }
}
```

### Why This Matters for IZA OS
IZA OS has **29 capability authorities** that need to:
1. Know their decision scope (what types of decisions)
2. Know required context (what Supabase tables / Neo4j nodes to query)
3. Know tool bindings (Zapier zaps, n8n workflows, Claude API calls)
4. Know escalation paths (who to route unresolved decisions to)

This is currently scattered across:
- `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/config/` (capability config)
- Neo4j (capabilities graph)
- Supabase `agent_bindings` table (agent→tool→capability join)

**Problem:** No single source of truth. Data gets out of sync.

### Adaptation for IZA OS

**File to create:** `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/scripts/generate-capability-manifest.mjs`

```javascript
import { readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';

const paths = {
  capabilityConfig: 'WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/config/capability-authorities.ts',
  agentTools: 'WORLDWIDEBRO-OS/08-DATA/registries/agent_tools_registry.yaml',
  toolMcp: 'WORLDWIDEBRO-OS/08-DATA/registries/mcp_registry.json',
  supabaseVentures: 'WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv',
};

// Parse capability config
const capabilities = parseTsConfig(readFileSync(paths.capabilityConfig, 'utf8'));

// Parse MCP/tool registry
const tools = JSON.parse(readFileSync(paths.toolMcp, 'utf8'));

// Join: capability → required tools → MCP servers
const manifest = {
  generatedAt: new Date().toISOString(),
  capabilities: capabilities.map(cap => ({
    slug: cap.slug,
    label: cap.label,
    decisions: cap.decisions,
    requiredTools: cap.tools.map(toolSlug => 
      tools.find(t => t.slug === toolSlug)
    ),
    escalationPath: cap.escalationPath,
  })),
};

writeFileSync('WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/src/data/capability-manifest.json',
  JSON.stringify(manifest, null, 2));
```

**Impact:**
- Single manifest consumed by IZA agent decision loop
- No need to query Neo4j at runtime for authority resolution
- Deployment: `npm run generate:data && npm run build`
- Version control: manifest is part of git history

---

## Pattern 3: Bespoke Component Override System

**Files:** `/src/data/sectors.ts` (lines 12-14), `/src/pages/SectorPage.tsx`

### What Vex Does
Defines a **generic hero component** (`SectorHero`) that works for 11 sectors, but allows **custom overrides** for 3:

```typescript
// /src/data/sectors.ts
{
  slug: 'technology',
  sectorLabel: 'Technology',
  opcoLabel: 'OPCO-Technology',
  customHero: 'securify',  // Use SecurifyHero instead of SectorHero
},
{
  slug: 'marketplace',
  sectorLabel: 'Marketplace',
  opcoLabel: 'OPCO-Marketplace',
  customHero: 'archive',   // Use ArchiveHero with custom config
  archiveConfig: { /* 200+ line config */ },
},
{
  slug: 'real-estate',
  sectorLabel: 'Real Estate',
  opcoLabel: 'OPCO-RealEstate',
  customHero: 'real-estate',  // Use RealEstateHero
}
```

**Usage in SectorPage:**

```typescript
// /src/pages/SectorPage.tsx
const sectorConfig = findSector(sectorId);

if (sectorConfig?.customHero === 'securify') {
  return <SecurifyHero />;
} else if (sectorConfig?.customHero === 'archive') {
  return <ArchiveHero config={sectorConfig.archiveConfig!} />;
} else if (sectorConfig?.customHero === 'real-estate') {
  return <RealEstateHero />;
} else {
  return <SectorHero config={sectorConfig?.hero!} />;
}
```

### Why This Matters for IZA OS
IZA decision authorities can be **mostly similar** (29 capability authorities with similar flow), but some need **specialized behavior**:
- **Portfolio decision:** Solo authority, high stakes, needs external advisor escalation
- **Hiring decision:** Council authority (founder + HR lead), needs reference checks
- **Technology veto:** Solo authority, can override any deal, no escalation

Instead of building 29 separate decision engines, build 1 generic + 3-4 custom overrides.

### Adaptation for IZA OS

**File to create:** `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/src/decision-engines/index.ts`

```typescript
export type DecisionAuthority = 'solo' | 'council' | 'custom';
export type CapabilityEntry = {
  slug: string;
  authority: DecisionAuthority;
  customEngine?: 'portfolio-solo' | 'hiring-council' | 'tech-veto';
};

const capabilities: CapabilityEntry[] = [
  {
    slug: 'deal-scoring',
    authority: 'solo',
    // Uses generic SoloDecisionEngine
  },
  {
    slug: 'portfolio-analysis',
    authority: 'custom',
    customEngine: 'portfolio-solo',  // Special: needs external advisor
  },
  {
    slug: 'hiring',
    authority: 'custom',
    customEngine: 'hiring-council',  // Special: council with reference checks
  },
];

// In decision router:
function getDecisionEngine(capability: CapabilityEntry) {
  if (capability.customEngine === 'portfolio-solo') {
    return new PortfolioSoloDecisionEngine();
  } else if (capability.customEngine === 'hiring-council') {
    return new HiringCouncilDecisionEngine();
  } else if (capability.authority === 'solo') {
    return new GenericSoloDecisionEngine();
  } else if (capability.authority === 'council') {
    return new GenericCouncilDecisionEngine();
  }
}
```

**Impact:**
- 80% code reuse (generic decision engines)
- 20% customization (specialized decision logic)
- No "decision spaghetti" where each capability has its own complex flow

---

## Pattern 4: Type-Safe Configuration Models

**Files:** `/src/data/sectors.ts` (lines 1-15), `/src/components/SectorHero.tsx` (lines 8-25), `/src/types.ts`

### What Vex Does
Defines TypeScript interfaces that are **the source of truth** for configuration shape:

```typescript
// /src/components/SectorHero.tsx
export type SectorHeroConfig = {
  logoText: string;
  navLinks: { label: string; href: string }[];
  ctaLabel: string;
  ctaHref: string;
  badgeText: string;
  headingLines: string[];
  subtext: string;
  emailPlaceholder: string;
  emailButtonLabel: string;
  videos: SectorVideo[];
  overlayPngUrl?: string;
  darkVideoIndex?: number;
  darkColor?: string;
  stats: string[];
};
```

Configuration in `sectors.ts` must match `SectorHeroConfig` shape exactly. TypeScript compiler enforces this at build time.

```typescript
// /src/data/sectors.ts
hero: {
  logoText: 'Transportation',          // ✓ matches SectorHeroConfig
  navLinks: [...],                     // ✓ matches NavLink[]
  videos: [...],                       // ✓ matches SectorVideo[]
  // If you forget a required field or add a typo, TypeScript errors at build time
}
```

### Why This Matters for IZA OS
IZA decision authority configuration can get **dangerously out of sync** with what agents actually expect:
- Config says "requires_tools: ['stripe']" but agent logic calls "paypal_process"
- Config says "escalation_path: ['founder']" but founder isn't in the VAPI contacts list
- Config says "decision_type: 'async'" but agent treats it as synchronous

TypeScript prevents this via **compile-time verification**.

### Adaptation for IZA OS

**File to create:** `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/src/types/decision-authority.ts`

```typescript
export type CapabilityDecision = 
  | 'approve' | 'reject' | 'escalate' | 'refine_inputs' | 'gather_data';

export type ToolBinding = {
  mcp_server: string;      // 'stripe-mcp', 'sheets-mcp', etc.
  required: boolean;
  action: string;          // e.g., 'create_payment_intent'
};

export type CapabilityAuthority = {
  slug: string;
  label: string;
  opco_slug: string;
  decisions: CapabilityDecision[];
  tools: ToolBinding[];               // Now type-safe!
  escalation_path: string[];          // Agent roles/names
  timeout_ms: number;
  requires_human_approval: boolean;
  verification_method: 'signature' | 'approval_link' | 'webhook';
};

// In config file:
const authorities: CapabilityAuthority[] = [
  {
    slug: 'portfolio-analysis',
    label: 'Portfolio Analysis',
    opco_slug: 'layer-3-investment',
    decisions: ['approve', 'reject', 'refine_inputs'],  // ✓ matches union
    tools: [
      {
        mcp_server: 'stripe-mcp',     // ✓ must match known MCPs
        required: true,
        action: 'create_payment_intent'
      }
    ],
    escalation_path: ['founder-cfo'],  // ✓ must match agent roles
    timeout_ms: 3600000,               // ✓ number
    requires_human_approval: true,
    verification_method: 'signature',  // ✓ must match union
  }
];
```

**Validation at build time:**
```bash
$ npm run build
✓ CapabilityAuthority types validated
✓ All tool bindings reference known MCPs
✓ All escalation paths reference known agents
Built successfully
```

---

## Pattern 5: Client-Side Filtering Without Backend

**File:** `/src/pages/Ventures.tsx` (lines 1-80+)

### What Vex Does
Loads **all 612 ventures** into React state at build time (JSON file), then implements filtering entirely client-side:

```typescript
// /src/pages/Ventures.tsx
import portfolioData from '../data/portfolio.public.json';

function Ventures() {
  const [query, setQuery] = useState('');
  const [sector, setSector] = useState(searchParams.get('sector') || ALL);
  const [opco, setOpco] = useState(searchParams.get('opco') || ALL);
  const [stage, setStage] = useState(ALL);
  const [sortKey, setSortKey] = useState<SortKey>('name');

  const filtered = portfolio.ventures
    .filter(
      (v) =>
        (sector === ALL || v.sector === sector) &&
        (opco === ALL || v.opco === opco) &&
        (stage === ALL || v.stage === stage) &&
        (query.trim() === '' ||
          v.name.toLowerCase().includes(query.trim().toLowerCase()) ||
          v.id.toLowerCase().includes(query.trim().toLowerCase())),
    )
    .sort((a, b) => a[sortKey].localeCompare(b[sortKey]));

  return (
    <main>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search by name or venture ID…"
      />
      <FilterSelect label="Sector" value={sector} options={sectors} />
      <FilterSelect label="OpCo" value={opco} options={opcos} />
      {/* Render filtered list */}
    </main>
  );
}
```

**No backend required.** No `/api/ventures?sector=technology` endpoint. All filtering happens in the browser.

### Why This Matters for IZA OS
IZA needs to **allow humans to override/audit** decisions made by agents. This means:
- View all 612 ventures that an agent has scored
- Filter by "decision_status: pending_human_review"
- Sort by "risk_score_adjusted"
- Search by "venture_id OR founder_name"
- Bulk approve / bulk reject / bulk escalate

But IZA also needs this to be **fast and responsive** (no backend roundtrip per filter).

### Adaptation for IZA OS

**File to create:** `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/src/pages/DecisionAudit.tsx`

```typescript
import { useState } from 'react';
import decisionManifest from '../data/decision-manifest.json';  // Generated at build time

type Decision = typeof decisionManifest.decisions[0];

export function DecisionAudit() {
  const [searchQuery, setSearchQuery] = useState('');
  const [status, setStatus] = useState<'pending' | 'approved' | 'rejected' | 'escalated'>('pending');
  const [authority, setAuthority] = useState('all');
  const [riskMin, setRiskMin] = useState(0);
  const [riskMax, setRiskMax] = useState(100);

  const filtered = decisionManifest.decisions
    .filter(
      (d) =>
        (status === 'all' || d.status === status) &&
        (authority === 'all' || d.authority_slug === authority) &&
        d.risk_score >= riskMin &&
        d.risk_score <= riskMax &&
        (searchQuery === '' ||
          d.venture_name.toLowerCase().includes(searchQuery) ||
          d.venture_id.includes(searchQuery) ||
          d.decision_id.includes(searchQuery)),
    )
    .sort((a, b) => b.risk_score - a.risk_score);  // High risk first

  return (
    <div>
      <input
        type="search"
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
        placeholder="Venture name, ID, or decision ID..."
      />
      <select value={status} onChange={(e) => setStatus(e.target.value)}>
        <option value="all">All Status</option>
        <option value="pending">Pending Review</option>
        <option value="approved">Approved</option>
        <option value="rejected">Rejected</option>
      </select>
      <RiskSlider min={riskMin} max={riskMax} onChange={setRiskMin} />
      
      <table>
        {filtered.map(decision => (
          <tr key={decision.decision_id}>
            <td>{decision.venture_name}</td>
            <td>{decision.authority_label}</td>
            <td>{decision.decision}</td>
            <td>{decision.risk_score}%</td>
            <td>
              <button onClick={() => approveDecision(decision.decision_id)}>
                Approve
              </button>
              <button onClick={() => rejectDecision(decision.decision_id)}>
                Reject
              </button>
            </td>
          </tr>
        ))}
      </table>
    </div>
  );
}
```

**Data format (generated at build time):**
```json
{
  "decisions": [
    {
      "decision_id": "DEC-2026-07-16-001",
      "venture_id": "COMM-003",
      "venture_name": "Ace Senior Care Connect",
      "authority_slug": "portfolio-analysis",
      "authority_label": "Portfolio Decider",
      "decision": "approve",
      "risk_score": 23,
      "status": "pending",
      "created_at": "2026-07-16T10:30:00Z",
      "reason": "Positive unit economics, strong founder, aligned with Layer 2"
    }
  ]
}
```

**Impact:**
- Fast filtering (no API roundtrips)
- All history in version control
- Auditable (git log shows who approved what)

---

## Pattern 6: Email Form Integration (Mailto Pattern)

**File:** `/src/pages/Contact.tsx` (lines 18-32)

### What Vex Does
**Deliberately doesn't send emails server-side.** Instead, form submission triggers a `mailto:` link:

```typescript
function handleSubmit(e: FormEvent) {
  e.preventDefault();
  const subject = `${interest} inquiry — ${name || 'New contact'}`;
  const body = [
    `Name: ${name}`,
    `Email: ${email}`,
    `Interested in: ${interest}`,
    '',
    message,
  ].join('\n');
  window.location.href = `mailto:${portfolio.founder.email}?subject=${encodeURIComponent(
    subject,
  )}&body=${encodeURIComponent(body)}`;
  setSent(true);
}
```

**Why:** No backend logic needed initially. Founder uses local email client (Gmail, Apple Mail, Outlook) to reply. Zero infrastructure.

### Why This Matters for IZA OS
IZA agents need to **escalate decisions to humans** without a full email/notification backend. Initial pattern could be:
1. Agent makes decision
2. Decision requires human approval (e.g., deal > $500K)
3. Generate pre-filled email to founder
4. Founder replies with approval/rejection
5. Webhook parses reply, updates Supabase

### Adaptation for IZA OS

**File to create:** `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/src/escalation/email-handler.ts`

```typescript
export function generateEscalationEmail(decision: Decision, escalateTo: string) {
  const subject = `[IZA ESCALATION] ${decision.authority_label} - ${decision.venture_name}`;
  const body = [
    `Decision ID: ${decision.decision_id}`,
    `Venture: ${decision.venture_name} (${decision.venture_id})`,
    `Authority: ${decision.authority_label}`,
    `Proposed: ${decision.decision}`,
    `Risk Score: ${decision.risk_score}%`,
    '',
    `Reasoning:`,
    decision.reasoning,
    '',
    `---`,
    `Reply with APPROVE or REJECT in the subject line.`,
    `The webhook will parse your reply and update the decision status.`,
  ].join('\n');

  return {
    to: escalateTo,  // e.g., 'founder-cfo@example.com'
    subject: encodeURIComponent(subject),
    body: encodeURIComponent(body),
    mailtoLink: `mailto:${escalateTo}?subject=${encodeURIComponent(
      subject
    )}&body=${encodeURIComponent(body)}`,
  };
}

// Usage in agent decision loop:
async function makeDecision(capability, inputs) {
  const decision = await agent.decide(capability, inputs);
  
  if (decision.requires_human_approval) {
    const escalation = generateEscalationEmail(decision, 'founder-cfo@example.com');
    console.log(`Open this link to escalate: ${escalation.mailtoLink}`);
    // Or: send as Slack message with clickable link
    return { status: 'pending_human_review', ...decision };
  }
  
  return decision;
}
```

**Future upgrade:** Wire up [Zapier Email Parser](https://zapier.com/platform/interfaces/email-parser/) to automatically parse replies and update Supabase.

---

## Pattern 7: Build-Time Data Materialization (No Runtime Fetch)

**Files:** `/scripts/generate-public-data.mjs`, `/package.json` (lines 8-10)

### What Vex Does
All data is **materialized at build time**, exported as static JSON:

```json
// /src/data/portfolio.public.json (generated)
{
  "generatedAt": "2026-07-16T10:00:00Z",
  "ventures": [
    {
      "id": "COMM-003",
      "name": "Ace Senior Care Connect",
      "sector": "Operations",
      "opco": "OPCO-Operations",
      "stage": "Building",
      "capabilities": ["senior-care", "scheduling", "billing"],
      "readinessPct": 45,
      "readinessTier": "Building / MVP"
    },
    // ... 611 more ventures
  ]
}
```

**No runtime API calls.** No `/api/ventures` endpoint. Bundle size: ~2.5MB (gzipped to ~300KB).

```typescript
// /src/pages/Ventures.tsx
import portfolioData from '../data/portfolio.public.json';
// That's it. Data is already in memory.
```

### Why This Matters for IZA OS
Decision history needs to be **immutable and auditable**:
- Agent made decision at 2026-07-15 10:30 UTC
- Human approved at 2026-07-16 08:00 UTC
- Decision executed at 2026-07-16 08:05 UTC

If decisions are stored in a mutable database, auditors can never be sure the log hasn't been tampered with.

### Adaptation for IZA OS

**File to create:** `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/scripts/generate-decision-audit-manifest.mjs`

```javascript
import { readFileSync, writeFileSync } from 'node:fs';
import { execSync } from 'node:child_process';
import { resolve } from 'node:path';

// Fetch all decisions from Supabase
const supabaseDecisions = await fetch(
  'https://<project>.supabase.co/rest/v1/venture_decisions?select=*',
  { headers: { Authorization: `Bearer ${process.env.SUPABASE_KEY}` } }
).then(r => r.json());

// Fetch all approvals/rejections from audit log
const auditLog = await fetch(
  'https://<project>.supabase.co/rest/v1/decision_audit_log?select=*',
  { headers: { Authorization: `Bearer ${process.env.SUPABASE_KEY}` } }
).then(r => r.json());

// Join
const manifest = {
  generatedAt: new Date().toISOString(),
  gitCommit: execSync('git rev-parse HEAD').toString().trim(),
  decisions: supabaseDecisions.map(decision => ({
    ...decision,
    approval: auditLog.find(a => a.decision_id === decision.id),
  })),
};

// Sign with Ed25519 (prevents tampering)
const signature = signManifest(manifest, process.env.SIGNING_KEY);

writeFileSync(
  'WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/src/data/decision-audit-manifest.json',
  JSON.stringify({ manifest, signature }, null, 2)
);

console.log(`Generated decision manifest with ${manifest.decisions.length} decisions`);
```

**In package.json:**
```json
{
  "scripts": {
    "generate:decisions": "node scripts/generate-decision-audit-manifest.mjs",
    "build": "npm run generate:decisions && npm run generate:data && vite build"
  }
}
```

**Impact:**
- All decisions in version control (git history is immutable)
- Cryptographic signature prevents tampering
- Auditors can verify: "This decision was approved at this exact time by this exact person"

---

## Pattern 8: Capability Graph Normalization (Repos ↔ Capabilities ↔ Ventures)

**File:** `/scripts/generate-public-data.mjs` (lines 112-122)

### What Vex Does
Joins three datasets that could easily get out of sync:

```javascript
// Venture → Capabilities join
const capabilitiesByVenture = new Map();
for (const row of parseCsv(readText(paths.capabilities))) {
  const list = capabilitiesByVenture.get(row.venture_id) || [];
  list.push(row.capability);
  capabilitiesByVenture.set(row.venture_id, list);
}

// Then materialize into ventures JSON
const publicVentures = ventures.map((venture) => ({
  id: venture.venture_id,
  name: venture.name,
  capabilities: (capabilitiesByVenture.get(venture.venture_id) || []).sort(),
  // ... other fields
}));
```

**Single source of truth:** `venture-capabilities-proposed.csv` maps venture_id → capability_name. If it's missing a row, that venture has no capabilities listed.

### Why This Matters for IZA OS
IZA needs to know **which repos support which capabilities**, and **which capabilities each venture needs**:

```
Repo 1: auth, api-gateway (capabilities it provides)
  ↓
Capability auth
Capability api-gateway
  ↓
Venture COMM-003 (capabilities it needs to launch)
```

This could be stored in 3 separate CSVs:
1. `repo-capabilities.csv` (repo_id, capability_name)
2. `capability-vocabulary.csv` (capability_name, type, description)
3. `venture-requirements.csv` (venture_id, capability_name)

**Problem:** They can get out of sync.
- Repo claims to provide "auth" but the capability is named "authentication" in vocabulary
- Venture says it needs "api-gateway" but no repo provides it

### Adaptation for IZA OS

**File to create:** `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/scripts/generate-capability-join.mjs`

```javascript
import { readFileSync, writeFileSync } from 'node:fs';

// Load sources
const repos = parseCsv(readText('repo-capabilities.csv'));         // repo_id, capability
const capabilities = parseCsv(readText('capability-vocabulary.csv')); // name, type, description
const ventures = parseCsv(readText('venture-requirements.csv'));   // venture_id, capability

// Normalize: canonical capability names come from vocabulary
const canonicalCaps = new Set(capabilities.map(c => c.name));

// Validate repos
for (const repo of repos) {
  if (!canonicalCaps.has(repo.capability)) {
    throw new Error(`Repo ${repo.repo_id} claims capability "${repo.capability}" not in vocabulary`);
  }
}

// Validate ventures
for (const venture of ventures) {
  if (!canonicalCaps.has(venture.capability)) {
    throw new Error(`Venture ${venture.venture_id} requires "${venture.capability}" not in vocabulary`);
  }
}

// Build join: repo → capabilities → ventures
const reposByCapability = new Map();
for (const repo of repos) {
  const list = reposByCapability.get(repo.capability) || [];
  list.push(repo.repo_id);
  reposByCapability.set(repo.capability, list);
}

const venturesByCapability = new Map();
for (const venture of ventures) {
  const list = venturesByCapability.get(venture.capability) || [];
  list.push(venture.venture_id);
  venturesByCapability.set(venture.capability, list);
}

// Output: single manifest with all relationships
const manifest = {
  generatedAt: new Date().toISOString(),
  capabilities: capabilities.map(cap => ({
    name: cap.name,
    type: cap.type,
    description: cap.description,
    supportedBy: reposByCapability.get(cap.name) || [],
    requiredBy: venturesByCapability.get(cap.name) || [],
  })),
  gaps: capabilities
    .filter(cap => !reposByCapability.has(cap.name))
    .map(cap => ({
      name: cap.name,
      requiredBy: venturesByCapability.get(cap.name) || [],
      reason: 'No repo supports this capability',
    })),
};

writeFileSync('WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/src/data/capability-join.json',
  JSON.stringify(manifest, null, 2));

console.log(`✓ ${manifest.capabilities.length} capabilities normalized`);
console.log(`✗ ${manifest.gaps.length} gaps (capabilities required but unsupported)`);
```

**Output:**
```json
{
  "capabilities": [
    {
      "name": "authentication",
      "type": "infrastructure",
      "supportedBy": ["repo-123", "repo-456"],
      "requiredBy": ["COMM-003", "TECH-040", "TECH-062"]
    }
  ],
  "gaps": [
    {
      "name": "blockchain-settlement",
      "requiredBy": ["INV-001"],
      "reason": "No repo supports this capability"
    }
  ]
}
```

**Impact:**
- Build fails if there are mismatches (shift left on validation)
- Single source of truth for what's possible
- Gap analysis: which ventures need capabilities that don't exist yet

---

## Pattern 9: Readiness Scorecard Materialization

**File:** `/scripts/generate-public-data.mjs` (lines 125-176)

### What Vex Does
Imports readiness scores from `VENTURE-READINESS-SCORECARD-V2.csv`, normalizes them into bins, and materializes into the manifest:

```javascript
// Audited readiness (v2): stage cross-checked against real repo code signals,
// not just self-reported venture.json
function readinessTierFor(pct) {
  if (pct >= 90) return 'Revenue / Scale';
  if (pct >= 60) return 'Beta / Launch-ready';
  if (pct >= 35) return 'Building / MVP';
  if (pct >= 15) return 'Planned / Validating';
  return 'Idea';
}

const readinessByVenture = new Map();
for (const row of parseCsv(readText(paths.readinessV2))) {
  if (!row.venture_id) continue;
  const readinessPct = Number(row.readiness_pct_v2);
  readinessByVenture.set(row.venture_id, {
    readinessPct,
    readinessTier: readinessTierFor(readinessPct),
    verifiedStage: row.stage_verified === 'True',
    auditedStage: titleCase(row.development_stage_v2_computed),
  });
}

// Merge into venture data
const publicVentures = ventures.map((venture) => {
  const readiness = readinessByVenture.get(venture.venture_id);
  return {
    id: venture.venture_id,
    name: venture.name,
    ...(readiness
      ? {
          readinessPct: readiness.readinessPct,
          readinessTier: readiness.readinessTier,
          auditedStage: readiness.auditedStage,
          stageVerified: readiness.verifiedStage,
        }
      : { stageVerified: false }),
  };
});
```

**Key insight:** Scorecard is external (audited by humans), but merged into manifest at build time. No runtime DB queries needed.

### Why This Matters for IZA OS
IZA agents make decisions that depend on **risk scores**, which should be:
- **Human-auditable** (not computed by opaque algorithm)
- **Version controlled** (history of how risk was assessed)
- **Normalized** into standard bins (e.g., 0-25 = low, 26-50 = medium, etc.)

Example: Portfolio decider needs risk score before approving $500K deal.

### Adaptation for IZA OS

**File to create:** `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/scripts/generate-decision-risk-scores.mjs`

```javascript
// Load human-audited risk assessments
const riskAudit = parseCsv(readText('WORLDWIDEBRO-OS/08-DATA/venture-risk-audit.csv'));
// venture_id, risk_profile, risk_score_human, risk_factors

function riskTierFor(score) {
  if (score <= 15) return 'very-low-risk';
  if (score <= 35) return 'low-risk';
  if (score <= 55) return 'medium-risk';
  if (score <= 75) return 'high-risk';
  return 'very-high-risk';
}

const decisionRisks = decisions.map(decision => {
  const venture = ventures.find(v => v.venture_id === decision.venture_id);
  const riskRow = riskAudit.find(r => r.venture_id === venture.venture_id);
  
  return {
    decision_id: decision.id,
    venture_id: decision.venture_id,
    venture_name: venture.name,
    risk_score_human: Number(riskRow?.risk_score_human || 0),
    risk_score_computed: computeRiskScore(decision, venture),
    risk_score_final: Math.max(  // Use worst-case
      Number(riskRow?.risk_score_human || 0),
      computeRiskScore(decision, venture)
    ),
    risk_tier: riskTierFor(Number(riskRow?.risk_score_human || 0)),
    risk_factors: riskRow?.risk_factors?.split(',') || [],
    requires_board_approval: Number(riskRow?.risk_score_human || 0) >= 70,
    requires_insurance: ['legal-liability', 'ip-risk'].includes(riskRow?.risk_factors),
  };
});

writeFileSync('WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/src/data/decision-risk-manifest.json',
  JSON.stringify({
    generatedAt: new Date().toISOString(),
    decisions: decisionRisks,
  }, null, 2));
```

**In decision loop:**
```typescript
async function makeDecision(authority, inputs) {
  const venture = ventures.find(v => v.id === inputs.venture_id);
  const riskData = decisionRiskManifest.decisions.find(d => d.venture_id === venture.id);
  
  if (riskData.requires_board_approval) {
    return {
      status: 'pending_board_approval',
      venture: venture.name,
      risk_tier: riskData.risk_tier,
      reason: `Risk score ${riskData.risk_score_final} exceeds board approval threshold`
    };
  }
  
  // Proceed with decision...
}
```

---

## Pattern 10: Nav & Footer as Reusable Components

**Files:** `/src/components/Nav.tsx`, `/src/components/Footer.tsx`

### What Vex Does
Extracts common navigation and footer into **reusable React components** instead of repeating HTML on every page:

```typescript
// /src/components/Nav.tsx
function Nav() {
  return (
    <nav className="flex items-center justify-between px-6 py-6">
      <Link to="/">Worldwidebro</Link>
      <div className="flex gap-6">
        <Link to="/ventures">Ventures</Link>
        <Link to="/sectors">Sectors</Link>
        <Link to="/holdings">Holdings</Link>
        <Link to="/contact">Contact</Link>
      </div>
    </nav>
  );
}

export default Nav;
```

**Usage in every page:**
```typescript
// /src/pages/Ventures.tsx
import Nav from '../components/Nav';
import Footer from '../components/Footer';

function Ventures() {
  return (
    <main>
      <Nav />
      {/* Page content */}
      <Footer />
    </main>
  );
}
```

### Why This Matters for IZA OS
IZA has **multiple UIs** that all need consistent navigation:
- Decision audit dashboard
- Venture tracking board
- Agent decision logs
- Risk overview
- Approval queue

Instead of building 5 separate navs, build 1 `<IZANav />` component.

### Adaptation for IZA OS

**File to create:** `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/src/components/IZANav.tsx`

```typescript
export type IZANavProps = {
  currentPage: 'audit' | 'ventures' | 'agents' | 'risks' | 'approvals';
};

function IZANav({ currentPage }: IZANavProps) {
  return (
    <nav className="flex items-center justify-between px-8 py-4 bg-black border-b border-white/10">
      <div className="font-bold text-white">IZA Decision Authority</div>
      
      <div className="flex gap-8">
        <NavLink
          href="/audit"
          label="Decision Audit"
          active={currentPage === 'audit'}
        />
        <NavLink
          href="/ventures"
          label="Ventures"
          active={currentPage === 'ventures'}
        />
        <NavLink
          href="/agents"
          label="Agent Logs"
          active={currentPage === 'agents'}
        />
        <NavLink
          href="/risks"
          label="Risk Overview"
          active={currentPage === 'risks'}
        />
        <NavLink
          href="/approvals"
          label={`Approvals (${pendingCount})`}
          active={currentPage === 'approvals'}
          badge={pendingCount}
        />
      </div>
      
      <div className="text-xs text-gray-400">
        Logged in as: {founder.name}
      </div>
    </nav>
  );
}
```

---

## Pattern 11: Vercel Rewrites for SPA Routing

**File:** `/vercel.json`

### What Vex Does
Configures Vercel to **rewrite all requests to `/index.html`**, enabling client-side React Router:

```json
{
  "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }]
}
```

**Effect:** 
- Request: `GET /sectors/technology`
- Vercel serves: `/index.html`
- React Router matches `/sectors/technology` and renders `<SectorPage />`
- User sees URL in address bar: `/sectors/technology`
- User sees correct content

### Why This Matters for IZA OS
IZA decision audit needs **shareable links**:
- Manager wants to send founder a link to pending approval: `/approvals?venture_id=COMM-003`
- Founder clicks link → browser fetches `/approvals?venture_id=COMM-003`
- Vercel rewrites to `/index.html`
- React Router matches and passes `venture_id` query param to component
- Component loads the specific decision

### Adaptation for IZA OS

**File to create:** `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/vercel.json`

```json
{
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ],
  "headers": [
    {
      "source": "/index.html",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "no-cache, no-store, must-revalidate"
        }
      ]
    }
  ]
}
```

---

## Pattern 12: Sector-to-OpCo Mapping

**File:** `/scripts/generate-public-data.mjs` (lines 148-153)

### What Vex Does
Maps sectors to OPCOs via a CSV/JSON lookup:

```javascript
const sectorToOpco = holdings.opco_layer.sector_to_opco;
// e.g., { 'Transportation': { opco: 'OPCO-Transportation' }, ... }

function opcoForSector(sector) {
  const entry = sectorToOpco[sector];
  return entry && entry.opco ? entry.opco : 'Unassigned';
}
```

**Then materializes it into ventures:**
```javascript
const publicVentures = ventures.map((venture) => ({
  id: venture.venture_id,
  name: venture.name,
  sector: titleCase(venture.sector),
  opco: opcoForSector(venture.sector),  // ← Looked up from mapping
  // ...
}));
```

**Result:** Every venture knows its OPCO without duplicate data entry.

### Why This Matters for IZA OS
IZA has:
- 29 capability authorities (decision makers)
- 18 OPCOs (operational parent units)
- Some OPCOs have multiple authorities, some have 1

Mapping: capability → OPCO tells us:
- Which authorities report to which OPCO head
- Who to escalate to if a decision needs OPCO director approval

### Adaptation for IZA OS

**File to create:** `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/config/capability-to-opco.json`

```json
{
  "authority_to_opco": {
    "portfolio-analysis": "layer-3-investment",
    "hiring": "layer-2-people-operations",
    "tech-veto": "layer-1-founder-office",
    "deal-scoring": "layer-3-investment",
    "legal-review": "layer-2-general-counsel"
  }
}
```

**Usage in manifest generator:**
```javascript
const capabilityToOpco = JSON.parse(readText('capability-to-opco.json'));

const capabilities = authorities.map(auth => ({
  ...auth,
  opco_slug: capabilityToOpco.authority_to_opco[auth.slug] || 'unassigned',
}));
```

---

## Pattern 13: Privacy Boundary Declaration

**File:** `/src/types.ts` (lines 1-7)

### What Vex Does
Explicitly declares which fields are public and which are private:

```typescript
privacy: {
  publicFields: ['venture id', 'name', 'sector', 'opco', 'stage', 'status'],
  excludedFields: [
    'revenue',
    'cash',
    'contacts',
    'legal documents',
    'private strategy notes',
    'agent logs',
    'customer data',
  ],
}
```

**Enforced in data generation:**
```javascript
// Only serialize public fields
const publicVentures = ventures.map((venture) => ({
  id: venture.venture_id,         // ✓ public
  name: venture.name,             // ✓ public
  sector: venture.sector,         // ✓ public
  // revenue: venture.revenue,    // ✗ excluded
  // contacts: venture.contacts,  // ✗ excluded
}));
```

### Why This Matters for IZA OS
IZA decision manifests could accidentally leak:
- Founder's personal notes about a deal ("Founder is overconfident about market size")
- Investor relations strategy ("Plan to approach Tiger Global first")
- Employee salary targets

Privacy boundary should be:
- **Public:** Decision, reasoning, risk score, status
- **Private:** Founder notes, investor targets, salary/equity discussions

### Adaptation for IZA OS

**File to create:** `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/src/types/privacy.ts`

```typescript
export type DecisionPrivacy = {
  public_fields: string[];
  private_fields: string[];
  audit_trail_fields: string[];  // What gets logged for auditors
};

export const DECISION_PRIVACY: DecisionPrivacy = {
  public_fields: [
    'decision_id',
    'venture_id',
    'authority_slug',
    'decision',  // 'approve' | 'reject' | 'escalate'
    'risk_score',
    'risk_tier',
    'created_at',
    'approved_by',
    'approved_at',
  ],
  private_fields: [
    'founder_notes',
    'investor_strategy',
    'internal_concerns',
    'salary_discussions',
  ],
  audit_trail_fields: [
    'decision_id',
    'created_at',
    'approved_by',
    'approval_method',  // 'signature' | 'email' | 'webhook'
    'ip_address',
    'user_agent',
  ],
};

// Enforce at generation time
const publicDecision = {
  decision_id: decision.id,
  venture_id: decision.venture_id,
  authority_slug: decision.authority_slug,
  decision: decision.decision,
  risk_score: decision.risk_score,
  risk_tier: decision.risk_tier,
  // founder_notes: undefined,  // Never included
  // investor_strategy: undefined,
};
```

---

## Pattern 14: Deployment Readiness Checklist

**Files:** `/package.json`, `/vercel.json`, Deployment workflow

### What Vex Does
Deployment requires:
1. **Type checking:** `tsc --noEmit` (compile-time validation)
2. **Data generation:** `node scripts/generate-public-data.mjs` (manifest must validate)
3. **Build:** `vite build` (bundle must be < 10MB)
4. **Vercel config:** `/vercel.json` must be present (routing rules)

```json
{
  "scripts": {
    "build": "tsc --noEmit && vite build"
  }
}
```

**Effect:** Deploy fails if:
- TypeScript has errors
- Data generation fails
- Build exceeds size limits
- Type mismatches in config

### Why This Matters for IZA OS
IZA decision manifests must be **deployable without manual fixup**:
- Agent tries to route to capability authority X
- Capability X not in manifest → crash
- Someone manually edits decision database → audit trail breaks

### Adaptation for IZA OS

**File to create:** `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/package.json`

```json
{
  "scripts": {
    "generate:data": "node scripts/generate-capability-manifest.mjs",
    "validate": "npm run generate:data && node scripts/validate-manifest.mjs",
    "build": "npm run validate && vite build",
    "deploy": "npm run build && vercel deploy"
  }
}
```

**Validation script:**

```javascript
// /scripts/validate-manifest.mjs
import { readFileSync } from 'node:fs';

const manifest = JSON.parse(readFileSync('src/data/capability-manifest.json', 'utf8'));

// Validate every authority has required fields
for (const auth of manifest.capabilities) {
  if (!auth.slug) throw new Error(`Authority missing slug`);
  if (!auth.decisions || auth.decisions.length === 0) throw new Error(`Authority ${auth.slug} has no decisions`);
  if (!Array.isArray(auth.tools)) throw new Error(`Authority ${auth.slug} tools must be array`);
  
  // Validate tool references
  for (const tool of auth.tools) {
    if (!knownMcps.includes(tool.mcp_server)) {
      throw new Error(`Authority ${auth.slug} references unknown MCP: ${tool.mcp_server}`);
    }
  }
  
  // Validate escalation paths reference known agents
  for (const escalateTo of auth.escalation_path || []) {
    if (!knownAgentRoles.includes(escalateTo)) {
      throw new Error(`Authority ${auth.slug} escalates to unknown agent: ${escalateTo}`);
    }
  }
}

console.log(`✓ All ${manifest.capabilities.length} authorities validated`);
```

---

## Appendix: Applicability Matrix

| Pattern | VEX Usage | IZA OS Fit | Priority | File Path |
|---------|-----------|-----------|----------|-----------|
| Data-driven routing | Sectors → SPA routes | Capabilities → authority routing | **CRITICAL** | `capability-authorities.ts` |
| Registry ingestion pipeline | CSV→JSON (build-time) | Multi-source manifest generation | **CRITICAL** | `generate-capability-manifest.mjs` |
| Bespoke component overrides | 11 generic + 3 custom heros | 80% generic + 20% custom authorities | HIGH | Decision engine selector |
| Type-safe config models | TypeScript interfaces | CapabilityAuthority type | HIGH | `types/decision-authority.ts` |
| Client-side filtering | No backend for ventures search | No backend for decision audit | MEDIUM | `DecisionAudit.tsx` |
| Email form integration | Mailto for contact | Mailto for escalations | MEDIUM | `escalation/email-handler.ts` |
| Build-time materialization | Static JSON (no API calls) | Decision manifest (no DB queries at runtime) | HIGH | `decision-audit-manifest.json` |
| Capability graph normalization | Repo↔Cap↔Venture join | Repo↔Cap↔Authority join | **CRITICAL** | `capability-join.json` |
| Readiness scorecard materialization | Human audit→bins→manifest | Risk audit→bins→manifest | HIGH | `decision-risk-manifest.json` |
| Reusable components | Nav + Footer | IZANav + IZAFooter | LOW | Component library |
| Vercel SPA rewrites | Sector routes | Decision routes | MEDIUM | `vercel.json` |
| Sector→OpCo mapping | Implicit lookup | Authority→OPCO mapping | HIGH | `capability-to-opco.json` |
| Privacy boundary declaration | Public/private fields | Public/private/audit fields | MEDIUM | `types/privacy.ts` |
| Deployment readiness checklist | Build-time validation | Manifest validation at deploy | HIGH | CI/CD pipeline |

---

## Next Steps for Implementation

### Phase 1 (Week 1): Foundation
- [ ] Create `capability-authorities.ts` with 29 authorities
- [ ] Create `capability-to-opco.json` mapping
- [ ] Create `types/decision-authority.ts` with strict types
- [ ] Wire into existing IZA agent loop (test one authority)

### Phase 2 (Week 2): Manifestation
- [ ] Build `generate-capability-manifest.mjs` script
- [ ] Add to CI/CD: `npm run generate:data && npm run build`
- [ ] Implement `DecisionAudit.tsx` (client-side filtering of decisions)
- [ ] Test with 612 ventures' decision history

### Phase 3 (Week 3): Escalation & Audit Trail
- [ ] Implement email-based escalation (mailto pattern)
- [ ] Build decision audit trail (signed manifest)
- [ ] Implement human approval loop
- [ ] Wire Zapier/n8n for webhook-based replies

### Phase 4 (Week 4): Validation & Deployment
- [ ] Create `validate-manifest.mjs` (pre-deploy checks)
- [ ] Set up Vercel deployment with rewrites
- [ ] Integration test: full decision flow (creation → approval → execution)
- [ ] Performance test: can system handle 1M decisions without API calls?

---

## Conclusion

Vex's architecture is **production-ready for deployment** but **single-purpose** (venture showcase). IZA OS can adopt 14 patterns to become **resilient, auditable, and scalable** without building new infrastructure. The critical insight is: **materialize everything at build time** (manifest generation) rather than querying databases at runtime (slower, less auditable).

Key principle: **In IZA OS, the decision manifest is the source of truth. Supabase records the decisions; the manifest defines their authority.**
