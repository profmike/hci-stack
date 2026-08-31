# Evidence and citation protocol

Keep **source tier**, **ingestion completeness**, **claim directness**, and
**claim-specific evidence strength** as four independent dimensions: a prestigious venue does not
make every statement strong evidence. A record such as `[T2A | FULL | Adjacent | ES1]` carries one
value per dimension, defined below; the same source takes different `ES` labels for different
claims. The contribution-strength ladder
(`Tier 1 — capability`, `Tier 2 — experience or outcome`, `Tier 3 — cost or access`) ranks what a
project may contribute; it does not rate evidence.

## Source tiers

**T1 — authoritative or strongest published evidence:** official statistics from a body with the
relevant remit, evidence syntheses, strong primary studies, and highly relevant peer-reviewed
work; use the original dataset or primary study. An authoritative body counts only within its
verified remit and in the role of the exact document used. Read [authoritative-domain-sources.md](authoritative-domain-sources.md) and
maintain `authoritative-source-map.md`. Authority never overrides ingestion, directness, recency,
document type, or the claim-specific `ES` audit. Prioritize CHI and the current official SIGCHI
sponsored/co-sponsored roster for related-work coverage; that priority
does **not** automatically assign `T1`, increase directness, repair bias, or upgrade an `ES`
label.

**T2A — useful published or external evidence:** adjacent venues, industry reports, telemetry,
official specifications or release records. State conflicts of interest and opacity; never treat
an industry survey with undisclosed recruitment, weighting, or instruments as population truth.

**T2B — the authors' evidence:** their own formative studies, log analysis, pilots, and
evaluations, reported with limitations, de-identified, kept inside the sampled population and
context.

## Claim support levels

**Direct** — same construct, population, context, relationship. **Inferred** — a bounded
conclusion the source does not state; keep it out of the default prior-work contribution boundary,
and never use source silence to infer an absent capability. **Adjacent** — a neighbor with the
difference named. **Analogy** — motivates a hypothesis or design transfer only. Prefer T1 direct
evidence, except that T2B direct evidence may be strongest for a novel, narrow need published work
has not studied. Prevalence, trend, causal, and equivalence wording each require the matching
design; absent it, bound the wording. Absence of published work is not proof that no work exists:
state the databases, queries, dates, and scope behind a novelty claim — distinct from a bounded
inference about one fully checked system.

## Reusable evidence-strength register

Maintain `evidence-strength-register.md` on two independent axes.

**Ingestion completeness.** `FULL`: the version needed for the assessment — methods, results,
limitations, supplements — was obtained and opened. `PARTIAL`: an abstract, excerpt, or partial
rendering, usable for identity or a narrow abstract-level fact but never a methods-dependent
claim. `BROKEN`: CAPTCHA, error page, failed import, or the wrong content, supplying no evidence.

**Claim-specific evidence strength**, judged for one named narrow claim, not for prestige or
overall study quality; a null finding retains strength when its design supports the bounded null.

- `ES3 ANCHOR`: a `FULL` primary or authoritative source matching construct, population, context,
  exposure/outcome, and relationship, with stated uncertainty and no risk-of-bias veto.
- `ES2 BOUNDED SUPPORT`: a `FULL` supporting source whose material limit — design, self-report,
  exposure mismatch, selected population, weak precision — forces bounded wording.
- `ES1 CONTEXT ONLY`: definition, lived experience, hypothesis, coverage, contradiction, or
  adjacent mechanism, unable to quantify or establish it.
- `ES0 DO NOT USE`: `BROKEN`, incomplete, or fatally flawed for the claim.

### Critical-risk-of-bias veto

`ES3` is prohibited while a critical issue remains in the part of the study supporting it:
incoherent allocation, comparison, exposure, or outcome construction; analysis incompatible with
the design or missing uncertainty; a component credited from a multi-component
intervention; attrition, selective reporting, confounding, or measurement validity that plausibly
overturns the result; an item not `FULL` or under correction; or stated limitations. A design
label such as "RCT", a large sample, or
venue prestige never overrides this veto.
NotebookLM ratings never override the veto.

### Cache and re-review rule

Each register row names the supported claim, ingestion tag, strength tag, direction, decisive
estimate/locator, decisive limitation, auditor/date, and re-review trigger. Reuse it without
re-reading only while the source version, the claim and its scope, and the known corrections and
risk-of-bias information are unchanged, and re-review when it becomes decision-critical. An
unmarked source is `UNASSESSED`, not implicitly `ES1`.

### Source-resolution rule

`UNASSESSED` describes missing assessment; it is never a terminal grade or end-of-round
disposition. Enter every potentially decision-relevant candidate in
`source-resolution.csv` when it is discovered, and continue until it is audited into a completed
register row; screened out by a documented check showing it cannot affect an active claim,
comparison, rank, or study requirement; superseded by a verified stronger source with the
consequence recorded; or blocked behind human-only access after lawful routes were tried and an
exact `NEEDS_AUTHOR_SOURCE_ACCESS` request was surfaced to the author. At phase readiness every
HTTP(S) `references.csv` citation key needs a resolution row, and only explicitly classified
`internal:` project evidence is exempt. A supersession must name a different retained, fully
assessed source with a stable citation key; a human-access state keeps the surfaced-request
date/locator, affected claims, fallback, and reopen trigger.

### Lawful acquisition routes to exhaust before declaring a source blocked

A `403` from an automated fetcher usually means bot detection, not absent entitlement. Cloudflare's
"Just a moment…" interstitial and similar challenges block the tool, not the reader. Do not record
`NEEDS_AUTHOR_SOURCE_ACCESS` on that signal alone. Drive the author's already-authenticated,
already-entitled headed browser instead, and try these routes in order:

1. **Direct fetch** with normal headers, for open-access and repository copies.
2. **The author's headed browser, using the attachment-disposition parameter.** For ACM Digital
   Library, appending `?download=true` to the PDF path makes the server respond with
   `Content-Disposition: attachment`, so the browser writes the file to its download directory:

   ```
   https://dl.acm.org/doi/pdf/<DOI>?download=true
   ```

   This changes only the response disposition and asserts no entitlement the session lacks: an
   unentitled session still receives the paywall page.
3. **Preflight the browser's download settings before the batch.** For Chrome, read (never write)
   `~/Library/Application Support/Google/Chrome/<Profile>/Preferences` and confirm
   `download.prompt_for_download` is `false` and `savefile.default_directory` is expected. If a
   prompt is configured, ask the author to change it; do not change it yourself.
4. **Publisher-neutral fallbacks**: Unpaywall, the institutional repository, author's page.

Rename publisher-assigned filenames (ACM uses `<prefix>.<suffix>.pdf`) to the repository
convention when copying into `research-framing/sources/full-text/`, keeping the original
identifier in the resolution row.

Never ask for, read, copy, or reuse passwords, cookies, session tokens, or browser profiles. Driving
a browser the author already controls is permitted; extracting its authentication material is not.
This route serves entitled access; it is not a paywall, CAPTCHA, or sign-in bypass. When a source is
genuinely unentitled, return to the `NEEDS_AUTHOR_SOURCE_ACCESS` path.

Record every supplied draft, bibliography, and reading-list entry in
`imported-bibliography-accountability.csv`; their presence makes them neither author decisions nor
evidence. Every materially relevant entry must reach a terminal `source-resolution.csv` row and,
when retained, its six-field accounting row — never a future-tense "obtain full copy" task inside a
completed audit. A downloaded file is only `FULL_TEXT_OBTAINED` until its methods,
results, limitations, and corrections have been reviewed.

### Author-provided seeds do not set the evidence ceiling

For every author-provided or imported source retained for a material claim, document an
independent upgrade search across these axes: institutional authority and remit; design validity,
causal identification, risk of bias, and coverage; directness to construct, population, context,
exposure, comparator, and outcome; currency, correction state, and contradictory evidence; and
publication quality. Never convert a venue label, citation count, institutional brand, or author
preference into evidence strength. Retain the seed while it remains uniquely direct but bound its
claim; mark it `SUPERSEDED` only when the replacement covers its evidentiary role more defensibly,
keeping the replacement locator and consequence. Reconcile any NotebookLM rating against the
opened original and record the disagreement rather than voting.

## Quantitative claims and citation verification

For each number, record what was measured, over what unit, period, sampling, and method; whether it
is an observed count, estimate, prediction, or marketing claim; and its uncertainty, denominator,
comparator, and locator. Use numbers only where they sharpen magnitude, trajectory, mismatch, or
validation. Resolve source identity through a stable identifier, check corrections, retractions,
and supersessions, and re-open the cited passage during the sentence-level audit.

## Prior-work six-field evidence accounting

Read [prior-work-contribution-boundaries.md](prior-work-contribution-boundaries.md) for the
decision procedure and labels; maintain `prior-work-evidence-accounting.csv`,
`idea-provenance-ledger.csv`, and the human-readable `prior-work-contribution-boundary.md`. For
every material prior-work or focal-project atom, record `AUTHOR CLAIM`,
`DEMONSTRATED ARTIFACT OR STUDY`, `OPERATED CAPABILITY`, `EVALUATED RESULT`,
`CAPABILITY COLLISION`, and `CONTRIBUTION CREDIT` independently: no field inherits truth from
another. Collision requires positive evidence that the smallest named operation ran plus a diff of
the complete human-activity predicate; credit requires an explicit author claim with matched
demonstration; both are bounded to the weakest supported unit, people, activity, comparator,
outcome, causal rung, and timeframe. `DEMONSTRATED_UNCLAIMED` takes credit `NONE`,
`CLAIMED_UNDEMONSTRATED` takes neither collision nor credit, and proposals, future work, and
unverified implementation claims go to `idea-provenance-ledger.csv` with
`CAPABILITY COLLISION=NONE` and `CONTRIBUTION CREDIT=NONE`. Assign `OPERATED CAPABILITY=NO` only
from positive artifact evidence about the audited version; source silence may create only
`SEARCH_PRIORITY` or `REOPEN_QUERY`.

## Evidence sufficiency by framing move

- **Context and why now:** authoritative facts on scale or trajectory, plus official
  release/capability evidence and the adoption, exposure, or contextual change.
- **Pain and gap:** direct user evidence with an evidence-ranked consequence, severity separate
  from confidence; primary papers/products carried through six-field evidence accounting, with
  collisions separated from attribution and proposals and silence excluded.
- **Approach and contribution:** enabling mechanism, adopted foundations, likely costs, an
  explicit line between implemented facts and plans, and a reusable capability or knowledge
  hypothesis with its Phase 2–3 evidence.

Before choosing a motivation frame, apply
[consequence-severity-research.md](consequence-severity-research.md). Do not use prevalence as
severity, significance as practical importance, cross-sectional association as causality, or
general downstream harms as though the target behavior established every causal step.

## Inherited foundations and reader-facing boundaries

A checked external source may establish a general mechanism, design fact, or measurement
relationship the project adopts. Do not demand a redundant project study because the project uses
that foundation; require project-specific evidence when the active claim concerns the
exact artifact, parameter value, implementation fidelity, coverage, dose, robustness, or
downstream effect. Keep the full uncertainty record internally; per
[claim-focused-writing.md](claim-focused-writing.md), a limitation enters narrative prose only
when it materially constrains a claim the text actually makes, and an unclaimed distal outcome
needs no prophylactic disclaimer.
