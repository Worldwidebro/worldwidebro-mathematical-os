---
name: agent-tool-capability-map
type: Agent → Tool → Capability Mapping (Current Infrastructure)
date: 2026-07-20
source: AGENTS.md + MCP_REGISTRY.json
version: 2.0
---

# Agent-Tool Capability Map (Current)

**Version:** 2.0 — **Current Infrastructure** (not Phase 1)

**Purpose:** Map which agents can use which tools. **This is the 9-systems-engineering gap: tools exist but agents can't discover or use them.**

**Answer to "do we see the MCP or Slack plugin?":** ✅ **MCPs exist but are NOT wired to agents.**

---

## Phase 1 Execution Goals

### Goal: Create Airtable Dashboard for 700 Ventures

| Need | MCP | Status | Effort | Notes |
|------|-----|--------|--------|-------|
| Create workspace | airtable | ✅ Ready | 10 min | Follow AIRTABLE_DASHBOARD_BLUEPRINT.md |
| Import venture CSV | airtable | ✅ Ready | 5 min | From ventures_16sector_classification.csv |
| Set up 5 views | airtable | ✅ Ready | 30 min | Views: Executive, OPCO, Status, Revenue, Red Flags |
| **PROCEED?** | | **✅ YES** | **45 min** | **All ready** |

---

## CRITICAL INSIGHT: 9 Systems Engineering Gaps

You have:
- ✅ 9 agents defined (AGENTS.md)
- ✅ Slack MCP available
- ✅ ClickUp MCP available
- ✅ OmniRoute (token compression)
- ✅ Loop Engineering (automation)

You're missing:
- ❌ **Agent identity in tool calls** — tools don't know who's calling them
- ❌ **Capability registry** — agents don't know what tools they can use
- ❌ **Permission layer** — no checks before agent actions
- ❌ **Tool discovery** — agents can't query "what's available?"
- ❌ **Event bus** — agents work in isolation
- ❌ **Memory controller** — agents access databases directly
- ❌ **Observability wiring** — no telemetry of agent actions
- ❌ **Coordination protocol** — no workflow orchestration
- ❌ **Organizational mapping** — tools not mapped to OPCO structure

### The Wiring Layer You Need

**Current flow (broken):**
```
venture_classifier → Supabase (direct)
                  ↓
                  (no audit, no permission check, no notification)
```

**Needed flow:**
```
venture_classifier
         ↓
   Capability Request: "Can I create ClickUp task?"
         ↓
   Permission Check: "Is venture_classifier allowed ClickUp?"
         ↓
   Tool Dispatch: "Call ClickUp MCP"
         ↓
   Audit Log: "venture_classifier called create_task at 11:20"
         ↓
   Event Publish: "venture_classified event"
         ↓
   Slack Notify: "#con-operations: New venture..."
```

---

### Goal: Create 18 Slack Channels (#opco-*)

| Need | MCP | Status | Effort |
|------|-----|--------|--------|
| create_channel | slack | ✅ Ready | 10 min |
| set_topic | slack | ✅ Ready | 5 min |
| add_members | slack | ✅ Ready | 10 min |
| **PROCEED?** | | **✅ YES** | **25 min** |

---

### Goal: Set Up ClickUp Task Management

| Need | MCP | Status | Effort |
|------|-----|--------|--------|
| create_space | clickup | ✅ Ready | 5 min |
| create_folder | clickup | ✅ Ready | 10 min |
| create_list | clickup | ✅ Ready | 5 min |
| auto_create_tasks | zapier | ✅ Ready | 30 min |
| **PROCEED?** | | **✅ YES** | **50 min** |

---

### Goal: Create Notion Documentation Hub

| Need | MCP | Status | Effort |
|------|-----|--------|--------|
| create_workspace | notion | ✅ Ready | 10 min |
| create_database | notion | ✅ Ready | 10 min |
| create_pages | notion | ✅ Ready | 30 min |
| daily_sync | zapier | ✅ Ready | 30 min |
| **PROCEED?** | | **✅ YES** | **80 min** |

---

### Goal: Populate 700 Ventures in Airtable

| Need | MCP | Status | Effort |
|------|-----|--------|--------|
| Query ventures | supabase | ✅ Ready | 5 min |
| Export CSV | native | ✅ Ready | 2 min |
| Bulk import | airtable | ✅ Ready | 10 min |
| **PROCEED?** | | **✅ YES** | **17 min** |

---

### Goal: Configure 4 Zapier Automation Zaps

| Zap | MCPs | Status | Effort |
|-----|------|--------|--------|
| Airtable → ClickUp | zapier | ✅ Ready | 15 min |
| Airtable → Notion | zapier | ✅ Ready | 15 min |
| Airtable → Slack | zapier | ✅ Ready | 15 min |
| Airtable → Gmail | zapier | ✅ Ready | 15 min |
| **PROCEED?** | | **✅ YES** | **60 min** |

---

### Goal: Schedule Weekly & Monthly Meetings

| Meeting | MCP | Status | Effort |
|---------|-----|--------|--------|
| OPCO Pres → CEO (Mon 10am) | google_calendar | ✅ Ready | 5 min |
| VM → OPCO Pres (Wed 2pm) | google_calendar | ✅ Ready | 5 min |
| Board meeting (Fri 2pm) | google_calendar | ✅ Ready | 5 min |
| Quarterly review (Last Fri) | google_calendar | ✅ Ready | 5 min |
| **PROCEED?** | | **✅ YES** | **20 min** |

---

---

## Wire These First (Priority Order)

### Priority 1: Slack Notifications (Week 1)
**What:** venture_classifier → Slack #con-operations when venture classified

**Config for venture_classifier:**
```yaml
agent_id: venture_classifier
slack_targets:
  - channel: "#con-operations"
    event: "venture_classified"
    template: "🎯 New venture: {name}, confidence: {confidence}"
```

**How cadence-check.py already does this:**
```python
python3 .grok/skills/cadence-check/cadence-check.py \
  --slack-webhook https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

### Priority 2: ClickUp Task Creation (Week 1-2)
**What:** venture_classifier → ClickUp: create task per classified venture

**Config:**
```yaml
agent_id: venture_classifier
clickup_targets:
  - list: "New Ventures (CON)"
    template: "Follow up: {venture_name}"
    assigned_to: "Venture Lead"
```

### Priority 3: Google Calendar Booking (Week 2)
**What:** project_scheduler → Calendar: book meetings from schedule

### Priority 4: Unified Memory Controller (Week 3)
**What:** All agents → shared memory access with permission checks

### Priority 5: Event Bus (Week 4)
**What:** Kafka/Redis topics so agents coordinate

---

### Goal: Send Weekly Executive Briefing (Monday 9am)

| Component | MCP | Status |
|-----------|-----|--------|
| Query data | airtable | ✅ Ready |
| Format email | gmail | ✅ Ready |
| Send email | gmail | ✅ Ready |
| Automate | zapier | ✅ Ready |
| **PROCEED?** | | **✅ YES** |

---

## All MCPs: Status Dashboard

| MCP | Priority | Status | Purpose | Last Tested |
|-----|----------|--------|---------|-------------|
| **airtable** | 🔴 CRITICAL | ✅ | Venture DB + dashboard | 2026-06-22 |
| **supabase** | 🔴 CRITICAL | ✅ | Data source + knowledge graph; also project/branch/migration/edge-function mgmt | 2026-07-08 |
| **clickup** | 🟠 HIGH | ✅ | Task management (tasks, docs, time tracking, chat) | 2026-07-08 |
| **notion** | 🟠 HIGH | ✅ | Documentation + binders (pages, databases, comments) | 2026-07-08 |
| **slack** | 🟠 HIGH | ✅ | Real-time alerts + canvas, channel/thread search | 2026-07-08 |
| **zapier** | 🟠 HIGH | ✅ | Automation (4 zaps) | 2026-06-22 |
| **gmail** | 🟠 HIGH | ✅ | Weekly briefings, drafts, labels, sensitive-message handling | 2026-07-08 |
| **github** | 🟠 HIGH | ✅ | Code deployment, PRs, issues, repo/branch mgmt | 2026-06-22 |
| **graphify** | 🟠 HIGH | ✅ | Knowledge graph | 2026-06-22 |
| **memory** | 🟠 HIGH | ✅ | Persistent context | 2026-06-22 |
| google_calendar | 🟡 MEDIUM | ✅ | Meeting scheduling, event response, time suggestions | 2026-07-08 |
| google_drive | 🟡 MEDIUM | ✅ | File search, read, create, copy, permissions | 2026-07-08 |
| stripe | 🟡 MEDIUM | ✅ | Payment capture, refunds, docs search | 2026-06-22 |
| hubspot | 🟡 MEDIUM | ✅ | CRM (contacts, deals, campaigns, analytics) | 2026-07-08 |
| **vercel** | 🟠 HIGH | ✅ | Deploys, project/domain mgmt, build/runtime logs — used for all sector/venture site launches | 2026-07-08 |
| jotform | 🟡 MEDIUM | ✅ | Form creation, submissions, app builder | 2026-07-08 |
| make | 🟢 LOW | ✅ | Scenario/automation builder (alt to Zapier) | 2026-07-08 |
| mermaid_chart | 🟢 LOW | ✅ | Diagram generation + GitHub/Notion/Jira sync | 2026-07-08 |
| pitchbook_premium | 🟢 LOW | ⚠️ auth required | Market/deal research | 2026-07-08 |
| planetscale | 🟢 LOW | ⚠️ auth required | Alt hosted DB | 2026-07-08 |
| hugging_face | 🟢 LOW | ⚠️ auth required | Model hub access | 2026-07-08 |
| indeed | 🟢 LOW | ✅ | Job/company data, resume lookup (career-ops) | 2026-07-08 |
| learning_commons_kg | 🟢 LOW | ✅ | Education standards knowledge graph (EDU sector) | 2026-07-08 |
| tavily | 🟡 MEDIUM | ✅ | Web search/crawl/extract/research | 2026-07-08 |
| exa | 🟡 MEDIUM | ✅ | Web search + fetch | 2026-07-08 |
| context7 | 🟡 MEDIUM | ✅ | Library/framework docs lookup | 2026-07-08 |
| playwright / puppeteer | 🟡 MEDIUM | ✅ | Browser automation, screenshots, form fill | 2026-07-08 |
| filesystem | 🟠 HIGH | ✅ | Local file read/write/search beyond default tools | 2026-07-08 |

**Note:** rows added 2026-07-08 reflect MCPs visible in the live tool list that were missing from this map (added 2026-06-22). Re-check this table whenever the deferred-tools system reminder shows names not listed here — that's the signal this file has drifted again.

---

## Video / Media Production Capability Map (added 2026-07-04)

**Reference:** `WORLDWIDEBRO-OS/06-TECHNOLOGY/repositories/OpenMontage/tools/tool_registry.py` (source of truth for this section — run `registry.provider_menu_summary()` for live status, don't trust this table to stay current forever)

Only **OpenMontage** is a real, working, agent-governed video production system today. MoneyPrinterTurbo/V2 are cloned but non-functional (0 packages installed, no config) and redundant with OpenMontage if fixed — do not stand them up.

| Need | Tool | Status | Effort | Notes |
|------|------|--------|--------|-------|
| Script → video orchestration | OpenMontage (`cinematic`/`hybrid` pipeline) | ✅ Ready | 0 | Only functional agentic video system; preflight via `registry.provider_menu_summary()` |
| Composition/render | ffmpeg, HyperFrames | ✅ Ready | 0 | Remotion registered but **not installed** (Node package unresolvable) — HyperFrames is the working motion-graphics runtime |
| TTS | Google TTS | ✅ Ready | 0 | Only configured TTS provider |
| TTS (free, better quality) | Piper (`tools/audio/piper_tts.py`) | ⚠️ Registered, not installed | 5 min | Local binary install, no API key needed |
| TTS (paid, best quality) | ElevenLabs | ❌ Needs key | 1 min | Set `ELEVENLABS_API_KEY` |
| Video generation (cloud) | Kling/Seedance/Veo/Minimax (via fal.ai) | ❌ Needs key | 1 min | One `FAL_KEY` unlocks all 4 |
| Video generation (free, local) | ComfyUI (`06-TECHNOLOGY/repositories/comfy`, WAN 2.2 workflows) | ❌ Cloned, zero setup | Complex (GPU + model downloads) | 1.8GB clone exists but no venv, no models, no custom_nodes — not a quick win |
| Image → motion on product stills (AnimateDiff) | Not wrapped anywhere | ❌ Genuine gap | Complex | Would run as a ComfyUI custom node, not a standalone repo |
| Shape-preserving product animation (ControlNet) | Not wrapped anywhere | ❌ Genuine gap | Complex | Same — ComfyUI custom node, not standalone |
| Music generation | `tools/audio/music_gen.py` | ⚠️ Misleading name | 1 min | This wraps **ElevenLabs Music API**, not Meta MusicGen/audiocraft — that's a genuine gap if wanted |
| Music search (free) | Pixabay | ✅ Ready | 0 | No local `music_library/` tracks yet either |
| Captions/subtitles | OpenMontage native + Remotion | ✅ Ready | 0 | |
| Social scheduling/publishing | Real gap — nothing in-house covers this | ❌ Not installed | — | `postiz-app` (starred, registry) is the fix |
| Paid-ads audit | — | ❌ Not installed | — | `claude-ads` skill (starred, registry) |
| SEO | — | ❌ Not installed | — | `claude-seo` skill (starred, registry) |
| Email marketing | — | ❌ Not installed | — | `listmonk` (starred, registry) |
| Full campaign orchestration | `iza-os-marketing-core/campaign-factory` | ❌ Facade only | — | `_run_agent()` is an explicit simulation stub — writes placeholder files, does not call any LLM. Do not rely on it. |

**PROCEED?** For product-cutout-driven kinetic ads (no live footage): ✅ YES with current free stack (ffmpeg + HyperFrames + Google TTS + Pixabay music). For cinematic b-roll/motion-from-stills: ⚠️ needs either `FAL_KEY` (fast, cheap, cloud) or a real ComfyUI setup investment (free, slow to stand up, local GPU).

---

## How to Use

**When asked to do something:**

1. **State the goal:** "Create 18 Slack channels"
2. **Look it up here:** Find "Goal: Create 18 Slack Channels"
3. **Check status:** All ✅? **Proceed immediately**
4. **Use the MCP:** Execute Slack commands
5. **No searching. No re-discovering. Just execute.**

---

## Key Rule

**Whenever you need a tool, FIRST check this map. If it's ✅ Ready, use it. If it's not in the map, ask me to check MCP_REGISTRY.json.**

Don't rely on memory or assumptions about what we have. This map is the truth.

---

**Source:** MCP_REGISTRY.json | **Updated:** 2026-06-22
