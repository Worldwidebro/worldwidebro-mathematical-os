#!/bin/bash

cd "/Users/acebless/The Company/Company Brain"

# Create README for key domains
create_readme() {
  local domain=$1
  local title=$2
  local description=$3
  
  cat > "$domain/README.md" << EOF
# $title

$description

## Overview

This domain handles [DESCRIBE PURPOSE].

## Contents

- [DESCRIBE SUB-DOMAINS]

## Key Files

- [LIST IMPORTANT FILES]

## Connected Domains

- [[]] → downstream
- [[]] ← upstream

## Control Points

See [[\\_REGISTRIES/control-points]] for ~$count operations in this domain.

## Status

🟡 In progress

---

Last updated: 2026-09-01
EOF
}

# Core domains
create_readme "00-CONSTITUTION" "Constitution" "Mission, vision, principles, non-negotiables, governance framework"
create_readme "01-IDENTITY" "Identity" "Company structure, holdings, subsidiaries, ventures, brands, products"
create_readme "02-SOURCES" "Data Sources" "Internal & external data sources, APIs, databases, repositories"
create_readme "04-DATA" "Data" "Raw, normalized, canonical, transactional, analytical data layers"
create_readme "08-KNOWLEDGE-GRAPH" "Knowledge Graph" "Entity nodes, relationships, embeddings, semantic queries"
create_readme "10-MEMORY" "Memory" "Working, episodic, semantic, and procedural memory systems"
create_readme "14-CAPABILITIES" "Capabilities" "Capability registry, implementations, dependencies, coverage"
create_readme "16-AGENTS" "Agents" "Agent registry, roles, permissions, routing, performance"
create_readme "17-MODELS" "Models" "Model registry, cloud & local models, benchmarks, costs"
create_readme "19-ORCHESTRATION" "Orchestration" "Router, planner, scheduler, workflow engine"
create_readme "23-VENTURES" "Ventures" "Venture registry, profiles, financials, operations, metrics"
create_readme "50-MASTER-CONTROL" "Master Control" "Current state, objectives, priorities, active work, system health"

echo "✅ README files created for key domains"
