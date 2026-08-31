# Motivation-claim strengthening loop

Use this loop to prevent `hypothesis` and `unsupported` from becoming permanent labels that are
merely repeated in reports. The goal is not to make every claim sound stronger. The goal is to
resolve each consequential motivation or problem-definition claim into the strongest defensible
state: supported, bounded, contradicted, superseded, retired, or assigned to the smallest original
project study that could establish it.

## Scope

Run the loop over every active claim-ledger row marked `hypothesis` or `unsupported`. Prioritize
claims that determine:

- whether the target behavior or experience exists and for whom;
- its prevalence, magnitude, consequences, or distribution;
- current practice, workarounds, and where they fail;
- why the problem is timely;
- the unmet need and opportunity boundary; and
- terminology that changes how the problem is understood.

Also inventory mechanism, experience, and outcome hypotheses about the proposed system, but
do not pretend external adjacency validates a system that has not been built or studied.

Skip no row silently. Rejected, superseded, and duplicate claims remain visible with their
disposition so later work does not restart them.

## Five resolution routes

Assign exactly one primary route before searching:

| Route | Use when | Resolution evidence |
|---|---|---|
| `A — external research` | Published evidence can test the target phenomenon, relationship, magnitude, consequence, or construct | Full primary studies, authoritative syntheses, and contradictions |
| `B — official practice audit` | The claim concerns current products, policies, platform behavior, releases, or documented controls | Dated first-party documentation plus version/scope checks |
| `C — author/project evidence` | The claim concerns the team's target users, workflow, workarounds, unmet need, or context that literature cannot establish directly | A checked existing artifact or a bounded formative evidence need |
| `D — future system evaluation` | The claim concerns the proposed intervention's mechanism, experience, feasibility, adoption, or outcome | A Phase 2 premise test or Phase 3 comparative evaluation |
| `E — retire or supersede` | The claim is vague, duplicated, contradicted, loaded, irrelevant, or unsafe | Explicit replacement or rejection rationale |

A route is not an evidence state. Route `D`, for example, leaves the claim a hypothesis until the
project generates the required evidence.

## Resolution cycle

Read [research-discovery-recall.md](research-discovery-recall.md) completely and create
`motivation-claim-research-queue.md` from the asset template, then:

1. **Enumerate.** Copy every active `hypothesis` and `unsupported` ledger row into the queue. Add
   important motivation-chain gaps that are absent from the ledger.
2. **Normalize.** Rewrite each item as one narrow, falsifiable claim. Split prevalence, association,
   causality, mechanism, current capability, user experience, and comparative effectiveness rather
   than joining them.
3. **Triage.** Assign one primary resolution route and explain why. Mark rejected or superseded
   claims before spending research effort on them.
4. **Prioritize.** Work first on claims with high framing impact, high uncertainty, and a feasible
   resolving route. Within a motivation chain, normally resolve target behavior and population,
   current practice, unmet need, consequence, and why-now before proposed-system mechanisms.
5. **Separate discovery from admissibility.** Build the population, task, interface/control,
   acquisition-stage, outcome/failure, context, and evidence-role facets before searching. Admit a
   candidate when it can expand vocabulary, a citation graph, a boundary, counterevidence, or an
   evidentiary role; do not require it to satisfy the final direct-evidence predicate at intake.
6. **Search in layers and challenge recall independently.** Use exact and disjunctive queries,
   component and neighboring tasks, discipline-native vocabulary and databases, systematic reviews,
   primary studies, official product documentation, intervention/adherence evidence,
   backward/forward/sibling citations, and an explicit contradiction/null search. Reconcile unique
   candidates from at least two independent retrieval systems. Preserve provider/model/version,
   exact prompt/query, date, filters, sort, screen depth, raw-result artifact/hash, and terminal
   candidate dispositions.
7. **Acquire and audit.** Obtain and open the full source, apply the source tier, ingestion,
   directness, and claim-specific evidence-strength axes, and record the decisive locator,
   uncertainty, limitation, and re-review trigger.
8. **Resolve.** Use one of:
   `supported-bounded`, `narrowed`, `contradicted`, `superseded`, `retired`,
   `routed-to-project-evidence`, `needs-author-source-access`, or `still-open`.
   Update the claim ledger and motivation evidence map; do not leave the old broad wording as the
   governing claim.
9. **Repeat.** Promote every title, DOI, or canonical URL found inside notes, references, reports,
   and candidates into its own terminal row. Run another ledger sweep after every material research
   batch because new findings
   often split or invalidate other claims.

## Research stopping rule

The gate reaches `MOTIVATION_CLAIM_AUDIT_COMPLETE` only when every active motivation or
problem-definition claim marked `hypothesis` or `unsupported` has:

- a precise claim and explicit route;
- a documented full-source or official-practice search, including contradictory evidence when
  externally resolvable;
- a replayable claim-facet matrix, independent retrieval challenger, reconciled candidate-role
  dispositions, passing non-title/non-author positive controls, and a complete zero-yield promotion
  wave for every high-impact external route;
- a disposition and bounded replacement wording; and
- either sufficient evidence for its current use or the smallest named project evidence action.

The gate does **not** require proving the proposed system's mechanism or effectiveness during Phase
1. Those claims may remain hypotheses only when they are explicitly routed to later evaluation with
an operational construct, comparator, and success/failure evidence need.

Do not declare the gate complete merely because a report lists open claims. If a high-impact
external or official-practice route remains researchable, continue the search. If a
decision-relevant full source is blocked, follow the author-access protocol and ask for the smallest
access action; do not ask the author to judge or choose the claim.

## Claim-type safeguards

- **Prevalence:** require a target population, sampling frame, episode definition, geography, and
  timeframe. Adjacent daily screen-time prevalence is not target-behavior prevalence.
- **Current practice:** distinguish reminders, soft limits, hard blocks, schedules, allowlists,
  visual changes, notification suppression, and override behavior. Do not compress a mixed control
  landscape into “binary.”
- **Failure or abandonment:** distinguish ignoring one prompt, temporarily bypassing a control,
  disabling a feature, uninstalling, attrition, and intervention abandonment.
- **Why now:** require a dated change plus evidence that it affects the target problem or makes the
  proposed research newly feasible. A recent product release alone may establish capability, not
  importance.
- **Terminology:** trace origin, operational definition, validated measures, and disciplinary use.
  A vivid popular phrase may be a discovery or participant-facing term without becoming the
  academic construct.
- **Proposed-system mechanism/outcome:** external evidence may justify plausibility or a design
  probe, but only direct project evidence can establish that the proposed system produces the
  claimed experience or outcome.

## NotebookLM use

NotebookLM may expand queries, cluster constructs, locate candidate sources, expose contradictions,
and apply the evidence rubric. Do not auto-import or retain a candidate solely because it appears
in a generated report. Curate primary and official sources, inspect the originals, reconcile
NotebookLM ratings manually, and persist the vetted claim-level markings so future analysis can
reuse them under the re-review rule.
