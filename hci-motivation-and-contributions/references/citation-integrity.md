# HCI citation integrity contract

Contract version: `HCI-CITATIONS-3`

This contract applies to every current and future `hci-*` skill in this repository.

## Durable citation identity

- Maintain `references.csv` in every project workspace that cites external work, using:
  `citation_key,author_year,short_title,venue_abbrev,full_title,full_authors,full_venue,url,aliases`.
- Give each exact work one stable, unique `citation_key`. Preserve that key across phase handoffs;
  merge catalog rows instead of re-keying the same work.
- Complete the bibliographic record before publishing it. Never guess authors, title, venue, or URL.
- Treat aliases as legacy/discovery conveniences. Every alias must be bibliographic, exact, and
  unique. Do not use a conceptual claim, mechanism label, or author surname shared by multiple
  works as an alias.

## Claim-local placement and cluster limit

- Place each citation immediately after the smallest claim, result, construct, or keyword it
  supports. Do not collect sources at the end of a sentence or paragraph when they support
  different propositions.
- Prefer one citation at each supported claim. When two sources jointly support the same smallest
  claim, they may share one cluster. Never put more than two citations in one cluster.
- When three or more sources matter, split the prose into distinct supported claims and place each
  source beside its relevant claim. Keep the complete source portfolio in the internal evidence
  record or a dedicated related-work synthesis rather than compressing it into a citation pile.
- These placement rules apply to GitHub Markdown and native manuscript profiles. Rendering syntax
  may differ, but source scope and proximity may not.

## Output profiles

Select and record the output profile before publishing. All profiles preserve the same
`references.csv` keys and complete bibliographic identity; presentation syntax is profile-specific.

### GitHub Markdown publication

- In Markdown that people read on GitHub, cite each work as
  `[Author (Year Venue): Short Title][CitationKey]` and define that exact key once in the file:

  ```markdown
  [CitationKey]: <https://canonical.example/work> "Full authors. Full title. Full venue."
  ```

- Use one keyed link per work. When exactly two works jointly support the same smallest claim, use
  `([First work][FirstKey]; [Second work][SecondKey])`.
- Hyperlink every scholarly citation. An author/title/venue/year shorthand such as
  `Author et al. (Venue Year)` or `System Name (Venue Year)` outside a keyed link is unfinished and
  must fail the output gate, even when the same work is linked elsewhere in the file.
- A migration publisher may replace an exact catalog-backed shorthand that contains a parenthetical
  year only when the surface maps to exactly one stable key. Ambiguous or uncatalogued surfaces must
  remain unresolved for explicit authoring; never guess through context or semantic similarity.
- A temporary `[@CitationKey]` token may be used while drafting or inside a structured narrative
  cell only when the phase's deterministic GitHub publication step resolves it before delivery.
  Raw `[@CitationKey]` is never a finished GitHub-facing citation.
- Backticks do not exempt a scholarly citation: an exact inline-code form such as `` `[@Key]` ``
  must publish as the same keyed link. Keep literal citation-syntax examples inside fenced code;
  the output audit rejects an inline-code token that survives publication.
- Derive the visible label, destination, and metadata from `references.csv`; authors do not hand-copy
  or redefine bibliographic identity in prose.
- Give every citation-bearing Markdown file a visible `References` section containing the full
  authors, full title, full venue, canonical destination, and stable key for every used work. The
  visible section is the keyboard, touch, and accessibility fallback for optional link-title hover.
- Never rely on a bare surname, grouped shorthand such as `Ruiz/Alin`, truncated title, or
  fuzzy/semantic matching to create a hyperlink.
- Keep the claim or concept in prose and put the keyed citation after it. Do not make a conceptual
  phrase such as “normative dissociation” an alias that a publisher will replace with a paper title.
- In a project-overview framing section, give every cited closest work enough local context to state
  what it built, studied, operated, or demonstrated and how the focal project differs. A list of
  mechanism labels plus links is not a positioning summary.
- Preserve the same key in Markdown, CSV narrative cells, decision records, handoffs, publication
  views, and later manuscript-facing artifacts.

### Native manuscript publication

- A manuscript may use BibTeX/LaTeX commands, Pandoc/CSL `[@CitationKey]`, Word citation fields,
  or venue-required numeric/author-year rendering when that syntax is native to its selected,
  recorded manuscript toolchain.
- Every manuscript citation and bibliography entry must map one-to-one to the same stable
  `references.csv` key and complete bibliographic record. Native rendering may change visible
  labels, ordering, and numbering; it may not change source identity or metadata.
- Run the selected manuscript toolchain's deterministic citation and bibliography validation before
  delivery. Reject unknown/duplicate keys, missing bibliography entries, metadata drift, unresolved
  citation commands, and broken internal cross-references. A durable Pandoc `[@CitationKey]` is valid
  only inside a declared Pandoc/CSL manuscript profile whose build resolves and validates it.

## Fail-closed publication and audit

Every output profile must fail before delivery when:

- a draft token or keyed link names an unknown key;
- citation keys are duplicated, including case-folded collisions;
- an alias can resolve to more than one work;
- citation-like parenthetical shorthand remains unresolved;
- a citation or bibliography entry cannot map one-to-one to `references.csv`;
- full metadata or canonical identity differs from `references.csv`; or
- an internal citation, cross-reference, or navigation target is broken.

Under the GitHub Markdown profile, additionally fail when file-local reference definitions are
duplicated; a citation's visible label or canonical destination differs from `references.csv`; a
used key lacks exactly one definition or visible full-reference entry; or a raw `[@CitationKey]`
token remains outside code. Publish GitHub keys deterministically as
`Author (Year Venue): Short Title`. Legacy exact-alias enrichment may remain for migration, but it
must never override a keyed citation or silently choose among collisions. Do not add fuzzy citation
matching as a fallback.

Validate external destination syntax and canonical identity without making automated network
reachability a publication prerequisite. Record blocked DOI/publisher reachability separately;
401/403/429, CAPTCHA, or bot protection does not by itself make a correct scholarly destination
invalid. For an HTML output profile, additionally require equivalent hover/focus metadata,
accessible labels, narrow-width inspection, and headed-browser review. For the GitHub Markdown
profile, require descriptive link text, exact file-local definitions, visible full references,
resolved relative links, and no machine-local absolute link targets. For a native manuscript
profile, require a successful citation/bibliography build or equivalent deterministic toolchain
audit and preserve its key-to-catalog reconciliation record.

## Cross-phase and future-skill gate

- Read this contract before writing the first citation-bearing artifact in a phase.
- Name the selected output profile and its deterministic citation gate before delivering any
  citation-bearing artifact; GitHub-facing Markdown and manuscript outputs may use different gates.
- Include the current `references.csv` in every phase handoff that contains citation-bearing
  claims, preserving stable keys and provenance.
- Every new `hci-*` skill must carry an exact copy at `references/citation-integrity.md`, route to it
  from `SKILL.md`, provide `assets/references.csv`, and include `references.csv` in its project
  workspace contract.
- The repository-wide contract test must scan all `hci-*` skills so adding a future phase without
  this contract fails validation.

## Read every identity off the copy itself

Wrong authors, wrong titles, and wrong page ranges enter a project the same way every time. Someone
types the identity out of a bibliography, a database record, a search result, or another paper's
reference list, and nobody ever opens the held copy's own front matter to contradict it. The error
then survives every consistency check in the workspace, because every later copy of that identity
descends from the same bad transcription and agrees with it perfectly.

So the identity of every retained source is read from that source's own front matter: its title
page, byline, masthead, running head, or colophon. Record where, in the `identity_verified_against`
column of `source-resolution.csv`, naming the page — for example `held copy p.1 title page,
2026-08-05`. A scan that will not extract to text is not exempt: read it visually and record the
page. `check_source_resolution.py` fails when a row holds a full copy and this column is empty or
names no place in that copy.

Verify these axes against the copy: every author's full given and family name, the author count and
order, the exact title wording, the year, the venue or journal name, the volume and issue, the page
range, and any DOI or ISBN the copy prints. A name the ledger abbreviates that the copy spells out
is a discrepancy worth recording, as is a diacritic the ledger dropped.

## Never store an identifier twice

An identifier that exists in two places will diverge, and the copy the author acts on is the one
that goes wrong. `source-manifest.md` used to hold a hand-maintained duplicate of the ledger's
identifiers; a correction made in the ledger never reached the page, and a mistranscription made on
the page was never contradicted by the ledger. Authors were sent to the wrong articles.

The manifest's ledger-derived columns are therefore generated. Run
`python3 scripts/render_source_manifest.py PROJECT_DIR` after any ledger change, and never edit
those columns by hand. The manifest-only judgement columns — tier, directness, discovery route,
ingestion status, provenance, notes — are preserved untouched by regeneration and remain
hand-maintained. `check_source_resolution.py` runs the same derivation in memory and fails on any
drift, so the duplicate cannot return.

The same rule governs every other author-facing page. When a page must quote a superseded
identifier in order to record the correction, mark that line with the word `CORRECTION`, which
exempts it from the broadcast check.
