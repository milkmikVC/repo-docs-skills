# Project Overrides

Use this reference when repository docs define local paths or rules that differ
from the standard docs contract.

## What Counts as an Override

Treat these as project-local overrides:

- A docs map in `docs/README.md`.
- A documentation workflow in `docs/contributing/documentation.md`.
- Rule IDs in `docs/reference/*.md`.
- Tooling or framework rules in `AGENTS.md`.
- ADR conventions or numbering rules.
- Project-specific architecture entry points.
- References to generated docs, OpenAPI docs, schema docs, or design docs.

## How to Apply Overrides

1. Verify the referenced path exists.
2. Prefer local docs over generic routing.
3. Read only the override relevant to the task.
4. Do not copy the override into the skill or treat it as universal.

## Conflict Handling

When docs disagree:

- Prefer the most specific current file for the task.
- Prefer implementation-status docs for shipped-vs-planned questions.
- Prefer ADRs for durable decision history.
- Prefer current source/runtime evidence when the user asks what actually works.
- Report the conflict briefly if it affects the answer or change.
