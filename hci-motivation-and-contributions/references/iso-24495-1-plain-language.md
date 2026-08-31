# ISO 24495-1 plain-language profile for Phase 1

Use [ISO 24495-1:2023 — Plain language, Part 1](https://www.iso.org/standard/78907.html) as the
reader-outcome standard for the project README and other short reader-facing Phase 1 summaries:
readers get what they need (**relevant**), can easily find it (**findable**), can easily understand
it (**understandable**), and can easily use it (**usable**). It is an outcome profile, not project
evidence and not a substitute for intended-reader evaluation.

## Declare readers and tasks before writing

Put this machine-auditable profile near the top of every project README:

```markdown
<!-- HCI-PLAIN-LANGUAGE: ISO 24495-1:2023 | audience=HCI researchers and project collaborators | tasks=understand the direction; inspect evidence; review decisions; continue to the next phase -->
```

Replace the audience and tasks for different intended readers, using concrete reader groups and two
or more actions; never leave placeholders such as `everyone`, `reader`, or `TBD`.

## Apply the four principles

**Relevant.** Lead with the people, activity, context, problem, proposed response, evidence state,
and current decision; move process history and repository mechanics into linked records, but keep
imported-material, non-claim, access-block, and prospective-status boundaries wherever omitting them
would mislead.

**Findable.** Start with `## At a glance`, giving current status and answer before background; put
comparisons in `## Closest prior work`, whose entries keep the **What it did:** /
**How this project differs:** form; and group descriptive links under reader goals in
`## Continue by task`. A scanning reader meets the research question, current decision, blocker, or
next action without following another link.

**Understandable.** Lead with familiar, concrete language, then define the exact scientific term at
first use, preserving the source's construct — plain language does not make neighboring constructs
interchangeable, and never forces readers to decode internal lifecycle labels or method shorthand.

**Usable.** State what the team must decide or do, who owns it, and which record holds the detail,
with every promised destination a descriptive, valid repository-relative link. Ask at least one
intended reader to locate and restate the problem, evidence state, closest difference, decision, and
next action, then revise on material failures; author or agent intuition does not establish
usability.

## Preserve research integrity

Plain language changes presentation, not evidence. It must never upgrade `planned`, `hypothesis`,
`aspiration`, or `unsupported` content; hide a contradiction or a qualifier needed to keep an active
claim true; convert a prospective contribution into a result; replace stable citation keys, exact
locators, workboard decisions, rejected variants, or reopen triggers; or make the README the sole
source of truth.

## Review gate

Before publication, inspect the README in GitHub rendering on desktop and phone against the declared
audience, tasks, and four principles. Automated checks enforce the profile marker, information
architecture, evidence-state visibility, links, and citation structure; they cannot establish that
real readers understand the document.
