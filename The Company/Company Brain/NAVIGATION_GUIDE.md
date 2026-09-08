# Company Brain Navigation Guide

[[STARTHERE]] | [[REALITY]] | [[00_RESPECT/RESPECT|RESPECT]] | [[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[INDEX-DOMAINS-COMPLETE]] | [[00-CONSTITUTION]]

**For:** New users, team members, developers integrating with Company Brain  
**Goal:** Learn Company Brain architecture in ~30 minutes; navigate effectively  
**Updated:** 2026-09-06

---

## Reading Flow: Fast Path (5 minutes)

1. **Start here:** [[STARTHERE.md]] (master orientation legend, reality check, priorities)
2. **Review ethical & respect rules:** [[00_RESPECT/RESPECT.md]] (the 20 core rules of respect)
3. **Understand architecture:** [[Company Brain/README]] (architecture diagram, 50 domains overview)
4. **Understand structure:** [[INDEX.md]] (see all 50 domains + 35 sectors at a glance)
5. **Learn to navigate:** This file (reading flow + key concepts)
6. **Dive into one domain:** Pick a domain relevant to your work (e.g., [[14-CAPABILITIES]], [[_MEMORY/MEMORY-OS]])
7. **Find what you need:** Use INDEX.md to jump directly to relevant sections

**You now understand:** Core architecture, domain layout, how to navigate.

---

## Reading Flow: Complete Path (30 minutes)

### Layer 1: Vision & Structure (5 min)

| File | What | Why |
|------|------|-----|
| [[00-CONSTITUTION]] | Mission, principles, governance | "Why does Company Brain exist?" |
| [[Company Brain/README]] | Architecture diagram, 50 domains | "What are the main pieces?" |
| [[INDEX.md]] | Full navigation index | "Where is everything?" |

### Layer 2: Organization (10 min)

| File | What | Why |
|------|------|-----|
| [[01-IDENTITY]] | Company structure, ventures | "How is company organized?" |
| [[SECTOR_INDEX.md]] | 36-sector taxonomy | "What sectors do we operate in?" |
| [[23-VENTURES]] | Venture registry | "Where are the 500 ventures?" |

### Layer 3: Intelligence Engine (10 min)

| File | What | Why |
|------|------|-----|
| [[_ONTOLOGY/OBJECT_TYPES.yaml]] | 60 entity types | "What kinds of things exist?" |
| [[_ONTOLOGY/RELATIONSHIPS.yaml]] | 25 relationship types | "How do things connect?" |
| [[_ONTOLOGY/EVIDENCE_STANDARDS.md]] | Proof & confidence | "Why do we trust claims?" |
| [[_ONTOLOGY/STATUS_LIFECYCLE.md]] | State machine | "How do things mature?" |
| [[14-CAPABILITIES]] | Capability registry | "What can company do?" |
| [[16-AGENTS]] | Agent registry | "What agents operate system?" |
| [[15-SKILLS]] | Skill library | "How are procedures documented?" |

### Layer 4: Execution & Outcomes (5 min)

| File | What | Why |
|------|------|-----|
| [[22-EXECUTION]] | Jobs, tasks, transactions | "How does work get done?" |
| [[_PIPELINES/execution/EXECUTION_TRACKING.md]] | Loop execution standard | "How do we track what happened?" |
| [[43-OUTCOMES]] | Recorded outcomes & metrics | "What results did we achieve?" |

### Layer 5: Learning & Evolution (5 min)

| File | What | Why |
|------|------|-----|
| [[44-LEARNING]] | Lessons extracted | "What did we learn?" |
| [[40-METRICS]] | KPIs, SLIs, SLOs | "How do we measure success?" |
| [[45-EVOLUTION]] | Optimization & improvement | "How does CB get better?" |

**You now understand:** Complete architecture, ontology, execution, learning.

---

## Quick Reference: "Where is X?"

### Looking for...

**A capability?**
1. Go to [[14-CAPABILITIES]]
2. Find by name or ID (CAP-000247)
3. See definition, status, dependencies

**A venture?**
1. Go to [[SECTOR_INDEX.md]]
2. Find sector, click Ventures
3. Find venture by name (VEN-000001)

**A sector?**
1. Go to [[SECTOR_INDEX.md]]
2. Find sector ID (SEC-013)
3. See OpCo, industries, ventures

**An agent?**
1. Go to [[16-AGENTS]]
2. Find by role or ID (AGT-000042)
3. See responsibilities, status

**A decision?**
1. Go to [[50-MASTER-CONTROL]]
2. Find decision (DEC-001567)
3. See evidence, confidence, impact

**A domain?**
1. Go to [[INDEX.md]]
2. Find domain (14-CAPABILITIES)
3. Explore organizational layer

**An execution?**
1. Go to [[22-EXECUTION]]
2. Find loop/agent (LOP-000042)
3. See latest runs, success rate

---

## Key Concepts Glossary

### Organizational

| Term | Definition | Example |
|------|-----------|---------|
| **Venture (VEN)** | Business unit | VEN-000042 |
| **Sector** | Industry vertical (36 total) | SEC-013 Hospitality |
| **OpCo** | Operating company | OpCo for Hospitality |
| **Domain** | Org layer (50 total) | 14-CAPABILITIES |

### Intelligence

| Term | Definition | Example |
|------|-----------|---------|
| **Capability (CAP)** | Repeatable capability | CAP-000247 Lead Scoring |
| **Skill (SKL)** | Executable procedure | SKL-000089 Build Dashboard |
| **Agent (AGT)** | Autonomous specialist | AGT-000042 Lead Gen Agent |
| **Loop (LOP)** | Recurring automation | LOP-000001 Weekly Scoring |

### Execution & Evidence

| Term | Definition | Example |
|------|-----------|---------|
| **Decision (DEC)** | Recorded choice with rationale | DEC-001567 Consolidate TC |
| **Outcome (OUT)** | Measured result | OUT-001234 15% revenue growth |
| **Execution (EXC)** | Recording of a loop/agent run | EXC-000847 Loop run, 483 items |
| **Evidence** | Data proving claim | DST-000087 supporting confidence |

### Status Lifecycle

| Status | Meaning |
|--------|---------|
| **DOCUMENTED** | Concept defined, not implemented |
| **REGISTERED** | In system with unique ID |
| **CONFIGURED** | Set up & tested, not production |
| **AVAILABLE** | Ready to deploy |
| **CONNECTED** | Deployed & receiving traffic |
| **TESTED** | 2+ weeks stable data |
| **ACTIVE** | SLA/SLO published |
| **TRUSTED** | Met SLA for 90+ days |

### Relationships (How things connect)

| Relationship | Meaning |
|--------------|---------|
| **USES** | Agent/Skill uses Tool/Capability |
| **DEPENDS_ON** | Service depends on another |
| **IMPLEMENTS** | Code implements Capability |
| **EXECUTES** | Agent/Loop executes Workflow |
| **PRODUCES** | Capability produces Outcome |
| **MEASURED_BY** | Entity measured by Metric |
| **EVIDENCED_BY** | Decision evidenced by Data |
| **BELONGS_TO** | Entity belongs to Organization |

---

## Workflow: Typical User Journeys

### Journey 1: New Venture Onboarding

```
1. Go to SECTOR_INDEX.md
2. Find sector (SEC-013 Hospitality)
3. Click Ventures → add venture
4. System assigns to sector → record execution
5. Assign to OpCo, domain, KPIs
6. Wire relationships (industry, market, team)
7. Loop learns: new venture added
```

### Journey 2: "Why Was This Decision Made?"

```
1. Find decision in 50-MASTER-CONTROL
2. Click Decision (DEC-001567)
3. See confidence (0.92), evidence, who decided
4. Click evidence links → read supporting data
5. Verify confidence > 0.85 (trusted)
6. See decision date, impact, outcome
7. Loop learns: was decision right?
```

### Journey 3: "Debug Failing Loop"

```
1. Go to 22-EXECUTION
2. Find Loop (LOP-000042)
3. Click Execution (EXC-000847)
4. See inputs, outputs, anomalies, errors
5. Check dependencies (all TRUSTED?)
6. Review anomalies (thresholds?)
7. Adjust & re-run
8. Record lesson in 44-LEARNING
```

### Journey 4: "Find Agents Using Capability CAP-000247"

**Method 1 (Wiki):**
```
1. Go to 14-CAPABILITIES
2. Find CAP-000247
3. Click "Used by" → see agents
```

**Method 2 (Neo4j):**
```
MATCH (a:Agent)-[:USES]->(c:Capability {ref_id: "CAP-000247"})
RETURN a.name, a.autonomy_level
```

---

## Learning Paths by Role

### **Executive (5 min)**
→ README.md → 50-MASTER-CONTROL → 40-METRICS → 43-OUTCOMES  
**Knows:** Current state, KPIs, outcomes

### **Product Manager (15 min)**
→ README.md → INDEX.md → 14-CAPABILITIES → 23-VENTURES → 22-EXECUTION  
**Knows:** What we can do, how ventures organized, execution

### **Engineer (30 min)**
→ README.md → _ONTOLOGY/ → 16-AGENTS → 15-SKILLS → _PIPELINES/execution/  
**Knows:** Architecture, ontology, execution tracking

### **Data Analyst (20 min)**
→ README.md → 04-DATA → 40-METRICS → 43-OUTCOMES → 44-LEARNING  
**Knows:** Data layer, metrics, outcomes, lessons

### **Sector Lead (20 min)**
→ SECTOR_INDEX.md → SEC-XXX → Ventures SEC-XXX → Capabilities SEC-XXX  
**Knows:** Sector structure, ventures, capabilities, agents

---

## Staying Current

**Weekly:**
- Check 50-MASTER-CONTROL for new decisions
- Review 43-OUTCOMES for results
- Scan 44-LEARNING for lessons

**Monthly:**
- Audit sector status via SECTOR_INDEX.md
- Review loop executions via 22-EXECUTION
- Check metric trends via 40-METRICS

**Quarterly:**
- Review one domain per week (50 weeks total)
- Validate all control points active
- Update OBJECT_TYPES.yaml if new types needed

---

## Troubleshooting

**"Can't find what I'm looking for"**  
→ Use INDEX.md, search by keyword

**"Don't understand a term"**  
→ Check Glossary above or GLOSSARY.md

**"Where's the venture data?"**  
→ SECTOR_INDEX.md → find sector → Ventures link

**"How do I know if something is reliable?"**  
→ Check status (TRUSTED is good) or confidence score (0.85+ is good)

**"How do I add something new?"**  
→ Check QUICK_START.md for instructions

**"When was this last updated?"**  
→ Check execution records in 22-EXECUTION or file's "Last Updated" date

---

## Next Steps

1. **Start:** Read [[Company Brain/README]] (5 min)
2. **Navigate:** Use [[INDEX.md]] (5 min)
3. **Dive deep:** Pick relevant domain/sector (15 min)
4. **Get hands-on:** Follow a user journey (varies)
5. **Stay synced:** Check [[50-MASTER-CONTROL]] weekly

**Questions?** Check QUICK_START.md or reach out to domain owner.

**Last Updated:** 2026-09-01
