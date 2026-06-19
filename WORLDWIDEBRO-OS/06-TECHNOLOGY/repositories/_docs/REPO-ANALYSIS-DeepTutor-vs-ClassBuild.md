# DeepTutor vs ClassBuild — Comparative Analysis

**Date:** June 6, 2026  
**Analysis Focus:** Architecture, capabilities, learning science, integration patterns  
**Repos:** 
- DeepTutor (HKUDS) — https://github.com/HKUDS/DeepTutor
- ClassBuild (jtangen) — https://github.com/jtangen/classbuild

---

## Executive Summary

| Dimension | DeepTutor | ClassBuild |
|-----------|-----------|-----------|
| **Primary Role** | Persistent tutoring agent + knowledge workspace | Course generation pipeline |
| **Architecture** | Python backend + Next.js 16 frontend (full-stack) | React 19 + TypeScript (frontend-heavy, headless API) |
| **Entry Point** | Tutoring bot, chat, knowledge bases, skills | Course generator (single workflow) |
| **Learning Science** | Implicit (through conversation flows) | Explicit (5 evidence-based principles per chapter) |
| **Deployment** | Local or Docker, multi-user optional | Browser-based, entirely client-side |
| **Extensibility** | MCP servers, persistent agents, multi-channel | Prompt builders (reusable library) |
| **Team Size** | HKUDS research group (~20k GitHub stars) | Solo creator (Jason Tangen) |
| **LLM Models** | Multi-provider (Anthropic, OpenAI, Gemini, Qwen, local) | Claude (primary), OpenAI (images), ElevenLabs (audio) |

---

## 1. Core Purpose & Use Cases

### DeepTutor

**What it does:**
- Persistent AI tutoring companion for learning and knowledge work
- Interactive workspace spanning chat, co-writing, book generation, and knowledge management
- Autonomous TutorBot agents with memory, skills, and multi-channel presence
- Multi-user deployments with per-user isolation

**Primary workflows:**
1. Chat modes (Chat, Solve, Quiz, Research, Visualize)
2. Co-Writer (Markdown workspace)
3. Book Engine (interactive materials)
4. Knowledge Bases (RAG)
5. TutorBot (persistent agents)
6. Space (review library)

**Target user:** Self-directed learners, teachers, institutions

---

### ClassBuild

**What it does:**
- One-shot course generator: topic → complete course
- Produces syllabus, chapters, quizzes, slides, teaching pack, narration, challenges
- Exports to multiple formats (PowerPoint, SCORM, zip, standalone viewer)
- Grounded in 5 evidence-based learning principles

**Primary workflow:**
1. Setup (topic, audience, chapter count)
2. Syllabus (course design)
3. Research (web sources)
4. Build (content generation)
5. Export (packaging)

**Target user:** Educators, course designers, curriculum builders

---

## 2. Architecture Comparison

### DeepTutor Stack

```
Frontend (Next.js 16 + React 19)
    ↓ WebSocket + HTTP
FastAPI Backend (Python 3.11+)
    ├── Agents & Tools
    ├── RAG (LlamaIndex)
    ├── Web search, code execution
    ├── Memory system (L1/L2/L3)
    └── Multi-user auth + isolation
    ↓
Data Storage (SQLite, JSON)
```

**Key features:**
- Agentic core (tool registry, streaming)
- Multi-provider LLM support
- Persistent state (chat, KB, memory)
- Four deployment options (PyPI, source, Docker, CLI-only)

---

### ClassBuild Stack

```
Browser App (React 19 + Vite)
    ↓ (Prompt builders + local storage)
External APIs (via SDK, client-side)
    ├── Anthropic Claude (generation)
    ├── OpenAI (images)
    └── ElevenLabs (audio)
    ↓
CLI (Node.js via tsx) for batch generation
    ↓
Export Formats (PPTX, SCORM, HTML, ZIP)
```

**Key design:**
- Browser-native, no backend
- Bring Your Own Key (BYOK) architecture
- Modular prompt builders
- Five-stage fixed pipeline

---

## 3. Feature Comparison

| Capability | DeepTutor | ClassBuild |
|-----------|-----------|-----------|
| **Course Generation** | ✅ (Book Engine) | ✅ (Primary) |
| **Persistent Memory** | ✅ (L1/L2/L3) | ❌ |
| **Knowledge Base/RAG** | ✅ | ❌ |
| **Chat Interface** | ✅ (5 modes) | ❌ |
| **Quiz Generation** | ✅ | ✅ |
| **Slide Generation** | ❌ | ✅ |
| **Autonomous Agents** | ✅ (TutorBot) | ❌ |
| **Multi-Channel Presence** | ✅ | ❌ |
| **Learning Science Annotation** | ❌ | ✅ |
| **Web Search** | ✅ | ✅ |
| **Code Execution** | ✅ | ❌ |
| **Audio Narration** | ❌ | ✅ |
| **Multi-User** | ✅ | ❌ |
| **SCORM Export** | ❌ | ✅ |

---

## 4. Learning Science Integration

### DeepTutor
- **Implicit:** Relies on instructional design of users
- **Flexible:** No pedagogical prescription
- **Tools:** RAG (retrieval), quizzes, multiple surfaces (elaboration)

### ClassBuild
- **Explicit:** 5 principles embedded in every chapter
  1. Retrieval practice (Think About It prompts + quizzes)
  2. Interleaving (mixed concepts across practice)
  3. Dual coding (visual + verbal)
  4. Concrete examples (vivid scenarios)
  5. Elaboration (discussion, thought experiments)
- **Prescribed:** Enforces quality standards
- **Annotated:** Each chapter tagged with principles used

---

## 5. Code Organization

### DeepTutor (60-70k LOC)

```
deeptutor/
├── core/              # Stream, tool protocol
├── agents/            # Agent orchestration
├── capabilities/      # Chat, Solve, Quiz, Research, Visualize
├── tools/             # RAG, web, code, reason
├── knowledge/         # LlamaIndex wrapper
├── book/              # Book engine
├── tutorbot/          # nanobot + channels
├── multi_user/        # Auth, grants
└── api/               # FastAPI routes

web/
├── app/               # Next.js app directory
├── components/        # React components
└── hooks/             # React hooks
```

**Key patterns:** Event-driven, plugin model, streaming-first

---

### ClassBuild (15-20k LOC)

```
src/
├── pages/             # SetupPage, SyllabusPage, etc.
├── prompts/           # 12 prompt builders
├── services/          # API calls
├── store/             # Zustand state
├── components/        # React components
└── themes/            # 6 chapter themes

scripts/
├── generate-course.ts # CLI driver
└── lib/               # Export helpers
```

**Key patterns:** Pipeline stages, prompt builders, multi-format export

---

## 6. Extensibility

### DeepTutor
- **MCP Servers:** External tool registry
- **Skills:** Custom teaching personas
- **Channels:** Custom chat protocols
- **Prompt overrides:** Per-capability customization

### ClassBuild
- **Prompt Builders:** Reusable library for other projects
- **Theme System:** Custom chapter themes
- **Export Formats:** Extend scripts/
- **CLI Flags:** Batch generation parameters

---

## 7. Deployment & Operations

### DeepTutor
- **Local:** `pip install deeptutor` + `deeptutor start`
- **Docker:** Self-contained container
- **Source:** Dev mode with hot reload
- **CLI-only:** Terminal-driven, no Web UI
- **Multi-user:** Optional auth + per-user isolation

### ClassBuild
- **Browser:** Visit classbuild.ai or self-host
- **Local:** `npm run dev`
- **CLI:** `npx tsx scripts/generate-course.ts` (batch)
- **No backend:** Browser-native, BYOK

---

## 8. Security & Privacy

### DeepTutor
- **Self-hosted:** Data stays on your machine/server
- **Multi-user:** API keys admin-only, users see redacted settings
- **Auth:** Optional JWT + bcrypt
- **Audit:** Every action logged

### ClassBuild
- **Zero-knowledge:** API keys never leave the browser
- **No backend:** No server logs of API calls
- **Privacy-first:** No analytics/telemetry
- **LocalStorage:** No persistent backend

---

## 9. Strengths & Weaknesses

### DeepTutor Strengths
✅ Persistent, multi-modal learning environment  
✅ Knowledge management (versioned RAG)  
✅ Autonomous agents (TutorBot)  
✅ Multi-user ready  
✅ Multi-provider LLM support  
✅ Extensive CLI  
✅ Extensible (MCP, skills, channels)  

### DeepTutor Weaknesses
❌ Complex deployment  
❌ Learning science implicit  
❌ No SCORM/LMS export  
❌ Stateful (requires backend)  

---

### ClassBuild Strengths
✅ Explicit learning science (5 principles)  
✅ One-click course generation  
✅ Full-featured exports (PowerPoint, SCORM, HTML)  
✅ Lightweight (no backend)  
✅ Privacy-first (BYOK)  
✅ Modular prompts (reusable)  
✅ Simple to use  

### ClassBuild Weaknesses
❌ Single-use workflow  
❌ No persistence  
❌ No multi-user  
❌ Limited customization  
❌ No RAG  
❌ No agents  

---

## 10. Integration Scenarios

### Scenario 1: Enterprise Learning Platform
- **ClassBuild:** Generate base courses (CLI)
- **DeepTutor:** Host persistent tutoring + KB
- **Flow:** ClassBuild SCORM → LMS + DeepTutor KB

### Scenario 2: Content Creator
- **ClassBuild:** Rapid course drafting
- **DeepTutor:** Interactive development & Book Engine
- **Export:** SCORM to LMS

### Scenario 3: Autonomous Tutoring
- **DeepTutor:** TutorBot agents with KB
- **Multi-channel:** Discord, Slack, Telegram
- **Memory:** Track student progress

### Scenario 4: Self-Paced Learning
- **ClassBuild:** Generate complete course
- **Deploy:** Static HTML viewer (GitHub Pages, Vercel)
- **No backend needed**

---

## 11. When to Use Which

| Use Case | Tool | Why |
|----------|------|-----|
| Rapid course draft | ClassBuild | One-click generation |
| Ongoing tutoring | DeepTutor | Persistent, agentic |
| Multi-user institution | DeepTutor | Auth, grants, isolation |
| Private corporate KB | DeepTutor | RAG, versioning |
| Podcast/audiobook | ClassBuild | ElevenLabs integration |
| Live classroom | Both | ClassBuild slides + DeepTutor interaction |
| LMS integration | ClassBuild export | SCORM packaging |
| Autonomous study | DeepTutor | TutorBot heartbeats |
| Learning science | ClassBuild | 5 principles explicit |
| Customizable curriculum | DeepTutor | Skills, MCP, extensibility |

---

## 12. Technology Stack

| Layer | DeepTutor | ClassBuild |
|-------|-----------|-----------|
| **Backend** | FastAPI (Python 3.11+) | None (browser-native) |
| **Frontend** | React 19 + Next.js 16 | React 19 + Vite 7 |
| **Database** | SQLite | Browser localStorage |
| **State** | Context + custom | Zustand |
| **RAG** | LlamaIndex | ❌ |
| **LLM** | 15+ providers | 3 (Claude, OpenAI, ElevenLabs) |
| **Styling** | Tailwind CSS | Tailwind CSS 4 |
| **CLI** | Typer | tsx (Node.js) |

---

## 13. Open Questions

### DeepTutor
1. How to surface learning science as explicitly as ClassBuild?
2. Can TutorBot be deployed without technical setup?
3. Integration with major LMS (Canvas, Blackboard, Moodle)?

### ClassBuild
1. Can stateful course editing be added (persist across sessions)?
2. Multi-user institutional deployments?
3. LMS integration for enrollment tracking?

### Convergence
1. Could ClassBuild's prompts power DeepTutor's Book Engine?
2. Could DeepTutor's memory track progress in ClassBuild courses?
3. Joint certification: ClassBuild design + DeepTutor deployment?

---

## Conclusion

**DeepTutor** and **ClassBuild** are complementary:

- **DeepTutor:** Persistent, agentic tutoring environment
- **ClassBuild:** Efficient, learning-science-grounded course generation

**Best outcome:** Use ClassBuild for rapid course drafting, import into DeepTutor for ongoing instruction. Institutions deploy DeepTutor with TutorBot agents. Designers export ClassBuild outputs (SCORM) for LMS.

---

**Analysis Date:** June 6, 2026  
**Repositories:**
- HKUDS/DeepTutor (20k+ GitHub stars, active)
- jtangen/classbuild (focused, MIT licensed)
