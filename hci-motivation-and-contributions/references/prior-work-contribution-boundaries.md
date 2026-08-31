# Prior-work evidence accounting and contribution boundaries

## Default: exclude until positive evidence earns inclusion

Do not infer what a work may have done. Credit only what its complete first-party record explicitly
claims and what matched evidence shows operated or was evaluated.

Canonical artifacts: `prior-work-evidence-accounting.csv`, one row per atomic operation, channel,
condition, or evaluated finding; `idea-provenance-ledger.csv`, proposals and lineage, never
capability or contribution accounting; `imported-bibliography-accountability.csv`, every supplied
citation and its terminal source-resolution disposition; `late-found-work-postmortem.csv`, every
material miss after a landscape was called bounded; `novelty-regression-sentinels.yaml`, non-title
retrieval tests for repaired routes. `prior-work-contribution-boundary.md` holds the
human-readable synthesis; the CSV ledgers stay authoritative.

## Complete six independent fields

Record all six independently for every material atom, at the smallest evidenced unit and for the
focal project. No field inherits truth from another.

| Field | Positive-evidence question |
|---|---|
| `AUTHOR CLAIM` | Does the first-party source explicitly present this atom as a contribution, finding, capability, or benefit — not by prominence, intent, or artifact behavior? |
| `DEMONSTRATED ARTIFACT OR STUDY` | Was this atom instantiated or studied with matched evidence at the claimed rung — not by the claim, venue prestige, a nearby measure, or a package result? |
| `OPERATED CAPABILITY` | Did an artifact perform the named operation in a concrete execution, technical test, study condition, official demonstration, or inspectable implementation? |
| `EVALUATED RESULT` | Did an evaluation directly measure the named result, with matched method, comparator, construct, scope, uncertainty? |
| `CAPABILITY COLLISION` | Does a demonstrated operated unit overlap the same complete human-activity predicate or an independently claimed sub-capability? |
| `CONTRIBUTION CREDIT` | What claimed-and-demonstrated capability or knowledge is fairly attributable? |

## Separate capability collision from contribution attribution

A capability is prior art only when positive evidence shows the operation ran: `EXACT` when the
complete human-activity predicate matches, `PARTIAL` when an independently consequential
sub-capability matches, even unclaimed. A component or generic qualifier alone is a precedent, not a
collision. Credit instead requires an explicit author claim plus matched demonstration, and
demonstrated operation for an artifact-capability atom; it covers only the matched intersection,
bounded to the weakest supported people, activity, artifact version, data, comparator, construct,
rung, and timeframe. An operated but unclaimed atom is `DEMONSTRATED_UNCLAIMED`: it narrows
a firstness claim, forces a fair comparator, or shows inheritance at its matched scope, but takes
`CONTRIBUTION CREDIT=NONE`. A claimed but undemonstrated atom is `CLAIMED_UNDEMONSTRATED`: both
fields `NONE` until positive evidence demonstrates the operation. In reader-facing prose never
substitute collision, precedent, and credit for one another; credit at the narrowest supported
scope, report a `DEMONSTRATED_UNCLAIMED` operation as an observed capability of the audited
artifact, never convert silence into absence.

### An idea without a demonstration or a study collides with nothing

A proposed idea, concept, design sketch, scenario, architecture, or intended affordance creates
**no capability collision and no contribution credit** at any scope: it cannot retire, narrow, or
pre-empt a focal capability, nor force a comparator, however closely it resembles the focal atom and
however early it was published. Idea priority is a Discussion-section courtesy.

Venue prompts the check, never the verdict in either direction: abstracts, posters, demos,
workshops, preprints, patents, and future-work sections often carry an idea, and a full paper at a
strong venue may too. Decide on content — a planned-system figure, a storyboard, a Wizard-of-Oz
stand-in, or prose asserting the system was built is not an operation; a walkthrough with no
measured construct or a pilot without method, N, or comparator is not a measured result. If nothing
was operated and nothing measured, the work is an idea: `NONE` in both columns, no diffing.
Otherwise audit only the demonstrated part, **at its own small scope**. For non-artifact knowledge
use `OPERATED CAPABILITY=N/A`; matched study evidence can still support credit.

## Compare the smallest named operation

Use the smallest named unit with positive evidence:

`command → parameter → input channel → reward channel → configuration → study condition →
evaluated finding`

Never generalize from one unit to its enclosing category or whole system. Record input or signal,
transformation or mapping, output meaning, recipient, timing, and generalization boundary.
`spoken "next" → advance-one-slide command` establishes only that command: it does not
establish backward navigation, arbitrary slide selection, annotation, general presentation
control, or a voice interface. `task-performance score → badge` is a computed-state-to-reward channel,
not user-action-to-command. A system using speech to advance one slide, a keyboard for navigation,
and a task score for a badge has three channels: audit three rows, never one whole-system label.
Project-specific terminology needs an operational definition and full-source evidence.

## Do not confuse an atomic operation with a complete capability

Atomic evidence never suffices to collide with a complete human capability. Write both
capabilities as a human-activity predicate:

`people/roles → meaningful action or information relationship → focal activity → immediate purpose
→ essential interdependence, semantics, timing, and control`

A loose subset of adjectives such as `live` or `multi-user` is not an independent sub-capability. Avoid the **component-subtraction fallacy**: familiar components do not erase a
novel complete capability; conversely a new domain noun does not rescue novelty when the same prior
capability ports unchanged.

## What counts as a collision: decision procedure

A collision means prior work already delivered the same capability to the same people for the same
purpose under the same essential constraints, not mere resemblance. Apply the
idea gate first: if nothing was operated and nothing measured, the answer is `NO_COLLISION`.
Otherwise run all three steps in order and record each answer.

**Step 1. Diff both predicates dimension by dimension** — people, activity, display and hardware,
emitted signal, what consumes it, what runs concurrently, bounding constraint — each taken from what
that system actually operates. A shared *mechanism* usually survives this diff and is not a
collision.

**Step 2. For every differing dimension, decide whether it is load-bearing**, stating each test's
result. *Removal test*: delete the dimension — if what people can meaningfully do changes, it is
load-bearing. *Drop-in-port test*: if the unchanged prior mechanism would need redesign rather than
reconfiguration to deliver the focal semantics, timing, and purpose, it is load-bearing.

**Step 3. Label the result. Only the first two labels are collisions.**

- `FULL_CAPABILITY_COLLISION` — every core dimension matches, no surviving difference load-bearing.
  Record `EXACT`.
- `INDEPENDENT_SUBCAPABILITY_COLLISION` — a sub-capability the focal project claims separately and
  consequentially matches in full; a collision at that scope only. Record `PARTIAL`.
- `COMPONENT_OR_MECHANISM_PRECEDENT` — a device, modality, transfer function, control law, routing
  pattern, timing property, or topology matches, but a load-bearing dimension differs. **Not a
  collision.** Record `CAPABILITY COLLISION=NONE` and credit the inherited component.
- `NO_COLLISION` — nothing positively operated overlaps at a claimed level. Record `NONE`.

### The mechanism-precedent trap

Commonest failure: finding a shared mechanism and reporting it as though the focal capability were
retired. A mechanism precedent **never** retires a capability, technique, or contribution; it bounds
what may be claimed as *new mechanism* and obliges citation and a fair comparator. Write "X inherits
Y's control law; the difference is Z" and say whether Z is load-bearing, never "X is Y" or "this
retires X". Never rank collisions on one severity scale mixing in precedents — keep collision label
and inheritance note in separate fields. Diff the prior authors' own wording, never two paraphrases
you wrote.

## Decompose mixed and hybrid systems

One accounting row per independently operated channel: user action → command; conventional input →
navigation; sensed or computed state → reward, adaptation, or feedback; activity → gating. Classify each row `ATOMIC_CHANNEL`, `PACKAGE_ONLY`, or `WHOLE_SYSTEM`, using `WHOLE_SYSTEM` only
when the project's operational definition names a required channel set and positive evidence
qualifies every member; if even one required channel is conventional, unrelated, unresolved, or
proposed, the classification stays atomic or mixed. Encode `required_channel_set` and
`qualified_channel_set` as `||`-separated `channel_id` values, and resolve every qualified ID to its
own operated `ATOMIC_CHANNEL` row; equality of two hand-entered lists is not evidence.

## Keep package evidence at package scope

A multi-component condition demonstrates the package, not which operator, component, timing, or
mechanism caused the result: use `PACKAGE_CONDITION` and
`causal_attribution_scope=PACKAGE_ONLY` unless an orthogonal, factorial, or dismantling contrast
identifies the component.

## Route ideas and provenance separately

Ideas, future work, use scenarios, interpretations, and unverified implementation assertions that
are not explicit author claims of a realized atom belong in `idea-provenance-ledger.csv`, not
capability accounting, each with `CAPABILITY COLLISION=NONE` and `CONTRIBUTION CREDIT=NONE`.

Idea provenance can constrain "first idea," "first proposed," or lineage language, but cannot
retire a demonstrated capability claim, establish feasibility or effectiveness, or show an
operation ran. If later positive evidence shows operation, open a new evidence-accounting row
rather than upgrading the idea row.

An explicit author claim that a realized capability, result, or contribution exists without matched
evidence is not hidden only in this ledger. Create a `CLAIMED_UNDEMONSTRATED` evidence-accounting
row so claim and exclusion are visible, optionally cross-referenced here as
`UNVERIFIED_IMPLEMENTATION_CLAIM`; both records keep `CAPABILITY COLLISION=NONE` and
`CONTRIBUTION CREDIT=NONE` until positive evidence establishes more.

## Apply the port and adaptation credit gate

Normalize away hardware, sensor, operating system, app, and delivery-platform labels. A port
or reimplementation takes `CONTRIBUTION CREDIT=NONE` by default, even when it required substantial
engineering, though it still collides when the underlying operation ran at the same full-predicate
or independently claimed sub-capability scope; otherwise it is a component precedent. Credit
survives only when complete-source evidence demonstrates a nontrivial adaptation yielding reusable
constraint/solution knowledge, a new class of human use actually instantiated, or a validated
empirical finding such as measured change in access, cost, burden, or performance.
Record the gate and its evidence; a claimed adaptation, possible use class, or unevaluated port
fails it.

## Treat source silence only as a search action

Source silence cannot establish that a system lacked a capability, that no prior work exists, or
that the work deserves credit. Silence may create only `SEARCH_PRIORITY` — inspect another version,
supplement, artifact, video, repository, or cited description — or `REOPEN_QUERY` for that
unresolved unit. Use `OPERATED CAPABILITY=UNRESOLVED`, not `NO`, until positive evidence settles the
boundary; assign `NO` only when inspected artifact architecture, execution, or mutually exclusive
state positively rules the operation out for the audited version.

## Repair imported and late-found work

Every supplied draft, bibliography, or reading-list entry enters
`imported-bibliography-accountability.csv`; a materially relevant one must reach a terminal
`source-resolution.csv` row: `FULL_TEXT_ASSESSED`, a specific `SCREENED_OUT`, a verified
`SUPERSEDED`, or a surfaced `NEEDS_AUTHOR_SOURCE_ACCESS`.

When late-found work changes a boundary, run a postmortem, not merely an added citation: identify
the route and seed that should have found it; screen siblings and repair query, graph, or database
coverage; rerun every affected claim, rating, collision, credit decision, ranking, gap, comparator,
and study requirement; add a non-title/non-author sentinel; rerun the repaired search through a
complete zero-yield promotion wave.
