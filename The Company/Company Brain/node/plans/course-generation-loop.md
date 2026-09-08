---
id: LOOP-EDU-001
title: "Course Generation Loop Specification"
loop_type: education
agent: education-teacher-agent
autonomy_levels: [L1, L2, L3]
max_cost: 50.00
max_iter_cost: 500.00
max_step_cost: 100.00
sector: SEC-037
control_plane: CP-031
created_at: 2026-09-02
updated_at: 2026-09-06
status: ACTIVE
tags: [loop, education, course-generation, fractal, execution-plan]
---

[[STARTHERE]] | [[19-ORCHESTRATION/19-ORCHESTRATION|Orchestration]] | [[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING|Loop Engineering]] | [[42-EVALUATION/README|42-EVALUATION]]

# Course Generation Loop

Comprehensive autonomous course creation from raw topics or document materials for [[SECTORS/SEC-037-education|SEC-037 (Education)]].

## Agents Involved
- **[[16-AGENTS/AGT-006-education-teacher|AGT-006]]** (Education Teacher) — Curriculum planning, slides, content structure.
- **[[16-AGENTS/AGT-007-education-peer|AGT-007]]** (Education Peer) — Discussion design, collaborative exercises.
- **[[16-AGENTS/AGT-008-education-content|AGT-008]]** (Education Content) — Quizzes, interactive exercises.
- **[[16-AGENTS/AGT-009-education-eval|AGT-009]]** (Education Eval) — Assessments, grading rubrics, outcomes analytics.

## Execution Sequence (7 Steps)
The execution flow progresses sequentially through dedicated step definitions in `node/plans/steps/course-generation/`:

1. [[node/plans/steps/course-generation/01-curriculum-planning|01. Curriculum Planning]] (L1: human approval required)
2. [[node/plans/steps/course-generation/02-slide-generation|02. Slide Generation]] (L2: auto-execute)
3. [[node/plans/steps/course-generation/03-quiz-creation|03. Quiz Creation]] (L2: auto-execute)
4. [[node/plans/steps/course-generation/04-interactive-design|04. Interactive Design]] (L2: auto-execute)
5. [[node/plans/steps/course-generation/05-tts-render|05. TTS Narration]] (L2: auto-execute)
6. [[node/plans/steps/course-generation/06-export-classroom|06. Export Classroom]] (L2: auto-execute)
7. [[node/plans/steps/course-generation/07-analytics-setup|07. Analytics & Outcomes Setup]] (L3: autonomous evaluation via AGT-009)

## Output & Database Persistence
- **PostgreSQL / Supabase Schema:** `courses`, `classrooms`, `slides`, `quiz_questions`, `quiz_results`, `learning_progress`.
- **Rendered Files:** `.pptx` presentations, `.html` interactive widgets, `.zip` classroom archives.
- **Evaluation Metrics:** `enrollment_count`, `completion_rate`, `comprehension_score`.

---

## Connected Subsystems
- **Evaluation Domain:** [[42-EVALUATION/README|42-EVALUATION]]
- **Loop Engineering:** [[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING|55-LOOP-ENGINEERING]]
- **Master Control:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
- **Target Sector:** [[SECTORS/SEC-037-education|SEC-037 (Education)]]
