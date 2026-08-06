---
name: AGENT-DECISION-LOOPS
title: Agent Decision Loops — Automated Responses to Signals
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Agent Decision Loops — Automated Responses to Signals

**Purpose**: Define how automations respond to real-time signals from HRMS execution  
**Owner**: CTO (builds infrastructure), CEO (calibrates thresholds)  
**Timeline**: Build infrastructure May 14-15, activate May 16+  
**Goal**: Turn learning into action without human intervention

---

## 🤖 Agent Types

### Agent 1: Sales Optimization Agent

**Listens to**: Cold email signals, discovery call signals, objection signals  
**Responds to**: Pattern changes in real-time

**Decision Loop 1.1: Email Version Optimization**
```
TRIGGER: 100 cold emails sent with version A, B, C
SIGNAL: Version A has 25% open rate, Version B has 35%, Version C has 20%

DECISION:
  IF open_rate[B] > 1.3 * open_rate[A]
    THEN increase version B allocation to 50% of next batch
    AND decrease version C to 10% (worst performer)
    AND notify sales team: "Version B outperforming by 35%"

NOTIFICATION: Slack alert to sales lead @ 5 PM daily

CALIBRATION (May 20): Check if allocation change improved overall open rate
```

**Decision Loop 1.2: Lead Scoring Refinement**
```
TRIGGER: 10 discovery calls completed
SIGNAL: Calls from "warm intros" convert at 70%, "cold email" at 25%

DECISION:
  IF conversion_rate[warm_intros] > 2x * conversion_rate[cold_email]
    THEN increase priority for warm intros
    AND route warm intro leads to senior sales reps
    AND allocate 20% of cold email time to warm intro generation
    AND record: "Warm intro conversion multiplier = 2.8x"

IMPACT: By May 20, expect conversion improvements from rep reassignment
ESCALATION: If gap widens to 3x+, pivot strategy entirely to warm intros
```

**Decision Loop 1.3: Objection Pattern Response**
```
TRIGGER: 5+ discovery calls mention same objection (e.g., "switching cost")
SIGNAL: Objection appears in 40% of calls, blocking ~50% of conversions

DECISION:
  IF objection_frequency > 3 per week
    AND objection_resolution_rate < 50%
    THEN: 
      1. Create objection-specific script (48-hour turnaround)
      2. Video record sales rep demonstrating resolution
      3. Roll out to all sales reps
      4. Track resolution rate over next 10 calls
    
EXAMPLE:
  Objection: "Switching from ADP is risky for compliance"
  Script Addition: "30-day money-back guarantee + free CPA review first month"
  Video: https://[recorded demo of guarantee in action]
  
NOTIFICATION: Email script + video to sales team within 48 hours

FEEDBACK (May 20): Did resolution rate improve from 40% → 60%?
```

**Agent 1 Success Metrics** (May 27):
- Email version optimization improved overall response rate by 15%
- Warm intro prioritization increased conversion rate by 25%
- Objection scripts reduced switching cost objections by 50%

---

### Agent 2: Trial Optimization Agent

**Listens to**: Trial signup signals, engagement signals, support ticket signals  
**Responds to**: Engagement drops, support issues, conversion risk

**Decision Loop 2.1: Proactive Trial Support**
```
TRIGGER: Trial customer has not completed first payroll by Day 3
SIGNAL: setup_time_actual > 30 mins OR customer hasn't logged in Day 2

DECISION:
  IF days_since_signup = 3 AND first_payroll_incomplete
    THEN:
      1. Automatically email customer: "Let's get your first payroll running today"
      2. Offer 30-min phone setup call (calendar link)
      3. If no response in 4 hours, notify CS lead
    
NOTIFICATION: CS rep sees alert in Slack + auto-email sent

ESCALATION: If customer doesn't respond in 24 hours, call directly

EXAMPLE TRIGGER:
  Trial 001: Signed up May 14, setup call May 14 was successful
  Day 2 (May 15): No login recorded
  → Auto-email: "Your first payroll is ready. Let's make sure it runs perfectly."
```

**Decision Loop 2.2: Feature Adoption Nudge**
```
TRIGGER: Day 7 of trial, customer has NOT enabled "Employee Self-Service Portal"
SIGNAL: feature_adoption rate < 50% on Day 7

DECISION:
  IF feature_adoption_rate < 50% on Day 7
    THEN:
      1. Send email: "One feature cutting onboarding time in half..."
      2. Include short video (2 mins) showing self-service in action
      3. Schedule light-touch follow-up call on Day 8
      4. Track adoption within 24 hours

INTENT: Low feature adoption often predicts churn. Nudge early.

NOTIFICATION: Email + video + calendar reminder for CS rep
```

**Decision Loop 2.3: Conversion Readiness Assessment**
```
TRIGGER: Day 9 of 10-day trial
SIGNAL: Multiple signals converge: first payroll run, email opens, support tickets

CONVERSION_READINESS_SCORE = (
  (first_payroll_success ? 30 : 0) +
  (email_open_rate > 60% ? 25 : 0) +
  (feature_adoption > 70% ? 20 : 0) +
  (support_tickets < 3 ? 15 : 0) +
  (customer_sentiment = confident ? 10 : 0)
)

IF conversion_readiness_score > 80:
  → Mark as "Ready to Convert", notify sales rep
  → Send Day 10 email with strong CTA
  → Schedule "close" call on Day 10
  
IF conversion_readiness_score 60-80:
  → Mark as "Likely Convert", prepare objection responses
  → Offer extended trial (3 more days)
  
IF conversion_readiness_score < 60:
  → Mark as "At Risk", escalate to CS lead
  → Identify blocking issues + resolve
  → Extend trial to Day 15 with intensive support

EXAMPLE: Trial 001 has setup time 18 mins, email opens 75%, adopted self-service
→ Score = 30 + 25 + 20 + 15 + 10 = 100 (ready to convert)
→ Action: Assign senior rep for close call
```

**Agent 2 Success Metrics** (May 27):
- Trial-to-paid conversion improved from 40% → 55%
- Avg trial length reduced from 10 days → 7.5 days (faster conversions)
- Support tickets per trial reduced 15% (proactive nudges resolved issues earlier)

---

### Agent 3: Crew Productivity Agent

**Listens to**: Onboarding signals, setup completion signals, customer health signals  
**Responds to**: Bottlenecks, low productivity, skill gaps

**Decision Loop 3.1: Setup Time Bottleneck Detection**
```
TRIGGER: 3+ implementation leads report avg setup time > 40 mins
SIGNAL: setup_time_actual > 40 mins threshold

DECISION:
  IF avg_setup_time > 40 mins for 2+ consecutive days
    THEN:
      1. Analyze common setup issues (support tickets + call notes)
      2. Identify bottleneck: Is it data migration? Tax setup? Integrations?
      3. Document quick fix (e.g., "pre-populate tax forms") + share with team
      4. Track setup time next day
      5. If still > 40 mins, escalate to CTO

EXAMPLE:
  May 17: Impl leads report avg setup 48 mins (target: 30)
  Bottleneck found: Manual tax rate lookup for multi-state companies
  Fix: Pre-populate tax rates in setup form
  May 18: Avg setup time drops to 32 mins ✓

ESCALATION PATH: Impl Lead → CTO (if fix not simple) → Auto-update playbook
```

**Decision Loop 3.2: CS Rep Productivity Pairing**
```
TRIGGER: Two CS reps managing same sector; one has 40% higher resolution time
SIGNAL: cs_rep_A avg resolution: 45 mins, cs_rep_B avg resolution: 30 mins

DECISION:
  IF resolution_time_difference > 25%
    THEN:
      1. Have slower rep shadow faster rep for 1 day
      2. Record top 5 resolution techniques from faster rep
      3. Share techniques via video/docs with team
      4. Re-measure in 3 days
      5. If gap persists, offer targeted training

INTENT: Identify best practices and spread them within crew

NOTIFICATION: Ops Manager facilitates pairing, Slack to team
```

**Decision Loop 3.3: Sector Crew Workload Balancing**
```
TRIGGER: End of each day, sum up work assigned to each sector crew
SIGNAL: Construction crew has 8 trials, Logistics crew has 2

DECISION:
  IF workload_imbalance_ratio > 3:1
    THEN:
      1. Identify trials from overloaded sector that are progressing well
      2. Transfer 2-3 trials to underloaded sector
      3. Notify both sector leads of change
      4. Re-measure next day
      5. Adjust sales rep lead allocation if pattern persists

INTENT: Prevent burnout, ensure all crews equally utilized

ALERT: Slack to CEO + Sector Leads: "Construction → Logistics: 2 trial transfers"
```

**Agent 3 Success Metrics** (May 27):
- Setup time per venture improved 35% (40 mins → 26 mins)
- CS rep resolution time variance reduced to <15% (best practices shared)
- Crew utilization balanced across all sectors

---

### Agent 4: Revenue & MRR Agent

**Listens to**: Trial conversion signals, paid subscription signals, churn signals  
**Responds to**: Revenue tracking, tier upsell opportunities, retention risks

**Decision Loop 4.1: Tier Upsell Trigger**
```
TRIGGER: Customer on Starter ($199/mo) has adopted 70%+ Pro features
SIGNAL: feature_adoption_score > 70% AND trial_to_paid < 7 days

DECISION:
  IF feature_adoption_score > 70%
    AND current_tier = starter
    AND pro_features_adopted > 70%
    THEN:
      1. Email customer: "You're using Pro features. Save time with Pro plan..."
      2. Offer $499/mo Pro tier with highlight: "Advanced reporting + multi-location"
      3. Track acceptance within 7 days
      4. If accepted, congratulate CS rep + record upsell

INTENT: Capture incremental revenue from high-adoption customers

NOTIFICATION: CS rep sees prompt to send upsell email
```

**Decision Loop 4.2: Churn Risk Detection**
```
TRIGGER: Paid customer has NOT logged in for 3+ days (after 1 week active)
SIGNAL: low_engagement within paid subscription

DECISION:
  IF days_since_login > 3
    AND customer_tenure_days > 7
    AND was_previously_active
    THEN:
      1. Email customer: "We noticed you haven't logged in. What's blocking payroll?"
      2. Offer 30-min tech support call (no charge)
      3. If no response in 24 hours, CS lead calls directly
      4. Determine: Is it feature gap? Support issue? Better alternative found?
      5. Document reason + work to resolve
      6. If unresolvable, consider pause/discount vs. churn

INTENT: Save customers before they churn

NOTIFICATION: CS lead alert + auto-email to customer
```

**Decision Loop 4.3: MRR Forecast & Burn Rate Check**
```
TRIGGER: Daily at 6 PM, calculate projected MRR for month
SIGNAL: MRR based on conversions to date + pipeline

CALCULATION:
  Projected_MRR = (paid_customers * avg_mrr_per_tier) + (trials_likely_to_convert * avg_tier)
  May 27 Target: $3-5K MRR
  Current MRR: $847 (4 customers × $211 avg)
  Trials converting (likely): 6 × $350 = $2,100
  Projected MRR: $847 + $2,100 = $2,947 (on track for lower bound)

DECISION:
  IF projected_mrr < target_lower_bound
    THEN:
      1. Analyze: Why are conversions lower?
      2. Check: Are discovery calls converting at 60%? (yes → problem is earlier in funnel)
      3. Check: Is trial-to-paid rate lower than 40%? (if yes → problem is trial experience)
      4. Escalate to CEO with options:
         - Option A: Increase discovery call volume
         - Option B: Improve trial onboarding
         - Option C: Extend deadline
      5. Execute decision by May 22

NOTIFICATION: Daily 6 PM Slack summary to CEO + Finance lead
```

**Agent 4 Success Metrics** (May 27):
- Upsell rate: 15-20% of Starter customers → Pro
- Churn rate: <5% (early intervention saves 80% of at-risk customers)
- MRR on track for $3-5K target (within ±10%)

---

## 🔌 Technical Implementation

### Step 1: Event-Driven Architecture (May 14)

**Supabase → PubSub → Agent Functions**

```
Events Table (Supabase)
  ↓ [realtime listener]
PubSub Channel
  ↓ [subscribes to: trial_signup, discovery_call_completed, objection_recorded, etc.]
Agent Decision Functions
  ↓ [each function has threshold + decision logic]
Action Execution
  ↓ [send email, Slack alert, trigger next step]
Result Logging
  ↓ [log agent decision + outcome for meta-learning]
```

### Step 2: Agent Thresholds (Calibrated May 14-15)

Each agent has configurable thresholds:

```json
{
  "agents": {
    "sales_optimization": {
      "email_version_switch_threshold": 0.35,  // 35% improvement
      "objection_pattern_frequency": 5,  // 5 mentions = action
      "objection_resolution_target": 0.60  // 60% resolution rate
    },
    "trial_optimization": {
      "setup_incomplete_days": 3,
      "feature_adoption_target": 0.50,
      "conversion_readiness_score_threshold": 80
    },
    "crew_productivity": {
      "setup_time_target_mins": 30,
      "resolution_time_variance_threshold": 0.25,  // 25% variance
      "workload_imbalance_ratio": 3.0
    },
    "revenue_mrr": {
      "feature_adoption_upsell_threshold": 0.70,
      "churn_detection_days_no_login": 3,
      "mrr_forecast_variance_tolerance": 0.10  // ±10% acceptable
    }
  }
}
```

### Step 3: Real-Time Automation (May 15+)

**Infrastructure**:
- Supabase Postgres Functions (run decision logic)
- SendGrid + Slack APIs (send notifications)
- Paperclip + Salesforce APIs (update records)
- Google Sheets API (update dashboards)

**Example Agent Function** (pseudocode):
```python
# Triggers when: trial_signup event created
def on_trial_signup(event):
    trial_id = event['trial_id']
    customer_id = event['customer_id']
    
    # Check: Do we have full onboarding info?
    if event['setup_preference'] == 'call':
        # Auto-schedule CS call for next available slot
        send_calendar_invite(
            customer_email=event['customer_email'],
            duration_mins=30,
            message="Your HRMS Trial Setup — Let's get payroll running!"
        )
        send_slack_alert(
            channel='#customer-success',
            message=f"Trial signup: {event['company_name']} ({event['sector']}), call scheduled"
        )
    
    # Log decision
    log_agent_decision(
        agent='trial_optimization',
        decision='auto_schedule_onboarding_call',
        outcome='success'
    )

# Triggers when: discovery_call_completed
def on_discovery_call_completed(event):
    objection = event['top_objection']
    resolution = event['objection_resolution']
    
    # Check: Is this objection new/unresolved?
    existing_resolution = lookup_objection_resolution(objection)
    if not existing_resolution or event['objection_resolution_success'] == false:
        # Escalate to CEO for script development
        send_slack_alert(
            channel='#blockers',
            message=f"New objection: {objection}. Resolution needed within 24 hrs."
        )
    
    # Log for pattern analysis
    log_objection_pattern(objection, resolution)
```

---

## 📈 Agent Learning Over Time

### Week 1 (May 14-20): Agents Learning
- Agents collect signals but thresholds may be off
- Manual calibration: CEO reviews agent decisions daily
- Adjust thresholds: If agent_accuracy > 80%, increase automation level

### Week 2 (May 21-27): Agents Optimizing
- Agents act on patterns with higher confidence
- Fewer manual overrides needed
- Thresholds stabilize

### Week 3+ (May 28+): Agents Predicting
- Agents anticipate problems before they occur
- Proactive vs. reactive
- Apply to next ventures with pre-trained thresholds

---

## 🎯 Success Targets (May 27)

| Agent | Metric | Target |
|-------|--------|--------|
| Sales Optimization | Email version improvement | +15% open rate |
| Sales Optimization | Objection script effectiveness | -50% objections by count |
| Trial Optimization | Trial-to-paid conversion | 40% → 55% |
| Trial Optimization | Setup time improvement | 40 mins → 26 mins |
| Crew Productivity | Crew utilization variance | <15% |
| Crew Productivity | Setup time consistency | All crews <30 mins |
| Revenue MRR | Upsell rate | 15-20% of Starters → Pro |
| Revenue MRR | Churn rate | <5% (from early intervention) |
| Revenue MRR | MRR projection accuracy | Within ±10% of actual |

---

## 📋 Activation Checklist (May 14-15)

- [ ] Create Supabase functions for each agent decision loop
- [ ] Setup Slack alerts + email automation
- [ ] Calibrate thresholds (conservative at first, loosen May 20+)
- [ ] Test each agent with synthetic data (May 14)
- [ ] Go live with Sales Optimization agent (May 15, 6 AM)
- [ ] Go live with Trial Optimization agent (May 16, 6 AM)
- [ ] Go live with Crew Productivity agent (May 17, 6 AM)
- [ ] Go live with Revenue MRR agent (May 18, 6 AM)
- [ ] Daily review of agent decisions (CEO + Sector Leads, 5 PM daily)
- [ ] Threshold calibration sync (Ops Manager, Tue/Fri 9 AM)

---

## 🔗 Integration with Niche Mastery OS

**Layer 3 (Feedback Loops)**: Agent decisions automatically captured  
**Layer 4 (Abstraction)**: Agent success rates feed into model training  
**Layer 6 (Simulation)**: Agent-generated data informs "what if" scenarios  
**Layer 10 (Meta-Learning)**: Agent learnings transfer to Ventures 2+

**Example**: "Sales Optimization Agent learned warm intros convert at 2.8x cold email. Apply this multiplier to Venture 2 (Construction Scheduling)."
