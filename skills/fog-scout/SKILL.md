---
name: fog-scout
description: Sweep unfamiliar territory for unknown unknowns before the plan hardens. Use when the user enters an unfamiliar codebase area or domain, asks for a blindspot pass, or a FOG.md item is tagged → scout.
---

# Fog Scout

Go look for what the user doesn't know exists: the module and its history, conventions and half-migrated patterns, documented limits of load-bearing dependencies, prior art in and out of the repo.

Report four things, ranked by how much each would change the plan:

- **Landmines** — mistakes a newcomer here typically makes.
- **Hidden constraints** — decisions already made that bound the work; invariants that must hold.
- **What good looks like** — 2–3 concrete examples to calibrate against.
- **Questions an expert would ask** — with your best-guess answer for each.

Then write the findings into the ledger (`fog` skill): new `KU`/`UK` items with resolvers; areas confirmed safe are dropped unless the confirmation shaped the plan. End by rewriting the user's original request as the territory shows it should read — the map, corrected.

Scouting ends at understanding — no implementation. "No significant fog here" is a valid, valuable report.
