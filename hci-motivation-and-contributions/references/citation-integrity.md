# HCI citation integrity contract

Contract version: `HCI-CITATIONS-4`

## Durable citation identity

- Maintain `references.csv` wherever a project cites external work:
  `citation_key,author_year,short_title,venue_abbrev,full_title,full_authors,full_venue,url,aliases`.
- One stable, unique `citation_key` per exact work. Preserve that key across phase handoffs; merge
  catalog rows instead of re-keying. Complete each record before publishing it; never guess its
  fields. Aliases are legacy conveniences: bibliographic, exact, unique.

## Claim-local placement and maximally split clusters

- Place each citation immediately after the smallest claim, result, construct, or keyword it
  supports, treating each independently supportable item in a coordinated list as its own citation
  atom. Repeat a work wherever it supports multiple distinct atoms, even within one sentence.
- A cluster has no numeric maximum, but every work in it must support the same smallest indivisible
  claim. Split clusters as finely as the evidence permits, in every profile.

## Output profiles

Select and record the profile before publishing, and name its deterministic citation gate.

### GitHub Markdown publication

- Cite as `[Author (Year Venue): Short Title][CitationKey]`, defining that exact key once per file:

  ```markdown
  [CitationKey]: <https://canonical.example/work> "Full authors. Full title. Full venue."
  ```

- Use one keyed link for each citation occurrence; works supporting the same indivisible claim may
  cluster as `([First work][FirstKey]; [Second work][SecondKey])`.
- Hyperlink every scholarly citation. Shorthand such as `Author et al. (Venue Year)` outside a keyed
  link fails the output gate, and backticks grant no exemption: an inline-code `` `[@Key]` ``
  publishes as the same keyed link, so keep literal citation-syntax examples in fenced code.
- A `[@CitationKey]` token may survive only in a draft or a structured narrative cell whose
  deterministic publication step resolves it.
- A migration publisher may replace an exact catalog-backed shorthand containing a parenthetical year
  only when the surface maps to exactly one stable key. Ambiguous or uncatalogued surfaces stay
  unresolved.
- Give every citation-bearing file a visible `References` section carrying the full authors, full
  title, full venue, canonical destination, and stable key of each used work, derived from
  `references.csv`, with descriptive link text.
- In a project-overview framing section, give each closest work enough context to state what it
  built, studied, operated, or demonstrated and how the focal project differs.

### Native manuscript publication

- A manuscript may use BibTeX/LaTeX commands, Pandoc/CSL `[@CitationKey]`, Word citation fields, or
  other rendering native to its recorded toolchain. Every citation and bibliography entry maps
  one-to-one to the same stable `references.csv` key.
- Run the selected manuscript toolchain's deterministic citation and bibliography validation before
  delivery, rejecting everything the fail-closed audit below names plus missing bibliography entries
  and unresolved citation commands. A durable `[@CitationKey]` is valid only inside a declared
  Pandoc/CSL profile whose build resolves it.

## Fail-closed publication and audit

Fail before delivery when a token or keyed link names an unknown key; keys are duplicated, including
case-folded collisions; an alias can resolve to more than one work; citation-like parenthetical
shorthand remains unresolved; an entry cannot map one-to-one to `references.csv`, or its metadata or
canonical identity differs from it; or an internal citation, cross-reference, or navigation target is
broken. Validate destination syntax and identity, but never make automated network reachability a
prerequisite: record blocked DOI/publisher reachability separately, since 401/403/429, CAPTCHA, or
bot protection does not invalidate a correct destination.

For the GitHub Markdown profile, additionally fail when file-local reference definitions are
duplicated or inexact; a used key lacks exactly one definition or visible full-reference entry; a
relative link is unresolved or a target is machine-local and absolute; or a raw `[@CitationKey]`
token remains outside code. Never fall back to fuzzy alias matching. HTML also requires hover/focus
metadata, accessible labels, and narrow-width headed-browser review; a manuscript requires a successful
citation/bibliography build with its key-to-catalog reconciliation record preserved.

## Cross-phase and future-skill gate

Read this contract before a phase's first citation-bearing artifact, and carry the current
`references.csv` in every handoff bearing cited claims. Every new `hci-*` skill must carry an exact
copy at `references/citation-integrity.md`, route to it from `SKILL.md`, provide
`assets/references.csv`, and include `references.csv` in its project workspace contract. The
repository-wide contract test scans all `hci-*` skills, so a phase lacking it fails.

## Read every identity off the copy itself

Read each retained source's identity off its own front matter — title page, byline,
masthead, or colophon, visually when a scan will not extract — and record where in the
`identity_verified_against` column of `source-resolution.csv`, naming the page, for example
`held copy p.1 title page, 2026-08-05`; `check_source_resolution.py` fails when a row holds a full
copy and this column is empty or names no place in it. Verify author count and order, given names,
diacritics, volume, issue, page range, and printed DOI or ISBN against that copy.

## Never store an identifier twice

A hand-maintained duplicate identifier in `source-manifest.md` once sent authors to the wrong
articles. The manifest's ledger-derived columns are therefore generated — run
`python3 scripts/render_source_manifest.py PROJECT_DIR` after any ledger change, never edit them by
hand — while its judgement columns (tier, directness, discovery route, ingestion status, provenance,
notes) survive regeneration. `check_source_resolution.py` reruns that derivation in memory and fails
on drift. The rule governs every author-facing page; mark a line that quotes a superseded identifier
to record a correction with the word `CORRECTION`, which exempts it from the broadcast check.
