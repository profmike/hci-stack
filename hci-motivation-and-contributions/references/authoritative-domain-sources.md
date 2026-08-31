# Authoritative domain-source protocol

“Authoritative” is a relationship among a **body, its remit, a document type, a population or
jurisdiction, a version, and one named claim** — not a permanent quality score. A WHO meeting report
can establish that WHO convened experts around a public-health concern while remaining only adjacent
context for a causal claim about one bedtime behavior. **Authority is claim-specific:** every
designation names the exact claim and remit, so neither omit the organizations that define practice
in a domain nor treat a name as proof for a nearby claim.

Author-provided authorities are seeds: verify the remit independently and search for a current,
claim-matched source with stronger authority, methodology, directness, or version status. A supplied
source may be kept for a unique role but never becomes the evidence ceiling.

## Map the active claim domains

Before motivation synthesis, decompose the active claims into domains rather than searching for one
generic “credible source”: population health and disease burden; guidance for a defined population;
a specialist domain such as sleep, exercise, ergonomics, accessibility, or safety; statistics,
regulation, or public policy; standards and measurement; product capability and platform policy; and
HCI venue scope. Create `authoritative-source-map.md` from the asset template with a row even where
no suitable authority exists, recording that absence and the alternative evidence route.

## Identify authorities by remit, not name recognition

For each domain: identify the body whose published remit covers the claim, population, and
jurisdiction; verify its identity and current source on its official first-party site; open the most
decision-relevant document in full; record date, version, supersession state, and a refresh trigger;
state the exact claim it supports and a parallel **cannot support** boundary; and assign tier,
ingestion completeness, directness, and claim-specific `ES` strength under the evidence protocol.

Never infer authority from search rank, citation count, a third-party summary, or a familiar
acronym, and never add an organization to confer prestige. Where bodies share remit, record the
joint statement or triangulate rather than picking the strongest rhetoric.

Correct routing — examples, not a required list — includes WHO for a global public-health program
within WHO's remit; AASM and the Sleep Research Society for a joint adult sleep-duration consensus;
ACSM (American College of Sports Medicine, not “ASCM”) for an applicable exercise/sports-medicine
position stand; a national statistical agency or regulator for a jurisdiction-specific official
estimate or rule; W3C, ISO, or NIST for the exact standard in scope; and ACM SIGCHI's official
roster for current conference scope, not for empirical validity.

## Distinguish document roles

Record the source type, because authority alone does not determine evidentiary use:

| Source type | Can establish | Cannot establish by itself |
|---|---|---|
| Guideline, consensus, position statement | the recommendation and its evidence boundary | uptake, effectiveness here, causality beyond the reviewed evidence |
| Official surveillance or statistics | an estimate for the stated population, measure, place, time | another population, construct, or period |
| Meeting or agenda report | institutional attention and stated concerns | guideline, diagnostic status, efficacy, causal estimate |
| Standard | the normative requirement and version | implementation, compliance, usability, outcome |
| Regulation or policy | the rule, scope, jurisdiction, effective date | enforcement, prevalence, experience, effectiveness |
| Official product documentation | capability, configuration, documented behavior | adoption, adherence, causal benefit, market absence |
| Professional or venue roster | scope at the checked date | evidence strength, relevance, study validity |

Label an old but historically useful document as historical and look for a current successor.

## Authority-map completion gate

Motivation synthesis waits until every active domain and governing motivation claim has an
authority-map row carrying a verified remit and official canonical source; document type,
date/version, population/jurisdiction, and supersession state; the exact supported claim and
explicit cannot-support boundary; evidence tags reconciled with the original; and a visible fallback
route for missing or disputed authority. Product and venue authorities are never outcome evidence.
Mark the artifact `AUTHORITATIVE_DOMAIN_SOURCES_MAPPED`, and use
`NEEDS_AUTHORITATIVE_SOURCE_MAPPING` while any decision-relevant row is unresolved. This gate
precedes motivation-frame selection; do not ask the author to choose a frame to compensate for
missing authority work.
