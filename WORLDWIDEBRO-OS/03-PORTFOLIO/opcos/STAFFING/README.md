# STAFFING — same OpCo as Professional Services

**Not a separate sector.** `opcos/PROFESSIONAL-SERVICES/CLAUDE.md` line 8 declares
`OPCO: OPCO-Staffing` — the 25 `PS-XXX` ventures in that folder and the projects here
(`staffing-os`, `marketeam`) are the same business unit under two folder names. This
is a pre-existing taxonomy/folder-structure mismatch, not an intentional split.

**Not yet merged.** Found 2026-07-09; flagged rather than moved because the repos
here are actively committed projects and a folder move should happen with the repo
owner present, not mid-session while unattended. See `AGENTS.md` (Documents root,
`## CRM (Twenty)` section) for the related finding on this OpCo's CRM data.

**When someone does the merge:** move `staffing-os/`, `marketeam/`, `go-to-market/`
into `opcos/PROFESSIONAL-SERVICES/`, delete this folder, and extend that folder's
`CLAUDE.md` to list these two projects alongside the 25 `PS-XXX` ventures.

**The real, deployed staffing venture** (`ops-staff-001-staffing`, Charlotte trades
placement, live at ops-staff-001-staffing.vercel.app) lives at the Documents root,
outside this folder entirely — it won't auto-load either this file or
`PROFESSIONAL-SERVICES/CLAUDE.md` via Claude Code's directory-tree walking. It needs
its own `AGENTS.md` if/when someone wants venture-specific context to load
automatically there.
