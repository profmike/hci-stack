# Related-work search-recall audit

Status: `NEEDS_RELATED_WORK_SEARCH_RECALL_AUDIT`

Last checked: YYYY-MM-DD

This audit tests whether the search process can retrieve close work expressed in unexpected
vocabulary. It complements the ACM/SIGCHI landscape audit; it does not estimate statistical recall
or prove that no unseen work exists.

## Target-problem identity contract

- **Target people:**
- **Focal activity:**
- **Triggering or temporal context:**
- **Unwanted state or episode:**
- **Intended change or outcome:**
- **Hypothesized mechanisms kept separate from the problem identity:**
- **Last reopened and why:**

## Mechanism and problem synonym lattice

Build terms independently before combining them. Populate terms from the project description,
known seeds, index terms, titles/abstracts, and the Related Work sections of close full papers.

| Dimension | Search terms and controlled vocabulary | Terms added from close papers | Queries using this dimension |
|---|---|---|---|
| Target people / activity | | | |
| Context / transition | | | |
| Human problem / construct | | | |
| Access state | | | |
| Changed parameter | | | |
| Progression variable | | | |
| Interaction or intervention mechanism | | | |
| Outcome / tradeoff | | | |

## Independent retrieval routes

| Route | Exact query, seed, or source | Date / filters / sort | Result count | Records/pages screened | Retained works and problem-proximity bands | Stopping criterion and result |
|---|---|---|---:|---:|---|---|
| Native ACM problem query | | | | | | |
| Native ACM mechanism-only query | | | | | | |
| Native ACM closest conjunction | | | | | | |
| Same/similar-problem saturation branch | | | | | | |
| Backward reference-title triage | | | | | | |
| Forward cited-by route A | | | | | | |
| Forward cited-by route B | | | | | | |
| Exact-title/author verification | | | | | | |
| Independent scholarly index or web route | | | | | | |

## Positive-control and sentinel recall

Select known close works only after the synonym lattice is drafted. Each sentinel should be
retrievable by at least one query that does not simply use its exact title or author.

| Sentinel close work | Why it must be retrievable | Non-title query expected to retrieve it | Retrieved? / rank or page | Failure diagnosis and query repair |
|---|---|---|---|---|
| | | | | |

## High-leverage forward-citation seed portfolio

Include closest and conditional comparators, retained author seeds, strongest active-component
foundations/falsifiers, decision-relevant syntheses/methods, evaluated product/current-practice
lineage, and prior late finds.

| Seed key and full identity | Role and active claim/component/decision | Why high leverage | Route A | Route B | Coverage current through | Expand, exclude, or promote rationale |
|---|---|---|---|---|---|---|
| | | | | | | |

## Forward-citation expansion wave ledger

Search newest-first and relevance/citation-ranked views. Screen all unique citing records when
tractable; otherwise record the year, venue/discipline, problem, mechanism/component,
outcome/failure, and methods partitions used. A single ranked prefix is not coverage.

| Wave | Seed key | Cited-by route and sort/partition | Provider count | Unique records screened | Retained / excluded / unresolved | New vocabulary or branch | Promoted seeds for next wave | Zero-yield/stopping result |
|---:|---|---|---:|---:|---|---|---|---|
| 0 | | seed inventory | | | | | | |
| 1 | | | | | | | | |

Stop only after a complete promotion wave across every active seed yields zero new
decision-relevant works and every material unresolved candidate has entered source resolution.

## Forward-citation candidate accountability

| Candidate identity / DOI | Citing relationship and wave | Include, exclude, acquire, or supersede | Specific decision relevance or exclusion | Full-copy/source-resolution state | Evidence/ranking/claim artifact affected |
|---|---|---|---|---|---|
| | | | | | |

## Reference-list title accountability

For each closest full paper, triage every title that could plausibly share the problem, causal
mechanism, access state, progression variable, or outcome tradeoff.

| Seed full paper | Plausible reference/citation title | Include, exclude, or acquire | Specific rationale | Full-copy/access state |
|---|---|---|---|---|
| | | | | |

## Supplied-bibliography accountability

Imported references are discovery seeds, not author decisions. Account for every item that could
affect an active problem, component, mechanism, outcome, comparison, or study requirement. The
canonical machine-checkable ledger is `imported-bibliography-accountability.csv`; this table is a
human-readable summary.

| Supplied artifact | Bibliographic item | Independent discovery route | Claim-matched authority/method/directness upgrade search | Stronger/counter source found | Include, bounded, corroborated, superseded, acquire, or exact screen-out | Role if retained | Source-resolution state |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Use `retained with explicit bounds` when the seed has a unique role but is weaker or less direct;
use `corroborated` when stronger claim-matched evidence agrees; use `superseded` only when a named
replacement more defensibly covers the intended role. Preserve the original seed and replacement
locators so downstream analysis can reconstruct the decision.

## Late-found-close-work postmortem

Complete this section whenever a close comparator appears after a landscape was called saturated.
The canonical machine-checkable incident rows are in `late-found-work-postmortem.csv`; retrieval
tests are in the JSON-compatible YAML file `novelty-regression-sentinels.yaml`.

| Late-found work | Why it is materially close | Route that should have found it | Exact process failure | Search/ranking/claim changes made | Regression sentinel added |
|---|---|---|---|---|---|
| | | | | | |

## Coverage and stopping decision

- **Same/similar-problem saturation:** State the final independent problem-space pass, eligible work
  count, zero-yield result, and any residual shortage/risk. Mechanism-only results cannot satisfy
  this item.
- **Separate portfolios:** Confirm that different-problem mechanism/capability collisions and
  concept/theory/foundations were retained without entering the primary problem-space ranking.
- **Large-result-set handling:** First-page screening never establishes coverage for a large result
  set. Record how the query was refined, paginated, stratified, or stopped.
- **Independent-route convergence:** Name at least two independent routes for each top comparator,
  or record the missing route as a risk.
- **Forward graph:** Record the high-leverage seed portfolio, two genuinely independent cited-by
  routes, newest and relevance/citation views, large-graph partitions, promotion waves, and the
  final complete zero-yield wave.
- **Last complete pass:** Record the pass in which no materially closer work was found.
- **Residual blind spots:** State database, language, indexing, date, paywall, terminology, and
  disciplinary limits.
- **Claims rerun after late discovery:** novelty, gap, contribution tier, ranking, fair comparator,
  capability collision, contribution credit, and broader-HCI positioning.
- **Regression-sentinel recheck:** Record each non-title/non-author query, retrieval route, result,
  and last check date.

## Gate checklist

- [ ] Independent problem and mechanism synonym lattices are populated.
- [ ] Target-problem identity is operationalized without importing the proposed mechanism.
- [ ] Same/similar-problem search is saturated independently before the primary ranking; a shortage
      is disclosed rather than padded with distant work.
- [ ] Every retained work has a problem-proximity band and separate portfolio assignment.
- [ ] Mechanism-only/disjunctive queries were run, not only target-heavy conjunctions.
- [ ] Large result sets have a declared pagination/refinement stopping rule; first 20 alone is not
      treated as coverage.
- [ ] Positive-control close works are retrieved or each failure has been repaired and documented.
- [ ] Plausible mechanism titles in every closest full paper's references were accounted for.
- [ ] The high-leverage seed portfolio includes comparators, retained author seeds, active
      component foundations/falsifiers, decision-relevant syntheses/methods, and prior late finds.
- [ ] Each high-leverage seed has two independent cited-by routes or a visible unavailable-route
      risk plus a compensating independent search.
- [ ] Newest and relevance/citation views and every material large-graph partition were screened;
      no single ranked prefix was treated as coverage.
- [ ] Every decision-changing or vocabulary-expanding work was promoted into the next citation
      wave, and one complete wave produced zero new decision-relevant works.
- [ ] Plausibly relevant items in supplied bibliographies were independently searched and
      recorded in `imported-bibliography-accountability.csv`; every material entry has terminal
      source resolution and none remains a future-tense `UNASSESSED` acquisition task.
- [ ] Every retained author-provided seed has a documented claim-matched upgrade search; venue
      prestige was not used as an evidence-strength proxy.
- [ ] Backward, multi-wave forward, and independent-index routes were completed.
- [ ] Each top comparator has two independent discovery routes or a visible residual risk.
- [ ] Every late-found material work triggered a sibling-citation sweep, regression sentinel,
      graph repair, completed `late-found-work-postmortem.csv` row, passing non-title retrieval,
      and rerun of affected evidence, capability collisions, contribution credit, rankings, claims,
      and study requirements.
- [ ] A complete rerun found no materially closer unreviewed work within the stated scope.

Gate: `NEEDS_RELATED_WORK_SEARCH_RECALL_AUDIT`
