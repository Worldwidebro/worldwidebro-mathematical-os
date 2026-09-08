#!/bin/bash

# Define all 50 domains with descriptions
declare -A domains=(
  ["00-CONSTITUTION"]="Mission, vision, principles, non-negotiables, governance"
  ["01-IDENTITY"]="Company structure, holdings, subsidiaries, ventures, brands"
  ["02-SOURCES"]="Data sources, APIs, databases, repositories, integrations"
  ["03-INGESTION"]="Pipelines, connectors, webhooks, imports, crawlers"
  ["04-DATA"]="Raw, normalized, canonical, transactional, analytical data"
  ["05-METADATA"]="Schemas, lineage, provenance, freshness, confidence"
  ["06-ENTITY-RESOLUTION"]="People, companies, ventures, products, deduplication"
  ["07-ONTOLOGY"]="Concepts, entities, relationships, industries, processes"
  ["08-KNOWLEDGE-GRAPH"]="Nodes, edges, embeddings, queries, analytics"
  ["09-KNOWLEDGE"]="Policies, procedures, playbooks, research, IP"
  ["10-MEMORY"]="Working, episodic, semantic, procedural memory"
  ["11-INDEXING"]="Full-text, vector, semantic, keyword indexing"
  ["12-CONTEXT"]="Task, company, venture, customer, financial context"
  ["13-REPOSITORIES"]="Code ownership, quality, dependencies, capabilities"
  ["14-CAPABILITIES"]="Registry, definitions, implementations, coverage"
  ["15-SKILLS"]="Library, instructions, examples, tests, evaluations"
  ["16-AGENTS"]="Registry, roles, permissions, routing, performance"
  ["17-MODELS"]="Registry, cloud, local, benchmarks, performance, costs"
  ["18-TOOLS"]="Registry, MCP servers, APIs, automation, integrations"
  ["19-ORCHESTRATION"]="Router, planner, scheduler, task queue, workflows"
  ["20-DECISIONS"]="Requests, recommendations, alternatives, approvals, history"
  ["21-POLICY"]="Authority, permissions, approvals, escalation, guardrails"
  ["22-EXECUTION"]="Jobs, tasks, actions, transactions, changes, approvals"
  ["23-VENTURES"]="Registry, profiles, plans, financials, operations, metrics"
  ["24-FINANCE"]="Accounting, revenue, expenses, budgets, forecasting, investments"
  ["25-SALES"]="Leads, prospects, accounts, opportunities, pipeline, forecasting"
  ["26-MARKETING"]="Research, audiences, campaigns, content, analytics, attribution"
  ["27-CUSTOMERS"]="Profiles, interactions, support, feedback, behavior, retention"
  ["28-PRODUCT"]="Strategy, requirements, roadmap, research, releases, feedback"
  ["29-OPERATIONS"]="Processes, SOPs, workflows, scheduling, procurement, logistics"
  ["30-HR"]="Workforce, roles, recruiting, onboarding, performance, training"
  ["31-LEGAL"]="Entities, contracts, IP, compliance, licenses, litigation"
  ["32-SECURITY"]="Identity, access, secrets, vulnerabilities, threats, incidents"
  ["33-COMPLIANCE"]="Regulatory, certifications, controls, audits, evidence"
  ["34-RISK"]="Enterprise, financial, operational, technology, legal, market risk"
  ["35-ASSETS"]="Real estate, equipment, vehicles, IP, software, digital assets"
  ["36-PARTNERS"]="Investors, lenders, vendors, strategic partners, relationships"
  ["37-RESEARCH"]="Market, competitors, technology, industry, academic, patents"
  ["38-OPPORTUNITIES"]="Discovered, scored, qualified, rejected, active, funded"
  ["39-EXPERIMENTS"]="Hypotheses, tests, results, failures, learnings, replications"
  ["40-METRICS"]="Company, ventures, finance, sales, operations, agents, OKRs"
  ["41-OBSERVABILITY"]="Logs, traces, metrics, events, costs, latency, errors, uptime"
  ["42-EVALUATION"]="Agents, models, skills, tools, accuracy, benchmarks, regression"
  ["43-OUTCOMES"]="Decisions, experiments, ventures, campaigns, products, financial"
  ["44-LEARNING"]="Lessons, failures, successes, patterns, heuristics, improvements"
  ["45-EVOLUTION"]="Optimization, self-improvement, skill evolution, architecture"
  ["46-GOVERNANCE"]="System of record, change control, approvals, audits, provenance"
  ["47-DOCUMENTS"]="Corporate, financial, legal, operational, technical, archives"
  ["48-AUTOMATION"]="Workflows, triggers, schedules, jobs, event handlers, remediation"
  ["49-SYSTEM"]="Configuration, environment, secrets, infrastructure, deployment"
  ["50-MASTER-CONTROL"]="Current state, objectives, priorities, blockers, health"
)

echo "Creating README.md for all 50 domains..."

for domain in "${!domains[@]}"; do
  description="${domains[$domain]}"
  
  cat > "$domain/README.md" << EOF
# $domain

$description

## Overview

This domain handles the following responsibilities and operations.

## Key Responsibilities

- [Primary responsibility 1]
- [Primary responsibility 2]
- [Primary responsibility 3]

## Contents

See sub-directories and related documents below.

## Connected Domains

**Upstream (inputs from):**
- [[upstream-1]]

**Downstream (outputs to):**
- [[downstream-1]]

## Control Points

This domain contains approximately X controllable operations.

See [[\\_REGISTRIES/control-points]] for the complete inventory mapped to this domain.

## Data & Resources

- **Primary storage:** 
- **Registries:** 
- **APIs:** 

## Status

🟡 **In Progress**

- [ ] Documentation complete
- [ ] Control points defined
- [ ] Implementations mapped
- [ ] Tests created

## Related Documentation

- [[\\_DOCS/architecture]]
- [[\\_REGISTRIES]]

## Quick Links

- **Master Index:** [[INDEX]]
- **Master Control:** [[50-MASTER-CONTROL]]
- **Infrastructure:** [[\\_INFRASTRUCTURE]]

---

**Last Updated:** 2026-09-01  
**Tags:** #company-brain #${domain:0:2}
EOF
done

echo "✅ README.md created for all 50 domains"

# Create bootstrap files in infrastructure
echo "Creating infrastructure bootstrap files..."
for dir in _INFRASTRUCTURE/{omniroute,ollama,agents,memory,tools,storage,integrations,observability,config}; do
  touch "$dir/.env.example"
  touch "$dir/README.md"
  cat > "$dir/README.md" << 'EOF'
# Infrastructure Component

[Description]

## Configuration

See `.env.example` for required environment variables.

## Status

🟡 Needs configuration

EOF
done

# Create registry bootstrap files
echo "Creating registry bootstrap files..."
for dir in _REGISTRIES/{control-points,capabilities,skills,agents,models,tools,repositories,services,integrations,coverage}; do
  touch "$dir/README.md"
  touch "$dir/.gitkeep"
  cat > "$dir/README.md" << 'EOF'
# Registry

[Description of what goes in this registry]

## Format

[YAML/JSON format expected]

## Examples

[Examples of entries]

## Status

🟡 Empty - awaiting population

EOF
done

echo "✅ Infrastructure & registry bootstrap files created"
echo ""
echo "Total files created:"
find . -type f -name README.md | wc -l | xargs echo "  README.md files:"
