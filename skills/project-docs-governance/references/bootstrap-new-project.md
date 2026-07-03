# Bootstrap a New Project

Use this workflow for a new or undocumented repository.

## Steps

1. Inspect the repository purpose, stack, apps, libraries, and existing README.
2. Copy only useful templates from `assets/docs-skeleton/`.
3. Replace placeholders with project-specific facts.
4. Keep the first docs set small.
5. Add an initial ADR only for a real durable decision.
6. Add roadmap and implementation status only if they will guide near-term work.
7. Add a document lifecycle section and status-marker rules to
   `docs/contributing/documentation.md`.

## Minimal Useful Set

For most projects, start with:

- `docs/README.md`
- `docs/contributing/documentation.md`
- `docs/product/vision.md`
- `docs/architecture/overview.md` or another architecture entry point
- `docs/planning/roadmap.md`

Add `docs/reference/`, `docs/adr/`, and implementation status when the project
has recurring conventions, durable decisions, or meaningful shipped-vs-planned
tracking.

Mark significant docs with a compact status block so future agents know whether
they describe current truth, a draft, an experiment, or historical context.

## Avoid

- Large generic docs that do not match the codebase.
- Multiple overlapping roadmap/status files.
- Copying every template file just because it exists.
- Storing secrets, private operational details, or unverifiable claims.
