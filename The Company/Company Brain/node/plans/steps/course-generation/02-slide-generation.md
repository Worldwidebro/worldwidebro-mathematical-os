---
id: STEP-02-slide-generation
title: "02. Slide Generation"
agent: education-teacher
step_file: "02-slide-generation.md"
status: ACTIVE
updated: 2026-09-06
tags: [loop-step, education, course-generation, fractal]
---

[[STARTHERE]] | [[node/plans/course-generation-loop|Course Generation Loop]] | [[16-AGENTS/AGT-006-education-teacher|education-teacher]] | [[42-EVALUATION/README|Evaluation]]

# 02. Slide Generation

**Navigation:** [[node/plans/steps/course-generation/01-curriculum-planning|Previous: 01-curriculum-planning]] ◄ ─── ► [[node/plans/steps/course-generation/03-quiz-creation|Next: 03-quiz-creation]]  
**Executing Agent:** [[16-AGENTS/AGT-006-education-teacher|education-teacher]]  
**Parent Loop:** [[node/plans/course-generation-loop|Course Generation Loop]]  
**Evaluation Subsystem:** [[42-EVALUATION/README|42-EVALUATION]]

---

# 2. Slide Generation

Create presentation slides from curriculum outline.

## Input
- Approved curriculum outline
- Module structure
- Learning objectives

## Process
1. Generate slide title and key points per module
2. Add speaker notes for each slide
3. Identify image/diagram opportunities
4. Generate image prompts for educational visuals
5. Structure as PPTX-compatible slides

## Output
- 50-200 slides depending on course length
- Includes: titles, bullet points, speaker notes
- Image placeholders with generation specs
- Consistent formatting template

## Validation
- At least 1 slide per learning objective
- Speaker notes non-empty on each slide
- All key concepts covered

---

## Step Execution Connections
- **Previous Step:** [[node/plans/steps/course-generation/01-curriculum-planning|Previous: 01-curriculum-planning]]
- **Next Step:** [[node/plans/steps/course-generation/03-quiz-creation|Next: 03-quiz-creation]]
- **Executing Agent:** [[16-AGENTS/AGT-006-education-teacher|education-teacher]]
- **Master Evaluation Hub:** [[42-EVALUATION/README|42-EVALUATION]]
- **Parent Plan:** [[node/plans/course-generation-loop|Course Generation Loop]]
