# Documentation Workflow

## Purpose

Documentation is part of the engineering system. It preserves product
direction, architecture decisions, implementation status, and repeatable
project conventions.

## Required Flow

Before meaningful product, architecture, API, data-model, or cross-cutting
work:

1. Read the relevant docs.
2. Make the change.
3. Update affected docs in the same change, or state why no docs update was
   needed.

## Which Docs to Read

- Product direction: `docs/product/vision.md`
- Architecture: `docs/architecture/`
- Decisions: `docs/adr/`
- Roadmap: `docs/planning/roadmap.md`
- Implementation status: `docs/planning/implementation-status.md`
- Repeatable conventions: `docs/reference/`
- Cross-cutting concerns: `docs/contributing/cross-cutting-concerns.md`

## When to Update Docs

Update docs when a change affects product behavior, architecture, API shape,
storage, environment configuration, shared conventions, or roadmap/status
assumptions.

## When Conversation Facts Become Docs

Update docs when a conversation establishes a durable project fact, accepted
decision, repeated convention, roadmap change, or correction to a stale
assumption that future agents or contributors should rely on.

Do not update docs for one-off task instructions, temporary preferences, or
brainstorming that has not become a decision.

## Document Status

Use a compact status block near the top of significant docs:

```md
> Status: Current
> Last reviewed: YYYY-MM-DD
> Applies to: Short scope statement.
```

Recommended document statuses:

- `Current`: authoritative within its scope.
- `Draft`: proposed but not accepted.
- `Experimental`: current trial or spike.
- `Superseded`: replaced by another doc or decision.
- `Historical`: no longer current but useful for rationale.
- `Archived`: no longer current and not expected to guide future work.
- `Unknown`: status is unclear.

Roadmap and planning items should use explicit statuses such as `Planned`,
`In progress`, `Shipped`, `Partial`, `Deferred`, `Dropped`, or `Superseded`.

## Completion Documentation Check

Before finishing meaningful work, check whether the task changed product
behavior, architecture, data flow, ownership, persistence, APIs, environment
variables, agent behavior, retrieval, citations, prompts, tools, shared
conventions, roadmap, implementation status, ADRs, or document status.

Update the relevant docs, or state why no docs update was needed.
