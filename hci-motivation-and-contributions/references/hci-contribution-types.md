# HCI research contribution types

From Jacob O. Wobbrock and Julie A. Kientz,
[“Research Contributions in Human-Computer Interaction”](https://interactions.acm.org/archive/view/may-june-2016/research-contribution-in-human-computer-interaction),
*Interactions* 23(3), 2016, DOI [10.1145/2907069](https://doi.org/10.1145/2907069)
([complete paper](https://faculty.washington.edu/wobbrock/pubs/interactions-16.pdf)).

A contribution is the reusable knowledge the work produces, not automatically the method, artifact,
data, or a section heading; one paper may make several.

## Seven knowledge-oriented types

| Type | Reusable output | Type-specific evaluation contract |
| --- | --- | --- |
| **Empirical knowledge** | Findings about people, interaction, practice, or outcomes. | Findings important; methods sound, precise, bounded. |
| **Artifact** | A system, tool, toolkit, technique, sketch, mockup, or envisionment opening a possibility. | Systems and tools by what they make possible and how; techniques quantitatively for human performance; design expressions by insight, portrayal, innovation, trade-offs. |
| **Methodological knowledge** | A new or improved way to discover, measure, analyze, build, or evaluate. | Useful, reproducible, reliable, valid; repeated validation is normally needed. |
| **Theoretical knowledge** | A concept, definition, model, principle, framework, or explanatory lens. | Novel and sound; describes, predicts, or explains without being so narrow or broad it has little power. Should be testable/falsifiable; usually validated empirically. |
| **Dataset** | A representative corpus or benchmark letting the community test, measure, or compare. | Provenance, gathering, representativeness, documentation, access, intended reuse all clear. |
| **Survey/meta-analysis** | An organized synthesis exposing the state of a mature topic, trends, gaps. | Complete, deep, well organized, synthetic rather than a bibliography. |
| **Opinion/argument** | A research-grounded position meant to change minds or redirect practice. | Strong, evidence-supported, fair to opposing views, broadly interesting, accessible. |

Not a quality ranking: an artifact does not become an empirical contribution because it was
user-tested, nor is an opinion contribution research-free because it persuades.

## Mapping to CHI submission labels

CHI 2016’s eight labels split empirical work into studies of system use and studies of people; both
map to **empirical knowledge**, the other six one-to-one. Keep the split when it clarifies the
empirical object; record the mapping back to the seven types. Design knowledge and open resource
never erase the dataset, survey, or opinion distinctions.

## Phase 1 protocol: identify, frame, classify, align evidence

**Identify atomic reusable outputs.** Ask: **What could the HCI community newly know, do, inspect,
reuse, compare, or debate because of this work?** One answer per candidate, activity separate from
output: building a system yields an **artifact** only if it opens a possibility;
running a user study yields **empirical knowledge** only if the finding is itself claimed;
using interviews or co-design yields **methodological knowledge** only if the method is new,
improved, and validated;
collecting study data yields a **dataset** only if the corpus is representative, documented, and
reusable; organizing Related Work yields a **survey/meta-analysis** only if the synthesis is complete,
deep, and generative; a diagram yields **theoretical knowledge** only if the concept carries testable
explanatory power. Atomize mixed candidates. Null-survival test: if the outcome is null,
heterogeneous, worse, or burdensome, state which reusable output remains; if none, it is an outcome
hypothesis, not a contribution.

**Frame, then classify.** Frame each candidate in the register's field order below, human value before
mechanism — an internal scaffold, not final prose.
Choose the primary type by the reusable output carrying the central
novelty, not the most expensive task, longest section, or preferred method.
Record supporting types only when each has an independent claim and evidence gate, plus the strongest
rejected alternative and why it does not fit. Primary/supporting is a convention; Wobbrock and Kientz do not
require one type per paper.

**Align each type with evidence.** Keep one contribution-candidate register across the live
workboard, decision packet, research outline, reports, and handoff. Every row:

| Field | Required content |
| --- | --- |
| Candidate ID | Stable through selection, rejection, supersession, reopen. |
| Benefit-first candidate | Human value, then reusable output and mechanism. |
| Reusable output | Exact knowledge, capability, artifact possibility, method, theory, corpus, synthesis, or argument. |
| Primary type | One, by the central reusable output. |
| Supporting type(s) | Optional; each needs its own claim and gate. |
| Classification rationale | Why it fits and the strongest rejected alternative does not. |
| Closest prior output and exact delta | Nearest contribution-relevant work; the supported delta. |
| Evidence state | `established`, `observed`, `planned`, `hypothesis`, `aspiration`, `needs evidence`. |
| Type-specific evidence gate | The type's standard and work needed to meet it. |
| Null-result survivor | What stays reusable if the outcome fails, else `none—outcome hypothesis only`. |
| Status and reopen trigger | `candidate`, `decision-ready`, `selected-primary`, `selected-supporting`, `rejected`, `blocked`, `reopened`, plus what changes it. |

Intended value or design insight is not a measured benefit, and naming a type never upgrades a
prospective claim. If the reusable output, closest-work difference, or evidence path cannot yet be
stated, mark the candidate `blocked` or `needs evidence` and research or narrow it.
