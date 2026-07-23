---
name: fog-plan
description: Turn a burned-down ledger into a persisted plan ordered by decision volatility — likeliest-to-change first, mechanical work last.
disable-model-invocation: true
---

# Fog Plan

A plan's job is not to prove completeness; it's to put the expensive-to-change decisions in front of the user while changing them is still free.

Before writing: any item still open converts to a labeled `[A]` assumption or blocks the plan — a plan over open fog is a guess.

Order by volatility, sourced from the ledger:

1. **Decisions you may want to tweak** — data model, interfaces, user-facing behavior. Each: the choice, one alternative considered, what changing it later costs. (From `Resolved`.)
2. **Assumptions standing** — the `[A]` batch: one line each, veto window, and the pivot signal — what observation during implementation forces revisiting it.
3. **Mechanical work** — compressed. The user trusts you here; reviewing it wastes their attention.

Write the plan to `PLAN.md` beside the ledger (`PLAN-<task-slug>.md` if the ledger is slugged) — the two files together are the launch packet for a fresh session.

End with the 2–4 items you need a yes or no on before starting. Keep the plan reviewable in minutes.
