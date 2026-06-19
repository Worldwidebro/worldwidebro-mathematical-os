#!/usr/bin/env python3
"""
Composio Command Dispatcher — Route 91 commands to execution teams
Maps CEO decisions → Composio commands → team execution
Part of Task 11 (Operations Manager orchestration)
"""

import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY", "")

@dataclass
class CommandExecution:
    """Track Composio command execution"""
    command_name: str
    team: str  # Lead Activation, SMS Service, Outreach
    venture_id: str
    parameters: Dict[str, Any]
    status: str  # QUEUED, EXECUTING, COMPLETED, FAILED
    result: Optional[Dict] = None
    error: Optional[str] = None


class ComposioCommandDispatcher:
    """Route commands to execution teams based on CEO decisions"""

    # Command routing: command_name → team
    COMMAND_ROUTING = {
        # Lead Management → Lead Activation (4) + Outreach (4)
        "composio_search_leads": "Lead Activation",
        "composio_qualify_lead": "Outreach",
        "composio_segment_audience": "Lead Activation",
        "composio_track_lead_source": "Outreach",
        "composio_update_lead_status": "Outreach",
        "composio_merge_duplicate_leads": "Outreach",
        "composio_export_leads": "Lead Activation",
        "composio_import_leads_batch": "Lead Activation",

        # Contact Management → Outreach (7)
        "composio_create_contact": "Outreach",
        "composio_update_contact": "Outreach",
        "composio_delete_contact": "Outreach",
        "composio_add_contact_note": "Outreach",
        "composio_tag_contact": "Outreach",
        "composio_get_contact_history": "Outreach",
        "composio_batch_contacts": "Outreach",

        # Email Campaigns → Outreach (5) + SMS Service (4)
        "composio_create_email_template": "Outreach",
        "composio_send_email": "Outreach",
        "composio_schedule_email": "Outreach",
        "composio_track_email_open": "SMS Service",
        "composio_track_email_click": "SMS Service",
        "composio_ab_test_email_subject": "SMS Service",
        "composio_ab_test_email_body": "SMS Service",
        "composio_reply_to_email": "Outreach",
        "composio_manage_email_suppression": "Outreach",

        # SMS/Messaging → SMS Service (8)
        "composio_send_sms": "SMS Service",
        "composio_schedule_sms": "SMS Service",
        "composio_track_sms_delivery": "SMS Service",
        "composio_track_sms_click": "SMS Service",
        "composio_ab_test_sms_message": "SMS Service",
        "composio_handle_sms_reply": "SMS Service",
        "composio_manage_sms_suppression": "SMS Service",
        "composio_bulk_sms_campaign": "SMS Service",

        # Call Management → Outreach (6)
        "composio_log_call": "Outreach",
        "composio_schedule_call": "Outreach",
        "composio_call_recording_link": "Outreach",
        "composio_call_analytics": "Outreach",
        "composio_voicemail_to_text": "Outreach",
        "composio_auto_dial_list": "Outreach",

        # LinkedIn → Lead Activation (3) + Outreach (4)
        "composio_search_linkedin_profiles": "Lead Activation",
        "composio_send_linkedin_message": "Outreach",
        "composio_scrape_linkedin_job_changes": "Outreach",
        "composio_export_linkedin_data": "Lead Activation",
        "composio_linkedin_post_engagement": "Outreach",
        "composio_linkedin_profile_update_trigger": "Outreach",
        "composio_sync_linkedin_to_crm": "Lead Activation",

        # Data Enrichment → Lead Activation (8)
        "composio_enrich_lead_firmographics": "Lead Activation",
        "composio_enrich_lead_technographics": "Lead Activation",
        "composio_enrich_lead_intent_data": "Lead Activation",
        "composio_enrich_lead_location": "Lead Activation",
        "composio_verify_email": "Lead Activation",
        "composio_verify_phone": "Lead Activation",
        "composio_ip_geolocation": "Lead Activation",
        "composio_company_api_lookup": "Lead Activation",

        # Reporting → CFO (4) + CTO (4)
        "composio_generate_campaign_report": "CTO",
        "composio_generate_roi_report": "CFO",
        "composio_export_metrics_to_bi_tool": "CFO",
        "composio_track_conversion_funnel": "CTO",
        "composio_compare_team_performance": "CFO",
        "composio_pipeline_health_report": "CTO",
        "composio_cost_per_lead_analysis": "CTO",
        "composio_forecast_revenue": "CFO",

        # Calendar & Scheduling → Outreach (5)
        "composio_schedule_meeting": "Outreach",
        "composio_send_meeting_reminder": "Outreach",
        "composio_sync_calendar_availability": "Outreach",
        "composio_calendar_conflict_detection": "Outreach",
        "composio_reschedule_meeting": "Outreach",

        # Automation & Workflow → CTO (8)
        "composio_trigger_workflow_on_lead_score": "CTO",
        "composio_trigger_workflow_on_email_open": "CTO",
        "composio_trigger_workflow_on_sms_click": "CTO",
        "composio_trigger_workflow_on_call_missed": "CTO",
        "composio_trigger_workflow_on_conversion": "CTO",
        "composio_create_custom_webhook": "CTO",
        "composio_queue_outreach_task": "CTO",
        "composio_pause_workflow_on_condition": "CTO",

        # Compliance & Suppression
        "composio_check_do_not_call_list": "SMS Service",
        "composio_check_gdpr_consent": "Outreach",
        "composio_log_audit_trail": "CFO",
        "composio_handle_unsubscribe": "SMS Service",
        "composio_manage_suppression_list": "SMS Service",
        "composio_generate_compliance_report": "CFO",

        # Integration & Webhooks → CTO (9)
        "composio_sync_crm_to_supabase": "CTO",
        "composio_sync_supabase_to_crm": "CTO",
        "composio_listen_webhook_lead_created": "CTO",
        "composio_listen_webhook_deal_closed": "CTO",
        "composio_send_webhook_to_slack": "CTO",
        "composio_send_webhook_to_discord": "CTO",
        "composio_auth_oauth_connection": "CTO",
        "composio_test_api_connection": "CTO",
        "composio_bulk_api_operation": "CTO",
    }

    # Decision → Command mapping
    DECISION_COMMANDS = {
        "KILL": [
            "composio_update_lead_status",  # Mark as "ARCHIVED"
            "composio_manage_sms_suppression",  # Stop all campaigns
            "composio_pause_workflow_on_condition",  # Halt execution
            "composio_sync_supabase_to_crm",  # Update venture status
        ],
        "OPTIMIZE": [
            "composio_search_linkedin_profiles",  # Retarget high-LTV segments
            "composio_enrich_lead_firmographics",  # Better qualification
            "composio_ab_test_email_subject",  # Test effectiveness
            "composio_track_conversion_funnel",  # Monitor improvement
        ],
        "SCALE": [
            "composio_search_leads",  # Expand sourcing
            "composio_segment_audience",  # New segments
            "composio_bulk_sms_campaign",  # Increase volume
            "composio_schedule_call",  # More outreach
            "composio_compare_team_performance",  # Track growth
        ],
        "COMPOUND": [
            "composio_export_linkedin_data",  # Multi-channel sourcing
            "composio_bulk_sms_campaign",  # Aggressive SMS
            "composio_send_linkedin_message",  # LinkedIn outreach
            "composio_auto_dial_list",  # Power dialing
            "composio_forecast_revenue",  # Growth projection
        ],
    }

    def __init__(self):
        self.queue = []
        self.executions = []
        self.api_key = COMPOSIO_API_KEY

    def dispatch_decision(self, decision_type: str, venture_id: str,
                         capital_allocated: float) -> List[CommandExecution]:
        """
        Dispatch CEO decision to appropriate Composio commands
        Maps decision → commands → teams
        """
        commands = self.DECISION_COMMANDS.get(decision_type, [])
        executions = []

        print(f"\n🚀 Dispatching {decision_type} decision for venture {venture_id}")
        print(f"   Capital: ${capital_allocated:,.0f}")
        print(f"   Commands: {len(commands)}")

        for command_name in commands:
            team = self.COMMAND_ROUTING.get(command_name, "Unknown")

            execution = CommandExecution(
                command_name=command_name,
                team=team,
                venture_id=venture_id,
                parameters={"capital": capital_allocated},
                status="QUEUED"
            )

            self.queue.append(execution)
            executions.append(execution)
            print(f"   ✓ {command_name} → {team}")

        return executions

    def execute_command(self, execution: CommandExecution) -> bool:
        """Execute Composio command with proper error handling"""
        try:
            print(f"\n⚡ Executing: {execution.command_name} ({execution.team})")

            # TODO: Integration point for Composio SDK
            # from composio import Composio
            # client = Composio(api_key=self.api_key)
            # result = client.execute(
            #     action=execution.command_name,
            #     params=execution.parameters
            # )

            execution.status = "COMPLETED"
            execution.result = {"status": "mocked"}
            self.executions.append(execution)

            return True

        except Exception as e:
            print(f"❌ Command failed: {e}")
            execution.status = "FAILED"
            execution.error = str(e)
            self.executions.append(execution)
            return False

    def execute_batch(self, executions: List[CommandExecution]) -> Dict:
        """Execute multiple commands, respecting team capacity"""
        results = {
            "total": len(executions),
            "completed": 0,
            "failed": 0,
            "by_team": {}
        }

        for execution in executions:
            team = execution.team
            if team not in results["by_team"]:
                results["by_team"][team] = {"completed": 0, "failed": 0}

            success = self.execute_command(execution)
            if success:
                results["completed"] += 1
                results["by_team"][team]["completed"] += 1
            else:
                results["failed"] += 1
                results["by_team"][team]["failed"] += 1

        print(f"\n{'='*70}")
        print(f"📊 EXECUTION BATCH COMPLETE")
        print(f"   Total: {results['total']}")
        print(f"   Completed: {results['completed']}")
        print(f"   Failed: {results['failed']}")
        print(f"   By Team:")
        for team, stats in results["by_team"].items():
            print(f"     {team}: {stats['completed']} completed, {stats['failed']} failed")
        print(f"{'='*70}\n")

        return results

    def get_team_commands(self, team: str) -> List[str]:
        """Get all commands assigned to a specific team"""
        return [cmd for cmd, t in self.COMMAND_ROUTING.items() if t == team]

    def get_command_team(self, command_name: str) -> Optional[str]:
        """Get team responsible for a command"""
        return self.COMMAND_ROUTING.get(command_name)

    def print_routing_summary(self):
        """Print command routing summary"""
        teams = {}
        for team in set(self.COMMAND_ROUTING.values()):
            teams[team] = len(self.get_team_commands(team))

        print(f"\n{'='*70}")
        print(f"📋 COMPOSIO COMMAND ROUTING")
        print(f"{'='*70}\n")
        print("Commands by Team:")
        for team, count in sorted(teams.items(), key=lambda x: x[1], reverse=True):
            print(f"  {team}: {count} commands")

        print(f"\nTotal Commands: {len(self.COMMAND_ROUTING)}")
        print(f"Teams: {len(teams)}")


def main():
    """Initialize and test dispatcher"""
    dispatcher = ComposioCommandDispatcher()

    if not COMPOSIO_API_KEY:
        print("⚠️  COMPOSIO_API_KEY not set")
        print("   Set environment variable to enable command execution")

    dispatcher.print_routing_summary()

    # Test dispatch
    test_executions = dispatcher.dispatch_decision(
        decision_type="SCALE",
        venture_id="venture_001",
        capital_allocated=50000
    )

    results = dispatcher.execute_batch(test_executions)
    print(f"\nResults: {results}")


if __name__ == "__main__":
    main()
