---
name: fog-log
description: During implementation, log deviations and newly discovered fog to the ledger instead of stopping or silently improvising. Use whenever implementing against a plan.
---

# Fog Log

When the territory contradicts the plan: take the most reversible option, log it, keep going — do not block on the user. Stop and ask only for architecture, data migration, security, cost, or user-visible behavior. When docs contradict the map, the territory wins; update the plan and log the correction.

Log to `FOG.md` under `## Deviations`: what the plan said, what was done instead, why, what revisiting costs — 2–3 lines each. New unknowns discovered mid-build go to `Open` with resolvers, even if resolved seconds later.

An unlogged deviation is worse than none — the ledger claims completeness. At session end, append a **Session summary** at the bottom of `## Deviations`: deviation count, the one most likely to be revisited, and what the next session should read first.
