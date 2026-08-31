# Forward-citation expansion protocol

Use this protocol during every related-work, component-foundation, seed-upgrade, and
decision-relevant methods search. A single cited-by click on the closest paper is discovery, not
forward-citation saturation. Forward-citation expansion complements rather than replaces
independent keyword, mechanism, author, venue, and backward-reference searches.
Citation graphs can be incomplete, stale, or disconnected, so keep diverse
canonical intervention-family and disciplinary seeds rather than one graph built
around preferred terminology.

## Build the high-leverage seed portfolio

The **high-leverage seed portfolio** is not just the closest contribution comparators. It also
holds every retained author-provided seed that could change an active claim or decision; canonical
intervention-family representatives with the strongest design/mechanism foundation and strongest
falsifier for each active component; reviews and methods precedents that organize a
decision-relevant literature; product or current-practice evaluations instantiating a material
control pattern; and every prior late find. Screen out sources with no active claim, component,
comparison, method, or decision role, recording the reason either way, and promote a lower-priority
source as soon as its full text introduces a new mechanism term, intervention family, adverse
effect, measurement approach, or citation path.

## Use independent cited-by routes

For every high-leverage seed, use at least two genuinely independent cited-by indexes when
available — ACM DL plus OpenAlex, Google Scholar plus Web of Science, Semantic Scholar plus a
publisher citation page. Two interfaces backed by the same underlying graph do not count as
independent routes. Record per route the seed identity and DOI, the provider, date, coverage,
filters, sort, and cited-by count, the records actually screened, each candidate's disposition, and
any access barrier, stale index, or count disagreement.

Search both **newest-first** and **relevance- or citation-ranked** views, querying citing titles,
abstracts, keywords, or full text with the problem, mechanism, component, outcome, failure-mode,
and methods vocabularies, screening for
decision relevance rather than title or semantic similarity alone. If only one route is lawfully
available, add an independent exact-title/author or mechanism query, retain the missing-route risk,
and keep the gate open when the uncovered graph could materially change a decision.

## Screen beyond one ranked prefix

Screen all unique citing records when tractable. For a large graph, never treat the first page,
first 20, or one relevance-ranked prefix as coverage: partition it — by year including the newest
incomplete indexing period, by venue or discipline, by problem and population, by mechanism or
intervention family, by outcome or evaluation method, and by newly learned vocabulary — and screen
every material partition to a documented no-new-relevant-work stopping point. Never discard a whole
partition because its title vocabulary looks distant.

## Expand in waves

1. **Wave 0 — seeds:** freeze the high-leverage seed portfolio and its roles.
2. **Wave 1 — direct citers:** run the independent cited-by routes for every Wave 0 seed and
   screen all material partitions.
3. **Promotion:** promote every newly retained work that changes a claim, comparator, mechanism,
   component foundation, failure mode, study design, or search vocabulary.
4. **Wave 2+ — promoted citers:** repeat the two-route expansion for every promoted work, add its
   new vocabulary to the synonym lattice, and rerun affected mechanism-only and component searches.
5. **Stop:** stop only after one complete promotion wave across every active seed produces zero
   new decision-relevant works, every unresolved candidate has entered source resolution, and the
   search is current through the recorded check date.

Do not recursively expand a citing work that is merely background, duplicate, or specifically
screened out. Seed families may run in parallel, but the lead agent deduplicates identities and
owns the stopping decision. Refresh the graph — recording the refresh date rather than claiming
permanent saturation — before a gap or contribution decision, before phase readiness, and after any
material mechanism or population change.

## Handle late-found work as a process failure

When a material paper surfaces after the pass was called complete, create or update
`late-found-work-postmortem.csv`:

1. identify the exact seed and cited-by route that should have surfaced it;
2. screen that seed's **sibling citing records**, not only the supplied paper, and repeat the
   expansion for every affected and newly promoted seed;
3. add a row to `novelty-regression-sentinels.yaml` that must recover the work through the repaired
   route without using its exact title or authors; and
4. rerun every affected downstream judgment, from evidence strength and capability collisions
   through contribution credit, ranking, gap, novelty, comparator, and study requirements.

If the paper has no citation relationship to an existing seed, repair the synonym lattice or
database coverage and add it as a new Wave 0 sentinel. “The paper was added” is not a postmortem:
the repair closes only when the sentinel passes and a complete repaired promotion wave yields zero
new decision-relevant work.

## Record candidates and evidence boundaries

Maintain the high-leverage seed inventory, wave ledger, and candidate accountability tables in
`related-work-search-recall-audit.md`, keyed by DOI-normalized identities so two services cannot
create duplicate sources. Every candidate that could affect an active decision enters
`source-resolution.csv` and needs full-text assessment, a specific screen-out, supersession, or an
exact author-access request before the round closes. A citation edge is discovery evidence only:
open the full work before using how it cites, extends, or criticizes a seed, and keep venue
priority separate from claim strength.

## Completion gate

Expansion is complete only when every rule above is recorded in
`related-work-search-recall-audit.md` — seed portfolio and route independence, screened counts and
stopping decisions, terminal source-resolution dispositions, any late-found repair, and the audit's
currency date with its residual database, indexing, language, and access risks — and one complete
promotion wave produced zero new decision-relevant works. Until then retain
`NEEDS_RELATED_WORK_SEARCH_RECALL_AUDIT` or `NEEDS_LANDSCAPE_RESEARCH`, and do not ask the author
to select a gap or contribution.
