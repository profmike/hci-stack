# Claim-focused research communication

## Treat reusable examples as illustrations, not project state

Examples in this reusable skill illustrate the method. They are not project evidence, author
decisions, active project claims, or a durable project record. When an author adopts one, record in the target
project repository before relying on it: selected wording or policy, author rationale, evidence
boundary, reader-facing qualifier disposition, propagation targets, and reopen trigger. That
project-owned record remains authoritative if a later skill revision changes the example. If the
target repository is unknown, keep the decision session-only;
never use the skill repository as substitute project storage.

## Keep the audit complete and the prose relevant

The **internal evidence record** — evidence register, claim ledger, workboard, handoff — preserves
every uncertainty, limitation, contrary finding, and reopen trigger. The **reader-facing narrative**
states the strongest supportable active claim with only the qualifiers needed to interpret it, never
stronger than the internal record and never weakened to display caution.

### Keep generic disclaimers in the researcher record

Keep review-wide caveats such as `Most of this evidence is correlational` internal; make each
reader-facing sentence accurate at source through evidence-matched verbs instead.

## Open with concrete findings, not importance labels

Do not begin with labels such as `a serious human problem`. Begin with the strongest concrete finding
— who does what, in what context, with what proximal consequence — and add downstream stakes only
through separately supported links. Keep sample sizes, protocols, and effect sizes in the internal
record or Related Work unless a number itself establishes scale.

## Put each citation beside the claim it supports

Place a citation immediately after the smallest supported claim, result, construct, or keyword, never
as a pile at the end of a sentence.
Repeat a work wherever it directly supports another key claim; a citation elsewhere does
not support the current claim. Treat independently supported items in an
enumeration as separate claim atoms and cite each immediately — `monitoring [A]`, `reminders [B]`,
`limits [C]`. Split citation clusters as finely as the evidence permits; a multi-source cluster fits
only when every work supports the same indivisible atom, and
it has no numeric cap in that case.

## Use a six-move Introduction for time-anchored transition interventions

When a project intervenes around a transition rather than an aggregate quota, order the
reader-facing Introduction as:

1. **Concrete behavior and consequence** in its temporal context, with only separately evidenced
   downstream stakes.
2. **Why the transition differs from aggregate control**, never as untested superiority.
3. **Prior approaches and measured limits.**
   Call prior controls binary, high-dropout, bypassed, or ineffective only when the checked evidence
   measures that exact property.
4. **Outcome-oriented approach, then mechanisms**, separating inherited mechanism evidence, the
   project's capability, and any unmeasured explanation. For a graded intervention, state each
   channel's full intensity range and whether an endpoint preserves or denies access: delivery delay
   may reduce immediacy, but `reduces the reward loop` remains a hypothesis unless reward processing
   is measured.
5. **Newly enabled investigation** — the comparison the capability makes possible.
6. **Study and contribution statement.** Use `We conducted` only after the study is complete and its
   evidence verified; otherwise use `We plan`, and keep every contribution prospective.

## Lead with human value before mechanism

Introduce every approach, feature, design choice, or contribution in the order
`human situation or tension → value people need → capability that supports it → necessary implementation detail`.
Ask: **What matters in this person's activity, and what breaks without it?** If the answer appears
only after the capability, reorder the passage.

### State motivation and user value declaratively

Write reader-facing motivation and user value as positive declarative statements.
Do not use author-voice `should`, `ought`, or `deserves` as a substitute for
showing the activity, constraint, consequence, or value. Deontic wording asks readers to endorse a
value judgment; strong motivation makes the warranted premise legible as fact. State an observed
condition directly (`One team play gives different players different jobs.`) and an untested value as
a design goal (`The design aims to let guidance step back as players learn.`).
Reserve `should` for a precisely attributed recommendation or policy — keeping that attribution in
the sentence — or for internal procedural instructions.

Prefer concrete people and actions over academic noun stacks: introduce
`players whose actions must work together` before `interdependent roles`, and
`different teammates hear the next instruction they need` before
`recipient-differentiated semantic guidance`.

Capability is not benefit. For a design rationale or outcome hypothesis write `is designed to`,
`aims to`, or `lets us investigate` rather than asserting the system already improves learning,
coordination, workload, or performance, and record the intended value and its evidence state
separately from the implemented mechanism.

## State the approach before its implementation substrate

The **approach invariant** is the human-activity, interaction, or control-policy change that stays
meaningful if the operating system, device, framework, or rendering medium changes; the
**implementation substrate / empirical waist** is what the project evaluates it on.

Reader-facing order:

`problem → closest-work residual gap → platform-independent approach → inherited rationale → implementation instance → prospective contributions`

Pattern: `We present [approach invariant]. We instantiate and evaluate it on [implementation
substrate].` Do not open with `We present an Android/iOS/VR/... system` when the platform merely
realizes the approach. Credit platform-specific work only when matched evidence shows non-routine
reusable adaptation knowledge, a new class of use, or a direct empirical finding — or where the
medium itself changes the human capability or access boundary.

## Separate capability collision, contribution attribution, and idea provenance

Apply the six-field accounting in
[prior-work-contribution-boundaries.md](prior-work-contribution-boundaries.md): a collision needs
positive evidence that the smallest named operation ran and a match at the
complete human-activity predicate or independently claimed sub-capability scope.
In prose, never let one demonstrated narrow channel stand for a general
capability, and never translate nonsignificance into equivalence.

## Apply the claim-local caveat test

Atomize each candidate sentence or comparison (construct, population/context, relationship, quantity,
comparator, causal level) and identify the exact evidence and internal boundary. Carry a qualifier,
counterfinding, or limitation into reader-facing prose only when it changes the active claim's truth,
scope, or interpretation, bears on the selected comparison, or belongs in a scoped Discussion or
Limitations passage; otherwise keep it internal.

Do not append a disclaimer about an outcome the text does not claim, and do not write “X; however, Y
is uncertain” merely because Y is downstream of X. Use direct verbs matched to the evidence rather
than reflex `may`, `could`, or `suggests`.
This rule never permits hiding contrary evidence that would make an active claim false or
materially misleading.

## Cite established foundations at the claimed level

Cite strong prior work for an inherited general mechanism or measurement relationship rather than
requiring a project to repeat an established study it adopts. Require project-specific
verification only when the active claim concerns this project's artifact, parameter value, or
downstream effect: a general
claim that night-mode displays reduce blue-light output can cite the studies that measured that
spectral change, while a claim about this project's overlay or its effect on sleep needs its own
evidence — and while only the general claim is active, keep uncertainty about
whole-night sleep outcomes in the internal review record.

## Apply the familiar-to-precise terminology rule

The **familiar-to-precise terminology rule** is reusable across domains: introduce the familiar term
first, define the exact source-matched scientific construct at first use, then use a concise approved short form
while it stays unambiguous — write
`blue light—the short-wavelength portion of visible display output` for a wavelength-resolved study,
or `blue-light exposure, quantified here as melanopic equivalent daylight illuminance` for a
melanopic metric. Do not treat those constructs as interchangeable: the definition preserves what
was measured.

In the workboard, outline, and handoff, record the internal evidence boundary, whether a
reader-facing qualifier is `required` or `not required`, the claim-local reason, and the reopen
trigger.
