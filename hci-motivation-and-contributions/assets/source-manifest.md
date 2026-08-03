# HCI motivation and contributions source manifest

Notebook title:
Notebook ID:
NotebookLM profile name (no credentials):
Created:
Last verified:
Human-facing evidence-map source/note:
Notebook maintenance record:

| Source ID | Citation key | Bibliographic identity | Tier | Directness | DOI/canonical URL | Canonical repository location | Added | Ingestion status | Source-resolution state/locator | Original checked | Present in author draft? | Found independently by skill? | Discovery route | Claim-matched upgrade search / stronger source | Author-access request surfaced date/locator | Provenance verified by/date | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Search log

| Date | Layer/database | Exact query | Filters/scope | Candidates screened | Sources retained | Exclusion notes |
|---|---|---|---|---:|---:|---|

Use `yes`, `no`, or `unclear` for **Present in author draft?** and **Found independently by
skill?**. Because the workflow inspects the project before research, “independently” is
route-based: the work must also emerge from a documented query or citation chain that did not use
the draft's title, citation, prose, notes, or supplied reading list as its seed. A blinded
pre-bibliography search is stronger when practical but is not required. Record mixed routes
honestly: for example, `independent concept search; exact full copy later supplied by author`. A
second pass by the author or reviewer should verify the search route rather than infer independence
from eventual title overlap or memory.

Every potentially decision-relevant row must also be reconciled with `source-resolution.csv`.
Metadata, a NotebookLM source ID, or `PARTIAL`/`BROKEN` ingestion does not close acquisition.
At phase readiness, every HTTP(S) reference in `references.csv` must have an explicit
source-resolution row. Use an `internal:` URL only for clearly classified project evidence.

Every supplied draft/bibliography/reading-list entry must also appear in
`imported-bibliography-accountability.csv`. Every retained source used for a prior-work collision
or contribution statement must resolve to `prior-work-evidence-accounting.csv`; proposals and
future work instead resolve to `idea-provenance-ledger.csv`. Late-found material sources must
resolve to `late-found-work-postmortem.csv` and, when they changed a boundary, a passing
`novelty-regression-sentinels.yaml` entry.

## Prior-work accounting reconciliation

- Prior-work evidence rows / retained material source count:
- Idea/provenance rows / proposal-only source count:
- Imported bibliography rows / supplied bibliography count:
- Late-found source rows / material late-find count:
- Active novelty regression sentinels / passing at last check:
- Accounting checker last command/date/result:

## Local source-file reconciliation

- Candidate source/import roots inventoried:
- Inventory command or method:
- Inventory date:
- Candidate files found:
- Files reconciled by bibliographic identity to `source-resolution.csv`:
- Unresolved files and consequence:
- Closure marker: `LOCAL_SOURCE_FILES_RECONCILED` / `LOCAL_SOURCE_FILES_NOT_RECONCILED`

Do not write `LOCAL_SOURCE_FILES_RECONCILED` while any local candidate capable of changing a
claim, mechanism, rank, comparator, or study requirement remains outside the ledger.

## Private source-store and sensitive-data check

- [ ] No credentials, cookies, auth files, or browser profiles are recorded.
- [ ] No identifiable participant data or confidential review material was uploaded.
- [ ] Copyright, license, and redistribution status was not used to exclude a research source from the private repository, version control, or the private NotebookLM notebook.
- [ ] Every retained full source has both a canonical repository copy and a verified NotebookLM source ID.
- [ ] Any missing mirror is recorded as an unresolved technical discrepancy with a repair action.
