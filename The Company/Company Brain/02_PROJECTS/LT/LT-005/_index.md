# LT-005: HealthRoute Medical Courier Dispatch

## Overview
- **Venture**: [[23-VENTURES/LT-005|HealthRoute Logistics LLC]]
- **Sector**: [[SECTORS/SEC-017-logistics-transportation|Logistics & Transportation]]
- **Repo**: [`Worldwidebro/lt-005-medical-courier-dispatch`](https://github.com/Worldwidebro/lt-005-medical-courier-dispatch) (Commit `1c7116a`)
- **Portal**: https://healthroute-courier.vercel.app

## State Machine Architecture & Email Engines
- **Blueprint**: [[docs/EMAIL-REVENUE-FUNNEL-STATE-MACHINE|Email Revenue Funnel State Machine]] (Sections A–W)
- **Database Schema**: `supabase/migrations/20260913_funnel_state_machine.sql`
- **Engines**:
  - Inbound Comprehension: `lib/email_intelligence.js` (`agency-email-intelligence-engineer`)
  - Outbound Deliverability: `lib/email_marketing.js` (`agency-email-marketing-strategist`)
  - Test Suite: `test/test_email_engine.js` (17/17 automated tests passing)
