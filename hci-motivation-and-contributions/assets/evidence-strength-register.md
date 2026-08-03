# Evidence-strength register

Status: `ACTIVE`

Last audited: YYYY-MM-DD

This is a claim-specific audit cache. It does not assign permanent quality scores to papers.
`FULL`/`PARTIAL`/`BROKEN` describes source ingestion; `ES3`/`ES2`/`ES1`/`ES0` describes support
for the named narrow claim.

## How to read one record

`[T2A | FULL | Adjacent | ES1]` means: a useful external source was fully opened, but it studies a
neighboring claim and therefore supplies context only for the named target. Source tier, ingestion,
directness, and evidence strength are separate axes. `ES3` is not “the best paper,” and `T1` does
not guarantee `ES3`.

These source tiers are unrelated to the related-work contribution ladder (`Tier 1 — capability`,
`Tier 2 — experience or outcome`, `Tier 3 — cost or access`).

## Evidence bar

| Tag | Meaning | Minimum use boundary |
|---|---|---|
| `FULL` | Relevant full methods, results, limitations, and supplements were obtained and opened | Eligible for `ES1`–`ES3` after audit |
| `PARTIAL` | Abstract, excerpt, repository record, institutional summary, or incomplete rendering | Identity or bounded abstract-level fact only |
| `BROKEN` | CAPTCHA, error/wrong page, failed import, or no intended source content | No evidentiary use |
| `ES3 ANCHOR` | Full, closely matched evidence with appropriate temporal/comparative leverage, interpretable uncertainty, and no critical risk-of-bias veto | May anchor only the named claim |
| `ES2 BOUNDED SUPPORT` | Full evidence with a material mismatch or validity limit | Association/bounded claim; corroborate before a major framing move |
| `ES1 CONTEXT ONLY` | Construct, lived experience, hypothesis, broad coverage, contradiction, or adjacent mechanism | Context only; no exact magnitude or causal claim |
| `ES0 DO NOT USE` | Inaccessible, invalid, fatally biased, or unable to support the named claim | Exclude from that claim |

## Critical-risk-of-bias veto

`ES3` is prohibited when allocation/comparison is unclear, reporting is internally inconsistent,
analysis is incompatible or materially underpowered, a multi-component effect is misattributed,
measurement/confounding/attrition/selective reporting can overturn the result, uncertainty is
missing, the source is not `FULL`, or a correction/version conflict is unresolved. Design labels,
sample size, venue prestige, and AI/NotebookLM ratings never override the veto.

## Source assessments

Every potentially decision-relevant source must also appear in `source-resolution.csv`.
`UNASSESSED` is transient: before an end-of-round summary, obtain and audit the full work or surface
an exact author-access request. Blocked rows preserve the actual surfaced date/locator, affected
claims, fallback or narrowing, and reopen trigger; superseded rows resolve to a different retained
and fully assessed replacement. Do not use this table as a parking lot for future acquisition.
Record whether a source began as an author-provided seed and the result of the independent
claim-matched upgrade/counterevidence search. Source provenance never raises the evidence grade.

| Source ID / citation | Provenance / seed status | NotebookLM source ID | Ingestion | Narrow supported claim | Strength | Direction / estimate / locator | Directness | Decisive limitation | Upgrade/counterevidence search and disposition | Re-review trigger | Auditor/date | Source-resolution state/locator |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pending | Independent / author-provided / imported bibliography | Pending | `UNASSESSED` | Pending | Pending | Pending | Pending | Pending | Pending; retain with bounds / corroborate / supersede | Claim, source version, evidence conflict, or decision-critical use changes | Pending | `ACQUIRING` — must become full-text assessed, specifically screened out, superseded, or an exact surfaced author-access request before the round ends |

## Reuse rule

Reuse a row without re-reading the whole source only when the source/version and proposed construct,
population, context, exposure, outcome, comparator, causal wording, and precision requirement are
unchanged. Re-review when any of those change; when a partial source becomes full; when new direct
contradictory evidence appears; when a correction/retraction is issued; or when the source becomes
decision-critical. Unmarked sources are `UNASSESSED`; that label starts the acquisition loop and
never closes it.

## NotebookLM reconciliation

| Date | Notebook/conversation | NotebookLM assessment | Manual audit decision | Disagreement and resolution |
|---|---|---|---|---|
| YYYY-MM-DD | Pending | Pending | Pending | Pending |
