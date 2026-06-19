# Iza OS Hub — Project Instructions

## Project Overview
This is the **Iza OS Hub** — a React 18 + Vite dashboard for managing a portfolio of 40+ AI-powered business ventures across multiple sectors. The dashboard visualizes venture status, architecture data flows, and infrastructure state.

**GitHub org:** `Worldwidebro` | **550+ repos total** | **Target revenue: $76k/mo**

## Tech Stack
- **Frontend:** React 18, Vite 5, JSX (no TypeScript)
- **Component:** Single component at `components/IzaOSDataFlow.jsx` (the main hub)
- **Entry:** `src/main.jsx` → renders `IzaOSHub`
- **Dev server:** `npm run dev` → port 5173

## Venture Portfolio
40 ventures across 3 sectors:
- **Financial Services** (35 ventures): Tax prep, crypto tax, banking, financial automation
- **E-Commerce & Arbitrage** (4 ventures): Price arbitrage, product sourcing
- **Construction** (1 venture): Ace Construction

Most ventures are at **MVP** stage. The **#1 blocker** across critical ventures is **Stripe integration**.

## Infrastructure Per Venture
Most ventures use: `postgres + stripe + docker`
Common agents assigned per venture: task-specific AI agents (e.g. `tax_parser_agent`, `filing_agent`)

## Full Architecture Stack (Iza OS Platform)
- **Frontend:** Next.js 14 (App Router, SSR, Edge), deployed on Vercel
- **Auth:** Clerk (session tokens + JWT)
- **CMS:** Sanity CMS (GROQ API, case studies, blog)
- **Email:** Resend
- **Scheduling:** Calendly
- **AI:** Claude Haiku (chat widget), Claude Sonnet (scoping form analysis)
- **CRM:** ClickUp (lead pipeline), Notion (client briefs), Slack (alerts)
- **Platform:** PostgreSQL, Redis (chat sessions), ChromaDB (RAG), Kong API Gateway
- **Analytics:** PostHog, Vercel Analytics

## MCP Servers Connected
ClickUp, Gmail, Google Calendar, Google Drive, Slack, Notion, Supabase, Vercel, Hugging Face

## Key Priorities
1. Add Stripe integration to critical financial ventures (FIN-001, FIN-006, FIN-009, FIN-021, FIN-033)
2. Build dashboards for ventures missing them
3. Wire Ace Construction contact intake

## Conventions
- React functional components, hooks (`useState`, etc.)
- No TypeScript — pure JSX
- Inline styles and CSS-in-JS patterns (no Tailwind)
- Dark theme UI (`#1a1a2e` base, sector-specific accent colors)
- Color system: financial=#10b981, e-commerce=#8b5cf6, construction=#f59e0b
- Status: mvp=#10b981, validation=#fbbf24, production=#60a5fa

## Common Commands
```bash
npm run dev      # Start dev server (port 5173)
npm run build    # Production build
```

## Do Not
- Do not add TypeScript
- Do not add a CSS framework (Tailwind, etc.)
- Do not split the single component without discussion
- Do not commit secrets or `.env` files
