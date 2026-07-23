---
name: fog-scout
description: Sweep unfamiliar territory for unknown unknowns before the plan hardens. Use when the user enters an unfamiliar codebase area or domain, asks for a blindspot pass, or a FOG.md item is tagged → scout.
---

# Fog Scout

Go look for what the user doesn't know exists: the module and its history, conventions and half-migrated patterns, documented limits of load-bearing dependencies, prior art in and out of the repo. The territory is read-only — record findings, never repair them.

Deliver the report in your reply, four sections, items ranked within each by how much they would change the plan:

- **Landmines** — mistakes a newcomer here typically makes.
- **Hidden constraints** — decisions already made that bound the work; invariants that must hold.
- **What good looks like** — 2–3 concrete examples to calibrate against.
- **Questions an expert would ask** — with your best-guess answer for each.

Then write the findings into the ledger (`fog` skill): territory facts to `Resolved` with their why, defaults to `Assumed`, remaining questions to `Open` with resolvers — including new `UU?`s for a deeper scout. Confirmed-safe areas are dropped unless a later step would act differently knowing them.

End by rewriting the user's original request as the territory shows it should read, and make it the ledger's `# FOG:` title — the map, corrected.

Scouting ends at understanding — no implementation. "No significant fog here" is a valid, valuable report.
