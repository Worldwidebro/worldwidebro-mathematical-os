# Venture Orchestration Autopilot

Auto-wire any venture from code → income in one command.

## Skill Dispatch: `/venture-ready {VENTURE_ID} --full-setup`

Execute in parallel:
1. **Audit** — verify venture has code + deployment target
2. **Stripe** — add payment processing (API keys, webhook)
3. **n8n workflow** — customer → invoice → payment → receipt email
4. **Supabase** — create venture_invoices, deal_payments tables
5. **Env** — inject STRIPE_KEY, SUPABASE_URL into .env + Vercel secrets
6. **Deploy** — push to Vercel
7. **Test** — smoke test payment flow (test card)
8. **Commit** — `chore: ready {VENTURE_ID} for revenue`
9. **Report** — live URL + status

## Status Board (from audit)

**Ready NOW (1 hour each):**
- ✅ CON-001 (has Vercel + code)
- ✅ EC-111 (has Vercel + code)
- ✅ OPS-001 (has Vercel + code)

**Ready in 2 hours:**
- captable (has Stripe + code, needs Vercel)
- mcp-dashboard (has Stripe + code, needs Vercel)
- +6 more with Vercel

**Audit summary:**
- 8 repos with Vercel deployed
- 2 repos with Stripe configured
- 0 repos with BOTH (no ready-now candidates currently)
- ~700 ventures need payment wiring

## Token Cost

This session estimate:
- Audit scan: 2K tokens
- Full 712 scan: 35K tokens
- Orchestration setup: 1K tokens
- Per `/venture-ready` run: 5K tokens
- **Total session: ~40-50K tokens**

## Execute

```bash
# Audit all 712 (detailed, ~1 hour)
/audit scan-all-ventures --detailed

# Wire 3 pilots in parallel (~3 hours)
/venture-ready CON-001 --full-setup &
/venture-ready EC-111 --full-setup &
/venture-ready OPS-001 --full-setup &
wait

# Live check
curl https://con-001-staging.vercel.app/api/test-payment
# Should return: {"status":"ready","stripe":"connected"}
```

## Files Created

- `.claude/ORCHESTRATION.md` — this file
- `.claude/audit-rules.md` — gap detection (next step)
- `.claude/skill-dispatch.yaml` — MCP routing (next step)

## Notes

Ponytail: Not building full infrastructure yet — just enough to wire 3 ventures to revenue. Expand when/if needed.
