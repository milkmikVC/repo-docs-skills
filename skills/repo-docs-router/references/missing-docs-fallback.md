# Missing Docs Fallback

Use this reference when expected docs are absent, incomplete, or inconsistent.

## Fallback Search

If standard docs are missing, search conservatively:

```bash
rg --files | rg '(^|/)(README|AGENTS|CONTRIBUTING|docs|adr|roadmap|architecture|reference)'
rg -n "ADR|roadmap|architecture|convention|documentation|environment|API|OpenAPI|Swagger|error handling|cross-cutting" .
```

Prefer `rg --files` over broad recursive shell output.

## What to Report

When missing docs affect the task, say:

- Which expected docs were missing.
- Which fallback files were used.
- Whether the answer depends on source inspection instead of docs.
- Whether `project-docs-governance` should be used to repair the docs system.

## What Not to Do

- Do not invent project rules.
- Do not silently treat generic conventions as project-specific facts.
- Do not create or reorganize docs with this skill.
- Do not read the entire repository when a targeted search is enough.
