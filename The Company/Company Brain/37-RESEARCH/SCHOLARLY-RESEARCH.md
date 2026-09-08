---
id: RES-SCHOL-001
title: "SCHOLARLY-RESEARCH — Academic Citation Graph & Research Synthesis"
tags: [research, academic, arxiv, citations, papers, knowledge]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[37-RESEARCH/README|37-RESEARCH]] | [[09-KNOWLEDGE/Awesome-Lists|Awesome Lists]] | [[42-EVALUATION/README|Evaluation]]

# SCHOLARLY-RESEARCH.md — Unified Scientific & Academic Intelligence

> **Authority:** Academic & Technical Knowledge Control Plane (CP-013)  
> **Integrated Sources:** arXiv (`SRC-ARXIV`), OpenAlex (`SRC-OPENALEX`), Semantic Scholar (`SRC-SEMANTIC-SCHOLAR`), Hugging Face (`SRC-HUGGINGFACE`), Papers with Code  
> **Schema Authority:** DOI & OpenAlex Persistent Identifier Graph

---

## 1. Multi-Source Scholarly Normalization

A paper cannot remain an isolated PDF link. Every ingested academic asset is normalized into a canonical entity schema:

```yaml
paper_id: "PAP-2026-0042"
doi: "10.48550/arXiv.2603.03126"
arxiv_id: "2603.03126"
openalex_id: "W4392817291"
semantic_scholar_id: "a89bc42..."
title: "Unified Scholarly Ontologies for Autonomous Agent Decision Systems"
published_date: "2026-03-01"

# Provenance & Truth Classification (Governed by REALITY.md)
truth_classification: "PEER_REVIEWED" 
# Allowed: PREPRINT | PEER_REVIEWED | PUBLISHED | REPLICATED | RETRACTED | UNVERIFIED
peer_reviewed: true
journal_or_venue: "NeurIPS 2026"
retracted: false
replication_status: "REPLICATED_INDEPENDENTLY"

# Entity Graph Links
authors:
  - name: "Dr. Elena Rostova"
    openalex_author_id: "A5019284"
    affiliation: "Stanford HAI"
funders:
  - name: "National Science Foundation"
    openalex_funder_id: "F4320321"
    award_id: "NSF-IIS-2401928"

# Actionable Tech Assets
code_repository: "https://github.com/example/scholarly-graph"
model_weights: "https://huggingface.co/org/scholarly-model-7b"
benchmark_dataset: "https://huggingface.co/datasets/org/scholarly-bench"
benchmarks_evaluated:
  - benchmark_name: "AgentBench-v3"
    score: 84.2
    baseline_delta: "+6.8%"

# Company Brain Application
relevant_ventures: ["OmniRoute", "Company Brain"]
capabilities_advanced: ["CAP-KNOWLEDGE-GRAPH", "CAP-AI-INFERENCE"]
```

---

## 2. Source Hierarchy & Cross-Verification

```text
               arXiv (Fast Preprints / Raw Signals)
                         │
                         ▼
        Semantic Scholar (Citation Graph & TLDRs)
                         │
                         ▼
           OpenAlex (Institutional & Funder Graph)
                         │
                         ▼
        Papers with Code & Hugging Face (Code Reality)
                         │
                         ▼
           CANONICAL PAPER NODE IN NEO4J
```

---

## 3. Neo4j Cypher Schema for Scholarly Research

Every paper ingested into Mac Studio's Neo4j (`civos_neo4j:7687`) creates the following relationship subgraph:
```cypher
(:Paper {doi: $doi, title: $title, truth_status: $truth_status})
  -[:AUTHORED_BY]-> (:Author {name: $author_name})
  -[:AFFILIATED_WITH]-> (:Institution {name: $institution})
  -[:FUNDED_BY]-> (:Funder {name: $funder})
  -[:IMPLEMENTED_IN]-> (:Repository {github_url: $github_url})
  -[:RELEASES_MODEL]-> (:AIModel {hf_id: $hf_id})
  -[:ENABLES_CAPABILITY]-> (:Capability {id: $cap_id})
  -[:OPPORTUNITY_FOR]-> (:Venture {id: $ven_id})
```

---

## 4. Citation Inflation & Retraction Protection
- **Retraction Watchlist:** The ingestion pipeline automatically flags any paper flagged as `RETRACTED` in Crossref or OpenAlex.
- **Influential Citation Ratio:** Raw citation counts are discounted. Only citations categorized as `Methodological Reliance` or `Result Confirmation` by Semantic Scholar are weighted in opportunity scoring.

---

## Connected Subsystems
- **Research OS:** [[37-RESEARCH/RESEARCH-OS]]
- **Source Registry:** [[37-RESEARCH/SOURCE-REGISTRY]]
- **Awesome Lists & Curated Repos:** [[09-KNOWLEDGE/Awesome-Lists]]
- **Evaluation Domain:** [[42-EVALUATION/README]]
