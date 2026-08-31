# Source-grounded related-work quadrant variations

Two-axis charts show the related-work landscape and the current work's distinguishing combination.
They are communication artifacts, not measurements, novelty proofs, or matrix substitutes.

## Two levels of rigor

**Communication mode is the default:** approximate ordinal placements from a reading of each saved
full work, with a rationale and `placement_status=interpretive`. **Strict audit mode** adds
`x_locator`, `y_locator`, and `placement_status=audited` for a submission-critical or contested
placement. In both, every plotted work must have a saved full copy that was opened and checked — not
a title, abstract, snippet, or summary.

## Output contract

Produce:

- `related-work-quadrant-variations.md`, comparing candidate views and recommending one;
- `quadrants/<variant-slug>.csv` and `quadrants/<variant-slug>.svg` for three to five axis pairs;
- `related-work-quadrant.csv` and `related-work-quadrant.svg`, copies of the selected view; and
- a **Chart corpus and rationale** section in `related-work-matrix.md` recording the comparison unit,
  included works, full-copy status, and the selected view.

Hold the same core comparison corpus across variants — same problem approached differently,
different problem approached similarly, same problem approached similarly — so no chart turns
persuasive by dropping an inconvenient neighbor. Chart proximity, a shared axis, or a nearby point
never upgrades problem proximity, turns component overlap into a full-capability collision, or
reorders the ranking. Split differing configurations from one paper into separate points; a review or
theory paper is `contextual—not point-comparable`.

## Generate an axis-pair portfolio

Offer three to five pairs before the author selects: a contribution pair turning the project's two
most important proposed capabilities into neutral operational axes; a topology or use-context pair
(recipient structure, task interdependence, agency, deployment context); a workflow-stage pair
covering before, during, and after the focal activity; and one from modality, adaptation input, or
locus of agency.

For a project framed as **real-time × individualized**, decide whether the claimed distinction is
content distribution or automatic adaptation, then use separate dimensions:

- **Guidance timing:** `0` before/after action, `50` concurrent but not task-event-coupled, `100`
  event-coupled with timing established;
- **Content differentiation:** `0` same shared content, `50` different by subgroup or role, `100`
  different by intended individual recipient;
- **adaptation provenance**, when consequential: fixed, human-selected or role/profile-configured,
  or from system-inferred recipient state; and
- **delivery concurrency**, when simultaneous differentiation is contribution-relevant: one stream at
  a time, partially overlapping, or distinct recipient-targeted streams at once. Do not smuggle this
  qualifier into the adaptation axis.

Do not conflate recipient differentiation with automatic personalization; use the vocabulary in
[related-work-positioning.md](related-work-positioning.md). A timing-unmeasured Wizard-of-Oz system
is not at “measured real-time,” nor role-configured cues at “automatic personalization.”

A hardware or interface pair is the contribution view only when the medium is the contribution:
“physical versus virtual” needs a difference in the human activity — co-presence,
interdependence, timing, agency, risk —
not merely the rendering environment. Otherwise reject only meaningless pairs: two names for one
construct, evaluative scales, venue prestige.

## Place works for communication

Use whole-number positions from `0` to `100`, normally the anchors `0`, `25`, `50`, `75`, `100`.
These are approximate ordinal judgments; small distances and Euclidean proximity mean nothing.

Per point: `source`, a local file path or NotebookLM source UUID for the saved full copy, never a DOI
or URL alone; `x_evidence` and `y_evidence`, a short full-text-grounded reason per axis;
`uncertainty`, any ambiguity or mixed configuration; a label of at most 36 characters; and
`verification_status=verified_full_text`, set for related research only after checking the whole
work, or `verified_project_artifacts` for the current work.

Place the current work from its implemented configuration under the same axis definitions, recording
unmeasured timing, manual assignment, or unresolved behavior in `uncertainty`, not as a study
result. Source silence is unresolved by default: place conservatively, split the configuration, or
omit the point with a reason, never placing an absent capability from silence. A plotted operation
must be the smallest named unit established by positive evidence in
`prior-work-evidence-accounting.csv`.

Keep capability collision separate from contribution attribution and from component inheritance, per
[prior-work-contribution-boundaries.md](prior-work-contribution-boundaries.md). A
`DEMONSTRATED_UNCLAIMED` operated capability earns a collision coordinate only at the matched
complete human-activity predicate or independently claimed sub-capability scope; label it
`CONTRIBUTION CREDIT=NONE`. A component or mechanism precedent supports its literal coordinate but
never weakens the complete capability. A `CLAIMED_UNDEMONSTRATED` atom stays off the chart; ideas and
hypotheticals survive as idea provenance for Discussion, with
`CAPABILITY COLLISION=NONE` and `CONTRIBUTION CREDIT=NONE`.

For mixed systems plot the smallest positively operated channel, never a whole-system label unless
every channel qualifies. A demonstrated
`spoken "next" → advance-one-slide command` channel does not establish backward navigation or a
complete voice interface, and a
`task-performance score → badge` channel is computed-state-to-reward, not user-action-to-command.
A port alone receives no contribution credit, although its operated capability can still collide.

## Render and present the variations

Copy `assets/related-work-quadrant.csv` per view; the renderer rejects unverified full-text
declarations and placeholders:

```bash
python3 scripts/render_related_work_quadrant.py \
  path/to/variant.csv path/to/variant.svg
```

Optional strict audit:

```bash
python3 scripts/render_related_work_quadrant.py --strict \
  path/to/variant.csv path/to/variant.svg
```

In `related-work-quadrant-variations.md`, compare each view on what it makes visible, what it hides,
and its disposition: select, supporting, discard. Recommend the view communicating the most
important distinction already present in the contribution and related-work prose, show tradeoffs,
and pause for the author's choice.

## Lightweight communication audit

Before presenting, confirm the closest predecessor is present, that
chart proximity has not been substituted for the problem-first ranking, and that content
differentiation, delivery concurrency, and adaptation provenance stay separate rather than collapsing
into one “individualized” axis.
