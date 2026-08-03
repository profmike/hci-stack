# Consequence severity research and ranking

## Contents

1. Gate contract
2. Build the consequence chain
3. Search the evidence layers
4. Extract comparable evidence
5. Rank severity without hiding uncertainty
6. Completion and presentation
7. Failure modes

## 1. Gate contract

Complete this research gate after the target people, behavior, activity, and context are bounded
enough to make searches meaningful and before asking the author to choose a motivation frame or
rank consequences.

The output is an evidence-ranked synthesis, not a preference survey. Before the synthesis is
complete, ask the author only for factual scope, direct observations, existing artifacts, and
access—not which consequence sounds most important.

Every retained source must satisfy the skill's full-copy rule. Search snippets, abstracts, AI
summaries, and general-domain harms may discover candidates but cannot determine a rank.

When an abstract or partial record suggests that an inaccessible paper could materially change the
ordering, magnitude, directness, or certainty of the ranking, follow the author-access protocol in
`author-collaboration.md`. Do not hide the blocker in a file or wait for a later decision gate.
Continue non-dependent searches, then ask for the highest-priority concrete access action. Use
`NEEDS_AUTHOR_SOURCE_ACCESS` until the full paper is audited or explicitly excluded from the
ranking; this is an access request, not a request for the author to judge consequences.

## 2. Build the consequence chain

Map plausible consequences without assuming every link:

`target behavior or exposure → immediate experience/displacement → proximal outcome → next-day
function → longer-term outcome`

For each node and arrow, record:

- construct and operational measure;
- population, setting, dose, timing, and comparator;
- whether the source measures the target behavior or only an adjacent exposure;
- whether temporal order and causality are supported;
- direct, adjacent, analogy, or unsupported claim support; and
- project evidence that agrees, conflicts, or remains absent.

Keep consequences distinct. For sleep-related work, bedtime, sleep onset, sleep opportunity, total
sleep time, sleep efficiency, awakenings, subjective quality, next-day sleepiness, mood, and
performance are not interchangeable.

Do not cite the general harms of sleep deprivation as though the target behavior caused those harms.
Each arrow from the project behavior to a downstream consequence needs its own evidence.

## 3. Search the evidence layers

Search all materially plausible layers, even when the brief names only one:

1. **Occurrence and dose:** how often, how long, for whom, and under what definition the target
   behavior occurs.
2. **Immediate experience:** regret, difficulty disengaging, autonomy, frustration, reactance,
   distress, or valued benefits of continued activity.
3. **Proximal behavioral or physiological outcomes:** timing, duration, interruption, arousal,
   attention, or another direct consequence.
4. **Next-activity functioning:** sleepiness, cognition, mood, safety, school/work performance, or
   social functioning.
5. **Longer-term outcomes:** retain only when the behavior-to-intermediate and
   intermediate-to-long-term chains are both supported.
6. **Heterogeneity and inequity:** age, health status, caregiving, shift work, disability,
   socioeconomic conditions, geography, culture, and other plausible moderators.

Use systematic reviews and meta-analyses to map the field and disagreements. Inspect the exact
primary studies that carry decisive estimates or unusually close populations and behaviors.
Prefer, when appropriate:

- experiments and natural experiments for causal effects;
- longitudinal designs for temporal order;
- objective device logs for exposure;
- actigraphy, polysomnography, or validated instruments for sleep;
- ecological momentary assessment and diaries for episodes and intention mismatch; and
- qualitative studies for meanings, mechanisms, workarounds, and experienced consequence.

Cross-sectional self-report may establish an association or reported experience, not direction or
causality. A clinically severe outcome in a weakly matched population must remain adjacent evidence.

## 4. Extract comparable evidence

For every retained claim, capture:

| Field | Required record |
|---|---|
| Identity | Exact work, version, DOI/canonical URL, full-copy location, NotebookLM source ID |
| Design | Experimental, longitudinal, cross-sectional, qualitative, review, dataset, or official record |
| Population | Inclusion criteria, age/context, geography, recruitment, and relevant subgroup |
| Coverage | Sample size, follow-up, exposure prevalence, attrition, and missingness |
| Exposure | Exact behavior, device/app/content, dose, timing, and measurement |
| Outcome | Construct, instrument, unit, timeframe, threshold, and clinical/practical interpretation |
| Estimate | Absolute and relative result, comparator, effect size, confidence interval or uncertainty |
| Analysis | Covariates, temporal order, multiplicity, sensitivity analyses, and causal identification |
| Boundary | Limitations, conflicts, corrections/retractions, and direct/adjacent/analogy support |

Prefer absolute changes and interpretable units. Statistical significance without effect magnitude,
uncertainty, baseline risk, and practical meaning cannot establish severity.

## 5. Rank severity without hiding uncertainty

Create `consequence-severity-ranking.md`. Rank within the selected population and context using
separate dimensions:

- **magnitude:** size of the observed or estimated consequence in an interpretable unit;
- **coverage:** how frequently the exposure and consequence occur in the relevant population;
- **functional importance:** impairment, lost opportunity, safety, distress, or other practical
  meaning;
- **causal proximity:** number and strength of supported links from the target behavior;
- **duration and reversibility:** immediate/transient, repeated/cumulative, or persistent;
- **distribution:** concentrated risk, vulnerable subgroups, inequity, or population-wide reach;
- **evidence certainty:** study design, directness, consistency, precision, and bias.

Do not collapse severity and evidence certainty into one score. A potentially grave but distal,
low-certainty consequence can rank as high possible severity with low confidence; it must not
silently outrank a moderate, direct, well-established consequence.

Use an ordinal evidence synthesis with ties and conditional ranks. For each consequence state:

1. severity rank or tier in the current scope;
2. confidence in that rank;
3. decisive estimates and locators;
4. causal-chain boundary;
5. populations or assumptions under which the rank changes; and
6. the evidence that would move it up, down, or out.

Do not compute a weighted composite score unless the weights have an explicit defensible source.
Run a qualitative sensitivity analysis: show whether rankings change when magnitude, coverage,
functional importance, or causal certainty receives more emphasis.

## 6. Completion and presentation

Mark the gate `CONSEQUENCE_RANKING_COMPLETE` only when:

- the plausible consequence inventory has been searched across all relevant layers;
- every retained ranking source has an obtained and opened full copy;
- the top-ranked consequence has direct evidence or is explicitly labeled adjacent;
- magnitude, coverage, uncertainty, and practical meaning are recorded where applicable;
- the causal chain and downstream extrapolations are bounded;
- contradictory evidence and meaningful subgroup differences are visible; and
- ranking sensitivity and unresolved evidence are stated.

Otherwise use `NEEDS_CONSEQUENCE_EVIDENCE`, or `NEEDS_AUTHOR_SOURCE_ACCESS` when the remaining
decision-relevant gap requires a human CAPTCHA, sign-in, subscription, or file transfer.

Present the ranked synthesis and its uncertainty to the author before constructing the motivation
decision packet. Do not ask the author to rank, select, or approve consequences while this gate is
incomplete. After it is complete, the later motivation-frame gate may ask the author to select or
combine evidence-grounded frames; preserve the evidence ranking independently of that rhetorical
choice.

## 7. Failure modes

- treating prevalence as severity;
- treating a p-value as practical importance;
- combining different sleep or wellbeing constructs under one label;
- converting cross-sectional association into causal consequence;
- transferring an effect from a mismatched population without marking it adjacent;
- using long-term harms of a general intermediate outcome to inflate the target behavior's stakes;
- ranking from one dramatic study or one industry statistic;
- ignoring valued benefits, workarounds, or reasons people continue the activity;
- hiding disagreement behind a composite score; or
- asking the author which consequence should lead before completing the evidence synthesis.
