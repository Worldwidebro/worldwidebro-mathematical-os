# LightRAG evaluation set (20 questions)

**Purpose:** Score grounded answers after each weekly Knowledge Ops loop.  
**Pass:** Answer names the correct venture/repo/sector and cites an ingest source (vault note, alignment CSV, registry, or graph).  
**Run:** `python3 WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/run_knowledge_ops_scorecard.py --rag-eval`

| # | Question | Expected in answer (minimum) | Primary layer |
|---|----------|------------------------------|---------------|
| 1 | What is the owned GitHub repo for the HRMS enterprise venture? | `ent-venture-001-hrms` or equivalent slug | CSV / 712 |
| 2 | Which sector is Civilization OS classified under? | `ai` or platform / OS | Classification |
| 3 | What repo powers the IZA OS RAG System venture? | `iza-os-rag-system` | CSV + bridge |
| 4 | Name three capabilities linked to Tax Intelligence Platform via starred repos. | Any of FinceptTerminal, LightRAG, database-optimizer family | Starred / deps |
| 5 | What are the required repos for HVAC Operations? | `con-012-hvac-services`, mobile/dispatch tooling | `ventures_dependencies.json` |
| 6 | What is the owned repo for Electrical Operations and how does it relate to HVAC dispatch? | `lt-009-hvac-technician-dispatch` | CSV |
| 7 | Which venture owns `the-office` and what is it for? | The Office venture, CRM/ops surface | CSV |
| 8 | How many GitHub owned repos are in the registry? | ~853 (±5 after export) | `github_owned.csv` |
| 9 | How many starred repos are tracked for portfolio compounding? | ~700 | `github_starred.csv` |
| 10 | What is the difference between the 629 classification ventures and the 712 master slugs? | 629 = UUID operating set; 712 includes slug-only/planned | Alignment docs |
| 11 | Where does LightRAG ingest alignment data from? | `the-office-export.csv` or combined alignment CSV via `--source=alignment` | `iza-os-rag-system/src/ingest.py` |
| 12 | What Graphify merge script builds the org view with owned + starred hubs? | `merge_github_obsidian_into_graphify.py` | `worldwidebro-vault/CLAUDE.md` |
| 13 | Which MCP should answer “who calls this function” in the open codebase? | SocratiCode | `VENTURE-BRAIN-LAYERS.md` |
| 14 | What is the CEO command center path for financial KPIs in WORLDWIDEBRO-OS? | `01_CEO_COMMAND_CENTER/KPIs/` | Filesystem |
| 15 | Name the execution map for ops-venture-001-hvac. | `ops-venture-001-hvac/EXECUTION_MAP.md` | WORLDWIDEBRO-OS |
| 16 | What starred repo is commonly tied to agent reach for platform ventures? | `Agent-Reach` (or airweave) | Dependencies |
| 17 | What is CON-010 Subcontractor Payments’ owned repo? | `iza-os-operations-security-bot` | Alignment row |
| 18 | Which document is the agent operations entry point before inventing new MCP lists? | `venture-hub/docs/AGENTIC-OPERATIONS-INDEX.md` | Docs |
| 19 | What weekly loop refreshes GitHub registries before alignment? | `hub:github-export` → align script → ingest | `COMPOUNDING_PLAYBOOK.md` |
| 20 | For venture `499604b7-08f2-40fb-b9e7-3af3fb45a86c`, what is the venture name and top required repo? | IZA OS RAG System + `iza-os-rag-system` | Alignment JSON |

## Scoring

- **Per question:** 1 = grounded correct, 0.5 = partially correct / no citation, 0 = wrong or hallucinated  
- **LightRAG component (25% of Knowledge Ops Score):** `(sum / 20) * 100`, target ≥ 80%

Record results in `knowledge-ops-scorecard-YYYY-MM-DD.csv` (column `rag_q1` … `rag_q20` or single `rag_eval_pct`).
