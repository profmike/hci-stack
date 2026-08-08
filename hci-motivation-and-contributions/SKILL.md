---
name: hci-motivation-and-contributions
description: |
  Interactively collaborate with authors to develop and rigorously validate the
  motivation, related-work landscape, research gap, novel approach, and
  prospective contributions of an HCI project. Maintain a live Phase 1 workboard,
  research decision-relevant evidence before asking authors to choose, and
  constructively challenge unsupported high-impact assumptions. Use when
  researchers need to determine whether they are solving the right problem,
  strengthen an early or in-progress research direction, investigate full-text
  prior work, position an approach, or prepare a research framing outline or
  GitHub-previewable Markdown research records before design, implementation, evaluation, or writing.
  Accepts any starting materials; outputs from HCI Office Hours or another prior
  phase are helpful but never required.
---

# HCI Motivation and Contributions

Help researchers solve the **right problem** before expensive design, implementation, and evaluation choices become fixed. Produce a defensible research direction and outline, not polished manuscript prose.

## Phase contract

Every phase is independently enterable. This is Phase 1 of:

`problem screening → motivation and contributions → design/build → validation → visuals → writing → video`

Never require an Office Hours brief or another prior-phase artifact. Accept any starting material.
Import prior conclusions as evidence-bounded hypotheses, not approved premises. Office Hours remains a complete standalone experience.

Read [pipeline-contract.md](references/pipeline-contract.md) when deciding phase scope or preparing the handoff. Read [exemplar-routing.md](references/exemplar-routing.md) before using full exemplar papers. Exemplars teach research structure and communication; they are not project evidence.

In scope: problem importance and timeliness, evidence status, current practice, related work,
terminology, gaps, approach hypotheses, positioning, prospective contributions, and Phase 2/3
evidence needs.

Out of scope: final Abstract, Introduction, Related Work, or paper prose; final design,
architecture, implementation, study approval, final analysis, publication figures, or claims of
effectiveness and generality not yet established. Inspect later-phase artifacts only to understand
the direction; do not grade their absence.

## Required reference routing

- Read [active-author-collaboration.md](references/active-author-collaboration.md), then
  [author-collaboration.md](references/author-collaboration.md), before the first consequential question or decision.
- Before executing Steps 1–13, read [phase-1-research-workflow.md](references/phase-1-research-workflow.md)
  completely.
- Before durable project writes, read [repository-boundaries.md](references/repository-boundaries.md).
- Before the first citation-bearing artifact, read [citation-integrity.md](references/citation-integrity.md).
- Before motivation research or claim assessment, read [evidence-protocol.md](references/evidence-protocol.md),
  [authoritative-domain-sources.md](references/authoritative-domain-sources.md), [research-discovery-recall.md](references/research-discovery-recall.md),
  [motivation-claim-strengthening.md](references/motivation-claim-strengthening.md), and
  [consequence-severity-research.md](references/consequence-severity-research.md).
- Before translating evidence into author discussion, report narrative, outline language, or downstream writing
  guidance, read [claim-focused-writing.md](references/claim-focused-writing.md).
- Before NotebookLM setup or ingestion, read [notebooklm-research.md](references/notebooklm-research.md).
- Before related-work search and comparison, read [acm-sigchi-related-work.md](references/acm-sigchi-related-work.md),
  [forward-citation-expansion.md](references/forward-citation-expansion.md), and
  [related-work-positioning.md](references/related-work-positioning.md), then read
  [prior-work-contribution-boundaries.md](references/prior-work-contribution-boundaries.md) before defining a
  prior-work boundary, gap, scope, or contribution comparison.
- Before terminology, charts, and type-specific contribution packages, read
  [terminology-contract.md](references/terminology-contract.md),
  [related-work-quadrant.md](references/related-work-quadrant.md),
  [hci-contribution-types.md](references/hci-contribution-types.md), and
  [contribution-rubric.md](references/contribution-rubric.md).
- Before constructive review and report generation, read [reviewer-panel.md](references/reviewer-panel.md) and
  [markdown-reports.md](references/markdown-reports.md), then
  [iso-24495-1-plain-language.md](references/iso-24495-1-plain-language.md).

## Non-negotiable operating rules

### Collaborate actively before converging

Maintain `phase-1-collaboration-workboard.md` and repeat:

`inspect → research → assess → challenge → compare → recommend → author decides → record → propagate → recheck`

Lead every author-facing update, handoff, and progress report with a decision-first current-state snapshot:
direction/readiness, established/observed/planned, settled boundaries, at most three consequence-ordered decisions with recommendations/tradeoffs, blockers, and next action/owner. State when no decision is ready. History and artifact inventories are supporting evidence; never make the author infer the current state or needed decision from them.

Research decision-relevant evidence and contradictions before asking the author to choose. Do not
treat an idea dump, draft, populated template, or fluent synthesis as completion. Present three to
five substantively different options when that many are defensible, recommend one, ask one
consequential question at a time, and preserve selected, combined, rejected, superseded, and
delegated variants.

Apply **constructive opposition** as a standing rule: author preference may choose among defensible
paths, but it cannot become evidence or waive a critical gap. State the precise mismatch and
consequence, then offer bounded research, existing-artifact verification, a decision-matched study
or probe when warranted, a better-supported alternative, a narrower claim, or a visible block. If
necessary evidence is declined, record `AUTHOR-DECLINED-EVIDENCE`, narrow or block the claim,
propagate the consequence, and retain a reopen trigger.

### Keep the session interactive and parallelize evidence work

At the start of each nontrivial research batch, tell the author what is running, why it matters,
and which next discussion it prepares. Use available subagents by default for bounded literature
retrieval, full-text audit, citation-chain expansion, stronger/counter-source search, related-work
analysis, and claim tracing unless the task explicitly needs author help. Keep one lead agent as
the sole writer, evidence integrator, workboard owner, and author-facing collaborator. Reconcile
the findings before changing claims or opening a decision gate; do not return only a silent batch
of generated documents.

Ask the author to help only with lawful access or CAPTCHA/authentication in their browser, locating
missing project artifacts, tacit project facts, values, constraints, resources, or consequential
choices that inspection and research cannot recover. Do not shift routine literature search or
analysis to the author. If subagents are unavailable, continue locally rather than blocking.

### Keep project data in the project repository

Resolve the target project repository before durable writes. Until it is known, keep starting
state and the live workboard in the session only; continue read-only inspection, research, and
interactive planning. Never put project research data in the reusable skill repository or an
arbitrary workspace. Once resolved, create `research-framing/` without overwriting existing work
and instantiate the relevant `assets/` templates there.

Create and maintain `research-framing/agent-context.json` as the host-neutral pointer manifest for
Codex `$gpt-pro` and Claude Code `/gpt-pro`. It must name this exact active skill, point only to
canonical repository-relative Phase 1 artifacts, and keep its NotebookLM ID/title/profile
synchronized with the source manifest. It is not a transcript or duplicate decision record. Never
put credentials, absolute machine paths, raw participant data, or copied conversation history in
it.

### Mirror full sources into both private project stores

Treat the project repository and its NotebookLM notebook as private, governed project stores.
Copyright, license, and redistribution status must not block, delay, or require separate
per-source author confirmation for saving a full source in the project repository, tracking it in
version control, or uploading it to the project's NotebookLM notebook.
Do not add ignore rules, omit NotebookLM sources, or keep only metadata because a source is
copyrighted or lacks an open license. Store a canonical repository copy of every retained full
source under `research-framing/sources/full-text/` and mirror it into NotebookLM by default. Record
both the repository-relative path and NotebookLM source ID; if a technical failure prevents one
copy, record and repair that discrepancy rather than treating it as policy-compliant completion.

This private copyrighted-source rule does not reclassify credentials, authentication material,
identifiable participant data, confidential peer-review material, or unrelated third-party
secrets as research sources. Continue to keep those categories out of the repository and
NotebookLM unless a separate, explicit data-governance decision authorizes them.

### Ground every retained claim in complete sources

Every retained reference must have an obtained, saved, and opened full copy. Abstracts, snippets,
AI summaries, and secondary paraphrases may discover candidates but cannot ground claims or
comparisons. Maintain stable `references.csv` keys and follow `HCI-CITATIONS-2`: GitHub Markdown
uses keyed links plus catalog-derived definitions and visible full references; resolve all draft
tokens and hyperlink every citation shorthand. Unknown/duplicate identities, missing metadata, and broken links block delivery.

Record each material claim's method, population/context, sample or coverage, result, uncertainty,
limitation, and exact locator. Keep ingestion completeness separate from claim strength in
`evidence-strength-register.md`; apply the critical-risk-of-bias veto before `ES3`. An unmarked
source is unassessed, not strong. `UNASSESSED` is a transient acquisition state, never an
acceptable disposition when declaring a bounded source audit or research round closed. Track every
such candidate in `source-resolution.csv`; obtain and audit its full text, screen it out before
retention with a specific relevance reason, supersede it, or surface an exact
`NEEDS_AUTHOR_SOURCE_ACCESS` request. Never deliver an “audit complete” report whose next action is
merely to obtain the papers. Before phase readiness, reconcile every external HTTP(S) key in
`references.csv` bidirectionally with that ledger; classify project evidence explicitly with an
`internal:` URL. A blocked-access row must record an actual surfaced date/locator, affected stable
claims, fallback or narrowing, and reopen trigger. A superseded row must resolve to a different
retained `FULL_TEXT_ASSESSED` row with a stable citation key.
At every bounded audit closure, inventory all candidate source files in the governed project
source/import roots and reconcile each identity with `source-resolution.csv`; record the roots,
counts, unresolved files, and `LOCAL_SOURCE_FILES_RECONCILED` marker in `source-manifest.md`.

**Read every identity off the copy itself, and never store an identifier twice.** Read each
retained source's authors, title, year, venue, and pages from the held copy's own front matter and
record where, in `identity_verified_against`. Generate the ledger-derived columns of
`source-manifest.md` with `render_source_manifest.py`; never retype them. See
[citation-integrity.md](references/citation-integrity.md).

For every material prior-work or focal-project atom, complete the six independent fields in
`prior-work-evidence-accounting.csv`: `AUTHOR CLAIM`, `DEMONSTRATED ARTIFACT OR STUDY`,
`OPERATED CAPABILITY`, `EVALUATED RESULT`, `CAPABILITY COLLISION`, and `CONTRIBUTION CREDIT`.
No field inherits truth from another. Compare the smallest positively evidenced operation against
the focal capability's complete human-activity predicate, not against isolated adjectives. A
demonstrated but unclaimed operation can create a capability collision only at the matched human
capability or independently claimed sub-capability scope; it receives no attributed contribution
credit. Record it as `DEMONSTRATED_UNCLAIMED`. A claimed but undemonstrated atom is
`CLAIMED_UNDEMONSTRATED` and receives neither capability nor contribution credit.

**An idea with no demonstration and no study collides with nothing.** Ask only whether an artifact
ran the named operation and whether an evaluation measured the named result. If both answers are
no, record `NONE` in both columns however closely the idea resembles the focal atom. Venue is the
prompt to check, never the verdict; see
[prior-work-contribution-boundaries.md](references/prior-work-contribution-boundaries.md).

Route proposals, future work, interpretations, and hypothetical scenarios only to the idea
provenance record in `idea-provenance-ledger.csv`, with both collision and credit `NONE`. An
explicit author claim that a realized capability exists without matched evidence remains visible as
a `CLAIMED_UNDEMONSTRATED` accounting row and never gains either. Decompose mixed systems channel by channel and reject whole-system labels
unless every required channel is demonstrated. Treat source silence only as `SEARCH_PRIORITY` or
`REOPEN_QUERY`, never as capability, absence, collision, or credit. A platform, hardware, sensor,
OS, app, or game port earns credit only through a demonstrated nontrivial adaptation, demonstrated
new use class, or directly validated empirical finding.

Treat every author-provided citation, draft bibliography, and reading list as an **initial
discovery seed**, never the final evidentiary choice. For each retained seed, independently search
for claim-matched sources with stronger institutional authority, methodological/causal rigor,
directness, currency, or publication review. Record the upgrade search and whether the seed is
retained with bounds, corroborated, or superseded. Venue prestige alone never upgrades evidence.

### Escalate human-only source access

Exhaust the lawful acquisition routes in [evidence-protocol.md](references/evidence-protocol.md),
and continue non-dependent research, before asking for help. A `403` from an automated fetcher is
normally bot detection, not absent entitlement; drive the author's already-entitled headed browser
rather than escalating on it. For a genuinely blocked source, record the exact citation, DOI/canonical
URL, attempted routes, obstacle, why it matters, and fallback boundary in `missing-full-copies.md`.
Then ask for one concrete action: university IP/library access or a VPN, a lawfully obtained PDF, a
CAPTCHA or institutional sign-in completed by the author, or an authorized link.

Never ask for passwords, cookies, session tokens, browser profiles, or copied authentication
material. If access remains blocking, use `NEEDS_AUTHOR_SOURCE_ACCESS`; do not substitute an AI
summary or stop at writing `missing-full-copies.md`. After the author supplies a download or says
the authenticated page is ready, locate and open the exact full work, complete its source and
claim audit, update the resolution records, and resume the blocked analysis.

### Use one NotebookLM notebook per project

Use Gemini NotebookLM through `notebooklm-mcp-cli` for source organization and synthesis. Create a
new notebook per project, use headed Chrome for authorized access, store notebook/source IDs but no
credentials, and write the resolved notebook ID, title, and profile to both `source-manifest.md`
and `agent-context.json`. Also link the notebook's `notebooklm.google.com/notebook/<id>` URL at
the top of the project's root `README.md` so the author can open it in one click; keep that link
current after any notebook change. Keep those records synchronized after any notebook/profile change and
persist the vetted evidence bar and source markings. Treat NotebookLM ratings as review aids that
must be reconciled against opened originals. Keep the notebook human-readable:
maintain a `START HERE` evidence map, verify imports contain the intended work, use readable
bibliographic/role titles, replace broken imports, and reconcile unassessed, duplicate, and
superseded objects after every bounded research round. Preserve unique evidence and obtain explicit
author confirmation for the exact source-ID set before any irreversible NotebookLM deletion.

### Keep unfinished claims unfinished

Use these states:

- `established-external`
- `inferred-external`
- `observed-project`
- `planned`
- `hypothesis`
- `aspiration`
- `unsupported`

Never convert `planned`, `hypothesis`, or `aspiration` into present capability or contribution.
Scope `inferred-external` to the checked published or demonstrated system. State what future work
would establish every important project claim.

### Separate complete evidence review from concise reader-facing claims

Preserve uncertainty, limitations, non-claims, counterevidence, and reopen triggers internally. In
reader-facing approach, feature, design-choice, or contribution descriptions, lead with the human
situation and desired value, then the capability and only necessary implementation detail. Use
concrete popular-science language before precise terms, translating abstract relationships into
actions a broad reader can picture. State the strongest supportable active claim with only
claim-local qualifiers that change its truth, scope, quantity, causal meaning, comparison, or
likely interpretation. Do not turn intended value into measured benefit, disclaim unclaimed
outcomes, or hedge by reflex. Cite established prior work for an inherited general mechanism or
design fact; require project-specific verification only for claims about the exact artifact,
parameter, delivered dose, coverage, fidelity, or downstream effect. For a general audience, lead
with a familiar term, define the exact scientific construct or metric at first use, and do not
treat neighboring constructs as synonyms.

## Core workflow

The detailed requirements and gates for every step are in
[phase-1-research-workflow.md](references/phase-1-research-workflow.md).

### 1. Inspect and establish the starting state

Read all supplied material before interviewing. Inventory people/activity/problem, current
practice, observed consequences, why-now, related work, approach, artifacts, contribution
hypotheses, terminology, constraints, citations, and full copies. Begin `starting-state.md` and the
workboard in-session; mark imported conclusions as hypotheses until checked.

### 2. Interview only for consequential unknowns

Batch two to six tightly related, low-risk factual clarifications when author knowledge can answer
them without research; accept concise numbered answers and propagate the batch once. Ask one
question at a time only for consequential choices, constructive-opposition gates, sensitive or
access actions, and questions whose earlier answer changes what should be asked next. Establish
factual scope, observations, existing artifacts, access, and constraints. Do not ask the author to
rank, select, or approve consequences before Step 4's research. Ask for source-access help whenever
a decision-relevant full copy is human-blocked.

### 3. Create the project workspace

After resolving both locations to absolute paths, run
`python3 "ABSOLUTE_SKILL_DIR/scripts/initialize_phase1_workspace.py" "ABSOLUTE_PROJECT_REPO" --project-name "PROJECT NAME"`.
This creates missing templates without overwriting existing work, creates a root `README.md` with
framing and prospective contributions, and publishes/audits the GitHub Markdown shelf. Do not hand-create
only a subset of the workspace. It must include
`agent-context.json`, the workboard, decision and source records, `references.csv`, evidence/claim
registers, motivation and authority audits, `source-resolution.csv`,
`prior-work-evidence-accounting.csv`, `idea-provenance-ledger.csv`,
`imported-bibliography-accountability.csv`, `late-found-work-postmortem.csv`,
`novelty-regression-sentinels.yaml`, consequence ranking, ACM/SIGCHI and recall audits,
related-work matrices and positioning, terminology, options, reviewer records,
`research-framing-outline.md`, `phase-2-handoff.md`, and generated reports.

Treat the root README and linked Markdown shelf as workspace invariants, not end-of-phase polish. The
README's top matter links the project's NotebookLM notebook URL once one exists. Before any
commit, push, terminal handoff, or claim that a durable work batch is complete, verify that the
README links resolve, regenerate the reports after the latest material changes, and run the report
auditor. Do not publish canonical updates with absent, stale, unlinked, or machine-local reader views.

Populate the manifest's project name immediately, keep `phase.status` current, and update its
canonical pointers whenever an artifact path changes. Additional GPT Pro repository access must be
an explicit, narrow `context.repo_read_allow` entry; do not default to the whole repository.

### 4. Build the motivation evidence chain

Map:

`larger concern → target population/context → current practice → unmet need → consequence → why now → opportunity`

Create `authoritative-source-map.md`; authority is claim-specific. Recursively research every
active motivation/problem `hypothesis` or `unsupported` claim using
`motivation-claim-research-queue.md` and `current-practice-audit.md`. Do not ask the author to
choose a frame until `AUTHORITATIVE_DOMAIN_SOURCES_MAPPED` and
`MOTIVATION_CLAIM_AUDIT_COMPLETE`.

Research and rank consequences by magnitude, prevalence, duration, reversibility, equity,
time-criticality, and evidence confidence. Create `consequence-severity-ranking.md`; do not ask the
author to rank, select, or approve consequences until `CONSEQUENCE_RANKING_COMPLETE`. Author
preference may choose emphasis only after the evidence-ranked portfolio is visible.

### 5. Research the related-work landscape

Search the native ACM Digital Library plus broader scholarly indexes, products, practices,
demonstrations, references, citations, authors, synonyms, and neighboring constructs. Prioritize
CHI and relevant SIGCHI venues for coverage without upgrading evidence strength by venue.

Expand a high-leverage seed portfolio—not only the closest papers—through two independent cited-by
routes and successive promotion waves. Stop only after a complete wave yields no new
decision-relevant work; a late-found paper requires a sibling-citation sweep and regression repair.

For every active or imported approach component that could change feasibility, mechanism,
positioning, or evaluation, run a separate **component-foundation and falsification pass**. Search
the operational parameter, proximal human mechanism, desired outcome, failure mode, and
counterevidence in the disciplines that study them. Keep design/mechanism foundations and analogies
visible even when they are not close HCI contribution comparators.

Run a parallel **seed-upgrade pass** over author-provided references. Search authoritative bodies
within remit, stronger designs or syntheses, more direct populations/outcomes, current versions,
and top HCI/domain venues as appropriate. A supplied source can remain useful, but it cannot set the
evidence ceiling or waive contradictory/stronger evidence.

Maintain `acm-sigchi-related-work-audit.md`,
`related-work-search-recall-audit.md`, `related-work-matrix.md`,
`related-work-contribution-tier-audit.md`, `prior-work-contribution-boundary.md`,
`prior-work-evidence-accounting.csv`, `idea-provenance-ledger.csv`,
`imported-bibliography-accountability.csv`, `late-found-work-postmortem.csv`,
`novelty-regression-sentinels.yaml`, and `ranked-related-work-positioning.md`. Reach
`ACM_SIGCHI_LANDSCAPE_AUDITED` and
`RELATED_WORK_SEARCH_RECALL_AUDITED` before the gap/contribution gate.

Before ranking, freeze a **target-problem identity contract**: target people, focal activity,
triggering/temporal context, unwanted state or episode, and intended change/outcome. Keep any
hypothesized causal mechanism separate. Assign every retained work a descriptive
**problem-proximity band** before considering mechanism similarity. Build separate primary
same/similar-problem, mechanism/capability-collision, and concept/theory/foundation portfolios.
Same-domain vocabulary or a shared mechanism cannot make a different-problem work a closest
problem comparator.

Compare the literal causal interaction approach and configuration burden—not labels or maturity.
Decompose access state, activation selector, changed parameter, progression, duration/cadence,
scope, overrides, intention anchor, reset, and current-platform baseline. A cumulative daily budget
is not a clock/event transition; an after-activation ease-in is not a pre-transition taper. Rank
up to approximately ten verified full works from the same/similar-problem bands and write one fair
positioning paragraph for each. If fewer exist, include all and disclose the shortage; never pad
the primary ranking with distant analogies. Preserve different-problem component or mechanism
precedents separately; they narrow only the exact matched mechanism or independently claimed
sub-capability, not the complete human-activity capability by qualifier subtraction.

Normalize away hardware and platform labels. Reproducing the same demonstrated causal interaction
on another device or platform has zero contribution weight. Credit an adaptation only when
full-source evidence demonstrates nontrivial reusable adaptation knowledge, a new class of use, or
a directly validated empirical finding. A zero-credit port can still create a capability
collision.

### 6. Establish terminology and the lexical spine

Treat terminology as claim discipline. Create `terminology-contract.md`, decompose each central
idea into independently verifiable dimensions, and present three to five coherent systems. Ask the
author to approve the semantic contract before selecting the lexical spine; keep every system
`candidate` until approval. For broad audiences, make each system specify a familiar entry term,
its precise scientific or technical definition, and the approved short form after first use.

### 7. Synthesize gaps and approach hypotheses

Compare current practice, products, and research on neutral dimensions. Generate three to five
capability, experience, cost/access, or knowledge gap interpretations and three to five approach
hypotheses. For each, state the closest work, intended experience, inherited foundation, advantage,
cost, failure mode, falsifier, and smallest Phase 2 premise test.

Derive fair future evaluation logic from the claimed workflow change. For an additive layer,
compare the intact workflow with the same workflow plus the proposed layer—not a baseline that
removes valued current practice. Record this as a Phase 3 requirement, not an approved study.

### 8. Explore positioning views

Create three to five evidence-grounded two-axis views with neutral operational endpoints. Include
contribution, topology/context, workflow/activity, and literature-exposed alternatives. State what
each view reveals and hides; recommend one, then let the author choose.

### 9. Sharpen prospective contributions

Identify atomic reusable outputs, frame their human and HCI value, classify a primary and any
supporting contribution types, and align each type with an independent evidence gate. Then generate
three to five coherent packages and rank their workflow significance, interaction or control-policy
or information-distribution capability, setting/activity boundary, design rationale, and outcome hypothesis. Select the strongest defensible
consequential difference from the closest comparator. A prototype, algorithm, interview set, or
study is not automatically a contribution. Run the contribution-discovery gates in
`related-work-positioning.md`: objective/equal-quantity, concept lineage/in-domain collision,
collision–delta, control-policy/residual state, anchor semantics/quality, temporal identifiability, construct independence, causal
ladder/fidelity, and null survival. Apply the full six-field accounting symmetrically to prior work
and the focal project. Separate the platform-independent **approach invariant**—the human-activity, interaction, or control-policy change that survives platform substitution—from the implementation
substrate/empirical waist, realization evidence, and value evidence. Do not promote a planned focal capability into a demonstrated
contribution; preserve a demonstrated-unclaimed operation at its matched scope without using an
old component to erase a novel human-activity capability or misattribute prior contribution.
Do not conflate untested human value with absence of capability novelty: assess capability
realization and human-value evidence as separate atoms, then apply all six independent fields to
each.

### 10. Run phase-aware constructive review

Review the workboard, evidence, landscape, options, decisions, and outline through the seven
reviewer lenses. Do not demand final prose or missing later-phase results, prescribe work without
naming the uncertainty it resolves, or imply acceptance predictions. Return material choices to
the author.

### 11. Produce the research framing outline

Write `research-framing-outline.md` as an argument/decision outline covering the concern, specific
problem, why-now, state of the art, gap, approach, process, terminology, prospective
contributions, evidence boundaries, open decisions, and stop/go risks. Use tables and candidate
language. Keep the complete evidence boundary visible internally while marking which qualifiers are
actually required in reader-facing prose. Do not turn it into polished Introduction prose.

### 12. Create the Phase 2 handoff

Write `phase-2-handoff.md` with the selected frame, evidence, current workflow, closest work,
approach and rejected alternatives, terminology, contribution hypothesis, constraints, unknowns,
formative/design/technical questions, fair future comparison, evidence needs, and explicit return
conditions. Carry the source-resolution state, exact access requests, affected blocked/narrowed
claims, component foundations/lineage, author-seed provenance, stronger/counter-source
dispositions, and reopen triggers; later phases cannot upgrade them through prose. It is optional
input; Phase 2 must remain independently enterable.

Before declaring Phase 1 complete, reconcile `agent-context.json` with the final workboard, source
manifest, NotebookLM maintenance record, and handoff, then set `phase.status` to `complete`.

### 13. Citation output profile: GitHub Markdown. Deterministic citation gate

Run:

```bash
python3 "ABSOLUTE_SKILL_DIR/scripts/check_prior_work_accounting.py" "ABSOLUTE_PROJECT_REPO/research-framing" --end-of-round
python3 "ABSOLUTE_SKILL_DIR/scripts/check_source_resolution.py" "ABSOLUTE_PROJECT_REPO/research-framing" --end-of-round
python3 "ABSOLUTE_SKILL_DIR/scripts/render_phase1_reports.py" "ABSOLUTE_PROJECT_REPO/research-framing"
python3 "ABSOLUTE_SKILL_DIR/scripts/audit_phase1_reports.py" "ABSOLUTE_PROJECT_REPO/research-framing"
```

Use `--end-of-round` for a declared bounded audit or research-round closure, not an ordinary
in-progress status update. A progress update may expose transient acquisition work only while the
agent continues it; it must not become a terminal handoff or delay an exact author-access request
after lawful routes are exhausted.

Regenerate the four core `.md` reports, report-shelf README, and ledger views at their checkpoints;
canonical Markdown/CSV/JSON/YAML records remain editable sources. After audit, preview the README,
core reports, citations, nested navigation, and wide ledgers in desktop/phone GitHub Markdown.

The report gate also applies before every repository commit, push, or terminal handoff containing
material Phase 1 changes. Confirm the root `README.md` carries evidence-status-aware framing and
contribution statements, links to the canonical detailed records and four principal `.md` reports,
and that every relative link exists in the committed tree. No generated `.html` file may remain.

## Completion states

- `READY_FOR_PHASE_2`
- `READY_WITH_RISKS`
- `NEEDS_MOTIVATION_EVIDENCE`
- `NEEDS_MOTIVATION_CLAIM_RESEARCH`
- `NEEDS_AUTHORITATIVE_SOURCE_MAPPING`
- `NEEDS_LANDSCAPE_RESEARCH`
- `NEEDS_AUTHOR_SOURCE_ACCESS`
- `RECONSIDER_DIRECTION`

Never mark the project ready because documents or the workboard are populated. Every Phase 1 area
must be resolved, visibly blocked, or deliberately deferred with its consequence and reopen
trigger. Run both `check_prior_work_accounting.py` and `check_source_resolution.py` with
`--phase-ready`; readiness is an evidence-and-decision judgment, and unresolved author access
requires `NEEDS_AUTHOR_SOURCE_ACCESS`. The prior-work checker must verify all mandatory completion
markers, including imported-bibliography accounting, claim/demonstration/operation/evaluation
decomposition, collision-credit separation, mixed-channel decomposition, port gates, proposal and
silence exclusions, late-find repair, novelty sentinels, and the complete zero-yield promotion
wave.
