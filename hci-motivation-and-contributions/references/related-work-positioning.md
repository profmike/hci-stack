# Related-work positioning protocol

Read this protocol before classifying retained works, auditing contribution strength, or writing
comparison options.

## Contents

- [Represent and classify works](#represent-and-classify-works)
- [Establish target-problem identity and separate portfolios](#establish-target-problem-identity-and-separate-portfolios)
- [Map current human practice](#map-current-human-practice)
- [Compare consequential interactions](#compare-consequential-interactions)
- [Discover objective, state, and temporal contributions](#discover-objective-state-and-temporal-contributions)
- [Apply six-field prior-work evidence accounting](#apply-six-field-prior-work-evidence-accounting)
- [Separate activity from implementation](#separate-activity-from-implementation)
- [Test conjunctive claims and terminology](#test-conjunctive-claims-and-terminology)
- [Calibrate novelty assertiveness](#calibrate-novelty-assertiveness)
- [Rank contribution strength and proximity](#rank-contribution-strength-and-proximity)
- [Situate the work in the HCI community](#situate-the-work-in-the-hci-community)
- [Write the ranked positioning dossier](#write-the-ranked-positioning-dossier)
- [Produce the audit](#produce-the-audit)

## Represent and classify works

Represent prior work objectively and positively. Describe capabilities, contexts, evidence, and
boundaries—not “failures” manufactured to make an empty gap.

First establish the target-problem identity and assign a problem-proximity band using the next
section. Then, before comparing differences or assigning contribution tiers, pass every retained
work through a mandatory **relationship-classification gate**:

1. closest contribution comparator;
2. secondary same-domain evidence;
3. adjacent system or analogous intervention;
4. complementary tool or current-practice baseline;
5. design foundation or inspiration;
6. motivation, theory, or review; or
7. excluded or unresolved.

Only the first category is eligible by relationship for overall contribution-comparator rank.
Attributed contribution credit still requires an explicit author claim and matched demonstration.
A demonstrated operated capability from another relationship class—including an unclaimed
operation—may create a narrow capability collision without becoming a closest overall comparator
or an attributed contribution. A secondary practical alternative may receive a tier when the
comparison is explicit and passes the same evidence accounting. Foundations, distant analogies,
theory, reviews, motivation sources, and under-described interactions normally receive `N/A`. A
change of application domain is not itself a Tier 1 capability.
Only `SAME-SPECIFIC-PROBLEM` or `SIMILAR-PROBLEM` work may be a closest overall contribution
comparator. An adjacent or different-problem work can instead be a claim-specific collision.

## Establish target-problem identity and separate portfolios

Before ranking any work, freeze a **target-problem identity contract**:

`target people → focal activity → triggering or temporal context → unwanted state or episode →
intended change or outcome`

Define each element operationally enough that two reviewers could tell whether another paper
addresses it. Do not put the proposed interface, intervention, or causal explanation inside this
identity. If constructs such as agency, stimulation, reward, burden, attention, or control are
hypotheses rather than directly established parts of the human problem, record them separately as
hypothesized mechanisms or outcomes. Reopen the contract when project evidence changes any of its
five elements. Do not use an unvalidated mechanism hypothesis to pull a paper solving a different
problem into the primary ranking.

Assign every retained work one descriptive **problem-proximity band** before mechanism similarity,
venue, evidence strength, or novelty leverage:

1. `SAME-SPECIFIC-PROBLEM`: substantially the same unwanted state or episode and intended
   change/outcome, with a close focal activity and triggering context;
2. `SIMILAR-PROBLEM`: the same focal human difficulty and intended change/outcome, with a bounded
   difference in population, activity, or context that must be named;
3. `ADJACENT-PROBLEM`: the same broad domain or construct, but a materially different unwanted
   state, objective, or intended outcome; or
4. `DIFFERENT-PROBLEM`: a different human problem that may still supply a mechanism collision,
   theory, design foundation, feasibility result, or analogy.

Same-domain vocabulary—such as wellbeing, agency, quality, control, engagement, social media,
collaboration, or personalization—cannot upgrade problem proximity. Neither can a shared device,
interaction label, outcome valence, or abstract observation. Evidence strength and venue quality
bound what can be claimed about a work; they do not change which problem it solves.

Keep three portfolios:

1. **Primary problem-space portfolio:** verified `SAME-SPECIFIC-PROBLEM` and `SIMILAR-PROBLEM`
   works. These alone compete for the closest-work ranking.
2. **Mechanism/capability-collision portfolio:** work that addresses another problem but positive
   evidence shows actually operated a causally similar mechanism or the exact capability being
   considered. It may decisively narrow that capability claim, including when the operation was
   not author-claimed, but it cannot displace a closer problem comparator. Keep contribution
   attribution separate. Put proposals in idea provenance, not this collision portfolio.
3. **Concept, theory, and foundation inventory:** abstract concepts, reviews, component evidence,
   theory, exemplars, current-practice lineage, and distant analogies. Give each a claim-specific
   role; do not assign an overall closeness rank.

A work can be distant overall yet decisive for one narrow claim. Label this a
**claim-specific collision**, name the exact claim it bounds, and preserve the broader problem
difference. Never translate “shares a mechanism or vocabulary” into “solves the same problem.”

## Map current human practice

Before comparing artifacts, map the **existing human workflow**:

`what people do before the focal activity → what they do during it → what they do afterward`

Record the actors, artifacts, representations, physical or social setting, purpose, and informal
human interventions or workarounds at each stage. Then state whether the proposed work replaces,
complements, extends, or bridges parts of that workflow. Credit the value of current practice.
“Augments rather than replaces” is not itself a novelty claim because competing systems may also
coexist with current practice; name the exact workflow stage and human activity affected.

Run a **current-practice collision check** before claiming that the project introduces support at a
new workflow stage:

> Is the proposed capability already performed at that stage by people through speech, gesture,
> demonstration, coordination, or another non-digital workaround?

“No prior system supports this” does not mean “no current practice supports this.” If people
already intervene at that stage, preserve that fact and identify the more precise change inside the
stage—for example who can address whom, whether recipients receive the same or different content,
whether delivery is concurrent or serialized, or how the intervention relates to the activity.

For every consequential stage, map its **communication and information-distribution structure**:

`sender → author or selector → intended and actual recipients → same or different content →
shared or recipient-differentiated visibility → concurrent or serialized delivery → selection
provenance → resulting shared awareness`

Do not equate a new communication topology with a new workflow stage. A project may extend an
existing human intervention by changing its recipient/content structure while leaving its timing
and overall workflow intact.

## Compare consequential interactions

For the closest predecessors, compare the interaction before comparing implementation maturity.
Trace the full information flow:

`who defines the guidance → what is sensed or authored → how it is transformed → what the output
means → who receives it → when they receive it → what they can do with it`

Do not confuse one data stream *about* each person with one distinct message delivered *to* each
person. Separate a paper's implemented and evaluated interaction from future scenarios in its
Discussion. Use the exemplar pattern for concise positioning:

1. credit the predecessor's most relevant capability or insight;
2. state one decisive contribution-level contrast, usually in recipient topology, information
   semantics, human agency, timing, or purpose; and
3. connect that contrast directly to the proposed contribution.

For each closest work, build a dimension-by-dimension comparison before compressing it into one
sentence:

`problem → people → activity → workflow stage → setting → sender → author/selector → intervention
semantics → intended and actual recipients → same/different content → concurrent/serialized
delivery → visibility/shared awareness → selection or adaptation provenance → timing → human
agency → evidence`

For behavior-change or access-control systems, expand `intervention semantics` into:

`intention/goal anchor → configuration object and certainty → access state → activation
selector/gate → changed parameter → progression variable → within-active ramp → duration →
onset/cadence → cap/reset → scope → override/exceptions → selector`

These dimensions are not interchangeable. A system that lengthens successive all-or-nothing
blocks has graduated **duration** but still binary **access**. A system that leaves an activity
usable while progressively changing display, latency, interaction effort, or available features
has graduated **attenuation**. Intermittent access windows do not make each intervened state
nonbinary. A cumulative daily-use budget and a target-bedtime schedule also encode different
intentions: aggregate quantity over an accounting day versus a transition relative to a clock or
event. Record the configuration burden and evidence for how concretely people can specify either
anchor; never promote an author intuition about that difference into an established user fact.
Name the literal operational difference first; only then decide whether it is a capability,
experience/outcome, or implementation distinction.

Treat under-description as unresolved by default. Record the exact source passage or positive
artifact trace needed. Never use silence or assumptions about what authors would have reported to
infer an absent capability.

Use implementation age, missing evaluation, latency, or other maturity boundaries only when they
are themselves central to the contribution. Do not substitute a limitation inventory for
positioning. Generate three to five candidate comparison sentences, with evidence and tradeoffs,
before asking the author to choose the emphasis.

## Discover objective, state, and temporal contributions

Feature-by-feature comparison can miss contributions that change what an intervention optimizes,
what state remains possible, or when a policy acts. Before finalizing contribution packages, run
all of the following gates. Keep the outputs separate until the closest-work and evidence audits
show that they form one defensible conjunction.

### Intervention-objective and equal-quantity gate

Map the proposed success criterion across:

`quantity or cessation → conditions of remaining activity → trajectory → perceived experience →
physiological process → distal outcome`

Then ask the **equal-quantity counterfactual**: if elapsed use, task completion, or another common
quantity were identical across conditions, what independently observed construct could still
differ? A broad statement that “quality matters, not only quantity” is not novel without a
closest-work audit. Name the operational, experiential, or outcome construct and the evidence that
would distinguish it.

### Concept-lineage versus in-domain-collision gate

Separate three novelty questions that are often collapsed:

1. **General concept lineage:** which field first established the abstract relationship, such as
   quantity not fully characterizing delivered conditions or behavior?
2. **In-domain translation:** which HCI work already applied that relationship to the target
   activity, values, or evaluand, such as agency or meaningfulness in digital wellbeing?
3. **Exact project delta:** which independently defined control policy, measure, mechanism, or
   finding remains after both lineages are credited?

A broad concept from another field does not automatically establish a domain-specific human value,
and an in-domain paper does not automatically cover every technical, experiential, physiological,
or distal causal rung. Compare the literal constructs and measures. **Retire novelty only at the overlapping level**;
do not let one paper absorb an entire causal chain because its framing sounds broad. Conversely,
moving a known principle into HCI is not itself novel when prior HCI work has already made that
translation.

### Collision–delta and control-policy anatomy gate

For each candidate record:

`closest prior → shared causal core → exact surviving delta`

For an intervention policy also record:

`anchor/configuration object → activation selector → states → transitions → actuators/changed
parameters → access semantics → protected value → override/bypass → reset/recovery`

A meaningful control state or relationship may be capability-level even when it does not enable a
wholly new task. Conversely, a familiar component does not become novel because it appears inside
a new label.

### Residual-state topology gate

Map what happens when the preferred behavior does not occur:

`continue unchanged → continue under named attenuation → retain selected functions → substitute
modality/activity → bypass → deny`

Record the protected human value, operational dimension changed, urgent-use path, substitution
opportunity, accessibility and task-success risk, and failure cost. Use structural language such
as `continued access under [named change]` until evidence establishes lower harm, better quality,
greater agency, or another benefit.

### Anchor semantics versus anchor quality gate

Separate the system fact encoded by an anchor from claims about how well it represents people.
Session duration, cumulative daily budget, intended clock/event transition, sensed receptivity,
and explicit mode selection are different control semantics. Clarity, precision, stability,
importance, calibration ease, comprehension, and intention fit are empirical **anchor-quality**
claims. A semantic difference cannot be relabeled as better alignment without evidence.

### Temporal-role and identifiability gate

Classify the policy as anticipatory, transition-time, reactive, recovery-oriented, or a stated
combination. Record onset, within-active trajectory, target-time intensity, duration, cumulative
dose, and reset. If a comparison varies more than one of these, name it as a policy-package
comparison. Do not attribute a result to anticipation, gradualness, intensity, or dose unless that
factor is identified by an orthogonal, matched, factorial, dismantling, or otherwise defensible
contrast.

### Construct-independence and composite-measure veto

Classify each proposed measure as manipulation/fidelity, delivered exposure, perceived mediator,
behavior, physiology, or distal outcome. A condition label, assigned level, or treatment-defined
weight may measure delivered dose; it cannot mechanically establish experience, harm reduction,
or benefit. A composite can support a methodological contribution only when:

- the construct is defined independently of treatment;
- weights are theoretically or empirically defensible;
- components remain separately reported;
- uncertainty and sensitivity to weights are shown;
- convergent and discriminant validity are assessed; and
- the score adds decision-relevant information beyond simpler measures.

Prefer a multidimensional profile over a scalar until these requirements pass.

### Causal-ladder and fidelity gate

Audit each edge separately:

`engineered setting → delivered operational exposure → perceived or behavioral mediator →
physiological mediator → distal outcome`

Record the evidence state and fidelity check for every rung and edge. Never infer a downstream
experience, mechanism, physiology, or outcome merely because an upstream setting changed. A
component-foundation paper can motivate a downstream hypothesis; it does not complete the chain
for the proposed artifact.

### Null-survival gate

For every contribution package, state what reusable capability or knowledge remains if the
preferred condition is null, worse, heterogeneous, or burdened. A package fails when its only
contribution is that one favored design wins. Boundary conditions, identified tradeoffs, validated
measures, and falsified mechanisms can be contributions when the design can actually establish
them.

## Apply six-field prior-work evidence accounting

Read [prior-work-contribution-boundaries.md](prior-work-contribution-boundaries.md). Maintain
`prior-work-evidence-accounting.csv`, `idea-provenance-ledger.csv`, and the human-readable
`prior-work-contribution-boundary.md`.

Atomize every material proposition and assign six independent fields:

- `AUTHOR CLAIM`;
- `DEMONSTRATED ARTIFACT OR STUDY`;
- `OPERATED CAPABILITY`;
- `EVALUATED RESULT`;
- `CAPABILITY COLLISION`; and
- `CONTRIBUTION CREDIT`.

No field inherits truth from another. Compare the smallest positively evidenced command, parameter,
input channel, reward channel, configuration, study condition, or finding.

Use two separate boundaries:

1. **Capability collision:** require positive evidence that the exact operation actually ran. An
   operated but unclaimed atom is `DEMONSTRATED_UNCLAIMED`; it may narrow firstness, force a fair
   comparator, or establish inheritance.
2. **Contribution attribution:** require an explicit author claim and matched demonstration. For an
   artifact-capability atom, also require demonstrated operation. Credit only the matched
   intersection and narrow it to the weakest supported scope.

A `DEMONSTRATED_UNCLAIMED` operation receives `CONTRIBUTION CREDIT=NONE`; describe it as an observed
capability of the audited artifact, not as the authors' claimed contribution. A
`CLAIMED_UNDEMONSTRATED` atom receives `CAPABILITY COLLISION=NONE` and
`CONTRIBUTION CREDIT=NONE` unless separate positive operation evidence exists.

Keep package results at package scope and reject operator-specific causal claims without an
isolating contrast. Reject equivalent, comparable, maintained, or non-inferior wording based only
on nonsignificance.

Assign `OPERATED CAPABILITY=NO` only from positive evidence that settles the audited artifact
version. If positive evidence does not settle the unit, use `UNRESOLVED`. Source silence can create
only `SEARCH_PRIORITY` or `REOPEN_QUERY`; it cannot establish capability, absence, collision, or
credit.

Put proposals, future-work directions, interpretations, and hypothetical scenarios only in
`idea-provenance-ledger.csv`, with collision and credit both `NONE`. They may constrain conceptual
provenance or “first idea” wording, never realized capability, effectiveness, or contribution
novelty. Preserve an explicit author claim of realized capability without matched evidence as a
`CLAIMED_UNDEMONSTRATED` accounting row; it may also be cross-referenced as an unverified
implementation claim in idea provenance, but gains neither collision nor credit.

Decompose mixed systems channel by channel—for example user-action-to-command,
conventional-input-to-navigation, sensed-or-computed-state-to-adaptation/reward,
condition-to-gating, and system-state-to-feedback.
Reject a whole-system label unless positive evidence qualifies every required channel.

## Separate activity from implementation

Run an **activity-versus-implementation counterfactual**:

> If both systems used the same hardware, interface, and output modality, would the proposed
> contribution-level difference remain?

If not, normally treat it as an implementation or design choice. The exception is a project whose
medium or device is itself the proposed contribution and complete-source evidence demonstrates a
nontrivial reusable adaptation, a new class of use, or a directly validated empirical finding.
Frame that demonstrated change, not the device label. A zero-credit port may still collide at the
underlying operated-capability level. Headset versus earbud,
tablet versus cue matrix, visual annotation versus speech, and physical versus rendered setting
**when described only as hardware or medium** are platform substitutions, not independent novelty
claims. A physical-versus-virtual distinction becomes contribution-relevant only when evidence
shows that it changes the supported human activity—for example the participants, interdependence,
real objects, movement, timing, agency, risk, or consequences—not merely where pixels are rendered.

## Test conjunctive claims and terminology

Run a **conjunctive claim test**. Split the candidate contribution into its necessary qualifiers
and identify which close work supplies each component. The claim survives only if no verified full
copy documents the complete conjunction. Never promote one qualifier—such as “real-time,”
“personalized,” “multi-user,” “audio,” or “physical”—into a standalone novelty claim when prior
work already establishes it.

Apply the same test **symmetrically to the proposed project**. For every qualifier in the surviving
conjunction, complete all six fields independently. Keep planned or future work outside capability
and contribution credit and list unknowns explicitly. If a qualifier is claimed in an author draft
but not independently inspectable, record only `AUTHOR CLAIM`; do not upgrade demonstration,
operation, evaluation, collision, or credit.

The claim cannot be stronger than its weakest necessary qualifier. Do not infer recipient-specific
routing from separate devices alone, recipient exclusivity from intended addressing, or concurrent
delivery from participation in the same session. “Independently addressed” requires routing
evidence; “private” requires an access or audibility rule; and “simultaneous” or “concurrent”
requires overlapping-stream or timing evidence. If several cues occur during one unfolding
activity but temporal overlap is not verified, say **during the same unfolding activity** instead.

Use a precise terminology contract:

- **shared or group-wide:** recipients receive the same content through a common channel;
- **player-specific or recipient-specific:** content is directed to a particular recipient; this
  alone establishes neither different content nor exclusivity;
- **recipient-differentiated:** intended recipients can receive different content; this says
  nothing by itself about privacy, automatic selection, or an individual model;
- **role- or profile-configured:** a person explicitly selects different content using declared
  roles, levels, or other configured attributes;
- **personalizable or user-adjustable:** a person can configure a named dimension; do not extend
  that property to the whole intervention;
- **system-personalized:** the system uses a stored or inferred individual model to select support;
  state how that model is created and whether it changes; and
- **adaptive:** the system updates support from changing inferred state, behavior, or performance.

`Individualized` is an accessible umbrella only when its project-specific basis is defined at
first use. Do not use it as a catch-all. `Personalized` more strongly suggests tailoring from named
personal characteristics, preferences, history, needs, or a person model; name the basis and
selector rather than applying the label to the whole system. Do not call manually configured
differentiation automatic personalization, and do not use “private” unless access and routing have
been verified. Distinguish information that is addressed to one recipient from information that
other participants cannot hear or see.

Do not demand one winner among these terms: a concrete recipient term, an architectural contrast
term, a scoped user-control term, and a reserved overclaim can coexist in one approved hierarchy.
Use the project's author-approved terminology contract when compressing comparisons, while
preserving each prior work's own exact terminology when describing what it claims.

Shared communication can also provide mutual awareness. Treat preserved awareness, reduced
distraction, lower workload, better coordination, or better learning as design rationales or
outcome hypotheses until appropriate evidence establishes them. Record whether a
recipient-differentiated channel could hide information that collaborators need.

## Calibrate novelty assertiveness

Do not let caution about untested outcomes erase a coherent **prospective** capability hypothesis,
but do not call it a current contribution before matched demonstration. Audit four
questions separately:

1. Does the project propose a new causal interaction, control policy, or humanly meaningful state?
2. Has that capability been implemented and demonstrated?
3. Does evidence establish consequential human value or benefit?
4. Which details are supporting implementation rather than novelty-bearing?

A missing or negative answer to question 2 keeps the focal capability outside its current
contribution boundary. A missing answer to question 3 excludes the value atom without erasing a
separately claimed-and-demonstrated artifact capability. Conversely, a proposed configuration or
mechanism does not establish that it is realized, usable, effective, beneficial, or preferable.

For every surviving conjunctive claim, separate:

- **novelty-bearing causal core:** the minimum set of interdependent elements that enacts one
  distinct human intention, information flow, access policy, or interaction capability;
- **supporting implementation:** platform, exact defaults, labels, brand list, algorithms,
  calibration values, and other details that do not independently change the human capability;
- **realization evidence:** what proves the proposed capability works as specified; and
- **value evidence:** what would establish behavioral, experiential, accessibility, safety, or
  outcome significance.

Reject a brittle “first” assembled from incidental qualifiers. A conjunction can remain a
prospective capability hypothesis when removing one core element changes the encoded human
intention or control policy—for example from an event-transition policy to a usage quota, from
automatic progression to explicit mode selection, or from usable attenuation to denial. It enters
the focal project's contribution boundary only after it is explicitly claimed and demonstrated.

Treat semantic control signals as interaction structure, not mere threshold values. Session
duration, cumulative daily budget, intended clock/event transition, sensed receptivity, and
explicit mode selection encode different reasons for intervention. Compare what the system is
responding to and what state it makes possible.

Distinguish prior-work realization status:

- a claimed-and-demonstrated operated atom can receive attributed contribution credit;
- a `DEMONSTRATED_UNCLAIMED` operation can create a capability collision but receives no attributed
  contribution credit;
- a `CLAIMED_UNDEMONSTRATED` atom receives no capability or contribution credit;
- a Discussion or future-work proposal belongs only to idea provenance, with collision and credit
  both `NONE`; and
- source silence creates only search priority or a reopen query.

Before finalizing positioning, write both:

1. the strongest attributed claimed-and-demonstrated contribution statement now, scoped to the
   audited corpus, plus every separate demonstrated-unclaimed capability collision and overclaiming
   risk; and
2. the stronger empirical/value statement that becomes available only after named evidence.

Challenge both understatement and overstatement. If the synthesis lists only collisions and
fallbacks, ask whether it has conflated outcome uncertainty with capability absence. If it lists
only differences, apply the activity/implementation counterfactual, conjunctive test, current-
practice collision, and closest-work audit again.

## Rank contribution strength and proximity

Rank each meaningful comparison by the strongest defensible user-facing difference:

1. **capability:** the project would let people do something consequential the comparison does not;
2. **experience or outcome:** the capability already exists, but the project may improve a
   meaningful human outcome, experience, or performance measure; and
3. **cost or access:** comparable capability and experience exist, but the project may make them
   smaller, lighter, cheaper, easier to deploy, or more accessible.

This is an ordered contribution-strength ladder, not a classification of research methods.
Quantitative validation of a new capability does not make the contribution “experience-level,” and
a statistically significant result does not make an incremental capability novel. Record a
fallback tier when the primary distinction is contestable.

Also record **comparison proximity**. A capability-level difference from a distant analogy is much
weaker novelty evidence than the same tier from the closest same-problem/similar-approach work.
Determine comparison proximity lexicographically: problem-proximity band first, then fit to the
people/activity/context within that band, then causal-mechanism similarity, then comparator or
novelty leverage. Do not collapse these dimensions into one scalar score that lets mechanism
similarity compensate for solving a different problem.

Do not force theory, reviews, component techniques, motivation sources, exemplars, or internal
artifacts into the ladder; label them `N/A` and state what role they actually serve. If nearly every
work appears to be Tier 1, the audit has probably mistaken domain change, surface mechanism overlap,
or implementation choice for novelty. Reclassify the corpus and rescope the intended contribution
before continuing.

## Situate the work in the HCI community

Complete the native ACM DL and SIGCHI coverage protocol in
[acm-sigchi-related-work.md](acm-sigchi-related-work.md) before selecting a gap. CHI and relevant
SIGCHI-sponsored/co-sponsored work receive deliberate search priority because they establish the
HCI conversation a reviewer expects the project to acknowledge. This priority does not confer
claim strength: assess every retained result through the same source, directness, method, and
claim-specific evidence gates.

Do not reduce positioning to a list of similar systems. Synthesize:

- the established HCI problem, interaction lineage, or design space the project joins;
- the unresolved tension, tradeoff, or knowledge uncertainty exposed across the closest works;
- any idea provenance found in prior Discussion or future-work proposals, explicitly kept at
  collision and contribution credit `NONE`;
- what studying the project could teach beyond its immediate artifact or population; and
- the boundary on transfer to other HCI settings.

Credit relevant CHI/SIGCHI work positively and say whether the project replicates, extends,
contrasts, instantiates, or tests a proposition from that lineage. A broader-HCI claim must reopen
a question or transferable design tension. Use idea provenance in Discussion to show how a
demonstrated result realizes, tests, complicates, or bounds an earlier aspiration; never present
the proposal as prior capability. “This is an interface” or “no one combined these components” is
insufficient.

## Write the ranked positioning dossier

Create `ranked-related-work-positioning.md` after the bounded full-copy landscape pass and before
the author chooses a gap or primary contribution. Select up to approximately ten verified works
from the primary problem-space portfolio so the dossier is deep enough for reviewer-facing
reasoning but still forces prioritization. Rank lexicographically by:

1. `SAME-SPECIFIC-PROBLEM` before `SIMILAR-PROBLEM`;
2. match to the target people, activity, and triggering or temporal context within that band;
3. similarity of the causal interaction mechanism, including access state and progression
   variable;
4. leverage over the claimed gap or novelty boundary; and
5. value as a fair empirical or design comparator.

Do not include venue prestige, recency alone, or evidence strength as a hidden relevance score.
Evidence strength still bounds what a paragraph may say. A work in an adjacent or different
problem band cannot displace a same/similar-problem work because it shares a mechanism or sounds
conceptually similar. If fewer than approximately ten verified same/similar-problem works exist,
include all of them, disclose the shortage and residual search risk, and **do not pad** the primary
ranking with distant analogies. State ties or conditional ordering when unfinished project choices
could change the ranking.

Write one full working paragraph per ranked work. Each paragraph must credit the predecessor's
claimed-and-demonstrated contribution, separately state any demonstrated-unclaimed capability
collision, state the material evidence boundary, name one literal consequential difference, say
what the project inherits, characterize the relationship as
replication, extension, contrast, instantiation, or a test, and end with the safe positioning
boundary. Keep demonstrated-unclaimed operated capabilities and overclaiming risks in the internal
record and surface them when they materially constrain firstness or comparator choice. Route proposals to
idea provenance for later Discussion. Do not turn a limitation list into the contrast, and do not
imply the planned project already works. These paragraphs are research artifacts that can later
support a Related Work section; they are not final manuscript prose.

Write a separate claim-specific note for each material item in the
mechanism/capability-collision portfolio: state the different problem, exact mechanism/capability
collision supported by demonstrated operation, whether it was author-claimed, its contribution-
credit disposition, the claim narrowed or retired, and what remains project-specific. Retain
ideas, proposals,
theory, foundations, reviews, secondary comparators, and rank-sensitive alternatives in their
named inventories. Re-rank when the target-problem identity, population, activity, mechanism,
access state, progression variable, user control, contribution layer, source completeness, or
closest-work set changes.

## Produce the audit

Create `related-work-contribution-tier-audit.md` covering every catalogued reference. For each
applicable work:

- record its relationship class and proximity;
- record its problem-proximity band and portfolio assignment before mechanism similarity;
- atomize each material proposition into the six independent accounting fields;
- use positively operated capability for collision and claimed-plus-demonstrated evidence for
  contribution attribution;
- record `DEMONSTRATED_UNCLAIMED` operations as collisions/risks with contribution credit `NONE`;
- record `CLAIMED_UNDEMONSTRATED` atoms with both collision and credit `NONE`;
- assign operated capability `NO` only from positive artifact evidence; route silence only to
  search priority or a reopen query;
- preserve proposals in the idea-provenance ledger with collision and credit both `NONE`;
- decompose mixed channels and reject unsupported whole-system labels;
- apply the demonstrated port/adaptation credit gate;
- compare the relevant dimensions and existing-workflow relationship;
- report the current-practice collision check and communication structure;
- run the activity-versus-implementation counterfactual and conjunctive claim test;
- separate and rank workflow significance, interaction or information-distribution capability,
  setting/activity boundary, implementation/design rationale, and untested outcome hypothesis;
- give the most concise significant difference;
- identify what the project learns or inherits;
- state the evidence boundary, tag evidence, capability/overclaim risks, idea-lineage role, and
  unresolved source question;
- list an unsafe claim to avoid and lower-tier fallback; and
- specify a fair future comparator that preserves valued current practice.

Include every non-comparator in a completeness inventory with its real role so references do not
silently disappear.

Cross-reference `acm-sigchi-related-work-audit.md`, including its native ACM queries, explicit
CHI/SIGCHI inclusion/exclusion decisions, independent contribution-boundary tags,
capability/overclaim risks, idea-lineage distinctions, citation-chain saturation, and broader-HCI
situating synthesis. The contribution audit cannot be complete while that coverage gate remains
open.
