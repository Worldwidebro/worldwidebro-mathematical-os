#!/usr/bin/env python3
"""
CrewAI Orchestrator for IZA OS Agents
Coordinates 4 CON agents (venture_classifier → estimator_gen1 → risk_assessor → project_scheduler)
Logs all execution to Supabase agent_executions table
"""

import os
import json
from datetime import datetime
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from supabase import create_client

# Environment
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize clients
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
llm = ChatOpenAI(model_name="gpt-4")

# ============================================================================
# AGENT DEFINITIONS (From AGENTS.md)
# ============================================================================

venture_classifier = Agent(
    role="Venture Intake Router",
    goal="Classify construction leads by venture type (94% accuracy)",
    backstory="""Expert at categorizing construction leads.
    You've classified 100+ projects with 94% accuracy.
    You know: residential, commercial, industrial, renovation venture types.
    You route leads to the correct venture based on scope and budget.""",
    verbose=True,
    allow_delegation=False,
)

estimator_gen1 = Agent(
    role="Cost Estimation Specialist",
    goal="Generate accurate bid estimates (88% accuracy, ±10% variance)",
    backstory="""Seasoned construction estimator with 88% accuracy.
    You generate detailed cost breakdowns with materials, labor, equipment, 10% contingency.
    You know material costs, labor rates, risk factors.
    You ask for clarification when scope is ambiguous.""",
    verbose=True,
    allow_delegation=False,
)

risk_assessor = Agent(
    role="Risk Identification & Compliance Officer",
    goal="Flag compliance and safety risks (91% accuracy)",
    backstory="""Construction safety expert with 91% accuracy at risk identification.
    You know OSHA regulations, insurance requirements, environmental rules.
    You flag weather, crew, equipment, compliance, and regulatory risks.""",
    verbose=True,
    allow_delegation=False,
)

project_scheduler = Agent(
    role="Resource & Project Scheduler",
    goal="Schedule work and equipment (75% on-time delivery)",
    backstory="""Project coordinator with 75% on-time delivery.
    You schedule crew, equipment, materials over project timeline.
    You handle delays, conflicts, and resource optimization.
    You build Gantt charts and critical path analysis.""",
    verbose=True,
    allow_delegation=False,
)

# ============================================================================
# TASK DEFINITIONS (Sequential workflow)
# ============================================================================

classify_task = Task(
    description="Classify lead: {lead_json}. Output: venture_type, confidence_score, rationale",
    expected_output="JSON: {venture_type, confidence_score, rationale}",
    agent=venture_classifier,
)

estimate_task = Task(
    description="Estimate costs for: {classified_lead}. Break down: materials, labor, equipment, contingency",
    expected_output="JSON: {line_items, total_cost, confidence_score}",
    agent=estimator_gen1,
)

risk_task = Task(
    description="Assess risks for: {estimated_project}. Flag: OSHA, insurance, weather, crew, equipment, compliance",
    expected_output="JSON: {risks, severity, mitigations}",
    agent=risk_assessor,
)

schedule_task = Task(
    description="Schedule project: {risk_assessed}. Allocate crew, equipment, materials. Show critical path",
    expected_output="JSON: {schedule, crew_allocation, equipment_allocation, critical_path}",
    agent=project_scheduler,
)

# ============================================================================
# CREW (Multi-agent orchestration)
# ============================================================================

con_crew = Crew(
    agents=[venture_classifier, estimator_gen1, risk_assessor, project_scheduler],
    tasks=[classify_task, estimate_task, risk_task, schedule_task],
    verbose=True,
    process="sequential"  # Strict order: classify → estimate → assess → schedule
)

# ============================================================================
# EXECUTION & LOGGING
# ============================================================================

def process_lead(lead_data: dict) -> dict:
    """Process lead through crew and log to Supabase."""
    start_time = datetime.now()
    lead_id = lead_data.get("id", "UNKNOWN")

    print(f"\n{'='*70}")
    print(f"CrewAI: Processing Lead {lead_id}")
    print(f"{'='*70}\n")

    try:
        # Execute crew
        result = con_crew.kickoff(inputs={"lead_json": json.dumps(lead_data)})
        duration = (datetime.now() - start_time).total_seconds()
        status = "success"
        error = None
    except Exception as e:
        duration = (datetime.now() - start_time).total_seconds()
        status = "failed"
        error = str(e)
        result = None
        print(f"✗ Crew execution failed: {error}")

    # Log to Supabase
    try:
        supabase.table("agent_executions").insert({
            "agent_name": "con_crew_orchestrator",
            "venture_id": lead_data.get("venture_id", "UNKNOWN"),
            "started_at": start_time.isoformat(),
            "ended_at": datetime.now().isoformat(),
            "status": status,
            "input_tokens": 0,  # TODO: Get from LLM usage
            "output_tokens": 0,
            "cost_usd": 0.00,
            "machine": "macbook-air",
            "model_used": "gpt-4-via-litellm",
            "error": error,
        }).execute()
        print(f"✓ Logged to agent_executions")
    except Exception as e:
        print(f"✗ Logging failed: {e}")

    return {
        "lead_id": lead_id,
        "status": status,
        "duration_seconds": duration,
        "error": error,
        "result": str(result) if result else None,
    }

# ============================================================================
# CLI ENTRY
# ============================================================================

if __name__ == "__main__":
    test_lead = {
        "id": "LEAD-20260720-001",
        "venture_id": "CON-001",
        "client": "Downtown Renovations LLC",
        "project_type": "Commercial Renovation",
        "location": "Charlotte, NC",
        "budget": "$150,000",
        "timeline": "60 days",
        "scope": "Renovation of office floors 2-4: electrical, HVAC, flooring, paint",
    }

    result = process_lead(test_lead)
    print(f"\n✓ Complete: {result['duration_seconds']:.1f}s, Status: {result['status']}")
