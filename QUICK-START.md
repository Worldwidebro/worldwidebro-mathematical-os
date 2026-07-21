# QUICK-START.md — 5-Minute Platform Onboarding

You have 2,000 skills. 300+ agents. Every MCP imaginable. **You've used zero.**

This fixes it in 5 minutes.

---

## Minute 1: CLI Works?

```bash
platform registry agents
platform registry skills
```

If you see numbers, you're connected. Done.

---

## Minute 2: Find What You Need

```bash
platform skill search "email"
platform agent list --capability "support"
platform mcp list --category "database"
```

Pick ONE. Note its name.

---

## Minute 3: Understand It

```bash
platform skill get send-email-smtp
platform agent get finance-analyst
platform mcp get postgres-primary
```

Read the output. You'll see parameters, returns, examples.

---

## Minute 4: Run It

```bash
# Dry run first
platform skill invoke send-email-smtp --params '{"to":"you@company.com","subject":"Test","body":"Platform alive."}' --dry-run

# Remove --dry-run if it looks right
platform skill invoke send-email-smtp --params '{"to":"you@company.com","subject":"Test","body":"Platform alive."}'
```

---

## Minute 5: Agent on Real Work

```bash
platform agent run support-triage-agent --task "Triage the last 20 support tickets"
platform agent logs support-triage-agent --follow
```

---

## That's It

**4 verbs:**
1. Search → `platform skill search "..."`
2. Get → `platform skill get <name>`
3. Invoke/Run → `platform skill invoke` OR `platform agent run`
4. Monitor → `platform agent logs <name> --follow`

Everything else is variations.

---

**For details:** See `COMMANDS.md`  
**For operations:** See `OPERATIONS-RUNBOOK.md`  
**For help:** `platform <anything> --help`
