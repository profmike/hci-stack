# ACM DL and SIGCHI related-work coverage

This is a **coverage and situating gate**, not a prestige filter: CHI and other relevant
SIGCHI-sponsored or co-sponsored conferences get deliberate search priority because HCI reviewers
expect authors to know that conversation, but venue never repairs a weak method, makes an indirect
result direct, or upgrades an `ES1` claim to `ES2` or `ES3`.

## Establish the current venue scope

At the start of each landscape pass, open the current official
[ACM SIGCHI conferences page](https://sigchi.org/conferences/), record the check date and relevant
sponsored/co-sponsored venues in `acm-sigchi-related-work-audit.md`, and verify each retained work's
venue, year, and sponsorship status. Never hard-code a venue list; sponsorship and names change.
Start from CHI, then search the parts of the current portfolio whose communities match the problem
or mechanism, filing PACM HCI articles under their actual conference identity.

## Run a native ACM Digital Library search

A general web or NotebookLM search never substitutes for a direct ACM DL pass. First freeze the
target-problem identity — target people, focal activity, triggering or temporal context, unwanted
state, intended change — keeping the proposed mechanism separate. Then run at least these query
families:

1. **Target problem:** population, activity, setting, consequence, established academic terms.
2. **Neighboring constructs:** alternative construct names, theories, participant language.
3. **Causal interaction mechanism:** what changes, when, through which interaction, under what
   user control.
4. **Closest conjunction:** problem + mechanism + context, with qualifiers that may carry the
   proposed contribution.
5. **Known seeds and lineage:** exact titles/authors, their references, their citers, and newer
   work that extends them.

Keep same/similar-problem work and different-problem mechanism collisions in separate queues; the
latter never stands in for saturation of the former. Log each query's exact string, date, result
count, filters, candidates screened, works retained, and exclusion reasons.

ACM results and abstracts are discovery only: a work cannot support a claim, comparison, or chart
placement until its exact full copy is opened under the evidence protocol. If access presents a
CAPTCHA, institutional sign-in, or subscription barrier, follow the human-access escalation
procedure: try lawful author/repository copies and the author's university IP or VPN, then surface
the exact unresolved paper and URL.

## Run a parallel component-foundation and falsification pass

The ACM pass locates the HCI conversation but does not complete the literature search for the
proposed components. For every active or imported component, search beyond comparators for
evidence that justifies or falsifies its operational mechanism, decomposing:

`component → changed parameter → proximal human mechanism → desired outcome → failure/side effect`

Search each component in its own discipline's indexes and vocabulary rather than the project's: a
display intervention pulls grayscale, luminance, spectral/blue-light, circadian, and perception
sources; a network intervention pulls latency, rebuffering, throughput, video QoE, and abandonment
sources. Classify every such work — even a distant one — as design/mechanism foundation,
technical-feasibility evidence, motivation/physiology evidence, counterevidence, analogy only, or
screened out; account for every supplied bibliography title in
`imported-bibliography-accountability.csv`; and route every source that could change an active
decision into full-text source resolution.

## Audit search recall, not only query completion

Read [forward-citation-expansion.md](forward-citation-expansion.md) completely before running
cited-by searches; it defines the high-leverage multi-route, multi-wave stopping rule.

The five query families are a minimum structure, not proof of coverage. Before combining terms,
build a synonym lattice that varies each mechanism dimension in the table below independently,
along with people, activity, context, problem constructs, participant language, channel words such
as delay, friction, degradation, or attenuation, and the intended outcome. Populate it from project
language, index terms, and — critically — the titles, keywords, abstracts, and Related Work
vocabulary of close full papers. Run disjunctive and mechanism-only queries alongside target-heavy
conjunctions, and saturate the same/similar-problem branch independently. A paper addressing a different problem through the same
causal mechanism may omit the target population entirely: retain it as a component/mechanism
precedent, or as a capability collision when its complete human-activity predicate or an
independently claimed sub-capability matches, but never as a closest problem comparator.

Screening only the first page or first 20 records of a large result set never establishes coverage:
refine by mechanism dimension, screen further strata, state a stopping rule, and record what was
screened. Then use known close works as positive-control sentinels — each must surface through a
non-title/non-author query, and a miss means repairing the vocabulary or filter and rerunning that
family. Sentinels test the search process; never use them to tune a novelty claim.

Coverage rests on **two independent discovery routes**, both recorded explicitly rather than
inferred from a fluent synthesis: the complete reference list of every closest full paper, with an
include, exclude, or acquire decision for each title plausibly sharing the problem, access state,
progression variable, causal interaction mechanism, or outcome tradeoff; and the forward-citation
protocol run wave by wave to its stopping point.

Create `related-work-search-recall-audit.md`. A material work discovered after saturation was
claimed is a process failure: record it in `late-found-work-postmortem.csv`, identify the route
that should have found it, screen sibling citing records from the missed seed, add a
non-title/non-author test to `novelty-regression-sentinels.yaml`, repair the coverage, and rerun
every downstream judgment it touches, from evidence boundary and capability collision through
contribution credit, ranking, gap, novelty, comparator, and broader-HCI synthesis.

## Prioritize without distorting the corpus

Screen same/similar-problem work first — CHI, then other currently verified SIGCHI venues, then
other ACM HCI work, then HCI and domain work outside ACM — before different-problem
mechanism/capability collisions and broader theory, health, technical, or product evidence. This
controls search effort only: retain a non-ACM paper when it is the strongest source for a claim,
exclude an ACM paper that is only a keyword or surface modality collision, and never let venue
prestige upgrade problem proximity or evidence strength.

Either discuss every relevant close CHI or SIGCHI work in the matrix and contribution audit, or
record a specific exclusion reason in `acm-sigchi-related-work-audit.md` — a different causal
mechanism, no matching activity or consequence, a superseded version, or an inaccessible full copy
with a visible access request. “Not useful” is not sufficient.

## Read the HCI conversation, not only the result

For the closest retained works, read the full paper and record the design tension and lineage it
inherits, what it implemented and evaluated versus only proposed as future work, the practice or
agency it preserves, the tradeoffs it exposes, how later papers characterize it, and its
problem-proximity band. A paper can be a claim-specific collision because it shares the complete
human-activity predicate or an independently claimed consequential sub-capability while remaining
adjacent in problem; a shared device, modality, channel, timing property, or low-level mechanism
alone is only a foundation to credit, not evidence that the complete capability is old.

Before using words such as *gradual*, *progressive*, *adaptive*, *stronger*, *soft*, or *hard*,
decompose each intervention into independent mechanism dimensions:

| Dimension | Required question |
|---|---|
| Access state | Usable, partly usable, or unavailable while active? |
| Intention / goal anchor | Regulating cumulative daily exposure, a session, a clock/event transition, or a sensed state? |
| Configuration object and certainty | What must the person specify, and is its clarity measured, author-observed, or hypothesized? |
| Activation selector/gate | What triggers activation, and is that gate intrinsic or study-fixed? |
| Changed parameter | Block duration, attenuation level, delay, feature availability, effort, or what else? |
| Progression variable | Which parameter changes across steps, and which stay fixed? |
| Within-active ramp | Immediate, eased in, stepwise, adaptive, or fixed — and what advances it? |
| Duration | How long does each state last? |
| Onset and cadence | What triggers a state, when does it recur, and are there access windows between? |
| Cap and reset | Where does progression saturate, what resets it, per what unit? Mark unreported reset behavior unresolved. |
| Scope | Which app, feature, content, device function, or channel is affected? |
| Override and exceptions | Can the person bypass, postpone, pause, or retain valued functions? |
| Selection/control | Who sets the threshold, schedule, level, or transition rule? |
| Design provenance | Originated here, adapted from platform practice, or inherited from research? |

Do not infer a graduated **intensity** mechanism from graduated **duration**, or a nonbinary access
state from intermittent access windows between binary blocks. Do not collapse a pre-trigger bedtime
taper into a post-budget ease-in: activation and within-active progression are separate mechanisms.
Distinguish a study-fixed threshold from an intrinsic product rule, never invent a reset from a
reported cap, and describe the changed parameter literally before compressing it into a design
label.

A daily usage budget and a target-bedtime schedule are likewise different constructs, not
interchangeable timers: a budget's threshold lands at a different clock time depending on earlier
use, while a bedtime anchor names an intended transition. A claim that people have a stronger or
less vague idea of target bedtime than of a daily cap is an author/project hypothesis until direct
evidence measures that difference.

Do not attribute a control pattern's origin to the first close HCI paper found. When a paper
follows a platform or product convention, record the genealogy as
`current-practice baseline → HCI adaptation → proposed project inheritance`, crediting the platform
for the convention, the HCI paper for its research-system use and evidence, and the project only
for a consequential surviving difference.

An explicit future-work proposal the prior system never implemented has
`CAPABILITY COLLISION=NONE` and `CONTRIBUTION CREDIT=NONE`. Preserve it in
`idea-provenance-ledger.csv`, label it `proposed-not-implemented`, and use it in Discussion to
connect the focal result to a broader HCI aspiration rather than as an existing capability.

## Situate relevance to the broader HCI community

Synthesize the corpus into a broader HCI question rather than a list of systems:

1. **Community conversation:** the concern, lineage, or design space this project joins.
2. **Unresolved tension:** the tradeoff or uncertainty that survives the closest work.
3. **Project leverage:** what it reveals beyond one app, device, or population.
4. **Transfer boundary:** which other settings can learn from it, and which qualifiers limit that.

The final outline must credit that lineage before stating a gap, name any direct collision with
the planned approach, and state one evidence-bounded broader-HCI implication. “Relevant to HCI
because it is an interface” does not pass.

## Completion gate

Create `acm-sigchi-related-work-audit.md` from the asset template. Step 5 is complete only when
every rule above has a recorded outcome there or in `related-work-search-recall-audit.md` — in
particular when:

- the recall audit carries the synonym lattice, large-result-set stopping rules, positive-control
  sentinels, reference-title accountability, and the complete high-leverage multi-route/multi-wave
  forward-citation ledger ending in a zero-yield promotion wave, with any late find postmortemed,
  sibling-swept, sentinel-tested, and rerun;
- every retained work has a problem-proximity band, a portfolio assignment, and either a verified
  full copy or a visible blocking author-access request, and every closest mechanism is decomposed
  across the dimension table above before novelty is judged;
- every material prior-work atom is accounted for under
  [prior-work-contribution-boundaries.md](prior-work-contribution-boundaries.md), with proposals
  and future work held in idea provenance at collision and credit `NONE`; and
- the broader-HCI synthesis is complete and the artifacts are marked
  `ACM_SIGCHI_LANDSCAPE_AUDITED` and `RELATED_WORK_SEARCH_RECALL_AUDITED`.

If any item remains open, use `NEEDS_LANDSCAPE_RESEARCH` or `NEEDS_AUTHOR_SOURCE_ACCESS`. An
`UNASSESSED` or acquire-only candidate is not a completed foundation/exclusion decision. Do not ask
the author to choose a gap or contribution while this gate is incomplete.
