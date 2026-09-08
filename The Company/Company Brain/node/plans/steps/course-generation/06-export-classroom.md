---
id: STEP-06-export-classroom
title: "06. Export Classroom"
agent: education-teacher
step_file: "06-export-classroom.md"
status: ACTIVE
updated: 2026-09-06
tags: [loop-step, education, course-generation, fractal]
---

[[STARTHERE]] | [[node/plans/course-generation-loop|Course Generation Loop]] | [[16-AGENTS/AGT-006-education-teacher|education-teacher]] | [[42-EVALUATION/README|Evaluation]]

# 06. Export Classroom

**Navigation:** [[node/plans/steps/course-generation/05-tts-render|Previous: 05-tts-render]] ◄ ─── ► [[node/plans/steps/course-generation/07-analytics-setup|Next: 07-analytics-setup]]  
**Executing Agent:** [[16-AGENTS/AGT-006-education-teacher|education-teacher]]  
**Parent Loop:** [[node/plans/course-generation-loop|Course Generation Loop]]  
**Evaluation Subsystem:** [[42-EVALUATION/README|42-EVALUATION]]

---

# 6. Export Classroom

Package course as deliverable formats.

## Input
- All course assets (slides, quizzes, interactives, audio)
- Metadata (title, author, date)

## Process
1. Generate PPTX file from slides
2. Create interactive HTML package
3. Generate printable PDF
4. Create ZIP archive with all formats
5. Generate manifest files

## Output
- course_name.pptx (PowerPoint)
- course_name.html (interactive web version)
- course_name.pdf (printable)
- course_name.zip (complete package)
- manifest.json (metadata)

## Validation
- All formats generate without errors
- File sizes reasonable
- Manifest includes all assets

---

## Step Execution Connections
- **Previous Step:** [[node/plans/steps/course-generation/05-tts-render|Previous: 05-tts-render]]
- **Next Step:** [[node/plans/steps/course-generation/07-analytics-setup|Next: 07-analytics-setup]]
- **Executing Agent:** [[16-AGENTS/AGT-006-education-teacher|education-teacher]]
- **Master Evaluation Hub:** [[42-EVALUATION/README|42-EVALUATION]]
- **Parent Plan:** [[node/plans/course-generation-loop|Course Generation Loop]]
