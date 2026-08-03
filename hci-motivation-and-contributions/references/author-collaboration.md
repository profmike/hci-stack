# Author collaboration and decision gates

Apply [active-author-collaboration.md](active-author-collaboration.md) throughout this phase. The
skill is an active research collaborator and constructive critic, not an autonomous framing
generator or a documentation service. It may continue source acquisition, contradiction checks,
and other non-dependent research independently, but central research choices require visible
author input after the relevant evidence has been assessed.

## Live Phase 1 coverage and workboard

Create and maintain `phase-1-collaboration-workboard.md` from the asset template. If the target
project repository is unknown, keep this state only in the current session or conversation; never
write it into the reusable skill repository or an arbitrary workspace.

Open the workboard and every author-facing status message with `Current state — read this first`.
Give the direction/readiness state, established-versus-observed-versus-planned boundary, settled
decisions, active blockers, and immediate next action before history or coverage inventories. Show
at most three decision-ready questions, ordered by consequence; for each, give the recommendation,
actual alternatives/tradeoff, consequence of delay, and direct links to the populated comparison
or decision-support artifacts. Say `No author decision is currently ready` when research must come
first. A source count, activity log, file list, or populated matrix is not a current-state summary.

At the start of each working round:

1. refresh the decision-first current-state snapshot;
2. show what is resolved, researching, reopened, evidence-blocked, or deliberately deferred;
3. identify the highest-consequence Phase 1 uncertainty that can currently move;
4. inspect and research enough to make the next decision meaningful;
5. state any constructive opposition before presenting options;
6. batch related low-risk factual clarifications when no research is needed, but ask only one
   consequential author question when a decision row is ready; and
7. after the answer, record and propagate the decision before advancing.

The coverage board must include the starting-state/import boundary, people/activity/problem scope,
authoritative and motivation evidence, consequence severity, current practice, related-work
coverage and ranked positioning, terminology and lexical spine, gap, approach hypotheses,
positioning views, contribution packages, constructive review, and Phase 2 handoff.

## Interactive parallel-research protocol

Keep the author-facing conversation live while evidence work proceeds. Start each nontrivial batch
with a short update naming the question, its decision consequence, the parallel tasks, and the
discussion those tasks are preparing. Update again when a source changes the boundary, a
human-only access action is needed, or the packet becomes decision-ready. A set of updated files
is not a substitute for this interaction.

Use available subagents by default for bounded literature retrieval and analysis unless author
help is explicitly required. Prefer independent task packets such as:

- acquire and verify complete copies of named works;
- audit methods, results, uncertainty, limitations, and exact locators;
- trace citations and search stronger authoritative or contradictory sources;
- compare the closest related systems on a defined interaction dimension; and
- map a new source to named claims and identify what changes or remains unsupported.

Give every subagent an exact scope, required source/locator output, and a read-only or non-writer
boundary. Keep one lead agent responsible for all durable edits, source-resolution states,
evidence-strength judgments, workboard updates, synthesis, and author questions. Reconcile
overlaps, disagreements, and the underlying full copies before propagating any finding.

Ask the author to act only for lawful library/publisher access, CAPTCHA or institutional
authentication in their own browser, a missing project artifact, tacit project facts, values,
constraints, resources, or consequential choices that cannot be recovered independently. Do not
delegate routine literature search or analysis back to the author. When subagents are unavailable,
continue the same work locally and preserve the interactive update cadence.

Do not confuse document presence with resolution. A Phase 1 row closes only when the current
evidence boundary, author decision where required, contrary findings, propagation targets, and
reopen trigger are explicit.

## Fast factual clarification batches

Do not turn reconstruction of one known design, state machine, artifact set, resource envelope, or
workflow into a slow sequence of single-fact turns. Ask two to six tightly related factual
questions together when the author can answer from direct project knowledge, no evidence search is
needed, the questions are low-risk, and an earlier answer will not invalidate later questions.
Number the questions, invite concise labeled answers, then record and propagate the batch once.

Keep sequential one-question pauses for consequential framing choices, constructive opposition,
source-access or sensitive actions, and dependent questions that require interpreting an earlier
answer. If a clarification exposes a significant evidence or literature gap, continue or delegate
that research and pause only at the resulting material decision or access barrier.

## Decisions that cannot be silently finalized

- the larger problem and impact aperture;
- the interpretation of the research gap;
- the proposed approach and its main enabling insight;
- the primary prospective contribution and empirical scope;
- the terminology contract and loaded technical terms;
- the paper-facing lexical spine;
- the paper-facing related-work axes; and
- any material change in target people, contribution type, claimed capability, or feasibility.

An author may explicitly delegate a choice. Still present the alternatives and explain the selected
option before propagating it.

## Gate sequence

Before the first author decision gate, complete the motivation-claim strengthening loop in
`motivation-claim-research-queue.md` and the evidence/severity ranking in
`consequence-severity-ranking.md`. These are research gates, not author preference gates. The
author may correct factual scope or contribute direct observations, but do not ask them to rank or
choose consequences or unsupported motivation claims until the synthesis is complete.

Normally work through:

1. motivation frame;
2. gap interpretation;
3. approach hypothesis;
4. provisional terminology contract;
5. prospective contribution package;
6. paper-facing lexical hierarchy;
7. quadrant view; and
8. final research-direction and readiness package.

Evidence may require a different order. Earlier choices constrain later ones; reopen a choice when
new findings invalidate it. The terminology contract fixes operational meanings and evidence
boundaries; the lexical hierarchy decides which approved terms should be the concrete default,
structural contrast, accessible umbrella, and scoped tailoring or control term. Record them as
separate decisions.

At a gate, pause dependent synthesis after presenting alternatives. Continue only source
acquisition, verification, or another non-dependent task until the author chooses, combines,
rejects, or delegates. Silence, a rough draft, and the agent's recommendation are not approval.

## Access assistance is not a choice gate

Ask the author for factual access help whenever a decision-relevant exact source remains blocked
after lawful independent acquisition routes are exhausted. This request is allowed before the
consequence ranking or another decision portfolio is complete, including when the author has said
not to ask them to rank, judge, or choose yet.

Do not stop at writing `missing-full-copies.md`. Continue every useful non-dependent task, then put a
specific access request in the conversation. Prioritize the source most likely to change the
current consequence rank, evidence strength, closest-work comparison, or framing boundary. Name:

1. the exact paper and DOI/canonical URL;
2. why its full methods/results could change the current analysis;
3. every route tried and the precise failure, such as CAPTCHA, institutional sign-in, paywall,
   failed import, or incomplete rendering;
4. the smallest safe author action—connect through their university IP or university VPN and retry
   in the same headed browser, attach a lawfully obtained PDF, complete the challenge or sign-in in
   their own headed browser and report that it is ready, or provide an authorized accessible link;
   and
5. what claim remains excluded or downgraded if the source stays unavailable.

Ask for one concrete access action at a time unless several sources can be resolved by the same
single action. Never request or record a password, cookie, browser profile, session token, or copied
authentication material. A CAPTCHA must be completed by the author; do not attempt to bypass it.
Suggest university IP/library access or a university VPN before asking the author to purchase a
paper. The author connects the VPN themselves; do not inspect, configure, or request its
credentials.

If the source remains unresolved after all non-dependent work is complete, use
`NEEDS_AUTHOR_SOURCE_ACCESS`. End on the concrete access request rather than a generic progress
summary. This state does not authorize the agent to make the blocked research choice.

Free-form `pending` or `no` text does not prove that the request was surfaced. Record the actual
non-future `YYYY-MM-DD` date, a stable session/conversation/workboard locator, affected claim IDs,
the fallback or narrowing that remains in force, and the evidence event that reopens the claim.
Carry these exact fields into the Phase 2 handoff.

Before declaring a bounded source audit or research round complete, sweep the source manifest,
supplied bibliographies, candidate inventories, citation-chain log, related-work audits, evidence register, and
`source-resolution.csv`. `UNASSESSED`, `DISCOVERED`, `ACQUIRING`, and `FULL_TEXT_OBTAINED` mean
there is still acquisition or review work to do. Do that work now; if a human-only barrier remains,
surface the exact manual-download, university-VPN/library, institutional-sign-in, or CAPTCHA action
before ending the round. Never call a bounded audit or research round complete while leaving
“obtain the papers” as the next action.

An ordinary in-progress status update is not a closure gate. It may expose transient acquisition
state while work continues, but must not become a terminal progress report, manufacture an early
human-access request before lawful routes are tried, or delay the request once those routes are
exhausted.

When the author says a download is complete, names a local path, attaches a PDF, or says an
authenticated page is ready, resume without asking them to repeat the research request. Verify the
exact identity, open and audit the full source, update the source-resolution, missing-copy,
manifest, and evidence records, and then propagate any changed claim, ranking, or positioning.

Treat every author-found or author-provided reference as a useful discovery seed, not an author
decision and not the evidence ceiling. After full-text review, independently search for
claim-matched sources with stronger authority, method, synthesis, directness, currency, publication
review, or contradictory findings. Show the author the precise evidence-role mismatch when it
matters, but do not ask whether to perform the upgrade search. Author preference may preserve a
source for history, framing, or a uniquely direct observation; it cannot upgrade its evidence
strength, suppress stronger contrary evidence, or waive a decision-critical gap.

## Present three to five substantive alternatives

Every option includes:

| Field | Required content |
|---|---|
| Name | Short memorable option label |
| Candidate | Exact framing, approach, contribution package, terminology set, or axis pair |
| Evidence | Checked full-text sources and project artifacts |
| Emphasis | What becomes central |
| Tradeoff | What is compressed, excluded, or riskily implied |
| Evidence status | established / observed / planned / hypothesis / aspiration / unsupported |
| Recommendation | Preferred option and what would change the recommendation |

Do not satisfy this rule with superficial synonym lists. When fewer than three defensible options
exist, show only the defensible options and explain why additional ones would be artificial.

Ask one decision question at a time. Invite the author to choose, combine named parts, reject the
portfolio, or delegate the decision.

## Apply constructive opposition to consequential gaps

Author preference can select emphasis and priorities among defensible paths. It cannot become
evidence, erase contrary findings, upgrade an evidence-strength rating, or waive a critical
problem, gap, validity, feasibility, safety, ethics, privacy, accessibility, or governance gap.

When support is insufficient for the decision's consequence, put this challenge in the workboard
before asking the author to choose:

1. the exact claim, framing move, or proposed commitment;
2. the strongest current evidence and its claim-specific strength/applicability boundary;
3. the precise population, activity, construct, method, mechanism, currency, or causal mismatch;
4. what could fail in the motivation, novelty boundary, approach premise, contribution, or later
   study if the assumption is wrong;
5. the least burdensome defensible recommendation; and
6. one question requesting a missing fact or a choice among defensible paths.

Offer paths proportionally:

1. find a stronger authority, synthesis, contradiction, or closest full paper;
2. verify an existing author artifact or analysis;
3. route a decision-matched observation, interview, study, design/technical probe, or analysis to
   the appropriate later phase when the residual gap genuinely requires original evidence;
4. select a better-supported framing or approach;
5. narrow the claim to what current evidence supports; or
6. remove or visibly block the claim.

For each path, state what it could and could not establish, author effort/access, and which options
it strengthens. Do not manufacture participant research when literature already resolves the
decision, and do not launch research, upload private data, choose a material study design, or
implement a prototype without authority.

If the author declines necessary evidence, record `AUTHOR-DECLINED-EVIDENCE`, preserve the claim
as `hypothesis`, `aspiration`, or `unsupported`, narrow or block the affected framing/readiness,
propagate the consequence to the outline and Phase 2 handoff, and state the evidence that would
reopen it. State the opposition once clearly and continue within the defensible paths; do not
badger the author over low-consequence, reversible taste.

## Separate review cautions from reader-facing prose

Read [claim-focused-writing.md](claim-focused-writing.md) before turning an evidence assessment
into report narrative, candidate language, or downstream writing guidance. Show the author the
complete internal boundary, including material uncertainty, counterevidence, non-claims, and reopen
triggers. Then decide separately whether each item is a reader-facing qualifier.

A qualifier belongs in the prose only when it changes the truth, scope, quantity, causal meaning,
comparison, or likely interpretation of a claim actually made. Otherwise keep it in the workboard,
evidence register, reviewer discussion, and handoff rather than appending a defensive disclaimer.
For example, if checked night-mode studies support only a general reduction in blue-light output,
cite that result directly. Keep inconsistent whole-night sleep findings in the internal review
record unless the paper makes a sleep-outcome claim.

Do not let this separation upgrade evidence or conceal a direct contradiction. Record the internal
boundary, `required` or `not required` reader-facing qualifier status, claim-local rationale, and
reopen trigger before propagation.

## Establish the terminology contract, then build a lexical spine

Read [terminology-contract.md](terminology-contract.md) completely. First decompose central claims
by addressee, same/different content, selection provenance, tailoring basis, user control,
adaptation, timing, access, and outcome. Then propose three to five coherent terminology systems
with plain-language definitions and implication risks. Prefer words used by participants and
domain practitioners when the artifacts support them.

For every central term, test whether it:

- is common in the target practice;
- is understandable to a broad CHI reader;
- implies automation, measurement, adaptation, privacy, expertise, causality, or effectiveness;
- accurately describes an unfinished project; and
- could remain consistent across later plans, figures, paper, and video.

For each term, record its operational meaning, likely reader inference, evidence/status, what it
does not imply, allowed variants, unsafe variants, first-definition location, and intended scope.
Do not force one word to carry several dimensions. A terminology system may use one concrete
default term, a different term for the structural contrast, a narrowly scoped term for a
user-adjustable dimension, and explicit reserved terms.

Prefer concrete phrases over compressed jargon. Do not call manually assigned cues
“personalization,” unmeasured low-latency behavior “real-time,” or a researcher-controlled
prototype “expert-operated” unless the planned evidence and actual design support those terms.
Distinguish recipient scope from selection provenance: `recipient-differentiated` means intended
recipients can receive different content; `role- or profile-configured` means a person selects it
from declared attributes; `system-personalized` requires a stored or inferred individual model;
and `adaptive` requires support to change with inferred state, behavior, or performance. Prefer a
clear domain term such as “player-specific” when it communicates scope without implying an
unsupported mechanism. `Personalizable` or `user-adjustable` applies only to the named dimension a
person can configure; it does not make the whole system personalized. Do not use “private” unless
access and routing are verified.

For a general audience, lead with the familiar term and define the exact scientific or technical
construct at first use. Preserve the source's operationalization: for example, introduce `blue
light` before defining `short-wavelength output` or the specific melanopic metric actually used.
Do not collapse those constructs into synonyms merely to simplify the language.

Ask the author to approve the semantic contract before selecting the lexical spine. Until then,
keep every terminology system and dependent contribution phrase `candidate`.

## Record and propagate decisions

Maintain `author-decisions.md`:

```markdown
| Date | Checkpoint | Options shown | Decision | Rationale | Evidence/status | Files to update |
```

After a choice:

1. restate the selected wording and scope;
2. record rejected implications and unresolved evidence;
3. propagate the decision through the evidence maps, related-work matrix, approach, contribution
   package, charts, research outline, handoff, and planned later paper sections; and
4. label superseded and reopened choices rather than erasing them.

Undecided choices remain `candidate`. Future Phase 2 or Phase 3 evidence can reopen any Phase 1
decision.
