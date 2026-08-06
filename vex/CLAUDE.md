---
name: vex/CLAUDE
title: CLAUDE.md — VEX Core Library
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# CLAUDE.md — VEX Core Library

**Scope:** Core data types, constants, and shared utilities for VEX ecosystem  
**Updated:** 2026-08-05  
**Phase:** 0 (Repository Ingestion)

---

## What This Repo Does

VEX core library exports:
- **Venture types** (Venture, Sector, Capability)
- **Agent types** (Agent, AgentResult, AgentPolicy)
- **Graph types** (Node, Relationship, Query)
- **Constants** (sectors, capabilities, agent registry)

Used by: vex-api, vex-engine, vex-hero-site

---

## Key Files

```
src/
├── types/
│   ├── ventures.ts       → Venture, Sector
│   ├── capabilities.ts   → Capability, Relationship
│   ├── agents.ts         → Agent, AgentPolicy, AgentResult
│   └── graph.ts          → Neo4j node/relationship types
│
├── constants/
│   ├── sectors.ts        → 31-sector taxonomy
│   ├── capabilities.ts   → 500+ capabilities
│   └── agents.ts         → Agent registry
│
├── utils/
│   ├── validation.ts     → Type guards, schemas
│   └── transform.ts      → Normalize venture/capability data
│
└── index.ts              → Public exports
```

---

## Commands

```bash
npm install          # Install deps
npm run build        # Build to dist/
npm run test         # Run tests
npm run types        # Generate TypeScript types
```

---

## Integration Points

| Consumer | Uses | Phase |
|----------|------|-------|
| vex-api | Types, constants, validation | Phase 4+ |
| vex-engine | Types, agent registry, graph utils | Phase 8+ |
| vex-hero-site | Types, Sector constants | Phase 13+ |

---

## Critical Rules

1. **No external dependencies** — This is the core library. Keep it dependency-free (only TypeScript).
2. **Types are API** — Breaking changes here break all consumers.
3. **Constants are SOT** — sectors.ts, capabilities.ts must match Supabase/Neo4j.

---

## Active Tasks (Phase 0)

- [ ] Generate repomix-output.xml
- [ ] Generate dependency-map.json
- [ ] Verify no external dependencies

---

## Related

- CLAUDE.md (root): `~/.claude/CLAUDE.md`
- VEX-IMPLEMENTATION-ROADMAP: Phase 0-15 guide
