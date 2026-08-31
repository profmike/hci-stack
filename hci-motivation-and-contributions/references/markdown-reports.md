# Phase 1 GitHub Markdown publication contract

Publish Phase 1 as linked Markdown that renders directly on GitHub. Do not generate HTML reports.
This layer is a reader view over the durable research record, never a second evidence source.

## Project navigation invariant

Create and maintain the project-root `README.md` from workspace initialization. Per
[iso-24495-1-plain-language.md](iso-24495-1-plain-language.md), declare readers and tasks in the
required `HCI-PLAIN-LANGUAGE` profile and apply its four reader outcomes — relevant, findable,
understandable, usable — without simplifying away evidence states. Evidence-status-aware, it
summarizes:

the sections of the `assets/project-readme.md` template — `## The user value` before the mechanism;
`## Introduction — structure and outline`, opening from a concrete behavior and consequence and
following the six-move order in [claim-focused-writing.md](claim-focused-writing.md);
the human problem and target context; and a `## Closest prior work` comparison in which every cited
work says **What it did:** and **How this project differs:**.

Never let a claim, decision, rejected variant, evidence gap, or reopen trigger exist only there.

Link the canonical records with relative links, all under `research-framing/`:
`phase-1-collaboration-workboard.md`; `research-framing-outline.md`;
`ranked-related-work-positioning.md`; `evidence-strength-register.md`; `author-decisions.md` and the
decision-packet index; `phase-2-handoff.md`; and `reports/README.md`.

Do not compress prior work into a label such as “progressive cues” plus a citation: name the smallest
demonstrated artifact, study, or finding and one literal difference. The auditor requires a
comparison bullet per framing citation with both bold labels.

## Publication files

`scripts/render_phase1_reports.py` emits Markdown only:

`reports/phase-1-progress.md`; `reports/literature-and-evidence.md`; `reports/phase-1-final.md`;
`reports/artifact-index.md`, listing every source artifact with status and SHA-256; and
`reports/README.md` plus Markdown mirrors of required CSV/JSON/YAML ledgers.

They never summarize claim content whose authoritative version lives elsewhere, and each records the
source paths and hashes so `scripts/audit_phase1_reports.py` rejects stale output.

Data mirrors include at least `references.md`; `source-resolution.md`;
`claim-evidence-ledger.md`; `prior-work-evidence-accounting.md`; `idea-provenance-ledger.md`;
`imported-bibliography-accountability.md`; `late-found-work-postmortem.md`;
`novelty-regression-sentinels.md`; and `agent-context.md`.

Render narrow CSV files as GitHub tables, wide ledgers as one record section per row so they stay
usable on phones, and JSON/YAML as fenced text linked to the canonical file. Missing sources
remain visible as `MISSING`; never fabricate one.

## All-Markdown navigation

Every Markdown file under `research-framing/` carries a managed navigation block linking back to the
README, artifact index, live workboard, and Phase 2 handoff. Compute paths from the file's directory
so nested files work on GitHub. The publication step maintains only that block and citation blocks;
it never rewrites research prose, decisions, evidence ratings, or statuses.

The auditor must reject a broken relative link or fragment; a link escaping the repository; a `file:`
URL or machine-local absolute path such as `/Users/...`; a live `.html` link or stale generated HTML
under `research-framing/reports/`; a Markdown artifact without that block; or a canonical artifact
unreachable from the README or artifact index. External HTTP(S) links are allowed with descriptive
labels; delivery never depends on a publisher accepting a probe.

## Citation publication

Follow [citation-integrity.md](citation-integrity.md); its GitHub Markdown profile and fail-closed
audit list govern here. Resolve each `[@CitationKey]` to
`[Author (Year Venue): Short Title][CitationKey]`, with one file-local definition and one
visible full-reference entry from `references.csv`. Place each citation after the smallest claim it
supports. Repeat the same
work wherever it supports another atom, including across items in one enumeration; a
multi-source cluster has no numeric cap only when every work supports the same indivisible atom.

## Report content requirements

`phase-1-progress.md` must make the decision-first current state the first substantive destination
and link to populated workboard and decision artifacts, not an empty template. The workboard in
`phase-1-collaboration-workboard.md` stays authoritative for readiness and evidence states,
decisions, blockers, contribution candidates and reopen triggers, `AUTHOR-DECLINED-EVIDENCE`, and
variant history. The report links each active decision to its packet; it may say no decision is
ready and name the preceding evidence action.

`literature-and-evidence.md` must link every Phase 1 evidence, source-access, search-recall,
positioning, accounting, provenance, and repair artifact. It may show
`NEEDS_AUTHOR_SOURCE_ACCESS` only with the surfaced-request fields required by
[author-collaboration.md](author-collaboration.md), and may not call a source audit complete while
a decision-relevant row stays transient.

## Publication and audit sequence

```bash
python3 scripts/check_prior_work_accounting.py PROJECT_DIR --end-of-round
python3 scripts/check_source_resolution.py PROJECT_DIR --end-of-round
python3 scripts/render_phase1_reports.py PROJECT_DIR
python3 scripts/audit_phase1_reports.py PROJECT_DIR
```

Use `--end-of-round` only for a declared research-round closure; for readiness, rerun both evidence
checkers with `--phase-ready` before publishing. Regenerate after every material evidence
batch, option portfolio, author decision, or review, and before every commit, push, or handoff.

Then preview the README, core reports, citation-dense files, and wide ledger mirrors on
GitHub or a local GitHub-Flavored Markdown renderer, checking desktop and phone
reading order, long tables, wrapped locators, and prospective-status language. Fix canonical content
when the record is wrong; fix the publisher when the defect can recur. Before claiming the overview
is usable under ISO 24495-1, ask an intended reader to restate the problem, evidence state, and next
action.
