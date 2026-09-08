---
id: STEP-07-analytics-setup
title: "07. Analytics & Outcomes Setup"
agent: education-eval
step_file: "07-analytics-setup.md"
status: ACTIVE
updated: 2026-09-06
tags: [loop-step, education, course-generation, fractal]
---

[[STARTHERE]] | [[node/plans/course-generation-loop|Course Generation Loop]] | [[16-AGENTS/AGT-009-education-eval|education-eval]] | [[42-EVALUATION/README|Evaluation]]

# 07. Analytics & Outcomes Setup

**Navigation:** [[node/plans/steps/course-generation/06-export-classroom|Previous: 06-export-classroom]] ◄ ─── ► End of Loop (Complete)  
**Executing Agent:** [[16-AGENTS/AGT-009-education-eval|education-eval]]  
**Parent Loop:** [[node/plans/course-generation-loop|Course Generation Loop]]  
**Evaluation Subsystem:** [[42-EVALUATION/README|42-EVALUATION]]

---

# 7. Analytics Setup

Configure learning metrics and outcomes tracking.

## Input
- Course structure
- Learning objectives
- Quiz questions

## Process
1. Create Supabase tables: courses, classrooms, enrollments, progress
2. Define metrics: completion_rate, quiz_scores, time_spent
3. Setup RLS policies (student privacy)
4. Create dashboard queries
5. Configure outcome tracking

## Output
- Supabase schema created
- Metrics pipeline configured
- Dashboard queries ready
- RLS policies enforced

## Validation
- Tables created successfully
- Sample data loads
- Privacy policies verified

---

## Step Execution Connections
- **Previous Step:** [[node/plans/steps/course-generation/06-export-classroom|Previous: 06-export-classroom]]
- **Next Step:** End of Loop (Complete)
- **Executing Agent:** [[16-AGENTS/AGT-009-education-eval|education-eval]]
- **Master Evaluation Hub:** [[42-EVALUATION/README|42-EVALUATION]]
- **Parent Plan:** [[node/plans/course-generation-loop|Course Generation Loop]]
