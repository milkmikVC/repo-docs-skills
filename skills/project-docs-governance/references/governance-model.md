# Documentation Governance Model

Use this reference when deciding the target shape for a repository docs system.

## Responsibility Split

| Layer | Responsibility |
| --- | --- |
| Coding agent runtime | Discover and trigger skills. |
| `repo-docs-router` skill | Find the smallest relevant docs set and route docs update decisions for ordinary work. |
| Repository docs | Store project-specific rules, facts, decisions, plans, and status. |
| `project-docs-governance` skill | Create, migrate, audit, and repair the docs system. |

## Standard Repository Docs

Recommended paths:

- `AGENTS.md`: project rules for coding agents when useful.
- `docs/README.md`: documentation map.
- `docs/contributing/documentation.md`: project-local docs workflow, special paths, and when conversation facts or completed work become documentation.
- `docs/contributing/cross-cutting-concerns.md`: when to define shared conventions.
- `docs/product/vision.md`: product thesis and durable principles.
- `docs/architecture/`: system design and boundaries.
- `docs/reference/`: repeatable implementation rules.
- `docs/adr/`: durable decisions.
- `docs/planning/roadmap.md`: direction and sequencing.
- `docs/planning/implementation-status.md`: current implementation truth against docs.

## Status Model

Significant documents should indicate whether they are current, draft,
experimental, superseded, historical, archived, or unknown. Planning docs
should distinguish planned, in-progress, shipped, partial, deferred, dropped,
and superseded work.

## Design Rules

- Keep project facts in the repository.
- Keep generic workflow in skills.
- Keep `AGENTS.md` short if present.
- Use reference docs for detailed repeatable rules.
- Use ADRs for decisions that should outlive an implementation step.
- Use implementation status for factual drift between docs and code.
- Mark stale or replaced docs explicitly instead of deleting useful history.
