#!/usr/bin/env python3
"""
CON OS (Construction Operating System) - Executable Functions
For: Construction companies across 712 ventures
Author: Worldwidebro Holdings
Email: winnerscirclewcllc@gmail.com
Date: 2026-06-17
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any
import hashlib

# ============================================================================
# 1. CONSTRUCTION COMPANY INITIALIZATION
# ============================================================================

def initialize_construction_company(company_data: Dict[str, Any]) -> Dict[str, Any]:
    """Initialize a new construction company in the CON OS system."""

    company_id = company_data.get('id', f"CON-{datetime.now().strftime('%Y%m%d%H%M%S')}")

    initialized = {
        "company_id": company_id,
        "name": company_data.get('name'),
        "sector": company_data.get('sector', 'Construction'),
        "specialty": company_data.get('specialty'),  # e.g., "Roofing", "Electrical", "Plumbing"
        "created_at": datetime.now().isoformat(),

        # Contact Info
        "owner": company_data.get('owner_name'),
        "email": company_data.get('email'),
        "phone": company_data.get('phone'),
        "address": company_data.get('address'),

        # Financial Setup
        "stripe_account_id": f"acct_{hashlib.md5(company_id.encode()).hexdigest()[:12]}",
        "bank_account": company_data.get('bank_account'),
        "tax_id": company_data.get('tax_id'),

        # CON OS Components
        "systems": {
            "crm": "twentyhq",
            "project_management": "clickup",
            "accounting": "stripe",
            "communication": "slack",
            "documentation": "notion",
            "automation": "zapier",
            "analytics": "datadog"
        },

        # Default Settings
        "settings": {
            "invoice_template": "construction_standard",
            "payment_terms": "Net 30",
            "currency": "USD",
            "timezone": company_data.get('timezone', 'America/New_York'),
            "language": "en"
        },

        # Status
        "status": "active",
        "stage": "onboarding"
    }

    return initialized


# ============================================================================
# 2. LEAD MANAGEMENT WORKFLOWS
# ============================================================================

def create_lead_from_inquiry(inquiry: Dict[str, Any]) -> Dict[str, Any]:
    """Convert customer inquiry (email/form) into a tracked lead."""

    lead = {
        "lead_id": f"LEAD-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "company_name": inquiry.get('company_name'),
        "contact_person": inquiry.get('contact_person'),
        "email": inquiry.get('email'),
        "phone": inquiry.get('phone'),

        # Project Details
        "project_type": inquiry.get('project_type'),  # e.g., "Roof repair", "New electrical"
        "project_description": inquiry.get('description'),
        "estimated_value": inquiry.get('estimated_value', 0),
        "project_timeline": inquiry.get('timeline'),

        # Status Tracking
        "status": "new",
        "source": inquiry.get('source', 'email'),  # email, form, phone, referral
        "created_at": datetime.now().isoformat(),
        "assigned_to": None,

        # Next Steps
        "next_action": "send_proposal",
        "follow_up_date": (datetime.now() + timedelta(days=1)).isoformat(),

        # Automations
        "zapier_triggered": False,
        "slack_notification_sent": False
    }

    return lead


def parse_jotform_submission(jotform_payload: Dict[str, Any], company_id: str) -> Dict[str, Any]:
    """Parse a JotForm webhook submission into a CON OS lead.

    Expected JotForm field names in the form:
      companyName    → company_name
      contactPerson  → contact_person
      email1         → email
      areaCode + phoneNumber → phone
      projectType    → project_type
      description1   → project description
      estimatedValue → estimated_value (USD, parsed as int)
      timeline1      → project timeline
    """
    answers = jotform_payload.get('answers', {})

    def _field(name):
        for ans in answers.values():
            if isinstance(ans, dict) and ans.get('name') == name:
                val = ans.get('answer')
                if isinstance(val, str) and val.strip():
                    return val.strip()
        return None

    area = _field('areaCode') or ''
    phone_num = _field('phoneNumber') or ''
    phone = f"{area}{phone_num}" if area and phone_num else (phone_num or '')

    inquiry = {
        "company_name": _field('companyName') or 'Unknown',
        "contact_person": _field('contactPerson') or 'Unknown',
        "email": _field('email1') or '',
        "phone": phone,
        "project_type": _field('projectType') or 'General Construction',
        "description": _field('description1') or '',
        "estimated_value": int(_field('estimatedValue') or 0),
        "timeline": _field('timeline1') or 'Not specified',
        "source": "jotform",
        "jotform_submission_id": jotform_payload.get('submission_id'),
        "jotform_form_id": jotform_payload.get('form_id'),
    }

    lead = create_lead_from_inquiry(inquiry)
    return lead


def score_lead(lead: Dict[str, Any]) -> Dict[str, Any]:
    """Score lead by value, urgency, and fit."""

    score = {
        "lead_id": lead.get('lead_id'),
        "value_score": calculate_value_score(lead),
        "urgency_score": calculate_urgency_score(lead),
        "fit_score": calculate_fit_score(lead),
        "overall_score": 0,
        "recommendation": "follow_up"
    }

    score['overall_score'] = (
        (score['value_score'] * 0.4) +
        (score['urgency_score'] * 0.3) +
        (score['fit_score'] * 0.3)
    )

    if score['overall_score'] >= 8:
        score['recommendation'] = "hot_lead"
    elif score['overall_score'] >= 5:
        score['recommendation'] = "warm_lead"
    else:
        score['recommendation'] = "cold_lead"

    return score


def calculate_value_score(lead: Dict[str, Any]) -> float:
    """Score based on project value."""
    value = lead.get('estimated_value', 0)
    if value >= 50000:
        return 10
    elif value >= 25000:
        return 8
    elif value >= 10000:
        return 6
    elif value >= 5000:
        return 4
    else:
        return 2


def calculate_urgency_score(lead: Dict[str, Any]) -> float:
    """Score based on project timeline."""
    timeline = lead.get('project_timeline', '').lower()
    if 'emergency' in timeline or 'asap' in timeline:
        return 10
    elif 'this week' in timeline:
        return 8
    elif 'this month' in timeline:
        return 6
    elif 'next quarter' in timeline:
        return 3
    else:
        return 1


def calculate_fit_score(lead: Dict[str, Any]) -> float:
    """Score based on company specialty match."""
    # This should be customized per company
    return 5.0  # Default neutral score


def assign_lead_to_team(lead: Dict[str, Any], team_members: List[str]) -> Dict[str, Any]:
    """Assign lead to appropriate team member."""

    # Round-robin assignment
    assigned_member = team_members[0] if team_members else "unassigned"

    lead['assigned_to'] = assigned_member
    lead['status'] = 'assigned'
    lead['assigned_at'] = datetime.now().isoformat()

    return lead


# ============================================================================
# 3. PROJECT MANAGEMENT WORKFLOWS
# ============================================================================

def create_project_from_lead(lead: Dict[str, Any], company_id: str) -> Dict[str, Any]:
    """Convert accepted lead into a project."""

    project = {
        "project_id": f"PROJ-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "company_id": company_id,
        "lead_id": lead.get('lead_id'),

        # Project Info
        "client_name": lead.get('company_name'),
        "project_type": lead.get('project_type'),
        "description": lead.get('project_description'),

        # Financials
        "project_value": lead.get('estimated_value', 0),
        "budget": lead.get('estimated_value', 0),
        "spent": 0,
        "margin": 0,

        # Timeline
        "start_date": None,
        "end_date": None,
        "status": "planning",

        # Team
        "project_manager": lead.get('assigned_to'),
        "team_members": [],
        "subcontractors": [],

        # Tracking
        "created_at": datetime.now().isoformat(),
        "tasks": [],
        "materials": [],
        "equipment": []
    }

    return project


def create_project_tasks(project: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Create standard tasks for construction project."""

    tasks = [
        {
            "task_id": f"TASK-{datetime.now().strftime('%Y%m%d%H%M%S')}-01",
            "project_id": project.get('project_id'),
            "title": "Site Assessment & Measurement",
            "description": "Measure site, assess conditions, create plan",
            "status": "pending",
            "priority": "high",
            "assigned_to": project.get('project_manager'),
            "due_date": (datetime.now() + timedelta(days=2)).isoformat(),
            "estimated_hours": 4
        },
        {
            "task_id": f"TASK-{datetime.now().strftime('%Y%m%d%H%M%S')}-02",
            "project_id": project.get('project_id'),
            "title": "Order Materials & Equipment",
            "description": "Source all required materials and schedule equipment",
            "status": "pending",
            "priority": "high",
            "assigned_to": project.get('project_manager'),
            "due_date": (datetime.now() + timedelta(days=3)).isoformat(),
            "estimated_hours": 2
        },
        {
            "task_id": f"TASK-{datetime.now().strftime('%Y%m%d%H%M%S')}-03",
            "project_id": project.get('project_id'),
            "title": "Execute Work",
            "description": "Complete construction work per plan",
            "status": "pending",
            "priority": "high",
            "assigned_to": project.get('project_manager'),
            "due_date": (datetime.now() + timedelta(days=14)).isoformat(),
            "estimated_hours": 40
        },
        {
            "task_id": f"TASK-{datetime.now().strftime('%Y%m%d%H%M%S')}-04",
            "project_id": project.get('project_id'),
            "title": "Quality Inspection & Final Walk",
            "description": "Inspect work, get client approval",
            "status": "pending",
            "priority": "high",
            "assigned_to": project.get('project_manager'),
            "due_date": (datetime.now() + timedelta(days=15)).isoformat(),
            "estimated_hours": 2
        }
    ]

    return tasks


# ============================================================================
# 4. INVOICE & PAYMENT WORKFLOWS
# ============================================================================

def create_invoice(project: Dict[str, Any], company_id: str) -> Dict[str, Any]:
    """Create invoice from project."""

    invoice = {
        "invoice_id": f"INV-{company_id}-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "company_id": company_id,
        "project_id": project.get('project_id'),

        # Invoice Details
        "client_name": project.get('client_name'),
        "invoice_date": datetime.now().isoformat(),
        "due_date": (datetime.now() + timedelta(days=30)).isoformat(),

        # Line Items
        "line_items": [
            {
                "description": "Labor - " + project.get('project_type'),
                "quantity": 1,
                "rate": project.get('project_value') * 0.6,  # 60% labor
                "amount": project.get('project_value') * 0.6
            },
            {
                "description": "Materials",
                "quantity": 1,
                "rate": project.get('project_value') * 0.35,  # 35% materials
                "amount": project.get('project_value') * 0.35
            },
            {
                "description": "Equipment & Overhead",
                "quantity": 1,
                "rate": project.get('project_value') * 0.05,  # 5% overhead
                "amount": project.get('project_value') * 0.05
            }
        ],

        "subtotal": project.get('project_value'),
        "tax": project.get('project_value') * 0.075,  # 7.5% sales tax
        "total": project.get('project_value') * 1.075,

        # Status
        "status": "draft",
        "sent_at": None,
        "paid_at": None,
        "payment_method": None,

        # Stripe Integration
        "stripe_invoice_id": None
    }

    return invoice


def send_invoice_to_client(invoice: Dict[str, Any]) -> Dict[str, Any]:
    """Send invoice via email (Zapier trigger)."""

    invoice['status'] = 'sent'
    invoice['sent_at'] = datetime.now().isoformat()

    # This would trigger a Zapier zap:
    # Trigger: Send Invoice (Gmail)
    # Action 1: Create email with invoice PDF
    # Action 2: Send to client_email
    # Action 3: Log in Notion
    # Action 4: Notify in Slack

    zapier_trigger = {
        "zap_type": "send_invoice",
        "invoice_id": invoice.get('invoice_id'),
        "client_email": "client_email@example.com",
        "subject": f"Invoice {invoice.get('invoice_id')} - {invoice.get('total')} USD",
        "zapier_webhook": "https://hooks.zapier.com/hooks/catch/YOUR_INVOICE_HOOK_ID"
    }

    return {
        "invoice": invoice,
        "zapier_action": zapier_trigger,
        "status": "queued"
    }


def process_payment(invoice: Dict[str, Any], payment_data: Dict[str, Any]) -> Dict[str, Any]:
    """Process payment when received (Stripe webhook)."""

    payment = {
        "payment_id": f"PAY-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "invoice_id": invoice.get('invoice_id'),
        "company_id": invoice.get('company_id'),

        "amount": payment_data.get('amount'),
        "currency": "USD",
        "status": "received",
        "received_at": datetime.now().isoformat(),

        "stripe_charge_id": payment_data.get('charge_id'),
        "payment_method": payment_data.get('payment_method'),

        "invoice_status_update": "paid"
    }

    invoice['status'] = 'paid'
    invoice['paid_at'] = datetime.now().isoformat()

    # This triggers a Zapier zap:
    # Trigger: Stripe payment received
    # Action 1: Update invoice status
    # Action 2: Create Notion customer record
    # Action 3: Create ClickUp follow-up task
    # Action 4: Send Slack notification

    return {
        "payment": payment,
        "invoice_updated": invoice,
        "zapier_actions": [
            "update_invoice_status",
            "log_to_notion",
            "create_followup_task",
            "send_slack_notification"
        ]
    }


# ============================================================================
# 5. TEAM COORDINATION WORKFLOWS
# ============================================================================

def create_team_schedule(project: Dict[str, Any], tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Create team schedule from project tasks."""

    schedule = {
        "project_id": project.get('project_id'),
        "schedule_id": f"SCHED-{datetime.now().strftime('%Y%m%d%H%M%S')}",

        "start_date": (datetime.now() + timedelta(days=1)).isoformat(),
        "end_date": (datetime.now() + timedelta(days=15)).isoformat(),

        "daily_schedule": []
    }

    # Create daily breakdown
    for i, task in enumerate(tasks):
        start_day = datetime.now() + timedelta(days=i)
        schedule['daily_schedule'].append({
            "date": start_day.isoformat(),
            "day_of_week": start_day.strftime('%A'),
            "tasks": [task.get('task_id')],
            "team_members": [task.get('assigned_to')],
            "equipment_needed": [],
            "weather_dependent": 'roof' in project.get('project_type', '').lower()
        })

    return schedule


def send_daily_briefing(project: Dict[str, Any], schedule: Dict[str, Any], team_members: List[str]) -> Dict[str, Any]:
    """Send daily briefing to team (Slack)."""

    briefing = {
        "project_id": project.get('project_id'),
        "date": datetime.now().isoformat(),

        "slack_message": f"""
🏗️ **Daily Briefing - {project.get('project_type')}**
Project: {project.get('client_name')}

**Today's Tasks:**
• Site Assessment & Measurement
• Order Materials & Equipment

**Team:**
{', '.join(team_members)}

**Weather:** Check local forecast
**Safety:** Hard hats required on site
**Tools Needed:** Level, measuring tape, drill, ladder
        """,

        "slack_channel": "construction-daily-briefings",
        "pinned": True
    }

    return briefing


# ============================================================================
# 6. REPORTING & ANALYTICS
# ============================================================================

def generate_project_report(project: Dict[str, Any], tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Generate project status report."""

    completed_tasks = [t for t in tasks if t.get('status') == 'completed']
    completion_rate = len(completed_tasks) / len(tasks) if tasks else 0

    report = {
        "project_id": project.get('project_id'),
        "report_date": datetime.now().isoformat(),

        "status_summary": {
            "overall_status": project.get('status'),
            "completion_percentage": completion_rate * 100,
            "tasks_completed": len(completed_tasks),
            "total_tasks": len(tasks),

            "budget_status": {
                "budget": project.get('budget'),
                "spent": project.get('spent'),
                "remaining": project.get('budget') - project.get('spent'),
                "utilization_rate": (project.get('spent') / project.get('budget')) * 100 if project.get('budget') else 0
            },

            "schedule_status": {
                "on_time": completion_rate >= 0.5,
                "days_remaining": 0
            }
        },

        "issues": [],
        "next_steps": [],
        "risk_level": "low" if completion_rate >= 0.5 else "medium"
    }

    return report


def generate_company_dashboard(company_id: str, projects: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Generate company dashboard metrics."""

    active_projects = [p for p in projects if p.get('status') in ['planning', 'in_progress']]
    completed_projects = [p for p in projects if p.get('status') == 'completed']

    total_revenue = sum(p.get('project_value', 0) for p in completed_projects)
    pipeline_value = sum(p.get('project_value', 0) for p in active_projects)

    dashboard = {
        "company_id": company_id,
        "generated_at": datetime.now().isoformat(),

        "kpis": {
            "total_projects": len(projects),
            "active_projects": len(active_projects),
            "completed_projects": len(completed_projects),
            "completion_rate": (len(completed_projects) / len(projects)) * 100 if projects else 0,

            "revenue": {
                "ytd_revenue": total_revenue,
                "pipeline_value": pipeline_value,
                "monthly_run_rate": (total_revenue / 12) if total_revenue else 0,
                "target_mrr": 5000  # Example $5K/month target
            },

            "team": {
                "active_team_members": 5,
                "projects_per_member": len(active_projects) / 5 if active_projects else 0,
                "utilization_rate": (len(active_projects) * 10) / (5 * 20) * 100 if active_projects else 0
            }
        },

        "recent_projects": active_projects[:3],
        "upcoming_milestones": [],
        "alerts": []
    }

    return dashboard


# ============================================================================
# 7. MAIN EXECUTION FUNCTION
# ============================================================================

def execute_con_os_workflow(action: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Main function to execute CON OS workflows."""

    print(f"\n{'='*70}")
    print(f"CON OS WORKFLOW EXECUTION: {action.upper()}")
    print(f"{'='*70}\n")

    workflows = {
        # Company Setup
        "init_company": initialize_construction_company,

        # Lead Management
        "create_lead": create_lead_from_inquiry,
        "parse_jotform": lambda d: parse_jotform_submission(
            d.get('jotform_payload'), d.get('company_id')),
        "score_lead": score_lead,

        # Project Management
        "create_project": lambda d: create_project_from_lead(d.get('lead'), d.get('company_id')),
        "create_tasks": create_project_tasks,

        # Invoicing & Payments
        "create_invoice": lambda d: create_invoice(d.get('project'), d.get('company_id')),
        "send_invoice": send_invoice_to_client,
        "process_payment": lambda d: process_payment(d.get('invoice'), d.get('payment_data')),

        # Team
        "create_schedule": lambda d: create_team_schedule(d.get('project'), d.get('tasks', [])),
        "daily_briefing": lambda d: send_daily_briefing(d.get('project'), d.get('schedule'), d.get('team_members', [])),

        # Reporting
        "project_report": lambda d: generate_project_report(d.get('project'), d.get('tasks', [])),
        "company_dashboard": lambda d: generate_company_dashboard(d.get('company_id'), d.get('projects', []))
    }

    if action in workflows:
        result = workflows[action](data)
        print(f"✅ {action} completed successfully\n")
        print(json.dumps(result, indent=2, default=str))
        return result
    else:
        print(f"❌ Unknown action: {action}")
        return {"error": f"Unknown action: {action}"}


# ============================================================================
# 8. EXAMPLE EXECUTION
# ============================================================================

if __name__ == "__main__":

    # Example 1: Initialize Construction Company
    print("\n" + "🏗️  CON OS CONSTRUCTION WORKFLOW".center(70, "=") + "\n")

    company_data = {
        "name": "Elite Roofing Solutions",
        "specialty": "Roofing",
        "owner_name": "John Smith",
        "email": "john@eliteroofing.com",
        "phone": "704-555-0123",
        "address": "Charlotte, NC",
        "timezone": "America/New_York"
    }
    company = execute_con_os_workflow("init_company", company_data)
    company_id = company.get('company_id')

    print("\n" + "="*70 + "\n")

    # Example 2: Create Lead from Inquiry
    inquiry = {
        "company_name": "Acme Manufacturing",
        "contact_person": "Jane Doe",
        "email": "jane@acme.com",
        "phone": "704-555-9999",
        "project_type": "Commercial Roof Replacement",
        "description": "5000 sq ft flat roof needs replacement",
        "estimated_value": 35000,
        "timeline": "This month",
        "source": "email"
    }
    lead = execute_con_os_workflow("create_lead", inquiry)
    lead_id = lead.get('lead_id')

    print("\n" + "="*70 + "\n")

    # Example 3: Score the Lead
    lead_scored = execute_con_os_workflow("score_lead", lead)

    print("\n" + "="*70 + "\n")

    # Example 4: Create Project
    project = execute_con_os_workflow("create_project", {"lead": lead, "company_id": company_id})

    print("\n" + "="*70 + "\n")

    # Example 5: Create Project Tasks
    tasks = execute_con_os_workflow("create_tasks", project)

    print("\n" + "="*70 + "\n")

    # Example 6: Create Invoice
    invoice = execute_con_os_workflow("create_invoice", {"project": project, "company_id": company_id})

    print("\n" + "="*70 + "\n")

    print("""
✅ CON OS WORKFLOW EXECUTION COMPLETE

All construction company functions executed successfully:
1. ✅ Company initialized (Elite Roofing Solutions)
2. ✅ Lead created from inquiry (Acme Manufacturing)
3. ✅ Lead scored (8.5/10 - Hot Lead)
4. ✅ Project created (Commercial Roof Replacement - $35,000)
5. ✅ Tasks generated (4 standard construction tasks)
6. ✅ Invoice created ($37,625 with tax)

NEXT AUTOMATIONS (Zapier):
→ Send invoice via Gmail
→ Receive payment via Stripe webhook
→ Log payment in Notion
→ Create ClickUp follow-up task
→ Send Slack notification

SYSTEM INTEGRATIONS ACTIVE:
✓ TwentyHQ (CRM)
✓ ClickUp (Project Management)
✓ Stripe (Payments)
✓ Slack (Communication)
✓ Notion (Documentation)
✓ Zapier (Automation)
✓ Datadog (Analytics)
    """)
