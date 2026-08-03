# ACM DL and SIGCHI related-work coverage

Use this protocol to prevent a common HCI positioning failure: presenting a technically plausible
idea without showing how it relates to the questions, systems, findings, and design tensions already
developed by the HCI community.

This is a **coverage and situating gate**, not a prestige filter. CHI and other relevant
SIGCHI-sponsored or co-sponsored conferences receive deliberate search priority because HCI
reviewers reasonably expect authors to know that conversation. Venue does not repair a weak method,
make an indirect result direct, or upgrade an `ES1` claim to `ES2` or `ES3`.

## Establish the current venue scope

At the start of each landscape pass:

1. open the current official [ACM SIGCHI conferences page](https://sigchi.org/conferences/);
2. record the check date and the relevant sponsored/co-sponsored venues in
   `acm-sigchi-related-work-audit.md`; and
3. verify the exact venue, year, and sponsorship/co-sponsorship status for each retained work.

Do not rely on a permanent hard-coded venue list. Sponsorship and conference names can change.
Treat CHI as the flagship starting point, then search the relevant parts of the current SIGCHI
portfolio—for example CSCW, DIS, UbiComp/ISWC, TEI, IUI, MobileHCI, or CHI PLAY when their
communities match the problem or mechanism. Include relevant PACM HCI articles under their actual
conference/issue identity.

## Run a native ACM Digital Library search

A general web or NotebookLM search does not substitute for a direct ACM DL pass. Search the ACM
Digital Library with at least these query families:

1. **Target problem:** population, activity, setting, consequence, and established academic terms.
2. **Neighboring constructs:** alternative construct names, theories, and participant language.
3. **Causal interaction mechanism:** what the system changes, when, through which interaction, and
   with what user control.
4. **Closest conjunction:** problem + mechanism + context, including qualifiers that may carry the
   proposed contribution.
5. **Known seeds and lineage:** exact titles/authors, their references, papers that cite them, and
   newer work that characterizes or extends them.

For every query, record the exact string, date, result count, filters or sorting, candidates
screened, works retained, and exclusion reasons. Search title variants and author names when ACM
metadata or punctuation makes a phrase query brittle.

Before running those families, freeze the target-problem identity as target people, focal activity,
triggering or temporal context, unwanted state or episode, and intended change or outcome. Keep
the proposed mechanism separate. Maintain distinct result queues for same/similar-problem work and
different-problem mechanism collisions; do not let the latter stand in for saturation of the
former.

Use ACM search results and abstracts for discovery. A work cannot support a claim, comparison, or
chart placement until its exact full copy is obtained and opened under the evidence protocol. If
ACM access presents a CAPTCHA, institutional sign-in, or subscription barrier, follow the
human-access escalation procedure: try lawful author/repository copies and the author's university
IP or VPN, then surface the exact unresolved paper and URL.

## Run a parallel component-foundation and falsification pass

The native ACM pass locates the HCI conversation; it does not complete the literature search for
the proposed components. For every active or imported approach component, search beyond contribution
comparators for the evidence needed to justify or falsify its operational mechanism. Decompose:

`component → changed parameter → proximal human mechanism → desired outcome → failure/side effect`

Use the relevant disciplinary indexes and vocabulary. Display interventions may require grayscale,
luminance, contrast, color temperature, spectral/blue-light, circadian, perception, and
accessibility sources. Network interventions may require latency, startup delay, rebuffering,
throughput, video QoE, engagement, abandonment, and perceived-failure sources. Trace named
interventions across product versions, authors, venues, randomized or longitudinal evaluations,
and current practice.

Record these works even when they are not close HCI contribution comparators. Classify them as
design/mechanism foundation, technical-feasibility evidence, motivation/physiology evidence,
counterevidence, analogy only, or screened out. For supplied bibliographies, account for every
title in `imported-bibliography-accountability.csv` and put every source that could change an active
decision into the full-text source-resolution loop.

## Audit search recall, not only query completion

Read [forward-citation-expansion.md](forward-citation-expansion.md) completely before running
cited-by searches. The protocol expands the seed graph beyond closest comparators and defines the
multi-route, multi-wave stopping rule.

The five query families are a minimum structure, not proof of coverage. Before combining terms,
build a synonym lattice along independent dimensions:

- target people/activity and context/transition;
- problem constructs and participant language;
- access state;
- changed parameter and progression variable;
- interaction or intervention channel, including terms such as delay, latency, effort, friction,
  input manipulation, interaction proxy, degradation, attenuation, intensity, or step increase;
- intention/goal anchor, configuration object and burden, onset, cadence, scope, override, and
  selector; and
- intended outcome or tradeoff.

Populate the lattice from known project language, index terms, and—critically—the titles,
keywords, abstracts, and Related Work vocabulary of close full papers. Run disjunctive and
mechanism-only queries as well as target-heavy conjunctions. Saturate the same/similar-problem
branch independently. A paper addressing a different problem through the same causal mechanism
may omit the target population and context entirely; retain it as a mechanism/capability collision
when relevant, but do not rank it as a closest problem comparator.

If a query returns hundreds or thousands of records, screening only the first page or first 20
records never establishes coverage. Refine the query by mechanism dimension, screen additional
pages or result strata, and state a stopping rule. Record the number of pages/records actually
screened. “Default recency, first 20” is a discovery sample, not a saturation decision.

After the lattice is drafted, use known close works as positive-control sentinels. Each sentinel
must appear through at least one non-title/non-author query. If it does not, diagnose the vocabulary
or filter failure, add the missing terms, and rerun the affected family. This tests the search
process; it must not be used to tune a novelty claim around a preferred result.

For every closest full paper, inspect its complete reference list and account for every title that
plausibly shares the problem, access state, progression variable, causal interaction mechanism, or
outcome tradeoff. Record a specific include, exclude, or acquire decision. Separately build the
high-leverage forward-citation seed portfolio across closest works, author seeds, component
foundations/falsifiers, decision-relevant syntheses/methods, and prior late finds. Run two
independent cited-by routes, newest and relevance/citation views, large-graph partitions, and
successive promotion waves until a complete wave yields no new decision-relevant work. The audit
must record those **two independent discovery routes** and waves explicitly rather than infer them
from a fluent synthesis.

Create `related-work-search-recall-audit.md`. If a material work is discovered after saturation was
claimed, treat it as a process failure: record it in `late-found-work-postmortem.csv`, identify the
route that should have found it, screen sibling citing records from the missed seed, add a
non-title/non-author test to `novelty-regression-sentinels.yaml`, repair the graph/query coverage,
and rerun the evidence boundary, capability collision, contribution credit, ranking, gap, novelty
boundary, contribution tier, fair comparator, study requirements, and broader-HCI synthesis.

## Prioritize without distorting the corpus

Screen in this order:

1. same/similar-problem CHI work;
2. same/similar-problem work from other currently verified SIGCHI-sponsored/co-sponsored
   conferences;
3. other same/similar-problem ACM HCI work;
4. same/similar-problem HCI and domain work outside ACM;
5. different-problem mechanism/capability collisions across the same venue routes; and
6. broader theory, health, behavioral-science, technical, or product evidence needed for the
   argument.

This order controls search effort, not inclusion or evidence strength. Retain a non-ACM paper when
it is the strongest source for a claim. Exclude an ACM paper when it is only a keyword collision or
surface-level modality match. Same-domain vocabulary and venue prestige cannot upgrade a work's
problem proximity. Never pad Related Work with venue citations that do not change the landscape.

For every relevant close CHI or SIGCHI work, either:

- include and discuss it in the matrix and contribution audit; or
- record a specific exclusion reason in `acm-sigchi-related-work-audit.md`.

“Not useful” is not a sufficient reason. Valid reasons include a different causal mechanism, no
matching activity or consequence, an extended abstract with no decision-relevant evidence, a
superseded version, duplicate publication, or an inaccessible full copy whose exclusion and access
request remain visible.

## Read the HCI conversation, not only the result

For the closest retained HCI works, read at least the Abstract, Introduction, Related Work,
system/intervention, study, findings, Discussion, limitations, and references. Record:

- the HCI problem or design tension the paper opens;
- the interaction lineage and theories it inherits;
- the product, platform, standard, or earlier system from which each material control pattern was
  adopted, when the paper reports one;
- what it implemented and evaluated versus what it only proposed as future work;
- the valued practice, need, agency, or experience it preserves;
- the design tradeoffs or negative results it exposes;
- how later HCI papers characterize, challenge, or extend it; and
- the precise relationship to the current project.

Before calling a paper close overall, record its problem-proximity band. A paper can be a
claim-specific collision because it shares an exact mechanism or capability while remaining
adjacent or different in problem, objective, context, and intended outcome.

Before using words such as *gradual*, *progressive*, *adaptive*, *stronger*, *soft*, or *hard*,
decompose each intervention into independent mechanism dimensions:

| Dimension | Required question |
|---|---|
| Access state | Is the target activity usable, partly usable, or unavailable while the intervention is active? |
| Intention / goal anchor | What is the person trying to regulate: cumulative exposure across a day, one session, a clock/event transition, a sensed state, or another goal? |
| Configuration object and certainty | What must the person specify: a duration budget, target clock time, event, app/feature set, or policy? Is its clarity/stability measured, author-observed, or only hypothesized? |
| Activation selector/gate | What must happen before the intervention activates: clock/context transition, session start, cumulative usage budget, threshold crossing, sensed state, or explicit user action? Is that gate intrinsic to the system or fixed only for the study? |
| Changed parameter | What exactly changes: block duration, attenuation level, delay, content/feature availability, interaction effort, reminder frequency, or something else? |
| Progression variable | Which parameter changes across steps, and which parameters remain fixed? |
| Within-active ramp | After activation, is the change immediate, eased in, stepwise, adaptive, or fixed? What event advances it: elapsed time, interaction count, context, or a new session? |
| Duration | How long does each intervention state last? |
| Onset and cadence | What triggers a state, when does it recur, and are there access windows between states? |
| Cap and reset | Where does progression saturate, what resets it, and does reset occur per interaction, opening, session, bypass, day, or not at all? Mark unreported reset behavior as unresolved. |
| Scope | Which app, feature, content, device function, or communication channel is affected? |
| Override and exceptions | Can the person bypass, postpone, pause, or retain emergency/valued functions? |
| Selection/control | Who sets the threshold, schedule, level, or transition rule? |
| Design provenance | Did the paper originate this control pattern, adapt it from current platform/product practice, or inherit it from earlier research? |

Do not infer a graduated **intensity** mechanism from graduated **duration**, or a nonbinary access
state from intermittent access windows between binary blocks. Do not collapse a pre-trigger
bedtime taper into a post-budget ease-in: activation and within-active progression are separate
mechanisms. Distinguish a study-fixed threshold from an intrinsic product rule, and do not invent a
reset when the paper reports only a cap. Describe the changed parameter literally before
compressing the comparison into a design label. If a paper uses an ambiguous label, retain its
wording as a quotation only after recording the actual operational mechanism.

A daily usage budget and a target-bedtime schedule are also different behavioral-control
constructs, not interchangeable timer implementations. A budget expresses an allowed cumulative
quantity over an accounting day; its threshold may be reached at different clock times depending
on earlier use. A bedtime anchor expresses an intended transition at a clock or event time and
allows a schedule relative to that transition. Compare the user’s configuration task, confidence,
stability, trigger predictability, behavioral objective, and failure mode. If a project claims that
people have a stronger or less vague idea of target bedtime than of a daily cap, record it as an
author/project hypothesis until direct evidence measures or observes that difference.

Do not attribute a control pattern’s origin to the first close HCI paper found. When a paper says it
follows a platform or product convention, record the genealogy as
`current-practice baseline → HCI adaptation → proposed project inheritance`. Credit each layer for
what it actually contributes: the platform for the existing interaction convention, the HCI paper
for its research-system use and evidence, and the project only for a consequential surviving
difference.

An explicit future-work proposal has `CAPABILITY COLLISION=NONE` and
`CONTRIBUTION CREDIT=NONE` when the prior system did not implement or demonstrate it. Preserve it
in `idea-provenance-ledger.csv`, label it `proposed-not-implemented`, and use it selectively in
Discussion to connect the focal result to a broader HCI aspiration. Do not misreport it as an
existing capability or demonstrated contribution.

## Situate relevance to the broader HCI community

Do more than list systems. Synthesize the corpus into a broader HCI question with four parts:

1. **Community conversation:** the established HCI concern, lineage, or design space this project
   joins.
2. **Unresolved tension:** the consequential tradeoff or knowledge uncertainty that survives the
   closest work.
3. **Project leverage:** what studying this project could reveal beyond one app, device, or
   population.
4. **Transfer boundary:** which other HCI settings may learn from the result, and which qualifiers
   limit that transfer.

Examples of broader relevance include autonomy versus effective self-regulation, friction versus
usability, valued digital use versus disengagement, intervention timing under changing attention,
and how context changes the acceptability of persuasive technology. These are examples, not claims
to copy.

The final outline must credit the closest HCI lineage before stating a gap, identify any direct
collision with the planned approach, and state one evidence-bounded broader-HCI implication or
research question. “Relevant to HCI because it is an interface” does not pass.

## Completion gate

Create `acm-sigchi-related-work-audit.md` from the asset template. Step 5 is complete only when:

- the current SIGCHI venue scope and check date are recorded;
- all five native ACM DL query families have been run and logged;
- the target-problem identity is explicit, the same/similar-problem branch is saturated
  independently, and every retained work has a problem-proximity band and portfolio assignment;
- the separate search-recall audit includes the mechanism/problem synonym lattice, large-result-set
  stopping rules, positive-control sentinels, reference-title accountability, and the complete
  high-leverage multi-route/multi-wave forward-citation ledger;
- close CHI and relevant SIGCHI works are included or specifically excluded;
- retained comparators have verified full copies, or a visible author-access request blocks them;
- every active/imported approach component has a documented foundation-and-falsification pass,
  including discipline-specific vocabulary, counterevidence, and source-resolution status;
- every closest mechanism is decomposed by access state, activation selector/gate, changed
  parameter, within-active progression, duration/cadence, cap/reset, scope, override, selector,
  intention/goal anchor, and configuration burden before similarity or novelty is judged;
- every material prior-work atom has independent author-claim, demonstrated-artifact/study,
  operated-capability, evaluated-result, capability-collision, and contribution-credit fields;
- capability collision uses only positively operated units, including demonstrated-unclaimed
  operations, while attributed contribution credit uses claimed-and-demonstrated evidence;
- proposals and future work remain in idea provenance with collision and credit `NONE`; source
  silence creates only search priority or a reopen query;
- mixed channels are decomposed, package evidence stays at package scope, and whole-system labels
  require every operationally necessary channel;
- zero-credit ports and any demonstrated adaptation-credit gate remain explicit;
- backward citations and a complete zero-yield forward-citation promotion wave reveal no
  decision-relevant unreviewed work;
- every supplied bibliography item is accounted for with terminal source resolution when material;
- any late-found close work has a completed postmortem, sibling sweep, passing regression sentinel,
  and documented rerun of affected claims;
- the broader-HCI conversation, unresolved tension, project leverage, and transfer boundary are
  synthesized; and
- the artifacts are marked `ACM_SIGCHI_LANDSCAPE_AUDITED` and
  `RELATED_WORK_SEARCH_RECALL_AUDITED`.

If any item remains open, use `NEEDS_LANDSCAPE_RESEARCH` or `NEEDS_AUTHOR_SOURCE_ACCESS`. An
`UNASSESSED` or acquire-only candidate is not a completed foundation/exclusion decision. Do not ask
the author to choose a gap or contribution while this gate is incomplete.
