#!/usr/bin/env python3
"""
Reorganize scattered files into WORLDWIDEBRO-OS numbered structure.
Creates proper folder hierarchy, moves all files, logs every action.

---
created: 2026-06-02T00:00:00Z
last_edited: 2026-06-02T00:00:00Z
edited_by: Claude Haiku 4.5
version: 1.0
---
"""

import os
import shutil
import argparse
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

DOCS_ROOT = Path("/Users/acebless/Documents")
WORLDWIDEBRO_OS = DOCS_ROOT / "WORLDWIDEBRO-OS"
LOG_FILE = DOCS_ROOT / "MIGRATION-LOG-2026-06-02.md"

FILE_MIGRATION_MAP = {
    # 01_CEO_COMMAND_CENTER
    "000-OBSIDIAN-MASTER-INDEX.md": "01_CEO_COMMAND_CENTER/Indexes",
    "AI-BOSS-HOLDINGS-REPO-OPERATING-SYSTEM.md": "01_CEO_COMMAND_CENTER/Architecture",
    "CLASSBUILD-DASHBOARD.html": "01_CEO_COMMAND_CENTER/Dashboards",
    "COMPANY-BRAIN-COMPLETION-REPORT.md": "01_CEO_COMMAND_CENTER/Architecture",
    "DYNASTY-STRUCTURE-COMPLETE.md": "01_CEO_COMMAND_CENTER/Architecture",
    "KNOWLEDGE-GRAPH-DASHBOARD.md": "01_CEO_COMMAND_CENTER/Indexes",
    "KNOWLEDGE-GRAPH-VISUAL.md": "01_CEO_COMMAND_CENTER/Indexes",
    "MASTER-INDEX.md": "01_CEO_COMMAND_CENTER/Indexes",
    "NICHE-MASTERY-OS-ARCHITECTURE.md": "01_CEO_COMMAND_CENTER/Architecture",
    "OPERATIONAL-ARCHITECTURE.md": "01_CEO_COMMAND_CENTER/Architecture",
    "ORG-CHART-OPERATIONAL.md": "01_CEO_COMMAND_CENTER/Architecture",
    "PATH-DECISION.md": "01_CEO_COMMAND_CENTER/Architecture",
    "PERSONAL-VENTURES-UNIFIED-PLAN.md": "01_CEO_COMMAND_CENTER/Architecture",
    "SYSTEM-ARCHITECTURE.md": "01_CEO_COMMAND_CENTER/Architecture",
    "SYSTEM-INTEGRATION-MAP.md": "01_CEO_COMMAND_CENTER/Architecture",
    "SYSTEM-LAUNCH-QUICKSTART.md": "01_CEO_COMMAND_CENTER/Architecture",
    "VENTURE-DEFINITIONS.md": "01_CEO_COMMAND_CENTER/Architecture",
    "VENTURE-GITHUB-GRAPH-FLOW-MAP.md": "01_CEO_COMMAND_CENTER/Architecture",
    "VENTURE-OPERATIONS-FRAMEWORK.md": "01_CEO_COMMAND_CENTER/Architecture",
    "UNIFIED-KNOWLEDGE-GRAPH-OS-v1.md": "01_CEO_COMMAND_CENTER/Architecture",
    "WORLDWIDEBRO-COMPLETE-ALIGNMENT-DASHBOARD.md": "01_CEO_COMMAND_CENTER/Dashboards",
    "Index.md": "01_CEO_COMMAND_CENTER/Indexes",
    "findings.md": "01_CEO_COMMAND_CENTER",
    "progress.md": "01_CEO_COMMAND_CENTER",
    "task_plan.md": "01_CEO_COMMAND_CENTER",
    "Knowledge_Graph.canvas": "01_CEO_COMMAND_CENTER/Dashboards",

    # 02_MARKETING
    "HRMS-30-DAY-MARKETING-PLAN.md": "02_MARKETING/HRMS",
    "HRMS-CUSTOMER-ACQUISITION.md": "02_MARKETING/HRMS",
    "HRMS-MARKETING-STRATEGY.md": "02_MARKETING/HRMS",
    "hrms_flier.html": "02_MARKETING/HRMS",
    "hrms_landing_page.html": "02_MARKETING/HRMS",
    "marketing_decision.md": "02_MARKETING",
    "SECTOR-SPECIFIC-MESSAGING.md": "02_MARKETING",

    # 03_SALES
    "CLICKUP-PIPELINE-SETUP.md": "03_SALES/CRM",
    "CLICKUP-SETUP-GUIDE.md": "03_SALES/CRM",
    "CONTACT-DATA-TEMPLATE.csv": "03_SALES/Contacts",
    "CONTACT-EXTRACTION-PLAN.md": "03_SALES/Scripts",
    "CONTACTS-INITIAL.csv": "03_SALES/Contacts",
    "CRM-QUICKSTART.md": "03_SALES/CRM",
    "DEAL-SCRIPTS-BY-SECTOR.md": "03_SALES/Scripts",
    "HRMS-ACQUISITION-PIPELINE.md": "03_SALES/Pipeline",
    "HRMS-BLOCKER-1-CPA-PREP.md": "03_SALES/Pipeline",
    "HRMS-BLOCKER-2-DISCOVERY-CALLS.md": "03_SALES/Pipeline",
    "HRMS-SALES-SCRIPT-PROSPECT-LIST.md": "03_SALES/Scripts",
    "OUTREACH-EXECUTION-GUIDE.md": "03_SALES/Scripts",
    "SALES-EXECUTION.md": "03_SALES",
    "commission-structure.md": "03_SALES",
    "contacts-extracted.csv": "03_SALES/Contacts",

    # 05_QUOTES_ESTIMATES
    "01-MASTER-SERVICES-AGREEMENT.md": "05_QUOTES_ESTIMATES/Agreements",
    "cac_metric.md": "05_QUOTES_ESTIMATES",
    "revenue_target.md": "05_QUOTES_ESTIMATES",

    # 06_SOPs
    "APPROACH-COMPARISON-2026-05-11.md": "06_SOPs",
    "CLASSBUILD-INTEGRATION.md": "06_SOPs/Integrations",
    "CLASSBUILD-SELF-SERVICE.md": "06_SOPs/Infrastructure",
    "CLASSBUILD-SETUP-COMPLETE.md": "06_SOPs/Infrastructure",
    "COMPOSIO-SETUP-GUIDE.md": "06_SOPs/Integrations",
    "CONTRACTOR-CAPABILITY-MAPPING.md": "06_SOPs",
    "CYBERSECURITY-CONTRACTOR-REQUIREMENTS.md": "06_SOPs",
    "CYBERSECURITY-DELIVERY-ROADMAP.md": "06_SOPs",
    "DEXTER-FINANCIAL-ORCHESTRATOR-GUIDE.md": "06_SOPs/Integrations",
    "DEXTER-READINESS.md": "06_SOPs/Infrastructure",
    "EXECUTE-INTELLIGENCE-LAYER.md": "06_SOPs/Infrastructure",
    "GITHUB-SYNC-GUIDE.md": "06_SOPs/Integrations",
    "HRMS-BUSINESS-LOGIC.md": "06_SOPs/Ventures",
    "HRMS-EXECUTION-START.md": "06_SOPs/Ventures",
    "HRMS-PAPERCLIP-WORKFLOWS.md": "06_SOPs/Ventures",
    "HRMS-SECTOR-CREWS.md": "06_SOPs/Ventures",
    "HRMS-TECH-STACK-INTEGRATION.md": "06_SOPs/Ventures",
    "HRMS-TO-NICHE-MASTERY-INTEGRATION.md": "06_SOPs/Ventures",
    "IMPLEMENTATION-MAP-RAG-OBSIDIAN-GRAPH.md": "06_SOPs/Infrastructure",
    "INFRASTRUCTURE-DEPLOYMENT-VERIFICATION.md": "06_SOPs/Infrastructure",
    "LIGHTRAG-DEPLOYED.md": "06_SOPs/Integrations",
    "LIGHTRAG-INTEGRATION-PLAN.md": "06_SOPs/Integrations",
    "LIGHTRAG-SUPABASE-SETUP.md": "06_SOPs/Infrastructure",
    "MOVE-2A-SETUP.md": "06_SOPs/Infrastructure",
    "OBSIDIAN-GRAPH-SETUP.md": "06_SOPs/Infrastructure",
    "OPENVOLO-INTEGRATION-GUIDE.md": "06_SOPs/Integrations",
    "PAPERCLIP-DEPLOYMENT-PLAN.md": "06_SOPs/Infrastructure",
    "SOCRATICODE-INTEGRATION-SUMMARY.md": "06_SOPs/Integrations",
    "SUPABASE-CLI-INTEGRATION.md": "06_SOPs/Infrastructure",
    "TASK-12-COMPOSIO-COMMANDS.md": "06_SOPs/Infrastructure",
    "VENDOR-PROCUREMENT-OS.md": "06_SOPs",
    "VENTURE-OPS-AUTONOMOUS-SETUP.md": "07_AUTOMATIONS/Venture-Ops",
    "backstage-integration-setup.md": "06_SOPs/Integrations",
    "ventures-requirements.md": "06_SOPs/Ventures",

    # 07_AUTOMATIONS - Venture Ops
    "VENTURE-OPERATIONS-TASK-TYPES.md": "07_AUTOMATIONS/Venture-Ops",
    "VENTURE-OPS-COMPLETION-CHECKLIST.md": "07_AUTOMATIONS/Venture-Ops",
    "task-executor.py": "07_AUTOMATIONS/Venture-Ops",
    "task-watcher.py": "07_AUTOMATIONS/Venture-Ops",
    "venture-ops-init.py": "07_AUTOMATIONS/Venture-Ops",

    # 07_AUTOMATIONS - Agents
    "agent_autonomy_deployment.md": "07_AUTOMATIONS",
    "AGENT-AUTONOMY-READY-2026-05-11.md": "07_AUTOMATIONS",
    "AGENT-CONFLICT-REMEDIATION.md": "07_AUTOMATIONS",
    "AGENT-DECISION-LOOPS.md": "07_AUTOMATIONS",
    "AGENT-REMEDIATION-EXECUTION.md": "07_AUTOMATIONS",
    "AGENT-SYSTEM-PROMPTS.md": "07_AUTOMATIONS",
    "agent_conflict_detector.py": "07_AUTOMATIONS/Agents",
    "agent_control_loop_demo.py": "07_AUTOMATIONS/Agents",
    "agent_control_loop.py": "07_AUTOMATIONS/Agents",
    "auto_align_agent.py": "07_AUTOMATIONS/Agents",
    "dexter_backtester.py": "07_AUTOMATIONS/Agents",
    "dexter_dashboard.html": "07_AUTOMATIONS/Agents",
    "dexter_dashboard.py": "07_AUTOMATIONS/Agents",
    "dexter_terminal.py": "07_AUTOMATIONS/Agents",
    "dexter.py": "07_AUTOMATIONS/Agents",
    "financial_analyst_cfo.py": "07_AUTOMATIONS/Agents",
    "financial_analyst_v2.py": "07_AUTOMATIONS/Agents",
    "lightrag_agent_queries.py": "07_AUTOMATIONS/Agents",
    "portfolio_optimizer.py": "07_AUTOMATIONS/Agents",
    "test_dexter.py": "07_AUTOMATIONS/Agents",
    "venture_forecasting.py": "07_AUTOMATIONS/Agents",

    # 07_AUTOMATIONS - Scripts
    "align_venture_repo_universe.py": "07_AUTOMATIONS/Scripts",
    "assign_sector_capabilities.py": "07_AUTOMATIONS/Scripts",
    "audit_ventures.py": "07_AUTOMATIONS/Scripts",
    "classbuild_batch_generator.py": "07_AUTOMATIONS/Scripts",
    "classbuild_integrate_venture.py": "07_AUTOMATIONS/Scripts",
    "classify_repos_heuristic.py": "07_AUTOMATIONS/Scripts",
    "classify_repos_institutional.py": "07_AUTOMATIONS/Scripts",
    "composio_client.py": "07_AUTOMATIONS/Scripts",
    "composio_command_dispatcher.py": "07_AUTOMATIONS/Scripts",
    "composio_local_server.py": "07_AUTOMATIONS/Scripts",
    "export_ventures_with_capabilities.py": "07_AUTOMATIONS/Scripts",
    "fix_repos_metadata.py": "07_AUTOMATIONS/Scripts",
    "github_repos_sync.py": "07_AUTOMATIONS/Scripts",
    "import_contacts_to_openvolo.py": "07_AUTOMATIONS/Scripts",
    "index_repos_local_embeddings.py": "07_AUTOMATIONS/Scripts",
    "index_repos_with_llamaindex.py": "07_AUTOMATIONS/Scripts",
    "ingest_rag_manifest.py": "07_AUTOMATIONS/Scripts",
    "lightrag_complete_pipeline.py": "07_AUTOMATIONS/Scripts",
    "lightrag_demo.py": "07_AUTOMATIONS/Scripts",
    "lightrag_supabase_sync.py": "07_AUTOMATIONS/Scripts",
    "obsidian_graph_build.py": "07_AUTOMATIONS/Scripts",
    "obsidian_graph_sync.py": "07_AUTOMATIONS/Scripts",
    "populate_repos_metadata.py": "07_AUTOMATIONS/Scripts",
    "populate_repos_simple.py": "07_AUTOMATIONS/Scripts",
    "populate_venture_knowledge_graph.py": "07_AUTOMATIONS/Scripts",
    "populate_ventures_served.py": "07_AUTOMATIONS/Scripts",
    "rag_document_preprocessor.py": "07_AUTOMATIONS/Scripts",
    "resegment_contacts.py": "07_AUTOMATIONS/Scripts",
    "run_audit.py": "07_AUTOMATIONS/Scripts",
    "run_osint_enrichment.py": "07_AUTOMATIONS/Scripts",
    "sector_initialization.py": "07_AUTOMATIONS/Scripts",
    "segment_contacts.py": "07_AUTOMATIONS/Scripts",
    "semantic_repo_analyzer.py": "07_AUTOMATIONS/Scripts",
    "sms_provider_integration.py": "07_AUTOMATIONS/Scripts",
    "socraticode_indexer.py": "07_AUTOMATIONS/Scripts",
    "starred-repos-install-order.py": "07_AUTOMATIONS/Scripts",
    "sync_712_ventures_and_socraticode.py": "07_AUTOMATIONS/Scripts",
    "sync_socraticode_to_supabase.py": "07_AUTOMATIONS/Scripts",
    "task-14-integration-demo.py": "07_AUTOMATIONS/Scripts",
    "test_genixbank_lite.py": "07_AUTOMATIONS/Scripts",
    "test_ollama_inference.py": "07_AUTOMATIONS/Scripts",
    "unify_contacts_ventures.py": "07_AUTOMATIONS/Scripts",
    "venture_generator_fast.py": "07_AUTOMATIONS/Scripts",
    "venture_generator.py": "07_AUTOMATIONS/Scripts",
    "verify_venture_repo_matching.py": "07_AUTOMATIONS/Scripts",

    # 07_AUTOMATIONS - Configs
    "AUTO-ALIGNMENT-712.json": "07_AUTOMATIONS/Configs",
    "GRAPHIFY-SOCRATICODE-MAPPING.json": "07_AUTOMATIONS/Configs",
    "HRMS-INTEGRATIONS-config.json": "07_AUTOMATIONS/Configs",
    "REPO_REGISTRY.json": "07_AUTOMATIONS/Configs",
    "SEMANTIC-ALIGNMENT-ANALYSIS.json": "07_AUTOMATIONS/Configs",
    "agent-wiring-config.json": "07_AUTOMATIONS/Configs",
    "agent_repo_responsibility.csv": "07_AUTOMATIONS/Configs",
    "classbuild_ventures.json": "07_AUTOMATIONS/Configs",
    "dexter-cycle-results.json": "07_AUTOMATIONS/Configs",
    "github-teams-config.json": "07_AUTOMATIONS/Configs",
    "socraticode_profiles.json": "07_AUTOMATIONS/Configs",
    "vapi-agent-bella-config.json": "07_AUTOMATIONS/Configs",
    "vapi-agent-echo-config.json": "07_AUTOMATIONS/Configs",
    "vapi-agent-swift-config.json": "07_AUTOMATIONS/Configs",

    # 07_AUTOMATIONS - SQL
    "phase1_audit.sql": "07_AUTOMATIONS/SQL",
    "update_ventures_classification.sql": "07_AUTOMATIONS/SQL",

    # 07_AUTOMATIONS - Shell
    "classbuild_venture_generator.sh": "07_AUTOMATIONS/Shell",
    "sync_alignment.sh": "07_AUTOMATIONS/Shell",
    "verify_classbuild_setup.sh": "07_AUTOMATIONS/Shell",

    # 07_AUTOMATIONS - JS/TS
    "composio-setup.js": "07_AUTOMATIONS/JS-TS",
    "composio-setup.ts": "07_AUTOMATIONS/JS-TS",
    "e2e-venture-test.ts": "07_AUTOMATIONS/JS-TS",
    "paperclip-setup.ts": "07_AUTOMATIONS/JS-TS",
    "rag-venture-context.js": "07_AUTOMATIONS/JS-TS",
    "sector-seeding.ts": "07_AUTOMATIONS/JS-TS",
    "vapi-api-integration.js": "07_AUTOMATIONS/JS-TS",
    "validate-mathematical-integration.ts": "07_AUTOMATIONS/JS-TS",
    "venture-repo-generator.ts": "07_AUTOMATIONS/JS-TS",
    "webhook-call-complete.js": "07_AUTOMATIONS/JS-TS",
    "webhook-server.js": "07_AUTOMATIONS/JS-TS",

    # 07_AUTOMATIONS - Documentation
    "AI-CALLING-SYSTEM-ARCHITECTURE.md": "07_AUTOMATIONS",
    "AOC-SWARM-RUNNER.md": "07_AUTOMATIONS",
    "COMPOSIO-TASK-EXECUTION-STATUS.md": "07_AUTOMATIONS",
    "DEXTER-DATA-SOURCES-INTEGRATION.md": "07_AUTOMATIONS",
    "DEXTER-WEEK-1-SUMMARY.md": "07_AUTOMATIONS",
    "HRMS-COMPOSIO-INTEGRATION.md": "07_AUTOMATIONS",
    "HRMS-INSTRUMENTATION-SCHEMA.md": "07_AUTOMATIONS",
    "OSINT-ENRICHMENT-INTEGRATION.md": "07_AUTOMATIONS",
    "STARRED-REPOS-MONITORING-WORKFLOW.md": "07_AUTOMATIONS",
    "VAPI-API-USAGE.md": "07_AUTOMATIONS",

    # 08_RESEARCH
    "CPA-REVIEW-BRIEFING.md": "08_RESEARCH",
    "ventures_master_with_sectors.csv": "08_RESEARCH/Ventures-Data",
    "ventures_with_capabilities.csv": "08_RESEARCH/Ventures-Data",
    "ventures_dependencies.json": "08_RESEARCH/Ventures-Data",
    "product_audit_results.json": "08_RESEARCH/Ventures-Data",
    "task-7-manifest.json": "08_RESEARCH/Ventures-Data",
    "task-8-audit-trail.json": "08_RESEARCH/Ventures-Data",
    "task-8-results.json": "08_RESEARCH/Ventures-Data",
    "task-8-test-output.log": "08_RESEARCH/Logs",
    "llamaindex_output.log": "08_RESEARCH/Logs",
    "populate_repos_output.log": "08_RESEARCH/Logs",
    "classification_run.log": "08_RESEARCH/Logs",
    "STARRED-REPOS-GOVERNANCE.csv": "08_RESEARCH/Repo-Analysis",
    "STARRED-REPOS-INSTALLATION-PRIORITY.csv": "08_RESEARCH/Repo-Analysis",
    "UNALIGNED-REPOS-CATEGORIZATION.csv": "08_RESEARCH/Repo-Analysis",
    "WORLDWIDEBRO-712-UNIFIED.csv": "08_RESEARCH/Ventures-Data",
    "VENTURE-CLASSIFICATION-BRIDGE.csv": "08_RESEARCH/Ventures-Data",
    "VENTURE-ID-CROSSWALK.csv": "08_RESEARCH/Ventures-Data",
    "VENTURE-RESOURCE-DEPENDENCIES.csv": "08_RESEARCH/Ventures-Data",
    "VENTURE-SHARED-SERVICES-MAPPING.csv": "08_RESEARCH/Ventures-Data",
    "VENTURE-UUID-NAME-BRIDGE.csv": "08_RESEARCH/Ventures-Data",
    "PRIVATE-REPOS-ACCESS-CONTROL.csv": "08_RESEARCH/Repo-Analysis",
    "PRIVATE-REPOS-ALIGNED.csv": "08_RESEARCH/Repo-Analysis",
    "PRIVATE-REPOS-UNALIGNED.csv": "08_RESEARCH/Repo-Analysis",
    "starred_repos_664.csv": "08_RESEARCH/Repo-Analysis",
    "starred-repos-full.json": "08_RESEARCH/Ventures-Data",
    "all-starred-repos.txt": "08_RESEARCH/Repo-Analysis",
    "RAG-INGESTION-MANIFEST.csv": "08_RESEARCH/Ventures-Data",
    "RAG-INGESTION-STATUS.json": "08_RESEARCH/Ventures-Data",
    "sector_gaps_and_recommendations.csv": "08_RESEARCH",
    "api_deployment_risk.md": "08_RESEARCH",
    "WORLDWIDEBRO-REPOS-4LAYERS.csv": "08_RESEARCH/Ventures-Data",
    "WORLDWIDEBRO-SUPERUNIFIED-4LAYERS.csv": "08_RESEARCH/Ventures-Data",
    "WORLDWIDEBRO-VENTURES-REPOS-ALIGNMENT.csv": "08_RESEARCH/Ventures-Data",
    "ventures_classified_option_a_plus_b.json": "08_RESEARCH/Ventures-Data",
    "ventures_enriched_option_b.json": "08_RESEARCH/Ventures-Data",
    "ventures_tier_classified_option_a.json": "08_RESEARCH/Ventures-Data",
    "starred_repos_with_capabilities.csv": "08_RESEARCH/Ventures-Data",
    "ventures_classification_final.csv": "08_RESEARCH/Ventures-Data",

    # 10_VENTURES
    "AGENT-AUTONOMY-READY-2026-05-11-ventures.md": "10_VENTURES",
    "hrms.md": "10_VENTURES",

    # Archive (dated session files)
    "BLOCKER-EXECUTION-2026-05-11.md": "archive",
    "BLOCKER-STATUS-SESSION-2.md": "archive",
    "BLOCKERS-EXECUTION-2026-05-13.md": "archive",
    "COMPLETION-STATUS-2026-05-11.md": "archive",
    "EXECUTION-CHECKLIST-MAY-11.md": "archive",
    "MEMORY-INDEX-PRESERVATION-2026-05-11.md": "archive",
    "SESSION-COMPLETION-2026-05-14.md": "archive",
    "SESSION-FILES-2026-05-11.md": "archive",
    "SYSTEM-COMPLETE-2026-05-11.md": "archive",
    "WEEK-1-EXECUTION-CHECKLIST.md": "archive",
    "DEXTER-WEEK-1-SUMMARY.md": "archive",

    # Archive - Planned but archived
    "PHASE-1-CHECKLIST.md": "01_CEO_COMMAND_CENTER",
    "PHASE-1-DEPLOYMENT-GUIDE.md": "01_CEO_COMMAND_CENTER",
    "PHASE-1-READY-TO-DEPLOY.md": "01_CEO_COMMAND_CENTER",
    "PROJECT-DISCOVERY-AND-EXECUTION.md": "01_CEO_COMMAND_CENTER",
    "PROJECT-DISCOVERY-SYSTEM.md": "01_CEO_COMMAND_CENTER",
    "REMAINING-TASKS.md": "01_CEO_COMMAND_CENTER",
    "TASK-16-GO-LIVE-CHECKLIST.md": "01_CEO_COMMAND_CENTER",
    "TASKS-9-11-READINESS.md": "01_CEO_COMMAND_CENTER",
    "TOOLS-REFERENCE.md": "01_CEO_COMMAND_CENTER",
    "OPERATIONS-EXECUTION-LAYER.md": "01_CEO_COMMAND_CENTER",
    "EXISTING-ARTIFACTS-INVENTORY.md": "01_CEO_COMMAND_CENTER",
    "MAY-14-EXECUTION-BRIEFING.md": "01_CEO_COMMAND_CENTER",
}

# Do not touch
DO_NOT_TOUCH = {
    ".env", ".env.example", ".env.local",
    ".gitignore",
    "node_modules", "supabase", "migrations", "lightrag_data",
    "LightRAG", "RAG-Anything", "iza-os-rag-system", "mcp-dashboard", "Claude",
    "integrations-venv", "make-workflows", "grafana", "nginx", "resolvers", "agents", "composio",
    "data", "_inbox", "The office", "SecondBrain", "Obsidian", "Knowledge Graph",
    "magic-portfolio", "ai-venture-studio-template", "autonomous-venture-studio",
    "bw-001-lash-extension-studio", "business-template-marketplace", "Civilization",
    "civilization-os-local", "generated-courses", "staffing-os", "venture-factory-core",
    "venture-hub", "security-stack", "opensre", "thunderbolt", "vibetunnel", "omi",
    "twenty-local-test", "archive", "osint_results", "integrations",
    "pitch-kit", "con-001-ace-construction", "worldwidebro-vault", "ADMIN_CREDENTIALS.md",
    "Untitled.base", "requirements-iza.txt", ".planning", "WORLDWIDEBRO-OS"
}

def should_skip(path: Path) -> bool:
    """Check if file/folder should be skipped"""
    return path.name in DO_NOT_TOUCH or any(path.name.startswith(prefix) for prefix in ["."]) or path.name == "reorganize_documents.py"

def create_folder_structure():
    """Create all required subfolders"""
    folders = [
        "01_CEO_COMMAND_CENTER/Dashboards",
        "01_CEO_COMMAND_CENTER/Architecture",
        "01_CEO_COMMAND_CENTER/Indexes",
        "01_CEO_COMMAND_CENTER/Execution-Logs",
        "02_MARKETING/HRMS",
        "03_SALES/CRM",
        "03_SALES/Scripts",
        "03_SALES/Contacts",
        "03_SALES/Pipeline",
        "05_QUOTES_ESTIMATES/Agreements",
        "06_SOPs/Integrations",
        "06_SOPs/Ventures",
        "06_SOPs/Infrastructure",
        "07_AUTOMATIONS/Scripts",
        "07_AUTOMATIONS/Configs",
        "07_AUTOMATIONS/Venture-Ops",
        "07_AUTOMATIONS/Agents",
        "07_AUTOMATIONS/SQL",
        "07_AUTOMATIONS/Shell",
        "07_AUTOMATIONS/JS-TS",
        "08_RESEARCH/Ventures-Data",
        "08_RESEARCH/Repo-Analysis",
        "08_RESEARCH/Logs",
        "archive",
    ]

    for folder in folders:
        folder_path = WORLDWIDEBRO_OS / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"  📁 {folder}")

def update_md_metadata(file_path: Path) -> None:
    """Update YAML frontmatter on .md files"""
    if not file_path.suffix == ".md":
        return

    try:
        with open(file_path, "r") as f:
            content = f.read()

        # Update frontmatter
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        updated = re.sub(
            r"last_edited: .*?\n",
            f"last_edited: {timestamp}\n",
            content
        )
        updated = re.sub(
            r"edited_by: .*?\n",
            "edited_by: Claude Haiku 4.5\n",
            updated
        )

        with open(file_path, "w") as f:
            f.write(updated)

    except Exception as e:
        print(f"  ⚠️  Could not update metadata: {e}")

def migrate_files(dry_run: bool = False) -> Tuple[int, List[str]]:
    """Migrate files to proper destinations"""
    moved_count = 0
    moves = []

    for filename, dest_path in FILE_MIGRATION_MAP.items():
        source = DOCS_ROOT / filename
        dest_dir = WORLDWIDEBRO_OS / dest_path
        dest_file = dest_dir / filename

        if not source.exists():
            continue

        if should_skip(source):
            continue

        dest_dir.mkdir(parents=True, exist_ok=True)

        if not dry_run:
            try:
                shutil.move(str(source), str(dest_file))
                update_md_metadata(dest_file)
                timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
                moves.append(f"[{timestamp}] MOVED: {source} → {dest_file}")
                moved_count += 1
            except Exception as e:
                moves.append(f"[ERROR] {source}: {e}")
        else:
            moves.append(f"[DRY-RUN] Would move: {filename} → {dest_path}/{filename}")
            moved_count += 1

    return moved_count, moves

def write_log(moves: List[str], dry_run: bool = False) -> None:
    """Write migration log"""
    if dry_run:
        log_path = DOCS_ROOT / "MIGRATION-LOG-2026-06-02.md"
    else:
        log_path = LOG_FILE

    log_content = f"""# Migration Log: 2026-06-02

**Status:** {'DRY RUN' if dry_run else 'EXECUTED'}
**Timestamp:** {datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}
**Total Moves:** {len(moves)}

---

## Migration Details

"""

    for move in moves:
        log_content += f"{move}\n"

    with open(log_path, "w") as f:
        f.write(log_content)

def main():
    parser = argparse.ArgumentParser(description="Reorganize WORLDWIDEBRO-OS files")
    parser.add_argument("--dry-run", action="store_true", help="Show planned moves without executing")
    args = parser.parse_args()

    print(f"\n🚀 File Reorganization: {'DRY RUN' if args.dry_run else 'EXECUTING'}\n")

    print("📂 Creating folder structure...")
    create_folder_structure()

    print(f"\n📋 {'Planning' if args.dry_run else 'Executing'} migrations...\n")
    moved_count, moves = migrate_files(dry_run=args.dry_run)

    print(f"\n✅ {moved_count} files {'would be' if args.dry_run else ''} moved\n")

    print("📝 Writing log...")
    write_log(moves, dry_run=args.dry_run)
    print(f"   Log: MIGRATION-LOG-2026-06-02.md\n")

    if args.dry_run:
        print("⚠️  DRY RUN COMPLETE")
        print("\nReview the log file and run without --dry-run to execute:\n")
        print("  python reorganize_documents.py\n")
    else:
        print("✨ MIGRATION COMPLETE")
        print("\nVerify with: ls /Users/acebless/Documents/WORLDWIDEBRO-OS/07_AUTOMATIONS/Venture-Ops/\n")

if __name__ == "__main__":
    main()
