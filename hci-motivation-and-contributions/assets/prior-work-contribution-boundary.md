# Prior-work contribution-boundary synthesis

Canonical row-level evidence: `prior-work-evidence-accounting.csv`.

Related accountability:

- `idea-provenance-ledger.csv`
- `imported-bibliography-accountability.csv`
- `late-found-work-postmortem.csv`
- `novelty-regression-sentinels.yaml`

Default rule: exclude until positive evidence supports the smallest named unit. Keep capability
collision separate from contribution attribution.

## Corpus summary

| Record ID | Work | Smallest unit / channel / finding | Author claim | Demonstrated artifact or study | Operated capability | Evaluated result | Capability collision | Contribution credit | Attribution status | Scope boundary |
|---|---|---|---|---|---|---|---|---|---|---|
| PWE-001 | | | | | | | `EXACT` / `PARTIAL` / `NONE` / `UNRESOLVED` | `FULL` / `PARTIAL` / `NONE` / `UNRESOLVED` | | |

## PWE-001 — [work and atomic proposition]

### Source and smallest unit

- **Work, source ID, and citation key:**
- **Complete first-party versions checked:**
- **Atomic proposition:**
- **Unit kind:** command / parameter / input channel / reward channel / configuration / condition /
  evaluated finding.
- **Smallest named operated unit:**
- **Input or signal → transformation → mapped command/effect:**
- **Generalization boundary:**

### Six independent fields

| Field | Status | Positive evidence and exact locator | Scope or mismatch |
|---|---|---|---|
| `AUTHOR CLAIM` | yes / no / partial / unresolved | | |
| `DEMONSTRATED ARTIFACT OR STUDY` | yes / no / partial / unresolved / N/A | | |
| `OPERATED CAPABILITY` | yes / no / partial / unresolved / N/A | | |
| `EVALUATED RESULT` | yes / no / partial / unresolved / N/A | | |
| `CAPABILITY COLLISION` | exact / partial / none / unresolved | | |
| `CONTRIBUTION CREDIT` | full / partial / none / unresolved | | |

No field inherits truth from another. `OPERATED CAPABILITY=no` requires positive evidence that
settles the audited version; source silence remains `unresolved`.

### Collision versus attribution

- **Attribution status:** `CLAIMED_AND_DEMONSTRATED` / `DEMONSTRATED_UNCLAIMED` /
  `CLAIMED_UNDEMONSTRATED` / `NEITHER` / `UNRESOLVED`.
- **Focal complete human-activity predicate:**
- **Prior positively operated human-activity predicate:**
- **Collision level:** `FULL_CAPABILITY_COLLISION` / `INDEPENDENT_SUBCAPABILITY_COLLISION` /
  `COMPONENT_OR_MECHANISM_PRECEDENT` / `NO_COLLISION`.
- **Removal-test result:** which dimensions change the meaningful human activity or relationship?
- **Drop-in-port result:** could the prior mechanism unchanged support the focal semantics,
  interdependence, and purpose?
- **Component-subtraction check:** confirm that a loose subset of generic qualifiers was not treated
  as an independent sub-capability or full collision.
- **Exact capability collision and focal claim affected:**
- **Component or mechanism inherited without narrowing the complete capability:**
- **Exact contribution fairly attributable to the authors:**
- **False-firstness, fair-comparator, inheritance, or implementation-novelty consequence:**
- **Claimed atom excluded for lack of matched evidence:**

### Evaluation and causal scope

- **Evidence granularity:** atomic operation / package condition / empirical finding / other.
- **Causal attribution:** atomic / package only / not applicable.
- **Comparator, construct, population/context, timeframe, and uncertainty:**
- **Why nonsignificance is or is not allowed to support equivalence/non-inferiority language:**

### Mixed-channel audit

- **Classification scope:** `ATOMIC_CHANNEL` / `PACKAGE_ONLY` / `WHOLE_SYSTEM`.
- **Required channel set for any whole-system label:** `||`-separated `channel_id` values.
- **Positively qualified channel set:** same syntax; each ID resolves to a positively demonstrated,
  positively operated `ATOMIC_CHANNEL` row.
- **Conventional, unrelated, unresolved, or proposal-only channels:**
- **Whole-system label allowed:** yes / no + evidence.

### Port/adaptation gate

- **Port status:** `NOT_A_PORT` / `PORT_ONLY` / `ADAPTATION_CANDIDATE`.
- **Underlying operated capability collision:**
- **Credit gate:** none / demonstrated nontrivial adaptation / demonstrated new use class /
  directly validated empirical finding.
- **Matched evidence:**
- **Contribution-credit disposition:**

### Silence and reopen action

- **Source-silence disposition:** `NOT_USED` / `SEARCH_PRIORITY` / `REOPEN_QUERY`.
- **Exact next source, artifact, version, supplement, repository, or query:**
- **Reopen trigger:**

## Idea provenance synthesis

- **Prior proposals or future work:** IDs from `idea-provenance-ledger.csv`.
- **First-idea or conceptual-lineage consequence:**
- **Confirmed `CAPABILITY COLLISION=NONE`:**
- **Confirmed `CONTRIBUTION CREDIT=NONE`:**
- **Potential Discussion use:**
- **Forbidden capability, feasibility, effectiveness, or contribution use:**

## Imported-bibliography and late-find repair

- **Supplied artifacts inventoried:**
- **Imported entries accounted for / total:**
- **Material imported entries with terminal source resolution:**
- **Late-found material works:**
- **Sibling records screened and routes repaired:**
- **Affected claims, collisions, credits, rankings, gaps, comparators, and study requirements rerun:**
- **Regression sentinels and last non-title retrieval result:**
- **Final complete zero-yield promotion wave:**

## Corpus-level conclusion

- **Attributed claimed-and-demonstrated prior contributions:**
- **Demonstrated-unclaimed capabilities that narrow firstness at a matched predicate or independent
  sub-capability scope:**
- **Claimed-undemonstrated atoms excluded:**
- **Exact and partial capability collisions:**
- **Component/mechanism precedents that establish inheritance without narrowing the complete
  capability:**
- **Zero-credit ports and any adaptation gates that passed:**
- **Package-level results that cannot support operator-specific causality:**
- **Mixed systems that cannot receive whole-system labels:**
- **Source-silence search priorities/reopen queries:**
- **Strongest search-bounded focal-project distinction:**
- **Residual source, search, and false-novelty risks:**

## Completion markers

Check a marker only after the named artifact and evidence are complete. The accounting checker
requires checked markers at bounded-round closure and phase readiness.

- [ ] `IMPORTED_BIBLIOGRAPHY_ACCOUNTED`
- [ ] `CLAIM_DEMONSTRATION_OPERATION_EVALUATION_DECOMPOSED`
- [ ] `CAPABILITY_COLLISION_AND_CREDIT_SEPARATED`
- [ ] `HUMAN_ACTIVITY_PREDICATES_AND_COLLISION_LEVELS_CHECKED`
- [ ] `NO_COMPONENT_SUBTRACTION_FALLACY`
- [ ] `DEMONSTRATED_UNCLAIMED_OPERATIONS_REVIEWED`
- [ ] `MIXED_CHANNELS_DECOMPOSED`
- [ ] `PORT_CREDIT_GATES_APPLIED`
- [ ] `NO_PROPOSAL_GRANTED_CAPABILITY_CREDIT`
- [ ] `NO_SILENCE_DERIVED_CAPABILITY_OR_ABSENCE`
- [ ] `LATE_FOUND_WORK_REPAIR_COMPLETE`
- [ ] `NOVELTY_REGRESSION_SENTINELS_RECHECKED`
- [ ] `ZERO_YIELD_PROMOTION_WAVE_COMPLETE`
