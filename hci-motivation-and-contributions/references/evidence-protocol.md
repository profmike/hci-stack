# Evidence and citation protocol

Use separate dimensions for **source tier**, **ingestion completeness**, **claim directness**, and
**claim-specific evidence strength**. A prestigious venue does not make every statement strong
evidence, and a large sample does not repair an indirect measure.

## Contents

1. Source tiers
2. Claim support levels
3. Method-strength rules
4. Reusable evidence-strength register
5. Quantitative-claim checklist
6. Citation verification
7. Prior-work six-field evidence accounting
8. Evidence sufficiency by framing move
9. Inherited foundations and reader-facing boundaries

## How to read the labels

A compact record such as `[T2A | FULL | Adjacent | ES1]` answers four different questions:

| Label | Question answered | Example interpretation |
|---|---|---|
| `T1`, `T2A`, `T2B` | What kind of source is this? | Strongest published/authoritative, useful external, or authors' own evidence |
| `FULL`, `PARTIAL`, `BROKEN` | How completely was the exact source obtained and opened? | Methods/results/limits available, incomplete, or unusable |
| `Direct`, `Inferred`, `Adjacent`, `Analogy` | How closely does it match the proposed claim? | Exact match through design-transfer only |
| `ES3`, `ES2`, `ES1`, `ES0` | How strongly does it support this one named claim after audit? | Anchor, bounded support, context only, or do not use |

These are not four versions of one grade. A `T1` meta-analysis can be `ES1` for an exact bedtime
feed-scrolling claim because its exposure is generic daily screen time. A careful `T2B` formative
study can be `ES3` for a narrow claim about the sampled users' workflow. The same source can receive
different ES labels for different claims.

Do not confuse source tiers with the separate related-work **contribution-strength ladder**
(`Tier 1 — capability`, `Tier 2 — experience or outcome`, `Tier 3 — cost or access`). The latter
ranks what a proposed project may contribute relative to a comparator; it does not rate evidence.

## Source tiers

### T1 - authoritative or strongest published evidence

- Official public-health, government, standards, or intergovernmental data for population facts
  (for example, WHO when the health claim is within WHO's remit).
- Systematic reviews, meta-analyses, consensus statements, and strong primary studies.
- Highly relevant, peer-reviewed work from the leading venue for the question (for HCI, prefer CHI
  over a less selective venue when both directly support the same claim).

Use the original dataset or primary study when it is available. "Highly cited" is a discovery
heuristic, not proof of validity.

An authoritative body is authoritative only for claims within its verified remit and for the role
of the exact document used. Read
[authoritative-domain-sources.md](authoritative-domain-sources.md) and maintain
`authoritative-source-map.md`. A meeting report may anchor institutional attention while remaining
weak for causality; a guideline may establish a recommendation but not uptake; official product
documentation may establish capability but not effectiveness. Authority never overrides
ingestion, directness, recency, document type, or the claim-specific `ES` audit.

For HCI related-work coverage, prioritize CHI and the relevant conferences on the current official
SIGCHI sponsored/co-sponsored roster. That search priority helps situate the project in its
community; it does **not** automatically assign `T1`, increase directness, repair bias, or upgrade
an `ES` label. A close, rigorous non-ACM source may be stronger evidence for a named claim than an
indirect CHI paper.

### T2A - useful published or external evidence

- Relevant peer-reviewed work from adjacent or second-tier venues and journals.
- Transparent industry reports, product telemetry, and market studies.
- Official product specifications and release records for technical or timing facts.

State conflicts of interest and methodological opacity. Do not present an industry survey as
population truth when recruitment, weighting, or instruments are undisclosed.

### T2B - the authors' evidence

- Formative interviews, contextual inquiry, diary studies, surveys, log analysis, pilots, and
  evaluations conducted by the authors.

Report recruitment, inclusion criteria, setting, sample, instrument/task, analysis, and limitations.
Use de-identified aggregate evidence. Do not generalize beyond the sampled population and context.

## Claim support levels

- **Direct:** the source measured or established the same construct, population, context, and
  relationship asserted by the claim.
- **Inferred:** checked evidence supports a bounded analytical conclusion that the source does not
  state directly. Keep it out of the default prior-work contribution boundary and never use source
  silence to infer an absent capability.
- **Adjacent:** the source supports a neighboring population, context, construct, or mechanism.
  Name the difference and use cautious language.
- **Analogy:** the source only motivates a hypothesis or design transfer. Never present it as direct
  proof of the target problem.

Prefer T1 direct evidence. T2B direct evidence can be the strongest support for a novel, narrowly
defined user need that published work has not studied.

## Method-strength rules

- Prevalence requires a defined population, sampling frame, measurement, and timeframe.
- Trends require comparable measurements across time; two unrelated point estimates are not a
  trend.
- Causal language requires a design and analysis that identify causality. Cross-sectional,
  observational, and self-report studies ordinarily support association only.
- Qualitative work supports experiences, mechanisms, meanings, and design implications; frequency
  within a small purposive sample is not population prevalence.
- Statistical significance alone does not establish practical importance. Record effect size and
  uncertainty where available.
- A non-significant difference is not evidence of equivalence without an appropriate equivalence or
  non-inferiority design.
- Absence of published work is not proof that no work exists. State the databases, queries, dates,
  and scope behind a novelty claim. This literature-search rule is distinct from a bounded
  inference about one fully checked published/demonstrated system.

## Reusable evidence-strength register

Maintain `evidence-strength-register.md`. Its purpose is to cache a completed source audit so later
analysis can reuse it without silently treating a source as universally strong.

Use two independent axes:

### Ingestion completeness

- `FULL`: the complete version needed for the assessment, including relevant methods, results,
  limitations, and supplements, was obtained and opened.
- `PARTIAL`: only an abstract, excerpt, repository record, institutional summary, or incomplete
  rendering is available. It may support identity or a narrowly stated abstract-level fact, but not
  a methods-dependent quantitative or causal claim.
- `BROKEN`: CAPTCHA, error page, wrong page, failed import, or content that does not contain the
  intended source. It supplies no evidence.

### Claim-specific evidence strength

- `ES3 ANCHOR`: for the **named narrow claim**, a `FULL` primary or authoritative source closely
  matches the construct, population, context, exposure/outcome, and relationship; supplies temporal
  or comparative leverage appropriate to the wording; reports interpretable estimates and
  uncertainty where quantitative; and passes the critical-risk-of-bias veto.
- `ES2 BOUNDED SUPPORT`: a `FULL` source supports the named claim, but one or more material limits
  require bounded wording—for example cross-sectional design, self-report, exposure mismatch,
  selected population, weak precision, or incomplete causal identification.
- `ES1 CONTEXT ONLY`: useful for construct definition, lived experience, hypothesis, broad
  coverage, contradiction, or an adjacent mechanism; it cannot quantify or causally establish the
  exact target claim.
- `ES0 DO NOT USE`: the source cannot support the named claim, is `BROKEN`, is too incomplete for
  the proposed use, or has a fatal validity/provenance problem.

These tags assess evidence for a claim, not paper prestige or overall study quality. The same source
may be `ES3` for a narrow descriptive result, `ES2` for a nearby association, and `ES0` for a
distal causal claim. Qualitative work may be strong for meanings and experience while remaining
inappropriate for prevalence. Null findings retain strength when the design supports the bounded
null; non-significance alone is not equivalence.

### Critical-risk-of-bias veto

`ES3` is prohibited when any critical issue remains in the part of the study supporting the claim:

- allocation, comparison, exposure, or outcome construction is unclear or internally inconsistent;
- the analysis is incompatible with the design, materially underpowered for the asserted
  conclusion, or omits required uncertainty;
- a multi-component intervention is credited to an isolated component without identification;
- attrition, missingness, selective reporting, multiplicity, confounding, or measurement validity
  plausibly overturns the result;
- the ingested item is not `FULL`, or a correction/retraction/version conflict is unresolved; or
- the source's own limitations contradict the proposed strength or causal wording.

A design label such as “RCT,” a large sample, venue prestige, or an AI/NotebookLM rating never
overrides this veto.

NotebookLM ratings never override the veto.

### Cache and re-review rule

Each register row must name the supported claim, ingestion tag, strength tag, direction, decisive
estimate/locator, decisive limitation, auditor/date, and re-review trigger. Future analysis may
reuse the row without re-reading the whole source only when all of these remain unchanged:

- bibliographic identity and source version;
- proposed construct, population, context, exposure, outcome, and comparator;
- association/causal wording and required precision; and
- known corrections, retractions, contradictions, and risk-of-bias information.

Re-review when any item changes, when a stronger claim is proposed, when the full source replaces a
partial import, when direct contradictory evidence appears, or when the source becomes
decision-critical. An unmarked source is `UNASSESSED`, not implicitly `ES1` or stronger.

### Source-resolution rule

`UNASSESSED` describes missing assessment; it is not a terminal evidence grade or a defensible
end-of-round disposition. Put every potentially decision-relevant candidate in
`source-resolution.csv` when it is discovered. Continue until it is:

- fully obtained, opened, audited, and linked to a completed evidence-register row;
- screened out before retention because a documented metadata/abstract relevance check shows it
  cannot affect an active claim, mechanism, comparison, rank, or study requirement;
- superseded by a verified stronger source with the consequence recorded; or
- blocked behind human-only access after lawful routes were tried and an exact
  `NEEDS_AUTHOR_SOURCE_ACCESS` request was surfaced to the author.

At phase readiness, use `references.csv` URLs to distinguish external research evidence from
project evidence: every HTTP(S) citation key needs a source-resolution row, while only explicitly
classified `internal:` project evidence is exempt. A supersession must resolve to a different
retained, fully assessed source with a stable citation key. A human-access state must preserve the
actual surfaced-request date/locator, affected claims, fallback or narrowing, and reopen trigger.

Record every supplied draft, bibliography, and reading-list entry in
`imported-bibliography-accountability.csv`. Their presence does not make them author decisions or
evidence. Every materially relevant entry must resolve to a terminal `source-resolution.csv` row
and, when retained, to the applicable six-field accounting row. A potentially relevant entry
cannot remain a future-tense “obtain full copy” task in a completed audit. `PARTIAL` and `BROKEN`
describe what was opened; they do not close the acquisition loop. A downloaded file is still
`FULL_TEXT_OBTAINED` until the relevant methods, results, limitations, corrections, and supplements
have actually been reviewed.

### Author-provided seeds do not set the evidence ceiling

For every author-provided or imported source retained for a material claim, document an independent
upgrade search. Compare at least:

- institutional authority and remit for normative or official claims;
- design validity, causal identification, risk of bias, sample/coverage, and synthesis quality;
- directness to the construct, population, context, exposure/intervention, comparator, and outcome;
- currency, correction/retraction/supersession state, and contradictory evidence; and
- publication and peer-review quality, including top HCI/domain venues where relevant.

These are independent axes. Do not convert a venue label, citation count, institutional brand, or
author preference into evidence strength. Retain the seed when it remains uniquely direct or useful,
but bound its claim. Corroborate it when stronger evidence agrees. Mark it `SUPERSEDED` only when the
replacement covers its intended evidentiary role more defensibly, and preserve the stable
replacement locator and consequence for downstream claims.

NotebookLM may apply and stress-test the rubric, but the final cached rating must be reconciled
against the opened original. Persist the vetted bar and markings in NotebookLM as a note or
dedicated text source when that notebook is the project's research hub. If NotebookLM disagrees
with the manual audit, record the disagreement; never resolve it by vote.

## Quantitative-claim checklist

For each number, record:

1. What was measured, in what unit, and over what period?
2. Who or what was sampled, how, and with what coverage or sample size?
3. What method produced the estimate?
4. Is the value an observed count, model estimate, effect, prediction, or marketing claim?
5. What uncertainty, denominator, comparator, and limitations affect interpretation?
6. Where exactly is the support: page, section, table, figure, dataset cell, or official page?

Use numbers when they sharpen magnitude, trajectory, mismatch, or validation. Do not add weak
statistics merely to make every sentence look quantitative.

## Citation verification

For every material factual claim:

- Resolve bibliographic identity using a DOI, PMID, ISBN, report identifier, dataset record, or
  canonical URL.
- Open the full source. Confirm title, authors/organization, year, venue, and version.
- Read the methods and limitations needed to interpret the cited result.
- Record the exact locator and a concise paraphrase of what the source actually supports.
- Cite the primary source instead of a secondary article that merely cites it.
- Check for corrections, retractions, superseding releases, and material conflicts.
- Re-open the cited passage during the sentence-level audit.

Reject a source when only an abstract, search snippet, AI summary, or another paper's paraphrase is
available for a claim that depends on methodological detail.

## Prior-work six-field evidence accounting

Read [prior-work-contribution-boundaries.md](prior-work-contribution-boundaries.md) and maintain
`prior-work-evidence-accounting.csv`, `idea-provenance-ledger.csv`, and the human-readable
`prior-work-contribution-boundary.md`.

For every material prior-work or focal-project atom, record these independently:

- `AUTHOR CLAIM`;
- `DEMONSTRATED ARTIFACT OR STUDY`;
- `OPERATED CAPABILITY`;
- `EVALUATED RESULT`;
- `CAPABILITY COLLISION`; and
- `CONTRIBUTION CREDIT`.

No field inherits truth from another. The familiar `Claimed`, `Demonstrated`, and `Capability`
tags are shorthand views only.

Capability collision requires positive evidence that the smallest named operation actually ran.
It can exist for `DEMONSTRATED_UNCLAIMED` operation and therefore narrow a firstness claim without
granting contribution credit. Contribution credit requires an explicit author claim and matched
demonstration; artifact-capability credit additionally requires demonstrated operation. Bound both
to the weakest supported command, parameter, channel, condition, people, activity, artifact
version, data, comparator, outcome, causal rung, and timeframe.

Treat the asymmetric states explicitly:

- `DEMONSTRATED_UNCLAIMED`: may create a capability collision and false-firstness,
  implementation-novelty, inheritance, or fair-comparator risk; contribution credit is `NONE` and
  the operation is not attributed as the authors' claimed contribution.
- `CLAIMED_UNDEMONSTRATED`: receives neither capability collision nor contribution credit unless
  separate positive execution evidence exists.
- A package comparison supports package-level results only. It cannot identify one operator or
  mechanism without a defensible isolating contrast.
- Nonsignificance never supports equivalent, comparable, maintained, or non-inferior wording
  without an appropriate equivalence or non-inferiority design.

Assign `OPERATED CAPABILITY=NO` only from positive artifact evidence that settles the audited
version's interaction or architecture. Source silence and expected author behavior may create only
`SEARCH_PRIORITY` or `REOPEN_QUERY`; they cannot populate positive capability, negative absence,
collision, or contribution credit. Use `UNRESOLVED` when positive evidence does not settle the
unit.

Put proposals, future work, interpretations, and hypothetical scenarios only in
`idea-provenance-ledger.csv`, with `CAPABILITY COLLISION=NONE` and
`CONTRIBUTION CREDIT=NONE`. They may constrain conceptual provenance or “first idea” wording, but
cannot retire a demonstrated capability claim. If an explicit author claim says a realized
capability exists but matched evidence does not verify it, keep a `CLAIMED_UNDEMONSTRATED`
accounting row so the excluded claim remains visible; it may also be cross-referenced as an
unverified implementation claim in idea provenance.

Decompose hybrid systems into one row per user-action-to-command, conventional-input,
sensed-or-computed-state-to-adaptation/reward, condition-to-gating, or system-state-to-feedback
channel. Reject a whole-system label unless positive evidence qualifies every channel required by
the operational definition.

Normalize away platform, hardware, sensor, OS, app, and game labels. A port receives contribution
credit only when complete-source evidence demonstrates nontrivial adaptation knowledge, a new use
class, or a directly validated empirical finding. A zero-credit port can still create a capability
collision.

## Evidence sufficiency by framing move

- **Context:** one or two authoritative facts that establish scale or trajectory.
- **Pain:** direct user evidence plus an evidence-ranked consequence; triangulate published evidence
  and the authors' observations when possible. Keep severity and confidence separate.
- **Gap:** primary papers/products with six-field evidence accounting, capability collisions
  separated from contribution attribution, and proposals/silence excluded—not review articles or
  inferred absences alone.
- **Why now:** official release/capability evidence plus adoption, exposure, or contextual change.
- **Approach hypothesis:** enabling mechanism, intended experience, adopted foundations, likely
  costs, and explicit distinction between implemented facts and plans.
- **Research process:** traceable completed artifacts and decisions plus labeled future work.
- **Prospective contribution:** a reusable capability or knowledge hypothesis with the Phase 2 and
  Phase 3 evidence required to support it.
- **Broader value:** a reasoned implication whose scope does not exceed the evidence.

Before choosing a motivation frame, apply
[consequence-severity-research.md](consequence-severity-research.md). Do not use prevalence as
severity, statistical significance as practical importance, cross-sectional association as
causality, or general downstream harms as though the target behavior established every causal
link.

## Inherited foundations and reader-facing boundaries

A checked external source may establish a general mechanism, design fact, or measurement
relationship that the project adopts. Do not demand a redundant project study merely because the
project uses that foundation. Require project-specific evidence when the active claim concerns the
exact artifact, parameter value, implementation fidelity, device or setting coverage, delivered
dose, robustness, or downstream effect.

Keep the full uncertainty and limitation record here even when a reader-facing passage does not
need every item. Apply [claim-focused-writing.md](claim-focused-writing.md): include a limitation or
counterfinding in narrative prose only when it materially constrains a claim or comparison the
text actually makes. An unclaimed distal outcome does not require a prophylactic disclaimer.
