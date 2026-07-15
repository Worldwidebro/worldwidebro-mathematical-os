---
name: open-source-layer
type: Third-party / vendored code — separation layer
date: 2026-07-03
---

# 11-OPEN-SOURCE

**This folder is new and currently empty on purpose.** It did not exist before 2026-07-03.
Third-party/vendored repos are not moved here yet — this just establishes where they go
going forward, per the venture-studio layering principle: don't mix third-party code with
your own.

Numbered 11 (not 03) because `03` is already taken by `03-PORTFOLIO`.

## Where the real repos still live (unmoved)

All 31 repo clones are still at `WORLDWIDEBRO-OS/06-TECHNOLOGY/repositories/` — mixed
together, third-party and proprietary side by side. Nothing has been moved. Rough triage
based on recognizable project names (not verified per-repo):

**Looks third-party / open-source (candidates to eventually move here):**
`comfy` (ComfyUI), `composio`, `LightRAG`, `magika`, `MoneyPrinterTurbo`, `MoneyPrinterV2`,
`omi`, `OpenBB`, `RAG-Anything`, `TradingAgents`, `TrendRadar`, `vibetunnel`, `opensre`,
`Miro-Fish`, `thunderbolt`, `claude-code-proxy`

**Looks proprietary / worth keeping close to `12-SHARED-LIBRARIES` or a venture (needs confirmation, not moved):**
`iza-os`, `iza-os-marketing-core`, `iza-os-rag-system`, `design-system`,
`design-system-integrated`, `design-system-live`, `portfolio-mcp`, `mcp-dashboard`,
`platform-repos`, `repos`, `security-stack`, `twenty-local-test`, `make-workflows`, `Claude`, `_docs`

This triage is a guess from folder names only — verify before actually moving anything.
The repo↔venture capability join only being 14/1,597 (0.9%, see the Holdings Playbook §5
and memory `company-factory-and-repo-platform`) is plausibly connected to this mixing:
capability tagging has no clean signal for "ours to modify" vs. "upstream, wrap it."

## Convention going forward

New third-party clones/forks should land here, one subfolder per project, unmodified where
possible. If a fork needs substantial changes, note that in this README rather than silently
diverging from upstream.
