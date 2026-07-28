# 01_AI_BRAIN — Claude's Decision & Reasoning Layer

**Purpose:** Central control for all AI agent reasoning, prompt engineering, decision frameworks, and system intelligence.

**Canonical Segments:**

## 01-PROMPTS
System prompts, role definitions, agent instructions. Single source of truth for all Claude configurations.
- `worldwidebro-boss-prompt.md` — Meta-prompt for the entire OS
- `agent-{role}-system.md` — Role-specific prompts (orchestrator, executor, analyst, etc.)
- `sector-{SECTOR}-directive.md` — Sector-specific decision logic

## 02-REASONING_FRAMEWORKS
Decision logic and thinking models the agents use.
- `venture-scoring-matrix.md` — How ventures are evaluated (6 dimensions, weighted rubric)
- `capital-allocation-logic.md` — How $$ flows across 4 layers
- `risk-assessment-taxonomy.md` — Threat identification and mitigation
- `venture-readiness-framework.md` — Stage → readiness mapping

## 03-KNOWLEDGE_GRAPH
Structured facts that agents reference.
- `entity-taxonomy.json` — All venture types, sector types, capability types
- `relationship-ruleset.json` — What entities can/cannot relate to each other
- `capability-vocabulary.json` — Canonical capability definitions (MECE)
- `sector-definitions.json` — 31+ sector definitions + economies

## 04-EXECUTION_LOOPS
Automated workflows Claude agents orchestrate.
- `venture-bootstrap-loop.md` — Steps 1-20 to go from idea to revenue
- `capital-escalation-loop.md` — $5K→$135K monthly progression
- `agent-orchestration-loop.md` — How agents coordinate (handoff rules, dependencies)
- `session-learning-loop.md` — How sessions feed back into prompts

## 05-MEMORY_CHECKPOINTS
Long-term reasoning state across sessions.
- `session-{date}.md` — Atomic session record (what was decided, why, blockers)
- `learned-patterns.md` — Cross-session insights (what works, what doesn't)
- `assumption-log.md` — Decisions made on incomplete data (revisit when data changes)
- `prompt-iterations.md` — Evolution of system prompts (what changed and why)

## 06-AUDIT_TRAILS
Reasoning transparency for post-hoc verification.
- `decision-log.md` — Every major decision + supporting evidence + date
- `model-output-examples.md` — Real examples of what Claude outputs (for calibration)
- `rejection-analysis.md` — Decisions Claude made NOT to do something (reasoning clarification)

---

**Access Rules:**
- 💾 **NEVER edit 01-PROMPTS directly** — version via git, test in isolated branches
- 🧠 **REASONING_FRAMEWORKS are sacred** — changes require evidence (data + user approval)
- 📊 **KNOWLEDGE_GRAPH is the source of truth** — keep synchronized with Supabase
- 📝 **MEMORY_CHECKPOINTS auto-created** — Claude writes at session end, user reviews/deletes

**How Claude Uses This:**
1. **At session start:** Load worldwidebro-boss-prompt.md + relevant reasoning frameworks + last 3 session records
2. **During work:** Reference entity-taxonomy.json when making venture decisions
3. **At session end:** Append to session-{date}.md, update learned-patterns.md if significant
4. **Monthly:** Audit decision-log.md for patterns; update prompts if needed

---

**Last Updated:** 2026-07-27
