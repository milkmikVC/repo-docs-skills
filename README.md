# Repo Docs Skills

Two Codex skills for routing agents through repository documentation and for
building healthy documentation governance systems.

## What This Repository Contains

- `repo-docs-router`: a lightweight skill that finds the smallest relevant docs
  set for ordinary coding work and routes documentation update decisions.
- `project-docs-governance`: a heavier governance skill for creating,
  migrating, auditing, and repairing a project's docs system.

The design keeps responsibilities separate:

- The coding agent runtime discovers skills.
- `repo-docs-router` finds project docs and decides whether durable facts or
  completed work should update docs.
- Repository docs store project-specific facts and rules.
- `project-docs-governance` repairs or creates the docs system itself.

## Why This Exists

Many repositories slowly turn `README.md`, `AGENTS.md`, roadmap docs, ADRs, and
architecture notes into overlapping rule piles. These skills provide a small
contract:

- standard docs paths are easy for agents to discover,
- project-specific facts stay in the repo,
- reusable routing logic lives in a skill,
- durable conversation facts and completed feature work have a docs lifecycle,
- stale, experimental, superseded, and dropped docs can be marked explicitly,
- docs governance work has a separate workflow from normal feature work.

## Repository Layout

```text
skills/
  repo-docs-router/
    SKILL.md
    references/
    scripts/
  project-docs-governance/
    SKILL.md
    references/
    scripts/
    assets/docs-skeleton/
```

## Install

Copy the skill folders into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/repo-docs-router "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/project-docs-governance "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart or refresh your Codex runtime if it does not discover newly copied
skills automatically.

## Usage

Use `repo-docs-router` for ordinary work that needs repository documentation
context or a docs update decision:

```text
Use $repo-docs-router to find the project docs I should read before changing this API.
```

```text
Use $repo-docs-router to decide whether this architecture decision should update docs.
```

Use `project-docs-governance` when the documentation system itself is the task:

```text
Use $project-docs-governance to audit this repository's docs entry points and propose a migration.
```

## Standard Docs Contract

The skills expect, but do not require, this documentation shape:

```text
AGENTS.md
docs/README.md
docs/contributing/documentation.md
docs/contributing/cross-cutting-concerns.md
docs/product/vision.md
docs/architecture/
docs/reference/
docs/adr/
docs/planning/roadmap.md
docs/planning/implementation-status.md
```

If a project uses different paths, repository docs remain the source of truth.
The router reads project-local overrides after discovering them.

## Validation

Validate each skill with the standard skill validator:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/repo-docs-router
python3 /path/to/skill-creator/scripts/quick_validate.py skills/project-docs-governance
```

The included inventory scripts are read-only:

```bash
python3 skills/repo-docs-router/scripts/inventory_docs.py /path/to/repo
python3 skills/project-docs-governance/scripts/inventory_docs.py /path/to/repo
```
