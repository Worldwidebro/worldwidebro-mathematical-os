#!/usr/bin/env python3
"""
Scaffold canonical README.md files for primary directories in Company Brain
"""

from pathlib import Path

primary_dirs = [
    ("02_PROJECTS", "Company Projects & Strategic Initiatives", "Operational tracking for cross-venture projects, technical initiatives, and milestones."),
    ("HARNESS-ENGINEERING", "Harness Engineering & Evaluation Frameworks", "Test harnesses, synthetic benchmark generators, and reality validation gates."),
    ("OPS-001-STAFFING", "OPS-001 CareerOps Staffing Workspace", "Dedicated operations workspace for CareerOps automated workforce dispatch and candidate routing."),
    ("TRADING-OS", "Trading OS & Capital Allocation Engine", "Algorithmic trading frameworks, liquidity tracking, and quantitative risk modeling."),
    ("_AGENTS", "Autonomous Agent Swarms & Orchestration", "Agent configuration templates, role prompts, and multi-agent coordination topologies."),
    ("_ARCHIVE", "Company Brain Historical Archive", "Preserved historical artifacts, audit snapshots, superseded registries, and past system states."),
    ("_ENGINE", "Cognitive & Data Processing Engines", "Underlying computational engines, parsers, embedding generators, and pipeline wrappers."),
    ("_IMPLEMENTATION", "Implementation Plans & Technical Blueprints", "Executable implementation guides, migration checklists, and deployment records."),
    ("_REFERENCE", "Reference Architecture & Standards Library", "External specifications, RFCs, regulatory frameworks (NAICS, SOC 2, HIPAA), and industry baselines."),
    ("_SCRIPTS", "Operational Automation Scripts", "Utility scripts for backup, validation, graph synchronization, and system maintenance."),
    ("_TOOLS", "Integrated Tooling & Local Knowledge Engines", "Developer tools, including Garry Tan gstack (make-pdf, review) and gbrain (PGLite knowledge engine)."),
    ("api", "Local REST & GraphQL API Endpoints", "FastAPI and Express route handlers connecting internal microservices and database engines."),
    ("calls", "Telephony & Audio Call Intelligence", "Inbound and outbound call recordings, transcripts, sentiment audits, and CRM sync payloads."),
    ("vex-wired", "VEX Portal Deployment & Wiring Manifests", "Configuration and deployment state for the WorldwideBro VEX venture portal.")
]

for dname, title, desc in primary_dirs:
    p = Path(dname)
    p.mkdir(parents=True, exist_ok=True)
    readme = p / "README.md"
    if not readme.exists() or len(readme.read_text().strip()) < 50:
        content = f"""---
id: PORTAL-{dname.replace("_", "").replace("-", "").upper()}-001
title: "{dname} — {title}"
aliases: ["{dname}", "{dname}/README", "{title}"]
tags: [portal, {dname.lower().replace("_", "")}]
status: ACTIVE
authority: "CP-001 / CP-027"
updated: 2026-09-12
---

[[STARTHERE]] | [[REALITY]] | [[INDEX]] | [[INDEX-DOMAINS-COMPLETE]]

# {dname} — {title}

> **Authority:** CP-001 / CP-027  
> **Status:** ACTIVE

## Overview
{desc}
"""
        readme.write_text(content)
        print(f"Created canonical README.md in {dname}/")

print("Primary directory README scaffolding complete.")
