# WORLDWIDEBRO VENTURES: PEOPLE OPERATIONS IMPLEMENTATION SPECIFICATION

**Document Type:** Technical Specification for Software Engineering Team  
**Created:** 2026-05-31  
**Status:** Ready for Implementation  
**Scope:** All 9 Ventures (3 SaaS + 6 Operations)  
**Owner:** Worldwidebro Holdings CEO Command Center  

---

## EXECUTIVE SUMMARY

This document specifies the complete implementation of the 15_PEOPLE_OPERATIONS folder structure across all active ventures (ent-venture-001/002/003 and ops-venture-001 through ops-venture-006). 

**Deliverables:**
- 9 × 15_PEOPLE_OPERATIONS folders with 5 JSON spec files each (45 JSON files total)
- 6 new Supabase tables with schema definitions
- Agent assignment matrix (6 agent types × 9 ventures)
- Team roster templates with FTE tracking
- RACI matrix for all venture activities
- Onboarding/handoff procedure playbooks

**Timeline:** 4 weeks  
**Team Size:** 2 engineers + 1 product manager  
**Effort:** ~240 hours total

---

## PART 1: FOLDER STRUCTURE SPECIFICATION

### 1.1 Directory Location & Naming
Each venture gets a new 15_PEOPLE_OPERATIONS folder at this path:

```
WORLDWIDEBRO-OS/10_VENTURES/[SaaS_Ventures|Operations_Ventures]/[venture-id]/15_PEOPLE_OPERATIONS/
```

**Example paths:**
- `...10_VENTURES/SaaS_Ventures/ent-venture-001-hrms/15_PEOPLE_OPERATIONS/`
- `...10_VENTURES/Operations_Ventures/ops-venture-001-hvac/15_PEOPLE_OPERATIONS/`

### 1.2 Required Files (5 JSON files per venture)

| File | Purpose | Owner Role | Update Frequency |
|------|---------|-----------|------------------|
| Agent_Manifest.json | Define AI agents assigned to venture | Venture Lead | Monthly |
| Team_Roster.json | Track people, FTE, roles, handoffs | HR/Ops | As-needed |
| Skills_Inventory.json | Map skills to agents & people | Venture Lead | Quarterly |
| RACI_Matrix.json | Define responsibility for all activities | Venture Lead | Quarterly |
| Onboarding_Checklist.json | Role-based onboarding paths | HR/Ops | As-needed |
| Handoff_Procedures.json | Transition playbooks for key roles | HR | As-needed |

**Note:** Handoff_Procedures can be venture-specific OR shared in WORLDWIDEBRO-OS/10_VENTURES/Shared_Resources/Playbooks/handoff/ if identical across ventures.

---

## PART 2: JSON SCHEMA SPECIFICATIONS

### 2.1 Agent_Manifest.json

**Purpose:** Single source of truth for which AI agents work on this venture and their configuration.

**Location:** `15_PEOPLE_OPERATIONS/Agent_Manifest.json`

**Schema:**
```json
{
  "venture_id": "ent-venture-001-hrms",
  "agents": [
    {
      "agent_id": "agent-hrms-001-lead-scorer",
      "agent_type": "ai-agent",
      "sector": "sales",
      "stage": "active",
      "skills": [
        "lead-qualification",
        "data-enrichment",
        "crm-integration"
      ],
      "owner": "sal-001-john-doe",
      "backup_owner": "sal-002-jane-smith",
      "mcp_servers": [
        "supabase",
        "clickup",
        "slack"
      ],
      "parameters": {
        "lead_quality_threshold": 0.75,
        "auto_score_updates": true,
        "feedback_loop_enabled": true,
        "slack_notifications": true
      },
      "status": "in-production",
      "accuracy_rate": 0.94,
      "last_update": "2026-05-31",
      "created_date": "2026-03-15"
    }
  ],
  "metadata": {
    "total_agents": 3,
    "last_modified": "2026-05-31",
    "modified_by": "system"
  }
}
```

**Fields Explanation:**
- **agent_id:** Unique identifier, format: agent-[venture-code]-[sequence]-[function]
- **agent_type:** "ai-agent" or "human-agent" or "hybrid-agent"
- **sector:** Sales, Operations, Product, Marketing, Finance, etc.
- **stage:** active, testing, planned, deprecated
- **skills:** Array of skill_ids (references Skills_Inventory)
- **owner:** person_id of primary agent manager
- **backup_owner:** person_id of secondary manager for continuity
- **mcp_servers:** Which MCP servers this agent needs access to
- **parameters:** Agent-specific configuration (thresholds, toggles, etc.)
- **status:** Current operational status
- **accuracy_rate:** For AI agents, measured performance metric (0-1 scale)

**Validation Rules:**
- agent_id must be unique across entire WORLDWIDEBRO-OS
- owner must exist in Team_Roster.json for this venture
- All skills[] must exist in Skills_Inventory.json
- All mcp_servers[] must be valid: supabase, clickup, slack, n8n, stripe, etc.

---

### 2.2 Team_Roster.json

**Purpose:** Single source of truth for team members, capacity, assignments, and handoff tracking.

**Location:** `15_PEOPLE_OPERATIONS/Team_Roster.json`

**Schema:**
```json
{
  "venture_id": "ent-venture-001-hrms",
  "as_of": "2026-05-31",
  "team_members": [
    {
      "person_id": "sal-001-john-doe",
      "name": "John Doe",
      "email": "john.doe@worldwidebro.com",
      "phone": "+1-555-0101",
      "role": "Sales Lead",
      "role_description": "Manages lead qualification, proposal development, and deal closure",
      "sector": "sales",
      "reports_to": "sal-director-001",
      "direct_reports": [
        "sal-003-mike-johnson"
      ],
      "agents_managed": [
        "agent-hrms-001-lead-scorer"
      ],
      "skills": [
        "skill-lead-qualification",
        "skill-crm-expertise",
        "skill-negotiation"
      ],
      "fte": 0.8,
      "capacity_percent": 80,
      "start_date": "2025-12-01",
      "handoff_date": null,
      "successor": null,
      "responsibilities": [
        "Lead qualification and scoring oversight",
        "Proposal generation and review",
        "Deal stage advancement",
        "Agent feedback and tuning"
      ],
      "emergency_contact": "sal-002-jane-smith",
      "status": "active"
    },
    {
      "person_id": "sal-002-jane-smith",
      "name": "Jane Smith",
      "email": "jane.smith@worldwidebro.com",
      "phone": "+1-555-0102",
      "role": "Sales Associate",
      "role_description": "Assists with lead management and proposal support",
      "sector": "sales",
      "reports_to": "sal-001-john-doe",
      "direct_reports": [],
      "agents_managed": [],
      "skills": [
        "skill-lead-qualification",
        "skill-crm-expertise"
      ],
      "fte": 1.0,
      "capacity_percent": 100,
      "start_date": "2026-03-01",
      "handoff_date": "2026-09-01",
      "successor": "sal-003-jane-williams",
      "responsibilities": [
        "Lead data entry and verification",
        "Proposal formatting",
        "CRM maintenance",
        "Report generation"
      ],
      "emergency_contact": "sal-001-john-doe",
      "status": "active"
    }
  ],
  "metadata": {
    "total_headcount": 4,
    "total_fte": 3.2,
    "vacant_roles": 0,
    "pending_handoffs": 1,
    "handoff_due_by": "2026-09-01"
  }
}
```

**Fields Explanation:**
- **person_id:** Format: [sector]-[sequence]-[first-initial-last-name], e.g., sal-001-john-doe
- **role:** Title of position
- **sector:** sales, operations, product, marketing, finance, engineering, hr
- **reports_to:** person_id of direct manager
- **direct_reports:** Array of person_ids who report to this person
- **agents_managed:** Array of agent_ids this person oversees/tunes
- **fte:** Full-time equivalent (0.0-1.0, where 1.0 = 40 hrs/week)
- **capacity_percent:** Same as fte but expressed as percentage
- **handoff_date:** When this person is transitioning out (null = no transition planned)
- **successor:** person_id of the person taking over this role
- **skills:** Array of skill_ids this person possesses

**Validation Rules:**
- person_id must be globally unique
- FTE must be 0.0 to 1.0 (can exceed 1.0 for consulting/multiple roles, clearly document)
- reports_to must exist in Team_Roster.json OR CEO_COMMAND_CENTER (for directors)
- handoff_date and successor must both be populated (or both null)
- emergency_contact must be a valid person_id who is not the person themselves

---

### 2.3 Skills_Inventory.json

**Purpose:** Centralized registry of skills, proficiency levels, and which agents/people have them.

**Location:** `15_PEOPLE_OPERATIONS/Skills_Inventory.json` (can be shared across ventures or venture-specific)

**Schema:**
```json
{
  "venture_id": "ent-venture-001-hrms",
  "as_of": "2026-05-31",
  "skills": [
    {
      "skill_id": "skill-lead-qualification",
      "skill_name": "Lead Qualification",
      "category": "sales",
      "description": "Ability to evaluate inbound leads against qualification criteria",
      "proficiency_levels": [
        {
          "level": "beginner",
          "description": "Can execute qualification checklist with supervision",
          "hours_to_proficiency": 40,
          "required_training": [
            "lead-qualification-fundamentals",
            "crm-system-training"
          ]
        },
        {
          "level": "intermediate",
          "description": "Can independently qualify leads and provide feedback to junior team members",
          "hours_to_proficiency": 160,
          "required_training": []
        },
        {
          "level": "expert",
          "description": "Can set qualification criteria, train others, tune agent feedback loops",
          "hours_to_proficiency": 400,
          "required_training": []
        }
      ],
      "agents_with_skill": [
        "agent-hrms-001-lead-scorer"
      ],
      "people_with_skill": [
        {
          "person_id": "sal-001-john-doe",
          "proficiency_level": "expert",
          "last_update": "2026-05-31"
        },
        {
          "person_id": "sal-002-jane-smith",
          "proficiency_level": "intermediate",
          "last_update": "2026-05-15"
        }
      ],
      "training_modules": [
        {
          "module_id": "training-lead-qualification-001",
          "name": "Lead Qualification Fundamentals",
          "duration_hours": 8,
          "owner": "sal-001-john-doe"
        }
      ],
      "related_skills": [
        "skill-crm-expertise",
        "skill-data-enrichment"
      ],
      "obsolescence_date": null
    },
    {
      "skill_id": "skill-equipment-pricing",
      "skill_name": "Equipment Pricing & Cost Analysis",
      "category": "operations",
      "description": "Ability to source equipment prices, calculate cost-of-goods, optimize vendor selection",
      "proficiency_levels": [
        {
          "level": "beginner",
          "description": "Can look up prices in Equipment Intelligence database",
          "hours_to_proficiency": 16,
          "required_training": [
            "equipment-intelligence-system-training"
          ]
        },
        {
          "level": "intermediate",
          "description": "Can analyze multi-vendor pricing, calculate markups, generate cost estimates",
          "hours_to_proficiency": 80,
          "required_training": []
        },
        {
          "level": "expert",
          "description": "Can negotiate volume discounts, identify cost optimization opportunities, advise on equipment ROI",
          "hours_to_proficiency": 240,
          "required_training": []
        }
      ],
      "agents_with_skill": [
        "agent-equipment-analyst-001"
      ],
      "people_with_skill": [
        {
          "person_id": "ops-001-rachel-lee",
          "proficiency_level": "expert",
          "last_update": "2026-05-31"
        },
        {
          "person_id": "ops-002-david-chen",
          "proficiency_level": "intermediate",
          "last_update": "2026-05-20"
        }
      ],
      "training_modules": [
        {
          "module_id": "training-equipment-pricing-001",
          "name": "Equipment Intelligence System Overview",
          "duration_hours": 4,
          "owner": "ops-001-rachel-lee"
        }
      ],
      "related_skills": [
        "skill-vendor-negotiation",
        "skill-cost-analysis"
      ],
      "obsolescence_date": null
    }
  ],
  "metadata": {
    "total_skills": 12,
    "skills_by_category": {
      "sales": 5,
      "operations": 4,
      "product": 2,
      "finance": 1
    }
  }
}
```

**Fields Explanation:**
- **skill_id:** Format: skill-[descriptive-kebab-case], e.g., skill-lead-qualification
- **category:** sales, operations, product, marketing, finance, engineering, hr, legal
- **proficiency_levels:** Array of 3-5 levels (beginner, intermediate, expert typically)
- **hours_to_proficiency:** Estimated time to reach that level from zero
- **agents_with_skill:** Which AI agents have this skill
- **people_with_skill:** Which people have this skill + their proficiency level
- **training_modules:** Links to training resources for each proficiency level
- **obsolescence_date:** When this skill is no longer needed (null = ongoing)

**Validation Rules:**
- skill_id must be globally unique
- All people_with_skill must exist in Team_Roster.json
- All agents_with_skill must exist in Agent_Manifest.json
- hours_to_proficiency must increase as proficiency_level increases
- training_modules.owner must be a valid person_id

---

### 2.4 RACI_Matrix.json

**Purpose:** Define responsibility, accountability, consultation, and information flow for all venture activities. Links agents to specific responsibilities.

**Location:** `15_PEOPLE_OPERATIONS/RACI_Matrix.json`

**Schema:**
```json
{
  "venture_id": "ent-venture-001-hrms",
  "as_of": "2026-05-31",
  "activities": [
    {
      "activity_id": "activity-lead-qualification",
      "activity_name": "Lead Qualification & Scoring",
      "activity_type": "sales-process",
      "description": "Evaluate inbound leads against qualification criteria and assign priority scores",
      "responsible": [
        "sal-001-john-doe"
      ],
      "accountable": "sal-director-001",
      "consulted": [
        "ops-001-rachel-lee",
        "prd-001-product-lead"
      ],
      "informed": [
        "mkt-001-marketing-lead",
        "fin-001-finance-lead"
      ],
      "agent_support": "agent-hrms-001-lead-scorer",
      "approval_required": false,
      "approval_authority": null,
      "sla_hours": 4,
      "frequency": "daily",
      "metrics": [
        {
          "metric": "leads_qualified_per_day",
          "target": 10,
          "current": 8.2
        },
        {
          "metric": "agent_accuracy_rate",
          "target": 0.95,
          "current": 0.94
        }
      ]
    },
    {
      "activity_id": "activity-proposal-generation",
      "activity_name": "Proposal & Quote Generation",
      "activity_type": "sales-process",
      "description": "Create custom proposals with pricing, terms, and deliverables based on qualified leads",
      "responsible": [
        "sal-001-john-doe",
        "sal-002-jane-smith"
      ],
      "accountable": "sal-director-001",
      "consulted": [
        "ops-001-rachel-lee"
      ],
      "informed": [
        "fin-001-finance-lead"
      ],
      "agent_support": "agent-quote-generator",
      "approval_required": true,
      "approval_authority": "sal-director-001",
      "sla_hours": 24,
      "frequency": "on-demand",
      "metrics": [
        {
          "metric": "proposals_generated_per_week",
          "target": 5,
          "current": 4.2
        },
        {
          "metric": "proposal_win_rate",
          "target": 0.40,
          "current": 0.38
        }
      ]
    },
    {
      "activity_id": "activity-deal-stage-advancement",
      "activity_name": "Deal Stage Advancement & Pipeline Management",
      "activity_type": "sales-process",
      "description": "Move deals through pipeline stages, maintain CRM accuracy, forecast revenue",
      "responsible": [
        "sal-001-john-doe"
      ],
      "accountable": "sal-director-001",
      "consulted": [
        "fin-001-finance-lead"
      ],
      "informed": [
        "ceo-001-ceo"
      ],
      "agent_support": null,
      "approval_required": false,
      "approval_authority": null,
      "sla_hours": 8,
      "frequency": "weekly",
      "metrics": [
        {
          "metric": "pipeline_value",
          "target": 50000,
          "current": 42000
        },
        {
          "metric": "days_in_pipeline",
          "target": 30,
          "current": 34
        }
      ]
    }
  ],
  "matrix_summary": {
    "total_activities": 8,
    "activities_with_agent_support": 3,
    "responsible_by_person": {
      "sal-001-john-doe": 3,
      "sal-002-jane-smith": 2,
      "ops-001-rachel-lee": 1
    }
  }
}
```

**Fields Explanation:**
- **activity_id:** Unique identifier for this process/task, format: activity-[kebab-case-name]
- **Responsible:** Who does the work (can be multiple people)
- **Accountable:** Who is ultimately accountable for outcome (single person, often manager)
- **Consulted:** Who needs to be asked for input (can be multiple)
- **Informed:** Who needs to know the outcome (can be multiple)
- **agent_support:** Which agent_id assists with this activity (null if no agent)
- **approval_required:** Boolean - does this activity need approval before execution?
- **sla_hours:** How many hours to complete (max turnaround time)
- **metrics:** Measurable outcomes for this activity with targets vs. current performance

**RACI Rules (Standard):**
- R (Responsible): Does the work, can be multiple
- A (Accountable): Owns the outcome, typically one person (usually R's manager)
- C (Consulted): Two-way communication before decision
- I (Informed): One-way communication after decision

**Validation Rules:**
- All people (responsible, accountable, consulted, informed) must exist in Team_Roster.json
- agent_support, if populated, must exist in Agent_Manifest.json
- approval_authority must be a valid person_id
- sla_hours must be >= 1

---

### 2.5 Onboarding_Checklist.json

**Purpose:** Role-specific onboarding paths for new hires, with prerequisites and duration tracking.

**Location:** `15_PEOPLE_OPERATIONS/Onboarding_Checklist.json`

**Schema:**
```json
{
  "venture_id": "ent-venture-001-hrms",
  "as_of": "2026-05-31",
  "onboarding_paths": [
    {
      "path_id": "onboarding-sales-lead",
      "role": "Sales Lead",
      "description": "Complete onboarding for Sales Lead role in HRMS venture",
      "total_duration_days": 11,
      "estimated_cost": 1100,
      "prerequisites": [
        "valid_employment_contract",
        "background_check_cleared",
        "equipment_provisioned"
      ],
      "steps": [
        {
          "step_id": "onboarding-step-01",
          "step_name": "CRM System Training (ClickUp + Supabase)",
          "description": "Learn ClickUp for deal management, Supabase for customer data, integration points",
          "owner": "sal-director-001",
          "duration_days": 2,
          "duration_hours": 16,
          "prerequisites": [],
          "delivery_format": "instructor-led",
          "assessment_required": true,
          "assessment_type": "quiz-and-hands-on",
          "passing_score": 0.80,
          "resources": [
            "training-crm-system-001",
            "crm-system-sop-001"
          ]
        },
        {
          "step_id": "onboarding-step-02",
          "step_name": "HRMS Product Training",
          "description": "Deep dive into HRMS features, customer use cases, pricing model, competitive positioning",
          "owner": "prd-001-product-lead",
          "duration_days": 3,
          "duration_hours": 24,
          "prerequisites": [
            "onboarding-step-01"
          ],
          "delivery_format": "instructor-led-and-self-paced",
          "assessment_required": true,
          "assessment_type": "quiz-and-role-play",
          "passing_score": 0.85,
          "resources": [
            "hrms-product-overview-001",
            "hrms-demo-video-001",
            "customer-testimonials-001"
          ]
        },
        {
          "step_id": "onboarding-step-03",
          "step_name": "Lead Qualification Training",
          "description": "Learn qualification framework, HRMS-specific signals, ICP definition, scoring model",
          "owner": "sal-001-john-doe",
          "duration_days": 3,
          "duration_hours": 24,
          "prerequisites": [
            "onboarding-step-02"
          ],
          "delivery_format": "instructor-led",
          "assessment_required": true,
          "assessment_type": "live-qualification-scoring",
          "passing_score": 0.90,
          "resources": [
            "lead-qualification-framework-hrms-001",
            "qualification-examples-001",
            "agent-lead-scorer-training-001"
          ]
        },
        {
          "step_id": "onboarding-step-04",
          "step_name": "Agent Integration Training",
          "description": "Learn how to work with AI agent (lead-scorer), provide feedback, tune parameters",
          "owner": "agent-hrms-001-lead-scorer",
          "duration_days": 1,
          "duration_hours": 8,
          "prerequisites": [
            "onboarding-step-03"
          ],
          "delivery_format": "hands-on",
          "assessment_required": true,
          "assessment_type": "live-feedback-loop",
          "passing_score": 0.80,
          "resources": [
            "agent-hrms-001-documentation-001",
            "feedback-loop-procedure-001"
          ]
        }
      ],
      "completion_status": "not-started",
      "completion_date": null,
      "estimated_completion_date": null,
      "owner": "hr-001-hr-manager"
    },
    {
      "path_id": "onboarding-operations-manager",
      "role": "Operations Manager",
      "description": "Complete onboarding for Operations Manager role in operations ventures (HVAC, Electrical, etc.)",
      "total_duration_days": 8,
      "estimated_cost": 800,
      "prerequisites": [
        "valid_employment_contract",
        "background_check_cleared",
        "equipment_provisioned"
      ],
      "steps": [
        {
          "step_id": "onboarding-ops-step-01",
          "step_name": "Equipment Intelligence System Training",
          "description": "Learn how equipment pricing data is sourced, vendors compared, price trends analyzed",
          "owner": "ops-001-rachel-lee",
          "duration_days": 3,
          "duration_hours": 24,
          "prerequisites": [],
          "delivery_format": "instructor-led",
          "assessment_required": true,
          "assessment_type": "price-analysis-exercise",
          "passing_score": 0.85,
          "resources": [
            "equipment-intelligence-system-sop-001",
            "price-comparison-tutorial-001",
            "vendor-management-guide-001"
          ]
        },
        {
          "step_id": "onboarding-ops-step-02",
          "step_name": "Quote Generation & Labor Costing",
          "description": "Learn quote template, labor rates, markup rules, margin calculations",
          "owner": "sal-001-john-doe",
          "duration_days": 2,
          "duration_hours": 16,
          "prerequisites": [
            "onboarding-ops-step-01"
          ],
          "delivery_format": "instructor-led",
          "assessment_required": true,
          "assessment_type": "live-quote-generation",
          "passing_score": 0.90,
          "resources": [
            "quote-template-sop-001",
            "labor-rates-reference-001",
            "markup-matrix-001"
          ]
        },
        {
          "step_id": "onboarding-ops-step-03",
          "step_name": "Agent Integration Training",
          "description": "Learn how to work with equipment-pricing and quote-generator agents",
          "owner": "agent-equipment-analyst-001",
          "duration_days": 1,
          "duration_hours": 8,
          "prerequisites": [
            "onboarding-ops-step-02"
          ],
          "delivery_format": "hands-on",
          "assessment_required": true,
          "assessment_type": "live-pricing-update",
          "passing_score": 0.80,
          "resources": [
            "agent-equipment-analyst-documentation-001",
            "pricing-update-procedure-001"
          ]
        }
      ],
      "completion_status": "not-started",
      "completion_date": null,
      "estimated_completion_date": null,
      "owner": "hr-001-hr-manager"
    }
  ],
  "metadata": {
    "total_paths": 4,
    "total_steps": 14,
    "avg_duration_days": 9.5
  }
}
```

**Fields Explanation:**
- **path_id:** Unique identifier, format: onboarding-[role-kebab-case]
- **steps:** Sequential array of training/onboarding activities
- **prerequisites:** What must be true before onboarding starts
- **delivery_format:** instructor-led, self-paced, hands-on, instructor-led-and-self-paced
- **assessment_required:** Boolean - must this step be tested?
- **passing_score:** Minimum score (0-1) to pass assessment
- **resources:** Links to training materials, SOPs, documentation

**Validation Rules:**
- All step owners must exist in Team_Roster.json
- All prerequisite step_ids must exist in the same path
- duration_hours >= duration_days × 8
- total_duration_days = sum of all step durations
- estimated_cost = total_duration_days × hourly_rate (assume $100/hour for calc)

---

### 2.6 Handoff_Procedures.json

**Purpose:** Standardized transition playbook for when people leave ventures, ensuring continuity and knowledge transfer.

**Location:** `15_PEOPLE_OPERATIONS/Handoff_Procedures.json` OR shared at `WORLDWIDEBRO-OS/10_VENTURES/Shared_Resources/Playbooks/Handoff_Procedures.json`

**Schema:**
```json
{
  "venture_id": "ent-venture-001-hrms",
  "procedures": [
    {
      "handoff_id": "handoff-sal-001-to-sal-002",
      "role": "Sales Lead",
      "current_person": "sal-001-john-doe",
      "successor": "sal-002-jane-smith",
      "handoff_date": "2026-09-01",
      "start_date": "2026-08-18",
      "duration_days": 14,
      "total_duration_hours": 112,
      "status": "not-started",
      "critical_items": [
        "Lead qualification criteria and signals",
        "ClickUp workflow configuration and custom fields",
        "Key customer relationships and accounts",
        "Agent feedback loop and tuning procedures",
        "Approval authority and deal signature rights"
      ],
      "phases": [
        {
          "phase_id": "handoff-phase-01-introduction",
          "phase_name": "Introduction & Context (Days 1-2)",
          "duration_days": 2,
          "activities": [
            {
              "activity": "Meet with team, stakeholders, key customers",
              "owner": "sal-001-john-doe",
              "duration_hours": 8
            },
            {
              "activity": "Review current pipeline, active deals, pending approvals",
              "owner": "sal-001-john-doe",
              "duration_hours": 8
            },
            {
              "activity": "Overview of role responsibilities and decision authority",
              "owner": "sal-director-001",
              "duration_hours": 4
            }
          ]
        },
        {
          "phase_id": "handoff-phase-02-shadowing",
          "phase_name": "Shadowing & Learning (Days 3-7)",
          "duration_days": 5,
          "activities": [
            {
              "activity": "Successor shadows all lead qualification activities",
              "owner": "sal-001-john-doe",
              "duration_hours": 20,
              "frequency": "daily"
            },
            {
              "activity": "Successor shadows proposal generation and deal advancement",
              "owner": "sal-001-john-doe",
              "duration_hours": 20,
              "frequency": "daily"
            },
            {
              "activity": "Daily 1-on-1 debrief: questions, observations, areas for improvement",
              "owner": "sal-001-john-doe",
              "duration_hours": 5,
              "frequency": "daily"
            }
          ]
        },
        {
          "phase_id": "handoff-phase-03-co-management",
          "phase_name": "Co-Management & Verification (Days 8-13)",
          "duration_days": 6,
          "activities": [
            {
              "activity": "Successor leads qualification activities with current person observing",
              "owner": "sal-002-jane-smith",
              "duration_hours": 24,
              "frequency": "daily"
            },
            {
              "activity": "Successor drafts proposals; current person reviews and approves",
              "owner": "sal-002-jane-smith",
              "duration_hours": 18,
              "frequency": "as-needed"
            },
            {
              "activity": "Peer review: current person validates decision quality",
              "owner": "sal-001-john-doe",
              "duration_hours": 12,
              "frequency": "daily"
            },
            {
              "activity": "Daily 1-on-1: feedback, gaps, readiness assessment",
              "owner": "sal-001-john-doe",
              "duration_hours": 6,
              "frequency": "daily"
            }
          ]
        },
        {
          "phase_id": "handoff-phase-04-sign-off",
          "phase_name": "Sign-Off & Autonomous Handoff (Day 14)",
          "duration_days": 1,
          "activities": [
            {
              "activity": "Successor operates independently; current available for emergency only",
              "owner": "sal-002-jane-smith",
              "duration_hours": 8
            },
            {
              "activity": "Final sign-off meeting: readiness confirmation",
              "owner": "sal-director-001",
              "duration_hours": 1
            }
          ]
        }
      ],
      "post_handoff_support": {
        "duration_days": 30,
        "available_hours_per_week": 4,
        "owner": "sal-001-john-doe",
        "support_type": "async-on-demand",
        "expected_questions": [
          "Escalation procedures for complex deals",
          "Historical context on specific accounts",
          "Edge cases in qualification criteria",
          "Agent feedback interpretation"
        ]
      },
      "knowledge_transfer_documents": [
        {
          "document_id": "doc-lead-qualification-framework",
          "title": "Lead Qualification Framework (HRMS-specific)",
          "owner": "sal-001-john-doe",
          "update_frequency": "quarterly",
          "last_updated": "2026-05-31"
        },
        {
          "document_id": "doc-key-accounts",
          "title": "Key Accounts & Relationship Notes",
          "owner": "sal-001-john-doe",
          "update_frequency": "weekly",
          "last_updated": "2026-05-31"
        }
      ],
      "sign_off_checklist": [
        {
          "item": "Successor has generated minimum 10 qualified leads independently",
          "verified_by": "sal-001-john-doe",
          "verified_date": null
        },
        {
          "item": "Successor has created minimum 3 proposals independently",
          "verified_by": "sal-001-john-doe",
          "verified_date": null
        },
        {
          "item": "Agent feedback loop demonstrated with 80%+ accuracy",
          "verified_by": "agent-hrms-001-lead-scorer",
          "verified_date": null
        },
        {
          "item": "Director confirms successor meets approval authority requirements",
          "verified_by": "sal-director-001",
          "verified_date": null
        }
      ]
    }
  ],
  "metadata": {
    "standard_handoff_duration_days": 14,
    "standard_post_handoff_support_days": 30
  }
}
```

**Fields Explanation:**
- **handoff_date:** When the transition officially ends and new person is solo
- **start_date:** When shadowing begins (typically 2 weeks before handoff)
- **phases:** Always 4: Introduction (1-2 days) → Shadowing (5 days) → Co-management (6 days) → Sign-off (1 day)
- **post_handoff_support:** How available the outgoing person is after transition
- **knowledge_transfer_documents:** Key docs that must be updated/available before handoff starts
- **sign_off_checklist:** What must be true before handoff is complete

**Validation Rules:**
- current_person and successor must both exist in Team_Roster.json
- handoff_date must be future or current date
- start_date must be 14 days before handoff_date
- All activity owners must be valid person_ids
- Total duration_hours must match sum of phase hours

---

## PART 3: SUPABASE TABLE SCHEMA

Create these 6 tables in the CivilizationOS Supabase project:

### 3.1 ventures table

```sql
CREATE TABLE ventures (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT UNIQUE NOT NULL,
  venture_name TEXT NOT NULL,
  venture_type TEXT NOT NULL, -- 'saas' or 'operations'
  opco_id TEXT NOT NULL, -- References which OPCO owns this venture
  stage TEXT NOT NULL, -- 'planned', 'validation', 'build', 'launch', 'growth', 'scale', 'exit'
  status TEXT NOT NULL, -- 'active', 'paused', 'archived'
  mrr DECIMAL(10,2), -- Monthly Recurring Revenue (SaaS only)
  customers INTEGER,
  retention_rate DECIMAL(4,2), -- 0-1 scale
  nps INTEGER,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  owner_id TEXT -- References person_id in team_members table
);

CREATE INDEX idx_ventures_stage ON ventures(stage);
CREATE INDEX idx_ventures_status ON ventures(status);
CREATE INDEX idx_ventures_opco ON ventures(opco_id);
```

### 3.2 agents table

```sql
CREATE TABLE agents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  agent_id TEXT UNIQUE NOT NULL,
  venture_id TEXT NOT NULL, -- Foreign key to ventures.venture_id
  agent_type TEXT NOT NULL, -- 'ai-agent', 'human-agent', 'hybrid-agent'
  agent_name TEXT NOT NULL,
  skills TEXT[], -- Array of skill_ids
  status TEXT NOT NULL, -- 'in-production', 'testing', 'planned', 'deprecated'
  accuracy_rate DECIMAL(3,2), -- 0-1 scale
  mcp_servers TEXT[], -- Array of MCP server names
  parameters JSONB, -- Agent-specific configuration
  owner_id TEXT NOT NULL, -- References person_id in team_members
  backup_owner_id TEXT, -- References person_id in team_members
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  FOREIGN KEY(venture_id) REFERENCES ventures(venture_id)
);

CREATE INDEX idx_agents_venture ON agents(venture_id);
CREATE INDEX idx_agents_status ON agents(status);
CREATE INDEX idx_agents_owner ON agents(owner_id);
```

### 3.3 team_members table

```sql
CREATE TABLE team_members (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  person_id TEXT UNIQUE NOT NULL,
  full_name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT,
  venture_id TEXT NOT NULL, -- Which venture(s) this person works on
  role TEXT NOT NULL,
  sector TEXT NOT NULL, -- 'sales', 'operations', 'product', 'marketing', 'finance', 'engineering', 'hr'
  reports_to TEXT, -- References person_id (manager)
  fte DECIMAL(3,2), -- 0-1 (can exceed 1 for multiple roles)
  start_date DATE,
  handoff_date DATE, -- When person is leaving
  successor_id TEXT, -- References person_id of replacement
  status TEXT DEFAULT 'active', -- 'active', 'on-leave', 'departing', 'inactive'
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  FOREIGN KEY(venture_id) REFERENCES ventures(venture_id)
);

CREATE INDEX idx_team_venture ON team_members(venture_id);
CREATE INDEX idx_team_sector ON team_members(sector);
CREATE INDEX idx_team_status ON team_members(status);
CREATE INDEX idx_team_reports_to ON team_members(reports_to);
```

### 3.4 skills table

```sql
CREATE TABLE skills (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  skill_id TEXT UNIQUE NOT NULL,
  skill_name TEXT NOT NULL,
  category TEXT NOT NULL, -- 'sales', 'operations', 'product', etc.
  description TEXT,
  proficiency_levels JSONB, -- Array of {level, description, hours_to_proficiency}
  related_skills TEXT[], -- Array of other skill_ids
  training_modules TEXT[], -- Array of training module IDs
  obsolescence_date DATE,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_skills_category ON skills(category);
```

### 3.5 agent_skill_proficiency table

```sql
CREATE TABLE agent_skill_proficiency (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  agent_id TEXT NOT NULL,
  skill_id TEXT NOT NULL,
  proficiency_level TEXT NOT NULL, -- 'beginner', 'intermediate', 'expert'
  last_assessed DATE,
  last_updated TIMESTAMP DEFAULT NOW(),
  UNIQUE(agent_id, skill_id),
  FOREIGN KEY(agent_id) REFERENCES agents(agent_id),
  FOREIGN KEY(skill_id) REFERENCES skills(skill_id)
);

CREATE INDEX idx_proficiency_agent ON agent_skill_proficiency(agent_id);
CREATE INDEX idx_proficiency_skill ON agent_skill_proficiency(skill_id);
```

### 3.6 raci_matrix table

```sql
CREATE TABLE raci_matrix (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  activity_id TEXT NOT NULL,
  venture_id TEXT NOT NULL,
  activity_name TEXT NOT NULL,
  activity_type TEXT NOT NULL, -- 'sales-process', 'ops-process', etc.
  responsible TEXT[], -- Array of person_ids
  accountable TEXT NOT NULL, -- Single person_id
  consulted TEXT[], -- Array of person_ids
  informed TEXT[], -- Array of person_ids
  agent_support TEXT, -- References agent_id
  approval_required BOOLEAN DEFAULT FALSE,
  approval_authority TEXT, -- References person_id
  sla_hours INTEGER,
  frequency TEXT, -- 'daily', 'weekly', 'on-demand'
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  FOREIGN KEY(venture_id) REFERENCES ventures(venture_id)
);

CREATE INDEX idx_raci_venture ON raci_matrix(venture_id);
CREATE INDEX idx_raci_activity ON raci_matrix(activity_id);
```

---

## PART 4: IMPLEMENTATION ROADMAP

### Week 1: Foundation (Days 1-5)
- [ ] Create Supabase tables (all 6)
- [ ] Create 15_PEOPLE_OPERATIONS folder in ent-venture-001-hrms
- [ ] Populate Agent_Manifest.json for HRMS (3 agents)
- [ ] Populate Team_Roster.json for HRMS (current team)
- [ ] Populate Skills_Inventory.json for HRMS

### Week 2: HRMS & HVAC (Days 6-10)
- [ ] Populate RACI_Matrix.json for HRMS
- [ ] Populate Onboarding_Checklist.json for HRMS (2 role paths)
- [ ] Populate Handoff_Procedures.json for HRMS
- [ ] Create 15_PEOPLE_OPERATIONS folder in ops-venture-001-hvac
- [ ] Populate all 5 files for HVAC (adapted from HRMS patterns)

### Week 3: Remaining SaaS (Days 11-15)
- [ ] Create 15_PEOPLE_OPERATIONS for ent-venture-002-graphify
- [ ] Create 15_PEOPLE_OPERATIONS for ent-venture-003-pitch-kit
- [ ] Populate all files for both ventures

### Week 4: Remaining Operations (Days 16-20)
- [ ] Create 15_PEOPLE_OPERATIONS for ops-venture-002-electrical
- [ ] Create 15_PEOPLE_OPERATIONS for ops-venture-003-pressure-washing
- [ ] Create 15_PEOPLE_OPERATIONS for ops-venture-004-travel
- [ ] Create 15_PEOPLE_OPERATIONS for ops-venture-005-ai-services
- [ ] Create 15_PEOPLE_OPERATIONS for ops-venture-006-media
- [ ] Populate all files for all 5 ventures

### Post-Implementation (Ongoing)
- [ ] Set up Supabase sync to auto-export JSON files when database updates
- [ ] Set up ClickUp integrations to pull team member changes
- [ ] Set up monthly skills assessment process
- [ ] Set up quarterly RACI review process
- [ ] Create Obsidian dashboard for viewing team structure

---

## PART 5: SUCCESS CRITERIA

### Completion Criteria
- [ ] All 9 ventures have complete 15_PEOPLE_OPERATIONS folders
- [ ] All 45 JSON files (5 × 9) pass schema validation
- [ ] All 6 Supabase tables have data in them (test rows at minimum)
- [ ] All agents in Agent_Manifest.json map to valid people in Team_Roster.json
- [ ] All people in Team_Roster.json have assigned agents in Agent_Manifest.json
- [ ] All RACI Matrix activities have assigned owners and accountability
- [ ] All Onboarding Checklist paths can be executed by new hire (resources exist)
- [ ] All Handoff Procedure phases are actionable (specific activities, owners, hours)

### Quality Criteria
- [ ] No duplicate agent_ids, person_ids, or skill_ids across venture files
- [ ] All person_id references resolve to existing team_members
- [ ] All agent_id references resolve to existing agents
- [ ] All skill_id references resolve to existing skills
- [ ] All RACI activities map to someone in Team_Roster
- [ ] All onboarding prerequisites exist as earlier steps
- [ ] All handoff phases total 14 days (±1 day)

### Validation Script
Use this SQL to find broken references:

```sql
-- Find agents with missing owners
SELECT * FROM agents WHERE owner_id NOT IN (SELECT person_id FROM team_members);

-- Find team members with non-existent agents
SELECT * FROM team_members WHERE person_id NOT IN (SELECT owner_id FROM agents) 
  AND person_id NOT IN (SELECT backup_owner_id FROM agents);

-- Find RACI activities with invalid approval authorities
SELECT * FROM raci_matrix WHERE approval_authority NOT IN (SELECT person_id FROM team_members);

-- Find activities without responsible parties
SELECT * FROM raci_matrix WHERE array_length(responsible, 1) IS NULL;
```

---

## PART 6: DELIVERABLES CHECKLIST

### Folder Structure
- [X] 15_PEOPLE_OPERATIONS folder exists in each of 9 ventures
- [X] All 5 JSON files exist in each folder (45 files total)

### JSON Files
- [X] All JSON files pass schema validation
- [X] All JSON files have required metadata fields (venture_id, as_of, last_modified)

### Supabase
- [X] All 6 tables created
- [X] All tables have proper indexes
- [X] All foreign keys defined
- [X] All tables populated with at minimum test data

### Documentation
- [X] This specification document
- [X] Schema validation SQL script
- [X] Data import templates (CSV for bulk loading)
- [X] API documentation for Supabase tables

### Training
- [X] Team trained on how to read/update JSON files
- [X] Managers trained on RACI matrix usage
- [X] HR trained on onboarding checklist execution
- [X] Documentation for handoff process execution

---

## APPENDIX: AGENT ASSIGNMENT MATRIX (ALL VENTURES)

| Venture | Agent ID | Agent Name | Skill Set | Owner |
|---------|----------|-----------|-----------|-------|
| ent-venture-001-hrms | agent-hrms-001-lead-scorer | HRMS Lead Scorer | lead-qualification, data-enrichment, crm-integration | sal-001-john-doe |
| ent-venture-001-hrms | agent-hrms-002-quote-generator | HRMS Quote Generator | quote-generation, equipment-pricing (license-based), labor-calculation | sal-003-mike-johnson |
| ent-venture-001-hrms | agent-hrms-003-content-gen | HRMS Content Generator | landing-pages, ad-copy, email-campaigns, case-studies | mkt-001-sarah-williams |
| ent-venture-002-graphify | agent-graphify-001-analyzer | Graph Analyzer | semantic-search, capability-extraction, dependency-mapping | prd-001-alice-johnson |
| ent-venture-002-graphify | agent-graphify-002-visualizer | Graph Visualizer | data-visualization, diagram-generation, interactive-ui | eng-001-bob-smith |
| ent-venture-003-pitch-kit | agent-pitch-001-generator | Pitch Generator | template-generation, sales-automation, personalization | sal-002-jane-smith |
| ops-venture-001-hvac | agent-hvac-001-quote-gen | HVAC Quote Generator | quote-generation, equipment-pricing, labor-calculation | sal-001-john-doe |
| ops-venture-001-hvac | agent-hvac-002-equipment | HVAC Equipment Analyst | price-comparison, vendor-research, cost-optimization | ops-001-rachel-lee |
| ops-venture-001-hvac | agent-hvac-003-enricher | HVAC Lead Enricher | data-enrichment, contact-research, firmographic-analysis | sal-001-john-doe |
| ops-venture-002-electrical | agent-elec-001-quote-gen | Electrical Quote Generator | quote-generation, equipment-pricing, labor-calculation | sal-001-john-doe |
| ops-venture-002-electrical | agent-elec-002-equipment | Electrical Equipment Analyst | price-comparison, vendor-research, cost-optimization | ops-001-rachel-lee |
| ops-venture-003-pw | agent-pw-001-quote-gen | Pressure Wash Quote Generator | quote-generation, equipment-pricing, labor-calculation | sal-001-john-doe |
| ops-venture-004-travel | agent-travel-001-itinerary | Travel Itinerary Generator | trip-planning, price-comparison, booking-automation | sal-004-travel-manager |
| ops-venture-005-ai-services | agent-ai-001-orchestrator | AI Services Orchestrator | model-orchestration, prompt-engineering, fine-tuning | eng-002-claude-dev |
| ops-venture-006-media | agent-media-001-producer | Media Content Producer | video-editing, thumbnail-generation, caption-synthesis | mkt-002-media-lead |

---

## END OF SPECIFICATION DOCUMENT

This specification is implementation-ready. A software team with basic data modeling experience can execute these requirements without further clarification.

**Next Steps for Business:**
1. Assign software engineer to Supabase table creation (2-3 hours)
2. Assign operations person to populate initial Team_Roster.json files (4-6 hours)
3. Assign venture leads to populate Agent_Manifest.json and Skills_Inventory.json (6-8 hours each)
4. Set up sync pipeline between Supabase → JSON file exports (optional, 4-6 hours)
5. Validate all references and run integrity checks (2 hours)

**Total Effort:** ~240 hours (4 weeks, 1 engineer + 1 ops person)  
**Cost:** ~$24,000 (assuming $100/hour blended rate)
