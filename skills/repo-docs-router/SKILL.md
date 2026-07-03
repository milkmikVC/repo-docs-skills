---
name: repo-docs-router
description: Route coding agents to the minimum relevant repository documentation using a standard docs contract, and decide whether durable conversation facts or completed work require docs updates. Use when Codex needs project documentation context for a software task, including product behavior, architecture, APIs, data models, frontend conventions, environment variables, ADRs, roadmap or implementation-status checks, cross-cutting conventions, document status, or repository docs entry point discovery. Read-only for docs-system structure; do not use for creating, migrating, or reorganizing a documentation system.
---

# Repo Docs Router

## Purpose

Find the smallest useful set of project documentation for the current task.
Treat repository files as the source of truth after they are found. Also decide
whether new durable facts, decisions, or completed work should be written back
to project docs.

This skill routes ordinary documentation reads and update decisions. It is not
a docs-system governance tool. Do not create, move, or reorganize the
documentation system with this skill. When docs are missing, conflicting, or
structurally unhealthy, report the issue and suggest using
`project-docs-governance`.

## Quick Workflow

1. Inventory docs entry points with `scripts/inventory_docs.py <repo-root>` or
   direct filesystem checks.
2. Read standard entry points that exist, especially `AGENTS.md`,
   `docs/README.md`, and `docs/contributing/documentation.md`.
3. Classify the task type.
4. Read only the docs needed for that task.
5. Follow project-local overrides when they exist.
6. Interpret document status before trusting a doc as current.
7. During discussion, identify durable project facts or decisions that should
   become docs.
8. Before finishing meaningful work, run the documentation lifecycle check.
9. If expected docs are missing or inconsistent, use the fallback guidance and
   mention the gap.

## Standard Docs Contract

Look for these paths first:

- `AGENTS.md`
- `docs/README.md`
- `docs/contributing/documentation.md`
- `docs/contributing/cross-cutting-concerns.md`
- `docs/product/vision.md`
- `docs/architecture/`
- `docs/reference/`
- `docs/adr/`
- `docs/planning/roadmap.md`
- `docs/planning/implementation-status.md`

Read `references/docs-contract.md` for the role of each path.

## Task Routing

Use `references/task-routing.md` to map a task to docs. Common examples:

- Product or UX behavior: product vision, relevant architecture docs, status.
- Architecture or boundaries: architecture docs, ADRs, roadmap/status.
- API, DTOs, errors, validation: API conventions, error handling, contracts.
- Frontend UI: web conventions, product docs, relevant architecture docs.
- Environment variables: environment docs and `.env.example`.
- Roadmap or status questions: roadmap and implementation-status docs.
- Cross-cutting concerns: contributing guidance, reference rules, ADRs.
- Documentation update decisions: documentation lifecycle and status guidance.

Read `references/documentation-lifecycle.md` before finalizing a meaningful
feature, architecture decision, API change, roadmap/status change, or durable
conversation fact.

Read `references/document-status.md` when docs have status markers or when a
doc may be stale, experimental, superseded, archived, planned, shipped, or
dropped.

## Project Overrides

If project docs define special paths, rule IDs, or mandatory reading order,
follow them. Read `references/project-overrides.md` for how to identify local
overrides without turning this skill into a project-specific rule source.

## Missing Docs

If the standard docs contract is absent or inconsistent, do not invent project
facts. Read `references/missing-docs-fallback.md`, search conservatively, and
tell the user which docs were missing.

## Output Expectations

When the user asks what to read, return a short ordered list of paths and why
each path matters. When working on a code change or architecture discussion,
read the relevant paths, confirm durable decisions when needed, and update or
recommend updates to the appropriate docs. Mention documentation gaps only
when they affect the task.
