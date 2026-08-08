# Phase 1 GitHub Markdown publication contract

Publish Phase 1 as linked Markdown that renders directly on GitHub. Do not generate HTML reports.
The Markdown publication layer is a traceable reader view over the durable research record, never a
second evidence or decision source.

## Project navigation invariant

Create the project-root `README.md` during workspace initialization and maintain it throughout the
phase. Read [iso-24495-1-plain-language.md](iso-24495-1-plain-language.md) and declare the intended
readers and tasks in the required `HCI-PLAIN-LANGUAGE` profile. Apply ISO 24495-1's four reader
outcomes—relevant, findable, understandable, and usable—without simplifying away evidence states,
claim boundaries, author decisions, or reopen triggers. It must contain a concise,
evidence-status-aware summary of:

- `## The user value`, stated before the mechanism;
- `## Introduction — structure and outline`, ordered from problem and residual gap through the
  platform-independent approach to its implementation substrate and planned evidence;
- the human problem and target context;
- a `## Closest prior work` comparison in which every cited work says **What it did:** and
  **How this project differs:**;
- the planned or demonstrated approach;
- the leading prospective contribution statements, with stable candidate IDs and evidence gates;
- current readiness, blockers, and the next decision/action; and
- the historical-input/non-decision boundary when imported drafts exist.

Start with `## At a glance` and state the answer and current evidence status before background.
Keep the detailed closest-work comparison in its own `## Closest prior work` section so readers can
find it without turning the opening into a literature review.
Use `## Continue by task` instead of one undifferentiated link inventory, with two or more reader
goals and descriptive links. Keep the current decision, blocker, or next action directly findable
in the README. Automated audit enforces this structure; intended-reader review determines whether
the wording is actually understandable and usable.

The README is a bounded overview. It must link to the exact canonical records that contain evidence
boundaries and author choices, including:

- `research-framing/phase-1-collaboration-workboard.md`;
- `research-framing/research-framing-outline.md`;
- `research-framing/ranked-related-work-positioning.md`;
- `research-framing/evidence-strength-register.md`;
- `research-framing/author-decisions.md` and the decision-packet index;
- `research-framing/phase-2-handoff.md`; and
- `research-framing/reports/README.md` and the four principal Markdown reports.

Use relative repository links. Never make the README the only place where a claim, decision,
rejected variant, evidence gap, or reopen trigger exists.

Do not compress prior work into labels such as “progressive cues,” “reflection,” or “contextual
intervention” followed by a citation. For each cited closest work, name the smallest demonstrated
artifact, study, capability, or finding that matters and one literal focal-project difference.
Keep planned focal capabilities prospective. The auditor must require exactly one comparison bullet
per framing citation and both bold field labels; human review remains responsible for whether the
two fields are evidence-bounded and substantively informative.

## Publication files

`scripts/render_phase1_reports.py` emits Markdown only:

- `reports/phase-1-progress.md` — links the current-state snapshot, workboard, decisions, blockers,
  source access, and immediate next action;
- `reports/literature-and-evidence.md` — links the evidence, source, search, related-work,
  contribution-boundary, and full-copy records;
- `reports/phase-1-final.md` — links the selected outline, contribution portfolio, terminology,
  decisions, readiness risks, and Phase 2 handoff;
- `reports/artifact-index.md` — lists every required source artifact with status and SHA-256; and
- `reports/README.md` plus Markdown mirrors of required CSV/JSON/YAML ledgers.

The core reports are navigation and provenance views. They do not duplicate or silently summarize
claim content whose authoritative version lives elsewhere. Each records the exact source paths and
hashes used, so `scripts/audit_phase1_reports.py` can reject stale output.

The required data mirrors include at least:

- `references.md`;
- `source-resolution.md`;
- `claim-evidence-ledger.md`;
- `prior-work-evidence-accounting.md`;
- `idea-provenance-ledger.md`;
- `imported-bibliography-accountability.md`;
- `late-found-work-postmortem.md`;
- `novelty-regression-sentinels.md`; and
- `agent-context.md`.

Render narrow CSV files as GitHub tables. Render wide ledgers as one record section per row so they
remain usable on phones. Render JSON/YAML as fenced source text with a direct link to the canonical
file. Missing required sources remain visible as `MISSING`; do not fabricate a placeholder source.

## All-Markdown navigation

Every Markdown file under `research-framing/` must carry a managed navigation block linking back to
the project README, Phase 1 artifact index, live workboard, and Phase 2 handoff. Compute paths from
the file's directory so nested files work on GitHub. The publication step may maintain only this
bounded block and citation blocks in canonical Markdown; it must not rewrite research prose,
decisions, evidence ratings, or statuses.

The auditor must reject:

- a broken relative file link or fragment;
- a link that escapes the repository;
- a `file:` URL or machine-local absolute path such as `/Users/...`;
- a live `.html` report link or stale generated HTML under `research-framing/reports/`;
- a Markdown artifact without the managed internal navigation block; or
- a required canonical artifact that is unreachable from the root README or artifact index.

External HTTP(S) links are allowed and must use descriptive labels or GitHub autolink syntax.
Automated delivery does not depend on publisher sites accepting a network probe.

## Citation publication

Follow [citation-integrity.md](citation-integrity.md). Maintain `references.csv` with:

`citation_key,author_year,short_title,venue_abbrev,full_title,full_authors,full_venue,url,aliases`.

Before delivery, resolve every temporary `[@CitationKey]` in Markdown to:

```markdown
[Author (Year Venue): Short Title][CitationKey]
```

Append one file-local definition and one visible full-reference entry for every used key. Derive
both from `references.csv`. The stable key remains explicit in Markdown source and downstream tools
can recover manuscript identity without parsing visible prose.

Fail publication or audit on unknown or case-folded duplicate keys, duplicate definitions,
ambiguous aliases, unresolved citation shorthand, raw draft tokens outside code, mismatched labels,
noncanonical destinations, missing metadata, missing visible reference entries, or broken internal
targets. The publisher may migrate an exact, unique catalog-backed shorthand with a parenthetical
year to its stable keyed link. An ambiguous or uncatalogued author/title/venue/year shorthand and a
generic `Author et al. (Venue Year)` citation must fail rather than be guessed. Do not enrich text
through fuzzy matching. A normal external link that is not being used as a scholarly citation may
remain a normal Markdown link.

## Current-state and variation preservation

`phase-1-progress.md` must make the decision-first current state the first substantive destination.
It must link to the populated workboard and decision artifacts, not an empty template. The workboard
remains authoritative for:

- direction/readiness and established, observed, planned, hypothesis, aspiration, or unsupported
  states;
- at most three consequence-ordered decision-ready questions;
- recommendations, tradeoffs, blockers, next action, and owner;
- contribution-candidate stable IDs, types, evidence gates, and reopen triggers;
- constructive-opposition entries and `AUTHOR-DECLINED-EVIDENCE`; and
- selected, combined, rejected, delegated, and superseded variants with author rationale.

The generated report must link every active decision to its populated packet. It may say no author
decision is ready and name the preceding evidence action.

## Literature and source-access visibility

`literature-and-evidence.md` must directly link the source-resolution view, evidence register,
authority map, current-practice audit, claim-research queue, search-recall and ACM/SIGCHI audits,
ranked positioning, prior-work accounting, idea provenance, seed accountability, late-find repairs,
novelty sentinels, source manifest, NotebookLM maintenance, and missing-copy record.

An end-of-round publication may show `NEEDS_AUTHOR_SOURCE_ACCESS` only when the exact request,
canonical URL, attempted routes, surfaced date/locator, affected stable claim IDs,
fallback/narrowing, and reopen trigger are present. It may not call a source audit complete while a
decision-relevant row remains transient.

## Publication and audit sequence

Run:

```bash
python3 scripts/check_prior_work_accounting.py PROJECT_DIR --end-of-round
python3 scripts/check_source_resolution.py PROJECT_DIR --end-of-round
python3 scripts/render_phase1_reports.py PROJECT_DIR
python3 scripts/audit_phase1_reports.py PROJECT_DIR
```

Use `--end-of-round` only for a declared bounded research-round closure. For readiness, rerun both
evidence checkers with `--phase-ready` before publishing.

Regenerate after every material evidence batch, option portfolio, author decision, or review, and
before every commit, push, or terminal handoff containing material Phase 1 changes. The auditor
must verify report hashes, README links, citation integrity, managed navigation, required data
mirrors, source-access visibility, no stale HTML, and no machine-local links.

After automated checks pass, preview the root README, four core reports, citation-dense files, wide
ledger mirrors, and nested navigation on GitHub or a local GitHub-Flavored Markdown renderer. Check
desktop and phone reading order, long tables, wrapped locators, visible references, decision
prominence, terminology, missing artifacts, and prospective-status language. Fix canonical content
when the record is wrong; fix the publisher when a presentation defect can recur. Ask an intended
reader to locate and accurately restate the problem, evidence state, closest-work difference,
current decision, and next action before claiming the overview is usable under ISO 24495-1.
