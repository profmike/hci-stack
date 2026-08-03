# Claim-focused research communication

Use this protocol after evidence assessment when translating the internal research record into
author discussion, research-report narrative, outline language, downstream writing guidance, or
manuscript-facing claims.

## Treat reusable examples as illustrations, not project state

Examples in this reusable skill illustrate the method. They are not project evidence, author
decisions, active project claims, or a durable project record.

When an author adopts or adapts an example, record the project-specific decision in the target
project repository before relying on it. Preserve the selected wording or policy, author rationale,
evidence boundary, reader-facing qualifier disposition, propagation targets, and reopen trigger.
That project-owned record remains authoritative if a later skill revision changes or removes the
example. If the target project repository is unknown, keep the decision session-only until the
repository is supplied; never use the skill repository as substitute project storage.

## Keep the audit complete and the prose relevant

Maintain two linked layers:

1. The **internal evidence record** preserves uncertainty, limitations, contrary findings,
   transfer boundaries, non-claims, source-strength judgments, and reopen triggers. Keep this
   detail in the evidence register, claim ledger, workboard, reviewer discussion, and handoff.
2. The **reader-facing narrative** states the strongest supportable active claim directly, with its
   evidence and only the qualifiers needed to interpret that claim. It is not a dump of every
   limitation found during review.

Never make the reader-facing layer stronger than the internal record. Conversely, do not make it
weaker or harder to read merely to display caution.

## Separate capability collision, contribution attribution, and idea provenance

For prior-work framing and scoping, use the six-field accounting in
[prior-work-contribution-boundaries.md](prior-work-contribution-boundaries.md). A capability
collision requires positive evidence that the smallest named operation ran. Contribution
attribution separately requires an explicit author claim and matched demonstration. Describe a
`DEMONSTRATED_UNCLAIMED` operation as an observed capability of the audited artifact, not as the
authors' claimed contribution. Give a `CLAIMED_UNDEMONSTRATED` atom neither capability nor
contribution credit.

Keep concrete proposals, future-work directions, interpretations, and hypothetical scenarios in
`idea-provenance-ledger.csv` with
`CAPABILITY COLLISION=NONE` and `CONTRIBUTION CREDIT=NONE`. Use them selectively in Discussion to explain how the focal
project’s demonstrated result realizes, tests, complicates, or bounds a prior aspiration and why
the result matters in other HCI settings. Always describe the prior item as a proposal, not as a
realized capability or demonstrated contribution.

When authors explicitly claim that a realized capability exists but matched evidence does not
verify it, retain a `CLAIMED_UNDEMONSTRATED` accounting row and zero collision/credit. It may also
be cross-referenced as an unverified implementation claim in idea provenance; do not let the
provenance record hide the excluded claim.

Keep mixed channels and package conditions separate. Do not use one demonstrated
advance-one-slide mapping to claim general presentation control or a whole-system class; do not use
a computed-state-to-reward channel as user-action-to-command. Do not attribute a package result to
one operator without an identifying contrast, and do not translate nonsignificance into
equivalence.

## Apply the claim-local caveat test

For each candidate sentence or comparison:

1. atomize the claim: construct, population/context, relationship, quantity, comparator, and
   causal level;
2. identify the exact evidence and internal boundary;
3. include a qualifier, counterfinding, or limitation in the reader-facing passage only when it:
   - changes the truth, scope, quantity, causal meaning, or interpretation of the active claim;
   - directly bears on the selected comparison or contribution distinction;
   - prevents a likely material misunderstanding of transfer or terminology; or
   - belongs in an explicitly scoped Discussion, Limitations, or reviewer-response passage;
4. otherwise retain it in the internal evidence record and omit it from that passage.

Do not append a disclaimer about an outcome the text does not claim. Do not write “X; however, Y
is uncertain” merely because Y is downstream of X. If the paper claims only X, support X and stop.
If it later claims Y, reopen the evidence record and assess Y.

Use direct verbs matched to the evidence: for example, `measured`, `reduced`, `was associated
with`, `participants reported`, or `the published system provides`. Do not add `may`, `could`,
`suggests`, or a generic “however” by reflex. Hedge when the active claim's evidence requires it,
not as a stylistic display of defensiveness.

This rule never permits hiding contrary evidence that would make an active claim or comparison
false or materially misleading.

## Cite established foundations at the claimed level

Use strong prior work to support an inherited general mechanism, design fact, or measurement
relationship. Do not require a project to repeat an already established study merely because it
adopts that foundation.

Require project-specific verification only when the active claim concerns the exact artifact,
parameter value, implementation fidelity, device or setting coverage, delivered dose, robustness,
or downstream effect. Match the claim accordingly:

- A general claim that night-mode displays reduce blue-light output can cite full studies that
  measured the relevant spectral change.
- A quantitative claim about the exact project's overlay, its performance across devices, or its
  effect on sleep requires evidence for that more specific claim.
- When only the first claim is active, keep uncertainty about whole-night sleep outcomes in the
  internal review record; do not append it as a manuscript disclaimer.

## Apply the familiar-to-precise terminology rule

The **familiar-to-precise terminology rule** is reusable across domains: for a general audience,
introduce the familiar term first and define the exact source-matched scientific construct or
metric at first use. Then use a concise approved short form when it remains unambiguous.

Examples:

- `blue light—the short-wavelength portion of visible display output` when the cited study
  measures wavelength-resolved spectral output;
- `blue-light exposure, quantified here as melanopic equivalent daylight illuminance` when the
  cited study uses a melanopic metric.

Do not treat `blue light`, `short-wavelength output`, melanopic weighting, or a particular
photometric metric as interchangeable. The accessible entry term orients the reader; the
definition preserves what was actually measured.

## Propagate the distinction

During author discussion, show material cautions and non-claims explicitly so the author can
review the boundary. In the workboard, outline, and handoff, record:

- the complete internal evidence boundary;
- whether a reader-facing qualifier is `required` or `not required`;
- the claim-local reason for that disposition; and
- the evidence or wording change that would reopen it.

Keep full limitations in evidence tables and audit artifacts. In narrative summaries, comparisons,
and candidate paper language, include only claim-local qualifiers. Downstream writing must receive
both layers so it can remain concise without silently expanding the claim.
