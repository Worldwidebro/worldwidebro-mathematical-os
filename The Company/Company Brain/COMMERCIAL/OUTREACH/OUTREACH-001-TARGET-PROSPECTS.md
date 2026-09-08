---
id: DOC-OUT-001
title: "COMMERCIAL OUTREACH — 5 Target Prospects & Battle-Tested Scripts"
aliases: ["COMMERCIAL/OUTREACH/OUTREACH-001-TARGET-PROSPECTS", "DOC-OUT-001", "Target Prospects Outreach"]
tags: ["commercial", "outreach", "sales", "revenue", "scripts"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[ECONOMIC-REALITY]] | [[COMMERCIAL/OFFERS/OFFER-001-LOCAL-AI-AUDIT|Local AI Audit Offer]] | [[23-VENTURES/23-VENTURES|23-VENTURES]]

# COMMERCIAL OUTREACH: 5 Target Prospects & Battle-Tested Scripts

> **Canonical Document ID:** `DOC-OUT-001`  
> **Linked Offer:** [[COMMERCIAL/OFFERS/OFFER-001-LOCAL-AI-AUDIT|OFR-AUDIT-001 (Local AI Audit)]]  
> **Campaign Goal:** 5 Discovery Conversations -> 1 Paid Audit ($7,500)  
> **Operating Law:** [[ECONOMIC-REALITY|ECONOMIC-REALITY.md]] Section 7: *Outreach must be direct, specific, and unashamed.*

---

## 1. Five Target Prospect Profiles (Targeting Strategy)

### Prospect 1: The Fast-Scaling AI Agent Startup (Series A)
- **Profile:** 15–40 engineers, building agentic developer tools or enterprise autonomous agents.
- **Pain Point:** OpenAI/Anthropic bills scaling non-linearly ($15k–$40k/mo). Agent loops eating tokens on raw error traces and file reads.
- **Target Title:** VP of Engineering / Head of Platform / Founder & CTO.

### Prospect 2: The B2B FinTech / HealthTech Engineering Org (Seed/Series A)
- **Profile:** 20–50 engineers, handling regulated data (SOC2, HIPAA, PCI).
- **Pain Point:** Developers want Claude Code / Cursor, but security compliance blocks cloud LLM usage for proprietary code and customer schemas.
- **Target Title:** VP of Information Security / CTO.

### Prospect 3: The High-Volume Dev Agency / Software Consultancy
- **Profile:** 30–80 developers building custom client applications across dozens of client repos.
- **Pain Point:** Substantial developer AI tool seat costs and inability to share contextual knowledge across client codebases.
- **Target Title:** Managing Partner / Chief Technology Officer.

### Prospect 4: The Monorepo SaaS Company (Series B)
- **Profile:** 50–120 engineers, massive monorepo (>500k LOC).
- **Pain Point:** Agent tools fail because they dump 100k+ tokens of context into context windows, blowing through rate limits and hallucinating dependencies.
- **Target Title:** Staff Platform Engineer / VP of Infrastructure.

### Prospect 5: The Bootstrapped Technical Founder Org ($1M–$5M ARR)
- **Profile:** 5–15 engineers, highly margin-sensitive.
- **Pain Point:** Need agentic coding speed without burning 10%–20% of net margin on cloud LLM inference bills.
- **Target Title:** Founder & CEO / Technical Co-founder.

---

## 2. High-Conversion Direct Outreach Scripts

### Channel A: Cold Email (Target: CTO / VP Engineering)

**Subject:** Quick question on your Claude / OpenAI API spend at {{Company}}

> Hey {{First_Name}},
>
> Noticed your engineering team has been scaling up agentic workflows with Claude and Cursor.
>
> Most technical teams your size (15–50 engineers) are hitting a brutal hidden tax right now: **$8k to $25k/mo in cloud token spend**, largely burned on repetitive build logs, terminal outputs, and bloated monorepo context dumps.
>
> We do a 48-hour diagnostic audit for engineering teams:
> 1. **Token Compression & Cascading Routing:** We benchmark how stacked compression (RTK/Caveman) drops token burn by 60%+ without loss of reasoning.
> 2. **Repo Knowledge Graphs:** We model your codebase into an AST graph (Neo4j) so agents only pull exact subgraphs instead of blind file scans.
> 3. **Local Mesh Strategy:** Sizing open-weights reasoning models (Qwen 2.5 Coder / DeepSeek R1) on existing local hardware for 100% private execution.
>
> We guarantee to uncover at least **3x the audit fee ($22,500)** in annualized compute savings, or the audit is 100% free.
>
> Open to seeing a 5-minute tear-down of how this works?
>
> Best,  
> {{Founder_Name}}  
> WorldwideBro AI Infrastructure

---

### Channel B: LinkedIn / X Direct Message (Founder-to-Founder)

> Hey {{First_Name}} — saw your recent update on {{Product_Feature / Launch}}.
>
> Quick observation: a lot of engineering founders I talk to are quietly getting murdered by their LLM token bills right now ($10k+/mo), mostly because agents are ingesting raw terminal traces and whole file dumps.
>
> We built a local-first model router and repo knowledge graph stack that cuts token waste by 60%+ and lets teams run sensitive codebase reasoning locally.
>
> Doing 3 fixed-fee 48-hour audits this month with a guaranteed 3x savings floor.
>
> Worth sending over a 1-page overview to see if it’s relevant for {{Company}}?

---

## 3. Objection Handling Playbook

### Objection 1: "We just use OpenAI / Anthropic directly, why bother with local or custom routing?"
> *"Totally makes sense for quick prototyping. But at your scale, 50% to 70% of tokens in agentic loops are repetitive terminal outputs, stack traces, and uncompressed diffs. That’s pure burned capital. Routing non-reasoning tasks and compressed contexts through a local gateway cuts those bills in half without changing your developers' daily workflow."*

### Objection 2: "We don't have dedicated GPUs or local servers."
> *"You don't need Nvidia clusters. If your developers or engineers are on Apple Silicon (M2/M3/M4 Max), you already have 64GB to 128GB of unified memory sitting idle. Our audit evaluates your existing hardware mesh and shows you how to run 32B code models locally via Tailscale before you spend a single dollar on new servers."*

### Objection 3: "Our security team won't give you code access."
> *"Our audit is designed specifically for high-compliance environments. We run entirely via sanitized local scripts or containerized tools on your internal sandbox, or provide a self-hosted runbook. Zero proprietary source code ever leaves your environment."*

---

## 4. Daily Execution Cadence

```yaml
daily_sales_rhythm:
  morning:
    action: "Identify 5 new CTO / VP Eng profiles on LinkedIn / GitHub"
    deliverable: "5 personalized cold emails / DMs dispatched"
  afternoon:
    action: "Follow up on all outstanding conversations (Day 2 / Day 4 cadence)"
    deliverable: "Zero unanswered inbound messages"
  metric_tracked:
    conversations_started: 5
    discovery_calls_booked: 1
    audits_closed: "$7,500"
```
