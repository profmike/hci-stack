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
| `CAPABILITY COLLISION` | Does a positively demonstrated operated unit overlap the same complete human-activity predicate or an independently claimed consequential sub-capability? | A claim, proposal, source silence, platform label, broader category name, or loose subset of generic qualifiers. |
| `CONTRIBUTION CREDIT` | What exact claimed-and-demonstrated capability or knowledge may fairly be attributed to the work? | Collision alone, operation the authors did not claim, a port by itself, or analyst interpretation. |

Keep the familiar `Claimed`, `Demonstrated`, and `Capability` tags only as shorthand views over the
first three fields. The six-field ledger is canonical.

## Separate capability collision from contribution attribution

These are different decisions:

- A capability is prior art only when positive evidence shows that the exact operation actually
  ran. It creates `EXACT` full-capability collision only when the complete human-activity predicate
  matches, or `PARTIAL` collision when an independently consequential sub-capability matches, even
  when the authors never claimed it as a contribution. A component or generic qualifier alone is a
  precedent, not a collision with the complete capability.
- Contribution credit requires an explicit author claim and matched demonstration. For an
  artifact-capability atom, it also requires demonstrated operation. Give credit only to the
  matched intersection and bound it to the weakest supported people, activity, artifact version,
  data, comparator, construct, causal rung, and timeframe.

Record an operated but unclaimed atom as `DEMONSTRATED_UNCLAIMED`. It can retire or narrow a
firstness claim only at its matched full-predicate or independently claimed sub-capability scope,
force a fair comparator, or show component inheritance. It receives `CONTRIBUTION CREDIT=NONE` and
must not be written as the authors' claimed contribution.

Record a claimed but undemonstrated atom as `CLAIMED_UNDEMONSTRATED`. It receives
`CAPABILITY COLLISION=NONE` and `CONTRIBUTION CREDIT=NONE` unless separate positive evidence
demonstrates the operation. A claim is not evidence for itself.

### An idea without a demonstration or a study collides with nothing

A proposed idea, concept, design sketch, scenario, architecture, or intended affordance creates
**no capability collision and no contribution credit**, at any scope. It cannot retire, narrow, or
pre-empt a focal capability, and it cannot force a comparator. Record
`CAPABILITY COLLISION=NONE`, `CONTRIBUTION CREDIT=NONE`, and `CLAIMED_UNDEMONSTRATED`. This holds no
matter how closely the idea resembles the focal atom, how early it was published, or how well known
the authors are. Priority of an idea is a Discussion-section courtesy, routed to
`idea-provenance-ledger.csv`; it is not prior art for a capability.

Venue is the prompt to check this, never the verdict. Formats that frequently carry an idea with no
matched demonstration or study include:

- posters and poster abstracts;
- CHI Extended Abstracts, Late-Breaking Work, and Work-in-Progress;
- demo and video abstracts;
- workshop position papers;
- vision, provocation, and *alt.chi* papers;
- preprints, tech reports, and patents describing an intended system;
- future-work sections and figures in an otherwise-demonstrating paper.

Run the check on the content, not the label, and record which way it went:

1. **Did an artifact actually run the named operation?** A concrete execution, technical test, study
   condition, official demonstration, or inspectable implementation record counts. A figure of a
   planned system, a storyboard, a Wizard-of-Oz stand-in for the operation under audit, or prose
   asserting that it was built does not.
2. **Did an evaluation directly measure the named result?** A formative walkthrough with no measured
   construct, an author's impression, or a pilot reported without method, N, or comparator does not.

If both answers are no, the work is an idea. Stop there: it takes `NONE` in both the collision and
the credit column, and no further diffing is needed.

If either answer is yes, audit the demonstrated part **at its own small scope** and only that part.
A four-page extended abstract that ran a working prototype and reports a five-person formative test
has positively operated a capability, and the short format never discounts what it actually ran. It
also never inflates it: the collision scope is the operation that ran, and the evaluated-result
scope is the construct that was measured, with its N and its comparator.

Two errors this rule prevents, in both directions:

- treating an early concept paper as though it had already delivered the capability, which retires a
  real contribution against nothing;
- dismissing a short paper that did build and test something, which hides a genuine collision behind
  a page count.

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

## Do not confuse an atomic operation with a complete capability

Atomic evidence is necessary for collision analysis but is not sufficient to collide with a
complete human capability. Write both the focal and prior capability as a human-activity predicate:

`people/roles → meaningful action or information relationship → focal activity → immediate purpose
→ essential interdependence, semantics, timing, and control`

Then label the overlap:

- `FULL_CAPABILITY_COLLISION`: every core predicate dimension matches; record `EXACT`.
- `INDEPENDENT_SUBCAPABILITY_COLLISION`: a named, separately consequential sub-capability claimed by
  the focal project matches; record `PARTIAL`.
- `COMPONENT_OR_MECHANISM_PRECEDENT`: only a device, modality, channel, routing pattern, timing
  property, topology, or low-level mechanism matches; record `NONE` for the complete capability and
  credit the inherited component.
- `NO_COLLISION`: no positively operated capability overlaps at a claimed level; record `NONE`.

Run a removal test—would deleting the dimension change what people can meaningfully do?—and a
drop-in-port test—could the prior mechanism unchanged support the focal semantics,
interdependence, and purpose? A loose subset of adjectives such as `live`, `multi-user`, `physical`,
`different outputs`, or `audio` is not an independent sub-capability. Do not perform the
**component-subtraction fallacy** by using separately familiar components to erase a novel complete
capability. Conversely, a new domain noun does not rescue novelty when the same prior capability
ports unchanged.

## What counts as a collision: decision procedure

A collision is not "these two things resemble each other." It is a finding that prior work already
delivered the same capability to the same people for the same purpose under the same essential
constraints. Run these three steps in order, and record the answer to each.

**Step 1. Write both predicates in full, then diff them dimension by dimension.** Write the prior
work's predicate from what its authors actually operated, and the focal predicate from what the
focal system actually operates. Diff every dimension: who the people are, what they do, on what
display and hardware, what signal the system emits, what consumes that signal, what else is running
at the same time, and what constraint bounds the whole arrangement. A shared *mechanism* will
usually survive this diff. That is expected and is not yet a collision.

**Step 2. For every dimension that differs, decide whether the difference is load-bearing.** Apply
both tests, and state the result of each:

- *Removal test*: delete the dimension. Does what people can meaningfully do change? If yes, the
  dimension is load-bearing.
- *Drop-in-port test*: could the prior mechanism, unchanged, deliver the focal semantics, timing,
  interdependence, and purpose? If it would need redesign rather than reconfiguration, the
  difference is load-bearing.

**Step 3. Label the result. Only the first two labels are collisions.**

- `FULL_CAPABILITY_COLLISION` — every core predicate dimension matches, and no surviving difference
  is load-bearing. This is a collision. Record `EXACT`.
- `INDEPENDENT_SUBCAPABILITY_COLLISION` — a sub-capability that the focal project claims separately
  and consequentially matches in full. This is a collision at that sub-capability's scope only, and
  never at the scope of the whole system. Record `PARTIAL`.
- `COMPONENT_OR_MECHANISM_PRECEDENT` — a device, modality, transfer function, control law, routing
  pattern, timing property, or topology matches, but at least one load-bearing dimension differs.
  **This is not a collision.** Record `CAPABILITY COLLISION=NONE` and credit the inherited component.
- `NO_COLLISION` — nothing positively operated overlaps at a claimed level. Record `NONE`.

Before Step 1, apply the idea gate above. If nothing was operated and nothing was measured, the
answer is `NO_COLLISION` and the three steps do not run.

### The mechanism-precedent trap

The most common failure in this workflow is finding a shared mechanism and reporting it as though
the focal capability were retired. Guard against it explicitly:

- A mechanism precedent **never** retires a capability, a technique, or a contribution. It bounds
  what may be claimed as *new mechanism*, and it obliges citation and a fair comparator. Nothing more.
- Do not write "X is Y", "X already does this", or "this retires X" on the strength of a mechanism
  precedent. Write "X inherits Y's control law; the difference is Z", and then say whether Z is
  load-bearing.
- Do not report collisions on one ordered severity scale that mixes precedents with collisions. A
  scale that runs `FULL > SUB-CAPABILITY > COMPONENT-PRECEDENT > NONE` invites a reader to treat a
  precedent as a weak collision. It is not a weak collision; it is a `NONE` with an inherited
  component. Report the collision label and the component-inheritance note as two separate fields.
- Restating the prior work in the focal project's own vocabulary makes a match look tighter than it
  is. Quote the prior authors' own description of what they operated, then diff against the focal
  description. Never diff two paraphrases you wrote yourself.

### Worked example: a shared control law is usually a precedent, not a collision

Prior work: in a surrounding projected display, the horizontal vector from the room centre to the
user's tracked head position drives travel; a neutral zone suppresses small displacements; speed
rises linearly with distance from that zone and saturates. Inside the neutral zone the display's
viewpoint stays coupled one-to-one to the head.

Focal work: the player's ground position, sensed by webcams, is converted into an analog-stick
deflection that is injected into an unmodified commercial console game shown on a fixed television,
while a separate head-orientation channel drives the in-game camera through a bounded gain curve.

The control law matches: displacement from a calibrated centre, dead zone, proportional gain,
saturation. Run step 2 on what differs:

- The emitted signal is a *stick deflection consumed by a game whose own transfer function,
  camera behaviour, and animation state sit downstream*, not a velocity applied directly to a
  viewpoint. Removal test: yes, load-bearing — the designer no longer controls the final motion.
- The display is fixed and does not surround the player, so the view channel cannot stay head-coupled
  and must instead be bounded by what the player can still see. Removal test: yes, load-bearing —
  it changes what the person can do with their head.
- A second body channel runs concurrently. Removal test: yes, load-bearing.
- Drop-in-port test: the prior mechanism cannot be reconfigured into this arrangement; it assumes a
  surrounding display and a tracked head as the position source.

Label: `COMPONENT_OR_MECHANISM_PRECEDENT`, therefore `CAPABILITY COLLISION=NONE` for the focal
capability, with the control law recorded as inherited and requiring citation. The correct sentence
is "the focal mapping inherits this control law and must cite it and compare against it", not "the
focal mapping is that technique."

Note what this does and does not settle. It does not by itself make the focal mapping a
contribution: inherited-mechanism plus load-bearing differences earns credit only through a
demonstrated nontrivial adaptation, a demonstrated new use class, or a directly validated empirical
finding. Collision and credit remain separate decisions.

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
ran at the same full-predicate or independently claimed sub-capability scope; otherwise it is a
component precedent.

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

Use full-predicate and independent-sub-capability collisions to bound capability novelty and fair-
comparator claims. Use component/mechanism precedents to show inheritance without implying that the
complete capability is old. Use contribution credit to describe what the prior authors contributed.
Never substitute one for another.

In prose:

- credit a claimed-and-demonstrated contribution at its narrowest scope;
- describe a `DEMONSTRATED_UNCLAIMED` operation as an observed capability of the audited artifact,
  not as the authors' claimed contribution;
- describe proposals as proposals;
- describe package-level results at package scope;
- describe ports only through the adaptation gate they actually pass; and
- state unresolved source boundaries without converting silence into absence.

## The idea gate

An idea with no demonstration and no study collides with nothing. A proposed concept, design
sketch, scenario, or intended affordance takes `CAPABILITY COLLISION=NONE` and
`CONTRIBUTION CREDIT=NONE` at every scope, however closely it resembles the focal atom. It cannot
retire or narrow a focal capability and cannot force a comparator.

Posters, CHI Extended Abstracts, Late-Breaking Work, Work-in-Progress, demo and video abstracts,
workshop position papers, vision and provocation papers, preprints, tech reports, and patents are
the formats where this arises most often. Treat the venue as the prompt to check and never as the
verdict, in either direction. A short paper that built something and measured something is audited
on what it ran and measured, exactly like a full paper, and receives no page-count discount. A full
paper at a strong venue that only proposed something is still an idea.

Ask two questions and nothing else:

1. Did an artifact actually run the named operation?
2. Did an evaluation directly measure the named result?

If both answers are no, stop and record `NONE` in both columns. If either is yes, audit the
demonstrated part at its own small scope, and credit nothing beyond what it ran and measured.
