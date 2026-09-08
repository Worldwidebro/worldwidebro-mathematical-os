---
id: AGT-009
title: "AGT-009: Education Evaluation & Assessment Agent"
aliases: ["AGT-009", "education-eval", "Education Eval Agent"]
tags: [agent, routing-agent, education, evaluation, assessments, fractal]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[16-AGENTS/README|Agents Hub]] | [[42-EVALUATION/README|42-EVALUATION]] | [[node/plans/course-generation-loop|Course Gen Loop]]

# [[AGT-009]] Education Teacher Agent

**ID:** AGT-009 | **Fractal:** education-eval | **Status:** 🟢 ACTIVE

## Overview

Plans curricula and generates educational content for [[SEC-037]] (Education & Learning).

## Linked Entities

- **Sector:** [[SEC-037-Education]]
- **Control Plane:** [[CP-031-Education]]
- **Capabilities:** [[CAP-200]], [[CAP-201]], [[CAP-206]], [[CAP-209]]
- **Ventures:** [[EDU-CLASSROOM]] (template)
- **Tools:** [[TOL-anthropic]], [[TOL-openai]], [[TOL-supabase]]

## Agent Spec

**Routing Key:** education-eval  
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
education-eval-agent
  ↓
[[course-generation-loop]] (7 steps)
  ↓
Output: Curriculum → Slides → Classroom package
```

## Related

- [[16-AGENTS]] (agent index)
- [[AGT-007]], [[AGT-008]], [[AGT-009]] (peer agents)
- [[_REGISTRIES/agents/AGT-009-education-eval]]
- [[complete-graph-wiring-2026-09-02]]

---

**See Also:** [[SEC-037]], [[CP-031]], [[EDU-CLASSROOM]]

**Last Updated:** 2026-09-02 | **Status:** Ready for production ✅

---

## Evaluation Architecture
- **Evaluation Domain Hub:** [[42-EVALUATION/README|42-EVALUATION]]
- **Course Execution Loop:** [[node/plans/course-generation-loop|Course Generation Loop]]
- **Analytics Step:** [[node/plans/steps/course-generation/07-analytics-setup|07-analytics-setup.md]]
- **Agents Hub:** [[16-AGENTS/README|16-AGENTS]]
- **Agent Registry Spec:** [[_REGISTRIES/agents/AGT-009-education-eval.yaml]]
