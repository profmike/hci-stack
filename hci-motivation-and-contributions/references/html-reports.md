# Phase 1 HTML report contract

Generate HTML as a view over durable research artifacts, never as a second source of truth. Update
the Markdown/CSV artifacts first, then regenerate the reports with
`scripts/render_phase1_reports.py`.

## Project navigation invariant

Create a project-root `README.md` during workspace initialization. It must identify the project,
state that Markdown/CSV/JSON/YAML are the editable sources of truth, and link directly to:

- `research-framing/reports/phase-1-progress.html`;
- `research-framing/reports/literature-and-evidence.html`;
- `research-framing/reports/phase-1-final.html`; and
- `research-framing/reports/artifact-index.html`.

Generate and audit the initial report shelf in the same operation that creates the durable project
workspace. Regenerate it after every material evidence batch, decision packet, author choice, or
review. Before a commit, push, or terminal handoff, verify that the README and every linked report
exist in the exact tree being published. Missing or stale navigation/report files are blocking
delivery defects even when the editable research artifacts are otherwise valid.

## Source and reader-view boundary

Markdown and CSV are the authoritative, editable, diffable research record. Generate
`artifact-index.html` plus standalone HTML mirrors for the reader-facing audits, registers,
matrices, and ranked positioning dossier. These mirrors solve a reading and sharing problem; they
must never become independently edited sources. Link the artifact shelf prominently from
`literature-and-evidence.html`.

Keep complete limitations, counterevidence, non-claims, and reopen triggers in the evidence tables
and audit mirrors. Apply [claim-focused-writing.md](claim-focused-writing.md) to narrative
summaries: state supported active claims directly and include only qualifiers that materially
change those claims or comparisons. Do not repeat unrelated limitations as defensive disclaimers.
For general audiences, lead with the familiar term and define the exact scientific or technical
construct at first use.

## Required reports

### `phase-1-progress.html`

A live collaboration dashboard. Its first substantive section must be `Current state — read this
first`, before progress history, coverage tables, or artifact inventories. It must answer, without
requiring inference: where the direction stands; what is established, observed, and planned; what
is settled; which at most three decisions are ready now; the recommendation and real tradeoff for
each; the consequence of delay; blockers; and the immediate next action/owner. If no author
decision is ready, state that and identify the preceding evidence action. Link each decision to the
populated comparison or decision artifact that supports it, not an empty template. Then include:

- the live Phase 1 workboard, current coverage states, constructive-opposition entries, blockers,
  reopen triggers, and the next factual clarification batch or one consequential author question;
- starting state and imported-material status;
- current motivation, gap, approach, contribution, terminology-contract, lexical-hierarchy, and
  chart choices;
- every three-to-five-option portfolio presented to the author;
- the author's selections, combinations, rejections, delegation, rationale, and open decisions;
- motivation and related-work progress;
- the motivation-claim research queue, resolution routes, current-practice audit, and whether the
  active hypothesis/unsupported sweep is complete;
- the current consequence-severity ranking, confidence, sensitivity, and incomplete-gate status;
- evidence gaps, missing full copies, active `NEEDS_AUTHOR_SOURCE_ACCESS` requests, whether each
  request was surfaced in the conversation, risks, and reviewer synthesis;
- the source-resolution sweep, with no transient `UNASSESSED`, `DISCOVERED`, `ACQUIRING`, or
  `FULL_TEXT_OBTAINED` row presented as end-of-round closure;
- links to the other two reports; and
- generation time plus an artifact hash inventory.

Source counts, activity history, file lists, and detailed matrices remain useful traceability, but
they must follow the snapshot and cannot substitute for it.

Regenerate after any material research batch, decision packet, author choice, or review.

### `literature-and-evidence.html`

The dedicated research record. Include:

- source manifest and NotebookLM identifiers without credentials;
- the domain-authority map, including remit, document type/version, exact supported claim, and
  explicit cannot-support boundary;
- exact queries, databases/layers, dates, filters, screening counts, and exclusions;
- the related-work search-recall audit, including mechanism/problem synonym lattices,
  positive-control sentinels, large-result-set stopping rules, reference-title accountability, and
  late-found-work postmortems;
- whether each reference was present in author materials and independently found by the skill;
- full-copy acquisition, ingestion, and original-check status;
- every candidate source's `source-resolution.csv` state and, for blocked sources, the exact
  manual-download/access request, actual surfaced date/locator, affected claims, fallback or
  narrowing, and reopen trigger;
- source tier, directness, method, population/context, sample/coverage, findings, uncertainty,
  locator, and limitations;
- a short explanation that source tier, ingestion completeness, directness, and ES strength are
  independent axes, and that they are not the contribution-tier ladder;
- every active motivation/problem `hypothesis` or `unsupported` claim, its research route,
  strongest support/contradiction, and disposition;
- dated official current-practice capabilities, bypasses, and collision boundaries;
- the consequence chain, outcome inventory, evidence-calibrated severity ranking, subgroup
  heterogeneity, and ranking sensitivity;
- same-problem/different-approach and different-problem/similar-approach synthesis;
- backward and forward citation chains, including how newer work cites seed papers;
- every material prior-work atom's six independent accounting fields; demonstrated operation and
  capability collision separated from attributed contribution credit; demonstrated-unclaimed and
  claimed-undemonstrated states; mixed-channel, package, whole-system, and port/adaptation gates;
  and idea provenance with collision and credit `NONE`;
- imported-bibliography terminal accountability, late-found-work postmortems, repaired search
  routes, novelty regression sentinels, and the final complete zero-yield promotion wave;
- a ranked approximately-ten-work positioning dossier with one full working comparison paragraph
  per work, plus its ranking basis and re-ranking triggers;
- missing exact full copies, routes attempted, exact author action requested, whether the request
  was surfaced, and the fallback evidence boundary;
- exemplar analysis clearly separated from project evidence; and
- an artifact hash inventory.

Do not display a candidate as usable evidence until the exact full work has been checked. Keep
inaccessible works visible with an author-access status. A report may show an active acquisition
state while work continues, but it must not call the audit complete or end the round until the
source is fully assessed, specifically screened out before retention, superseded, or paired with an
exact surfaced `NEEDS_AUTHOR_SOURCE_ACCESS` request.

### `phase-1-final.html`

A decision-complete research-direction report. Include:

- selected research framing outline;
- evidence-state boundaries;
- all author choices and their rationale;
- all unselected and superseded alternatives in collapsible sections;
- reviewer findings and dispositions;
- readiness status and stop/go risks;
- optional Phase 2 handoff;
- links to the progress and literature/evidence reports; and
- generation time plus an artifact hash inventory.

The final report is not paper prose and must not imply that planned systems or studies exist.

### Reader-facing artifact shelf

Generate `artifact-index.html` and standalone mirrors for at least:

- `phase-1-collaboration-workboard.md`;
- `ranked-related-work-positioning.md`;
- `acm-sigchi-related-work-audit.md`;
- `related-work-search-recall-audit.md`;
- `related-work-matrix.md`;
- `related-work-contribution-tier-audit.md`;
- `prior-work-contribution-boundary.md`;
- `prior-work-evidence-accounting.csv`;
- `idea-provenance-ledger.csv`;
- `imported-bibliography-accountability.csv`;
- `late-found-work-postmortem.csv`;
- `novelty-regression-sentinels.yaml`;
- `evidence-strength-register.md`;
- `authoritative-source-map.md`;
- `consequence-severity-ranking.md`;
- `current-practice-audit.md`;
- `motivation-claim-research-queue.md`;
- `source-manifest.md`;
- `source-resolution.csv`; and
- `missing-full-copies.md`.

Generate a visible missing-source page instead of silently omitting a required mirror. Every mirror
must identify its source path and SHA-256 hash and use the same citation catalog, self-contained
styles, navigation, escaping, and accessibility rules as the three core reports.

The report auditor must require `source-resolution.html`,
`prior-work-evidence-accounting.html`, `idea-provenance-ledger.html`,
`imported-bibliography-accountability.html`, `late-found-work-postmortem.html`, and
`novelty-regression-sentinels.html`; a missing ledger mirror is a blocking defect, not an optional
artifact warning.

## Variation and choice preservation

Store each option portfolio in `decision-packets/` using the decision-packet template. Never
overwrite a packet after a decision; append the decision or create a superseding packet. Maintain
`author-decisions.md` as the cross-project index.

The renderer includes:

- every file under `decision-packets/`;
- `*-options.md` files;
- the related-work quadrant portfolio;
- the native ACM DL/SIGCHI coverage audit, including exact queries, inclusion/exclusion
  accountability, implemented-versus-proposed collisions, and broader-HCI situating synthesis; and
- the author decision log.

Use stable checkpoint names and dates so later phases can trace why a direction was chosen.

## Rendering rules

- Follow [citation-integrity.md](citation-integrity.md). In reader-facing source artifacts, write
  one explicit `[@CitationKey]` token per cited work; use
  `([@FirstKey]; [@SecondKey])` for multiple works.
- Maintain `references.csv` with these columns:
  `citation_key,author_year,short_title,venue_abbrev,full_title,full_authors,full_venue,url,aliases`.
  Separate optional exact aliases with `||`.
- Keep aliases bibliographic and unique. Never register a conceptual phrase, grouped author
  shorthand, or an ambiguous bare surname as an alias. Legacy exact-alias enrichment is a migration
  aid, not the authoring contract.
- Render every recognized citation as
  `Author (Year Venue): Short Title`, linked to its canonical DOI/publisher/official URL. For
  example: `Saiki et al. (2026 Front. Virtual Real.): Large-Scale MR Stadium`.
- Recognize the citation key, author-year forms, configured aliases, and the unambiguous short-title
  slug. This keeps title-only references such as “PanoCoach” linked and expanded into the same
  readable citation label.
- Put complete authors, full title, and full venue in both the link's native hover title and
  accessible label. Never guess missing bibliographic fields; complete the catalog first.
- Fail generation or audit on an unknown explicit key, duplicate key, alias collision, unresolved
  citation-like parenthetical shorthand, missing citation metadata, or broken destination. Never
  select the first of several possible references.
- Include a full anchored reference catalog in `literature-and-evidence.html`. When a work has no
  public canonical URL, link citations to that internal catalog entry.
- Produce standalone HTML with inline CSS and no remote fonts, scripts, analytics, or dependencies.
- Escape all artifact content before rendering.
- Embed generated SVG quadrant charts as data URLs when available.
- Display missing artifacts as missing rather than fabricating empty content.
- Include project-relative paths, modification times, and SHA-256 hashes.
- Keep full source PDFs as canonical private-repository files and link them by project-relative
  path rather than duplicating binary bytes inside generated HTML. Do not embed private raw
  participant data, credentials, cookies, or NotebookLM authentication files.
- Treat reports as potentially shareable: include only project artifacts approved for that
  audience.

## Post-render review

After generation, run:

```bash
python3 scripts/audit_phase1_reports.py PROJECT_DIR
```

Then inspect all three core reports, the artifact index, and each generated reader-facing mirror in
a headed browser at desktop and narrow widths. Review at least:

- tables with long evidence, equations, escaped pipes, and multiline cells;
- every citation style used in prose and CSV tables;
- explicit citation-key replacement, multi-work citations, and absence of unresolved bare-surname,
  slash-grouped, or truncated-title parentheticals;
- hover and keyboard-focus access to complete bibliographic metadata;
- canonical citation destinations and internal reference anchors;
- option portfolios and author-choice visibility;
- decision-first current-state prominence, no more than three active author decisions, and direct
  links or names for their populated decision-support artifacts;
- terminology definitions, non-implications, reserved terms, propagation conflicts, and separate
  semantic-contract versus lexical-hierarchy status;
- familiar-first definitions of scientific or technical terms, direct supported narrative, and no
  disclaimer about an outcome that the narrative does not claim;
- chart dimensions, labels, and overflow;
- raw Markdown escapes, HTML fragments, placeholders, or split cells;
- missing artifacts and misleading readiness language; and
- print layout when a report is intended for archival or sharing.

Fix the source artifact when the data is wrong; fix the renderer when the same presentation defect
could recur. Regenerate all reports and rerun both automated and visual review. Do not deliver a
report merely because the renderer exited successfully.
