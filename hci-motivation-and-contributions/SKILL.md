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

Help researchers solve the **right problem** before design, implementation, and evaluation choices become fixed. Produce a defensible research direction and outline, not manuscript prose.

## Phase contract

Every phase is independently enterable. This is Phase 1 of:

`problem screening → motivation and contributions → design/build → validation → visuals → writing → video`

Never require an Office Hours brief or another prior-phase artifact; accept any starting material and import prior conclusions as evidence-bounded hypotheses. Office Hours remains a complete standalone experience. See [pipeline-contract.md](references/pipeline-contract.md) for scope and handoff, and [exemplar-routing.md](references/exemplar-routing.md) before using exemplar papers, which teach structure, never project evidence.

In scope: problem importance, evidence status, current practice, related work, terminology, gaps, approach hypotheses, positioning, prospective contributions, and Phase 2/3 evidence needs. Out of scope: final Abstract, Introduction, Related Work, or paper prose; final design, implementation, study approval, analysis, figures, and unestablished effectiveness claims. Inspect later-phase artifacts to understand the direction, never to grade their absence.

## Required reference routing

- Read [active-author-collaboration.md](references/active-author-collaboration.md), then [author-collaboration.md](references/author-collaboration.md), before the first consequential question or decision.
- Before executing Steps 1–13, read [phase-1-research-workflow.md](references/phase-1-research-workflow.md) completely.
- Motivation and claim assessment: [authoritative-domain-sources.md](references/authoritative-domain-sources.md), [research-discovery-recall.md](references/research-discovery-recall.md), [motivation-claim-strengthening.md](references/motivation-claim-strengthening.md).
- Related work: [acm-sigchi-related-work.md](references/acm-sigchi-related-work.md), [forward-citation-expansion.md](references/forward-citation-expansion.md), [related-work-positioning.md](references/related-work-positioning.md).
- Terminology, charts, type-specific contribution packages: [terminology-contract.md](references/terminology-contract.md), [related-work-quadrant.md](references/related-work-quadrant.md), [hci-contribution-types.md](references/hci-contribution-types.md), [contribution-rubric.md](references/contribution-rubric.md).
- NotebookLM [notebooklm-research.md](references/notebooklm-research.md); review and reports [reviewer-panel.md](references/reviewer-panel.md), [markdown-reports.md](references/markdown-reports.md), [iso-24495-1-plain-language.md](references/iso-24495-1-plain-language.md).

## Non-negotiable operating rules

### Collaborate actively before converging

Maintain `phase-1-collaboration-workboard.md` and repeat:

`inspect → research → assess → challenge → compare → recommend → author decides → record → propagate → recheck`

Lead every author-facing update, handoff, and progress report with a decision-first current-state snapshot: direction/readiness, established/observed/planned, settled boundaries, at most three consequence-ordered decisions with recommendations, blockers, and next action/owner; say so when no decision is ready. History and artifact inventories are supporting evidence, never the author's route to the current state. Research decision-relevant evidence before asking the author to choose, then offer three to five substantively different options with a recommendation, ask one consequential question at a time, and preserve rejected and superseded variants.

Apply **constructive opposition**: author preference may choose among defensible paths, but cannot become evidence or waive a critical gap. State the mismatch and consequence, then offer bounded research, a decision-matched probe, a better-supported framing or approach, a narrower claim, or a visible block. If necessary evidence is declined, record `AUTHOR-DECLINED-EVIDENCE`, narrow or block the claim, propagate, and retain a reopen trigger.

### Keep the session interactive and parallelize evidence work

Open each nontrivial research batch by naming what is running and the decision it prepares. Use available subagents by default for bounded retrieval, full-text audit, citation-chain expansion, counter-source search, and claim tracing; continue locally when unavailable. Keep one lead agent as the sole writer, evidence integrator, workboard owner, and author-facing collaborator, reconciling findings before claims change or a decision gate opens. Ask the author for help only with lawful access or CAPTCHA/authentication in their browser, missing artifacts, and tacit facts, values, constraints, or consequential choices research cannot recover. Do not shift routine literature search or analysis to the author.

### Keep project data in the project repository

Resolve the target project repository before durable writes; until then keep starting state and the live workboard in-session and continue read-only inspection, research, and interactive planning, per [repository-boundaries.md](references/repository-boundaries.md). Never put project research data in the reusable skill repository or an arbitrary workspace. Once resolved, create `research-framing/` from the `assets/` templates without overwriting existing work.

Maintain `research-framing/agent-context.json` as the host-neutral pointer manifest for Codex `$gpt-pro` and Claude Code `/gpt-pro`: it names this exact active skill, points only to canonical repository-relative Phase 1 artifacts, and syncs its NotebookLM ID/title/profile with the source manifest. It never holds a transcript, duplicate decision record, credentials, a machine-local absolute path, raw participant data, or conversation history.

### Mirror full sources into both private project stores

The project repository and its NotebookLM notebook are private, governed project stores. Copyright, license, and redistribution status must not block, delay, or require separate per-source author confirmation for saving a full source in the repository, tracking it in version control, or uploading it to the notebook; never add ignore rules, omit NotebookLM sources, or keep only metadata for that reason. Store a canonical repository copy of every retained full source under `research-framing/sources/full-text/`, mirror it into NotebookLM by default, and record both the repository-relative path and NotebookLM source ID; repair a failed copy instead of calling it complete. This does not reclassify credentials, authentication material, identifiable participant data, confidential peer-review material, or third-party secrets as research sources: keep those out of both stores unless an explicit data-governance decision authorizes them.

### Ground every retained claim in complete sources

Every retained reference needs an obtained, saved, and opened full copy; abstracts, snippets, AI summaries, and paraphrases may discover candidates but cannot ground claims. **Read every identity off the copy itself, and never store an identifier twice** ([citation-integrity.md](references/citation-integrity.md)). Keep `references.csv` keys stable and follow `HCI-CITATIONS-4`: keyed links, catalog-derived definitions, a visible full-reference entry, draft tokens resolved, every citation shorthand hyperlinked. Unknown or duplicate identities, missing metadata, and broken links block delivery.

Keep ingestion completeness separate from claim strength in `evidence-strength-register.md`, record each claim's exact locator, and apply the critical-risk-of-bias veto before `ES3`; an unmarked source is unassessed, not strong. `UNASSESSED` is a transient acquisition state, never an acceptable disposition when a bounded audit or research round is declared closed: track the candidate in `source-resolution.csv`, then audit its full text, screen it out with a specific relevance reason, supersede it to a different retained `FULL_TEXT_ASSESSED` row with a stable citation key, or surface an exact `NEEDS_AUTHOR_SOURCE_ACCESS` request recording an actual surfaced date/locator, affected claims, fallback, and reopen trigger. Never deliver an “audit complete” report whose next action is merely to obtain the papers. Before phase readiness, reconcile every external HTTP(S) key in `references.csv` bidirectionally with that ledger and mark project evidence with an `internal:` URL. At each closure, reconcile the candidate source files in the governed source/import roots against `source-resolution.csv` and record the roots, counts, unresolved files, and `LOCAL_SOURCE_FILES_RECONCILED` marker in `source-manifest.md`.

For every material prior-work or focal-project atom, complete the six independent fields in `prior-work-evidence-accounting.csv`—`AUTHOR CLAIM`, `DEMONSTRATED ARTIFACT OR STUDY`, `OPERATED CAPABILITY`, `EVALUATED RESULT`, `CAPABILITY COLLISION`, `CONTRIBUTION CREDIT`—and let no field inherit truth from another. Compare the smallest positively evidenced operation against the focal capability's complete human-activity predicate, not isolated adjectives. A demonstrated but unclaimed operation can create a capability collision only at the matched human capability or independently claimed sub-capability scope, takes no contribution credit, and is `DEMONSTRATED_UNCLAIMED`; a claimed but undemonstrated atom is `CLAIMED_UNDEMONSTRATED` and takes neither.

**An idea with no demonstration and no study collides with nothing.** Ask only whether an artifact ran the named operation and whether an evaluation measured the named result; if not, record `NONE` in both columns however closely the idea resembles the focal atom. Venue is the prompt to check, never the verdict. Route proposals, future work, interpretations, and hypotheticals to the idea provenance record in `idea-provenance-ledger.csv` with collision and credit `NONE`; an explicit author claim that a realized capability exists without matched evidence remains visible as a `CLAIMED_UNDEMONSTRATED` row. Treat source silence only as `SEARCH_PRIORITY` or `REOPEN_QUERY`. Decompose mixed systems channel by channel and gate port credit as [prior-work-contribution-boundaries.md](references/prior-work-contribution-boundaries.md) requires.

Treat every author-provided citation, bibliography, and reading list as an **initial discovery seed**: search independently for claim-matched sources with stronger authority, rigor, directness, or currency, and record whether the seed is retained with bounds, corroborated, or superseded. A supplied source cannot set the evidence ceiling, and venue prestige alone never upgrades evidence.

### Escalate human-only source access

Exhaust the lawful acquisition routes in [evidence-protocol.md](references/evidence-protocol.md), and continue non-dependent research, before asking for help. A `403` from an automated fetcher is normally bot detection, not absent entitlement; drive the author's already-entitled headed browser rather than escalating on it. For a genuinely blocked source, record the exact citation, DOI/canonical URL, attempted routes, obstacle, why it matters, and fallback boundary in `missing-full-copies.md`, then ask for one concrete action: university IP or university VPN access, a lawfully obtained PDF, a CAPTCHA or institutional sign-in completed by the author, or an authorized link. Never ask for passwords, cookies, session tokens, browser profiles, or other authentication material.

If access remains blocking, use `NEEDS_AUTHOR_SOURCE_ACCESS`; never substitute an AI summary or stop at writing `missing-full-copies.md`. Once the author supplies a download or authenticated page, open the exact full work, complete its source and claim audit, update the resolution records, and resume the blocked analysis.

### Use one NotebookLM notebook per project

Use Gemini NotebookLM through `notebooklm-mcp-cli`: one new notebook per project, headed Chrome for authorized access, notebook and source IDs stored but never credentials. Write the resolved notebook ID, title, and profile to both `source-manifest.md` and `agent-context.json`, keep them synchronized after any notebook or profile change, and link the `notebooklm.google.com/notebook/<id>` URL at the top of the root `README.md`. Treat NotebookLM ratings as review aids to reconcile against opened originals. Keep the notebook human-readable: a `START HERE` evidence map, imports verified to contain the intended work, readable titles, broken imports replaced, and unassessed, duplicate, and superseded objects reconciled each bounded round. Obtain explicit author confirmation for the exact source-ID set before any irreversible NotebookLM deletion.

### Keep unfinished claims unfinished

Use these states:

- `established-external`
- `inferred-external`
- `observed-project`
- `planned`
- `hypothesis`
- `aspiration`
- `unsupported`

Never convert `planned`, `hypothesis`, or `aspiration` into present capability or contribution. Scope `inferred-external` to the checked published or demonstrated system, and state what future work would establish every important project claim.

### Separate complete evidence review from concise reader-facing claims

Preserve uncertainty, limitations, non-claims, counterevidence, and reopen triggers internally. In reader-facing descriptions, lead with the human situation and desired value, then the capability and only necessary implementation detail; open with concrete behavior, never an abstract label such as `a serious human problem`. Place each citation immediately after the smallest claim or keyword it supports, cite each independently supported item in an enumeration, and split clusters as finely as the evidence permits. A multi-source cluster has no numeric cap only when every work supports the same indivisible atom. Keep generic disclaimers internal while retaining any claim-local qualifier the synthesis needs, and follow the placement and transition rules in [claim-focused-writing.md](references/claim-focused-writing.md).

Do not turn intended value into measured benefit, call a field ineffective without direct evidence, or present an unmeasured mechanism as fact. Cite established foundations for inherited mechanisms, and require project-specific verification of the exact artifact, parameter, dose, coverage, or fidelity. For a general audience, lead with a familiar term, define the exact source-matched construct at first use, and never treat neighboring constructs as synonyms.

## Core workflow

[phase-1-research-workflow.md](references/phase-1-research-workflow.md) carries each step's full requirements and gates; the steps below carry the governing artifacts, markers, and constraints.

### 1. Inspect and establish the starting state

Inventory the supplied material — people/activity/problem, current practice, consequences, why-now, related work, approach, contribution hypotheses, terminology, constraints, and citations with their full copies — into `starting-state.md` and the workboard, in-session; mark imported conclusions as hypotheses until checked.

### 2. Interview only for consequential unknowns

Batch two to six tightly related, low-risk factual clarifications that author knowledge can answer without research, and propagate the batch once. Ask one question at a time only for consequential choices, constructive-opposition gates, sensitive or access actions, and questions whose answer changes what to ask next.

### 3. Create the project workspace

After resolving both locations to absolute paths, run
`python3 "ABSOLUTE_SKILL_DIR/scripts/initialize_phase1_workspace.py" "ABSOLUTE_PROJECT_REPO" --project-name "PROJECT NAME"`.
Never hand-create a subset of the workspace: the initializer instantiates every `assets/` template, including `agent-context.json`, the workboard, decision and source records, `references.csv`, `source-resolution.csv`, the Step 5 ledgers, `research-framing-outline.md`, `phase-2-handoff.md`, the generated reports, and a root `README.md` whose top matter links the NotebookLM notebook URL once one exists.

The README and its Markdown shelf are workspace invariants, not end-of-phase polish. Before every commit, push, terminal handoff, or completion claim, verify that the README links resolve, regenerate the reports, and run the report auditor; never publish absent, stale, unlinked, or machine-local reader views. Keep the manifest's project name, `phase.status`, and canonical pointers current, and grant additional GPT Pro repository access only as a narrow `context.repo_read_allow` entry.

### 4. Build the motivation evidence chain

Map:

`larger concern → target population/context → current practice → unmet need → consequence → why now → opportunity`

Create `authoritative-source-map.md`; authority is claim-specific. Research every active motivation or problem `hypothesis` or `unsupported` claim through `motivation-claim-research-queue.md` and `current-practice-audit.md`, and rank consequences in `consequence-severity-ranking.md` on the dimensions in [consequence-severity-research.md](references/consequence-severity-research.md). Do not ask the author to rank, select, or approve consequences, or to choose a frame, until `AUTHORITATIVE_DOMAIN_SOURCES_MAPPED`, `MOTIVATION_CLAIM_AUDIT_COMPLETE`, and `CONSEQUENCE_RANKING_COMPLETE`; preference may choose emphasis only once the evidence-ranked portfolio is visible.

### 5. Research the related-work landscape

Search the native ACM Digital Library plus broader indexes, products, practices, demonstrations, references, citations, authors, synonyms, and neighboring constructs, prioritizing CHI and relevant SIGCHI venues without upgrading evidence strength by venue. Expand a high-leverage seed portfolio—not only the closest papers—through two independent cited-by routes and successive promotion waves; stop only after a complete wave yields no new decision-relevant work, and treat a late find as requiring a sibling-citation sweep and regression repair. Run a separate **component-foundation and falsification pass** for every approach component that could change feasibility, mechanism, positioning, or evaluation, and a parallel seed-upgrade pass over author-provided references.

Maintain `acm-sigchi-related-work-audit.md`, `related-work-search-recall-audit.md`, `related-work-matrix.md`, `related-work-contribution-tier-audit.md`, `prior-work-contribution-boundary.md`, `prior-work-evidence-accounting.csv`, `idea-provenance-ledger.csv`, `imported-bibliography-accountability.csv`, `late-found-work-postmortem.csv`, `novelty-regression-sentinels.yaml`, and `ranked-related-work-positioning.md`, and reach `ACM_SIGCHI_LANDSCAPE_AUDITED` and `RELATED_WORK_SEARCH_RECALL_AUDITED` before the gap/contribution gate.

Before ranking, freeze a target-problem identity contract—target people, focal activity, triggering/temporal context, unwanted state, intended outcome—keep any hypothesized mechanism separate, and band every retained work by problem proximity before considering mechanism similarity. Shared vocabulary or mechanism never makes a different-problem work a closest problem comparator; keep same/similar-problem, mechanism-collision, and foundation portfolios separate.

Compare the literal causal interaction approach and configuration burden—not labels or maturity—as [related-work-positioning.md](references/related-work-positioning.md) prescribes. Rank up to approximately ten verified full works from the same/similar-problem bands, one fair positioning paragraph each; if fewer exist, include all and disclose the shortage. Different-problem component or mechanism precedents narrow only the exact matched mechanism or independently claimed sub-capability, never the complete human-activity capability by qualifier subtraction; reproducing a demonstrated causal interaction on another platform carries zero contribution weight though such a port can still create a capability collision.

### 6. Establish terminology and the lexical spine

Treat terminology as claim discipline. In `terminology-contract.md`, decompose each central idea into independently verifiable dimensions and present three to five coherent systems, each with a familiar entry term, its precise definition, and the approved short form after first use. Ask the author to approve the semantic contract before selecting the lexical spine; every system stays `candidate` until approval.

### 7. Synthesize gaps and approach hypotheses

Compare current practice, products, and research on neutral dimensions, then generate three to five gap interpretations (capability, experience, cost/access, knowledge) and three to five approach hypotheses, each with its closest work, inherited foundation, cost, failure mode, falsifier, and smallest Phase 2 premise test. For an additive layer, compare the intact workflow with the same workflow plus the proposed layer, never a baseline that removes valued practice; record it as a Phase 3 requirement, not an approved study.

### 8. Explore positioning views

Create three to five evidence-grounded two-axis views with neutral operational endpoints, covering contribution, topology/context, workflow/activity, and literature-exposed alternatives. State what each reveals and hides, recommend one, and let the author choose; before polishing, record the view's reader task and show the alternatives in placed context. Do not sync it to Overleaf until the author marks an exact version decided or final and separately authorizes release.

### 9. Sharpen prospective contributions

Identify atomic reusable outputs, frame their human and HCI value, classify a primary and any supporting contribution types, and align each type with an independent evidence gate. Generate three to five coherent packages, rank their workflow significance, capability, setting boundary, and outcome hypothesis, and select the strongest defensible consequential difference from the closest comparator; a prototype, algorithm, interview set, or study is not automatically a contribution.

Run the contribution-discovery gates in `related-work-positioning.md`—objective/equal-quantity, concept lineage/in-domain collision, collision–delta, control-policy/residual state, anchor semantics/quality, temporal identifiability, construct independence, causal ladder/fidelity, null survival—and apply the six-field accounting symmetrically to prior work and the focal project. Separate the platform-independent **approach invariant**—the human-activity, interaction, or control-policy change surviving platform substitution—from the implementation substrate, realization evidence, and value evidence. Never promote a planned focal capability into a demonstrated contribution, and preserve a demonstrated-unclaimed operation at its matched scope rather than letting an old component erase a novel human-activity capability. Do not conflate untested human value with absence of capability novelty: assess capability realization and human-value evidence as separate atoms.

### 10. Run phase-aware constructive review

Review the workboard, evidence, landscape, options, decisions, and outline through the seven reviewer lenses; never demand final prose or later-phase results, prescribe work without naming the uncertainty it resolves, or imply acceptance predictions. Return material choices to the author.

### 11. Produce the research framing outline

Write `research-framing-outline.md` from its template as an argument and decision outline in tables and candidate language, keeping the full evidence boundary visible internally while marking which qualifiers reader-facing prose requires. Do not turn it into polished Introduction prose.

### 12. Create the Phase 2 handoff

Fill `phase-2-handoff.md` from its template, carrying the selected frame, evidence, closest work, rejected alternatives, terminology, contribution hypothesis, constraints, open questions, fair future comparison, return conditions, source-resolution state, exact access requests, affected blocked or narrowed claims, component foundations and lineage, author-seed provenance, counter-source dispositions, and reopen triggers; later phases cannot upgrade them through prose. It is optional input; Phase 2 must remain independently enterable. Before declaring Phase 1 complete, reconcile `agent-context.json` with the final workboard, source manifest, NotebookLM record, and handoff, then set `phase.status` to `complete`.

### 13. Citation output profile: GitHub Markdown. Deterministic citation gate

Run:

```bash
python3 "ABSOLUTE_SKILL_DIR/scripts/check_prior_work_accounting.py" "ABSOLUTE_PROJECT_REPO/research-framing" --end-of-round
python3 "ABSOLUTE_SKILL_DIR/scripts/check_source_resolution.py" "ABSOLUTE_PROJECT_REPO/research-framing" --end-of-round
python3 "ABSOLUTE_SKILL_DIR/scripts/render_phase1_reports.py" "ABSOLUTE_PROJECT_REPO/research-framing"
python3 "ABSOLUTE_SKILL_DIR/scripts/audit_phase1_reports.py" "ABSOLUTE_PROJECT_REPO/research-framing"
```

Use `--end-of-round` for a declared bounded audit or research-round closure, not an ordinary status update; a progress update may expose transient acquisition work only while the agent continues it, and must not become a terminal handoff or delay an exact author-access request after lawful routes are exhausted.

Regenerate the four core `.md` reports, report-shelf README, and ledger views at their checkpoints; canonical Markdown/CSV/JSON/YAML records remain the editable sources, and no generated `.html` file may remain. After audit, preview the README, core reports, citations, navigation, and wide ledgers in desktop and phone GitHub Markdown. This gate also applies before every repository commit, push, or terminal handoff carrying material Phase 1 changes; confirm that the root `README.md` carries evidence-status-aware framing and contribution statements, links the canonical records and four principal `.md` reports, and that every relative link resolves in the committed tree.

## Completion states

- `READY_FOR_PHASE_2`
- `READY_WITH_RISKS`
- `NEEDS_MOTIVATION_EVIDENCE`
- `NEEDS_MOTIVATION_CLAIM_RESEARCH`
- `NEEDS_AUTHORITATIVE_SOURCE_MAPPING`
- `NEEDS_LANDSCAPE_RESEARCH`
- `NEEDS_AUTHOR_SOURCE_ACCESS`
- `RECONSIDER_DIRECTION`

Never mark the project ready because documents or the workboard are populated; every Phase 1 area must be resolved, visibly blocked, or deliberately deferred with its consequence and reopen trigger. Run both `check_prior_work_accounting.py` and `check_source_resolution.py` with `--phase-ready`; readiness is an evidence-and-decision judgment, unresolved author access requires `NEEDS_AUTHOR_SOURCE_ACCESS`, and the prior-work checker must verify every mandatory completion marker in `prior-work-contribution-boundary.md`.
