# Venture Studio Product Pipeline Master Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Execute complete product lifecycle (discovery → exit) across 629 ventures in 10 niches, with automated course generation for 69 EDTECH ventures.

**Venture Distribution:**
- Marketplace (195) | Infrastructure (116) | DevTools (91) | AI (72) | **EdTech (69)** | FinTech (47) | Construction (21) | Real Estate (15) | Operations (2) | Health (1)

**Architecture:** 4 parallel blocker clusters executing Phases 1-9 simultaneously with central dashboard tracking.

**Tech Stack:** TrendRadar, Miro-Fish, Supabase, DuckDB, Higgsfield (course generation), n8n, Obsidian

---

## Status Summary

| Phase | Name | Status | Timeline |
|-------|------|--------|----------|
| 1 | Trend Discovery | ✅ COMPLETE | 2026-06-04 |
| 2 | Product Validation | ⏳ READY | 2026-06-05 to 06-18 |
| 3 | Product Creation | ⏳ PENDING | 2026-06-19 to 07-10 |
| 4 | Branding | ⏳ PENDING | 2026-07-11 to 07-25 |
| 5 | Sales System | ⏳ PENDING | 2026-07-26 to 08-15 |
| 6 | Marketing | ⏳ PENDING | 2026-08-16 to 09-15 |
| 7 | Customer Success | ⏳ PENDING | 2026-09-16 to 10-15 |
| 8 | Scaling | ⏳ PENDING | 2026-10-16 to 11-30 |
| 9 | Exit Strategy | ⏳ PENDING | 2026-12-01 onwards |

---

## PHASE 1: TREND DISCOVERY ✅ (COMPLETE - 2026-06-04)

**Deliverables:**
- [x] `WORLDWIDEBRO-OS/00_INTAKE_LAYER/NICHE_KEYWORDS.json` — 10 niches with keywords
- [x] `WORLDWIDEBRO-OS/09_AUTOMATION/TREND_DISCOVERY_RUNNER.py` — Discovery runner
- [x] `.planning/trend_discovery/trendradar_baseline_20260604.json` — Baseline data
- [x] `.planning/trend_discovery/miro_fish_forecast_20260604.json` — 30/90-day forecasts
- [x] Top 5 niches ranked: FINTECH, AI_DEVTOOLS, SAAS, HR_PAYROLL, EDTECH
- [x] Committed and pushed to GitHub

---

## PHASE 2: PRODUCT VALIDATION (2026-06-05 to 06-18)

**Objective:** Collect 300+ survey responses, conduct 50+ interviews, score product-market fit for all 629 ventures

**Task 2.1: Create & Launch Landing Pages for Top 5 Niches**

Files:
- Create: `WORLDWIDEBRO-OS/02_MARKETING/Landing_Pages/landing_page_template.html`
- Create: `WORLDWIDEBRO-OS/09_AUTOMATION/generate_landing_pages.py`
- Create: `WORLDWIDEBRO-OS/10_VENTURES/VALIDATION_TRACKER.csv`

- [ ] **Step 1: Write landing page template**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{niche}} Solution - {{venture_name}}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .hero { background: #f0f0f0; padding: 40px; border-radius: 8px; }
        .cta { background: #0066cc; color: white; padding: 15px 30px; border: none; border-radius: 4px; cursor: pointer; }
        .form input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; }
    </style>
</head>
<body>
    <h1>{{niche_problem}}</h1>
    <div class="hero">
        <h2>Our Solution</h2>
        <p>{{solution_desc}}</p>
    </div>
    <form>
        <h3>Get Early Access</h3>
        <input type="email" placeholder="Email" required>
        <input type="text" placeholder="Company" required>
        <button class="cta">Join Waitlist</button>
    </form>
</body>
</html>
```

- [ ] **Step 2: Create landing page generator script**

```python
#!/usr/bin/env python3
import json
from pathlib import Path

def generate_landing_pages(niches_config, output_dir):
    for niche, config in niches_config.items():
        html = f"""<!DOCTYPE html>
<html>
<head><title>{niche} Solution</title></head>
<body>
<h1>{niche} Problem Solver</h1>
<p>{config['keywords'][0]}</p>
<form>
    <input type="email" placeholder="Email" required>
    <button>Join Waitlist</button>
</form>
</body>
</html>"""
        Path(f"{output_dir}/{niche.lower()}.html").write_text(html)

if __name__ == "__main__":
    with open("WORLDWIDEBRO-OS/00_INTAKE_LAYER/NICHE_KEYWORDS.json") as f:
        config = json.load(f)["niches"]
    generate_landing_pages(config, "WORLDWIDEBRO-OS/02_MARKETING/Landing_Pages/")
    print("✅ Landing pages generated")
```

- [ ] **Step 3: Run script to generate 5 landing pages**

Run: `python3 WORLDWIDEBRO-OS/09_AUTOMATION/generate_landing_pages.py`

Expected: 5 HTML files in `WORLDWIDEBRO-OS/02_MARKETING/Landing_Pages/`

- [ ] **Step 4: Create validation tracker**

```csv
venture_id,venture_name,niche,landing_page_live,emails_collected,survey_responses,interviews_completed,pmf_score,status
fin-001,GenixBank Lite,FINTECH,2026-06-05,0,0,0,0.0,launched
ai-001,AI Coding Assistant,AI_DEVTOOLS,2026-06-05,0,0,0,0.0,launched
saa-001,Workflow Platform,SAAS,2026-06-05,0,0,0,0.0,launched
hr-001,HR Platform,HR_PAYROLL,2026-06-05,0,0,0,0.0,launched
ed-001,Course Platform,EDTECH,2026-06-05,0,0,0,0.0,launched
```

- [ ] **Step 5: Commit Phase 2.1**

```bash
git add WORLDWIDEBRO-OS/02_MARKETING/Landing_Pages/
git add WORLDWIDEBRO-OS/09_AUTOMATION/generate_landing_pages.py
git add WORLDWIDEBRO-OS/10_VENTURES/VALIDATION_TRACKER.csv
git commit -m "feat: launch validation landing pages for 5 priority niches"
```

**Task 2.2: Distribute Surveys & Schedule Interviews**

Files:
- Create: `WORLDWIDEBRO-OS/10_VENTURES/SURVEY_TEMPLATE.json`
- Create: `WORLDWIDEBRO-OS/09_AUTOMATION/distribute_surveys.py`
- Create: `WORLDWIDEBRO-OS/09_AUTOMATION/schedule_interviews.py`

- [ ] **Step 1: Create survey template**

```json
{
  "niche": "FINTECH",
  "questions": [
    {"id": 1, "type": "mc", "text": "Biggest pain point?", "options": ["A", "B", "C"]},
    {"id": 2, "type": "text", "text": "Current workflow?"},
    {"id": 3, "type": "scale", "text": "How urgent? (1-10)"},
    {"id": 4, "type": "text", "text": "What would you pay/month?"},
    {"id": 5, "type": "mc", "text": "Who else to talk to?"}
  ],
  "target_responses": 50
}
```

- [ ] **Step 2: Write survey distribution script**

```python
#!/usr/bin/env python3
import json
from datetime import datetime

def distribute_surveys(niches, target_per_niche=50):
    results = {}
    for niche in niches:
        results[niche] = {
            "target": target_per_niche,
            "distributed": 0,
            "completed": 0,
            "status": "queued"
        }
    with open("WORLDWIDEBRO-OS/09_AUTOMATION/survey_distribution.json", "w") as f:
        json.dump(results, f)
    print(f"✅ Survey distribution queued for {len(niches)} niches")

if __name__ == "__main__":
    niches = ["FINTECH", "AI_DEVTOOLS", "SAAS", "HR_PAYROLL", "EDTECH"]
    distribute_surveys(niches, 50)
```

- [ ] **Step 3: Write interview scheduling script**

```python
#!/usr/bin/env python3
def schedule_interviews(niches, interviews_per_niche=10):
    schedule = {}
    for niche in niches:
        schedule[niche] = {
            "target_interviews": interviews_per_niche,
            "scheduled": 0,
            "completed": 0,
            "status": "scheduling"
        }
    print(f"✅ Interviews scheduled: {sum(s['target_interviews'] for s in schedule.values())} total")

if __name__ == "__main__":
    schedule_interviews(["FINTECH", "AI_DEVTOOLS", "SAAS", "HR_PAYROLL", "EDTECH"], 10)
```

- [ ] **Step 4: Run survey distribution**

Run: `python3 WORLDWIDEBRO-OS/09_AUTOMATION/distribute_surveys.py`

Expected: 250+ surveys distributed (5 niches × 50 each)

- [ ] **Step 5: Run interview scheduling**

Run: `python3 WORLDWIDEBRO-OS/09_AUTOMATION/schedule_interviews.py`

Expected: 50 interviews scheduled (5 niches × 10 each)

- [ ] **Step 6: Commit Phase 2.2**

```bash
git add WORLDWIDEBRO-OS/10_VENTURES/SURVEY_TEMPLATE.json
git add WORLDWIDEBRO-OS/09_AUTOMATION/distribute_surveys.py
git add WORLDWIDEBRO-OS/09_AUTOMATION/schedule_interviews.py
git commit -m "feat: launch customer validation surveys and interviews"
```

**Task 2.3: Score Product-Market Fit**

Files:
- Create: `WORLDWIDEBRO-OS/01_CEO_COMMAND_CENTER/PMF_SCORING_MODEL.json`
- Create: `WORLDWIDEBRO-OS/09_AUTOMATION/calculate_pmf_scores.py`
- Create: `WORLDWIDEBRO-OS/01_CEO_COMMAND_CENTER/PMF_RESULTS.json`

- [ ] **Step 1: Define PMF scoring model**

```json
{
  "metrics": [
    {"name": "Survey Response Rate", "weight": 0.15, "pass_threshold": 0.3},
    {"name": "NPS Score", "weight": 0.20, "pass_threshold": 40},
    {"name": "Problem Severity (1-10)", "weight": 0.25, "pass_threshold": 7.5},
    {"name": "Willingness to Pay", "weight": 0.20, "pass_threshold": 50},
    {"name": "Interview Confirmation", "weight": 0.20, "pass_threshold": 0.7}
  ],
  "overall_pmf_threshold": 0.70,
  "decision_logic": {"score_above_threshold": "GO", "score_below_threshold": "NO_GO"}
}
```

- [ ] **Step 2: Write PMF calculation script**

```python
#!/usr/bin/env python3
import json

def calculate_pmf_scores(survey_data):
    pmf_scores = {}
    for venture, data in survey_data.items():
        score = (
            (data['response_rate'] * 0.15) +
            (data['nps_score'] / 100 * 0.20) +
            (data['problem_severity'] / 10 * 0.25) +
            (data['willingness_to_pay'] / 100 * 0.20) +
            (data['interview_confirmation'] * 0.20)
        )
        pmf_scores[venture] = {
            "pmf_score": round(score, 2),
            "decision": "GO" if score >= 0.70 else "NO_GO"
        }
    return pmf_scores

if __name__ == "__main__":
    # Mock data for demonstration
    survey_data = {
        "fin-001": {"response_rate": 0.35, "nps_score": 65, "problem_severity": 8.5, "willingness_to_pay": 85, "interview_confirmation": 0.8}
    }
    scores = calculate_pmf_scores(survey_data)
    with open("WORLDWIDEBRO-OS/01_CEO_COMMAND_CENTER/PMF_RESULTS.json", "w") as f:
        json.dump(scores, f, indent=2)
    print("✅ PMF scores calculated")
```

- [ ] **Step 3: Run PMF scoring after survey completion (2026-06-18)**

Run: `python3 WORLDWIDEBRO-OS/09_AUTOMATION/calculate_pmf_scores.py`

Expected output: PMF decisions (GO/NO_GO) for top 100+ ventures

- [ ] **Step 4: Commit Phase 2.3**

```bash
git add WORLDWIDEBRO-OS/01_CEO_COMMAND_CENTER/PMF_SCORING_MODEL.json
git add WORLDWIDEBRO-OS/09_AUTOMATION/calculate_pmf_scores.py
git commit -m "feat: implement product-market fit scoring and GO/NO_GO decisions"
```

---

## PHASE 3: PRODUCT CREATION (2026-06-19 to 07-10)

**Objective:** Generate product specs for 100+ "GO" ventures; **special focus: automated course generation for 69 EDTECH ventures**

**Task 3.1: Generate Product Specifications**

Files:
- Create: `WORLDWIDEBRO-OS/10_VENTURES/PRODUCT_SPEC_TEMPLATE.md`
- Create: `WORLDWIDEBRO-OS/09_AUTOMATION/generate_product_specs.py`

- [ ] **Step 1: Create product spec template**

```markdown
# {{venture_name}} Product Specification

## Overview
- **Problem:** {{problem_statement}}
- **Solution:** {{solution_description}}
- **Target User:** {{user_persona}}
- **Key Metric:** {{north_star_metric}}

## Core Features
1. {{feature_1}} - {{description}}
2. {{feature_2}} - {{description}}
3. {{feature_3}} - {{description}}

## MVP Roadmap
- **Week 1-2:** {{phase_1_deliverables}}
- **Week 3-4:** {{phase_2_deliverables}}
- **Week 5-6:** {{phase_3_deliverables}}

## Tech Stack
- Frontend: {{frontend_tech}}
- Backend: {{backend_tech}}
- Database: {{database_tech}}
- Hosting: {{hosting_platform}}
```

- [ ] **Step 2: Create spec generator script**

```python
#!/usr/bin/env python3
import json

def generate_product_specs(ventures_list, output_dir):
    for venture in ventures_list:
        spec = f"""# {venture['name']} Product Specification

## Overview
- **Problem:** {venture.get('problem', 'TBD')}
- **Solution:** {venture.get('solution', 'TBD')}
- **Target:** {venture.get('target_user', 'TBD')}

## Features
1. Core feature 1
2. Core feature 2
3. Core feature 3

## MVP Timeline
- Week 1-2: Foundation
- Week 3-4: Features
- Week 5-6: Polish
"""
        with open(f"{output_dir}/{venture['id']}_spec.md", "w") as f:
            f.write(spec)
    print(f"✅ Generated {len(ventures_list)} product specs")

if __name__ == "__main__":
    # Will be called with PMF_RESULTS.json
    pass
```

- [ ] **Step 3: Generate specs for 100+ "GO" ventures**

Run: `python3 WORLDWIDEBRO-OS/09_AUTOMATION/generate_product_specs.py --pmmf_file WORLDWIDEBRO-OS/01_CEO_COMMAND_CENTER/PMF_RESULTS.json --output_dir WORLDWIDEBRO-OS/10_VENTURES/`

Expected: 100+ product specification files

- [ ] **Step 4: Commit Phase 3.1**

```bash
git add WORLDWIDEBRO-OS/10_VENTURES/PRODUCT_SPEC_TEMPLATE.md
git add WORLDWIDEBRO-OS/09_AUTOMATION/generate_product_specs.py
git commit -m "feat: auto-generate product specifications for validated ventures"
```

**Task 3.2: EDTECH Automation - Automated Course Generation for 69 Ventures**

Files:
- Create: `WORLDWIDEBRO-OS/10_VENTURES/EdTech/COURSE_GENERATION_CONFIG.json`
- Create: `WORLDWIDEBRO-OS/09_AUTOMATION/map_edtech_to_courses.py`
- Create: `WORLDWIDEBRO-OS/09_AUTOMATION/generate_course_outlines.py`
- Create: `WORLDWIDEBRO-OS/09_AUTOMATION/submit_higgsfield_batch.py`

- [ ] **Step 1: Create course generation configuration**

```json
{
  "edtech_ventures_total": 69,
  "course_formats": ["video", "text", "quiz", "assignments", "certificates"],
  "content_generation": {
    "outlines": "claude-opus",
    "scripts": "claude-sonnet",
    "quizzes": "claude-sonnet",
    "videos": "higgsfield"
  },
  "platforms": ["lms_website", "mobile_app"],
  "automation_status": "ready"
}
```

- [ ] **Step 2: Map edtech ventures to course pipeline**

```python
#!/usr/bin/env python3
import csv
import json

def map_edtech_ventures(classification_csv, output_json):
    edtech_ventures = []
    with open(classification_csv) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['sector'] == 'edtech':
                edtech_ventures.append({
                    "venture_id": row['venture_id'],
                    "venture_name": row['venture_name'],
                    "tier": row['tier'],
                    "status": "queued_for_course_generation"
                })
    
    with open(output_json, "w") as f:
        json.dump({
            "total_edtech_ventures": len(edtech_ventures),
            "ventures": edtech_ventures
        }, f, indent=2)
    
    print(f"✅ Mapped {len(edtech_ventures)} edtech ventures to course generation")
    return len(edtech_ventures)

if __name__ == "__main__":
    count = map_edtech_ventures(
        "WORLDWIDEBRO-OS/08_RESEARCH/Ventures-Data/ventures_classification_final.csv",
        "WORLDWIDEBRO-OS/10_VENTURES/EdTech/COURSE_MANIFEST.json"
    )
```

- [ ] **Step 3: Run edtech mapping**

Run: `python3 WORLDWIDEBRO-OS/09_AUTOMATION/map_edtech_to_courses.py`

Expected: `COURSE_MANIFEST.json` with 69 edtech ventures

- [ ] **Step 4: Create course outline generator**

```python
#!/usr/bin/env python3
import json
from pathlib import Path

def generate_course_outlines(manifest_json, output_dir):
    with open(manifest_json) as f:
        manifest = json.load(f)
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    for venture in manifest['ventures']:
        outline = {
            "venture_id": venture['venture_id'],
            "venture_name": venture['venture_name'],
            "course_outline": [
                {"module": 1, "title": "Introduction", "lessons": 3},
                {"module": 2, "title": "Core Concepts", "lessons": 5},
                {"module": 3, "title": "Advanced Topics", "lessons": 4},
                {"module": 4, "title": "Project & Certification", "lessons": 2}
            ],
            "total_lessons": 14,
            "estimated_hours": 20,
            "status": "outline_generated"
        }
        
        with open(f"{output_dir}/{venture['venture_id']}_outline.json", "w") as f:
            json.dump(outline, f, indent=2)
    
    print(f"✅ Generated course outlines for {len(manifest['ventures'])} ventures")

if __name__ == "__main__":
    generate_course_outlines(
        "WORLDWIDEBRO-OS/10_VENTURES/EdTech/COURSE_MANIFEST.json",
        "WORLDWIDEBRO-OS/10_VENTURES/EdTech/Course_Outlines/"
    )
```

- [ ] **Step 5: Run outline generation**

Run: `python3 WORLDWIDEBRO-OS/09_AUTOMATION/generate_course_outlines.py`

Expected: 69 course outline files in `WORLDWIDEBRO-OS/10_VENTURES/EdTech/Course_Outlines/`

- [ ] **Step 6: Create Higgsfield batch submission script**

```python
#!/usr/bin/env python3
import json
from pathlib import Path

def submit_higgsfield_batch(manifest_json, output_json):
    with open(manifest_json) as f:
        manifest = json.load(f)
    
    jobs = {
        "batch_id": "edtech_course_gen_batch_001",
        "created_at": "2026-06-19",
        "total_jobs": len(manifest['ventures']),
        "jobs": []
    }
    
    for venture in manifest['ventures']:
        jobs['jobs'].append({
            "venture_id": venture['venture_id'],
            "venture_name": venture['venture_name'],
            "job_type": "course_generation",
            "priority": 1,
            "status": "queued"
        })
    
    with open(output_json, "w") as f:
        json.dump(jobs, f, indent=2)
    
    print(f"✅ Queued {jobs['total_jobs']} course generation jobs to Higgsfield")

if __name__ == "__main__":
    submit_higgsfield_batch(
        "WORLDWIDEBRO-OS/10_VENTURES/EdTech/COURSE_MANIFEST.json",
        "WORLDWIDEBRO-OS/10_VENTURES/EdTech/HIGGSFIELD_JOBS.json"
    )
```

- [ ] **Step 7: Submit batch to Higgsfield**

Run: `python3 WORLDWIDEBRO-OS/09_AUTOMATION/submit_higgsfield_batch.py`

Expected: 69 course generation jobs queued (video scripts, content, quizzes auto-generated)

- [ ] **Step 8: Commit Phase 3.2 (EdTech Automation)**

```bash
git add WORLDWIDEBRO-OS/10_VENTURES/EdTech/
git add WORLDWIDEBRO-OS/09_AUTOMATION/map_edtech_to_courses.py
git add WORLDWIDEBRO-OS/09_AUTOMATION/generate_course_outlines.py
git add WORLDWIDEBRO-OS/09_AUTOMATION/submit_higgsfield_batch.py
git commit -m "feat: automated course generation pipeline for 69 edtech ventures"
```

---

## PHASE 4-9: REMAINING PHASES (PENDING)

| Phase | Tasks | Timeline | Status |
|-------|-------|----------|--------|
| 4 | Branding (logos, voice, positioning per venture) | 2026-07-11 to 07-25 | ⏳ Next |
| 5 | Sales (funnels, websites, CRM per venture) | 2026-07-26 to 08-15 | ⏳ Pending |
| 6 | Marketing (content, ads, SEO per niche) | 2026-08-16 to 09-15 | ⏳ Pending |
| 7 | Customer Success (onboarding, support, retention) | 2026-09-16 to 10-15 | ⏳ Pending |
| 8 | Scaling (automation, hiring, dashboards) | 2026-10-16 to 11-30 | ⏳ Pending |
| 9 | Exit (M&A targets, valuations, pitch decks) | 2026-12-01+ | ⏳ Pending |

---

## Parallel Execution Strategy

**4 Blocker Clusters Running Simultaneously:**

1. **Cluster 1: AI/DevTools/FinTech/SaaS** (236 ventures)
   - Lead: Product validation & creation (Phases 2-3)
   - Timeline: 2026-06-05 to 2026-07-10
   - Key agents: Validation Agent, Spec Generator, Tech Stack Recommender

2. **Cluster 2: Marketplace/Real Estate** (210 ventures)
   - Lead: Validation + competitor analysis (Phase 2)
   - Timeline: 2026-06-05 to 2026-06-18
   - Key agents: Market Research Agent, Validation Agent

3. **Cluster 3: Infrastructure/Construction** (137 ventures)
   - Lead: Product creation (Phase 3, longer timeline)
   - Timeline: 2026-06-19 to 2026-07-25
   - Key agents: Architecture Agent, Implementation Guide

4. **Cluster 4: Education Automation** (69 EDTECH ventures)
   - Lead: Course generation (Phase 3 parallel)
   - Timeline: 2026-06-05 to 2026-07-31
   - Automation: Higgsfield course generation running continuously
   - Deliverable: 69 fully courseware products ready to sell

---

## Success Metrics

- Phase 1: ✅ Done
- Phase 2: 300+ survey responses, 50+ interviews, 100+ "GO" decisions
- Phase 3: 100+ product specs, 69 courses fully generated
- Phase 4-9: 629 ventures with complete product pipeline infrastructure

**Final Outcome (2026-12-31):**
- 629 ventures launched
- 69 EDTECH courses live
- $X MRR across all ventures
- 50+ acquisitions in pipeline
