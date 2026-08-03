# Prior-work evidence accounting and contribution boundaries

Use this protocol to decide, at the smallest evidenced unit, what a prior work claimed, operated,
demonstrated, evaluated, collided with, and earned contribution credit for. Apply the same rules to
the focal project.

## Default: exclude until positive evidence earns inclusion

Do not infer what a work may have done. Credit only what its complete first-party record explicitly
claims and what matched evidence shows actually operated or was evaluated. Ideas, future-work
proposals, interpretations, hypothetical scenarios, and unverified implementation claims receive
zero capability and contribution credit.

Maintain these canonical artifacts:

- `prior-work-evidence-accounting.csv` — one row per atomic operation, channel, condition, or
  evaluated finding;
- `idea-provenance-ledger.csv` — proposals and intellectual lineage that never enter capability or
  contribution accounting;
- `imported-bibliography-accountability.csv` — every supplied citation and its terminal
  source-resolution disposition;
- `late-found-work-postmortem.csv` — every material miss after a landscape was called bounded; and
- `novelty-regression-sentinels.yaml` — non-title retrieval tests for repaired search routes.

Use `prior-work-contribution-boundary.md` for human-readable synthesis and completion markers. The
CSV ledgers remain authoritative for row-level accounting.

## Complete six independent fields

For every material atom, record all six fields independently. No field inherits truth from another.

| Field | Positive-evidence question | What cannot establish it |
|---|---|---|
| `AUTHOR CLAIM` | Does the complete first-party source explicitly present this exact atom as a contribution, finding, realized capability, or benefit? | Prominence, likely intent, analyst interpretation, artifact behavior, or future work. |
| `DEMONSTRATED ARTIFACT OR STUDY` | Was the exact atom instantiated or studied with matched evidence at the claimed rung? | The claim itself, venue prestige, a nearby measure, an architecture diagram alone, or a package result used for one component. |
| `OPERATED CAPABILITY` | Did an artifact actually perform the named operation in a concrete execution, technical test, study condition, official demonstration, or inspectable implementation record? | Mock-ups, scenarios, intended affordances, plausible architecture, or unverified implementation prose. |
| `EVALUATED RESULT` | Did an evaluation directly measure the named result, with method, comparator, construct, scope, and uncertainty appropriate to the wording? | Operation alone, nonsignificance, proxy measures, or a bundled condition used for component causality. |
| `CAPABILITY COLLISION` | Does a positively demonstrated operated unit overlap the focal capability at that same unit and scope? | A claim, proposal, source silence, platform label, or broader category name. |
| `CONTRIBUTION CREDIT` | What exact claimed-and-demonstrated capability or knowledge may fairly be attributed to the work? | Collision alone, operation the authors did not claim, a port by itself, or analyst interpretation. |

Keep the familiar `Claimed`, `Demonstrated`, and `Capability` tags only as shorthand views over the
first three fields. The six-field ledger is canonical.

## Separate capability collision from contribution attribution

These are different decisions:

- A capability is prior art only when positive evidence shows that the exact operation actually
  ran. It may create `EXACT` or `PARTIAL` capability collision even when the authors never claimed
  it as a contribution.
- Contribution credit requires an explicit author claim and matched demonstration. For an
  artifact-capability atom, it also requires demonstrated operation. Give credit only to the
  matched intersection and bound it to the weakest supported people, activity, artifact version,
  data, comparator, construct, causal rung, and timeframe.

Record an operated but unclaimed atom as `DEMONSTRATED_UNCLAIMED`. It can retire or narrow a
capability-level firstness claim, force a fair comparator, or show inheritance. It receives
`CONTRIBUTION CREDIT=NONE` and must not be written as the authors' claimed contribution.

Record a claimed but undemonstrated atom as `CLAIMED_UNDEMONSTRATED`. It receives
`CAPABILITY COLLISION=NONE` and `CONTRIBUTION CREDIT=NONE` unless separate positive evidence
demonstrates the operation. A claim is not evidence for itself.

For non-artifact empirical, design, methodological, or theoretical knowledge, use
`OPERATED CAPABILITY=N/A`; matched evaluation or study evidence can still support contribution
credit.

## Compare the smallest named operation

Use the smallest named unit supported by positive evidence:

`command → parameter → input channel → reward channel → configuration → study condition →
evaluated finding`

Do not generalize from one unit to its enclosing category or whole system. Record the input or
signal, transformation or mapping, output meaning, recipient, timing, and explicit generalization
boundary.

Examples:

- `spoken "next" → advance-one-slide command` can establish only that exact command. It does not
  establish backward navigation, arbitrary slide selection, annotation, general presentation
  control, a complete voice interface, or every command.
- `task-performance score → badge` is a computed-state-to-reward channel. It is not
  user-action-to-command.
- A system that uses speech to advance one slide, a keyboard for navigation, and a task score for a
  badge has three channels. Audit three rows; do not apply one whole-system label.

These examples illustrate unit discipline. Project-specific terminology still requires an
operational definition and full-source evidence.

## Decompose mixed and hybrid systems

Create one accounting row for each independently operated channel:

- user action → command;
- conventional input → navigation or action;
- sensed or computed state → reward, adaptation, or feedback;
- condition or activity → gating or unlock;
- system state → feedback.

Classify a row as `ATOMIC_CHANNEL`, `PACKAGE_ONLY`, or `WHOLE_SYSTEM`. Use `WHOLE_SYSTEM` only when
the project's operational definition names a required channel set and positive evidence qualifies
every member. If even one required channel is conventional, unrelated, unresolved, or only
proposed, keep the classification atomic or mixed.

Encode `required_channel_set` and `qualified_channel_set` as `||`-separated `channel_id` values.
Every qualified ID must resolve to its own positively demonstrated, positively operated
`ATOMIC_CHANNEL` row; equality between two hand-entered lists is not evidence.

## Keep package evidence at package scope

A multi-component condition demonstrates the package. It does not identify which operator,
component, timing feature, or mechanism caused the result. Use `PACKAGE_CONDITION` and
`causal_attribution_scope=PACKAGE_ONLY` unless an orthogonal, factorial, dismantling, matched, or
otherwise defensible contrast identifies the component.

Likewise, nonsignificance does not establish equivalence, comparability, maintenance, or
non-inferiority. Use those terms only when an appropriate equivalence or non-inferiority design and
margin support them.

## Route ideas and provenance separately

Put these in `idea-provenance-ledger.csv`, not in capability accounting:

- ideas and concepts;
- future work and explicit proposals;
- hypothetical use scenarios;
- analyst interpretations;
- unverified or unattributed implementation assertions that are not explicit author claims of a
  realized atom.

For every row set:

`CAPABILITY COLLISION=NONE`

`CONTRIBUTION CREDIT=NONE`

Idea provenance can constrain “first idea,” “first proposed,” or conceptual-lineage language. It
cannot retire a demonstrated capability claim, establish feasibility or effectiveness, or show
that an operation existed. If later positive evidence shows operation, create a new evidence-
accounting row; do not silently upgrade the idea row.

An explicit author claim that a realized capability, result, or contribution exists without
matched evidence is not hidden only in this ledger. Create a `CLAIMED_UNDEMONSTRATED` evidence-
accounting row so the claim and exclusion are visible; optionally cross-reference it here as
`UNVERIFIED_IMPLEMENTATION_CLAIM`. Both records retain `CAPABILITY COLLISION=NONE` and
`CONTRIBUTION CREDIT=NONE` until separate positive evidence establishes more.

## Apply the port and adaptation credit gate

Normalize away hardware, sensor, operating system, app, game, and delivery-platform labels. A port
or reimplementation receives `CONTRIBUTION CREDIT=NONE` by default, even when it required
substantial engineering. It can still create a capability collision when the underlying operation
ran.

Credit survives only when complete-source evidence demonstrates at least one of:

1. a nontrivial adaptation that yields reusable constraint/solution knowledge;
2. a new class of human use, activity, population, or context that was actually instantiated and
   demonstrated; or
3. a directly validated empirical finding, including a measured change in access, cost, burden,
   performance, experience, or outcome.

Record the exact gate and evidence. A claimed adaptation, possible use class, or unevaluated port
does not pass.

## Treat source silence only as a search action

Source silence cannot establish that a system lacked a capability, that no prior work exists, or
that the work deserves contribution credit. Silence may create only:

- `SEARCH_PRIORITY` — inspect another version, supplement, artifact, video, repository, or cited
  description; or
- `REOPEN_QUERY` — reopen the search or author-access request for the exact unresolved unit.

Use `OPERATED CAPABILITY=UNRESOLVED`, not `NO`, until positive evidence settles the boundary.
Assign `NO` only when the inspected artifact architecture, execution, or mutually exclusive state
positively rules the operation out for the audited version.

## Repair imported and late-found work

Every supplied draft, bibliography, or reading-list item enters
`imported-bibliography-accountability.csv`. A materially relevant item must resolve to a terminal
`source-resolution.csv` row: `FULL_TEXT_ASSESSED`, a specific `SCREENED_OUT`, a verified
`SUPERSEDED`, or an actually surfaced `NEEDS_AUTHOR_SOURCE_ACCESS`.

When late-found work changes a boundary, complete a postmortem rather than merely adding the
paper:

1. identify the route and seed that should have found it;
2. screen sibling records and repair the query, graph, or database coverage;
3. rerun every affected claim, evidence rating, collision, credit decision, ranking, gap,
   comparator, and study requirement;
4. add a non-title/non-author regression sentinel; and
5. rerun the repaired search through a complete zero-yield promotion wave.

## Reader-facing use

Use capability collisions to bound capability novelty and fair-comparator claims. Use contribution
credit to describe what the prior authors contributed. Never substitute one for the other.

In prose:

- credit a claimed-and-demonstrated contribution at its narrowest scope;
- describe a `DEMONSTRATED_UNCLAIMED` operation as an observed capability of the audited artifact,
  not as the authors' claimed contribution;
- describe proposals as proposals;
- describe package-level results at package scope;
- describe ports only through the adaptation gate they actually pass; and
- state unresolved source boundaries without converting silence into absence.
