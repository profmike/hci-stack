# Prospective contribution sharpening

Phase 1 constructs contribution hypotheses and evidence requirements. It does not announce
completed contributions before design, implementation, and validation support them.

Check the official target-year CHI guidance before applying venue-specific criteria. CHI commonly
weighs significance, originality, research quality, presentation clarity, and relevant previous
work; exact language and procedures can change.

## Contribution hypothesis

For each candidate, make every field explicit:

> We aim to contribute [reusable HCI capability or knowledge] for [people/task class]. It may be
> original relative to [closest work] because [precise difference]. We plan to instantiate it in
> [empirical waist]. Phase 2 must establish [design/system facts], and Phase 3 must establish
> [human/technical/knowledge claims]. If supported, it may help [broader HCI audience] where
> [shared mechanism] recurs, subject to [transfer boundary].

The outline may use shorter language, but it must retain the evidence states.

## Contribution types

Use only types the proposed research could plausibly support:

- **Artifact/capability:** a system, interaction, device, toolkit, dataset, or infrastructure that
  enables a meaningful human action, state, control relationship, or information relationship.
- **Empirical knowledge:** a robust finding about people, interaction, practice, or outcomes.
- **Design knowledge:** a reusable design space, mapping, tradeoff, principle, or process insight.
- **Methodological knowledge:** a defensible new way to design, measure, or evaluate an HCI
  phenomenon.
- **Theoretical knowledge:** an explanatory model, framework, or lens.
- **Open resource:** a reusable artifact whose completeness, documentation, and license enable use.

A prototype, algorithm, interview set, user study, or “insights” is usually a means. State the
reusable capability or knowledge it is intended to produce.

### Contribution-type discipline

Use the seven knowledge-oriented types in [hci-contribution-types.md](hci-contribution-types.md)
when classifying a candidate. The paper’s type is the reusable output, not the technique or paper
section that happens to contain it:

| Paper type | Required Phase 1 question |
| --- | --- |
| Empirical knowledge | What important finding is produced, and why are the observation and analysis sound? |
| Artifact | What meaningful possibility does the system, tool, technique, or design expression open, and which artifact-specific standard applies? |
| Methodological knowledge | What reusable way of discovering, measuring, analyzing, creating, or evaluating is improved, and how will utility, reproducibility, reliability, or validity be established? |
| Theoretical knowledge | What concept, model, principle, or framework explains what to expect and why, and what would test or falsify it? |
| Dataset | What useful and representative corpus or benchmark becomes available, with what provenance, documentation, access, and reuse boundary? |
| Survey/meta-analysis | What mature body of work is synthesized into trends, gaps, or opportunities beyond a literature list? |
| Opinion/argument | What position is being advanced, what credible evidence supports it, and which opposing view is represented fairly? |

CHI 2016 split empirical work into “system use” and “people”; preserve that distinction when it
helps identify the empirical object, but map both to empirical knowledge in the seven-type record.
Keep the skill’s design-knowledge and open-resource labels as explicit packaging mappings rather
than silently collapsing dataset, survey, or argument work into them. A single package may have a
primary type and supporting types, but each type must carry a separate claim and evidence gate.

Before scoring a package, run the complete identify → frame → classify → align-evidence protocol in
[hci-contribution-types.md](hci-contribution-types.md). A package is not decision-ready unless every
atomic candidate records its benefit-first reusable output, primary and optional supporting types,
classification rationale and strongest rejected alternative, closest prior output and exact delta,
current evidence state, type-specific evidence gate, null-result survivor, status, and reopen
trigger. Classification does not strengthen the underlying evidence and cannot turn an outcome
hypothesis, study method, implementation choice, or collected dataset into a contribution.

## Phase 1 tests

### Significance

- Who experiences the problem, how often, and with what consequence?
- What user tension or desired value motivates each proposed capability or control?
- Does the paper-facing explanation state that value before listing capability or implementation?
- If the value is not yet measured, is it clearly a rationale or hypothesis rather than a benefit claim?
- What does the existing workflow already do well before, during, and after the focal activity?
- Is the claimed “missing” stage already served by people through speech, gesture, demonstration,
  coordination, or another workaround?
- Which exact stage does the project replace, complement, extend, or bridge?
- Within that stage, what are the sender, intended and actual recipients, same/different content,
  concurrency, visibility, selection provenance, and shared-awareness effects?
- Is this a capability, experience, access/cost, or knowledge gap?
- Would expected value exceed setup, learning, hardware, privacy, safety, and adoption costs?
- Why will this matter now and over the next three years?
- What evidence would show the problem is too small or misframed?

### Originality

- What is the closest predecessor, not the easiest comparison?
- Did a new author success criterion, residual state, anchor, or temporal estimand reopen the
  closest-work search rather than merely rename the existing feature comparison?
- What does the intervention optimize: cessation/quantity, the conditions of remaining activity,
  trajectory, perceived experience, physiology, or a distal outcome?
- Under an equal-quantity counterfactual, what independently observed construct could still differ?
- Which source owns the general concept lineage, which source owns the in-domain HCI translation,
  and which exact construct remains for the project? Retire only literal overlap; do not let a
  framing-level similarity absorb unmeasured technical, experiential, physiological, or outcome
  rungs.
- What are the policy's anchor, trigger, states, transitions, actuators, access semantics,
  protected value, override, and reset?
- Does the residual-state topology distinguish unchanged continuation, named attenuation,
  selective availability, substitution, bypass, and denial?
- Is anchor semantics kept separate from empirical anchor quality such as clarity, stability,
  precision, comprehension, or intention fit?
- If timing differs, are onset, trajectory, target intensity, cumulative dose, and transition
  semantics separately identified or honestly labeled a policy-package comparison?
- Has every retained work been classified before it is used as a novelty comparator?
- Is the focal capability written as a complete human-activity predicate—people/roles, meaningful
  action or information relationship, activity, purpose, and essential interdependence, semantics,
  timing, and control—and is each prior capability rewritten in the same grammar?
- Is every overlap classified as `FULL_CAPABILITY_COLLISION`,
  `INDEPENDENT_SUBCAPABILITY_COLLISION`, `COMPONENT_OR_MECHANISM_PRECEDENT`, or `NO_COLLISION`?
- Does the removal test show that each purportedly core dimension changes what people can
  meaningfully do, and does the drop-in-port test show whether the prior mechanism could support the
  focal semantics and interdependence unchanged?
- Does a “similar approach” share the causal interaction mechanism, or merely a modality, device,
  sensing method, multi-user topology, or personalization label?
- If the closest systems used identical hardware, interfaces, and output modalities, would the
  proposed contribution-level difference remain?
- If the device or medium is itself contribution-bearing, what consequential platform-specific
  constraint/solution knowledge, human capability, validated new use class, or measured
  outcome/access change is explicitly claimed and demonstrated beyond its label?
- Is “physical versus virtual” changing the human activity—participants, interdependence, real
  objects, movement, timing, agency, risk, or consequences—or merely the display setting?
- What is learned from, inherited from, or inspired by that work?
- Is the difference user-facing or knowledge-producing rather than a fashionable component?
- Does the proposed claim survive a conjunctive comparison across problem, people, activity,
  setting, sender, recipient/content topology, concurrency, visibility, selection or adaptation
  provenance, intervention semantics, timing, agency, and evidence?
- Which individual qualifiers are already established by different prior works, and have they been
  credited as component precedents without committing the component-subtraction fallacy against a
  novel complete capability?
- Does “recipient-differentiated” accurately describe different content by intended recipient, or
  does “individualized” incorrectly imply inferred or adaptive personalization?
- Does “player-specific” identify only the addressee, while any different-content, tailoring,
  access, or adaptation property is stated separately?
- Does “personalizable” or “user-adjustable” name the exact controllable dimension rather than
  relabeling the whole intervention as personalized?
- If “personalized” is used, are the personal attributes or needs, selector, and person model
  explicitly identified?
- Does “private” describe verified access/routing, or only information addressed to one person?
- Has every material prior-work and focal-project atom independently recorded `AUTHOR CLAIM`,
  `DEMONSTRATED ARTIFACT OR STUDY`, `OPERATED CAPABILITY`, `EVALUATED RESULT`,
  `CAPABILITY COLLISION`, and `CONTRIBUTION CREDIT`?
- Does capability collision require positive evidence that the smallest named operation ran, while
  contribution attribution separately requires an explicit claim and matched demonstration?
- Is every `DEMONSTRATED_UNCLAIMED` operation allowed to narrow firstness only at its matched
  complete-predicate or independently claimed sub-capability scope, while a component precedent
  leaves full-capability firstness intact and receives contribution credit `NONE`?
- Does every `CLAIMED_UNDEMONSTRATED` atom receive collision and contribution credit `NONE`?
- For each short-format or non-archival work in the corpus — poster, extended abstract,
  late-breaking work, work-in-progress, demo abstract, position paper, vision paper, preprint,
  tech report, patent — does the row record which of the two idea-gate questions was answered
  positively? A work where nothing ran and nothing was measured takes `NONE` in both columns. A work
  that did run and measure something is audited at the scope of what it ran, without a page-count
  discount.
- Is operated capability `NO` supported by positive artifact evidence, while source silence creates
  only `SEARCH_PRIORITY` or `REOPEN_QUERY`?
- Are future work, ideas, interpretations, and hypothetical scenarios kept only in idea provenance
  with collision and credit `NONE`? Does every explicit but unverified author claim of realized
  capability also remain visible as `CLAIMED_UNDEMONSTRATED`, with collision and credit `NONE`?
- Are mixed systems decomposed into atomic user-action/command, conventional-input,
  sensed-or-computed-state/adaptation-or-reward, condition/gating, and system-state/feedback
  channels? Is any whole-system label supported for every channel its operational definition
  requires?
- Does a package condition support only package-level causality unless an isolating contrast exists?
- Is equivalent, comparable, maintained, or non-inferior wording backed by an equivalence or
  non-inferiority design rather than nonsignificance?
- Does every platform/hardware/sensor/OS/app/game port receive credit `NONE` unless full-source
  evidence demonstrates nontrivial adaptation, a new use class, or a directly validated empirical
  finding? Is any underlying operated-capability collision still preserved?
- Could the approach have been pursued 3, 5, or 10 years ago? What concretely changed?
- Is the novelty a scoped hypothesis rather than a claim that “no one has done this”?

### Plausibility and researchability

- Is there a credible mechanism connecting the approach to the proposed benefit?
- Does every claim stay on its supported rung of `engineered setting → delivered operational
  exposure → perceived or behavioral mediator → physiological mediator → distal outcome`?
- Is each measure classified as manipulation/fidelity, delivered exposure, experience, behavior,
  physiology, or distal outcome?
- Does any proposed composite encode treatment assignment or weights that mechanically favor one
  condition? If so, report components separately and veto benefit or experience claims.
- For a methodological composite, are the construct and weights intervention-independent,
  components reported, sensitivity/uncertainty analyzed, convergent/discriminant validity tested,
  and decision value demonstrated?
- Are workflow significance, interaction/information-distribution capability, setting/activity
  boundary, implementation rationale, and untested outcomes separated and then ranked without a
  universal ordering?
- Is the primary contribution the strongest defensible consequential difference from the closest
  comparator, even when workflow significance is a supporting layer rather than the originality?
- Could recipient-differentiated support remove shared information collaborators need, and is any
  “preserved awareness” claim still labeled as a rationale or hypothesis?
- Can Phase 2 explore the experience before overbuilding the system?
- Can the team access representative people and realistic contexts?
- Are the technical, safety, privacy, and ethical risks tractable?
- Can Phase 3 obtain evidence proportional to the intended claim?
- Does the future comparator preserve valued current practice—for an additive layer, the intact
  workflow versus the same workflow plus that layer?

### Broader HCI value

- Can an intelligent reader outside the domain restate the contribution using concrete people and
  actions rather than the project's technical labels?
- What reusable idea might remain after removing the application name?
- What capability or knowledge survives if the preferred result is null, worse, heterogeneous, or
  burdened?
- Which prior proposals can the Discussion use as idea provenance to broaden the demonstrated
  result's relevance while keeping their capability collision and contribution credit at `NONE`?
- Which adjacent domains share the mechanism rather than merely looking similar?
- What transfer requires new co-design, implementation, or validation?
- Would a broad CHI researcher learn something usable even if they never build this artifact?

## Scope calibration

- Replace unbounded “first” with a bounded search scope, date, and closest-work comparison, but do
  not weaken a surviving complete-capability claim merely because its supporting components are
  individually familiar.
- Replace “real-time” with the planned operational latency and synchronization requirement until
  measured.
- Replace “individualized” or ambiguous “personalized” with `recipient-differentiated` when
  intended recipients receive different content, `role- or profile-configured` when a person
  selects from declared attributes, `system-personalized` when the system uses a stored or inferred
  individual model, `personalizable` or `user-adjustable` for the exact dimension a person can
  configure, or `adaptive` only when support changes with inferred state, behavior, or performance.
  Use `player-specific` or another domain term when only the intended addressee is established.
- Replace “generalizable” with hypothesized transfer dimensions and required validation.
- Replace “improves” with “is designed to support” until comparative evidence exists.
- Replace “augments rather than replaces” with the exact retained workflow, newly supported stage,
  and activity-level difference.
- Replace “users need” with the population, task, evidence type, and boundary.
- Replace “our contribution is” with “we propose” or “we aim to investigate” when it remains
  prospective.

## Readiness packages

The final gate should offer three to five internally coherent packages. Each keeps motivation,
gap, approach, empirical waist, future evidence, broader implication, vocabulary, limitations, and
return conditions aligned. A package may be narrower than the team's ambition; it cannot be broader
than what the planned research could credibly establish.
