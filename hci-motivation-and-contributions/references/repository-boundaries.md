# HCI repository-boundary contract

Contract version: `HCI-REPOS-2`

This contract applies to every current and future `hci-*` skill in this repository.

## Reusable skill changes

- Treat the version-controlled HCI skill repository as the source of truth. An installed skill copy
  is derived state, never the only edited copy.
- After changing a reusable skill, validate it, commit the skill and shared-contract changes to the
  skill repository, and push the commit. Do not leave a requested skill correction only in a local
  installation or unpushed worktree.
- After the canonical commit is pushed, synchronize every existing local installation of the skill
  from that committed repository version, remove stale files that are absent from the canonical
  package, and verify recursive equality. This includes Codex, Claude Code, Gemini, and other local
  hosts when their installation directories exist.
- Never finish a skill-update task with the repository and any installed copy divergent. If an
  urgent correction began in an installed copy, port it into the canonical repository, validate and
  push there, then reinstall all local copies before reporting completion.
- Stage explicit skill/shared-test paths and inspect the staged diff before committing. Never include
  project-specific research data, reports, sources, or generated artifacts in a skill commit.

## Project-specific data

- Store each project's briefs, sources, evidence registers, participant materials, designs,
  reports, and handoffs only in that project's own repository or approved governed data store.
- Resolve the target project repository before creating durable project artifacts. If it has not
  been created or provided, continue only read-only inspection, research, and interactive planning
  in the current session; request the target when durable writing becomes necessary. Do not create
  new durable project artifacts in the reusable skill repository or an arbitrary workspace.
- If project data already exists in a skill repository worktree, keep it out of skill commits.
  Migrate it only after the target project repository is known, preserving provenance and without
  deleting the original until the move is verified.

## Private copyrighted-source storage

- Treat the project repository and the project's NotebookLM notebook as private, governed project
  stores. Copyright, license, and redistribution status are not gating conditions for saving a
  source in the repository, tracking it in version control, or uploading it to NotebookLM.
- Do not require a separate per-source author confirmation for those private storage actions once
  the author has placed the project, repository, and notebook in scope.
- Do not exclude or ignore a project source merely because it is copyrighted or lacks an open
  license. Store every retained full source canonically under
  `research-framing/sources/full-text/`, mirror it into NotebookLM by default, and record both its
  repository-relative path and NotebookLM source ID.
- Treat a missing repository or NotebookLM copy as a technical discrepancy to record and repair,
  not as a license-compliance outcome.
- This rule applies to copyrighted research sources. It does not authorize storing credentials,
  authentication material, identifiable participant data, confidential peer-review material, or
  unrelated third-party secrets without a separate explicit data-governance decision.

## Future-skill gate

Every new `hci-*` skill must carry an exact copy at
`references/repository-boundaries.md` and route to it from `SKILL.md`. The repository-wide contract
test must fail when a current or future HCI skill omits or diverges from this policy.
