---
name: fog
description: Maintain a FOG.md unknowns ledger for a task. Use when a task has unresolved decisions or unverified constraints, when the user mentions unknowns or the fog ledger, or when another fog-* skill needs the ledger rules.
---

# Fog

Fog is the gap between the map (prompt, plan, assumptions) and the territory (codebase, APIs, real constraints, user taste). The ledger makes fog visible and burns it down to a defined end.

## The ledger

One file per task: `FOG.md`, next to where the work happens (or where the user says). When a second task joins the directory, rename the existing ledger to `FOG-<task-slug>.md` before creating the new one, also slugged.

```markdown
# FOG: <task>

## Open
- [KU] <fact to verify> → lookup
- [KU] <decision the user must make> → ask
- [UK] <taste the user will recognize on sight> → show
- [UU?] <suspected constraint nobody has checked> → scout

## Assumed
- [A] <default taken> — cost to revisit: <cost>

## Resolved
- [x] <decision or finding> (<who: user | territory>, <date>) — <why>

## Deviations            <!-- add on first deviation; never keep it empty -->
- <plan said / did instead / why / cost to revisit>
```

`territory` covers anything verified against the real system, including your own experiments. Each arrow names the resolver: `→ lookup` you do yourself; the rest are the matching fog-* skill.

## Quadrants and their resolvers

| Tag | Fog type | Resolver |
|---|---|---|
| — | Known known | Not fog. Straight into the spec. |
| `KU` | Known unknown, **fact** | `→ lookup` — the territory answers it. Never ask what code or docs can answer. |
| `KU` | Known unknown, **decision** | `→ ask` (`fog-ask`) |
| `UK` | Unknown known — taste, recognized only on sight | `→ show` (`fog-show`) |
| `UU?` | Suspected unknown unknown | `→ scout` (`fog-scout`) |
| `A` | Low-risk residue | Take the most reversible default and label it. |

## Rules

- **Every open item carries its resolver.** The ledger is a work queue, not a diary.
- **Burn-down is visible.** Announce `<n> open, <m> assumed` after every ledger write. Planning is complete when every open item is resolved or converted to a labeled assumption.
- **Assumptions are vetoable, not silent.** Present them as one batch; never interleave with blocking questions.
- **Resolved keeps its why** — decisions and territory findings that shaped the plan. A finding shaped the plan only if a later step would act differently knowing it; the rest is dropped.

## Lifecycle

- **Birth:** any fog-* skill that would write to a missing ledger (or section) creates it first.
- **Handoff:** the ledger plus the persisted plan (see `fog-plan`) is the launch packet — hand both to any fresh context or subagent.
- **Death:** after the task's acceptance gate (merge, sign-off, or delivery) passes, graduate whys worth keeping into ADRs, docs, or the commit message, then delete the ledger. It is working memory, not documentation.
