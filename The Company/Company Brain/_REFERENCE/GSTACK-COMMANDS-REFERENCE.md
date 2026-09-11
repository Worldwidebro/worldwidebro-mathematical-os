# Gstack Slash Commands Reference Guide

Quick navigation: **PLANNING** | **REVIEW** | **SHIPPING** | **BROWSER/QA** | **DEBUGGING** | **CONFIG** | **DOCS**

---

## PLANNING & STRATEGY

### `/office-hours`
**When:** Brainstorm, pitch a concept, ask "is this worth building?"  
**What it does:** Structured ideation with premise challenge, market research, and design exploration  
**Example:** "I want to build a dispatch system for contractors"  
**Output:** DESIGN.md with vision, alternatives, and scope recommendations  

### `/spec`
**When:** Turn an idea into a GitHub issue, write up a ticket, create a backlog item  
**What it does:** Converts loose description into a precise, executable spec  
**Example:** "We need real-time notifications for when orders arrive"  
**Output:** Detailed spec with acceptance criteria, edge cases, test plan  

### `/plan-ceo-review`
**When:** Strategy, scope, ambition — "think bigger", "is this the right problem?"  
**What it does:** CEO-level review of plans, challenges premises, proposes expansions  
**Example:** "Should we build the full deal engine or start with manual deals?"  
**Modes:** SCOPE EXPANSION, SELECTIVE EXPANSION, HOLD SCOPE, SCOPE REDUCTION  

### `/plan-eng-review`
**When:** Review architecture, technical feasibility, design lock-in  
**What it does:** Engineering-focused plan review, system design, database decisions  
**Example:** "Is PostgreSQL the right choice for our analytics?"  

### `/plan-design-review`
**When:** Design system, visual identity, UX flows in the plan  
**What it does:** Design-focused review of UX/UI decisions  

### `/plan-devex-review`
**When:** Developer experience, API/CLI/SDK design  
**What it does:** Reviews API contracts, onboarding flow, ergonomics  

### `/autoplan`
**When:** "Review everything" — you want all reviews at once  
**What it does:** Runs CEO, Eng, Design, and DevEx reviews in sequence  

---

## CODE REVIEW & QA

### `/review`
**When:** Pre-landing code review, "look at my changes", check the diff  
**What it does:** Comprehensive code review for correctness, security, performance  
**Output:** Findings table with severity, file:line, and recommendations  

### `/qa`
**When:** Test the site, find bugs, "does this work?", check a deploy  
**What it does:** Visual QA testing, flow validation, screenshot capture  
**Uses:** Aside browser (real browser with your login) or gstack's fallback browser  

### `/qa-only`
**When:** Just report bugs, don't fix them  
**What it does:** Pure bug hunting without implementation  

### `/design-review`
**When:** Visual polish, design audit, "this looks off"  
**What it does:** Checks typography, spacing, color, layout, accessibility  
**Output:** Findings + suggested fixes  

### `/design-consultation`
**When:** Building a design system from scratch  
**What it does:** Creates DESIGN.md with typography, color palette, spacing rules  

### `/design-html`
**When:** Generate production HTML/CSS for a design  
**What it does:** Turns DESIGN.md into pixel-perfect, accessible HTML  

### `/canary`
**When:** Monitor production after shipping  
**What it does:** Post-deploy health checks, error monitoring, performance baselines  

### `/benchmark`
**When:** Page speed, performance regression, Core Web Vitals  
**What it does:** Runs performance tests, compares baselines, flags regressions  

---

## SHIPPING & DEPLOYMENT

### `/ship`
**When:** Land it — deploy, push, create a PR, merge to main  
**What it does:** Review diff → bump VERSION → update CHANGELOG → commit → push → create PR  
**Output:** GitHub PR with auto-filled body, linked to commits  

### `/land-and-deploy`
**When:** Merge + deploy + verify as one flow  
**What it does:** `/ship` + immediate deployment to production + health check  

### `/setup-deploy`
**When:** Configure deployment for your project  
**What it does:** Wires up CI/CD, environment variables, deployment targets  

### `/document-release`
**When:** Update docs after shipping  
**What it does:** Regenerates README, API docs, CHANGELOG from code  

### `/document-generate`
**When:** Write docs from scratch  
**What it does:** Generates documentation, architecture guides, API references  

---

## DEBUGGING & INVESTIGATION

### `/investigate`
**When:** Bug report, broken behavior, "why is this broken?"  
**What it does:** Root-cause analysis, hypothesis testing, fix validation  
**Example:** "Checkout fails on mobile"  

### `/cso` (Chief Security Officer)
**When:** Security audit, OWASP vulnerabilities, "is this secure?"  
**What it does:** Threat modeling, vulnerability scanning, security recommendations  

### `/health`
**When:** Code quality dashboard  
**What it does:** Reports coverage, debt, test status, dependency vulnerabilities  

---

## BROWSER & SCRAPING

### `/browse`
**When:** Open a site, inspect a page, take a screenshot, test interactively  
**What it does:** Real browser automation with Aside (your real sessions)  
**Fallback:** gstack's own browser if Aside not running  

### `/open-gstack-browser`
**When:** Launch gstack's fallback browser (on Linux/Windows or if Aside unavailable)  
**What it does:** Opens a dedicated browser for agent work  

### `/setup-browser-cookies`
**When:** Import cookies for authenticated testing  
**What it does:** Loads your login sessions into the test browser  

### `/pair-agent`
**When:** Share browser with another agent (Codex, OpenClaw, etc.)  
**What it does:** Hands off browser control to a sister agent  

### `/scrape`
**When:** Pull data off a page, "grab the table from…"  
**What it does:** Extracts structured data from web pages  
**Output:** CSV, JSON, or markdown table  

### `/skillify`
**When:** Save the last `/scrape` as a reusable skill  
**What it does:** Turns a one-off scrape into a reusable tool  

---

## MONITORING & ANALYSIS

### `/retro`
**When:** Weekly retrospective, "how'd we do?"  
**What it does:** Analyzes what shipped, what broke, lessons learned  
**Output:** Structured retro report with learnings  

### `/learn`
**When:** "What has gstack learned?"  
**What it does:** Shows learnings from past sessions (fixes, patterns, pitfalls)  

### `/codex`
**When:** Get a second opinion, second-model review  
**What it does:** Independent review from a different AI model (Codex)  

---

## CONFIGURATION & SAFETY

### `/gstack-upgrade`
**When:** Update gstack to latest version  
**What it does:** Pulls latest, runs setup, shows what's new  

### `/plan-tune`
**When:** Stop asking me that question, tune question sensitivity  
**What it does:** Customizes AskUserQuestion behavior  

### `/context-save`
**When:** Save progress, checkpoint your work  
**What it does:** Saves state to `.planning/STATE.md` for later resumption  

### `/context-restore`
**When:** Resume, where was I?  
**What it does:** Loads prior checkpoint and restarts from there  

### `/freeze` / `/unfreeze`
**When:** Restrict edits to a directory (safety mode)  
**What it does:** Locks a directory so changes can only be read, not modified  

### `/careful` / `/guard`
**When:** Safety mode, need extra verification on destructive operations  
**What it does:** Adds approval gates to risky operations (force-push, delete, etc.)  

---

## QUICK FIXES (GSD)

### `/gsd-fast`
**When:** Typo fix, config update, rename variable (≤3 files, ≤1 minute)  
**What it does:** Direct inline execution without planning overhead  

### `/gsd-quick`
**When:** Multi-step fix that needs planning  
**What it does:** Lightweight planning + execution (not as heavy as full GSD)  

### `/gsd-upgrade`
**When:** Update GSD framework  
**What it does:** Upgrades the GSD toolchain  

---

## WHEN IN DOUBT

**Use this decision tree:**

1. **Is it a new idea?** → `/office-hours`
2. **Do I need to spec it?** → `/spec`
3. **Is it strategic/scope?** → `/plan-ceo-review`
4. **Is it technical design?** → `/plan-eng-review`
5. **Is it UI/design?** → `/plan-design-review`
6. **Do I need to test?** → `/qa`
7. **Do I need code review?** → `/review`
8. **Ready to ship?** → `/ship`
9. **Something broken?** → `/investigate`
10. **Is it secure?** → `/cso`
11. **Quick fix?** → `/gsd-fast`

**If nothing matches → answer directly (no skill needed)**

---

## COMING SOON / EXPERIMENTAL

- `/make-pdf` — Convert to PDF
- `/devex-review` — Developer experience audit
- `/document-release` — Release note generation

---

**Tip:** Most skills can be invoked with just the command. Some take arguments:
```bash
/ship "feat: add real-time notifications"
/qa https://example.com
/codex "is this approach correct?"
/investigate "checkout fails on mobile"
```

**Keyboard shortcut:** In Claude Code, type `/` to see the full list of available commands.

