# Author collaboration and decision gates

Apply [active-author-collaboration.md](active-author-collaboration.md) throughout this phase; it
carries the general collaboration contract, the interactive loop, the workboard field and lifecycle
schema, and the constructive-opposition packet. This file adds the Phase 1 specifics. Run
non-dependent research independently, but take central research choices to the author once the
relevant evidence is assessed.

## Live Phase 1 coverage and workboard

Maintain `phase-1-collaboration-workboard.md` from the asset template, keeping it session-only
until the target project repository is known. Open it and every
author-facing status message with `Current state — read this first`: direction/readiness state, the
established-versus-observed-versus-planned boundary, settled decisions, active blockers, and the
immediate next action, ahead of any history or inventory. Then show at most three decision-ready
questions ordered by consequence, each with the recommendation, the actual alternatives and
tradeoff, the consequence of delay, and direct links to the populated decision-support artifacts.
Say `No author decision is currently ready` when research must come first. A source count, activity
log, file list, or populated matrix is not a current-state summary.

Each round, refresh that snapshot, take the highest-consequence Phase 1 uncertainty that can
currently move, research enough to make the next decision meaningful, and state constructive
opposition before presenting options.

Cover every phase area listed in the template's Phase coverage table, from the starting state and
imported assumptions through the Phase 2 handoff. Document presence is not resolution: a row closes
only when its evidence boundary, author decision where required, contrary findings, propagation
targets, and reopen trigger are explicit.

## Interactive parallel-research protocol

Keep the author-facing conversation live while evidence work proceeds: open each nontrivial batch
with the question it serves, and update again when a source changes the boundary, a human-only
access action is needed, or the packet becomes decision-ready. A set of updated files is not a
substitute for this interaction.

Use available subagents by default for bounded literature retrieval and analysis unless author help
is explicitly required; the lead agent still owns every durable edit, source-resolution state,
evidence-strength judgment, and author question, and reconciles subagent findings against the
underlying full copies before propagating anything. Without subagents, do the same work locally at
the same cadence. Do not delegate routine literature search or analysis back to the author.

## Fast factual clarification batches

Do not turn reconstruction of one known design, state machine, artifact set, resource envelope, or
workflow into a slow sequence of single-fact turns: batch those clarifications under the general
batching rule. If a clarification exposes an evidence or literature gap, run or delegate that
research and pause only at the resulting material decision or access barrier.

## Decisions that cannot be silently finalized and their gate sequence

These are author decisions, never silent agent commitments: the problem and impact aperture; the gap
interpretation; the approach and its main enabling insight; the primary prospective contribution and
empirical scope; the terminology contract and loaded technical terms; the paper-facing lexical
spine; the paper-facing related-work axes; and any material change in target people, contribution
type, claimed capability, or feasibility. An author may explicitly delegate a choice; still present
the alternatives and explain the selected option before propagating it.

Before the first author decision gate, complete the motivation-claim strengthening loop in
`motivation-claim-research-queue.md` and the evidence/severity ranking in
`consequence-severity-ranking.md`. These are research gates, not author preference gates: the author
may correct factual scope or contribute direct observations, but do not ask them to rank or choose
consequences or unsupported motivation claims until the synthesis is complete.

Normally gate in that order — motivation frame, gap, approach hypothesis, provisional terminology
contract, contribution package, lexical hierarchy, quadrant view, final research-direction and
readiness package — recording the terminology contract and the lexical hierarchy as separate
decisions. Evidence may require another order; earlier choices constrain later ones; reopen a choice
when new findings invalidate it.

At a gate, pause dependent synthesis after presenting alternatives and continue only non-dependent
acquisition or verification until the author chooses, combines, rejects, or delegates. Silence, a
rough draft, and the agent's recommendation are not approval.

## Access assistance is not a choice gate

Ask the author for factual access help whenever a decision-relevant exact source remains blocked
after lawful independent acquisition routes are exhausted, even before the consequence ranking or
another decision portfolio is complete, and even when the author has said not to ask them to rank,
judge, or choose yet.

Do not stop at writing `missing-full-copies.md`. Continue every useful non-dependent task, then put a
specific access request in the conversation for the source most likely to change the current
consequence rank, evidence strength, closest-work comparison, or framing boundary, naming the exact
paper and DOI/canonical URL; why its full methods/results could change the analysis; every route
tried and the precise failure, such as CAPTCHA, institutional sign-in, paywall, failed import, or
incomplete rendering; the smallest safe author action—connect through their university IP or
university VPN and retry in the same headed browser, attach a lawfully obtained PDF, complete the
challenge or sign-in in their own headed browser and report that it is ready, or provide an
authorized accessible link; and what claim remains excluded or downgraded if the source stays
unavailable.

Ask for one concrete access action at a time unless several sources can be resolved by the same
single action. Never request or record a password, cookie, browser profile, session token, or copied
authentication material. A CAPTCHA must be completed by the author; do not attempt to bypass it.
Suggest university IP/library access or a university VPN before asking the author to purchase a
paper. The author connects the VPN themselves; do not inspect, configure, or request its
credentials.

If the source is still unresolved after all non-dependent work is complete, use
`NEEDS_AUTHOR_SOURCE_ACCESS` and end on the concrete access request, not a generic progress summary.
This state does not authorize the agent to make the blocked research choice. Free-form `pending` or
`no` text does not prove the request was surfaced: record the actual non-future `YYYY-MM-DD` date, a
stable session/conversation/workboard locator, affected claim IDs, the fallback or narrowing in
force, and the reopening evidence event, and carry these exact fields into the Phase 2 handoff.

Before declaring a bounded source audit or research round complete, sweep the source manifest,
supplied bibliographies, candidate inventories, citation-chain log, related-work audits, evidence
register, and `source-resolution.csv`: `UNASSESSED`, `DISCOVERED`, `ACQUIRING`, and
`FULL_TEXT_OBTAINED` mean acquisition or review work remains, so do it now and surface any remaining
human-only manual-download, university-VPN/library, institutional-sign-in, or CAPTCHA action before
ending the round.
Never call a bounded audit or research round complete while leaving “obtain the papers” as the next
action. An in-progress update may show transient acquisition state, but must not become a terminal
progress report or shift the timing of the access request.

When the author reports a completed download, local path, attached PDF, or ready authenticated page,
resume without asking them to repeat the request: verify the exact identity, audit the full source,
update the source-resolution, missing-copy, manifest, and evidence records, then propagate any
changed claim, ranking, or positioning.

Treat every author-found or author-provided reference as a discovery seed, not an author decision
and not the evidence ceiling. After full-text review, independently search for claim-matched sources
with stronger authority, method, synthesis, directness, currency, publication review, or
contradictory findings, without asking whether to perform that upgrade search. Author preference may
preserve a source for history, framing, or a uniquely direct observation, but cannot upgrade its
evidence strength or suppress stronger contrary evidence.

## Present three to five substantive alternatives

Fill the option table in `decision-packet.md` — name, exact candidate framing/approach/contribution
package/terminology set/axis pair, checked full-text evidence, emphasis, tradeoff, status
(`established` / `observed` / `planned` / `hypothesis` / `aspiration` / `unsupported`), and the
recommendation with what would change it.

Superficial synonym lists do not satisfy this rule. When fewer than three defensible options exist,
show only those and explain why more would be artificial. Ask one decision question at a time, and
invite the author to choose, combine named parts, reject the portfolio, or delegate.

## Apply constructive opposition to consequential gaps

The standing rule also covers the Phase 1 problem and gap: author preference cannot become evidence,
erase contrary findings, upgrade an evidence-strength rating, or waive a critical problem, gap,
validity, feasibility, safety, ethics, privacy, accessibility, or governance gap.

Put the constructive-opposition packet in the workboard before asking the author to choose. In
Phase 1 its mismatch field names the
precise population, activity, construct, method, mechanism, currency, or causal mismatch, and its
consequence field names what could fail in the motivation, novelty boundary, approach premise,
contribution, or later study. Its defensible paths take Phase 1 forms: a stronger authority,
synthesis, contradiction, or closest full paper; verification of an author artifact; a
decision-matched study or probe routed to the later phase that should own it; a
better-supported framing or approach; a narrowed claim; or removal or visible blocking of the
claim. Do not manufacture participant research when literature already resolves the decision, and do
not launch research, upload private data, choose a material study design, or implement a prototype
without authority.

On `AUTHOR-DECLINED-EVIDENCE`, propagate the consequence to the research outline and Phase 2 handoff
as well as the workboard. State the opposition once clearly and continue within the defensible
paths; do not badger the author over low-consequence, reversible taste.

## Separate review cautions from reader-facing prose

Read [claim-focused-writing.md](claim-focused-writing.md) before turning an evidence assessment into
report narrative, candidate language, or downstream writing guidance, and apply its claim-local
caveat test here. Show the author the complete internal boundary — material uncertainty,
counterevidence, non-claims, reopen triggers — then decide separately whether each item is a
reader-facing qualifier. The separation never upgrades evidence or conceals a contradiction.

## Establish the terminology contract, then build a lexical spine

Read [terminology-contract.md](terminology-contract.md) completely; it carries the decomposition
dimensions, the per-system field requirements, and the propagation rules. Decompose central claims
first, then propose three to five coherent terminology systems, preferring words used by
participants and domain practitioners when the artifacts support them, and never forcing one word to
carry several dimensions.

Prefer concrete phrases over compressed jargon. Do not call manually assigned cues
“personalization,” unmeasured low-latency behavior “real-time,” or a researcher-controlled
prototype “expert-operated” unless the planned evidence and actual design support those terms.
Distinguish recipient scope from selection provenance: `recipient-differentiated` means intended
recipients can receive different content; `role- or profile-configured` means a person selects it
from declared attributes; `system-personalized` requires a stored or inferred individual model;
and `adaptive` requires support to change with inferred state, behavior, or performance. A term for
one configurable dimension does not make the whole system personalized, and “private” requires
verified access and routing.

For a general audience, apply the familiar-to-precise rule: lead with the familiar term and define
the exact source-matched construct at first use. Paper-facing approach and contribution descriptions
lead with the human situation and the value people need before capability and implementation, and
keep that value at its evidence state — a rationale or hypothesis does not become a measured benefit
because it makes the explanation more compelling.

Ask the author to approve the semantic contract before selecting the lexical spine. Until then, keep
every terminology system and dependent contribution phrase `candidate`.

## Record and propagate decisions

Maintain `author-decisions.md`:

```markdown
| Date | Checkpoint | Options shown | Decision | Rationale | Evidence/status | Files to update |
```

After a choice, restate the selected wording and scope, record rejected implications and unresolved
evidence, propagate through the evidence maps, related-work matrix, approach, contribution package,
charts, research outline, handoff, and planned later paper sections, and label superseded and
reopened choices rather than erasing them. Undecided choices remain `candidate`; Phase 2 or Phase 3
evidence can reopen any Phase 1 decision.
