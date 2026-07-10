# Standard Repository Docs Contract

Use this reference when identifying the normal documentation paths in a
software repository.

## Standard Paths

| Path | Role |
| --- | --- |
| `AGENTS.md` | Project rules for coding agents when present. It is a project rule source, not the required mechanism for finding skills. |
| `docs/README.md` | Map of the documentation set and primary docs entry points. |
| `docs/contributing/documentation.md` | Project-local documentation workflow, update rules, and special paths. |
| `docs/contributing/cross-cutting-concerns.md` | Rules for deciding when a repeated pattern needs a shared convention. |
| `docs/product/vision.md` | Durable product thesis, principles, and non-goals. |
| `docs/architecture/` | System design, data flow, ownership, boundaries, and open questions. |
| `docs/reference/` | Concrete repeatable conventions, often with rule IDs. |
| `docs/adr/` | Architecture Decision Records for durable decisions. |
| `docs/planning/roadmap.md` | Sequencing and intended direction. |
| `docs/planning/implementation-status.md` | Factual comparison between documented expectations and current implementation. |

## Document Status

Significant docs should identify whether they are current, draft,
experimental, superseded, historical, archived, or unknown. See
`references/document-status.md` for the status model.

## Reading Order

Do not read every file by default. Start from entry points, then route by task:

1. Check `docs/contributing/documentation.md` for the local workflow, update
   rules, and special paths.
2. Check `docs/README.md` for a docs map.
3. Load task-specific docs from architecture, reference, ADR, planning, or
   product areas.
4. Use `AGENTS.md` as a project rule source when present.

## Source-of-truth Rule

The repository wins over this generic contract. If a project intentionally uses
different paths, follow the project docs after verifying that the path exists.
