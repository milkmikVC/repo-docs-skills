# Documentation Governance Model

Use this reference when deciding the target shape for a repository docs system.

## Responsibility Split

| Layer | Responsibility |
| --- | --- |
| Coding agent runtime | Discover and trigger skills. |
| `repo-docs-router` skill | Find the smallest relevant docs set for ordinary work. |
| Repository docs | Store project-specific rules, facts, decisions, plans, and status. |
| `project-docs-governance` skill | Create, migrate, audit, and repair the docs system. |

## Standard Repository Docs

Recommended paths:

- `AGENTS.md`: project rules for coding agents when useful.
- `docs/README.md`: documentation map.
- `docs/contributing/documentation.md`: project-local docs workflow and special paths.
- `docs/contributing/cross-cutting-concerns.md`: when to define shared conventions.
- `docs/product/vision.md`: product thesis and durable principles.
- `docs/architecture/`: system design and boundaries.
- `docs/reference/`: repeatable implementation rules.
- `docs/adr/`: durable decisions.
- `docs/planning/roadmap.md`: direction and sequencing.
- `docs/planning/implementation-status.md`: current implementation truth against docs.

## Design Rules

- Keep project facts in the repository.
- Keep generic workflow in skills.
- Keep `AGENTS.md` short if present.
- Use reference docs for detailed repeatable rules.
- Use ADRs for decisions that should outlive an implementation step.
- Use implementation status for factual drift between docs and code.
