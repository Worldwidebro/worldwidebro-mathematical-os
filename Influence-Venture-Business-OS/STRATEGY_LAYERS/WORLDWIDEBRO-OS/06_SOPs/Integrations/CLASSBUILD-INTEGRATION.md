# ClassBuild Self-Service Course Generation

Education ventures can auto-generate complete, production-ready courses using ClassBuild. This system allows ventures to independently create and update course content without manual intervention.

## Quick Start

For any education venture in the 10-course program:

```bash
# From Documents directory:
./classbuild_venture_generator.sh EDU-023-Cybersecurity-Bootcamp "Cybersecurity Bootcamp"
```

This generates a complete course with:
- ✓ Interactive HTML chapters (with embedded widgets)
- ✓ Gamified practice quizzes (with confidence calibration)
- ✓ PowerPoint slides (with speaker notes)
- ✓ AI-narrated audiobooks (Gemini TTS)
- ✓ AI-generated infographics
- ✓ Teaching pack (discussion starters, activities)
- ✓ Mastery challenges (SCORM 2004 compatible)
- ✓ Research dossiers (sources and synthesis)

## Batch Generation

To generate courses for all 10 ventures:

```bash
cd ~/Documents
python3 classbuild_batch_generator.py
```

Set environment variables first:
```bash
export ANTHROPIC_API_KEY=sk-...
export GEMINI_API_KEY=...  # Optional, for audio + infographics
```

## What Gets Generated

Each venture's `/courses` directory contains:

```
EDU-023-Cybersecurity-Bootcamp/
├── courses/
│   ├── chapter-001-fundamentals/
│   │   ├── content.html          # Interactive chapter
│   │   ├── quiz.json             # Practice quiz
│   │   ├── slides.pptx           # Presentation
│   │   ├── audio.mp3             # Narration
│   │   ├── infographic.png       # Visual summary
│   │   └── research.md           # Sources + synthesis
│   ├── chapter-002-...
│   ├── syllabus.json             # Course architecture
│   ├── index.html                # Course viewer
│   └── export/
│       ├── course.zip            # All materials
│       └── course-viewer.html    # Standalone viewer
├── VENTURE.json                  # Updated with course metadata
└── README.md
```

## Configuration

Each venture is configured in `/Documents/classbuild_ventures.json`:

```json
{
  "EDU-023-Cybersecurity-Bootcamp": {
    "topic": "Cybersecurity Fundamentals & Ethical Hacking",
    "chapters": 12,
    "level": "intermediate",
    "notes": "Hands-on security labs and penetration testing"
  }
}
```

Parameters:
- **topic**: Course subject (required)
- **chapters**: Number of chapters (8-24 recommended)
- **level**: `beginner`, `intermediate`, `advanced`, `advanced-undergrad`, `professional`
- **notes**: Custom instructions (audience, tone, specific topics)

## API Keys Required

| API | Purpose | Optional |
|-----|---------|----------|
| Anthropic Claude | Course generation (all stages) | ❌ Required |
| Google Gemini | Audio narration + infographics | ✅ Optional |

Get keys:
- [Claude API](https://console.anthropic.com/api-keys)
- [Gemini API](https://aistudio.google.com/app/apikey)

## Venture Self-Service Workflow

1. **Define Course** — Add/update entry in `classbuild_ventures.json`
2. **Generate** — Run `classbuild_venture_generator.sh` or batch generator
3. **Review** — Open `courses/index.html` to preview
4. **Export** — Download `courses/export/course.zip` for LMS/distribution
5. **Iterate** — Update `classbuild_ventures.json` and regenerate

## Example: From Idea to Deployed Course

### Step 1: Update Configuration

```json
{
  "EDU-023-Cybersecurity-Bootcamp": {
    "topic": "Cybersecurity Fundamentals & Ethical Hacking",
    "chapters": 12,
    "level": "intermediate",
    "notes": "Hands-on security labs. Include NIST framework, threat modeling, and real breach case studies."
  }
}
```

### Step 2: Generate Course

```bash
export ANTHROPIC_API_KEY=sk-...
./classbuild_venture_generator.sh EDU-023-Cybersecurity-Bootcamp "Cybersecurity Bootcamp"
```

### Step 3: Preview & Export

```bash
# Open in browser
open ~/Library/Mobile\ Documents/com~apple~CloudDocs/Documents/Obsidian\ Vault/07-BUSINESS-STRATEGY/ventures/Education/EDU-023-Cybersecurity-Bootcamp/courses/index.html

# Export for LMS
cp ~/Library/Mobile\ Documents/com~apple~CloudDocs/Documents/Obsidian\ Vault/07-BUSINESS-STRATEGY/ventures/Education/EDU-023-Cybersecurity-Bootcamp/courses/export/course.zip ~/Downloads/EDU-023-course.zip
```

### Step 4: Update Venture Metadata

VENTURE.json is automatically updated with:

```json
{
  "classbuild": {
    "topic": "Cybersecurity Fundamentals & Ethical Hacking",
    "chapters": 12,
    "level": "intermediate",
    "status": "generated",
    "generated_at": "2026-05-16T14:23:45.123456"
  }
}
```

## ClassBuild Learning Science

Every generated course applies five evidence-based learning principles:

1. **Retrieval Practice** — "Think About It" prompts test recall before answers
2. **Interleaving** — Related concepts mixed across practice sets
3. **Dual Coding** — Both verbal + visual representations
4. **Concrete Examples** — Abstract concepts grounded in real-world cases
5. **Elaboration** — Connections to prior knowledge via discussions + thought experiments

The syllabus annotates which principle each chapter emphasizes.

## Advanced Configuration

For full control, see ClassBuild CLI flags:
- `--theme`: Visual design (`midnight`, `classic`, `ocean`, `warm`)
- `--length`: Content depth (`concise`, `standard`, `comprehensive`)
- `--widgets`: Interactive elements per chapter (default: 3)
- `--cohort`: Expected class size (affects activity design)
- `--environment`: Teaching context (`lecture-theatre`, `collaborative`, `flat-classroom`, `online-hybrid`)

Edit the scripts to pass these:

```bash
# In classbuild_venture_generator.sh, modify the npx tsx command:
npx tsx scripts/generate-course.ts \
    --topic "$TOPIC" \
    --chapters "$CHAPTERS" \
    --level "$LEVEL" \
    --theme warm \
    --length comprehensive \
    --environment online-hybrid \
    --output "$OUTPUT_DIR"
```

## Status

Currently generating for:
- ✅ EDU-002: Code Bootcamp Pro
- ✅ EDU-003: Math Mastery Platform
- ✅ EDU-004: Language Learning App
- ✅ EDU-006: Executive MBA Online
- ✅ EDU-008: Data Science Bootcamp
- ✅ EDU-014: Coding For Beginners
- ✅ EDU-015: Fitness Coach Certification
- ✅ EDU-017: Cloud Computing Academy
- ✅ EDU-022: Leadership Development Program
- ✅ EDU-023: Cybersecurity Bootcamp

## Next Steps

1. Install ClassBuild dependencies: `cd /tmp/classbuild && npm install`
2. Set `ANTHROPIC_API_KEY` environment variable
3. Run batch generator or per-venture generator
4. Review generated courses in `/courses` subdirectory
5. Export and deploy to LMS/distribution channel

---

**Related Files:**
- `/Documents/classbuild_batch_generator.py` — Batch generation orchestrator
- `/Documents/classbuild_venture_generator.sh` — Per-venture generator
- `/Documents/classbuild_ventures.json` — Venture configuration
