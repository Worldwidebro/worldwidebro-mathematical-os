---
id: STEP-05-tts-render
title: "05. TTS Narration"
agent: education-teacher
step_file: "05-tts-render.md"
status: ACTIVE
updated: 2026-09-06
tags: [loop-step, education, course-generation, fractal]
---

[[STARTHERE]] | [[node/plans/course-generation-loop|Course Generation Loop]] | [[16-AGENTS/AGT-006-education-teacher|education-teacher]] | [[42-EVALUATION/README|Evaluation]]

# 05. TTS Narration

**Navigation:** [[node/plans/steps/course-generation/04-interactive-design|Previous: 04-interactive-design]] ◄ ─── ► [[node/plans/steps/course-generation/06-export-classroom|Next: 06-export-classroom]]  
**Executing Agent:** [[16-AGENTS/AGT-006-education-teacher|education-teacher]]  
**Parent Loop:** [[node/plans/course-generation-loop|Course Generation Loop]]  
**Evaluation Subsystem:** [[42-EVALUATION/README|42-EVALUATION]]

---

# 5. TTS Narration

Generate text-to-speech audio for course content.

## Input
- Slide content and speaker notes
- Course structure
- Voice preferences

## Process
1. Extract all speaker notes and narration text
2. Generate TTS audio clips per slide
3. Adjust timing and pacing
4. Attach timing metadata
5. Create audio manifest

## Output
- MP3/WAV audio files (1 per slide)
- Audio timing metadata
- Subtitle/transcript files
- Audio manifest JSON

## Validation
- Audio duration matches content
- All slides have audio (or marked as silent)
- Quality check: clarity, no glitches

---

## Step Execution Connections
- **Previous Step:** [[node/plans/steps/course-generation/04-interactive-design|Previous: 04-interactive-design]]
- **Next Step:** [[node/plans/steps/course-generation/06-export-classroom|Next: 06-export-classroom]]
- **Executing Agent:** [[16-AGENTS/AGT-006-education-teacher|education-teacher]]
- **Master Evaluation Hub:** [[42-EVALUATION/README|42-EVALUATION]]
- **Parent Plan:** [[node/plans/course-generation-loop|Course Generation Loop]]
