# HCI research contribution types

Use this reference when a project moves from comparing prior work to formulating a prospective
contribution package. It distills Jacob O. Wobbrock and Julie A. Kientz,
[“Research Contributions in Human-Computer Interaction”](https://interactions.acm.org/archive/view/may-june-2016/research-contribution-in-human-computer-interaction),
*Interactions* 23(3), 2016, DOI [10.1145/2907069](https://doi.org/10.1145/2907069), using the
[complete paper](https://faculty.washington.edu/wobbrock/pubs/interactions-16.pdf).

## The unit of analysis

The paper’s central distinction is that a contribution is the reusable knowledge produced or
advanced by the work, not automatically the method used, the artifact built, the data collected,
or a section heading. One paper may make more than one contribution. For each candidate, name a
primary type, any supporting types, the reusable output, and the evidence that would establish it.
Do not let a compelling implementation or study method silently stand in for the knowledge or
capability it is meant to produce.

## Seven knowledge-oriented types

| Type | Reusable output | Type-specific evaluation contract |
| --- | --- | --- |
| **Empirical knowledge** | Findings about people, interaction, practice, or outcomes, from qualitative or quantitative observation and data. | Are the findings important, and are the methods sound, precise, and appropriately bounded? |
| **Artifact** | A system, architecture, tool, toolkit, technique, sketch, mockup, or envisionment that opens a meaningful possibility. | Evaluate the artifact by subtype: systems/tools holistically by what they make possible and how; techniques precisely and quantitatively for human performance; design expressions by insight, compelling portrayal, innovation, and trade-offs. |
| **Methodological knowledge** | A new or improved way to discover, measure, analyze, create, build, or evaluate. | Is it useful, reproducible, reliable, and valid? Repeated validation is normally needed to establish those properties. |
| **Theoretical knowledge** | A concept, definition, model, principle, framework, or explanatory lens that says what to expect and why. | Is it novel and sound, and does it describe, predict, or explain without becoming so narrow or broad that it has little power? It should be testable/falsifiable and is usually validated empirically. |
| **Dataset** | A useful, representative corpus or benchmark that lets the community test, measure, or compare. | Are provenance, gathering/creation procedures, representativeness, documentation, access, and intended reuse clear? |
| **Survey/meta-analysis** | An organized synthesis that exposes the state of a mature topic, trends, gaps, and research opportunities. | Is it complete, deep, mature, well organized, and genuinely synthetic rather than a bibliography or laundry list? |
| **Opinion/argument** | A research-grounded position intended to change minds, provoke reflection, or redirect practice. | Is the argument strong, supported by credible evidence, fair to opposing perspectives, broadly interesting, and accessible? |

These types are not a quality ranking. Their standards differ. A dataset does not become a strong
dataset contribution merely because an analysis accompanies it; an artifact does not become an
empirical contribution merely because it was user-tested; and an opinion contribution is not
research-free simply because persuasion is its goal.

## Mapping to CHI submission labels

The paper reports that CHI 2016 exposed eight labels by splitting empirical work into two labels:

- “Empirical study that tells us about how people use a system” → **empirical knowledge**
- “Empirical study that tells us about people” → **empirical knowledge**
- “Artifact or system” → **artifact**
- “Method” → **methodological knowledge**
- “Theory” → **theoretical knowledge**
- “Dataset” → **dataset**
- “Meta-analysis / literature survey” → **survey/meta-analysis**
- “Essay / argument” → **opinion/argument**

Keep the split when it clarifies the empirical object, but map it back to the seven-type knowledge
taxonomy when writing the contribution package. The skill’s additional labels—design knowledge and
open resource—are useful HCI packaging categories, not reasons to erase the paper’s dataset,
survey, or opinion distinctions. Record the relationship explicitly.

## Phase 1 protocol: identify, frame, classify, and align evidence

Run these four passes before presenting contribution-package options. Do not jump from a list of
project components to polished contribution prose.

### 1. Identify atomic reusable outputs

For every candidate, ask: **What could the HCI community newly know, do, inspect, reuse, compare,
or debate because of this work?** Record one answer per candidate. Separate the research activity
from its prospective output:

- building a system may yield an **artifact** contribution when the system embodies and explains a
  meaningful new possibility; merely building it is not the claim;
- running a user study may yield **empirical knowledge** when an important finding is itself
  claimed; evaluation alone does not create a second contribution;
- using interviews, experiments, or co-design does not create **methodological knowledge** unless
  the way of conducting research or design is itself new or improved and validated;
- collecting study data does not create a **dataset** contribution unless a useful,
  representative, documented, and reusable corpus is being offered;
- organizing Related Work does not create a **survey/meta-analysis** contribution unless the
  synthesis is sufficiently complete, deep, mature, and generative; and
- design implications or a conceptual diagram do not automatically create **theoretical
  knowledge** unless the concept, model, principle, or framework carries explanatory or predictive
  power and can be tested.

Atomize mixed candidates. Apply the null-survival test: if a hoped-for outcome is null,
heterogeneous, worse, or burdensome, state exactly which reusable output would remain. If nothing
survives, the candidate is currently an outcome hypothesis, not a contribution.

### 2. Frame the value, reusable output, and difference

Lead with why people or the HCI community would value the candidate, then name the reusable output
and necessary mechanism. A Phase 1 candidate should answer, in plain language:

1. Who faces what consequential situation, and what value could the work create for them?
2. What reusable capability or knowledge is proposed?
3. What is the closest prior reusable output, and what exact supported difference remains?
4. Why might the result matter beyond the project’s empirical waist or example domain?
5. What is established now, what is prospective, and what remains explicitly unclaimed?

Use this internal scaffold, not as mandatory final prose: **For [people/situation], we aim to
[human value] by contributing [reusable capability or knowledge]. Relative to [closest work], the
exact difference is [supported delta]. We classify it primarily as [type], with [supporting type]
only if separately claimed, because [reason]. It currently has [evidence state] and requires
[type-specific evidence].** Generate three to five coherent package variations for author choice;
do not finalize the lexical spine or contribution wording without that choice.

### 3. Classify the output, not the work activity

Choose the primary type by the reusable output that carries the central novelty and would organize
the paper’s main claim—not by the most expensive task, longest section, preferred method, or most
visually distinctive artifact. Use this diagnostic:

- important observation or finding → **empirical knowledge**;
- constructed interactive possibility → **artifact**;
- reusable way of discovering, measuring, analyzing, creating, or evaluating →
  **methodological knowledge**;
- explanatory or predictive concept, model, principle, or framework → **theoretical knowledge**;
- reusable corpus or benchmark → **dataset**;
- mature synthesis of a body of research → **survey/meta-analysis**; and
- evidence-grounded position intended to persuade or redirect the field → **opinion/argument**.

Record any supporting types only when each has an independent claim and evidence gate. Also record
the strongest rejected alternative classification and why it does not fit. The skill’s primary/supporting
designation is a framing convention for decision clarity; it does not imply that Wobbrock and
Kientz require every paper to have exactly one type. Types are not quality ranks.

### 4. Align each type with evidence and later phases

Maintain one contribution-candidate register across the live workboard, decision packet, research
outline, reports, and handoff. Every row must contain:

| Field | Required content |
| --- | --- |
| Candidate ID | Stable ID retained through selection, rejection, supersession, and reopening. |
| Benefit-first candidate | Human value first, then the reusable output and necessary mechanism. |
| Reusable output | The exact knowledge, capability, artifact possibility, method, theory, corpus, synthesis, or argument offered to HCI. |
| Primary type | One primary type for framing clarity, selected by the central reusable output. |
| Supporting type(s) | Optional supporting types, each with an independent claim and evidence gate. |
| Classification rationale | Why the primary type fits and why the strongest rejected alternative was not selected. |
| Closest prior output and exact delta | The nearest contribution-relevant work and the precise evidence-supported difference. |
| Evidence state | `established`, `observed`, `planned`, `hypothesis`, `aspiration`, or `needs evidence`. |
| Type-specific evidence gate | The exact standard above and the later research, build, study, synthesis, or argument needed to meet it. |
| Null-result survivor | What remains reusable if the preferred outcome fails; otherwise `none—outcome hypothesis only`. |
| Status and reopen trigger | `candidate`, `decision-ready`, `selected-primary`, `selected-supporting`, `rejected`, `blocked`, or `reopened`, plus what would change it. |

Separate rationale from result. Intended value, design insight, or a persuasive position is not a
measured benefit. Never upgrade a prospective claim because its type has been named. If the
reusable output, closest-work difference, or type-specific evidence path cannot yet be stated,
mark the candidate `blocked` or `needs evidence` and research, narrow, or reject it before framing
it more strongly.
