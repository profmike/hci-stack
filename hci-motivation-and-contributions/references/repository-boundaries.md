# HCI repository-boundary contract

Contract version: `HCI-REPOS-1`

This contract applies to every current and future `hci-*` skill in this repository.

## Reusable skill changes

The version-controlled HCI skill repository is the source of truth; an installed copy is derived
state. After changing a reusable skill, validate it, commit the skill and shared-contract changes to
the skill repository, and push the commit; never leave a requested correction only in a local
installation or unpushed worktree. Stage explicit skill/shared-test paths, inspect the staged diff,
and keep project-specific research data, reports, sources, and generated artifacts out of skill
commits.

## Project-specific data

Store each project's briefs, sources, evidence registers, participant materials, designs, reports, and
handoffs only in that project's own repository or approved governed data store. Resolve that target
repository before creating any durable project artifact. If it has not been created or provided,
continue only read-only inspection, research, and interactive planning in the current session, and
request the target when durable writing becomes necessary. Do not create new durable project artifacts in the reusable skill
repository or an arbitrary workspace. Migrate project data already sitting in a skill worktree only
once the target repository is known, preserving provenance and keeping the original until the move is
verified.

## Future-skill gate

Every new `hci-*` skill must carry an exact copy at `references/repository-boundaries.md` and route to
it from `SKILL.md`. The repository-wide contract test must fail when a current or future HCI skill
omits or diverges from this policy.
