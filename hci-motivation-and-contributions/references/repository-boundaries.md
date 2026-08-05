# HCI repository-boundary contract

Contract version: `HCI-REPOS-1`

This contract applies to every current and future `hci-*` skill in this repository.

## Reusable skill changes

- Treat the version-controlled HCI skill repository as the source of truth. An installed skill copy
  is derived state, never the only edited copy.
- After changing a reusable skill, validate it, commit the skill and shared-contract changes to the
  skill repository, and push the commit. Do not leave a requested skill correction only in a local
  installation or unpushed worktree.
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

## Future-skill gate

Every new `hci-*` skill must carry an exact copy at
`references/repository-boundaries.md` and route to it from `SKILL.md`. The repository-wide contract
test must fail when a current or future HCI skill omits or diverges from this policy.
