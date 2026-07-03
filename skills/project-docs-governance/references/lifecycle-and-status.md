# Documentation Lifecycle and Status

Use this reference when adding a documentation lifecycle to a new project or
repairing an existing one.

## Required Lifecycle

A healthy docs workflow should cover both sides of normal agent work:

1. Before work, route to the docs that establish current project facts.
2. During discussion, identify durable user-confirmed facts and decisions.
3. After work, decide whether docs must be created or updated.
4. Before final response, state which docs changed or why no update was needed.

## Conversation Facts

Add a section like this to `docs/contributing/documentation.md`:

```md
## When Conversation Facts Become Docs

Update docs when a conversation establishes a durable project fact, accepted
decision, repeated convention, roadmap change, or correction to a stale
assumption that future agents or contributors should rely on.

Do not update docs for one-off task instructions, temporary preferences, or
brainstorming that has not become a decision.
```

## Completion Check

Add a completion check that asks whether the task changed:

- product behavior or user workflow,
- architecture, data flow, ownership, persistence, or APIs,
- environment variables,
- agent behavior, retrieval, citations, prompts, or tools,
- a repeated convention,
- roadmap, implementation status, ADRs, or document status.

## Document Status Block

Use a compact status block for significant docs:

```md
> Status: Current
> Last reviewed: 2026-07-03
> Applies to: API error handling and validation responses.
```

Recommended document statuses:

- `Current`: authoritative within its scope.
- `Draft`: proposed but not accepted.
- `Experimental`: current trial or spike.
- `Superseded`: replaced by another doc or decision.
- `Historical`: no longer current but useful for rationale.
- `Archived`: no longer current and not expected to guide future work.
- `Unknown`: status is unclear.

When marking a doc `Superseded`, include the replacement path.

## Plan Item Status

Use explicit statuses in roadmap and planning docs:

- `Planned`
- `In progress`
- `Shipped`
- `Partial`
- `Deferred`
- `Dropped`
- `Superseded`

Keep roadmap intent separate from implementation truth. Use implementation
status docs to compare intended work with current code.
