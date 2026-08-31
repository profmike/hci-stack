# Changelog

## [0.4.6] - 2026-08-09 — Declarative Motivation and User Value

### Changed

- **Declarative reader-facing motivation.** Motivation, human need, and user value now state the
  evidenced condition or grounded need directly instead of asking readers to endorse that people
  `should` receive a benefit. Untested benefits remain explicit design goals rather than facts.
- **Publication audit.** The project overview now fails publication when its `At a glance` or
  `The user value` section uses author-voice `should`; attributed recommendations and internal
  procedural requirements remain available outside those sections.

## [0.4.5] - 2026-08-09 — Recall-First Motivation Research

### Added

- **Research-discovery recall contract.** High-impact motivation claims now separate recall-first
  candidate intake from strict evidentiary admission, use a population/task/control/acquisition/
  outcome/context facet matrix, promote embedded titles and identifiers, and reconcile an
  independent retrieval challenger.
- **Replayable external-research records.** Search logs and motivation queues now preserve
  provider/model versions, exact prompts or queries, filters, screen depth, raw-artifact hashes,
  candidate roles, and terminal dispositions. Opaque session citation handles cannot serve as
  evidence.
- **Fail-closed phase completion.** The publication audit rejects `phase.status=complete` while the
  motivation, ACM/SIGCHI, or related-work recall gate is open, unchecked, or still templated.

### Changed

- Synchronized previously installed Phase 1 contract, report, citation, and source-manifest fixes
  back into the canonical skill package so the version-controlled source and Codex installation
  are identical.

## [0.4.4] - 2026-08-05 — Source Identity Is Read, Not Retyped

Wrong DOIs and wrong author names reached an author. Both defects had the same shape: an
identifier that existed in two places, or an identity that was never read off the paper itself.

### Added

- **`scripts/render_source_manifest.py`.** The manifest's eight ledger-derived columns are now
  generated from `source-resolution.csv`. Manifest-only judgements — tier, directness, discovery
  route, ingestion status, provenance, notes — survive regeneration untouched.
- **`identity_verified_against` column in `source-resolution.csv`.** A row that holds a full copy
  must record where in that copy the authors, title, year, venue, and pages were read. A scan that
  will not extract is read visually and its page recorded. This is the only check that reaches the
  paper; every other identity check compares copies of a value against each other, so one bad
  transcription out of somebody else's bibliography passes all of them.
- **Two fail-closed checks in `check_source_resolution.py`:** `check_identity_verification` and
  `check_source_manifest_generated`.
- **`tests/test_render_source_manifest.py`**, plus identity-verification cases in
  `tests/test_check_source_resolution.py`.

### Changed

- `references/citation-integrity.md` gains "Read every identity off the copy itself" and "Never
  store an identifier twice", including which axes to verify against the copy.
- `references/prior-work-contribution-boundaries.md` gains "The idea gate", moved out of SKILL.md
  in full: an idea with no demonstration and no study collides with nothing, and venue is the
  prompt to check rather than the verdict in either direction.
- Step 13 of the workflow runs the manifest renderer before the checkers.

### Migration

Existing projects fail with a named missing column until `identity_verified_against` is added and
populated for every row holding a full copy. That is the intended behaviour: an unverified identity
was always unverified, and the column makes it visible.

## [0.4.1] - 2026-08-03 — Durable Phase 1 Workspace

### Added

- **Idempotent workspace initializer.** The motivation-and-contributions skill now creates the
  complete Phase 1 artifact set, a project-root navigation README, and an initially rendered and
  audited HTML report shelf without overwriting existing project work.

### Changed

- **Publish-time reader-view gate.** Material Phase 1 commits, pushes, and handoffs must regenerate
  and audit the report shelf and verify the root README links.
- **Source-manifest template.** Fixed the Markdown column separator count so the provenance table
  renders consistently.

## [0.4.0] - 2026-08-03 — Motivation and Contributions

### Added

- **HCI Motivation and Contributions skill.** Added the complete Phase 1 framing workflow,
  evidence templates, strict prior-work contribution accounting, report tooling, and tests.
- **Private research-source mirroring.** Copyright and license status no longer blocks storing
  full sources in a private project repository, tracking them in version control, or uploading
  them to a private project NotebookLM notebook.

### Changed

- **Multi-skill installers.** The Unix and Windows installers now synchronize every packaged HCI
  skill into each selected local agent rather than installing only Office Hours.
- **Canonical synchronization.** Reusable skill changes are versioned here first and then copied
  to local agent installations so repository and installed copies remain identical.

## [0.3.0] - 2026-04-06 — Cross-Platform, Multi-Agent

### Added

- **Gemini CLI support.** Install script detects `~/.gemini/` and copies skill there. Version check scans Gemini skill path. Usage: `./install gemini`.
- **Windows support.** Added `install.ps1` PowerShell script. Version check uses `$HOME` instead of `~` for Git Bash and PowerShell compatibility.
- **CC BY-NC-SA 4.0 license.** Added LICENSE file.

### Changed

- **Install script now supports 4 targets:** `./install [claude|codex|gemini|auto]`. Auto-detect installs for all agents found on the system.
- **Version check is cross-platform.** Path detection loop uses `$HOME` and covers Claude, Codex, Gemini, and project-local installs.

## [0.2.1] - 2026-03-31 - Reliable Upgrade Detection

### Changed

- Updated the skill startup instructions so failed remote version checks are surfaced to the user instead of silently skipped.
- Added Codex-specific guidance to prefer reinstalling from the public GitHub skill URL over ad hoc `curl` updates when possible.
- Clarified that hosts without network access or browsing support must say that update checking is unavailable.

## [0.2.0] - 2026-03-31 - Claude + Codex Compatibility

### Changed

- Packaged the skill as a self-contained folder by adding `hci-office-hours-with-mike/VERSION`, so Codex GitHub installs keep local version tracking intact.
- Added `hci-office-hours-with-mike/agents/openai.yaml` for Codex skill metadata and explicit `$hci-office-hours-with-mike` invocation support.
- Updated `install` to copy the whole skill directory, preserving `agents/` metadata and future bundled resources for both Claude Code and Codex installs.
- Rewrote host-specific instructions in `SKILL.md` so the same skill body works in Claude and Codex, including generic user-prompting, web search, and a shared brief output path.
- Kept the repo-root `VERSION` file for backward-compatible update checks used by older installs.

## [0.1.0] - 2026-03-31 — Initial Release

HCI research office hours skill for problem definition, motivation, related work, and contribution positioning.

### Added

- **Six forcing questions** — Pain, Observation, Gap, Insight, Impact, Killer Scenario. Smart routing by research stage (Exploring, Problem forming, Positioning).
- **3-tier gap/contribution taxonomy** — capability gap (High), experience gap (Medium), cost gap (Low). Consistent framework across Q3, competitive positioning, and research brief.
- **Competitive positioning with 2-axis quadrant charts** — WebSearch-powered landscape verification with academic, commercial, and open-source coverage. Iterative axis refinement.
- **Evidence quality assessment** — Tier 1 (published), Tier 2 (observed), Tier 3 (hypothetical). Gates next steps based on evidence strength.
- **Problem portfolio ranking** — 7-criterion scoring matrix. Pushes students with one idea to generate alternatives before committing.
- **Simulated CHI reviewer objections** — 2-3 likely R2 objections with draft responses. CHI review criteria context (significance + quality).
- **Research brief output** — Structured markdown document saved to `~/.claude/hci-briefs/`.
- **Operating principles** — Observation is the only currency, solve YOUR problem, interview both practitioners and experts, HCI is about user experience not technology, AI makes prototyping fast, must be able to test with real users.
- **Anti-sycophancy rules** — Never praise vague ideas, challenge technique-driven research, flag mature-field incremental work.
- **Bilingual support** — Responds in Traditional/Simplified Chinese when the student uses it.
- **Version tracking and auto-update** — Prints version at session start and in research briefs. Checks GitHub for updates.
