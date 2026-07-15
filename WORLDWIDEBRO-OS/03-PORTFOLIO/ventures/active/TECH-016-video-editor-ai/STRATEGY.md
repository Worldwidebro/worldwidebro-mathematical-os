# Foldcraft (mc-006) — Strategy

This is the strategic frame for this repo: what business it serves, what product powers it, what the repo itself is for, and what's real vs. aspirational as of 2026-07-06.

---

## Business Goal (mc-006 / Foldcraft)

> Help businesses turn ideas into high-quality video content faster, at lower cost, through AI-assisted creative production.

Target metrics: projects delivered, MRR, client retention, production turnaround time, customer satisfaction.

**Status: aspirational, not yet tracked.** `VENTURE.json` in this repo still carries auto-generated boilerplate for a newsletter business (`first_dollar.platform: Substack`, ICP about "curated business deals + AI tools") — a mismatch left over from mass venture-shell generation, not real content for a video studio. None of the target metrics above have a tracking mechanism yet. Fixing `VENTURE.json` to reflect an actual video-production offer is a prerequisite for this goal meaning anything.

---

## Product Goal (OpenMontage)

> Build an AI-native production system that orchestrates every stage of video creation — from intake to final delivery — with humans involved only where they add the most value.

**Status: partially real, verified this session.** OpenMontage (`Worldwidebro/Worldwidebro` monorepo, `WORLDWIDEBRO-OS/06-TECHNOLOGY/repositories/OpenMontage`) already implements a pipeline-manifest + stage-director + tool-registry + checkpoint architecture: `research → proposal → script → scene_plan → assets → edit → compose → publish`, with human-approval gates and an append-only decision log. This was proven end-to-end producing a real deliverable — a TikTok ad for a different venture (Angels in Daylight / EC-001) — with schema-validated artifacts at every stage and an actual rendered, ffprobe-verified MP4.

What's **not** yet real: "coordinate AI models" is thin (video-generation providers are 5 of 17 configured as of this session — Grok, Kling, Minimax, Seedance, Veo, via one `FAL_KEY`); "learn from completed work" has no implementation — there is no feedback loop from delivered projects back into future planning.

---

## Repository Goal

> Create a modular, extensible AI video production platform that combines workflows, models, and agents into a reusable production operating system for creative studios, agencies, and enterprises.

**Status: real — this already describes OpenMontage's actual architecture** (third-party open source, tool registry with `capability`/`provider`/`runtime` metadata, pluggable pipeline definitions in `pipeline_defs/`, Layer 2/3 skill separation). This repo (Foldcraft) is deliberately **not** where that platform lives — it's the frontend/brand layer only. Duplicating the platform here would fragment the one working implementation.

---

## Long-Term Vision

> The production operating system that powers every Media & Content (MC-sector) venture in the portfolio — commercials, social content, education, marketing, animation, podcasts, branded media.

**Status: directionally correct, unproven at scale.** As of this session, exactly **one** venture (Foldcraft/mc-006, via this frontend + the Angels in Daylight ad as a proof-of-concept render) has touched OpenMontage. The other ~14 MC-sector ventures already scaffolded (mc-001 YouTube network, mc-002 podcast network, mc-005 content-creation studio, mc-007 animation studio, mc-008 music production, etc.) are empty shells with no connection to OpenMontage yet.

## North Star

> Transform a client's idea into a professionally delivered multimedia project by orchestrating AI models, specialized agents, human approvals, and creative workflows — maximizing quality, speed, and scalability.

## Venture Ecosystem Position

```
Worldwidebro Holdings
    └── Media & Content Division (MC sector, ~20 ventures scaffolded)
            └── OpenMontage — shared backend production engine (real, proven once)
                    ├── Foldcraft (mc-006) — THIS repo: client-facing brand + frontend
                    └── mc-001, mc-002, mc-005, mc-007, mc-008, ... — not yet connected
```

Foldcraft is the client-facing brand; OpenMontage is the reusable platform other MC-sector ventures could share. That sharing does not exist yet — this is the first and, so far, only connection between a venture frontend and the OpenMontage backend.

## What's actually done vs. aspirational (as of this session)

| Item | Status |
|---|---|
| Foldcraft frontend (this repo) | ✅ Built, build-verified, browser-verified at desktop + mobile, pushed to `main` |
| OpenMontage backend | ✅ Cloned, configured, proven end-to-end on one real deliverable |
| Client Portal, Asset Library, Workflow Automation, Publishing System, Analytics | ❌ Not built — names in a proposed diagram, not implemented systems |
| Business metrics tracking | ❌ Not built — `VENTURE.json` has placeholder/mismatched content |
| Multi-venture sharing of OpenMontage | ❌ Not built — one connection exists (this repo), the other ~14 MC ventures are unconnected shells |
