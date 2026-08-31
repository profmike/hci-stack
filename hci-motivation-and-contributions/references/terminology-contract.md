# Terminology contract

A loaded adjective silently adds an unsupported claim about recipients, tailoring, automation,
privacy, timing, or outcomes.

## Separate semantics from rhetoric

The **terminology contract** is the semantic contract: operational meanings, evidence boundaries,
non-implications, and permitted or reserved terms. The **lexical spine** assigns approved terms to
recurring rhetorical jobs. Never choose the lexical spine first and retrofit meanings around
attractive wording. Apply the familiar-to-precise terminology rule of
[claim-focused-writing.md](claim-focused-writing.md); a broad reader must be able to restate the
people, activity, and value without the precise label.

## Decompose the claim

Map each dimension independently, for the project and each closest work.

| Dimension | Question |
|---|---|
| People and activity | Who acts, in what task, with what interdependence? |
| Addressee | Group, role, device, named person, or inferred profile? |
| Content relationship | Same content for all, or possibly different? |
| Selection provenance | Who authors, selects, or infers it? |
| Tailoring basis | Which role, preference, history, or state affects it? |
| User control | What dimension can a person adjust? |
| Adaptation | Does support change from evolving sensed state? |
| Timing | Before, during, or after action; serialized or overlapping? |
| Access | Who can actually hear, see, or inspect it? |
| Outcome | What is implemented, and which effects remain hypotheses? |

## Common loaded terms

Use the narrowest supported term.

| Term | Operational meaning | Does not establish |
|---|---|---|
| `player-specific` or `recipient-specific` | Directed to one player. | Inaccessibility, differing content, model-based selection. |
| `recipient-differentiated` | Recipients may receive different content. | Privacy, modeling, automatic selection, simultaneity. |
| `individualized delivery` | Distinct channels; needs routing evidence. | Different content, exclusivity, personalization. |
| `individualized` | Umbrella; define the basis at first use. | Inference or adaptation. |
| `personalizable` or `user-adjustable` | A person can configure a named dimension. | That the intervention is personalized. |
| `personalized` | Tailored using named characteristics or a person model. | Automatic adaptation. Name the basis. |
| `adaptive` | Support changes from evolving sensed state. | Correct diagnosis, useful adaptation, improved outcomes. Name signal and timescale. |
| `independently addressed` | Routing evidence shows separate direction. | Exclusivity, privacy, temporal overlap. |
| `recipient-exclusive` | An access rule limits content to that recipient. | Confidentiality, security, data protection. |
| `concurrent` or `simultaneous` | Verified overlap under an explicit criterion. | Latency, responsiveness, real-time performance. |
| `real-time` | A measured latency and reliability requirement is met. | Concurrency, adaptation. |
| `intention-anchored` | A named intention is the configuration object. | That the intention is accurate, stable, or better than another anchor. |
| `intention-aligned` | Evidence shows use or outcome matches the intention. | A stored target. Prefer `intention-anchored` before validation. |
| `anticipatory` | The policy begins before a named target event. | Gradualness, lower exposure, benefit. |
| `attenuated access` or `attenuated continuation` | Access remains while named parameters change. | Reduced harm, quality, task success. |
| `operational exposure` | An instrumented delivered quantity: luminance, throughput. | Perception, physiology, outcome. |
| `stimulation` | Reserved umbrella; decompose into a measured construct. | That display settings change arousal or sleep. |
| `reduced impact` | Only when the named impact and comparison are measured. | A synonym for attenuation, friction, or delay. |

## Present terminology systems for author choice

Offer three to five coherent systems rather than isolated synonyms. Each specifies its default and
structural terms; its benefit-first entry sentence (human situation, desired value, then capability);
its familiar entry term, first-use definition, and approved short form;
reserved terms; the likely reader inference; and evidence status. When all are defensible, one should optimize domain
naturalness, one broad-CHI clarity, and one system/evidence precision. Recommend one, but let the
author choose, combine named parts, or reject the set, and record the semantic-contract decision
separately from the lexical-spine decision.

## Propagate without semantic drift

Propagate the approved hierarchy through motivation framing; related-work classifications; gap and
contribution packages; approach descriptions; figure labels and captions;
future Abstract, Introduction, Related Work, method, study conditions, measures, and results; and
the Phase 2 handoff. Do not vary terms for elegance when the variation changes the implied mechanism
or evidence, and preserve a prior work's exact technical terms even when the project names itself
differently.

## Audit and reopen

Before a Phase 1 readiness decision, search artifacts and reports for every selected, allowed,
reserved, and superseded term and inspect each loaded occurrence in context: first use
supplies the operational definition, and figures, captions, study conditions, and contribution
wording carry the same meanings without upgrading any term beyond its evidence state. Mark
quotations of prior work so they are not read as project claims, and record conflicts in
`terminology-contract.md`.

Reopen the contract when a system trace changes what is implemented, formative work changes the
domain language, a study operationalizes a term differently, a closer work narrows the distinction,
or an author changes contribution emphasis. Never erase a definition; mark it superseded.
