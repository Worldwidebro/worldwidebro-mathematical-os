import { useState } from "react";

// ─── Venture Data (from ventures/registry.json via extract-ventures.ts) ───────
const VENTURES = [
  {
    ventureId: "FIN-001",
    name: "GenixBank Lite",
    sector: "financial",
    status: "mvp",
    revenueModel: "licensing",
    automationLevel: 0.85,
    hasCode: true,
    hasDashboard: true,
    hasPayments: false,
    githubRepo: "https://github.com/Worldwidebro/fin-001-genixbank-lite",
    agentsAssigned: ["banking_agent", "compliance_agent"],
    infrastructure: ["postgres", "stripe", "docker"],
    monthlyCostEstimate: 240,
    revenueProjection: 10000,
    completionPercent: 95,
    nextAction: "Add Stripe integration",
    priority: "critical",
  },
  {
    ventureId: "FIN-006",
    name: "Tax Prep Filing Services",
    sector: "financial",
    status: "mvp",
    revenueModel: "subscription",
    automationLevel: 0.85,
    hasCode: true,
    hasDashboard: true,
    hasPayments: false,
    dashboardPort: 8511,
    githubRepo: "https://github.com/Worldwidebro/fin-006-tax-prep-filing-services",
    agentsAssigned: ["tax_parser_agent", "filing_agent", "client_onboarding_agent"],
    infrastructure: ["postgres", "stripe", "docker"],
    monthlyCostEstimate: 240,
    revenueProjection: 10000,
    completionPercent: 95,
    nextAction: "Add Stripe integration",
    priority: "critical",
  },
  {
    ventureId: "FIN-009",
    name: "Crypto Tax Optimizer",
    sector: "financial",
    status: "mvp",
    revenueModel: "subscription",
    automationLevel: 0.85,
    hasCode: true,
    hasDashboard: true,
    hasPayments: false,
    dashboardPort: 8512,
    githubRepo: "https://github.com/Worldwidebro/fin-009-crypto-tax-optimizer",
    agentsAssigned: ["crypto_parser_agent", "tax_optimizer_agent"],
    infrastructure: ["postgres", "stripe", "docker"],
    monthlyCostEstimate: 240,
    revenueProjection: 8000,
    completionPercent: 95,
    nextAction: "Add Stripe integration",
    priority: "critical",
  },
  {
    ventureId: "FIN-021",
    name: "Tax Deduction Finder",
    sector: "financial",
    status: "mvp",
    revenueModel: "subscription",
    automationLevel: 0.85,
    hasCode: true,
    hasDashboard: true,
    hasPayments: false,
    dashboardPort: 8513,
    githubRepo: "https://github.com/Worldwidebro/fin-021-tax-deduction-finder",
    agentsAssigned: ["deduction_finder_agent", "receipt_parser_agent"],
    infrastructure: ["postgres", "stripe", "docker"],
    monthlyCostEstimate: 240,
    revenueProjection: 6000,
    completionPercent: 95,
    nextAction: "Add Stripe integration",
    priority: "critical",
  },
  {
    ventureId: "FIN-033",
    name: "AI Tax Preparation Service",
    sector: "financial",
    status: "mvp",
    revenueModel: "subscription",
    automationLevel: 0.85,
    hasCode: true,
    hasDashboard: true,
    hasPayments: false,
    dashboardPort: 8514,
    githubRepo: "https://github.com/Worldwidebro/fin-033-ai-tax-preparation-service",
    agentsAssigned: ["tax_prep_agent", "document_processor_agent"],
    infrastructure: ["postgres", "stripe", "docker"],
    monthlyCostEstimate: 240,
    revenueProjection: 12000,
    completionPercent: 95,
    nextAction: "Add Stripe integration",
    priority: "critical",
  },
  {
    ventureId: "ARBITRAGE-001",
    name: "Arbitrage Nexus",
    sector: "e-commerce",
    status: "mvp",
    revenueModel: "subscription",
    automationLevel: 0.75,
    hasCode: true,
    hasDashboard: false,
    hasPayments: false,
    githubRepo: "https://github.com/Worldwidebro/arbitrage-nexus",
    agentsAssigned: ["arbitrage_finder_agent", "price_tracker_agent"],
    infrastructure: ["postgres", "redis", "docker"],
    monthlyCostEstimate: 180,
    revenueProjection: 15000,
    completionPercent: 85,
    nextAction: "Add payment integration + dashboard",
    priority: "high",
  },
  {
    ventureId: "CON-001",
    name: "Ace Construction",
    sector: "construction",
    status: "validation",
    revenueModel: "services",
    automationLevel: 0.25,
    hasCode: true,
    hasDashboard: false,
    hasPayments: false,
    githubRepo: "https://github.com/Worldwidebro/ace-construction",
    agentsAssigned: ["operator_agent", "market_analysis_agent", "process_improvement_agent"],
    infrastructure: ["static-site", "vercel-or-netlify"],
    monthlyCostEstimate: 25,
    revenueProjection: 15000,
    completionPercent: 40,
    nextAction: "Create dedicated repository and wire contact intake",
    priority: "high",
  },
];

const SECTORS = [
  {
    sectorId: "financial",
    name: "Financial Services",
    color: "#10b981",
    ventureCount: 35,
    repoCount: 35,
    description: "AI-powered tax, banking, crypto, and financial automation tools",
    seeded: 5,
  },
  {
    sectorId: "e-commerce",
    name: "E-Commerce & Arbitrage",
    color: "#8b5cf6",
    ventureCount: 4,
    repoCount: 4,
    description: "Price arbitrage, product sourcing, and e-commerce automation",
    seeded: 1,
  },
  {
    sectorId: "construction",
    name: "Construction",
    color: "#f59e0b",
    ventureCount: 1,
    repoCount: 1,
    description: "Operator-led construction services with AI process improvement",
    seeded: 1,
  },
];

const PORTFOLIO_STATS = {
  totalVentures: 40,
  totalRepos: 550,
  venturesWithCode: 40,
  venturesWithDashboards: 35,
  venturesRevenueReady: 0,
  githubOrg: "Worldwidebro",
  totalProjectedRevenue: 76000,
};

// ─── Architecture Data ────────────────────────────────────────────────────────
const LAYERS = [
  {
    id: "client", label: "Client Browser", sublabel: "Vercel Edge CDN",
    color: "#e2e8f0", bg: "#1e2433", border: "#e2e8f040",
    nodes: [
      { id: "nextjs", label: "Next.js 14", sub: "App Router · SSR · Edge" },
      { id: "clerk_fe", label: "Clerk Auth", sub: "Session tokens" },
      { id: "posthog_fe", label: "PostHog", sub: "Events · Funnels" },
    ],
  },
  {
    id: "content", label: "Content Layer", sublabel: "No database needed",
    color: "#a78bfa", bg: "#1a1428", border: "#a78bfa40",
    nodes: [
      { id: "sanity", label: "Sanity CMS", sub: "Case studies · Blog · Testimonials" },
      { id: "sanity_cdn", label: "Sanity CDN", sub: "Image delivery · GROQ API" },
      { id: "static", label: "Static Assets", sub: "Vercel Blob · Images" },
    ],
  },
  {
    id: "comms", label: "Communications Layer", sublabel: "Stateless — no storage",
    color: "#34d399", bg: "#0f1f18", border: "#34d39940",
    nodes: [
      { id: "resend", label: "Resend", sub: "Lead emails · Notifications" },
      { id: "calendly", label: "Calendly", sub: "Discovery call booking" },
      { id: "claude_chat", label: "Claude Haiku", sub: "Chat widget · Pre-qualification" },
      { id: "claude_scope", label: "Claude Sonnet", sub: "Scoping form analysis" },
    ],
  },
  {
    id: "crm", label: "CRM / Lead Layer", sublabel: "Your existing stack",
    color: "#fbbf24", bg: "#1f1a0a", border: "#fbbf2440",
    nodes: [
      { id: "clickup", label: "ClickUp", sub: "Lead tasks · Pipeline" },
      { id: "notion", label: "Notion", sub: "Client briefs · Docs" },
      { id: "slack", label: "Slack", sub: "Lead alerts · Team notifs" },
    ],
  },
  {
    id: "platform", label: "Iza OS Platform Layer", sublabel: "Existing infrastructure — read via API",
    color: "#f87171", bg: "#1f0f0f", border: "#f8717140",
    nodes: [
      { id: "postgres", label: "PostgreSQL", sub: "Client data · Project status" },
      { id: "redis", label: "Redis", sub: "Chat sessions · Rate limiting" },
      { id: "chromadb", label: "ChromaDB", sub: "RAG · Knowledge retrieval" },
      { id: "kong", label: "Kong Gateway", sub: "API routing · Auth" },
    ],
  },
  {
    id: "auth", label: "Auth & Analytics", sublabel: "Managed services",
    color: "#60a5fa", bg: "#0f1520", border: "#60a5fa40",
    nodes: [
      { id: "clerk_be", label: "Clerk", sub: "User sessions · JWT" },
      { id: "posthog_be", label: "PostHog Cloud", sub: "Analytics · Session replay" },
      { id: "vercel_anal", label: "Vercel Analytics", sub: "Core web vitals · Perf" },
    ],
  },
];

const FLOWS = [
  { from: "nextjs", to: "sanity", label: "GROQ fetch", color: "#a78bfa", type: "query" },
  { from: "nextjs", to: "sanity_cdn", label: "Image CDN", color: "#a78bfa", type: "asset" },
  { from: "nextjs", to: "clerk_fe", label: "Session check", color: "#60a5fa", type: "auth" },
  { from: "clerk_fe", to: "clerk_be", label: "JWT verify", color: "#60a5fa", type: "auth" },
  { from: "nextjs", to: "posthog_fe", label: "Track events", color: "#94a3b8", type: "analytics" },
  { from: "posthog_fe", to: "posthog_be", label: "Event stream", color: "#94a3b8", type: "analytics" },
  { from: "nextjs", to: "resend", label: "Form submit", color: "#34d399", type: "lead" },
  { from: "nextjs", to: "calendly", label: "Booking embed", color: "#34d399", type: "lead" },
  { from: "resend", to: "clickup", label: "Create lead task", color: "#fbbf24", type: "crm" },
  { from: "resend", to: "slack", label: "Alert webhook", color: "#fbbf24", type: "crm" },
  { from: "claude_scope", to: "notion", label: "Save brief", color: "#fbbf24", type: "crm" },
  { from: "nextjs", to: "claude_chat", label: "Chat message", color: "#34d399", type: "ai" },
  { from: "nextjs", to: "claude_scope", label: "Scoping form", color: "#34d399", type: "ai" },
  { from: "claude_chat", to: "redis", label: "Session store", color: "#f87171", type: "platform" },
  { from: "claude_scope", to: "chromadb", label: "RAG lookup", color: "#f87171", type: "platform" },
  { from: "nextjs", to: "kong", label: "Portal API calls", color: "#f87171", type: "platform" },
  { from: "kong", to: "postgres", label: "Project data", color: "#f87171", type: "platform" },
];

const FLOW_TYPE_LEGEND = [
  { type: "query", color: "#a78bfa", label: "Content fetch" },
  { type: "auth", color: "#60a5fa", label: "Auth / session" },
  { type: "lead", color: "#34d399", label: "Lead capture" },
  { type: "crm", color: "#fbbf24", label: "CRM routing" },
  { type: "ai", color: "#34d399", label: "AI inference" },
  { type: "platform", color: "#f87171", label: "Platform API" },
  { type: "analytics", color: "#94a3b8", label: "Analytics" },
];

const V2_NODES = ["redis", "chromadb"];

// ─── Helpers ──────────────────────────────────────────────────────────────────
const SECTOR_META = {
  financial:    { color: "#10b981", label: "Financial" },
  "e-commerce": { color: "#8b5cf6", label: "E-Commerce" },
  construction: { color: "#f59e0b", label: "Construction" },
};

const STATUS_META = {
  mvp:        { color: "#10b981", bg: "#10b98115", label: "MVP" },
  validation: { color: "#fbbf24", bg: "#fbbf2415", label: "Validation" },
  ideation:   { color: "#94a3b8", bg: "#94a3b815", label: "Ideation" },
  production: { color: "#60a5fa", bg: "#60a5fa15", label: "Production" },
};

const PRIORITY_META = {
  critical: { color: "#f87171", bg: "#f8717115" },
  high:     { color: "#fbbf24", bg: "#fbbf2415" },
  medium:   { color: "#94a3b8", bg: "#94a3b815" },
  low:      { color: "#475569", bg: "#47556915" },
};

function fmt(n) {
  if (n >= 1000) return `$${(n / 1000).toFixed(0)}k`;
  return `$${n}`;
}

// ─── Component ────────────────────────────────────────────────────────────────
export default function IzaOSHub() {
  const [view, setView] = useState("portfolio");
  const [sectorFilter, setSectorFilter] = useState("all");
  const [statusFilter, setStatusFilter] = useState("all");
  const [activeNode, setActiveNode] = useState(null);
  const [activeLayer, setActiveLayer] = useState(null);
  const [expanded, setExpanded] = useState(null);

  const filtered = VENTURES.filter(v => {
    if (sectorFilter !== "all" && v.sector !== sectorFilter) return false;
    if (statusFilter !== "all" && v.status !== statusFilter) return false;
    return true;
  });

  const highlightedFlows = activeNode
    ? FLOWS.filter(f => f.from === activeNode || f.to === activeNode)
    : FLOWS;

  const totalRevenue = filtered.reduce((s, v) => s + v.revenueProjection, 0);

  const TABS = [
    { id: "portfolio",    label: "Portfolio" },
    { id: "sectors",      label: "Sectors" },
    { id: "architecture", label: "Architecture" },
    { id: "db",           label: "DB Decision" },
  ];

  return (
    <div style={{
      background: "#060810",
      minHeight: "100vh",
      fontFamily: "'IBM Plex Mono', 'Fira Code', monospace",
      color: "#e2e8f0",
    }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500&family=Epilogue:wght@400;700;900&display=swap');
        * { box-sizing: border-box; margin: 0; padding: 0; }
        ::-webkit-scrollbar { width: 3px; }
        ::-webkit-scrollbar-thumb { background: #ffffff20; }
        .tab { background: transparent; border: none; border-bottom: 2px solid transparent; color: #64748b; padding: 8px 18px; cursor: pointer; font-family: 'IBM Plex Mono', monospace; font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; transition: all 0.15s; }
        .tab:hover { color: #e2e8f0; }
        .tab.active { color: #e2e8f0; border-bottom-color: #e2e8f0; }
        .pill { transition: all 0.15s ease; cursor: pointer; }
        .pill:hover { transform: scale(1.03); }
        .layer-card { transition: all 0.2s ease; cursor: pointer; }
        .layer-card:hover { transform: translateX(3px); }
        .venture-card { transition: background 0.15s; border-bottom: 1px solid #ffffff08; }
        .venture-card:hover { background: #ffffff05; }
        .filter-btn { background: transparent; border: 1px solid #ffffff15; color: #64748b; padding: 5px 12px; border-radius: 4px; cursor: pointer; font-family: 'IBM Plex Mono', monospace; font-size: 10px; letter-spacing: 0.06em; transition: all 0.15s; }
        .filter-btn:hover { color: #e2e8f0; border-color: #ffffff30; }
        .filter-btn.active { color: #e2e8f0; border-color: #ffffff50; background: #ffffff08; }
        @keyframes fadeUp { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
        .fade-up { animation: fadeUp 0.25s ease both; }
        @keyframes pulse-dot { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }
        .pulse { animation: pulse-dot 2s ease infinite; }
        .flow-row { border-bottom: 1px solid #ffffff08; transition: background 0.15s; }
        .flow-row:hover { background: #ffffff06; }
        .stat-card { border: 1px solid #ffffff10; border-radius: 8px; background: #0a0e18; padding: 16px 20px; }
      `}</style>

      {/* ── Header ── */}
      <div style={{
        borderBottom: "1px solid #ffffff10",
        padding: "0 32px",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        height: 52,
        background: "#060810",
        position: "sticky",
        top: 0,
        zIndex: 50,
      }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
          <div style={{ width: 7, height: 7, borderRadius: "50%", background: "#34d399" }} className="pulse" />
          <span style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 900, fontSize: 13, letterSpacing: "0.05em" }}>
            IZA OS
          </span>
          <span style={{ color: "#ffffff25", fontSize: 11 }}>/ Venture Portfolio Hub</span>
        </div>

        {/* Global stats strip */}
        <div style={{ display: "flex", gap: 24, alignItems: "center" }}>
          {[
            { label: "ventures", value: PORTFOLIO_STATS.totalVentures },
            { label: "repos", value: `${PORTFOLIO_STATS.totalRepos}+` },
            { label: "sectors", value: SECTORS.length },
            { label: "projected/mo", value: `$${(PORTFOLIO_STATS.totalProjectedRevenue / 1000).toFixed(0)}k` },
          ].map(s => (
            <div key={s.label} style={{ textAlign: "right" }}>
              <div style={{ fontSize: 14, fontWeight: 500, color: "#e2e8f0", fontFamily: "'Epilogue', sans-serif" }}>{s.value}</div>
              <div style={{ fontSize: 9, color: "#ffffff30", textTransform: "uppercase", letterSpacing: "0.1em" }}>{s.label}</div>
            </div>
          ))}
        </div>

        <div style={{ display: "flex" }}>
          {TABS.map(t => (
            <button key={t.id} className={`tab ${view === t.id ? "active" : ""}`} onClick={() => setView(t.id)}>
              {t.label}
            </button>
          ))}
        </div>
      </div>

      {/* ══════════════════════════════════════════════════════════
          PORTFOLIO VIEW
      ══════════════════════════════════════════════════════════ */}
      {view === "portfolio" && (
        <div style={{ padding: "32px", maxWidth: 1100, margin: "0 auto" }} className="fade-up">
          <div style={{ marginBottom: 24, display: "flex", alignItems: "flex-start", justifyContent: "space-between", gap: 20 }}>
            <div>
              <h2 style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 900, fontSize: 22, marginBottom: 4 }}>
                Venture Portfolio
              </h2>
              <p style={{ fontSize: 11, color: "#64748b" }}>
                Worldwidebro GitHub Org · {PORTFOLIO_STATS.totalRepos}+ repositories · {PORTFOLIO_STATS.totalVentures} ventures tracked
              </p>
            </div>

            {/* Filters */}
            <div style={{ display: "flex", gap: 24, alignItems: "flex-start" }}>
              <div>
                <div style={{ fontSize: 9, color: "#ffffff25", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: 6 }}>Sector</div>
                <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
                  <button className={`filter-btn ${sectorFilter === "all" ? "active" : ""}`} onClick={() => setSectorFilter("all")}>All</button>
                  {SECTORS.map(s => (
                    <button
                      key={s.sectorId}
                      className={`filter-btn ${sectorFilter === s.sectorId ? "active" : ""}`}
                      onClick={() => setSectorFilter(s.sectorId)}
                      style={sectorFilter === s.sectorId ? { borderColor: s.color + "60", color: s.color } : {}}
                    >
                      {s.name.split(" ")[0]}
                    </button>
                  ))}
                </div>
              </div>
              <div>
                <div style={{ fontSize: 9, color: "#ffffff25", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: 6 }}>Status</div>
                <div style={{ display: "flex", gap: 6 }}>
                  {["all", "mvp", "validation"].map(s => (
                    <button
                      key={s}
                      className={`filter-btn ${statusFilter === s ? "active" : ""}`}
                      onClick={() => setStatusFilter(s)}
                      style={statusFilter === s && s !== "all" ? { borderColor: STATUS_META[s]?.color + "60", color: STATUS_META[s]?.color } : {}}
                    >
                      {s === "all" ? "All" : STATUS_META[s]?.label || s}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* Summary bar */}
          <div style={{
            display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 12, marginBottom: 24,
          }}>
            {[
              { label: "Showing", value: filtered.length, sub: "ventures" },
              { label: "Projected", value: fmt(totalRevenue), sub: "per month" },
              { label: "Avg completion", value: `${Math.round(filtered.reduce((s, v) => s + v.completionPercent, 0) / (filtered.length || 1))}%`, sub: "build progress" },
              { label: "Total agents", value: filtered.reduce((s, v) => s + v.agentsAssigned.length, 0), sub: "assigned" },
            ].map((s, i) => (
              <div key={i} className="stat-card">
                <div style={{ fontSize: 9, color: "#ffffff25", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: 4 }}>{s.label}</div>
                <div style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 900, fontSize: 22, color: "#e2e8f0" }}>{s.value}</div>
                <div style={{ fontSize: 10, color: "#64748b" }}>{s.sub}</div>
              </div>
            ))}
          </div>

          {/* Venture cards */}
          <div style={{ border: "1px solid #ffffff10", borderRadius: 10, overflow: "hidden" }}>
            {filtered.length === 0 && (
              <div style={{ padding: "32px", textAlign: "center", color: "#ffffff25", fontSize: 12 }}>
                No ventures match the current filters.
              </div>
            )}
            {filtered.map((v, i) => {
              const sector = SECTOR_META[v.sector] || { color: "#94a3b8", label: v.sector };
              const status = STATUS_META[v.status] || { color: "#94a3b8", bg: "#94a3b815", label: v.status };
              const priority = PRIORITY_META[v.priority] || { color: "#94a3b8", bg: "#94a3b815" };
              const isExpanded = expanded === v.ventureId;

              return (
                <div key={v.ventureId} className="venture-card" style={{ animationDelay: `${i * 0.04}s` }}>
                  {/* Main row */}
                  <div
                    style={{
                      padding: "16px 20px",
                      display: "grid",
                      gridTemplateColumns: "3px 1fr auto",
                      gap: 16,
                      alignItems: "start",
                      cursor: "pointer",
                    }}
                    onClick={() => setExpanded(isExpanded ? null : v.ventureId)}
                  >
                    {/* Sector accent bar */}
                    <div style={{ width: 3, height: "100%", minHeight: 40, background: sector.color, borderRadius: 2, alignSelf: "stretch" }} />

                    <div>
                      {/* Top line */}
                      <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 8, flexWrap: "wrap" }}>
                        <span style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 700, fontSize: 14, color: "#e2e8f0" }}>
                          {v.name}
                        </span>
                        <span style={{ fontSize: 10, color: "#ffffff25" }}>{v.ventureId}</span>
                        <span style={{
                          fontSize: 9, padding: "2px 8px", borderRadius: 3,
                          background: status.bg, color: status.color,
                          border: `1px solid ${status.color}30`, fontWeight: 700, letterSpacing: "0.06em",
                        }}>{status.label}</span>
                        <span style={{
                          fontSize: 9, padding: "2px 8px", borderRadius: 3,
                          background: priority.bg, color: priority.color,
                          border: `1px solid ${priority.color}30`, fontWeight: 700, letterSpacing: "0.06em",
                        }}>{v.priority}</span>
                        <span style={{ fontSize: 9, padding: "2px 8px", borderRadius: 3, background: sector.color + "15", color: sector.color, border: `1px solid ${sector.color}30` }}>
                          {sector.label}
                        </span>
                      </div>

                      {/* Metrics */}
                      <div style={{ display: "flex", gap: 20, flexWrap: "wrap" }}>
                        <div style={{ fontSize: 11, color: "#94a3b8" }}>
                          <span style={{ color: "#10b981", fontWeight: 500 }}>{fmt(v.revenueProjection)}/mo</span>
                          <span style={{ color: "#ffffff20" }}> projected</span>
                        </div>
                        <div style={{ fontSize: 11, color: "#94a3b8" }}>
                          <span style={{ color: "#60a5fa", fontWeight: 500 }}>{v.completionPercent}%</span>
                          <span style={{ color: "#ffffff20" }}> complete</span>
                        </div>
                        <div style={{ fontSize: 11, color: "#94a3b8" }}>
                          <span style={{ color: "#fbbf24", fontWeight: 500 }}>{v.agentsAssigned.length}</span>
                          <span style={{ color: "#ffffff20" }}> agents</span>
                        </div>
                        <div style={{ fontSize: 11, color: "#94a3b8" }}>
                          <span style={{ color: "#f87171" }}>{fmt(v.monthlyCostEstimate)}/mo</span>
                          <span style={{ color: "#ffffff20" }}> cost</span>
                        </div>
                      </div>

                      {/* Progress bar */}
                      <div style={{ marginTop: 10, height: 3, background: "#ffffff08", borderRadius: 2, width: "100%", maxWidth: 300 }}>
                        <div style={{
                          height: "100%", borderRadius: 2,
                          width: `${v.completionPercent}%`,
                          background: v.completionPercent >= 90 ? "#10b981" : v.completionPercent >= 60 ? "#60a5fa" : "#fbbf24",
                        }} />
                      </div>
                    </div>

                    {/* Right: chevron */}
                    <div style={{ color: "#ffffff20", fontSize: 12, paddingTop: 4, transition: "transform 0.2s", transform: isExpanded ? "rotate(90deg)" : "rotate(0deg)" }}>
                      ›
                    </div>
                  </div>

                  {/* Expanded detail */}
                  {isExpanded && (
                    <div style={{
                      padding: "0 20px 20px 39px",
                      display: "grid",
                      gridTemplateColumns: "1fr 1fr 1fr",
                      gap: 20,
                      borderTop: "1px solid #ffffff08",
                      paddingTop: 16,
                    }} className="fade-up">
                      <div>
                        <div style={{ fontSize: 9, color: "#ffffff25", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: 8 }}>Agents</div>
                        <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
                          {v.agentsAssigned.map(a => (
                            <span key={a} style={{
                              fontSize: 10, padding: "3px 8px", borderRadius: 4,
                              background: "#8b5cf615", border: "1px solid #8b5cf630", color: "#a78bfa",
                            }}>{a}</span>
                          ))}
                        </div>
                      </div>
                      <div>
                        <div style={{ fontSize: 9, color: "#ffffff25", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: 8 }}>Infrastructure</div>
                        <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
                          {v.infrastructure.map(t => (
                            <span key={t} style={{
                              fontSize: 10, padding: "3px 8px", borderRadius: 4,
                              background: "#ffffff08", border: "1px solid #ffffff15", color: "#94a3b8",
                            }}>{t}</span>
                          ))}
                        </div>
                      </div>
                      <div>
                        <div style={{ fontSize: 9, color: "#ffffff25", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: 8 }}>Next action</div>
                        <div style={{ fontSize: 11, color: "#fbbf24", lineHeight: 1.5 }}>{v.nextAction}</div>
                        {v.githubRepo && (
                          <a
                            href={v.githubRepo}
                            target="_blank"
                            rel="noopener noreferrer"
                            style={{
                              display: "inline-flex", alignItems: "center", gap: 5,
                              marginTop: 10, fontSize: 10, color: "#60a5fa",
                              textDecoration: "none", border: "1px solid #60a5fa30",
                              background: "#60a5fa08", padding: "4px 10px", borderRadius: 4,
                            }}
                            onClick={e => e.stopPropagation()}
                          >
                            ↗ GitHub
                          </a>
                        )}
                        {v.dashboardPort && (
                          <div style={{ marginTop: 6, fontSize: 10, color: "#94a3b8" }}>
                            Dashboard: <span style={{ color: "#34d399" }}>:{v.dashboardPort}</span>
                          </div>
                        )}
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>

          <div style={{ marginTop: 14, fontSize: 10, color: "#ffffff20", textAlign: "center" }}>
            Showing {filtered.length} seeded ventures · {PORTFOLIO_STATS.totalVentures} total tracked in registry
          </div>
        </div>
      )}

      {/* ══════════════════════════════════════════════════════════
          SECTORS VIEW
      ══════════════════════════════════════════════════════════ */}
      {view === "sectors" && (
        <div style={{ padding: "32px", maxWidth: 1000, margin: "0 auto" }} className="fade-up">
          <h2 style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 900, fontSize: 22, marginBottom: 4 }}>Sectors</h2>
          <p style={{ fontSize: 11, color: "#64748b", marginBottom: 28 }}>Portfolio organized by industry vertical</p>

          <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
            {SECTORS.map((sector, i) => {
              const sectorVentures = VENTURES.filter(v => v.sector === sector.sectorId);
              const totalRev = sectorVentures.reduce((s, v) => s + v.revenueProjection, 0);
              const avgCompletion = Math.round(sectorVentures.reduce((s, v) => s + v.completionPercent, 0) / (sectorVentures.length || 1));

              return (
                <div key={sector.sectorId} style={{
                  border: `1px solid ${sector.color}30`,
                  borderRadius: 12,
                  background: sector.color + "06",
                  overflow: "hidden",
                  animationDelay: `${i * 0.08}s`,
                }}>
                  {/* Sector header */}
                  <div style={{
                    padding: "18px 24px",
                    borderBottom: `1px solid ${sector.color}20`,
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "space-between",
                    background: sector.color + "08",
                  }}>
                    <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
                      <div style={{ width: 4, height: 28, background: sector.color, borderRadius: 2 }} />
                      <div>
                        <div style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 900, fontSize: 18, color: sector.color }}>{sector.name}</div>
                        <div style={{ fontSize: 11, color: "#64748b", marginTop: 2 }}>{sector.description}</div>
                      </div>
                    </div>
                    <div style={{ display: "flex", gap: 28, textAlign: "right" }}>
                      <div>
                        <div style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 900, fontSize: 24, color: "#e2e8f0" }}>{sector.ventureCount}</div>
                        <div style={{ fontSize: 9, color: "#ffffff25", textTransform: "uppercase", letterSpacing: "0.1em" }}>ventures</div>
                      </div>
                      <div>
                        <div style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 900, fontSize: 24, color: "#e2e8f0" }}>{sector.repoCount}</div>
                        <div style={{ fontSize: 9, color: "#ffffff25", textTransform: "uppercase", letterSpacing: "0.1em" }}>repos</div>
                      </div>
                      {sectorVentures.length > 0 && (
                        <>
                          <div>
                            <div style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 900, fontSize: 24, color: "#10b981" }}>{fmt(totalRev)}</div>
                            <div style={{ fontSize: 9, color: "#ffffff25", textTransform: "uppercase", letterSpacing: "0.1em" }}>proj/mo</div>
                          </div>
                          <div>
                            <div style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 900, fontSize: 24, color: "#60a5fa" }}>{avgCompletion}%</div>
                            <div style={{ fontSize: 9, color: "#ffffff25", textTransform: "uppercase", letterSpacing: "0.1em" }}>avg done</div>
                          </div>
                        </>
                      )}
                    </div>
                  </div>

                  {/* Seeded ventures in this sector */}
                  {sectorVentures.length > 0 && (
                    <div style={{ padding: "16px 24px", display: "flex", gap: 10, flexWrap: "wrap" }}>
                      {sectorVentures.map(v => (
                        <div key={v.ventureId} style={{
                          padding: "10px 14px",
                          borderRadius: 8,
                          border: `1px solid ${sector.color}25`,
                          background: sector.color + "0a",
                          minWidth: 160,
                        }}>
                          <div style={{ fontSize: 12, fontWeight: 500, color: "#e2e8f0", marginBottom: 4 }}>{v.name}</div>
                          <div style={{ fontSize: 10, color: "#64748b", marginBottom: 6 }}>{v.ventureId}</div>
                          <div style={{ height: 2, background: "#ffffff08", borderRadius: 1 }}>
                            <div style={{
                              height: "100%", borderRadius: 1,
                              width: `${v.completionPercent}%`,
                              background: sector.color,
                            }} />
                          </div>
                          <div style={{ marginTop: 4, fontSize: 10, color: sector.color }}>{v.completionPercent}% · {fmt(v.revenueProjection)}/mo</div>
                        </div>
                      ))}

                      {sector.ventureCount > sectorVentures.length && (
                        <div style={{
                          padding: "10px 14px", borderRadius: 8,
                          border: `1px dashed ${sector.color}20`,
                          background: "transparent",
                          minWidth: 160, display: "flex", alignItems: "center", justifyContent: "center",
                          color: "#ffffff25", fontSize: 11,
                        }}>
                          +{sector.ventureCount - sectorVentures.length} more in registry
                        </div>
                      )}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* ══════════════════════════════════════════════════════════
          ARCHITECTURE VIEW
      ══════════════════════════════════════════════════════════ */}
      {view === "architecture" && (
        <div style={{ padding: "32px", display: "grid", gridTemplateColumns: "1fr 280px", gap: 24, maxWidth: 1200, margin: "0 auto" }} className="fade-up">
          <div>
            <div style={{ marginBottom: 20, display: "flex", alignItems: "center", justifyContent: "space-between" }}>
              <div>
                <h2 style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 900, fontSize: 20, marginBottom: 4 }}>Infrastructure Layers</h2>
                <p style={{ fontSize: 11, color: "#64748b" }}>Click any node to highlight its data flows →</p>
              </div>
              {activeNode && (
                <button onClick={() => setActiveNode(null)} style={{
                  background: "#ffffff10", border: "1px solid #ffffff20",
                  color: "#e2e8f0", padding: "5px 12px", borderRadius: 4,
                  cursor: "pointer", fontSize: 11, fontFamily: "'IBM Plex Mono', monospace",
                }}>
                  Clear ✕
                </button>
              )}
            </div>

            <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
              {LAYERS.map((layer, li) => (
                <div
                  key={layer.id}
                  className="layer-card"
                  style={{
                    border: `1px solid ${activeLayer === layer.id ? layer.color + "70" : layer.border}`,
                    borderRadius: 10,
                    background: activeLayer === layer.id ? layer.bg + "dd" : layer.bg + "88",
                    overflow: "hidden",
                    animationDelay: `${li * 0.06}s`,
                  }}
                  onClick={() => setActiveLayer(activeLayer === layer.id ? null : layer.id)}
                >
                  <div style={{
                    padding: "10px 16px", borderBottom: `1px solid ${layer.border}`,
                    display: "flex", alignItems: "center", justifyContent: "space-between",
                  }}>
                    <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                      <div style={{ width: 3, height: 16, background: layer.color, borderRadius: 2 }} />
                      <span style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 700, fontSize: 12, color: layer.color }}>{layer.label}</span>
                    </div>
                    <span style={{ fontSize: 10, color: "#ffffff30", fontStyle: "italic" }}>{layer.sublabel}</span>
                  </div>

                  <div style={{ padding: "12px 16px", display: "flex", gap: 8, flexWrap: "wrap" }}>
                    {layer.nodes.map(node => {
                      const isV2 = V2_NODES.includes(node.id);
                      const isActive = activeNode === node.id;
                      const isHighlighted = activeNode && highlightedFlows.some(f => f.from === node.id || f.to === node.id);
                      return (
                        <div
                          key={node.id}
                          className="pill"
                          onClick={e => { e.stopPropagation(); setActiveNode(isActive ? null : node.id); }}
                          style={{
                            padding: "8px 14px", borderRadius: 6,
                            border: `1px solid ${isActive ? layer.color : isHighlighted ? layer.color + "60" : "#ffffff15"}`,
                            background: isActive ? layer.color + "25" : isHighlighted ? layer.color + "10" : "#ffffff05",
                            opacity: activeNode && !isActive && !isHighlighted ? 0.35 : 1,
                            position: "relative",
                          }}
                        >
                          {isV2 && (
                            <div style={{
                              position: "absolute", top: -6, right: -6,
                              background: "#fbbf24", color: "#000", fontSize: 8,
                              padding: "1px 5px", borderRadius: 3, fontWeight: 700,
                            }}>V2</div>
                          )}
                          <div style={{ fontSize: 12, fontWeight: 500, color: isActive ? layer.color : "#e2e8f0", marginBottom: 2 }}>{node.label}</div>
                          <div style={{ fontSize: 10, color: "#64748b" }}>{node.sub}</div>
                        </div>
                      );
                    })}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Sidebar */}
          <div>
            {activeNode && (
              <div style={{ border: "1px solid #ffffff15", borderRadius: 10, background: "#0f1520", overflow: "hidden", marginBottom: 16 }}>
                <div style={{ padding: "12px 16px", borderBottom: "1px solid #ffffff10", background: "#ffffff05" }}>
                  <div style={{ fontSize: 11, color: "#64748b", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: 4 }}>Active flows for</div>
                  <div style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 700, fontSize: 14 }}>{activeNode}</div>
                </div>
                <div style={{ padding: "12px 16px", display: "flex", flexDirection: "column", gap: 8 }}>
                  {highlightedFlows.filter(f => f.from === activeNode || f.to === activeNode).map((f, i) => (
                    <div key={i} style={{ fontSize: 11 }}>
                      <div style={{ display: "flex", alignItems: "center", gap: 6, color: f.color, marginBottom: 2 }}>
                        <div style={{ width: 6, height: 6, borderRadius: "50%", background: f.color }} />
                        {f.label}
                      </div>
                      <div style={{ color: "#64748b", paddingLeft: 12 }}>
                        {f.from === activeNode ? `→ ${f.to}` : `← ${f.from}`}
                      </div>
                    </div>
                  ))}
                  {highlightedFlows.filter(f => f.from === activeNode || f.to === activeNode).length === 0 && (
                    <div style={{ fontSize: 11, color: "#ffffff25" }}>No direct flows</div>
                  )}
                </div>
              </div>
            )}

            <div style={{ border: "1px solid #ffffff10", borderRadius: 10, background: "#0a0e18", overflow: "hidden", marginBottom: 16 }}>
              <div style={{ padding: "10px 16px", borderBottom: "1px solid #ffffff08" }}>
                <span style={{ fontSize: 10, color: "#ffffff30", textTransform: "uppercase", letterSpacing: "0.12em" }}>Flow Types</span>
              </div>
              <div style={{ padding: "12px 16px", display: "flex", flexDirection: "column", gap: 8 }}>
                {FLOW_TYPE_LEGEND.map(fl => (
                  <div key={fl.type} style={{ display: "flex", alignItems: "center", gap: 8 }}>
                    <div style={{ width: 20, height: 2, background: fl.color, borderRadius: 1 }} />
                    <span style={{ fontSize: 11, color: "#94a3b8" }}>{fl.label}</span>
                  </div>
                ))}
              </div>
            </div>

            <div style={{ border: "1px solid #fbbf2430", borderRadius: 10, background: "#fbbf2408", padding: "14px 16px" }}>
              <div style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 700, color: "#fbbf24", fontSize: 12, marginBottom: 8 }}>V2 nodes</div>
              <p style={{ fontSize: 11, color: "#94a3b8", lineHeight: 1.7 }}>
                Redis and ChromaDB are marked V2 — only needed when you add persistent chat history or RAG to the site itself. Your existing Iza OS platform already has them; it's just a matter of exposing them via Kong.
              </p>
            </div>
          </div>
        </div>
      )}

      {/* ══════════════════════════════════════════════════════════
          DB DECISION VIEW
      ══════════════════════════════════════════════════════════ */}
      {view === "db" && (
        <div style={{ padding: "32px", maxWidth: 860, margin: "0 auto" }} className="fade-up">
          <h2 style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 900, fontSize: 20, marginBottom: 4 }}>DB Decision Tree</h2>
          <p style={{ fontSize: 11, color: "#64748b", marginBottom: 32 }}>When do you actually need a new database?</p>

          {[
            { feature: "Marketing pages, blog, case studies", need: "Sanity CMS", db: false, color: "#34d399", launch: "V1", reason: "Managed document store — no tables, no migrations" },
            { feature: "Contact / scoping form submissions", need: "Resend → ClickUp webhook", db: false, color: "#34d399", launch: "V1", reason: "Stateless pipeline — email + task creation only" },
            { feature: "Discovery call booking", need: "Calendly embed", db: false, color: "#34d399", launch: "V1", reason: "Calendly owns its own data — zero storage on your side" },
            { feature: "Site analytics + session replay", need: "PostHog (managed)", db: false, color: "#34d399", launch: "V1", reason: "PostHog stores its own ClickHouse internally" },
            { feature: "User auth (client portal)", need: "Clerk", db: false, color: "#34d399", launch: "V1", reason: "Clerk manages sessions — JWT passed to your API" },
            { feature: "Client portal — project status", need: "Existing Iza OS Postgres via Kong", db: false, color: "#fbbf24", launch: "V1", reason: "Read-only API call to your existing DB — no new instance" },
            { feature: "ROI calculator — saved results", need: "Supabase (new)", db: true, color: "#f87171", launch: "V2", reason: "First feature that requires persisting user-generated data" },
            { feature: "Chat widget — conversation history", need: "Redis (existing Iza OS)", db: true, color: "#f87171", launch: "V2", reason: "Expose existing Redis via Kong — no new DB, new endpoint only" },
            { feature: "Scoping AI — RAG on your repo knowledge", need: "ChromaDB (existing Iza OS)", db: true, color: "#f87171", launch: "V2", reason: "Expose existing ChromaDB via Kong — your 539-repo KB already loaded" },
            { feature: "Referral / affiliate tracking", need: "Supabase (new) or existing Postgres", db: true, color: "#f87171", launch: "V2", reason: "Needs new tables — add to existing Postgres or separate Supabase project" },
          ].map((item, i) => (
            <div key={i} style={{ display: "grid", gridTemplateColumns: "14px 1fr", gap: 0, marginBottom: 4 }}>
              <div style={{ display: "flex", flexDirection: "column", alignItems: "center", paddingTop: 18 }}>
                <div style={{ width: 8, height: 8, borderRadius: "50%", background: item.color, flexShrink: 0 }} />
                {i < 9 && <div style={{ width: 1, flex: 1, background: "#ffffff10", minHeight: 8 }} />}
              </div>
              <div style={{
                marginLeft: 14, padding: "14px 18px",
                border: `1px solid ${item.db ? item.color + "30" : "#ffffff10"}`,
                borderRadius: 8,
                background: item.db ? item.color + "08" : "#ffffff04",
                marginBottom: 8,
              }}>
                <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between", marginBottom: 8, gap: 12 }}>
                  <div style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 700, fontSize: 13, color: "#e2e8f0" }}>{item.feature}</div>
                  <div style={{ display: "flex", gap: 6, flexShrink: 0 }}>
                    <span style={{
                      fontSize: 9, padding: "2px 7px", borderRadius: 3,
                      background: item.launch === "V1" ? "#34d39920" : "#f8717120",
                      border: `1px solid ${item.launch === "V1" ? "#34d39940" : "#f8717140"}`,
                      color: item.launch === "V1" ? "#34d399" : "#f87171",
                      fontWeight: 700, letterSpacing: "0.08em",
                    }}>{item.launch}</span>
                    <span style={{
                      fontSize: 9, padding: "2px 7px", borderRadius: 3,
                      background: item.db ? "#f8717115" : "#34d39915",
                      border: `1px solid ${item.db ? "#f8717135" : "#34d39935"}`,
                      color: item.db ? "#f87171" : "#34d399",
                      fontWeight: 700,
                    }}>{item.db ? "NEW DB" : "NO DB"}</span>
                  </div>
                </div>
                <div style={{ display: "flex", gap: 20, flexWrap: "wrap" }}>
                  <div>
                    <div style={{ fontSize: 9, color: "#ffffff25", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: 3 }}>Solution</div>
                    <div style={{ fontSize: 12, color: item.color }}>{item.need}</div>
                  </div>
                  <div style={{ flex: 1 }}>
                    <div style={{ fontSize: 9, color: "#ffffff25", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: 3 }}>Why</div>
                    <div style={{ fontSize: 11, color: "#64748b", lineHeight: 1.6 }}>{item.reason}</div>
                  </div>
                </div>
              </div>
            </div>
          ))}

          <div style={{
            marginTop: 24, padding: "20px 24px",
            border: "1px solid #34d39930", borderRadius: 10, background: "#34d39908",
            display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 20,
          }}>
            {[
              { label: "V1 — no new DB", value: "6 features", color: "#34d399", sub: "Ship immediately" },
              { label: "V2 — expose existing", value: "2 endpoints", color: "#fbbf24", sub: "Kong config only" },
              { label: "V2 — new DB needed", value: "1 Supabase project", color: "#f87171", sub: "ROI calc + referrals" },
            ].map((s, i) => (
              <div key={i}>
                <div style={{ fontSize: 10, color: "#ffffff30", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: 4 }}>{s.label}</div>
                <div style={{ fontFamily: "'Epilogue', sans-serif", fontWeight: 900, fontSize: 16, color: s.color, marginBottom: 2 }}>{s.value}</div>
                <div style={{ fontSize: 11, color: "#64748b" }}>{s.sub}</div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
