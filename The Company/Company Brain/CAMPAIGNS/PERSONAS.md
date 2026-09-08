# PERSONAS — Detailed Buyer & Technical Persona Blueprints

> **Canonical Document ID:** `DOC-PER-CAM-001`  
> **Authority:** Commercial Strategy (CP-006 / CP-026)  
> **Status:** ACTIVE SPECIFICATION  
> **Canonical Alias:** [[CAMPAIGNS/BUYER-PERSONAS.md]]

---

## 1. Persona Blueprint: The VP of Engineering (`PER-001`)

```text
Title: VP of Engineering / Head of Platform / Director of Infrastructure
Company Size: 15–60 engineers
Reports To: CTO / CEO
Core Mandate: Developer velocity, cloud infrastructure budget predictability, platform uptime
Acute Fear: Enduring an executive board review where cloud LLM bills are scrutinized as wasteful
```

- **Current Mindset:** "Every engineer wants Cursor and Claude Code. Velocity is up, but our API bill is surging past $18,000/month. I don't have time to build custom caching."
- **Objections:** "Will this disrupt developer workflows? Do my engineers have to learn a new tool?"
- **Winning Argument:** "Zero workflow changes for developers. We optimize the routing and compression layers behind the scenes, and feed exact AST subgraphs so responses are faster and 60% cheaper."

---

## 2. Persona Blueprint: The CTO / Technical Founder (`PER-002`)

```text
Title: Chief Technology Officer / Technical Co-Founder
Company Size: 10–40 engineers
Reports To: Board of Directors / Investors
Core Mandate: Architectural integrity, proprietary IP protection, enterprise valuation
Acute Fear: Codebase IP leaking to OpenAI/Anthropic or being used to train third-party foundation models
```

- **Current Mindset:** "We want to leverage the latest reasoning models, but our compliance team is terrified of third-party API exposure."
- **Objections:** "Local models aren't smart enough to write enterprise code."
- **Winning Argument:** "Modern quantized reasoning models (Qwen 2.5 Coder 32B, DeepSeek R1 distilled) running on unified-memory Apple Silicon rival GPT-4o on real coding benchmarks at zero token cost."

---

## 3. Master Links

- Master OS: [[CAMPAIGNS/CAMPAIGN-OS]]
- ICP: [[CAMPAIGNS/ICP]]
- Objections Handling: [[CAMPAIGNS/OBJECTION-HANDLING]]
- Commercial Outreach: [[COMMERCIAL/OUTREACH/OUTREACH-001-TARGET-PROSPECTS]]
