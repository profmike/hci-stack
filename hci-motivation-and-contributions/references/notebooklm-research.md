# NotebookLM research workflow

`notebooklm-mcp-cli` is an unofficial client for internal NotebookLM APIs verified with `nlm 0.9.4`;
run `nlm --version` and `--help` when syntax differs.

## 1. Setup and authentication

```bash
command -v nlm
command -v notebooklm-mcp
nlm login --check
```

If missing, obtain permission before changing user-level tools, install `notebooklm-mcp-cli` with
`uv tool` or `pipx`, then register it by absolute path:

```bash
codex mcp add notebooklm-mcp -- /absolute/path/to/notebooklm-mcp
claude mcp add --scope user notebooklm-mcp -- /absolute/path/to/notebooklm-mcp
nlm skill install codex --level user
nlm skill install claude-code --level user
nlm config set auth.browser chrome
nlm login
```

For multiple accounts use `nlm login --profile NAME` consistently. The author must complete Google
sign-in. Never capture or print cookies, auth JSON, or browser-profile files.

## 2. Notebook and source lifecycle

One notebook per research project; confirm ingestion before querying.

```bash
nlm notebook create "HCI Motivation and Contributions - PROJECT" --json
nlm notebook list --title
nlm source add NOTEBOOK_ID --file /absolute/path/paper.pdf --wait --json
nlm source add NOTEBOOK_ID --url https://canonical.example/report --wait --json
nlm source add NOTEBOOK_ID --drive GOOGLE_DRIVE_ID --type pdf --wait --json
nlm source list NOTEBOOK_ID --full --json
```

## 3. Headed Chrome acquisition

Use a connected, visible Chrome session so the author can handle institutional login, consent,
CAPTCHA, and downloads. Acquire only through authorized access to the canonical publisher, DOI,
agency, or dataset page — never snippets, AI summaries, or mirrors of uncertain provenance — then
confirm identity, record the landing URL/DOI and access date, and save the copy under
`research-framing/sources/full-text/` with its repository-relative path and NotebookLM source ID.

Repository and notebook are private project stores: copyright, license, and redistribution status
must not block repository storage, version control, or NotebookLM upload, and none of these requires
separate per-source author confirmation. Mirror every retained source into both stores and repair
failures that leave them inconsistent.

## 4. Searching and synthesizing

```bash
nlm research start "LAYERED QUERY" --source web --mode deep --notebook-id NOTEBOOK_ID
nlm research status NOTEBOOK_ID --max-wait 0
nlm research import NOTEBOOK_ID TASK_ID --cited-only
```

Discovery does not confer T1 status. Mirror every decision-relevant candidate into
`source-resolution.csv` immediately. NotebookLM research completion or
successful metadata import does not close that row: open the exact full source, or exhaust the
lawful acquisition routes and surface a concrete author-access request. Never end an audit with
candidates merely labeled `UNASSESSED`.

Author-provided references are seed sources that must not set the evidence ceiling or bias
synthesis; run the upgrade search and disposition recording in
[evidence-protocol.md](evidence-protocol.md). NotebookLM comparison is an analysis aid: verify
quantitative claims in the original table, figure, dataset, or passage and related-work limitations
in the primary paper, and let the manual original-source audit set the cached claim-specific
rating.

### Keep the notebook human-readable

Source imports are append-only and never reconcile themselves against a later manual audit. After
every bounded research round:

1. list the sources and verify that each object contains the intended work rather than a CAPTCHA,
   login, error, metadata-only, or wrong page, and replace broken imports before synthesis uses
   them;
2. keep a `START HERE` evidence map pointing to the evidence register, and retitle retained objects
   with bibliographic and evidence-role names; and
3. resolve every new candidate in `source-resolution.csv` as assessed, screened out, superseded, or
   a surfaced author-access request, log duplicates, superseded snapshots, and broken or
   screened-out objects in `notebooklm-maintenance.md`, and reconcile the notebook list against the
   source manifest, evidence register, and missing-copy queue.

Deletion is irreversible: preserve unique content and locators first, show the author the
exact source-ID deletion set and reasons, and obtain explicit confirmation before deleting a source.
An unconfirmed deletion stays visibly pending and must not block other work.

Query narrowly with explicit source IDs; answers may omit caveats or misattribute claims, so
re-open the originals before using one.

```bash
nlm notebook describe NOTEBOOK_ID --json
nlm source describe SOURCE_ID --json
nlm notebook query NOTEBOOK_ID \
  "For each selected source, report population, method, N or coverage, exact result, uncertainty, limitations, and the passage that supports the claim. Separate direct evidence from inference." \
  --source-ids SOURCE_ID_1,SOURCE_ID_2 --json
```

### Recursive related-work discovery

Synthesis does not replace citation chaining, which runs per
[forward-citation-expansion.md](forward-citation-expansion.md): read each retained seed in full,
take backward citations in both required categories (same problem approached differently, different
problem approached similarly), open each exact citing work before retaining it, verify every claim
about a seed against the seed itself, and repeat until a pass finds no materially closer work.
NotebookLM's semantic similarity, source ordering, or fluent synthesis cannot promote a shared
concept or mechanism into a closest overall problem comparator; assign the problem-proximity band
from [related-work-positioning.md](related-work-positioning.md).

Never substitute an abstract, snippet, thesis, preprint, or citing paper for the published work. A
full copy supplied later is verified, reconciled against the earlier exclusion, and propagated to
`source-resolution.csv`, the source manifest, missing-copy queue, and evidence register before
synthesis resumes.

## 5. Saving durable research state

```bash
nlm chats list NOTEBOOK_ID
nlm chats to-note NOTEBOOK_ID CONVERSATION_ID --title "HCI motivation and contributions synthesis"
nlm chats export NOTEBOOK_ID --conversation-id CONVERSATION_ID \
  --format md --output research-framing/notebooklm-synthesis.md
nlm note create NOTEBOOK_ID --title "Verified framing" --content "CONTENT"
```

Fill every column of `source-manifest.md`, recording the profile name without secrets and keeping a
work that appeared in the author draft distinct from one the skill also found through a route that
did not use that reference as a seed. The manifest and evidence ledger are the durable state;
NotebookLM chat alone is not a reproducible record.

Mirror the notebook ID, user-facing title, and profile name into
`research-framing/agent-context.json` in the same work round; that pointer manifest is read
identically by Codex `$gpt-pro` and Claude Code `/gpt-pro` and must not contain credentials,
cookies, auth paths, source contents, or synthesis. Reconcile it with `source-manifest.md` after a
notebook rename, replacement, or profile change and before a terminal handoff.

## 6. Verification and privacy

- Copyrighted sources may be stored in the private project repository and uploaded to the private
  project NotebookLM without license or redistribution screening.
- Do not upload raw participant data, PII, confidential drafts, peer-review material, credentials,
  authentication material, or unrelated third-party secrets unless a separate explicit
  data-governance decision authorizes that category; for the authors' studies prefer de-identified
  aggregate summaries and manuscript sections approved for external processing.
- Keep `~/.notebooklm-mcp-cli/` and all auth material outside repositories and logs. If
  authentication fails, stop the research step and report the exact login action needed; do not
  silently replace NotebookLM grounding with unsourced model memory.
