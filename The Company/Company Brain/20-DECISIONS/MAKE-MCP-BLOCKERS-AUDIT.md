# Make MCP Blockers Audit — Sep 12, 2026

**Status:** 🔴 **BLOCKED** — Admin permission issue preventing scenario creation  
**Severity:** HIGH — Blocking LT-005 automation deployment  
**Root Cause:** Make MCP scopes insufficient for `organization view` + `scenarios_create`

---

## Errors Encountered

### Error 1: Insufficient Rights (scenarios_list)
```
MakeApiError: Insufficient rights, admin permission "organization view" is needed.
Call: mcp__claude_ai_Make__scenarios_list(teamId=1)
```

### Error 2: Insufficient Rights (apps_list)
```
MakeApiError: Insufficient rights, admin permission "organization view" is needed.
Call: mcp__claude_ai_Make__apps_list(organizationId=3363991, teamId=1)
```

### Error 3: Token Expired
```
MakeApiError: MCP server "claude.ai Make" requires re-authorization (token expired)
Call: After `/mcp status` showed "Reconnected"
```

### Error 4: Insufficient Rights (scenarios_create)
```
MakeApiError: Insufficient rights, admin permission "organization view" is needed.
Call: mcp__claude_ai_Make__scenarios_create(teamId=1, blueprint={...})
```

---

## Blockers

| # | Blocker | Cause | Impact | Fix |
|---|---------|-------|--------|-----|
| **B1** | Missing Admin Scopes | MCP token granted but doesn't include admin/organization view | Cannot list/create scenarios | Re-auth Make with explicit admin scopes |
| **B2** | Wrong TeamId | Using teamId=1 (default) but user's actual team may differ | API rejects calls even with auth | Discover real team ID from Make API |
| **B3** | Organization vs Team Permissions | Make distinguishes org-level vs team-level roles | organizationId works but teamId doesn't have rights | Elevate user role in Make workspace |
| **B4** | Token Expiry After Re-auth | `/mcp status` showed reconnected but token was invalid | Forced re-auth mid-workflow | Make better auth state tracking |
| **B5** | User Role in Make Workspace | User (Divine) may not be org/team admin | MCP calls require admin-level access | Check Make user role + elevate if needed |
| **B6** | Scope Declaration Missing | MCP auth flow didn't request explicit scopes | Token has baseline access but not admin | Store + pass scope list on re-auth |

---

## What We Know

### ✅ Working
- `users_me()` call succeeded → MCP is connected + authenticated
- **User:** Divine
- **Email:** winnerscirclewcllc@gmail.com
- **User ID:** 3247259
- **Make Role:** Owner (verified Sep 12, 12:49 PM)
- **Organization:** Winners Circle
- **Organization ID:** 3363991
- **Supabase Project:** aipehhzlsmfxxzwceppd
- **Supabase:** ✅ Complete (3 tables, 25 facilities loaded)

### ❌ Not Working
- `scenarios_list()` → "admin permission needed"
- `apps_list()` → "admin permission needed"
- `scenarios_create()` → "admin permission needed"
- Token persistence → expires after reconnect

---

## Root Cause Analysis

Make.com distinguishes **3 permission levels**:
1. **User Level:** Basic access (can view own stuff)
2. **Team Level:** Can manage team's scenarios + apps
3. **Organization Level:** Can view org config + admin functions

**Our Issue:** MCP token has **User** level, needs **Team** + **Organization** level.

---

## Steps to Fix

### Step 1: Verify User Role in Make
```bash
# Check: Is your Make account an admin?
Go to: https://us2.make.com/organization/3051755/settings/members
Look for your email (winnerscirclewcllc@gmail.com)
Expected: Role should be "Owner" or "Admin"
Actual: ???
```

### Step 2: Re-authorize Make with Explicit Scopes
```bash
/mcp disconnect make
# Then explicitly in browser:
# Make sure to grant: scenarios:read, scenarios:write, apps:read, organization:view
/mcp
# Select Make → Sign in → Grant all permissions
```

### Step 3: Discover Real Team ID
Once re-authed, run:
```bash
/mcp
Make → Check stored credentials → should show team ID
```

### Step 4: Test Auth State
```bash
# This should work after re-auth:
/mcp status
# Output should show: "✓ Make: connected (winnerscirclewcllc@gmail.com) — scopes: [admin, scenarios, organization]"
```

---

## Success Criteria

When fixed, these should all work:

```bash
# Should return user data
mcp__claude_ai_Make__users_me()  ✓ Already works

# Should return list of scenarios
mcp__claude_ai_Make__scenarios_list(teamId=<REAL_TEAM_ID>)  ✗ Currently blocked

# Should return list of available apps
mcp__claude_ai_Make__apps_list(organizationId=3363991, teamId=<REAL_TEAM_ID>)  ✗ Currently blocked

# Should create LT-005 scenario
mcp__claude_ai_Make__scenarios_create(teamId=<REAL_TEAM_ID>, blueprint={...})  ✗ Currently blocked
```

---

## Workaround (Not Recommended)

Build LT-005 scenario manually in Make UI (BrowserOS Neo):
1. make.com/scenarios
2. Create new → Add Supabase trigger
3. Add Gmail action → Twilio → Supabase logging
4. Save & activate

**But:** This doesn't fix the root issue. We need proper MCP auth for:
- Automation via Claude Code
- Future scenarios
- Integrated testing

---

## Action Items

**Priority 1 (BLOCKER):**
- [ ] Verify user role in Make workspace (Owner/Admin?)
- [ ] Re-authenticate Make with explicit admin scopes
- [ ] Discover real team ID from Make API
- [ ] Test scenarios_list() to confirm fix

**Priority 2 (LT-005 Deployment):**
- [ ] Once auth fixed: Create LT-005 scenario via Make MCP
- [ ] Wire Supabase → Gmail → Twilio → Supabase
- [ ] Set schedule: every 6 hours
- [ ] Activate & test first outreach

**Priority 3 (Prevent Future Issues):**
- [ ] Document Make auth flow in CLAUDE.md
- [ ] Create Make MCP integration test suite
- [ ] Add auth-scope validation before scenario creation

---

## Timeline

**Today (Sep 12):**
- [ ] Fix auth (30 min)
- [ ] Deploy LT-005 (15 min)
- [ ] Test first outreach (15 min)

**This week:**
- Start generating revenue from LT-005
- Replicate pattern to OPS-001, CON-001, RE-001

---

## Questions for User

1. **Are you an Owner/Admin** in your Make workspace?
2. **Do you want me to fix this now**, or handle LT-005 via manual UI?
3. **Should I create a Make MCP test suite** to prevent future auth issues?
