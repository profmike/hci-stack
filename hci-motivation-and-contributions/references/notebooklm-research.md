# NotebookLM research workflow

`notebooklm-mcp-cli` is an unofficial client for internal NotebookLM APIs. Commands and Google
behavior may change. Run `nlm --version` and the relevant `--help` command when syntax differs.
The commands below were verified with `nlm 0.9.4`.

## Contents

1. Setup and authentication
2. Notebook and source lifecycle
3. Headed Chrome acquisition
4. Searching and synthesizing
5. Saving durable research state
6. Verification and privacy

## 1. Setup and authentication

Check first:

```bash
command -v nlm
command -v notebooklm-mcp
nlm login --check
```

If missing, obtain permission before changing user-level tools. Preferred install:

```bash
uv tool install notebooklm-mcp-cli
```

If `uv` is unavailable:

```bash
pipx install notebooklm-mcp-cli
```

Register the MCP server with the clients the author uses. Resolve the full executable path with
`command -v notebooklm-mcp`, then pass that exact path:

```bash
codex mcp add notebooklm-mcp -- /absolute/path/to/notebooklm-mcp
claude mcp add --scope user notebooklm-mcp -- /absolute/path/to/notebooklm-mcp
nlm skill install codex --level user
nlm skill install claude-code --level user
```

Use a headed Chrome profile for authentication:

```bash
nlm config set auth.browser chrome
nlm login
nlm login --check
```

For multiple accounts, use `nlm login --profile NAME` and pass `--profile NAME` consistently. The
author must complete Google sign-in. Never capture or print cookies, auth JSON, or browser-profile
files.

## 2. Notebook and source lifecycle

Create one notebook per research project and capture the JSON response:

```bash
nlm notebook create "HCI Motivation and Contributions - PROJECT" --json
nlm notebook list --title
```

Add full sources and wait for ingestion:

```bash
nlm source add NOTEBOOK_ID --file /absolute/path/paper.pdf --wait --json
nlm source add NOTEBOOK_ID --url https://canonical.example/report --wait --json
nlm source add NOTEBOOK_ID --drive GOOGLE_DRIVE_ID --type pdf --wait --json
nlm source list NOTEBOOK_ID --full --json
```

Use local-file upload when a headed browser was required for authorized access. Use canonical URLs
for open official pages. Confirm ingestion status before querying.

## 3. Headed Chrome acquisition

Use a connected, visible Chrome session so the author can handle institutional login, consent,
CAPTCHA, and downloads. For each candidate:

1. Start from the canonical publisher, DOI, agency, or dataset page.
2. Confirm bibliographic identity and whether the source is primary.
3. Inspect methods, population, dates, measures, results, and limitations.
4. Download only through authorized access.
5. Give the file a stable bibliographic name and record the landing URL/DOI and access date.
6. Upload it with `nlm source add --file ... --wait`.
7. Save the canonical copy under `research-framing/sources/full-text/`, track it in the private
   project repository, and record both its repository-relative path and NotebookLM source ID.

The project repository and NotebookLM notebook are private project stores. Copyright, license, and
redistribution status must not block repository storage, version control, or NotebookLM upload,
and these actions do not require separate per-source author confirmation. Do not omit a source,
keep only metadata, or add a PDF ignore rule because the work is copyrighted or lacks an open
license. Mirror every retained full source into both stores by default; record and repair technical
failures that leave the two working sets inconsistent.

Do not rely on search-result snippets, AI-generated result summaries, or mirrors of uncertain
provenance.

## 4. Searching and synthesizing

NotebookLM web research can discover candidates:

```bash
nlm research start "LAYERED QUERY" --source web --mode deep --notebook-id NOTEBOOK_ID
nlm research status NOTEBOOK_ID --max-wait 0
nlm research import NOTEBOOK_ID TASK_ID --cited-only
```

Review every imported candidate. Discovery does not confer T1 status.

Immediately mirror every potentially decision-relevant candidate into
`source-resolution.csv`. NotebookLM research completion or successful metadata import does not
close that row. Obtain and open the exact full source, or try the lawful acquisition routes and
surface a concrete author-access request. Never end a source audit with NotebookLM candidates
merely labeled `UNASSESSED`.

Author-provided PDFs, reading lists, and imported draft bibliographies are seed sources. Do not let
their presence in the notebook set the evidence ceiling or bias synthesis toward only those works.
Run the independent claim-matched upgrade search in the evidence protocol, add stronger and
contradictory sources when lawful, and save the seed disposition (`retained-with-bounds`,
`corroborated`, or `SUPERSEDED`) with stable locators. A NotebookLM comparison is an analysis aid;
the manual original-source audit determines the cached claim-specific rating.

### Keep the notebook human-readable

NotebookLM source imports are append-only working objects; they do not reconcile themselves when a
manual audit later replaces, screens out, or supersedes a source. After every bounded research
round:

1. list the complete source set and verify that each object contains the intended work rather than
   a CAPTCHA, login, error, metadata-only, or wrong page;
2. maintain a human-readable `START HERE` evidence map explaining the project's strength tags and
   pointing to the canonical project evidence register;
3. rename retained objects with readable bibliographic and evidence-role titles instead of
   machine-only state strings;
4. replace broken imports before allowing NotebookLM synthesis to rely on them;
5. resolve every new candidate as fully assessed, screened out, superseded, or an exact surfaced
   author-access request in `source-resolution.csv`;
6. record duplicates, superseded snapshots, broken objects, and screened-out objects in
   `notebooklm-maintenance.md`; and
7. reconcile the notebook list with the source manifest, evidence register, missing-copy queue,
   and source-resolution ledger.

Source deletion is irreversible. Preserve unique content and stable locators first, show the
author the exact source-ID deletion set and reasons, and obtain explicit confirmation before
deleting any NotebookLM source. A cleanup proposal may close a research round; an unconfirmed
deletion must remain visibly pending and must not block other evidence work.

Generate overviews:

```bash
nlm notebook describe NOTEBOOK_ID --json
nlm source describe SOURCE_ID --json
```

Query narrowly, preferably with explicit source IDs:

```bash
nlm notebook query NOTEBOOK_ID \
  "For each selected source, report population, method, N or coverage, exact result, uncertainty, limitations, and the passage that supports the claim. Separate direct evidence from inference." \
  --source-ids SOURCE_ID_1,SOURCE_ID_2 --json
```

Useful query sequence:

1. Extract study design and methodological limits source by source.
2. Ask which source directly supports a proposed claim and which only supports an analogy.
3. Compare findings, populations, measures, and disagreements across sources.
4. Identify the closest prior approaches and their author-stated limitations.
5. Ask what evidence would falsify or narrow the proposed framing.
6. Draft a synthesis only after the source-level checks.

NotebookLM answers may omit caveats or misattribute claims. Re-open the originals before using the
answer.

### Recursive related-work discovery

NotebookLM synthesis does not replace citation chaining. For every retained seed paper:

1. read the complete Abstract, Introduction, Related Work, and reference list;
2. identify backward citations in the two required categories: the same problem approached
   differently, and a different problem approached similarly;
3. use headed Chrome to inspect forward citations and retrieve newer works;
4. save and open the exact complete work before retaining it;
5. find each passage in which a newer work cites the seed, then record the newer authors'
   characterization, positive inheritance, and stated boundary or limitation with an exact
   locator; and
6. verify every claim about the seed against the seed itself.

Assign a problem-proximity band before treating any discovered paper as close. Saturate
same/similar-problem discovery independently and keep different-problem mechanism/capability
collisions in their own portfolio. NotebookLM's semantic similarity, source ordering, or fluent
synthesis cannot promote a shared concept or mechanism into a closest overall problem comparator.

Repeat until a complete pass finds no materially closer work. Record inaccessible exact works
separately; never substitute an abstract, search snippet, thesis, preprint, or citing paper when the
exact published work is the intended reference. When an author later supplies a missing full copy,
reconcile its identity and update the exclusion rather than leaving contradictory records.

After a manual download or headed-browser access handoff, verify the file/page identity, inspect the
full methods, results, limitations, corrections, and relevant supplements, then update
`source-resolution.csv`, the source manifest, missing-copy queue, and evidence register before
resuming NotebookLM synthesis. Save the verified full source in the private project repository and
upload it to the private project NotebookLM regardless of copyright, license, or redistribution
status. If either operation fails technically, record the exact failure and keep the reconciliation
open until repaired.

## 5. Saving durable research state

Save a synthesis inside NotebookLM and export the conversation:

```bash
nlm chats list NOTEBOOK_ID
nlm chats to-note NOTEBOOK_ID CONVERSATION_ID --title "HCI motivation and contributions synthesis"
nlm chats export NOTEBOOK_ID --conversation-id CONVERSATION_ID \
  --format md --output research-framing/notebooklm-synthesis.md
```

Or save an explicit note:

```bash
nlm note create NOTEBOOK_ID --title "Verified framing" --content "CONTENT"
```

The project source manifest should record notebook ID, profile name without secrets, source ID,
bibliographic identity, DOI/canonical URL, tier, canonical repository location, upload status,
verification status, access date, whether the work appeared in the author draft, whether the skill
also found it through a documented route that did not use the draft reference as a seed, the actual
discovery route, and who verified that provenance. Treat the manifest and evidence ledger as
durable state; NotebookLM chat alone is not a reproducible record.

Mirror the notebook ID, user-facing title, and profile name into
`research-framing/agent-context.json` in the same work round. That pointer manifest is consumed
identically by Codex `$gpt-pro` and Claude Code `/gpt-pro`; it must not contain credentials,
cookies, auth paths, source contents, or duplicated synthesis. Reconcile it with
`source-manifest.md` after a notebook rename, replacement, or profile change and before a terminal
handoff.

## 6. Verification and privacy

- Verify quantitative claims in the original table, figure, dataset, or passage.
- Verify related-work limitations in the primary paper; do not accept NotebookLM's comparison
  without checking.
- Copyrighted sources may be stored in the private project repository and uploaded to the private
  project NotebookLM without license or redistribution screening.
- Do not upload raw participant data, PII, confidential drafts, peer-review material, credentials,
  authentication material, or unrelated third-party secrets unless a separate explicit
  data-governance decision authorizes that category.
- For the authors' studies, prefer de-identified aggregate summaries and manuscript sections
  approved for external processing.
- Keep `~/.notebooklm-mcp-cli/` and all auth material outside repositories and logs.
- If authentication fails, stop the research step and report the exact login action needed. Do not
  silently replace NotebookLM grounding with unsourced model memory.
