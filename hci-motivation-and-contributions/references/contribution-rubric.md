# Prospective contribution sharpening

Phase 1 constructs contribution hypotheses and evidence requirements; it does not announce completed
contributions before design, implementation, and validation support them. Check the official
target-year CHI guidance before applying venue-specific criteria — CHI commonly weighs significance,
originality, research quality, presentation clarity, and relevant previous work, but its exact
language and procedures change.

## Contribution hypothesis

For each candidate, make every field explicit:

> We aim to contribute [reusable HCI capability or knowledge] for [people/task class]. It may be
> original relative to [closest work] because [precise difference]. We plan to instantiate it in
> [empirical waist]. Phase 2 must establish [design/system facts], and Phase 3 must establish
> [human/technical/knowledge claims]. If supported, it may help [broader HCI audience] where
> [shared mechanism] recurs, subject to [transfer boundary].

The outline may use shorter language, but it must retain the evidence states.

## Contribution types

Use only types the proposed research could plausibly support. Classify every candidate with the
seven knowledge-oriented types — **Empirical knowledge**, **Artifact**,
**Methodological knowledge**, **Theoretical knowledge**, **Dataset**, **Survey/meta-analysis**,
**Opinion/argument** — and run the identify → frame → classify → align-evidence protocol, CHI-label
mapping, and type-specific evaluation contracts in
[hci-contribution-types.md](hci-contribution-types.md) before scoring a package. The paper’s type is
the reusable output, not the technique or the paper section that contains it.

Two packaging labels remain available: **design knowledge**, a reusable design space, mapping,
tradeoff, principle, or process insight; and **open resource**, a reusable artifact whose
completeness, documentation, and license enable use. Map them onto the seven types explicitly rather
than collapsing dataset, survey, or argument work into them. An **artifact/capability** claim must
name the meaningful human action, state, control relationship, or information relationship it
enables; a prototype, algorithm, interview set, user study, or “insights” is a means, so state the
reusable capability or knowledge it should produce.

A package may carry a primary type and supporting types, each with its own claim and evidence gate,
and is decision-ready only when every atomic candidate has a complete contribution-candidate
register row as specified in that reference. Classification does not strengthen evidence and cannot
turn an outcome hypothesis, study method, implementation choice, or collected dataset into a
contribution.

## Phase 1 tests

### Significance

- Who experiences the problem, how often, and with what consequence, and what user tension or
  desired value motivates each proposed capability? State that value before capability or
  implementation, and label unmeasured value a rationale or hypothesis, not a benefit claim.
- What does the existing workflow already do well before, during, and after the focal activity, and
  is the claimed “missing” stage already served through speech, gesture, demonstration,
  coordination, or another workaround? Name the exact stage the project replaces, complements,
  extends, or bridges, and within it the sender, intended and actual recipients, same/different
  content, concurrency, visibility, selection provenance, and shared-awareness effects.
- Is this a capability, experience, access/cost, or knowledge gap; would expected value exceed
  setup, learning, hardware, privacy, safety, and adoption costs; why does it matter over the next
  three years; and what evidence would show the problem too small or misframed?

### Originality

- What is the closest predecessor, not the easiest comparison? Did a new author success criterion,
  residual state, anchor, or temporal estimand reopen the closest-work search rather than rename the
  existing feature comparison, and was every retained work classified before being used as a novelty
  comparator?
- Have the discovery gates in [related-work-positioning.md](related-work-positioning.md) been run
  and recorded, including which source owns the general concept lineage, which owns the
  in-domain HCI translation, and which exact construct remains? Residual-state topology must stay
  distinguishable: unchanged continuation, named attenuation, selective availability, substitution,
  bypass, denial. Retire only literal overlap; framing-level similarity never absorbs unmeasured
  technical, experiential, physiological, or outcome rungs.
- Is the focal capability written as a complete human-activity predicate, is each prior capability
  rewritten in the same grammar, and is every overlap classified `FULL_CAPABILITY_COLLISION`,
  `INDEPENDENT_SUBCAPABILITY_COLLISION`, `COMPONENT_OR_MECHANISM_PRECEDENT`, or `NO_COLLISION` using
  the removal and drop-in-port tests in
  [prior-work-contribution-boundaries.md](prior-work-contribution-boundaries.md)? Credit
  individually familiar qualifiers as component precedents without committing the
  component-subtraction fallacy against a novel complete capability.
- Does a “similar approach” share the causal interaction mechanism, or merely a modality, device,
  sensing method, multi-user topology, or personalization label? Is “physical versus virtual” a
  difference in the human activity — participants, interdependence, real objects, movement, timing,
  agency, risk, consequences — or merely the display setting? Apply the
  activity-versus-implementation counterfactual and the medium-as-contribution rule in
  [related-work-positioning.md](related-work-positioning.md), then test the claim conjunctively
  across problem, people, activity, setting, sender, recipient/content topology, concurrency,
  visibility, selection or adaptation provenance, intervention semantics, timing, agency, and
  evidence.
- Is prior-work evidence accounting complete for every material prior-work and focal-project atom —
  `AUTHOR CLAIM`, `DEMONSTRATED ARTIFACT OR STUDY`, `OPERATED CAPABILITY`, `EVALUATED RESULT`,
  `CAPABILITY COLLISION`, `CONTRIBUTION CREDIT` — with capability collision kept separate from
  contribution attribution? Component precedents, `CLAIMED_UNDEMONSTRATED` atoms, idea provenance,
  and bare ports take credit `NONE`; source silence yields only `SEARCH_PRIORITY` or `REOPEN_QUERY`;
  and short-format or non-archival works are audited at the scope of what actually ran and was
  measured, without a page-count discount.
- Are mixed systems decomposed into their atomic user-action/command, conventional-input,
  sensed-or-computed-state/adaptation-or-reward, condition/gating, and system-state/feedback
  channels before any whole-system label is used? A package condition supports only package-level
  causality absent an isolating contrast, and equivalent, comparable, maintained, or non-inferior
  wording requires an equivalence or non-inferiority design rather than nonsignificance.
- Could the approach have been pursued 3, 5, or 10 years ago, and what concretely changed? Is the
  novelty a scoped hypothesis rather than a claim that “no one has done this”?

### Plausibility and researchability

- Is there a credible mechanism from approach to proposed benefit, does every claim stay on its
  supported rung of `engineered setting → delivered operational exposure → perceived or behavioral
  mediator → physiological mediator → distal outcome`, and is each measure classified as
  manipulation/fidelity, delivered exposure, experience, behavior, physiology, or distal outcome?
- Does any proposed composite encode treatment assignment or weights that mechanically favor one
  condition? If so, report components separately and veto benefit or experience claims. A
  methodological composite also requires intervention-independent construct and weights, reported
  components, sensitivity and uncertainty analysis, convergent and discriminant validity, and
  demonstrated decision value.
- Are workflow significance, interaction/information-distribution capability, setting/activity
  boundary, implementation rationale, and untested outcomes separated and ranked without a universal
  ordering, with the primary contribution the strongest defensible consequential difference from the
  closest comparator? Could recipient-differentiated support remove shared information collaborators
  need, and is any “preserved awareness” claim still labeled a rationale or hypothesis?
- Can Phase 2 explore the experience before overbuilding the system, can Phase 3 obtain evidence
  proportional to the claim, and does the future comparator preserve valued current practice — for
  an additive layer, the intact workflow versus that workflow plus the layer?

### Broader HCI value

- Can a reader outside the domain restate the contribution in concrete people and actions rather
  than the project's technical labels, and what reusable idea remains once the application name is
  removed?
- What capability or knowledge survives if the preferred result is null, worse, heterogeneous, or
  burdened, and which prior proposals can the Discussion use as idea provenance while keeping their
  capability collision and contribution credit at `NONE`?
- Which adjacent domains share the mechanism rather than merely looking similar, what transfer needs
  new co-design, implementation, or validation, and would a broad CHI researcher learn something
  usable without building this artifact?

## Scope calibration

- Replace unbounded “first” with a bounded search scope, date, and closest-work comparison, without
  weakening a surviving complete-capability claim merely because its supporting components are
  individually familiar. Replace “real-time” with the planned operational latency and
  synchronization requirement until measured.
- Replace “individualized” or ambiguous “personalized” with the precise term from the vocabulary in
  [related-work-positioning.md](related-work-positioning.md) — `recipient-differentiated`,
  `role- or profile-configured`, `system-personalized`, `personalizable` or `user-adjustable`,
  `adaptive`, or `player-specific`. Any surviving use of “personalized” must identify the personal
  attributes or needs, the selector, and the person model, and “private” requires verified access or
  routing, not information merely addressed to one person.
- Replace “augments rather than replaces” with the exact retained workflow, newly supported stage,
  and activity-level difference; “generalizable” with hypothesized transfer dimensions and required
  validation; “improves” with “is designed to support” until comparative evidence exists; “users
  need” with the population, task, evidence type, and boundary; and “our contribution is” with “we
  propose” or “we aim to investigate” while the claim remains prospective.

## Readiness packages

The final gate offers three to five internally coherent packages, each keeping motivation, gap,
approach, empirical waist, future evidence, broader implication, vocabulary, limitations, and return
conditions aligned. A package may be narrower than the team's ambition, never broader than what the
planned research could credibly establish.
