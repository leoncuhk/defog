---
name: fog-ask
description: Resolve open decisions in the ledger by interviewing the user, one evidence-priced question at a time. Use when FOG.md has open KU decision items, or the user asks to be grilled about a plan.
---

# Fog Ask

Decisions belong to the user; facts belong to the territory. Before asking anything, strike every item the codebase or docs can answer yourself.

For what remains, ask **one question per turn**, highest blast radius first — answers that would change the architecture before answers that pick a default. Every question must pass three gates: **material** (the answer changes the plan), **grounded** (points at evidence, not preference fishing), **answerable** (options plus a recommended default the user can wave through).

Format:

> **Question:** …
> **Why it matters:** what changes between answers
> **Evidence:** file / doc / test citation
> **Recommended:** default + why. Silence = this.

Budget: ~5 blocking questions. Past that, ask whether to continue. **Fatigue valve:** answers going one-word or "just pick" → stop interviewing, convert the rest to `[A]` assumptions, present the batch for veto.

Write each answer to `Resolved` with its why. An answer defaulted through silence is recorded as `[A]`, not as a user decision. Done when no open `KU` decisions remain.
