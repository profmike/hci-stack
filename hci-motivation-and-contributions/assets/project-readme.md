# {{PROJECT_NAME}}

This private project repository contains the evidence, decisions, and research framing developed
with the `hci-motivation-and-contributions` workflow.

<!-- HCI-PLAIN-LANGUAGE: ISO 24495-1:2023 | audience=HCI researchers and project collaborators | tasks=understand the direction; inspect evidence; review decisions; continue to Phase 2 -->

## At a glance

**Status: `unsupported` pending project-specific research.** State the target people, activity,
context, unwanted state or episode, intended change, and current decision or next action here. Lead
with the answer readers need; keep the checked evidence and exact claim boundaries in the linked
[research framing outline](research-framing/research-framing-outline.md).

## The user value

**Evidence state: `hypothesis`.** Describe the specific people, transition or activity, and value the
project aims to support before naming the mechanism. Link the exact evidence boundary in the
[research framing outline](research-framing/research-framing-outline.md). State the motivation and
user value declaratively; do not ask readers to endorse that people `should` receive a benefit.

## Introduction — structure and outline

This is an argument outline, not polished manuscript prose. Use this move order:

1. **Concrete behavior and consequence:** state who does what in the focal context, how it disrupts
   the focal activity or intended transition, the proximal outcome, and only separately supported
   downstream stakes.
2. **Why the focal context differs from the general intervention target:** synthesize the general
   intervention landscape, then identify the distinct timing, goal, configuration object, or
   behavioral problem without claiming untested superiority.
3. **Prior approaches and measured limits:** summarize user-enacted and technical approaches, then
   report only directly measured adherence, override, abandonment, burden, or substitution limits.
4. **Outcome-oriented approach and mechanisms:** state the human outcome first, then the
   platform-independent approach, inherited rationale, mechanisms, implementation substrate, and
   any demonstrated adaptation credit. For graded interventions, state each channel's full range
   and whether its endpoint preserves or denies access. Label unmeasured psychological explanations
   as hypotheses.
5. **Newly enabled investigation:** name the comparison, common controls, and behavioral or
   experiential outcomes that the capability makes observable.
6. **Study and contribution statement:** use `We conducted` only for a completed, verified study;
   otherwise use planned-study language and keep contributions prospective.

Open with the concrete finding, not a label such as `a serious human problem`. Write conclusion-level
synthesis rather than study-by-study detail. Put each citation immediately after the smallest claim
or keyword it supports. Repeat a work wherever it supports another atom, cite each independently
supported item in an enumeration, and split clusters as finely as the evidence permits. A cluster
has no numeric cap only when every work supports the same indivisible atom. Keep generic review
disclaimers in the internal evidence record; retain a claim-local qualifier when removing it would
change the statement's truth, scope, causal meaning, or likely interpretation.

State explicitly:

- **Approach invariant:**
- **Essential interaction/control-policy dimensions:**
- **Implementation substrate / empirical waist:**
- **Platform-substitution result:**
- **Adaptation-credit disposition:**

## Closest prior work

When the framing cites prior work, add one compact bullet per work using the exact structure
`citation — **What it did:** evidence-bounded description. **How this project differs:** literal
difference.` Do not leave citations as unexplained mechanism labels.

## Planned approach

**Status: `planned`.** Summarize the human situation and intended value first, then the planned
platform-independent approach, essential dimensions, and only then the implementation substrate.
State the substitution result and whether any platform adaptation independently earns credit. Link the selected approach
and rejected alternatives in the [collaboration workboard](research-framing/phase-1-collaboration-workboard.md)
and [author decisions](research-framing/author-decisions.md).

## Prospective contributions

**Status: `hypothesis`.** List the leading stable contribution-candidate IDs, primary/supporting
types, closest-work delta, evidence gate, and null-result survivor. These statements remain
prospective until the linked evidence gates are met. See the
[research framing outline](research-framing/research-framing-outline.md) and
[Phase 2 handoff](research-framing/phase-2-handoff.md).

## Current status

Phase 1 is active. The [live workboard](research-framing/phase-1-collaboration-workboard.md) is the
authoritative record of readiness, blockers, active decisions, recommendation, next action/owner,
and reopen triggers.

## Continue by task

### Understand the direction

- [Live Phase 1 workboard](research-framing/phase-1-collaboration-workboard.md)
- [Research framing outline](research-framing/research-framing-outline.md)
- [Ranked related-work positioning](research-framing/ranked-related-work-positioning.md)

### Inspect evidence

- [Evidence-strength register](research-framing/evidence-strength-register.md)
- [Literature and evidence](research-framing/reports/literature-and-evidence.md)
- [Source manifest](research-framing/source-manifest.md)
- [Citation identity registry](research-framing/references.csv)

### Review decisions

- [Author decisions](research-framing/author-decisions.md)
- [Decision packets](research-framing/decision-packets/README.md)

### Continue to Phase 2 or inspect the complete record

- [Phase 2 handoff](research-framing/phase-2-handoff.md)
- [GitHub Markdown report shelf](research-framing/reports/README.md)
- [Phase 1 progress](research-framing/reports/phase-1-progress.md)
- [Phase 1 research direction](research-framing/reports/phase-1-final.md)
- [Complete artifact index](research-framing/reports/artifact-index.md)

## Record boundary

The root README is a bounded overview, not a second evidence or decision source. Canonical Markdown,
CSV, JSON, and YAML records under `research-framing/` remain authoritative and diffable. The
publisher maintains relative navigation, keyed citation links, visible references, ledger views,
and source-hash provenance; fix substantive content in the canonical record and republish. This
overview uses [ISO 24495-1:2023](https://www.iso.org/standard/78907.html) as its plain-language
profile for the declared readers and tasks.
