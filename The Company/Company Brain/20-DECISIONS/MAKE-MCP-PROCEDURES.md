# Make.com MCP Integration — Procedures & Reference

**Last Updated:** Sep 12, 2026  
**Status:** Active (Owner-level access verified)  
**Owner:** Divine (winnerscirclewcllc@gmail.com, ID: 3247259)

---

## Identifiers (Bookmark These)

| Component | Value | Purpose |
|-----------|-------|---------|
| **User** | Divine | Account name |
| **Email** | winnerscirclewcllc@gmail.com | Login credential |
| **User ID** | 3247259 | API reference |
| **Organization** | Winners Circle | Make workspace |
| **Org ID** | 3363991 | API calls |
| **Org Settings** | https://us2.make.com/organization/3051755/settings/members | Verify role |
| **Supabase Project** | aipehhzlsmfxxzwceppd | LT-005 data |
| **Supabase URL** | https://aipehhzlsmfxxzwceppd.supabase.co | Database |

---

## Quick Commands

### Check MCP Status
```bash
/mcp status
# Expected output: ✓ Make: connected (winnerscirclewcllc@gmail.com) — Owner access
```

### Test MCP Connection
```bash
# If Make is connected, this should work:
/mcp status | grep -i make
```

### List Make Scenarios (When Fixed)
```bash
# Via Claude Code MCP:
mcp__claude_ai_Make__scenarios_list(teamId=1)
```

### Get User Info
```bash
# Always works when connected:
mcp__claude_ai_Make__users_me()
# Returns: {id: 3247259, name: "Divine", email: "winnerscirclewcllc@gmail.com", ...}
```

---

## Setup Procedure (If Needed Again)

### Initial Setup
```
/mcp
→ Find "Make"
→ Click "Connect"
→ Sign in: winnerscirclewcllc@gmail.com
→ Grant ALL permissions:
   ✅ Scenarios (read, create, update, delete)
   ✅ Apps (read, list)
   ✅ Organization (view, admin)
   ✅ Teams (admin, manage)
→ Complete auth flow
```

### Re-auth (Token Expired)
```
/mcp disconnect make
/mcp
→ Find "Make"
→ Click "Sign in"
→ When prompted: grant ALL permissions (explicit)
→ Complete auth
→ Verify: /mcp status → "Owner access" should appear
```

---

## Scenario Creation Template

### LT-005 (Medical Facility Outreach - Charlotte, NC)

**Scenario ID:** 6252367  
**Status:** ✅ LIVE & ACTIVATED (Sep 12, 2026, 17:46 UTC)  
**Schedule:** Every 6 hours (21,600 seconds)  
**Created by:** Divine (winnerscirclewcllc@gmail.com)

**Modules:**
1. **Webhook Trigger** — HTTP POST (manual or scheduled)
2. **Supabase Query** — Fetch not_contacted facilities
3. **Iterator** — Loop through results
4. **Gmail** — Send outreach email
5. **Supabase Update** — Log outreach attempt
6. **Wait** — 30 seconds (rate limiting)
7. **Supabase Insert** — Log to activity table
8. **Router** — Follow-up logic (optional)

**Connections:**
- Supabase: `aipehhzlsmfxxzwceppd.supabase.co`
- Gmail: `winnerscirclewcllc@gmail.com`
- Vapi: [API key in env]

---

## Deployment Checklist

- [ ] Make MCP authenticated (Owner access verified)
- [ ] Supabase connected (tables exist, 25 facilities loaded)
- [ ] Gmail authorized (OAuth via Make)
- [ ] Vapi tested (cold call functionality verified)
- [ ] LT-005 scenario created via Make MCP
- [ ] Scenario activated and scheduled
- [ ] First test run completed
- [ ] Revenue monitoring dashboard created

---

## Troubleshooting

### "Admin permission needed"
**Problem:** MCP calls fail with "Insufficient rights"  
**Cause:** Token was granted but lacks explicit scopes  
**Fix:** Run re-auth procedure above (disconnect → reconnect with explicit permission grant)

### "Token expired"
**Problem:** `/mcp status` shows "Reconnected" but API calls fail  
**Cause:** Token refreshed but not properly stored  
**Fix:** Disconnect and re-auth with explicit scope grants

### "Wrong teamId"
**Problem:** API accepts auth but rejects scenarios_list  
**Cause:** Using default teamId=1, but real team ID is different  
**Fix:** Check Make workspace settings for actual team ID, update calls

### "User not Owner"
**Problem:** All calls fail with permission denied  
**Cause:** User role is Member/Guest, not Owner/Admin  
**Fix:** Check https://us2.make.com/organization/3051755/settings/members → elevate role

---

## Related Documentation

- **Blockers Audit:** `20-DECISIONS/MAKE-MCP-BLOCKERS-AUDIT.md`
- **Full Integration Audit:** `20-DECISIONS/INTEGRATION-STATUS-FULL-AUDIT.md`
- **LT-005 Automation:** `20-DECISIONS/LT-005-MAKE-AUTOMATION-COMPLETE.md`
- **Master Setup:** `~/.claude/CLAUDE.md` (Make.com MCP section)

---

## Revenue Timeline (Once Deployed)

| Phase | Timeline | Action | Expected Revenue |
|-------|----------|--------|------------------|
| **Setup** | Today (Sep 12) | Deploy LT-005 scenario | $0 (launching) |
| **Week 1** | Sep 13-15 | Test & optimize outreach | $200-300 |
| **Week 2** | Sep 16-20 | Scale facilities + OPS-001 | $800-1,200 |
| **Week 3** | Sep 23-30 | Add CON-001 + RE-001 | $2,000-3,000 |

---

## Owner Contact Info

**If issues arise:**
- Name: Divine
- Email: winnerscirclewcllc@gmail.com
- Make Account: Owner role in Winners Circle workspace
- Verify Role: https://us2.make.com/organization/3051755/settings/members

**Last auth:** Sep 12, 2026, 12:49 PM EST
