---
description: Pre-flight QA verification and zero-hour launch execution for a Company Brain campaign
globs: CAMPAIGNS/**
---

# /campaign-launch Workflow

Run this workflow to execute a safe, zero-defect campaign launch conforming to AntiGravity Rule #3 (no fake completion).

## Steps:

1. **Verify Canonical Campaign Record:**
   - Read the target campaign file (e.g., `CAMPAIGNS/CAMPAIGN.md`).
   - Confirm all metadata fields are populated (status, budget, offer_id, owner).

2. **Execute Pre-Flight QA Verification:**
   - Run through all items in [[CAMPAIGNS/LAUNCH-CHECKLIST.md]].
   - Verify calendar booking links (Cal.com) resolve cleanly.
   - Verify tracking webhooks and UTM parameters in `_REGISTRIES/CAMPAIGN-UTM-REGISTRY.json`.
   - Verify Stripe / Mercury escrow deposit payment link is active.

3. **Check Circuit Breakers & Stop-Rules:**
   - Confirm daily spending caps ($150/day) and deliverability bounce caps (<2%) are configured in [[CAMPAIGNS/STOP-RULES.md]].

4. **Execute Launch & Update State:**
   - Set campaign `status: LIVE` and `reality_status: VERIFIED`.
   - Record launch timestamp in `_REGISTRIES/CAMPAIGN-REGISTRY.json`.
   - Dispatch first wave of communications via Outbound Strategist.
