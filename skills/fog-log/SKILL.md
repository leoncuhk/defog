---
name: fog-log
description: During implementation, log deviations and newly discovered fog to the ledger instead of stopping or silently improvising. Use whenever implementing against a plan.
---

# Fog Log

First act: if `FOG.md` or `PLAN.md` exists, read both and announce the open count — a launch packet only works if the receiving session opens it.

When the territory contradicts the map: take the most reversible option, log it, update the plan line it invalidates, and keep going — do not block on the user. Stop and ask only for architecture, data migration, security, cost, or anything that changes what the user was promised — even if the response shape looks the same. Stop at a coherent checkpoint (stub, don't half-build); unrelated work may continue while you wait.

Feeling certain is not evidence of safety. Before touching a running service, shared resource, or config other components depend on, re-read the ledger's constraints and deviations — straightforward-sounding steps are where sessions do silent damage.

Log to `FOG.md` under `## Deviations` (create the section on first write): what the plan said, what was done instead, why, what revisiting costs — 2–3 lines each. New unknowns discovered mid-build go to `Open` with resolvers, even if resolved seconds later.

An unlogged deviation is worse than none — the ledger claims completeness.
