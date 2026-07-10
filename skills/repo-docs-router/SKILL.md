---
name: repo-docs-router
description: Use when Codex is handling every conversation in a software repository, before it answers or takes action. This includes short, read-only, or apparently docs-unrelated requests as well as coding, debugging, review, planning, product, architecture, operations, and documentation work.
---

# Repo Docs Router

## Required Preflight

Before answering or running commands for any repository request:

1. Find the repository root and run `scripts/inventory_docs.py <repo-root>` or
   equivalent read-only checks.
2. Read `docs/contributing/documentation.md` when present for local structure,
   update rules, and special paths.
3. Use `docs/README.md` as the map, classify the request, and load only relevant
   task docs.
4. Check document status before trusting a file as current.

Do not skip this preflight because a request is short, obvious, read-only, or
apparently unrelated to docs. It is valid to load no task-specific docs after
checking the local workflow and map.

Treat `AGENTS.md` as a project rule source, not the docs or skill discovery
mechanism. Repository files remain authoritative.

## During and After Work

Identify durable confirmed facts or decisions during discussion. Before
finishing meaningful work, decide whether docs need updates. Use
`project-docs-governance` only to create, migrate, or reorganize the docs
system.

## References

- Routing: `references/docs-contract.md`, `references/project-overrides.md`,
  and `references/task-routing.md`.
- Lifecycle: `references/documentation-lifecycle.md` and
  `references/document-status.md`.
- Missing docs: `references/missing-docs-fallback.md`.
