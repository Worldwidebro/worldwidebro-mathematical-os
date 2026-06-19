# ClassBuild Self-Service Course Generation

Each education venture can independently regenerate their course materials at any time.

## For Venture Teams

### Quick Start: Generate Your Course

```bash
cd ~/Documents
./classbuild_venture_generator.sh EDU-023-Cybersecurity-Bootcamp "Cybersecurity Bootcamp"
```

This generates a complete course with:
- ✓ Interactive HTML chapters
- ✓ Gamified practice quizzes
- ✓ PowerPoint slides with speaker notes
- ✓ AI-narrated audiobook
- ✓ Infographics
- ✓ Teaching materials
- ✓ Mastery challenges

Output goes to your venture's `/courses` directory.

### Regenerate After Updates

Edit your venture's config in `/Documents/classbuild_ventures.json`:

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

Then regenerate:

```bash
./classbuild_venture_generator.sh EDU-023-Cybersecurity-Bootcamp "Cybersecurity Bootcamp"
```

Changes reflected in `/courses/index.html` within minutes.

### Course Structure

Your generated course includes:

```
courses/
├── chapter-001-fundamentals/
│   ├── content.html          # Interactive chapter
│   ├── quiz.json             # Practice quiz
│   ├── slides.pptx           # Presentation
│   ├── audio.mp3             # Narration
│   ├── infographic.png       # Visual summary
│   └── research.md           # Sources + synthesis
├── index.html                # Course viewer
├── syllabus.json             # Course architecture
└── export/
    ├── course.zip            # All materials (download this)
    └── course-viewer.html    # Standalone viewer
```

### Export & Distribute

1. **Download all materials**: `courses/export/course.zip`
2. **Share standalone viewer**: `courses/export/course-viewer.html` (no dependencies)
3. **Import to LMS**: Upload `course.zip` to your learning management system

### Advanced: Customize Generation

Edit `classbuild_ventures.json` parameters:

| Parameter | Options | Effect |
|-----------|---------|--------|
| `chapters` | 8-24 | Course length and depth |
| `level` | `beginner`, `intermediate`, `advanced`, `advanced-undergrad`, `professional` | Complexity and audience |
| `notes` | Custom text | Additional instructions (audience, tone, specific topics) |

Example advanced config:

```json
{
  "EDU-023-Cybersecurity-Bootcamp": {
    "topic": "Cybersecurity Fundamentals & Ethical Hacking",
    "chapters": 14,
    "level": "advanced",
    "notes": "Hands-on labs. Include NIST framework, breach case studies, real-world threat modeling. Assume students have sysadmin experience."
  }
}
```

### Troubleshooting

**"Course directory doesn't exist"**
- Run: `mkdir -p ~/path/to/venture/courses`

**"Config file not found"**
- Ensure `/Documents/classbuild_ventures.json` exists with your venture entry

**"Generation takes too long"**
- Large chapters (20+) may take 30+ minutes
- Check progress in terminal output

**"API key error"**
- Ensure `ANTHROPIC_API_KEY` is set: `export ANTHROPIC_API_KEY=sk-...`

### Next Steps

1. Review generated course: Open `courses/index.html` in browser
2. Test interactive elements and quizzes
3. Download `courses/export/course.zip` for distribution
4. Share with students or upload to LMS
5. Gather feedback and regenerate with improved notes

---

**For batch generation** (all ventures at once), see `/Documents/CLASSBUILD-INTEGRATION.md`
