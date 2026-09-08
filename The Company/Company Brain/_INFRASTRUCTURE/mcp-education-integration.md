---
id: INFRA-MCP-EDU
title: "Model Context Protocol (MCP) Servers for Education Integration"
aliases: ["_INFRASTRUCTURE/mcp-education-integration", "MCP Education Integration"]
tags: [infrastructure, mcp, education, tools, supabase, sequential-thinking]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_INFRASTRUCTURE/README|Operational Infrastructure]] | [[16-AGENTS/AGT-009-education-eval|AGT-009]] | [[node/plans/course-generation-loop|Course Gen Loop]] | [[_MCP/README|MCP Hub]]

# MCP Servers for Education Integration

## Official MCP Servers (modelcontextprotocol/servers)

### 🎯 Direct Education Fit
- **Sequential Thinking** — Dynamic problem-solving through thought sequences (ideal for course pacing, quiz difficulty)
- **Memory** — Knowledge graph-based persistent memory (student progress, learning profiles, knowledge retention)

### 🔗 Infrastructure Support
- **Fetch** — Web content fetching (import learning materials, embed external resources)
- **Filesystem** — Secure file operations (manage course exports, student work, assets)
- **Git** — Repository operations (version control for course content, student submissions)
- **Time** — Timezone management (async student cohorts across regions, deadline handling)

### 📊 Data & Integration
- **Postgres** — Database access (direct Supabase queries for courses, enrollments, progress)
- **SQLite** — Local data storage (offline mode, caching)

---

## Community MCP Servers (Relevant for Education)

### Content & Knowledge
- **Zotero** (zotero-server) — Bibliography & reference management
- **Hypothesis** — Annotation & highlighting tool integration
- **Notion** — Course wiki & knowledge base synchronization
- **Obsidian** — Course notes & learning management
- **Wikipedia** — Fact-checking & reference materials

### Communication
- **Slack** — Student notifications, cohort announcements
- **Discord** — Live Q&A channels, study groups
- **Email** — Course enrollment confirmations, progress reports

### Assessment & Tracking
- **LMS APIs** — Canvas, Blackboard, Moodle (if needed)
- **Analytics** — Mixpanel, PostHog (student engagement tracking)
- **Google Sheets** — Gradebook integration, roster management

### AI & Content Generation
- **Anthropic API** — Claude for grading, feedback generation
- **OpenAI** — Supplementary LLM for interactive content
- **Replicate** — Image/video generation for course materials
- **Stability AI** — Asset generation (diagrams, illustrations)

---

## Recommended Stack for Worldwidebro Education

### Tier 1 (Must Have)
1. **Postgres** MCP — Direct Supabase schema queries
2. **Sequential Thinking** — Adaptive pacing based on student performance
3. **Memory** — Knowledge graph of student profiles & learning paths
4. **Filesystem** — Export courses (PPTX, HTML, ZIP)

### Tier 2 (Should Have)
5. **Git** — Version control for course evolution
6. **Fetch** — Embed live web content in courses
7. **Notion** — Course wiki & instructor collaboration
8. **Slack** — Real-time notifications & support channels

### Tier 3 (Nice to Have)
9. **Google Sheets** — Gradebook & attendance sync
10. **Zotero** — Academic citation management for advanced courses

---

## Implementation Path

**Week 1:** Wire Postgres MCP (direct Supabase access)  
**Week 2:** Integrate Sequential Thinking (adaptive curriculum)  
**Week 3:** Implement Memory MCP (student profiles)  
**Week 4:** Add Filesystem exports (PPTX/HTML generation)  

**Milestone:** Full education loop (ClickUp → Fractal → Supabase → Student Dashboard)

---

## Connected Subsystems
- **Education Eval Agent:** [[16-AGENTS/AGT-009-education-eval|AGT-009]]
- **Course Generation Loop:** [[node/plans/course-generation-loop|Course Generation Loop]]
- **MCP Server Architecture:** [[_MCP/README|MCP Architecture]]
- **Tools Domain Hub:** [[18-TOOLS/README|18-TOOLS]]
