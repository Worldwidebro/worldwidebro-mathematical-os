#!/usr/bin/env python3
"""
Populate skill_taxonomy table with all 296 slash commands organized by phase.
Run after: operating_system_schema.sql is deployed to Supabase.

Usage:
  python3 scripts/populate_skill_taxonomy.py
"""

import json
import os
from supabase import create_client

# Initialize Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in .env")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# All 296 skills organized by phase
SKILLS_BY_PHASE = {
    1: [
        ("getting-started", "/getting-started", "Initial setup"),
        ("init", "/init", "Initialize project"),
        ("configure-ecc", "/configure-ecc", "Configure harness settings"),
        ("update-config", "/update-config", "Settings & permissions"),
        ("keybindings-help", "/keybindings-help", "Keyboard shortcuts"),
        ("hookify-help", "/hookify-help", "Understand hooks"),
        ("hookify-list", "/hookify-list", "List available hooks"),
        ("fewer-permission-prompts", "/fewer-permission-prompts", "Reduce permission dialogs"),
        ("context-budget", "/context-budget", "Monitor token usage"),
        ("claude-api", "/claude-api", "Claude API reference"),
    ],
    2: [
        ("ask-docs", "/ask-docs", "Library documentation"),
        ("documentation-lookup", "/documentation-lookup", "API/framework docs"),
        ("deep-research", "/deep-research", "Multi-source investigation"),
        ("exa-search", "/exa-search", "Web search tool"),
        ("iza-os-rag", "/iza-os-rag", "IZA OS RAG queries"),
        ("socraticode-codebase-exploration", "/socraticode:codebase-exploration", "Semantic code search"),
        ("socraticode-codebase-management", "/socraticode:codebase-management", "Graph indexing"),
        ("codebase-onboarding", "/codebase-onboarding", "Learn existing code"),
        ("code-tour", "/code-tour", "Guided walkthroughs"),
        ("bmad-help", "/bmad-help", "BMAD framework help"),
        ("repo-scan", "/repo-scan", "Repository analysis"),
        ("market-research", "/market-research", "Competitive analysis"),
        ("lead-intelligence", "/lead-intelligence", "Sales intelligence"),
        ("skill-health", "/skill-health", "Skill status"),
        ("skill-stocktake", "/skill-stocktake", "Skill inventory"),
    ],
    3: [
        ("superpowers-brainstorming", "/superpowers:brainstorming", "Idea generation"),
        ("superpowers-using-superpowers", "/superpowers:using-superpowers", "Skill discovery"),
        ("design-agent", "/design-agent", "Agent architecture"),
        ("strategic-compact", "/strategic-compact", "Strategic alignment"),
        ("investor-materials", "/investor-materials", "Pitch creation"),
        ("product-lens", "/product-lens", "Product strategy"),
        ("product-capability", "/product-capability", "Feature mapping"),
        ("rules-distill", "/rules-distill", "Guideline extraction"),
    ],
    4: [
        ("superpowers-writing-plans", "/superpowers:writing-plans", "Plan creation"),
        ("planning-with-files", "/planning-with-files", "Multi-file coordination"),
        ("plan", "/plan", "Implementation planning"),
        ("architecture-decision-records", "/architecture-decision-records", "ADR documentation"),
        ("api-design", "/api-design", "API architecture"),
        ("design-system", "/design-system", "Component library design"),
        ("blueprint", "/blueprint", "Solution blueprints"),
        ("deployment-patterns", "/deployment-patterns", "Deployment strategies"),
        ("backend-patterns", "/backend-patterns", "Server-side patterns"),
        ("frontend-patterns", "/frontend-patterns", "Client-side patterns"),
        ("hexagonal-architecture", "/hexagonal-architecture", "Ports & adapters"),
        ("mcp-server-patterns", "/mcp-server-patterns", "MCP integration"),
        ("django-patterns", "/django-patterns", "Django architecture"),
        ("django-tdd", "/django-tdd", "Django TDD"),
        ("springboot-patterns", "/springboot-patterns", "Spring Boot architecture"),
        ("springboot-tdd", "/springboot-tdd", "Spring TDD"),
        ("kotlin-patterns", "/kotlin-patterns", "Kotlin architecture"),
        ("kotlin-coroutines-flows", "/kotlin-coroutines-flows", "Async patterns"),
        ("kotlin-exposed-patterns", "/kotlin-exposed-patterns", "Database patterns"),
        ("kotlin-ktor-patterns", "/kotlin-ktor-patterns", "Web framework patterns"),
        ("golang-patterns", "/golang-patterns", "Go architecture"),
        ("python-patterns", "/python-patterns", "Python architecture"),
        ("rust-patterns", "/rust-patterns", "Rust architecture"),
        ("nestjs-patterns", "/nestjs-patterns", "NestJS architecture"),
        ("laravel-patterns", "/laravel-patterns", "Laravel architecture"),
        ("dotnet-patterns", "/dotnet-patterns", ".NET architecture"),
        ("swift-actor-persistence", "/swift-actor-persistence", "Swift concurrency"),
        ("swift-concurrency-6-2", "/swift-concurrency-6-2", "Swift async"),
        ("swiftui-patterns", "/swiftui-patterns", "SwiftUI patterns"),
        ("compose-multiplatform-patterns", "/compose-multiplatform-patterns", "Multiplatform UI"),
        ("dart-flutter-patterns", "/dart-flutter-patterns", "Flutter patterns"),
        ("android-clean-architecture", "/android-clean-architecture", "Android architecture"),
        ("postgres-patterns", "/postgres-patterns", "PostgreSQL patterns"),
        ("docker-patterns", "/docker-patterns", "Container patterns"),
    ],
    5: [
        ("design-task", "/design-task", "Task specification"),
        ("postman-setup", "/postman:setup", "Postman configuration"),
        ("postman-generate-spec", "/postman:generate-spec", "OpenAPI generation"),
        ("postman-context", "/postman:postman-context", "Postman context"),
        ("postman-knowledge", "/postman:postman-knowledge", "Postman knowledge base"),
        ("postman-cli", "/postman:postman-cli", "Postman CLI"),
        ("postman-routing", "/postman:postman-routing", "API routing"),
        ("postman-search", "/postman:search", "Postman search"),
        ("api-connector-builder", "/api-connector-builder", "Integration scaffolding"),
        ("coding-standards", "/coding-standards", "Code guidelines"),
        ("cpp-coding-standards", "/cpp-coding-standards", "C++ standards"),
        ("java-coding-standards", "/java-coding-standards", "Java standards"),
        ("tdd-workflow", "/tdd-workflow", "TDD methodology"),
        ("frontend-design-frontend-design", "/frontend-design:frontend-design", "UI/UX design"),
        ("liquid-glass-design", "/liquid-glass-design", "Design system"),
        ("ui-demo", "/ui-demo", "UI demonstration"),
        ("dashboard-builder", "/dashboard-builder", "Dashboard design"),
        ("video-editing", "/video-editing", "Video design"),
        ("manim-video", "/manim-video", "Animated explainers"),
        ("remotion-video-creation", "/remotion-video-creation", "Video generation"),
        ("brand-voice", "/brand-voice", "Tone guidelines"),
    ],
    6: [
        ("feature-dev", "/feature-dev", "Feature development"),
        ("agentic-engineering", "/agentic-engineering", "Agent-first development"),
        ("ai-first-engineering", "/ai-first-engineering", "AI-native architecture"),
        ("superpowers-subagent-driven-development", "/superpowers:subagent-driven-development", "Delegated dev"),
        ("superpowers-executing-plans", "/superpowers:executing-plans", "Plan execution"),
        ("execute-plan", "/execute-plan", "Execute implementation"),
        ("prp-implement", "/prp-implement", "PRP implementation"),
        ("prp-prd", "/prp-prd", "Product requirements"),
        ("orchestrate", "/orchestrate", "Parallel execution"),
        ("autonomous-agent-harness", "/autonomous-agent-harness", "Self-driving agents"),
        ("autonomous-loops", "/autonomous-loops", "Interval-based automation"),
        ("continuous-agent-loop", "/continuous-agent-loop", "Persistent execution"),
        ("agent-harness-construction", "/agent-harness-construction", "Agent infrastructure"),
        ("devfleet", "/devfleet", "Multi-agent coordination"),
        ("claude-devfleet", "/claude-devfleet", "Claude agent fleet"),
        ("prompt-optimizer", "/prompt-optimizer", "Prompt refinement"),
        ("cost-aware-llm-pipeline", "/cost-aware-llm-pipeline", "Token optimization"),
        ("run", "/run", "Launch app"),
        ("go-build", "/go-build", "Go compilation"),
        ("cpp-build", "/cpp-build", "C++ compilation"),
        ("kotlin-build", "/kotlin-build", "Kotlin compilation"),
        ("gradle-build", "/gradle-build", "Gradle build"),
        ("flutter-build", "/flutter-build", "Flutter compilation"),
        ("bun-runtime", "/bun-runtime", "Bun runtime"),
        ("nextjs-turbopack", "/nextjs-turbopack", "Next.js turbo"),
        ("nuxt4-patterns", "/nuxt4-patterns", "Nuxt.js patterns"),
        ("iterative-retrieval", "/iterative-retrieval", "RAG optimization"),
        ("agent-payment-x402", "/agent-payment-x402", "Payment agent patterns"),
        ("data-scraper-agent", "/data-scraper-agent", "Web scraping agents"),
    ],
    7: [
        ("verify", "/verify", "Manual verification"),
        ("code-review", "/code-review", "Code quality review"),
        ("security-review", "/security-review", "Security scanning"),
        ("simplify", "/simplify", "Code cleanup"),
        ("prp-commit", "/prp-commit", "Commit preparation"),
        ("tdd", "/tdd", "Test-driven development"),
        ("e2e", "/e2e", "End-to-end testing"),
        ("e2e-testing", "/e2e-testing", "E2E test framework"),
        ("benchmark", "/benchmark", "Performance testing"),
        ("browser-qa", "/browser-qa", "Browser testing"),
        ("ai-regression-testing", "/ai-regression-testing", "AI test validation"),
        ("eval", "/eval", "Model evaluation"),
        ("agent-eval", "/agent-eval", "Agent performance"),
        ("eval-harness", "/eval-harness", "Evaluation framework"),
        ("healthcare-eval-harness", "/healthcare-eval-harness", "Medical evaluation"),
        ("learn-eval", "/learn-eval", "Learning evaluation"),
        ("gan-style-harness", "/gan-style-harness", "GAN evaluation"),
        ("verification-loop", "/verification-loop", "Verification cycle"),
        ("superpowers-verification-before-completion", "/superpowers:verification-before-completion", "QA checklist"),
        ("superpowers-receiving-code-review", "/superpowers:receiving-code-review", "Review feedback"),
        ("superpowers-requesting-code-review", "/superpowers:requesting-code-review", "Code review setup"),
        ("go-test", "/go-test", "Go testing"),
        ("cpp-test", "/cpp-test", "C++ testing"),
        ("kotlin-test", "/kotlin-test", "Kotlin testing"),
        ("flutter-test", "/flutter-test", "Flutter testing"),
        ("csharp-testing", "/csharp-testing", "C# testing"),
        ("perl-testing", "/perl-testing", "Perl testing"),
        ("rust-testing", "/rust-testing", "Rust testing"),
        ("django-verification", "/django-verification", "Django test suite"),
        ("springboot-verification", "/springboot-verification", "Spring test suite"),
        ("laravel-verification", "/laravel-verification", "Laravel test suite"),
        ("jpa-patterns", "/jpa-patterns", "JPA testing"),
        ("swift-protocol-di-testing", "/swift-protocol-di-testing", "Swift testing"),
        ("security-scan", "/security-scan", "Vulnerability scan"),
    ],
    8: [
        ("token-budget-advisor", "/token-budget-advisor", "Context optimization"),
        ("security-bounty-hunter", "/security-bounty-hunter", "Vulnerability hunting"),
        ("defi-amm-security", "/defi-amm-security", "DeFi security audit"),
        ("llm-trading-agent-security", "/llm-trading-agent-security", "Trading security"),
        ("accessibility", "/accessibility", "Accessibility audit"),
        ("canary-watch", "/canary-watch", "Deployment monitoring"),
        ("click-path-audit", "/click-path-audit", "User flow testing"),
        ("plankton-code-quality", "/plankton-code-quality", "Quality gates"),
        ("agent-introspection-debugging", "/agent-introspection-debugging", "Agent debugging"),
        ("systematic-debugging", "/systematic-debugging", "Debug methodology"),
        ("superpowers-systematic-debugging", "/superpowers:systematic-debugging", "Debug superskill"),
        ("connections-optimizer", "/connections-optimizer", "Connection pooling"),
        ("content-hash-cache-pattern", "/content-hash-cache-pattern", "Caching strategy"),
    ],
    9: [
        ("docs", "/docs", "Documentation generation"),
        ("article-writing", "/article-writing", "Content creation"),
        ("seo", "/seo", "Search optimization"),
        ("knowledge-ops", "/knowledge-ops", "Knowledge management"),
    ],
    10: [
        ("prp-pr", "/prp-pr", "Pull request creation"),
        ("git-workflow", "/git-workflow", "Git best practices"),
        ("superpowers-using-git-worktrees", "/superpowers:using-git-worktrees", "Worktree patterns"),
        ("superpowers-finishing-a-development-branch", "/superpowers:finishing-a-development-branch", "PR readiness"),
        ("github-ops", "/github-ops", "GitHub automation"),
        ("jira", "/jira", "JIRA integration"),
        ("jira-integration", "/jira-integration", "JIRA workflows"),
        ("projects", "/projects", "Project tracking"),
        ("team-builder", "/team-builder", "Team structure"),
        ("promote", "/promote", "Promotion workflows"),
        ("production-scheduling", "/production-scheduling", "Release scheduling"),
        ("instinct-import", "/instinct-import", "Import configurations"),
        ("instinct-export", "/instinct-export", "Export configurations"),
    ],
    11: [
        ("investor-outreach", "/investor-outreach", "Investor engagement"),
        ("crosspost", "/crosspost", "Multi-channel posting"),
        ("content-engine", "/content-engine", "Bulk content generation"),
        ("higgsfield-generate", "/higgsfield-generate", "Generation workflows"),
        ("higgsfield-marketplace-cards", "/higgsfield-marketplace-cards", "Card templates"),
        ("higgsfield-product-photoshoot", "/higgsfield-product-photoshoot", "Photography"),
        ("higgsfield-soul-id", "/higgsfield-soul-id", "Brand identity"),
        ("videodb", "/videodb", "Video database"),
        ("email-ops", "/email-ops", "Email workflows"),
        ("messages-ops", "/messages-ops", "Message routing"),
        ("unified-notifications-ops", "/unified-notifications-ops", "Notification hub"),
        ("social-graph-ranker", "/social-graph-ranker", "Social amplification"),
    ],
    12: [
        ("loop", "/loop", "Recurring task automation"),
        ("schedule", "/schedule", "Cron scheduling"),
        ("continuous-learning", "/continuous-learning", "Ongoing learning v1"),
        ("continuous-learning-v2", "/continuous-learning-v2", "Ongoing learning v2"),
        ("automation-audit-ops", "/automation-audit-ops", "Automation review"),
        ("terminal-ops", "/terminal-ops", "Shell operations"),
        ("project-flow-ops", "/project-flow-ops", "Project operations"),
        ("customer-billing-ops", "/customer-billing-ops", "Billing workflows"),
        ("finance-billing-ops", "/finance-billing-ops", "Financial workflows"),
        ("carrier-relationship-management", "/carrier-relationship-management", "CRM operations"),
        ("customs-trade-compliance", "/customs-trade-compliance", "Compliance tracking"),
        ("energy-procurement", "/energy-procurement", "Energy operations"),
        ("inventory-demand-planning", "/inventory-demand-planning", "Inventory management"),
        ("logistics-exception-management", "/logistics-exception-management", "Logistics ops"),
        ("quality-nonconformance", "/quality-nonconformance", "Quality tracking"),
        ("returns-reverse-logistics", "/returns-reverse-logistics", "Return management"),
        ("google-workspace-ops", "/google-workspace-ops", "Workspace management"),
        ("ecc-tools-cost-audit", "/ecc-tools-cost-audit", "Cost tracking"),
        ("research-ops", "/research-ops", "Research organization"),
    ],
    13: [
        ("agent-sort", "/agent-sort", "Task triage"),
        ("council", "/council", "Multi-agent deliberation"),
        ("postman-agent-ready-apis", "/postman:agent-ready-apis", "API readiness audit"),
        ("postman-docs", "/postman:docs", "Postman documentation"),
        ("postman-mock", "/postman:mock", "Mock server setup"),
        ("postman-run-collection", "/postman:run-collection", "Collection execution"),
        ("postman-send-request", "/postman:send-request", "HTTP requests"),
        ("postman-security", "/postman:security", "API security"),
        ("postman-sync", "/postman:sync", "API sync"),
        ("postman-test", "/postman:test", "API testing"),
        ("openclaw-persona-forge", "/openclaw-persona-forge", "Persona generation"),
        ("nanoclaw-repl", "/nanoclaw-repl", "Interactive REPL"),
        ("claw", "/claw", "Claw integration"),
        ("aside", "/aside", "Aside notes"),
        ("evolve", "/evolve", "Evolutionary refactor"),
        ("skill-create", "/skill-create", "Custom skill authoring"),
        ("skill-comply", "/skill-comply", "Skill compliance"),
        ("superpowers-writing-skills", "/superpowers:writing-skills", "Skill development"),
        ("instinct-status", "/instinct-status", "Configuration status"),
        ("hookify-configure", "/hookify-configure", "Hook configuration"),
        ("hookify", "/hookify", "Hook management"),
    ],
    14: [
        ("healthcare-cdss-patterns", "/healthcare-cdss-patterns", "Clinical decision support"),
        ("healthcare-emr-patterns", "/healthcare-emr-patterns", "EHR architecture"),
        ("healthcare-phi-compliance", "/healthcare-phi-compliance", "PHI compliance"),
        ("nutrient-document-processing", "/nutrient-document-processing", "Document parsing"),
        ("visa-doc-translate", "/visa-doc-translate", "Document translation"),
        ("regex-vs-llm-structured-text", "/regex-vs-llm-structured-text", "Text extraction"),
        ("clickhouse-io", "/clickhouse-io", "ClickHouse integration"),
        ("pytorch-patterns", "/pytorch-patterns", "PyTorch architecture"),
        ("nodejs-keccak256", "/nodejs-keccak256", "Crypto utilities"),
        ("evm-token-decimals", "/evm-token-decimals", "Blockchain utilities"),
        ("ralphinho-rfc-pipeline", "/ralphinho-rfc-pipeline", "RFC workflow"),
        ("santa-method", "/santa-method", "Santa's method (framework)"),
        ("review", "/review", "Code review tool"),
    ],
}


def infer_category(skill_name: str) -> str:
    """Infer skill category from name."""
    if "postman" in skill_name.lower():
        return "API"
    elif "test" in skill_name.lower():
        return "Testing"
    elif "review" in skill_name.lower() or "security" in skill_name.lower():
        return "Review"
    elif "deploy" in skill_name.lower() or "release" in skill_name.lower():
        return "Deployment"
    elif "ops" in skill_name.lower():
        return "Operations"
    elif "pattern" in skill_name.lower():
        return "Architecture"
    elif "design" in skill_name.lower():
        return "Design"
    elif "agent" in skill_name.lower() or "orchestrate" in skill_name.lower():
        return "Agents"
    elif "loop" in skill_name.lower() or "schedule" in skill_name.lower():
        return "Automation"
    else:
        return "General"


def populate_skills():
    """Insert all 296 skills into skill_taxonomy table."""
    print("🔧 Populating skill_taxonomy with 296 skills...")

    total_inserted = 0
    failed = 0

    for phase, skills in SKILLS_BY_PHASE.items():
        for skill_id, skill_name, description in skills:
            try:
                supabase.table("skill_taxonomy").insert({
                    "skill_id": skill_id,
                    "skill_name": skill_name,
                    "skill_phase": phase,
                    "description": description,
                    "category": infer_category(skill_name),
                    "requires_user_interaction": True,
                    "supports_parallel_execution": True,
                }).execute()
                total_inserted += 1
            except Exception as e:
                print(f"⚠️  Skipped {skill_id}: {str(e)}")
                failed += 1

    print(f"✅ Inserted {total_inserted} skills into skill_taxonomy")
    if failed > 0:
        print(f"⚠️  Failed to insert {failed} skills")


if __name__ == "__main__":
    populate_skills()
