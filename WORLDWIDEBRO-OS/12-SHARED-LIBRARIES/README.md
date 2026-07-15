---
name: shared-libraries-layer
type: Proprietary reusable code — separation layer
date: 2026-07-03
---

# 12-SHARED-LIBRARIES

**This folder is new and currently empty on purpose.** It did not exist before 2026-07-03.
Nothing has been moved into it — this establishes where reusable, proprietary code
(auth, logging, prompting, evaluation, database, vector, payments, email, common utils)
belongs going forward, separate from `11-OPEN-SOURCE` (third-party, unmodified where
possible) and from individual venture/product code.

Numbered 12 (not 04) because `04` is already taken by `04-OPERATIONS`.

## Why this didn't exist before

Reusable code currently lives scattered inside `06-TECHNOLOGY/repositories/` alongside
third-party repos — e.g. `iza-os`, `iza-os-marketing-core`, `iza-os-rag-system`,
`design-system`, `design-system-integrated`, `design-system-live`, `portfolio-mcp`,
`mcp-dashboard` look like candidates, but that's a guess from folder names, not a verified
audit. See `11-OPEN-SOURCE/README.md` for the same caveat on the open-source side.

## Convention going forward

New shared/reusable modules should land here, one subfolder per concern (e.g.
`authentication/`, `prompting/`, `vector/`), referenced by ventures and products rather
than duplicated into each one.
