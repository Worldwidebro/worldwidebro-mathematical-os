---
name: HRMS-INSTRUMENTATION-SCHEMA
title: HRMS Instrumentation Schema — Signal Capture
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# HRMS Instrumentation Schema — Signal Capture

**Purpose**: Define exactly what signals to log from HRMS execution (May 14-27)  
**Owner**: Sales, CS, Implementation leads (daily logging at point of action)  
**Destination**: Supabase `events` table for real-time analysis  
**Used By**: Meta-learning system to train predictive models

---

## 🎯 Signal Categories

### Category 1: Cold Email Signals

**Event**: `cold_email_sent`
```json
{
  "event_type": "cold_email_sent",
  "timestamp": "2026-05-14T09:30:00Z",
  "sales_rep_id": "rep_001",
  "company_id": "company_abc",
  "sector": "construction",
  "company_size": 150,
  "email_version": "A",  // A=pain-based, B=growth, C=compliance
  "subject_line": "ADP is overcharging [Company] by $1,200/month",
  "message_template": "campaign_A_v1"
}
```

**Event**: `cold_email_opened`
```json
{
  "event_type": "cold_email_opened",
  "timestamp": "2026-05-14T10:45:00Z",
  "email_id": "ref_to_cold_email_sent",
  "time_to_open_mins": 75
}
```

**Event**: `cold_email_clicked`
```json
{
  "event_type": "cold_email_clicked",
  "timestamp": "2026-05-14T10:47:00Z",
  "email_id": "ref_to_cold_email_sent",
  "link_clicked": "calendly_booking_link"
}
```

**Event**: `cold_email_reply_received`
```json
{
  "event_type": "cold_email_reply_received",
  "timestamp": "2026-05-14T14:20:00Z",
  "email_id": "ref_to_cold_email_sent",
  "reply_sentiment": "interested",  // interested, defer, reject, spam
  "reply_text": "This looks interesting. When can we chat?",
  "time_to_reply_mins": 290
}
```

**Collection Target**: 350+ by May 27 (track: version A vs B vs C response rates)

---

### Category 2: Discovery Call Signals

**Event**: `discovery_call_scheduled`
```json
{
  "event_type": "discovery_call_scheduled",
  "timestamp": "2026-05-14T11:00:00Z",
  "call_id": "discovery_001",
  "source": "cold_email",  // cold_email, warm_intro, linkedin, referral, etc.
  "sector": "construction",
  "company_size": 150,
  "decision_maker_title": "Operations Manager",
  "company_current_tool": "ADP",
  "estimated_annual_payroll_spend": 50000
}
```

**Event**: `discovery_call_completed`
```json
{
  "event_type": "discovery_call_completed",
  "timestamp": "2026-05-14T14:00:00Z",
  "call_id": "discovery_001",
  "sales_rep_id": "rep_001",
  "call_duration_mins": 18,
  "outcome": "trial_offered",  // trial_offered, defer, reject, not_fit
  "pain_points_mentioned": ["compliance", "time_savings", "cost_reduction"],
  "pricing_reaction": "acceptable",  // too_high, acceptable, competitive
  "budget_mentioned": 400,  // $/month customer estimated
  "feature_priorities": ["multi_location", "tax_compliance", "direct_deposit"],
  "top_objection": "switching_cost",
  "objection_resolution": "30_day_money_back_guarantee",
  "transcript_key_quotes": [
    "Our biggest headache is CA/TX/NY compliance",
    "We're spending $500/month on ADP for 80 people"
  ]
}
```

**Event**: `objection_recorded`
```json
{
  "event_type": "objection_recorded",
  "timestamp": "2026-05-14T14:02:00Z",
  "call_id": "discovery_001",
  "objection_type": "switching_cost",  // switching_cost, feature_gap, price, compliance_risk
  "objection_severity": 7,  // 1-10, how much this blocks deal
  "sales_rep_response": "30_day_money_back_guarantee",
  "customer_reaction_after_response": "satisfied",  // satisfied, skeptical, still_objecting
  "notes": "Customer worried about data migration, settled with our 30-day promise"
}
```

**Collection Target**: 40+ calls by May 27 (track: call duration, outcome %, pain point patterns)

---

### Category 3: Trial Signup & Activation Signals

**Event**: `trial_signup`
```json
{
  "event_type": "trial_signup",
  "timestamp": "2026-05-14T15:30:00Z",
  "trial_id": "trial_001",
  "customer_id": "cust_001",
  "company_id": "company_abc",
  "sector": "construction",
  "source": "discovery_call",  // discovery_call, landing_page, referral, etc.
  "company_size": 150,
  "current_payroll_tool": "ADP",
  "monthly_payroll_cost": 500,
  "customer_email": "john@company.com",
  "customer_phone": "555-1234",
  "customer_title": "Operations Manager"
}
```

**Event**: `trial_onboarding_call_scheduled`
```json
{
  "event_type": "trial_onboarding_call_scheduled",
  "timestamp": "2026-05-14T15:35:00Z",
  "trial_id": "trial_001",
  "cs_rep_id": "cs_001",
  "scheduled_time": "2026-05-14T16:00:00Z"
}
```

**Event**: `trial_onboarding_call_completed`
```json
{
  "event_type": "trial_onboarding_call_completed",
  "timestamp": "2026-05-14T16:30:00Z",
  "trial_id": "trial_001",
  "cs_rep_id": "cs_001",
  "call_duration_mins": 22,
  "setup_time_mins": 22,
  "employees_onboarded": 150,
  "integrations_connected": ["stripe", "zenefits"],
  "customer_sentiment": "confident",  // confident, hesitant, frustrated
  "blockers_encountered": [],
  "next_step": "first_payroll_on_2026-05-17"
}
```

**Event**: `trial_first_payroll_run`
```json
{
  "event_type": "trial_first_payroll_run",
  "timestamp": "2026-05-17T10:00:00Z",
  "trial_id": "trial_001",
  "days_since_signup": 3,
  "employees_paid": 150,
  "gross_payroll_amount": 45000,
  "tax_withholding_calculated": 8500,
  "payroll_status": "successful",  // successful, needs_adjustment, error
  "time_to_complete_mins": 12,
  "customer_email_opened": true,
  "customer_email_open_time": 300  // seconds after payroll sent
}
```

**Collection Target**: 27 trials by May 27 (track: signup → setup → first payroll flow times)

---

### Category 4: Trial Engagement Signals

**Event**: `trial_email_sent`
```json
{
  "event_type": "trial_email_sent",
  "timestamp": "2026-05-15T09:00:00Z",
  "trial_id": "trial_001",
  "email_sequence": "day_3_checkin",  // day_1_welcome, day_3_checkin, day_7_feature_deep_dive, day_10_close
  "email_subject": "Your first payroll (and a question)",
  "sent_by": "automation"
}
```

**Event**: `trial_email_engagement`
```json
{
  "event_type": "trial_email_engagement",
  "timestamp": "2026-05-15T10:30:00Z",
  "trial_id": "trial_001",
  "email_id": "ref_to_trial_email_sent",
  "action": "opened",  // opened, clicked, ignored, unsubscribed
  "action_timestamp": "2026-05-15T10:30:00Z"
}
```

**Event**: `trial_feature_adoption`
```json
{
  "event_type": "trial_feature_adoption",
  "timestamp": "2026-05-15T14:00:00Z",
  "trial_id": "trial_001",
  "feature": "employee_self_service_login",
  "adopted": true,
  "adoption_delay_days": 1
}
```

**Event**: `trial_support_ticket`
```json
{
  "event_type": "trial_support_ticket",
  "timestamp": "2026-05-15T11:00:00Z",
  "trial_id": "trial_001",
  "ticket_id": "support_001",
  "issue_type": "tax_calculation",  // tax_calculation, integration, ui, data_migration
  "severity": 5,  // 1-10
  "resolution_time_mins": 45,
  "resolved": true,
  "escalated_to_cto": false
}
```

**Collection Target**: 27 trials × 10 days each = 270 engagement events (track: email open %, feature adoption, support volume)

---

### Category 5: Trial-to-Paid Conversion Signals

**Event**: `trial_conversion_decision`
```json
{
  "event_type": "trial_conversion_decision",
  "timestamp": "2026-05-24T14:00:00Z",
  "trial_id": "trial_001",
  "decision": "converting_to_paid",  // converting_to_paid, requesting_extension, churning
  "trial_length_days": 10,
  "decision_trigger": "second_payroll_successful",
  "chosen_tier": "starter",  // starter, pro, enterprise
  "monthly_cost": 199
}
```

**Event**: `paid_subscription_started`
```json
{
  "event_type": "paid_subscription_started",
  "timestamp": "2026-05-24T14:30:00Z",
  "customer_id": "cust_001",
  "subscription_id": "sub_001",
  "tier": "starter",
  "mrr": 199,
  "source_trial_id": "trial_001",
  "payment_method": "credit_card",
  "billing_interval": "monthly"
}
```

**Event**: `conversion_objections_overcome`
```json
{
  "event_type": "conversion_objections_overcome",
  "timestamp": "2026-05-24T14:00:00Z",
  "trial_id": "trial_001",
  "objections_presented_during_trial": ["switching_cost", "feature_gap"],
  "objections_overcome": ["switching_cost"],
  "objections_still_blocking": [],
  "conversion_successful": true
}
```

**Collection Target**: 10-12 conversions by May 27 (track: trial length → conversion, objections overcome)

---

### Category 6: CPA Consultation Signals (Blocker 1)

**Event**: `cpa_consultation_scheduled`
```json
{
  "event_type": "cpa_consultation_scheduled",
  "timestamp": "2026-05-13T10:00:00Z",
  "cpa_id": "cpa_001",
  "cpa_name": "Jane Smith CPA",
  "consultation_date": "2026-05-14T10:00:00Z",
  "focus_states": ["CA", "TX", "NY"]
}
```

**Event**: `cpa_consultation_completed`
```json
{
  "event_type": "cpa_consultation_completed",
  "timestamp": "2026-05-14T11:30:00Z",
  "cpa_id": "cpa_001",
  "consultation_duration_mins": 90,
  "approval_status": "approved_with_notes",  // approved, needs_fixes, rejected
  "compliance_gaps_found": [
    "CA overtime rules updated Jan 2026",
    "NY minimum wage effective date",
    "Multi-state resident withholding"
  ],
  "required_fixes": [
    "Add CA overtime logic",
    "Update NY minimum wage",
    "Fix multi-state resident handling"
  ],
  "estimated_fix_time_hours": 8,
  "cpa_confidence_rating": 8.5  // 1-10
}
```

**Collection Target**: 1-2 consultations by May 14 (track: gaps found, confidence rating)

---

### Category 7: Crew Hiring & Onboarding Signals

**Event**: `job_posting_published`
```json
{
  "event_type": "job_posting_published",
  "timestamp": "2026-05-13T09:00:00Z",
  "role": "Sector Lead",
  "sector": "construction",
  "posted_on": ["linkedin", "angellist", "internal"]
}
```

**Event**: `candidate_application`
```json
{
  "event_type": "candidate_application",
  "timestamp": "2026-05-14T14:00:00Z",
  "role": "Implementation Lead",
  "sector": "construction",
  "candidate_id": "cand_001",
  "candidate_name": "Alice Johnson",
  "relevant_experience": 5,  // years
  "relevant_tools": ["Procore", "Toast", "Raken"],
  "source": "linkedin"
}
```

**Event**: `offer_letter_sent`
```json
{
  "event_type": "offer_letter_sent",
  "timestamp": "2026-05-15T10:00:00Z",
  "candidate_id": "cand_001",
  "role": "Implementation Lead",
  "sector": "construction",
  "base_salary": 65000,
  "equity_pct": 0.08
}
```

**Event**: `offer_accepted`
```json
{
  "event_type": "offer_accepted",
  "timestamp": "2026-05-16T09:30:00Z",
  "candidate_id": "cand_001",
  "start_date": "2026-05-20"
}
```

**Event**: `onboarding_completed`
```json
{
  "event_type": "onboarding_completed",
  "timestamp": "2026-05-22T17:00:00Z",
  "employee_id": "emp_001",
  "role": "Implementation Lead",
  "sector": "construction",
  "onboarding_days": 3,
  "systems_access_granted": ["github", "supabase", "salesforce", "paperclip"],
  "first_venture_setup_scheduled": true,
  "setup_date": "2026-05-23"
}
```

**Collection Target**: 20 hires by May 15, 38 by May 27 (track: hiring velocity, time-to-productive)

---

## 📊 Real-Time Dashboards

### Dashboard 1: Acquisition Funnel (Daily)
```
Cold Emails Sent: 80 → Opened: 24 (30%) → Clicked: 8 (10%) → Discovery Calls: 5
Discovery Calls: 5 → Converted: 3 (60%) → Trials Started: 3
Trials Started: 3 → Converting: 2 (67%) → Paid Customers: 2
MRR: $398
```

### Dashboard 2: Trial Health (Daily)
```
Trials Active: 3
Avg Days Since Signup: 4.3
Avg Setup Time: 18 mins
First Payroll Complete: 3/3 (100%)
Avg Customer Sentiment: Confident
Avg Email Open Rate: 68%
Feature Adoption: 85%
Support Tickets: 2 (avg resolution 45 mins)
Projected Conversions: 2.8 / 3
Projected MRR from Trials: $558
```

### Dashboard 3: Crew Status (Weekly)
```
Offers Sent: 20 | Accepted: 15 (75%) | Onboarded: 8
Implementation Leads: 4/4 onboarded ✓
CS Reps: 6/8 onboarded
Sales Reps: 4/4 onboarded ✓
Sector Leads: 3/4 onboarded
Avg Time-to-Productive: 2.8 days
```

---

## 🔧 Implementation

### Step 1: Create Supabase Tables (May 14)
```sql
-- Main events table
CREATE TABLE events (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  event_type TEXT NOT NULL,
  timestamp TIMESTAMP DEFAULT NOW(),
  payload JSONB NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for fast queries
CREATE INDEX idx_events_type ON events(event_type);
CREATE INDEX idx_events_timestamp ON events(timestamp DESC);
CREATE INDEX idx_events_source ON events((payload->>'source'));
```

### Step 2: Instrument Point of Action (May 14-27)
- **Sales**: Log emails sent/opened/clicked/replied
- **Sales**: Log discovery calls scheduled/completed/objections
- **CS**: Log trial signups/onboarding/engagement
- **Impl**: Log CPA consultations/crew onboarding
- **Ops**: Auto-aggregate from Stripe/SendGrid/Salesforce APIs

### Step 3: Real-Time Alerts (May 15)
- Trial signup → Auto-notify CS rep
- Cold email open → Auto-notify sales rep to follow up
- Objection recorded → Auto-alert CEO if blocker pattern found
- Support ticket → Auto-escalate if >5 severity

### Step 4: Weekly Analysis (May 20, 27)
- Pull all events from previous week
- Calculate conversion rates by source/sector/rep
- Identify pattern changes week-over-week
- Update Layer 3-4 models in meta-learning system

---

## 🎯 Success Targets (May 27)

| Signal Category | Target | Evidence |
|-----------------|--------|----------|
| Cold Emails | 350+ | Event logs with email_sent entries |
| Cold Email Response Rate | 4-5% | email_opened + email_clicked / email_sent |
| Discovery Calls | 40+ | discovery_call_completed events |
| Call-to-Trial Rate | 60% | trial_signup / discovery_call_completed |
| Trial Signups | 27+ | trial_signup events |
| Avg Setup Time | <30 mins | trial_onboarding_call_completed.setup_time_mins avg |
| First Payroll Success Rate | 90%+ | trial_first_payroll_run.payroll_status = successful |
| Trial-to-Paid Conversion | 40-50% | paid_subscription_started / trial_signup |
| Customer Conversions | 10-12 | paid_subscription_started count |
| MRR | $3-5K | SUM(paid_subscription_started.mrr) |
| Crew Hiring | 20/20 | offer_accepted count |
| Crew Onboarded | 15/20 | onboarding_completed count |

---

## 📡 Next Steps

1. ✅ Define instrumentation schema (this document)
2. 📝 **NEXT**: AGENT-DECISION-LOOPS.md (how automations respond to signals)
3. 🔧 **NEXT**: Create Supabase tables + logging infrastructure (May 14)
4. 📊 **NEXT**: Wire up real-time alerts (May 15)
5. 📈 **NEXT**: Weekly analysis + model training (May 20, 27)
