# Detailed Phase 1 research workflow

Read this reference completely before executing the Phase 1 workflow. It preserves the detailed
research gates, artifact requirements, comparison logic, and completion criteria routed from the
lean core skill.

## Contents

1. [Phase contract](#phase-contract)
2. [Non-negotiable operating rules](#non-negotiable-operating-rules)
3. [Inspect and establish the starting state](#1-inspect-and-establish-the-starting-state)
4. [Interview for consequential unknowns](#2-interview-for-consequential-unknowns)
5. [Create the project research workspace](#3-create-the-project-research-workspace)
6. [Build the motivation evidence chain](#4-build-the-motivation-evidence-chain)
7. [Research the related-work landscape](#5-research-the-related-work-landscape)
8. [Establish terminology, gaps, and approach](#6-establish-the-terminology-contract)
9. [Position and sharpen contributions](#8-explore-positioning-views)
10. [Review, outline, and hand off](#10-run-a-phase-aware-constructive-review)
11. [Generate and audit HTML reports](#13-generate-the-html-reports)
12. [Completion states](#completion-states)

Help researchers solve the **right problem** before the expensive parts of an HCI project become
fixed. Work as a rigorous research collaborator: investigate, compare, expose uncertainty, propose
substantive alternatives, and let the author make consequential framing decisions.

The goal is a defensible **research direction and outline**, not polished manuscript prose.

## Phase contract

This is Phase 1 of a looping HCI research workflow:

`problem screening → motivation and contributions → design/build → validation → visuals → writing → video`

Every phase is independently enterable. Never require an Office Hours brief or any other
prior-phase output. Start from whatever the researcher has: an idea, notes, a class report, papers,
observations, preliminary designs, a prototype, study plans, or partial results.

When an Office Hours brief exists, import it as a useful hypothesis—not an approved premise. Office
Hours remains a complete standalone experience; this skill deliberately revisits some of its
questions with deeper source acquisition, exhaustive comparison, and explicit claim-level
traceability.

Read [pipeline-contract.md](pipeline-contract.md) when deciding what belongs in this
phase or constructing the handoff.

Use full exemplar papers throughout the pipeline. Read
[exemplar-routing.md](exemplar-routing.md) before analyzing exemplars or transferring
their patterns. Exemplars teach how strong research is structured and communicated; they are not
evidence for the project's own problem, gap, or effectiveness unless independently relevant.

### In scope

- establish the scale, consequence, and timeliness of the human problem;
- distinguish published evidence, author observations, assumptions, and aspirations;
- find and analyze the closest academic work, products, practices, and demonstrations;
- identify gaps without treating prior work negatively;
- develop and compare novel approach hypotheses;
- position the project using matrices and alternative two-axis views;
- sharpen prospective HCI contributions and their evidence requirements;
- identify what Phase 2 and Phase 3 must learn, build, and validate.

### Out of scope

- final Abstract, Introduction, Related Work, or paper prose;
- final interaction design or system architecture;
- implementing prototypes;
- approving a formative, pilot, summative, or field-study protocol;
- performing final quantitative or qualitative analysis;
- claiming effectiveness, generality, or transfer not yet established;
- designing final publication figures or submission videos.

Plans, rough concepts, and results may be inspected to understand the direction. Do not grade
missing later-phase artifacts as though the work were already complete.

## Non-negotiable operating rules

### Collaborate actively before converging

Read [active-author-collaboration.md](active-author-collaboration.md) and
[author-collaboration.md](author-collaboration.md) before the first consequential
question or decision. Maintain `phase-1-collaboration-workboard.md` and repeat:

`inspect → research → assess → challenge → compare → recommend → author decides → record → propagate → recheck`

Do not treat a large idea dump, draft, populated template, or fluent synthesis as a completed
phase. Research decision-relevant evidence and contradictions before asking the author to choose.
For each material choice, show three to five substantively different options when that many are
defensible, state the evidence boundary and recommendation, ask one consequential question at a
time, and preserve selected and rejected variants.

Apply the standing **constructive opposition** rule: author preference may choose among defensible
paths, but it cannot become evidence or silently waive a critical gap. State the precise mismatch
and consequence, then offer bounded research, verification of project evidence, a
decision-matched study or probe when warranted, a better-supported alternative, a narrower claim,
or a visible block. If necessary evidence is declined, record `AUTHOR-DECLINED-EVIDENCE`, narrow
or block the claim, propagate the consequence, and retain a reopen trigger.

### Keep the session interactive and orchestrate parallel research

At the beginning of a nontrivial evidence batch, send a concise author-facing update naming the
research question, why it can change the framing, the bounded parallel tasks, and the next
discussion the batch is intended to prepare. Send another update when material evidence changes
the boundary, a human-only access barrier appears, or the decision packet becomes ready. Do not
replace the live collaboration with a final report dump.

When subagent capacity is available, delegate independent, bounded literature research and
analysis by default unless the task explicitly needs author assistance. Useful task splits include
full-paper retrieval and identity checks, methods/results/limitations audits, citation-chain and
authoritative-source searches, contradiction checks, closest-work comparisons, and
claim-to-source impact tracing. Each task must name its scope, expected evidence/locator output,
and read-only or non-writer boundary. Avoid duplicate searches unless independence is the point.

The lead agent remains the sole durable-artifact writer and owns synthesis, evidence ratings,
claim changes, workboard updates, and all author questions. Treat a subagent report as analysis,
not as a replacement for the underlying source: reconcile it against the opened full copy,
preserve exact locators and contrary findings, and resolve disagreements before propagation.

Ask the author for help only when research explicitly requires lawful publisher/library access,
CAPTCHA or institutional authentication in the author's headed browser, a missing local or project
artifact, tacit project knowledge, values, constraints, resources, or a consequential choice. Do
not ask the author to perform routine discovery, screening, or analysis that available subagents
can complete. If no subagent slot or facility is available, continue locally rather than stopping.

### Ground research in complete sources

Every retained research reference must have an obtained, saved, and opened full copy. Abstracts,
snippets, AI summaries, or another paper's paraphrase may discover candidates but cannot ground
claims or comparisons.

Read [citation-integrity.md](citation-integrity.md) before writing the first
citation-bearing artifact. Maintain stable `references.csv` keys across phases and use explicit
`[@CitationKey]` tokens in reader-facing prose. Treat an unknown key, duplicate key, alias
collision, or unresolved citation shorthand as a blocking defect rather than guessing a link.

For every material claim, record the source, method, population/context, sample or coverage,
result, uncertainty, limitation, and exact locator. Read
[evidence-protocol.md](evidence-protocol.md) before motivation research or claim
assessment. Maintain `evidence-strength-register.md` as a reusable, claim-specific audit cache.
Read [claim-focused-writing.md](claim-focused-writing.md) before translating that complete
internal record into author discussion, report narrative, outline language, or downstream writing
guidance.
Record source-ingestion completeness separately from claim strength, apply the critical-risk-of-bias
veto before assigning `ES3`, and state the conditions that require re-review. An unmarked source is
unassessed, not strong evidence.

Maintain `source-resolution.csv` as the machine-checkable acquisition queue. `UNASSESSED`,
`DISCOVERED`, `ACQUIRING`, and `FULL_TEXT_OBTAINED` are transient states, not end-of-round
dispositions. Before declaring a bounded source audit or research round closed, every potentially
decision-relevant source must be:

- `FULL_TEXT_ASSESSED`, with the full-copy, review, and evidence-register locators;
- `SCREENED_OUT` before retention or claim use, with a specific relevance reason;
- `SUPERSEDED`, with the verified stronger source and consequence recorded; or
- `NEEDS_AUTHOR_SOURCE_ACCESS`, after the exact access request has actually been surfaced in the
  conversation.

At phase readiness, every HTTP(S) citation key in `references.csv` must appear in the ledger; only
explicit `internal:` project-evidence keys are exempt. A retained full-text row must resolve back
to `references.csv`. A `SUPERSEDED` row must point by source ID or citation key to a different
retained `FULL_TEXT_ASSESSED` row with a stable citation key—never a missing, self, transient, or
ambiguous replacement. A `NEEDS_AUTHOR_SOURCE_ACCESS` row must include the actual non-future
surfaced date, stable session/conversation/workboard locator, affected claim IDs,
fallback/narrowing consequence, and reopen trigger; placeholders do not close the row. Separate
multiple affected claim IDs with `||`. At bounded-round closure and phase readiness, every ID must
resolve exactly in `claim-evidence-ledger.csv`; free-form claim prose cannot stand in for stable
claim identity.

This applies to sources discovered by search, supplied bibliographies, citation chains, full-paper
references, NotebookLM, and late-found-work audits. Do not call an audit complete while leaving
“obtain full copy” as a future action. Run
`scripts/check_source_resolution.py PROJECT_DIR --end-of-round` before an end-of-round report or
summary and `--phase-ready` before a readiness decision.

It also applies to candidate files already present in the governed project repository or source
store. At the start of a bounded audit and again before closure, use `rg --files` to inventory the
declared source/import roots, including ignored or governed full-text and extraction directories.
Resolve every candidate file by bibliographic identity to a `source-resolution.csv` row, including
retained, screened-out, superseded, and access-blocked dispositions. A file is not reconciled merely
because it is readable, extracted, mentioned in prose, or resembles another paper's title. Record
the roots, file count, accounted count, unresolved identities, timestamp, and the literal marker
`LOCAL_SOURCE_FILES_RECONCILED` in `source-manifest.md`. Any unresolved candidate that could change
a claim, mechanism, rank, comparator, or study requirement blocks bounded-round closure.

Here, “end of round” means a declared bounded-audit/research-round closure or deliverable, not a
brief in-progress status update while acquisition continues. A progress update may show transient
rows, but it cannot be used to pause avoidably, claim completion, or postpone an exact access
request once lawful routes have been exhausted.

Read
[motivation-claim-strengthening.md](motivation-claim-strengthening.md) before resolving
motivation or problem-definition claims marked `hypothesis` or `unsupported`. Do not let those
labels become a static inventory: research, narrow, contradict, supersede, retire, or route each
consequential claim to the smallest original project evidence need.

### Escalate human-only source access

Do not merely log an inaccessible decision-relevant source and end with a progress report. After
trying lawful independent routes—including the DOI/publisher, open repositories, author or
institutional copies, supplements, alternate renderings, and any university-library route already
available to the author—record the exact work and every failed route in
`missing-full-copies.md`. Continue all non-dependent research first, then surface the smallest
concrete author action that can unblock the highest-priority source.

An access-assistance request is not a framing-choice gate. Ask it even when the author has said
not to judge, rank, or choose yet. State:

- the exact citation, DOI/canonical URL, and why the full paper could change a claim, rank, or
  comparison;
- the exact obstacle and routes already tried;
- one concrete action: connect through their university IP or university VPN and retry in the same
  headed browser, attach a lawfully obtained PDF, complete the CAPTCHA or institutional sign-in in
  their own headed browser and say when it is ready, or provide an authorized accessible link; and
- the fallback evidence boundary if access remains unavailable.

Never ask for passwords, cookies, session tokens, browser profiles, or copied authentication
material. A VPN connection is a connectivity state, not authentication material: ask the author to
connect it themselves, then retry access without inspecting or changing its configuration. If a
human-only access barrier still blocks decision-relevant verification after
non-dependent work is exhausted, use `NEEDS_AUTHOR_SOURCE_ACCESS` and make the access request the
next user-facing question. Do not call the phase complete or substitute an AI summary. A
non-decision-relevant inaccessible candidate may remain visibly excluded with its re-review
trigger.

When the author downloads a paper manually, ask them to attach it or name the exact local path.
Then verify the file identity, open the full methods/results/limitations and relevant supplements,
update `source-resolution.csv`, `source-manifest.md`, `missing-full-copies.md`, and
`evidence-strength-register.md`, and resume the analysis that was blocked. Do not leave the request
resolved merely because a file appeared.

### Create one NotebookLM notebook per project

Use Gemini NotebookLM through `notebooklm-mcp-cli` to organize sources and synthesis. Create a new
notebook even when the researcher already has another project's notebook. Use a headed Chrome
session for authorized publisher access and author-mediated authentication.

If the CLI is missing, explain the install and registration steps for both Codex and Claude, obtain
permission before user-level installation, and do not silently substitute ungrounded model memory.
Read [notebooklm-research.md](notebooklm-research.md) before setup or source ingestion.
Create `notebooklm-maintenance.md` from the asset and reconcile the human-facing source list after
each bounded research round. Do not leave broken, CAPTCHA, machine-only, unassessed, duplicate, or
superseded objects mixed invisibly with usable evidence. Preserve unique content and ask the author
to confirm the exact source-ID set before irreversible deletion.

Treat the repository and NotebookLM as private, governed project stores. Copyright, license, and
redistribution status must not block or delay repository storage, version control, or NotebookLM
upload and does not require separate per-source author confirmation. Keep every retained full
source under `research-framing/sources/full-text/`, mirror it into NotebookLM by default, and record
both the repository-relative path and source ID. A missing copy is an unresolved technical
discrepancy, not an acceptable copyright or license disposition.

As soon as the project workspace exists and the notebook is created or resolved, record its exact
ID, user-facing title, and profile name without credentials in both `source-manifest.md` and
`agent-context.json`. Update both in the same work round after any notebook rename, replacement,
account-profile change, or reconciliation. This durable scope lets Codex `$gpt-pro` and Claude
Code `/gpt-pro` expose the correct notebook through the same read-only CLI broker without asking
the author to repeat its name.

### Treat the project as unfinished

Label claims as one of:

- `established-external`: supported by checked published or authoritative evidence;
- `inferred-external`: a bounded analytical conclusion from checked external evidence that the
  source does not state directly; never use it inside the default prior-work contribution
  boundary or to infer an absent capability from silence;
- `observed-project`: supported by checked project data or artifacts;
- `planned`: the team intends to build or study it;
- `hypothesis`: plausible but untested;
- `aspiration`: desired broader value; or
- `unsupported`: no current evidence.

Never convert `planned`, `hypothesis`, or `aspiration` into a present-tense capability or
contribution. Scope `inferred-external` conclusions to the checked published or demonstrated
system and keep them outside the explicitly claimed-and-demonstrated contribution boundary; never
turn them into technical impossibility or claims about unpublished variants. The research outline
must say what future work would establish each important project claim.

## Workflow

### 1. Inspect and establish the starting state

Read all user-supplied materials before interviewing. Inventory:

- problem and target people;
- current practices and workarounds;
- claimed pain, consequence, and why-now;
- related work already known;
- proposed approach and alternatives considered;
- formative work, designs, prototypes, studies, or results, if any;
- candidate contributions and terminology;
- constraints, access, ethics, safety, and timeline;
- citations and full copies already available.

Begin `starting-state.md` and `phase-1-collaboration-workboard.md` in the session. Do not create
durable copies until Step 3 resolves the project repository; then instantiate the asset templates
there. Use the workboard to expose every Phase 1 area, the highest-consequence movable uncertainty,
independent research in progress, and the next one author question. Use this starting-state table:

| Element | Current statement | Evidence/status | Confidence | Open question |
|---|---|---|---|---|

Mark imported prior-phase conclusions as hypotheses until checked here. Do not force the user to
re-answer facts already present in their materials.

### 2. Interview for consequential unknowns

Batch two to six tightly related, low-risk factual clarifications when they can be answered from
author knowledge without research and are not sequentially dependent. Invite concise numbered
answers, then record and propagate the batch once instead of rerunning the full protocol after each
fact. Ask one question at a time for consequential choices, constructive-opposition gates,
sensitive/access actions, or dependencies where an earlier answer changes the next question. Give
a short evidence-based interpretation before consequential questions. Before motivation evidence
is synthesized, use the interview to establish factual scope, direct observations, existing
artifacts, access, and constraints. Do **not** ask the author to rank consequences or choose which
one should motivate the project. Once target people and activity are bounded enough for meaningful
searches, run the consequence-severity research gate in Step 4.
Prioritize questions whose answers change the research direction:

- Who experiences the problem, during what activity, and what do they do now?
- What consequences has the team directly observed, and through what artifact or method?
- What has the team directly observed that published work may miss?
- Why is the problem newly important, or why is an old problem newly solvable?
- What is the closest existing solution, and what does it already do well?
- What new user experience or knowledge could the approach enable?
- What would make the proposed direction not worth pursuing?
- Can the team access the people, setting, expertise, and technology needed to test it?

Separate practitioner needs from expert/instructor/organizational needs when relevant. Respect the
author's domain knowledge; challenge inference quality, not unsupported stereotypes about the
domain.

### 3. Create the project research workspace

Read [repository-boundaries.md](repository-boundaries.md), then resolve the
project-specific repository before writing durable artifacts. Never create project research data
inside the reusable skill repository. If the project repository has not been created or provided,
continue only read-only inspection, research, and interactive planning in the session; request the
target when durable writing becomes necessary. Once resolved, create a durable project folder
without overwriting existing material. Run:

```bash
python3 scripts/initialize_phase1_workspace.py PROJECT_REPOSITORY --project-name "PROJECT NAME"
```

The initializer must create every missing mandatory template, the source/full-text and working
directories, a root `README.md`, and the initial rendered and audited HTML shelf without
overwriting existing artifacts. Do not approximate this by copying only the files immediately
needed for the current analysis. Include:

```text
research-framing/
├── agent-context.json
├── starting-state.md
├── sources/
│   └── full-text/
├── phase-1-collaboration-workboard.md
├── author-decisions.md
├── source-manifest.md
├── source-resolution.csv
├── imported-bibliography-accountability.csv
├── notebooklm-maintenance.md
├── evidence-strength-register.md
├── references.csv
├── search-log.md
├── missing-full-copies.md
├── claim-evidence-ledger.csv
├── motivation-claim-research-queue.md
├── motivation-evidence-map.md
├── authoritative-source-map.md
├── current-practice-audit.md
├── consequence-severity-ranking.md
├── acm-sigchi-related-work-audit.md
├── related-work-search-recall-audit.md
├── related-work-matrix.md
├── related-work-contribution-tier-audit.md
├── ranked-related-work-positioning.md
├── prior-work-contribution-boundary.md
├── prior-work-evidence-accounting.csv
├── idea-provenance-ledger.csv
├── late-found-work-postmortem.csv
├── novelty-regression-sentinels.yaml
├── citation-chain-log.md
├── exemplar-analysis.md
├── approach-options.md
├── contribution-options.md
├── terminology-contract.md
├── decision-packets/
├── related-work-quadrant-variations.md
├── quadrants/
├── reviewer-panel/
├── research-framing-outline.md
├── phase-2-handoff.md
└── reports/
    ├── phase-1-progress.html
    ├── literature-and-evidence.html
    ├── phase-1-final.html
    ├── artifact-index.html
    └── [reader-facing HTML mirrors of the working audits, registers, matrices, and positioning]
```

The project root must also contain `README.md` with direct relative links to
`phase-1-progress.html`, `literature-and-evidence.html`, `phase-1-final.html`, and
`artifact-index.html`. These navigation and reader-view files are workspace invariants from the
first durable write onward.

Copy the templates from `assets/` where useful. Record each full source's canonical repository path,
NotebookLM notebook ID, and source ID, but never credentials, cookies, or raw participant data.
Copyrighted full sources are expected in both private stores and may be tracked in version control
without license or redistribution screening. When NotebookLM is used, persist the vetted evidence
bar and source markings in the notebook as a note or dedicated text source. Treat a
NotebookLM-generated rating as a review aid, not the final rating: reconcile it against the opened
original before caching it.

Instantiate `agent-context.json` from the asset and replace its project-name placeholder
immediately. Keep it as a small pointer map:

- `phase.skill` remains the exact `hci-motivation-and-contributions` skill name;
- `phase.status` is `active` or `paused` while Phase 1 is live and `complete` only after the handoff
  and final reconciliation;
- `context.always_include` points to the workboard, author decisions, and starting state;
- `context.include_when_relevant` points to the source manifest, NotebookLM maintenance record, and
  Phase 2 handoff;
- `context.repo_read_allow` stays narrowly limited to project material the author has put in scope;
  its default is `research-framing/**`, not the whole repository; and
- every path is relative to the live project repository.

The manifest is shared configuration for Codex and Claude Code. Do not store conversation history,
duplicated decision summaries, absolute machine paths, remotes containing credentials, auth data,
or participant data in it. The pointed-to artifacts remain authoritative. Refresh the manifest
after a material path, phase-status, skill, notebook, or profile change and before every terminal
handoff.

### 4. Build the motivation evidence chain

Research and map:

`larger human concern → target population/context → current practice → unmet need → consequence → why now → opportunity`

Before synthesizing the larger concern or normative baseline, read
[authoritative-domain-sources.md](authoritative-domain-sources.md) completely and create
`authoritative-source-map.md` from the asset template. Decompose the active claims into domains,
identify each relevant body's actual remit, verify the current canonical first-party source, obtain
and open the exact full document, and record its document type, population/jurisdiction,
date/version, supersession state, exact supported claim, and explicit cannot-support boundary.
Authority is claim-specific: an official meeting report, guideline, standard, surveillance
estimate, product manual, and venue roster do different evidentiary work. A prestigious
organization never automatically upgrades directness or `ES` strength.

Reach `AUTHORITATIVE_DOMAIN_SOURCES_MAPPED` only when every active domain has a verified row or a
visible missing/conditional-authority route. For example, WHO may be appropriate for a global
public-health agenda claim, AASM/SRS for an applicable sleep consensus, ACSM for an applicable
exercise/sports-medicine position, product vendors for current capability facts, and SIGCHI for
current venue scope. These are routing examples, not a permanent list. Do not ask the author to
select a motivation frame while this map is incomplete.

Before synthesizing that chain, read
[motivation-claim-strengthening.md](motivation-claim-strengthening.md) completely and
create `motivation-claim-research-queue.md` from the asset template. Sweep every active
`hypothesis` and `unsupported` row in the claim ledger and assign one primary resolution route:
external research, official practice audit, author/project evidence, future system evaluation, or
retirement/supersession. Create `current-practice-audit.md` whenever a claim concerns current
products or documented controls.

Work the queue recursively. Prioritize motivation and problem-definition claims that can change
whether the project is worth pursuing: target behavior/population, current practice, unmet need,
consequence, and why-now. Search exact and neighboring constructs, full primary sources, official
documentation, backward/forward citations, and contradictions/nulls. After each material batch,
update the claim ledger with bounded replacement wording and sweep it again.

Do not use adjacent external work to “prove” the proposed system's progressive attenuation,
visual/network mechanism, experience, adherence, or outcome. Route those claims to the smallest
Phase 2 premise test or Phase 3 comparison. Do not ask the author to judge or choose among
unsupported claims while this research is underway; ask only for factual corrections, existing
project evidence, or concrete help with a decision-relevant full-source access barrier.

Reach `MOTIVATION_CLAIM_AUDIT_COMPLETE` only when every active motivation/problem-definition
`hypothesis` or `unsupported` claim has a precise route, documented research or official audit,
explicit disposition, and either sufficient bounded support or the smallest named project evidence
action. A report that merely repeats the labels does not pass.

Use authoritative sources for population health, policy, standards, or large-scale facts. Prefer
systematic reviews, highly relevant primary studies, and top HCI venues for the questions they can
actually answer. Industry evidence may establish adoption or practice when methodology and
interests are disclosed. The team's own studies may directly establish a narrow need when their
method and limits are clear.

For every proposed statistic or consequence, record what was measured, by whom, using what method,
for which population and timeframe, and with what uncertainty. Quantification should sharpen
magnitude or trajectory; do not decorate the argument with weak numbers.

Before synthesizing, create or update `evidence-strength-register.md` from the asset template. Every
retained source receives an ingestion tag (`FULL`, `PARTIAL`, or `BROKEN`) and a claim-specific
strength tag (`ES3`, `ES2`, `ES1`, or `ES0`) with a narrow supported claim, decisive limitation,
and re-review trigger. Reuse a cached assessment only when the source/version and the proposed
claim, population, exposure, outcome, and causal wording are unchanged. Never promote a source
because its title says “randomized,” its sample is large, or NotebookLM rated it highly; the
critical-risk-of-bias veto still applies.

Before building motivation frames, read
[consequence-severity-research.md](consequence-severity-research.md) completely and
create `consequence-severity-ranking.md` from the asset template. Research immediate, proximal,
next-activity, and longer-term consequences across full sources. Keep severity, prevalence, causal
proximity, and evidence certainty separate; record effect magnitude, uncertainty, practical
importance, duration, reversibility, subgroup distribution, and every supported link in the
consequence chain. Rank consequences with ties and conditional ranks where warranted.

Do not ask the author to rank, select, or approve consequences while this gate is incomplete.
Present the evidence-ranked synthesis first. Only after it reaches
`CONSEQUENCE_RANKING_COMPLETE` may the later motivation-frame gate ask the author to select or
combine rhetorical frames; the evidence ranking remains independent of that choice.

Create three to five **motivation frames**, such as:

- population consequence;
- breakdown in an important human activity;
- inequity or access;
- emerging-device or societal shift;
- newly enabling technical capability.

Each frame must include a full-text evidence chain, what it foregrounds, what it risks obscuring,
and what evidence would weaken it. After the consequence-ranking gate is complete, ask the author
to select or combine frames.

### 5. Research the related-work landscape

Read
[acm-sigchi-related-work.md](acm-sigchi-related-work.md) and
[forward-citation-expansion.md](forward-citation-expansion.md) completely before searching.
Run a required native ACM Digital Library pass and create
`acm-sigchi-related-work-audit.md` from the asset template. Start with CHI, then prioritize close
work from the relevant conferences on the current official SIGCHI sponsored/co-sponsored roster.
Record the roster check date, exact ACM DL queries and result counts, and an inclusion or specific
exclusion decision for every plausibly close CHI/SIGCHI work.

This is a coverage and community-situating requirement, not an evidence shortcut. Venue priority
never upgrades ingestion completeness, directness, method validity, or claim-specific
`ES1`–`ES3` strength. Keep non-ACM work when it is the strongest evidence for a claim, and exclude
surface-level ACM matches when their causal interaction approach is not relevant.

Create `related-work-search-recall-audit.md` from the asset template before declaring the
landscape saturated. First freeze a **target-problem identity contract** that states the target
people, focal activity, triggering or temporal context, unwanted state or episode, and intended
change or outcome. Keep the proposed design and any hypothesized causal mechanism separate from
that problem identity. Build separate synonym lattices for the problem and causal mechanism,
including access state, changed parameter, progression variable, duration/cadence, friction or
manipulation channel, and outcome tradeoff. Saturate the same/similar-problem branch before using
distant work to fill a ranked set. Run mechanism-only and disjunctive queries in addition to
target-heavy conjunctions. A first page or first 20 records from a large result set never counts as
coverage: refine, stratify, or paginate until a documented stopping criterion is met.

Use known close works as **positive-control sentinels** only after drafting the lattice. Each should
be retrievable without relying solely on its exact title or author; a miss requires a query repair,
not a claim of saturation. Triage every plausibly mechanism-relevant title in the reference list of
each closest full paper. Build the broader high-leverage seed portfolio, then run two independent
cited-by routes, newest and relevance/citation sorts, material large-graph partitions, and
successive promotion waves. Stop only after a complete zero-yield wave produces no new
decision-relevant work. If material work appears after saturation was claimed, record it in
`late-found-work-postmortem.csv`, screen its sibling citing records, repair the missed route, add a
non-title/non-author test to `novelty-regression-sentinels.yaml`, and rerun the affected evidence,
capability collision, contribution credit, novelty boundary, gap, contribution tier, ranking, fair
comparator, study requirements, and broader-HCI synthesis.

Search in two required categories:

1. work addressing the **same problem through different approaches**; and
2. work addressing a **different problem through a similar approach**.

Also include same-problem/similar-approach work whenever it exists; these are often the closest
predecessors. Keep the categories as separate portfolios. The primary problem-space ranking draws
only from same-specific-problem and similar-problem work. Different-problem/similar-approach work
belongs in a mechanism/capability-collision portfolio only when positive evidence shows the
relevant operation actually ran. A `DEMONSTRATED_UNCLAIMED` operation may therefore retire or
narrow a capability claim while receiving no attributed contribution credit. It cannot displace a
closer problem comparator. Route proposals to idea provenance instead.

“Similar approach” means a genuinely similar **causal interaction approach**: the intervention
acts on people, activity, or coordination through substantially the same mechanism. A shared
modality, device, sensing technique, personalization label, multi-user topology, or output channel
alone is insufficient. For example, two systems delivering different audio to different people do
not become contribution comparators when one manages concurrent conversations and the other guides
linked physical actions. Retain such a work as a design or mechanism foundation when it informs a
choice; otherwise omit it from the comparison corpus.

### Run a component-foundation and falsification pass

Closest-comparator recall and mechanism foundations are separate gates. For every approach
component present in supplied materials or an active option—and specific enough to affect
feasibility, novelty, mechanism, or evaluation—map:

`component → operational change → proximal percept/behavior/mechanism → desired outcome → failure or side effect`

Then search each link and its counterevidence using the vocabulary and databases of the discipline
that studies it. For example:

- visual/display attenuation may require grayscale, brightness or luminance, contrast, spectrum or
  color temperature, blue-light filter, display physiology, circadian, perception, and
  accessibility searches;
- network attenuation may require latency, startup delay, rebuffering, throughput degradation,
  video quality of experience (QoE), engagement, abandonment, perceived failure, and networking systems
  searches; and
- an inherited intervention or product may require a **product lineage** pass across exact product
  names, authors, versions, evaluation papers, later longitudinal studies, and current-practice
  provenance.

Do not force these works into the closest-HCI ranking. Classify each as contribution comparator,
design/mechanism foundation, technical-feasibility source, motivation/physiology evidence,
counterevidence, analogy only, or screened out. A source can be essential to the design rationale
while remaining `ES1` or unusable for the target outcome.

#### Supplied-bibliography accountability

Account for every bibliographic item in supplied reports, drafts, and reading lists in
`imported-bibliography-accountability.csv`. Imported references are discovery seeds, not author
decisions and not automatically relevant. Give each an include, full-text-acquire, or specific
screen-out disposition. Any material item that could change an active mechanism, claim, rank,
comparator, or study requirement must resolve to a terminal `source-resolution.csv` row and, when
retained, to its `prior-work-evidence-accounting.csv` rows.

For every retained seed, run a **claim-matched seed-upgrade pass**. Search independently for:

- a competent authoritative body and current official document when the claim concerns guidance,
  burden, policy, standards, or current product capability;
- a stronger systematic synthesis, randomized or quasi-experimental design, validated measure, or
  larger/more representative dataset when the claim concerns effects or magnitude;
- a more direct population, behavior, context, intervention, comparator, or outcome;
- a current or corrected version and relevant contradictory evidence; and
- top HCI or domain venues when they are plausible discovery routes.

Do not collapse these axes into venue prestige. A famous venue can contain an adjacent or weakly
identified result; a lower-profile source can remain the most direct valid evidence. Record the
queries, databases, comparison, and disposition: `retained-with-bounds`, `corroborated`, or
`SUPERSEDED` by stable key/locator. Author preference cannot stop this search, upgrade the seed's
strength, or discard stronger contrary evidence. The supplied bibliography never sets the
evidence ceiling.

After locating seed works:

1. obtain and save the exact full work;
2. read its Abstract, Introduction, Related Work, method/system, results, limitations, and
   references;
3. follow relevant backward references;
4. run the complete multi-route forward-citation expansion protocol for newer work;
5. read how newer papers characterize, build on, and delimit the seed;
6. obtain and verify each retained exact work; and
7. promote every decision-changing or vocabulary-expanding work and repeat until a complete
   promotion wave yields no new decision-relevant work.

For the closest HCI works, atomize every material proposition and complete the independent
`AUTHOR CLAIM`, `DEMONSTRATED ARTIFACT OR STUDY`, `OPERATED CAPABILITY`, `EVALUATED RESULT`,
`CAPABILITY COLLISION`, and `CONTRIBUTION CREDIT` fields. Use demonstrated operation to decide
capability collision and claimed-plus-demonstrated evidence to decide contribution attribution.
Preserve future-work proposals only in `idea-provenance-ledger.csv` with collision and credit
`NONE`. Read the works' Related Work and follow that lineage for later Discussion, not as evidence
that a capability or contribution was realized.

Decompose mixed systems by channel. Give user-action-to-command, conventional-input,
sensed-or-computed-state-to-adaptation/reward, condition-to-gating, and system-state-to-feedback
paths separate rows. A mapping such as spoken "next" to an advance-one-slide command establishes
only that command, not backward navigation, arbitrary slide selection, general presentation
control, or a whole-system class. A task-performance score that yields a badge is
computed-state-to-reward, not user-action-to-command. Reject a whole-system label unless positive
evidence qualifies every required channel.

Before calling two interventions gradual, progressive, adaptive, soft, hard, or similar, decompose
their access state, activation selector/gate, changed parameter, within-active progression,
duration, onset/cadence, cap/reset, scope, override/exceptions, selector, intention/goal anchor, and
configuration burden. Separate what happens **before activation** from an ease-in **after
activation**; a post-usage-budget ramp is not a pre-bedtime taper. A cumulative daily-use budget
regulates quantity across an accounting day and may activate at an unpredictable clock time,
whereas a target-bedtime schedule is anchored to an intended transition at a clock/event time.
Do not assume that people specify one anchor more clearly: treat claims that target bedtime is more
concrete or stable than a daily cap as a project hypothesis until direct evidence compares
certainty, calibration, and day-to-day revision. Record whether a threshold is intrinsic or merely
study-fixed, and leave unreported reset behavior unresolved. Do not confuse graduated block
**duration** with graduated attenuation **intensity**, or intermittent access windows with a
nonbinary intervened state. State the literal operational difference before assigning a
contribution tier.

Normalize away hardware, sensor, operating-environment, model, app, game, and delivery-platform
labels. Reproducing the same demonstrated causal interaction on another platform has zero
contribution credit by default, even when the port required substantial engineering. Count only an
adaptation atom for which complete-source evidence demonstrates nontrivial reusable adaptation
knowledge, a new use class, or a directly validated empirical finding. A zero-credit port can
still create a collision at the demonstrated operated-capability level.

For each reference, track:

- whether it appeared in the supplied draft or materials;
- whether the skill found it independently through a documented route;
- the discovery route;
- what it contributes positively;
- what this project learns from, builds on, or is inspired by;
- the factual difference from this project; and
- uncertainty caused by unfinished project decisions.

Read [related-work-positioning.md](related-work-positioning.md) completely before
classifying or comparing retained work. Apply its relationship gate, existing-workflow map,
current-practice collision check, communication-topology analysis, activity-versus-implementation
counterfactual, conjunctive claim test, terminology contract, shared-awareness check, contribution
strength ladder, target-problem identity contract, problem-proximity bands, separate-portfolio
rules, and proximity ordering.

The required audit must cover every catalogued reference. Read
[prior-work-contribution-boundaries.md](prior-work-contribution-boundaries.md) and maintain
`prior-work-contribution-boundary.md` plus all five CSV/YAML accounting and accountability
artifacts. Credit each
work's claimed-and-demonstrated contribution, then separately state every demonstrated-unclaimed
capability collision before stating the most concise consequential difference. Separate and rank workflow
significance, interaction or information-distribution capability, setting/activity boundary,
implementation/design rationale, and untested outcomes rather than assuming a fixed hierarchy.
Treat under-description as unresolved by default. Give a demonstrated-unclaimed artifact operation
its evidence-supported capability collision but contribution credit `NONE`. Give a
claimed-undemonstrated atom neither.
Assign operated capability `NO` only from positive artifact evidence that settles the audited
version; source silence may create only search priority or a reopen query. Keep package evidence at
package scope, apply the port gate, and reject equivalence language based only on nonsignificance.
Generate three to five evidence-grounded comparison sentences before asking the author to choose
the emphasis.

Before the gap or contribution decision gate, create `ranked-related-work-positioning.md` from the
asset template. Assign every work a problem-proximity band before ranking. Rank up to approximately
ten verified full works in the primary problem-space portfolio lexicographically: same-specific
problem before similar problem, then target people/activity/context fit, causal
interaction-mechanism match, ability to change the gap or novelty boundary, and value as a fair
empirical or design comparator. A paper about a different objective cannot move upward because it
shares broad vocabulary, an application domain, or one mechanism. If fewer than approximately ten
same/similar-problem works survive full-text review, include all and disclose the shortage rather
than padding with adjacent or conceptual work. Venue priority affects search coverage, not the
ranking. State ties and rank sensitivity instead of inventing precision.

Maintain separate **mechanism/capability-collision** and **concept/theory/foundation** portfolios.
A different-problem work may be a decisive claim-specific collision for an exact mechanism or
capability when positive evidence shows that operation ran, including a
`DEMONSTRATED_UNCLAIMED` operation, and should be discussed there; it is not a closest overall
problem comparator. Keep contribution attribution separate. Proposals remain idea provenance with
collision and credit `NONE`. Evidence strength, venue, recency, and citation count remain separate
from problem proximity.

For every work in the primary ranked set, write one complete **working positioning paragraph** that
credits its claimed-and-demonstrated contribution, separately states any demonstrated-unclaimed
capability collision, states the material method/evidence boundary, names the literal operational
difference from the planned project, identifies what the project inherits, credits any current-
platform/product baseline separately from the HCI paper that adapted it, characterizes the relationship as
replication/extension/contrast/instantiation/test, and ends with the strongest safe claim
boundary. Write claim-specific comparison notes for mechanism collisions instead of presenting
them as equally close overall predecessors. These are reviewer-ready comparison drafts for
research reasoning, not a final Related Work section. Keep capability/overclaim risks, idea
provenance, foundations, secondary works, and problem-space shortage or search risk visible, and
re-rank when the target problem identity, activity, mechanism, contribution layer, full-copy
state, or closest-work corpus changes.

Before the gap or contribution decision gate, synthesize how the project sits in the broader HCI
community: name the existing community conversation, the unresolved design tension or knowledge
uncertainty, what this project could teach beyond one app/device/population, and the boundary on
that transfer. Use idea provenance in Discussion to show how demonstrated findings realize, test,
complicate, or bound prior aspirations while keeping both capability collision and contribution
credit at `NONE`.
Step 5 remains incomplete until the ACM/SIGCHI audit is marked
`ACM_SIGCHI_LANDSCAPE_AUDITED` **and** the search-recall audit is marked
`RELATED_WORK_SEARCH_RECALL_AUDITED`. The accounting artifacts must also be internally valid under
`scripts/check_prior_work_accounting.py`.

If an exact full copy remains inaccessible, follow **Escalate human-only source access** above.
Exclude it from claim support and chart placement until verified. Recording it in
`missing-full-copies.md` does not count as asking the author; the conversation must contain the
specific access request. An `UNASSESSED` or acquire-only row cannot satisfy the landscape,
foundation, or end-of-round gate.

### 6. Establish the terminology contract

Treat terminology as claim discipline, not late copy-editing. Before contribution wording or chart
labels converge, create `terminology-contract.md` and read
[terminology-contract.md](terminology-contract.md) completely.

First decompose each central idea into independently verifiable dimensions, including:

- people, task, activity, and unit of analysis;
- intended recipient or addressee;
- whether recipients receive the same or different content;
- who authors, selects, configures, or infers that content;
- whether a person can adjust a specific dimension;
- whether the system changes support from evolving state or performance;
- delivery timing and whether streams actually overlap;
- access, visibility, or audibility; and
- claimed experience or outcome.

Then present three to five coherent terminology systems. For each central term, state its
operational definition, likely reader inference, supporting evidence/status, what it does **not**
imply, allowed variants, unsafe variants, first-definition location, and intended scope. Do not
force one adjective to carry several dimensions. A useful hierarchy may select a concrete default
term, a structural contrast term, a narrowly scoped tailoring or control term, and reserved terms
that remain unavailable without stronger evidence.

Ask the author to approve the semantic contract before choosing the paper-facing lexical spine.
The **terminology contract** fixes meanings and evidence boundaries; the **lexical spine** chooses
which approved terms do which rhetorical jobs. Record both decisions separately and reopen them
when the approach, system, study, or closest-work evidence changes. Until approval, label every set
`candidate` and do not propagate a preferred set as final.

For a general audience, make the selected system lead with a familiar entry term, define the exact
scientific or technical construct or metric at first use, and specify the approved later short
form. Do not simplify by treating neighboring constructs as synonyms.

### 7. Synthesize gaps and approach hypotheses

Create a matrix comparing current practice, products, and research using neutral dimensions exposed
by the full texts. Distinguish:

- **capability gap:** people cannot currently do something important;
- **experience gap:** the capability exists, but meaningful human outcomes or use remain poor;
- **cost/access gap:** comparable value exists but adoption costs exclude relevant users; and
- **knowledge gap:** an important phenomenon, mechanism, or design tradeoff remains unknown.

Generate three to five gap interpretations. For each, identify the closest work, exact distinction,
importance, why-now, existing-workflow boundary, risk of incrementalism, and evidence that could
falsify it.

Then generate three to five approach hypotheses. For each:

- describe the intended user experience, not only the technology;
- state the enabling insight;
- identify what is inherited from prior work;
- state the hypothesized advantage and likely costs;
- identify alternatives and failure modes;
- distinguish planned implementation from established capability; and
- name the smallest Phase 2 investigation that would test the premise.

Ask the author to choose, combine, or reject options. Do not optimize an approach before confirming
that it addresses the selected problem.

For each approach, derive the fair **future evaluation logic** from the claimed workflow change.
When a project proposes an additive layer, the informative comparison is normally the intact
current workflow versus that same workflow plus the proposed layer—not “no instruction,” “no
tool,” or another baseline that removes valued current practice. Record this as a Phase 3 evidence
requirement, not as an approved study design. If current practice already provides a shared
intervention, do not silently replace it with “no intervention”; compare it with the proposed
shared-plus-differentiated or otherwise augmented condition. Preserve any coordination value of
shared information unless the research question explicitly tests changing it.

After every consequential decision, update the workboard and `author-decisions.md`, retain the
complete option packet in `decision-packets/`, propagate the choice, and regenerate the progress
report. Never replace rejected alternatives with only the winning choice.

### 8. Explore positioning views

Build three to five two-axis chart variations from the same core corpus. The chart is a
communication and thinking artifact, not proof of novelty. Approximate placements are acceptable,
but every research point requires a checked full copy and a concise rationale.

Include:

- an axis pair aligned with the proposed contribution;
- a topology or use-context pair;
- a workflow-stage or activity-coverage pair when the project extends an existing practice; and
- at least one meaningful alternative exposed by the literature.

Use neutral, operational endpoints. Avoid “traditional → novel,” “bad → good,” venue prestige, or
paper quality. Show what each view reveals, compresses, and makes appear close. Recommend a view,
then let the author select it.

Read [related-work-quadrant.md](related-work-quadrant.md) before preparing charts.

### 9. Sharpen prospective contributions

Generate three to five coherent contribution packages, not synonym lists. Each package must specify:

- the larger problem and target people;
- the existing workflow and the precise stage being replaced, complemented, extended, or bridged;
- the current human intervention at that stage and the result of the current-practice collision
  check;
- the gap relative to the closest work;
- the workflow relationship or significance;
- the interaction or information-distribution capability;
- the setting or activity boundary;
- the implementation choices and design rationales, including whether any independently enables a
  consequential capability rather than merely instantiating the interaction;
- the proposed reusable HCI capability or knowledge;
- the empirical waist or planned instantiation;
- what is established now;
- what Phase 2 must build or learn;
- what Phase 3 must validate;
- the plausible broader HCI implication;
- what remains explicitly unclaimed;
- the fair future comparator that preserves valued current practice; and
- an author-approved terminology contract and consistent lexical spine with plain definitions.

A prototype, algorithm, interview set, or user study is usually a means, not automatically a
contribution. Use contribution language prospectively until evidence exists. Read
[terminology-contract.md](terminology-contract.md) and
[contribution-rubric.md](contribution-rubric.md) before presenting packages. If the
terminology gate is pending, show contribution packages as candidates and preserve their
terminology dependencies instead of silently resolving them.

Build every package against the six-field prior-work accounting and apply the same fields to the
focal project. Use positively operated capability for collision and claimed-plus-demonstrated
evidence for attribution. A `DEMONSTRATED_UNCLAIMED` operation can narrow firstness but receives no
contribution credit; a `CLAIMED_UNDEMONSTRATED` atom receives neither. Keep ideas and proposals
only for broader Discussion provenance, never capability or contribution novelty.

Separate these layers, then rank them—do not impose a universal order:

- **workflow relationship or significance:** how the work relates to an existing human process and
  why the change matters;
- **interaction or information-distribution capability:** how people can act, address recipients,
  receive content, or coordinate differently;
- **setting or activity boundary:** which consequential participants, interdependencies, objects,
  movements, risks, or constraints are present;
- **implementation/design rationale:** why a device, modality, interface, or form factor may realize
  the interaction; and
- **outcome hypothesis:** what might improve and therefore requires comparative evidence.

Choose the primary contribution as the strongest defensible consequential difference relative to
the closest comparator, not whichever layer appears first. A workflow relationship may explain
significance while an interaction or information-distribution capability carries the originality.
Record the selected primary layer, the ranking rationale, and the strongest fallback.

Do not promote a lower-level implementation choice into the primary contribution merely because it
is visually distinctive or technically difficult. If the hardware or medium is itself
contribution-bearing, state and support the human capability, outcome, or access change it enables.

### 10. Run a phase-aware constructive review

Use the seven lenses in [reviewer-panel.md](reviewer-panel.md). Review the live
workboard, frozen research outline, evidence maps, landscape, approach options, contribution
packages, decisions, and project materials.

Reviewers must not:

- demand polished paper prose;
- treat missing implementation or results as defects when they are not yet expected;
- prescribe elaborate systems or studies without explaining which uncertainty they resolve;
- optimize details before challenging the premise; or
- imply that the panel predicts acceptance or an award.

Synthesize concerns into concrete framing revisions, evidence needs, Phase 2/3 questions, or explicit
risks. Return material choices to the author.

### 11. Produce the research framing outline

Write `research-framing-outline.md` as an argument and decision outline:

1. **Larger concern:** authoritative evidence and why the broad issue matters.
2. **Specific human problem:** people, activity, current practice, unmet need, and consequence.
3. **Why now:** new problem/context or newly enabling approach.
4. **State of the art:** positive synthesis of the two related-work categories with capability
   collision separated from contribution attribution, demonstrated-unclaimed operation visible,
   and ideas/proposals kept separate.
5. **Gap:** selected interpretation and closest-work comparison.
6. **Approach hypothesis:** intended experience, enabling insight, inherited foundations, and risks.
7. **Research process:** what is known, underway, and planned.
8. **Terminology contract:** operational meanings, selected hierarchy, non-implications, and open
   terms.
9. **Prospective contributions:** selected package, empirical waist, and broader implication.
10. **Evidence boundaries:** established, observed, planned, hypothesized, aspirational,
    unsupported.
11. **Open decisions and stop/go risks:** what could still invalidate the direction.

Use bullets, evidence tables, argument links, and candidate language. Do not turn it into polished
Introduction prose.

### 12. Create the Phase 2 handoff

Write `phase-2-handoff.md` containing:

- selected problem, target people, activity, and stakes;
- existing workflow before, during, and after the focal activity;
- current informal human interventions and the current-practice collision result;
- the exact stage the approach replaces, complements, extends, or bridges;
- existing and proposed sender-recipient, content-distribution, concurrency, visibility, and
  selection-provenance structures;
- evidence-backed motivation and why-now;
- target-problem identity contract, primary same/similar-problem ranking, any shortage or residual
  search risk, separate claim-specific mechanism/capability collisions, gap, and adopted
  concept/theory/foundations;
- the six-field prior-work evidence accounting, capability collisions separated from attributed
  contribution credit, demonstrated-unclaimed and claimed-undemonstrated states, mixed-channel
  decomposition, port gates, source-silence queries, and idea provenance;
- imported-bibliography accountability, late-found-work postmortems, repaired routes, regression
  sentinels, and the final complete zero-yield promotion wave;
- component-foundation/falsification findings and product/intervention lineage that constrain
  related-work or contribution claims;
- stable citation keys and full-review locators for every source eligible for comparison or claim
  support;
- author-provided seed provenance, independent stronger/counter-source searches, and each
  retained-with-bounds, corroborated, or superseded disposition;
- every unresolved source, affected blocked or narrowed claim, exact author-access request and
  attempted routes, next action, and reopen trigger;
- selected approach hypothesis and rejected alternatives;
- contribution hypothesis, terminology contract, lexical spine, and explicit terms to avoid;
- consequential unknowns;
- formative research questions;
- UX/system requirements that are hypotheses, not fixed specifications;
- prototype questions and technical-risk probes;
- access, ethics, safety, privacy, and deployment constraints;
- proposed pilot and performance questions;
- fair future evaluation logic that preserves valued current practice;
- shared-awareness value, risk, and still-untested outcome claims;
- evidence needed later for each contribution;
- explicit return conditions for revisiting Phase 1.

Downstream design and writing may cite or compare only opened full copies or clearly marked project
evidence. They must not omit an unresolved source from the internal handoff, strengthen its
affected claim in prose, conceal counterevidence that materially constrains an active claim, or
convert a supplied seed into the evidence ceiling. Preserve the complete internal boundary while
marking which claim-local qualifiers are required in reader-facing prose; do not automatically
turn every limitation or unclaimed distal outcome into a disclaimer.

This handoff is optional input to Phase 2. The next skill must also accept any other starting
materials.

Reconcile `agent-context.json` against the final workboard, author decisions, source manifest,
NotebookLM maintenance record, and handoff. Set `phase.status` to `complete` only after that
reconciliation; the manifest then lets either Codex or Claude Code rehydrate the bounded handoff
without silently reactivating Phase 1.

### 13. Generate the HTML reports

Read [html-reports.md](html-reports.md), then run:

```bash
python3 scripts/check_prior_work_accounting.py research-framing/ --end-of-round
python3 scripts/check_source_resolution.py research-framing/ --end-of-round
python3 scripts/render_phase1_reports.py research-framing/
python3 scripts/audit_phase1_reports.py research-framing/
```

Regenerate:

- `phase-1-progress.html` after each evidence batch, option portfolio, author decision, or review;
- `literature-and-evidence.html` after every material literature-search pass; and
- all three reports before the Phase 1 completion decision.

Also regenerate `artifact-index.html` and the standalone reader-facing HTML mirrors for the working
audits, registers, matrices, and ranked positioning dossier. Markdown and CSV remain the editable,
diffable sources of truth; the HTML files are generated views. Link the shelf prominently from
`literature-and-evidence.html` so a reader does not have to locate or render source artifacts.

The reports must be self-contained, readable without the repository, and traceable to their source
artifacts. They must show missing inputs honestly. A final report never erases unselected
variations, superseded choices, evidence gaps, or reviewer concerns.

Keep evidence tables complete, but apply the claim-local caveat test to narrative summaries. State
supported claims directly, omit disclaimers about outcomes not claimed, and introduce familiar
terms before defining their exact scientific or technical meaning.

An end-of-round report may show `NEEDS_AUTHOR_SOURCE_ACCESS` only when the exact request, direct
URL, failed routes, and author action have already been surfaced. It may not call the source audit
complete while retaining `UNASSESSED`, `DISCOVERED`, `ACQUIRING`, or `FULL_TEXT_OBTAINED`. Before
`READY_FOR_PHASE_2` or `READY_WITH_RISKS`, rerun the source-resolution checker with
`--phase-ready` and run `scripts/check_prior_work_accounting.py research-framing/ --phase-ready`.
The latter must verify the eleven checked completion markers in
`prior-work-contribution-boundary.md`; prose assertions do not substitute for valid ledgers,
terminal imported-source rows, completed late-find repairs, passing sentinels, and a complete
zero-yield promotion wave.

Use the explicit citation-key contract in
[citation-integrity.md](citation-integrity.md). The renderer and audit must fail closed
on unknown tokens, duplicate keys, alias collisions, unresolved citation-like shorthand, missing
metadata, or broken destinations. Never repair a citation by adding an ambiguous bare-surname or
conceptual-phrase alias.

After the automated audit passes, inspect all three reports in a headed browser. Check desktop and
narrow widths, citation links and hover tips, long tables, escaped characters, charts, decision
history, and missing-artifact messages. Fix the underlying artifact or renderer, regenerate, and
re-audit. Do not deliver unchecked generated HTML.

Before every commit, push, or terminal handoff that contains material Phase 1 changes, regenerate
the complete HTML shelf, rerun the auditor, and verify that every report linked from the root
`README.md` exists in the staged or committed tree. A durable batch is not publishable when its
README is absent, its links are broken, or its reader views are missing or stale.

## Completion states

- `READY_FOR_PHASE_2`: selected framing is evidence-grounded; key uncertainties have bounded Phase 2
  investigations.
- `READY_WITH_RISKS`: direction is promising, but named evidence or feasibility risks remain.
- `NEEDS_MOTIVATION_EVIDENCE`: the pain, consequence, population, or why-now is not yet supported.
- `NEEDS_MOTIVATION_CLAIM_RESEARCH`: active motivation/problem hypotheses or unsupported claims
  have not yet completed the strengthening loop.
- `NEEDS_AUTHORITATIVE_SOURCE_MAPPING`: one or more active claim domains lacks a verified
  authority/remit/document-role row or a visible fallback route.
- `NEEDS_LANDSCAPE_RESEARCH`: closest work or the claimed gap remains uncertain.
- `NEEDS_AUTHOR_SOURCE_ACCESS`: a human-only CAPTCHA, authentication, subscription, or file-access
  barrier blocks a decision-relevant full-source check; the exact author action has been surfaced.
- `RECONSIDER_DIRECTION`: evidence suggests the selected problem, gap, or approach is not worth the
  expected investment.

Never mark the project ready merely because the outline or workboard is populated. Every required
Phase 1 area must be resolved, visibly blocked, or deliberately deferred with consequences and a
reopen trigger. A potentially decision-relevant source cannot be “deliberately deferred” instead
of acquired or surfaced as an exact author-access request. Readiness is a research judgment with an
explicit evidence boundary.
