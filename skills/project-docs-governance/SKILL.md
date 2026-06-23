---
name: project-docs-governance
description: Create, migrate, audit, and repair project documentation governance systems for software repositories. Use when bootstrapping docs for a new project, reorganizing or deduplicating existing docs, defining AGENTS.md/docs/README.md/docs/contributing/documentation.md roles, creating ADR/roadmap/status/reference structures, fixing stale or conflicting docs entry points, or extracting a reusable documentation workflow. Do not use for ordinary feature work when a healthy docs workflow already exists.
---

# Project Docs Governance

## Purpose

Build and maintain the documentation system itself. Use this skill when the
project needs a docs contract, not when a normal code task merely needs to read
existing docs.

Keep project facts in repository files. The skill provides workflow, templates,
and audit rules; it must not become the hidden source of truth for a project.

## Workflow Decision

1. Classify the repository:
   - New or undocumented.
   - Partially documented.
   - Mature but stale or conflicting.
   - Healthy docs system with one targeted governance change.
2. Inventory current docs with `scripts/inventory_docs.py <repo-root>`.
3. Pick the smallest relevant workflow:
   - New project bootstrap: read `references/bootstrap-new-project.md`.
   - Existing project migration: read `references/migrate-existing-project.md`.
   - Drift or conflict audit: read `references/audit-docs-drift.md`.
   - Rule-index design: read `references/rule-index-and-reference-docs.md`.
   - ADR, roadmap, or status work: read `references/adr-roadmap-status.md`.
4. Preserve existing useful project facts.
5. Create or update repository docs.
6. State what changed and why.

## Target Model

Read `references/governance-model.md` for the complete model. In short:

- Runtime skill discovery finds skills.
- `repo-docs-router` finds the right docs for normal work.
- Repository docs store project-specific facts and rules.
- `AGENTS.md` may hold project rules, but should not be required as the skill
  or docs discovery mechanism.
- `docs/README.md` maps the documentation set.
- `docs/contributing/documentation.md` records project-local docs workflow and
  special paths.
- `docs/reference/` stores repeatable implementation rules.
- `docs/adr/` stores durable decisions.
- `docs/planning/roadmap.md` stores direction.
- `docs/planning/implementation-status.md` stores current implementation truth
  against documented expectations.

## Assets

Use `assets/docs-skeleton/` as a starting point for new or heavily undocumented
projects. Copy only the files that are useful. Do not overwrite existing docs
without inspecting them first.

## Writing Rules

Read `references/writing-style.md` before writing new docs. Keep docs direct,
small, explicit, and tied to the current repository.
