# Phase 1 constructive reviewer panel

Use multiple lenses to improve the research direction, not to imitate a final-paper review or
manufacture consensus. The project may have no design, system, study, or results yet.

## Review bundle and independence

Freeze one read-only bundle:

- starting-state inventory and supplied project materials;
- motivation evidence map and claim-evidence ledger;
- source manifest, search log, citation-chain log, and full copies;
- related-work matrix and quadrant variations;
- problem, gap, approach, contribution, and lexical-spine option packets;
- author decision log;
- research framing outline; and
- draft Phase 2 handoff.

Record paths or hashes in `frozen-artifacts.md`. Give every reviewer the same bundle plus one lens.
Do not share reviewer outputs until all reviews finish. Reviewers make no edits, commits, source
uploads, participant contact, implementation, or invented analyses.

Missing later-phase work is not a finding by itself. A reviewer may identify an uncertainty and
recommend the smallest later-phase investigation that resolves it.

## Seven lenses

### 1. Domain-expert HCI researcher

Assess whether the people, activity, pain, current practice, consequence, terminology, and
constraints are faithful to the domain. Check whether authoritative domain evidence, closest
research, products, and practices are present. Identify what the project should learn from, build
on, or preserve from each closest work. Check whether a claimed new workflow stage collides with
existing human intervention through speech, gesture, demonstration, coordination, or another
workaround. Verify the sender-recipient, content-distribution, concurrency, visibility, and
selection-provenance account. Recommend practitioner or field evidence only where a specific
assumption remains consequential.

### 2. HCI researcher outside the domain

Assess whether a broad CHI reader can understand why this human problem matters, why now, what
existing work enables, the gap hypothesis, intended experience, and broader HCI promise. Identify
jargon, hidden assumptions, inflated generality, and an empirical waist too narrow to support the
claimed field-level value.

### 3. Technical HCI systems researcher

Assess whether the proposed technical mechanism could plausibly create the intended experience.
Identify capability dependencies, difficult failure modes, sensing/computation/output bottlenecks,
latency or reliability thresholds, safety/privacy risks, and the smallest technical probes Phase 2
needs. Do not demand production architecture, exhaustive optimization, or performance results from
an unbuilt system.

### 4. Designer

Assess whether the proposed experience follows from real needs and practice rather than technology
enthusiasm. Identify stakeholders, tensions, agency/control questions, accessibility, inclusion,
ethics, breakdown/recovery, and meaningful alternative concepts. Recommend formative activities
that would discriminate among approaches. For differentiated channels, examine what shared
information and mutual awareness might be lost as well as what recipient relevance might be gained;
do not prescribe a polished interface.

### 5. Quantitative-methods researcher

Assess whether the motivating quantitative claims are interpreted according to their sampling,
constructs, methods, uncertainty, and causal limits. For prospective claims, identify estimands,
comparators, units, measures, and feasibility questions that Phase 3 will eventually need—at the
level necessary to judge researchability, not a finalized statistical analysis plan.

### 6. Qualitative-methods researcher

Assess what remains unknown about experience, practice, mechanism, stakeholders, and context.
Check whether existing qualitative evidence supports the claimed kind of knowledge. Recommend
formative or future qualitative inquiry, sampling logic, and contexts that could challenge the
premise; do not nitpick coding procedures for a study that has not been designed.

### 7. Academic researcher and popular-science communicator

Assess whether the research outline has a compelling and honest conceptual arc:

`larger concern → specific pain → evidence → state of the art → gap → approach hypothesis →
prospective contribution → broader HCI value`

Test whether a non-specialist can restate the direction accurately and remember its central idea.
Check that familiar terms lead and exact scientific or technical constructs are defined at first
use. Check that every approach, feature, control, and contribution is introduced through the human
situation and value it serves before the mechanism or implementation, and that an intended value
is not presented as a measured benefit. Distinguish a material claim-local qualifier from a
nonresponsive disclaimer about an outcome the project does not claim. Recommend clearer concepts,
examples, and terminology—not final paragraphs or rhetorical polish.

## Required reviewer output

Each reviewer writes:

1. **Restatement:** problem, gap, approach, and prospective contribution in one or two sentences.
2. **Strengths to preserve:** two to four specific assets of the direction.
3. **Highest-leverage uncertainties:** three to seven findings, each with:
   - stable ID;
   - priority: `direction-blocking`, `important`, or `later-phase`;
   - confidence;
   - exact artifact/location;
   - reasoning and evidence;
   - smallest resolving action;
   - phase responsible: `1`, `2`, or `3`; and
   - what result would change the framing.
4. **Best defensible direction:** strongest current problem-gap-approach-contribution package.
5. **Premise challenge:** strongest reason not to invest in this direction.
6. **Opportunity:** a concrete way the work could become more significant without unsupported
   scope expansion.
7. **Uncertainty/conflicts:** context missing from the bundle or likely tension with another lens.

Avoid sentence-level edits unless terminology itself changes the research claim.

## Synthesis

After all seven reviews are frozen, create `synthesis.md`:

- reviewed bundle and independence statement;
- finding matrix keyed by reviewer and ID;
- grouped causal themes without erasing minority concerns;
- disposition: `revise-phase-1`, `plan-phase-2`, `plan-phase-3`, `accept-risk`, or `reject`;
- evidence-grounded rationale;
- smallest action, owner, and return condition;
- conflicts needing author choice; and
- readiness recommendation.

Review lenses advise; they do not outvote evidence or replace the author. A domain expert cannot
waive a validity problem, a methods expert cannot redefine lived practice, a systems reviewer
cannot make the technology the contribution, and a communicator cannot simplify away an evidence
boundary.
