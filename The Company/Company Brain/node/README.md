---
id: PORTAL-NODE-PLANS-001
title: "node/ — Autonomous Loop Execution Plans & Step Harnesses"
aliases: ["node", "node/README", "Node Plans", "Loop Step Harnesses"]
tags: ["node", "plans", "execution", "loops", "course-generation"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING|55-LOOP-ENGINEERING]] | [[node/plans/course-generation-loop|Course Gen Loop]] | [[_EVAL/README|Operational Evaluation Hub]]

# node/ — Autonomous Loop Execution Plans & Step Harnesses

> **Authority:** Autonomous Execution Control Plane ([[50-MASTER-CONTROL/50-MASTER-CONTROL|CP-022]])  
> **Primary Plan:** [[node/plans/course-generation-loop|course-generation-loop.md]]  
> **Status:** 🟢 ACTIVE — 7-Step Course Generation Pipeline (2026-09-06)

---

## 1. Executive Summary

The **`node/`** directory houses production execution plans and structured step harnesses for multi-stage autonomous agents:
- **Master Plan**: [[node/plans/course-generation-loop|course-generation-loop.md]] — End-to-end curriculum production loop.
- **Step Sequence (`node/plans/steps/course-generation/`)**:
  1. `01-curriculum-planning.md` — Curriculum topic selection and module architecture.
  2. `02-slide-generation.md` — Visual presentation slide authoring.
  3. `03-quiz-creation.md` — Diagnostic quizzes and question bank synthesis.
  4. `04-interactive-design.md` — Interactive code sandboxes and exercise design.
  5. `05-tts-render.md` — Text-to-speech audio rendering and timecoding.
  6. `06-export-classroom.md` — SCORM / LMS package bundling and export.
  7. `07-analytics-setup.md` — Learning telemetry hooks and outcome tracking.

---

## 2. Connected Subsystems
- **Loop Orchestration**: [[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING|55-LOOP-ENGINEERING]] & [[fractal]]
- **Evaluation Agent**: [[16-AGENTS/AGT-009-education-eval|AGT-009 (Education Eval Agent)]]
- **Database Schema**: [[_INFRASTRUCTURE/supabase-education-schema.sql]]
