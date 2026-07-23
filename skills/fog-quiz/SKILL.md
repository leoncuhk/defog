---
name: fog-quiz
description: Generate a merge-gate quiz from the ledger, cross-checked against the diff — questions target what was actually uncertain.
disable-model-invocation: true
---

# Fog Quiz

The ledger records where the fog was, so quiz from it. But the ledger can only grade what it logged — so first **reconcile ledger against diff**: scan the actual changes for anything no plan step, resolved item, or deviation accounts for. Unaccounted changes are unlogged deviations; add them to the ledger before quizzing, and flag them to the user — they are the highest-risk items in the room.

Then a report, grouped by intent: what changed, how it interacts with existing code paths, and the 2–3 mental-model updates the user should walk away with.

Then 5–8 questions drawn from the ledger — resolved decisions, deviations (especially the just-discovered ones), standing assumptions — weighted toward what would bite an unaware maintainer. Mix recall ("what happens to in-flight jobs during deploy now?") with prediction ("someone calls X with a stale token — what do they see?").

Grade honestly, one round at a time. A miss is either a gap in the user's model or a change too clever — say which. Never pass out of politeness: a false pass defeats the gate. Two failed rounds → recommend splitting or simplifying the change, not a third quiz.

Pass = merge-ready. Offer the ledger's death rite (`fog` skill): graduate the whys worth keeping, delete the file.
