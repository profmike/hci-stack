# Detailed Phase 1 research workflow

Read this reference completely before executing the Phase 1 workflow.

## Contents

[Phase contract](#phase-contract) ·
[Operating rules](#non-negotiable-operating-rules) ·
[Workspace](#3-create-the-project-research-workspace) ·
[Related work](#5-research-the-related-work-landscape) ·
[Publish](#13-publish-the-github-markdown-record) ·
[Completion states](#completion-states)

## Phase contract

Phase 1 of a looping HCI research workflow:

`problem screening → motivation and contributions → design/build → validation → visuals → writing → video`

Every phase is independently enterable; never require an Office Hours brief or other prior-phase
output, and import such a brief as a hypothesis, not an approved premise. Read
[pipeline-contract.md](pipeline-contract.md) when deciding what belongs in this phase, and
[exemplar-routing.md](exemplar-routing.md) before analyzing exemplars, which are not evidence for
this project's problem, gap, or effectiveness. Inspect later-phase materials to understand the
direction, but never grade missing later-phase artifacts as defects.

## Non-negotiable operating rules

### Collaborate actively before converging

Read [active-author-collaboration.md](active-author-collaboration.md) and
[author-collaboration.md](author-collaboration.md) before the first consequential question,
maintain `phase-1-collaboration-workboard.md`, and repeat:

`inspect → research → assess → challenge → compare → recommend → author decides → record → propagate → recheck`

A large idea dump, draft, populated template, or fluent synthesis is not a completed phase. Under the
standing **constructive opposition** rule, if necessary evidence is declined, record
`AUTHOR-DECLINED-EVIDENCE`, narrow or block the claim, and retain a reopen trigger.

### Keep the session interactive and orchestrate parallel research

Open a nontrivial evidence batch with a short author-facing update naming the research question, why
it can change the framing, the bounded parallel tasks, and the discussion it prepares; update again
when evidence moves the boundary, an access barrier appears, or a decision packet is ready.
Delegate bounded literature work to subagents by default when capacity allows—full-paper retrieval
and identity checks, methods/results/limitations audits, citation-chain and authoritative-source
searches, contradiction checks, closest-work comparisons, and claim-to-source impact tracing—each
with a named scope, expected evidence/locator output, and read-only or non-writer boundary. Treat a
subagent report as analysis, not as a replacement for the underlying source: reconcile it against the
opened full copy and preserve exact locators and contrary findings. With no subagent slot free,
continue locally rather than stopping.

### Ground research in complete sources

Read [citation-integrity.md](citation-integrity.md) before the first citation-bearing artifact and
keep `references.csv` keys stable across phases; read [evidence-protocol.md](evidence-protocol.md)
before motivation research or claim assessment and maintain `evidence-strength-register.md` as the
claim-specific audit cache it defines, down to the exact locator; and read
[claim-focused-writing.md](claim-focused-writing.md) before turning that record into discussion,
report narrative, or outline language.

Maintain `source-resolution.csv` as the machine-checkable acquisition queue. `UNASSESSED`,
`DISCOVERED`, `ACQUIRING`, and `FULL_TEXT_OBTAINED` are transient, not end-of-round dispositions.
Before a bounded audit or research round closes, every potentially decision-relevant source must
be:

- `FULL_TEXT_ASSESSED`, with full-copy, review, and evidence-register locators;
- `SCREENED_OUT` before retention or claim use, with a specific relevance reason;
- `SUPERSEDED`, pointing by source ID or citation key to a different retained `FULL_TEXT_ASSESSED`
  row with a stable citation key—never a missing, self, transient, or ambiguous replacement; or
- `NEEDS_AUTHOR_SOURCE_ACCESS`, after the exact request was surfaced in the conversation, with the
  non-future surfaced date, session/conversation/workboard locator, affected claim IDs (separate multiple affected claim IDs with `||`), fallback consequence, and reopen trigger.

At phase readiness every HTTP(S) citation key in `references.csv` must appear in the ledger (only
explicit `internal:` keys are exempt), every retained full-text row must resolve back to
`references.csv`, and every claim ID must resolve exactly in `claim-evidence-ledger.csv`. This
governs sources from search, supplied bibliographies, citation chains, full-paper references,
NotebookLM, and late-find audits.
Run `scripts/check_source_resolution.py PROJECT_DIR --end-of-round` before an end-of-round report
and `--phase-ready` before a readiness decision. “End of round” means a declared bounded-audit
closure or deliverable, not an in-progress update; transient rows never justify pausing, claiming
completion, or postponing an access request once lawful routes are exhausted.

It also governs files already in the repository or source store: at the start of a bounded audit and
again before closure, use `rg --files` to inventory the declared source/import roots, including
ignored or governed full-text and extraction directories, and resolve every file by bibliographic
identity to a `source-resolution.csv` row—readable, extracted, or prose-mentioned is not reconciled.
Record the roots, file count, accounted count, unresolved identities, timestamp, and the literal
marker `LOCAL_SOURCE_FILES_RECONCILED` in `source-manifest.md`. An unresolved candidate that could
change a claim, rank, comparator, or study requirement blocks closure.

### Escalate human-only source access

Do not merely log an inaccessible decision-relevant source and end with a progress report. After
trying lawful independent routes—DOI/publisher, open repositories, author or institutional copies,
supplements, and any university-library route already available to the author—record the work and
every failed route in `missing-full-copies.md`, continue non-dependent research, then surface the
smallest author action unblocking the highest-priority source.

An access-assistance request is not a framing-choice gate; ask it even when the author has said not
to judge, rank, or choose yet. State the exact citation, DOI/canonical URL, why the full paper could
change a claim, the obstacle and routes tried, the fallback evidence boundary, and one concrete
action—connect through their university IP or university VPN and retry in the same headed browser,
attach a lawfully obtained PDF, complete the CAPTCHA or institutional sign-in in their own headed
browser, or provide an authorized accessible link. Never
ask for passwords, cookies, session tokens, browser profiles, or copied authentication material; a
VPN connection is a connectivity state the author connects themselves, after which you retry without
inspecting or changing its configuration.

While a human-only barrier still blocks decision-relevant verification, use
`NEEDS_AUTHOR_SOURCE_ACCESS` and make the access request the next user-facing question; a
non-decision-relevant candidate may instead remain visibly excluded with its re-review trigger. When
the author supplies a paper manually, verify the file identity, open the full
methods/results/limitations and relevant supplements, update the source ledger, manifest,
`missing-full-copies.md`, and `evidence-strength-register.md`, and resume the blocked analysis.

### Create one NotebookLM notebook per project

Read [notebooklm-research.md](notebooklm-research.md) before setup or source ingestion, and create a
new notebook even when the researcher already has another project's notebook. If `notebooklm-mcp-cli`
is missing, explain the install and registration steps for Codex and Claude, obtain permission before
user-level installation, and never substitute ungrounded model memory. Create
`notebooklm-maintenance.md` from the asset and reconcile the human-facing source list after each
bounded research round, so broken, CAPTCHA, machine-only, unassessed, duplicate, or superseded
objects are not mixed with usable evidence. Ask the author to confirm the exact source-ID
set before irreversible deletion.

Treat the repository and NotebookLM as private, governed project stores. Copyright, license, and
redistribution status must not block or delay repository storage, version control, or NotebookLM
upload, and needs no per-source author confirmation; a missing copy is an unresolved technical
discrepancy, not a copyright disposition.

As soon as the workspace exists and the notebook is resolved, record its exact ID, user-facing title,
and profile name without credentials in both `source-manifest.md` and `agent-context.json`, and
update both in the same work round after any rename, replacement, or account-profile change, so that
Codex `$gpt-pro` and Claude Code `/gpt-pro` expose the correct notebook through the same read-only
CLI broker.

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
contribution. Scope `inferred-external` conclusions to the checked published or demonstrated system
and never turn them into technical impossibility or claims about unpublished variants. The research
outline must say what future work would establish each important project claim.

## Workflow

### 1. Inspect and establish the starting state

Inventory the supplied materials into `starting-state.md`: problem, target people, current practice,
claimed pain and why-now, known related work, approach and alternatives, existing results, candidate
contributions and terminology, constraints, access, ethics, safety, timeline, and available citations
and full copies. Mark imported prior-phase conclusions as hypotheses, and never make the author
re-answer facts in their own materials.

Keep `starting-state.md` and `phase-1-collaboration-workboard.md` in the session; create durable
copies only after Step 3 resolves the project repository. Lead the workboard with
`Current state — read this first`: direction/readiness, decisive evidence boundaries, settled
decisions, at most three consequence-ordered decision-ready questions with recommendations and
populated support artifacts, blockers, and next action/owner. Say when no author decision is ready,
and put coverage, history, and inventory after that snapshot. Use this starting-state table:

| Element | Current statement | Evidence/status | Confidence | Open question |
|---|---|---|---|---|

### 2. Interview for consequential unknowns

Apply the batching rule of
[active-author-collaboration.md](active-author-collaboration.md), asking one question at a time for
consequential choices, constructive-opposition gates, sensitive or access actions, and dependent
questions, with a short evidence-based interpretation first. Do **not** ask the author to rank
consequences or choose which one should motivate the
project; once target people and activity are bounded enough for meaningful searches, run the
consequence-severity research gate in Step 4. Prioritize questions whose answers change the research
direction: who experiences the problem during what activity and what they do now; what the team
directly observed and through what artifact or method; why the problem is newly important or newly
solvable; what the closest existing solution already does well; and what would make the direction not
worth pursuing, including access to the people, setting, expertise, and technology needed to test it.
Challenge inference quality, not the author's domain knowledge.

### 3. Create the project research workspace

Read [repository-boundaries.md](repository-boundaries.md) and resolve the project-specific repository
before writing durable artifacts; until it exists, keep work read-only and in-session, and request
the target when durable writing becomes necessary. Then run:

```bash
python3 "ABSOLUTE_SKILL_DIR/scripts/initialize_phase1_workspace.py" "ABSOLUTE_PROJECT_REPO" --project-name "PROJECT NAME"
```

The initializer creates every missing mandatory template, the source/full-text and working
directories, a root `README.md`, and the initial published and audited Markdown shelf without
overwriting existing artifacts; do not approximate it by copying only the files the current analysis
needs:

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
    ├── README.md
    ├── phase-1-progress.md
    ├── literature-and-evidence.md
    ├── phase-1-final.md
    ├── artifact-index.md
    └── [GitHub Markdown views of machine-readable ledgers]
```

The project root must also contain `README.md` with the Step 13 framing and onward links plus direct
relative links to author decisions and the four core `.md` reports; these navigation files are
workspace invariants from the first durable write onward. Record each full source's canonical
repository path, NotebookLM notebook ID, and source ID—never credentials or participant data.

Instantiate `agent-context.json` from the asset, replace its project-name placeholder, and keep it a
small pointer map whose every path is relative to the project repository:

- `phase.skill`: the exact `hci-motivation-and-contributions` skill name;
- `phase.status`: `active` or `paused` while Phase 1 is live, `complete` only after final
  reconciliation;
- `context.always_include`: workboard, author decisions, starting state;
- `context.include_when_relevant`: source manifest, NotebookLM maintenance record, Phase 2 handoff;
- `context.repo_read_allow`: only project material the author put in scope, defaulting to
  `research-framing/**` rather than the whole repository.

Never store conversation history, duplicated decision summaries, absolute machine paths, remotes
containing credentials, auth data, or participant data in the manifest. Refresh it after a material
path, phase-status, skill, notebook, or profile change and before each terminal handoff.

### 4. Build the motivation evidence chain

Research and map:

`larger human concern → target population/context → current practice → unmet need → consequence → why now → opportunity`

Before synthesizing the larger concern or normative baseline, read
[authoritative-domain-sources.md](authoritative-domain-sources.md) completely and build
`authoritative-source-map.md` from its asset template, one verified row per active domain. Reach
`AUTHORITATIVE_DOMAIN_SOURCES_MAPPED` only when every active domain has a verified row or a visible
missing/conditional-authority route, and do not ask for a motivation frame while the map is
incomplete.

Before synthesizing the chain, read [research-discovery-recall.md](research-discovery-recall.md) and
[motivation-claim-strengthening.md](motivation-claim-strengthening.md) completely, build
`motivation-claim-research-queue.md` from the asset template with one primary resolution route per
active `hypothesis` or `unsupported` claim-ledger row, and create `current-practice-audit.md`
whenever a claim concerns current products or documented controls. Work the queue recursively and
update the ledger with bounded replacement wording after each batch. Do not use adjacent external
work to “prove” the proposed system's own attenuation, mechanism, experience, adherence, or outcome;
route those to the smallest Phase 2 premise test or Phase 3 comparison.

Reach `MOTIVATION_CLAIM_AUDIT_COMPLETE` only when every such claim has a precise route, documented
research or official audit, explicit disposition, and either sufficient bounded support or the
smallest named project evidence action, and high-impact external routes also satisfy the recall
machinery of [research-discovery-recall.md](research-discovery-recall.md); a report that merely
repeats the labels does not pass. Maintain `evidence-strength-register.md` with the tags
[evidence-protocol.md](evidence-protocol.md) defines, and never promote a source because its sample
is large or NotebookLM rated it highly.

Before building motivation frames, read
[consequence-severity-research.md](consequence-severity-research.md) completely and build
`consequence-severity-ranking.md` from its asset template. Do not ask the author to rank, select, or
approve consequences while this gate is incomplete; only after `CONSEQUENCE_RANKING_COMPLETE` may the
motivation-frame gate ask the author to select or combine rhetorical frames, which never changes the
evidence ranking. Create three to five **motivation frames**—for example population consequence,
inequity, or a newly enabling technical capability—each with a full-text evidence chain, what it
foregrounds, what it risks obscuring, and what evidence would weaken it.

### 5. Research the related-work landscape

Read [acm-sigchi-related-work.md](acm-sigchi-related-work.md) and
[forward-citation-expansion.md](forward-citation-expansion.md) completely before searching, and build
`acm-sigchi-related-work-audit.md` and `related-work-search-recall-audit.md` from their asset
templates.

Run a required native ACM Digital Library pass under that protocol: CHI first, then the relevant
conferences on the current official SIGCHI roster, with an inclusion or specific exclusion decision
for every plausibly close CHI/SIGCHI work. Venue priority is coverage only; it never upgrades
ingestion completeness, directness, method validity, or claim-specific `ES1`–`ES3` strength, and
non-ACM work that is the strongest evidence for a claim is retained.

Before declaring the landscape saturated, freeze a **target-problem identity contract**—target
people, focal activity, triggering or temporal context, unwanted state or episode, intended change
or outcome—keeping the proposed design and any hypothesized causal mechanism outside it. Then run
those protocols' recall machinery: saturate the same/similar-problem branch before filling a ranked
set with distant work, build the high-leverage seed portfolio, and run the independent
cited-by routes until a complete zero-yield wave produces nothing new. If material work appears after
saturation was claimed, record it in `late-found-work-postmortem.csv`, repair the route, add a
sentinel to `novelty-regression-sentinels.yaml`, and rerun every conclusion it touches.

Search two required categories—the **same problem through different approaches** and a **different
problem through a similar approach**—and include same-problem/similar-approach work, often the
closest predecessor. Keep separate portfolios: the primary
problem-space ranking draws only from same-specific-problem and similar-problem work, while
different-problem/similar-approach work enters a mechanism/capability-collision portfolio only when
positive evidence shows the relevant operation ran. Classify that operation against the complete
human-activity predicate: it narrows the full capability only when the predicate or an independently
claimed sub-capability scope matches, while a shared component or loose subset of qualifiers
establishes inheritance only.

“Similar approach” means a genuinely similar **causal interaction approach**: the intervention acts on
people, activity, or coordination through substantially the same mechanism. A shared modality,
device, sensing technique, personalization label, multi-user topology, or output channel is not
enough—two systems delivering different audio to different people are not contribution comparators
when one manages concurrent conversations and the other guides linked physical actions—though such a
work is retained as a mechanism foundation.

### Run a component-foundation and falsification pass

Closest-comparator recall and mechanism foundations are separate gates. For every approach component
specific enough to affect feasibility, novelty, mechanism, or evaluation, map:

`component → operational change → proximal percept/behavior/mechanism → desired outcome → failure or side effect`

Search each link and its counterevidence in the vocabulary and databases of the discipline studying
it—grayscale, luminance, contrast, color temperature, blue-light filter, display
physiology, circadian, perception, and accessibility searches for visual/display attenuation;
latency, startup delay, rebuffering, throughput degradation, video quality of experience (QoE),
engagement, abandonment, and networking-systems searches for network attenuation—and run a
**product lineage**
pass for any inherited intervention or product across exact product names, authors, versions,
evaluation papers, later longitudinal studies, and current-practice provenance. Do not force these
works into the closest-HCI ranking: classify each as contribution comparator, design/mechanism
foundation, technical-feasibility source, motivation/physiology evidence, counterevidence, analogy
only, or screened out; a source can be essential to design rationale while remaining `ES1` for the
target outcome.

#### Supplied-bibliography accountability

Account for every bibliographic item in supplied reports, drafts, and reading lists in
`imported-bibliography-accountability.csv` with an include, full-text-acquire, or specific screen-out
disposition; imported references are discovery seeds, not author decisions. Any item that could
change an active mechanism, claim, rank, comparator, or study requirement must resolve to a terminal
`source-resolution.csv` row and its accounting rows.

For every retained seed, run a **claim-matched seed-upgrade pass**: search independently for a
competent authoritative body and current official document, a stronger design or larger dataset, a
more direct population/behavior/context/intervention/comparator/outcome, a corrected version, and
contradictory evidence, without collapsing these axes into venue prestige. Record queries,
comparison, and disposition—`retained-with-bounds`, `corroborated`, or `SUPERSEDED` by stable
key/locator. Author preference cannot stop this search or discard contrary evidence, and the supplied
bibliography never sets the evidence ceiling. Read each seed's exact full copy including its
references and run the multi-route forward-citation expansion protocol until a promotion wave yields
nothing new.

For the closest HCI works, atomize every material proposition and complete the six accounting fields
and decompositions defined in
[prior-work-contribution-boundaries.md](prior-work-contribution-boundaries.md) before any tier or
equivalence judgment, stating the literal operational difference first. A `DEMONSTRATED_UNCLAIMED`
operation cannot displace a closer problem comparator, and operated capability `NO` follows only from
positive artifact evidence. A task-performance score that yields a badge
is computed-state-to-reward, not user-action-to-command; a daily-use budget regulating quantity
across an accounting day is not a target-bedtime taper anchored to an intended transition; graduated
block **duration** is not graduated attenuation **intensity**; and intermittent access windows are
not a nonbinary intervened state. Reject a whole-system label unless positive evidence qualifies
every required channel.

Read [related-work-positioning.md](related-work-positioning.md) completely before classifying or
comparing retained work and apply every gate it defines, including the port gate. The audit covers
every catalogued reference in `prior-work-contribution-boundary.md` plus all five accounting
artifacts.

Before the gap or contribution decision gate, create `ranked-related-work-positioning.md` from the
asset template, rank up to approximately ten verified full works in the primary problem-space
portfolio by that template's problem-proximity criteria, and write its positioning paragraph for
each; if fewer than ten same/similar-problem works survive full-text review, include all and disclose
the shortage. Keep **mechanism/capability-collision** and
**concept/theory/foundation** portfolios separate from that ranking: a different-problem work is a
decisive claim-specific collision only when positive evidence shows the same complete
human-activity predicate or an independently claimed consequential sub-capability ran, while a
different-problem component or mechanism precedent is a `COMPONENT_OR_MECHANISM_PRECEDENT` crediting
what transfers without weakening the full capability. Neither is a closest overall problem
comparator, and evidence strength, venue, recency, and citation count stay separate from problem
proximity. Re-rank when the problem identity, mechanism, contribution layer, or closest-work corpus
changes, and state the broader HCI community position and its transfer boundary.

Step 5 remains incomplete until the ACM/SIGCHI audit is marked `ACM_SIGCHI_LANDSCAPE_AUDITED` **and**
the search-recall audit is marked `RELATED_WORK_SEARCH_RECALL_AUDITED`, with the accounting artifacts
valid under `scripts/check_prior_work_accounting.py`. If an exact full copy remains inaccessible,
follow **Escalate human-only source access** above and exclude it from claim support and chart
placement until verified; recording it in `missing-full-copies.md` does not count as asking the
author, and an `UNASSESSED` or acquire-only row cannot satisfy any gate.

### 6. Establish the terminology contract

Before contribution wording or chart labels converge, create `terminology-contract.md` and read
[terminology-contract.md](terminology-contract.md) completely, then present three to five terminology
systems with the fields the protocol requires. Never force one adjective to carry
several dimensions; a hierarchy may hold a concrete default term, a structural contrast term, a
narrowly scoped tailoring or control term, and reserved terms unavailable without stronger
evidence.

Ask the author to approve the semantic contract before choosing the paper-facing lexical spine: the
**terminology contract** fixes meanings and evidence boundaries, the **lexical spine** chooses which
approved terms do which rhetorical jobs. Record both separately, label every set `candidate` until
approval, and reopen them when the approach, system, study, or closest-work evidence changes.

### 7. Synthesize gaps and approach hypotheses

Compare current practice, products, and research on neutral dimensions from the full texts,
distinguishing:

- **capability gap:** people cannot do something important;
- **experience gap:** the capability exists, but outcomes or use remain poor;
- **cost/access gap:** comparable value exists but adoption costs exclude relevant users; and
- **knowledge gap:** a phenomenon, mechanism, or design tradeoff remains unknown.

Generate three to five gap interpretations, each with the closest work, exact distinction, why-now,
workflow boundary, risk of incrementalism, and falsifying evidence.

Then generate three to five approach hypotheses, each stating the human situation and desired value
with its evidence state, the capability and only the implementation needed to understand it, what is
inherited from prior work, the hypothesized advantage, likely costs, failure modes, the line between
planned implementation and established capability, and the smallest Phase 2 investigation that would
test the premise. Do not optimize an approach before confirming that it addresses the selected
problem.

Derive each approach's fair **future evaluation logic** from the claimed workflow change: for an
additive layer the informative comparison is the intact current workflow versus that workflow plus
the proposed layer, never a baseline that removes valued current practice. Record this as a Phase 3
evidence requirement, not an approved study design.

After every consequential decision, update the workboard and `author-decisions.md`, retain the option
packet in `decision-packets/`, propagate the choice, and regenerate the progress report; never
replace rejected alternatives with only the winning choice.

### 8. Explore positioning views

Read [related-work-quadrant.md](related-work-quadrant.md), then build the axis-pair variations it
specifies from the same core corpus. The chart is a communication artifact, not proof of novelty; every
research point needs a checked full copy and a concise rationale, and axis endpoints stay neutral
and operational—never “traditional → novel,” “bad → good,” venue prestige, or paper quality. Show
what each view reveals and compresses, then recommend one and let the author select.

### 9. Sharpen prospective contributions

Identify atomic reusable outputs, frame their human and HCI value, classify each using the
seven knowledge-oriented types , and align each type with its own evidence gate. Read
[hci-contribution-types.md](hci-contribution-types.md), [terminology-contract.md](terminology-contract.md),
and [contribution-rubric.md](contribution-rubric.md) first, and keep one stable-ID
contribution-candidate register across the workboard, decision packet, outline, reports, and handoff.
Never ask the author to select a package while any candidate lacks a reusable output, primary type,
classification rationale, closest-output delta, or type-specific evidence path; if the terminology
gate is pending, show packages as candidates.

Generate three to five coherent contribution packages, not synonym lists, filling every field of the
`contribution-options.md` asset template. Each package must additionally state:
a plain-language, benefit-first lead moving from human situation and desired value to capability and
necessary mechanism; the existing workflow, the precise stage being replaced, complemented, extended,
or bridged, and the current-practice collision check result;
the platform-independent approach invariant and its essential interaction/control-policy dimensions; and what remains explicitly
unclaimed alongside the fair future comparator that preserves valued current practice.

Use contribution language prospectively until evidence exists. Build every package
against the six-field prior-work accounting of Step 5, applying the same fields to the focal project:
a `DEMONSTRATED_UNCLAIMED` operation can narrow firstness only at the matched complete-predicate or
independently claimed sub-capability scope and receives no contribution credit, a component precedent
shows inheritance without narrowing the complete capability, and a `CLAIMED_UNDEMONSTRATED` atom
receives neither.

Separate these layers, then rank them—do not impose a universal order:

- **workflow relationship or significance:** how the work changes an existing human process;
- **interaction or information-distribution capability:** how people act, address recipients, receive
  content, or coordinate differently;
- **setting or activity boundary:** which participants, interdependencies, objects, movements, risks,
  or constraints are present;
- **implementation/design rationale:** why a device, modality, interface, or form factor may realize
  the interaction; and
- **outcome hypothesis:** what might improve and therefore requires comparative evidence.

Choose the primary contribution as the strongest defensible consequential difference relative to the
closest comparator, not whichever layer appears first: a workflow relationship may explain
significance while an interaction or information-distribution capability carries the originality.
Record the primary layer, the ranking rationale, and the strongest fallback. Never promote a
lower-level implementation choice because it is visually distinctive or technically difficult; where
the hardware or medium is contribution-bearing, support the human capability, outcome, or access
change it enables. Treat an OS, device, framework, sensor, or medium as the empirical waist unless
matched evidence shows reusable adaptation knowledge, a new use class, or a direct empirical
finding.

### 10. Run a phase-aware constructive review

Use the seven lenses in [reviewer-panel.md](reviewer-panel.md) over the workboard, research outline,
evidence maps, landscape, approach options, contribution packages, and decisions. Reviewers must
not demand polished paper prose, treat not-yet-expected implementation or results as defects,
optimize details before challenging the premise, or imply the panel predicts acceptance.
Synthesize concerns into framing revisions, evidence needs, Phase 2/3 questions, or risks, and
return material choices to the author.

### 11. Produce the research framing outline

Write the `Reader-facing Introduction spine` first as a conclusion-level outline:

1. concrete behavior and consequence;
2. why the focal context differs from the general intervention target;
3. prior user-enacted and technical approaches plus measured limits;
4. outcome-oriented approach and mechanisms;
5. the newly enabled investigation, controls, and observable outcomes; and
6. an evidence-state-matched study and contribution statement.

Open with findings rather than an abstract importance label, apply the citation-placement and
qualifier rules of [claim-focused-writing.md](claim-focused-writing.md), and use `We conducted` only
after the study is complete.

Then fill every section of the `research-framing-outline.md` asset template, keeping capability
collision separated from contribution attribution and the approach invariant before the
implementation substrate. Use bullets, evidence tables, and candidate language, not polished
Introduction prose.

### 12. Create the Phase 2 handoff

Instantiate `phase-2-handoff.md` from the asset template and fill every section it defines. Carry
forward, beyond the template's prompts: port gates and source-silence queries; the
component-foundation/falsification findings and product lineage constraining related-work or
contribution claims; author-provided seed dispositions; every unresolved source with its blocked
claim, access request, and reopen trigger; rejected alternatives and terms to avoid; and UX/system
requirements marked as hypotheses.

Downstream work may cite or compare only opened full copies or clearly marked project evidence, and
must not omit an unresolved source from the handoff, strengthen its affected claim, or conceal
counterevidence. This handoff is optional input to Phase 2.

Reconcile `agent-context.json` against the final workboard, author decisions, source manifest,
NotebookLM record, and handoff, and set `phase.status` to `complete` only after that reconciliation.
The auditor must fail when
`phase.status` is `complete` while the motivation-claim, ACM/SIGCHI, or search-recall file retains an open status,
unchecked gate, or template placeholder.

### 13. Publish the GitHub Markdown record

Read [markdown-reports.md](markdown-reports.md) and
[iso-24495-1-plain-language.md](iso-24495-1-plain-language.md), then run:

```bash
python3 "ABSOLUTE_SKILL_DIR/scripts/render_source_manifest.py" "ABSOLUTE_PROJECT_REPO/research-framing"
python3 "ABSOLUTE_SKILL_DIR/scripts/check_prior_work_accounting.py" "ABSOLUTE_PROJECT_REPO/research-framing" --end-of-round
python3 "ABSOLUTE_SKILL_DIR/scripts/check_source_resolution.py" "ABSOLUTE_PROJECT_REPO/research-framing" --end-of-round
python3 "ABSOLUTE_SKILL_DIR/scripts/render_phase1_reports.py" "ABSOLUTE_PROJECT_REPO/research-framing"
python3 "ABSOLUTE_SKILL_DIR/scripts/audit_phase1_reports.py" "ABSOLUTE_PROJECT_REPO/research-framing"
```

Regenerate `phase-1-progress.md` after each material evidence batch, option portfolio, author
decision, or review; regenerate `literature-and-evidence.md` after each search pass; and regenerate
the three core reports, `artifact-index.md`, report-shelf README, and required ledger views before a
completion decision. Canonical Markdown/CSV/JSON/YAML records remain the
editable sources of truth; generated views carry navigation, hashes, and previews—not independent
claims. The root README is a bounded overview that never erases unresolved
evidence, access blocks, rejected variants, or reopen triggers.

`phase-1-progress.md` must lead with the decision-first current state, linking to the populated
workboard, author decisions, active access record, and supporting decision packet. Apply the
claim-local caveat test to narrative summaries: state supported claims directly, omit disclaimers
about outcomes not claimed, and introduce familiar terms before defining their exact scientific or
technical meaning at first use.

An end-of-round report may show `NEEDS_AUTHOR_SOURCE_ACCESS` only when the exact request, direct
URL, failed routes, and author action have already been surfaced, and may not call the source audit
complete while retaining `UNASSESSED`, `DISCOVERED`, `ACQUIRING`, or `FULL_TEXT_OBTAINED`. Before
`READY_FOR_PHASE_2` or `READY_WITH_RISKS`, rerun the source-resolution and prior-work checkers with
`--phase-ready`; the latter must verify the thirteen checked completion markers in
`prior-work-contribution-boundary.md`, and prose does not substitute for valid ledgers, terminal
imported-source rows, completed late-find repairs, passing sentinels, and a complete zero-yield
promotion wave.

Every Markdown file under `research-framing/` must link back to the project README, artifact index,
live workboard, and Phase 2 handoff, and no generated `.html` file may remain. Before every commit,
push, or terminal handoff containing material Phase 1 changes, republish, rerun the auditor, and
preview the set on GitHub or a local GitHub-Flavored Markdown renderer, verifying that links, source
hashes, citation definitions, and canonical paths match the staged tree; fix canonical content when
the record is wrong and the publisher when the defect could recur. A durable batch is not publishable
when navigation is broken, a generated view is stale, or prospective claims are presented as
completed results.

## Completion states

- `READY_FOR_PHASE_2`: framing is evidence-grounded; key uncertainties have bounded Phase 2 work.
- `READY_WITH_RISKS`: direction is promising, but named evidence or feasibility risks remain.
- `NEEDS_MOTIVATION_EVIDENCE`: the pain, consequence, population, or why-now is not yet supported.
- `NEEDS_MOTIVATION_CLAIM_RESEARCH`: active hypotheses or unsupported claims have not completed the
  strengthening loop.
- `NEEDS_AUTHORITATIVE_SOURCE_MAPPING`: an active claim domain lacks a verified
  authority/remit/document-role row or a visible fallback route.
- `NEEDS_LANDSCAPE_RESEARCH`: closest work or the claimed gap remains uncertain.
- `NEEDS_AUTHOR_SOURCE_ACCESS`: a human-only CAPTCHA, authentication, subscription, or file-access
  barrier blocks a decision-relevant full-source check; the exact author action has been surfaced.
- `RECONSIDER_DIRECTION`: evidence suggests the problem, gap, or approach is not worth the
  expected investment.

Never mark the project ready merely because the outline or workboard is populated: every required
Phase 1 area must be resolved, visibly blocked, or deferred with consequences and a reopen trigger,
and a decision-relevant source cannot be deferred instead of acquired or surfaced as an exact
author-access request.
