# Documentation Lifecycle

Use this reference during ordinary project work, after routing to the relevant
docs. It covers when new facts from chat or completed work should update
repository documentation.

## Conversation Flow

For architecture, product, API, data-model, or workflow discussions:

1. Use `repo-docs-router` to find the local docs workflow.
2. Read `docs/contributing/documentation.md` first when it exists.
3. Read only the relevant product, architecture, reference, ADR, roadmap, or
   status docs.
4. Discuss and confirm the key decision or durable fact with the user.
5. Add or update the smallest appropriate doc.
6. State what docs changed, or why no docs update was needed.

## When Chat Facts Become Docs

Write or update docs when the conversation establishes a durable fact that
future agents or contributors should rely on:

- The user states a long-lived project rule.
- The user corrects a product, architecture, API, data-model, or workflow
  assumption that future work may repeat.
- A decision chooses one direction over another.
- A recurring pattern becomes a shared convention.
- A runtime/source investigation proves docs are stale.
- A plan changes from possible future work to intended work, shipped work, or
  dropped work.
- A feature exposes a gap between documented intent and current behavior.

Ask before documenting when the fact is still exploratory, politically
sensitive, or would create a broad convention the user has not accepted.

## When Not to Update Docs

Do not update docs for:

- One-off task instructions.
- Temporary preferences for the current turn.
- Brainstorming that has not become a decision.
- Pure formatting, rename, or mechanical code changes with no documented
  behavior impact.
- Implementation details likely to change before anyone should depend on them.
- Facts already accurately covered by existing docs.

If no update is needed after meaningful work, say why.

## Where to Write

| Durable fact or change | Typical doc target |
| --- | --- |
| Product thesis, principle, non-goal | `docs/product/vision.md` |
| System behavior, ownership, data flow, boundaries | `docs/architecture/*.md` |
| Concrete repeatable implementation rule | `docs/reference/*.md` |
| Important decision choosing one direction over another | `docs/adr/NNNN-title.md` |
| Sequencing or intended future work | `docs/planning/roadmap.md` |
| Current shipped-vs-documented truth | `docs/planning/implementation-status.md` |
| Docs workflow or special docs paths | `docs/contributing/documentation.md` |
| Shared-convention decision process | `docs/contributing/cross-cutting-concerns.md` |
| Runtime variables | environment docs and `.env.example` |

Prefer the smallest single doc update that future agents can find.

## Completion Check

Before finalizing meaningful work, check:

- Did the work change product behavior or user workflow?
- Did it change architecture, data flow, ownership, persistence, or APIs?
- Did it add, remove, or rename an API contract or environment variable?
- Did it affect agent behavior, retrieval, citations, prompts, or tools?
- Did it introduce or change a repeated convention?
- Did it create, accept, reverse, supersede, or drop a decision?
- Did it change roadmap status or implementation status?
- Did any doc used during the task have a stale or non-current status?

If yes, update the docs or explain why a docs update is intentionally deferred.
