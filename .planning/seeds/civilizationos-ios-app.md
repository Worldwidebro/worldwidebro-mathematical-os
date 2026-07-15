---
title: CivilizationOS iOS app
trigger_condition: 5-10 ventures reach business_complete status (per venture-completion-definition)
planted_date: 2026-07-12
---

# CivilizationOS iOS app

Full spec pasted by user 2026-07-12: an executive-operating-system iOS app (SwiftUI, TabView nav) covering Portfolio, AI agent center, Finance, CRM, Infrastructure monitoring, Knowledge Graph, Alerts, and an AI-chat command interface — modeled on Berkshire Hathaway portfolio oversight + Linear + Notion + Bloomberg dashboards.

## Why deferred, not built now

Zero ventures currently generate revenue (see `[[venture-completion-definition]]`), so there is no real data to power a "Today's Revenue / MRR / Portfolio Health" dashboard — it would be instrumentation for a business that doesn't exist yet. Building it now means designing screens around fabricated or empty data.

## Trigger to revisit

Once 5-10 ventures independently hit business_complete (2 consecutive months of nonzero revenue), there's enough real signal to justify a dashboard, and the earliest screens to build first would likely be Home Dashboard + Portfolio (the two most data-dependent, most-used sections per the original spec).
