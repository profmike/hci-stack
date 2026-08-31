# Consequence severity research and ranking

## 1. Gate contract

Complete this gate once the target people, behavior, activity, and context are bounded enough for
meaningful searches, and before asking the author to choose a motivation frame or rank consequences;
until then ask the author only for factual scope, observations, artifacts, and access. Every
retained source must satisfy the full-copy rule; snippets, abstracts, AI summaries, and
general-domain harms may discover candidates but cannot determine a rank. When an inaccessible paper
could materially change the ranking, run the author-access protocol in `author-collaboration.md`
immediately rather than logging the blocker for a later gate: continue non-dependent searches, ask
for the highest-priority concrete access action, and use `NEEDS_AUTHOR_SOURCE_ACCESS` until that
paper is audited or explicitly excluded. This is an access request, not a request for the author to
judge consequences.

## 2. Build the consequence chain

Map plausible consequences without assuming every link:

`target behavior or exposure → immediate experience/displacement → proximal outcome → next-day
function → longer-term outcome`

For each node and arrow, record the construct and operational measure; population, setting, dose,
timing, and comparator; whether the source measures the target behavior or an adjacent exposure;
whether temporal order and causality are supported; whether support is direct, adjacent, analogy, or
unsupported; and project evidence that agrees, conflicts, or is absent.

Keep consequences distinct: for sleep-related work, bedtime, sleep onset, total sleep time, sleep
efficiency, subjective quality, next-day sleepiness, mood, and performance are not interchangeable,
and the general harms of sleep deprivation are not evidence that the target behavior caused them.
Every arrow needs its own evidence.

## 3. Search the evidence layers

Search every materially plausible layer even when the brief names only one: occurrence and dose;
immediate experience, including autonomy, reactance, and the valued benefits of continuing the
activity; proximal outcomes; next-activity functioning; longer-term outcomes, retained only when
both the behavior-to-intermediate and intermediate-to-long-term chains are supported; and
heterogeneity and inequity across age, health, caregiving, disability, socioeconomic conditions, and
culture. Map the field with reviews, then inspect the primary studies carrying decisive estimates or
unusually close populations. Cross-sectional self-report may establish an association, not direction
or causality, and a clinically severe outcome in a weakly matched population stays adjacent
evidence.

## 4. Extract comparable evidence

For every retained claim, capture:

| Field | Required record |
|---|---|
| Identity | Exact work, version, DOI/canonical URL, full-copy location, NotebookLM source ID |
| Design | Experimental, longitudinal, cross-sectional, qualitative, review, dataset, or official record |
| Population | Inclusion criteria, age/context, geography, recruitment, relevant subgroup |
| Coverage | Sample size, follow-up, exposure prevalence, attrition, missingness |
| Exposure | Exact behavior, device/app/content, dose, timing, measurement |
| Outcome | Construct, instrument, unit, timeframe, threshold, practical interpretation |
| Estimate | Absolute and relative result, comparator, effect size, uncertainty |
| Analysis | Covariates, temporal order, multiplicity, sensitivity analyses, causal identification |
| Boundary | Limitations, conflicts, corrections/retractions, direct/adjacent/analogy support |

Prefer absolute changes and interpretable units; significance without effect magnitude, uncertainty,
baseline risk, and practical meaning cannot establish severity.

## 5. Rank severity without hiding uncertainty

Create `consequence-severity-ranking.md` and rank within the selected population and context on
separate dimensions: **magnitude** in an interpretable unit; **coverage** of exposure and
consequence in the relevant population; **functional importance** such as impairment, lost
opportunity, safety, or distress; **causal proximity**, meaning the number and strength of supported
links from the target behavior; **duration and reversibility**; **distribution**, including
concentrated risk, vulnerable subgroups, and inequity; and **evidence certainty** from design,
directness, consistency, precision, and bias.

Do not collapse severity and evidence certainty into one score. A potentially grave but distal,
low-certainty consequence can rank as high possible severity with low confidence; it must not
silently outrank a moderate, direct, well-established consequence.

Use an ordinal synthesis with ties and conditional ranks, stating per consequence its rank,
confidence, decisive estimates and locators, causal-chain boundary, the assumptions under which the
rank changes, and the evidence that would move it. Compute no weighted composite unless the weights
have a defensible source; run a qualitative sensitivity analysis instead.

## 6. Completion and presentation

Mark the gate `CONSEQUENCE_RANKING_COMPLETE` only when every relevant layer has been searched with
an opened full copy behind every retained ranking source; the top-ranked consequence has direct
evidence or is labeled adjacent; magnitude, coverage, uncertainty, and practical meaning are
recorded; the causal chain and extrapolations are bounded; contradictory evidence and subgroup
differences are visible; and ranking sensitivity is stated. Otherwise use
`NEEDS_CONSEQUENCE_EVIDENCE`, or `NEEDS_AUTHOR_SOURCE_ACCESS` when the remaining gap requires a
human CAPTCHA, sign-in, subscription, or file transfer.

Present the ranked synthesis and its uncertainty before building the motivation decision packet, and
do not ask the author to rank, select, or approve consequences while this gate is incomplete. The
later motivation-frame gate may ask the author to select or combine evidence-grounded frames; the
evidence ranking stays independent of that rhetorical choice.
