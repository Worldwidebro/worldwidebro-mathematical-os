#!/bin/bash

mkdir -p "Company Brain"/{00-CONSTITUTION,01-IDENTITY,02-SOURCES,03-INGESTION,04-DATA,05-METADATA,06-ENTITY-RESOLUTION,07-ONTOLOGY,08-KNOWLEDGE-GRAPH,09-KNOWLEDGE,10-MEMORY,11-INDEXING,12-CONTEXT,13-REPOSITORIES,14-CAPABILITIES,15-SKILLS,16-AGENTS,17-MODELS,18-TOOLS,19-ORCHESTRATION,20-DECISIONS,21-POLICY,22-EXECUTION,23-VENTURES,24-FINANCE,25-SALES,26-MARKETING,27-CUSTOMERS,28-PRODUCT,29-OPERATIONS,30-HR,31-LEGAL,32-SECURITY,33-COMPLIANCE,34-RISK,35-ASSETS,36-PARTNERS,37-RESEARCH,38-OPPORTUNITIES,39-EXPERIMENTS,40-METRICS,41-OBSERVABILITY,42-EVALUATION,43-OUTCOMES,44-LEARNING,45-EVOLUTION,46-GOVERNANCE,47-DOCUMENTS,48-AUTOMATION,49-SYSTEM,50-MASTER-CONTROL}

# Add subdirectories for each domain
for domain in "00-CONSTITUTION" "01-IDENTITY" "02-SOURCES" "03-INGESTION" "04-DATA" "05-METADATA" "06-ENTITY-RESOLUTION" "07-ONTOLOGY" "08-KNOWLEDGE-GRAPH" "09-KNOWLEDGE" "10-MEMORY" "11-INDEXING" "12-CONTEXT" "13-REPOSITORIES" "14-CAPABILITIES" "15-SKILLS" "16-AGENTS" "17-MODELS" "18-TOOLS" "19-ORCHESTRATION" "20-DECISIONS" "21-POLICY" "22-EXECUTION" "23-VENTURES" "24-FINANCE" "25-SALES" "26-MARKETING" "27-CUSTOMERS" "28-PRODUCT" "29-OPERATIONS" "30-HR" "31-LEGAL" "32-SECURITY" "33-COMPLIANCE" "34-RISK" "35-ASSETS" "36-PARTNERS" "37-RESEARCH" "38-OPPORTUNITIES" "39-EXPERIMENTS" "40-METRICS" "41-OBSERVABILITY" "42-EVALUATION" "43-OUTCOMES" "44-LEARNING" "45-EVOLUTION" "46-GOVERNANCE" "47-DOCUMENTS" "48-AUTOMATION" "49-SYSTEM" "50-MASTER-CONTROL"; do
  touch "Company Brain/$domain/.keep"
done

# Create infrastructure layer
mkdir -p "Company Brain/_INFRASTRUCTURE"/{omniroute,ollama,agents,memory,tools,storage,integrations,observability,config}
touch "Company Brain/_INFRASTRUCTURE"/.keep

# Create registries layer
mkdir -p "Company Brain/_REGISTRIES"/{capabilities,skills,agents,models,tools,repositories,services,integrations,control-points,coverage}
touch "Company Brain/_REGISTRIES"/.keep

# Create pipelines layer  
mkdir -p "Company Brain/_PIPELINES"/{code-intelligence,ingestion,processing,transformation,indexing,retrieval,reasoning,execution,observability,learning}
touch "Company Brain/_PIPELINES"/.keep

# Create documentation
mkdir -p "Company Brain/_DOCS"/{architecture,guides,procedures,api,reference}
touch "Company Brain/_DOCS"/.keep

echo "✅ Company Brain folder structure created"
ls -la "Company Brain" | head -20
