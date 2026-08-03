# Forward-citation expansion protocol

Use this protocol during every related-work, component-foundation, seed-upgrade, and
decision-relevant methods search. A single cited-by click on the closest paper is discovery, not
forward-citation saturation.

Forward-citation expansion complements rather than replaces independent keyword, mechanism,
author, venue, review, and backward-reference searches. Citation graphs can be incomplete, stale,
or disconnected, and a relevant new work may cite none of the seeds already retained. Maintain
diverse canonical intervention-family and disciplinary seeds rather than building one graph around
project-preferred terminology.

## Contents

- [Build the high-leverage seed portfolio](#build-the-high-leverage-seed-portfolio)
- [Use independent cited-by routes](#use-independent-cited-by-routes)
- [Screen beyond one ranked prefix](#screen-beyond-one-ranked-prefix)
- [Expand in waves](#expand-in-waves)
- [Handle late-found work as a process failure](#handle-late-found-work-as-a-process-failure)
- [Record candidates and evidence boundaries](#record-candidates-and-evidence-boundaries)
- [Completion gate](#completion-gate)

## Build the high-leverage seed portfolio

Do not limit forward expansion to the approximately ten closest contribution comparators. Before
searching, inventory:

1. every closest comparator and conditionally close alternative;
2. every retained author-provided seed that supports or could change an active claim or decision;
3. canonical intervention-family representatives plus the strongest design/mechanism foundation
   and strongest falsifier for each active component;
4. current systematic reviews, authoritative syntheses, and methods precedents that organize a
   decision-relevant literature;
5. current-practice or product-intervention evaluations that instantiate a material control
   pattern; and
6. every late-found work that changed vocabulary, positioning, contribution level, design,
   evaluation, or an evidence boundary.

Classify these as the **high-leverage seed portfolio**. A large bibliography does not make every
item high leverage: screen out sources with no active claim, component, comparison, method, or
decision role. Record the reason for both inclusion and exclusion. Promote a lower-priority source
when its full text introduces a new mechanism term, intervention family, adverse effect,
measurement approach, review, or citation path that could change the project.

## Use independent cited-by routes

For every high-leverage seed, use at least two genuinely independent cited-by indexes or scholarly
routes when available—for example ACM DL plus OpenAlex, Google Scholar plus Web of Science or
Scopus, Semantic Scholar plus a publisher citation page, or another claim-appropriate
combination. Two interfaces backed by the same underlying graph do not count as independent
routes.

For each route, record:

- exact seed identity and stable DOI or canonical locator;
- route/provider, search date, date coverage, filters, and sort;
- cited-by count shown by the provider;
- records actually screened and the pages, partitions, or exports used;
- duplicates and version merges;
- retained, excluded, unresolved, and full-copy-required candidates; and
- any provider limitation, access barrier, stale index, or citation-count disagreement.

Search both **newest-first** and **relevance- or citation-ranked** views. New work can be highly
relevant before it accumulates citations, while older influential work can be buried by a
newest-only view. Query within citing titles, abstracts, keywords, or full text using the problem,
mechanism, component, outcome, failure-mode, and methods vocabularies. A title need not name the
component it evaluates. Screen for decision relevance rather than title or semantic similarity
alone.

If only one cited-by route is lawfully available, add an independent exact-title/author or
mechanism query, retain the missing-route risk, and keep the gate open when the uncovered graph
could materially change a decision.

## Screen beyond one ranked prefix

Screen all unique citing records when tractable. For a large graph, never treat the first page,
first 20, or one relevance-ranked prefix as coverage. Partition the graph by:

- publication year, including the newest incomplete indexing period;
- venue or disciplinary community;
- problem and population;
- mechanism, component, access state, or intervention family;
- outcome, adverse effect, or evaluation method; and
- exact phrases and newly learned vocabulary.

Screen every material partition to a documented no-new-relevant-work stopping point. Record
excluded candidates at the level needed to reproduce the decision; do not silently discard a
whole partition because its title vocabulary looks distant. Deduplicate preprints, accepted
manuscripts, conference papers, journal extensions, corrections, and publisher versions while
preserving their lineage.

## Expand in waves

Run forward expansion as a bounded graph traversal:

1. **Wave 0 — seeds:** freeze the high-leverage seed portfolio and its roles.
2. **Wave 1 — direct citers:** run the independent cited-by routes for every Wave 0 seed and
   screen all material partitions.
3. **Promotion:** promote every newly retained work that changes a claim, comparator, mechanism,
   component foundation, failure mode, study design, or search vocabulary.
4. **Wave 2+ — promoted citers:** run the same two-route forward expansion for every promoted
   work. Add any new vocabulary to the synonym lattice and rerun affected mechanism-only and
   component searches.
5. **Stop:** stop only after one complete promotion wave across every active seed produces zero
   new decision-relevant works, every unresolved candidate has entered source resolution, and the
   search is current through the recorded check date.

Do not recursively expand a citing work that is merely background, duplicate, or specifically
screened out. This keeps the graph bounded without cutting off new branches that alter the
research direction. Run independent seed families in parallel when possible; the lead agent must
deduplicate identities, reconcile classifications, and own the stopping decision.

Refresh the forward graph before a gap/contribution decision, before phase readiness, after a
material mechanism or population change, and after a long enough interval that newly indexed work
could change the landscape. Record the refresh date rather than claiming permanent saturation.

## Handle late-found work as a process failure

When the author or a later search supplies a material paper that the completed pass missed, create
or update `late-found-work-postmortem.csv`:

1. verify whether it cites, is cited by, shares an author with, or uses vocabulary from any
   retained seed;
2. identify the exact seed and cited-by route that should have surfaced it;
3. screen the missed paper's **sibling citing records** from that seed, not only the supplied
   paper;
4. repeat the expansion for every affected seed and any newly promoted work;
5. add a row to `novelty-regression-sentinels.yaml` that must recover the work through the repaired
   citation route without using its exact title or authors; and
6. rerun affected evidence strength, operated-capability accounting, capability collisions,
   contribution credit, comparison ranking, gap, novelty, contribution tier, fair comparator,
   study requirements, and broader-HCI positioning.

If the paper has no citation relationship to an existing seed, repair the synonym lattice or
database coverage and add the paper as a new Wave 0 sentinel. “The paper was added” is not a
postmortem. Do not close the repair until the sentinel passes and a complete repaired promotion
wave yields zero new decision-relevant work.

## Record candidates and evidence boundaries

Maintain the high-leverage seed inventory, wave ledger, and candidate accountability tables in
`related-work-search-recall-audit.md`. Use stable keys or DOI-normalized identities so two services
cannot create duplicate sources. Every candidate that could affect an active decision enters
`source-resolution.csv`; complete full-text assessment, a specific screen-out, supersession, or an
exact author-access request before declaring the round closed.

A citation edge is discovery evidence only. It does not establish agreement, quality, directness,
or evidence strength. Open the full work before using how it cites, extends, criticizes, or
replicates a seed. Keep venue priority separate from claim strength.

## Completion gate

Forward-citation expansion is complete only when:

- the high-leverage seed portfolio covers comparators, active component foundations/falsifiers,
  retained author seeds, decision-relevant syntheses/methods, and prior late finds;
- each seed has two independent cited-by routes, or a documented unavailable-route risk and
  compensating independent search;
- newest-first and relevance/citation-ranked views and all material large-graph partitions were
  screened with counts and stopping decisions;
- every promoted decision-changing or vocabulary-expanding work received another forward wave;
- one complete promotion wave produced zero new decision-relevant works;
- every material candidate has a terminal full-text/source-resolution disposition;
- late-found work triggered a completed postmortem, sibling sweep, passing non-title regression
  sentinel, affected-claim/collision/credit rerun, and repaired zero-yield wave; and
- the audit records its currency date and residual database, indexing, language, and access risks.

If any item is missing, retain `NEEDS_RELATED_WORK_SEARCH_RECALL_AUDIT` or
`NEEDS_LANDSCAPE_RESEARCH`. Do not ask the author to select a gap or contribution.
