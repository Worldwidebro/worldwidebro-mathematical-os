# Graft Integration (TOL-000001)

**Status:** ✅ Registered  
**Version:** 0.16.0+  
**Node Requirement:** 20+  
**Company Brain Base:** 57-CODE-INTELLIGENCE  
**Related:** [[EXECUTION_STACK]] | [[FRACTAL_INTEGRATION]] | [[HERDR_INTEGRATION]]

---

## What Graft Does

Graft generates a **persistent code context graph** for any repository.

Instead of agents rediscovering repo structure every session (50+ tool calls), Graft builds:

```
Repository
    │
    ├── CODE_GRAPH (CGP-XXXX)
    │    ├── Symbols (functions, classes, exports)
    │    ├── Call relationships
    │    ├── Dependencies
    │    ├── Modules
    │    └── APIs
    │
    ├── CODE_NODE (CND-XXXX, per symbol)
    ├── CODE_EDGE (CED-XXXX, per relationship)
    ├── DEPENDENCY (DEP-XXXX, external libs)
    └── BLAST_RADIUS (BLR-XXXX, impact analysis)
```

---

## Agent Efficiency Gain

**Before Graft:**
- 30+ tool calls | 2-3 minutes | Rediscovered every session

**With Graft:**
- 1 tool call | <1 second | Persistent cache

---

## Object Types

| Type | ID | Purpose |
|---|---|---|
| CODE_GRAPH | CGP | Root analysis for repository |
| CODE_NODE | CND | Symbol (function/class/export) |
| CODE_EDGE | CED | Relationship (calls, imports) |
| DEPENDENCY | DEP | External library or module |
| BLAST_RADIUS | BLR | Impact analysis of change |

---

## Key Relationships

```
CBD HAS_CODE_GRAPH CGP
CGP CONTAINS_CODE_NODE CND (many)
CND CALLS CND (call graph)
CND DEPENDS_ON_CODE DEP
CND IMPLEMENTS_CODE CAP
CND HAS_BLAST_RADIUS BLR
```

---

## Setup

```bash
npm install -g @nanonets/graft
graft analyze <repo-path>  # Generates code graph
```

---

## Integration with Fractal

When [[FRACTAL_INTEGRATION]] agent spawns for a repository:

1. Load Graft output (1 call)
2. Agent immediately knows architecture
3. Start real work (not 50 discovery calls)

---

**See also:** [[EXECUTION_STACK]] | [[57-CODE-INTELLIGENCE]]
