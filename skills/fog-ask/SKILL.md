---
name: fog-ask
description: Resolve open decisions in the ledger by interviewing the user, one evidence-priced question at a time. Use when FOG.md has open KU decision items, or the user asks to be grilled about a plan.
---

# Fog Ask

Decisions belong to the user; facts belong to the territory. Before asking anything, re-triage every open item as fact or decision, and strike the facts via `→ lookup` yourself.

For what remains, ask **one question per turn**, highest blast radius first — answers that would change the architecture before answers that pick a default. Every question must pass three gates: **material** (the answer changes the plan), **grounded** (points at evidence, not preference fishing), **answerable** (options plus a recommended default the user can wave through).

Format:

> **Question:** …
> **Why it matters:** what changes between answers
> **Evidence:** file / doc / test citation
> **Recommended:** default + why. Silence = this.

Silence means the user's next message doesn't address the question, or they tell you to proceed.

Exits — both land the same way: convert every remaining item to `[A]`, present the batch for veto.

- **Budget:** hard cap of 5 blocking questions.
- **Fatigue valve:** one "just pick"-class or one-word reply fires it, and the question that drew it counts as unanswered.

If the user asks for everything at once, present the whole remaining frontier as one numbered round — recommendations attached — and treat unanswered items as silence.

Write each real answer to `Resolved` with its why. A defaulted answer goes to `Assumed` as `[A]`, never to `Resolved`. Done when no open `KU` decisions remain.
