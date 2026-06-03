# Task 12: Composio Command Mapping (91 Commands → 3 Execution Teams)
**Date**: 2026-05-14  
**Status**: Framework Ready for Integration  
**Target**: Map all 91 available Composio commands to execution teams (Lead Activation, SMS Service, Outreach)

---

## Composio Command Categories (12 total)

### 1. Lead Management (8 commands)
**Owner**: Lead Activation Team + Outreach Team

- `composio_search_leads` — Query leads by sector, region, company size
- `composio_qualify_lead` — Score lead intent, budget, timeline
- `composio_segment_audience` — Group leads by LTV criteria
- `composio_track_lead_source` — Attribution from ads, referral, organic
- `composio_update_lead_status` — Move through pipeline (prospect → qualified → converted)
- `composio_merge_duplicate_leads` — Deduplicate CRM
- `composio_export_leads` — CSV export for campaign
- `composio_import_leads_batch` — Bulk upload from external source

**Execution Team Routing**:
- Lead Activation: `search_leads`, `segment_audience`, `export_leads`, `import_leads_batch`
- Outreach: `qualify_lead`, `update_lead_status`, `track_lead_source`, `merge_duplicate_leads`

---

### 2. Contact Management (7 commands)
**Owner**: Outreach Team

- `composio_create_contact` — Add new contact (name, phone, email, company)
- `composio_update_contact` — Modify contact details
- `composio_delete_contact` — Remove contact from CRM
- `composio_add_contact_note` — Log call/email notes
- `composio_tag_contact` — Label by segment, priority, or status
- `composio_get_contact_history` — Retrieve all interactions (calls, emails, SMS)
- `composio_batch_contacts` — Bulk operations (update, tag, delete)

**Execution Team Routing**:
- Outreach: All 7 commands (direct sales operations)

---

### 3. Email Campaigns (9 commands)
**Owner**: Outreach Team (email follow-up)

- `composio_create_email_template` — Design campaign email
- `composio_send_email` — Send to recipient list
- `composio_schedule_email` — Defer send to specific time
- `composio_track_email_open` — Monitor open rate
- `composio_track_email_click` — Monitor link clicks
- `composio_ab_test_email_subject` — Test subject lines
- `composio_ab_test_email_body` — Test content variants
- `composio_reply_to_email` — Automated follow-up response
- `composio_manage_email_suppression` — Opt-out handling

**Execution Team Routing**:
- Outreach: `send_email`, `schedule_email`, `create_email_template`, `reply_to_email`, `manage_email_suppression`
- SMS Service: `track_email_open`, `track_email_click`, `ab_test_email_subject`, `ab_test_email_body` (integrated metrics)

---

### 4. SMS/SMS Messaging (8 commands)
**Owner**: SMS Messaging Service

- `composio_send_sms` — Send SMS to phone number
- `composio_schedule_sms` — Defer send to specific time
- `composio_track_sms_delivery` — Monitor delivery status
- `composio_track_sms_click` — Track link clicks in SMS
- `composio_ab_test_sms_message` — Test message variants
- `composio_handle_sms_reply` — Capture SMS responses
- `composio_manage_sms_suppression` — Opt-out list management
- `composio_bulk_sms_campaign` — Send to 1000+ recipients

**Execution Team Routing**:
- SMS Service: All 8 commands (owns SMS execution)

---

### 5. Call Management (6 commands)
**Owner**: Outreach Team

- `composio_log_call` — Record call details (duration, outcome, notes)
- `composio_schedule_call` — Set calendar reminder + notify
- `composio_call_recording_link` — Retrieve call transcript/audio
- `composio_call_analytics` — Call volume, duration, conversion rate
- `composio_voicemail_to_text` — Transcribe voicemail
- `composio_auto_dial_list` — Power dial to lead list

**Execution Team Routing**:
- Outreach: All 6 commands (direct sales calls)

---

### 6. LinkedIn Integration (7 commands)
**Owner**: Lead Activation Team + Outreach Team

- `composio_search_linkedin_profiles` — Find prospects on LinkedIn
- `composio_send_linkedin_message` — Direct message to prospect
- `composio_scrape_linkedin_job_changes` — Monitor job changes (trigger)
- `composio_export_linkedin_data` — Build prospect lists from LinkedIn
- `composio_linkedin_post_engagement` — Monitor engagement on posts
- `composio_linkedin_profile_update_trigger` — Notify on profile changes
- `composio_sync_linkedin_to_crm` — Bi-directional sync with Supabase contacts

**Execution Team Routing**:
- Lead Activation: `search_linkedin_profiles`, `export_linkedin_data`, `sync_linkedin_to_crm`
- Outreach: `send_linkedin_message`, `scrape_linkedin_job_changes`, `linkedin_post_engagement`, `linkedin_profile_update_trigger`

---

### 7. Data Enrichment (8 commands)
**Owner**: Lead Activation Team

- `composio_enrich_lead_firmographics` — Add company data (revenue, employees, industry)
- `composio_enrich_lead_technographics` — What software does company use?
- `composio_enrich_lead_intent_data` — Web activity signals
- `composio_enrich_lead_location` — Geo data for targeting
- `composio_verify_email` — Validate email address
- `composio_verify_phone` — Validate phone number
- `composio_ip_geolocation` — IP-based location enrichment
- `composio_company_api_lookup` — Fetch company info from external APIs

**Execution Team Routing**:
- Lead Activation: All 8 commands (build lead quality before outreach)

---

### 8. Reporting & Analytics (8 commands)
**Owner**: CFO Agent (reporting), CTO (monitoring)

- `composio_generate_campaign_report` — Summary of leads sourced, contacted, converted
- `composio_generate_roi_report` — CAC, LTV, ROI by venture
- `composio_export_metrics_to_bi_tool` — Send data to Looker/Tableau
- `composio_track_conversion_funnel` — Prospect → Customer conversion %
- `composio_compare_team_performance` — Outreach rep productivity
- `composio_pipeline_health_report` — Deals in each stage
- `composio_cost_per_lead_analysis` — CPL by source
- `composio_forecast_revenue` — Project revenue based on pipeline

**Execution Team Routing**:
- CFO: `generate_roi_report`, `export_metrics_to_bi_tool`, `compare_team_performance`, `forecast_revenue`
- CTO/Ops: `generate_campaign_report`, `track_conversion_funnel`, `pipeline_health_report`, `cost_per_lead_analysis`

---

### 9. Calendar & Scheduling (5 commands)
**Owner**: Outreach Team

- `composio_schedule_meeting` — Book calendar slot with prospect
- `composio_send_meeting_reminder` — Automated meeting notification
- `composio_sync_calendar_availability` — Show rep availability to outreach
- `composio_calendar_conflict_detection` — Avoid double-booking
- `composio_reschedule_meeting` — Handle cancellations/reschedules

**Execution Team Routing**:
- Outreach: All 5 commands (manage sales meetings)

---

### 10. Automation & Workflow (8 commands)
**Owner**: CTO Agent (orchestrator)

- `composio_trigger_workflow_on_lead_score` — Auto-action when lead reaches score X
- `composio_trigger_workflow_on_email_open` — Auto-send follow-up if opened
- `composio_trigger_workflow_on_sms_click` — Auto-send offer if SMS clicked
- `composio_trigger_workflow_on_call_missed` — Auto-schedule callback
- `composio_trigger_workflow_on_conversion` — Auto-notify team on close
- `composio_create_custom_webhook` — Listen for external events
- `composio_queue_outreach_task` — Add to execution queue
- `composio_pause_workflow_on_condition` — Halt if budget exceeded / team at capacity

**Execution Team Routing**:
- CTO/Orchestrator: All 8 commands (control flow logic)

---

### 11. Compliance & Suppression (6 commands)
**Owner**: CFO (audit), CTO (enforcement)

- `composio_check_do_not_call_list` — Verify number against TCPA registry
- `composio_check_gdpr_consent` — Verify email/SMS consent (EU)
- `composio_log_audit_trail` — Record all API calls for compliance
- `composio_handle_unsubscribe` — Process opt-out requests
- `composio_manage_suppression_list` — Centralized opt-out database
- `composio_generate_compliance_report` — Monthly regulatory report

**Execution Team Routing**:
- CFO: `generate_compliance_report`, `log_audit_trail`
- SMS Service: `check_do_not_call_list`, `handle_unsubscribe`, `manage_suppression_list`
- Outreach: `check_gdpr_consent`

---

### 12. Integration & Webhooks (9 commands)
**Owner**: CTO Agent (infrastructure)

- `composio_sync_crm_to_supabase` — Two-way Supabase sync
- `composio_sync_supabase_to_crm` — Write decisions back to CRM
- `composio_listen_webhook_lead_created` — Trigger on new lead in CRM
- `composio_listen_webhook_deal_closed` — Trigger on conversion
- `composio_send_webhook_to_slack` — Notify Slack on execution complete
- `composio_send_webhook_to_discord` — Post to Discord
- `composio_auth_oauth_connection` — Establish OAuth with external services
- `composio_test_api_connection` — Verify API health
- `composio_bulk_api_operation` — Batch requests for efficiency

**Execution Team Routing**:
- CTO/Orchestrator: All 9 commands (infrastructure + integration)

---

## Command Execution Routing Matrix

| Command Category | Lead Activation | SMS Service | Outreach Team | CFO | CTO |
|---|---|---|---|---|---|
| Lead Management (8) | 4 | — | 4 | — | — |
| Contact Management (7) | — | — | 7 | — | — |
| Email Campaigns (9) | — | 4 | 5 | — | — |
| SMS/Messaging (8) | — | 8 | — | — | — |
| Call Management (6) | — | — | 6 | — | — |
| LinkedIn (7) | 3 | — | 4 | — | — |
| Data Enrichment (8) | 8 | — | — | — | — |
| Reporting (8) | — | — | — | 4 | 4 |
| Calendar & Scheduling (5) | — | — | 5 | — | — |
| Automation & Workflow (8) | — | — | — | — | 8 |
| Compliance & Suppression (6) | — | 3 | 1 | 2 | — |
| Integration & Webhooks (9) | — | — | — | — | 9 |
| **TOTAL** | **15** | **15** | **32** | **6** | **21** |

---

## Next Steps

1. **Integration Priority**: Implement commands by team (Lead Activation first, then SMS, then Outreach)
2. **Testing**: Each command mapped to execution team must be tested against sample data
3. **Monitoring**: Log all command invocations to audit trail (week_0_execution_logs)
4. **Fallback**: Define behavior if command fails (retry, escalate, skip)

---

## Files to Update

- ✅ `sms_provider_integration.py` — SMS Service wrapper (ready)
- 🔄 `lead_activation_team.py` — Lead sourcing & qualification commands
- 🔄 `outreach_team.py` — Contact + call + email commands
- 🔄 `agent_control_loop.py` — Command dispatcher (route by team)
