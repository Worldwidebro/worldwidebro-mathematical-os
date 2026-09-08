# DESIGN — Visual Design Principles & Technical Graphics

> **Canonical Document ID:** `DOC-DSN-CAM-001`  
> **Authority:** Design Architecture (CP-026)  
> **Status:** ACTIVE SPECIFICATION  
> **Canonical Aliases:** [[CAMPAIGNS/VISUALS.md]], [[CAMPAIGNS/IMAGERY.md]], [[CAMPAIGNS/GRAPHICS.md]]

---

## 1. Visual Token System

- **Background:** Jet Black (`#0A0A0A`) / Carbon Surface (`#141414`).
- **Accent Primary:** Electric Emerald (`#10B981`) for savings metrics; Pure White (`#FFFFFF`) for typography.
- **Typography:** JetBrains Mono for code/metrics; Inter for executive prose.
- **Charts:** High-contrast bar charts showing before/after token spend.

---

## 2. AST Knowledge Graph Visual Architecture

```mermaid
graph LR
    subgraph BRUTE SCAN CONTEXT TAX
        F1[File 1: 20k tokens] --> LLM[Cloud LLM]
        F2[File 2: 30k tokens] --> LLM
        F3[Build Log: 40k tokens] --> LLM
    end
    
    subgraph WORLDWIDEBRO AST GRAPH
        G[Neo4j AST Relational Subgraph: 4.2k tokens] --> LOCAL[Local MLX Reasoning Engine]
    end
```

---

## 3. Master Links

- Creative Master: [[CAMPAIGNS/CREATIVE]]
- Assets: [[CAMPAIGNS/CREATIVE-ASSETS]]
