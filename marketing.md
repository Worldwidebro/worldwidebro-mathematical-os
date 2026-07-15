# Marketing Skills & Agents Map

Source list: [marketingtoolslist/awesome-marketing](https://github.com/marketingtoolslist/awesome-marketing) — 12 tool categories.
This maps each category to the skills (`/slash-commands`) and agents already available in this Claude Code environment, so ventures can execute the same functions without external SaaS tools.

---

## 1. Marketing Strategy & Planning
*(segmentation, campaign planning, budgeting, competitor/market analysis, marketing mix modeling)*

- **Agents:** Business Strategist, Trend Researcher, Growth Hacker, Pricing Analyst
- **Skills:** `competitor-analysis`, `competitor-tracking`, `competitor-alternatives`, `competitor-profiling`, `market-sizing`, `market-sizing-analysis`, `swot-analysis`, `porters-five-forces`, `ansoff-matrix`, `pestle-analysis`, `pricing-strategy`, `pricing`, `lean-canvas`, `osterwalder-canvas-architect`, `startup-business-analyst:market-opportunity`, `startup-business-analyst:competitive-landscape`

## 2. SEO
- **Agents:** SEO Specialist, Baidu SEO Specialist (China market)
- **Skills:** `seo`, `seo-fundamentals`, `seo-technical`, `seo-audit`, `seo-content-planner`, `seo-content-writer`, `seo-content-auditor`, `seo-keyword-strategist`, `seo-meta-optimizer`, `seo-schema`, `seo-sitemap`, `seo-snippet-hunter`, `seo-structure-architect`, `seo-cannibalization-detector`, `seo-authority-builder`, `seo-content-refresher`, `seo-programmatic`, `seo-hreflang`, `seo-forensic-incident-response`, `schema-markup`, `schema-markup-generator`, `pagespeed-enhancer`, `everything-claude-code:seo`
- **Adjacent (AI-search era):** `ai-seo`, `seo-aeo-*` skills (blog writer, content cluster, keyword research, internal linking, landing page writer, meta description, schema, quality auditor) — for optimizing against ChatGPT/Perplexity/AI Overviews, not just Google

## 3. Social Media Marketing
- **Agents:** Social Media Strategist, TikTok Strategist, Instagram Curator, LinkedIn Content Creator, Twitter/X Intelligence Analyst, Reddit Community Builder, Douyin Strategist, Xiaohongshu Specialist, Weibo Strategist, Bilibili Content Strategist, Kuaishou Strategist
- **Skills:** `social-content`, `social-orchestrator`, `social-post-writer-seo`, `linkedin-automation`, `linkedin-content-generator`, `linkedin-post-writer`, `twitter-automation`, `instagram-automation`, `tiktok-automation`, `reddit-automation`, `youtube-automation`, `discord-automation`, `telegram-automation`, `taisly-social-media-posting`, `social-publishing:social-publishing`, `canva-automation`, `buffer` MCP

## 4. Content Marketing
- **Agents:** Content Creator, Technical Writer, Book Co-Author
- **Skills:** `content-marketer`, `content-engine`, `content-strategy`, `content-creator`, `article-writing`, `copywriting`, `copywriting-psychologist`, `brand-voice`, `avoid-ai-writing`, `beautiful-prose`, `blog-writing-guide`, `wordpress-centric-high-seo-optimized-blogwriting-skill`, `landing-page-generator`, `remotion-video-creation`, `manim-video`, `video-editing`

## 5. Email Marketing
- **Agents:** Email Marketing Strategist
- **Skills:** `activecampaign-automation`, `mailchimp-automation`, `klaviyo-automation`, `convertkit-automation`, `sendgrid-automation`, `postmark-automation`, `brevo-automation`, `mailtrap-sending-emails`, `mailtrap-managing-contacts`, `email-sequence`, `email-systems`, `subject-line-psychologist`

## 6. Marketing Automation
*(lead nurturing, workflow automation, customer journey mapping)*

- **Agents:** Growth Hacker
- **Skills:** `n8n-workflow-patterns`, `n8n-code-javascript`, `n8n-code-python`, `n8n-node-configuration`, `n8n-expression-syntax`, `zapier-make-patterns`, `make-automation`, `workflow-automation`, `workflow-orchestration-patterns`, `customer-journey-map`, `onboarding-psychologist`, `activecampaign-automation`, `hubspot-automation`

## 7. Search Engine Marketing (SEM) — PPC, Display, Retargeting
- **Agents:** PPC Campaign Strategist, Paid Media Auditor, Paid Social Strategist, Programmatic & Display Buyer, Search Query Analyst, Tracking & Measurement Specialist, Ad Creative Strategist
- **Skills:** `paid-ads`, `ad-creative`

## 8. Analytics & Reporting
*(web analytics, CRO, dashboards)*

- **Agents:** Analytics Reporter, Financial Analyst (for revenue-side reporting)
- **Skills:** `google-analytics-automation`, `segment-automation`, `segment-cdp`, `mixpanel-automation`, `amplitude-automation`, `posthog-automation`, `datadog-automation`, `grafana-dashboards`, `metrics-dashboard`, `kpi-dashboard-design`, `dataviz`, `ab-testing`, `ab-test-setup`, `ab-test-analysis`, `cohort-analysis`, `north-star-metric`, `analytics-tracking`, `analytics-product`

## 9. Customer Relationship Management (CRM)
- **Agents:** Customer Success Manager, Sales Coach, Deal Strategist, Account Strategist, Salesforce Architect
- **Skills/Live MCPs:** `hubspot-automation` / `hubspot-integration` (+ live `mcp__hubspot__*` and `mcp__claude_ai_HubSpot__*` tools already connected), `salesforce-automation`, `zoho-crm-automation`, `pipedrive-automation`, `close-automation`, `freshdesk-automation`, `zendesk-automation`, `intercom-automation`, `clickup-automation` (+ live `mcp__claude_ai_ClickUp__*`) — **note:** the ClickUp+Supabase CRM described in memory ([[crm-system-complete]]) is already live for this portfolio; wire new ventures into that rather than standing up a fresh CRM tool

## 10. Advertising & Media Buying
*(programmatic, affiliate, native)*

- **Agents:** Programmatic & Display Buyer, Ad Creative Strategist, Paid Social Strategist
- **Skills:** `referral-program`, `growth-loops`, `viral-generator-builder`, `paid-ads`

## 11. Market Research & Competitor Analysis
- **Agents:** Trend Researcher, Business Strategist, X/Twitter Intelligence Analyst
- **Skills:** `market-research`, `competitor-analysis`, `competitor-tracking`, `competitor-alternatives`, `competitor-profiling`, `survey-generator`, `customer-research`, `customer-psychographic-profiler`, `user-personas`, `user-segmentation`, `deep-research`, `exa-search`, `tavily-web`

## 12. Brand Management
*(reputation, monitoring, DAM)*

- **Agents:** Brand Guardian, PR & Communications Manager, Whimsy Injector, Visual Storyteller
- **Skills:** `brand-guidelines`, `brand-guidelines-anthropic`, `brand-guidelines-community`, `brand-perception-psychologist`, `theme-factory`, `taste-skill:brandkit`

---

## Execution pattern for any venture

1. **Research phase:** `market-research` skill / Trend Researcher agent → `competitor-analysis` → `customer-research`
2. **Strategy phase:** Business Strategist agent → `pricing-strategy` → `lean-canvas`
3. **Content phase:** Content Creator agent + platform-specific strategist (TikTok/Instagram/LinkedIn/etc.) → `content-engine` for bulk generation
4. **Distribution phase:** `social-publishing:social-publishing` or platform `*-automation` skills → `crosspost`
5. **Paid phase (if funded):** PPC Campaign Strategist / Paid Social Strategist agents
6. **Measurement phase:** `google-analytics-automation` → `kpi-dashboard-design` → `dataviz` → report into existing Grafana/DuckDB stack (see CLAUDE.md Data Layer section — don't stand up a new analytics tool, wire into what's already running)

Per-venture use `/orchestrate` to run research → strategy → content skills in parallel, and log outputs to Supabase `skill_executions` table per the existing Skill Execution Framework in CLAUDE.md.
