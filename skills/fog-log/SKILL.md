---
name: fog-log
description: During implementation, log deviations and newly discovered fog to the ledger instead of stopping or silently improvising. Use whenever implementing against a plan.
---

# Fog Log

When the territory contradicts the map: take the most reversible option, log it, update the plan line it invalidates, and keep going — do not block on the user. Stop and ask only for architecture, data migration, security, cost, or anything that changes what the user was promised — even if the response shape looks the same. Stop at a coherent checkpoint (stub, don't half-build); unrelated work may continue while you wait.

Log to `FOG.md` under `## Deviations` (create the section on first write): what the plan said, what was done instead, why, what revisiting costs — 2–3 lines each. New unknowns discovered mid-build go to `Open` with resolvers, even if resolved seconds later.

An unlogged deviation is worse than none — the ledger claims completeness. At session end, append a **Session summary** at the bottom of `## Deviations`: deviation count (entries in this section, excluding the summary), the one most likely to be revisited, and what the next session should read first.
