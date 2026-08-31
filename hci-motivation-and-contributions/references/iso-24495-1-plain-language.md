# ISO 24495-1 plain-language profile for Phase 1

Use ISO 24495-1:2023 as the reader-outcome standard for the project README and other short
reader-facing Phase 1 summaries. The standard applies to technical writing as well as public
communication. Its four governing principles are:

1. readers get what they need (**relevant**);
2. readers can easily find what they need (**findable**);
3. readers can easily understand what they find (**understandable**); and
4. readers can easily use the information (**usable**).

Authoritative source: [ISO 24495-1:2023 — Plain language, Part 1](https://www.iso.org/standard/78907.html).
The standard is a communication process and outcome profile, not project evidence and not a
substitute for intended-reader evaluation.

## Declare readers and tasks before writing

Put this machine-auditable profile near the top of every project README:

```markdown
<!-- HCI-PLAIN-LANGUAGE: ISO 24495-1:2023 | audience=HCI researchers and project collaborators | tasks=understand the direction; inspect evidence; review decisions; continue to the next phase -->
```

Replace the audience and tasks when the project has different intended readers. Use concrete
reader groups and two or more actions; never leave generic placeholders such as `everyone`,
`reader`, `TBD`, or `understand this document`.

## Apply the four principles

### Relevant

- Lead with the people, activity, context, problem, proposed response, evidence state, and current
  decision or action that the declared readers need.
- Put process history, repository mechanics, and exhaustive caveats in linked records unless they
  change the overview's active claim or next action.
- Preserve imported-material, non-claim, access-block, and prospective-status boundaries where
  omitting them would mislead the declared reader.

### Findable

- Start with `## At a glance`; give the current status and answer before background. Put detailed
  comparisons in a separate `## Closest prior work` section.
- Use descriptive headings and short lists. Keep closest-work entries in the explicit
  **What it did:** / **How this project differs:** form.
- Use `## Continue by task` and group links under reader goals such as understanding the direction,
  checking evidence, reviewing decisions, and continuing to the next phase.
- Put the primary research question, current decision, blocker, or next action where a scanning
  reader will encounter it without following another link.

### Understandable

- Lead with familiar, concrete language, then define the exact scientific or technical term at
  first use. Preserve the source's construct; plain language does not make neighboring constructs
  interchangeable.
- Prefer people and actions to academic noun stacks. Use direct verbs matched to the evidence.
- Break a sentence when it combines the intervention, result, limitation, comparison, and project
  difference. Use bullets when readers must compare repeated fields.
- Explain necessary technical terms in place. Do not force readers to decode internal lifecycle
  labels, contribution taxonomies, or method shorthand to understand the overview.

### Usable

- State what the project team currently needs to decide or do, who owns it, and what record contains
  the supporting detail.
- Make every promised destination a descriptive, valid repository-relative link.
- Ask at least one intended reader to locate the problem, evidence state, closest difference,
  current decision, and next action and to restate each accurately. Record material failures and
  revise; author or agent intuition alone does not establish usability.

## Preserve research integrity

Plain language changes presentation, not evidence. It must never:

- upgrade `planned`, `hypothesis`, `aspiration`, or `unsupported` content;
- hide a direct contradiction or a qualifier needed to keep an active claim true;
- convert a prospective contribution into a result;
- replace stable citation keys, exact source locators, workboard decisions, rejected variants, or
  reopen triggers; or
- make the README the sole source of truth.

Keep the full evidence and decision records in their canonical artifacts. The README is a bounded,
reader-tested route into them.

## Review gate

Before publication, inspect the README in GitHub rendering on desktop and phone. Check the declared
audience and tasks against all four principles. Automated checks may enforce the profile marker,
required information architecture, evidence-state visibility, links, and citation structure; they
cannot establish that real intended readers understand or can use the document.
