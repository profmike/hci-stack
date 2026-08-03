# HCI citation integrity contract

Contract version: `HCI-CITATIONS-1`

This contract applies to every current and future `hci-*` skill in this repository.

## Durable citation identity

- Maintain `references.csv` in every project workspace that cites external work, using:
  `citation_key,author_year,short_title,venue_abbrev,full_title,full_authors,full_venue,url,aliases`.
- Give each exact work one stable, unique `citation_key`. Preserve that key across phase handoffs;
  merge catalog rows instead of re-keying the same work.
- Complete the bibliographic record before rendering it. Never guess authors, title, venue, or URL.
- Treat aliases as legacy/discovery conveniences. Every alias must be bibliographic, exact, and
  unique. Do not use a conceptual claim, mechanism label, or author surname shared by multiple
  works as an alias.

## Reader-facing authoring

- Cite with an explicit key token: `[@CitationKey]`.
- Cite multiple works with one token per work, for example
  `([@FirstKey]; [@SecondKey])`.
- Never rely on a bare surname, a grouped shorthand such as `Ruiz/Alin`, a truncated title, or
  fuzzy/semantic matching to create a hyperlink.
- Keep the claim or concept in prose and put the citation token after it. Do not make a conceptual
  phrase such as “normative dissociation” an alias that a renderer will replace with a paper title.
- Use the same key in Markdown, CSV narrative cells, decision records, handoffs, reports, and later
  manuscript-facing artifacts.

## Fail-closed rendering and audit

Any HCI skill that renders or publishes reader-facing artifacts must fail before delivery when:

- an explicit token names an unknown key;
- citation keys are duplicated;
- an alias can resolve to more than one work;
- citation-like parenthetical shorthand remains unresolved;
- a rendered citation lacks its canonical destination, complete hover metadata, or accessible
  label; or
- an internal citation target is broken.

Render explicit tokens deterministically as `Author (Year Venue): Short Title`. Legacy exact-alias
enrichment may remain for old artifacts, but it must never override explicit tokens or silently
choose among collisions. Hover/focus metadata must contain the full authors, full title, and full
venue, with equivalent native-hover and accessible labels. Do not add fuzzy citation matching as a
fallback.

Automated checks are necessary but not sufficient. Inspect citation-dense passages and narrow-width
HTML in a headed browser before delivery.

## Cross-phase and future-skill gate

- Read this contract before writing the first citation-bearing artifact in a phase.
- Include the current `references.csv` in every phase handoff that contains citation-bearing
  claims, preserving stable keys and provenance.
- Every new `hci-*` skill must carry an exact copy at `references/citation-integrity.md`, route to it
  from `SKILL.md`, provide `assets/references.csv`, and include `references.csv` in its project
  workspace contract.
- The repository-wide contract test must scan all `hci-*` skills so adding a future phase without
  this contract fails validation.
