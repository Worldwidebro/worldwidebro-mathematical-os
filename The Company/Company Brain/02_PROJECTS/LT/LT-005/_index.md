# LT-005: HealthRoute Medical Courier Dispatch

## Overview
- **Venture**: [[23-VENTURES/LT-005|HealthRoute Logistics LLC]]
- **Sector**: [[SECTORS/SEC-017-logistics-transportation|Logistics & Transportation]]
- **Repo**: [`Worldwidebro/lt-005-medical-courier-dispatch`](https://github.com/Worldwidebro/lt-005-medical-courier-dispatch) (Commit `0561580`)
- **Portal**: https://healthroute-courier.vercel.app

## State Machine Architecture & Email Engines
- **Blueprint**: [[docs/EMAIL-REVENUE-FUNNEL-STATE-MACHINE|Email Revenue Funnel State Machine]] (Sections A–W)
- **Visual System**: Clean Hero Photo Architecture (Headline above image, real HTML CTA button underneath, 6 operational photo categories)
- **Database Schema**: `supabase/migrations/20260913_funnel_state_machine.sql`
- **Engines**:
  - Inbound Comprehension: `lib/email_intelligence.js` (`agency-email-intelligence-engineer`)
  - Outbound Deliverability: `lib/email_marketing.js` (`agency-email-marketing-strategist`)
  - Test Suite: `test/test_email_engine.js` (19/19 automated tests passing)

