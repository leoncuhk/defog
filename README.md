> **Archived — superseded by [terra](https://github.com/leoncuhk/terra)**, the unified successor by the same author. The ideas live on there; this repo is kept read-only for lineage and existing installs.

# defog

[![skills.sh](https://skills.sh/b/leoncuhk/defog)](https://skills.sh/leoncuhk/defog)

**Seven tiny agent skills that burn down the gap between your prompt and reality — through one shared ledger.**

Your prompt is a map. The codebase, the APIs, the real constraints, your own taste — that's the territory. The gap between them is **fog**, and with strong models the quality of agent work is bottlenecked by it: every patch of fog the agent guesses through, and guesses compound.

Existing skill sets attack this from two sides and each leaves a hole:

| | Composable | Stateful | The hole |
|---|---|---|---|
| [mattpocock/skills](https://github.com/mattpocock/skills) | ✅ small, pruned | ❌ | `grill-me` "writes nothing and leaves no workspace behind" — consensus dies with the session |
| [finding-unknowns-skills](https://github.com/Neeeophytee/finding-unknowns-skills) | ✅ 8 independent | ❌ | the 8 skills don't talk to each other; each starts from zero |
| [grill-for-unknowns](https://github.com/nicobailon/grill-for-unknowns) | ❌ 239-line monolith | ✅ ledger + 5 templates | right mechanisms, wrong form — a single skill you can't compose |

defog takes the missing quadrant: **composable AND stateful**. Skills stay tiny (all seven combined are smaller than one monolith), and they compose through a file instead of through conversation memory.

## The ledger

One primitive: `FOG.md`, a per-task unknowns ledger. Every unknown gets a quadrant tag and — this is the point — **its cheapest resolver**:

```markdown
# FOG: order-refund sync

## Open
- [KU] One-way or two-way refund sync? → ask
- [UK] Dashboard density — user will know it on sight → show
- [UU?] Stripe rate limits on bulk refund unverified → scout

## Assumed
- [A] Exponential backoff on retry — cost to revisit: one function

## Resolved
- [x] Webhook endpoint reused, not duplicated (user, 2026-07-23) — idempotency already handled there
```

The ledger is a **work queue, not a diary**. Burn-down is announced ("2 open, 1 assumed"), planning is complete only when every open item is resolved or converted to a labeled assumption, and the file outlives the session — hand it to a fresh context or a subagent and nothing is lost.

## The skills

| Skill | Phase | One move |
|---|---|---|
| [`fog`](skills/fog/SKILL.md) | always | The ledger: format, quadrants, resolver table, rules |
| [`fog-scout`](skills/fog-scout/SKILL.md) | before | Sweep unfamiliar territory for unknown unknowns; end by rewriting the request |
| [`fog-ask`](skills/fog-ask/SKILL.md) | before | One evidence-priced question at a time — with a ~5-question budget and a fatigue valve |
| [`fog-show`](skills/fog-show/SKILL.md) | before | Contrasting throwaway artifacts for taste; the deliverable is the criterion sentence |
| [`fog-plan`](skills/fog-plan/SKILL.md) | gate | Persisted plan ordered by decision volatility — likeliest-to-change first, mechanics last |
| [`fog-log`](skills/fog-log/SKILL.md) | during | Most reversible option, log the deviation, keep going |
| [`fog-quiz`](skills/fog-quiz/SKILL.md) | after | Merge-gate quiz **from the ledger, reconciled against the diff** |

Why quiz from the ledger matters: a quiz generated from a diff asks trivia; a quiz generated from the ledger asks about exactly the decisions, deviations, and assumptions that were once open. But the ledger can only grade what it logged — so the quiz first reconciles the ledger against the diff, and anything unaccounted for surfaces as an unlogged deviation before a single question is asked.

## Install

```bash
npx skills add leoncuhk/defog
```

Or copy any `skills/<name>` folder into `.claude/skills/` (Claude Code), or anywhere your agent reads the [agentskills.io](https://agentskills.io) SKILL.md format. Each skill stands alone; `fog` is the only one others reference.

## A full pass

1. New task in unfamiliar territory → `fog-scout` sweeps, seeds the ledger, rewrites your request.
2. Taste-shaped items → `fog-show`; decision items → `fog-ask` (budgeted, evidence-priced). Facts never get asked — the agent looks them up.
3. Leftover low-risk fog → labeled assumptions, batched for veto.
4. Every item resolved or assumed → `/fog-plan` writes `PLAN.md` beside the ledger. You review only the volatile decisions.
5. Fresh session implements with `FOG.md` + `PLAN.md` as the launch packet; `fog-log` records every deviation.
6. Before merge → `/fog-quiz`: reconcile against the diff, quiz, pass = you actually understand what shipped. Then the ledger's whys graduate to ADRs or the commit message, and the file is deleted — working memory, not documentation.

## Testing

Every skill was behaviorally tested, not just proofread: an agent loads the skill, executes a realistic scenario end to end (a real repo as territory for `fog-scout`, a role-played fatigued user for `fog-ask`, a hidden taste persona for `fog-show`, a git repo with a planted unlogged drive-by change for `fog-quiz`), and grades itself against the skill's own completion criteria. Text ambiguities those runs exposed — an indecisive convert-or-block rule, a Resolved/Assumed contradiction, belief labels priming the user, an undefined quiz round — were fixed before release. `scripts/validate.py` (run in CI) checks frontmatter, naming, cross-references, and the README's own claims.

## Design principles

- **Occam's razor.** One primitive (the ledger), six moves on it. No templates directory, no phases framework, no router — the resolver table in `fog` *is* the router.
- **Every open item carries its resolver.** Classification without a next action is a diary entry, not work.
- **Facts vs decisions.** Anything the territory can answer is never asked. Only genuine decisions and genuine taste reach the user.
- **Budgets over relentlessness.** Interviews have a question budget and a fatigue valve. Not asking about a non-material topic is correct behavior.
- **Written in the style it preaches**: pruned prose, leading words (*fog*, *burn-down*, *blast radius*, *territory wins*), explicit completion criteria — per [writing-great-skills](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md).

## Lineage

defog adapts ideas, with gratitude, from:

- **Matt Pocock** — [skills](https://github.com/mattpocock/skills) (MIT): the grilling loop (one question at a time, facts vs decisions, recommended answers), skill-writing principles.
- **Thariq Shihipar** — [*A Field Guide to Claude Fable 5: Finding Your Unknowns*](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns): the map/territory frame and the four-quadrant taxonomy.
- **Neeeophytee** — [finding-unknowns-skills](https://github.com/Neeeophytee/finding-unknowns-skills) (MIT): belief-labeled prototypes, the criterion sentence, blast-radius question ordering.
- **Nico Bailon** — [grill-for-unknowns](https://github.com/nicobailon/grill-for-unknowns) (MIT): the unknowns ledger, question budget, fatigue valve, material/grounded/answerable gates.

None of the above authors were involved in this project. See [NOTICE.md](NOTICE.md).

## License

MIT
