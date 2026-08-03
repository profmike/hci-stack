# Authoritative domain-source protocol

Use this protocol to prevent two opposite errors: omitting the organizations that define practice
or guidance in a domain, and treating an organization's name as automatic proof for every nearby
claim.

“Authoritative” is a relationship among a **body, its remit, a document type, a population or
jurisdiction, a version, and one named claim**. It is not a permanent quality score. A WHO meeting
report can directly establish that WHO convened experts around a public-health concern while
remaining only adjacent context for a causal claim about one bedtime behavior. An official product
manual can establish what a control does, but not whether people use it or whether it works.
**Authority is claim-specific:** every authority designation must name the exact claim and remit.

Author-provided authorities and citations are only seeds. Independently verify the remit and search
for a current, claim-matched source with stronger authority, methodology, directness, or version
status. Preserve a supplied source when it has a unique role, but do not let it become the evidence
ceiling merely because the author selected it.

## Map the active claim domains

Before motivation synthesis, decompose the active claims into domains rather than searching for one
generic “credible source.” Common domain roles include:

- population health, disease burden, or global public-health agenda;
- clinical or behavioral guidance for a defined age/population;
- sleep, exercise, nutrition, ergonomics, accessibility, safety, or another specialist domain;
- national statistics, regulation, education, labor, or public policy;
- technical standards, interoperability, measurement, or safety engineering;
- current product capability and platform policy; and
- HCI community and venue scope.

Create `authoritative-source-map.md` from the asset template. Include a row even when no suitable
authority exists; record that absence and the alternative evidence route rather than silently
substituting a convenient organization.

## Identify authorities by remit, not name recognition

For each domain:

1. identify the body whose published remit actually covers the claim, population, and jurisdiction;
2. verify the body's identity and the current source on its official site;
3. prefer the most decision-relevant document type—current guideline, consensus or position
   statement, official surveillance/statistics, standard, policy, or capability documentation;
4. obtain and open the exact full source, including methods/evidence review and limitations when
   the claim depends on them;
5. record publication/adoption date, version, supersession state, and a future refresh trigger;
6. state the exact claim the source supports and a parallel **cannot support** boundary; and
7. assign source tier, ingestion completeness, directness, and claim-specific `ES` strength under
   the evidence protocol.

Search current first-party pages for the body and the document. Do not infer authority from search
rank, citation count, a third-party summary, or a familiar acronym. Where more than one body shares
remit, record the joint statement or triangulate the bodies rather than selecting whichever source
has stronger rhetoric.

Examples of correct routing—not a permanent required list—include:

- WHO for a global public-health program or intergovernmental meeting within WHO's remit;
- AASM and the Sleep Research Society for a joint adult sleep-duration consensus;
- ACSM (American College of Sports Medicine, not “ASCM”) for an applicable exercise/sports-medicine
  position stand;
- a national statistical agency or regulator for a jurisdiction-specific official estimate or
  rule;
- W3C, ISO, NIST, or another competent standards body for the exact standard in scope;
- Apple, Google, or another vendor's official documentation for that vendor's current product
  capabilities only; and
- ACM SIGCHI's official roster for current SIGCHI conference scope, not for empirical validity.

These examples illustrate claim-to-remit matching. Never add an organization merely to confer
prestige, and never assume one body covers an entire multidisciplinary project.

## Distinguish document roles

Record the source type because authority alone does not determine evidentiary use:

| Source type | Usually can establish | Usually cannot establish by itself |
|---|---|---|
| Current guideline, consensus, or position statement | the issuing body's recommendation and its stated evidence boundary | uptake, effectiveness in this project's context, or causality beyond the reviewed evidence |
| Official surveillance or statistics | a defined estimate for the stated population, measure, place, and time | another population, construct, or current period |
| Meeting or agenda report | institutional attention, deliberation, questions, and stated concerns | a clinical guideline, diagnostic status, consensus efficacy, or modern causal estimate |
| Standard | the normative technical requirement and version | actual implementation, compliance, usability, or outcome |
| Regulation/policy | the rule, scope, jurisdiction, and effective date | enforcement, prevalence, experience, or effectiveness unless separately measured |
| Official product documentation | available capability, configuration, exceptions, and documented behavior | adoption, adherence, causal benefit, or exhaustive market absence |
| Professional/venue roster | community or venue scope at the checked date | evidence strength, relevance, novelty, or study validity |

When a document is old but still useful historically, label it historical and look for a current
successor. Do not silently present a meeting report as a guideline or an institutional statement as
an empirical result.

## Authority-map completion gate

The motivation evidence chain is not ready for synthesis until:

- every active domain and governing motivation claim has an authority-map row;
- each named authority has a verified remit and official canonical source;
- document type, date/version, population/jurisdiction, and supersession state are recorded;
- the exact supported claim and explicit cannot-support boundary are present;
- full-copy state and claim-specific evidence tags are reconciled with the original;
- missing or disputed authority is visible with a fallback route;
- product and venue authorities are not used as outcome evidence; and
- the artifact is marked `AUTHORITATIVE_DOMAIN_SOURCES_MAPPED`.

Use `NEEDS_AUTHORITATIVE_SOURCE_MAPPING` while any decision-relevant row remains unresolved. This
gate precedes motivation-frame selection; do not ask the author to choose a frame to compensate for
missing authority work.
