# Source-grounded related-work quadrant variations

Use two-axis charts to help authors and readers see the related-work landscape and the current
work's distinguishing combination. They are communication artifacts, not measurements, exhaustive
novelty proofs, or substitutes for the related-work matrix.

## Two levels of rigor

**Communication mode is the default.** Approximate ordinal placements are acceptable when they are
based on a reading of each saved full work and accompanied by a concise rationale. The purpose is
to explore and explain useful views of the landscape.

**Strict audit mode is optional.** Use it before relying heavily on a chart in a submission or when
an exact placement is contested. It additionally requires exact x- and y-specific source locators
and an `audited` placement status.

Both modes retain one non-negotiable rule: every plotted research work must have a saved full copy
that was opened and checked. A title, abstract, search snippet, another paper's summary, or a
plausible memory is not enough.

## Output contract

Produce:

- `related-work-quadrant-variations.md`, comparing the candidate views and recommending one for
  author selection;
- `quadrants/<variant-slug>.csv` and `quadrants/<variant-slug>.svg` for three to five useful axis
  pairs;
- `related-work-quadrant.csv` and `related-work-quadrant.svg` as copies of the selected view; and
- a short **Chart corpus and rationale** section in `related-work-matrix.md` recording the
  comparison unit, included works, full-copy status, and the selected view.

Use the same core comparison corpus across variants so a chart does not become persuasive merely
by dropping an inconvenient neighbor. Include works from:

1. the same problem approached differently;
2. a different problem approached similarly; and
3. the same problem approached similarly, when such close predecessors exist.

This deliberately broad chart corpus is not the closest-work ranking. Carry each work's
problem-proximity band and portfolio assignment into the chart rationale, and visually or textually
distinguish the primary same/similar-problem portfolio from different-problem
component/mechanism precedents and genuine capability collisions. Euclidean chart proximity, one
shared axis, or a visually nearby point cannot upgrade problem proximity, turn component overlap
into a full-capability collision, or reorder the primary ranking.

Plot comparable implementations or evaluated configurations. A heterogeneous review, theory
paper, or contextual authority can shape the corpus and motivation without becoming one point;
record it as `contextual—not point-comparable`. Split materially different configurations from one
paper into separate labeled points when that distinction helps readers.

## Generate an axis-pair portfolio

Generate three to five candidate pairs before asking the author to select one. Include:

1. **The contribution pair.** Translate the project's two most important proposed capabilities
   into neutral, operational axes.
2. **A topology or use-context pair.** Test whether recipient structure, task interdependence,
   agency, or deployment context explains the gap better.
3. **A workflow-stage or activity-coverage pair.** When the work extends an existing practice,
   compare the stages supported—before, during, or after the focal activity—and the activity
   conditions that remain present.
4. **A meaningful alternative.** Use modality, adaptation input, shared awareness, evaluation
   scope, or another recurring distinction exposed by the matrix.

For a project initially framed as **real-time × individualized**, first determine whether the
claimed distinction is content distribution or automatic adaptation. Prefer separate operational
dimensions such as:

- **Guidance timing:** `0 = before/after action`, `50 = concurrent but not task-event-coupled`,
  `100 = event-coupled during unfolding action with timing established`; and
- **Content differentiation:** `0 = the same shared content for intended recipients`, `50 =
  different content by subgroup or role`, `100 = different content by intended individual
  recipient`.

When adaptation is itself consequential, use a separate **adaptation provenance** dimension:
`0 = fixed content`, `50 = human-selected or role/profile-configured content`, `100 = content
selected or updated from system-inferred recipient state`.

When simultaneous differentiation is contribution-relevant, use a separate **delivery
concurrency** dimension: `0 = one content stream at a time`, `50 = partially overlapping or
multi-channel delivery`, `100 = distinct recipient-targeted streams deliverable concurrently`.
Do not smuggle this qualifier into the adaptation axis.

Do not conflate recipient differentiation with automatic personalization. Use
“recipient-differentiated” rather than “individualized” unless the project defines the latter
precisely. Reserve “system-personalized” for a stored or inferred individual model and “adaptive”
for support that changes with inferred state, behavior, or performance.
Do not place a timing-unmeasured Wizard-of-Oz system at “measured real-time,” or manually
role-configured cues at “automatic personalization.” A chart can still show that a system occupies
a distinctive intermediate or upper-region combination.

Other useful dimensions include:

- workflow stage or temporal coverage;
- relation to current practice: replaces, complements, extends, or bridges;
- recipient or collaboration topology;
- content differentiation: shared versus recipient-differentiated;
- delivery concurrency: serialized versus concurrent distinct streams;
- channel visibility and resulting shared awareness;
- task coupling and interdependence;
- locus of agency or control;
- representation or feedback modality;
- deployment context;
- adaptation input; and
- evaluation scope.

Do not use headset versus earbud, tablet versus cue matrix, annotation versus speech, or another
hardware/interface pair as the contribution view unless the actual contribution is the medium
itself. “Physical versus virtual” is meaningful only when operationalized as a difference in the
human activity, such as co-presence, interdependence, real objects, movement, timing, agency, risk,
or consequences—not merely the rendering environment.

Reject only pairs that are meaningless or misleading: two names for the same construct, “bad to
good,” “traditional to novel,” venue prestige, research quality, or axes that cannot be applied to
most of the comparison corpus. Do not require the selected chart to carry the entire novelty
argument.

## Place works for communication

Use whole-number positions from `0` to `100`, normally the anchors `0`, `25`, `50`, `75`, and
`100`. These are approximate ordinal judgments. Small distances and Euclidean proximity have no
meaning.

For every point:

- identify the saved full copy or NotebookLM source ID in `source`;
- give a short full-text-grounded reason for each axis in `x_evidence` and `y_evidence`;
- state material ambiguity or mixed configurations in `uncertainty`;
- use a short chart label of at most 36 characters;
- set related research to `verification_status=verified_full_text` only after checking the complete
  work; the current work may use `verified_project_artifacts`; and
- set `placement_status=interpretive` for ordinary communication charts.

Exact `x_locator` and `y_locator` values are optional in communication mode. Add them and use
`placement_status=audited` when running strict mode.

The renderer accepts an existing local file path (absolute or relative to the CSV) or a NotebookLM
source UUID. A DOI or web URL alone does not pass the saved-full-copy gate.

Apply the same axis definitions to the current work, but do not pretend that the chart is a study
result. Place the current work from its implemented configuration and available evidence; describe
unmeasured timing, manual assignment, Wizard-of-Oz control, or unresolved behavior in
`uncertainty`. A chart may communicate an approximate position while the prose states those
boundaries explicitly.

Source silence is unresolved by default. Use a conservative placement, a visibly separate
configuration, or omit the point with a recorded reason when the full work genuinely does not
support an estimate. A plotted operation must be the smallest named unit established by positive
evidence in `prior-work-evidence-accounting.csv`.

Keep capability collision separate from contribution attribution and from component inheritance.
A `DEMONSTRATED_UNCLAIMED` operated capability may support a separate collision coordinate only at
the matched complete human-activity predicate or independently claimed sub-capability scope. A
component or mechanism precedent may support its literal axis coordinate but must not be described
as weakening the complete capability. Label unclaimed operations and give them
`CONTRIBUTION CREDIT=NONE`. A
`CLAIMED_UNDEMONSTRATED` atom supports neither a capability coordinate nor contribution credit.
Never place an absent capability from source silence.

Keep ideas, future-work proposals, hypothetical scenarios, and interpretations out of capability
and novelty placement. Preserve them only as idea
provenance for Discussion, with `CAPABILITY COLLISION=NONE` and
`CONTRIBUTION CREDIT=NONE`. An explicit but unverified author claim of realized capability stays
off the chart and remains visible as `CLAIMED_UNDEMONSTRATED`; it may also be cross-referenced in
idea provenance.

For mixed systems, plot the smallest positively operated channel or separate channels; do not plot
a whole-system label unless every required channel qualifies. A demonstrated
`spoken "next" → advance-one-slide command` channel does not establish backward navigation,
arbitrary slide selection, annotation, general presentation control, or a complete voice
interface. A `task-performance score → badge` channel is computed-state-to-reward, not
user-action-to-command. Normalize away platform and hardware labels: a port alone receives no
contribution credit, although its underlying operated capability can still collide.

## Render and present the variations

Copy `assets/related-work-quadrant.csv` for each view and render communication charts with:

```bash
python3 scripts/render_related_work_quadrant.py \
  path/to/variant.csv path/to/variant.svg
```

Optional strict audit:

```bash
python3 scripts/render_related_work_quadrant.py --strict \
  path/to/variant.csv path/to/variant.svg
```

The renderer:

- keeps point coordinates fixed while moving labels;
- marks exact overlaps with a count badge rather than secretly jittering points;
- highlights the current work separately from related-work categories;
- rejects unverified full-text declarations and unresolved template placeholders; and
- states in the caption that placements are approximate interpretive judgments, not quality or
  novelty measurements.

In `related-work-quadrant-variations.md`, place the charts side by side when practical and compare:

| View | What it makes visible | What it hides or compresses | Closest neighbor | Evidence caveat | Use |
|---|---|---|---|---|---|
| Contribution pair | ... | ... | ... | ... | select / supporting / discard |

Recommend the view that most clearly communicates a substantively important distinction already
present in the contribution and related-work prose. This recommendation is not the selection:
present the whole portfolio, explain the tradeoffs, and pause for the author. Keep discarded
variants when they reveal a different useful interpretation.

## Lightweight communication audit

Before presenting a chart, check:

- all plotted research works have saved, checked full copies;
- the closest predecessor is not omitted;
- primary same/similar-problem comparators and different-problem collisions are distinguishable;
- full-capability, independent-sub-capability, and component/mechanism overlap are not conflated;
- chart proximity has not been substituted for the problem-first related-work ranking;
- the axes use neutral capability language;
- each point has a concise placement rationale;
- current-work aspirations are not shown as established capabilities;
- content differentiation, delivery concurrency, and adaptation provenance are not collapsed into
  one “individualized” axis;
- shared-awareness consequences are not presented as outcomes without evidence;
- overlapping points remain visible;
- the same core corpus is recognizable across variants; and
- the prose explains both what the selected view reveals and what it compresses.

Run the strict audit only when its additional precision is useful. Do not block an exploratory
landscape chart merely because exact page locators or formal sensitivity analyses are absent.
