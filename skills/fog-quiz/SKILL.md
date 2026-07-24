---
name: fog-quiz
description: Generate a merge-gate quiz from the ledger, cross-checked against the diff — questions target what was actually uncertain.
disable-model-invocation: true
---

# Fog Quiz

The ledger can only grade what it logged — so first **reconcile ledger against diff**: scan the actual changes for anything no plan step, resolved item, or deviation accounts for. Unaccounted changes are unlogged deviations — the highest-risk items in the room. Each must be dispositioned before the gate can pass: the user owns it (moves it to `Resolved` with a why) or it is reverted or split into its own change.

Then a report, grouped by intent: what changed, how it interacts with existing code paths, and the 2–3 mental-model updates the user should walk away with.

Then the quiz, scaled to the fog it guards: if reconciliation found no unlogged deviations and the ledger holds fewer than ~4 entries, one round of 2–3 questions suffices. Otherwise a **round** is 5–8 questions drawn from the ledger — resolved decisions, deviations (especially just-discovered ones), standing assumptions — asked and graded **one question at a time**, never in bulk. Mix recall ("what happens to in-flight jobs during deploy now?") with prediction ("someone calls X with a stale token — what do they see?"). Weight toward what would bite an unaware maintainer.

Grade honestly. A miss is either a gap in the user's model or a change too clever — say which. Never pass out of politeness. A round passes when every question is answered correctly. After a failed round: walk the missed ledger entries with the user, then run a second round of variant questions on the missed ground — never reuse questions verbatim. Two failed rounds → recommend splitting or simplifying the change, not a third quiz.

Pass = merge-ready. Offer the ledger's death rite (`fog` skill): graduate the whys worth keeping, delete the file.
