---
name: fog
description: Maintain a FOG.md unknowns ledger for a task. Use when a task has unresolved decisions or unverified constraints, when the user mentions unknowns or the fog ledger, or when another fog-* skill needs the ledger rules.
---

# Fog

Fog is the gap between the map (prompt, plan, assumptions) and the territory (codebase, APIs, real constraints, user taste). The ledger makes fog visible and burns it down to a defined end.

## The ledger

One file per task: `FOG.md`, next to where the work happens (or where the user says). If several tasks share a directory, use `FOG-<task-slug>.md`.

```markdown
# FOG: <task>

## Open
- [KU] <decision the user must make> → ask
- [UK] <taste the user will recognize on sight> → show
- [UU?] <suspected constraint nobody has checked> → scout

## Assumed
- [A] <default taken> — reversible at <what revisiting costs>

## Resolved
- [x] <decision or finding> (<who: user | territory>, <date>) — <why>

## Deviations            <!-- appears once implementation starts -->
- <plan said / did instead / why / cost to revisit>
```

## Quadrants and their resolvers

| Tag | Fog type | Resolver |
|---|---|---|
| — | Known known | Not fog. Straight into the spec. |
| `KU` | Known unknown, **fact** | Look it up in the territory. Never ask what code or docs can answer. |
| `KU` | Known unknown, **decision** | → `fog-ask` |
| `UK` | Unknown known — taste, recognized only on sight | → `fog-show` |
| `UU?` | Suspected unknown unknown | → `fog-scout` |
| `A` | Low-risk residue | Take the most reversible default and label it. |

## Rules

- **Every open item carries its resolver.** The ledger is a work queue, not a diary.
- **Burn-down is visible.** When resolving, announce the count: "3 open, 1 assumed." Planning is complete when every open item is resolved or converted to a labeled assumption.
- **Assumptions are vetoable, not silent.** Present them as one batch; never interleave with blocking questions.
- **Resolved keeps its why** — decisions and territory findings that shaped the plan. Trivia that shaped nothing is dropped.

## Lifecycle

- **Birth:** any fog-* skill that would write to a missing ledger creates it first.
- **Handoff:** the ledger plus the persisted plan (see `fog-plan`) is the launch packet — hand both to any fresh context or subagent.
- **Death:** after the merge gate passes, graduate whys worth keeping into ADRs, docs, or the commit message, then delete the ledger. It is working memory, not documentation.
