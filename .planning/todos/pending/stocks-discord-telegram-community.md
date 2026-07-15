---
title: Launch stocks Discord+Telegram community
date: 2026-07-13
priority: medium
---

# Launch stocks Discord+Telegram community

New venture concept — not a fit for any existing registry entry (checked `ventures.csv`: FIN-023 Investment Portfolio AI and FIN-031 Investor Dashboard Builder are planned software tools, not community ventures; EM-015 Crypto Trading AI is also tool-shaped, not community-shaped). No venture_id assigned yet.

## What it is

A paid (~$50/mo) community around stock market content, mirrored across Discord and Telegram via a shared bot backend (both platforms have free, well-documented bot APIs — a single backend can post to both). WhatsApp explicitly excluded from this one: no free real-time group-broadcast bot API, requires WhatsApp Business Platform + approved message templates + per-message cost, doesn't fit live community chat the way Discord/Telegram do.

## Content framing (deliberately chosen)

**"Here's what I'm personally trading and why"** — disclosure of personal positions/reasoning as education, not individualized buy/sell recommendations. This was chosen specifically to reduce regulatory exposure: content combining general market commentary with direct "buy this" recommendations in exchange for a subscription fee is the fact pattern that risks looking like unregistered investment advice. Personal-disclosure framing (own trades, own reasoning, clear it's not a recommendation) sits on safer ground, though this is not a substitute for actual legal review before charging money — flagged, not resolved, in this session.

## Open items before building

- No venture_id / entity assigned — decide whether this becomes a formal FIN-sector venture entry or stays informal
- Bot backend build: Discord.py/discord.js + Telegram Bot API, shared content pipeline
- Payment/paid-access gating (Stripe → Discord paid role + Telegram invite link)
- Actual compliance review of the disclosure framing before charging money — this session flagged the concern and picked a safer structure, did not get legal sign-off
