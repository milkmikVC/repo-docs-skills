# Task Routing Matrix

Use this reference to choose the smallest documentation set for a task.

## Product Behavior

Read:

- `docs/product/vision.md`
- Relevant `docs/architecture/*.md`
- `docs/planning/implementation-status.md` when the question is shipped vs planned

## Architecture and Boundaries

Read:

- Relevant `docs/architecture/*.md`
- Relevant `docs/adr/*.md`
- `docs/planning/roadmap.md` when sequencing or future direction changes
- `docs/planning/implementation-status.md` when current conformance matters

## API, Backend, DTOs, Errors, Validation

Read:

- `docs/reference/api-conventions.md` when present
- `docs/architecture/error-handling.md` when present
- Relevant contracts, controller, service, or schema docs
- `docs/contributing/cross-cutting-concerns.md` if a repeated pattern is involved

## Frontend UI

Read:

- `docs/reference/web-conventions.md` when present
- Relevant product or architecture docs
- Design-system or component-library docs when the repository references them

## Data Model and Persistence

Read:

- Relevant `docs/architecture/*.md`
- Relevant `docs/adr/*.md`
- Migration or local database docs when present
- `docs/contributing/cross-cutting-concerns.md` for persistence conventions

## Environment Variables

Read:

- `docs/architecture/environment.md` when present
- `.env.example`
- Runtime config loader docs or source only after reading docs

## Roadmap, Status, or Planning

Read:

- `docs/planning/roadmap.md`
- `docs/planning/implementation-status.md`
- Relevant architecture docs if the status claim is subsystem-specific

## ADR or Decision Work

Read:

- Existing `docs/adr/*.md`
- Relevant architecture docs
- `docs/contributing/documentation.md` for local ADR rules

## Cross-cutting Conventions

Read:

- `docs/contributing/cross-cutting-concerns.md`
- Relevant `docs/reference/*.md`
- Relevant architecture docs
- ADRs if the decision is durable

## Documentation Update Decisions

Read:

- `docs/contributing/documentation.md`
- `references/documentation-lifecycle.md` from this skill
- `references/document-status.md` from this skill when document freshness or
  plan status matters

Route updates as follows:

- Product facts and principles -> `docs/product/vision.md`
- System behavior, ownership, data flow -> `docs/architecture/*.md`
- Repeatable implementation rules -> `docs/reference/*.md`
- Durable decisions -> `docs/adr/*.md`
- Intended work or sequencing -> `docs/planning/roadmap.md`
- Shipped-vs-documented truth -> `docs/planning/implementation-status.md`
- Docs workflow rules or special paths -> `docs/contributing/documentation.md`
