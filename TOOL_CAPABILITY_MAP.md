---
name: tool-capability-map
type: Business Goals to MCP Mapping
date: 2026-06-22
source: MCP_REGISTRY.json
---

# Tool Capability Map

**Reference:** MCP_REGISTRY.json (source of truth) | **Use this. Don't search for tools.**

**Purpose:** Map business goals → available MCPs. Check this before asking "do we have a tool for X?"

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
| **supabase** | 🔴 CRITICAL | ✅ | Data source + knowledge graph | 2026-06-22 |
| **clickup** | 🟠 HIGH | ✅ | Task management | 2026-06-22 |
| **notion** | 🟠 HIGH | ✅ | Documentation + binders | 2026-06-22 |
| **slack** | 🟠 HIGH | ✅ | Real-time alerts | 2026-06-22 |
| **zapier** | 🟠 HIGH | ✅ | Automation (4 zaps) | 2026-06-22 |
| **gmail** | 🟠 HIGH | ✅ | Weekly briefings | 2026-06-22 |
| **github** | 🟠 HIGH | ✅ | Code deployment | 2026-06-22 |
| **graphify** | 🟠 HIGH | ✅ | Knowledge graph | 2026-06-22 |
| **memory** | 🟠 HIGH | ✅ | Persistent context | 2026-06-22 |
| google_calendar | 🟡 MEDIUM | ✅ | Meeting scheduling | 2026-06-22 |
| stripe | 🟡 MEDIUM | ✅ | Payment capture | 2026-06-22 |
| hubspot | 🟡 MEDIUM | ✅ | CRM (Phase 2) | 2026-06-22 |

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
