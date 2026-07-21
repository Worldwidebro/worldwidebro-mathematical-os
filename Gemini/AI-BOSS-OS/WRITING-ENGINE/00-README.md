# Writing Engine (Narrative Engine)

Welcome to the **AI Boss OS Writing Engine**. This engine serves as the narrative nervous system of the 712-venture ecosystem. It organizes all copy, business writing, content creation, and agentic workflows into a standardized operational capability.

## Folder Directory

- **00-README.md**: This index and overview.
- **00-SYSTEM-DESIGN.md**: Integrations with the Agent Registry, Neo4j, and execution gateways.
- **01-FOUNDATION/**: Corporate principles, brand voice guidelines, style rules, and psychology.
- **02-COPYWRITING/**: Sales copies, email sequences, ad guidelines, landing pages, and CTAs.
- **03-CONTENT/**: Templates and guidelines for organic/social content (LinkedIn, Twitter, TikTok, YouTube).
- **04-BUSINESS-WRITING/**: Formal internal documents: Business Plans, PRDs, SOPs, proposals.
- **05-VENTURE-WRITING/**: Shared multi-tenancy layer. New ventures inherit the template and can specify overrides.
- **06-KNOWLEDGE-BASE/**: Documented lessons, mental models, and performance logs syncable with Neo4j.
- **07-AI-WRITER-AGENTS/**: Configuration and prompt files for the AI writer agents (Copywriter, Editor, SEO, etc.).
- **08-TEMPLATES/**: Reusable snippets and skeletons for emails, proposals, and posts.
- **09-ARCHIVE/**: Old campaigns, historical experiments, and previous drafts.
- **10-AUDIO-VISUAL/**: Scripts and prompt layouts for video, image generation, and audio synthesis.
- **11-STRATEGY-DOCS/**: Content calendar scheduler targets and keyword maps.
- **12-APPROVAL-WORKFLOWS/**: Regulatory checklists, compliance reviews, and executive sign-off logic.
- **13-METRICS-ANALYTICS/**: Live conversion dashboards and writer agent attribution scores.

## Multi-Tenancy Strategy

Each venture created by the Venture Factory inherits the writing engine defaults. 
Overrides should be placed in `VENTURES/[venture-id]/WRITING/` (such as `BRAND-VOICE.md`), which will be picked up by the runner instead of the global foundation file.
