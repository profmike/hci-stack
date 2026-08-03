# Terminology contract

Terminology is part of research validity. A loaded adjective can silently add an unsupported
claim about recipients, tailoring, automation, privacy, timing, or outcomes. Phase 1 therefore
defines meanings before it optimizes wording.

## Separate semantics from rhetoric

Maintain two linked artifacts:

1. The **terminology contract** is the semantic contract: it records the concepts, operational
   meanings, evidence boundaries, non-implications, and permitted or reserved terms.
2. The **lexical spine** assigns approved terms to recurring rhetorical jobs in the outline,
   figures, later paper sections, and video.

Do not choose the lexical spine first and retrofit meanings around attractive wording. A term can
be accurate in one sentence and misleading as a label for the whole system.

## Lead familiar, then define precisely

For a general HCI or public-facing audience, use an accessible entry term before introducing the
scientific or technical construct. Define the exact construct or metric at first use, then choose
an approved short form for later sentences.

The accessible and scientific terms do different work. The accessible term provides orientation;
the precise term fixes the operational meaning. For example, introduce `blue light` before
defining the cited study's `short-wavelength spectral output` or melanopic metric. Do not treat
those constructs as interchangeable, and do not let the familiar term broaden the evidence.

## Decompose the claim

Before comparing candidate words, map each relevant dimension independently:

| Dimension | Question |
|---|---|
| People and activity | Who is acting, in what task, and with what interdependence? |
| Addressee | Is content directed to a group, role, device, named person, or inferred profile? |
| Content relationship | Do recipients receive the same content or can they receive different content? |
| Selection provenance | Who authors, selects, configures, or infers the content? |
| Tailoring basis | Which declared role, experience, preference, history, behavior, or state affects it? |
| User control | What exact dimension can a person adjust? |
| Adaptation | Does support change from evolving sensed or inferred state, behavior, or performance? |
| Timing | Is delivery before, during, or after action; are streams serialized or overlapping? |
| Access | Who can actually hear, see, retrieve, or inspect the content? |
| Outcome | What capability is implemented, and which experience or performance effects remain hypotheses? |

Do not compress these dimensions into one adjective. Apply the same evidence test to the proposed
project and to each closest work.

## Common loaded terms

Use the narrowest supported term. Domain-specific equivalents may be better when they are clear to
both practitioners and broad HCI readers.

| Term | Operational meaning | Does not establish by itself |
|---|---|---|
| `group-wide` or `team-wide` | A common item is addressed or made available to the group. | That every person attended to, understood, or benefited from it. |
| `player-specific` or `recipient-specific` | An item is directed to a particular player or recipient. | That another recipient cannot access it, that the content differs, or that a model selected it. |
| `recipient-differentiated` | Intended recipients can receive different content. | Privacy, individual modeling, automatic selection, adaptation, or simultaneous delivery. |
| `individualized delivery` | The system provides distinct recipient channels so content can be delivered separately to individuals. | Different content, recipient exclusivity, personalization, adaptation, or concurrency. Routing evidence is required. |
| `individualized` | An umbrella term whose project-specific basis must be defined at first use. | Automatic inference or adaptation. Prefer a more concrete term when possible. |
| `personalizable` or `user-adjustable` | A person can configure a named dimension. | That the entire intervention is personalized or that the chosen setting is beneficial. |
| `personalized` | Content is tailored using named personal characteristics, preferences, history, needs, or a person model. | Automatic adaptation unless the updating mechanism is established. Always name the tailoring basis and selector. |
| `adaptive` | The system changes support from evolving sensed or inferred state, behavior, or performance. | Correct diagnosis, useful adaptation, or improved outcomes. Name the signal, rule/model, and timescale. |
| `independently addressed` | Routing evidence shows that content can be directed separately to selected recipients. | Recipient exclusivity, privacy, or temporal overlap. |
| `recipient-exclusive` | An operational access or audibility rule limits the content to the selected recipient. | Confidentiality, security, or privacy in the broader data-protection sense. |
| `concurrent` or `simultaneous` | Verified streams or events overlap according to an explicit timing criterion. | Low latency, responsiveness, or real-time performance. |
| `real-time` | A measured end-to-end latency and reliability requirement is met for the target activity. | Concurrency or adaptation. Use a concrete activity phrase until measured. |
| `intention-anchored` | A named user-entered or otherwise established intention is the configuration object or selector for the policy. | That the intention is accurate, stable, strong, well understood, or better than another anchor. |
| `intention-aligned` | Direct evidence shows that the policy, use, or outcome matches the person's stated intention under a defined criterion. | Alignment merely because the system stores a target or schedule. Prefer `intention-anchored` before validation. |
| `anticipatory` | A policy begins before a named target event or transition. | Gradualness, lower cumulative exposure, benefit, or a separately identified anticipatory effect. |
| `attenuated access` or `attenuated continuation` | Access remains technically available while named operational parameters are changed. | Reduced harm, better quality, preserved task success, agency, accessibility, or acceptability. |
| `operational exposure` | An instrumented quantity delivered by the system, such as luminance, content throughput, latency, or interruptions. | The person's perception, physiology, experience, or downstream outcome. |
| `stimulation` | A reserved umbrella that must be decomposed into a measured visual, content, interaction, subjective, physiological, or other construct. | That changing display or delivery settings changes arousal, reward, or sleep. |
| `reduced impact` | Outcome-bearing language permitted only when the named impact and comparison are directly measured. | A structural synonym for attenuation, friction, delay, dimming, or reduced throughput. |

For example, **player-specific guidance** can be the default concrete description of who receives
a cue; **recipient-differentiated guidance** can describe the communication transition;
**player-adjustable detail** can name one configurable dimension; and **personalized coaching** can
remain reserved. These phrases perform different jobs and should not be treated as synonyms.

## Present terminology systems for author choice

Offer three to five coherent systems rather than five isolated synonyms. Each system must specify:

- its concrete default term;
- its structural or comparative term;
- any familiar entry term, the precise construct it introduces, and their first-use definition;
- the approved short form after that definition;
- any narrowly scoped tailoring, user-control, timing, or access term;
- reserved or forbidden terms;
- likely reader inference;
- evidence and status;
- what the system foregrounds and compresses; and
- where the system would first be defined.

At least one option should optimize domain naturalness, one broad-CHI clarity, and one
system/evidence precision when all are defensible. Recommend an option, but ask the author to
choose, combine named parts, reject the set, or delegate. Record the semantic-contract decision
separately from the lexical-spine decision.

## Propagate without semantic drift

After author approval, propagate the selected hierarchy through:

- problem and motivation framing;
- related-work classifications and comparison sentences;
- gap and contribution packages;
- approach and system descriptions;
- chart axes, figure labels, and captions;
- future Abstract, Introduction, Related Work, method, study conditions, measures, results, and
  Discussion;
- Phase 2 and Phase 3 plans; and
- the Phase 2 handoff.

Lead with a familiar term when it helps the target audience, define the exact scientific or
technical construct at first use, and use an allowed short form only after that definition.
Do not vary terms merely for stylistic elegance when the variation changes the implied mechanism
or evidence. Preserve exact technical terms when describing a prior work, even if the project uses
different terms for itself.

## Audit and reopen

Before a Phase 1 readiness decision:

1. search artifacts and generated reports for every selected, allowed, reserved, and superseded
   term;
2. inspect each loaded occurrence in context;
3. confirm that the first use supplies the operational definition;
4. check that figures, captions, study conditions, and contribution wording use the same meanings;
5. mark intentional quotations or descriptions of prior work so they are not mistaken for project
   claims; and
6. record unresolved conflicts and propagation status in `terminology-contract.md`.

Reopen the contract when a system trace changes what is implemented, formative work changes the
domain language, a study operationalizes a term differently, a closer work narrows the distinction,
or an author chooses a different contribution emphasis. Never erase the prior definition; mark it
superseded and record why.
