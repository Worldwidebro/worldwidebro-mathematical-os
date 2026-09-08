# [[AGT-007]] Education Teacher Agent

**ID:** AGT-007 | **Fractal:** education-peer | **Status:** 🟢 ACTIVE

## Overview

Plans curricula and generates educational content for [[SEC-037]] (Education & Learning).

## Linked Entities

- **Sector:** [[SEC-037-Education]]
- **Control Plane:** [[CP-031-Education]]
- **Capabilities:** [[CAP-200]], [[CAP-201]], [[CAP-206]], [[CAP-209]]
- **Ventures:** [[EDU-CLASSROOM]] (template)
- **Tools:** [[TOL-anthropic]], [[TOL-openai]], [[TOL-supabase]]

## Agent Spec

**Routing Key:** education-peer  
**Type:** Routing Agent (delegates to Claude Opus)  
**Autonomy Levels:** L1 (report), L2 (generate), L3 (publish)

**Cost Model:**
- Per-step: $2.50
- Per-iteration: $50.00
- Per-run: $250.00

## Capabilities Implemented

| Cap ID | Name | Purpose |
|---|---|---|
| CAP-200 | Curriculum planning | Outline learning structure |
| CAP-201 | Slide generation | Create presentation slides |
| CAP-206 | Diagram creation | Generate educational visuals |
| CAP-209 | Content structuring | Organize educational content |

## Execution Flow

```
ClickUp Task: "Create course on [TOPIC]"
  ↓
education-peer-agent
  ↓
[[course-generation-loop]] (7 steps)
  ↓
Output: Curriculum → Slides → Classroom package
```

## Related

- [[16-AGENTS]] (agent index)
- [[AGT-007]], [[AGT-008]], [[AGT-009]] (peer agents)
- [[_REGISTRIES/agents/AGT-007-education-peer]]
- [[complete-graph-wiring-2026-09-02]]

---

**See Also:** [[SEC-037]], [[CP-031]], [[EDU-CLASSROOM]]

**Last Updated:** 2026-09-02 | **Status:** Ready for production ✅
